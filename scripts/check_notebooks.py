#!/usr/bin/env python3
"""Check the three public notebooks; optionally replay the fictional example.

This checks structure, local navigation and limited publication hazards. It does
not establish source fidelity, reader comprehension or scholarly approval.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = (
    'docs/START-HERE.ipynb',
    'docs/FACULTY-GUIDE.ipynb',
    'methods/evidence-review/trace-a-claim.ipynb',
)
READING_GUIDES = set(NOTEBOOKS[:2])
SECRET_PATTERNS = (
    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    r'\bgh[pousr]_[A-Za-z0-9]{30,}\b',
    r'\bgithub_pat_[A-Za-z0-9_]{40,}\b',
    r'\bsk-[A-Za-z0-9_-]{30,}\b',
)
PRIVATE_PATH_PATTERN = r'(?:/Users/|/private/tmp/|/mnt/data/|file://)'
ACTIVE_HTML_PATTERN = r'<\s*(?:script|iframe|object|embed|form)\b'
INLINE_LINK = re.compile(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)')


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON field: ' + key)
        result[key] = value
    return result


def source_text(value):
    if isinstance(value, str):
        return value
    if isinstance(value, list) and all(isinstance(x, str) for x in value):
        return ''.join(value)
    raise ValueError('Expected a string or list of strings')


def textual_values(value):
    """Read decoded text so JSON newline escapes cannot hide token boundaries."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        if all(isinstance(item, str) for item in value):
            yield ''.join(value)
        else:
            for item in value:
                yield from textual_values(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from textual_values(item)


def local_link_errors(text, notebook_path, root):
    errors = []
    body = re.sub(r'```.*?```', '', text, flags=re.S)
    for target in INLINE_LINK.findall(body):
        target = target.strip('<>')
        parsed = urlsplit(target)
        if parsed.scheme and parsed.scheme not in ('https', 'http', 'mailto'):
            errors.append('Unsupported link scheme: ' + parsed.scheme)
            continue
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        dest = (notebook_path.parent / unquote(parsed.path)).resolve()
        try:
            relative = dest.relative_to(root.resolve())
        except ValueError:
            errors.append('Local link escapes repository: ' + target)
            continue
        if any(part in {'private', 'raw-course', 'transcripts', 'correspondence'} for part in relative.parts):
            errors.append('Restricted local link: ' + target)
        elif not dest.exists():
            errors.append('Missing local link: ' + target)
    return errors


def validate_notebook(data, notebook_path, root=ROOT, reading_only=False):
    errors = []
    if not isinstance(data, dict):
        return ['Notebook must be a JSON object']
    if data.get('nbformat') != 4 or type(data.get('nbformat_minor')) is not int or data.get('nbformat_minor', 0) < 5:
        errors.append('Expected notebook format 4.5 or later with stable cell IDs')
    metadata = data.get('metadata')
    if not isinstance(metadata, dict):
        errors.append('Notebook metadata must be an object')
    elif reading_only:
        if not isinstance(metadata.get('title'), str) or not metadata['title'].strip():
            errors.append('Reading guide needs a descriptive metadata title')
        guide_metadata = metadata.get('study_reader_guide')
        if not isinstance(guide_metadata, dict) or guide_metadata.get('execution_required') is not False:
            errors.append('Reading guide must declare that execution is not required')
    cells = data.get('cells')
    if not isinstance(cells, list) or not cells:
        return errors + ['Notebook requires nonempty cells']
    raw = '\n'.join(textual_values(data))
    if any(re.search(pattern, raw) for pattern in SECRET_PATTERNS):
        errors.append('Potential credential material in notebook')
    if re.search(PRIVATE_PATH_PATTERN, raw):
        errors.append('Private host path in notebook')
    if isinstance(metadata, dict) and 'widgets' in metadata:
        errors.append('Embedded widget state is outside the public notebook scope')
    identifiers = set()
    heading_count = 0
    code_count = 0
    for number, cell in enumerate(cells, 1):
        label = f'Cell {number}: '
        if not isinstance(cell, dict):
            errors.append(label + 'cell must be an object')
            continue
        ident = cell.get('id')
        if not isinstance(ident, str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,64}', ident):
            errors.append(label + 'missing or invalid cell ID')
        elif ident in identifiers:
            errors.append(label + 'duplicate cell ID')
        identifiers.add(ident if isinstance(ident, str) else number)
        if not isinstance(cell.get('metadata'), dict):
            errors.append(label + 'cell metadata must be an object')
        try:
            text = source_text(cell.get('source'))
        except ValueError:
            errors.append(label + 'invalid source text')
            continue
        kind = cell.get('cell_type')
        if kind == 'markdown':
            heading_count += len(re.findall(r'^#\s+\S', text, flags=re.M))
            if 'outputs' in cell or 'execution_count' in cell:
                errors.append(label + 'Markdown cell has execution fields')
            if cell.get('attachments'):
                errors.append(label + 'embedded attachments require a separate publication review')
            if re.search(ACTIVE_HTML_PATTERN, text, flags=re.I):
                errors.append(label + 'active HTML is outside the reading-guide scope')
            errors.extend(label + error for error in local_link_errors(text, notebook_path, root))
        elif kind == 'code':
            code_count += 1
            if reading_only:
                errors.append(label + 'prose reader guide cannot contain executable cells')
            count = cell.get('execution_count')
            if count is not None and (type(count) is not int or count < 1):
                errors.append(label + 'invalid execution count')
            outputs = cell.get('outputs')
            if not isinstance(outputs, list):
                errors.append(label + 'code outputs must be a list')
                continue
            if outputs and count is None:
                errors.append(label + 'saved output has no execution count')
            for output in outputs:
                if not isinstance(output, dict) or output.get('output_type') != 'stream' or output.get('name') not in ('stdout', 'stderr'):
                    errors.append(label + 'only plain-text stream output is allowed')
                    continue
                try:
                    source_text(output.get('text'))
                except ValueError:
                    errors.append(label + 'invalid stream output text')
        else:
            errors.append(label + 'unsupported cell type')
    if heading_count != 1:
        errors.append('Notebook must have one top-level Markdown title')
    if not reading_only and not code_count:
        errors.append('Worked example requires an executable demonstration cell')
    return errors


def check(root=ROOT):
    errors = []
    for name in NOTEBOOKS:
        path = root / name
        try:
            data = json.loads(path.read_text(), object_pairs_hook=unique_object)
            issues = validate_notebook(data, path, root, name in READING_GUIDES)
        except (OSError, ValueError, TypeError) as exc:
            issues = [str(exc)]
        errors.extend(name + ': ' + issue for issue in issues)
    return errors


def execute_worked(root=ROOT):
    """Replay the known fictional cell in a child process without rewriting it."""
    path = root / NOTEBOOKS[2]
    # The child keeps imports in the demonstration folder, blocks socket calls,
    # captures the saved stream format, and compares output without mutation.
    harness = r'''
import contextlib, io, json, os, socket, sys
from pathlib import Path
from unittest.mock import patch
os.environ['LANGSMITH_TRACING'] = 'false'
os.environ['LANGCHAIN_TRACING_V2'] = 'false'
notebook = json.loads(Path('trace-a-claim.ipynb').read_text())
namespace = {'__name__': '__main__'}
results = []
for cell in notebook['cells']:
    if cell['cell_type'] != 'code':
        continue
    stdout, stderr = io.StringIO(), io.StringIO()
    with patch.object(socket.socket, 'connect', side_effect=AssertionError('Network connection blocked')), patch.object(socket.socket, 'connect_ex', side_effect=AssertionError('Network connection blocked')), contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        exec(compile(''.join(cell['source']), 'trace-a-claim.ipynb', 'exec'), namespace)
    expected = {name: ''.join(''.join(o['text']) for o in cell['outputs'] if o['name'] == name) for name in ['stdout', 'stderr']}
    if stdout.getvalue() != expected['stdout'] or stderr.getvalue() != expected['stderr']:
        raise AssertionError('Executed example differs from saved plain-text output')
    results.append({'cell_id': cell['id'], 'saved_output_matches': True})
print(json.dumps({'worked_cells': results, 'network_connections': 'blocked', 'notebook_rewritten': False}))
'''
    try:
        result = subprocess.run([sys.executable, '-B', '-c', harness], cwd=path.parent,
                                capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return ['Worked notebook replay did not finish within 60 seconds']
    if result.returncode:
        return [result.stderr.strip() or result.stdout.strip() or 'Worked notebook replay failed']
    return []


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute-worked', action='store_true', help='Also replay the fictional cell; requires its recorded workflow dependencies')
    args = parser.parse_args()
    errors = check()
    if not errors and args.execute_worked:
        errors.extend(execute_worked())
    if errors:
        print('\n'.join(errors))
        return 1
    scope = 'structure, local links and limited output/publication checks'
    if args.execute_worked:
        scope += '; fictional cell output reproduced with socket connections blocked'
    print(f'Notebook checks passed for {len(NOTEBOOKS)} notebooks: {scope}. Source fidelity and reader comprehension were not assessed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
