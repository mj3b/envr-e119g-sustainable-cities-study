#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for p in sorted((root/'modules').rglob('fidelity-gates.json')):
    d=json.loads(p.read_text());print(f"Class {d['class_number']}: "+', '.join(f"{g['name']}={g['status']}" for g in d['gates']))
r=json.loads((root/'assignments/assignment-01/requirements.json').read_text())
print('Assignment 1 drafting:', 'authorized' if r['drafting_authorized'] else 'paused')
print('Geography locked:',json.loads((root/'cases/candidate-family.json').read_text())['geography_locked'])
