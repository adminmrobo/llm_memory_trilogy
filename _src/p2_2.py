# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
from p2_1 import X1C
P=dict(
 title='창을 키우면 될까 — 읽는 값과 가운데 놓침',chip='손님 대화 앵커',
 q='창에 전부 넣기만 하면 전부 쓰일까?',
 lead='<p>2-1에서 창을 3,600조각으로 키우니 질문 10개를 다 맞혔다. 그러면 창만 키우면 기억 문제는 끝일까? 두 가지를 따져야 한다. 하나는 <b>읽는 값</b>이다. 창에 넣은 글은 요청마다 통째로 다시 읽힌다. 다른 하나는 <b>쓰임</b>이다. 창 안에 있다고 해서 모든 글이 똑같이 답에 쓰이는 것은 아니다.</p>',
 objs=['조각 수가 두 배가 되면 서로 견줄 쌍이 네 배가 되는 까닭을 말한다','긴 입력의 가운데에 놓인 정보가 덜 쓰이는 경향을 설명한다','“창 안에 있다”와 “답에 쓰였다”를 구분한다'],mins=20,
 kpis=[('4배','조각이 2배일 때 서로 견줄 쌍'),('13배','3,600조각의 쌍 수 (1,000조각 대비)'),('6.8 / 10','가운데가 절반만 쓰인다고 볼 때 맞힐 질문 (기대값)'),('1,400조각','대결에서 초파리가 쓴 창')],
 hero=['오늘은 큰 창의 값을 따져요. 넣는 것과 쓰이는 것은 다른 이야기예요.','30일 대화 3,600조각을 통째로 넣은 창을 다시 가져왔어요.','다 넣었다고 다 읽힐까? 한가운데 낀 말은 묻힐 것 같은데.','창 안에 있으면 본 거지! 4,000조각 창은 틀릴 일이 없어.'],
 first3=['창을 키우면 더 많이 넣을 수 있지만, 읽는 값이 조각 수보다 빠르게 늘고, 가운데에 놓인 말은 덜 쓰이는 경향이 있다.','“큰 창 모델을 쓰면 다 해결된다”는 기대가 왜 절반만 맞는지 알 수 있다.','긴 자료를 통째로 붙여 넣을 때, 꼭 지켜야 할 조건은 맨 앞이나 맨 끝에 둔다. 가운데에 묻어 두지 않는다.'],
 abbr=['LLM','QA'],cast=dict(fly='고른 것만 끝에 둔다',robo='전부 넣으면 된다',**X1C),
 whyh='왜 큰 창을 의심해 보나',whytag='방법: 넣은 양과 쓰인 양을 따로 재기',prev='2-1 문맥 창 = 글의 창',
 why=[('2-1의 숨은 가정','2-1의 채점은 “창 안에 있으면 반드시 쓰인다”고 봤다. 이 가정이 맞는지 확인하지 않았다.'),('읽는 값','큰 창은 요청마다 그만큼의 글을 다시 읽는다. 값이 조각 수에 비례해서만 늘지도 않는다.'),('놓치는 자리','긴 입력에서는 가운데에 놓인 정보가 잘 쓰이지 않는다는 평가 연구가 있다 [[liu2024lost]].')],
 levels=[dict(id='lv1',no='①',title='읽는 값 — 조각이 두 배면 견줄 쌍은 네 배',nav='읽는 값',tag1='방법: 창 안의 모든 조각을 서로 견주기 (어텐션)',tag2='일상: 모임에서 모두가 모두와 악수하기',
  why=('창을 키워 대화를 통째로 넣고 싶다. 값이 얼마나 드는지 알고 싶다.','“조각이 두 배면 값도 두 배”라고 생각하기 쉽다. 기본 구조의 대화형 AI는 그렇지 않다.','모델은 창 안의 조각 하나를 읽을 때 다른 모든 조각을 함께 살핀다(어텐션) [[vaswani2017attention]]. 조각이 n개면 견줄 쌍은 n × n개다. 조각이 두 배면 쌍은 네 배다.','모임에서 모두가 모두와 한 번씩 악수한다면, 사람이 두 배로 늘 때 악수는 네 배로 는다.'),
  math=dict(ask='쌍이 n × n개라는 건 어떻게 세는 거예요?',school='제곱이다. 한 변이 n인 정사각형의 칸 수와 같다.',
   eq='서로 견줄 쌍 = 조각 수 × 조각 수',pieces=[('조각 수','창에 넣은 글의 양'),('쌍','조각 하나가 다른 조각 하나를 살피는 일 한 번'),('제곱','같은 수를 두 번 곱한 것')],
   num='1,000조각이면 1,000 × 1,000 = 100만 쌍이다. 2,000조각이면 400만 쌍으로 네 배다. 3,600조각이면 3,600 × 3,600 = 1,296만 쌍, 1,000조각의 약 13배다.',comment='글은 3.6배인데 견줄 쌍은 13배네요. 그걸 요청마다 다시 하고요.'),
  pair=('열 명이 모이면 저마다 나머지 모두와 눈을 맞춘다. 스무 명이 모이면 한 사람이 살필 상대도 두 배, 사람 수도 두 배다. 모임이 커질수록 한 바퀴 도는 데 훨씬 오래 걸린다.','기본 구조에서는 조각 수의 제곱만큼 견줄 일이 생긴다. 실제 서비스는 여러 절약 기법을 쓰지만, 긴 입력일수록 느리고 비싸진다는 방향은 같다. 그리고 2-1에서 봤듯 이 값을 요청마다 다시 치른다.'),
  talk=[('doc','front','창에 넣는 글을 1,000조각에서 3,600조각으로 늘리면 일은 몇 배가 될까요?'),('robo','chart','3.6배! 넣은 만큼만 더 내면 되지.'),('fly','arms','정말? 슬라이더를 3,600에 놓고 쌍 수를 봐.')],
  panel='<div class="panel"><h3>실험 — 조각 수와 견줄 쌍</h3>'+cv('c1','가로축은 창에 넣은 조각 수, 세로축은 서로 견줄 쌍의 수. 곡선이 위로 휘어 올라간다')+'<div class="ctrl">'+rg('r1N','창에 넣는 글 (조각)',500,8000,3600,100)+'</div><div class="kpis" id="k1"></div><div class="insight" id="ins1" aria-live="polite"></div><h3>행동으로 보기 — 모두가 모두를 살핀다</h3>'+cv('c1b','점들이 원 위에 놓이고 모든 점 사이에 선이 그어진 그림. 점이 늘수록 선이 빽빽해진다','wide')+note('점 하나가 조각 100개 묶음이다. 선 하나가 두 묶음을 견주는 일이다.')+'</div>',
  report='보고드려요. 1,000조각은 100만 쌍, 3,600조각은 1,296만 쌍이에요. 글은 3.6배인데 쌍은 약 13배예요.',
  stepsh='왜 제곱인가',steps=['모델은 조각 하나를 읽을 때 창 안의 다른 조각들을 모두 살핀다.','조각이 n개면 조각마다 n번, 모두 n × n번이다.','그래서 조각이 2배면 4배, 3배면 9배가 된다.','이 일을 요청마다 다시 한다. 긴 대화일수록 한 번의 답이 비싸진다.'],
  lim='값을 치르고 다 넣었다고 하자. 그러면 넣은 글은 다 쓰일까? 다음 칸에서 본다.',
  concepts=['concept/attention','concept/quadratic-cost','concept/context-window']),
 dict(id='lv2',no='②',title='가운데 놓침 — 창 안에 있어도 덜 쓰이는 자리',nav='가운데 놓침',tc='m',tag1='방법: 자리마다 쓰일 가능성을 다르게 두고 채점',tag2='일상: 긴 회의에서 가운데 안건이 흐릿해지기',
  why=('30일 대화를 통째로 창에 넣었다. 2-1에서는 10개를 다 맞힌다고 했다.','그 채점은 창 안의 모든 글이 똑같이 쓰인다고 가정했다. 여러 문서를 넣고 답을 찾게 한 평가에서는, 정답이 맨 앞이나 맨 끝에 있을 때 가장 잘 맞히고 가운데 있을 때 성적이 떨어졌다 [[liu2024lost]].','자리마다 “쓰일 가능성”을 다르게 두고 다시 채점한다. 앞과 끝은 높게, 가운데는 낮게 둔다. 가운데가 얼마나 꺼지는지는 슬라이더로 바꿔 본다.','세 시간짜리 회의가 끝나면 첫 안건과 마지막 안건은 또렷한데 가운데 안건은 흐릿하다.'),
  math=dict(ask='자리마다 가능성이 다르다는 걸 어떻게 숫자로 정해요?',school='이차함수다. 가운데가 가장 낮은 그릇 모양 곡선을 쓴다.',
   eq='쓰일 가능성 = 1 − 깊이 × 4 × 자리 × (1 − 자리)',pieces=[('자리','0이 맨 앞, 1이 맨 끝, 0.5가 한가운데'),('깊이','가운데가 얼마나 꺼지는지. 0이면 어디든 똑같이 쓰인다'),('4 × 자리 × (1 − 자리)','한가운데에서 1, 양 끝에서 0이 되는 값')],
   num='깊이가 0.5라고 하자. 한가운데(자리 0.5)는 1 − 0.5 × 4 × 0.5 × 0.5 = 0.5다. 절반만 쓰인다. 앞쪽(자리 0.1)은 1 − 0.5 × 4 × 0.1 × 0.9 = 0.82다.',comment='한가운데는 0.5, 앞쪽은 0.82. 같은 창 안인데 자리에 따라 이렇게 다르게 치는군요.'),
  pair=('긴 회의록을 통째로 건네받았다. 맨 앞의 결정 사항과 맨 끝의 다음 일정은 눈에 들어온다. 가운데 어딘가에 적힌 “예산 한도는 오백만 원”은 놓치기 쉽다.','이 칸의 곡선은 연구에서 보고된 경향의 “모양”만 흉내 낸 것이다. 깊이 값은 지어낸 숫자다. 실제로 얼마나 꺼지는지는 모델과 과제에 따라 다르다. 여기서 볼 것은 “넣었다”와 “쓰였다”가 다르다는 점이다.'),
  talk=[('doc','think','3,600조각을 다 넣었어요. 15일쯤에 한 말, 그러니까 한가운데 있는 말도 잘 쓰일까요?'),('robo','happy','창 안이잖아! 안에 있으면 다 똑같아.'),('fly','point','깊이를 0.5로 올려 봐. 가운데 질문들이 어떻게 되는지.')],
  panel='<div class="panel"><h3>실험 — 자리와 쓰임</h3>'+cv('c2','가로축은 창 안의 자리(왼쪽이 맨 앞, 오른쪽이 맨 끝), 세로축은 쓰일 가능성. 그릇 모양 곡선 위에 질문 10개의 정답 자리가 점으로 찍혀 있다')+'<div class="ctrl">'+rg('r2D','가운데가 꺼지는 깊이',0,0.8,0.5,0.1)+'</div><div class="kpis" id="k2"></div>'+cv('c2b','질문 10개마다 맞힐 가능성을 표시한 칸. 정답이 가운데 자리에 있는 질문일수록 가능성이 낮다')+'<div class="insight" id="ins2" aria-live="polite"></div></div>',
  report='보고드려요. 깊이 0.5로 두면 10개 가운데 6.8개를 맞힐 것으로 기대돼요. 깊이 0이면 2-1과 같은 10개고요. 가장 낮은 것은 15일에 말한 예산이었어요.',
  stepsh='넣었다와 쓰였다',steps=['창 안에 있는 글은 모델이 읽을 수 있는 글이다.','읽을 수 있다고 해서 답을 쓸 때 반드시 반영되는 것은 아니다.','긴 입력일수록, 가운데 자리일수록 놓칠 가능성이 커진다는 보고가 있다.','그래서 중요한 말은 자리도 골라야 한다. 맨 앞이나 맨 끝이다.'],
  lim='창을 키우는 길에는 값과 놓침이 따라온다. 창이 아닌 다른 곳에 기억을 둘 수는 없을까? 2-3에서 기억을 둘 수 있는 서랍 셋을 편다.',
  intern=SIA,concepts=['concept/lost-in-the-middle','concept/position-effect','limitation/in-window-not-used'])],
 duel=dict(title='전부 그대로 vs 고른 것을 끝에 — 가운데가 절반만 쓰일 때',metric='맞힐 질문 수 (기대값)',tag='일상: 회의록 통째 vs 요점 메모',q='가운데가 꺼지는 깊이를 0.5로 둔다. 30일 대화를 그대로 다 넣는 쪽과, 최근 대화에 요점 메모를 끝에 붙이는 쪽 가운데 누가 더 많이 맞힐까?',
  fly=('최근 1,000조각 + 요점 메모 400조각을 맨 끝에 — 모두 1,400조각','중요한 말 열 줄을 끝에 다시 적어 두면 돼. 나머지는 버려.'),robo=('30일 대화 3,600조각을 그대로 전부','하나도 안 버렸어. 창 안에 다 있다고!'),rule='맞힐 질문 수의 기대값(많을수록 좋음). 막대가 긴 쪽이 이긴다. 이 판정은 “깊이 0.5”라는 가정 위에서만 성립한다.'),
 sumh='정리 — 큰 창의 값',
 sum='<div class="tw"><table class="tb" id="sumTb"><tr><th>방법</th><th>요청에 넣는 조각</th><th>견줄 쌍 (1,000조각 대비)</th><th>맞힐 질문 — 깊이 0</th><th>맞힐 질문 — 깊이 0.5</th></tr></table></div><p style="font-size:14px;color:var(--muted)">깊이 0은 “창 안의 글은 어디든 똑같이 쓰인다”는 가정, 깊이 0.5는 “한가운데는 절반만 쓰인다”는 가정이다. 둘 다 설명용 모형이다.</p>'+steps3([('넣는 값은 제곱으로','조각이 두 배면 견줄 쌍은 네 배다. 그 값을 요청마다 치른다.'),('넣었다 ≠ 쓰였다','긴 입력의 가운데는 덜 쓰이는 경향이 있다.'),('자리를 고른다','중요한 말은 맨 앞이나 맨 끝에 둔다. 그러려면 무엇이 중요한지 먼저 골라야 한다.')])+field('긴 문서나 긴 대화를 통째로 붙여 넣고 질문할 때, 꼭 지켜야 할 조건과 핵심 질문은 맨 끝에 한 번 더 적는다. 답이 조건을 어기면 조건을 가운데에서 끝으로 옮겨 다시 묻는다.','“요점 메모”는 누군가 무엇이 중요한지 미리 골랐다는 뜻이다. 누가, 언제, 어떻게 고르는지가 2-4와 3부의 주제다.'),
 outro=[('doc','front','오늘의 한 줄이에요. 창에 넣는 것과 답에 쓰이는 것은 달라요. 큰 창은 값도 크고 놓치는 자리도 생겨요.'),('asst','smile','글이 3.6배인데 견줄 쌍이 13배라는 계산이 기억에 남아요.'),('fly','coffee','요점을 끝에 두는 게 통했지. 그런데 그 요점은 누가 골라 주지? 그게 걸려.'),('robo','meh','다 넣었는데 가운데가 묻히다니… 가정이 0이면 비겼을 텐데. 다른 서랍을 찾아봐야겠어.'),('moa','report','요점 메모 열 줄은 제가 따로 적어 뒀어요. 다음 편에서 어느 서랍에 넣을지 정해요.')],
 examples=['쓰일 가능성 곡선(1 − 깊이 × 4 × 자리 × (1 − 자리))은 연구에서 보고된 “앞과 끝이 높고 가운데가 낮은” 경향의 모양만 흉내 낸 설명용 모형이다. 깊이 0.5는 지어낸 값이다','견줄 쌍의 수(조각 수의 제곱)는 기본 구조의 어텐션을 기준으로 한 셈이다. 실제 서비스의 값과 속도는 구현에 따라 다르다','초파리의 요점 메모는 질문 10개의 정답 문장을 사람이 미리 골라 40조각씩 맨 끝에 붙였다고 가정했다','맞힐 질문 수는 가능성을 더한 기대값이다. 실제 모델의 답을 채점한 것이 아니다'],
 refs=['liu2024lost','vaswani2017attention','cognee2026llmmemory'],
 claims=[('claim/lost-in-middle','긴 입력에서 관련 정보가 처음이나 끝에 있을 때 성능이 가장 높고 가운데 있을 때 떨어지는 경향이 보고되었다','#lv2','liu2024lost','논문 전체','concept/lost-in-the-middle'),
  ('claim/attention-pairs','트랜스포머의 어텐션은 입력의 각 조각이 다른 모든 조각을 살피게 한다','#lv1','vaswani2017attention','논문 전체','concept/attention'),
  ('claim/uneven-use','입력이 길어져도 모든 조각이 응답에 똑같이 영향을 주지는 않는다','#lv2','cognee2026llmmemory','컨텍스트 윈도우 절','concept/position-effect')],
 openq=[('question/mem-other-places','창이 아닌 다른 곳에 기억을 둘 수는 없을까?','#lv2','2-3에서 서랍 셋으로 다룬다')],
 nodes=[('concept/attention','Concept','서로 견주기 (어텐션)','attention','#lv1','창 안의 조각 하나를 읽을 때 다른 조각들을 함께 살피는 계산.'),
  ('concept/quadratic-cost','Concept','제곱으로 느는 값','quadratic cost','#lv1','조각이 n개면 견줄 쌍이 n × n개가 되어, 조각 수보다 빠르게 일이 느는 성질.'),
  ('concept/context-window','Concept','문맥 창','context window','#lv1','대화형 AI가 한 번에 읽고 쓸 수 있는 글의 양.'),
  ('concept/lost-in-the-middle','Concept','가운데 놓침','lost in the middle','#lv2','긴 입력의 가운데에 놓인 정보가 앞·끝에 놓인 정보보다 덜 쓰이는 경향.'),
  ('concept/position-effect','Concept','자리 효과','position effect','#lv2','같은 정보라도 입력 안의 자리에 따라 답에 쓰이는 정도가 달라지는 현상.'),
  ('limitation/in-window-not-used','Limitation','창 안에 있어도 쓰이지 않을 수 있다','in context is not the same as used','#lv2','창에 넣은 글이 답에 반드시 반영되는 것은 아니다.'),
  ('sim/2-2-pairs','Simulation','조각 수와 견줄 쌍','tokens vs attention pairs','#lv1'),('sim/2-2-position','Simulation','자리와 쓰임','position vs use','#lv2'),('sim/2-2-duel','Simulation','대결: 전부 그대로 vs 요점을 끝에','duel: full dump vs notes at the end','#vs')],
 edges=[('concept/attention','prerequisiteOf','concept/quadratic-cost','#lv1'),('concept/context-window','hasLimitation','concept/quadratic-cost','#lv1'),('concept/position-effect','broader','concept/lost-in-the-middle','#lv2'),('concept/context-window','hasLimitation','limitation/in-window-not-used','#lv2'),
  ('limitation/in-window-not-used','raises','question/mem-other-places','#lv2'),('concept/quadratic-cost','demonstratedBy','sim/2-2-pairs','#lv1'),('concept/lost-in-the-middle','demonstratedBy','sim/2-2-position','#lv2'),('concept/position-effect','demonstratedBy','sim/2-2-duel','#vs')],
 gloss={'문맥 창':['문맥 창','생성 AI','대화형 AI가 한 번에 읽고 쓸 수 있는 글의 양.'],'조각':['조각 (토큰)','생성 AI','모델이 글을 읽는 단위.'],'어텐션':['어텐션','모델 구조','조각 하나를 읽을 때 창 안의 다른 조각들을 함께 살피는 계산.'],'쌍':['견줄 쌍','계산','조각 하나가 다른 조각 하나를 살피는 일 한 번.'],
  '기대값':['기대값','확률','가능성을 다 더한 값. “평균적으로 이만큼 맞힌다”는 뜻.'],'가운데 놓침':['가운데 놓침','현상','긴 입력의 가운데에 놓인 정보가 덜 쓰이는 경향.'],'깊이':['깊이','설명용 설정','이 페이지의 모형에서 가운데가 얼마나 꺼지는지를 정하는 값.'],'요점 메모':['요점 메모','쓰임','중요한 말만 골라 짧게 다시 적은 것.']},
 core=['어텐션','가운데 놓침','기대값','문맥 창'],
 quiz={'why':[Q('2-1의 채점에 숨어 있던 가정은?',['창이 무한히 크다','창 안에 있으면 반드시 쓰인다','모델이 대화를 기억한다'],1,'이 편에서 그 가정을 다시 따졌어요.','“넣었다”와 “쓰였다”를 떠올려 보세요.','limitation/in-window-not-used')],
  'lv1':[Q('조각이 3배가 되면 서로 견줄 쌍은 몇 배가 될까?',['3배','6배','9배'],2,'3 × 3 = 9배예요.','쌍 수는 조각 수의 제곱이에요.','concept/quadratic-cost','계산')],
  'lv2':[Q('깊이 0.5일 때 자리 0.5(한가운데)의 쓰일 가능성은?',['0.5','0.82','1'],0,'1 − 0.5 × 4 × 0.5 × 0.5 = 0.5예요.','4 × 0.5 × 0.5 = 1이에요.','concept/lost-in-the-middle','계산'),
        Q('긴 자료를 붙여 넣을 때 꼭 지켜야 할 조건은 어디에 두는 것이 좋을까?',['한가운데','맨 앞이나 맨 끝','어디든 같다'],1,'가운데는 덜 쓰이는 경향이 보고돼 있어요.','그릇 모양 곡선을 떠올려 보세요.','concept/position-effect')],
  'vs':[Q('이 대결의 판정에 꼭 붙여야 할 말은?',['언제나 요점 메모가 이긴다','“가운데가 절반만 쓰인다”는 가정에서 그렇다','큰 창은 쓸모없다'],1,'깊이를 0으로 두면 10 대 10으로 비겨요. 가정에 따라 달라지는 판정이에요.','깊이 0일 때의 결과를 떠올려 보세요.','concept/lost-in-the-middle')]},
)
JS=r'''
var NN=3600,cv=$('#c1'),cvb=$('#c1b');
function upd1(){var pr=NN*NN,x=pr/1e6;
  kpis($('#k1'),[[NN.toLocaleString()+'조각','창에 넣는 글','a'],[(pr>=1e8?f2(pr/1e8,2)+'억':Math.round(pr/1e4).toLocaleString()+'만')+' 쌍','서로 견줄 쌍','r'],[f2(NN/1000,1)+'배','글의 양 (1,000조각 대비)','i'],[f2(x,1)+'배','쌍의 수 (1,000조각 대비)','m']]);
  $('#ins1').innerHTML=tpl('<p>글은 {0}배인데 견줄 쌍은 {1}배예요. 이 일을 요청 한 번마다 다시 해요.</p>',f2(NN/1000,1),f2(x,1));drawAll();}
bindRange('r1N',function(v){NN=v;upd1();},function(v){return v.toLocaleString()+'조각';});
addMod(cv,function(){var H=260,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var d=[],l=[];for(var i=0;i<=80;i++){d.push(i*i/100);l.push(i/10);}
  var o=plot(ctx,W,H,{x0:0,x1:80,y0:0,y1:64,yn:4,yfmt:function(v){return v.toFixed(0)+'배';},xticks:[10,20,36,50,80],xlab:function(v){return (v*100).toLocaleString();},lines:[{d:l,color:COL.muted,w:1.3,dash:[5,4]},{d:d,color:COL.eye,w:2.3}],legend:[['견줄 쌍',COL.eye],['글의 양',COL.muted]],marks:[{x:NN/100,color:COL.amber,label:NN.toLocaleString()}]});
  txt(ctx,'세로축: 1,000조각일 때를 1배로',W-o.P.r-6,o.P.t+o.ih-8,{size:10,color:COL.muted,align:'right'});stamp(ctx,W,'설명용 도식');});
addMod(cvb,function(){var H=170,W=fit(cvb,H),ctx=cvb.getContext('2d');ctx.clearRect(0,0,W,H);var n=Math.max(2,Math.round(NN/100)),m=Math.min(n,40),cx=W/2,cy=88,R=64,pts=[];
  for(var i=0;i<m;i++){var a=i/m*Math.PI*2;pts.push([cx+Math.cos(a)*R*1.6,cy+Math.sin(a)*R]);}
  ctx.strokeStyle='rgba(240,96,77,'+Math.max(0.05,0.5/Math.sqrt(m))+')';ctx.lineWidth=1;for(i=0;i<m;i++)for(var j=i+1;j<m;j++){ctx.beginPath();ctx.moveTo(pts[i][0],pts[i][1]);ctx.lineTo(pts[j][0],pts[j][1]);ctx.stroke();}
  ctx.fillStyle=COL.amber;pts.forEach(function(p){ctx.beginPath();ctx.arc(p[0],p[1],3,0,7);ctx.fill();});
  txt(ctx,tpl('묶음 {0}개{1} · 묶음끼리 잇는 선 {2}개',n,n>40?' (그림은 40개까지)':'',(n*(n-1)/2).toLocaleString()),8,16,{size:11,color:COL.muted});stamp(ctx,W,'설명용 도식');});
/* 칸 ② */
var DP=0.5,cv2=$('#c2'),cv2b=$('#c2b'),T=3600;
function flyScore(dp){var Tt=1400,ex=QIDX.map(function(i,j){return useProb((1000+40*j+20)/Tt,dp);});return {ex:ex,n:ex.reduce(function(a,b){return a+b;},0)};}
function upd2(){var r=scoreMiddle(T,DP),lo=0;r.ex.forEach(function(v,i){if(v<r.ex[lo])lo=i;});
  kpis($('#k2'),[[f2(DP,1),'가운데가 꺼지는 깊이','a'],[f2(r.n,1)+' / 10','맞힐 질문 (기대값)',r.n>9?'g':'r'],[f2(1-DP,2),'한가운데 자리의 쓰일 가능성','m'],[QLAB[lo]+' '+Math.round(r.ex[lo]*100)+'%','가장 낮은 질문','i']]);
  $('#ins2').innerHTML=DP<0.05?'<p class="g">깊이 0이에요. 창 안의 글은 어디든 똑같이 쓰인다고 본 거예요. 2-1의 채점과 같아서 10개를 다 맞혀요.</p>':tpl('<p class="r">깊이 {0}에서는 한가운데 자리가 {1}만 쓰여요. 10개 가운데 {2}개를 맞힐 것으로 기대돼요. 창 안에 다 있는데도요.</p>',f2(DP,1),f2(1-DP,2),f2(r.n,1))+'<p>거래처와 회의 요일은 27일, 29일에 고쳐 말한 것이 끝 가까이에 있어 가능성이 높아요.</p>';drawAll();}
bindRange('r2D',function(v){DP=v;upd2();},function(v){return f2(v,1);});
addMod(cv2,function(){var H=250,W=fit(cv2,H),ctx=cv2.getContext('2d');ctx.clearRect(0,0,W,H);var d=[];for(var i=0;i<=100;i++)d.push(useProb(i/100,DP));
  var o=plot(ctx,W,H,{x0:0,x1:100,y0:0,y1:1.08,yn:4,yfmt:function(v){return v.toFixed(2);},xticks:[0,25,50,75,100],xlab:function(v){return v===0?'맨 앞 (1일)':(v===100?'맨 끝 (30일)':(v===50?'한가운데':''));},lines:[{d:d,color:COL.amber,w:2.3}]});
  QIDX.forEach(function(i){var a=factAge(latestOf(i)),x=(1-a/T)*100,y=useProb(x/100,DP);ctx.fillStyle=COL.gfp;ctx.beginPath();ctx.arc(o.X(x),o.Y(y),4.5,0,7);ctx.fill();});
  txt(ctx,'● 질문 10개의 정답이 놓인 자리',o.P.l+6,o.P.t+ o.ih-10,{size:11,color:COL.gfp});stamp(ctx,W,'설명용 모형 · 곡선 모양만 흉내 냄');});
addMod(cv2b,function(){drawBoard(cv2b,scoreMiddle(T,DP).ex,'30일 대화를 전부 넣었을 때','설명용 모형');});
PAGE._T={mid5:scoreMiddle(3600,0.5).n,fly5:flyScore(0.5).n,fly0:flyScore(0).n,mid0:scoreMiddle(3600,0).n,ex:scoreMiddle(3600,0.5).ex};
/* 대결 */
Duel({el:'#duel',higherIsBetter:true,drawMargin:0.05,fmt:function(v){return f2(v,1)+'개';},run:function(){return {fly:flyScore(0.5).n,robo:scoreMiddle(3600,0.5).n,metric:'맞힐 질문 수'};},
  say:function(f,b){return tpl('깊이 0.5에서 맞힐 질문은 초파리 쪽 요점 메모가 {0}개, 주판봇 쪽 전부 넣기가 {1}개로 기대돼요. 창에 넣은 글은 1,400조각 대 3,600조각이에요.',f2(f,1),f2(b,1));},
  lessons:{F:'가운데가 덜 쓰인다면, 고른 것을 끝에 두는 쪽이 통째로 넣는 쪽보다 낫다. 넣은 양이 아니라 놓인 자리가 갈랐다',D:'이 가정에서는 둘이 비슷했다',R:'통째로 넣은 쪽이 앞섰다'},
  after:function(){$('#duelNote').innerHTML=tpl('<p>깊이를 0으로 두면 초파리 {0}개, 주판봇 {1}개로 비겨요. 이 판정은 가정에 따라 달라져요. 어느 가정이 현실에 가까운지는 모델과 과제마다 재 봐야 해요.</p><p>견줄 쌍은 초파리 쪽이 약 {2}배, 주판봇 쪽이 약 13배예요(1,000조각 대비).</p>',f2(flyScore(0).n,1),f2(scoreMiddle(3600,0).n,1),f2(1.4*1.4,1));}});
function row(n,t,a,b){return '<tr><td>'+n+'</td><td class="num">'+t.toLocaleString()+'</td><td class="num">'+f2(t*t/1e6,1)+'배</td><td class="num">'+a+'</td><td class="num">'+b+'</td></tr>';}
$('#sumTb').insertAdjacentHTML('beforeend',row('창 1,000조각 (최근 것만)',1000,scoreWindow(1000).n+'.0',f2(scoreMiddle(1000,0.5).n,1))+row('최근 1,000 + 요점 메모 400',1400,f2(flyScore(0).n,1),f2(flyScore(0.5).n,1))+row('30일 전부 3,600조각',3600,f2(scoreMiddle(3600,0).n,1),f2(scoreMiddle(3600,0.5).n,1)));
upd1();upd2();
'''
