# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
P=dict(
 title='지우개 달린 메모장 — 무엇을 남길지 스스로 정하는 기억',chip='메모장 앵커',
 q='30칸 전에 들은 한마디를 잡음 속에서 끝까지 붙들 수 있을까?',
 lead='<p>1-4의 메모는 늘 같은 비율로 흐려졌다. 중요한 일도 하찮은 일도 똑같이 흐려진다. 이 페이지의 메모장에는 <b>지우개</b>와 <b>펜</b>이 달려 있다. 칸을 읽을 때마다 얼마나 지울지, 얼마나 적을지를 그때그때 정한다. 이름은 LSTM이다 [[hochreiter1997long]].</p><p style="font-size:14px;color:var(--muted)">문 세 개를 하나씩 뜯어보는 자세한 해설은 「시계열 3부작」 2-2에 있다 [[ahn2026ts3_2_2]]. 여기서는 “기억”에 필요한 만큼만 다룬다.</p>',
 objs=['새 메모 = 지우개 × 옛 메모 + 펜 × 새 내용을 계산한다','지우개를 열어 두면(1에 가깝게) 먼 칸의 신호가 왜 살아남는지 말한다','늘 같은 비율로 흐려지는 메모와 문 달린 메모장의 차이를 과제로 확인한다'],mins=22,
 kpis=[('2개','기억에 쓰는 문 (지우개 · 펜)'),('1.0','지우개를 다 열었을 때 한 칸에 곱해지는 수'),('30칸','신호 기억 시험의 길이'),('101개','대결에서 메모장이 정한 숫자')],
 hero=['오늘은 메모에 문을 달아요. 지울지 적을지를 칸마다 따로 정하는 메모장이에요.','신호 기억 시험을 준비했어요. 첫 칸에 신호가 하나 오고, 뒤로 29칸은 잡음이에요.','문이 많으면 고장도 많아. 메모 한 칸으로는 정말 안 될까?','문 달린 메모장! 숫자가 101개나 되잖아. 이건 이긴 거야.'],
 first3=['칸을 읽을 때마다 “옛 메모를 얼마나 남길지”와 “새 내용을 얼마나 적을지”를 따로 정하는 메모장이다.','중요한 것은 오래 붙들고 하찮은 것은 흘려보내는 일은 대화형 AI의 기억 관리에서도 똑같이 필요하다.','모든 것을 같은 비율로 잊는 요약은 정작 중요한 한마디를 놓친다. 무엇을 남길지 정하는 규칙이 따로 있어야 한다.'],
 abbr=['LSTM','RNN','MAE'],cast=dict(fly='메모 한 칸이면 된다',robo='문 달린 메모장이 낫다'),
 whyh='왜 메모에 문을 다는가',whytag='방법: 지우개와 펜을 칸마다 조절하기',prev='1-4 읽으며 기억하기',
 why=[('똑같이 흐려지는 메모','1-4의 메모는 중요한 값도 잡음도 같은 비율로 섞고 같은 비율로 잊었다.'),('사라지는 학습 신호','먼 칸으로 되돌아가는 신호가 칸마다 줄어, 먼 과거를 쓰는 법을 배울 수 없었다.'),('두 문제를 한 번에','메모가 다음 칸으로 넘어갈 때 곱해지는 수를 문으로 조절한다. 문을 열어 두면 메모도, 학습 신호도 줄지 않고 지나간다.')],
 levels=[dict(id='lv1',no='①',title='지우개와 펜 — 메모 한 줄을 손으로 고쳐 쓰기',nav='지우개와 펜',tag1='방법: 지우개 × 옛 메모 + 펜 × 새 내용',tag2='일상: 수첩의 지우개와 펜',
  why=('첫 칸에서 중요한 값을 하나 들었다. 그 뒤로 잡음이 수십 칸 이어진다. 끝에서 첫 칸의 값을 말해야 한다.','늘 같은 비율로 고쳐 쓰는 메모는 잡음이 들어올 때마다 첫 값을 조금씩 덮어쓴다. 남기는 비율을 높이면 첫 값도 조금밖에 못 적는다.','문을 두 개 둔다. 지우개 문은 옛 메모를 얼마나 남길지, 펜 문은 새 내용을 얼마나 적을지 정한다. 둘을 따로 움직인다. 중요한 칸에서는 펜을 열고, 잡음 칸에서는 펜을 닫고 지우개만 열어 둔다.','수첩에 중요한 약속을 적고 나면 펜 뚜껑을 닫아 둔다. 다음 약속이 생길 때까지 수첩은 그대로다.'),
  math=dict(ask='1-4의 식이랑 비슷해 보이는데, 뭐가 달라졌어요?',school='일차식이다. 곱셈 두 번과 덧셈 한 번. 달라진 점은 두 비율이 서로 묶여 있지 않다는 것이다.',
   eq='새 메모 = 지우개 × 옛 메모 + 펜 × 새 내용',pieces=[('지우개 (0~1)','옛 메모를 남기는 비율. 1이면 하나도 안 지운다'),('펜 (0~1)','새 내용을 적는 세기. 0이면 아무것도 안 적는다'),('1-4의 메모','펜 = 1 − 지우개로 묶여 있었다. 많이 남기면 조금밖에 못 적었다')],
   num='옛 메모가 10이다. 지우개 0.9, 펜 0.5, 새 내용이 4라면 0.9 × 10 + 0.5 × 4 = 9 + 2 = 11이다. 지우개 1, 펜 0이면 1 × 10 + 0 × 4 = 10. 새 내용이 무엇이든 메모는 그대로다.',comment='지우개 1, 펜 0이면 몇 칸을 지나도 10이 그대로네요. 곱해지는 수가 딱 1이니까 1-4의 사라지는 신호 문제도 없고요!'),
  pair=('수첩에 지우개와 펜이 달려 있다. 중요한 약속을 들으면 펜으로 꾹 눌러 적는다. 그 뒤 잡담이 이어지는 동안에는 펜 뚜껑을 닫고 지우개도 대지 않는다. 약속이 끝나면 그때 지운다.','LSTM은 칸마다 문을 여닫는 정도를 입력을 보고 계산한다. 메모(셀 상태)가 다음 칸으로 넘어갈 때 곱해지는 수는 지우개 문의 값이다. 이 값이 1에 가까우면 메모도 학습 신호도 줄지 않는다. 지우개 문은 뒤에 더해진 장치다 [[gers2000learning]].'),
  talk=[('doc','front','첫 칸에 10을 적고 잡음 속에서 50칸을 지나요. 끝에 10이 남아 있게 하려면 문을 어떻게 둘까요?'),('robo','chart','지우개도 펜도 활짝! 문은 열라고 있는 거야.'),('fly','arms','정말? 펜을 0으로, 지우개를 1로 놓아 봐. 그다음 지우개만 0.9로 내려 보고.')],
  panel='<div class="panel"><h3>실험 — 50칸 동안의 메모 한 줄</h3>'+cv('c1','가로축은 칸 번호 1부터 50, 세로축은 메모 값. 첫 칸에 10을 적은 뒤 문 설정에 따라 메모가 유지되거나 흐려지거나 잡음에 덮인다')+'<div class="ctrl">'+rg('r1F','지우개 (남기는 비율)',0.5,1,1,0.01)+rg('r1I','펜 (적는 세기)',0,1,0,0.05)+'</div><div class="kpis" id="k1"></div><div class="insight" id="ins1" aria-live="polite"></div><h3>행동으로 보기 — 칸마다 달라지는 문</h3>'+cv('c1b','50칸의 문 상태를 칸마다 색으로 표시. 첫 칸만 펜이 열리고 나머지는 닫히는 “그때그때” 방식과 늘 같은 방식을 견준다','wide')+note('위 줄은 슬라이더로 정한 “늘 같은 문”, 아래 줄은 “첫 칸만 펜을 열고 나머지는 닫는 문”이다. 밝을수록 열려 있다.')+'</div>',
  report='보고드려요. 지우개 1, 펜 0이면 50칸 뒤에도 10이 그대로예요. 지우개를 0.9로 내리면 0.06이 남고, 펜을 0.5로 열면 잡음이 메모를 덮었어요.',
  stepsh='문이 하는 일',steps=['지우개를 1로 두면 메모가 다음 칸으로 그대로 넘어간다. 곱해지는 수가 1이다.','펜을 0으로 두면 잡음이 메모에 들어오지 못한다.','슬라이더는 모든 칸에 같은 문을 쓴다. 그러면 첫 칸의 값도 적을 수 없다(펜 0). 그래서 문은 칸마다 달라야 한다.','LSTM은 “이 칸에서 문을 얼마나 열지”를 입력을 보고 정하는 규칙을 기록에서 배운다.'],
  lim='문을 여닫는 규칙을 사람이 정해 줄 수는 없다. 기록에서 정말 배울 수 있을까? 다음 칸에서 작은 메모장을 직접 학습시켜 본다.',
  concepts=['method/lstm','concept/cell-state','concept/forget-gate','concept/input-gate','concept/constant-error-path']),
 dict(id='lv2',no='②',title='신호 기억 시험 — 배운 문 들여다보기',nav='신호 기억 시험',tc='m',tag1='방법: 작은 LSTM을 이 페이지에서 학습시키기',tag2='일상: 귓속말을 끝까지 붙들기',
  why=('30칸짜리 줄이 있다. 첫 칸에 “+1” 또는 “−1” 신호가 오고, 나머지 29칸은 잡음이다. 끝에서 첫 칸이 무엇이었는지 맞혀야 한다.','문이 없는 메모 한 칸은 잡음과 신호를 같은 비율로 섞는다. 30칸 뒤에는 신호가 잡음에 묻힌다. 5칸 창은 첫 칸을 아예 보지 못한다.','문 달린 메모장을 연습 문제 300개로 학습시킨다. 문 여닫는 규칙은 알려 주지 않는다. 끝에서 틀린 만큼만 되돌려 보낸다.','“첫마디만 기억해”라고 시키지 않는다. 문제를 풀게 하고 채점만 해 준다. 그러면 스스로 첫마디를 붙드는 법을 익힌다.'),
  math=dict(ask='정답률은 어떻게 세요? 그리고 찍어도 절반은 맞잖아요.',school='비율과 확률이다. 맞힌 개수를 전체 개수로 나눈다. 둘 중 하나를 고르는 문제는 찍어도 50%쯤 맞는다.',
   eq='정답률 = 맞힌 문제 수 ÷ 전체 문제 수 × 100',pieces=[('전체 문제 수','처음 보는 시험 문제 200개'),('50%','아무것도 기억 못 하고 찍었을 때의 기준선'),('100%','첫 칸의 신호를 끝까지 붙든 것')],
   num='시험 문제 200개 가운데 104개를 맞히면 104 ÷ 200 × 100 = 52%다. 찍은 것과 다를 바 없다. 199개를 맞히면 99.5%다.',comment='52%면 기억을 못 한 거고, 100% 가까이 나와야 진짜 기억한 거군요.'),
  pair=('서른 명이 떠드는 방에서 맨 처음 들은 한마디를 끝까지 기억해야 한다. 들은 말을 전부 조금씩 섞어 기억하는 사람은 끝에 가면 헷갈린다. 첫마디를 수첩에 적고 뚜껑을 닫은 사람은 틀리지 않는다.','학습을 마친 LSTM이 칸마다 내놓는 답을 그려 본다. 첫 칸의 신호가 “+1”이었던 줄과 “−1”이었던 줄이 끝까지 섞이지 않고 마지막 칸에서 위아래로 갈라져 있으면, 신호를 붙들고 있다는 뜻이다.'),
  talk=[('doc','think','문 여닫는 법을 알려 주지 않고 채점만 해 줘도 첫마디를 붙들 수 있을까요?'),('fly','arms','채점만으로? 못 믿겠는데. 문 없는 메모와 나란히 놓고 봐야겠어.'),('robo','happy','“메모장 학습시키기”를 눌러! 2초면 끝나.')],
  panel='<div class="panel"><h3>실험 — 문 달린 메모장을 학습시키기</h3><div class="ctrl"><div class="group"><button class="bt primary" type="button" id="b2T">메모장 학습시키기 (2초쯤 걸려요)</button></div></div><div class="kpis" id="k2"></div>'+cv('c2','가로축은 칸 번호 1부터 30, 세로축은 메모장이 그 칸에서 내놓는 답. 첫 칸 신호가 +1인 줄과 −1인 줄이 갈라져 끝까지 떨어져 있다')+'<div class="insight" id="ins2" aria-live="polite"></div><h3>행동으로 보기 — 시험 200문제의 마지막 값</h3>'+cv('c2b','시험 200문제의 마지막 값을 점으로 찍은 두 줄. 윗줄(문 달린 메모장)은 초록과 빨강이 양쪽으로 갈라지고, 아랫줄(문 없는 메모)은 뒤섞여 있다','wide')+note('점 하나가 시험 문제 하나의 마지막 값이다. 초록은 “첫 칸 +1”, 빨강은 “첫 칸 −1”이었던 문제다. 두 색이 좌우로 갈라져 있어야 맞힐 수 있다.')+'</div>',
  report='보고드려요. 학습을 마친 메모장은 시험 200문제를 거의 다 맞혔어요. 문 없는 메모 한 칸과 5칸 창은 절반 근처, 찍은 것과 비슷했어요.',
  stepsh='무엇을 배웠나',steps=['처음에는 문이 아무렇게나 열려 있어 찍는 수준이다.','틀릴 때마다 되돌아오는 신호로 숫자 101개를 조금씩 고친다. 메모가 다음 칸으로 넘어가는 길이 따로 있어 30칸 전까지 신호가 닿는다.','학습이 끝나면 두 종류의 줄이 끝까지 섞이지 않는다. 중간 칸의 답은 오르내리지만 마지막 칸에서는 정확히 갈라진다. 메모장은 신호를 사람이 읽기 쉬운 모양이 아니라 자기 나름의 모양으로 품는다.','문 여닫는 법을 알려 준 적이 없다. 채점만으로 익혔다. 그래서 익힌 방식이 “펜을 닫고 지우개를 1로” 같은 교과서 모양은 아니다. 지우개 평균은 1보다 낮고 중간 답은 오르내린다. 그래도 끝에서는 맞힌다.'],
  lim='메모장의 칸 수는 정해져 있다. 여기서는 4칸이었다. 신호 하나는 붙들 수 있어도, 긴 글 전체를 몇 칸에 담을 수는 없다. 그리고 학습에 연습 문제 300개가 필요했다. 1-6에서 1부를 정리하고, 2부에서는 메모 대신 “창 안을 통째로 다시 보는” 대화형 AI의 방식으로 넘어간다.',
  intern=SIA,concepts=['task/cue-recall','method/lstm','concept/forget-gate'])],
 duel=dict(title='메모 한 칸 vs 문 달린 메모장 — 신호 기억 시험',metric='정답률',tag='일상: 감 하나 vs 수첩',q='30칸 전의 신호를 맞히는 시험 200문제. 문 없는 메모 한 칸과 문 달린 메모장(LSTM), 누가 더 많이 맞힐까?',
  fly=('메모 한 칸 (남기는 비율 0.95) — 정할 숫자 2개','0.95면 30칸 뒤에도 첫 칸이 21%는 남아. 그거면 돼.'),robo=('문 달린 메모장 (메모 4칸) — 정할 숫자 101개','문이 있어야 잡음을 막지. 101개의 힘을 보라고!'),rule='정답률(높을수록 좋음). 막대가 긴 쪽이 이긴다. 찍으면 50%쯤 나온다.'),
 sumh='정리 — 세 가지 기억의 시험 성적',
 sum='<div class="tw"><table class="tb" id="sumTb"><tr><th>기억 방식</th><th>정할 숫자</th><th>신호 기억 시험 정답률</th><th>한 줄 평</th></tr></table></div><p style="font-size:14px;color:var(--muted)">대결을 열거나 “메모장 학습시키기”를 누르면 표가 채워진다. 숫자는 브라우저가 직접 학습하고 채점한 값이다.</p>'+steps3([('문이 기억을 고른다','지우개와 펜을 따로 움직여, 중요한 것은 붙들고 잡음은 막는다.'),('곱해지는 수를 1로','지우개를 열어 두면 메모도 학습 신호도 줄지 않고 지나간다. 1-4의 문제에 대한 답이다.'),('규칙은 배운다','문 여닫는 법은 사람이 정하지 않는다. 채점만으로 익힌다.')])+field('긴 이력에서 “무엇을 남기고 무엇을 흘릴지”를 정하는 규칙이 기억 설계의 핵심이다. 모든 것을 같은 비율로 줄이는 요약은 결정적인 한마디를 놓친다.','이 시험은 신호가 늘 첫 칸에 오는 아주 단순한 과제다. 실제 기록에서는 무엇이 중요한지부터 알아내야 한다.'),
 outro=[('doc','front','오늘의 한 줄이에요. 좋은 기억은 많이 담는 기억이 아니라, 남길 것을 고르는 기억이에요.'),('asst','smile','문 여닫는 법을 안 알려 줬는데 채점만으로 익힌 게 신기했어요.'),('fly','coffee','졌어. 문 없는 메모로는 잡음을 못 막더군. 그래도 숫자 101개는 과해. 단순한 기록에서도 그만한 값을 할까?'),('robo','happy','문 달린 메모장의 승리! 다음 편에서 매출 기록으로 한 번 더 붙자고!'),('moa','report','오늘 시험지는 제가 모아 뒀어요. 1부 마지막 편에서 성적표로 정리해 드릴게요.')],
 examples=['신호 기억 시험: 30칸짜리 줄. 첫 칸은 +1 또는 −1, 나머지 29칸은 평균 0·표준편차 0.5인 잡음. 연습 문제 300개(시드 11), 시험 문제 200개(시드 12)','문 달린 메모장: 메모 4칸짜리 LSTM, 정할 숫자 101개. 이 페이지에서 30번 되풀이해 학습한다 (시드 고정이라 누를 때마다 같은 결과)','문 없는 메모 한 칸: 남기는 비율 0.95로 줄을 읽은 뒤 끝 값의 부호로 답한다. 5칸 창: 마지막 5칸만 본다','칸 ①의 50칸 실험은 첫 칸에 10을 적고 이후 잡음(표준편차 3)을 넣은 설명용 도식이다','“30칸 뒤 21%”는 0.95를 29번 곱한 값(0.226)을 어림한 것이다'],
 refs=['hochreiter1997long','gers2000learning','bengio1994learning','ahn2026ts3_2_2'],
 claims=[('claim/lstm-1997','LSTM은 오차 신호가 줄지 않고 지나가는 길을 두어 먼 칸의 의존을 배우도록 제안되었다','#lv1','hochreiter1997long','논문 전체','method/lstm'),
  ('claim/forget-gate-2000','잊기 문(지우개)은 2000년에 LSTM에 더해졌다','#lv1','gers2000learning','논문 전체','concept/forget-gate')],
 openq=[('question/mem-beyond-cells','칸 수가 정해진 메모에 담기지 않는 긴 글은 어떻게 기억할까?','#lv2','2부에서 문맥 창과 바깥 저장소로 다룬다')],
 nodes=[('method/lstm','Method','LSTM (지우개 달린 메모장)','long short-term memory','#lv1','문으로 메모를 지우고·적고·내보내는 순환 신경망.'),
  ('concept/cell-state','Concept','메모 (셀 상태)','cell state','#lv1','LSTM이 칸마다 들고 다니는 메모. 지우개와 펜으로 고쳐 쓴다.'),
  ('concept/forget-gate','Concept','지우개 문 (잊기 문)','forget gate','#lv1','옛 메모를 얼마나 남길지 정하는 0~1 사이 값.'),
  ('concept/input-gate','Concept','펜 문 (입력 문)','input gate','#lv1','새 내용을 얼마나 적을지 정하는 0~1 사이 값.'),
  ('concept/constant-error-path','Concept','줄지 않는 길','constant error path','#lv1','지우개가 1에 가까울 때 메모와 학습 신호가 줄지 않고 지나가는 경로.'),
  ('task/cue-recall','Task','신호 기억 시험','cue recall task','#lv2','첫 칸의 신호를 잡음 수십 칸 뒤에 맞히는 과제.'),
  ('limitation/fixed-cells','Limitation','메모 칸 수는 정해져 있다','fixed memory size','#lv2','정해진 칸 수의 메모에 긴 입력 전체를 담을 수는 없다.'),
  ('sim/1-5-gates','Simulation','50칸 동안의 메모 한 줄','hand-set gates over 50 steps','#lv1'),('sim/1-5-train','Simulation','문 달린 메모장 학습시키기','training a tiny LSTM','#lv2'),('sim/1-5-duel','Simulation','대결: 메모 한 칸 vs LSTM','duel: plain memo vs LSTM','#vs')],
 edges=[('concept/cell-state','partOf','method/lstm','#lv1'),('concept/forget-gate','partOf','method/lstm','#lv1'),('concept/input-gate','partOf','method/lstm','#lv1'),('concept/forget-gate','prerequisiteOf','concept/constant-error-path','#lv1'),
  ('method/lstm','solves','task/cue-recall','#lv2'),('method/lstm','hasLimitation','limitation/fixed-cells','#lv2'),('limitation/fixed-cells','raises','question/mem-beyond-cells','#lv2'),
  ('concept/forget-gate','demonstratedBy','sim/1-5-gates','#lv1'),('task/cue-recall','demonstratedBy','sim/1-5-train','#lv2'),('method/lstm','demonstratedBy','sim/1-5-duel','#vs')],
 gloss={'메모':['메모 (셀 상태)','이 시리즈의 별명','지난 일을 줄여 담은 숫자 칸.'],'지우개':['지우개 (잊기 문)','LSTM','옛 메모를 얼마나 남길지 정하는 0~1 사이 값. 1이면 안 지운다.'],'펜':['펜 (입력 문)','LSTM','새 내용을 얼마나 적을지 정하는 0~1 사이 값. 0이면 안 적는다.'],
  'LSTM':['LSTM','신경망','지우개와 펜이 달린 메모장을 가진 순환 신경망. 1997년 제안, 지우개는 2000년에 더해졌다.'],'잡음':['잡음','데이터','뜻 없이 출렁이는 값. 기억할 필요가 없는 부분.'],'학습 신호':['학습 신호 (기울기)','학습','끝에서 틀린 만큼을 앞쪽으로 되돌려 보내는 값.'],
  '정답률':['정답률','지표','맞힌 문제 수를 전체 문제 수로 나눈 비율.'],'남기는 비율':['남기는 비율','설정값','메모를 고쳐 쓸 때 옛 메모를 얼마나 남기는지.'],'창':['창 (window)','설정값','펼쳐 놓는 과거 구간.']},
 core=['지우개','펜','LSTM','메모','정답률'],
 quiz={'why':[Q('1-4의 메모가 가진 두 문제는?',['너무 비싸고 느리다','모든 것을 같은 비율로 잊고, 먼 칸의 학습 신호가 사라진다','창이 너무 길다'],1,'문은 이 두 문제를 함께 겨눠요.','흐려짐과 사라지는 신호를 떠올려 보세요.','method/lstm')],
  'lv1':[Q('옛 메모 20, 지우개 0.5, 펜 1, 새 내용 6이면 새 메모는?',['13','16','26'],1,'0.5 × 20 + 1 × 6 = 10 + 6 = 16이에요.','지우개는 옛 메모에, 펜은 새 내용에 곱해요.','concept/cell-state','계산'),
        Q('지우개를 1 가까이 열어 두면 먼 칸의 학습 신호는?',['금방 사라진다','거의 줄지 않고 지나간다','끝없이 커진다'],1,'칸마다 곱해지는 수가 1에 가까워서예요.','1을 여러 번 곱하면 얼마일까요?','concept/constant-error-path')],
  'lv2':[Q('시험 200문제 가운데 150개를 맞히면 정답률은?',['50%','75%','150%'],1,'150 ÷ 200 × 100 = 75%예요.','맞힌 수를 전체 수로 나눠요.','task/cue-recall','계산'),
        Q('문 없는 메모 한 칸이 이 시험에서 찍는 수준에 머문 까닭은?',['계산이 느려서','신호와 잡음을 같은 비율로 섞어 30칸 뒤에는 신호가 묻혀서','연습 문제가 없어서'],1,'잡음을 막을 문이 없어요.','잡음 29칸이 메모에 어떻게 들어오는지 떠올려 보세요.','concept/input-gate')],
  'vs':[Q('이 대결의 교훈은?',['숫자가 많으면 언제나 이긴다','잡음 속에서 하나를 붙들어야 할 때는 여닫는 문이 값을 한다','메모는 쓸모없다'],1,'과제가 “고르는 기억”을 요구했어요. 단순한 기록에서는 결과가 다를 수 있어요.','과제의 성격을 떠올려 보세요.','method/lstm')]},
)
JS=r'''
/* 칸 ① : 손으로 정한 문 */
var Ff=1,Ii=0,cv=$('#c1'),cvb=$('#c1b'),NZ=(function(){var r=rng(21),a=[];for(var i=0;i<50;i++)a.push(3*gauss(r));return a;})();
function runMemo(f,i,smart){var c=10,out=[10];for(var t=1;t<50;t++){c=(smart?1:f)*c+(smart?0:i)*NZ[t];out.push(c);}return out;}
function upd1(){var m=runMemo(Ff,Ii,false),keep=Math.pow(Ff,49);
  kpis($('#k1'),[[f2(Ff,2),'지우개 (한 칸에 곱해지는 수)','a'],[f2(Ii,2),'펜 (잡음이 들어오는 세기)','m'],[f2(10*keep,2),'50칸 뒤 남은 처음 값 (10에서)',keep>0.9?'g':'r'],[f2(m[49],2),'50칸 뒤 실제 메모',Math.abs(m[49]-10)<0.5?'g':'r']]);
  $('#ins1').innerHTML=(Ff>=0.999&&Ii<=0.001)?'<p class="g">지우개 1, 펜 0이에요. 50칸 내내 메모는 10이에요. 다만 이 설정으로는 새 내용을 영영 적을 수 없어요. 그래서 문은 칸마다 달라야 해요.</p>':
    (Ii>0.001?tpl('<p class="m">펜이 {0}만큼 열려 있어 칸마다 잡음이 메모에 섞여요. 50칸 뒤 메모는 {1}로, 처음의 10과 달라졌어요.</p>',f2(Ii,2),f2(m[49],2)):'')+
    (Ff<0.999?tpl('<p class="r">지우개가 {0}이라 칸마다 메모가 {0}배가 돼요. 50칸 뒤 처음 값은 {1}만 남아요.</p>',f2(Ff,2),f2(10*keep,2)):'');drawAll();}
bindRange('r1F',function(v){Ff=v;upd1();},function(v){return f2(v,2);});bindRange('r1I',function(v){Ii=v;upd1();},function(v){return f2(v,2);});
addMod(cv,function(){var H=270,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var m=runMemo(Ff,Ii,false),s=runMemo(1,0,true),rgv=rangeOf([m,[0,12]]);
  var o=plot(ctx,W,H,{x0:1,x1:50,y0:Math.min(rgv[0],-2),y1:Math.max(rgv[1],12),yn:4,xticks:[1,10,20,30,40,50],xlab:function(v){return v+'칸';},lines:[{d:s,x0:1,color:COL.gfp,w:1.6,dash:[5,4]},{d:m,x0:1,color:COL.amber,w:2.2}],legend:[['늘 같은 문 (슬라이더)',COL.amber],['첫 칸만 적고 닫는 문',COL.gfp]]});stamp(ctx,W,'설명용 도식');});
addMod(cvb,function(){var H=120,W=fit(cvb,H),ctx=cvb.getContext('2d');ctx.clearRect(0,0,W,H);var gw=(W-110)/50;
  [['늘 같은 문',function(t){return Ii;},26],['그때그때 문',function(t){return t===0?1:0;},70]].forEach(function(z){txt(ctx,z[0],6,z[2]+12,{size:11,color:COL.muted});
    for(var t=0;t<50;t++){var v=z[1](t);rr(ctx,100+t*gw+1,z[2],gw-2,24,3,'rgba(255,134,184,'+(0.08+0.85*v)+')','rgba(255,134,184,.5)');}});
  txt(ctx,'펜이 열린 정도 (밝을수록 열림) · 왼쪽이 첫 칸',100,110,{size:10,color:COL.muted});stamp(ctx,W,'설명용 도식');});
/* 칸 ② : 학습 */
var RES=null,cv2=$('#c2'),cv2b=$('#c2b'),TT=30;
function trainAll(){if(RES)return RES;var tr=cueData(11,300,TT),te=cueData(12,200,TT),net=LSTM(4,3);lstmTrain(net,tr.X,tr.Y,{epochs:30,lr:0.03,batch:16,seed:5});
  var ok=0;te.X.forEach(function(s,i){if(lstmForward(net,s)*te.Y[i]>0)ok++;});
  var F=tr.X.map(function(s){return [memoEnd(s,0.95)];}),b=linfit(F,tr.Y),km=0;te.X.forEach(function(s,i){if(linpred(b,[memoEnd(s,0.95)])*te.Y[i]>0)km++;});
  var Fw=tr.X.map(function(s){return s.slice(-5);}),bw=linfit(Fw,tr.Y),kw=0;te.X.forEach(function(s,i){if(linpred(bw,s.slice(-5))*te.Y[i]>0)kw++;});
  var ip=te.Y.indexOf(1),im=te.Y.indexOf(-1);
  function trace(s){var f=lstmForward(net,s,true),o=[],fg=0;f.tr.forEach(function(z){var y=net.by[0];for(var j=0;j<4;j++){y+=net.Wy[j]*z.h[j];fg+=z.f[j];}o.push(y);});return {y:o,f:fg/(4*f.tr.length)};}
  function mtrace(s){var h=0,o=[];s.forEach(function(v){h=0.95*h+0.05*v;o.push(h);});return o;}
  var tp=trace(te.X[ip]),tm=trace(te.X[im]);
  var eL=te.X.map(function(s,i){return [lstmForward(net,s),te.Y[i]];}),eM=te.X.map(function(s,i){return [memoEnd(s,0.95),te.Y[i]];});
  RES={eL:eL,eM:eM,lstm:ok/2,memo:km/2,win:kw/2,tp:tp.y,tm:tm.y,fg:(tp.f+tm.f)/2};PAGE._T={lstm:RES.lstm,memo:RES.memo,win:RES.win};fillSum();return RES;}
function show2(){var r=RES;if(!r){kpis($('#k2'),[['–','문 달린 메모장 정답률','g'],['–','문 없는 메모 한 칸','a'],['–','5칸 창','m'],['50%','찍었을 때','r']]);$('#ins2').innerHTML='<p>아직 학습 전이에요. 위 단추를 누르면 이 페이지 안에서 작은 메모장을 학습시켜요.</p>';return;}
  kpis($('#k2'),[[f2(r.lstm,1)+'%','문 달린 메모장 정답률','g'],[f2(r.memo,1)+'%','문 없는 메모 한 칸','a'],[f2(r.win,1)+'%','5칸 창','m'],['50%','찍었을 때','r']]);
  $('#ins2').innerHTML=tpl('<p class="g">학습을 마쳤어요. 초록 선과 빨강 선이 서로 거울처럼 반대로 움직여요. 중간에 오르내려도 둘이 뭉개지지 않고, 마지막 칸에서 초록은 위, 빨강은 아래로 갈라져요. 두 줄을 읽는 동안 지우개 문의 평균값은 {0}이었어요. 칸 ①에서 손으로 해 본 것처럼 늘 1로 열어 둔 것이 아니에요. 학습이 찾아낸 방식은 사람이 짐작한 깔끔한 방식과 달라요.</p><p>아래 점 그림에서 문 없는 메모는 초록과 빨강이 뒤섞여 있어요. 끝 값으로는 구분할 수 없으니 정답률이 {1}%에 머물러요.</p>',f2(r.fg,2),f2(r.memo,1));drawAll();}
$('#b2T').addEventListener('click',function(){var b=this;b.disabled=true;b.textContent='학습 중…';setTimeout(function(){trainAll();show2();b.textContent='학습 완료';},30);});
addMod(cv2,function(){var H=250,W=fit(cv2,H),ctx=cv2.getContext('2d');ctx.clearRect(0,0,W,H);
  if(!RES){txt(ctx,'“메모장 학습시키기”를 누르면 그림이 나와요',W/2,H/2,{size:13,color:COL.muted,align:'center'});return;}
  var rgv=rangeOf([RES.tp,RES.tm]),o=plot(ctx,W,H,{x0:1,x1:30,y0:Math.min(rgv[0],-1.4),y1:Math.max(rgv[1],1.4),yn:4,yfmt:function(v){return v.toFixed(1);},xticks:[1,5,10,15,20,25,30],xlab:function(v){return v+'칸';},lines:[{d:RES.tp,x0:1,color:COL.gfp,w:2.2},{d:RES.tm,x0:1,color:COL.eye,w:2.2}],legend:[['첫 칸이 +1인 줄',COL.gfp],['첫 칸이 −1인 줄',COL.eye]]});
  ctx.strokeStyle='rgba(157,155,184,.4)';ctx.beginPath();ctx.moveTo(o.P.l,o.Y(0));ctx.lineTo(W-o.P.r,o.Y(0));ctx.stroke();stamp(ctx,W,'이 페이지에서 학습한 작은 모형');});
addMod(cv2b,function(){var H=170,W=fit(cv2b,H),ctx=cv2b.getContext('2d');ctx.clearRect(0,0,W,H);
  if(!RES){txt(ctx,'학습 뒤에 함께 보여 드려요',W/2,H/2,{size:13,color:COL.muted,align:'center'});return;}
  var r=rng(3);[['문 달린 메모장',RES.eL,1.6,46],['문 없는 메모 한 칸',RES.eM,0.12,118]].forEach(function(z){var x0=150,x1=W-16,cx=(x0+x1)/2;
    txt(ctx,z[0],8,z[3],{size:12,color:COL.muted,w:'700'});ctx.strokeStyle='rgba(157,155,184,.35)';ctx.beginPath();ctx.moveTo(x0,z[3]);ctx.lineTo(x1,z[3]);ctx.moveTo(cx,z[3]-26);ctx.lineTo(cx,z[3]+26);ctx.stroke();
    z[1].forEach(function(e){var x=cx+clamp(e[0]/z[2],-1,1)*(x1-x0)/2;ctx.fillStyle=e[1]>0?'rgba(94,227,156,.6)':'rgba(240,96,77,.6)';ctx.beginPath();ctx.arc(x,z[3]+(r()-0.5)*40,2.6,0,7);ctx.fill();});});
  txt(ctx,'← 음수 쪽 · 가운데 세로선이 0 · 양수 쪽 →',(150+W-16)/2,160,{size:10,color:COL.muted,align:'center'});stamp(ctx,W,'이 페이지에서 학습한 작은 모형');});
/* 대결 */
Duel({el:'#duel',higherIsBetter:true,drawMargin:0.05,fmt:function(v){return f2(v,1)+'%';},run:function(){var r=trainAll();show2();var b=$('#b2T');b.disabled=true;b.textContent='학습 완료';return {fly:r.memo,robo:r.lstm,metric:'정답률'};},
  say:function(f,b){return tpl('정답률은 초파리 쪽 메모 한 칸이 {0}%, 주판봇 쪽 문 달린 메모장이 {1}%예요. 찍으면 50%쯤이에요.',f2(f,1),f2(b,1));},
  lessons:{R:'잡음 속에서 하나를 붙들려면 여닫는 문이 있어야 한다. 같은 비율로 흐려지는 메모는 찍는 수준이었다',D:'문이 있어도 없어도 비슷했다',F:'문 없는 메모가 버텼다'},
  after:function(){$('#duelNote').innerHTML=tpl('<p>마지막 5칸만 보는 창은 {0}%였어요. 첫 칸이 창 밖이라 볼 수 없어요. 1-1의 “창 밖은 없는 것”이에요.</p>',f2(RES.win,1));}});
function fillSum(){var r=RES;function row(n,k,a,c){return '<tr><td>'+n+'</td><td class="num">'+k+'</td><td class="num">'+a+'</td><td>'+c+'</td></tr>';}
  $$('#sumTb tr').slice(1).forEach(function(e){e.remove();});
  $('#sumTb').insertAdjacentHTML('beforeend',row('5칸 창','6개',f2(r.win,1)+'%','첫 칸이 창 밖이다')+row('문 없는 메모 한 칸','2개',f2(r.memo,1)+'%','신호가 잡음에 묻힌다')+row('문 달린 메모장 (LSTM)','101개',f2(r.lstm,1)+'%','첫 칸의 신호를 끝까지 구분한다'));}
upd1();show2();
'''
