"""Regression tests for the public notebook reading surface and output boundary."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('notebook_checks', ROOT / 'scripts/check_notebooks.py')
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class NotebookTests(unittest.TestCase):
    def setUp(self):
        self.path = ROOT / 'docs/START-HERE.ipynb'
        self.reader = json.loads(self.path.read_text())
        self.worked_path = ROOT / 'methods/evidence-review/trace-a-claim.ipynb'
        self.worked = json.loads(self.worked_path.read_text())

    def errors(self, data=None, reader=True):
        return checks.validate_notebook(data if data is not None else self.reader,
                                       self.path if reader else self.worked_path,
                                       ROOT, reader)

    def test_all_three_public_notebooks_have_valid_reading_surfaces(self):
        self.assertEqual(checks.check(), [])

    def test_executable_cells_are_rejected_in_reading_guides(self):
        self.reader['cells'].append({'id': 'accidental-code', 'cell_type': 'code', 'metadata': {}, 'source': ['print(1)'], 'execution_count': None, 'outputs': []})
        self.assertTrue(any('cannot contain executable' in e for e in self.errors()))

    def test_broken_or_private_navigation_is_rejected(self):
        self.reader['cells'][0]['source'].append('\n[Missing](a-missing-reader-page.md)\n[Private](../private/notes.md)\n[Escape](../../../outside.md)')
        errors = self.errors()
        self.assertTrue(any('Missing local link' in e for e in errors))
        self.assertTrue(any('Restricted local link' in e for e in errors))
        self.assertTrue(any('escapes repository' in e for e in errors))

    def test_host_paths_and_credentials_are_detected_in_outputs(self):
        cell = next(c for c in self.worked['cells'] if c['cell_type'] == 'code')
        cell['outputs'][0]['text'].append('/Users/example/private.txt\n' + 'ghp_' + 'x' * 40)
        errors = self.errors(self.worked, reader=False)
        self.assertTrue(any('Private host path' in e for e in errors))
        self.assertTrue(any('credential' in e for e in errors))

    def test_active_or_error_outputs_are_rejected(self):
        for output in [
            {'output_type': 'display_data', 'data': {'text/html': '<script>alert(1)</script>'}, 'metadata': {}},
            {'output_type': 'error', 'ename': 'RuntimeError', 'evalue': 'failed', 'traceback': []},
        ]:
            with self.subTest(output_type=output['output_type']):
                notebook = copy.deepcopy(self.worked)
                next(c for c in notebook['cells'] if c['cell_type'] == 'code')['outputs'] = [output]
                self.assertTrue(any('plain-text stream' in e for e in self.errors(notebook, reader=False)))

    def test_output_without_execution_count_is_rejected(self):
        next(c for c in self.worked['cells'] if c['cell_type'] == 'code')['execution_count'] = None
        self.assertTrue(any('no execution count' in e for e in self.errors(self.worked, reader=False)))

    def test_duplicate_cells_and_malformed_text_are_rejected(self):
        self.reader['cells'][1]['id'] = self.reader['cells'][0]['id']
        self.reader['cells'][2]['source'] = {'unexpected': 'text'}
        errors = self.errors()
        self.assertTrue(any('duplicate cell ID' in e for e in errors))
        self.assertTrue(any('invalid source' in e for e in errors))

    def test_duplicate_json_fields_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate JSON'):
            json.loads('{"cells": [], "cells": []}', object_pairs_hook=checks.unique_object)

    def test_html_and_embedded_attachments_are_rejected(self):
        self.reader['cells'][0]['source'].append('\n<iframe src="https://example.org"></iframe>')
        self.reader['cells'][1]['attachments'] = {'image.png': {'image/png': 'unused'}}
        errors = self.errors()
        self.assertTrue(any('active HTML' in e for e in errors))
        self.assertTrue(any('attachments' in e for e in errors))

    def test_malformed_reader_metadata_is_rejected(self):
        self.reader['metadata']['study_reader_guide'] = ['unexpected']
        self.assertTrue(any('execution is not required' in e for e in self.errors()))

    def test_worked_replay_timeout_returns_a_bounded_failure(self):
        with patch.object(checks.subprocess, 'run', side_effect=checks.subprocess.TimeoutExpired('python', 60)) as run:
            errors = checks.execute_worked(ROOT)
        self.assertEqual(run.call_args.kwargs['timeout'], 60)
        self.assertTrue(any('60 seconds' in e for e in errors))

    def test_compatibility_pages_point_to_real_notebooks(self):
        for name in ['START-HERE', 'FACULTY-GUIDE']:
            text = (ROOT / 'docs' / (name + '.md')).read_text()
            self.assertIn(name + '.ipynb', text)
            self.assertLess(len(text.split()), 90)


if __name__ == '__main__':
    unittest.main()
