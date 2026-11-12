# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
X1C=dict(x1='연구실과 30일 동안 대화하는 익명 손님. 대사는 소리만',moa='손님의 대화 기록을 맡은 사람 · 응원')
P=dict(
 title='문맥 창 = 글의 창 — 대화가 이어져 보이는 까닭',chip='손님 대화 앵커',
 q='대화형 AI는 지난 대화를 정말 기억하고 있을까?',
 lead='<p>2부의 주인공은 대화형 AI다. 앞에서 한 말을 받아서 이어 말하니 기억하는 것처럼 보인다. 속을 들여다보면 다르다. 모델은 요청을 받을 때마다 처음부터 다시 읽는다. 읽을 수 있는 양에는 한도가 있다. 그 한도가 <b>문맥 창</b>이다. 1-1의 창이 글로 옮겨 온 것이다.</p><p style="font-size:14px;color:var(--muted)">2부와 3부에서는 익명의 손님 한 분이 연구실 AI와 30일 동안 나눈 대화를 계속 쓴다. 하루에 120조각씩, 모두 3,600조각이다.</p>',
 objs=['대화가 이어져 보이는 것이 “매번 다시 보내기” 때문임을 설명한다','n번째 요청까지 보낸 조각 수를 계산한다','창 크기에 따라 30일 대화의 어느 날까지 읽히는지 계산한다'],mins=20,
 kpis=[('0개','대화 중에 바뀌는 모델 속 숫자'),('3,600조각','손님과의 30일 대화 전체'),('3 / 10','창 1,000조각으로 맞힌 질문'),('10 / 10','창 4,000조각으로 맞힌 질문')],
 hero=['2부를 시작해요. 대화형 AI의 기억은 어디에 있을까요? 먼저 가장 흔한 오해부터 풀어요.','손님 한 분과 30일 동안 나눈 대화를 준비했어요. 마지막 날 질문 10개를 드릴 거예요.','모델이 대화를 기억한다고? 창 밖으로 밀려난 건 못 볼 텐데. 정말 기억일까?','창을 크게 하면 되지! 4,000조각이면 30일이 통째로 들어가.'],
 first3=['대화형 AI는 대화를 기억하지 않는다. 요청마다 지난 대화를 통째로 다시 받아 처음부터 읽는다. 읽을 수 있는 양의 한도가 문맥 창이다.','“아까 말했잖아”가 통하지 않는 순간이 왜 생기는지, 긴 대화가 왜 비싸지는지가 이 구조에서 나온다.','긴 대화에서 처음에 정한 조건이 지켜지지 않으면, 그 조건이 창에서 밀려났는지부터 의심한다. 중요한 조건은 다시 적어 준다.'],
 abbr=['LLM','API','KV 캐시'],cast=dict(fly='작은 창으로 아낀다',robo='큰 창에 다 넣는다',**X1C),
 whyh='왜 “기억한다”는 말부터 따져 보나',whytag='방법: 요청 하나에 무엇이 들어가는지 보기',prev='1-6 1부 대결·정리',
 why=[('기억의 자리를 정확히','모델 속 숫자에 있는 기억, 창 안에 있는 기억, 바깥에 적어 둔 기억은 성질이 다르다. 2-3에서 셋을 가른다. 오늘은 창부터다.'),('흔한 오해','“AI가 내 말을 배워서 기억한다”고 생각하기 쉽다. 대화하는 동안 모델 속 숫자는 하나도 바뀌지 않는다.'),('1부와 같은 눈으로','창 안은 보이고 창 밖은 없다. 1-1에서 숫자로 본 구조가 글에서도 그대로다.')],
 levels=[dict(id='lv1',no='①',title='대화가 이어져 보이는 까닭 — 매번 처음부터 다시 읽는다',nav='매번 다시 읽기',tag1='방법: 지난 대화를 새 질문 앞에 붙여 다시 보내기',tag2='일상: 전화할 때마다 지난 통화 녹취록을 다시 읽어 주기',
  why=('손님이 열 번째 말을 건넸다. AI는 첫 번째 말에서 정한 조건을 지키며 답한다. 기억하고 있는 것처럼 보인다.','모델은 요청 하나를 처리하고 나면 아무것도 들고 있지 않는다. 대화하는 동안 모델 속 숫자는 바뀌지 않는다. 모델만으로는 대화가 이어질 수 없다.','대화 프로그램이 지난 대화 전체를 새 질문 앞에 붙여 매번 다시 보낸다. 모델은 그 긴 글을 처음부터 읽고 다음 말을 쓴다. 지난 대화를 빼고 보내면 모델에게 그 대화는 없던 일이 된다 [[cognee2026llmmemory]].','기억력이 전혀 없는 상담원에게, 전화할 때마다 지난 통화 녹취록을 처음부터 다시 읽어 주는 것이다.'),
  math=dict(ask='매번 처음부터 다시 보내면, 대화가 길수록 보내는 양이 엄청 늘겠네요?',school='1부터 n까지 더하는 등차수열의 합이다. 1 + 2 + … + n = n × (n + 1) ÷ 2.',
   eq='n번째까지 보낸 조각 = 한 번의 조각 수 × n × (n + 1) ÷ 2',pieces=[('한 번의 조각 수','손님 말과 AI 답을 한 번 주고받을 때 늘어나는 글의 양'),('n','지금까지 주고받은 횟수'),('n번째 요청','그때까지 쌓인 대화 전부 = 한 번의 조각 수 × n')],
   num='한 번 주고받을 때 40조각이 는다고 하자. 열 번째 요청에는 40 × 10 = 400조각을 보낸다. 첫 번째부터 열 번째까지 보낸 것을 모두 더하면 40 × 10 × 11 ÷ 2 = 2,200조각이다. 새로 쓴 말은 400조각뿐인데 읽힌 양은 다섯 배가 넘는다.',comment='같은 말이 요청마다 다시 읽히니까 대화가 두 배 길어지면 읽는 양은 네 배쯤 되는군요.'),
  pair=('상담원은 전화를 끊는 순간 통화 내용을 전부 잊는다. 그래서 손님은 전화할 때마다 지난 통화 녹취록을 처음부터 읽어 준 다음 새 질문을 한다. 통화가 거듭될수록 읽어 줄 녹취록이 길어진다.','요청 하나에 들어가는 글은 “지난 대화 전부 + 새 질문”이다. 모델은 이것을 창에 넣고 한 번에 읽는다. 창 안에 든 것이 그 순간 모델이 아는 대화의 전부다. 같은 글을 다시 읽는 계산을 잠깐 아껴 주는 장치(KV 캐시)가 있지만, 대화가 끝나면 사라지므로 기억은 아니다.'),
  talk=[('doc','front','열 번 주고받았어요. 열한 번째 요청에는 무엇이 들어갈까요?'),('robo','chart','새 질문 하나만 보내면 되지! 앞의 건 모델이 기억하잖아.'),('fly','arms','정말? 슬라이더를 밀어 봐. 요청 하나에 들어가는 조각이 어떻게 느는지.')],
  panel='<div class="panel"><h3>실험 — 요청 하나에 들어가는 글</h3>'+cv('c1','가로축은 몇 번째 요청인지, 세로축은 그 요청에 보낸 조각 수. 막대가 계단처럼 한 칸씩 높아진다. 막대 맨 위 한 칸만 새로 쓴 말이다')+'<div class="ctrl">'+rg('r1N','주고받은 횟수',1,30,10)+'</div><div class="kpis" id="k1"></div><div class="insight" id="ins1" aria-live="polite"></div><h3>행동으로 보기 — 요청과 요청 사이</h3>'+cv('c1b','가운데 모델 상자는 늘 비어 있고, 왼쪽에서 점점 두꺼워지는 대화 묶음이 요청마다 통째로 건너간다','wide')+note('가운데가 모델이다. 요청을 처리하는 동안만 글을 읽고, 끝나면 비워진다. 대화 묶음을 들고 있는 쪽은 대화 프로그램이다.')+'</div>',
  report='보고드려요. 한 번에 40조각씩이면 열 번째 요청은 400조각, 서른 번째 요청은 1,200조각이에요. 서른 번째까지 보낸 것을 다 더하면 18,600조각이에요.',
  stepsh='요청 하나의 속',steps=['손님이 새 말을 건넨다.','대화 프로그램이 지난 대화 전부를 그 앞에 붙인다.','모델이 그 글을 처음부터 끝까지 읽고 다음 말을 쓴다.','모델은 아무것도 간직하지 않는다. 다음 요청에서 2번을 다시 한다.'],
  lim='지난 대화를 통째로 붙이는 방법은 대화가 창보다 길어지면 통하지 않는다. 다음 칸에서 30일 대화로 확인한다.',
  concepts=['concept/context-window','concept/stateless-model','concept/history-resend','concept/token'],
  code=[('messages.append({"role": "user", "content": new_question})','새 질문을 지난 대화 목록 끝에 붙인다'),('reply = model(messages)','지난 대화 전체와 새 질문을 한꺼번에 모델에 보낸다')],codenote='대화 프로그램이 하는 일을 보인 예다. 실제 호출 이름은 서비스마다 다르다.'),
 dict(id='lv2',no='②',title='창이 차면 — 30일 대화의 어디까지 읽히나',nav='창이 차면',tc='m',tag1='방법: 창 크기를 바꿔 가며 질문 10개 채점',tag2='일상: 책상에 올릴 수 있는 녹취록 분량',
  why=('손님과 30일 동안 대화했다. 하루에 120조각씩 3,600조각이 쌓였다. 마지막 날 손님이 지난 한 달 동안 말한 것들에 대해 묻는다.','창이 3,600조각보다 작으면 대화 전체를 붙일 수 없다. 넘치는 만큼 맨 앞부터 잘라 낸다. 잘린 날에 한 말은 모델에게 없는 말이다.','창 크기를 바꿔 가며 질문 10개를 채점한다. 정답이 든 날이 창 안에 있으면 맞히고, 밖이면 못 맞힌다고 본다.','책상에 녹취록을 열 장만 올릴 수 있다면 최근 열 장만 올린다. 스무 장 전의 약속은 책상 위에 없다.'),
  math=dict(ask='창이 1,000조각이면 며칠 치가 들어가요?',school='나눗셈이다. 창 크기를 하루치 조각 수로 나눈다.',
   eq='창에 들어가는 날 수 = 창 크기 ÷ 하루치 조각 수',pieces=[('창 크기','한 번에 읽을 수 있는 조각 수'),('하루치 조각 수','이 대화에서는 120조각'),('나머지','하루를 다 못 채우는 자투리. 그날은 일부만 읽힌다')],
   num='창이 1,000조각이면 1,000 ÷ 120 = 8.3이다. 최근 8일은 다 들어가고 9일 전은 일부만 들어간다. 30일 전체를 넣으려면 120 × 30 = 3,600조각이 필요하다.',comment='1,000조각이면 최근 8일뿐이네요. 첫날 들은 “매운 걸 못 먹어요”는 22일이나 창 밖이고요.'),
  pair=('녹취록 30일 치가 쌓여 있다. 책상이 좁아 최근 며칠 치만 올려 둘 수 있다. 손님이 “제가 첫날 뭐라고 했죠?”라고 물으면, 책상 위에는 그 종이가 없다.','대화가 창보다 길어지면 가장 오래된 부분부터 잘린다. 모델은 잘린 부분에 대해 물으면 모른다고 하거나 그럴듯하게 지어낼 수 있다. 어느 쪽이든 그 말을 “읽고” 답한 것은 아니다.'),
  talk=[('doc','think','창이 1,000조각이라면 질문 10개 가운데 몇 개를 맞힐까요?'),('fly','arms','최근 것만 물어볼 테니 절반은 맞히겠지. 정말 그럴까?'),('robo','happy','슬라이더를 3,600까지 밀어! 다 넣으면 다 맞혀.')],
  panel='<div class="panel"><h3>실험 — 창 크기와 질문 10개</h3>'+cv('c2','30일을 칸으로 늘어놓은 띠. 창 안의 날은 밝고 창 밖의 날은 어둡다. 별표는 손님이 중요한 말을 한 날이다','wide')+'<div class="ctrl">'+rg('r2W','창 크기 (조각)',400,4000,1000,100)+'</div><div class="kpis" id="k2"></div>'+cv('c2b','질문 10개마다 맞혔는지 표시한 칸. 정답이 든 날이 창 안이면 초록, 밖이면 빨강이다')+'<div class="insight" id="ins2" aria-live="polite"></div></div>',
  report='보고드려요. 창 1,000조각이면 10개 가운데 3개, 2,000조각이면 6개, 3,600조각이면 10개를 다 맞혔어요.',
  stepsh='채점 규칙',steps=['질문마다 정답이 든 날이 있다. 손님이 그 말을 한 날이다.','그날이 창 안에 있으면 모델이 읽을 수 있으니 맞힌 것으로 친다.','거래처와 회의 요일은 중간에 바뀌었다. 바뀐 뒤의 말이 최근이라 작은 창에도 들어온다.','“창 안에 있으면 반드시 쓰인다”는 것은 이 칸의 가정이다. 2-2에서 이 가정을 다시 따진다.'],
  lim='창을 3,600조각으로 키우면 다 맞힌다. 그러면 창만 키우면 될까? 요청마다 3,600조각을 읽는 값과, 창 안의 글이 정말 다 쓰이는지를 2-2에서 본다.',
  intern=SIA,concepts=['concept/truncation','concept/context-window','limitation/window-eviction'])],
 duel=dict(title='창 1,000조각 vs 4,000조각 — 30일 뒤의 질문 10개',metric='맞힌 질문 수',tag='일상: 8일 치 vs 한 달 치',q='손님과의 30일 대화가 끝났다. 지난 한 달에 대한 질문 10개를 작은 창과 큰 창 가운데 누가 더 많이 맞힐까?',
  fly=('창 1,000조각 — 요청마다 1,000조각을 읽는다','사람들은 최근 일을 묻는 법이야. 8일 치면 충분해.'),robo=('창 4,000조각 — 요청마다 3,600조각을 읽는다','한 달이 통째로 들어가잖아. 못 맞힐 게 없지!'),rule='맞힌 질문 수(많을수록 좋음). 막대가 긴 쪽이 이긴다. 창 안에 정답이 있으면 맞힌 것으로 친다.'),
 sumh='정리 — 창이라는 기억, 글 편',
 sum='<div class="tw"><table class="tb" id="sumTb"><tr><th>창 크기</th><th>들어가는 날 수</th><th>맞힌 질문</th><th>요청 하나에 읽는 조각</th></tr></table></div><p style="font-size:14px;color:var(--muted)">표의 숫자는 이 페이지를 열 때 브라우저가 직접 계산한 값이다.</p>'+steps3([('모델은 간직하지 않는다','대화가 이어지는 것은 지난 대화를 매번 다시 보내기 때문이다.'),('창 밖은 없는 글','창보다 긴 대화는 앞부터 잘린다. 잘린 말은 답에 쓰일 수 없다.'),('키우면 맞히지만','창을 키우면 더 맞힌다. 그 값이 얼마인지가 다음 편이다.')])+field('긴 대화에서 초반에 정한 형식이나 조건이 어느 순간부터 지켜지지 않는다면, 그 말이 창에서 밀려났을 수 있다. 중요한 조건은 대화 끝에 다시 적거나, 새 대화를 열어 처음에 적는다.','실제 서비스는 창이 차면 그냥 자르지 않고 요약하거나 따로 적어 둔 것을 다시 넣기도 한다. 그 방법들이 2-4와 2-5의 주제다.'),
 outro=[('doc','front','오늘의 한 줄이에요. 대화형 AI의 “기억”은 대부분 창 안에 다시 넣어 준 글이에요.'),('asst','smile','모델 속 숫자가 대화 중에 하나도 안 바뀐다는 게 제일 뜻밖이었어요.'),('fly','coffee','3개밖에 못 맞혔군. 그래도 요청마다 3,600조각씩 읽히는 건 과해. 그 값은 따져 봐야지.'),('robo','happy','다 넣으니 다 맞혔지! 창은 클수록 좋아. 다음 편에서도 보여 주겠어!'),('moa','report','손님의 30일 대화는 제가 날짜별로 묶어 뒀어요. 필요한 날을 말씀하시면 꺼내 드릴게요.')],
 examples=['손님과의 30일 대화: 하루 120조각, 모두 3,600조각으로 정한 설명용 모형이다. 손님이 중요한 말을 한 날은 12일이고, 그 가운데 이틀은 앞에 한 말을 고친 날이다','질문 10개의 채점은 “정답이 든 날이 창 안이면 맞힘”이라는 단순한 규칙이다. 실제 모델의 답을 받아 채점한 것이 아니다','한 번 주고받을 때 40조각이라는 값은 계산을 쉽게 하려고 정한 숫자다','조각(토큰) 수는 실제 서비스의 창 크기와 단위가 다르다. 실제 창은 이보다 훨씬 크다'],
 refs=['cognee2026llmmemory','vaswani2017attention','ahn2026ts3_1_1'],
 claims=[('claim/history-resend','대화가 이어져 보이는 것은 이전 메시지를 매 요청마다 다시 넣기 때문이며, 이력이 빠지면 문맥에서도 사라진다','#lv1','cognee2026llmmemory','대화 이력 설명','concept/history-resend'),
  ('claim/context-window-limit','문맥 창은 한 번의 추론에서 처리할 수 있는 글의 양을 제한한다','#lv1','cognee2026llmmemory','컨텍스트 윈도우 절','concept/context-window'),
  ('claim/kv-cache-not-memory','KV 캐시는 계산을 다시 쓰는 장치일 뿐 대화 사이에 남는 기억이 아니다','#lv1','cognee2026llmmemory','KV 캐시 설명','concept/stateless-model')],
 openq=[('question/mem-just-enlarge','창을 키우기만 하면 기억 문제가 풀릴까?','#lv2','2-2에서 값과 가운데 놓침으로 다룬다')],
 nodes=[('concept/context-window','Concept','문맥 창','context window','#lv1','대화형 AI가 한 번에 읽고 쓸 수 있는 글의 양.'),
  ('concept/stateless-model','Concept','간직하지 않는 모델','stateless inference','#lv1','모델은 요청을 처리한 뒤 아무것도 들고 있지 않는다. 대화 중에 모델 속 숫자는 바뀌지 않는다.'),
  ('concept/history-resend','Concept','지난 대화 다시 보내기','conversation history resend','#lv1','대화 프로그램이 지난 대화 전체를 새 질문 앞에 붙여 매번 다시 보내는 방식.'),
  ('concept/token','Concept','조각 (토큰)','token','#lv1','모델이 글을 읽는 단위.'),
  ('concept/truncation','Concept','앞부분 잘라 내기','truncation','#lv2','대화가 창보다 길 때 가장 오래된 부분부터 버리는 처리.'),
  ('limitation/window-eviction','Limitation','창에서 밀려난 말은 없는 말이다','evicted context is gone','#lv2','창 밖으로 잘린 대화는 다시 넣어 주지 않는 한 답에 쓰일 수 없다.'),
  ('sim/2-1-resend','Simulation','요청 하나에 들어가는 글','tokens per request','#lv1'),('sim/2-1-window','Simulation','창 크기와 질문 10개','window size vs recall','#lv2'),('sim/2-1-duel','Simulation','대결: 창 1,000 vs 4,000','duel: small vs large window','#vs')],
 edges=[('concept/stateless-model','prerequisiteOf','concept/history-resend','#lv1'),('concept/token','partOf','concept/context-window','#lv1'),('concept/history-resend','prerequisiteOf','concept/truncation','#lv2'),('concept/context-window','hasLimitation','limitation/window-eviction','#lv2'),
  ('limitation/window-eviction','raises','question/mem-just-enlarge','#lv2'),('concept/history-resend','demonstratedBy','sim/2-1-resend','#lv1'),('limitation/window-eviction','demonstratedBy','sim/2-1-window','#lv2'),('concept/context-window','demonstratedBy','sim/2-1-duel','#vs')],
 gloss={'문맥 창':['문맥 창 (context window)','생성 AI','대화형 AI가 한 번에 읽고 쓸 수 있는 글의 양.'],'조각':['조각 (토큰)','생성 AI','모델이 글을 읽는 단위. 낱말보다 잘게 나뉘기도 한다.'],'요청':['요청','쓰임','모델에게 글을 보내고 답을 받는 한 번의 주고받기.'],
  '대화 프로그램':['대화 프로그램','쓰임','사용자와 모델 사이에서 지난 대화를 모아 요청을 만들어 보내는 프로그램.'],'창':['창','설정값','한 번에 읽을 수 있는 범위. 1부에서는 날 수, 2부에서는 조각 수로 센다.'],'모델 속 숫자':['모델 속 숫자 (가중치)','모델','모델이 학습으로 얻은 숫자들. 대화하는 동안에는 바뀌지 않는다.']},
 core=['문맥 창','조각','요청','대화 프로그램'],
 quiz={'why':[Q('대화하는 동안 모델 속 숫자(가중치)는',['말할 때마다 조금씩 바뀐다','바뀌지 않는다','대화가 끝나면 바뀐다'],1,'대화는 창에 넣은 글로 이어져요. 모델 속 숫자는 그대로예요.','“흔한 오해”를 떠올려 보세요.','concept/stateless-model')],
  'lv1':[Q('한 번에 40조각씩 늘 때, 5번째 요청까지 보낸 조각을 모두 더하면?',['200조각','600조각','1,000조각'],1,'40 × 5 × 6 ÷ 2 = 600조각이에요.','40 × (1+2+3+4+5)예요.','concept/history-resend','계산'),
        Q('지난 대화를 빼고 새 질문만 보내면 모델은',['지난 대화를 기억해서 이어 답한다','지난 대화를 모르는 채로 답한다','오류를 낸다'],1,'모델은 간직하지 않아요. 보내 준 글만 읽어요.','상담원과 녹취록을 떠올려 보세요.','concept/stateless-model')],
  'lv2':[Q('하루 120조각인 대화에서 창이 600조각이면 며칠 치가 들어갈까?',['3일','5일','6일'],1,'600 ÷ 120 = 5일이에요.','나눗셈 한 번이에요.','concept/truncation','계산'),
        Q('창보다 긴 대화에서 먼저 잘리는 쪽은?',['가장 최근 부분','가장 오래된 부분','가운데 부분'],1,'이 페이지의 방식은 앞에서부터 잘라요.','책상 위 녹취록을 떠올려 보세요.','limitation/window-eviction')],
  'vs':[Q('큰 창이 이긴 이 대결에서 따로 따져 봐야 할 것은?',['요청마다 읽는 조각이 3.6배라는 값','큰 창이 틀린 답을 냈다는 점','작은 창이 반칙했다는 점'],0,'더 맞혔지만 요청마다 3,600조각을 읽었어요. 그 값이 다음 편의 주제예요.','두 선수가 읽은 조각 수를 견줘 보세요.','concept/context-window')]},
)
JS=r'''
/* 칸 ① */
var NN=10,PER=40,cv=$('#c1'),cvb=$('#c1b');
function upd1(){var cum=PER*NN*(NN+1)/2;
  kpis($('#k1'),[[NN+'번째','요청','i'],[(PER*NN).toLocaleString()+'조각','이번 요청에 보내는 글','a'],[(PER*(NN-1)).toLocaleString()+'조각','그 가운데 다시 읽히는 지난 대화','m'],[cum.toLocaleString()+'조각','지금까지 보낸 글의 합','r']]);
  $('#ins1').innerHTML=tpl('<p>{0}번 주고받는 동안 새로 쓴 말은 {1}조각이에요. 모델이 읽은 양은 {2}조각으로 {3}배예요.</p>',NN,(PER*NN).toLocaleString(),cum.toLocaleString(),f2(cum/(PER*NN),1));drawAll();}
bindRange('r1N',function(v){NN=v;upd1();},function(v){return v+'번';});
addMod(cv,function(){var H=260,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var vals=[0];for(var i=1;i<=30;i++)vals.push(i<=NN?PER*i:0);
  var o=bars(ctx,W,H,vals,NN,{y0:0,y1:1260,ticks:[0,400,800,1200],fmt:function(v){return v.toFixed(0);},col:function(){return 'rgba(130,184,255,.7)';},xl:function(i){return i%5===0||i===1?i+'번':'';}});
  for(i=1;i<=NN;i++){ctx.fillStyle=COL.gfp;ctx.fillRect(o.X(i)-o.bw*0.35,o.Y(PER*i),o.bw*0.7,Math.max(2,o.Y(PER*(i-1))-o.Y(PER*i)));}
  txt(ctx,'초록 = 새로 쓴 말 · 파랑 = 다시 읽히는 지난 대화',o.P.l+4,14,{size:10,color:COL.muted});stamp(ctx,W,'설명용 도식');});
var ph=0;addMod(cvb,function(dt){var H=150,W=fit(cvb,H),ctx=cvb.getContext('2d');ctx.clearRect(0,0,W,H);if(!REDUCE)ph+=dt;var cyc=(ph%3)/3,th=Math.min(70,8+NN*2.2),mx=W/2;
  rr(ctx,mx-46,40,92,70,12,'rgba(37,40,58,.9)',COL.doc);txt(ctx,'모델',mx,58,{size:12,color:COL.doc,align:'center',w:'700'});
  var reading=cyc>0.3&&cyc<0.7;txt(ctx,reading?'읽는 중':'비어 있음',mx,88,{size:12,color:reading?COL.amber:COL.muted,align:'center'});
  var sx=40+(cyc<0.3?cyc/0.3:1)*(mx-120),ex=mx+70+(cyc>0.7?(cyc-0.7)/0.3:0)*(W-mx-150);
  if(cyc<0.7){rr(ctx,sx,75-th/2,56,th,4,'rgba(130,184,255,.5)',COL.info);rr(ctx,sx,75-th/2,56,5,2,COL.gfp);}
  if(cyc>0.7){rr(ctx,ex,66,44,18,4,'rgba(241,182,70,.5)',COL.amber);}
  txt(ctx,'대화 프로그램',44,134,{size:11,color:COL.muted});txt(ctx,tpl('지난 대화 {0}조각 + 새 질문',(PER*(NN-1)).toLocaleString()),44,22,{size:11,color:COL.info});txt(ctx,'답',W-60,134,{size:11,color:COL.amber});stamp(ctx,W,'설명용 도식');});
/* 칸 ② */
var WW=1000,cv2=$('#c2'),cv2b=$('#c2b');
function upd2(){var r=scoreWindow(WW),days=WW/DAY_TOK;
  kpis($('#k2'),[[WW.toLocaleString()+'조각','창 크기','a'],[days>=30?'30일 전부':f2(days,1)+'일 치','창에 들어가는 대화','i'],[r.n+' / 10','맞힌 질문',r.n===10?'g':(r.n>=5?'a':'r')],[r.cost.toLocaleString()+'조각','요청 하나에 읽는 글','m']]);
  $('#ins2').innerHTML=r.n===10?'<p class="g">30일이 통째로 창에 들어왔어요. 질문 10개의 정답이 모두 창 안에 있어요.</p>':tpl('<p class="r">최근 {0}일 치만 창에 들어와요. 그보다 앞에 한 말은 모델에게 없는 말이에요. 10개 가운데 {1}개의 정답이 창 밖이에요.</p>',f2(days,1),10-r.n)+'<p>거래처와 회의 요일은 27일, 29일에 바뀐 말이 창 안에 있어서 맞혔어요.</p>';drawAll();}
bindRange('r2W',function(v){WW=v;upd2();},function(v){return v.toLocaleString()+'조각';});
addMod(cv2,function(){drawDays(cv2,{win:WW,H:110});});
addMod(cv2b,function(){drawBoard(cv2b,scoreWindow(WW).ok,'마지막 날의 질문 10개');});
PAGE._T={w1000:scoreWindow(1000).n,w2000:scoreWindow(2000).n,w3600:scoreWindow(3600).n,w4000:scoreWindow(4000).n,cum30:PER*30*31/2};
/* 대결 */
Duel({el:'#duel',higherIsBetter:true,drawMargin:0.05,fmt:function(v){return v+'개';},run:function(){return {fly:scoreWindow(1000).n,robo:scoreWindow(4000).n,metric:'맞힌 질문 수'};},
  say:function(f,b){return tpl('맞힌 질문은 초파리 쪽 창 1,000조각이 {0}개, 주판봇 쪽 창 4,000조각이 {1}개예요. 요청마다 읽은 글은 1,000조각 대 3,600조각이에요.',f,b);},
  lessons:{R:'창 밖은 없는 글이다. 한 달 전의 말을 물으면 한 달이 들어가는 창이 이긴다',F:'작은 창으로 충분했다',D:'창 크기는 차이를 만들지 못했다'},
  after:function(){$('#duelNote').innerHTML='<p>큰 창은 요청마다 3.6배의 글을 읽었어요. 그리고 이 채점은 “창 안에 있으면 반드시 쓰인다”고 가정했어요. 두 가지를 2-2에서 따져요.</p>';}});
$('#sumTb').insertAdjacentHTML('beforeend',[500,1000,2000,3000,3600].map(function(w){var r=scoreWindow(w);return '<tr><td class="num">'+w.toLocaleString()+'조각</td><td class="num">'+(w>=3600?'30일':f2(w/DAY_TOK,1)+'일')+'</td><td class="num">'+r.n+' / 10</td><td class="num">'+r.cost.toLocaleString()+'조각</td></tr>';}).join(''));
upd1();upd2();
'''
