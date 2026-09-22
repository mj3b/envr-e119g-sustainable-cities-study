"""Test added class-number support without creating human-review approval."""
import copy
import json
import unittest
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]


class ClassThreeSchemaTests(unittest.TestCase):
    def setUp(self):
        self.sources = json.loads((ROOT / 'cross-course/evidence-registry.json').read_text())
        self.claims = json.loads((ROOT / 'cross-course/claims.json').read_text())
        self.source_schema = json.loads((ROOT / 'schemas/source_record.schema.json').read_text())
        self.claim_schema = json.loads((ROOT / 'schemas/claims.schema.json').read_text())

    def test_class_three_source_and_claim_are_accepted(self):
        source = next(s for s in self.sources if s['id'] == 'LOW22')
        claim = next(c for c in self.claims if c['id'] == 'LOW-01')
        self.assertEqual(source['class_number'], 3)
        self.assertEqual(claim['class_number'], 3)
        jsonschema.validate([source], self.source_schema)
        jsonschema.validate([claim], self.claim_schema)

    def test_unsupported_class_number_still_rejected(self):
        source = copy.deepcopy(next(s for s in self.sources if s['id'] == 'LOW22'))
        source['class_number'] = 99
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate([source], self.source_schema)

    def test_new_export_does_not_replace_existing_source(self):
        old = next(s for s in self.sources if s['id'] == 'L2')
        new = next(s for s in self.sources if s['id'] == 'L2-R20260922')
        self.assertNotEqual(old['private_path'], new['private_path'])
        self.assertNotEqual(old['sha256'], new['sha256'])

    def test_source_class_still_requires_known_evidence_category(self):
        claim = copy.deepcopy(next(c for c in self.claims if c['id'] == 'LOW-01'))
        claim['evidence_class'] = 'independently_validated_by_ai'
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate([claim], self.claim_schema)


if __name__ == '__main__':
    unittest.main()
