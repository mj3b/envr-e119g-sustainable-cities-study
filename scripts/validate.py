#!/usr/bin/env python3
"""Structural checks are separate from scholarly or human approval."""
import argparse, hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
CLASSES = {'assigned_reading','instructor_lecture','ta_guidance','peer_discourse','external_context','our_synthesis'}
def load(root,path):
    return json.loads((root/path).read_text())
def unique(rows,label,errors):
    ids=[x['id'] for x in rows]
    if len(ids)!=len(set(ids)): errors.append(f'Duplicate {label} ID')
    return {x['id']:x for x in rows}
def validate(root=ROOT,local=False):
    errors=[]
    try:
        sources=unique(load(root,'cross-course/evidence-registry.json'),'source',errors)
        claims=unique(load(root,'cross-course/claims.json'),'claim',errors)
        concepts=unique(load(root,'cross-course/concept-registry.json'),'concept',errors)
        for source in sources.values():
            if source['evidence_class'] not in CLASSES: errors.append(f"Bad source class: {source['id']}")
            path=source.get('private_path')
            if path:
                full=(root/path).resolve()
                if not full.is_relative_to((root/'private').resolve()):errors.append(f"Unsafe archive path: {source['id']}")
                elif local:
                    if not full.is_file():errors.append(f"Missing local source: {source['id']}")
                    elif hashlib.sha256(full.read_bytes()).hexdigest()!=source['sha256']:errors.append(f"Source digest mismatch: {source['id']}")
        for c in claims.values():
            ident=c['id']; kind=c['evidence_class']; source=sources.get(c['source_id'])
            if kind not in CLASSES:errors.append(f'Bad claim class: {ident}')
            if not source:errors.append(f'Unknown source: {ident}')
            if not c.get('locator'):errors.append(f'Missing locator: {ident}')
            if c['status']=='source_checked' and ('pending' in c['locator'].lower() or (source and source['status']=='missing')):errors.append(f'Unchecked support promoted: {ident}')
            expected={'assigned_reading':'author','instructor_lecture':'instructor','ta_guidance':'ta','peer_discourse':'student','our_synthesis':'analyst','external_context':'source_author'}
            if kind in expected and c['speaker_role'] not in [expected[kind],'unknown']:errors.append(f'Role/class mismatch: {ident}')
            if source and source['evidence_class']!=kind:
                allowed=kind=='our_synthesis' or (source['source_kind']=='mixed_speaker_transcript' and kind in {'instructor_lecture','ta_guidance','peer_discourse'})
                if not allowed:errors.append(f'Evidence-class laundering: {ident}')
            if kind=='our_synthesis' and not c['depends_on']:errors.append(f'Synthesis lacks dependencies: {ident}')
            for dep in c['depends_on']:
                if dep not in claims:errors.append(f'Unknown dependency {dep}: {ident}')
            for concept in c['concept_ids']:
                if concept not in concepts:errors.append(f'Unknown concept {concept}: {ident}')
            if c['human_review']=='approved' and c['status']!='source_checked':errors.append(f'Unverified approved claim: {ident}')
        def visit(id,trail):
            if id in trail:errors.append(f'Dependency cycle: {id}');return
            for dep in claims[id]['depends_on']:
                if dep in claims:visit(dep,trail|{id})
        for id in claims:visit(id,set())
        for concept in concepts.values():
            for id in concept['claim_ids']:
                if id not in claims:errors.append(f'Unknown concept claim: {id}')
        for p in (root/'modules').rglob('alignment.json'):
            for row in json.loads(p.read_text()):
                for k in ['reading_claim_ids','lecture_claim_ids']:
                    for id in row[k]:
                        if id not in claims:errors.append(f'Unknown alignment claim: {id}')
                        elif k=='reading_claim_ids' and claims[id]['evidence_class']!='assigned_reading':errors.append(f'Non-reading in reading lane: {id}')
        for p in (root/'modules').rglob('fidelity-gates.json'):
            pack=json.loads(p.read_text()); gs=pack['gates']
            if {g['id'] for g in gs}!={'G1','G2','G3'} or len(gs)!=3:errors.append(f'Incomplete gates: {p}')
            for g in gs:
                if g['status']=='pass' and (not g.get('reviewer') or not g.get('reason')):errors.append(f'Gate passed without review: {g["id"]}')
                for path in g['evidence']:
                    if not (root/path).is_file():errors.append(f'Missing gate evidence: {path}')
            if pack['master_brief_status']=='approved':errors.extend(promotion_errors(root,pack['class_number']))
        for p in (root/'modules').rglob('*master-brief.md'):
            pack=json.loads((p.parent/'fidelity-gates.json').read_text())
            if pack['master_brief_status']!='approved':errors.append(f'Unapproved master brief: {p}')
        case=load(root,'cases/candidate-family.json')
        if case['geography_locked'] and not case['selected_case_id']:errors.append('Geography locked without selected case')
        req=load(root,'assignments/assignment-01/requirements.json')
        if not req['drafting_authorized']:
            if any((root/'assignments/assignment-01').glob('*draft*')):errors.append('Assignment draft exists while paused')
    except (KeyError,TypeError,ValueError,OSError) as e:errors.append(f'Malformed or missing required record: {e}')
    try:
        from integrity import checks
        errors.extend(checks(root))
    except (KeyError,TypeError,ValueError,OSError,RecursionError) as e:
        errors.append(f'Malformed cross-file record: {e}')
    try:
        from research_checks import checks as research_checks
        errors.extend(research_checks(root))
    except (KeyError,TypeError,ValueError,OSError,RecursionError) as e:
        errors.append(f'Malformed research record: {e}')
    return errors

