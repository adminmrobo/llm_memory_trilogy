# -*- coding: utf-8 -*-
"""기억 3부작 생성기: python3 _build/gen.py <key …|all>   (key 예: 1_2)  →  out/<파일>"""
import sys,os,re,json,subprocess,importlib.util,html
B=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(B); sys.path.insert(0,B)
from series import *
def rd(p): return open(p,encoding='utf-8').read()
KEYS=[n.replace('-','_') for n,_,_ in PAGES]
def built(): return {k for k in KEYS if os.path.exists(os.path.join(ROOT,'_src','p'+k+'.py')) or os.path.exists(os.path.join(ROOT,'_src',k,'body.html'))}
def info(num): return [p for p in PAGES if p[0]==num][0]
def pager(num):
    part=num[0]; bs=built(); o='<nav class="pager" aria-label="%s부 안 페이지">'%part
    for n,f,t in PAGES:
        if n[0]!=part: continue
        if n==num: o+='<a href="%s" class="cur" title="%s">%s</a>'%(f,t,n)
        elif n.replace('-','_') in bs: o+='<a href="%s" title="%s">%s</a>'%(f,t,n)
        else: o+='<a class="soon" title="%s (준비 중)">%s</a>'%(t,n)
    return o+'</nav>'
def nextprev(num):
    i=[p[0] for p in PAGES].index(num); bs=built()
    if i==0: a='<a href="https://adminmrobo.github.io/timeseries-trilogy/1_1_lookback_window.html"><small>← 앞 글</small>시계열 3부작 1-1 lookback과 window</a>'
    else: n,f,t=PAGES[i-1]; a='<a href="%s"><small>← 이전</small>%s %s</a>'%(f,n,t)
    if i==len(PAGES)-1: b='<a href="index.html" style="text-align:right"><small>끝 →</small>시리즈 목차</a>'
    else:
        n,f,t=PAGES[i+1]
        b=('<a href="%s" style="text-align:right"><small>다음 →</small>%s %s</a>'%(f,n,t)) if n.replace('-','_') in bs else '<a class="soon" style="text-align:right"><small>다음 → (준비 중)</small>%s %s</a>'%(n,t)
    return '<div class="nextprev">'+a+b+'</div>'
def say(who,mood,text,cls='',name=None):
    return '<div class="say%s" data-who="%s"><img class="who" data-who="%s" data-mood="%s" alt="" aria-hidden="true"><div><b class="name">%s</b><p>%s</p></div></div>'%((' '+cls) if cls else '',who,who,mood,name or NAME[who],text)
CAST='''<section class="level" id="cast"><div class="wrap"><h2>등장인물 · 이 페이지 사용법</h2><div class="cast"><div><img data-who="doc" data-mood="front" alt="" aria-hidden="true"><b style="color:var(--c-doc)">박사</b><span>해설자 · 심판. 판정은 숫자대로</span></div><div><img data-who="asst" data-mood="smile" alt="" aria-hidden="true"><b style="color:var(--c-asst)">하루(조수)</b><span>실험 진행 · 숫자 발표 · 수식 질문</span></div><div><img data-who="fly" data-mood="clip" alt="" aria-hidden="true"><b style="color:var(--c-fly)">초파리 연구원</b><span>의심하는 쪽 · %s</span></div><div><img data-who="robo" data-mood="smile" alt="" aria-hidden="true"><b style="color:var(--c-robo)">주판봇</b><span>확신하는 쪽 · %s</span></div><div><img data-who="sia" data-mood="smile" alt="" aria-hidden="true"><b>인턴 시아</b><span>진행 신호 · 순서 안내</span></div><div><img data-who="moa" data-mood="smile" alt="" aria-hidden="true"><b>인턴 모아</b><span>%s</span></div></div><p style="margin:10px 0"><button type="button" class="bt" id="xBtn" aria-expanded="false" aria-controls="xRoster">미공개 식구 보기</button></p><div class="cast xroster" id="xRoster" hidden><div><img data-who="x1" data-mood="hint" alt="" aria-hidden="true"><b>미공개</b><span>%s</span></div><div><img data-who="x2" data-mood="hint" alt="" aria-hidden="true"><b>미공개</b><span>%s</span></div><div><img data-who="x3" data-mood="hint" alt="" aria-hidden="true"><b>미공개</b><span>%s</span></div></div><div class="steps"><div><b class="n">1</b><p>밑줄 친 말을 누르거나 마우스를 올리면 뜻이 나와요. 오른쪽 아래 단추로 밑줄을 핵심 → 전체 → 끄기로 바꿀 수 있어요.</p></div><div><b class="n">2</b><p>그림 위 <span class="stampnote">설명용 모형 · 실제 데이터 아님</span> 도장은 정해진 규칙으로 만든 연습용 데이터라는 표시예요.</p></div><div><b class="n">3</b><p>칸 끝의 확인 퀴즈로 이해를 점검하세요. 점수는 저장되지 않아요.</p></div></div></div></section>'''
KGEX=None
def kgex():
    global KGEX
    if KGEX is None:
        s=rd(os.path.join(ROOT,'_src','1_1','body.html')); KGEX=s[s.find('<section class="level" id="kg">'):s.find('<footer>')]
    return KGEX
