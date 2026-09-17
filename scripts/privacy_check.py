#!/usr/bin/env python3
"""Reject raw/private files in staged paths or any reachable Git history."""
import argparse,subprocess,sys
from pathlib import PurePosixPath
p=argparse.ArgumentParser();p.add_argument('--staged',action='store_true');a=p.parse_args()
def git(*args):return subprocess.check_output(['git',*args]).decode()
def forbidden(path):
    p=PurePosixPath(path)
    return ('private' in p.parts or p.suffix.lower() in {'.pdf','.zip','.png','.jpg','.jpeg','.mp3','.mp4','.wav','.srt','.vtt'} or p.name.startswith('.env') or p.name in {'prior-conversation.json','day1-conversation.json'})
paths=git('diff','--cached','--name-only','-z').split('\0') if a.staged else git('ls-files','-z').split('\0')
if not a.staged:
    r=subprocess.run(['git','rev-list','--objects','--all'],capture_output=True,text=True)
    paths += [line.split(' ',1)[1] for line in r.stdout.splitlines() if ' ' in line]
bad=sorted(set(x for x in paths if x and forbidden(x)))
if bad:print('Forbidden private/raw paths:\n'+'\n'.join(bad));sys.exit(1)
print('Privacy path/history check passed; review authored text for confidential content before sharing.')
