/* ===== 기억 3부작 공용 도구 ===== */
// 표본 자기상관: 구간 [a,b)에서 시차 k
function acf(y,k,a,b){a=a||0;b=b===undefined?y.length:b;var m=0,i,n=b-a;for(i=a;i<b;i++)m+=y[i];m/=n;var v=0,c=0;
  for(i=a;i<b;i++)v+=(y[i]-m)*(y[i]-m);for(i=a+k;i<b;i++)c+=(y[i]-m)*(y[i-k]-m);return c/v;}
// 요일 평균 빼기: 훈련 구간 [0,tr)의 요일 평균을 전 구간에서 뺀다
function deseason(y,tr){var s=[0,0,0,0,0,0,0],c=[0,0,0,0,0,0,0],i;for(i=0;i<tr;i++){s[i%7]+=y[i];c[i%7]++;}
  var mu=s.map(function(v,j){return v/c[j];});return {mu:mu,e:y.map(function(v,i){return v-mu[i%7];})};}
// 분수 차분 잡음 ARFIMA(0,d,0): x_t = Σ ψ_k ε_{t−k}, ψ_k = ψ_{k−1}(k−1+d)/k (K항에서 자름)
function makeLong(seed,n,d,o){o=o||{};var K=o.K||400,r=rng(seed),psi=[1],k,t,eps=[],x=[];for(k=1;k<K;k++)psi.push(psi[k-1]*(k-1+d)/k);
  for(t=0;t<n+K;t++)eps.push((o.sd||3)*gauss(r));
  for(t=0;t<n;t++){var s=0;for(k=0;k<K;k++)s+=psi[k]*eps[t+K-k];x.push((o.level===undefined?100:o.level)+s);}return x;}
// 이론 자기상관: 분수 차분 ρ(k)=Π (i−1+d)/(i−d)
function rhoLong(d,k){var p=1;for(var i=1;i<=k;i++)p*=(i-1+d)/(i-d);return p;}
// 메모 칸(지수평균) 여러 개: h_j(t)=a_j·h_j(t−1)+(1−a_j)·y(t−1). 반환 H[t][j] = t시점 예측에 쓸 수 있는 메모(어제까지 반영)
function memos(y,as){var h=as.map(function(){return y[0];}),H=[];for(var t=0;t<y.length;t++){H.push(h.slice());h=h.map(function(v,j){return as[j]*v+(1-as[j])*y[t];});}return H;}
// 최소제곱: X(행마다 특징), y → 계수 [상수, β…]
function linfit(X,y,lam){var k=X[0].length+1,A=[],b=[],i,j,n;for(i=0;i<k;i++){A.push(new Array(k).fill(0));b.push(0);}
  for(n=0;n<X.length;n++){var x=[1].concat(X[n]);for(i=0;i<k;i++){b[i]+=x[i]*y[n];for(j=0;j<k;j++)A[i][j]+=x[i]*x[j];}}
  for(i=1;i<k;i++)A[i][i]+=(lam||1e-6)*X.length;return solve(A,b);}
function linpred(beta,x){var v=beta[0];for(var j=0;j<x.length;j++)v+=beta[j+1]*x[j];return v;}
// 창 길이별 검증 오차표: y, 훈련 [0,tr), 검증 [tr,va)
function scoreAR(y,L,tr,va){var m=fitAR(y,L,0,tr);return {m:m,tr:mae(rollingAR(m,y,L,tr),y.slice(L,tr)),va:mae(rollingAR(m,y,tr,va),y.slice(tr,va))};}
// 메모 모델 점수: 메모 칸 as, 훈련 [w,tr) (w=예열), 검증 [tr,va)
function scoreMemo(y,as,tr,va,w){w=w||30;var H=memos(y,as),beta=linfit(H.slice(w,tr),y.slice(w,tr)),p=[],q=[],t;
  for(t=w;t<tr;t++)q.push(linpred(beta,H[t]));for(t=tr;t<va;t++)p.push(linpred(beta,H[t]));
  return {beta:beta,H:H,tr:mae(q,y.slice(w,tr)),va:mae(p,y.slice(tr,va)),pred:p};}
