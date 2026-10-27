#!/usr/bin/env python3
"""Dependency-free static publisher for sourced editions and data snapshots."""
from __future__ import annotations
import argparse
import datetime as dt
from email.utils import format_datetime
import hashlib
import html
import json
import os
from pathlib import Path
import posixpath
import shutil
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
from news_graphics import render as illustration, graphic_alt, validate_graphic

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
E=lambda s: html.escape(str(s),quote=True)
TZ=dt.timezone(dt.timedelta(hours=8))
def script_json(obj): return json.dumps(obj,ensure_ascii=False).replace('<','\\u003c')
def load(p): return json.loads((ROOT/p).read_text())
def localtime(s): return dt.datetime.fromisoformat(s.replace('Z','+00:00')).astimezone(TZ).strftime('%Y-%m-%d %H:%M')
def compact(n):
    return f'{n/1e6:.2f}M' if n>=1e6 else f'{n/1e3:.1f}k' if n>=1e3 else str(n)
def money(n): return f'{n:.6f}'.rstrip('0').rstrip('.') if n else '0'
def news_paragraphs(event):
    return event['body']
def short_model(s): return s.split(': ',1)[-1]
def icon(name):
    shapes={
      'rss':'<path d="M5 4a15 15 0 0 1 15 15M5 10a9 9 0 0 1 9 9"/><circle cx="5" cy="19" r="1.4" fill="currentColor"/>',
      'search':'<circle cx="10" cy="10" r="6.5"/><path d="m15 15 5 5"/>',
      'arrow':'<path d="M4 12h15m-6-6 6 6-6 6"/>',
      'chart':'<path d="M5 19V9m7 10V4m7 15v-7"/>',
      'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
      'star':'<path d="m12 3 2.7 5.5 6 .9-4.3 4.2 1 6-5.4-2.9L6.6 20l1-6-4.3-4.2 6-.9z"/>',
      'price':'<path d="M18 6H9a4 4 0 0 0 0 8h6a4 4 0 0 1 0 8M12 2v20"/>',
    }
    return f'<svg class="icon" aria-hidden="true" viewBox="0 0 24 24">{shapes.get(name,shapes["arrow"])}</svg>'


