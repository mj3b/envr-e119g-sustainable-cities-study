import copy,json,shutil,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate import ROOT,validate,promotion_errors
class IntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        for name in ['cross-course','modules','cases','assignments']:
            shutil.copytree(ROOT/name,self.root/name)
    def tearDown(self):self.tmp.cleanup()
    def mutate_claim(self,index,**changes):
        p=self.root/'cross-course/claims.json';data=json.loads(p.read_text());data[index].update(changes);p.write_text(json.dumps(data))
    def test_valid_calibration(self):self.assertEqual(validate(self.root),[])
    def test_bad_source(self):
        self.mutate_claim(0,source_id='invented');self.assertTrue(any('Unknown source' in e for e in validate(self.root)))
    def test_peer_laundering(self):
        p=self.root/'cross-course/claims.json';data=json.loads(p.read_text());i=next(i for i,c in enumerate(data) if c['id']=='P2-05')
        self.mutate_claim(i,evidence_class='assigned_reading',speaker_role='author');self.assertTrue(any('laundering' in e for e in validate(self.root)))
    def test_cycle(self):
        self.mutate_claim(0,depends_on=['N-01']);self.assertTrue(any('cycle' in e for e in validate(self.root)))
    def test_missing_locator(self):
        self.mutate_claim(0,locator='');self.assertTrue(any('Missing locator' in e for e in validate(self.root)))
    def test_promotion_fails_closed(self):
        self.assertTrue(promotion_errors(self.root,1));self.assertTrue(promotion_errors(self.root,2))
    def test_pass_without_reviewer(self):
        p=next((self.root/'modules').rglob('fidelity-gates.json'));d=json.loads(p.read_text());d['gates'][0]['status']='pass';p.write_text(json.dumps(d));self.assertTrue(any('without review' in e for e in validate(self.root)))
    def test_unauthorized_draft(self):
        (self.root/'assignments/assignment-01/memo-draft.md').write_text('unauthorized');self.assertTrue(any('draft exists' in e for e in validate(self.root)))
    def test_wrong_archive_path(self):
        p=self.root/'cross-course/evidence-registry.json';d=json.loads(p.read_text());d[0]['private_path']='../escape.pdf';p.write_text(json.dumps(d));self.assertTrue(any('Unsafe archive' in e for e in validate(self.root)))
    def test_complete_review_allows_promotion(self):
        for p in (self.root/'modules').rglob('fidelity-gates.json'):
            d=json.loads(p.read_text())
            for g in d['gates']:g.update(status='pass',reviewer='test-reviewer',reason='Synthetic test approval only')
            p.write_text(json.dumps(d))
        p=self.root/'cross-course/claims.json';d=json.loads(p.read_text())
        for c in d:c.update(status='source_checked',human_review='approved')
        p.write_text(json.dumps(d))
        p=self.root/'cross-course/omissions.json';d=json.loads(p.read_text())
        for o in d:o['status']='resolved'
        p.write_text(json.dumps(d))
        self.assertEqual(promotion_errors(self.root,1),[])
        self.assertEqual(promotion_errors(self.root,2),[])
    def test_passed_gates_do_not_erase_omissions(self):
        for p in (self.root/'modules').rglob('fidelity-gates.json'):
            d=json.loads(p.read_text())
            for g in d['gates']:g.update(status='pass',reviewer='test-reviewer',reason='Synthetic test')
            p.write_text(json.dumps(d))
        self.assertIn('Blocking omissions remain open',promotion_errors(self.root,1))
if __name__=='__main__':unittest.main()
