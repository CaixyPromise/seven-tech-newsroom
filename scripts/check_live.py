#!/usr/bin/env python3
"""Check deployed edition, batch, commit and feed; GET only, no callback."""
import argparse
import datetime as dt
import json
from pathlib import Path
import time
from urllib.parse import urlparse
import urllib.request
import uuid
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
def get(base,path):
    req=urllib.request.Request(base.rstrip('/')+'/'+path+'?check='+uuid.uuid4().hex,headers={'User-Agent':'Seven-Tech-Newsroom-Health/1.0','Cache-Control':'no-cache'})
    with urllib.request.urlopen(req,timeout=20) as r:return r.read().decode('utf-8')
def inspect(base,expected_date=None,expected_batch=None,expected_commit=None):
    status=json.loads(get(base,'status.json'))
    if expected_date and status['latest_issue_date']!=expected_date:raise ValueError(f'Edition stale: expected {expected_date}, got {status["latest_issue_date"]}')
    if expected_batch and status['batch_id']!=expected_batch:raise ValueError('Deployed content batch does not match the expected batch')
    if expected_commit and status.get('commit_sha')!=expected_commit:raise ValueError('Deployed commit does not match the expected revision')
    homepage=get(base,'index.html');date=status['latest_issue_date']
    if status['batch_id'] not in homepage or 'Seven Tech Newsroom' not in homepage:raise ValueError('Homepage branding/batch mismatch')
    issue=get(base,f'daily/{date}/index.html')
    if status['batch_id'] not in issue:raise ValueError('Daily page batch mismatch')
    feed=ET.fromstring(get(base,'feed.xml'));items=feed.findall('./channel/item')
    if not any(i.findtext('guid')=='urn:ai-rizhi:daily:'+date for i in items):raise ValueError('RSS is missing the latest issue GUID')
    if not any(i.findtext('link')==base.rstrip('/')+f'/daily/{date}/index.html' for i in items):raise ValueError('RSS link does not match the deployed base URL')
    site=json.loads((ROOT/'config/site.json').read_text())
    if site['author_url'] not in homepage or site['repository_url'] not in homepage:raise ValueError('Footer author/repository link missing')
    return status
def main():
    p=argparse.ArgumentParser();p.add_argument('--base-url');p.add_argument('--date');p.add_argument('--batch');p.add_argument('--commit');p.add_argument('--today',action='store_true');p.add_argument('--retries',type=int,default=1);p.add_argument('--delay',type=int,default=5);a=p.parse_args()
    site=json.loads((ROOT/'config/site.json').read_text());base=a.base_url or site['site_url']
    expected=dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date().isoformat() if a.today else a.date
    for attempt in range(max(1,a.retries)):
        try:
            status=inspect(base,expected,a.batch,a.commit)
            print(json.dumps({'result':'PASS',**status},ensure_ascii=False,indent=2));return
        except Exception as exc:
            print(f'Check {attempt+1}: {type(exc).__name__}: {exc}',flush=True)
            if attempt+1>=a.retries:raise SystemExit(1)
            time.sleep(min(a.delay,30))
if __name__=='__main__':main()
