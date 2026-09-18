import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from assure import fingerprint, inventory, link_errors, receipt_errors


class AssuranceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        (self.root / 'README.md').write_text('[Missing](missing.md)\n')

    def tearDown(self):
        self.temp.cleanup()

    def receipt(self, files):
        return {'schema_version': 1, 'evaluated_at': '2026-01-01T00:00:00Z',
                'files': files, 'fingerprint': fingerprint(files),
                'automated_status': 'pass', 'human_fidelity': 'not_assessed_by_this_runner',
                'checks': [{'id': x, 'exit_code': 0} for x in [
                    'structural_and_schema', 'privacy_paths_and_history', 'unit_tests', 'local_markdown_links']]}

    def test_stale_receipt_after_prose_edit(self):
        old = inventory(self.root)
        result = self.receipt(old)
        self.assertEqual(receipt_errors(self.root, result, old), [])
        (self.root / 'README.md').write_text('Changed interpretation')
        self.assertTrue(any('stale' in x for x in receipt_errors(self.root, result, inventory(self.root))))

    def test_missing_and_failed_check_cannot_pass(self):
        files = inventory(self.root)
        result = self.receipt(files)
        result['checks'].pop()
        self.assertTrue(any('missing required' in x for x in receipt_errors(self.root, result, files)))
        result = self.receipt(files)
        result['checks'][0]['exit_code'] = 1
        self.assertTrue(any('did not pass' in x for x in receipt_errors(self.root, result, files)))

    def test_receipt_cannot_certify_human_fidelity(self):
        files = inventory(self.root)
        result = self.receipt(files)
        result['human_fidelity'] = 'approved'
        self.assertTrue(any('cannot certify' in x for x in receipt_errors(self.root, result, files)))

    def test_dead_and_escaping_links(self):
        (self.root / 'README.md').write_text('[Missing](missing.md) [Outside](../secret.md) [Web](https://example.org)')
        count, errors = link_errors(self.root, inventory(self.root))
        self.assertEqual(count, 2)
        self.assertEqual(len(errors), 2)

    def test_receipt_excluded_and_ignored_sources_excluded(self):
        (self.root / '.gitignore').write_text('private/\n')
        (self.root / 'private').mkdir()
        (self.root / 'private/source.txt').write_text('private content')
        (self.root / 'governance').mkdir()
        (self.root / 'governance/evaluation-results.json').write_text('{}')
        names = inventory(self.root)
        self.assertNotIn('private/source.txt', names)
        self.assertNotIn('governance/evaluation-results.json', names)
        self.assertIn('README.md', names)

    def test_only_exact_pending_receipt_link_is_exempt(self):
        (self.root / 'README.md').write_text('[Wrong](evaluation-results.json) [Right](governance/evaluation-results.json)')
        count, errors = link_errors(self.root, inventory(self.root), pending_receipt=True)
        self.assertEqual(count, 2)
        self.assertEqual(len(errors), 1)
        self.assertIn('missing local link: evaluation-results.json', errors[0])

    def test_untracked_raw_file_fails_privacy_before_staging(self):
        (self.root / 'leak.pdf').write_text('Synthetic test content')
        script = Path(__file__).resolve().parents[1] / 'scripts/privacy_check.py'
        run = subprocess.run([sys.executable, str(script)], cwd=self.root, capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn('leak.pdf', run.stdout)


if __name__ == '__main__':
    unittest.main()
