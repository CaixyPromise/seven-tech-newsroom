#!/usr/bin/env python3
"""Read-only public metadata collection. No credentials or model calls required."""
import concurrent.futures
import datetime as dt
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
REPOS = ['huggingface/transformers','ggml-org/llama.cpp','ollama/ollama',
         'vllm-project/vllm','langchain-ai/langchain','open-webui/open-webui']
ENDPOINTS = {f'github:{r}': f'https://api.github.com/repos/{r}' for r in REPOS}
ENDPOINTS.update({
 'hf:text-generation': 'https://huggingface.co/api/models?pipeline_tag=text-generation&sort=downloads&direction=-1&limit=6',
 'hf:feature-extraction': 'https://huggingface.co/api/models?pipeline_tag=feature-extraction&sort=downloads&direction=-1&limit=6',
 'openrouter:models': 'https://openrouter.ai/api/v1/models',
})

def fetch(pair):
    key, url = pair
    at = dt.datetime.now(dt.timezone.utc).isoformat()
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Seven-Tech-Newsroom/1.0','Accept':'application/json'})
        with urllib.request.urlopen(req, timeout=25) as resp:
            body = resp.read(12_000_000)
            status = resp.status
        return key, {'source_url':url,'observed_at':at,'http_status':status,
                     'response_sha256':hashlib.sha256(body).hexdigest()}, json.loads(body)
    except Exception as exc:
        return key, {'source_url':url,'observed_at':at,'error_type':type(exc).__name__}, None

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, ENDPOINTS.items()))
    snapshot = {'schema_version':1,'collected_at':dt.datetime.now(dt.timezone.utc).isoformat(),
      'github':[], 'huggingface':{}, 'prices':[], 'sources':[],
      'history_available':False, 'scope':'First public metadata observation; not historical daily snapshots.'}
    for key, meta, data in results:
        snapshot['sources'].append({'id':key,**meta})
        if data is None: continue
        if key.startswith('github:'):
            snapshot['github'].append({'id':data['full_name'],'name':data['name'],
                'url':data['html_url'],'stars':data['stargazers_count'],'forks':data['forks_count'],
                'description':data.get('description'),'observed_at':meta['observed_at'],
                'source_url':meta['source_url'],'daily_delta':None})
        elif key.startswith('hf:'):
            snapshot['huggingface'][key.split(':',1)[1]]=[{
                'id':row['id'],'downloads_30d':row.get('downloads'),'likes':row.get('likes'),
                'task':row.get('pipeline_tag'),'url':'https://huggingface.co/'+row['id'],
                'observed_at':meta['observed_at']} for row in data]
        else:
            models=data.get('data',[])
            wanted=['moonshotai/kimi-k3.1-pro','minimax/minimax-m3.1-flash',
                    'deepseek/deepseek-v4.1-flash-1017','anthropic/claude-sonnet-5.5',
                    'anthropic/claude-haiku-5.5','openai/gpt-6-luna',
                    'google/gemini-4-argon','qwen/qwen3.8-max']
            for mid in wanted:
                row=next((m for m in models if m['id']==mid),None)
                if row is None: continue
                p=row.get('pricing',{})
                if p.get('prompt') is None or p.get('completion') is None: continue
                ip,op=float(p['prompt'])*1e6,float(p['completion'])*1e6
                snapshot['prices'].append({'id':row['id'],'canonical_slug':row.get('canonical_slug'),
                    'name':row['name'],'input_per_million':ip,'output_per_million':op,
                    'context_tokens':row.get('context_length'),'currency':'USD',
                    'fixed_text_cost':round(ip*.01+op*.002,8),
                    'url':'https://openrouter.ai/'+row['id'],'observed_at':meta['observed_at'],
                    'source_url':meta['source_url'],'scope':'OpenRouter listed route base token price'})
            snapshot['price_catalog_model_count']=len(models)
    snapshot['github'].sort(key=lambda r:r['stars'],reverse=True)
    path=ROOT/'data'/'snapshot.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    failed=[key for key,meta,data in results if data is None]
    if failed or len(snapshot['github'])!=len(REPOS) or len(snapshot['huggingface'])!=2 or not snapshot['prices']:
        raise SystemExit('Collection incomplete; previous snapshot retained. Failed groups: '+', '.join(failed))
    # Preserve an existing observation rather than overwriting the evidence baseline.
    if path.exists():
        history=ROOT/'data'/'observations'
        history.mkdir(exist_ok=True)
        old=json.loads(path.read_text())
        stamp=old['collected_at'].replace(':','').replace('+','_')
        (history/f'{stamp}.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
    temporary=path.with_suffix('.tmp')
    temporary.write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n')
    temporary.replace(path)
    print(json.dumps({'github':len(snapshot['github']),'hf_groups':list(snapshot['huggingface']),
        'prices':len(snapshot['prices']),'model_ids':[p['id'] for p in snapshot['prices']],
        'sources':[{'id':x['id'],'status':x.get('http_status',x.get('error_type'))} for x in snapshot['sources']]},ensure_ascii=False,indent=2))
    if not snapshot['github'] or not snapshot['prices'] or not snapshot['huggingface']:
        raise SystemExit('Required source group unavailable; inspect snapshot before publishing.')

if __name__=='__main__': main()
