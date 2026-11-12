# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
P=dict(
 title='1부 대결·정리 — 숫자의 기억에서 글의 기억으로',chip='매출 기록 · 강 수위 앵커',
 q='가장 좋은 기억 장치는 하나로 정해져 있을까?',
 lead='<p>1부에서 다섯 가지 기억을 봤다. 창, 달력(요일 평균표), 오래 가는 메아리, 메모, 문 달린 메모장이다. 이 페이지에서는 같은 기록 위에 다섯을 나란히 세워 성적을 견준다. 그리고 숫자에서 배운 것을 글로 옮길 다리를 놓는다. 2부부터의 주인공은 대화형 AI다.</p>',
 objs=['기록의 성질에 따라 이기는 기억 방식이 달라진다는 것을 성적표로 설명한다','1부의 개념 넷이 2부·3부의 무엇과 짝을 이루는지 말한다','글의 창에서 밀려난 말이 답에 쓰이지 못하는 장면을 그림에서 찾는다'],mins=18,
 kpis=[('5가지','1부에서 다룬 기억 방식'),('2.51','매출 기록 1등: 요일 평균표 + 어제 하나 (만 원)'),('2.29','강 A 1등: 20일 창 (cm)'),('1승·2승·2무','1-1~1-5 대결: 초파리 · 주판봇 · 무승부')],
 hero=['1부를 정리해요. 가장 좋은 기억은 정해져 있지 않았어요. 기록이 정했어요.','다섯 가지 방식의 성적을 한 표에 모았어요.','결국 단순한 쪽이 꽤 이겼지. 마지막 대결도 그럴까?','마지막은 문 달린 메모장으로 간다! 숫자 199개짜리야.'],
 first3=['1부에서 다룬 기억 방식 다섯 가지를 같은 기록 위에서 견주고, 2부로 넘어갈 대응표를 만든다.','대화형 AI의 기억도 같은 갈림길에 선다. 길게 펼칠지, 줄여 담을지, 따로 적어 둘지다.','기억 방식을 고를 때 “어느 것이 최고인가”가 아니라 “이 기록은 어떤 성질인가”부터 묻는다.'],
 abbr=['AR','LSTM','LLM','MAE'],cast=dict(fly='단순한 계산기 편',robo='문 달린 메모장 편',x1='2부부터 연구실과 여러 날 대화하는 익명 손님으로 나온다'),
 whyh='왜 한자리에 모아 보나',whytag='방법: 같은 기록 위에서 나란히 견주기',prev='1-5 지우개 달린 메모장',
 why=[('편마다 기록이 달랐다','매출 기록, 강 수위, 신호 시험. 편마다 다른 기록을 썼다. 한 표에 모아야 무엇이 언제 이기는지 보인다.'),('대결 결과도 갈렸다','초파리 1승, 주판봇 2승, 무승부 2번이다. 단순한 쪽도 복잡한 쪽도 늘 이기지는 않았다.'),('2부의 준비','대화형 AI의 기억을 볼 때 쓸 눈을 여기서 정리해 둔다.')],
 levels=[dict(id='lv1',no='①',kind='성적표',title='1부 성적표 — 기록이 승자를 정한다',nav='1부 성적표',tag1='방법: 같은 검증 기간, 같은 지표',tag2='일상: 과목마다 다른 1등',
  why=('기억 방식이 다섯 가지나 된다. 무엇을 써야 할지 고르고 싶다.','한 가지 기록에서 이긴 방식을 다른 기록에 그대로 쓰면 진다. 1-2의 승자는 1-3에서 졌다.','기록을 바꿔 가며 다섯 방식의 검증 오차를 나란히 놓는다. 방식마다 “정해야 할 숫자 수”도 함께 본다.','국어 1등과 수학 1등이 다르듯, 기록마다 1등 기억이 다르다.'),whyh='왜 나란히 놓고 보나',
  pair=('반에서 국어 1등과 수학 1등은 다른 학생일 수 있다. “가장 공부 잘하는 학생”을 한 명으로 정하기 어렵다. 과목을 말해야 답이 나온다.','기억 방식도 같다. 요일 무늬가 뚜렷한 매출 기록에서는 달력과 어제 하나가 이겼다. 메아리가 오래 가는 강 A에서는 긴 창과 메모 여러 칸이 앞섰다.'),
  talk=[('doc','front','매출 기록과 강 A에서 1등이 같을까요?'),('robo','chart','숫자를 제일 많이 쓴 쪽이 둘 다 1등이지!'),('fly','arms','“강 A”로 바꿔 봐. 그리고 막대 옆의 숫자 개수도 같이 봐.')],
  panel='<div class="panel"><h3>실험 — 다섯 방식 나란히</h3><div class="ctrl">'+tg('g1','기록',[('s','매출 기록'),('r','강 A')])+'</div>'+cv('c1','기억 방식마다 검증 오차를 가로 막대로 그린 그림. 막대가 짧을수록 좋다. 막대 옆에 정해야 할 숫자 수가 적혀 있다')+'<div class="insight" id="ins1" aria-live="polite"></div></div>',
  report='보고드려요. 매출 기록의 1등은 요일 평균표와 어제 하나를 쓴 방식으로 2.51만 원이에요. 강 A의 1등은 20일 창으로 2.29cm이고, 메모 세 칸이 2.31cm로 바로 뒤예요.',
  stepsh='성적표 읽는 법',steps=['막대가 짧을수록 덜 빗나간 것이다.','매출 기록: 요일처럼 되풀이되는 무늬는 표로 떼어 내고, 남은 것은 어제 하나면 된다. 메모는 무늬를 뭉개서 어제 값을 그대로 쓰는 것만큼 빗나간다.','강 A: 무늬가 없고 메아리가 오래 간다. 긴 창과 메모 여러 칸이 앞선다.','숫자를 가장 많이 쓴 방식이 1등인 기록은 없었다.'],
  lim='이 성적표는 “내일 하루 맞히기” 한 종목뿐이다. 1-3의 멀리 내다보기나 1-5의 신호 기억처럼 종목이 바뀌면 순위가 또 바뀐다.',
  concepts=['concept/no-single-best-memory','concept/record-property']),
 dict(id='lv2',no='②',kind='다리',title='숫자의 창에서 글의 창으로',nav='글의 창',tc='m',tag1='방법: 글을 조각으로 세고 창에 넣기',tag2='일상: 대화의 앞부분이 밀려나기',
  why=('대화형 AI와 긴 대화를 나눈다. 처음에 한 말을 AI가 끝까지 알고 있을지 궁금하다.','대화형 AI도 한 번에 읽을 수 있는 글의 양이 정해져 있다 [[cognee2026llmmemory]]. 1-1의 창과 같은 구조다. 넘친 앞부분은 모델에게 없는 글이다.','1부에서 배운 눈으로 본다. 글도 조각으로 세고, 창에 들어온 조각과 밀려난 조각을 가른다. 밀려난 것을 어떻게 다시 쓸지가 2부와 3부의 주제다.','대화가 길어지면 맨 앞의 말부터 책상 밖으로 떨어진다. 떨어진 말은 주워 오지 않는 한 쓸 수 없다.'),
  math=dict(ask='글의 길이는 글자 수로 세는 게 아니에요?',school='뺄셈이다. 창의 크기에서 지금까지 쌓인 글의 조각 수를 뺀다.',
   eq='밀려난 조각 수 = 지금까지의 조각 수 − 창 크기 &nbsp;(0보다 작으면 0)',pieces=[('조각 (토큰)','모델이 글을 읽는 단위. 낱말보다 잘게 나뉘기도 한다'),('창 크기','한 번에 읽을 수 있는 조각 수'),('밀려난 조각','창에 들어가지 못한 앞부분')],
   num='창 크기가 20조각이다. 대화가 26조각 쌓였다면 26 − 20 = 6조각이 밀려난다. 맨 앞 6조각에 중요한 말이 있었다면 모델은 그 말을 보지 못한다.',comment='1-1에서 창 밖의 단체 주문이 예측을 0만 원 바꾼 것과 똑같네요.'),
  pair=('손님이 대화 첫머리에 “저는 매운 걸 못 먹어요”라고 했다. 그 뒤로 회의 시간, 보고서 마감, 주말 계획 이야기가 이어졌다. 한참 뒤 손님이 점심 메뉴를 추천해 달라고 한다.','모델은 창 안에 있는 글만 읽고 답한다. 첫머리의 말이 창에 남아 있으면 매운 음식을 피한 답이 나올 수 있다. 밀려났다면 그 말은 답에 쓰일 길이 없다.'),
  talk=[('doc','think','대화가 길어져 첫 말이 창에서 밀려났어요. 모델이 그 말을 기억할까요?'),('robo','happy','아까 분명히 들었잖아! 한 번 들은 건 기억하지.'),('fly','point','창 크기를 줄여 봐. 초록 조각이 창 밖으로 나가는 순간을 보라고.')],
  panel='<div class="panel"><h3>실험 — 글의 창</h3>'+cv('c2','대화를 조각으로 나눠 늘어놓은 그림. 창 안의 조각은 밝고 창 밖으로 밀려난 조각은 어둡다. “매운 걸 못 먹어요”가 초록으로 표시된다')+'<div class="ctrl">'+rg('r2W','창 크기 (조각 수)',6,31,31)+'</div><div class="kpis" id="k2"></div><div class="insight" id="ins2" aria-live="polite"></div></div>',
  report='보고드려요. 이 대화는 모두 31조각이에요. 창이 30조각보다 작아지는 순간 “매운”이 창 밖으로 나갔어요.',
  stepsh='숫자의 창과 글의 창',steps=['숫자의 창은 지난 며칠을, 글의 창은 지난 조각들을 담는다.','둘 다 창 밖은 없는 것이다. 흐려지는 것이 아니라 끊긴다.','다른 점도 있다. 숫자 모델은 창 안을 정해진 비율로 섞는다. 대화형 AI는 창 안의 조각들을 그때그때 다른 무게로 본다 [[vaswani2017attention]].','그래서 2부는 “밀려난 것을 어떻게 되살릴까”와 “창 안은 정말 다 쓰일까”를 함께 묻는다.'],
  lim='이 그림은 낱말 단위로 조각을 나눈 설명용 도식이다. 실제 모델의 조각은 더 잘게 나뉘고 창은 훨씬 크다. 그래도 창이 차면 앞이 밀려난다는 구조는 같다. 2-1에서 자세히 본다.',
  intern=SIA,concepts=['concept/context-window','concept/token','concept/sliding-window'])],
 duel=dict(title='계산기 vs 메모장 — 매출 기록 결승',metric='검증 오차',tag='일상: 28쪽 계산기 vs 문 달린 수첩',q='1부의 마지막 대결. 매출 기록의 검증 50일에서, 28일 창 계산기와 문 달린 메모장(LSTM) 가운데 누가 덜 빗나갈까? 각자 고른 설정으로 붙는다.',
  fly=('28일 창 계산기 — 정할 숫자 29개','이 기록은 요일 무늬가 전부야. 곱하고 더하면 끝이지.'),robo=('문 달린 메모장 (메모 6칸, 14일씩 읽기) — 정할 숫자 199개','1-5에서 이긴 그 메모장이야. 숫자도 199개!'),rule='검증 오차(평균 절대 오차, 낮을수록 좋음). 막대가 짧은 쪽이 이긴다. 메모장은 이 페이지에서 바로 학습한다(2~3초).'),
 sumh='정리 — 1부에서 2부로',
 sum='<div class="tw"><table class="tb"><tr><th>편</th><th>기억 방식</th><th>얻은 것</th><th>남은 한계</th><th>2~3부의 짝</th></tr><tr><td class="num">1-1</td><td>창</td><td>창 안은 또렷이 본다</td><td>창 밖은 없다. 늘리면 값을 치른다</td><td>문맥 창 (2-1, 2-2)</td></tr><tr><td class="num">1-2</td><td>달력 + 어제 하나</td><td>되풀이는 표로, 여운은 짧게</td><td>빨리 꺼지는 기록에서만 통한다</td><td>정해진 틀의 프로필 (3-2)</td></tr><tr><td class="num">1-3</td><td>오래 가는 메아리</td><td>먼 과거가 쓸모 있는 기록이 있다</td><td>긴 창이 필요하고 세기를 사람이 고른다</td><td>바깥 저장소 (2-3, 2-5)</td></tr><tr><td class="num">1-4</td><td>메모</td><td>펼치지 않고 줄여 담는다</td><td>뭉갠다. 배우게 하면 신호가 사라진다</td><td>대화 요약·압축 (2-4)</td></tr><tr><td class="num">1-5</td><td>문 달린 메모장</td><td>남길 것을 고른다</td><td>칸 수가 정해져 있다</td><td>기억 고치기·지우기 (3-3), 기억 토큰 (3-4)</td></tr></table></div>'+steps3([('기록이 승자를 정한다','가장 좋은 기억 장치는 없다. 기록의 성질과 종목이 정한다.'),('세 가지 길','길게 펼치기, 줄여 담기, 고를 것만 붙들기. 2부와 3부에서도 이 셋이 되풀이된다.'),('다음 질문','글의 창에서 밀려난 말을 어떻게 다시 쓸까? 2부가 여기서 시작한다.')])+'<p class="lim" style="font-size:14px;color:var(--muted)">비유의 한계 · 표의 짝은 구조가 닮았다는 뜻이다. 같은 기술이라는 뜻이 아니다. 어디가 다른지는 2부와 3부의 해당 편에서 하나씩 짚는다.</p>',
 outro=[('doc','front','1부의 한 줄이에요. 기억은 길이가 아니라 맞춤이에요. 기록에 맞는 기억이 이겨요.'),('asst','smile','편마다 승자가 달라서, 성적표를 모아 보니 비로소 그림이 보였어요.'),('fly','coffee','단순한 쪽이 꽤 버텼지. 그런데 글은 숫자랑 다를 거야. 2부에서는 조심해야겠어.'),('robo','meh','숫자 199개로도 졌네… 글의 세계에서는 큰 쪽이 이길 거야. 두고 보라고!'),('moa','report','1부 기록은 서랍 하나에 모아 뒀어요. 2부부터는 손님들의 대화 기록도 제가 맡을게요.')],
 examples=['매출 기록: 가게 하루 매출(만 원) 300일 (시드 2026). 훈련 200일 · 검증 50일','강 A: 가상의 하루 수위(cm) 2000일 (시드 2027). 훈련 1400일 · 검증 300일','대결의 메모장: 메모 6칸짜리 LSTM, 14일씩 읽기, 80번 되풀이 학습 (시드 고정). 시계열 3부작과 같은 작은 모형이다','글의 창 실험은 대화를 낱말 단위 31조각으로 나눈 설명용 도식이다. 실제 모델의 조각 나누기와 다르다','1-1~1-5 대결 전적: 1-1 무승부, 1-2 초파리, 1-3 주판봇, 1-4 무승부, 1-5 주판봇'],
 refs=['cognee2026llmmemory','vaswani2017attention','hochreiter1997long','ahn2026ts3_1_1'],
 claims=[('claim/context-window-limit','문맥 창은 한 번의 추론에서 처리할 수 있는 글의 양을 제한한다','#lv2','cognee2026llmmemory','컨텍스트 윈도우 절','concept/context-window'),
  ('claim/attention-weights','트랜스포머는 창 안의 조각들을 입력에 따라 다른 무게로 본다 (어텐션)','#lv2','vaswani2017attention','논문 전체','concept/context-window')],
 openq=[('question/mem-recover-evicted','글의 창에서 밀려난 말을 어떻게 다시 쓸 수 있을까?','#lv2','2부 전체의 질문')],
 nodes=[('concept/no-single-best-memory','Concept','기록이 승자를 정한다','no single best memory','#lv1','어느 기억 방식이 좋은지는 기록의 성질과 과제에 따라 달라진다.'),
  ('concept/record-property','Concept','기록의 성질','properties of a record','#lv1','되풀이되는 무늬가 있는지, 메아리가 빨리 꺼지는지 오래 가는지 같은 특성.'),
  ('concept/context-window','Concept','문맥 창','context window','#lv2','대화형 AI가 한 번에 읽고 쓸 수 있는 글의 양.'),
  ('concept/token','Concept','조각 (토큰)','token','#lv2','모델이 글을 읽는 단위. 낱말보다 잘게 나뉘기도 한다.'),
  ('concept/sliding-window','Concept','창 (window)','sliding window','#lv2','다음 값을 짐작할 때 펼쳐 놓는 과거 구간.'),
  ('sim/1-6-scoreboard','Simulation','다섯 방식 나란히','scoreboard across records','#lv1'),('sim/1-6-text-window','Simulation','글의 창','text window','#lv2'),('sim/1-6-duel','Simulation','대결: 28일 창 vs LSTM','duel: AR(28) vs LSTM','#vs')],
 edges=[('concept/record-property','prerequisiteOf','concept/no-single-best-memory','#lv1'),('concept/token','partOf','concept/context-window','#lv2'),('concept/sliding-window','prerequisiteOf','concept/context-window','#lv2'),('concept/context-window','raises','question/mem-recover-evicted','#lv2'),
  ('concept/no-single-best-memory','demonstratedBy','sim/1-6-scoreboard','#lv1'),('concept/context-window','demonstratedBy','sim/1-6-text-window','#lv2'),('concept/no-single-best-memory','demonstratedBy','sim/1-6-duel','#vs')],
 gloss={'창':['창 (window)','설정값','다음 값을 짐작할 때 펼쳐 놓는 과거 구간.'],'문맥 창':['문맥 창 (context window)','생성 AI','대화형 AI가 한 번에 읽고 쓸 수 있는 글의 양.'],'조각':['조각 (토큰)','생성 AI','모델이 글을 읽는 단위. 낱말보다 잘게 나뉘기도 한다.'],
  '메모':['메모','이 시리즈의 별명','지난 일을 줄여 담은 숫자 칸.'],'메아리':['메아리','이 시리즈의 별명','과거의 값이 오늘 값에 남긴 흔적.'],'검증 오차':['검증 오차','지표','모델이 본 적 없는 검증 기간에서 평균적으로 빗나간 크기.'],'요일 평균표':['요일 평균표','손질','요일별 평균 매출 7개를 적은 표.'],'LSTM':['LSTM','신경망','지우개와 펜이 달린 메모장을 가진 순환 신경망.']},
 core=['창','문맥 창','조각','메모','검증 오차'],
 quiz={'why':[Q('1부의 대결 결과에서 알 수 있는 것은?',['단순한 쪽이 늘 이긴다','복잡한 쪽이 늘 이긴다','기록과 과제에 따라 승자가 달라진다'],2,'초파리도 주판봇도 늘 이기지는 않았어요.','편마다 승자를 떠올려 보세요.','concept/no-single-best-memory')],
  'lv1':[Q('매출 기록에서 메모 세 칸이 크게 빗나간 까닭은?',['숫자가 너무 많아서','요일 무늬를 뭉개서','기록이 길어서'],1,'메모는 값을 섞어 평균 내요. 7일마다 되풀이되는 날카로운 무늬가 사라져요.','1-4의 한계를 떠올려 보세요.','concept/record-property')],
  'lv2':[Q('창 크기가 30조각, 대화가 42조각이면 밀려난 조각은?',['0조각','12조각','30조각'],1,'42 − 30 = 12조각이에요.','뺄셈 한 번이에요.','concept/context-window','계산'),
        Q('창에서 밀려난 첫머리의 말은 모델의 답에',['흐릿하게 반영된다','다시 넣어 주지 않는 한 쓰일 수 없다','언제나 반영된다'],1,'창 밖은 흐려지는 게 아니라 끊겨요.','1-1의 단체 주문 실험을 떠올려 보세요.','concept/context-window')],
  'vs':[Q('문 달린 메모장이 1-5에서는 이기고 여기서는 진 까닭은?',['학습을 덜 해서만','과제가 달라서. 매출 기록은 곱하고 더하는 계산기로 충분한 단순한 기록이다','메모장이 고장 나서'],1,'잡음 속 신호 붙들기와 요일 무늬 따라가기는 다른 종목이에요.','두 과제의 성격을 견줘 보세요.','concept/no-single-best-memory')]},
)
JS=r'''
var Y=makeSeries(2026,300,{}),XA=makeLong(2027,2000,0.4,{K:1000}),DS=deseason(Y,200),AS=[0.5,0.9,0.98];
var nv=[],t;for(t=200;t<250;t++)nv.push(Y[t-1]);var mA=mean(XA.slice(0,1400));
var SC={s:[['어제 값 그대로',mae(nv,Y.slice(200,250)),'0개'],['7일 창',scoreAR(Y,7,200,250).va,'8개'],['28일 창',scoreAR(Y,28,200,250).va,'29개'],['요일 평균표 + 어제 하나',scoreAR(DS.e,1,200,250).va,'9개'],['메모 세 칸',scoreMemo(Y,AS,200,250).va,'4개']],
  r:[['평소 평균만',mae(XA.slice(1400,1700).map(function(){return mA;}),XA.slice(1400,1700)),'1개'],['어제 하나',scoreAR(XA,1,1400,1700).va,'2개'],['20일 창',scoreAR(XA,20,1400,1700).va,'21개'],['50일 창',scoreAR(XA,50,1400,1700).va,'51개'],['메모 세 칸',scoreMemo(XA,AS,1400,1700,100).va,'4개']]};
PAGE._T={s:SC.s.map(function(z){return z[1];}),r:SC.r.map(function(z){return z[1];})};
var REC='s',cv=$('#c1');
function upd1(){var a=SC[REC],best=0;a.forEach(function(z,i){if(z[1]<a[best][1])best=i;});
  $('#ins1').innerHTML=tpl('<p class="g">{0}의 1등은 “{1}” 방식이에요. 검증 오차 {2}{3}, 정한 숫자 {4}.</p>',REC==='s'?'매출 기록':'강 A',a[best][0],f2(a[best][1],2),REC==='s'?'만 원':'cm',a[best][2])+(REC==='s'?'<p>요일 무늬를 표로 떼어 낸 방식이 긴 창보다 앞섰어요. 메모 세 칸은 무늬를 뭉개서 어제 값을 그대로 쓰는 것만큼 빗나갔어요.</p>':'<p>무늬가 없고 메아리가 오래 가는 기록이에요. 긴 창과 메모 세 칸이 나란히 앞섰어요. 숫자 4개와 숫자 21개의 차이가 아주 작아요.</p>');drawAll();}
toggleGroup('#g1 button',function(v){REC=v;upd1();});
addMod(cv,function(){var a=SC[REC],H=40+a.length*42,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var mx=0,best=0;a.forEach(function(z,i){mx=Math.max(mx,z[1]);if(z[1]<a[best][1])best=i;});
  var x0=Math.min(190,W*0.36),bw=W-x0-110;a.forEach(function(z,i){var y=34+i*42,w=z[1]/mx*bw;txt(ctx,z[0],8,y+12,{size:12,color:i===best?COL.gfp:COL.text,w:i===best?'700':'400'});
    rr(ctx,x0,y,w,24,5,i===best?'rgba(94,227,156,.75)':'rgba(130,184,255,.45)');txt(ctx,f2(z[1],2),x0+w+8,y+12,{size:12,color:COL.text,w:'700'});txt(ctx,'숫자 '+z[2],W-8,y+12,{size:11,color:COL.muted,align:'right'});});
  txt(ctx,'막대가 짧을수록 좋음 · 단위 '+(REC==='s'?'만 원':'cm'),8,14,{size:10,color:COL.muted});stamp(ctx,W,'설명용 모형 · 실제 데이터 아님');});
/* 칸 ② 글의 창 */
var TALK=[['손님','저는 매운 걸 못 먹어요'],['AI','네 기억해 둘게요'],['손님','내일 회의는 세 시예요'],['AI','세 시로 적어 둘게요'],['손님','보고서는 금요일까지 내야 해요'],['AI','금요일 마감이군요'],['손님','주말에는 등산을 가요'],['AI','좋은 계획이네요'],['손님','점심 메뉴 추천해 줘요']];
var TOK=[];TALK.forEach(function(u,ui){u[1].split(' ').forEach(function(w,wi){TOK.push({w:w,who:u[0],ui:ui,first:wi===0,key:ui===0});});});
var NT=TOK.length,KEYI=1,WW=NT,cv2=$('#c2');PAGE._T.nt=NT;
function upd2(){var out=Math.max(0,NT-WW),inside=KEYI>=out;
  kpis($('#k2'),[[NT+'조각','지금까지의 대화','i'],[WW+'조각','창 크기','a'],[out+'조각','밀려난 조각',out?'r':'g'],[inside?'창 안':'창 밖','“매운 걸 못 먹어요”',inside?'g':'r']]);
  $('#ins2').innerHTML=inside?'<p class="g">첫머리의 말이 아직 창 안에 있어요. 모델은 메뉴를 고를 때 그 말을 읽을 수 있어요.</p>':tpl('<p class="r">앞의 {0}조각이 밀려났어요. “매운”이 창 밖이에요. 모델은 손님이 매운 걸 못 먹는다는 말을 읽은 적이 없는 상태로 메뉴를 골라요.</p>',out)+'<p>밀려난 말을 되살리는 길은 셋이에요. 창을 키우기(2-2), 줄여서 창 안에 남기기(2-4), 따로 적어 뒀다가 다시 넣기(2-5).</p>';drawAll();}
bindRange('r2W',function(v){WW=Math.min(v,NT);upd2();},function(v){return v+'조각';});
addMod(cv2,function(){var W=fit(cv2,10),ctx=cv2.getContext('2d');ctx.font='13px '+FONT;var x=10,y=34,rows=[],out=Math.max(0,NT-WW);
  TOK.forEach(function(k,i){var tw=ctx.measureText(k.w).width+16,lab=k.first?ctx.measureText(k.who).width+14:0;if(k.first&&i>0){x=10;y+=38;}if(x+lab+tw>W-10){x=10+ (k.first?0:40);y+=30;}rows.push({x:x+lab,y:y,w:tw,lab:k.first?x:null});x+=lab+tw+5;});
  var H=y+44;W=fit(cv2,H);ctx=cv2.getContext('2d');ctx.clearRect(0,0,W,H);
  TOK.forEach(function(k,i){var p=rows[i],gone=i<out;if(p.lab!==null)txt(ctx,k.who,p.lab,p.y+12,{size:11,color:k.who==='손님'?COL.info:COL.muted,w:'700'});
    rr(ctx,p.x,p.y,p.w,24,6,gone?'rgba(40,42,60,.6)':(k.key?'rgba(94,227,156,.35)':'rgba(241,182,70,.18)'),gone?'rgba(70,72,96,.7)':(k.key?COL.gfp:'rgba(241,182,70,.6)'));
    txt(ctx,k.w,p.x+8,p.y+12,{size:13,color:gone?'#55597a':COL.text});});
  txt(ctx,'밝은 조각 = 창 안 (모델이 읽는 글) · 어두운 조각 = 밀려난 글',10,14,{size:10,color:COL.muted});stamp(ctx,W,'설명용 도식');});
/* 대결 */
var LS=null;function trainL(){if(LS!==null)return LS;var mu=mean(Y.slice(0,200)),sd=std(Y.slice(0,200)),Z=Y.map(function(v){return (v-mu)/sd;}),net=LSTM(6,3),w=windows(Z,14,0,200);
  lstmTrain(net,w.X,w.Y,{epochs:80,lr:0.02,batch:16,seed:5});var Pp=[];for(var t=200;t<250;t++)Pp.push(lstmForward(net,Z.slice(t-14,t))*sd+mu);LS=mae(Pp,Y.slice(200,250));PAGE._T.lstm=LS;return LS;}
Duel({el:'#duel',higherIsBetter:false,drawMargin:0.05,fmt:function(v){return f2(v,2);},run:function(){return {fly:SC.s[2][1],robo:trainL(),metric:'검증 오차'};},
  say:function(f,b){return tpl('검증 오차는 초파리 쪽 28일 창 계산기가 {0}만 원, 주판봇 쪽 문 달린 메모장이 {1}만 원이에요. 차이는 큰 값의 {2}%예요.',f2(f,2),f2(b,2),f2(Math.abs(f-b)/Math.max(f,b)*100,1));},
  lessons:{F:'무늬가 단순한 기록에서는 곱하고 더하는 계산기로 충분하다. 좋은 기억 장치도 맞는 자리에 써야 한다',D:'단순한 기록 앞에서 계산기와 메모장이 비겼다',R:'문 달린 메모장이 단순한 기록에서도 앞섰다'},
  after:function(){$('#duelNote').innerHTML=tpl('<p>같은 14일 창을 쓰는 계산기는 {0}만 원이에요. 메모장은 같은 14일을 보고 비슷한 성적을 냈지만, 28일을 고른 계산기에는 미치지 못했어요.</p><p>1-5의 신호 기억 시험에서는 같은 종류의 메모장이 100% 가까이 맞혔어요. 종목이 다르면 승자가 달라요.</p>',f2(scoreAR(Y,14,200,250).va,2));}});
upd1();upd2();
'''
