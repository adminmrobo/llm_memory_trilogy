PAGE.page=function(){
var Y=makeSeries(2026,300,{});

/* ---------- 창 길이별 성적표 (1~100일) : 한 번만 계산 ---------- */
var R=[null];
for(var q=1;q<=100;q++){var mm=fitAR(Y,q,0,200);
  R.push({L:q,n:200-q,k:q+1,tr:mae(rollingAR(mm,Y,q,200),Y.slice(q,200)),va:mae(rollingAR(mm,Y,200,250),Y.slice(200,250)),m:mm});}
var BEST=1;for(q=2;q<=100;q++)if(R[q].va<R[BEST].va)BEST=q;
var nv=[];for(var t0=200;t0<250;t0++)nv.push(Y[t0-1]);var NAIVE=mae(nv,Y.slice(200,250));
PAGE._R=R;PAGE._BEST=BEST;PAGE._NAIVE=NAIVE;

/* ---------- 칸 ① 창 밖에서 일어난 일 ---------- */
var L=14,K=20,EV=false,T=230,AMP=40,cv=$('#c1'),cvb=$('#c1b');
function series(){var Z=Y.slice();if(EV)Z[T-K]+=AMP;return Z;}
function upd1(){
  var m=R[L].m,base=arPred(m,Y,T),now=arPred(m,series(),T),inside=K<=L,d=now-base;
  kpis($('#k1'),[[tpl('{0}일',L),tpl('창 ({0}~{1})',dayLabel(T-L),dayLabel(T-1)),'a'],
    [tpl('{0}일 전',K),tpl('사건 날 ({0})',dayLabel(T-K)),'m'],
    [EV?(inside?'창 안':'창 밖'):'사건 없음','사건의 자리',EV?(inside?'g':'r'):''],
    [(d>=0?'+':'−')+f2(Math.abs(d),2)+'만 원','예측이 바뀐 크기',Math.abs(d)>1e-9?'g':'r']]);
  $('#eq1').innerHTML=tpl('{0} 예측 = <b>{1}</b>만 원 &nbsp;→&nbsp; 사건을 넣은 뒤 <b>{2}</b>만 원 &nbsp; (실제 <i>{3}</i>만 원)',dayLabel(T),f2(base,2),f2(now,2),f2(Y[T],1));
  var msg;
  if(!EV)msg='<p>아직 사건이 없어요. “단체 주문 넣기”를 누르면 '+tpl('{0}일 전({1}) 매출이 40만 원 뛰어요.',K,dayLabel(T-K))+'</p>';
  else if(!inside)msg=tpl('<p class="r">사건은 {0}일 전인데 창은 {1}일이에요. 사건이 창 밖이라 예측은 한 푼도 바뀌지 않았어요. 모델에게 그날은 없는 날이에요.</p>',K,L)+'<p>창 길이를 사건 날짜 이상으로 늘리거나, 사건을 창 안으로 옮겨 보세요.</p>';
  else msg=tpl('<p class="g">사건이 창 안으로 들어왔어요. {0}일 전 값에 곱하는 비율이 {1}이라, 40 × {1} = {2}만 원만큼 예측이 움직였어요.</p>',K,f2(m.phi[K-1],3),f2(AMP*m.phi[K-1],2))+'<p>움직인 크기는 사건 크기가 아니라 “그 자리의 비율”이 정해요. 비율이 0에 가까운 자리면 창 안이어도 거의 안 움직여요.</p>';
  $('#ins1').innerHTML=msg;drawAll();
}
bindRange('r1L',function(v){L=v;upd1();},function(v){return tpl('{0}일',v);});
bindRange('r1K',function(v){K=v;upd1();},function(v){return tpl('{0}일 전',v);});
$('#b1E').addEventListener('click',function(){EV=!EV;this.setAttribute('aria-pressed',EV?'true':'false');this.textContent=EV?'단체 주문 빼기':'단체 주문 넣기 (+40만 원)';upd1();});
addMod(cv,function(){var H=300,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);
  var a=T-66,b=T+3,Z=series(),seg=Z.slice(a,T+1),rg=rangeOf([seg,[Y[T-K]+AMP]]);
  var o=plot(ctx,W,H,{x0:a,x1:b,y0:rg[0],y1:rg[1],xticks:[a,T-45,T-30,T-15,T],xlab:dayLabel,
    spans:[{a:T-L-0.5,b:T-0.5,color:'rgba(241,182,70,.16)'}],lines:[{d:seg,x0:a,color:'#c9c7dc',w:1.4}]});
  // 창 밖 가리기
  ctx.fillStyle='rgba(8,8,14,.72)';ctx.fillRect(o.P.l,o.P.t,Math.max(0,o.X(T-L-0.5)-o.P.l),o.ih);
  if(o.X(T-L-0.5)-o.P.l>120)txt(ctx,'창 밖 — 모델에게는 없는 날',o.P.l+10,o.P.t+16,{size:11,color:COL.muted});
  txt(ctx,tpl('창 {0}일',L),o.X(T-L/2-0.5),o.P.t+o.ih-10,{size:11,color:COL.amber,align:'center',w:'700'});
  if(EV){var ex=o.X(T-K),ey=o.Y(Z[T-K]),ins=K<=L;ctx.fillStyle=ins?COL.gfp:COL.eye;ctx.beginPath();ctx.arc(ex,ey,5,0,7);ctx.fill();
    txt(ctx,ins?'★ 단체 주문 (보임)':'★ 단체 주문 (안 보임)',clamp(ex,o.P.l+70,W-90),ey-14,{size:11,color:ins?COL.gfp:COL.eye,align:'center',w:'700'});}
  var m=R[L].m,pr=arPred(m,Z,T);ctx.fillStyle=COL.robo;ctx.beginPath();ctx.arc(o.X(T),o.Y(clamp(pr,rg[0],rg[1])),5,0,7);ctx.fill();
  ctx.strokeStyle=COL.text;ctx.lineWidth=2;ctx.beginPath();ctx.arc(o.X(T),o.Y(Y[T]),5,0,7);ctx.stroke();
  txt(ctx,'● 예측  ○ 실제',o.X(T)-6,o.P.t+12,{size:11,color:COL.robo,align:'right'});
  stamp(ctx,W,'설명용 모형 · 실제 데이터 아님');});
