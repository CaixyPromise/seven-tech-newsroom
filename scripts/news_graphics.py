"""Render sourced editorial information graphics from an explicit per-story brief."""
import html
import math
from pathlib import PurePosixPath

PALETTES={'blue':('#eaf1ff','#2159ca','#c9d9fa'),'violet':('#f0ebfa','#6950ad','#dcd1f1'),'teal':('#e6f5f1','#187c71','#c6e7df'),'amber':('#fbf1df','#a36515','#eddbb9')}
LAYOUTS={'specs','timeline','flow','layers','hub','bars'}
def esc(value):return html.escape(str(value),quote=True)
def width(text):return sum(1 if ord(c)<256 else 1.85 for c in str(text))
def lines(text,limit):
    out=[];line='';used=0
    for char in str(text):
        w=1 if ord(char)<256 else 1.85
        if used+w>limit:out.append(line);line='';used=0
        line+=char;used+=w
    if line:out.append(line)
    return out or ['']
def validate_graphic(event):
    g=event.get('graphic')
    if not isinstance(g,dict):raise ValueError('Every event needs a sourced graphic brief')
    if g.get('layout') not in LAYOUTS or g.get('theme') not in PALETTES:raise ValueError('Unknown graphic layout or theme')
    for key,limit in [('title',32),('eyebrow',40),('caption',160)]:
        if not isinstance(g.get(key),str) or not 0<len(g[key])<=limit:raise ValueError('Invalid graphic '+key)
    refs=g.get('source_refs')
    if not isinstance(refs,list) or not refs or any(type(n) is not int or not 0<=n<len(event['sources']) for n in refs):raise ValueError('Graphic needs valid source references')
    items=g.get('items')
    if not isinstance(items,list) or not 2<=len(items)<=6:raise ValueError('Graphic needs 2–6 concrete items')
    for item in items:
        for key,limit in [('label',24),('value',36),('detail',60)]:
            if not isinstance(item.get(key),str) or not 0<len(item[key])<=limit:raise ValueError('Invalid graphic item '+key)
        if g['layout']=='bars':
            n=item.get('amount')
            if type(n) not in [int,float] or not math.isfinite(n) or n<0:raise ValueError('Invalid chart amount')
    if g['layout']=='bars' and (type(g.get('axis_max')) not in [int,float] or not math.isfinite(g['axis_max']) or g['axis_max']<=0 or any(i['amount']>g['axis_max'] for i in items)):raise ValueError('Invalid zero-based chart scale')
    if g['layout']=='hub' and len(items)>4:raise ValueError('Hub graphics support up to four branches')
    if g['layout']=='hub':
        focus=g.get('focus')
        if not isinstance(focus,dict) or any(not isinstance(focus.get(k),str) or not 0<len(focus[k])<=32 for k in ['value','label']):raise ValueError('Hub graphics need a concrete focus')
    artwork=event.get('artwork')
    if artwork:
        path=PurePosixPath(artwork.get('path',''))
        if path.is_absolute() or '..' in path.parts or path.parts[:2]!=('content','images') or path.suffix.lower() not in ['.png','.jpg','.jpeg','.webp']:raise ValueError('Artwork must be a local content/images raster asset')
        if artwork.get('kind') not in ['generated','official']:raise ValueError('Unknown artwork kind')
        for key in ['alt','credit','rights']:
            if not isinstance(artwork.get(key),str) or not artwork[key].strip() or len(artwork[key])>300:raise ValueError('Missing artwork '+key)
        if artwork['kind']=='official':
            for key in ['source_url','image_url','rights_url']:
                if not artwork.get(key,'').startswith('https://'):raise ValueError('Official artwork needs source, image and rights URLs')
        for key in ['width','height']:
            if key in artwork and (type(artwork[key]) is not int or not 1<=artwork[key]<=20000):raise ValueError('Invalid artwork dimensions')
    return g