class Publisher:
    def __init__(self,base):
        self.base=base.rstrip('/')
        self.site=load('config/site.json')
        self.is_local=urlparse(self.base).hostname in ['localhost','127.0.0.1','::1']
        self.content=load('content/edition.json');self.snapshot=load('data/snapshot.json');self.usage=load('data/usage.json')
        self.events={x['id']:x for x in self.content['events']}
        self.issues=sorted(self.content['issues'],key=lambda x:x['date'],reverse=True)
        self.latest=self.issues[0]
        assets={}
        for event in self.events.values():
            validate_graphic(event)
            if event.get('artwork'):assets[event['artwork']['path']]=hashlib.sha256((ROOT/event['artwork']['path']).read_bytes()).hexdigest()
        seed=json.dumps([self.content,self.snapshot,self.usage,self.site,assets],sort_keys=True,ensure_ascii=False).encode()
        self.batch=hashlib.sha256(seed).hexdigest()[:12]
        self.style_version=hashlib.sha256((ROOT/'src/style.css').read_bytes()).hexdigest()[:12]
        self.current='index.html'
    def url(self,target):
        if target.startswith(('http:','https:','#','mailto:')): return target
        return posixpath.relpath(target,posixpath.dirname(self.current) or '.')
    def link(self,destination,label,cls='',**attrs):
        extra=' '.join(f'{k.replace("_","-")}="{E(v)}"' for k,v in attrs.items())
        return f'<a href="{E(self.url(destination))}" class="{E(cls)}" {extra}>{label}</a>'
    def event_url(self,event):return f'news/{event["id"]}/index.html'
    def issue_url(self,issue):return f'daily/{issue["date"]}/index.html'
    def write(self,path,text):
        p=OUT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
    def source_meta(self,e):
        date=f'原文 {e["published_at"][5:].replace("-","/")}' if e['published_at'] else '原始发布日待确认'
        source=e['sources'][0]
        return f'<div class="meta"><span>{E(source["publisher"])}</span><span>·</span><span>{date}</span>{self.link(source["url"],"原文 ↗",rel="noopener noreferrer",target="_blank")}</div>'
    def document(self,title,body,active='',description='',article=None):
        nav=''.join(self.link(p,label,aria_current='page') if active==key else self.link(p,label) for key,p,label in [
            ('home','index.html','最新一期'),('data','data/index.html','数据观察'),('archive','archive/index.html','历史归档'),('about','about/index.html','关于')])
        canonical=self.base+'/'+self.current
        structured=''
        if article:
            obj={'@context':'https://schema.org','@type':'Article','headline':article['title'],'description':article['summary'],
                 'datePublished':article['discovered_at'],'dateModified':article['verified_at'],
                 'author':{'@type':'Organization','name':'Seven Tech Newsroom'},'citation':[s['url'] for s in article['sources']]}
            structured=f'<script type="application/ld+json">{script_json(obj)}</script>'
        return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
        <title>{E(title)} · Seven Tech Newsroom</title><meta name="description" content="{E(description or title)}"><meta name="color-scheme" content="light">
        <meta name="ai-daily-batch" content="{self.batch}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(description or title)}">
        <link rel="canonical" href="{E(canonical)}"><link rel="icon" href="{self.url('assets/favicon.svg')}" type="image/svg+xml">
        <link rel="alternate" type="application/rss+xml" title="Seven Tech Newsroom · 每日摘要" href="{self.url('feed.xml')}">
        <link rel="stylesheet" href="{self.url('assets/style.css')}?v={self.style_version}"><script defer src="{self.url('assets/app.js')}"></script>{structured}</head>
        <body><a class="skip" href="#main">跳到正文</a><div class="topline" id="top"></div><header class="site-header"><div class="container header-inner">
        {self.link('index.html','<span class="brand-mark">7</span><span>Seven<small>TECH NEWSROOM</small></span>','brand',aria_label='Seven Tech Newsroom首页')}
        <nav class="nav" aria-label="主要导航">{nav}</nav><div class="header-actions">
        {self.link('search/index.html',icon('search')+'<span>搜索</span>','search-link',aria_label='搜索新闻')}
        {self.link('subscribe/index.html',icon('rss')+'RSS 订阅','rss-btn')}</div></div></header>
        <main id="main" class="container">{body}</main>{self.footer()}</body></html>'''
    def footer(self):
        recent=''.join(self.link(self.issue_url(i),i['date']+' · 第 '+i['number']+' 期') for i in self.issues[:2])
        return f'''<footer class="site-footer"><div class="container"><div class="footer-grid">
        <div class="footer-brand">{self.link('index.html','<span class="brand-mark">7</span><span>Seven<small>TECH NEWSROOM</small></span>','brand',aria_label=self.site['name'])}<p>每天读一点，<br>看清 AI 与科技的变化。</p><span class="footer-edition">{len(self.issues)} 期归档 · {len(self.events)} 条有来源的新闻</span></div>
        <div class="footer-column"><h2>继续阅读</h2>{recent}{self.link('archive/index.html','全部期刊 →')}{self.link('search/index.html','搜索新闻')}</div>
        <div class="footer-column"><h2>数据观察</h2>{self.link('data/index.html#usage','平台模型用量')}{self.link('data/index.html#prices','模型价格与费用')}{self.link('data/index.html#opensource','开源项目关注')}{self.link('data/index.html#downloads','开放模型下载')}</div>
        <div class="footer-column"><h2>订阅与项目</h2>{self.link('subscribe/index.html',icon('rss')+'订阅每日摘要')}{self.link(self.site['repository_url'],'GitHub 仓库 ↗',rel='noopener noreferrer',target='_blank')}{self.link(self.site['author_url'],self.site['author']+' 的主页 ↗',rel='noopener noreferrer',target='_blank')}{self.link('about/index.html','来源与编辑规范')}{self.link('methodology/index.html','指标方法')}</div></div>
        <div class="footer-bottom"><span>© {dt.datetime.now(TZ).year} {E(self.site['name'])} · Created by {self.link(self.site['author_url'],E(self.site['author']))} · 数据按各自截至时间展示。</span><div>{self.link(self.site['repository_url'],'源码仓库 ↗')}{self.link('readme/index.html','README 日报')}{self.link('#top','回到顶部 ↑')}</div></div></div></footer>'''

    def page(self,path,title,fn,active='',description='',article=None):
        self.current=path
        self.write(path,self.document(title,fn(),active,description,article))
    def news_row(self,e,index,search=False):
        searchtext=' '.join([e['title'],e['summary'],e['category'],*e['tags']]).lower()
        attrs=f'data-category="{E(e["category"])}"'+(f' data-search="{E(searchtext)}"' if search else '')
        return f'''<article class="news-row" {attrs}><span class="news-number">{index:02d}</span><div><span class="pill">{E(e['category'])}</span><span class="status-tag">{E(e['status'])}</span>
        <h3>{self.link(self.event_url(e),E(e['title']))}</h3><p>{E(e['summary'])}</p>{self.source_meta(e)}
        {('<div class="meta" style="margin-top:8px">收录于 '+self.link('daily/'+e['issue_date']+'/index.html',e['issue_date'])+'</div>') if search else ''}</div>{self.link(self.event_url(e),self.image_markup(e),"news-thumbnail",aria_label=e["title"])}</article>'''
    def metric_cards(self):
        s=self.snapshot;u=self.usage
        minp=min(s['prices'],key=lambda p:p['fixed_text_cost'])
        top=u['rows'][0];repo=s['github'][0];hf=s['huggingface']['text-generation'][0]
        vals=[('文本基本费估算','$'+money(minp['fixed_text_cost']),short_model(minp['name'])+' · 10K 入 / 2K 出','price',False),
              ('平台单日用量领先',top['name'],f'约 {top["tokens_trillion"]}T Token · UTC {u["source_as_of"][5:].replace("-","/")}','chart',True),
              ('开源项目关注',compact(repo['stars']),repo['name']+' · 跟踪池 Stars 总数','star',False),
              ('文本模型下载观察',compact(hf['downloads_30d']),hf['id'].split('/')[-1]+' · 近 30 日','chart',False)]
        cards=''
        for label,value,note,ico,name in vals:
            cards+=self.link('data/index.html',f'<span class="metric-label">{label}{icon(ico)}</span><strong class="metric-value {"name" if name else ""}">{E(value)}</strong><span class="metric-note">{E(note)}</span>','metric-card')
        return '<div class="metric-grid">'+cards+'</div>'
    def bar_chart(self,rows,field,name,unit='',id='',model_attrs=False):
        maximum=max(r[field] for r in rows) if rows else 0
        bars=''
        for r in rows:
            value=r[field];label=('$'+money(value)) if unit=='money' else compact(value) if unit=='count' else f'{value:g}T'
            key=f' data-model="{E(r["id"])}"' if model_attrs else ''
            bars+=f'<div class="bar-row"{key}><span class="bar-name">{E(r[name])}</span><div class="bar-track" aria-hidden="true"><div class="bar-fill" style="width:{value/maximum*100 if maximum else 0:.3f}%"></div></div><span class="bar-value">{label}</span></div>'
        identity=f' id="{E(id)}"' if id else ''
        return f'<div class="chart-rows"{identity} role="group" aria-label="数据条形图">{bars}</div>'
    def usage_panel(self,limit=5):
        rows=self.usage['rows'][:limit]
        return f'''<h3>大家在用什么模型？</h3><p class="subtext">OpenRouter 单日用量 · {self.usage["source_as_of"]} UTC</p>
        {self.bar_chart(rows,'tokens_trillion','name')}
        <p class="chart-source">1T = 1 万亿 Token，数值经来源四舍五入。仅包含 OpenRouter 平台公开流量。</p>
        {self.link('data/index.html#usage','查看完整榜单与数据表 →','panel-link')}'''
    def issue_intro(self,issue,home):
        opts=''.join(f'<option value="{E(self.url(self.issue_url(i)))}" {"selected" if i["date"]==issue["date"] else ""}>{i["date"]} · 第 {i["number"]} 期</option>' for i in self.issues)
        retrospective=issue.get('kind')=='回溯样刊'
        label='回溯样刊' if retrospective else '每日精选'
        note=f'收录范围：{issue["coverage"]}。整理于 {localtime(issue["published_at"])} UTC+8。'
        return f'''<div class="issue-intro"><div><div class="eyebrow"><span class="dot"></span>{issue['date'].replace('-','.')} <span>/</span> DAILY BRIEF · NO.{issue['number']}</div><h1>{E(issue['title'])}</h1><p class="dek">{E(issue['dek'])}</p></div><div class="edition-control"><label class="small muted" for="edition-select">切换期刊</label><select id="edition-select">{opts}</select></div></div><div class="retrospective"><span class="label">{label}</span><span>{E(note)}</span></div>'''

    def home(self,issue=None):
        issue=issue or self.latest
        lead=[self.events[k] for k in issue['lead_ids']];e=lead[0]
        featured=f'''<div class="lead-grid"><article class="hero-story"><div class="hero-copy"><span class="pill">本期头条 · {E(e['category'])}</span>
        <h2>{self.link(self.event_url(e),E(e['title']))}</h2><p class="hero-summary">{E(e['summary'])}</p>{self.source_meta(e)}</div>
        <a class="hero-art" href="{self.url(self.event_url(e))}" aria-label="阅读：{E(e['title'])}">{self.image_markup(e,lazy=False)}</a></article>
        <div class="lead-side">'''
        briefs={'oracle-deep-trust':'安全与业务规则，进入软件、数据与执行层。',
                'nanbeige-43':'33B 教师模型，权重可得；性能为团队自报。',
                'olmoearth-13':'全球预计算卫星嵌入，配套浏览器地图工具。',
                'copilot-teams':'从问题通知发起代码任务，再由团队审查 PR。'}
        for n in lead[1:]: featured+=f'<article class="side-story">{self.link(self.event_url(n),self.image_markup(n,"side-story-image"),"side-story-art",aria_label=n["title"])}<span class="pill">{E(n["category"])}</span><h3>{self.link(self.event_url(n),E(n["title"]))}</h3><p>{E(briefs.get(n["id"],n["summary"]))}</p>{self.source_meta(n)}</article>'
        featured+='</div></div>'
        ishome=self.current=='index.html'
        if ishome:
            stats=f'<div class="section-head"><h2>数据速览</h2><span class="small">观测 {localtime(self.snapshot["collected_at"])} UTC+8</span></div>'+self.metric_cards()
        elif issue.get('metric_snapshot'):
            stats=f'<div class="section-head"><h2>本期数据快照</h2><span class="small">观测 {localtime(self.snapshot["collected_at"])} UTC+8</span></div>'+self.metric_cards()+self.link('downloads/data/'+issue['date']+'.json','下载本期原始指标 JSON →','panel-link')
        else:
            stats=f'<div class="scope-note" style="margin-top:24px"><p>本期没有当日指标快照。当前数据另列采集时间，供独立查看。</p>{self.link("data/index.html","查看最新数据 →")}</div>'
        cats=['全部']+list(dict.fromkeys(self.events[k]['category'] for k in issue['event_ids']))
        buttons=''.join(f'<button class="filter-btn" type="button" data-filter="{cat}" aria-pressed="{str(i==0).lower()}">{cat}</button>' for i,cat in enumerate(cats))
        rows=''.join(self.news_row(self.events[k],i+1) for i,k in enumerate(issue['event_ids']))
        prior=next((i for i in self.issues if i['date']<issue['date']),None)
        continuation=''
        if prior:
            previous_rows=''.join(self.news_row(self.events[k],j+1) for j,k in enumerate(prior['event_ids']))
            continuation=f'''<div class="edition-end"><p>本期 {len(issue['event_ids'])} 条已读完，上一期还有 {len(prior['event_ids'])} 条。</p><button type="button" class="continue-button" id="load-previous" data-edition-label="{prior['date']} · 第 {prior['number']} 期" data-edition-count="{len(prior['event_ids'])}" aria-expanded="false" aria-controls="previous-issue">继续阅读 {prior["date"]} · 第 {prior["number"]} 期 {icon('arrow')}</button><span id="continuation-status" role="status" class="small muted"></span></div><section id="previous-issue" class="previous-edition" hidden><div class="previous-edition-heading"><div class="eyebrow">{prior['date']} / NO.{prior['number']}</div><h2>{E(prior['title'])}</h2><p>{E(prior['dek'])}</p>{self.link(self.issue_url(prior),'打开完整期刊 →','panel-link')}</div><div class="news-list">{previous_rows}</div><p class="all-read">已到当前展开期刊的末尾。{self.link('subscribe/index.html','订阅下一期 →')}</p></section>'''
        else:
            continuation=f'<div class="edition-end"><p>已读到当前最早一期。</p>{self.link(self.issue_url(self.latest),"阅读最新一期 →","continue-button")}</div>'
        sidebar=f'<aside class="sidebar"><section class="panel">{self.usage_panel()}</section><section class="panel"><h3>往期也值得一读</h3>'
        for i in self.issues[:7]:
            sidebar+=f'<article class="issue-mini"><time>{i["date"]} / NO.{i["number"]}</time><h4>{self.link(self.issue_url(i),E(i["title"]))}</h4><p>{len(i["event_ids"])} 条精选 · {E(i.get("kind","每日精选"))}</p></article>'
        sidebar+=f'''{self.link('archive/index.html','浏览历史归档 →','panel-link')}</section><section class="panel subscribe-panel"><h3>把每天的重点带走</h3><p>订阅每日摘要，在你习惯的阅读器中查看新一期。</p>{self.link('subscribe/index.html',icon('rss')+'获取 RSS 地址','primary-link')}</section></aside>'''
        return self.issue_intro(issue,ishome)+featured+stats+f'''<div class="content-grid"><section class="news-panel" aria-labelledby="news-heading"><div class="section-head"><h2 id="news-heading">本期精选</h2><span class="small" id="filter-count" aria-live="polite">全部 · {len(issue['event_ids'])} 条</span></div><div class="filterbar" aria-label="筛选新闻分类">{buttons}</div><div class="news-list" id="edition-news">{rows}</div>{continuation}</section>{sidebar}</div>
        <div class="bottom-band"><div><h3>有来源，也有来龙去脉。</h3><p>阅读原始材料，查看数据口径，沿着归档追踪变化。</p></div>{self.link('methodology/index.html','了解指标方法 '+icon('arrow'),'primary-link')}</div>'''
    def issue_page(self,issue):
        if not issue.get('metric_snapshot'):return self.home(issue)
        saved=load(issue['metric_snapshot']);snapshot,usage=self.snapshot,self.usage
        try:
            self.snapshot,self.usage=saved['snapshot'],saved['usage']
            return self.home(issue)
        finally:self.snapshot,self.usage=snapshot,usage
    def visual_alt(self,e):return e['artwork']['alt'] if e.get('artwork') else graphic_alt(e)
    def visual_path(self,e):
        return 'assets/editorial/'+Path(e['artwork']['path']).name if e.get('artwork') else 'assets/visuals/'+e['id']+'.svg'
    def image_markup(self,e,css='',lazy=True):
        dimensions=e.get('artwork') or {'width':1200,'height':760}
        return f'<img class="{css} {"editorial-image" if e.get("artwork") else "infographic"}" src="{self.url(self.visual_path(e))}" width="{dimensions.get("width",1200)}" height="{dimensions.get("height",760)}" alt="{E(self.visual_alt(e))}" loading="{"lazy" if lazy else "eager"}" decoding="async">'
    def top(self,small,title,description):
        return f'<div class="page-top"><div class="eyebrow"><span class="dot"></span>{small}</div><h1>{E(title)}</h1><p>{E(description)}</p></div>'
    def table(self,heads,rows):
        return '<div class="table-wrap"><table class="data-table"><thead><tr>'+''.join(f'<th scope="col">{E(h)}</th>' for h in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{c}</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table></div>'
    def data(self):
        s,u=self.snapshot,self.usage
        prices=[{**p,'short_name':short_model(p['name'])} for p in sorted(s['prices'],key=lambda x:x['fixed_text_cost'])]
        jsdata=lambda id,obj:f'<script type="application/json" id="{id}">{script_json(obj)}</script>'
        top=self.top('THE NUMBERS','少一点印象，多一点数据。','模型成本、平台用量、开源关注和下载观察，各自保留范围与时间。')
        top+=f'<div class="scope-note"><p>本次观测：{localtime(s["collected_at"])} UTC+8。价格、Stars 和下载量为当前快照；统计范围分别标注。</p>{self.link("methodology/index.html","查看完整口径 →")}</div>'
        usage=f'<section class="panel" id="usage"><h2>OpenRouter 平台单日用量</h2><p class="subtext">{u["source_as_of"]} 00:00—24:00 UTC · 约数 · 1T = 1 万亿 Token</p>{self.bar_chart(u["rows"],"tokens_trillion","name")}'
        usage+=f'<p class="chart-source">{self.link(u["source_url"],"来源：OpenRouter Rankings ↗")} · 页面日榜，采集于 {localtime(u["observed_at"])} UTC+8。CC BY 4.0。Token 口径，不代表用户数或全行业份额。</p>'
        usage+='<details class="details-table"><summary>查看榜单数据表</summary>'+self.table(['模型','Token 用量','较前日变化'],[[E(r['name']),f'约 {r["tokens_trillion"]:g}T',E(r['change_label'])] for r in u['rows']])+'</details></section>'
        price=f'<section class="panel" id="prices"><h2>同样的 Token，基本费多少？</h2><p class="subtext">{len(s["prices"])} 个模型的 OpenRouter 标示路由价格 · USD</p><div class="chart-tabs" role="group" aria-label="价格指标">'
        for i,(key,label) in enumerate([('fixed_text_cost','固定用量'),('input_per_million','输入单价'),('output_per_million','输出单价')]):
            price+=f'<button type="button" class="chart-tab" data-price-field="{key}" aria-pressed="{str(i==0).lower()}">{label}</button>'
        price+='</div><p class="chart-unit" id="price-unit">USD / 10K 输入 + 2K 输出</p>'+self.bar_chart(prices,'fixed_text_cost','short_name','money','price-chart',True)
        price+=f'<p class="chart-source">{self.link("https://openrouter.ai/api/v1/models","来源：OpenRouter 模型目录 ↗")} · 观测 {localtime(s["sources"][-1]["observed_at"])} UTC+8。只比较标示基本文本单价，不表示能力相同。</p>'
        price+='<details class="details-table"><summary>查看输入／输出原始单价</summary>'+self.table(['模型','输入 $/M','输出 $/M','上下文 Token'],[[E(short_model(p['name'])),money(p['input_per_million']),money(p['output_per_million']),f'{p["context_tokens"]:,}'] for p in prices])+'</details></section>'
        gh=f'<section class="panel" id="opensource"><h2>开源项目关注</h2><p class="subtext">本站固定跟踪的 {len(s["github"])} 个项目 · Stars 总数，非全站排行</p>'
        gh+=self.bar_chart(s['github'],'stars','name','count')
        gh+=f'<p class="chart-source">来源：{self.link("https://docs.github.com/en/rest/repos/repos#get-a-repository","GitHub Repository API ↗")} · 观测 {localtime(s["github"][0]["observed_at"])} UTC+8。</p><p class="notice-inline">Stars 展示跟踪池总数，历史观测按实际采集时间归档。</p>'
        gh+='<details class="details-table"><summary>查看完整项目与精确数量</summary>'+self.table(['项目','Stars','Forks'],[[self.link(r['url'],E(r['id'])),f'{r["stars"]:,}',f'{r["forks"]:,}'] for r in s['github']])+'</details></section>'
        hf='<section class="panel" id="downloads"><h2>开放模型下载观察</h2><p class="subtext">按任务分类的近 30 日下载量 · 每组取接口返回前 6 项</p><div class="chart-tabs" role="group" aria-label="下载榜任务分类">'
        for i,(key,label) in enumerate([('text-generation','文本生成'),('feature-extraction','特征提取 / 嵌入')]):
            hf+=f'<button type="button" class="chart-tab" data-hf-task="{key}" aria-pressed="{str(i==0).lower()}">{label}</button>'
        hf+='</div>'
        for i,(key,rows) in enumerate(s['huggingface'].items()):
            hf+=f'<div data-hf-group="{key}" {"hidden" if i else ""}>'+self.bar_chart(rows,'downloads_30d','id','count')
            hf+='<details class="details-table"><summary>查看下载量与 Likes 数据表</summary>'+self.table(['模型','近 30 日下载','Likes'],[[self.link(r['url'],E(r['id'])),f'{r["downloads_30d"]:,}',f'{r["likes"]:,}'] for r in rows])+'</details></div>'
        hf+=f'<p class="chart-source">{self.link("https://huggingface.co/docs/hub/models-download-stats","来源：Hugging Face Hub 与下载计数说明 ↗")} · 观测 {localtime(s["collected_at"])} UTC+8。下载量不是人数，也不是当天新增。</p></section>'
        calc='''<section class="panel full-panel" id="calculator"><h2>换成你的用量，算一算。</h2><p class="subtext">使用同一份价格快照，估算三款模型的基本文本 Token 费用。</p><noscript><p>交互计算需要 JavaScript。上方仍可查看固定用量及原始单价。</p></noscript><div class="calculator"><label for="input-tokens">输入 Token<input type="number" id="input-tokens" min="0" max="100000000" step="1" value="10000" inputmode="numeric"></label><label for="output-tokens">输出 Token<input type="number" id="output-tokens" min="0" max="100000000" step="1" value="2000" inputmode="numeric"></label><div class="calc-results" aria-live="polite">'''
        for p in [s['prices'][0],s['prices'][1],s['prices'][-1]]:
            calc+=f'<div class="calc-result"><span>{E(short_model(p["name"]))}</span><strong data-calc-model="{E(p["id"])}">${money(p["fixed_text_cost"])}</strong></div>'
        calc+='</div><p class="calculator-note" id="calc-note">仅估算基本文本 Token 费用。</p></div></section>'
        return top+'<div class="data-grid">'+usage+price+gh+hf+'</div>'+calc+jsdata('price-data',s['prices'])+jsdata('hf-data',s['huggingface'])
    def article(self,e):
        issue=next(i for i in self.issues if i['date']==e['issue_date'])
        sourcecards=''.join(f'<div class="source-card">{self.link(s["url"],E(s["publisher"])+" · 阅读原始资料 ↗",target="_blank",rel="noopener noreferrer")}<p>{E(s["url"])}</p><p>{"原文日期："+E(s["published_at"]) if s["published_at"] else "原文未提供可确认的首次发布日期"} · 核实 {localtime(s["accessed_at"])} UTC+8</p></div>' for s in e['sources'])
        corrections=''.join('<p>'+E(c['at'])+' · '+E(c['note'])+'</p>' for c in e.get('corrections',[]))
        if corrections:corrections='<section class="scope-note"><h2>更正记录</h2>'+corrections+'</section>'
        prose=''.join('<p>'+E(paragraph)+'</p>' for paragraph in news_paragraphs(e))
        edit_note=f'<p class="small muted editorial-note">编辑更新：{localtime(e["editorial_updated_at"])} UTC+8</p>' if e.get('editorial_updated_at') else ''
        related=''.join(self.link(self.event_url(self.events[k]),E(self.events[k]['title'])) for k in issue['event_ids'] if k!=e['id'])
        image_credit=e['artwork']['credit'] if e.get('artwork') else e['graphic']['caption']
        graphic_path='assets/visuals/'+e['id']+'.svg'
        full_graphic=self.link(graphic_path,'查看完整内容图 ↗',target='_blank',rel='noopener noreferrer')
        fact_graphic=f'<figure class="fact-graphic"><img src="{self.url(graphic_path)}" alt="{E(graphic_alt(e))}" width="1200" height="760" loading="lazy"><figcaption>{E(e["graphic"]["caption"])} · {full_graphic}</figcaption></figure>' if e.get('artwork') else ''
        if not e.get('artwork'):image_credit=E(image_credit)+' · '+full_graphic
        else:image_credit=E(image_credit)
        return f'''<div class="article-layout"><div>{self.link(self.issue_url(issue),'← 返回 '+issue['date']+' 日报','back-link')}<article class="article-main"><div class="article-header"><span class="pill">{E(e['category'])}</span><span class="status-tag">{E(e['status'])}</span><h1>{E(e['title'])}</h1><p class="summary">{E(e['summary'])}</p>{self.source_meta(e)}</div>
        <figure class="article-visual">{self.image_markup(e,lazy=False)}<figcaption>{image_credit}</figcaption></figure>
        <div class="article-body"><div class="news-prose">{prose}</div>{fact_graphic}<h2>消息来源</h2>{sourcecards}{corrections}{edit_note}<p class="small muted" style="margin-top:20px">本站摘要于 {localtime(e['discovered_at'])} UTC+8 整理，收录在 {e['issue_date']} 期刊。</p></div></article></div><aside class="article-side"><section class="panel"><h3>本期还收录了</h3><p>{E(issue['title'])}</p><div class="article-related">{related}</div>{self.link('archive/index.html','回看所有期刊 →','panel-link')}</section></aside></div>'''
    def archive(self):
        out=self.top('THE ARCHIVE','每天的变化，留下记录。','按日期回看已发布期刊，来源与实际整理时间独立保留。')+'<div class="archive-grid">'
        for i in self.issues:
            out+=f'<article class="archive-card"><span class="number">{i["date"]} / NO.{i["number"]}</span><h2>{self.link(self.issue_url(i),E(i["title"]))}</h2><p>{E(i["dek"])}</p><div class="card-bottom"><span>{len(i["event_ids"])} 条精选 · {E(i.get("kind","每日精选"))}</span>{self.link(self.issue_url(i),"阅读本期 →")}</div></article>'
        out+='</div><section class="panel full-panel"><h3>每期一份，独立保存。</h3><p class="muted small">回溯样刊与每日精选分别标记。指标仅在实际保存了快照时才属于当期期刊。</p><div class="feed-actions">'
        for i in self.issues:out+=self.link('downloads/'+i['date']+'.md',i['date']+' Markdown ↓','secondary-link',download=i['date']+'.md')
        return out+'</div></section>'
    def readme_page(self):
        rows=''.join(self.news_row(self.events[k],i+1) for i,k in enumerate(self.latest['event_ids']))
        return self.top('README DAILY','最新一期，一份可带走的日报。','与本地 README 使用同一份内容；可在这里阅读，也可下载 Markdown。')+f'''<div class="scope-note"><p>{self.latest['date']} · {E(self.latest['title'])}</p>{self.link('downloads/README.md','下载 README.md ↓',download='README.md')}</div><div class="feed-actions">{self.link(self.issue_url(self.latest),'阅读完整日报 →','primary-link')}{self.link('archive/index.html','查看历史归档','secondary-link')}</div><div class="news-list" style="margin-top:23px">{rows}</div>'''
    def about(self):
        publishers={x['publisher'] for e in self.events.values() for x in e['sources']}
        return self.top('ABOUT SEVEN TECH NEWSROOM','把重要变化，讲清楚。','面向所有关心 AI 与科技的人，提供简洁、可回查的中文新闻和数据观察。')+f'''<div class="prose"><section class="panel"><h2>由谁维护？</h2><p>{E(self.site['name'])} 由 {self.link(self.site['author_url'],E(self.site['author']))} 维护，代码与内容档案保存在 {self.link(self.site['repository_url'],'GitHub 仓库')}。</p><h2>新闻从哪里来？</h2><p>当前归档 {len(self.issues)} 期、{len(self.events)} 个独立条目，涵盖 {len(publishers)} 个发布者。优先使用官方公告、研究文章、原始项目文档与独立评测。内容由 AI 辅助整理，摘要保留原始来源与核实时间。</p><h2>怎样区分事实与主张？</h2><p>厂商提供的成绩注明厂商报告，独立评测保留出处与设置范围。项目发现不等于新品发布，原始发布日期无法确认时直接注明。回溯样刊与每日精选按各自实际时间标记。</p><h2>怎样阅读数据？</h2><p>新闻插图依据文字事实绘制。价格、平台用量、Stars 和下载量来自各自公开来源，分别保留统计窗口与观测时间。数据不足时不填零、不补造增长曲线。</p><h2>纠错与贡献</h2><p>可以通过 {self.link(self.site['repository_url']+'/issues','仓库 Issues')} 提供来源或提出更正。后续更正在原期刊与事件中保留记录。</p><h2>内容使用</h2><p>本站代码、原创摘要与第三方内容分别适用各自说明；第三方新闻、数据和标识保留原有权利。OpenRouter 聚合用量摘录按 CC BY 4.0 署名。</p><p>{self.link('methodology/index.html','阅读指标方法 →')}　{self.link('subscribe/index.html','订阅每日摘要 →')}</p></section></div>'''

    def methodology(self):
        return self.top('METHODOLOGY','数字，要有上下文。','来源、窗口与公式写在这里，也保留在各张图表旁。')+f'''<div class="prose"><section class="panel"><h2>平台用量</h2><p>来源为 {self.link(self.usage['source_url'],'OpenRouter Rankings')} 的公开日榜文字表，统计 {self.usage["source_as_of"]} UTC 日桶内的输入与输出 Token。数值按来源的 T/B 单位换算，保留约数属性。不同模型的分词和输出长度会影响总量，不能推断用户数、质量、收入或全行业市场份额。表中的变化由来源提供，表示较前日变化；本站没有据此构建历史序列。</p><p>本轮使用公开页面核对摘录，尚未接入需要 Key 的 Data API。署名：Source: OpenRouter (openrouter.ai/rankings), usage through {self.usage["source_as_of"]}. Licensed under CC BY 4.0.</p><h2>模型价格</h2><p>从 {self.link('https://openrouter.ai/api/v1/models','OpenRouter 模型目录')} 采集 7 个选定模型的标示路由基本输入和输出价格，单位由每 Token 转换为每百万 Token，币种 USD。价格不保证代表厂商直连，也不完整覆盖长上下文价档、推理 Token、缓存、批处理、工具、请求及其他费用。</p><p>固定用量估算 = 0.01 × 每百万输入单价 + 0.002 × 每百万输出单价，对应 10,000 输入 + 2,000 输出 Token。这是费用估算，不是等能力任务的性价比测试。计算器使用同样的基本费公式。</p><h2>开源关注</h2><p>用 GitHub Repository API 读取预先选定的 6 个项目 Stars 与 Forks。榜单仅限本站跟踪池，既不是 GitHub Trending，也不是全站 AI 排名。首次观测只有总数，日增为空；后续仅在相同项目和可比时间间隔下计算净变化。</p><h2>模型下载</h2><p>用 Hugging Face Hub 模型列表按 text-generation 与 feature-extraction 两类任务、downloads 降序分别取得 6 项。downloads 表示近 30 日滚动计数。下载可能由软件程序触发，不是独立用户；滚动窗口的两日差额不能当作单日新增。</p><p>{self.link('https://huggingface.co/docs/hub/models-download-stats','查看 Hugging Face 官方计数说明 ↗')}</p><h2>日期与历史</h2><p>新闻期号采用 UTC+8；数据保留上游 UTC 统计桶和实际采集时间。回溯样刊没有补造当日指标。缺失使用 null，历史不足时只展示当前横截面。每次重建读取固定内容与快照，不会重新抓取并悄悄修改样刊。</p><h2>本地预览与 RSS</h2><p>RSS 的 pubDate 为期刊实际首次整理时间，标题中的日期是内容期号。GUID 由稳定期号生成，重建不重复生成订阅项。订阅入口使用当前站点地址；本地预览与正式站点的链接分别生成。</p></section></div>'''
    def subscribe(self):
        addr=self.base+'/feed.xml'
        out=self.top('STAY IN THE LOOP','用你习惯的方式，读新一期。','每日摘要，一期一条。标题、重点与原始资料入口都保留。')+f'''<div class="prose"><section class="panel"><h2>每日摘要 RSS</h2><p>将地址添加到 RSS 阅读器，或先打开 XML 查看已归档内容。</p><label class="small muted" for="feed-address">订阅地址</label><div class="rss-address"><input id="feed-address" readonly value="{E(addr)}"><button type="button" id="copy-feed" class="primary-link">复制地址</button></div><p id="copy-status" class="copy-status" role="status"></p><div class="feed-actions">{self.link('feed.xml','打开 RSS XML ↗','secondary-link')}{self.link('atom.xml','打开 Atom XML ↗','secondary-link')}</div><p class="small muted" style="margin-top:17px">{"当前为本地预览地址，需要在本机访问。" if self.is_local else "这是公开订阅地址，可添加到支持 RSS 或 Atom 的阅读器。"}</p><h2>订阅内容预览</h2><div class="feed-preview">'''
        for i in self.issues:
            out+=f'<article class="feed-item"><time class="small muted">{i["date"]} · 第 {i["number"]} 期</time><h3>{self.link(self.issue_url(i),E(i["title"]))}</h3><p>{E(i["dek"])}</p><p>首次整理：{localtime(i["published_at"])} UTC+8</p></article>'
        return out+'</div></section></div>'
    def search(self):
        rows=sorted(self.events.values(),key=lambda e:e['issue_date'],reverse=True)
        return self.top('SEARCH THE ARCHIVE','找回那条新闻。','搜索标题、摘要、分类或发布者；支持用空格组合关键词。')+f'''<form id="search-form" class="search-form" role="search"><label class="small muted" for="search-query">{icon('search')}<span style="position:absolute;clip:rect(0,0,0,0)">搜索新闻</span></label><input id="search-query" name="q" type="search" placeholder="例如：模型、Hugging Face、开源" autocomplete="off"></form><p id="search-count" class="search-count" aria-live="polite">共 {len(rows)} 条新闻</p><div class="news-list search-list" id="search-results">{''.join(self.news_row(e,i+1,True) for i,e in enumerate(rows))}<p class="empty-state" id="search-empty" hidden>没有找到匹配新闻。可以缩短关键词，或按发布者搜索。</p></div>'''
    def rss(self):
        atom='http://www.w3.org/2005/Atom';ET.register_namespace('atom',atom)
        rss=ET.Element('rss',version='2.0');ch=ET.SubElement(rss,'channel')
        for k,v in [('title','Seven Tech Newsroom · 每日摘要'),('link',self.base+'/'),('description','有来源的 AI / 科技新闻与数据观察。'),('language','zh-CN')]:ET.SubElement(ch,k).text=v
        ET.SubElement(ch,f'{{{atom}}}link',href=self.base+'/feed.xml',rel='self',type='application/rss+xml')
        ET.SubElement(ch,'lastBuildDate').text=format_datetime(dt.datetime.fromisoformat(self.content.get('updated_at',self.content['created_at'])),usegmt=True)
        feed=ET.Element(f'{{{atom}}}feed')
        for k,v in [('title','Seven Tech Newsroom · 每日摘要'),('id','urn:ai-rizhi:daily'),('updated',self.content.get('updated_at',self.content['created_at']))]:ET.SubElement(feed,f'{{{atom}}}{k}').text=v
        ET.SubElement(feed,f'{{{atom}}}link',href=self.base+'/atom.xml',rel='self')
        author=ET.SubElement(feed,f'{{{atom}}}author');ET.SubElement(author,f'{{{atom}}}name').text='Seven Tech Newsroom'
        for i in self.issues:
            item=ET.SubElement(ch,'item');title=i['date']+'｜'+i['title'];url=self.base+'/'+self.issue_url(i);guid='urn:ai-rizhi:daily:'+i['date']
            content='<p>'+E(i['dek'])+'</p><p>'+E(i.get('kind','每日精选'))+'；于 '+localtime(i['published_at'])+' UTC+8 整理。</p><ul>'
            for key in i['event_ids']:
                e=self.events[key]
                paragraphs=''.join('<p>'+E(paragraph)+'</p>' for paragraph in news_paragraphs(e))
                sources=' · '.join(f'<a href="{E(source["url"])}">{E(source["publisher"])} · 原始资料</a>' for source in e['sources'])
                image=f'<img src="{self.base}/{self.visual_path(e)}" alt="{E(self.visual_alt(e))}" width="640">'
                credit=e['artwork']['credit'] if e.get('artwork') else e['graphic']['caption']
                content+=f'<li><h3><a href="{self.base}/{self.event_url(e)}">{E(e["title"])}</a></h3>{image}<p>{E(credit)}</p>{paragraphs}<p>{sources}</p></li>'
            content+='</ul>'
            for k,v in [('title',title),('link',url),('description',content),('pubDate',format_datetime(dt.datetime.fromisoformat(i['published_at']),usegmt=True))]:ET.SubElement(item,k).text=v
            ET.SubElement(item,'guid',isPermaLink='false').text=guid
            entry=ET.SubElement(feed,f'{{{atom}}}entry')
            for k,v in [('title',title),('id',guid),('published',i['published_at']),('updated',i.get('updated_at',i['published_at']))]:ET.SubElement(entry,f'{{{atom}}}{k}').text=v
            ET.SubElement(entry,f'{{{atom}}}link',href=url)
            ET.SubElement(entry,f'{{{atom}}}content',type='html').text=content
        self.write('feed.xml',ET.tostring(rss,encoding='unicode',xml_declaration=True))
        self.write('atom.xml',ET.tostring(feed,encoding='unicode',xml_declaration=True))
    def markdown(self,issue):
        s=f'# Seven Tech Newsroom · {issue["date"]}\n\n**{issue["title"]}**\n\n{issue["dek"]}\n\n{issue.get("kind","每日精选")}，第 {issue["number"]} 期。收录范围：{issue["coverage"]}。\n实际首次整理：{localtime(issue["published_at"])} UTC+8。\n指标按实际保存的批次与采集时间查看。\n\n'
        for n,key in enumerate(issue['event_ids'],1):
            e=self.events[key];s+=f'## {n}. {e["title"]}\n\n'
            s+=f'![{self.visual_alt(e)}]({self.site["site_url"]}/{self.visual_path(e)})\n\n'
            s+=(e['artwork']['credit'] if e.get('artwork') else e['graphic']['caption'])+'\n\n'
            s+='\n\n'.join(news_paragraphs(e))+'\n\n'
            s+=f'分类：{e["category"]}；状态：{e["status"]}；原文日期：{e["published_at"] or "待确认"}。\n\n'
            s+='\n'.join(f'来源：[{x["publisher"]}]({x["url"]})' for x in e['sources'])+'\n\n'
            for c in e.get('corrections',[]):s+='更正：'+c['at']+' · '+c['note']+'\n\n'
        return s.rstrip()+'\n'
    def build(self):
        OUT.mkdir(exist_ok=True)
        (OUT/'assets').mkdir(exist_ok=True)
        for name in ['style.css','app.js']:shutil.copy2(ROOT/'src'/name,OUT/'assets'/name)
        self.write('assets/favicon.svg','<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#285cdb"/><text x="32" y="44" text-anchor="middle" fill="white" font-size="36" font-family="sans-serif">7</text></svg>')
        for e in self.events.values():
            self.write('assets/visuals/'+e['id']+'.svg',illustration(e))
            if e.get('artwork'):
                target=OUT/self.visual_path(e);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/e['artwork']['path'],target)
        self.page('index.html',self.latest['date']+'｜'+self.latest['title'],self.home,'home',self.latest['dek'])
        for issue in self.issues:self.page(self.issue_url(issue),issue['date']+' 日报',lambda i=issue:self.issue_page(i),'archive',issue['dek'])
        for e in self.events.values():self.page(self.event_url(e),e['title'],lambda a=e:self.article(a),'',e['summary'],e)
        for path,title,fn,active in [('data','数据观察',self.data,'data'),('archive','历史归档',self.archive,'archive'),('about','关于 Seven Tech Newsroom',self.about,'about'),('methodology','指标方法',self.methodology,''),('subscribe','RSS 订阅',self.subscribe,''),('search','搜索新闻',self.search,''),('readme','README 日报',self.readme_page,'')]:
            self.page(path+'/index.html',title,fn,active)
        self.rss()
        self.write('.nojekyll','')
        self.write('status.json',json.dumps({'name':self.site['name'],'batch_id':self.batch,'latest_issue_date':self.latest['date'],'latest_issue_kind':self.latest.get('kind'),'issue_count':len(self.issues),'event_count':len(self.events),'snapshot_at':self.snapshot['collected_at'],'commit_sha':os.environ.get('GITHUB_SHA') or os.environ.get('NEWSROOM_COMMIT_SHA'),'repository_url':self.site['repository_url']},ensure_ascii=False,indent=2)+'\n')
        (OUT/'downloads/data').mkdir(parents=True,exist_ok=True)
        for i in self.issues:
            text=self.markdown(i);archive=ROOT/'archive'/f'{i["date"]}.md';archive.parent.mkdir(exist_ok=True);archive.write_text(text)
            self.write('downloads/'+i['date']+'.md',text)
            if i.get('metric_snapshot'):shutil.copy2(ROOT/i['metric_snapshot'],OUT/'downloads/data'/f'{i["date"]}.json')
        readme='# Seven Tech Newsroom\n\n每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。\n\n'
        readme+='[访问网站]('+self.site['site_url']+'/) · [RSS]('+self.site['site_url']+'/feed.xml) · [源码仓库]('+self.site['repository_url']+') · [作者主页]('+self.site['author_url']+') · [运行说明](OPERATIONS.md)\n\n'
        readme+=f'最近一期：{self.latest["date"]}。共 {len(self.issues)} 期、{len(self.events)} 条独立记录；按实际发布状态与来源标时。\n\n'
        readme+='**最新数据快照**：'+localtime(self.snapshot['collected_at'])+' UTC+8；OpenRouter 日榜另截至 '+self.usage['source_as_of']+' UTC。\n\n'
        minimum=min(self.snapshot['prices'],key=lambda p:p['fixed_text_cost'])
        top_repo=self.snapshot['github'][0];top_hf=self.snapshot['huggingface']['text-generation'][0];top_usage=self.usage['rows'][0]
        readme+='| 观察项 | 最新观测 | 范围 |\n| --- | --- | --- |\n'
        readme+=f'| 模型基本费估算 | ${money(minimum["fixed_text_cost"])} · {short_model(minimum["name"])} | {len(self.snapshot["prices"])} 个选定模型，10K 输入 + 2K 输出 Token |\n'
        readme+=f'| 平台单日用量 | 约 {top_usage["tokens_trillion"]}T Token · {top_usage["name"]} | OpenRouter {self.usage["source_as_of"]} UTC 公开日榜 |\n'
        readme+=f'| 开源关注 | {top_repo["stars"]:,} Stars · {top_repo["id"]} | 本站固定跟踪的 {len(self.snapshot["github"])} 个项目 |\n'
        readme+=f'| 文本模型下载 | {top_hf["downloads_30d"]:,} · {top_hf["id"]} | HF 文本生成类，近 30 日滚动量 |\n\n'
        readme+='来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。\n\n'
        readme+=self.markdown(self.latest).replace('# Seven Tech Newsroom ·','## 最新一期 ·',1)
        readme+='\n**历史归档**\n\n'+''.join(f'- [{i["date"]} · {i["title"]}](archive/{i["date"]}.md)\n' for i in self.issues)
        (ROOT/'README.md').write_text(readme);self.write('downloads/README.md',readme)
        (ROOT/'build-manifest.json').write_text(json.dumps({'batch_id':self.batch,'base_url':self.base,'issues':[i['date'] for i in self.issues],
            'events':len(self.events),'snapshot_at':self.snapshot['collected_at'],'pages':len(list(OUT.rglob('*.html'))),
            'publication':'local preview' if self.is_local else 'public static site'},ensure_ascii=False,indent=2)+'\n')
        print(f'Built {len(list(OUT.rglob("*.html")))} static pages, {len(self.events)} articles, 2 feeds. Batch {self.batch}.')

def main():
    p=argparse.ArgumentParser();p.add_argument('--base-url',default=os.environ.get('SITE_URL',load('config/site.json')['site_url']))
    args=p.parse_args();url=urlparse(args.base_url)
    if url.scheme not in ['http','https'] or not url.netloc:raise SystemExit('base-url must be an absolute HTTP(S) URL.')
    Publisher(args.base_url).build()
if __name__=='__main__':main()
