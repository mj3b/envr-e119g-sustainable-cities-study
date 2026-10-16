"""Regression tests for author-selected text and administrative state."""
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('final_checker',ROOT/'scripts/check_final_assignment.py')
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
load=lambda p:json.loads((ROOT/p).read_text())
sha=lambda p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()

class FinalAssignmentTests(unittest.TestCase):
    def test_final_manuscript_binding(self):
        self.assertEqual(checker.check(ROOT), [])

    def test_counts_do_not_include_disclosure(self):
        text=(ROOT/'assignments/assignment-02/final-v011.md').read_text()
        self.assertEqual(checker.word_count(checker.body(text)),1129)
        self.assertNotIn('AI assistance.',checker.body(text))
        self.assertIn('Closing reflection.',checker.body(text))

    def test_protected_research_unchanged(self):
        audit=load('audit/2026-10-15-final-lock-v011.json')
        for p,h in audit['protected_sha256'].items():
            self.assertEqual(sha(p),h,p)

    def test_prior_ai_activity_objects_preserved(self):
        audit=load('audit/2026-10-15-final-lock-v011.json')
        acts=load('methods/ai-activity.json')['activities']
        old=acts[:audit['prior_ai_activity_count']]
        self.assertEqual(hashlib.sha256(json.dumps(old,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),audit['prior_ai_activity_sha256'])
        self.assertEqual([x['id'] for x in acts[-2:]],['ACT26','ACT27'])

    def test_release_state_does_not_claim_submission(self):
        lock=load('assignments/assignment-02/final-lock-v011.json')
        self.assertEqual(lock['release_tag'],'v0.3.3')
        self.assertEqual(lock['submission']['status'],'not_recorded')
        self.assertIsNone(lock['submission']['submitted_at'])
        self.assertIsNone(lock['submission']['receipt'])

    def test_approved_body_and_reference_history(self):
        a=(ROOT/'assignments/assignment-02/history/submission-candidate-v011.md').read_text()
        b=(ROOT/'assignments/assignment-02/final-v011.md').read_text()
        self.assertEqual(checker.body(a),checker.body(b))
        self.assertEqual(a.split('## References\n\n')[1],b.split('## References\n\n')[1])

if __name__=='__main__': unittest.main()
