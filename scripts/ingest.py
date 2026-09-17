#!/usr/bin/env python3
"""Archive a source without modifying its original; registration is explicit."""
import argparse,hashlib,json,re,shutil
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('--id',required=True);a=p.parse_args()
if not re.fullmatch(r'[A-Za-z0-9_-]+',a.id):raise SystemExit('Use a simple source ID.')
if not a.source.is_file():raise SystemExit('Source file is missing.')
dest=root/'private/intake'/a.id/a.source.name
dest.parent.mkdir(parents=True,exist_ok=True)
if dest.exists():raise SystemExit('Source already archived; use a versioned ID.')
shutil.copy2(a.source,dest)
print(json.dumps({'id':a.id,'private_path':str(dest.relative_to(root)),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'status':'awaiting_registry_and_content_review'},indent=2))
