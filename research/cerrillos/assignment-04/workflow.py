"""Route a versioned Zone 1 case set into a provisional local review packet."""

import argparse
from collections import Counter
from datetime import date
from hashlib import sha256
from importlib.metadata import version
import json
from pathlib import Path
import platform
import re
import sys
from typing import TypedDict
from urllib.parse import urlsplit

from langchain_core.documents import Document
from langgraph.graph import END, START, StateGraph
from langsmith import tracing_context


PENDING = "pending_human_review"
RELATIONS = {"supports", "contradicts", "context_only"}
LABELS = ("Supported", "Contradicted", "Insufficient")
HERE = Path(__file__).resolve().parent


class ReviewState(TypedDict, total=False):
    case_set: dict
    documents: dict[str, Document]
    results: list[dict]


def unique_object(pairs):
    data = {}
    for key, value in pairs:
        if key in data:
            raise ValueError(f"Repeated JSON key: {key}")
        data[key] = value
    return data


def fields(record, expected, label):
    if not isinstance(record, dict) or record.keys() != set(expected.split()):
        raise ValueError(f"Unexpected fields in {label}; expected {expected}")


def nonblank(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Expected text for {label}")


def dated(value, label):
    nonblank(value, label)
    if date.fromisoformat(value).isoformat() != value:
        raise ValueError(f"Expected YYYY-MM-DD for {label}")


def items(records, label, allow_empty=False):
    if not isinstance(records, list) or (not records and not allow_empty):
        raise ValueError(f"Expected a list for {label}")
    return records


def indexed(records, expected, label):
    index = {}
    for row in items(records, label):
        fields(row, expected, label)
        identifier = row["id"]
        nonblank(identifier, f"{label} ID")
        if identifier in index:
            raise ValueError(f"Duplicate {label} ID: {identifier}")
        index[identifier] = row
    return index


def validate(state: ReviewState) -> dict:
    data = state["case_set"]
    fields(data, "version as_of sources passages claims", "case set")
    if data["version"] != "0.1":
        raise ValueError("Unsupported case set version")
    dated(data["as_of"], "as_of")
    sources = indexed(data["sources"], "id title url kind date sha256", "source")
    for source in sources.values():
        for key in ("title", "kind", "url"):
            nonblank(source[key], f"{source['id']} {key}")
        url = urlsplit(source["url"])
        if url.scheme != "https" or not url.hostname or url.username or url.password:
            raise ValueError(f"Expected a public HTTPS source URL: {source['id']}")
        dated(source["date"], source["id"])
        if source["date"] > data["as_of"]:
            raise ValueError(f"Source date exceeds the study cutoff: {source['id']}")
        digest = source["sha256"]
        if digest is not None and (
            not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)
        ):
            raise ValueError(f"Invalid source digest: {source['id']}")
    passages = indexed(
        data["passages"], "id source_id locator text representation", "passage"
    )
    for passage in passages.values():
        for key in ("source_id", "locator", "text"):
            nonblank(passage[key], f"{passage['id']} {key}")
        if passage["source_id"] not in sources:
            raise ValueError(f"Unknown source for {passage['id']}")
        if passage["representation"] not in ("paraphrase", "quotation"):
            raise ValueError(f"Invalid passage representation: {passage['id']}")
    claims = indexed(data["claims"], "id text clauses", "claim")
    clause_ids = set()
    for claim in claims.values():
        nonblank(claim["text"], claim["id"])
        for clause in indexed(claim["clauses"], "id text links", "clause").values():
            nonblank(clause["text"], clause["id"])
            if clause["id"] in clause_ids:
                raise ValueError(f"Duplicate clause ID: {clause['id']}")
            clause_ids.add(clause["id"])
            linked = set()
            for link in items(clause["links"], "links", allow_empty=True):
                fields(link, "passage_id relation rationale", "evidence link")
                passage_id = link["passage_id"]
                nonblank(passage_id, "passage ID")
                nonblank(link["rationale"], "relation rationale")
                if passage_id not in passages or passage_id in linked:
                    raise ValueError(f"Unknown or duplicate passage link: {passage_id}")
                if not isinstance(link["relation"], str) or link["relation"] not in RELATIONS:
                    raise ValueError(f"Invalid relation: {link['relation']}")
                linked.add(passage_id)
    return {}


