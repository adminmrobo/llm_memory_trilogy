# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
P=dict(
 title='읽으며 기억하기 — 기록을 펼치는 대신 메모 한 칸',chip='강 수위 · 매출 기록 앵커',
 q='기록을 펼쳐 놓지 않고도 먼 과거를 들고 다닐 수 있을까?',
 lead='<p>지금까지의 기억은 창이었다. 기록을 펼쳐 놓고 본다. 길게 보려면 길게 펼쳐야 했다. 이 페이지에서는 방법을 바꾼다. 기록은 한 번 읽고 넘기고, 읽을 때마다 <b>메모 한 칸</b>을 고쳐 쓴다. 숫자 하나에 지난 일 전부를 줄여 담는다. 한 칸씩 읽으며 메모를 고치는 신경망(순환 신경망)의 가장 단순한 꼴이다.</p>',
 objs=['창과 메모가 과거를 담는 방식의 차이(끊김과 흐려짐)를 말한다','새 메모 = 옛 메모 × 남기는 비율 + 새 값 × 나머지를 계산한다','먼 칸으로 되돌아가는 학습 신호가 왜 사라지는지 설명한다'],mins=22,
 kpis=[('1개','메모 한 칸이 들고 다니는 숫자'),('4 대 51','대결에서 두 선수가 정한 숫자 수'),('0.005','0.9를 50번 곱한 값'),('117','1.1을 50번 곱한 값')],
 hero=['오늘은 기억하는 방식을 바꿔요. 펼치지 않고, 읽으면서 메모를 고쳐 써요.','강 A의 기록을 다시 가져왔어요. 메모는 숫자 한 개짜리 칸이에요.','숫자 하나에 과거가 다 들어간다고? 뭉개질 텐데. 정말 쓸 만할까?','한 칸은 너무 적어! 창을 50일로 펼친 내 쪽이 든든하지.'],
 first3=['기록을 길게 펼치는 대신, 숫자 하나짜리 메모를 들고 다니며 새 값이 올 때마다 조금씩 고쳐 쓴다.','대화형 AI가 긴 대화를 요약해 들고 다니는 것과 같은 생각이다. 싸지만 뭉개진다는 장단점도 같다.','“최근 평균이 얼마쯤”처럼 줄여 둔 숫자 몇 개가, 수십 일 치 원본과 맞먹는 경우가 있다. 맞먹지 못하는 경우도 있다.'],
 abbr=['RNN','AR','MAE','LSTM'],cast=dict(fly='메모 몇 칸이면 된다',robo='길게 펼쳐야 든든하다'),
 whyh='왜 메모로 바꿔 볼까',whytag='방법: 읽을 때마다 메모 고쳐 쓰기',prev='1-3 꺼지지 않는 메아리',
 why=[('창은 길수록 비싸다','강 A에서 20일 창이 이겼지만 숫자 21개를 정하고 20일 치를 늘 펼쳐야 했다. 메아리는 그보다 훨씬 멀리 간다.'),('창 밖은 여전히 0','아무리 길게 펼쳐도 창 밖은 없는 것이다. 멀리서 오는 흔적을 조금이라도 담을 길이 없다.'),('줄여 담는다는 생각','지난 일을 전부 펼치는 대신 줄여서 한 칸에 담는다. 2부의 대화 요약, 3부의 기억 토큰으로 이어지는 생각이다.')],
 levels=[dict(id='lv1',no='①',title='메모 한 칸 — 끊기는 창, 흐려지는 메모',nav='메모 한 칸',tag1='방법: 옛 메모를 조금 남기고 새 값을 조금 더하기',tag2='일상: “요즘 평균 얼마쯤”이라는 감',
  why=('먼 과거의 흔적이 남는 기록(강 A)을 다룬다. 창을 길게 펼치면 숫자도 많이 정해야 하고 연습 문제도 준다.','창 모델은 창 안을 전부, 창 밖을 0으로 본다. “조금만 기억하기”가 안 된다.','숫자 하나를 메모로 둔다. 새 값이 오면 옛 메모를 일정 비율만 남기고, 새 값을 나머지만큼 더한다. 기록 원본은 넘겨 버린다.','가계부를 다 들고 다니는 대신 “요즘 하루에 얼마쯤 쓴다”는 감 하나만 들고 다니는 것이다.'),
  math=dict(ask='메모를 고쳐 쓰는 규칙이 식으로는 어떻게 생겼어요?',school='앞의 값으로 다음 값을 만드는 수열의 규칙(점화식)이다. 곱셈 두 번과 덧셈 한 번이다.',
   eq='새 메모 = 남기는 비율 × 옛 메모 + (1 − 남기는 비율) × 새 값',pieces=[('남기는 비율','옛 메모를 얼마나 남길지. 1에 가까울수록 옛일을 오래 붙든다'),('옛 메모','어제까지의 일을 줄여 담은 숫자'),('새 값','오늘 새로 읽은 값')],
   num='남기는 비율이 0.8, 옛 메모가 100, 오늘 읽은 값이 110이다. 0.8 × 100 + 0.2 × 110 = 80 + 22 = 102. 메모는 100에서 102로 조금 움직인다. 오늘 값의 몫은 0.2, 어제 값의 몫은 0.2 × 0.8 = 0.16, 그제는 0.128이다.',comment='기록을 안 펼쳐도 그제 값의 몫이 메모 안에 남아 있네요. 흐려지긴 해도 끊기지는 않고요.'),
  pair=('가계부 전체를 들고 다니지 않는다. “요즘 하루 3만 원쯤 쓴다”는 감 하나만 들고 다닌다. 오늘 5만 원을 쓰면 감을 조금 올린다. 석 달 전 지출도 그 감 속에 아주 조금 섞여 있다.','메모는 지난 모든 값의 몫을 조금씩 품는다. 가까운 날의 몫이 크고 먼 날의 몫은 작다. 순환 신경망은 이 메모(은닉 상태)를 여러 칸 두고, 고쳐 쓰는 규칙을 기록에서 배운다 [[elman1990finding]].'),
  talk=[('doc','front','창은 과거를 “끊어서” 보고, 메모는 “흐리게” 담아요. 50일 전 값은 어느 쪽에 남아 있을까요?'),('robo','chart','50일 창이면 50일 전이 또렷이 보이지! 메모엔 남은 게 없을걸.'),('fly','arms','“메모 세 칸”을 눌러 봐. 빠른 메모, 중간 메모, 느린 메모를 같이 쓰는 거야.')],
  panel='<div class="panel"><h3>실험 — 과거의 날마다 돌아가는 몫</h3>'+cv('c1','가로축은 며칠 전인지, 세로축은 그날 값이 기억에 차지하는 몫. 창은 네모난 모양으로 뚝 끊기고 메모는 비스듬히 흐려진다')+'<div class="ctrl">'+tg('g1','기억 방식',[('one','메모 한 칸'),('three','메모 세 칸')])+rg('r1A','남기는 비율',0.5,0.98,0.9,0.01)+'</div><div class="kpis" id="k1"></div><div class="insight" id="ins1" aria-live="polite"></div><h3>행동으로 보기 — 강 A를 읽으며 고쳐 쓰는 메모</h3>'+cv('c1b','강 A의 수위 200일과 그 위를 따라가는 메모 선. 남기는 비율이 클수록 메모가 느리고 매끈하게 움직인다','wide')+note('회색이 실제 수위, 청록이 메모다. 메모는 수위를 뒤따라가며 매끈하게 움직인다.')+'</div>',
  report='보고드려요. 남기는 비율 0.9인 메모 한 칸에서 10일 전 값의 몫은 3.9%, 50일 전은 0.06%예요. 20일 창은 20일 전까지 5%씩이고 21일 전부터는 0이에요.',
  stepsh='창과 메모 견주기',steps=['창은 창 안의 날마다 몫을 줄 수 있지만 창 밖은 0이다. 몫마다 숫자를 하나씩 정해야 한다.','메모 한 칸은 숫자 하나로 모든 과거에 몫을 준다. 다만 몫의 모양은 “하루마다 같은 비율로 줄기” 하나뿐이다.','빠른 메모·중간 메모·느린 메모 세 칸을 함께 쓰면 몫의 모양이 달라진다. 가까운 날은 크게, 먼 날도 얇게 오래 남는다. 1-3의 “나누기로 줄기”와 닮은 모양이다.','그래서 메모 몇 칸으로 오래 가는 메아리를 흉내 낼 수 있다.'],
  lim='메모는 뭉갠다. 7일마다 되풀이되는 요일 흐름처럼 날카로운 무늬는 메모 속에서 섞여 사라진다. 그리고 남기는 비율을 사람이 정했다. 기록에서 배우게 하면 어떨까? 다음 칸에서 그때 생기는 문제를 본다.',
  concepts=['concept/running-memo','concept/hidden-state','method/rnn','concept/retention-rate','concept/multi-timescale'],
  bridges=[gen('긴 대화를 다 들고 다니는 대신 요약 한 단락을 들고 다니는 것이 같은 생각이다. 원문은 넘기고, 줄인 것만 남긴다. 2-4에서 대화 압축으로 다시 만난다.','메모는 숫자를 섞어 평균 내지만, 대화 요약은 글의 뜻을 추려야 한다. 무엇이 뭉개지는지는 훨씬 복잡하다.')]),
 dict(id='lv2',no='②',title='전달 놀이 — 먼 칸의 신호가 사라진다',nav='사라지는 신호',tc='m',tag1='방법: 칸마다 같은 수를 거듭 곱하기',tag2='일상: 귓속말 전달 놀이',
  why=('남기는 비율 같은 숫자를 사람이 정하지 않고 기록에서 배우게 하고 싶다. 신경망은 끝에서 틀린 만큼을 앞 칸으로 되돌려 보내며 숫자를 고친다.','메모를 고쳐 쓰는 칸을 50번 지나왔다면, 되돌아가는 신호도 50칸을 거슬러 가야 한다. 칸을 지날 때마다 신호에 어떤 수가 곱해진다.','그 수가 1보다 작으면 신호가 금방 0이 되고, 1보다 크면 걷잡을 수 없이 커진다. 이 문제를 먼저 똑바로 봐야 고칠 수 있다 [[bengio1994learning]].','귓속말 전달 놀이다. 한 사람 지날 때마다 말이 조금씩 흐려지면, 쉰 번째 사람에게는 아무 말도 닿지 않는다.'),
  math=dict(ask='조금씩 줄어드는 건데 그렇게 큰 문제인가요?',school='같은 수를 거듭 곱하는 거듭제곱(지수)이다. 1보다 조금 작은 수도 거듭 곱하면 0에 가까워진다.',
   eq='n칸 뒤 신호 크기 = 처음 크기 × 곱해지는 수<sup>n</sup>',pieces=[('곱해지는 수','한 칸을 지날 때 신호가 몇 배가 되는지'),('n','거슬러 가는 칸 수'),('1보다 작으면','거듭할수록 0으로 간다 (신호가 사라짐)'),('1보다 크면','거듭할수록 끝없이 커진다 (신호가 터짐)')],
   num='0.9를 두 번 곱하면 0.81이다. 열 번이면 0.35, 쉰 번이면 0.005다. 처음 신호의 200분의 1이다. 거꾸로 1.1을 쉰 번 곱하면 117이 된다.',comment='0.9와 1.1은 별 차이 없어 보였는데 50번 곱하니 0.005와 117이네요. 딱 1이 아니면 어느 쪽으로든 망가지는군요.'),
  pair=('쉰 명이 한 줄로 서서 귓속말을 전한다. 한 사람이 10%씩만 흘려도 끝에 닿는 말은 처음의 200분의 1이다. 거꾸로 한 사람이 10%씩 부풀리면 끝에서는 117배의 헛소문이 된다.','순환 신경망이 배울 때 먼 칸으로 되돌아가는 학습 신호가 이렇게 줄어든다. 그래서 “50칸 전의 일이 지금 답에 중요했다”는 것을 배우기 어렵다. 메모는 먼 과거를 품을 수 있어도, 품는 법을 배우지 못한다.'),
  talk=[('doc','think','한 칸에 0.9배씩이면 50칸 뒤에는 얼마가 남을까요?'),('robo','happy','0.9면 거의 그대로잖아! 절반은 남겠지.'),('fly','point','곱해지는 수를 0.9에 놓고 칸 수를 50까지 밀어 봐. 그다음 1.1로 바꿔 보고.')],
  panel='<div class="panel"><h3>실험 — 거슬러 가는 신호</h3>'+cv('c2','가로축은 거슬러 간 칸 수, 세로축은 남은 신호 크기. 곱해지는 수가 1보다 작으면 0으로 떨어지고 1보다 크면 치솟는다')+'<div class="ctrl">'+rg('r2W','한 칸에 곱해지는 수',0.7,1.3,0.9,0.05)+rg('r2N','거슬러 가는 칸 수',5,60,50)+'</div><div class="kpis" id="k2"></div><div class="insight" id="ins2" aria-live="polite"></div><h3>행동으로 보기 — 귓속말 줄</h3>'+cv('c2b','한 줄로 선 칸마다 신호 막대가 그려진다. 왼쪽 끝에서 출발한 신호가 오른쪽으로 갈수록 작아지거나 커진다','wide')+note('오른쪽 끝이 지금, 왼쪽으로 갈수록 먼 과거 칸이다. 막대 높이가 그 칸에 닿은 학습 신호의 크기다.')+'</div>',
  report='보고드려요. 0.9배씩이면 50칸 뒤 0.005, 1.1배씩이면 117이에요. 작은 신경망에서 실제로 재 보니 같은 0.9라도 식보다 더 빨리 줄었어요.',
  stepsh='왜 배우기 어려운가',steps=['신경망은 끝에서 틀린 만큼을 앞 칸으로 되돌려 보내 숫자를 고친다.','되돌아가는 길에 칸마다 같은 종류의 수가 곱해진다.','그 수가 1보다 작으면 먼 칸에는 신호가 닿지 않는다. 먼 과거를 쓰는 법을 못 배운다.','1보다 크면 신호가 터져서 학습이 망가진다. 딱 1 근처로 유지하기가 어렵다.'],
  lim='메모는 먼 과거를 싸게 품지만, 무엇을 오래 붙들지 스스로 배우지 못한다. 신호가 줄지 않고 지나갈 곧은 길과, 그때그때 여닫는 문이 필요하다. 1-5의 지우개 달린 메모장이다.',
  intern=SIA,concepts=['concept/vanishing-gradient','concept/exploding-gradient','concept/backprop-through-time'])],
 duel=dict(title='메모 세 칸 vs 50일 창 — 강 A에서',metric='검증 오차',tag='일상: 감 세 개 vs 50쪽',q='강 A의 내일 수위를 맞힌다. 빠른·중간·느린 메모 세 칸을 쓰는 쪽과 50일 창을 쓰는 쪽, 검증 300일에서 누가 덜 빗나갈까?',
  fly=('메모 세 칸 — 정할 숫자 4개','숫자 네 개면 돼. 먼 과거는 느린 메모가 들고 있어.'),robo=('50일 창 — 정할 숫자 51개','메아리가 오래 가는 강이야. 50일을 또렷이 본 쪽이 이겨!'),rule='검증 오차(평균 절대 오차, 낮을수록 좋음). 막대가 짧은 쪽이 이긴다.'),
 sumh='정리 — 창과 메모',
 sum='<div class="tw"><table class="tb" id="sumTb"><tr><th>기억 방식</th><th>정할 숫자</th><th>강 A 검증 오차 (cm)</th><th>매출 기록 검증 오차 (만 원)</th></tr></table></div><p style="font-size:14px;color:var(--muted)">표의 숫자는 이 페이지를 열 때 브라우저가 직접 계산한 값이다. 매출 기록의 창은 28일, 강 A의 창은 50일이다.</p>'+steps3([('창은 끊기고 메모는 흐려진다','창은 또렷하지만 길이만큼 값을 치른다. 메모는 싸지만 뭉갠다.'),('기록에 따라 승자가 갈린다','매끈하게 오래 가는 강 A에서는 메모 세 칸이 50일 창과 비겼다. 요일 무늬가 뚜렷한 매출 기록에서는 메모가 크게 졌다.'),('배우게 하면 신호가 사라진다','메모 고쳐 쓰는 법을 기록에서 배우려면, 먼 칸까지 학습 신호가 닿아야 한다.')])+field('긴 이력을 다 들고 다니는 대신 “요약 숫자 몇 개”를 들고 다니는 설계는 흔하다. 최근 평균, 느린 평균을 함께 두는 식이다. 쓰기 전에 그 요약이 뭉개 버리는 무늬(요일, 월말 같은 것)가 없는지 확인한다.','이 페이지의 메모는 남기는 비율을 사람이 정한 가장 단순한 꼴이다. 실제 순환 신경망은 메모가 여러 칸이고 고쳐 쓰는 규칙도 배운다.'),
 outro=[('doc','front','오늘의 한 줄이에요. 기억은 펼칠 수도 있고 줄여 담을 수도 있어요. 줄이면 싸지만 뭉개져요.'),('asst','smile','숫자 4개가 숫자 51개와 비긴 게 놀라웠어요. 매출 기록에서는 크게 졌지만요.'),('fly','coffee','비긴 걸로 만족해. 그런데 남기는 비율을 내가 정한 게 걸려. 배우게 할 수는 없나?'),('robo','meh','51개나 정했는데 비기다니… 다음엔 문 달린 메모장으로 제대로 붙어 보자!'),('moa','report','오늘 메모 세 칸은 제가 받아 적어 뒀어요. 숫자 세 개라 주머니에 들어가요.')],
 examples=['강 A: 가상의 하루 수위(cm) 2000일 (1-3과 같은 기록, 시드 2027). 훈련 1400일 · 검증 300일','매출 기록: 가게 하루 매출(만 원) 300일 (시드 2026). 훈련 200일 · 검증 50일','메모 세 칸의 남기는 비율 0.5 · 0.9 · 0.98은 사람이 고른 값이다. 세 메모를 섞는 비율 4개만 훈련 기록으로 정했다','“작은 신경망에서 잰 값”은 메모 한 칸짜리 순환 신경망에 무작위 입력을 넣고 계산한 설명용 값이다','0.9와 1.1을 50번 곱한 값(0.005, 117)은 계산값이다'],
 refs=['elman1990finding','bengio1994learning','granger1980introduction'],
 claims=[('claim/elman-srn','단순 순환 신경망은 앞 칸의 상태를 다음 칸의 입력으로 되돌려 시간의 구조를 배운다','#lv1','elman1990finding','논문 전체','method/rnn'),
  ('claim/bengio-vanishing','순환 신경망에서 먼 칸으로 되돌아가는 학습 신호는 칸 수에 따라 지수적으로 줄거나 커진다','#lv2','bengio1994learning','논문 전체','concept/vanishing-gradient')],
 openq=[('question/mem-learn-what-to-keep','무엇을 오래 붙들지 기록에서 스스로 배우게 할 수 있을까?','#lv2','1-5에서 LSTM의 문으로 다룬다')],
 nodes=[('concept/running-memo','Concept','메모 한 칸 (지수 평균)','running memo (exponential average)','#lv1','새 값이 올 때마다 옛 메모를 일정 비율 남기고 새 값을 더해 고쳐 쓰는 숫자 하나.'),
  ('concept/hidden-state','Concept','은닉 상태','hidden state','#lv1','순환 신경망이 칸마다 고쳐 쓰는 메모. 지난 입력을 줄여 담는다.'),
  ('method/rnn','Method','순환 신경망 (RNN)','recurrent neural network','#lv1','한 칸씩 읽으며 메모(은닉 상태)를 고쳐 쓰는 신경망.'),
  ('concept/retention-rate','Concept','남기는 비율','retention rate','#lv1','메모를 고쳐 쓸 때 옛 메모를 얼마나 남기는지.'),
  ('concept/multi-timescale','Concept','속도가 다른 메모 여러 칸','multiple timescales','#lv1','빠른 메모와 느린 메모를 함께 써서 천천히 꺼지는 메아리를 흉내 내는 방법.'),
  ('concept/vanishing-gradient','Concept','사라지는 학습 신호 (기울기 소실)','vanishing gradient','#lv2','먼 칸으로 되돌아가는 학습 신호가 거듭 곱해져 0에 가까워지는 현상.'),
  ('concept/exploding-gradient','Concept','터지는 학습 신호 (기울기 폭주)','exploding gradient','#lv2','거듭 곱해지는 수가 1보다 커서 학습 신호가 끝없이 커지는 현상.'),
  ('concept/backprop-through-time','Concept','시간을 거슬러 되돌려 보내기','backpropagation through time','#lv2','끝에서 틀린 만큼을 앞 칸으로 차례로 되돌려 보내 숫자를 고치는 학습 방법.'),
  ('limitation/memo-blurs','Limitation','메모는 뭉갠다','a memo blurs sharp patterns','#lv1','요일 흐름처럼 날카로운 무늬는 메모 속에서 섞여 사라진다.'),
  ('sim/1-4-weights','Simulation','과거의 날마다 돌아가는 몫','weight profile: window vs memo','#lv1'),('sim/1-4-chain','Simulation','거슬러 가는 신호','gradient chain','#lv2'),('sim/1-4-duel','Simulation','대결: 메모 세 칸 vs 50일 창','duel: three memos vs 50-day window','#vs')],
 edges=[('concept/running-memo','broader','concept/hidden-state','#lv1'),('concept/hidden-state','partOf','method/rnn','#lv1'),('concept/retention-rate','partOf','concept/running-memo','#lv1'),('concept/running-memo','prerequisiteOf','concept/multi-timescale','#lv1'),
  ('concept/running-memo','hasLimitation','limitation/memo-blurs','#lv1'),('method/rnn','hasLimitation','concept/vanishing-gradient','#lv2'),('concept/vanishing-gradient','contrastsWith','concept/exploding-gradient','#lv2'),('concept/backprop-through-time','prerequisiteOf','concept/vanishing-gradient','#lv2'),
  ('concept/vanishing-gradient','raises','question/mem-learn-what-to-keep','#lv2'),('concept/running-memo','demonstratedBy','sim/1-4-weights','#lv1'),('concept/vanishing-gradient','demonstratedBy','sim/1-4-chain','#lv2'),('concept/multi-timescale','demonstratedBy','sim/1-4-duel','#vs')],
 gloss={'메모':['메모 (은닉 상태)','이 시리즈의 별명','지난 일을 줄여 담은 숫자 칸. 새 값이 올 때마다 고쳐 쓴다.'],'남기는 비율':['남기는 비율','설정값','메모를 고쳐 쓸 때 옛 메모를 얼마나 남기는지. 1에 가까울수록 옛일을 오래 붙든다.'],
  '순환 신경망':['순환 신경망 (RNN)','신경망','한 칸씩 읽으며 메모를 고쳐 쓰는 신경망.'],'은닉 상태':['은닉 상태','신경망','순환 신경망이 칸마다 고쳐 쓰는 메모.'],'학습 신호':['학습 신호 (기울기)','학습','끝에서 틀린 만큼을 앞쪽으로 되돌려 보내는 값. 이 값으로 숫자를 고친다.'],
  '창':['창 (window)','설정값','다음 값을 짐작할 때 펼쳐 놓는 과거 구간.'],'메아리':['메아리','이 시리즈의 별명','과거의 값이 오늘 값에 남긴 흔적.'],'검증 오차':['검증 오차','지표','모델이 본 적 없는 검증 기간에서 평균적으로 빗나간 크기.'],'몫':['몫 (가중치)','계산','과거의 어느 날 값이 지금 기억에서 차지하는 비중.'],'요일 흐름':['요일 흐름','데이터','요일마다 되풀이되는 오르내림.']},
 core=['메모','남기는 비율','순환 신경망','학습 신호','몫'],
 quiz={'why':[Q('메모가 창과 다른 점은?',['기록을 더 길게 펼친다','기록을 펼치지 않고 줄인 숫자만 들고 다닌다','과거를 전혀 쓰지 않는다'],1,'읽고 넘기면서 메모만 고쳐 써요.','펼치기와 줄여 담기를 견줘 보세요.','concept/running-memo')],
  'lv1':[Q('남기는 비율 0.8, 옛 메모 50, 새 값 100이면 새 메모는?',['60','80','90'],0,'0.8 × 50 + 0.2 × 100 = 40 + 20 = 60이에요.','옛 메모에 0.8, 새 값에 0.2를 곱해요.','concept/retention-rate','계산'),
        Q('메모 세 칸(빠른·중간·느린)을 함께 쓰는 까닭은?',['계산을 빠르게 하려고','가까운 날은 크게, 먼 날도 얇게 오래 담으려고','요일 흐름을 또렷이 보려고'],1,'속도가 다른 메모를 섞으면 천천히 꺼지는 몫 모양을 만들 수 있어요.','1-3의 “나누기로 줄기”를 떠올려 보세요.','concept/multi-timescale')],
  'lv2':[Q('한 칸에 0.5배씩 줄어드는 신호는 3칸 뒤에 얼마가 남을까?',['0.5','0.25','0.125'],2,'0.5 × 0.5 × 0.5 = 0.125예요.','0.5를 세 번 곱해요.','concept/vanishing-gradient','계산'),
        Q('학습 신호가 먼 칸에 닿지 않으면 생기는 일은?',['먼 과거를 쓰는 법을 배우지 못한다','계산이 빨라진다','메모가 커진다'],0,'고칠 신호가 안 오니 먼 과거와 지금을 잇는 법을 못 배워요.','신호가 닿아야 숫자를 고칠 수 있어요.','concept/vanishing-gradient')],
  'vs':[Q('강 A에서 메모 세 칸이 50일 창과 비긴 결과의 뜻은?',['메모가 언제나 창만큼 좋다','이 기록에서는 줄여 담은 숫자 몇 개가 긴 원본과 맞먹었다','창이 쓸모없다'],1,'매끈하게 오래 가는 메아리는 메모로 잘 담겨요. 매출 기록에서는 결과가 달랐어요.','매출 기록의 결과도 함께 떠올려 보세요.','concept/multi-timescale')]},
)
JS=r'''
var XA=makeLong(2027,2000,0.4,{K:1000}),Y=makeSeries(2026,300,{}),TR=1400,VA=1700,AS=[0.5,0.9,0.98];
var M3=scoreMemo(XA,AS,TR,VA,100),M1=scoreMemo(XA,[0.9],TR,VA,100),W50=scoreAR(XA,50,TR,VA),W20=scoreAR(XA,20,TR,VA);
var SM3=scoreMemo(Y,AS,200,250),SM1=scoreMemo(Y,[0.9],200,250),SW=scoreAR(Y,28,200,250);
// 세 메모의 섞는 비율 → 날마다의 몫
var mixW=[];(function(){var b=M3.beta;for(var k=0;k<=80;k++){var s=0;for(var j=0;j<3;j++)s+=b[j+1]*(1-AS[j])*Math.pow(AS[j],k);mixW.push(s);}})();
PAGE._T={m3:M3.va,m1:M1.va,w50:W50.va,w20:W20.va,sm3:SM3.va,sm1:SM1.va,sw:SW.va,beta:M3.beta};
/* 칸 ① */
var MODE='one',Aa=0.9,cv=$('#c1'),cvb=$('#c1b');
function wOne(k){return (1-Aa)*Math.pow(Aa,k);}
function upd1(){var hl=Math.log(0.5)/Math.log(Aa);
  if(MODE==='one')kpis($('#k1'),[['1개','들고 다니는 숫자','g'],[f2(wOne(9)*100,1)+'%','10일 전 값의 몫','a'],[f2(wOne(49)*100,2)+'%','50일 전 값의 몫','m'],[tpl('{0}일',f2(hl,1)),'몫이 절반이 되는 날 수','i']]);
  else kpis($('#k1'),[['3개','들고 다니는 숫자','g'],[f2(mixW[9]/mixW[0]*100,0)+'%','10일 전 몫 (어제 몫 대비)','a'],[f2(mixW[49]/mixW[0]*100,1)+'%','50일 전 몫 (어제 몫 대비)','m'],['0.5 · 0.9 · 0.98','세 메모의 남기는 비율','i']]);
  $('#ins1').innerHTML=MODE==='one'?tpl('<p>남기는 비율 {0}인 메모예요. 몫은 {1}일마다 절반이 돼요. 20일 창(회색 네모)은 21일 전부터 0이지만, 메모는 얇게나마 이어져요.</p>',f2(Aa,2),f2(hl,1)):
    '<p class="g">빠른 메모(0.5), 중간 메모(0.9), 느린 메모(0.98)를 강 A의 훈련 기록이 정한 비율로 섞었어요. 가까운 날은 크게, 먼 날은 얇고 길게 남아요. 한 칸짜리 곡선보다 꼬리가 길어요.</p>';drawAll();}
toggleGroup('#g1 button',function(v){MODE=v;upd1();});bindRange('r1A',function(v){Aa=v;upd1();},function(v){return f2(v,2);});
addMod(cv,function(){var H=280,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var d=[],w=[],i;
  for(i=0;i<=80;i++){d.push(MODE==='one'?wOne(i)/wOne(0):mixW[i]/mixW[0]);w.push(i<20?0.5:0);}
  var o=plot(ctx,W,H,{x0:1,x1:81,y0:0,y1:1.05,yn:4,yfmt:function(v){return v.toFixed(2);},xticks:[1,10,20,30,50,80],xlab:function(v){return v+'일 전';},lines:[{d:w,x0:1,color:COL.muted,w:1.4,dash:[5,4]},{d:d,x0:1,color:COL.robo,w:2.3}],legend:[[MODE==='one'?'메모 한 칸':'메모 세 칸',COL.robo],['20일 창',COL.muted]]});
  txt(ctx,'세로축: 어제 값의 몫을 1로 본 상대 크기',W-o.P.r-6,o.P.t+ih_(o)-8,{size:10,color:COL.muted,align:'right'});stamp(ctx,W,'설명용 도식');});
function ih_(o){return o.ih;}
addMod(cvb,function(){var H=180,W=fit(cvb,H),ctx=cvb.getContext('2d');ctx.clearRect(0,0,W,H);var a=1200,seg=XA.slice(a,a+200),m=[],h=XA[a-1],hs=[XA[a-1],XA[a-1],XA[a-1]],i;
  for(i=0;i<200;i++){if(MODE==='one'){h=Aa*h+(1-Aa)*seg[i];m.push(h);}else{hs=hs.map(function(v,j){return AS[j]*v+(1-AS[j])*seg[i];});m.push(hs[2]);}}
  var rgv=rangeOf([seg]),o=plot(ctx,W,H,{x0:0,x1:199,y0:rgv[0],y1:rgv[1],yn:3,xticks:[0,50,100,150,199],xlab:function(v){return v+'일';},lines:[{d:seg,color:'#8f8da8',w:1},{d:m,color:COL.robo,w:2.2}]});
  txt(ctx,MODE==='one'?'메모 한 칸':'세 칸 가운데 느린 메모(0.98)',o.P.l+6,o.P.t+10,{size:11,color:COL.robo});stamp(ctx,W,'설명용 모형 · 실제 데이터 아님');});
/* 칸 ② */
var Ww=0.9,Nn=50,cv2=$('#c2'),cv2b=$('#c2b');
// 메모 한 칸짜리 순환 신경망 h=tanh(w·h+x)에서 실제로 잰 되돌림 신호 (입력 시드 고정)
function realChain(w,n){var r=rng(7),h=0,hs=[];for(var t=0;t<n;t++){h=tanh(w*h+0.6*gauss(r));hs.push(h);}var g=1,out=[1];for(t=n-1;t>=1;t--){g*=w*(1-hs[t]*hs[t]);out.push(Math.abs(g));}return out;}
function tiny(x){return x<0.001?'0.001보다 작음':f2(x,3);}
function upd2(){var v=Math.pow(Ww,Nn),rc=realChain(Ww,Nn+1)[Nn];
  kpis($('#k2'),[[f2(Ww,2),'한 칸에 곱해지는 수','a'],[Nn+'칸','거슬러 가는 칸 수','i'],[v<0.001?tiny(v):(v>1000?Math.round(v).toLocaleString():f2(v,3)),'식으로 계산한 남은 신호',v<0.05?'r':(v>20?'m':'g')],[tiny(rc),'작은 신경망에서 잰 값','i']]);
  $('#ins2').innerHTML=Math.abs(Ww-1)<1e-9?'<p class="g">딱 1이면 신호가 그대로 지나가요. 문제는 이 값을 늘 1로 지키기 어렵다는 거예요.</p>':
    (Ww<1?tpl('<p class="r">{0}칸 전에는 처음 신호를 1로 볼 때 {1}만 닿아요. 그 칸의 일이 지금 답에 중요했더라도, 그걸 배울 신호가 없어요.</p>',Nn,v<0.001?'0.001에도 못 미치는 크기':f2(v,3)):tpl('<p class="m">{0}칸을 거슬러 가면 신호가 {1}배로 불어나요. 숫자를 한 번에 너무 크게 고쳐 학습이 망가져요.</p>',Nn,v>1000?Math.round(v).toLocaleString():f2(v,1)))+
    '<p>작은 신경망에서 잰 값이 식보다 작은 것은, 메모를 고쳐 쓸 때 값을 일정 범위 안으로 눌러 주는 단계가 신호를 한 번 더 줄이기 때문이에요.</p>';drawAll();}
bindRange('r2W',function(v){Ww=v;upd2();},function(v){return f2(v,2);});bindRange('r2N',function(v){Nn=v;upd2();},function(v){return v+'칸';});
addMod(cv2,function(){var H=270,W=fit(cv2,H),ctx=cv2.getContext('2d');ctx.clearRect(0,0,W,H);var d=[],rc=realChain(Ww,61),hi=Math.max(1.2,Math.min(8,Math.pow(Ww,Nn)*1.1));
  for(var i=0;i<=60;i++)d.push(Math.min(Math.pow(Ww,i),hi));
  var o=plot(ctx,W,H,{x0:0,x1:60,y0:0,y1:hi,yn:4,yfmt:function(v){return v.toFixed(1);},xticks:[0,10,20,30,40,50,60],xlab:function(v){return v+'칸';},lines:[{d:rc.map(function(v){return Math.min(v,hi);}),color:COL.info,w:1.4,dash:[4,3]},{d:d,color:COL.amber,w:2.3}],legend:[['식: 곱해지는 수를 거듭 곱함',COL.amber],['작은 신경망에서 잰 값',COL.info]],marks:[{x:Nn,color:COL.eye,label:Nn+'칸'}]});
  if(Math.pow(Ww,60)>hi)txt(ctx,'↑ 그림 밖으로 치솟음',W-o.P.r-6,o.P.t+26,{size:11,color:COL.eye,align:'right',w:'700'});stamp(ctx,W,'설명용 도식');});
var ph=0;addMod(cv2b,function(dt){var H=140,W=fit(cv2b,H),ctx=cv2b.getContext('2d');ctx.clearRect(0,0,W,H);if(!REDUCE)ph+=dt;var n=Math.min(Nn,30),gw=(W-20)/n,cur=REDUCE?n:Math.floor(ph/0.12)%(n+10),mx=Math.max(1,Math.pow(Ww,n-1));
  for(var i=0;i<n&&i<=cur;i++){var v=Math.pow(Ww,i)/mx,x=W-10-(i+1)*gw,hh=Math.max(1.5,v*86);rr(ctx,x+2,112-hh,gw-4,hh,3,v<0.05?'rgba(240,96,77,.6)':'rgba(241,182,70,.75)');}
  txt(ctx,'지금',W-12,126,{size:10,color:COL.muted,align:'right'});txt(ctx,n+'칸 전',12,126,{size:10,color:COL.muted});stamp(ctx,W,'설명용 도식');});
/* 대결 */
Duel({el:'#duel',higherIsBetter:false,drawMargin:0.05,fmt:function(v){return f2(v,2);},run:function(){return {fly:M3.va,robo:W50.va,metric:'검증 오차'};},
  say:function(f,b){return tpl('검증 오차는 초파리 쪽 메모 세 칸이 {0}cm, 주판봇 쪽 50일 창이 {1}cm예요. 차이는 큰 값의 {2}%예요.',f2(f,2),f2(b,2),f2(Math.abs(f-b)/Math.max(f,b)*100,1));},
  lessons:{D:'숫자 4개가 숫자 51개와 비겼다. 매끈하게 오래 가는 메아리는 줄여 담아도 잃는 것이 적다',F:'줄여 담은 메모가 긴 창을 앞섰다',R:'또렷이 본 긴 창이 뭉갠 메모를 앞섰다'},
  after:function(){$('#duelNote').innerHTML=tpl('<p>같은 대결을 매출 기록에서 하면 메모 세 칸 {0}만 원, 28일 창 {1}만 원으로 메모가 크게 져요. 요일 흐름이 메모 속에서 뭉개지기 때문이에요.</p><p>강 A에서 메모 한 칸(0.9)만 쓰면 {2}cm, 20일 창은 {3}cm예요.</p>',f2(SM3.va,2),f2(SW.va,2),f2(M1.va,2),f2(W20.va,2));}});
/* 정리 */
function row(n,k,a,b){return '<tr><td>'+n+'</td><td class="num">'+k+'</td><td class="num">'+a+'</td><td class="num">'+b+'</td></tr>';}
$('#sumTb').insertAdjacentHTML('beforeend',row('메모 한 칸 (0.9)','2개',f2(M1.va,2),f2(SM1.va,2))+row('메모 세 칸','4개',f2(M3.va,2),f2(SM3.va,2))+row('창','51개 · 29개',f2(W50.va,2),f2(SW.va,2)));
upd1();upd2();
'''
