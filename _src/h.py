# -*- coding: utf-8 -*-
def cv(i,alt,cls=''): return '<div class="cwrap"><canvas id="%s"%s aria-label="%s"></canvas></div>'%(i,(' class="%s"'%cls) if cls else '',alt)
def rg(i,lab,mn,mx,v,st=1): return '<div class="group"><label class="glabel" for="%s">%s</label><input type="range" id="%s" min="%s" max="%s" value="%s" step="%s"><span class="val" id="%sV"></span></div>'%(i,lab,i,mn,mx,v,st,i)
def tg(i,lab,opts): return '<div class="group" id="%s"><span class="glabel">%s</span>%s</div>'%(i,lab,''.join('<button type="button" class="bt" data-v="%s" aria-pressed="%s">%s</button>'%(v,'true' if j==0 else 'false',t) for j,(v,t) in enumerate(opts)))
def bt(i,t): return '<div class="group"><button class="bt" type="button" id="%s" aria-pressed="false">%s</button></div>'%(i,t)
def note(t): return '<p style="font-size:14px;color:var(--muted);margin-bottom:0">%s</p>'%t
def steps3(a): return '<div class="steps">'+''.join('<div><b class="n">%d</b><h4>%s</h4><p>%s</p></div>'%(i+1,h,p) for i,(h,p) in enumerate(a))+'</div>'
def field(p,lim): return '<div class="bridge field"><h4>업무에 옮기면</h4><p>%s</p><p class="lim">비유의 한계 · %s</p></div>'%(p,lim)
def gen(p,lim): return ('gen','생성 AI로 치면',p,lim)
def Q(q,o,a,why,hint,t=None,kind=None):
    d=dict(q=q,o=o,a=a,why=why,hint=hint)
    if t: d['t']=t
    if kind: d['kind']=kind
    return d
SIA=('sia','guide','순서대로 말씀드릴게요. 다음은 대결, 그다음이 정리예요.')
