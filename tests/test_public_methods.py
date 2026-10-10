import importlib.util, json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def module(name,path):
    s=importlib.util.spec_from_file_location(name,ROOT/path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
jev=module('jev_runner','experiments/jev/runner.py')
publication=module('pub_check','scripts/publication_check.py')
class PublicMethodsTests(unittest.TestCase):
    def setUp(self): self.rows=json.loads((ROOT/'experiments/jev/fixtures.json').read_text())
    def test_public_scope(self): self.assertEqual(publication.check(),[])
    def test_prepare_never_calls_provider(self): self.assertEqual(jev.execute(self.rows,'prepare','jev-latest')['calls'],0)
    def test_mock_not_measurement(self):
        result=jev.execute(self.rows,'mock','jev-latest'); self.assertEqual(result['calls'],0); self.assertFalse(result['human_scholarly_approval'])
    def test_missing_evidence_abstains(self): self.assertEqual(jev.execute(self.rows[-1:],'mock','jev-latest')['results'][0]['route'],'abstain_missing_evidence')
    def test_reference_label_blinded(self): self.assertNotIn('reference_label',str(jev.request_for(self.rows[0],'jev-latest')))
    def test_live_requires_explicit_gate(self):
        with self.assertRaises(ValueError): jev.execute(self.rows,'live','jev-latest')
    def test_live_rejects_unreviewed_labels(self):
        with self.assertRaises(ValueError): jev.execute(self.rows,'live','jev-latest',True,12)
    def test_malformed_response_rejected(self):
        with self.assertRaises(ValueError): jev.validate_answer({'answers':{}})
    def test_probabilities_checked(self):
        with self.assertRaises(ValueError): jev.validate_answer({'model':'fixture','answers':{'support':{'type':'choice','choice':'supported','confidence':1,'probabilities':{'supported':2,'contradicted':0,'insufficient':0}}}})
    def test_no_human_approval_fabricated(self):
        card=json.loads((ROOT/'methods/translator-card.json').read_text()); self.assertEqual(card['human_review']['status'],'pending'); self.assertFalse(card['operational_authorization'])
    def test_preserved_exports(self):
        import hashlib
        reg=json.loads((ROOT/'research/preservation-index.json').read_text())
        for r in reg['records']:
            if r['public_content_path']: self.assertEqual(hashlib.sha256((ROOT/r['public_content_path']).read_bytes()).hexdigest(),r['sha256'])
    def test_network_error_preserves_failed_attempt(self):
        from unittest.mock import patch
        rows=self.rows[:2]
        for row in rows:
            row['human_reference_review']={'reviewer':'SYNTHETIC TEST ONLY','reviewed_at':'fixture-only','record_sha256':jev.digest({k:v for k,v in row.items() if k!='human_reference_review'})}
        with patch.dict('os.environ',{'TYPESAFE_API_KEY':'synthetic-test-placeholder'}), patch.object(jev.urllib.request,'urlopen',side_effect=TimeoutError):
            result=jev.execute(rows,'live','test-fixture',True,2)
        self.assertFalse(result['complete']); self.assertEqual(result['calls'],1)
        self.assertEqual(result['results'][0]['route'],'provider_error_abstain')
    def test_draft_boundary(self):
        text=(ROOT/'assignments/assignment-02/review-draft-v01.md').read_text(); self.assertIn('REVIEW DRAFT',text); self.assertIn('human',text.lower())
if __name__=='__main__': unittest.main()