CROWD='<div class="crowd" aria-label="방청석"><span class="clabel">방청석</span><figure><img data-who="moa" data-mood="cheer" alt="" aria-hidden="true"><figcaption><b>인턴 모아</b><span class="cl" data-c="moa">두 분 다 힘내세요!</span></figcaption></figure><figure class="x"><img data-who="x1" data-mood="hint" alt="" aria-hidden="true"><figcaption><b>누군가</b><span class="cl">(…)</span></figcaption></figure><figure class="x"><img data-who="x2" data-mood="hint" alt="" aria-hidden="true"><figcaption><b>누군가</b><span class="cl">(반짝)</span></figcaption></figure><figure class="x"><img data-who="x3" data-mood="hint" alt="" aria-hidden="true"><figcaption><b>누군가</b><span class="cl">(두근)</span></figcaption></figure></div>'
def level(L):
    o='<section class="level" id="%s"><div class="wrap"><div class="lvhead"><div class="hexno">%s<small>%s</small></div><h2>%s</h2><p class="sub"><span class="lvtag %s">%s</span><span class="lvtag">%s</span></p></div>'%(L['id'],L['no'],L.get('kind','실험'),L['title'],L.get('tc','g'),L['tag1'],L['tag2'])
    w=L.get('why'); m=L.get('math')
    if w:
        wb='<div class="whybox"><h4>%s</h4><p><b>문제 상황</b> · %s</p><p><b>앞 방법의 한계</b> · %s</p><p><b>해법</b> · %s</p><p class="easy"><b>쉽게 말하면</b> %s</p></div>'%(L.get('whyh','왜 이 방법을 쓰나'),w[0],w[1],w[2],w[3])
        if m:
            pc=''.join('<tr><td>%s</td><td>%s</td></tr>'%p for p in m['pieces'])
            mb=('<div class="mathbox"><h4>수학 수식을 어려워하는 조수가 대신 물어봅니다</h4>'+say('asst','shock',m['ask'],'mini')+'<p><b>학교 수학으로 보면</b> · %s</p><div class="eq" data-nogloss>%s</div><div class="tw"><table class="tb pieces"><tr><th>식 조각</th><th>뜻</th></tr>%s</table></div><p><b>숫자로 한 번 해 보기</b> · %s</p>'%(m['school'],m['eq'],pc,m['num'])+say('asst','spark',m['comment'],'mini')+'</div>')
            o+='<div class="twobox">'+wb+mb+'</div>'
        else: o+='<div class="twobox one">'+wb+'</div>'
    p=L.get('pair')
    if p: o+='<div class="pair"><div><div class="tag fly">일상으로 치면</div><p>%s</p></div><div><div class="tag nn">%s</div><p>%s</p></div></div>'%(p[0],L.get('pairR','모델에서는'),p[1])
    if L.get('talk'): o+='<div class="talk">'+''.join(say(*t) for t in L['talk'])+'</div>'
    o+=L.get('panel','')
    if L.get('report'): o+=say('asst','report',L['report'])
    if L.get('steps'):
        o+='<div class="explain"><h4>풀이 — %s</h4><ol>%s</ol><p class="lim"><b>이 칸의 한계</b> · %s</p></div>'%(L.get('stepsh','한 걸음씩'),''.join('<li>%s</li>'%s for s in L['steps']),L['lim'])
    if L.get('code'):
        o+='<details class="math code"><summary>파이썬 코드로 보면 (몰라도 됩니다)</summary><div class="tw"><table class="tb"><tr><th>코드 한 줄</th><th>뜻</th></tr>%s</table></div><p style="font-size:13px;color:var(--muted)">%s</p></details>'%(''.join('<tr><td><code>%s</code></td><td>%s</td></tr>'%(html.escape(c),d) for c,d in L['code']),L.get('codenote','쓰임새를 보인 예다. 이 페이지의 계산은 같은 원리를 브라우저 안에서 직접 했다.'))
    for b in L.get('bridges',[]): o+='<div class="bridge %s"><h4>%s</h4><p>%s</p><p class="lim">비유의 한계 · %s</p></div>'%b
    if L.get('intern'): o+=say(*L['intern'])
    o+=L.get('extra','')
    return o+'<div class="quiz" data-quiz="%s"></div></div></section>'%L['id']