def promotion_errors(root,class_number):
    errors=[]
    paths=list((root/'modules').rglob('fidelity-gates.json'))
    packs=[json.loads(p.read_text()) for p in paths]
    pack=next((p for p in packs if p['class_number']==class_number),None)
    if not pack:return ['Unknown class']
    if any(g['status']!='pass' or not g['reviewer'] or not g['reason'] for g in pack['gates']):errors.append('All three human fidelity gates must pass')
    claims=load(root,'cross-course/claims.json')
    relevant=[c for c in claims if c['class_number']==class_number]
    by_id={c['id']:c for c in claims}
    closure=set(c['id'] for c in relevant)
    pending=list(closure)
    while pending:
        current=by_id.get(pending.pop())
        if current:
            for dep in current['depends_on']:
                if dep not in closure:closure.add(dep);pending.append(dep)
    if any(id not in by_id or by_id[id]['human_review']!='approved' or by_id[id]['status']!='source_checked' for id in closure):errors.append('Included claims and dependencies require human approval and source checks')
    omissions=load(root,'cross-course/omissions.json')
    if any(o['status']=='open' and o['severity']=='blocking' and o['class_number'] in [None,class_number] for o in omissions):errors.append('Blocking omissions remain open')
    from integrity import checks
    errors.extend(checks(root))
    return errors

def schema_errors(root=ROOT):
    try:
        import jsonschema
    except ImportError:
        return ['Schema validation requires requirements-dev.txt (pip install -r requirements-dev.txt)']
    pairs=[('source_record','cross-course/evidence-registry.json'),('claims','cross-course/claims.json'),('concepts','cross-course/concept-registry.json')]
    pairs += [('research_objects','cases/research-objects.json'),('discovery','cases/discovery.json')]
    pairs += [('fidelity_gates',str(p.relative_to(root))) for p in (root/'modules').rglob('fidelity-gates.json')]
    pairs += [('lecture_alignment',str(p.relative_to(root))) for p in (root/'modules').rglob('alignment.json')]
    pairs += [('reading_analysis',str(p.relative_to(root))) for p in (root/'modules').rglob('analysis.json')]
    pairs += [('synthesis',str(p.relative_to(root))) for p in (root/'modules').rglob('syn-*.json')]
    pairs += [('assignment_relevance',str(p.relative_to(root))) for p in (root/'assignments').rglob('a1-r*.json')]
    errors=[]
    for p in (root/'schemas').glob('*.json'):
        try:jsonschema.Draft202012Validator.check_schema(json.loads(p.read_text()))
        except jsonschema.SchemaError as e:errors.append(str(e))
    for name,path in pairs:
        validator=jsonschema.Draft202012Validator(load(root,f'schemas/{name}.schema.json'))
        errors.extend(f'{path}: {e.message}' for e in validator.iter_errors(load(root,path)))
    return errors
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--local',action='store_true');ap.add_argument('--schemas',action='store_true');args=ap.parse_args()
    errors=validate(local=args.local)+(schema_errors() if args.schemas else [])
    if errors:
        print('\n'.join(errors));sys.exit(1)
    print('Structural validation passed. Research gates and human review are separate; run scripts/status.py.')