var ph=0;
addMod(cvb,function(dt){var H=150,W=fit(cvb,H),ctx=cvb.getContext('2d');ctx.clearRect(0,0,W,H);
  if(!REDUCE)ph+=dt;var N=60,padR=78,gw=(W-16-padR)/N,y0=52,ch=Math.min(34,gw*1.6);
  for(var i=N;i>=1;i--){var x=8+(N-i)*gw,ins=i<=L,isE=EV&&i===K;
    rr(ctx,x+1,y0,gw-2,ch,3,ins?(isE?'rgba(94,227,156,.55)':'rgba(241,182,70,'+(0.30+0.10*Math.sin(ph*2+i*0.4))+')'):'rgba(60,62,84,.35)',ins?COL.amber:'rgba(60,62,84,.6)');
    if(isE)txt(ctx,'★',x+gw/2,y0-10,{size:13,color:ins?COL.gfp:COL.eye,align:'center'});}
  txt(ctx,'60일 전',8,y0+ch+14,{size:10,color:COL.muted});txt(ctx,'어제',8+N*gw,y0+ch+14,{size:10,color:COL.muted,align:'right'});
  var wx=8+(N-L)*gw;ctx.strokeStyle=COL.amber;ctx.lineWidth=2;ctx.strokeRect(wx,y0-3,L*gw,ch+6);
  txt(ctx,tpl('책상 위 {0}쪽',L),wx+L*gw/2,y0+ch+14,{size:11,color:COL.amber,align:'center',w:'700'});
  drawSprite(ctx,px('robo'),W-padR/2-4,y0+ch/2,2.2);
  var say=!EV?'펼친 쪽만 봐요':(K<=L?'★ 보여요!':'★? 못 봤어요');
  txt(ctx,say,W-padR/2-4,y0-18,{size:11,color:!EV?COL.muted:(K<=L?COL.gfp:COL.eye),align:'center',w:'700'});
  txt(ctx,tpl('밝은 칸 {0}개 = 모델이 기억하는 전부',L),8,16,{size:11,color:COL.muted});
  stamp(ctx,W,'설명용 도식');});