def render(event):
    g=validate_graphic(event);bg,accent,soft=PALETTES[g['theme']];items=g['items'];parts=[]
    def text(x,y,value,size=28,fill='#24334b',weight=400,limit=None):
        for j,line in enumerate(lines(value,limit) if limit else [str(value)]):parts.append(f'<text x="{x}" y="{y+j*size*1.38:.1f}" font-size="{size}" fill="{fill}" font-weight="{weight}">{esc(line)}</text>')
    def rect(x,y,w,h,fill='white',radius=18,stroke='none'):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')
    def card(x,y,w,h,item,highlight=False):
        rect(x,y,w,h,accent if highlight else 'white');ink='white' if highlight else '#24334b';muted='#e4edff' if highlight else '#63718a'
        text(x+26,y+43,item['label'],23,muted,500,limit=(w-52)/14)
        value_size=min(48,int((w-52)/max(width(item['value']),1)*1.7));value_size=max(26,value_size)
        text(x+26,y+103,item['value'],value_size,ink,700,limit=(w-52)/(value_size*.57))
        text(x+26,y+h-53,item['detail'],21,muted,400,limit=(w-52)/12)
    opening=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 760" role="img" aria-labelledby="title desc" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,PingFang SC,Hiragino Sans GB,sans-serif"><title id="title">{esc(g["title"])}</title><desc id="desc">{esc(graphic_alt(event))}</desc>'
    rect(0,0,1200,760,bg,0);rect(48,50,7,76,accent,3)
    text(78,74,g['eyebrow'],21,accent,600);text(76,128,g['title'],40,'#182c4a',700)
    layout=g['layout'];n=len(items)
    if layout=='bars':
        left=270;right=1115;top=210;bottom=610
        for tick in [0,g['axis_max']/2,g['axis_max']]:
            x=left+(right-left)*tick/g['axis_max'];parts.append(f'<path d="M{x} {top-15}V{bottom}" stroke="#cbd6e7" stroke-width="2"/>');text(x-6,bottom+38,f'{tick:g}',20,'#65758c')
        step=min(140,360/n)
        for j,item in enumerate(items):
            y=top+j*step;text(76,y+38,item['label'],25,'#2f4260',600,limit=13)
            rect(left,y,right-left,60,soft,10);bar=(right-left)*item['amount']/g['axis_max'];rect(left,y,bar,60,accent if j==n-1 else '#829fcd',10)
            text(left+min(bar+14,right-left-100),y+42,item['value'],31,accent,700)
            text(left,y+91,item['detail'],21,'#62728c',limit=62)
    elif layout=='layers':
        step=min(100,430/n)
        for j,item in enumerate(items):
            x=76+25*(n-j-1);w=1048-50*(n-j-1);y=185+j*step
            rect(x,y,w,step-12,accent if j==n-1 else 'white',12)
            text(x+25,y+39,item['value'],29,'white' if j==n-1 else accent,700)
            text(x+w*.43,y+38,item['detail'],22,'#e5eeff' if j==n-1 else '#61718b',limit=w*.51/13)
    elif layout=='flow' or layout=='timeline':
        cols=min(3,n);w=(1048-(cols-1)*26)/cols;rows=math.ceil(n/cols);h=330 if rows==1 else 205
        for j,item in enumerate(items):
            x=76+(j%cols)*(w+26);y=220+(j//cols)*(h+24)
            card(x,y,w,h,item,j==0)
            text(x+24,y-24,f'{j+1:02d}' if layout=='flow' else item['label'],22,accent,600)
            if j%cols<cols-1 and j<n-1:parts.append(f'<path d="M{x+w+5} {y+h/2}h16m-7-7 7 7-7 7" fill="none" stroke="{accent}" stroke-width="3"/>')
    elif layout=='hub':
        focus=g.get('focus',{'value':event['category'],'label':g['title']})
        rect(432,270,336,240,accent,28);text(462,342,focus['value'],48,'white',700,limit=10);text(462,453,focus['label'],25,'#edf3ff',limit=18)
        positions=[(76,190),(844,190),(76,450),(844,450)]
        for j,item in enumerate(items):
            x,y=positions[j];left=x<400
            parts.append(f'<path d="M{x+280 if left else x} {y+95}H{432 if left else 768}" stroke="{accent}" stroke-width="3" stroke-dasharray="8 5"/>')
            card(x,y,280,190,item)
    else:
        cols=2 if n in [2,4] else 3;rows=math.ceil(n/cols);w=(1048-(cols-1)*24)/cols;h=370 if rows==1 else 211
        for j,item in enumerate(items):card(76+(j%cols)*(w+24),185+(j//cols)*(h+20),w,h,item,j==0)
    parts.append('<path d="M76 680h1048" stroke="#cbd6e7"/>')
    source=' / '.join(event['sources'][i]['publisher'] for i in g['source_refs'])
    text(76,714,'资料：'+source,18,'#64748b',limit=103)
    text(1124-width(event['issue_date'])*10,714,event['issue_date'],18,'#64748b')
    return opening+''.join(parts)+'</svg>'

def graphic_alt(event):
    g=event['graphic']
    return g['title']+'。'+'；'.join(i['label']+'：'+i['value']+'，'+i['detail'] for i in g['items'])
