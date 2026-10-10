import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("progress", ROOT / "scripts/research_progress.py")
progress = importlib.util.module_from_spec(spec)
spec.loader.exec_module(progress)


class ResearchProgressTests(unittest.TestCase):
    def setUp(self):
        self.ledger = json.loads((ROOT / progress.LEDGER).read_text())
        self.draft = json.loads((ROOT / progress.DRAFT).read_text())

    def test_snapshot_matches_current_inputs(self):
        self.assertEqual(progress.snapshot(), json.loads((ROOT / progress.OUTPUT).read_text()))

    def test_status_totals_match_separate_populations(self):
        out = progress.snapshot()
        for name in ("historical_ledger", "draft_register"):
            self.assertEqual(out[name]["entries"], sum(out[name]["status_counts"].values()))
        self.assertIn("overlap", out["overlap_warning"])

    def test_duplicate_claim_is_rejected(self):
        self.ledger["claims"].append(copy.deepcopy(self.ledger["claims"][0]))
        self.ledger["claim_count"] += 1
        with self.assertRaisesRegex(ValueError, "unique IDs"):
            progress.summarize(self.ledger, self.draft, {})

    def test_incorrect_declared_count_is_rejected(self):
        self.ledger["claim_count"] += 1
        with self.assertRaisesRegex(ValueError, "claim_count"):
            progress.summarize(self.ledger, self.draft, {})

    def test_unknown_status_is_rejected(self):
        self.ledger["claims"][0]["status"] = "probably true"
        with self.assertRaisesRegex(ValueError, "Unknown historical"):
            progress.summarize(self.ledger, self.draft, {})

    def test_missing_review_is_not_inferred(self):
        del self.draft["new_claim_evidence"][0]["human_review"]
        with self.assertRaisesRegex(ValueError, "review"):
            progress.summarize(self.ledger, self.draft, {})

    def test_duplicate_dependency_is_rejected(self):
        self.draft["uninspected_originals"].append(self.draft["uninspected_originals"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate dependency"):
            progress.summarize(self.ledger, self.draft, {})

    def test_counts_do_not_create_research_results(self):
        out = progress.snapshot()
        self.assertIsNone(out["study_wide_review_coverage"])
        self.assertIsNone(out["environmental_effect_estimate"])
        self.assertIsNone(out["ai_productivity_estimate"])
        self.assertFalse(out["human_scholarly_approval_by_this_script"])

    def test_public_readme_routes_and_boundary(self):
        text = (ROOT / "README.md").read_text()
        for link in ("docs/START-HERE.md", "research/cerrillos/README.md",
                     "archive/README.md", "methods/MEASUREMENT.md", "AI-USE-LOG.md"):
            self.assertIn(link, text)
        self.assertIn("B. GO — NARROWED COURT/INSTRUMENT QUESTION", text)
        self.assertEqual(sum(line.startswith("# ") for line in text.splitlines()), 1)