/* ---------- 칸 ② 창 길이별 성적표 ---------- */
var L2=28,cv2=$('#c2');
var act=Act($('#c2b'),{h:180,get:function(){var d=[],a=[],b=[],lb=[];for(var t=200;t<214;t++){a.push(arPred(R[L2].m,Y,t));b.push(arPred(R[7].m,Y,t));d.push(Y[t]);lb.push(dayLabel(t));}
  return {actual:d,labels:lb,tol:4,rows:[{name:tpl('주판봇 {0}일 창',L2),who:'robo',color:COL.robo,vals:a},{name:'초파리 7일 창',who:'fly',color:COL.fly,vals:b}]};}});
function upd2(){var r=R[L2];
  kpis($('#k2'),[[tpl('{0}개',r.n),'연습 문제 수 (200 − 창)','g'],[tpl('{0}개',r.k),'정해야 할 숫자 수 (창 + 1)','a'],[f2(r.tr,2),'훈련 오차 (만 원)','m'],[f2(r.va,2),'검증 오차 (만 원)',r.va<=R[BEST].va*1.1?'g':(r.va>R[7].va?'r':'i')]]);
  var per=r.n/r.k,msg;
  if(L2<7)msg=tpl('<p class="r">창이 일주일보다 짧아요. 요일 흐름을 한 번도 다 보지 못해 평균 {0}만 원씩 빗나가요.</p>',f2(r.va,2));
  else if(L2<21)msg=tpl('<p class="a">지난주 같은 요일이 창에 들어왔어요. 검증 오차 {0}만 원. 아직 더 내려갈 자리가 있어요.</p>',f2(r.va,2));
  else if(L2<=60)msg=tpl('<p class="g">숫자 하나에 연습 문제가 {0}개씩 돌아가요. 검증 오차 {1}만 원. 이 기록에서 가장 낮은 값은 {2}일 창의 {3}만 원이에요.</p>',f2(per,1),f2(r.va,2),BEST,f2(R[BEST].va,2));
  else if(L2<95)msg=tpl('<p class="m">숫자 하나에 연습 문제가 {0}개뿐이에요. 훈련 오차는 {1}까지 내려갔는데 검증 오차는 {2}로 다시 올라갔어요. 외우기 시작한 거예요.</p>',f2(per,1),f2(r.tr,2),f2(r.va,2));
  else msg=tpl('<p class="r">연습 문제 {0}개에 정할 숫자가 {1}개예요. 문제보다 숫자가 많거나 거의 같아요. 훈련 오차 {2}, 검증 오차 {3}만 원. 답을 통째로 외운 모델이에요.</p>',r.n,r.k,f2(r.tr,2),f2(r.va,2));
  $('#ins2').innerHTML=msg;act.refresh();drawAll();}
