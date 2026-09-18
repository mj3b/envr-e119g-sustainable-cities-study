#!/usr/bin/env python3
"""Record reproducible automated checks without creating scholarly approval."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = 'governance/evaluation-results.json'


def inventory(root):
    result = subprocess.run(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'],
        cwd=root, capture_output=True, check=True)
    names = sorted(set(result.stdout.decode().split('\0')) - {'', RECEIPT})
    files = {}
    for name in names:
        path = root / name
        if path.is_symlink():
            raise ValueError(f'Symlink requires explicit review: {name}')
        if path.is_file():
            files[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        else:
            files[name] = 'deleted'
    return files


def fingerprint(files):
    return hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()


def link_errors(root, files, pending_receipt=False):
    errors = []
    count = 0
    for name in files:
        path = root / name
        if path.suffix != '.md' or not path.is_file():
            continue
        # Inline Markdown links/images. Reference-style and fragment targets are
        # not verified; this intentionally does not claim rendered-page testing.
        body = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', body):
            parsed = urlsplit(target.strip('<>'))
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            count += 1
            dest = (path.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(root.resolve()):
                errors.append(f'{name}: local link escapes repository: {target}')
            elif not dest.exists() and not (pending_receipt and dest == (root / RECEIPT).resolve()):
                errors.append(f'{name}: missing local link: {target}')
    return count, errors


def receipt_errors(root, result, files):
    errors = []
    if result.get('schema_version') != 1:
        errors.append('Unsupported evaluation receipt version')
    if result.get('files') != files or result.get('fingerprint') != fingerprint(files):
        errors.append('Evaluation receipt is stale: evaluated files changed')
    checks = result.get('checks', [])
    expected = {'structural_and_schema', 'privacy_paths_and_history', 'unit_tests', 'local_markdown_links'}
    if {c.get('id') for c in checks} != expected or len(checks) != len(expected):
        errors.append('Evaluation receipt is missing required checks')
    if result.get('automated_status') != 'pass' or any(c.get('exit_code') != 0 for c in checks):
        errors.append('Automated evaluation did not pass')
    if result.get('human_fidelity') != 'not_assessed_by_this_runner':
        errors.append('Automated receipt cannot certify human fidelity')
    try:
        dt = datetime.fromisoformat(result['evaluated_at'].replace('Z', '+00:00'))
        if dt.tzinfo is None or dt > datetime.now(timezone.utc):
            errors.append('Invalid evaluation time')
    except (KeyError, ValueError, TypeError):
        errors.append('Invalid evaluation time')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--local', action='store_true', help='Verify ignored local source digests too')
    parser.add_argument('--check', action='store_true', help='Check stored receipt freshness, without rerunning evaluation')
    args = parser.parse_args()
    files = inventory(ROOT)
    if args.check:
        try:
            result = json.loads((ROOT / RECEIPT).read_text())
            errors = receipt_errors(ROOT, result, files)
        except (OSError, ValueError, TypeError) as exc:
            errors = [f'Cannot inspect evaluation receipt: {exc}']
        # Reachable Git history and staging can change without file-byte changes.
        privacy = subprocess.run([sys.executable, 'scripts/privacy_check.py'], cwd=ROOT,
                                 capture_output=True, text=True)
        if privacy.returncode:
            errors.append('Current privacy check failed: ' + (privacy.stdout + privacy.stderr).strip())
        print('\n'.join(errors) if errors else 'Automated receipt is current; human fidelity remains separate.')
        return bool(errors)

    checks = []
    commands = [
        ('structural_and_schema', [sys.executable, 'scripts/validate.py', '--schemas'] + (['--local'] if args.local else [])),
        ('privacy_paths_and_history', [sys.executable, 'scripts/privacy_check.py']),
        ('unit_tests', [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v']),
    ]
    for ident, command in commands:
        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        output = (run.stdout + run.stderr).strip()
        # Keep the command portable across developer machines.
        checks.append({'id': ident, 'command': ['python'] + command[1:], 'exit_code': run.returncode, 'output': output})
        print(f'{ident}: {"pass" if run.returncode == 0 else "FAIL"}')
    count, errors = link_errors(ROOT, {**files, RECEIPT: ''}, pending_receipt=True)
    checks.append({'id': 'local_markdown_links', 'exit_code': int(bool(errors)), 'checked_links': count,
                   'scope': 'Inline repository-relative path targets; excludes anchors, external URLs and reference-style links',
                   'output': '\n'.join(errors) if errors else 'Local Markdown path targets resolve'})
    print(f'local_markdown_links: {"pass" if not errors else "FAIL"} ({count} targets)')
    after = inventory(ROOT)
    if after != files:
        print('Files changed during evaluation; no receipt written. Repeat after edits finish.')
        return 1
    result = {
        'schema_version': 1,
        'evaluated_at': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'executor': 'automated Python runner; invoked in an AI-assisted work session',
        'scope': 'repository files; local source digests included' if args.local else 'repository files; private original bytes not checked',
        'automated_status': 'pass' if all(c['exit_code'] == 0 for c in checks) else 'fail',
        'human_fidelity': 'not_assessed_by_this_runner',
        'checks': checks,
        'fingerprint': fingerprint(files),
        'files': files,
    }
    (ROOT / RECEIPT).write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(f'Receipt written: {RECEIPT}. Human review was not changed.')
    return result['automated_status'] != 'pass'


if __name__ == '__main__':
    raise SystemExit(main())
