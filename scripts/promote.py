#!/usr/bin/env python3
"""Produce a master brief only from approved records; never approve gates."""
import argparse,json,sys
from validate import ROOT,validate,promotion_errors
p=argparse.ArgumentParser();p.add_argument('class_number',type=int,choices=[1,2]);a=p.parse_args()
errors=validate()+promotion_errors(ROOT,a.class_number)
if errors:print('\n'.join(errors));sys.exit(1)
pack_path=next(p for p in (ROOT/'modules').rglob('fidelity-gates.json') if json.loads(p.read_text())['class_number']==a.class_number)
claims=json.loads((ROOT/'cross-course/claims.json').read_text())
text=f'# Class {a.class_number:02d} master brief\n\nApproved claim compilation.\n\n'
for c in claims:
    if c['class_number']==a.class_number:text+=f"- [{c['evidence_class']}] {c['id']}: {c['text']} ({c['source_id']}, {c['locator']}).\n"
out=pack_path.parent/f'class-{a.class_number:02d}-master-brief.md'
if out.exists():raise SystemExit('Refusing to overwrite an existing master brief; review and version it explicitly.')
out.write_text(text)
pack=json.loads(pack_path.read_text());pack['master_brief_status']='approved';pack_path.write_text(json.dumps(pack,indent=2)+'\n')
print(out)