// 막대 그림: vals[1..n]. o={y0,y1,ticks,fmt,col(i,v),xl(i)} → {X(i),Y(v),P}
function bars(ctx,W,H,vals,sel,o){var P={l:40,r:12,t:28,b:26},n=vals.length-1,iw=W-P.l-P.r,ih=H-P.t-P.b,bw=iw/n;
  var Yf=function(v){return P.t+(1-(v-o.y0)/(o.y1-o.y0))*ih;};
  ctx.save();ctx.strokeStyle='rgba(157,155,184,.15)';ctx.fillStyle=COL.muted;ctx.font='11px '+FONT;ctx.textAlign='right';ctx.textBaseline='middle';
  o.ticks.forEach(function(v){ctx.beginPath();ctx.moveTo(P.l,Yf(v));ctx.lineTo(W-P.r,Yf(v));ctx.stroke();ctx.fillText(o.fmt?o.fmt(v):v.toFixed(1),P.l-6,Yf(v));});
  for(var i=1;i<=n;i++){var v=vals[i],x=P.l+(i-1)*bw;ctx.fillStyle=i===sel?COL.amber:(o.col?o.col(i,v):(v>=0?COL.gfp:COL.eye));
    ctx.globalAlpha=i===sel?1:0.7;ctx.fillRect(x+bw*0.15,Math.min(Yf(v),Yf(0)),bw*0.7,Math.max(1,Math.abs(Yf(v)-Yf(0))));ctx.globalAlpha=1;
    if(o.xl&&o.xl(i))txt(ctx,o.xl(i),x+bw/2,H-P.b+12,{size:10,color:COL.muted,align:'center'});}
  ctx.restore();return {X:function(i){return P.l+(i-0.5)*bw;},Y:Yf,P:P,bw:bw};}
function panel(title,cid,alt,ctrl,extra){return '';}
// 신호 기억 과제: 첫 칸에 +1 또는 −1, 나머지는 잡음. 맨 끝에서 첫 칸의 부호를 맞힌다
function cueData(seed,n,T){var r=rng(seed),Xs=[],Ys=[];for(var i=0;i<n;i++){var c=r()<0.5?-1:1,s=[c];for(var t=1;t<T;t++)s.push(0.5*gauss(r));Xs.push(s);Ys.push(c);}return {X:Xs,Y:Ys};}
function memoEnd(s,a){var h=0;s.forEach(function(v){h=a*h+(1-a)*v;});return h;}
/* ===== 2~3부 공용: 손님과의 30일 대화 (설명용 모형) ===== */
// 하루 120조각. 사실: {d:말한 날, t:말, kw:낱말, tag:뜻 꼬리표, dq:같은 낱말로 묻기, iq:다른 말로 묻기, a:답, sup:뒤에 바뀜(새 사실 번호)}
var CHAT_DAYS=30,DAY_TOK=120;
var FACTS=[
 {d:1,t:'저는 매운 걸 못 먹어요',kw:['매운'],tag:'음식',dq:'매운 음식 괜찮으세요?',iq:'점심으로 떡볶이 어때요?',a:'매운 것은 피한다'},
 {d:2,t:'회의는 매주 화요일 세 시예요',kw:['회의'],tag:'일정',dq:'회의가 무슨 요일이죠?',iq:'이번 주에 꼭 비워 둘 시간은요?',a:'화요일 세 시',sup:11},
 {d:4,t:'보고서는 표를 맨 위에 둬요',kw:['보고서','표'],tag:'문서',dq:'보고서에서 표는 어디에 두죠?',iq:'문서 첫머리에 뭘 놓을까요?',a:'표를 맨 위에'},
 {d:6,t:'거래처는 초록상사예요',kw:['거래처'],tag:'거래',dq:'거래처 이름이 뭐였죠?',iq:'견적서를 어디로 보내죠?',a:'초록상사',sup:10},
 {d:9,t:'출장은 부산으로 가요',kw:['출장'],tag:'이동',dq:'출장은 어디로 가죠?',iq:'기차표는 어느 역으로 끊을까요?',a:'부산'},
 {d:12,t:'커피는 디카페인만 마셔요',kw:['커피'],tag:'음료',dq:'커피는 어떤 걸로 할까요?',iq:'오후 음료 주문해 드릴까요?',a:'디카페인'},
 {d:15,t:'예산 한도는 오백만 원이에요',kw:['예산'],tag:'돈',dq:'예산 한도가 얼마였죠?',iq:'이 견적 승인해도 될까요?',a:'오백만 원'},
 {d:18,t:'발표는 십 분 안에 끝내야 해요',kw:['발표'],tag:'발표',dq:'발표 시간 제한이 있었나요?',iq:'슬라이드는 몇 장이 좋을까요?',a:'십 분'},
 {d:21,t:'글은 존댓말로 써 주세요',kw:['존댓말'],tag:'말투',dq:'존댓말로 쓸까요?',iq:'안내문 초안 써 드릴까요?',a:'존댓말'},
 {d:24,t:'마감은 매달 이십오 일이에요',kw:['마감'],tag:'일정표',dq:'마감이 며칠이죠?',iq:'이번 달 일정표 짜 드릴까요?',a:'이십오 일'},
 {d:27,t:'거래처가 파랑상사로 바뀌었어요',kw:['거래처'],tag:'거래',a:'파랑상사',upd:3},
 {d:29,t:'회의가 수요일로 옮겨졌어요',kw:['회의'],tag:'일정',a:'수요일',upd:1}];
