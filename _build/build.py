# -*- coding: utf-8 -*-
"""기억 3부작 빌드: python3 _build/build.py 1_1  →  out/<FILE>"""
import sys,os,re,json,subprocess,importlib.util,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B=os.path.join(ROOT,'_build')
def rd(p): return open(p,encoding='utf-8').read()
def main(key):
    src=os.path.join(ROOT,'_src',key)
    spec=importlib.util.spec_from_file_location('d',os.path.join(src,'data.py')); D=importlib.util.module_from_spec(spec); spec.loader.exec_module(D)
    body=rd(os.path.join(src,'body.html')); pjs=rd(os.path.join(src,'page.js'))
    pack=json.load(open(os.path.join(B,'lab_pack.json'),encoding='utf-8')); alias=pack['alias']; img=pack['img']
    # 필요한 그림 키
    need=set(re.findall(r'data-who="(\w+)" data-mood="(\w+)"',body))
    duel={'fly':['arms','sigh','coffee','cry','point'],'robo':['coffee','cry','happy','meh','blush','coin'],'doc':['judge','think','front'],'asst':['spark','smile','shock','firm'],'sia':['signal','proud','stop'],'moa':['cheer','tea']}
    if 'class="duel"' in body:
        for w,ms in duel.items(): need|={(w,m) for m in ms}
    whos={w for w,_ in need}
    keys=set(); al={}; miss=[]
    for w,m in sorted(need):
        k=w+'_'+m; r=alias.get(k,k)
        if r in img: keys.add(r); 
        else: miss.append(k); r=None
        if r and r!=k: al[k]=r
    for w in whos: keys.add(w+'_e13')
    sprite={k:img[k] for k in sorted(keys)}
    facing={k:v for k,v in pack.get('facing',{}).items() if k in sprite}
    kg={'version':'1.0','page':D.PID,'nodes':D.NODES,'edges':D.EDGES}
    ids={n['id'] for n in kg['nodes']}
    for e in kg['edges']:
        assert e['s'] in ids and e['o'] in ids,('끊긴 관계',e)
    assert len(ids)==len(kg['nodes']),'중복 노드'
    page={'anchor':D.ANCHOR,'gloss':D.G,'core':D.CORE,'quiz':D.QUIZ}
    lib=rd(os.path.join(B,'lib_core.js'))
    # kg-ld는 공용 모듈의 toJsonLd로 만든다
    node_src="global.document={documentElement:{lang:'ko'}};global.window={};global.IntersectionObserver=function(){this.observe=function(){};};\n"+lib+"\nprocess.stdout.write(JSON.stringify(toJsonLd(JSON.parse(require('fs').readFileSync(0,'utf8')),%s)));"%json.dumps(D.META,ensure_ascii=False)
    try:
        ld=subprocess.run(['node','-e',node_src],input=json.dumps(kg,ensure_ascii=False),capture_output=True,text=True,check=True).stdout
    except subprocess.CalledProcessError as ex:
        print(ex.stderr[-800:]); raise
    esc=lambda o: json.dumps(o,ensure_ascii=False).replace('</','<\\/')
    css=rd(os.path.join(B,'base.css'))+'\n'+rd(os.path.join(B,'plain.css'))
    t=html.escape(D.META['title']); 
    head=('<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
     '<title>%s %s · 기억 3부작</title><meta name="description" content="%s">'%(D.NUM,html.escape(D.TITLE.split(' — ')[0]),html.escape(D.DESC))+
     '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:type" content="article"><meta property="og:image" content="https://adminmrobo.github.io/llm_memory_trilogy/assets/img/og_ch1.jpg">'%(t,html.escape(D.DESC))+
     '<meta name="citation_title" content="%s"><meta name="citation_author" content="안상선"><meta name="citation_publication_date" content="%s">'%(t,D.DATE.replace('-','/'))+
     '<meta name="dc.title" content="%s"><meta name="dc.creator" content="안상선"><meta name="dc.date" content="%s"><meta name="dc.language" content="ko"><meta name="dc.relation.ispartof" content="%s">'%(t,D.DATE,html.escape(D.SERIES))+
     '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">'
     '<style>'+css+'</style></head>')
    out=(head+'<body>'+body.strip()+
     '\n<script type="application/json" id="kg-raw">'+esc(kg)+'</script>'
     '\n<script type="application/ld+json" id="kg-ld">'+ld.replace('</','<\\/')+'</script>'
     '\n<script type="application/json" id="refs-csl">'+esc(D.REFS)+'</script>'
     '\n<script type="application/json" id="page-meta">'+esc(D.META)+'</script>'
     '\n<script>\nvar SPRITE='+json.dumps(sprite)+';\nvar SPRITE_ALIAS='+json.dumps(al)+';\nvar SPRITE_FACING='+json.dumps(facing)+';\n'+lib+
     '\n/* ===== 페이지 스크립트 ===== */\nvar PAGE='+esc(page)+';\n'+pjs+'\n</script></body></html>')
    os.makedirs(os.path.join(ROOT,'out'),exist_ok=True)
    fp=os.path.join(ROOT,'out',D.FILE); open(fp,'w',encoding='utf-8').write(out)
    print(fp,len(out.encode())//1024,'KB','그림',len(sprite),'개','없는 표정',miss,'노드',len(kg['nodes']),'관계',len(kg['edges']))
if __name__=='__main__': main(sys.argv[1])
