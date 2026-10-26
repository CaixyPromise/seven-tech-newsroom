#!/usr/bin/env python3
"""Bounded public-content scan, excluding ignored local evidence and build cache."""
import argparse
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser();p.add_argument('--dist',action='store_true');a=p.parse_args()
    if a.dist:paths=[f for f in (ROOT/'dist').rglob('*') if f.is_file()]
    elif (ROOT/'.git').exists():
        result=subprocess.run(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=ROOT,check=True,capture_output=True)
        paths=[ROOT/s for s in result.stdout.decode().split('\x00') if s]
    else:
        paths=[f for f in ROOT.rglob('*') if f.is_file() and not set(f.relative_to(ROOT).parts)&{'dist','output','__pycache__','.git'} and f.name not in ['REVIEW.md','build-manifest.json']]
    patterns=[('private local path',re.compile(r'/(?:Users|home)/[A-Za-z0-9_.-]+/')),
              ('GitHub credential',re.compile(r'(?:gh[opusr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{35,})')),
              ('private key',re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----'))]
    if a.dist:patterns+=[('local preview URL',re.compile(r'https?://(?:localhost|127\.0\.0\.1)(?::\d+)?'))]
    failures=[]
    for path in paths:
        try:text=path.read_text()
        except (UnicodeDecodeError,OSError):continue
        for name,pattern in patterns:
            if pattern.search(text):failures.append(f'{path.relative_to(ROOT)}: {name}')
    if failures:raise SystemExit('\n'.join(failures))
    print(f'PASS: scanned {len(paths)} public files; no private paths, credential patterns'+(' or local preview URLs.' if a.dist else '.'))
if __name__=='__main__':main()