var QIDX=[0,1,2,3,4,5,6,7,8,9]; // 질문 10개 (처음 열 가지 주제). 정답은 가장 최근 사실
function factAge(i){return DAY_TOK*(CHAT_DAYS-FACTS[i].d+1);} // 그 말이 끝에서 몇 조각 전에 시작됐나
function latestOf(i){return FACTS[i].sup!==undefined?FACTS[i].sup:i;}
// 전부 넣기: 창 W조각. 질문 i의 정답 사실이 창 안이면 맞힘. (옛 사실만 보이고 새 사실이 안 보이는 경우는 없다: 새 것이 더 가깝다)
function scoreWindow(W){var ok=[];QIDX.forEach(function(i){ok.push(factAge(latestOf(i))<=W?1:0);});return {ok:ok,n:ok.reduce(function(a,b){return a+b;},0),cost:Math.min(W,CHAT_DAYS*DAY_TOK)};}
// 요약하며 가기: 창 W. 넘치면 최근 W/2만 원문으로 두고 나머지는 요약(크기 ratio배)으로. 요약될 때마다 사실은 keep의 확률로 살아남는다 → 기대값
function scoreCompact(W,keep,ratio){ratio=ratio||0.2;var raw=[],S=0,k=FACTS.map(function(){return -1;}),events=0; // k=-1: 아직 안 나옴, 0: 원문, ≥1: 요약 횟수
  for(var d=1;d<=CHAT_DAYS;d++){raw.push(d);FACTS.forEach(function(f,i){if(f.d===d)k[i]=0;});
    if(raw.length*DAY_TOK+S>W){var moved=[];while(raw.length*DAY_TOK>W/2)moved.push(raw.shift());events++;
      FACTS.forEach(function(f,i){if(k[i]>=1||(k[i]===0&&moved.indexOf(f.d)>=0))k[i]++;});S=ratio*(S+moved.length*DAY_TOK);}}
  var ex=QIDX.map(function(i){var j=latestOf(i);return Math.pow(keep,k[j]);});
  return {ex:ex,n:ex.reduce(function(a,b){return a+b;},0),k:k,events:events,cost:raw.length*DAY_TOK+S,S:S,raw:raw.length};}
// 꺼내 읽기: 쪽지(사실 문장)마다 낱말 또는 뜻 꼬리표로 찾기. mode 'word'|'tag', 질문 'dq'|'iq'. 최신 우선 여부 newest
function scoreRetrieve(mode,qk,newest){var ok=[],hits=[];QIDX.forEach(function(i){var f=FACTS[i],c=[];
    FACTS.forEach(function(g,j){var m=mode==='tag'?g.tag===f.tag:(qk==='dq'&&g.kw.some(function(w){return f.kw.indexOf(w)>=0;}));if(m)c.push(j);});
    var pick=c.length?(newest?c[c.length-1]:c[0]):-1;hits.push(c);ok.push(pick===latestOf(i)?1:0);});
  return {ok:ok,n:ok.reduce(function(a,b){return a+b;},0),hits:hits,cost:40};}
// 창 안에서의 쓰임(가운데 놓침) 모형: 위치 x(0=맨 앞,1=맨 끝)에서 쓰일 확률. depth=가운데가 꺼지는 깊이
function useProb(x,depth){return 1-depth*4*x*(1-x);}
function scoreMiddle(W,depth){var T=Math.min(W,CHAT_DAYS*DAY_TOK),ex=QIDX.map(function(i){var a=factAge(latestOf(i));if(a>W)return 0;return useProb(1-a/T,depth);});return {ex:ex,n:ex.reduce(function(a,b){return a+b;},0),cost:T};}
// 질문판: 질문 10개마다 맞힘 정도(0~1)를 칸으로. vals[i], 반환 높이
var QLAB=['매운 음식','회의 요일','보고서 표','거래처','출장지','커피','예산','발표 시간','말투','마감'];
function drawBoard(cv,vals,title,stampText){var n=vals.length,cols=cv.clientWidth<520?2:5,rowsN=Math.ceil(n/cols),H=34+rowsN*50,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);
  var gw=(W-16)/cols;txt(ctx,title||'질문 10개',8,14,{size:11,color:COL.muted});
  vals.forEach(function(v,i){var x=8+(i%cols)*gw,y=28+Math.floor(i/cols)*50,c=v>=0.999?COL.gfp:(v<=0.001?COL.eye:COL.amber);
    rr(ctx,x+2,y,gw-4,42,8,'rgba(37,40,58,.9)',c);rr(ctx,x+2,y+36,Math.max(0,(gw-4)*v),6,3,c);
    txt(ctx,QLAB[i],x+10,y+13,{size:12,color:COL.text,w:'700'});txt(ctx,v>=0.999?'맞힘':(v<=0.001?'못 맞힘':'맞힐 가능성 '+Math.round(v*100)+'%'),x+10,y+27,{size:10,color:c});});
  stamp(ctx,W,stampText||'설명용 모형');return H;}
