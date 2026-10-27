#!/usr/bin/env python3
"""Validate and import a sourced editorial draft; never execute draft content."""
import argparse
import copy
import datetime as dt
import json
from pathlib import Path
import re
import tempfile
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
CATEGORIES={'模型','产品','价格','开源','研究','基础设施','产业','治理'}
def require(ok,message):
    if not ok:raise ValueError(message)
def safe_text(value,label,maximum):
    require(isinstance(value,str) and 0<len(value.strip())<=maximum,f'Invalid {label}')
    require(not any(c in value for c in ['\x00','\r']),f'Invalid control character in {label}')
    return value.strip()
def validate_draft(draft):
    issue=draft['issue'];date=dt.date.fromisoformat(issue['date']).isoformat()
    for key,limit in [('title',100),('dek',200),('coverage',180)]:safe_text(issue[key],key,limit)
    events=draft['events'];require(3<=len(events)<=12,'A reviewed issue requires 3–12 independent events')
    ids=set();urls=set()
    for e in events:
        require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e['id']) is not None,'Unsafe event ID')
        require(e['id'] not in ids,'Duplicate event ID');ids.add(e['id'])
        require(e['category'] in CATEGORIES,'Unknown category')
        for key,limit in [('title',120),('summary',350),('context',450),('status',80)]:safe_text(e[key],key,limit)
        body=e.get('body')
        require(isinstance(body,list) and 2<=len(body)<=4,'Need 2–4 narrative body paragraphs')
        for paragraph in body:safe_text(paragraph,'body paragraph',500)
        require(1<=len(e['facts'])<=4,'Need 1–4 sourced facts')
        for f in e['facts']:safe_text(f,'fact',250)
        require(1<=len(e['sources'])<=5,'Need original source links')
        for source in e['sources']:
            parsed=urlparse(source['url'])
            require(parsed.scheme=='https' and parsed.hostname and not parsed.username and not parsed.password,'Source must be a public HTTPS URL')
            require(parsed.hostname not in ['localhost','127.0.0.1'] and not re.match(r'^\d+\.\d+\.\d+\.\d+$',parsed.hostname),'Private/IP source is not allowed')
            safe_text(source['publisher'],'publisher',100)
        main=e['sources'][0]['url'];require(main not in urls,'Same primary source duplicated');urls.add(main)
        if e.get('published_at'):dt.date.fromisoformat(e['published_at'][:10])
        else:require('待确认' in e['status'],'Unknown date must be labelled')
    require(1<=len(issue['lead_ids'])<=3 and set(issue['lead_ids'])<=ids,'Lead IDs must belong to this issue')
    return date
def merge(content,draft,now):
    date=validate_draft(draft);out=copy.deepcopy(content)
    old_issue=next((i for i in out['issues'] if i['date']==date),None)
    old_events={e['id']:e for e in out['events']}
    for event in draft['events']:
        prior=old_events.get(event['id'])
        require(not prior or prior['issue_date']==date,'Existing event belongs to a different issue; link follow-up or choose a new ID')
        e=copy.deepcopy(event);e['issue_date']=date
        e['discovered_at']=prior['discovered_at'] if prior else now
        e['verified_at']=e.get('verified_at',now)
        if prior and prior.get('editorial_updated_at'):e.setdefault('editorial_updated_at',prior['editorial_updated_at'])
        e.setdefault('published_at',None);e.setdefault('visual','grid');e.setdefault('tags',[e['category']])
        e.setdefault('corrections',prior.get('corrections',[]) if prior else [])
        e.setdefault('publication_precision','date' if e['published_at'] else 'unknown')
        for s in e['sources']:
            old_source=next((x for x in prior['sources'] if x['url']==s['url']),{}) if prior else {}
            s.setdefault('accessed_at',old_source.get('accessed_at',now));s.setdefault('published_at',e['published_at']);s.setdefault('title',e['title'])
        if prior and {k:v for k,v in e.items() if k not in ['verified_at','corrections']} != {k:v for k,v in prior.items() if k not in ['verified_at','corrections']}:
            require(bool(e['corrections']) and e['corrections']!=prior.get('corrections',[]),'Changing an existing event requires a new correction record')
        for correction in e['corrections']:
            dt.datetime.fromisoformat(correction['at']);safe_text(correction['note'],'correction note',300)
        old_events[e['id']]=e
    ids=[e['id'] for e in draft['events']]
    if old_issue:require(ids==old_issue['event_ids'],'Same-day corrections must preserve the published event set')
    issue=copy.deepcopy(draft['issue']);issue['event_ids']=ids
    issue['number']=old_issue['number'] if old_issue else f'{max((int(i["number"]) for i in out["issues"]),default=0)+1:03d}'
    issue['published_at']=old_issue['published_at'] if old_issue else now
    issue['updated_at']=now;issue['kind']=old_issue.get('kind','每日精选') if old_issue else '每日精选'
    issue['metric_snapshot']=old_issue.get('metric_snapshot') if old_issue else f'data/issues/{date}.json'
    out['events']=list(old_events.values());out['issues']=[i for i in out['issues'] if i['date']!=date]+[issue]
    out['updated_at']=now
    return out,issue
def atomic_json(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile('w',dir=path.parent,delete=False,encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n');tmp=Path(f.name)
    tmp.replace(path)
def main():
    p=argparse.ArgumentParser();p.add_argument('--draft',required=True);p.add_argument('--check-only',action='store_true');args=p.parse_args()
    now=dt.datetime.now(dt.timezone.utc).isoformat()
    content=json.loads((ROOT/'content/edition.json').read_text());draft=json.loads(Path(args.draft).read_text())
    out,issue=merge(content,draft,now)
    if not args.check_only:
        metrics=ROOT/issue['metric_snapshot'] if issue['metric_snapshot'] else None
        if metrics and not metrics.exists():atomic_json(metrics,{'issue_date':issue['date'],'saved_at':now,'snapshot':json.loads((ROOT/'data/snapshot.json').read_text()),'usage':json.loads((ROOT/'data/usage.json').read_text())})
        atomic_json(ROOT/'content/edition.json',out)
    print(json.dumps({'date':issue['date'],'number':issue['number'],'events':len(issue['event_ids']),'check_only':args.check_only},ensure_ascii=False))
if __name__=='__main__':main()
