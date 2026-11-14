import json
from pathlib import Path
import socket
import unittest
from unittest.mock import patch

from langsmith import utils as tracing_utils

from workflow import PENDING, run


HERE = Path(__file__).resolve().parent


def data():
    return {
        "version": "0.1",
        "as_of": "2026-11-13",
        "sources": [
            {
                "id": "S1",
                "title": "Synthetic source",
                "url": "https://example.org/record",
                "kind": "test_fixture",
                "date": "2026-09-09",
                "sha256": None,
            },
        ],
        "passages": [
            {
                "id": f"P{i}",
                "source_id": "S1",
                "locator": f"PDF p. {i}",
                "text": f"Synthetic paraphrase {i}",
                "representation": "paraphrase",
            }
            for i in range(1, 4)
        ],
        "claims": [{"id": "C1", "text": "Synthetic claim", "clauses": []}],
    }


def add_clause(case_set, *relations):
    clauses = case_set["claims"][0]["clauses"]
    clauses.append({
        "id": f"C1-{len(clauses) + 1}",
        "text": "Synthetic clause",
        "links": [
            {"passage_id": f"P{i}", "relation": relation, "rationale": "Fixture"}
            for i, relation in enumerate(relations, 1)
        ],
    })


def route(case_set):
    return run(json.dumps(case_set).encode())


class WorkflowTests(unittest.TestCase):
    def test_label_rules(self):
        for relations, expected in (
            (("supports",), "Supported"),
            (("contradicts",), "Contradicted"),
            (("context_only",), "Insufficient"),
            ((), "Insufficient"),
            (("supports", "contradicts"), "Insufficient"),
            (("supports", "context_only"), "Supported"),
        ):
            with self.subTest(relations=relations):
                case_set = data()
                add_clause(case_set, *relations)
                self.assertEqual(route(case_set)["claims"][0]["candidate_label"], expected)

    def test_compound_rules(self):
        for second, expected in (
            ("supports", "Supported"),
            ("context_only", "Insufficient"),
            ("contradicts", "Contradicted"),
        ):
            with self.subTest(second=second):
                case_set = data()
                add_clause(case_set, "supports")
                add_clause(case_set, second)
                self.assertEqual(route(case_set)["claims"][0]["candidate_label"], expected)

    def test_traceability_and_no_promotion(self):
        case_set = data()
        add_clause(case_set, "supports")
        packet = route(case_set)
        claim = packet["claims"][0]
        link = claim["clauses"][0]["evidence"][0]
        self.assertEqual(link["locator"], "PDF p. 1")
        self.assertEqual(link["source"]["id"], "S1")
        self.assertEqual(link["passage_text"], "Synthetic paraphrase 1")
        self.assertEqual(link["representation"], "paraphrase")
        self.assertEqual(claim["review_status"], PENDING)
        self.assertEqual(packet["review_status"], PENDING)
        self.assertIsNone(packet["runtime_model"])

    def test_unknown_fields_and_relations_are_rejected(self):
        case_set = data()
        add_clause(case_set, "supports")
        case_set["claims"][0]["verified"] = True
        with self.assertRaisesRegex(ValueError, "Unexpected fields"):
            route(case_set)
        del case_set["claims"][0]["verified"]
        case_set["claims"][0]["clauses"][0]["links"][0]["relation"] = "publish"
        with self.assertRaisesRegex(ValueError, "Invalid relation"):
            route(case_set)

    def test_duplicate_json_fields_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Repeated JSON key"):
            run(b'{"version":"0.1","version":"0.2"}')

    def test_unknown_source_and_passage_are_rejected(self):
        case_set = data()
        add_clause(case_set, "supports")
        case_set["passages"][0]["source_id"] = "S2"
        with self.assertRaisesRegex(ValueError, "Unknown source"):
            route(case_set)
        case_set["passages"][0]["source_id"] = "S1"
        case_set["claims"][0]["clauses"][0]["links"][0]["passage_id"] = "P99"
        with self.assertRaisesRegex(ValueError, "Unknown or duplicate passage"):
            route(case_set)

    def test_missing_locator_is_rejected(self):
        case_set = data()
        add_clause(case_set, "supports")
        case_set["passages"][0]["locator"] = " "
        with self.assertRaisesRegex(ValueError, "locator"):
            route(case_set)

    def test_later_source_is_rejected(self):
        case_set = data()
        add_clause(case_set, "supports")
        case_set["sources"][0]["date"] = "2026-11-14"
        with self.assertRaisesRegex(ValueError, "study cutoff"):
            route(case_set)

    def test_duplicate_passage_is_rejected(self):
        case_set = data()
        add_clause(case_set, "supports")
        case_set["passages"].append(case_set["passages"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate passage ID"):
            route(case_set)

    def test_runtime_stays_local_and_disables_tracing(self):
        case_set = data()
        add_clause(case_set, "supports")
        import workflow
        original = workflow.evaluate_claims

        def checked(state):
            self.assertFalse(tracing_utils.tracing_is_enabled())
            return original(state)

        with (
            patch.dict("os.environ", {"LANGSMITH_TRACING": "true", "LANGCHAIN_TRACING_V2": "true"}),
            patch.object(workflow, "evaluate_claims", checked),
            patch.object(socket.socket, "connect", side_effect=AssertionError("Network connection")),
            patch.object(socket.socket, "connect_ex", side_effect=AssertionError("Network connection")),
        ):
            self.assertFalse(route(case_set)["hosted_tracing"])

    def test_case_set_replays_with_all_claims_pending(self):
        case_bytes = (HERE / "cases.json").read_bytes()
        packet = run(case_bytes)
        self.assertEqual(packet, run(case_bytes))
        self.assertEqual(sum(packet["counts"].values()), len(packet["claims"]))
        self.assertEqual(
            {claim["id"]: claim["candidate_label"] for claim in packet["claims"]},
            {
                "T01": "Contradicted",
                "T02": "Insufficient",
                "T03": "Supported",
                "T04": "Insufficient",
            },
        )
        compound = next(row for row in packet["claims"] if row["id"] == "T04")
        self.assertEqual(
            [clause["candidate_label"] for clause in compound["clauses"]],
            ["Supported", "Insufficient"],
        )
        self.assertTrue(all(row["review_status"] == PENDING for row in packet["claims"]))


if __name__ == "__main__":
    unittest.main()
