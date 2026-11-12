/* ===== 공용: 도우미 ===== */
function rng(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);
  t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function gauss(r){var u=0;while(!u)u=r();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*r())}
function sig(z){return 1/(1+Math.exp(-z))}
function tanh(z){var e=Math.exp(2*z);return (e-1)/(e+1)}
function clamp(v,a,b){return v<a?a:v>b?b:v}
function $(s,r){return (r||document).querySelector(s)}
function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))}
function f2(v,d){return (v===null||v===undefined||isNaN(v))?'–':Number(v).toFixed(d===undefined?2:d)}
function fit(c,h){var d=window.devicePixelRatio||1, w=c.clientWidth||c.parentElement.clientWidth||600;
  if(c.width!==Math.round(w*d)||c.height!==Math.round(h*d)){c.width=Math.round(w*d);c.height=Math.round(h*d);c.style.height=h+'px';}
  var x=c.getContext('2d'); x.setTransform(d,0,0,d,0,0); return w;}
var REDUCE=(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches);
var LANG=((document.documentElement&&document.documentElement.lang)||'ko').slice(0,2);
// 통째 문장 틀: tpl('노드 {0}개 · 관계 {1}개', a, b) — 번역 때 어순을 바꿀 수 있게 조각 이어 붙이기 대신 쓴다
function tpl(s){var a=arguments;return String(s).replace(/\{(\d+)\}/g,function(m,i){return String(a[+i+1]);});}
function lab(n){return (n.label&&(n.label[LANG]||(LANG!=='ko'&&n.label.en)||n.label.ko))||'';}
function defn(n){return n.definition?(n.definition[LANG]||n.definition.ko||''):'';}
var FONT='"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",system-ui,sans-serif';
var COL={bg:'#13141f',panel:'#1c1e2d',panel2:'#25283a',rule:'#363a52',text:'#eceaf3',muted:'#9d9bb8',
  stain:'#d672d6',gfp:'#5ee39c',eye:'#f0604d',amber:'#f1b646',info:'#82b8ff',fly:'#ef5b5b',robo:'#57d0dc',doc:'#b07cff',asst:'#ff86b8'};

/* ===== 보이는 캔버스만 그리는 루프 (B-2) ===== */
var mods=[], vis=new Set(), io=new IntersectionObserver(function(es){
  es.forEach(function(e){ e.isIntersecting?vis.add(e.target):vis.delete(e.target); });},{rootMargin:'100px'});
function addMod(el,fn){mods.push({el:el,fn:fn}); io.observe(el);}
var _last=0;
function _loop(ts){var dt=_last?Math.min(0.05,(ts-_last)/1000):0.016; _last=ts;
  mods.forEach(function(m){ if(vis.has(m.el)) m.fn(dt); }); requestAnimationFrame(_loop);}
function drawAll(){mods.forEach(function(m){try{m.fn(0);}catch(e){console.error(e);}});}

/* ===== 도장 (B-7) ===== */
function stamp(ctx,W,txt){ctx.save(); ctx.font='700 11px '+FONT;
  var tw=ctx.measureText(txt).width+16, x=W-tw-8, y=8;
  ctx.fillStyle='rgba(241,182,70,.14)'; ctx.strokeStyle='rgba(241,182,70,.7)';
  ctx.beginPath(); ctx.roundRect?ctx.roundRect(x,y,tw,20,10):ctx.rect(x,y,tw,20); ctx.fill(); ctx.stroke();
  ctx.fillStyle='#f1b646'; ctx.textAlign='left'; ctx.textBaseline='alphabetic'; ctx.fillText(txt,x+8,y+14); ctx.restore();}

/* ===== 픽셀 지도 (부록 A, 행동으로 보기·히어로 전용) ===== */
var PAL={K:'#1d1a22',W:'#eceaf3',R:'#e04a3a',r:'#a8281c',U:'#23467e',Y:'#f1c84a',L:'#5a4636',S:'rgba(0,0,0,.35)',
  B:'#3fb8f0',F:'#f6d3b8',G:'#1e6e73',P:'#ff86b8',N:'#2b3a7a',V:'#b9a6e8',O:'#d4a54a',
  E:'#eadfc6',D:'#17352c',M:'#5befa5',A:'#8b5a2b',Q:'#d2603c',H:'#9c978c'};  // E~H: 주판봇
var FLY_MAP=['....K......K....','.....K....K.....','....UUUUUUUU....','...UUYUUUUYUU...','..RRRUUUUUURRR..','.RRrRRKKKKRRrRR.','.RRRRKKKKKKRRRR.','..RRKKKKKKKKRR..','WW..WKKKKKKW..WW','WWW.WWKKKKWW.WWW','.WWWWWKKKKWWWWW.','..L.WWKKKKWW.L..','.L...WKKKKW...L.','L.....KKKK.....L','.......KK.......','................'];
var ROBO_MAP=['.......Q........','.......K........','..KKKKKKKKKKKK..','..KEEEEEEEEEEK..','..KEDDDDDDDDEK..','..KEDMDDDDMDEK..','..KEDDDDDDDDEK..','..KEDMDDDDMDEK..','..KEDDMMMMDDEK..','.HKEEEEEEEEEEKH.','HHAAAAAAAAAAAAHH','HHAEQEQEEQEQEAHH','..AAAAAAAAAAAA..','..AEQEQEEQEQEA..','..AAAAAAAAAAAA..','.KKKK......KKKK.'];  // 주판봇 (캐릭터 팩 CHAR_lab4 A-3)
var DOC_MAP=['....KKKKKKK.....','...KKKWKKKKK....','..KKKWWKKKKKK...','..KFFFFFFFFFK...','..FGGFFFFGGFF...','..FGKFFFFGKFF...','..FFFFFFFFFFF...','...FFFRRRFFF....','....FFFFFFF.....','...WWWKKKWWW....','..WWWWKRKWWWW...','..WWWWKRKWWWW...','..WFWWKKKWWFW...','..WWWWKKKWWWW...','...LL.....LL....','...KK.....KK....'];
var ASST_MAP=['.PP..........PP.','.PP..PPPPPP..PP.','PPPPPPPPPPNPPPPP','.PPPPFFFFFFPPPP.','..PPFFFFFFFFPP..','..PFFBFFFFBFFP..','..PFFBFFFFBFFP..','..PFFFFFFFFFFP..','...FFFFRRFFFF...','....FFFFFFFF....','...WWVVVVVVWW...','..WWWVVVVVVWWW..','..WWWVVVVVVWWW..','..WFWVVVVVVWFW..','...NN......NN...','...NN......NN...'];
function spriteFromMap(rows,pal){var h=rows.length,w=rows[0].length,cv=document.createElement('canvas');
  cv.width=w;cv.height=h;var c=cv.getContext('2d');
  rows.forEach(function(r,y){r.split('').forEach(function(ch,x){if(ch==='.')return;c.fillStyle=pal[ch];c.fillRect(x,y,1,1);});});return cv;}
function drawSprite(ctx,cv,x,y,scale,flip){ctx.save();ctx.imageSmoothingEnabled=false;ctx.translate(x,y);if(flip)ctx.scale(-1,1);
  ctx.drawImage(cv,-cv.width*scale/2,-cv.height*scale/2,cv.width*scale,cv.height*scale);ctx.restore();}
var PXS={};
function px(who){if(!PXS[who])PXS[who]=spriteFromMap({fly:FLY_MAP,robo:ROBO_MAP,doc:DOC_MAP,asst:ASST_MAP}[who],PAL);return PXS[who];}

/* ===== 캐릭터 (B-4) ===== */
var Cast=(function(){
  var DEFAULT={doc:'doc_e13',asst:'asst_e13',fly:'fly_e13',robo:'robo_e13',sia:'sia_e13',moa:'moa_e13',x1:'x1_e13',x2:'x2_e13',x3:'x3_e13'};
  function resolve(who,mood){var k=who+'_'+(mood||''); k=SPRITE_ALIAS[k]||k;
    if(SPRITE[k]) return k; return SPRITE[DEFAULT[who]]?DEFAULT[who]:null;}
  var PXW={doc:1,asst:1,fly:1,robo:1};
  function pixel(who){var big=document.createElement('canvas');big.width=64;big.height=64;var b=big.getContext('2d');
    b.imageSmoothingEnabled=false;b.drawImage(px(who),0,0,64,64);return big.toDataURL();}
  function apply(img,who,mood){var k=resolve(who,mood), s=k?SPRITE[k]:(PXW[who]?pixel(who):null);
    if(s){img.src=s;img.style.visibility='';}else{img.removeAttribute('src');img.style.visibility='hidden';}
    if(k) img.dataset.img=k;
    var want=img.dataset.face, has=(k&&SPRITE_FACING[k])||'front';
    img.style.transform=(want&&has!=='front'&&want!==has)?'scaleX(-1)':'';}
  function set(img,who,mood){img.style.transition='opacity .2s';img.style.opacity=0;
    setTimeout(function(){apply(img,who,mood);img.style.opacity=1;},REDUCE?0:200);}
  function fill(){$$('img[data-who]').forEach(function(i){apply(i,i.dataset.who,i.dataset.mood||'');});}
  return {set:set,fill:fill,key:resolve};
})();

