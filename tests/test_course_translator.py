"""Bookkeeping and boundary checks; no source-fidelity or scientific verdict."""
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'research/course-readings'
spec = importlib.util.spec_from_file_location('course_translator', ROOT / 'scripts/run_course_translator.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

class CourseTranslatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = json.loads((DATA / 'source-cards.json').read_text())
        cls.cards = cls.corpus['cards']
        cls.receipt = json.loads((DATA / 'translator-execution.json').read_text())
        cls.checks = json.loads((DATA / 'completion-checks.json').read_text())

    def test_source_identity_and_counts(self):
        self.assertEqual(len(self.cards), 11)
        self.assertEqual(len({c['sha256'] for c in self.cards}), 11)
        self.assertEqual(sum(c['physical_pages'] for c in self.cards), 233)

    def test_module_populations_remain_separate(self):
        self.assertEqual(sum(c['source_id'].startswith('M1-') for c in self.cards), 6)
        self.assertEqual(sum(c['source_id'].startswith('M2-') for c in self.cards), 5)
        self.assertFalse(any(c['source_id'] == 'M2-MCCONNELL' for c in self.cards))

    def test_catalog_keeps_all_38_readings(self):
        cat = json.loads((DATA / 'syllabus-catalog.json').read_text())
        self.assertEqual(cat['reading_count'], 38)
        self.assertEqual(len(cat['entries']), 38)
        self.assertEqual(len({c['reading_id'] for c in cat['entries']}), 38)
        self.assertEqual(sum(c['module'] == 'III' for c in cat['entries']), 6)

    def test_no_human_acceptance(self):
        for card in self.cards:
            self.assertEqual(card['human_review']['status'], 'pending')
            self.assertIsNone(card['human_review']['reviewer'])
            self.assertEqual(card['claim']['status'], 'qualified')

    def test_candidate_generation_is_bounded(self):
        for card in self.cards:
            pack = runner.artifacts(card, self.corpus['created_at_utc'])
            self.assertNotIn('human_gate.json', pack)
            self.assertNotIn('decision_summary.json', pack)
            self.assertEqual(pack['run_output.json']['result']['human_review']['status'], 'pending')
            self.assertFalse(pack['agent_spec.json']['provenance']['original_pdf_in_public_pack'])
            self.assertTrue(pack['agent_spec.json']['provenance']['ai_authored_input'])

    def test_each_claim_retains_qualifications(self):
        for card in self.cards:
            claim = card['claim']
            for field in ['text', 'locator', 'evidence_quote', 'contrary_or_qualifying_evidence',
                          'permitted_use', 'prohibited_inference', 'missing_dependency']:
                self.assertTrue(claim[field])
            self.assertLessEqual(len(claim['evidence_quote'].split()), 25)

    def test_original_validator_receipt(self):
        r = self.receipt
        self.assertEqual(r['validator_invocations'], 55)
        self.assertEqual((r['passed'], r['failed']), (55, 0))
        self.assertEqual(len(r['commands']), 55)
        self.assertEqual(len(r['artifact_sha256']), 88)
        self.assertTrue(all(c['exit_code'] == 0 for c in r['commands']))

    def test_receipt_binds_source_cards(self):
        current = hashlib.sha256((DATA / 'source-cards.json').read_bytes()).hexdigest()
        self.assertEqual(self.receipt['source_cards_sha256'], current)
        self.assertEqual(self.checks['schema_recheck']['source_cards_sha256'], current)
        self.assertEqual(self.checks['pdf_intake']['source_cards_sha256'], current)

    def test_original_bytes_recorded_in_receipt(self):
        sources = {c['source_id']: c['sha256'] for c in self.cards}
        self.assertEqual({c['source_id']: c['sha256'] for c in self.receipt['source_checks']}, sources)
        self.assertTrue(all(c['byte_check'] == 'pass' for c in self.receipt['source_checks']))
        self.assertEqual({c['source_id']: c['source_sha256'] for c in self.checks['source_checks']}, sources)

    def test_actual_pdf_intake_is_not_semantic_success(self):
        r = self.checks['pdf_intake']
        self.assertEqual((r['invocation_count'], r['command_success_count']), (11, 11))
        self.assertEqual((r['nonempty_extraction_count'], r['empty_extraction_count']), (10, 1))
        north = next(x for x in self.checks['source_checks'] if x['source_id'] == 'M1-NORTH')
        self.assertEqual(north['extracted_nonwhitespace_characters'], 0)
        self.assertEqual(north['extraction_status'], 'empty_visual_source_review_required')
        self.assertIsNone(self.checks['human_scholarly_approval'])
        self.assertFalse(self.checks['raw_pdfs_published'])

    def test_recheck_separate_from_recovered_run(self):
        self.assertTrue(self.checks['schema_recheck']['artifact_hashes_match_recovered_run'])
        self.assertEqual(self.checks['schema_recheck']['passed'], 55)
        self.assertFalse(self.checks['recovery']['compressed_stream_complete'])
        self.assertEqual(self.checks['recovery']['complete_file_records_recovered'], 23)

    def test_unresolved_quantitative_issues_retained(self):
        q = json.loads((DATA / 'quantitative-register.json').read_text())
        self.assertEqual(len(q['records']), 18)
        self.assertEqual({i['issue_id'] for i in q['issues']}, {'I01', 'I02', 'I03', 'I04'})
        self.assertTrue(all(i['missing_dependency'] for i in q['issues']))

    def test_research_boundaries_unchanged(self):
        self.assertEqual(self.corpus['case_verdict'], 'B. GO — NARROWED COURT/INSTRUMENT QUESTION')
        a = json.loads((ROOT / 'audit/2026-10-14-course-source-review.json').read_text())
        for name, expected in a['preserved_files'].items():
            self.assertEqual(hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), expected, name)

if __name__ == '__main__':
    unittest.main()
