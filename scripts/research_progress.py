#!/usr/bin/env python3
"""Count named research records without adjudicating evidence or human review."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = "research/cerrillos/history/ENVR_E119g_Cerrillos_Source_Closure_Ledger.json"
DRAFT = "research/cerrillos/draft-source-checks.json"
OUTPUT = "research/progress.json"
STATES = {"closed", "blocked", "qualified", "discarded", "locator-only"}


def unique_rows(rows, key, label):
    if not isinstance(rows, list) or any(not isinstance(r, dict) for r in rows):
        raise ValueError(label + " must be a list of objects")
    ids = [r.get(key) for r in rows]
    if any(not isinstance(i, str) or not i.strip() for i in ids) or len(ids) != len(set(ids)):
        raise ValueError(label + " needs nonempty unique IDs")


def summarize(ledger, draft, hashes):
    rows = ledger.get("claims")
    unique_rows(rows, "claim_id", "Historical claims")
    if ledger.get("claim_count") != len(rows):
        raise ValueError("Historical claim_count differs from its entries")
    if any(r.get("status") not in STATES for r in rows):
        raise ValueError("Unknown historical status")
    current = draft.get("new_claim_evidence")
    unique_rows(current, "id", "Draft claims")
    if any(r.get("status") not in STATES for r in current):
        raise ValueError("Unknown draft status")
    if any(not isinstance(r.get("human_review"), str) or not r["human_review"] for r in current):
        raise ValueError("Missing explicit draft human-review state")
    deps = draft.get("uninspected_originals")
    if not isinstance(deps, list) or any(not isinstance(d, str) or not d.strip() for d in deps):
        raise ValueError("Dependencies must be explicit strings")
    if len(deps) != len(set(deps)):
        raise ValueError("Duplicate dependency")
    return {
        "schema_version": 1,
        "scope": "Deterministic census of two named files; no source adjudication",
        "input_sha256": hashes,
        "historical_ledger": {
            "population": LEDGER,
            "unit": "historical ledger entry",
            "entries": len(rows),
            "status_counts": dict(sorted(Counter(r["status"] for r in rows).items())),
            "interpretation": "Inherited mixed claim/access labels, not renewed source verification"
        },
        "draft_register": {
            "population": DRAFT + "#new_claim_evidence",
            "unit": "draft legal-claim entry",
            "entries": len(current),
            "status_counts": dict(sorted(Counter(r["status"] for r in current).items())),
            "human_review_state_counts": dict(sorted(Counter(r["human_review"] for r in current).items())),
            "uninspected_original_dependency_count": len(deps),
            "uninspected_original_dependencies": deps,
            "interpretation": "Recorded review states only; underlying passages are not reviewed by this counter"
        },
        "overlap_warning": "Populations overlap in substance; do not sum them as independent or deduplicated claims",
        "study_wide_review_coverage": None,
        "coverage_limitation": "No complete material-claim denominator and content-bound accepted human reviews established by this counter",
        "environmental_effect_estimate": None,
        "ai_productivity_estimate": None,
        "human_scholarly_approval_by_this_script": False
    }


def snapshot(root=ROOT):
    root = Path(root)
    raw = {name: (root / name).read_bytes() for name in (LEDGER, DRAFT)}
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in raw.items()}
    return summarize(json.loads(raw[LEDGER]), json.loads(raw[DRAFT]), hashes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare with the committed snapshot")
    args = parser.parse_args()
    try:
        result = snapshot()
        if args.check:
            stored = json.loads((ROOT / OUTPUT).read_text())
            if result != stored:
                print("Record snapshot is stale; inspect inputs before regenerating.")
                return 1
            print("Record counts and input hashes match; scholarly review is separate.")
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print("Cannot compute record snapshot: " + str(exc))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