/* ===== 용어 말풍선 (11-2) ===== */
function Gloss(dict,opt){
  opt=opt||{}; var core=opt.core||[];
  var terms=Object.keys(dict).filter(function(t){return t.length>=2||/[^\x00-\x7f]/.test(t);}).sort(function(a,b){return b.length-a.length;});
  if(!terms.length) return;
  var KO=(LANG==='ko'),DL={};Object.keys(dict).forEach(function(k){DL[k.toLowerCase()]=dict[k];});var CORE=core.map(function(c){return c.toLowerCase();});
  var re=new RegExp('('+terms.map(function(t){var e=t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');return (!KO&&/^[\x00-\x7f]+$/.test(t))?'\\b'+e+'\\b':e;}).join('|')+')',KO?'':'i');
  var SKIP=['BUTTON','H1','H2','NAV','CANVAS','SVG','SCRIPT','STYLE','A','TEXTAREA','INPUT','PRE','CODE','SUMMARY'];
  $$(opt.scope||'section, header.hero, footer').forEach(function(scope){
    if(scope.closest('#kg,#export')) return;
    var seen={}, walker=document.createTreeWalker(scope,NodeFilter.SHOW_TEXT,{acceptNode:function(n){
      var p=n.parentElement; if(!p) return NodeFilter.FILTER_REJECT;
      if(p.closest('.kpis,.jt,.qwho,.lvtag,.chip,svg,#kg,#export,.duel .bars,[data-nogloss]')) return NodeFilter.FILTER_REJECT;
      for(var e=p;e&&e!==scope;e=e.parentElement){ if(SKIP.indexOf(e.tagName)>=0) return NodeFilter.FILTER_REJECT; }
      return re.test(n.nodeValue)?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT;}});
    var list=[],n; while((n=walker.nextNode())) list.push(n);
    list.forEach(function(node){
      var txt=node.nodeValue, frag=document.createDocumentFragment(), changed=false, rest=txt, m;
      while((m=rest.match(re))){
        var t=m[1], i=m.index, tk=t.toLowerCase(); if(seen[tk]){ frag.appendChild(document.createTextNode(rest.slice(0,i+t.length))); rest=rest.slice(i+t.length); continue; }
        seen[tk]=1; changed=true;
        frag.appendChild(document.createTextNode(rest.slice(0,i)));
        var s=document.createElement('span'); s.className='jt'; s.tabIndex=0; s.textContent=t; s.dataset.term=t;
        if(CORE.indexOf(tk)>=0) s.dataset.core='1'; frag.appendChild(s); rest=rest.slice(i+t.length);
      }
      frag.appendChild(document.createTextNode(rest));
      if(changed) node.parentNode.replaceChild(frag,node);
    });
  });
  var tip=$('#tip');
  function show(el){ if(document.body.classList.contains('gl-off')) return;
    if(document.body.classList.contains('gl-core')&&!el.dataset.core) return;
    var d=dict[el.dataset.term]||DL[el.dataset.term.toLowerCase()]; if(!d) return;
    tip.innerHTML='<b>'+d[0]+'</b> <small>'+d[1]+'</small>'+d[2]; tip.style.display='block';
    var r=el.getBoundingClientRect(), tw=Math.min(300,window.innerWidth-16);
    tip.style.left=clamp(r.left,8,window.innerWidth-tw-8)+'px';
    var top=r.bottom+8; if(top+tip.offsetHeight>window.innerHeight-8) top=r.top-tip.offsetHeight-8;
    tip.style.top=top+'px'; tip._el=el;}
  function hide(){tip.style.display='none'; tip._el=null;}
  document.addEventListener('pointerover',function(e){var t=e.target.closest&&e.target.closest('.jt'); if(t&&e.pointerType==='mouse') show(t);});
  document.addEventListener('pointerout',function(e){var t=e.target.closest&&e.target.closest('.jt'); if(t&&e.pointerType==='mouse') hide();});
  document.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('.jt'); if(t){ if(tip._el===t) hide(); else show(t);} else if(!e.target.closest('#tip')) hide();});
  document.addEventListener('focusin',function(e){if(e.target.classList&&e.target.classList.contains('jt')) show(e.target);});
  document.addEventListener('focusout',function(e){if(e.target.classList&&e.target.classList.contains('jt')) hide();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape') hide();});
  window.addEventListener('scroll',hide,{passive:true});
}

/* ===== 학습 도우미·퀴즈 (11-3, 11-4) ===== */
function Study(o){
  var solved={}, total=0, mode=['core','all','off'], mi=0, LBL={core:'핵심',all:'전체',off:'끄기'};
  document.body.classList.add('gl-core');
  Object.keys(o.quiz||{}).forEach(function(id){
    var box=document.querySelector('.quiz[data-quiz="'+id+'"]'); if(!box) return;
    o.quiz[id].forEach(function(q,qi){ total++; var key=id+'_'+qi;
      var d=document.createElement('div'); d.className='qi';
      d.innerHTML=tpl('<div class="qh">확인 퀴즈 {0}{1}</div><p class="qq"></p><div class="opts" role="group"></div><div class="fb" aria-live="polite"></div>',qi+1,q.kind?' · '+q.kind:'');
      d.querySelector('.qq').textContent=q.q;
      var opts=d.querySelector('.opts'), fb=d.querySelector('.fb');
      q.o.forEach(function(t,oi){var b=document.createElement('button'); b.type='button'; b.textContent=t;
        b.addEventListener('click',function(){
          if(oi===q.a){ b.classList.add('ok'); fb.className='fb ok'; fb.textContent=tpl('정답이에요. {0}',q.why);
            if(!solved[key]){solved[key]=1; upd();} $$('button',opts).forEach(function(x){x.disabled=true;}); }
          else { b.classList.add('no'); fb.className='fb no'; fb.textContent=tpl('힌트: {0}',q.hint); }
        }); opts.appendChild(b);});
      box.appendChild(d);});
  });
  var st=document.createElement('div'); st.id='study'; st.setAttribute('aria-live','polite');
  st.innerHTML=tpl('<span>읽은 곳 <b id="stR">0%</b> · 퀴즈 <b id="stQ">0/{0}</b></span><button type="button" id="stG">밑줄: 핵심</button>',total);
  document.body.appendChild(st);
  $('#stG').addEventListener('click',function(){ document.body.classList.remove('gl-'+mode[mi]); mi=(mi+1)%3;
    document.body.classList.add('gl-'+mode[mi]); this.textContent=tpl('밑줄: {0}',LBL[mode[mi]]); });
  function upd(){$('#stQ').textContent=Object.keys(solved).length+'/'+total;}
  function sc(){var h=document.documentElement, p=h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight);
    $('#prog').style.width=(p*100).toFixed(1)+'%'; $('#stR').textContent=Math.round(p*100)+'%';}
  window.addEventListener('scroll',sc,{passive:true}); sc();
}

/* ===== 대결 (B-5, 6장) ===== */
function Duel(o){
  var root=$(o.el), shown=false, guess=null;
  var flyImg=root.querySelector('.vs img[data-who=fly]'), roboImg=root.querySelector('.vs img[data-who=robo]');
  var fmt=o.fmt||function(v){return f2(v,2);};
  $$('.guess button',root).forEach(function(b){b.addEventListener('click',function(){
    guess=b.dataset.g; $$('.guess button',root).forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false');});
    root.querySelector('.guess .gl').textContent=tpl('{0} 쪽을 골랐어요. 결과를 열어 보세요.',guess==='F'?'초파리':'주판봇');});});
  function bar(name,v,max,c){var w=max>0?Math.max(2,v/max*100):2;
    return '<div class="bar"><span>'+name+'</span><div class="trk"><div class="fill" style="width:'+w.toFixed(1)+'%;background:'+c+'"></div></div><b>'+fmt(v)+'</b></div>';}
  var btn=root.querySelector('.reveal');
  btn.addEventListener('click',function(){
    if(shown){reset();return;}
    btn.disabled=true; btn.textContent='계산 중…';
    setTimeout(function(){
      var r=o.run(), f=r.fly, b=r.robo, d=o.higherIsBetter?f-b:b-f, res;
      if(r.foul) res='X'; else if(Math.abs(f-b)<=o.drawMargin*Math.max(Math.abs(f),Math.abs(b))) res='D'; else res=d>0?'F':'R';
      var big=Math.abs(f-b)/Math.max(Math.abs(f),Math.abs(b),1e-9)>=0.10;
      var M={F:['arms','sigh','judge','spark'],R:[big?'cry':'coffee','happy','judge','spark'],D:['coffee','meh','think','smile'],X:['arms','blush','judge','shock']}[res];
      Cast.set(flyImg,'fly',M[0]); Cast.set(roboImg,'robo',M[1]);
      var dImg=root.querySelector('.verdict img'), aImg=root.querySelector('.asst img');
      if(dImg) Cast.set(dImg,'doc',M[2]); if(aImg) Cast.set(aImg,'asst',M[3]);
      var mx=Math.max(f,b);
      root.querySelector('.bars').innerHTML=bar('초파리',f,mx,COL.fly)+bar('주판봇',b,mx,COL.robo);
      root.querySelector('.asst p').textContent=o.say?o.say(f,b,r):(tpl('{0}은 초파리 쪽 {1}, 주판봇 쪽 {2}이에요.',r.metric,fmt(f),fmt(b)));
      var who={F:'초파리 승.',R:'주판봇 승.',D:'이번 판은 나눠 갖는다.',X:'규칙 위반으로 주판봇 실격.'}[res];
      root.querySelector('.verdict p').textContent=(o.lessons&&o.lessons[res]?o.lessons[res]:o.lesson)+(/^(zh|ja)$/.test(LANG)?'\u3002':'. ')+who;
      var g=root.querySelector('.guess .gl'); if(guess) g.textContent=tpl('{0}실제 결과: {1}',guess===res?'맞혔어요! ':'예상과 달랐어요. ',{F:'초파리 승',R:'주판봇 승',D:'무승부',X:'실격'}[res]);
      var ref=root.querySelector('.ref p'), rImg=root.querySelector('.ref img');
      if(ref) ref.textContent={F:'판정 확인했습니다. 초파리 연구원 쪽 깃발을 올립니다.',R:'판정 확인했습니다. 주판봇 쪽 깃발을 올립니다.',D:'판정 확인했습니다. 양쪽 깃발을 함께 올립니다.',X:'반칙 확인했습니다. 경기를 멈춥니다.'}[res];
      if(rImg) Cast.set(rImg,'sia',res==='X'?'stop':'proud');
      var mo=root.querySelector('.crowd [data-c=moa]'), mImg=root.querySelector('.crowd img[data-who=moa]');
      if(mo) mo.textContent={F:'초파리 연구원님 축하드려요! 주판봇님도 차 한 잔 하실래요?',R:'주판봇님 축하드려요! 초파리 연구원님도 차 한 잔 하실래요?',D:'두 분 다 수고하셨어요. 차는 두 잔 준비할게요.',X:'괜찮으세요? 차 한 잔 하고 다시 해요.'}[res];
      if(mImg) Cast.set(mImg,'moa','tea');
      $$('.crowd figure.x .cl',root).forEach(function(e,i){e.textContent=['(짝짝)','(반짝반짝)','(오오…)'][i];});
      if(o.after) o.after(r,res);
      root.classList.add('open'); shown=true; btn.disabled=false; btn.textContent='다시 닫기';
    },30);
  });
  function reset(){Cast.set(flyImg,'fly','point');Cast.set(roboImg,'robo','coin');
    var dImg=root.querySelector('.verdict img'), aImg=root.querySelector('.asst img');
    if(dImg) Cast.set(dImg,'doc','front'); if(aImg) Cast.set(aImg,'asst','firm');
    var ref=root.querySelector('.ref p'), rImg=root.querySelector('.ref img');
    if(ref) ref.textContent='확인했습니다. 같은 기간, 같은 지표, 같은 시드로 시작합니다.'; if(rImg) Cast.set(rImg,'sia','signal');
    var mo=root.querySelector('.crowd [data-c=moa]'), mImg=root.querySelector('.crowd img[data-who=moa]');
    if(mo) mo.textContent='두 분 다 힘내세요!'; if(mImg) Cast.set(mImg,'moa','cheer');
    $$('.crowd figure.x .cl',root).forEach(function(e,i){e.textContent=['(…)','(반짝)','(두근)'][i];});
    root.classList.remove('open');shown=false;btn.textContent='결과 보기';}
}

/* ===== 시계열 도구 ===== */
var DAY0=Date.UTC(2026,1,2); // 2026-02-02 = 1번째 날
function dayLabel(i){var d=new Date(DAY0+i*864e5);return (d.getUTCMonth()+1)+'/'+d.getUTCDate();}
// 매출 기록 시계열: 수준 + 추세 + 주간·월간 패턴 + AR(1) 잡음
function makeSeries(seed,n,o){o=o||{}; var r=rng(seed), y=[], e=0;
  var wk=o.weekly===undefined?[0,4,6,5,3,-7,-11]:o.weekly;
  for(var t=0;t<n;t++){ e=(o.phi===undefined?0.5:o.phi)*e+(o.sd===undefined?3:o.sd)*gauss(r);
    var v=(o.level===undefined?100:o.level)+(o.trend||0)*t+(wk.length?wk[t%7]*(o.wAmp===undefined?1:o.wAmp):0)
      +(o.mAmp?o.mAmp*Math.sin(2*Math.PI*t/30.4):0)+e;
    if(o.f) v=o.f(t,y,r,v);
    y.push(v);}
  return y;}
function solve(A,b){var n=b.length,M=A.map(function(r,i){return r.concat([b[i]]);});
  for(var c=0;c<n;c++){var p=c;for(var i=c+1;i<n;i++)if(Math.abs(M[i][c])>Math.abs(M[p][c]))p=i;
    var t=M[c];M[c]=M[p];M[p]=t; var d=M[c][c]||1e-12;
    for(var j=c;j<=n;j++)M[c][j]/=d;
    for(i=0;i<n;i++)if(i!==c){var f=M[i][c];if(f)for(j=c;j<=n;j++)M[i][j]-=f*M[c][j];}}
  return M.map(function(r){return r[n];});}
// AR(p) 최소제곱: 정답 시점 t ∈ [p+from, to) — 앞 p개는 입력으로만 쓰인다
function fitAR(y,p,from,to,lam){from=from||0;to=to===undefined?y.length:to;lam=lam||1e-6;
  var k=p+1, A=[], b=[], i,j,t; for(i=0;i<k;i++){A.push(new Array(k).fill(0));b.push(0);}
  var n=0;
  for(t=from+p;t<to;t++){var x=[1];for(j=1;j<=p;j++)x.push(y[t-j]);
    for(i=0;i<k;i++){b[i]+=x[i]*y[t];for(j=0;j<k;j++)A[i][j]+=x[i]*x[j];} n++;}
  for(i=1;i<k;i++)A[i][i]+=lam*n;
  var beta=solve(A,b); return {c:beta[0],phi:beta.slice(1),p:p,n:n};}
function arPred(m,hist,t){var v=m.c;for(var j=1;j<=m.p;j++)v+=m.phi[j-1]*hist[t-j];return v;}
// 굴려 가며 예측: 매일 실제값을 보고 다음 날 하나 예측
function rollingAR(m,y,from,to){var out=[];for(var t=from;t<to;t++)out.push(arPred(m,y,t));return out;}
// 한 번에 예측: from 시점 이후는 예측값을 다시 입력으로
function multiAR(m,y,from,h){var hist=y.slice(0,from),out=[];
  for(var s=0;s<h;s++){var v=arPred(m,hist,from+s);hist.push(v);out.push(v);}return out;}
// 예측구간: 훈련 잔차 표준편차와 ψ 가중치 (정상 AR 가정)
function arSigma(m,y,from,to){var s=0,n=0;for(var t=from+m.p;t<to;t++){var e=y[t]-arPred(m,y,t);s+=e*e;n++;}return Math.sqrt(s/Math.max(1,n-m.p-1));}
function arPsi(m,H){var psi=[1];for(var j=1;j<H;j++){var v=0;for(var i=1;i<=Math.min(j,m.p);i++)v+=m.phi[i-1]*psi[j-i];psi.push(v);}return psi;}
function arBand(m,sig,h){var psi=arPsi(m,h),c=0,out=[];for(var j=0;j<h;j++){c+=psi[j]*psi[j];out.push(1.96*sig*Math.sqrt(c));}return out;}
function mae(a,b){var s=0;for(var i=0;i<a.length;i++)s+=Math.abs(a[i]-b[i]);return s/a.length;}
function rmse(a,b){var s=0;for(var i=0;i<a.length;i++)s+=(a[i]-b[i])*(a[i]-b[i]);return Math.sqrt(s/a.length);}
function mean(a){var s=0;a.forEach(function(v){s+=v;});return s/a.length;}
function std(a){var m=mean(a),s=0;a.forEach(function(v){s+=(v-m)*(v-m);});return Math.sqrt(s/a.length);}

/* ===== 작은 LSTM (설명용, 순수 JS) ===== */
function LSTM(H,seed,D){D=D||1; var r=rng(seed), K=D+H, s=1/Math.sqrt(K);
  var m={H:H,D:D,W:new Float64Array(4*H*K),b:new Float64Array(4*H),Wy:new Float64Array(H),by:new Float64Array(1)};
  for(var i=0;i<m.W.length;i++)m.W[i]=(r()*2-1)*s;
  for(i=0;i<H;i++){m.b[H+i]=1;m.Wy[i]=(r()*2-1)*s;}  // 순서 [i,f,o,g], 잊기 문 편향 1
  return m;}
function lstmForward(m,seq,keep){var H=m.H,D=m.D,K=D+H,h=new Float64Array(H),c=new Float64Array(H),tr=[];
  for(var t=0;t<seq.length;t++){var x=seq[t], xin=new Float64Array(K);
    if(D===1)xin[0]=x;else for(var d=0;d<D;d++)xin[d]=x[d];
    for(var j=0;j<H;j++)xin[D+j]=h[j];
    var gi=new Float64Array(H),gf=new Float64Array(H),go=new Float64Array(H),gg=new Float64Array(H),cn=new Float64Array(H),hn=new Float64Array(H);
    for(j=0;j<H;j++){var a=[m.b[j],m.b[H+j],m.b[2*H+j],m.b[3*H+j]];
      for(var q=0;q<4;q++){var row=(q*H+j)*K,s=a[q];for(var k=0;k<K;k++)s+=m.W[row+k]*xin[k];a[q]=s;}
      gi[j]=sig(a[0]);gf[j]=sig(a[1]);go[j]=sig(a[2]);gg[j]=tanh(a[3]);
      cn[j]=gf[j]*c[j]+gi[j]*gg[j];hn[j]=go[j]*tanh(cn[j]);}
    tr.push({x:xin,i:gi,f:gf,o:go,g:gg,cp:c,c:cn,h:hn});c=cn;h=hn;}
  var y=m.by[0];for(j=0;j<H;j++)y+=m.Wy[j]*h[j];
  return keep?{y:y,tr:tr}:y;}
function lstmTrain(m,X,Y,o){o=o||{};var ep=o.epochs||60,lr=o.lr||0.01,bs=o.batch||16,r=rng(o.seed||1),H=m.H,D=m.D,K=D+H;
  var P=[m.W,m.b,m.Wy,m.by],M1=P.map(function(p){return new Float64Array(p.length);}),M2=P.map(function(p){return new Float64Array(p.length);}),step=0;
  var idx=X.map(function(_,i){return i;}),hist=[];
  for(var e=0;e<ep;e++){
    for(var i=idx.length-1;i>0;i--){var j=Math.floor(r()*(i+1)),t=idx[i];idx[i]=idx[j];idx[j]=t;}
    var tot=0;
    for(var s0=0;s0<idx.length;s0+=bs){
      var G=P.map(function(p){return new Float64Array(p.length);}),nb=0;
      for(var s=s0;s<Math.min(idx.length,s0+bs);s++){var n=idx[s],f=lstmForward(m,X[n],true),dy=f.y-Y[n];tot+=dy*dy;nb++;
        var T=f.tr.length,dh=new Float64Array(H),dc=new Float64Array(H);
        for(j=0;j<H;j++){G[2][j]+=dy*f.tr[T-1].h[j];dh[j]=dy*m.Wy[j];} G[3][0]+=dy;
        for(var tt=T-1;tt>=0;tt--){var z=f.tr[tt],da=new Float64Array(4*H),dcp=new Float64Array(H);
          for(j=0;j<H;j++){var tc=tanh(z.c[j]);dc[j]+=dh[j]*z.o[j]*(1-tc*tc);
            var dO=dh[j]*tc,dI=dc[j]*z.g[j],dG=dc[j]*z.i[j],dF=dc[j]*z.cp[j];
            da[j]=dI*z.i[j]*(1-z.i[j]);da[H+j]=dF*z.f[j]*(1-z.f[j]);da[2*H+j]=dO*z.o[j]*(1-z.o[j]);da[3*H+j]=dG*(1-z.g[j]*z.g[j]);
            dcp[j]=dc[j]*z.f[j];}
          var dx=new Float64Array(K);
          for(var q=0;q<4*H;q++){var g=da[q];if(!g)continue;G[1][q]+=g;var row=q*K;
            for(var k=0;k<K;k++){G[0][row+k]+=g*z.x[k];dx[k]+=m.W[row+k]*g;}}
          for(j=0;j<H;j++)dh[j]=dx[D+j]; dc=dcp;}
      }
      step++;var b1=0.9,b2=0.999,c1=1-Math.pow(b1,step),c2=1-Math.pow(b2,step);
      for(var pi=0;pi<4;pi++){var p=P[pi],g1=M1[pi],g2=M2[pi],gr=G[pi];
        for(k=0;k<p.length;k++){var gk=gr[k]/nb;gk=clamp(gk,-5,5);g1[k]=b1*g1[k]+(1-b1)*gk;g2[k]=b2*g2[k]+(1-b2)*gk*gk;
          p[k]-=lr*(g1[k]/c1)/(Math.sqrt(g2[k]/c2)+1e-8);}}
    }
    hist.push(tot/idx.length);}
  return hist;}

/* ===== 작은 MLP (은닉 1층, tanh) ===== */
function MLP(D,H,seed){var r=rng(seed),s1=1/Math.sqrt(D),s2=1/Math.sqrt(H);
  var m={D:D,H:H,W1:new Float64Array(H*D),b1:new Float64Array(H),W2:new Float64Array(H),b2:new Float64Array(1)};
  for(var i=0;i<m.W1.length;i++)m.W1[i]=(r()*2-1)*s1*1.5; for(i=0;i<H;i++){m.b1[i]=(r()*2-1)*0.5;m.W2[i]=(r()*2-1)*s2;} return m;}
function mlpHidden(m,x){var h=new Float64Array(m.H);for(var j=0;j<m.H;j++){var s=m.b1[j];for(var k=0;k<m.D;k++)s+=m.W1[j*m.D+k]*x[k];h[j]=tanh(s);}return h;}
function mlpForward(m,x){var h=mlpHidden(m,x),y=m.b2[0];for(var j=0;j<m.H;j++)y+=m.W2[j]*h[j];return y;}
function mlpTrain(m,X,Y,o){o=o||{};var ep=o.epochs||200,lr=o.lr||0.02,bs=o.batch||32,r=rng(o.seed||3),l2=o.l2||0;
  var P=[m.W1,m.b1,m.W2,m.b2],M1=P.map(function(p){return new Float64Array(p.length);}),M2=P.map(function(p){return new Float64Array(p.length);}),step=0,idx=X.map(function(_,i){return i;});
  for(var e=0;e<ep;e++){for(var i=idx.length-1;i>0;i--){var j=Math.floor(r()*(i+1)),t=idx[i];idx[i]=idx[j];idx[j]=t;}
    for(var s0=0;s0<idx.length;s0+=bs){var G=P.map(function(p){return new Float64Array(p.length);}),nb=0;
      for(var s=s0;s<Math.min(idx.length,s0+bs);s++){var n=idx[s],x=X[n],h=mlpHidden(m,x),y=m.b2[0];
        for(j=0;j<m.H;j++)y+=m.W2[j]*h[j]; var dy=y-Y[n];nb++; G[3][0]+=dy;
        for(j=0;j<m.H;j++){G[2][j]+=dy*h[j];var dz=dy*m.W2[j]*(1-h[j]*h[j]);G[1][j]+=dz;for(var k=0;k<m.D;k++)G[0][j*m.D+k]+=dz*x[k];}}
      step++;var c1=1-Math.pow(0.9,step),c2=1-Math.pow(0.999,step);
      for(var pi=0;pi<4;pi++){var p=P[pi];for(k=0;k<p.length;k++){var gk=G[pi][k]/nb+(pi===0||pi===2?l2*p[k]:0);
        M1[pi][k]=0.9*M1[pi][k]+0.1*gk;M2[pi][k]=0.999*M2[pi][k]+0.001*gk*gk;p[k]-=lr*(M1[pi][k]/c1)/(Math.sqrt(M2[pi][k]/c2)+1e-8);}}}}
  return m;}
// 창 만들기: lookback L → (입력 L개, 정답 1개)
function windows(y,L,from,to){var X=[],Y=[];for(var t=from+L;t<to;t++){X.push(y.slice(t-L,t));Y.push(y[t]);}return {X:X,Y:Y};}

/* ===== 그리기 도우미 ===== */
// plot(ctx,W,H,{x0,x1,y0,y1,pad,lines:[{d,x0,color,w,dash,dots}],spans:[{a,b,color,label}],marks:[{x,color,label}],xlab:fn,yticks})
function plot(ctx,W,H,o){var P=o.pad||{l:44,r:14,t:30,b:28},iw=W-P.l-P.r,ih=H-P.t-P.b;
  var X=function(x){return P.l+(x-o.x0)/(o.x1-o.x0)*iw;},Y=function(y){return P.t+(1-(y-o.y0)/(o.y1-o.y0))*ih;};
  ctx.save(); ctx.font='11px '+FONT;
  (o.spans||[]).forEach(function(s){ctx.fillStyle=s.color;ctx.fillRect(X(s.a),P.t,X(s.b)-X(s.a),ih);
    if(s.label){ctx.fillStyle=s.tc||COL.muted;ctx.textAlign='left';ctx.fillText(s.label,X(s.a)+4,P.t+12);}});
  ctx.strokeStyle='rgba(157,155,184,.12)';ctx.lineWidth=1;ctx.fillStyle=COL.muted;ctx.textAlign='right';ctx.textBaseline='middle';
  var nt=o.yn||4; for(var i=0;i<=nt;i++){var v=o.y0+(o.y1-o.y0)*i/nt,yy=Y(v);ctx.beginPath();ctx.moveTo(P.l,yy);ctx.lineTo(W-P.r,yy);ctx.stroke();ctx.fillText(o.yfmt?o.yfmt(v):v.toFixed(0),P.l-6,yy);}
  ctx.textAlign='center';ctx.textBaseline='top';
  if(o.xticks)o.xticks.forEach(function(t){ctx.fillText(o.xlab?o.xlab(t):t,X(t),H-P.b+6);});
  (o.marks||[]).forEach(function(m){ctx.strokeStyle=m.color||COL.amber;ctx.setLineDash([4,4]);ctx.beginPath();ctx.moveTo(X(m.x),P.t);ctx.lineTo(X(m.x),P.t+ih);ctx.stroke();ctx.setLineDash([]);
    if(m.label){ctx.fillStyle=m.color||COL.amber;ctx.textBaseline='bottom';ctx.fillText(m.label,X(m.x),P.t-2);}});
  (o.bands||[]).forEach(function(B){ctx.fillStyle=B.color;ctx.beginPath();B.hi.forEach(function(v,i){var x=X((B.x0||0)+i);i?ctx.lineTo(x,Y(v)):ctx.moveTo(x,Y(v));});
    for(var i=B.lo.length-1;i>=0;i--)ctx.lineTo(X((B.x0||0)+i),Y(B.lo[i]));ctx.closePath();ctx.fill();});
  (o.lines||[]).forEach(function(L){ctx.strokeStyle=L.color;ctx.lineWidth=L.w||1.6;ctx.setLineDash(L.dash||[]);ctx.beginPath();var st=false;
    L.d.forEach(function(v,i){if(v===null||v===undefined||isNaN(v)){st=false;return;}var x=X((L.x0||0)+i),y=Y(v);if(!st){ctx.moveTo(x,y);st=true;}else ctx.lineTo(x,y);});ctx.stroke();ctx.setLineDash([]);
    if(L.dots){ctx.fillStyle=L.color;L.d.forEach(function(v,i){if(v===null||isNaN(v))return;ctx.beginPath();ctx.arc(X((L.x0||0)+i),Y(v),L.r||2,0,7);ctx.fill();});}});
  if(o.legend){var lx=P.l+6,ly=P.t+6;ctx.textAlign='left';ctx.textBaseline='middle';o.legend.forEach(function(g){ctx.fillStyle=g[1];ctx.fillRect(lx,ly+4,12,3);ctx.fillStyle=COL.text;ctx.fillText(g[0],lx+16,ly+5);lx+=ctx.measureText(g[0]).width+34;});}
  ctx.restore(); return {X:X,Y:Y,P:P,iw:iw,ih:ih};}
function rangeOf(arrs,padf){var lo=Infinity,hi=-Infinity;arrs.forEach(function(a){a.forEach(function(v){if(v===null||isNaN(v))return;if(v<lo)lo=v;if(v>hi)hi=v;});});
  var p=(hi-lo)*(padf===undefined?0.08:padf)||1;return [lo-p,hi+p];}
function txt(ctx,s,x,y,o){o=o||{};ctx.save();ctx.font=(o.w||'400')+' '+(o.size||12)+'px '+FONT;ctx.fillStyle=o.color||COL.text;
  ctx.textAlign=o.align||'left';ctx.textBaseline=o.base||'middle';ctx.fillText(s,x,y);ctx.restore();}
function rr(ctx,x,y,w,h,r,fill,stroke){ctx.beginPath();ctx.roundRect?ctx.roundRect(x,y,w,h,r):ctx.rect(x,y,w,h);if(fill){ctx.fillStyle=fill;ctx.fill();}if(stroke){ctx.strokeStyle=stroke;ctx.stroke();}}
function bindRange(id,fn,fmt){var el=document.getElementById(id),out=document.getElementById(id+'V');
  function u(){var v=+el.value;if(out)out.textContent=fmt?fmt(v):v;fn(v);}el.addEventListener('input',u);u();return el;}
function toggleGroup(sel,fn){var bs=$$(sel);bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false');});fn(b.dataset.v,b);});});}
function kpis(el,items){el.innerHTML=items.map(function(k){return '<div class="kpi '+(k[2]||'')+'"><b>'+k[0]+'</b><span>'+k[1]+'</span></div>';}).join('');}

/* ===== 행동으로 보기: 매출 기록 길 위를 걷는 캐릭터 ===== */
// Act(canvas,{h,get:function(){return {actual:[],rows:[{name,who,color,vals}],tol,labels,stampText}}})
function Act(cv,o){var t=0,pos=0,data=null,H=o.h||200;
  function refresh(){data=o.get();t=0;pos=REDUCE?data.actual.length-1:0;}
  refresh();
  addMod(cv,function(dt){var W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);
    var n=data.actual.length,rows=data.rows,lo=Infinity,hi=-Infinity;
    data.actual.forEach(function(v){lo=Math.min(lo,v);hi=Math.max(hi,v);});rows.forEach(function(r){r.vals.forEach(function(v){lo=Math.min(lo,v);hi=Math.max(hi,v);});});
    var padL=150,gw=(W-padL-16)/n,rowH=(H-50)/rows.length;
    if(!REDUCE){t+=dt;if(t>0.45){t=0;pos=(pos+1)%(n+4);}}
    var cur=Math.min(pos,n-1);
    ctx.font='11px '+FONT;
    for(var i=0;i<n;i++){var x=padL+i*gw+gw/2;txt(ctx,data.labels?data.labels[i]:(i+1)+'',x,H-12,{size:10,color:COL.muted,align:'center'});}
    rows.forEach(function(r,ri){var y0=30+ri*rowH;
      txt(ctx,r.name,8,y0+rowH/2,{size:12,color:r.color,w:'700'});if(r.who)drawSprite(ctx,px(r.who),padL-22,y0+rowH/2,1.4);
      for(var i=0;i<=cur&&i<n;i++){var x=padL+i*gw+gw/2,a=data.actual[i],p=r.vals[i],err=Math.abs(p-a),ok=err<=data.tol;
        var c=ok?COL.gfp:COL.eye;rr(ctx,x-gw*0.42,y0+6,gw*0.84,rowH-14,6,ok?'rgba(94,227,156,.12)':'rgba(240,96,77,.12)',c);
        txt(ctx,ok?'맞음':(p>a?'높게':'낮게'),x,y0+rowH/2-4,{size:10,color:c,align:'center',w:'700'});
        txt(ctx,'±'+err.toFixed(1),x,y0+rowH/2+10,{size:9,color:COL.muted,align:'center'});}
      if(cur<n){var cx=padL+cur*gw+gw/2;if(r.who)drawSprite(ctx,px(r.who),cx,y0+4,1.5);else{ctx.fillStyle=r.color;ctx.beginPath();ctx.arc(cx,y0+4,6,0,7);ctx.fill();}} });
    var hit=rows.map(function(r){var k=0;for(var i=0;i<=cur&&i<n;i++)if(Math.abs(r.vals[i]-data.actual[i])<=data.tol)k++;return r.name+' '+k+'/'+(Math.min(cur,n-1)+1);});
    txt(ctx,tpl('허용 오차 ±{0} 안이면 "맞음"  ·  {1}',data.tol,hit.join('  ·  ')),8,14,{size:11,color:COL.muted});
    stamp(ctx,W,data.stampText||'설명용 모형 · 실제 데이터 아님');});
  return {refresh:function(){refresh();}};}

/* ===== 히어로 픽셀아트 ===== */
function heroArt(cv,kind){var W=132,H=86;cv.width=W;cv.height=H;var c=cv.getContext('2d');c.imageSmoothingEnabled=false;
  var r=rng(5);
  if(kind==='C'){ // 매출 기록: 주판봇 + 큰 주판 + 상승 매출선
    c.fillStyle='#5a3a1e';c.fillRect(48,18,76,4);c.fillRect(48,70,76,4);c.fillRect(48,18,4,56);c.fillRect(120,18,4,56);c.fillRect(52,40,68,2);
    for(var k=0;k<6;k++){var yy=26+k*8;if(k===2)continue;c.fillStyle='#9c978c';c.fillRect(52,yy+2,68,1);
      for(var j=0;j<9;j++){var up=r()<0.45,bx=54+j*7+(k<2?(up?0:2):(up?2:0));c.fillStyle=(j+k)%3?'#8b5a2b':'#d2603c';c.fillRect(bx,yy,5,5);}}
    c.strokeStyle='#5ee39c';c.beginPath();var y=60;c.moveTo(10,y);for(k=1;k<8;k++){y+=(r()-0.7)*6;c.lineTo(10+k*5,clamp(y,14,70));}c.stroke();
    c.drawImage(px('robo'),10,44,32,32);c.drawImage(px('fly'),100,0,18,18);}
  else if(kind==='D'){ // 일상: 책장 + 독서대
    for(k=0;k<5;k++){c.fillStyle='#2b2140';c.fillRect(54,10+k*14,74,2);for(j=0;j<11;j++){var bh=6+Math.floor(r()*5);c.fillStyle=['#d672d6','#5ee39c','#82b8ff','#f1b646','#f0604d','#b9a6e8'][Math.floor(r()*6)];c.fillRect(56+j*6,10+k*14-bh,5,bh);}}
    c.fillStyle='#5a4636';c.fillRect(8,66,40,4);c.fillStyle='#eceaf3';c.fillRect(12,58,32,8);c.fillStyle='#f1b646';c.fillRect(16,61,10,1);c.fillRect(16,63,18,1);
    c.drawImage(px('fly'),14,30,24,24);c.drawImage(px('robo'),96,58,22,22);}
  else if(kind==='A'){ // 생물: 큰 초파리
    c.drawImage(px('fly'),58,6,64,64);for(k=0;k<40;k++){c.fillStyle=r()<0.5?'rgba(214,114,214,.8)':'rgba(94,227,156,.8)';c.fillRect(Math.floor(r()*50),Math.floor(r()*80),1,1);}
    c.drawImage(px('doc'),10,56,24,24);}
  else { // 연구실
    c.fillStyle='#2b2140';c.fillRect(6,60,120,3);for(k=0;k<8;k++){c.fillStyle=['#d672d6','#5ee39c','#82b8ff'][k%3];c.fillRect(70+k*6,48,3,12);}
    c.drawImage(px('doc'),10,30,30,30);c.drawImage(px('asst'),40,30,30,30);c.drawImage(px('fly'),90,14,20,20);c.drawImage(px('robo'),104,62,20,20);}
}

/* ===== 지식 색인 (O1-7) ===== */
var KG_TYPES={Concept:['개념','#5ee39c'],Method:['방법','#d672d6'],Task:['문제','#82b8ff'],Metric:['지표','#f1b646'],Claim:['주장','#f0604d'],
  Term:['용어','#b9a6e8'],Question:['질문','#ff86b8'],Analogy:['비유','#57d0dc'],BioAnalogue:['생물 대응','#ef5b5b'],Limitation:['한계','#e48cff'],
  Simulation:['시뮬레이션','#7fd1a8'],Work:['문헌','#c48a5a'],Dataset:['데이터','#9ab8ff'],QuizItem:['퀴즈','#6f7396'],Section:['섹션','#55597a']};
var KG_CHIPS=[['Concept'],['Method'],['Task'],['Metric'],['Claim'],['Term'],['Question'],['Analogy','BioAnalogue'],['Limitation','Simulation','Work','Dataset','QuizItem','Section']];
var KG_PRED={'lab:broader':'더 넓은 개념','lab:partOf':'부분','lab:prerequisiteOf':'먼저 알아야 함','lab:hasLimitation':'한계','lab:addressedBy':'해결','lab:contrastsWith':'대비',
  'lab:analogyOf':'비유','lab:bioAnalogueOf':'생물 대응','lab:solves':'푼다','lab:evaluatedBy':'지표','lab:evaluatedOn':'데이터','lab:supports':'근거','lab:assertedIn':'출처',
  'lab:demonstratedBy':'시뮬레이션','lab:assesses':'퀴즈','lab:explainedIn':'설명 위치','lab:raises':'질문','lab:relatedTo':'관련'};
function KGIndex(){
  var KG=JSON.parse($('#kg-raw').textContent), on={}, q='';
  KG_CHIPS.forEach(function(g,i){on[i]=(i<8);});
  var byId={};KG.nodes.forEach(function(n){byId[n.id]=n;});
  var chips=$('#kgChips');
  chips.innerHTML=KG_CHIPS.map(function(g,i){var t=g.length>1&&i===8?'기타':KG_TYPES[g[0]][0]+(g.length>1?'·'+KG_TYPES[g[1]][0]:'');
    return '<button type="button" aria-pressed="'+on[i]+'" data-i="'+i+'" style="--c:'+KG_TYPES[g[0]][1]+'">'+t+'</button>';}).join('');
  $$('button',chips).forEach(function(b){b.addEventListener('click',function(){var i=+b.dataset.i;on[i]=!on[i];b.setAttribute('aria-pressed',on[i]);list();});});
  function chipOf(t){for(var i=0;i<KG_CHIPS.length;i++)if(KG_CHIPS[i].indexOf(t)>=0)return i;return 8;}
  function deg(id){return KG.edges.filter(function(e){return e.s===id||e.o===id;}).length;}
  function list(){var box=$('#kgList'),qq=q.trim().toLowerCase();
    var items=KG.nodes.filter(function(n){if(!on[chipOf(n.type)])return false;if(!qq)return true;
      var s=[lab(n),n.label.ko,n.label.en,(n.altLabel&&n.altLabel.ko||[]).join(' '),defn(n)].join(' ').toLowerCase();return s.indexOf(qq)>=0;});
    box.innerHTML=items.map(function(n){var T=KG_TYPES[n.type]||['?','#888'];
      return tpl('<div class="kg-item" id="kgi-{0}"><div class="t"><span class="ty" style="--c:{1}">{2}</span><b>{3}</b><small style="color:var(--muted)">{4}</small></div>{5}<a href="{6}">설명 보러 가기 →</a> <small style="color:var(--muted)">· 연결 {7}개{8}</small></div>',n.id.replace(/[^a-z0-9]/gi,'_'),T[1],T[0],lab(n),LANG==='ko'?(n.label.en||''):'',defn(n)?'<p>'+defn(n)+'</p>':'',n.anchor,deg(n.id),n.evidence&&n.evidence.length?tpl(' · 근거 {0}',n.evidence.length):'');}).join('')||'<div class="kg-item"><p>찾는 항목이 없어요.</p></div>';
    $('#kgCount').textContent=tpl('{0}개 표시',items.length);}
  $('#kgQ').addEventListener('input',function(){q=this.value;list();});
  list();
  // 통계
  var cnt={};KG.nodes.forEach(function(n){cnt[n.type]=(cnt[n.type]||0)+1;});
  var ver=0;KG.nodes.forEach(function(n){(n.match||[]).forEach(function(m){if(m.verified)ver++;});});
  $('#kgStats').textContent=tpl('노드 {0}개 · 관계 {1}개 · {2} · 외부 매핑 확인 {3}개',KG.nodes.length,KG.edges.length,Object.keys(cnt).map(function(k){return (KG_TYPES[k]||[k])[0]+' '+cnt[k];}).join(' · '),ver);
  // 사다리 경로
  var chain=KG.edges.filter(function(e){return e.p==='lab:prerequisiteOf'||e.p==='lab:hasLimitation'||e.p==='lab:addressedBy';});
  $('#kgPath').innerHTML=chain.length?chain.map(function(e){return '<span class="s on">'+lab(byId[e.s])+' → <small>'+KG_PRED[e.p]+'</small> → '+lab(byId[e.o])+'</span>';}).join(''):'<span class="s">이 페이지에는 사다리 사슬이 없어요</span>';
  $('#kgOpen').innerHTML=KG.nodes.filter(function(n){return n.type==='Question';}).map(function(n){return '<li><a href="'+n.anchor+'">'+lab(n)+'</a>'+(defn(n)?' — <span style="color:var(--muted)">'+defn(n)+'</span>':'')+'</li>';}).join('');
  // 빠른 내보내기
  $('#kgJson').addEventListener('click',function(){download(new Blob([JSON.stringify(KG,null,2)],{type:'application/json'}),'kg_'+KG.page+'.json');});
  $('#kgMmd').addEventListener('click',function(){download(new Blob([toMermaid(KG)],{type:'text/plain'}),'kg_'+KG.page+'.mmd');});
  // 미니 그래프 (힘 배치, 시드 고정, 200회 후 정지)
  var cv=$('#kgGraph'),Hh=420,nodes=KG.nodes.slice(),hidden=0;
  if(nodes.length>80){nodes=nodes.filter(function(n){return n.type!=='Section'&&n.type!=='QuizItem';});hidden=KG.nodes.length-nodes.length;}
  var ids={};nodes.forEach(function(n){ids[n.id]=1;});
  var E=KG.edges.filter(function(e){return ids[e.s]&&ids[e.o];}),r=rng(42),P={};
  nodes.forEach(function(n){P[n.id]={x:r()*600,y:r()*Hh,vx:0,vy:0};});
  for(var it=0;it<200;it++){
    for(var a=0;a<nodes.length;a++)for(var b=a+1;b<nodes.length;b++){var A=P[nodes[a].id],B=P[nodes[b].id],dx=A.x-B.x,dy=A.y-B.y,d2=dx*dx+dy*dy+0.01,f=1800/d2;A.vx+=dx*f;A.vy+=dy*f;B.vx-=dx*f;B.vy-=dy*f;}
    E.forEach(function(e){var A=P[e.s],B=P[e.o],dx=B.x-A.x,dy=B.y-A.y,d=Math.sqrt(dx*dx+dy*dy)+0.01,f=(d-60)*0.02;A.vx+=dx/d*f;A.vy+=dy/d*f;B.vx-=dx/d*f;B.vy-=dy/d*f;});
    nodes.forEach(function(n){var p=P[n.id];p.vx+=(300-p.x)*0.004;p.vy+=(Hh/2-p.y)*0.004;p.x+=clamp(p.vx,-20,20);p.y+=clamp(p.vy,-20,20);p.vx*=0.6;p.vy*=0.6;});}
  var bx=[Infinity,-Infinity,Infinity,-Infinity];nodes.forEach(function(n){var p=P[n.id];bx[0]=Math.min(bx[0],p.x);bx[1]=Math.max(bx[1],p.x);bx[2]=Math.min(bx[2],p.y);bx[3]=Math.max(bx[3],p.y);});
  var sel=null,scr={};
  addMod(cv,function(){var W=fit(cv,Hh),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,Hh);
    var sx=function(x){return 20+(x-bx[0])/(bx[1]-bx[0]||1)*(W-40);},sy=function(y){return 20+(y-bx[2])/(bx[3]-bx[2]||1)*(Hh-40);};
    ctx.lineWidth=1;E.forEach(function(e){var A=P[e.s],B=P[e.o];var hot=sel&&(e.s===sel||e.o===sel);ctx.strokeStyle=hot?'rgba(241,182,70,.8)':'rgba(157,155,184,.22)';
      var x1=sx(A.x),y1=sy(A.y),x2=sx(B.x),y2=sy(B.y);ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();
      var ang=Math.atan2(y2-y1,x2-x1),hx=x2-Math.cos(ang)*7,hy=y2-Math.sin(ang)*7;ctx.beginPath();ctx.moveTo(hx,hy);ctx.lineTo(hx-Math.cos(ang-0.4)*5,hy-Math.sin(ang-0.4)*5);ctx.lineTo(hx-Math.cos(ang+0.4)*5,hy-Math.sin(ang+0.4)*5);ctx.fillStyle=ctx.strokeStyle;ctx.fill();});
    nodes.forEach(function(n){var p=P[n.id],x=sx(p.x),y=sy(p.y),T=KG_TYPES[n.type]||['','#888'];scr[n.id]=[x,y];
      ctx.beginPath();ctx.arc(x,y,n.id===sel?7:5,0,7);ctx.fillStyle=T[1];ctx.fill();
      var LB=lab(n);if(n.type!=='QuizItem'&&n.type!=='Section'||n.id===sel)txt(ctx,LB.length>(LANG==='ko'?14:22)?LB.slice(0,LANG==='ko'?13:21)+'…':LB,x+8,y,{size:10,color:n.id===sel?COL.amber:COL.muted});});
    if(hidden)txt(ctx,tpl('섹션·퀴즈 노드 {0}개 숨김',hidden),10,Hh-10,{size:10,color:COL.muted});});
  cv.addEventListener('pointerdown',function(e){var r0=cv.getBoundingClientRect(),x=e.clientX-r0.left,y=e.clientY-r0.top,best=null,bd=14*14;
    Object.keys(scr).forEach(function(id){var d=(scr[id][0]-x)*(scr[id][0]-x)+(scr[id][1]-y)*(scr[id][1]-y);if(d<bd){bd=d;best=id;}});
    sel=best;if(best){var n=byId[best],ci=chipOf(n.type);if(!on[ci]){on[ci]=true;$$('button',chips)[ci].setAttribute('aria-pressed','true');}
      $('#kgQ').value='';q='';list();var el=document.getElementById('kgi-'+best.replace(/[^a-z0-9]/gi,'_'));
      $$('.kg-item.hl').forEach(function(x){x.classList.remove('hl');});if(el){el.classList.add('hl');el.parentNode.scrollTop=el.offsetTop-el.parentNode.offsetTop-10;}}});
  $('#kgLegend').innerHTML=Object.keys(KG_TYPES).filter(function(k){return cnt[k];}).map(function(k){return '<span class="chip" style="border-color:'+KG_TYPES[k][1]+';color:'+KG_TYPES[k][1]+'">'+KG_TYPES[k][0]+'</span>';}).join(' ');
}
function toMermaid(g){var ns=g.nodes.filter(function(n){return n.type!=='QuizItem'&&n.type!=='Section';}).slice(0,40),ok={},L=['graph LR'];
  ns.forEach(function(n,i){ok[n.id]='n'+i;L.push('  n'+i+'["'+lab(n).replace(/"/g,"'")+'"]');});
  g.edges.forEach(function(e){if(ok[e.s]&&ok[e.o])L.push('  '+ok[e.s]+' -->|'+(KG_PRED[e.p]||e.p)+'| '+ok[e.o]);});return L.join('\n');}

/* ===== 꾸러미 (O2, 부록 O-B) ===== */
var CRC=(function(){var t=[],c;for(var n=0;n<256;n++){c=n;for(var k=0;k<8;k++)c=c&1?0xEDB88320^(c>>>1):c>>>1;t[n]=c>>>0;}
  return function(u8){var x=0xFFFFFFFF;for(var i=0;i<u8.length;i++)x=t[(x^u8[i])&255]^(x>>>8);return (x^0xFFFFFFFF)>>>0;};})();
function makeZip(files){var enc=new TextEncoder(),parts=[],central=[],off=0;
  function u16(v){return [v&255,(v>>8)&255];} function u32(v){return [v&255,(v>>8)&255,(v>>16)&255,(v>>>24)&255];}
  files.forEach(function(f){var name=enc.encode(f.name),data=enc.encode(f.text),crc=CRC(data);
    var head=[].concat(u32(0x04034b50),u16(20),u16(0x0800),u16(0),u16(0),u16(0),u32(crc),u32(data.length),u32(data.length),u16(name.length),u16(0));
    parts.push(new Uint8Array(head),name,data);
    central.push(new Uint8Array([].concat(u32(0x02014b50),u16(20),u16(20),u16(0x0800),u16(0),u16(0),u16(0),u32(crc),u32(data.length),u32(data.length),u16(name.length),u16(0),u16(0),u16(0),u16(0),u32(0),u32(off))),name);
    off+=head.length+name.length+data.length;});
  var cdStart=off,cdLen=0;central.forEach(function(c){parts.push(c);cdLen+=c.length;});
  parts.push(new Uint8Array([].concat(u32(0x06054b50),u16(0),u16(0),u16(files.length),u16(files.length),u32(cdLen),u32(cdStart),u16(0))));
  return new Blob(parts,{type:'application/zip'});}
function download(blob,name){var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;
  document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},500);}
var BIBT={'article-journal':'article','paper-conference':'inproceedings','book':'book','chapter':'incollection','webpage':'misc','dataset':'misc','report':'techreport','thesis':'phdthesis','software':'misc'};
var RIST={'article-journal':'JOUR','paper-conference':'CPAPER','book':'BOOK','chapter':'CHAP','webpage':'ELEC','dataset':'DATA','report':'RPRT','thesis':'THES','software':'COMP'};
function names(a){return (a||[]).map(function(p){return p.literal||(p.family+(p.given?', '+p.given:''));});}
function yearOf(r){return r.issued&&r.issued['date-parts']&&r.issued['date-parts'][0][0];}
function toBib(r){var f=[],add=function(k,v){if(v!==undefined&&v!==null&&v!=='')f.push('  '+k+' = {'+v+'}');};
  add('title',r.title);add('author',names(r.author).map(function(n){return n==='et al.'?'others':n;}).join(' and '));add('year',yearOf(r));
  add(r.type==='article-journal'?'journal':'booktitle',r['container-title']);add('volume',r.volume);add('number',r.issue);
  add('pages',r.page);add('publisher',r.publisher);add('doi',r.DOI);add('url',r.URL);
  if(r.lab&&r.lab.note)add('note',r.lab.note);
  return '@'+(BIBT[r.type]||'misc')+'{'+r.id+',\n'+f.join(',\n')+'\n}';}
function toRis(r){var L=['TY  - '+(RIST[r.type]||'GEN')],add=function(t,v){if(v)L.push(t+'  - '+v);};
  add('TI',r.title);names(r.author).forEach(function(n){add('AU',n);});add('PY',yearOf(r));
  add('T2',r['container-title']);add('VL',r.volume);add('IS',r.issue);
  if(r.page){var pp=String(r.page).split(/[-–]/);add('SP',pp[0]);add('EP',pp[1]);}
  add('PB',r.publisher);add('DO',r.DOI);add('UR',r.URL);if(r.lab&&r.lab.note)add('N1',r.lab.note);L.push('ER  - ');return L.join('\r\n');}
function plainCite(r){var au=names(r.author),a=au.length>2?tpl('{0} 외',au[0]):au.join(', ');
  return a+' ('+(yearOf(r)||'연도 미상')+'). '+r.title+'.'+(r['container-title']?' '+r['container-title']+(r.volume?', '+r.volume:'')+(r.issue?'('+r.issue+')':'')+(r.page?', '+r.page:'')+'.':'')+(r.publisher?' '+r.publisher+'.':'')+(r.DOI?' https://doi.org/'+r.DOI:'');}
var LD_TYPE={Concept:'skos:Concept',Method:'skos:Concept',Task:'skos:Concept',Term:'skos:Concept',Work:'schema:CreativeWork',Claim:'schema:Claim',Dataset:'schema:Dataset',QuizItem:'schema:Question',Section:'schema:WebPageElement'};
var LD_PRED={'lab:broader':'skos:broader','lab:partOf':'schema:isPartOf','lab:relatedTo':'skos:related','lab:assertedIn':'schema:citation'};
function toJsonLd(g,META){var byS={};g.edges.forEach(function(e){(byS[e.s]=byS[e.s]||[]).push(e);});
  var graph=g.nodes.map(function(n){var o={'@id':n.id,'@type':['lab:'+n.type].concat(LD_TYPE[n.type]?[LD_TYPE[n.type]]:[]),
    'skos:prefLabel':[{'@value':n.label.ko,'@language':'ko'}].concat(n.label.en?[{'@value':n.label.en,'@language':'en'}]:[]),
    'schema:name':n.label.ko};
    if(n.definition&&n.definition.ko){o['skos:definition']={'@value':n.definition.ko,'@language':'ko'};}
    if(n.altLabel&&n.altLabel.ko&&n.altLabel.ko.length)o['skos:altLabel']=n.altLabel.ko.map(function(v){return {'@value':v,'@language':'ko'};});
    o['lab:page']=n.page;o['lab:anchor']=n.anchor;o['lab:status']=n.status;o['lab:confidence']=n.confidence;
    (n.match||[]).forEach(function(m){if(m.verified&&m.id)o['skos:'+m.rel]={'@id':m.id};});
    (byS[n.id]||[]).forEach(function(e){(o[e.p]=o[e.p]||[]).push({'@id':e.o});if(LD_PRED[e.p])(o[LD_PRED[e.p]]=o[LD_PRED[e.p]]||[]).push({'@id':e.o});});
    return o;});
  return {'@context':{skos:'http://www.w3.org/2004/02/skos/core#',schema:'https://schema.org/',dct:'http://purl.org/dc/terms/',prov:'http://www.w3.org/ns/prov#',lab:'urn:lab:'},
    '@id':'urn:lab:page/'+g.page,'dct:title':META.title,'@graph':graph};}
function ttlStr(s){return '"'+String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n')+'"';}
function iri(id){return '<urn:'+id+'>';}
function toTurtle(g){var L=['@prefix skos: <http://www.w3.org/2004/02/skos/core#> .','@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .','@prefix lab: <urn:lab:> .',''];
  g.nodes.forEach(function(n){var t=[iri(n.id)+' a lab:'+n.type+' ;','  skos:prefLabel '+ttlStr(n.label.ko)+'@ko'+(n.label.en?' , '+ttlStr(n.label.en)+'@en':'')+' ;'];
    if(n.definition&&n.definition.ko)t.push('  skos:definition '+ttlStr(n.definition.ko)+'@ko ;');
    t.push('  lab:anchor '+ttlStr(n.anchor)+' ;','  lab:status '+ttlStr(n.status)+' .');L.push(t.join('\n'));});
  L.push('');g.edges.forEach(function(e){L.push(iri(e.s)+' <urn:'+e.p+'> '+iri(e.o)+' .');});return L.join('\n')+'\n';}
function csvCell(v){v=(v===undefined||v===null)?'':String(v);return /[",\n]/.test(v)?'"'+v.replace(/"/g,'""')+'"':v;}
function toNodesCsv(g){return ['id,type,label_ko,label_en,status,level,family,page,anchor'].concat(g.nodes.map(function(n){return [n.id,n.type,n.label.ko,n.label.en,n.status,n.level,n.family,n.page,n.anchor].map(csvCell).join(',');})).join('\r\n');}
function toEdgesCsv(g){return ['source,predicate,target,anchor,confidence'].concat(g.edges.map(function(e){return [e.s,e.p,e.o,e.anchor,e.confidence].map(csvCell).join(',');})).join('\r\n');}
function toProvCsv(g,REF){var L=['item,kind,work,loc,factCard,confidence,verified,pageAnchor'];
  g.nodes.forEach(function(n){(n.source||[]).forEach(function(s){L.push([n.id,'node',s.work||'',s.loc||'',(n.evidence||[]).join(' '),n.confidence,s.verified?'true':'false',n.anchor].map(csvCell).join(','));});});
  g.edges.forEach(function(e){if(e.p==='lab:assertedIn'){var w=e.o.replace('lab:work/','');L.push([e.s+' '+e.p+' '+e.o,'edge',w,'',(e.evidence||[]).join(' '),e.confidence,'',e.anchor].map(csvCell).join(','));}});
  return L.join('\r\n');}
function filterScope(KG,scope){if(scope==='all')return KG;
  var keep={},T={concepts:['Concept','Method','Term','Task','Metric','Limitation'],claims:['Claim','Work','Question']}[scope];
  var E;
  if(scope==='prereq'){E=KG.edges.filter(function(e){return ['lab:prerequisiteOf','lab:hasLimitation','lab:addressedBy'].indexOf(e.p)>=0;});E.forEach(function(e){keep[e.s]=keep[e.o]=1;});}
  else{KG.nodes.forEach(function(n){if(T.indexOf(n.type)>=0)keep[n.id]=1;});
    if(scope==='claims')KG.edges.forEach(function(e){if(keep[e.s]&&(e.p==='lab:supports'||e.p==='lab:assertedIn'))keep[e.o]=1;});
    E=KG.edges.filter(function(e){return keep[e.s]&&keep[e.o];});}
  return {version:KG.version,page:KG.page,scope:scope,nodes:KG.nodes.filter(function(n){return keep[n.id];}),edges:E};}
function readme(META,g,REF){var chk=[];REF.forEach(function(r){Object.keys(r.lab.verified||{}).forEach(function(k){if(!r.lab.verified[k])chk.push(tpl('{0}: {1} 미확인',r.id,k));});});
  ['creator','license','url'].forEach(function(k){var v=META[k];if(!v||(Array.isArray(v)&&!v.length))chk.push(tpl('page_meta.{0} 채워 넣을 것',k));});
  if(!META.license)chk.push('page_meta.license 채워 넣을 것');if(!META.url)chk.push('page_meta.url 채워 넣을 것');
  return [tpl('온톨로지·서지 꾸러미 — {0}',META.title),tpl('시리즈: {0} {1} (v{2}, {3})',META.series,META.number,META.version,META.date),'',
    tpl('권장 인용: {0}',META.suggestedCitation),'','파일','- manifest.json  꾸러미 목록','- page_meta.json  페이지 서지 정보','- kg.json  중립 지식 그래프 (원본)','- kg.jsonld  JSON-LD (SKOS·schema.org 매핑)','- kg.ttl  Turtle','- nodes.csv / edges.csv  노드·관계 표 (UTF-8 BOM)','- references.csl.json  참고문헌 원본 (CSL-JSON)','- references.bib / references.ris  BibTeX·RIS','- provenance.csv  주장·관계 ↔ 문헌 ↔ 원문 위치','',
    tpl('규모: 노드 {0} · 관계 {1} · 문헌 {2}',g.nodes.length,g.edges.length,REF.length),'',tpl('확인 필요 ({0})',chk.length)].concat(chk.map(function(c){return '- '+c;})).concat(['','lab: 어휘 IRI는 urn:lab: (사용자 도메인이 정해지면 바꿀 것).','시뮬레이션 수치는 모두 설명용 모형 값이며 실제 데이터가 아니다.']).join('\r\n');}
function buildPackage(scope){
  var KG=JSON.parse($('#kg-raw').textContent),REF=JSON.parse($('#refs-csl').textContent),META=JSON.parse($('#page-meta').textContent);
  var g=filterScope(KG,scope);
  var files=[{name:'page_meta.json',text:JSON.stringify(META,null,2)},{name:'kg.json',text:JSON.stringify(g,null,2)},
    {name:'kg.jsonld',text:JSON.stringify(toJsonLd(g,META),null,2)},{name:'kg.ttl',text:toTurtle(g)},
    {name:'nodes.csv',text:'﻿'+toNodesCsv(g)},{name:'edges.csv',text:'﻿'+toEdgesCsv(g)},
    {name:'references.csl.json',text:JSON.stringify(REF,null,2)},{name:'references.bib',text:REF.map(toBib).join('\n\n')+'\n'},
    {name:'references.ris',text:REF.map(toRis).join('\r\n')+'\r\n'},{name:'provenance.csv',text:'﻿'+toProvCsv(g,REF)},{name:'README.txt',text:readme(META,g,REF)}];
  files.unshift({name:'manifest.json',text:JSON.stringify({package:'lab-kg',version:META.version,page:META.number,created:new Date().toISOString().slice(0,10),scope:scope,
    registry:META.registryVersion||'',counts:{nodes:g.nodes.length,edges:g.edges.length,refs:REF.length},files:files.map(function(f){return f.name;})},null,2)});
  return files;}
function ExportBox(){
  var KG=JSON.parse($('#kg-raw').textContent),REF=JSON.parse($('#refs-csl').textContent),META=JSON.parse($('#page-meta').textContent),scope='all';
  var claims=KG.nodes.filter(function(n){return n.type==='Claim';}),withSrc=claims.filter(function(n){return (n.source||[]).length;}).length;
  var vRef=REF.filter(function(r){var v=r.lab.verified;return v.title&&v.authors&&v.year;}).length;
  kpis($('#exKpi'),[[KG.nodes.length,'노드','g'],[KG.edges.length,'관계','m'],[REF.length,'문헌','a'],[Math.round(vRef/Math.max(1,REF.length)*100)+'%','기본 서지 확인','i'],[claims.length?Math.round(withSrc/claims.length*100)+'%':'–','출처 있는 주장','r']]);
  var bibSelf='@misc{'+META.id+',\n  title = {'+META.title+'},\n'+(META.creator.length?'  author = {'+META.creator.map(function(c){return c.name;}).join(' and ')+'},\n':'')+'  year = {'+META.date.slice(0,4)+'},\n  note = {'+META.series+' '+META.number+', v'+META.version+'}'+(META.url?',\n  url = {'+META.url+'}':'')+'\n}';
  var risSelf=['TY  - ELEC','TI  - '+META.title].concat(META.creator.map(function(c){return 'AU  - '+c.name;})).concat(['PY  - '+META.date.slice(0,4),'T2  - '+META.series+' '+META.number,META.url?'UR  - '+META.url:'','ER  - ']).filter(Boolean).join('\r\n');
  var cites={plain:META.suggestedCitation,bib:bibSelf,ris:risSelf},cur='plain';
  function sc(){$('#exCite').textContent=cites[cur];}
  toggleGroup('#exCiteFmt .bt',function(v){cur=v;sc();});sc();
  $('#exCopy').addEventListener('click',function(){var t=cites[cur],b=this;
    (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){b.textContent='복사했어요';setTimeout(function(){b.textContent='복사';},1400);},
      function(){var r=document.createRange();r.selectNodeContents($('#exCite'));var s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='선택해 두었어요 (Ctrl+C)';});});
  var ROLE={primary:'주 자료',background:'배경',data:'수치',figure:'그림',software:'소프트웨어'};
  var byId={};KG.nodes.forEach(function(n){byId[n.id]=n;});
  $('#exRefs').innerHTML=REF.map(function(r){var v=r.lab.verified,ok=v.title&&v.authors&&v.year;
    var sup=(r.lab.supports||[]).filter(function(id){return byId[id];});
    return '<li>'+plainCite(r)+' <span class="chip">'+(ROLE[r.lab.role]||r.lab.role)+'</span><span class="badge '+(ok?'ok':'chk')+'">'+(ok?'서지 확인됨':'확인 필요')+'</span>'+
      (v.doi===false&&!r.DOI&&r.type!=='book'?'<span class="badge chk">DOI 미확인</span>':'')+
      (sup.length?tpl('<details><summary style="cursor:pointer;color:var(--info);font-size:13px">뒷받침하는 항목 {0}개</summary>{1}</details>',sup.length,sup.map(function(id){return '<a href="#kgi-'+id.replace(/[^a-z0-9]/gi,'_')+'" style="margin-right:10px;font-size:13px">'+lab(byId[id])+'</a>';}).join('')):'')+'</li>';}).join('');
  toggleGroup('#exScope .bt',function(v){scope=v;});
  $('#exZip').addEventListener('click',function(){download(makeZip(buildPackage(scope)),'kg_'+META.number+(scope==='all'?'':'_'+scope)+'.zip');});
  var fb=$('#exFiles');buildPackage('all').forEach(function(f){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=f.name;
    b.addEventListener('click',function(){var ff=buildPackage(scope).filter(function(x){return x.name===f.name;})[0];download(new Blob([ff.text],{type:'text/plain;charset=utf-8'}),f.name);});fb.appendChild(b);});
  var chk=[];REF.forEach(function(r){Object.keys(r.lab.verified).forEach(function(k){if(!r.lab.verified[k])chk.push(tpl('<li><b>{0}</b> — {1} 미확인{2}</li>',r.id,k,r.lab.note?' ('+r.lab.note+')':''));});});
  KG.nodes.forEach(function(n){(n.match||[]).forEach(function(m){if(!m.verified)chk.push(tpl('<li><b>{0}</b> — 외부 ID({1}) 미확인</li>',lab(n),m.scheme));});});
  if(!META.license)chk.push('<li><b>페이지 라이선스</b> — 채워 넣을 것</li>');if(!META.url)chk.push('<li><b>공개 주소</b> — 채워 넣을 것</li>');
  $('#exCheck').innerHTML=chk.join('');$('#exNchk').textContent=chk.length;
  $('#exVer').textContent=tpl('꾸러미 v{0} · 만든 날 {1} · 등록부 {2}',META.version,META.date,META.registryVersion||'—');
}

/* ===== 내비 표시·시작 ===== */
function navSpy(){var links=$$('nav.top .links a[href^="#"]'),map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a;});
  var ob=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&map[e.target.id]){links.forEach(function(a){a.classList.remove('on');});map[e.target.id].classList.add('on');
    var L=map[e.target.id];L.parentNode.scrollLeft=L.offsetLeft-40;}});},{rootMargin:'-40% 0px -55% 0px'});
  Object.keys(map).forEach(function(id){var el=document.getElementById(id);if(el)ob.observe(el);});}
