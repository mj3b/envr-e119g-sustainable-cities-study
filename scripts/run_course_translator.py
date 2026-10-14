#!/usr/bin/env python3
"""Build bounded course packs and execute the pinned upstream schema validators.

This does not call a model, read a PDF semantically, or create a human decision.
The AI-authored source cards are inputs, not outputs of an independent evaluator.
"""
from __future__ import annotations
import argparse
import concurrent.futures
import hashlib
import importlib.metadata
import json
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'research/course-readings'
PIN = '4e5d742378dd2fecbafd525eeb9754c975b83aa0'
STEPS = [
    ('agent_spec', 'validate_pack.sh', None),
    ('claims', 'validate_claims.sh', None),
    ('tasks', 'validate_tasks.sh', None),
    ('run_input', 'validate_run_input.sh', 'run_input.json'),
    ('run_output', 'validate_run_output.sh', 'run_output.json'),
]


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def artifacts(card: dict, created_at: str) -> dict:
    sid = card['source_id']
    claim = card['claim']
    task_id = sid + '-T1'
    run_id = sid + '-20261014-candidate'
    non_goals = [card['claim']['prohibited_inference'], 'No new Cerrillos finding or case-source revalidation.',
                 'No human acceptance, deployment authorization or course submission.',
                 'No independent scientific replication or automated full-paper interpretation.']
    criteria = ['Source identity and locator are present.', 'The candidate preserves its qualifying evidence.',
                'The output does not turn an attributed argument or projection into an observation.',
                'A human must decide source fidelity and memo fit.']
    source = {'paper_text_path': 'source/paper_text.txt',
              'method': 'AI-assisted direct reading of supplied PDF text and selected page images; bounded quotation record',
              'notes': 'Only the quoted anchor is included publicly. The full supplied PDF and extraction remain outside Git. '
                       'These are candidate source descriptions; theoretical and normative claims are not recast as experimentally established facts.'}
    claims = {'claims_version': '1.0', 'pack_id': sid, 'created_at': created_at, 'source': source,
              'claims': [{'claim_id': claim['claim_id'], 'claim_type': 'measurement' if sid.startswith('M2') or sid=='M1-LOWE' else 'other',
                          'claim_text': claim['text'],
                          'operationalization': {'task': card['task']['name'], 'inputs': [card['filename'], claim['locator']],
                              'outputs': ['Candidate source-to-method mapping', 'Qualifying evidence', 'Pending human review'],
                              'metric': 'Source-fidelity and scope checklist; this is not a causal-effect metric.'},
                          'testability': {'level': 'medium', 'eval_hint': 'Compare the bounded source description with the identified passages. This tests fidelity of the description, not truth of the underlying theory.',
                                          'failure_modes': non_goals},
                          'dependencies': [claim['missing_dependency']],
                          'evidence': [{'source': 'paper_text', 'quote': claim['evidence_quote'], 'location_hint': claim['locator']}]}]}
    field = {'name': 'source_card', 'type': 'object', 'description': 'Versioned, AI-authored source description and limits', 'example': {'source_id': sid}}
    output_schema = {'type':'object','required':['source_id','candidate_use','qualifications','human_review'],
                     'properties':{'source_id':{'type':'string'},'candidate_use':{'type':'string'},'qualifications':{'type':'array'},'human_review':{'type':'object'}}}
    task = {'task_id': task_id, 'from_claim_id': claim['claim_id'], 'name': card['task']['name'],
            'objective': 'Prepare evidence-limited reading relevance for Assignment 2; the author retains the decision.',
            'inputs': {'required':[field], 'optional':[]}, 'outputs': {'primary_schema':output_schema,'evidence_items_min':1},
            'constraints': {'assumptions':['The supplied edition remains the citation basis.'], 'non_goals':non_goals,
                            'allowed_tools':['Local file hashing','Original upstream JSON-schema validators','Human source review']},
            'abstention': {'required': True, 'triggers':['Source-byte mismatch','Unsupported numerical or causal claim','Edition mismatch','Missing case-specific evidence'],
                           'fallback_action':'Retain a qualified or blocked source-use candidate; do not fill gaps.'},
            'evaluation': {'metrics':criteria,'acceptance_thresholds':['All structural schemas must pass; human fidelity remains pending.'],
                           'test_set_plan':'This 11-reading corpus is a task-defined set, not a representative benchmark or independent test set.'},
            'governance': {'human_checkpoint':'Mark reviews the source, interpretation and final assignment wording.',
                           'logging_requirements':['Original SHA-256','Source version and locator','Actual command and exit code','No invented human gate']}}
    tasks={'tasks_version':'1.0','pack_id':sid,'created_at':created_at,
           'source':{'claims_path':'claims.json','method':'Deterministic serialization of an AI-authored bounded task'},'tasks':[task]}
    sf={**field,'constraints':{'allowed_values':None,'regex':None,'min':None,'max':None},'required':True}
    spec={'spec_version':'1.0','spec_id':sid+'-SPEC','created_at':created_at,'status':'review',
          'decision':{'name':'Course-source use candidate','user':{'persona':'Student researcher','primary_goal':'Prepare a defensible Assignment 2 research plan','environment':'Public study repository with private source originals'},
              'decision_statement':'Recommend a bounded use of this reading for human review.',
              'failure_cost':{'severity':'medium','harms':['Unsupported academic claim','False source access or attribution'],'reversibility':'partially_reversible'},
              'success_criteria':criteria,'scope':{'included':['Versioned source card','Candidate task','Schema validation'],'excluded':non_goals}},
          'inputs':{'modalities':['text','source-page images inspected by the assisting model'],'required_fields':[sf], 'optional_fields':[],
                    'data_quality_assumptions':['Text extraction can omit symbols, layout and scanned content.'],
                    'redaction_rules':[{'rule':'Publish source metadata, short anchors and authored analysis; exclude full course files.'}]},
          'outputs':{'primary_output_schema':output_schema,
                     'evidence_requirements':{'citations_required':True,'citation_format':'Supplied version, PDF page and printed page/section','min_evidence_items':1},
                     'confidence_labeling':{'required':True,'scale':'Qualitative, bounded to source-description fidelity','calibration_notes':'Model confidence is not human acceptance.'},
                     'abstention':{'required':True,'triggers':[{'condition':x} for x in task['abstention']['triggers']], 'fallback_action':task['abstention']['fallback_action'],'message_template':'Source use remains qualified or blocked pending the named dependency.'}},
          'evaluation':task['evaluation'],'governance':{'human_review':'pending','reviewer':None,'source_validation_by_schema':False},
          'provenance':{'upstream_commit':PIN,'source_sha256':card['sha256'],'original_pdf_in_public_pack':False,'ai_authored_input':True}}
    result={'source_id':sid,'candidate_use':claim['permitted_use'],'qualifications':claim['contrary_or_qualifying_evidence'],
            'priority':card['assignment2_priority'],'prohibited_inference':claim['prohibited_inference'], 'human_review':card['human_review']}
    run_input={'run_id':run_id,'pack_id':sid,'task_id':task_id,'created_at':created_at,
               'inputs':{'source_card':card,'source_card_origin':'AI-authored in the current conversation; not an independent model run'}}
    run_output={'run_id':run_id,'pack_id':sid,'task_id':task_id,'created_at':created_at,'status':'ok','result':result,
                'evidence':[claim['locator'], 'Original PDF SHA-256: '+card['sha256']],
                'notes':'ok means a candidate mapping was serialized. It is not approval or evidence that a scientific claim is correct.'}
    return {'agent_spec.json':spec,'claims.json':claims,'tasks.json':tasks,'eval_plan.json':task['evaluation'],
            'run_input.json':run_input,'run_output.json':run_output}


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--translator-root',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True,help='New directory, preferably outside the public checkout')
    p.add_argument('--source-dir',type=Path,help='Directory holding the original uploaded PDFs; bytes are hashed but never copied')
    p.add_argument('--structures-only',action='store_true',help='Explicitly skip original PDF checks; produces a different scope record')
    a=p.parse_args()
    if bool(a.source_dir)==bool(a.structures_only): p.error('Choose --source-dir or --structures-only, exclusively.')
    if a.output.exists(): p.error('Output already exists; choose a new directory to preserve the previous run.')
    up=a.translator_root.resolve()
    expected=json.loads((DATA/'upstream-files.json').read_text())
    for rel,digest in expected['files_sha256'].items():
        if sha(up/rel)!=digest: raise ValueError('Pinned upstream file differs: '+rel)
    corpus=json.loads((DATA/'source-cards.json').read_text())
    cards=corpus['cards']
    inspections=[]
    for c in cards:
        if not re.fullmatch(r'M[12]-[A-Z]+',c['source_id']): raise ValueError('Unsafe pack id')
        if Path(c['filename']).name!=c['filename']: raise ValueError('Source filename is not a basename')
        if a.source_dir:
            source=a.source_dir/c['filename']
            actual=sha(source)
            if actual!=c['sha256']: raise ValueError('Original byte mismatch: '+c['filename'])
            inspections.append({'source_id':c['source_id'],'filename':c['filename'],'sha256':actual,'byte_check':'pass'})
        else:
            inspections.append({'source_id':c['source_id'],'filename':c['filename'],'sha256':c['sha256'],'byte_check':'not_performed'})
    a.output.mkdir(parents=True)
    started=datetime.now(timezone.utc).isoformat()
    logs=[]; artifact_hashes={}; pending_commands=[]
    for c in cards:
        pack=a.output/c['source_id']; pack.mkdir(); (pack/'source').mkdir()
        # Explicit short quotation record, not a surrogate full paper.
        (pack/'source/paper_text.txt').write_text(c['claim']['evidence_quote']+'\n',encoding='utf-8')
        (pack/'README.md').write_text('# '+c['title']+'\n\nCandidate course pack; human review pending.\n\nSource: '+c['supplied_version']+'. '+c['claim']['locator']+'.\n\nThe source text file contains only a short anchor quotation. The full course PDF remains private. These artifacts were authored with AI assistance and mechanically validated; they are not a new independent interpretation by Translator.\n',encoding='utf-8')
        for name,value in artifacts(c,corpus['created_at_utc']).items(): write_json(pack/name,value)
        for ident,script,target in STEPS:
            argument=pack/target if target else pack
            command=['bash','scripts/'+script,str(argument.resolve())]
            pending_commands.append((c['source_id'],ident,command))
        for f in sorted(pack.rglob('*')):
            if f.is_file(): artifact_hashes[f.relative_to(a.output).as_posix()]=sha(f)
    def execute(item):
        sid,ident,command=item
        run=subprocess.run(command,cwd=up,capture_output=True,text=True,timeout=60)
        return {'source_id':sid,'check':ident,'command':command,'cwd':str(up),
                'exit_code':run.returncode,'stdout':run.stdout,'stderr':run.stderr}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        logs=list(pool.map(execute,pending_commands))
    receipt={'schema_version':1,'record_type':'Actual execution receipt; schema-validation phase of upstream Translator',
             'started_at_utc':started,'finished_at_utc':datetime.now(timezone.utc).isoformat(),
             'upstream_repository':'node-and-norm/applied-ai-research-translator','upstream_commit':PIN,
             'upstream_verified_files':expected['files_sha256'],'source_cards_sha256':sha(DATA/'source-cards.json'),
             'python':platform.python_version(),'jsonschema':importlib.metadata.version('jsonschema'),
             'mode':'source_bytes_checked_and_candidate_schemas_validated' if a.source_dir else 'structures_only_original_bytes_not_checked',
             'source_checks':inspections,'pack_count':len(cards),'validator_invocations':len(logs),
             'passed':sum(x['exit_code']==0 for x in logs),'failed':sum(x['exit_code']!=0 for x in logs),
             'commands':logs,'artifact_sha256':artifact_hashes,
             'candidate_analysis_origin':'ChatGPT-assisted reading; supplied source-cards.json. Upstream validators only check structure.',
             'semantic_validation':'Not performed by upstream software; candidate readings remain subject to human checking.',
             'provider_api_calls':0,'live_jev_calls':0,'upstream_agent_runloop_executed':False,
             'human_gate_written':False,'decision_summary_written':False,'human_scholarly_approval':None,
             'safety_policy_intake':'Not invoked: these packs are bounded urban-course source-use records, not AI safety-policy intake or operational authorization.',
             'scope_limits':['validate_pack.sh validates agent_spec.json only; the other four validators are listed separately.',
                 'No automated full-PDF reader, scientific replication, model accuracy benchmark or field evaluation ran.',
                 'No raw course PDF or full extraction was copied into the packs.',
                 'The candidate generation was not preregistered or independent of the authoring model.',
                 'McConnell external HTML is separately recorded and excluded from this uploaded-PDF run.']}
    write_json(a.output/'execution-receipt.json',receipt)
    print(json.dumps({'packs':len(cards),'invocations':len(logs),'passed':receipt['passed'],'failed':receipt['failed'],
                      'mode':receipt['mode'],'receipt':str(a.output/'execution-receipt.json')}))
    return bool(receipt['failed'])

if __name__=='__main__':
    sys.exit(main())
