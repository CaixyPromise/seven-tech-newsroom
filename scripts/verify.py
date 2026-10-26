#!/usr/bin/env python3
"""Focused static content, routing, provenance and feed acceptance checks."""
from collections import Counter
from html.parser import HTMLParser
import datetime as dt
from email.utils import parsedate_to_datetime
import re
import hashlib
import importlib.util
import json
from pathlib import Path
import posixpath
import urllib.parse
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
errors=[];counts=Counter()
def check(ok,msg):
    counts['assertions']+=1
    if not ok:errors.append(msg)
class Page(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.refs=[];self.meta={};self.lang=None;self.h1=0;self.title=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id'in a:self.ids.append(a['id'])
        if tag=='html':self.lang=a.get('lang')
        if tag=='h1':self.h1+=1
        if tag=='title':self.title=True
        if tag=='meta':self.meta[a.get('name')]=a.get('content')
        for key in ['href','src']:
            if key in a:self.refs.append(a[key])
        if tag=='img':check(bool(a.get('alt')),f'Missing image alt: {a}')
pages={}
for path in OUT.rglob('*.html'):
    parser=Page();parser.feed(path.read_text());pages[path.relative_to(OUT).as_posix()]=parser
    check(parser.lang=='zh-CN',f'Language: {path}')
    check(parser.h1==1,f'Expected 1 h1: {path}, got {parser.h1}')
    check(parser.title,f'Missing title: {path}')
    check(len(parser.ids)==len(set(parser.ids)),f'Duplicate IDs: {path}')
for key,p in pages.items():
    for raw in p.refs:
        parsed=urllib.parse.urlparse(raw)
        if parsed.scheme or raw.startswith('//'):continue
        rel=posixpath.normpath(posixpath.join(posixpath.dirname(key),urllib.parse.unquote(parsed.path))) if parsed.path else key
        path=OUT/rel
        check(path.exists(),f'Broken local reference in {key}: {raw}')
        if parsed.fragment and rel in pages:check(parsed.fragment in pages[rel].ids,f'Broken fragment in {key}: {raw}')
manifest=json.loads((ROOT/'build-manifest.json').read_text())
content=json.loads((ROOT/'content/edition.json').read_text())
snapshot=json.loads((ROOT/'data/snapshot.json').read_text())
usage=json.loads((ROOT/'data/usage.json').read_text())
for key,p in pages.items():check(p.meta.get('ai-daily-batch')==manifest['batch_id'],f'Batch mismatch: {key}')
site=json.loads((ROOT/'config/site.json').read_text())
issues=content['issues'];events=content['events'];event_map={e['id']:e for e in events}
check(bool(issues) and bool(events),'Need sourced issues and events')
check(len({i['date'] for i in issues})==len(issues),'Duplicate issue dates')
check(len({i['number'] for i in issues})==len(issues),'Duplicate issue numbers')
check(len(event_map)==len(events),'Duplicate event IDs')
referenced=[]
for issue in issues:
    dt.date.fromisoformat(issue['date']);dt.datetime.fromisoformat(issue['published_at'])
    check(bool(issue['event_ids']),'Empty issue')
    check(1<=len(issue['lead_ids'])<=3 and set(issue['lead_ids'])<=set(issue['event_ids']),'Invalid lead set')
    for key in issue['event_ids']:
        check(key in event_map and event_map[key]['issue_date']==issue['date'],'Event ownership mismatch: '+key)
        referenced.append(key)
    if issue.get('metric_snapshot'):
        path=ROOT/issue['metric_snapshot'];check(path.is_file(),'Missing frozen metrics')
        if path.is_file():
            saved=json.loads(path.read_text());check(saved['issue_date']==issue['date'],'Frozen metrics issue mismatch')
            check(bool(saved['snapshot']['sources']),'Frozen metrics lack provenance')
    else:check(issue.get('kind')=='回溯样刊','Daily edition needs an actual saved metrics snapshot')
check(len(referenced)==len(set(referenced))==len(events),'Orphaned or multiply owned events')
for e in events:
    check(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e['id']) is not None,'Unsafe event ID')
    check(bool(e['sources']) and bool(e['verified_at']),'Missing news provenance')
    for source in e['sources']:
        check(urllib.parse.urlparse(source['url']).scheme=='https','News source must use HTTPS')
        check(bool(source.get('accessed_at')),'News source missing access time')
check(all(e.get('daily_delta') is None or e.get('comparison_start') for e in snapshot['github']),'Unsubstantiated daily change')
check(all(r.get('http_status')==200 for r in snapshot['sources']),'Required source collection failed')
dt.date.fromisoformat(usage['source_as_of'])
check(bool(usage['collection_method']) and bool(usage['source_url']),'Usage provenance missing')
check(usage['license']=='CC BY 4.0','Missing usage attribution')
check(bool(snapshot['prices']) and bool(snapshot['github']) and bool(snapshot['huggingface']),'Missing metrics group')
for key in pages:
    text=(OUT/key).read_text();footer=text.split('<footer',1)[-1]
    check(site['name'] in text,'Missing product name: '+key)
    check(site['author_url'] in footer and site['repository_url'] in footer,'Footer attribution missing: '+key)
status=json.loads((OUT/'status.json').read_text())
check(status['batch_id']==manifest['batch_id'],'Status batch mismatch')
check(status['latest_issue_date']==max(i['date'] for i in issues),'Status edition mismatch')
rss=ET.parse(OUT/'feed.xml');items=rss.findall('./channel/item')
atom=ET.parse(OUT/'atom.xml');ns='{http://www.w3.org/2005/Atom}'
check(len(items)==len(issues),'RSS item count')
check(len(atom.findall(ns+'entry'))==len(issues),'Atom item count')
guids=[i.findtext('guid') for i in items];check(len(set(guids))==len(issues),'RSS duplicate GUIDs')
for item in items:
    link=item.findtext('link');check(link.startswith(manifest['base_url']+'/'),'RSS origin mismatch')
    target=link[len(manifest['base_url'])+1:];check((OUT/target).exists(),'RSS link missing: '+target)
    check('原始资料' in item.findtext('description'),'RSS source links missing')
    check(parsedate_to_datetime(item.findtext('pubDate')).tzinfo is not None,'RSS publication date missing')
for e in content['events']:
    root=ET.fromstring((OUT/'assets/visuals'/f'{e["id"]}.svg').read_text())
    check(root.tag.endswith('svg'),'Invalid news SVG')
    if e['published_at'] is None:check('待确认' in e['status'],'Unknown date unlabelled')
check(set(guids)=={'urn:ai-rizhi:daily:'+i['date'] for i in issues},'RSS identity mismatch')
print(f'Checked {len(pages)} pages, {len(events)} event SVGs, 2 feeds; {counts["assertions"]} assertions.')
if errors:
    print('\n'.join('FAIL: '+e for e in errors));raise SystemExit(1)
print('PASS: internal links, anchors, content provenance, batch IDs, RSS/Atom and metric scope.')
