"""Check evidence bookkeeping and document boundaries; never confer human approval."""
import hashlib
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name): return json.loads((ROOT/name).read_text())
def sha(name): return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
class AssignmentIntegrationTests(unittest.TestCase):
    def test_all_module_one_profiles_are_substantive(self):
        paths=list((ROOT/'modules/01-theories-sustainable-development').rglob('analysis.json'))
        self.assertEqual(len(paths),6)
        for p in paths:
            a=json.loads(p.read_text())['substantive_analysis']
            self.assertGreaterEqual(len(a['argument_steps']),3)
            self.assertTrue(a['source_locator'])
            self.assertTrue(a['prohibited_inference'])
            self.assertEqual(a['human_review']['status'],'pending')
            self.assertIsNone(a['human_review']['reviewer'])
    def test_seventeen_supplied_pdfs_do_not_mean_38_readings(self):
        one=load('research/course-readings/source-cards.json')['cards']
        three=load('research/course-readings/module-iii/source-cards.json')['cards']
        self.assertEqual(len(one+three),17)
        self.assertEqual(len({c['sha256'] for c in one+three}),17)
        self.assertEqual(sum(c['physical_pages'] for c in three),304)
        self.assertEqual(load('research/course-readings/syllabus-catalog.json')['reading_count'],38)
    def test_prior_module_three_execution_is_preserved(self):
        a=load('audit/2026-10-14-assignment-integration.json')
        self.assertEqual(sha('research/course-readings/module-iii/translator/execution-receipt.json'),a['prior_execution_receipt_sha256'])
        self.assertFalse(a['new_translator_validator_execution'])
        self.assertEqual(a['module3_candidate_artifact_hashes_checked'],48)
    def test_lecture_public_records_exclude_exact_excerpts(self):
        x=load('research/lecture-2026-10-09/guidance.json')
        self.assertEqual(len(x['claims']),29)
        self.assertIsNone(x['human_review'])
        self.assertFalse(x['raw_transcript_or_exact_excerpts_published'])
        for c in x['claims']:
            self.assertNotIn('exact_excerpt_as_transcribed',c)
            self.assertTrue(c['locator']['speaker_turn_start'])
    def test_draft_hash_and_scope_are_bound(self):
        e=load('assignments/assignment-02/evidence-v02.json')
        self.assertEqual(e['draft_sha256'],sha('assignments/assignment-02/review-draft-v02.md'))
        self.assertIsNone(e['human_scholarly_approval'])
        self.assertFalse(e['submission_performed'])
        self.assertFalse(e['word_count']['formal_limit_confirmed'])
        self.assertEqual(len(e['material_claims']),12)
    def test_rehearsal_is_not_measured_delivery(self):
        x=load('assignments/assignment-03/preparation.json')
        self.assertEqual(sum(x['planned_sections_seconds']),300)
        self.assertIsNone(x['rehearsal_seconds'])
        self.assertIsNone(x['human_approval'])
        self.assertFalse(x['submission_format_confirmed'])
        self.assertEqual(x['script_sha256'],sha('assignments/assignment-03/rehearsal-script-v01.md'))
        self.assertEqual(x['assignment_2_basis_sha256'],sha('assignments/assignment-02/review-draft-v02.md'))
    def test_protected_evidence_is_unchanged(self):
        x=load('audit/2026-10-14-assignment-integration.json')
        for p,h in x['protected_sha256'].items(): self.assertEqual(sha(p),h,p)
        self.assertEqual(x['case_verdict'],'B. GO — NARROWED COURT/INSTRUMENT QUESTION')
    def test_recovery_does_not_invent_complete_transfer(self):
        x=load('audit/2026-10-14-assignment-integration.json')['recovery']
        self.assertEqual(x['available_compressed_parts'],3)
        self.assertEqual(x['unretrieved_parts'],12)
        self.assertEqual(x['complete_change_records_recovered'],8)
        self.assertFalse(x['full_original_payload_recovered'])
if __name__=='__main__': unittest.main()
