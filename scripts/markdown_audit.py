#!/usr/bin/env python3
"""Inventory Markdown and flag selected maintenance patterns; no truth/rights verdict."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

PATTERNS = {
    "legacy_writing_label": r"\bE5\b",
    "private_only_language": r"repository remains private|this private repository|keep (?:the )?repository private|private-only",
    "open_case_language": r"geography remains (?:open|unselected)|six open candidates|no case selected|case selection remains open|six candidates remain",
    "authorization_language": r"preparation.only|do not draft|does not.*permit.*draft|no submission recorded",
    "named_ai_or_tool": r"\b(?:ChatGPT|Codex|Perplexity|SciSpace|Claude|Jev|Translator|Otter)\b",
    "version_or_check_count": r"\bv0\.\d|\b\d+ (?:unit )?tests|\b\d+ .*Markdown.*(?:links|targets)",
}

def scan(root):
    root = Path(root).resolve()
    raw = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=root
    ).decode("utf-8")
    names = sorted({n for n in raw.split("\0") if n and Path(n).suffix.lower() == ".md"})
    result = []
    for name in names:
        path = root / name
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError("Unsafe Markdown path: " + name)
        if not path.is_file():
            result.append({"path": name, "access": "missing_tracked_file", "sha256": None, "hits": []})
            continue
        data = path.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError("Unreadable UTF-8 Markdown: " + name) from exc
        hits = []
        for line, value in enumerate(text.splitlines(), 1):
            kinds = [key for key, pattern in PATTERNS.items() if re.search(pattern, value, re.I)]
            if kinds:
                hits.append({"line": line, "flags": kinds})
        result.append({"path": name, "access": "readable_utf8", "bytes": len(data),
                       "lines": len(text.splitlines()), "sha256": hashlib.sha256(data).hexdigest(),
                       "hits": hits})
    return {"schema_version": 1, "scope": "tracked and non-ignored Markdown paths in this working tree",
            "classification": "candidate maintenance flags, not errors or source-verification results",
            "file_count": len(result), "flagged_file_count": sum(bool(r["hits"]) for r in result),
            "patterns": PATTERNS, "files": result}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(scan(args.root), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