// 30일 띠: o={win:창 조각 수, sumDays:요약된 날 수, hl:[날], H}
function drawDays(cv,o){var H=o.H||120,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var gw=(W-16)/CHAT_DAYS,y=40,ch=34,winDays=(o.win||0)/DAY_TOK;
  for(var d=1;d<=CHAT_DAYS;d++){var x=8+(d-1)*gw,inside=d>CHAT_DAYS-winDays,sm=o.sumDays&&d<=o.sumDays,has=FACTS.some(function(f){return f.d===d;});
    rr(ctx,x+1,y,gw-2,ch,3,sm?'rgba(214,114,214,.28)':(inside?'rgba(241,182,70,.30)':'rgba(60,62,84,.35)'),sm?COL.stain:(inside?COL.amber:'rgba(60,62,84,.6)'));
    if(has)txt(ctx,'★',x+gw/2,y+ch/2,{size:Math.min(13,gw*0.8),color:(inside||sm)?COL.gfp:'#6f7396',align:'center'});
    if(d===1||d%5===0)txt(ctx,d+'일',x+gw/2,y+ch+12,{size:10,color:COL.muted,align:'center'});}
  if(o.win){var wx=8+(CHAT_DAYS-Math.min(winDays,CHAT_DAYS))*gw;ctx.strokeStyle=COL.amber;ctx.lineWidth=2;ctx.strokeRect(wx,y-3,W-8-wx,ch+6);}
  txt(ctx,o.title||'30일 대화 (★ = 손님이 중요한 말을 한 날)',8,16,{size:11,color:COL.muted});if(o.note)txt(ctx,o.note,8,H-10,{size:11,color:COL.muted});stamp(ctx,W,'설명용 모형');}
/* ===== 3-5: 작은 미로와 두 에이전트 (설명용 모형) ===== */
// G×G 방, 무작위 깊이 우선으로 만든 미로(갈림길만 있고 고리가 없다). 반환 {adj, goal}
function makeMaze(seed,G){var r=rng(seed),n=G*G,adj=[],vis=[],st=[0],i;for(i=0;i<n;i++){adj.push([]);vis.push(false);}vis[0]=true;
  while(st.length){var c=st[st.length-1],x=c%G,y=Math.floor(c/G),nb=[];if(x>0&&!vis[c-1])nb.push(c-1);if(x<G-1&&!vis[c+1])nb.push(c+1);if(y>0&&!vis[c-G])nb.push(c-G);if(y<G-1&&!vis[c+G])nb.push(c+G);
    if(!nb.length){st.pop();continue;}var t=nb[Math.floor(r()*nb.length)];adj[c].push(t);adj[t].push(c);vis[t]=true;st.push(t);}
  var goal=1+Math.floor(r()*(n-1));return {adj:adj,goal:goal,G:G};}
// 에이전트: mem=false 아무 문이나, mem=true 가 본 방을 기억해 안 가 본 방 먼저(없으면 온 길로 되돌아감). 반환 {path, turns(성공 시 걸린 턴, 실패 -1)}
function runAgent(mz,T,mem,seed){var r=rng(seed),cur=0,path=[0],seen={0:1},back=[];for(var t=1;t<=T;t++){var nb=mz.adj[cur],nx;
    if(mem){var fresh=nb.filter(function(v){return !seen[v];});if(fresh.length){nx=fresh[Math.floor(r()*fresh.length)];back.push(cur);}else if(back.length)nx=back.pop();else nx=nb[Math.floor(r()*nb.length)];}
    else nx=nb[Math.floor(r()*nb.length)];
    cur=nx;seen[cur]=1;path.push(cur);if(cur===mz.goal)return {path:path,turns:t};}
  return {path:path,turns:-1};}
function mazeStats(G,T,N){var a=0,b=0,ta=0,tb=0;for(var s=0;s<N;s++){var mz=makeMaze(1000+s,G),x=runAgent(mz,T,false,5000+s),y=runAgent(mz,T,true,9000+s);if(x.turns>0){a++;ta+=x.turns;}if(y.turns>0){b++;tb+=y.turns;}}
  return {none:a/N*100,mem:b/N*100,tn:a?ta/a:0,tm:b?tb/b:0};}
