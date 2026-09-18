import json,shutil,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate import ROOT,validate,schema_errors
from integrity import claim_digest

class ResearchTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        for name in ['cross-course','modules','cases','assignments','schemas']:
            shutil.copytree(ROOT/name,self.root/name)
    def tearDown(self):self.tmp.cleanup()
    def change(self,ident,**changes):
        p=self.root/'cases/research-objects.json';rows=json.loads(p.read_text())
        next(o for o in rows if o['id']==ident)['data'].update(changes)
        p.write_text(json.dumps(rows))
    def assert_error(self,needle):self.assertTrue(any(needle in e for e in validate(self.root)),validate(self.root))
    def test_complete_packet(self):self.assertEqual(validate(self.root),[])
    def test_schemas(self):self.assertEqual(schema_errors(self.root),[])
    def test_missing_temporal_access(self):
        self.change('EV-DAL-PUBLIC',available_to_actor_date=None);self.assert_error('timely access')
    def test_hindsight_leak(self):
        self.change('EV-DAL-PUBLIC',available_to_actor_date='2022-01-01');self.assert_error('timely access')
    def test_wrong_authority_type(self):
        self.change('DEC-DAL',authority_id='ACT-DAL-COUNCIL');self.assert_error('Invalid authority')
    def test_unknown_is_not_zero(self):
        self.change('MEAS-DAL-GAP',value=0);self.assert_error('Unknown measurement has value')
    def test_capacity_is_not_energy(self):
        self.change('MEAS-MEM-CAP',quantity_kind='energy');self.assert_error('MW mislabeled')
    def test_outcome_cannot_use_scenario(self):
        self.change('OUT-DAL-01',outcome_status='observed',measurement_ids=['MEAS-MEM-SCALE']);self.assert_error('lacks observations')
    def test_measurement_cycle(self):
        self.change('MEAS-MEM-CAP',input_ids=['MEAS-MEM-SCALE']);self.assert_error('dependency cycle')
    def test_alternative_ownership(self):
        self.change('ALT-DAL-DEFER',decision_id='DEC-MEM');self.assert_error('ownership mismatch')
    def test_unknown_cannot_pass_selection(self):
        p=self.root/'cases/discovery.json';d=json.loads(p.read_text());d['candidates'][1]['selection_ready']=True;p.write_text(json.dumps(d));self.assert_error('unresolved evidence')
    def test_schema_rejects_missing_disconfirmation(self):
        p=self.root/'cases/research-objects.json';d=json.loads(p.read_text());next(o for o in d if o['id']=='H-01')['data'].pop('disconfirming_evidence');p.write_text(json.dumps(d));self.assertTrue(schema_errors(self.root))
    def test_stale_review_rejected(self):
        p=self.root/'cross-course/claims.json';d=json.loads(p.read_text());d[0]['human_review']='approved';p.write_text(json.dumps(d))
        receipt=dict(target='claim:'+d[0]['id'],digest=claim_digest(self.root,d[0]['id']),decision='approved',reviewer='synthetic',rationale='Test fixture',reviewed_at='2026-01-01T00:00:00Z')
        (self.root/'cross-course/review-receipts.json').write_text(json.dumps([receipt]))
        d[0]['text']+=' Changed after review.';p.write_text(json.dumps(d));self.assert_error('stale claim review')
    def test_research_approval_needs_receipt(self):
        p=self.root/'cases/research-objects.json';d=json.loads(p.read_text());d[0]['human_review']='approved';p.write_text(json.dumps(d));self.assert_error('stale research review')

if __name__=='__main__':unittest.main()
