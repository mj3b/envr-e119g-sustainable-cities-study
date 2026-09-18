"""Cross-file reference closure and content-bound review receipts.

Receipts detect stale reviews; they do not authenticate a human or prove support.
"""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

def read(root,path):
    return json.loads((root/path).read_text())

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()

def claim_digest(root,ident,trail=()):
    claims={c['id']:c for c in read(root,'cross-course/claims.json')}
    sources={s['id']:s for s in read(root,'cross-course/evidence-registry.json')}
    if ident in trail: return 'cycle'
    c=dict(claims[ident]);c.pop('human_review',None)
    return digest({'claim':c,'source':sources.get(c['source_id']),
        'dependencies':{d:claim_digest(root,d,trail+(ident,)) for d in c['depends_on'] if d in claims}})

def gate_digest(root,pack,gate):
    """Conservatively invalidate after any canonical research or class artifact change."""
    paths=set()
    for folder in ['cross-course','modules','cases']:
        paths.update(p for p in (root/folder).rglob('*') if p.is_file() and p.suffix in {'.json','.md','.yaml'} and p.name not in {'review-receipts.json','fidelity-gates.json'} and not p.name.endswith('master-brief.md'))
    return digest({'class_number':pack['class_number'],'scope':pack['scope'],
        'gate':{k:gate[k] for k in ['id','name','evidence']},
        'files':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}})

def valid_receipt(receipts,target,expected,reviewer=None):
    for r in receipts:
        if r.get('target')!=target or r.get('digest')!=expected or r.get('decision')!='approved':continue
        if not r.get('reviewer','').strip() or not r.get('rationale','').strip():continue
        if reviewer and r['reviewer']!=reviewer:continue
        try:
            dt=datetime.fromisoformat(r['reviewed_at'].replace('Z','+00:00'))
            if dt.tzinfo is None or dt>datetime.now(timezone.utc):continue
        except (ValueError,KeyError,TypeError):continue
        return True
    return False

def checks(root):
    errors=[]
    claims={c['id']:c for c in read(root,'cross-course/claims.json')}
    sources={s['id']:s for s in read(root,'cross-course/evidence-registry.json')}
    concepts={c['id']:c for c in read(root,'cross-course/concept-registry.json')}
    receipt_path=root/'cross-course/review-receipts.json'
    receipts=json.loads(receipt_path.read_text()) if receipt_path.exists() else []
    if not isinstance(receipts,list):return ['Review receipts must be an array']
    reqids={r['id'] for p in (root/'assignments').glob('*/requirements.json') for r in json.loads(p.read_text())['requirements']}
    def walk(obj,path):
        if isinstance(obj,list):
            for item in obj:walk(item,path)
        elif isinstance(obj,dict):
            for k,v in obj.items():
                lookup=None
                if k in {'claim_ids','reading_claim_ids','lecture_claim_ids','depends_on'}:lookup=claims
                elif k in {'concept_ids','related_concepts'}:lookup=concepts
                elif k=='source_ids':lookup=sources
                if lookup is not None:
                    if not isinstance(v,list):errors.append(f'Expected reference list {k}: {path}')
                    else:
                        for ident in v:
                            if not isinstance(ident,str) or ident not in lookup:errors.append(f'Unknown {k} reference {ident}: {path}')
                if k=='source_id' and v not in sources:errors.append(f'Unknown source reference {v}: {path}')
                if k=='requirement_id' and v not in reqids:errors.append(f'Unknown assignment requirement {v}: {path}')
                if k=='argument_map':
                    full=(root/v).resolve()
                    if not full.is_relative_to(root.resolve()) or not full.is_file():errors.append(f'Invalid argument map: {path}')
                walk(v,path)
    for folder in ['modules','assignments','study','cases','cross-course']:
        for p in (root/folder).rglob('*.json'):
            if '.template.' not in p.name and p.name!='review-receipts.json':walk(json.loads(p.read_text()),p.relative_to(root))
    for c in claims.values():
        if c['human_review']=='approved':
            if c['speaker_role']=='unknown' or (c['evidence_class'] in {'instructor_lecture','ta_guidance','peer_discourse'} and c['speaker_confidence'] in {'low','not_applicable'}):errors.append(f'Unresolved speaker approved: {c["id"]}')
            if not valid_receipt(receipts,'claim:'+c['id'],claim_digest(root,c['id'])):errors.append(f'Missing or stale claim review: {c["id"]}')
    names={'G1':'source_fidelity','G2':'lecture_fidelity','G3':'synthesis_fidelity'}
    for p in (root/'modules').rglob('fidelity-gates.json'):
        pack=json.loads(p.read_text())
        for g in pack['gates']:
            if names.get(g['id'])!=g['name']:errors.append(f'Gate ID/name mismatch: {p}')
            if g['status']=='pass':
                if not g['evidence']:errors.append(f'Gate has no evidence: {p}')
                if not valid_receipt(receipts,f'gate:{pack["class_number"]}:{g["id"]}',gate_digest(root,pack,g),g['reviewer']):errors.append(f'Missing or stale gate review: {pack["class_number"]}/{g["id"]}')
    case=read(root,'cases/candidate-family.json');ids=[c['id'] for c in case['candidates']]
    selected=[c['id'] for c in case['candidates'] if c['selected']]
    if len(ids)!=len(set(ids)):errors.append('Duplicate case candidate')
    if case['selected_case_id'] is not None and case['selected_case_id'] not in ids:errors.append('Unknown selected case')
    if case['geography_locked']:
        if selected!=[case['selected_case_id']]:errors.append('Case selection flags disagree')
        decision=root/'cases/selection-decision.json'
        if not decision.exists():errors.append('Locked geography requires a selection decision')
        else:
            d=json.loads(decision.read_text())
            if d.get('selected_case_id')!=case['selected_case_id'] or not d.get('rationale') or not d.get('alternatives') or not d.get('evidence_ids') or any(s not in sources for s in d.get('evidence_ids',[])):errors.append('Incomplete selection decision')
    elif selected or case['selected_case_id'] is not None:errors.append('Unlocked case has selection flags')
    return errors
