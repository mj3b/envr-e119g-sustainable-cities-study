#!/usr/bin/env python3
"""Limited public-content checks. Does not certify privacy, rights, or truth."""
import json, re, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def check(root=ROOT):
    errors=[]
    policy=json.loads((root/'governance/publication-policy.json').read_text())
    if policy.get('expected_visibility')!='public' or policy.get('owner_authorized_public') is not True:
        errors.append('Explicit public-mode record required')
    if policy.get('submission_authorized') is not False or policy.get('human_scholarly_approval_by_automation') is not False:
        errors.append('Unsupported approval authority')
    paths=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=root).decode().split('\0')
    # Pattern scan is deliberately narrow and is not called a secrets audit.
    patterns=[r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'\bgh[pousr]_[A-Za-z0-9]{30,}\b',r'\bgithub_pat_[A-Za-z0-9_]{40,}\b']
    for name in set(paths)-{''}:
        path=root/name
        if any(x in Path(name).parts for x in ['raw-course','correspondence','transcripts']): errors.append('Restricted path: '+name)
        if path.is_file() and path.suffix in {'.md','.json','.py','.yaml','.yml','.txt'}:
            text=path.read_text(errors='replace')
            if any(re.search(p,text) for p in patterns): errors.append('Potential credential material: '+name)
    return errors
if __name__=='__main__':
    errors=check(); print('\n'.join(errors) if errors else 'Public-mode checks passed; semantic publication and source-fidelity reviews remain separate.')
    raise SystemExit(bool(errors))
