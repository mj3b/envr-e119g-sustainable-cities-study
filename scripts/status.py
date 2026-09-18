#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for p in sorted((root/'modules').rglob('fidelity-gates.json')):
    d=json.loads(p.read_text());print(f"Class {d['class_number']}: "+', '.join(f"{g['name']}={g['status']}" for g in d['gates']))
r=json.loads((root/'assignments/assignment-01/requirements.json').read_text())
print('Assignment 1 drafting:', 'authorized' if r['drafting_authorized'] else 'paused')
print('Geography locked:',json.loads((root/'cases/candidate-family.json').read_text())['geography_locked'])
objects=json.loads((root/'cases/research-objects.json').read_text())
discovery=json.loads((root/'cases/discovery.json').read_text())
print(f'Research objects: {len(objects)} across {len(set(o["type"] for o in objects))} types')
print(f'Candidates assessed: {len(discovery["candidates"])}; selection-ready: {sum(c["selection_ready"] for c in discovery["candidates"])}')
print('External source discovery is provisional; source access does not establish an outcome.')