var LANGS=['ko'];   // 2026-11-11 전면 재작성: 한국어판 먼저. 번역판을 만들면 여기에 더한다 (en zh ja ru uz vi)   // 만들어진 언어판 (언어를 더하면 여기에 추가)
function LangSwitch(){
  var LN={ko:String.fromCharCode(54620,44397,50612),en:'English',zh:'\u4e2d\u6587',ja:'\u65e5\u672c\u8a9e',ru:'\u0420\u0443\u0441\u0441\u043a\u0438\u0439',uz:'O\u02bbzbekcha',vi:'Ti\u1ebfng Vi\u1ec7t'};
  var path=location.pathname.split('/').pop()||'00_index.html',base=path.replace(/\.[a-z]{2}\.html$/,'.html');
  function fileOf(l){return l==='ko'?base:base.replace(/\.html$/,'.'+l+'.html');}
  var q=new URLSearchParams(location.search).get('lang');
  if(q&&q!==LANG&&LANGS.indexOf(q)>=0){location.replace(fileOf(q)+'?lang='+q+location.hash);return;}
  if(LANG==='ko'&&!q){var nl=((navigator.languages&&navigator.languages[0])||navigator.language||'ko').toLowerCase().slice(0,2);
    if(nl!=='ko'&&LANGS.indexOf(nl)>0){location.replace(fileOf(nl)+location.hash);return;}}
  if(q==='ko')$$('a[href]').forEach(function(a){var h=a.getAttribute('href');if(/^[^#?:/]+\.html(#.*)?$/.test(h))a.setAttribute('href',h.replace(/\.html/,'.html?lang=ko'));});
  var nav=$('nav.top');if(!nav)return;
  if(LANGS.length<2)return;
  var sel=document.createElement('select');sel.className='langsel';sel.setAttribute('aria-label','Language');
  LANGS.forEach(function(l){var o=document.createElement('option');o.value=fileOf(l)+(l==='ko'?'?lang=ko':'');o.textContent=LN[l];o.setAttribute('lang',l);if(l===LANG)o.selected=true;sel.appendChild(o);});
  sel.addEventListener('change',function(){location.href=sel.value+location.hash;});nav.appendChild(sel);}
function LabStart(o){
  LangSwitch();
  Cast.fill();
  var ha=$('canvas.pixelart');if(ha)heroArt(ha,o.anchor||'B');
  var xb=$('#xBtn');if(xb)xb.addEventListener('click',function(){var r=$('#xRoster'),op=r.hidden;r.hidden=!op;xb.setAttribute('aria-expanded',op?'true':'false');xb.textContent=op?'미공개 식구 숨기기':'미공개 식구 보기';});
  if(o.page)try{o.page();}catch(e){console.error(e);}
  if($('#kg-raw')&&$('#kgList'))KGIndex();
  if($('#exRefs'))ExportBox();
  Gloss(o.gloss||{},{core:o.core||[]});
  Study({quiz:o.quiz||{}});
  navSpy();
  drawAll(); var rt;window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(drawAll,120);});
  requestAnimationFrame(_loop);
}
