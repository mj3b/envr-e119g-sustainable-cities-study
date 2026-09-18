"""Research references, temporal boundaries, measurements, and selection checks."""
import json
from datetime import date
from integrity import digest, valid_receipt

def read(root,path):
    return json.loads((root/path).read_text())

def research_digest(root):
    # Bind the entire small research packet, including source and claim changes.
    return digest({p:read(root,p) for p in ['cases/research-objects.json',
        'cases/discovery.json','cases/candidate-family.json',
        'cross-course/claims.json','cross-course/evidence-registry.json']})

def checks(root):
    errors=[]
    rows=read(root,'cases/research-objects.json')
    by_id={o['id']:o for o in rows}
    if len(by_id)!=len(rows):errors.append('Duplicate research object ID')
    family=read(root,'cases/candidate-family.json')
    candidates={c['id'] for c in family['candidates']}
    claims={c['id']:c for c in read(root,'cross-course/claims.json')}
    sources={s['id'] for s in read(root,'cross-course/evidence-registry.json')}
    receipts=read(root,'cross-course/review-receipts.json')
    types={'research_question','hypothesis','assumption','actor','authority','decision',
        'decision_evidence','timeline_event','measurement','contradiction','alternative','outcome'}
    ref_types={'question_id':'research_question','rival':'hypothesis','actor_id':'actor',
        'authority_id':'authority','decision_id':'decision','evidence_ids':'decision_evidence',
        'alternative_ids':'alternative','outcome_ids':'outcome','measurement_ids':'measurement',
        'input_ids':'measurement','assumption_ids':'assumption'}
    def ref(ident,expected,owner):
        target=by_id.get(ident)
        if not target or target['type']!=expected:
            errors.append(f'Invalid {expected} reference {ident}: {owner}')
        return target
    for o in rows:
        ident=o['id'];d=o['data'];kind=o['type']
        if kind not in types:errors.append(f'Unknown research type: {ident}')
        if o['evidence_class']!='our_synthesis':errors.append(f'Research object changes evidence lane: {ident}')
        for k,registry in [('candidate_ids',candidates),('claim_ids',claims),('source_ids',sources)]:
            for value in o[k]:
                if value not in registry:errors.append(f'Unknown research {k} {value}: {ident}')
        for k,expected in ref_types.items():
            if k in d:
                for value in d[k] if isinstance(d[k],list) else [d[k]]:ref(value,expected,ident)
        for k in ['left_claim_id','right_claim_id']:
            if k in d and d[k] not in claims:errors.append(f'Unknown contradiction claim: {ident}')
        for k,v in d.items():
            if k.endswith('_date') and v is not None:
                try:date.fromisoformat(v)
                except (ValueError,TypeError):errors.append(f'Invalid date {k}: {ident}')
        if o['human_review']=='approved':
            if not valid_receipt(receipts,'research:'+ident,research_digest(root)):
                errors.append(f'Missing or stale research review: {ident}')
            if any(claims.get(c,{}).get('human_review')!='approved' for c in o['claim_ids']):
                errors.append(f'Research approval depends on unapproved claims: {ident}')
        if kind=='decision_evidence':
            dec=by_id.get(d['decision_id'],{}).get('data',{})
            when=dec.get('decision_date');available=d['available_to_actor_date']
            if d['availability']=='documented_at_decision':
                if not when or not available or available>when:
                    errors.append(f'Decision-time evidence lacks timely access: {ident}')
                if d['event_date'] and when and d['event_date']>when:
                    errors.append(f'Later event used at decision time: {ident}')
            if not o['source_ids'] or not d['locator'] or not d['availability_basis']:
                errors.append(f'Decision evidence lacks provenance: {ident}')
        if kind=='decision':
            for field in ['evidence_ids','alternative_ids','outcome_ids']:
                for value in d[field]:
                    target=by_id.get(value)
                    if target and target['data'].get('decision_id')!=ident:
                        errors.append(f'Decision ownership mismatch: {ident}/{value}')
        if kind=='measurement':
            status=d['observation_status'];value=d['value']
            if status=='unknown' and value is not None:errors.append(f'Unknown measurement has value: {ident}')
            if status!='unknown' and value is None:errors.append(f'Valued measurement missing value: {ident}')
            if status in {'observed','reported','modeled','projected'} and (not o['source_ids'] or not d['locator']):
                errors.append(f'Measurement lacks source and locator: {ident}')
            if d['unit']=='MW' and d['quantity_kind']!='power':errors.append(f'MW mislabeled as energy: {ident}')
            if d['unit']=='MWh' and d['quantity_kind']!='energy':errors.append(f'MWh mislabeled: {ident}')
            if status=='observed' and any(by_id.get(i,{}).get('data',{}).get('observation_status') in {'illustrative','projected','modeled'} for i in d['input_ids']):
                errors.append(f'Modeled input promoted to observation: {ident}')
        if kind=='alternative' and d['origin']=='documented_proposal' and (not o['source_ids'] or not d['locator']):
            errors.append(f'Documented alternative lacks provenance: {ident}')
        if kind=='outcome':
            if d['outcome_status']=='observed' and (not d['measurement_ids'] or any(by_id.get(i,{}).get('data',{}).get('observation_status')!='observed' for i in d['measurement_ids'])):
                errors.append(f'Observed outcome lacks observations: {ident}')
            if d['causal_status']=='supported' and (not d['comparison'] or not d['competing_explanations'] or d['outcome_status']=='unknown'):
                errors.append(f'Causal outcome lacks comparison: {ident}')
    # Only derivation edges must be acyclic. Rival hypotheses can reference each other.
    def visit(ident,trail):
        if ident in trail:errors.append(f'Measurement dependency cycle: {ident}');return
        for dep in by_id[ident]['data'].get('input_ids',[]):
            if dep in by_id:visit(dep,trail|{ident})
    for o in rows:
        if o['type']=='measurement':visit(o['id'],set())
    discovery=read(root,'cases/discovery.json')
    scored=[c['candidate_id'] for c in discovery['candidates']]
    if len(scored)!=len(set(scored)) or set(scored)!=candidates:
        errors.append('Discovery candidates do not match family')
    if set(discovery['retrieval_priority'])!=candidates or len(discovery['retrieval_priority'])!=len(candidates):
        errors.append('Retrieval priority must include each candidate once')
    if discovery['selection']!=family['selected_case_id']:errors.append('Discovery selection disagrees with family')
    for c in discovery['candidates']:
        if set(c['assessments'])!=set(discovery['criteria']):errors.append('Incomplete selection dimensions')
        for a in c['assessments'].values():
            if a['score'] not in [None,0,1,2,3] or isinstance(a['score'],bool):errors.append('Invalid discovery score')
            if not a['reason'].strip():errors.append('Discovery score lacks rationale')
        if c['selection_ready']:
            if any(a['score'] is None or a['score']<2 for a in c['assessments'].values()):
                errors.append('Selection-ready case has unresolved evidence dimensions')
            decisions=[o for o in rows if o['type']=='decision' and c['candidate_id'] in o['candidate_ids'] and o['data']['decision_date'] and o['data']['record_status']=='recorded_vote']
            if not decisions:errors.append('Selection-ready case lacks bounded decision record')
    if family['geography_locked']:
        selected=next((c for c in discovery['candidates'] if c['candidate_id']==family['selected_case_id']),{})
        if not selected.get('selection_ready'):errors.append('Selected case has not passed discovery checks')
    return errors