def body(P):
    num=P['num']; part=int(num[0]); _,f,short=info(num)
    links=[('first','3줄 요약'),('why','왜 이 주제인가')]+([('big',P.get('bign','큰 그림'))] if P.get('big') else [])+[(L['id'],L.get('nav',L['title'])) for L in P['levels']]+([('vs','대결')] if P.get('duel') else [])+[('sum','정리'),('kg','지식 색인'),('export','꾸러미')]
    o='<div id="prog"></div><nav class="top"><a class="logo" href="index.html"><i></i>기억 3부작</a><div class="links">'+''.join('<a href="#%s">%s</a>'%l for l in links)+'</div></nav>'
    o+='<!-- lab-cover --><header class="cover cover-strip" id="cover" data-img="cover_ch%d"><div class="cover-fb" role="img" aria-label="표지 그림 자리. 네 캐릭터가 나란히 선 대체 표지"><img class="c-fly" data-who="fly" data-mood="point" data-face="right" alt=""><img class="c-doc" data-who="doc" data-mood="think" alt=""><img class="c-asst" data-who="asst" data-mood="smile" alt=""><img class="c-robo" data-who="robo" data-mood="coin" data-face="left" alt=""></div><span class="cover-chip">기억 3부작 · %s</span></header><!-- /lab-cover -->\n'%(part,PARTS[part])
    o+='<header class="hero" id="top"><div class="hex-bg"></div><canvas class="pixelart" aria-hidden="true"></canvas><div class="wrap"><div class="hero-text"><div class="kicker"><b>%s</b><span>%s</span><span class="chip">%s</span><span class="chip">비전공 독자용</span></div><h1>%s</h1><p class="q">%s</p><div class="lead">%s</div>'%(SERIES,PARTS[part].replace('부 ','부 · '),P['chip'],P['title'],P['q'],P['lead'])
    nq=sum(len(v) for v in P['quiz'].values())
    o+='<div class="objbox"><b>이 쪽을 마치면</b><span class="chip">약 %d분 · 퀴즈 %d문항</span><ol>%s</ol></div></div>'%(P['mins'],nq,''.join('<li>%s</li>'%x for x in P['objs']))
    o+='<div class="kpis">'+''.join('<div class="kpi %s"><b>%s</b><span>%s</span></div>'%(c,v,l) for (v,l),c in zip(P['kpis'],'gamr'))+'</div>'
    note=P.get('kpinote') or ('이 숫자들은 연습용 데이터에서 이 페이지가 직접 계산한 값이다.' if part==1 else '이 숫자들은 지어낸 가정을 둔 <b>설명용 모형</b>에서 계산한 값이다. 실제 서비스나 실제 모델을 잰 값이 아니다.')
    o+='<p class="kpinote">'+note+'</p>'
    o+='<div class="hero-dialog">'+''.join(say(w,m,t) for (w,m),t in zip([('doc','think'),('asst','smile'),('fly','point'),('robo','coin')],P['hero']))+'</div>'+pager(num)+'</div></header>\n'
    o+='<section class="level" id="first"><div class="wrap"><div class="first3"><h2>처음 오신 분께 — 이 페이지를 3줄로</h2><ol><li><b>무엇을</b> %s</li><li><b>왜 중요한가</b> %s</li><li><b>업무에서는</b> %s</li></ol><p class="ok">코드·수식을 몰라도 됩니다. 수식이 나오는 곳에서는 조수가 대신 물어봅니다.</p><details class="abbr"><summary>영어 약어 풀이 (눌러서 펼치기)</summary><dl>%s</dl></details></div></div></section>\n'%(P['first3'][0],P['first3'][1],P['first3'][2],''.join('<dt>%s</dt><dd>%s</dd>'%(k,ABBR[k]) for k in P['abbr']))
    c=P.get('cast',{}); o+=(CAST if num.endswith('-1') else CAST.replace('<div class="wrap"><h2>등장인물 · 이 페이지 사용법</h2>','<div class="wrap"><details class="castfold"><summary>등장인물 · 이 페이지 사용법 (눌러서 펼치기)</summary>').replace('</div></div></section>','</div></details></div></section>'))%(c.get('fly','작고 단순한 쪽을 고른다'),c.get('robo','크고 많은 쪽을 고른다'),c.get('moa','기록을 모아 두는 사람 · 응원'),c.get('x1','방청석의 누군가'),c.get('x2','방청석의 누군가'),c.get('x3','방청석의 누군가'))+'\n'
    o+='<section class="level" id="why"><div class="wrap"><div class="lvhead"><div class="hexno">?<small>도입</small></div><h2>%s</h2><p class="sub"><span class="lvtag g">%s</span><span class="lvtag">앞 편: %s</span></p></div><div class="steps">%s</div><div class="quiz" data-quiz="why"></div></div></section>\n'%(P['whyh'],P['whytag'],P['prev'],''.join('<div><b class="n">%d</b><h4>%s</h4><p>%s</p></div>'%(i+1,h,p) for i,(h,p) in enumerate(P['why'])))
    if P.get('big'): o+='<section class="level" id="big"><div class="wrap"><div class="lvhead"><div class="hexno">◇<small>지도</small></div><h2>%s</h2></div>%s</div></section>\n'%(P.get('bigh','큰 그림'),P['big'])
    o+='\n'.join(level(L) for L in P['levels'])+'\n'
    d=P.get('duel')
    if d:
        o+='<section class="level" id="vs"><div class="wrap"><div class="lvhead"><div class="hexno">⚔<small>대결</small></div><h2>%s</h2><p class="sub"><span class="lvtag g">판정: %s</span><span class="lvtag">%s</span></p></div><div class="duel" id="duel"><p style="margin-top:0"><b>대결 질문</b> · %s</p>'%(d['title'],d['metric'],d['tag'],d['q'])
        o+=say('sia','signal','확인했습니다. 같은 기록, 같은 지표, 같은 조건으로 시작합니다.','ref','인턴 시아 · 진행')
        o+='<div class="vs"><div class="fl"><img data-who="fly" data-mood="point" data-face="right" alt="" aria-hidden="true"><b>초파리 연구원</b></div><div class="mid">VS</div><div class="rb"><img data-who="robo" data-mood="coin" data-face="left" alt="" aria-hidden="true"><b>주판봇</b></div></div>'
        o+='<div class="picks"><div class="pf"><b>초파리의 선택</b><p style="margin:4px 0">%s</p><p style="margin:0;color:var(--muted);font-size:14px">“%s”</p></div><div class="pr"><b>주판봇의 선택</b><p style="margin:4px 0">%s</p><p style="margin:0;color:var(--muted);font-size:14px">“%s”</p></div></div>'%(d['fly'][0],d['fly'][1],d['robo'][0],d['robo'][1])
        o+='<p style="font-size:14px;color:var(--muted)">판정 기준: %s 두 값의 차이가 큰 값의 5%% 안쪽이면 무승부다.</p>'%d['rule']
        o+='<div class="guess"><span class="glabel">먼저 맞혀 보기</span><button type="button" class="bt" data-g="F" aria-pressed="false">초파리가 이길 것 같다</button><button type="button" class="bt" data-g="R" aria-pressed="false">주판봇이 이길 것 같다</button><span class="gl glabel" aria-live="polite">기록만 하고 저장하지 않아요.</span></div>'+CROWD
        o+='<button type="button" class="bt primary reveal">결과 보기</button><div class="result" aria-live="polite"><div class="bars" data-nogloss></div>'+say('asst','firm','','asst')+say('doc','front','','verdict')+'</div></div><div class="insight" id="duelNote" aria-live="polite"></div><div class="quiz" data-quiz="vs"></div></div></section>\n'
    o+='<section class="level" id="sum"><div class="wrap"><div class="lvhead"><div class="hexno">∑<small>정리</small></div><h2>%s</h2><p class="sub"><span class="lvtag">한 장으로</span></p></div>%s</div></section>\n'%(P['sumh'],P['sum'])
    o+='<section class="level" id="outro"><div class="wrap"><h2>오늘의 마무리</h2>'+''.join(say(*t) for t in P['outro'])+'</div></section>\n'
    o+=kgex()
    rows=''.join('<tr id="src-%s"><td class="num">[%d]</td><td>%s</td><td>%s</td></tr>'%(r,i+1,REFDB[r]['_row'],REFDB[r]['lab']['note']) for i,r in enumerate(P['refs']))
    o+='<footer><div class="wrap"><h3 id="sources">출처</h3><div class="tw"><table class="tb"><tr><th>#</th><th>문헌</th><th>메모</th></tr>%s<tr><td class="num">—</td><td>캐릭터 그림: adminmrobo/fruitfly-lab-expressions (86d04ac)</td><td>연구실 식구 공식 표정 그림</td></tr></table></div><h3>예시값 · 설명용 모형인 것</h3><ul>%s</ul>'%(rows,''.join('<li>%s</li>'%x for x in P['examples']))
    o+=nextprev(num)+'<p>글 · 안상선 (<a href="https://adminmrobo.github.io/who_am_i/who_am_i.html">소개</a>) · (주)M-Robo 대표 · %s %s · v1.0 · 2026-11-12 · <a href="index.html">시리즈 목차</a></p></div></footer>\n<div id="tip" role="tooltip"></div>'%(SERIES,num)
    return o
