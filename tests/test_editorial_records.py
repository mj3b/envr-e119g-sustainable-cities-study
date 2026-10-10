import hashlib
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("markdown_audit", ROOT / "scripts/markdown_audit.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class EditorialRecordsTests(unittest.TestCase):
    def test_inventory_covers_nested_and_uppercase_markdown(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            subprocess.run(["git","init","-q",td],check=True)
            (root/"nested").mkdir()
            (root/"a.md").write_text("# Example\n")
            (root/"nested/b.MD").write_text("Jev is prepared; no live call.\n")
            (root/"skip.txt").write_text("Not Markdown")
            r=mod.scan(root)
            self.assertEqual(r["file_count"],2)
            self.assertEqual(r["flagged_file_count"],1)
            self.assertIn("not errors",r["classification"])

    def test_ignored_material_is_excluded(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);subprocess.run(["git","init","-q",td],check=True)
            (root/".gitignore").write_text("private/\n")
            (root/"private").mkdir();(root/"private/raw.md").write_text("private source")
            self.assertEqual(mod.scan(root)["file_count"],0)

    def test_unreadable_markdown_fails_explicitly(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);subprocess.run(["git","init","-q",td],check=True)
            (root/"bad.md").write_bytes(bytes([255]))
            with self.assertRaisesRegex(ValueError,"Unreadable UTF-8"):
                mod.scan(root)

    def test_baseline_audit_has_unique_dispositions(self):
        a=json.loads((ROOT/"audit/2026-10-10-markdown-inventory.json").read_text())
        self.assertEqual(len(a["files"]),a["baseline_markdown_count"])
        self.assertEqual(len({x["path"] for x in a["files"]}),len(a["files"]))
        self.assertTrue(all(x["disposition"] and len(x["sha256"])==64 for x in a["files"]))
        self.assertIsNone(a["human_approval"])
        self.assertFalse(a["research_revalidation_performed"])

    def test_protected_history_and_research_unchanged(self):
        a=json.loads((ROOT/"audit/2026-10-10-markdown-inventory.json").read_text())
        for path,digest in a["protected_sha256"].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
        log=(ROOT/"AI-USE-LOG.md").read_text()
        suffix=log[log.index(a["preserved_log_suffix"]["starts_with"]):]
        self.assertEqual(hashlib.sha256(suffix.encode()).hexdigest(),a["preserved_log_suffix"]["sha256"])
        activities=json.loads((ROOT/"methods/ai-activity.json").read_text())["activities"]
        original=[x for x in activities if x["id"] in {f"ACT{i:02}" for i in range(1,9)}]
        self.assertEqual(hashlib.sha256(json.dumps(original,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),a["preserved_activity_objects_sha256"])

    def test_standard_and_current_activity_boundaries(self):
        text=(ROOT/"standards/WRITING.md").read_text()
        self.assertEqual(text.splitlines()[0],"# Mark’s Writing Rules and Voice Register System")
        self.assertNotIn("E5",text)
        a=json.loads((ROOT/"methods/ai-activity.json").read_text())
        ids=[x["id"] for x in a["activities"]]
        self.assertEqual(len(ids),len(set(ids)))
        for x in a["activities"]:
            if x["id"] in ["ACT09","ACT10","ACT11","ACT12"]:
                self.assertEqual(x["human_review"]["status"],"pending")
                self.assertIsNone(x["human_review"]["reviewer"])
