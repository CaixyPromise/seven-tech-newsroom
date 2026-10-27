#!/usr/bin/env python3
"""Find source-page image candidates in one bounded batch; never auto-publish them."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import urllib.parse
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
class Images(HTMLParser):
    def __init__(self,base):super().__init__();self.base=base;self.rows=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);url=None;kind=None
        if tag=='meta' and a.get('property',a.get('name','')).lower() in ['og:image','og:image:url','twitter:image','twitter:image:src']:
            url=a.get('content');kind='social-preview'
        elif tag=='img':
            url=a.get('src') or a.get('data-src');kind='article-image'
        if not url:return
        url=urllib.parse.urljoin(self.base,url)
        if urllib.parse.urlparse(url).scheme!='https' or re.search(r'(?:logo|favicon|tracking|pixel|spacer)',url,re.I):return
        if any(x['image_url']==url for x in self.rows):return
        if len(self.rows)<8:self.rows.append({'image_url':url,'kind':kind,'alt':a.get('alt','')[:300]})

def fetch_source(source):
    url=source['url'];parsed=urllib.parse.urlparse(url)
    if parsed.scheme!='https' or not parsed.hostname or parsed.username or parsed.password:raise ValueError('HTTPS news source required')
    request=urllib.request.Request(url,headers={'User-Agent':'SevenTechNewsroom/1.0 (editorial image discovery)'})
    with urllib.request.urlopen(request,timeout=5) as response:
        if 'text/html' not in response.headers.get('Content-Type',''):return []
        data=response.read(1_500_001)
        if len(data)>1_500_000:raise ValueError('Source page exceeds discovery size limit')
        parser=Images(response.url);parser.feed(data.decode(response.headers.get_content_charset() or 'utf-8',errors='replace'))
    return parser.rows

def discover(event):
    result={'event_id':event['id'],'title':event['title'],'candidates':[],'errors':[]}
    for source in event['sources'][:1]:
        try:
            result['candidates'] += [dict(row,source_url=source['url'],publisher=source['publisher'],rights_status='needs-review') for row in fetch_source(source)]
        except Exception as error:result['errors'].append({'source_url':source['url'],'error':type(error).__name__})
    return result

def main():
    p=argparse.ArgumentParser();p.add_argument('--draft',required=True);p.add_argument('--out',default='work/image-candidates.json');args=p.parse_args()
    data=json.loads(Path(args.draft).read_text());events=data['events']
    if not 1<=len(events)<=20:raise SystemExit('Image batch accepts 1–20 stories.')
    # No downloading, hotlinking, image-model calls or remote commands. A failed
    # source only removes its candidates; the sourced SVG remains publishable.
    with ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(discover,events))
    output=ROOT/args.out
    if not output.resolve().is_relative_to((ROOT/'work').resolve()):raise SystemExit('Candidate output must stay in ignored work/.')
    output.parent.mkdir(exist_ok=True);output.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(f'Image discovery: {len(rows)} stories, {sum(len(r["candidates"]) for r in rows)} candidates; {sum(bool(r["errors"]) for r in rows)} source failures. Nothing auto-published.')
if __name__=='__main__':main()