bindRange('r2L',function(v){L2=v;upd2();},function(v){return tpl('{0}일',v);});
addMod(cv2,function(){var H=300,W=fit(cv2,H),ctx=cv2.getContext('2d');ctx.clearRect(0,0,W,H);
  var CAP=7,va=[],tr=[];for(var i=1;i<=100;i++){va.push(Math.min(R[i].va,CAP));tr.push(R[i].tr);}
  var o=plot(ctx,W,H,{x0:1,x1:100,y0:0,y1:CAP,yn:7,xticks:[1,7,14,28,50,80,100],xlab:function(v){return v+'일';},
    lines:[{d:tr,x0:1,color:COL.muted,w:1.4,dash:[5,4]},{d:va,x0:1,color:COL.robo,w:2.2}],legend:[['검증 오차',COL.robo],['훈련 오차',COL.muted]],
    marks:[{x:L2,color:COL.amber,label:tpl('{0}일',L2)}]});
  ctx.fillStyle=COL.gfp;ctx.beginPath();ctx.arc(o.X(BEST),o.Y(R[BEST].va),4,0,7);ctx.fill();
  txt(ctx,tpl('가장 낮음 {0}일',BEST),o.X(BEST),o.Y(R[BEST].va)+16,{size:10,color:COL.gfp,align:'center'});
  ctx.fillStyle=COL.amber;ctx.beginPath();ctx.arc(o.X(L2),o.Y(Math.min(R[L2].va,CAP)),5,0,7);ctx.fill();
  if(R[100].va>CAP)txt(ctx,tpl('↑ 100일 창은 {0}',f2(R[100].va,2)),o.X(100)-4,o.P.t+12,{size:11,color:COL.eye,align:'right',w:'700'});
  txt(ctx,'세로축: 평균 오차(만 원), 낮을수록 좋음',o.P.l+4,H-o.P.b-8,{size:10,color:COL.muted});
  stamp(ctx,W,'설명용 모형 · 실제 데이터 아님');});

/* ---------- 대결 ---------- */
Duel({el:'#duel',higherIsBetter:false,drawMargin:0.05,fmt:function(v){return f2(v,2);},
  run:function(){return {fly:R[7].va,robo:R[80].va,metric:'검증 오차'};},
  say:function(f,b){return tpl('검증 오차는 초파리 쪽 7일 창이 {0}만 원, 주판봇 쪽 80일 창이 {1}만 원이에요. 차이는 {2}만 원, 큰 값의 {3}%예요.',f2(f,2),f2(b,2),f2(Math.abs(f-b),2),f2(Math.abs(f-b)/Math.max(f,b)*100,1));},
  lessons:{D:'기억을 11배로 늘렸는데 성적은 그대로다. 짧은 창은 못 봐서, 긴 창은 외워서 빗나간다',F:'긴 창은 외우느라 빗나갔다',R:'긴 창이 먼 과거를 살려 냈다'},
  after:function(r,res){$('#duelNote').innerHTML=tpl('<p>참고로 둘 사이에 있는 28일 창은 {0}만 원, 이 기록에서 가장 낮은 {1}일 창은 {2}만 원이에요. 두 선수 모두 최선의 길이를 고르지 못했어요.</p><p>어제 값만 쓰는 가장 쉬운 방법은 {3}만 원이었어요. 두 창 모두 그보다는 나아요.</p>',f2(R[28].va,2),BEST,f2(R[BEST].va,2),f2(NAIVE,2));}});

/* ---------- 정리 표 ---------- */
var note={7:'요일 흐름은 본다. 더 먼 흐름은 못 본다',28:'넉 주를 본다. 이 표에서 가장 고르다',80:'외우기 시작했다. 7일 창과 비슷한 성적',100:'문제보다 숫자가 많다. 통째로 외웠다'};
var rows=[7,28,80,100];
$('#sumTb').insertAdjacentHTML('beforeend',rows.map(function(l){var r=R[l];return '<tr><td class="num">'+l+'일</td><td class="num">'+r.n+'</td><td class="num">'+r.k+'</td><td class="num">'+f2(r.tr,2)+'</td><td class="num">'+f2(r.va,2)+'</td><td>'+note[l]+'</td></tr>';}).join(''));
upd1();upd2();
};
LabStart(PAGE);