def cite(P,r): return '<a href="#src-%s">[%d]</a>'%(r,P['refs'].index(r)+1)
def kg(P):
    num=P['num']; pid='mem3_'+num; nodes=[]; edges=[]
    def N(id,typ,ko,en,anchor,d=None,**kw):
        n={'id':'lab:'+id,'type':typ,'label':{'ko':ko,'en':en},'page':pid,'anchor':anchor,'domain':['ai']+(['stats'] if num[0]=='1' else []),'status':kw.pop('status','known'),'confidence':kw.pop('confidence','high')}
        if d: n['definition']={'ko':d}
        n.update(kw); n['level']=1; nodes.append(n)
    def E(s,p,o,a,**kw): e={'s':'lab:'+s,'p':'lab:'+p,'o':'lab:'+o,'anchor':a,'confidence':'high'}; e.update(kw); edges.append(e)
    for t in P['nodes']: N(t[0],t[1],t[2],t[3],t[4],t[5] if len(t)>5 else None)
    sec='section/'+num+'/'
    secs=[('why',P['whyh'])]+[(L['id'],L['title']) for L in P['levels']]+([('vs','대결')] if P.get('duel') else [])+[('sum','정리')]
    for i,t in secs: N(sec+i,'Section',re.sub('<[^>]+>','',t),'','#'+i)
    q='question/mem-'+num+'-core'; N(q,'Question',P['q'],'','#top','이 페이지의 핵심 질문')
    for t in P.get('openq',[]): N(t[0],'Question',t[1],'',t[2],t[3],status='open')
    for i,(cid,text,anchor,ref,loc,sup) in enumerate(P.get('claims',[])):
        N(cid,'Claim',text,'',anchor,evidence=['F%02d'%(i+1)],source=[{'work':ref,'loc':loc,'verified':True}])
        E(cid,'supports',sup,anchor,evidence=['F%02d'%(i+1)]); E(cid,'assertedIn','work/'+ref,anchor,evidence=['F%02d'%(i+1)])
    for r in P['refs']: N('work/'+r,'Work',REFDB[r]['title'],REFDB[r]['title'] if REFDB[r]['title'].isascii() else '','#src-'+r)
    for L in P['levels']:
        for c in L.get('concepts',[]): E(c,'explainedIn',sec+L['id'],'#'+L['id'])
    for s,qs in P['quiz'].items():
        for i,qq in enumerate(qs):
            qid='quiz/mem-%s-%s-%d'%(num,s,i+1); N(qid,'QuizItem',(qq['q'][:34]+'…') if len(qq['q'])>34 else qq['q'],'','#'+s)
            if qq.get('t'): E(qid,'assesses',qq['t'],'#'+s)
    for t in P['edges']: E(*t)
    if P['nodes']: E(P['nodes'][0][0],'raises',q,'#top')
    return pid,{'version':'1.0','page':pid,'nodes':nodes,'edges':edges}