def prepare_documents(state: ReviewState) -> dict:
    case_set = state["case_set"]
    sources = {row["id"]: row for row in case_set["sources"]}
    documents = {}
    for row in case_set["passages"]:
        source = sources[row["source_id"]]
        documents[row["id"]] = Document(
            id=row["id"],
            page_content=row["text"],
            metadata={
                "source": source,
                "locator": row["locator"],
                "representation": row["representation"],
            },
        )
    return {"documents": documents}


def evaluate_clause(clause, documents):
    relations = {link["relation"] for link in clause["links"]}
    direct = relations & {"supports", "contradicts"}
    if direct == {"supports"}:
        label, rule = "Supported", "direct_support"
    elif direct == {"contradicts"}:
        label, rule = "Contradicted", "direct_contradiction"
    elif direct:
        label, rule = "Insufficient", "unresolved_conflict"
    else:
        label, rule = "Insufficient", "no_direct_evidence"
    evidence = []
    for link in clause["links"]:
        document = documents[link["passage_id"]]
        evidence.append({
            **link,
            **document.metadata,
            "passage_text": document.page_content,
        })
    return {
        "id": clause["id"],
        "text": clause["text"],
        "candidate_label": label,
        "rule": rule,
        "evidence": evidence,
    }


def evaluate_claims(state: ReviewState) -> dict:
    results = []
    for claim in state["case_set"]["claims"]:
        clauses = [
            evaluate_clause(clause, state["documents"]) for clause in claim["clauses"]
        ]
        labels = {clause["candidate_label"] for clause in clauses}
        if "Contradicted" in labels:
            label, rule = "Contradicted", "a_clause_is_contradicted"
        elif labels == {"Supported"}:
            label, rule = "Supported", "all_clauses_supported"
        else:
            label, rule = "Insufficient", "a_clause_remains_unresolved"
        results.append({
            "id": claim["id"],
            "text": claim["text"],
            "candidate_label": label,
            "rule": rule,
            "review_status": PENDING,
            "clauses": clauses,
        })
    return {"results": results}


def run(case_bytes: bytes) -> dict:
    case_set = json.loads(case_bytes, object_pairs_hook=unique_object)
    with tracing_context(enabled=False):
        builder = StateGraph(ReviewState)
        builder.add_node("validate", validate)
        builder.add_node("prepare_documents", prepare_documents)
        builder.add_node("evaluate_claims", evaluate_claims)
        builder.add_edge(START, "validate")
        builder.add_edge("validate", "prepare_documents")
        builder.add_edge("prepare_documents", "evaluate_claims")
        builder.add_edge("evaluate_claims", END)
        results = builder.compile().invoke({"case_set": case_set})["results"]
    counts = Counter(row["candidate_label"] for row in results)
    return {
        "workflow_version": "0.1",
        "case_version": case_set["version"],
        "as_of": case_set["as_of"],
        "input_sha256": sha256(case_bytes).hexdigest(),
        "workflow_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "spec_sha256": sha256((HERE / "SPEC.md").read_bytes()).hexdigest(),
        "dependencies": {
            "python": platform.python_version(),
            **{
                name: version(name)
                for name in ("langgraph", "langchain-core", "langsmith")
            },
        },
        "runtime_model": None,
        "hosted_tracing": False,
        "annotation_origin": "AI-assisted analyst annotations",
        "review_status": PENDING,
        "counts": {label: counts[label] for label in LABELS},
        "claims": results,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=HERE / "cases.json")
    args = parser.parse_args()
    try:
        packet = run(args.cases.read_bytes())
    except (OSError, ValueError) as error:
        parser.exit(2, f"Cannot produce review packet: {error}\n")
    json.dump(packet, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
