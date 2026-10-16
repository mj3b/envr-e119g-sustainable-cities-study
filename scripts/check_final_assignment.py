#!/usr/bin/env python3
"""Verify the approved manuscript lock. This does not certify scholarly claims."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'assignments/assignment-02'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def body(text):
    return text[text.index('**A forecast'):text.index('## AI Use Disclosure')]


def word_count(text):
    text = re.sub(r'^\|\s*:?-+[^\n]*$', '', text, flags=re.M)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.M)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = text.replace('**', '').replace('*', '').replace('|', ' ')
    return len(text.split())


def check(root=ROOT):
    folder = root / 'assignments/assignment-02'
    lock = json.loads((folder/'final-lock-v011.json').read_text())
    final = (folder/'final-v011.md').read_text()
    original = (folder/'history/submission-candidate-v011.md').read_text()
    errors = []
    if body(final) != body(original):
        errors.append('The selected argument changed.')
    if digest(body(final).encode()) != lock['argument_sha256']:
        errors.append('Argument hash differs from owner-selected content.')
    if final.split('## References\n\n')[1] != original.split('## References\n\n')[1]:
        errors.append('The selected references changed.')
    if word_count(body(final)) != 1129:
        errors.append('Expected 1,129 counted words including headings and tables.')
    fname = 'ENVR_E119g_Assignment2_Final_v0.11.md'
    if digest(final.encode()) != lock['final_files'][fname]['sha256']:
        errors.append('Final Markdown hash mismatch.')
    cname = 'ENVR_E119g_Assignment2_Submission_Candidate_v0.11.md'
    if digest(original.encode()) != lock['prior_candidate_files_sha256'][cname]:
        errors.append('Original candidate changed.')
    previous = (folder/'history/authoring-checks-v011.json').read_bytes()
    if digest(previous) != lock['prior_candidate_files_sha256']['ENVR_E119g_Assignment2_Checks_v0.11.json']:
        errors.append('Historical authoring receipt changed.')
    if lock['status'] != 'author_approved_for_submission':
        errors.append('Unexpected manuscript selection state.')
    if lock['submission']['status'] != 'not_recorded' or lock['submission']['receipt'] is not None:
        errors.append('No course submission receipt was supplied for this edition.')
    if lock['human_fidelity_gates_modified'] or lock['new_translator_execution']:
        errors.append('Administrative locking cannot imply new fidelity approval or tool execution.')
    if '/tree/'+lock['release_tag'] not in final:
        errors.append('Supplementary link and checkpoint disagree.')
    expected = original.replace('*Submission candidate v0.11 | Not submitted*', '*Author-approved final v0.11*', 1)
    expected = expected.replace('/tree/v0.3.2)', '/tree/'+lock['release_tag']+')', 1)
    expected = expected.replace('Final source and voice review remain pending.', 'I have approved this version for submission.', 1)
    if final != expected:
        errors.append('An unrecorded change exceeds the finalization scope.')
    return errors


if __name__ == '__main__':
    errors = check()
    print('\n'.join(errors) if errors else 'Final lock passes: 1,129 words; approved argument unchanged; no submission inferred.')
    raise SystemExit(bool(errors))