def refs(P):
    out=[]
    for r in P['refs']:
        d={k:v for k,v in REFDB[r].items() if k!='_row'}; d['lab']=dict(d['lab']); cl=[c for c in P.get('claims',[]) if c[3]==r]
        d['lab']['supports']=['lab:'+c[0] for c in cl]; d['lab']['locs']=[{'claim':'lab:'+c[0],'loc':c[4]} for c in cl]; d['lab']['role']='primary' if cl else 'background'; out.append(d)
    return out
def assemble(fname,num,title,desc,bodyhtml,pjs,G,core,quiz,anchor,KG,REFS,META):
    pack=json.load(open(os.path.join(B,'lab_pack.json'),encoding='utf-8')); alias=pack['alias']; img=pack['img']
    need=set(re.findall(r'data-who="(\w+)" data-mood="(\w+)"',bodyhtml))
    duel={'fly':['arms','sigh','coffee','cry','point'],'robo':['coffee','cry','happy','meh','blush','coin'],'doc':['judge','think','front'],'asst':['spark','smile','shock','firm'],'sia':['signal','proud','stop'],'moa':['cheer','tea']}
    if 'class="duel"' in bodyhtml:
        for w,ms in duel.items(): need|={(w,m) for m in ms}
    for w,m in re.findall(r"Cast\.set\([^,]+,'(\w+)','(\w+)'\)",pjs): need.add((w,m))
    keys=set(); al={}; miss=[]
    for w,m in sorted(need):
        k=w+'_'+m; r=alias.get(k,k)
        if r in img: keys.add(r); al.update({k:r} if r!=k else {})
        else: miss.append(k)
        keys.add(w+'_e13')
    sprite={k:img[k] for k in sorted(keys)}; facing={k:v for k,v in pack.get('facing',{}).items() if k in sprite}
    ids=[n['id'] for n in KG['nodes']]; assert len(ids)==len(set(ids)),('중복 노드',[i for i in ids if ids.count(i)>1])
    for e in KG['edges']: assert e['s'] in ids and e['o'] in ids,('끊긴 관계',e)
    lib=rd(os.path.join(B,'lib_core.js'))+'\n'+rd(os.path.join(B,'mem_lib.js'))
    node_src="global.document={documentElement:{lang:'ko'}};global.window={};global.IntersectionObserver=function(){this.observe=function(){};};\n"+lib+"\nprocess.stdout.write(JSON.stringify(toJsonLd(JSON.parse(require('fs').readFileSync(0,'utf8')),%s)));"%json.dumps(META,ensure_ascii=False)
    r=subprocess.run(['node','-e',node_src],input=json.dumps(KG,ensure_ascii=False),capture_output=True,text=True)
    if r.returncode: print(r.stderr[-600:]); raise SystemExit(1)
    esc=lambda o: json.dumps(o,ensure_ascii=False).replace('</','<\\/')
    css=rd(os.path.join(B,'base.css'))+'\n'+rd(os.path.join(B,'plain.css')); t=html.escape(META['title']); part=num[0]
    head=('<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
     '<title>%s %s · 기억 3부작</title><meta name="description" content="%s">'%(num,html.escape(info(num)[2]),html.escape(desc))+
     '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:type" content="article"><meta property="og:image" content="%sassets/img/og_ch%s.jpg">'%(t,html.escape(desc),BASE,part)+
     '<meta name="citation_title" content="%s"><meta name="citation_author" content="안상선"><meta name="citation_publication_date" content="2026/11/12">'%t+
     '<meta name="dc.title" content="%s"><meta name="dc.creator" content="안상선"><meta name="dc.date" content="2026-11-12"><meta name="dc.language" content="ko"><meta name="dc.relation.ispartof" content="%s">'%(t,html.escape(SERIES))+
     '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">'
     '<style>'+css+'</style></head>')
    out=(head+'<body>'+bodyhtml.strip()+'\n<script type="application/json" id="kg-raw">'+esc(KG)+'</script>\n<script type="application/ld+json" id="kg-ld">'+r.stdout.replace('</','<\\/')+'</script>'
     '\n<script type="application/json" id="refs-csl">'+esc(REFS)+'</script>\n<script type="application/json" id="page-meta">'+esc(META)+'</script>'
     '\n<script>\nvar SPRITE='+json.dumps(sprite)+';\nvar SPRITE_ALIAS='+json.dumps(al)+';\nvar SPRITE_FACING='+json.dumps(facing)+';\n'+lib+
     '\n/* ===== 페이지 스크립트 ===== */\nvar PAGE='+esc({'anchor':anchor,'gloss':G,'core':core,'quiz':quiz})+';\n'+pjs+'\nLabStart(PAGE);\n</script></body></html>')
    os.makedirs(os.path.join(ROOT,'out'),exist_ok=True); fp=os.path.join(ROOT,'out',fname); open(fp,'w',encoding='utf-8').write(out)
    print(fname,len(out.encode())//1024,'KB · 그림',len(sprite),'· 없는 표정',miss,'· 노드',len(KG['nodes']),'· 관계',len(KG['edges']))
def load(path):
    spec=importlib.util.spec_from_file_location('m',path); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def meta(num,title,about,refids):
    f=info(num)[1]
    return {'id':'ahn2026mem3_'+num.replace('-','_'),'title':'기억 3부작 %s — %s'%(num,title),'series':SERIES,'number':num,'creator':[{'name':'안상선','role':'author'}],'contributor':[{'name':'AI 보조 제작','role':'assistant'}],
     'date':'2026-11-12','version':'1.0','language':['ko'],'license':'','url':BASE+f,'about':about,'educationalLevel':'입문','learningResourceType':'interactive explainer','basedOn':refids,'registryVersion':'mem3-reg-1.0',
     'suggestedCitation':'안상선 (2026). 기억 3부작 %s — %s. %s %s, v1.0.'%(num,title,SERIES,num)}
def build(key):
    num=key.replace('_','-')
    if key=='1_1':
        D=load(os.path.join(ROOT,'_src','1_1','data.py')); b=rd(os.path.join(ROOT,'_src','1_1','body.html')).replace('{{PAGER}}',pager(num)).replace('{{NEXTPREV}}',nextprev(num))
        pjs=rd(os.path.join(ROOT,'_src','1_1','page.js')).replace('\nLabStart(PAGE);','')
        return assemble(D.FILE,num,D.TITLE,D.DESC,b,pjs,D.G,D.CORE,D.QUIZ,D.ANCHOR,{'version':'1.0','page':D.PID,'nodes':D.NODES,'edges':D.EDGES},D.REFS,D.META)
    m=load(os.path.join(ROOT,'_src','p'+key+'.py')); P=m.P; P['num']=num
    for k,v in list(P.items()):
        if isinstance(v,str): P[k]=re.sub(r'\[\[(\w+)\]\]',lambda mm:cite(P,mm.group(1)),v)
    b=re.sub(r'\[\[(\w+)\]\]',lambda mm:cite(P,mm.group(1)),body(P)); pid,KG=kg(P)
    quiz={s:[{k:v for k,v in q.items() if k!='t'} for q in qs] for s,qs in P['quiz'].items()}
    assemble(info(num)[1],num,P['title'],re.sub('<[^>]+>','',P['q']),b,'PAGE.page=function(){\n'+m.JS+'\n};',P['gloss'],P['core'],quiz,P.get('anchor','C'),KG,refs(P),meta(num,P['title'],['lab:'+n[0] for n in P['nodes'][:5]],P['refs']))
if __name__=='__main__':
    ks=sorted(built()) if sys.argv[1:]==['all'] else sys.argv[1:]
    for k in ks: build(k)
