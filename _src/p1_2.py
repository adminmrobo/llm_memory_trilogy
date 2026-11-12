# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *


P=dict(
 title='메아리는 언제 꺼지나 — 과거가 오늘에 남기는 흔적 재기',chip='매출 기록 앵커',
 q='어제의 일은 며칠 뒤까지 오늘에 남아 있을까?',
 lead='<p>1-1에서 창을 늘리면 값을 치른다는 것을 봤다. 그러면 먼저 물어야 한다. 먼 과거는 얼마나 쓸모가 있을까? 이 페이지에서는 과거가 오늘에 남기는 흔적을 <b>메아리</b>라 부르고, 그 크기를 날 수별로 잰다. 통계에서는 이것을 자기상관이라 한다.</p>',
 objs=['며칠 전 값과 오늘 값이 함께 움직이는 정도(자기상관)를 그림에서 읽는다','되풀이되는 흐름과 빨리 꺼지는 메아리를 구분한다','메아리가 절반으로 줄어드는 날 수(반감기)를 계산한다'],mins=20,
 kpis=[('0.72','7일 전 값과 오늘 값의 상관'),('0.48','요일 흐름을 뺀 뒤 어제와의 상관'),('1일','그 메아리가 절반이 되는 날 수'),('2.51','요일 평균 + 어제 하나의 검증 오차 (만 원)')],
 hero=['오늘은 과거의 메아리를 재요. 며칠 전 일이 오늘까지 얼마나 울리는지 숫자로 볼 거예요.','훈련 200일로 1일 전부터 35일 전까지 다 재 놨어요.','먼 과거의 메아리는 금방 꺼질 거야. 정말 한 달 전이 들릴까?','7일 전, 14일 전, 28일 전… 전부 크게 울리는데? 메아리는 영원해!'],
 first3=['과거의 값이 오늘 값과 얼마나 함께 움직이는지 날 수별로 잰다. 이 흔적을 메아리라 부른다.','메아리가 빨리 꺼지는 기록이라면 긴 기억은 필요 없다. 기억 장치를 고르기 전에 메아리부터 재야 한다.','“지난주 같은 요일”처럼 되풀이되는 흐름과, 어제 일의 여운을 따로 봐야 예측 도구를 제대로 고를 수 있다.'],
 abbr=['AR','ACF','MAE'],cast=dict(fly='메아리는 금방 꺼진다',robo='메아리는 오래 간다'),
 whyh='왜 메아리를 재야 할까',whytag='방법: 며칠 전 값과 오늘 값 견주기',prev='1-1 창 밖은 없는 것',
 why=[('성적표는 이유를 말하지 않는다','1-1의 성적표는 28일 창이 좋다고만 알려 줬다. 왜 28일인지는 말해 주지 않았다.'),('기억의 값어치','먼 과거가 오늘과 상관이 없다면 기억할 까닭이 없다. 상관이 남아 있는 곳까지만 기억하면 된다.'),('두 가지 메아리','되풀이되는 흐름이 만드는 메아리와, 어제 일의 여운이 만드는 메아리는 성질이 다르다. 이 페이지에서 둘을 가른다.')],
 levels=[dict(id='lv1',no='①',title='메아리 재기 — 며칠 전과 오늘은 함께 움직이나',nav='메아리 재기',tag1='방법: 날 수별 상관 재기 (자기상관)',tag2='일상: 동굴에서 메아리 듣기',
  why=('1-1에서 창 길이를 검증 오차로 골랐다. 그런데 창 안의 어느 날이 실제로 도움이 되는지는 알 수 없었다.','창 길이별 성적표는 답만 주고 이유를 주지 않는다. 길이마다 모델을 다시 맞춰야 해서 품도 든다.','k일 전 값과 오늘 값을 짝지어, 둘이 얼마나 함께 오르내리는지 숫자 하나로 잰다. k를 1부터 늘려 가며 막대로 늘어놓는다.','동굴에서 소리치고 메아리가 몇 번, 얼마나 크게 돌아오는지 세는 일이다.'),
  math=dict(ask='상관이 0.72라는 게 무슨 뜻이에요? 72% 맞힌다는 건가요?',school='두 값을 짝지어 점으로 찍는 산점도와 상관관계다. 점들이 오른쪽 위로 곧게 늘어설수록 +1에, 오른쪽 아래로 늘어설수록 −1에 가깝다.',
   eq='메아리 크기(k) = k일 전 값과 오늘 값의 상관 &nbsp;(−1 ~ +1)',pieces=[('+1','한쪽이 오르면 다른 쪽도 꼭 같이 오른다'),('0','서로 아무 상관이 없다'),('−1','한쪽이 오르면 다른 쪽은 꼭 내린다'),('k','거슬러 가는 날 수')],
   num='(1, 2, 3)과 (2, 4, 6)은 함께 오르니 상관이 +1이다. (1, 2, 3)과 (6, 4, 2)는 거꾸로 가니 −1이다. 0.72는 “맞히는 비율”이 아니라 “꽤 뚜렷하게 같이 움직인다”는 뜻이다.',comment='퍼센트가 아니라 같이 움직이는 정도군요. 0이면 기억해 봐야 소용없고요.'),
  pair=('동굴에서 “야호” 하고 외친다. 1초 뒤, 2초 뒤에 돌아오는 소리의 크기를 차례로 적는다. 어떤 동굴은 금방 조용해지고, 어떤 동굴은 일정한 간격으로 다시 울린다.','k일 전 값과 오늘 값의 상관을 k = 1, 2, 3 …에 대해 잰다. 이 막대들을 늘어놓은 그림이 자기상관 그림이다. 막대가 0에 가까운 날은 오늘을 짐작하는 데 거의 도움이 안 된다.'),
  talk=[('doc','front','매출 기록에서 메아리를 35일 전까지 재 봤어요. 어디가 가장 크게 울릴까요?'),('robo','chart','당연히 어제지! 가까울수록 크게 울리는 법이야.'),('fly','arms','정말? 슬라이더를 7에 놓고, 그다음 3에 놓아 봐.')],
  panel='<div class="panel"><h3>실험 — 날 수별 메아리</h3>'+cv('c1','가로축은 거슬러 간 날 수 1일부터 35일, 세로축은 상관. 7일마다 높은 막대가 서고 3~4일 전은 음수다')+'<div class="ctrl">'+rg('r1K','며칠 전',1,35,7)+'</div><div class="kpis" id="k1"></div><div class="insight" id="ins1" aria-live="polite"></div><h3>행동으로 보기 — 짝지어 찍은 점</h3>'+cv('c1b','가로축은 며칠 전 매출, 세로축은 오늘 매출인 산점도. 상관이 크면 점이 비스듬한 띠를 이룬다')+'<p style="font-size:14px;color:var(--muted);margin-bottom:0">점 하나가 하루다. 가로는 고른 날 수만큼 전의 매출, 세로는 그날 매출이다.</p></div>',
  report='보고드려요. 어제와의 상관은 0.47인데 7일 전은 0.72였어요. 3일 전은 −0.49로 거꾸로 움직였고요. 28일 전도 0.62나 남아 있어요.',
  stepsh='막대 읽는 법',steps=['막대가 높은 날은 그날 값을 알면 오늘을 짐작하기 쉽다.','7일, 14일, 21일, 28일에 막대가 높다. 같은 요일끼리 닮았기 때문이다.','3~4일 전은 음수다. 주중과 주말이 엇갈리는 간격이라 거꾸로 움직인다.','1-1에서 7일 창부터 오차가 뚝 떨어진 까닭이 여기에 있다. 7일 전 막대가 가장 높다.'],
  lim='28일 전에도 0.62가 남았다. 그러면 이 기록은 한 달 전 일을 기억하고 있는 걸까? 아니다. 요일이 되풀이될 뿐이다. 다음 칸에서 되풀이를 걷어 내고 다시 잰다.',
  concepts=['concept/autocorrelation','concept/echo','concept/lag','concept/seasonality'],
  code=[('plot_acf(train, lags=35)','1일 전부터 35일 전까지의 상관을 막대로 그린다')],codenote='파이썬 통계 도구 statsmodels의 자기상관 그림 쓰임새를 보인 예다. 이 페이지의 막대는 같은 계산을 브라우저 안에서 직접 했다.'),
 dict(id='lv2',no='②',title='요일 흐름을 빼면 — 빨리 꺼지는 메아리',nav='빨리 꺼지는 메아리',tc='m',tag1='방법: 되풀이를 빼고 남은 것의 메아리 재기',tag2='일상: 종을 한 번 치고 귀 기울이기',
  why=('28일 전까지 메아리가 크게 남아 있었다. 정말 한 달 전 일이 오늘을 움직이는지 알고 싶다.','앞의 막대에는 “요일이 되풀이된다”는 사실과 “어제 일의 여운”이 섞여 있다. 섞인 채로는 기억이 얼마나 길어야 하는지 알 수 없다.','요일별 평균을 먼저 빼고, 남은 출렁임만 가지고 메아리를 다시 잰다. 그 메아리가 하루마다 몇 배로 줄어드는지 본다.','달력에 적힌 정기 행사는 달력이 기억한다. 머리로 기억해야 하는 것은 달력에 없는 일뿐이다.'),
  math=dict(ask='하루마다 절반씩 준다는 걸 식으로는 어떻게 써요?',school='같은 수를 거듭 곱하는 등비수열이다. 1, ½, ¼, ⅛ … 처럼 줄어든다.',
   eq='k일 뒤 남는 크기 = 처음 크기 × φ × φ × … (k번) = 처음 크기 × φ<sup>k</sup>',pieces=[('φ (파이)','하루가 지날 때 남는 비율. 0과 1 사이'),('k','지난 날 수'),('반감기','남는 크기가 절반이 되는 날 수')],
   num='어제 매출이 평소보다 10만 원 많았다. 남는 비율이 0.5라면 오늘은 5만 원, 내일은 2.5만 원, 모레는 1.25만 원이 남는다. 사흘 만에 8분의 1이다. 남는 비율이 0.9라면 0.9를 일곱 번 곱해야 0.48, 곧 절반이 된다.',comment='비율이 0.5면 하루 만에 절반, 0.9면 일주일 만에 절반이네요. 비율 하나가 기억 길이를 정하는군요.'),
  pair=('종을 한 번 친다. 소리는 처음에 크고, 시간이 갈수록 일정한 비율로 작아진다. 어떤 종은 금방 멎고 어떤 종은 오래 운다. 하지만 어느 종이든 결국 들리지 않게 된다.','요일 평균을 뺀 나머지에서는 어제와의 상관이 0.48, 그제 0.26, 사흘 전 0.15였다. 하루마다 절반쯤으로 준다. 이렇게 일정한 비율로 꺼지는 메아리를 가진 기록을 <b>단기기억</b> 기록이라 한다.'),
  talk=[('doc','think','요일 흐름을 걷어 내면 메아리는 며칠이나 갈까요?'),('robo','happy','28일 전에도 0.62였잖아! 걷어 내도 한 달은 가지.'),('fly','point','“실제 메아리 겹쳐 보기”를 눌러 봐. 그리고 남는 비율을 0.5에 맞춰 봐.')],
  panel='<div class="panel"><h3>실험 — 충격 하나가 꺼지는 모습</h3>'+cv('c2','가로축은 지난 날 수 0일부터 30일, 세로축은 남은 비율. 남는 비율에 따라 곡선이 빨리 또는 천천히 0으로 내려간다')+'<div class="ctrl">'+rg('r2P','하루 뒤 남는 비율',0.1,0.95,0.5,0.05)+'<div class="group"><button class="bt" type="button" id="b2M" aria-pressed="false">실제 메아리 겹쳐 보기</button></div></div><div class="kpis" id="k2"></div><div class="insight" id="ins2" aria-live="polite"></div><h3>행동으로 보기 — 종소리</h3>'+cv('c2b','원이 날마다 일정한 비율로 작아지는 그림. 원 하나가 하루 뒤 남은 소리 크기다','wide')+'<p style="font-size:14px;color:var(--muted);margin-bottom:0">원 하나가 하루다. 왼쪽이 종을 친 날이고 오른쪽으로 갈수록 날이 지난다.</p></div>',
  report='보고드려요. 요일 평균을 빼고 재니 어제 0.48, 그제 0.26, 사흘 전 0.15였고, 일주일 전은 0에 가까웠어요. 28일 전의 0.62는 요일이 되풀이된 것이었어요.',
  stepsh='두 메아리를 가르기',steps=['요일마다 평균 매출을 구한다. 숫자 7개짜리 표다. 이것이 “달력이 기억하는 것”이다.','날마다 그 요일 평균을 뺀다. 남은 것이 달력에 없는 출렁임이다.','남은 것의 메아리를 다시 잰다. 하루마다 절반쯤으로 줄어 일주일이면 0이다.','그래서 이 기록에 필요한 기억은 “요일 평균표 + 어제 하나”면 된다.'],
  lim='세상의 모든 기록이 이렇게 빨리 꺼지는 것은 아니다. 강 수위나 금융 시장의 출렁임에서는 몇 달 전의 흔적이 좀처럼 꺼지지 않는다. 1-3에서 그런 메아리를 만난다.',
  intern=('sia','guide','순서대로 말씀드릴게요. 다음은 대결, 그다음이 정리예요.'),
  concepts=['concept/short-memory','concept/half-life','concept/decay-rate','method/deseasonalize'])],
 duel=dict(title='어제 하나 vs 28일 창 — 요일 흐름을 뺀 뒤',metric='검증 오차',tag='일상: 한 쪽 vs 28쪽',q='요일 평균을 뺀 나머지 출렁임을 맞힌다. 어제 값 하나만 쓰는 쪽과 28일 창을 쓰는 쪽, 검증 50일에서 누가 덜 빗나갈까?',
  fly=('어제 하나 — 정할 숫자 2개','메아리가 하루에 절반씩 꺼져. 어제만 보면 돼.'),robo=('28일 창 — 정할 숫자 29개','1-1에서 28일 창이 제일 고르다고 했잖아. 이번에도 28일!'),rule='검증 오차(평균 절대 오차, 낮을수록 좋음). 막대가 짧은 쪽이 이긴다.'),
 sumh='정리 — 메아리 성적표',
 sum='<div class="tw"><table class="tb" id="sumTb"><tr><th>며칠 전</th><th>그대로 잰 메아리</th><th>요일 흐름을 뺀 뒤</th><th>읽는 법</th></tr></table></div><p style="font-size:14px;color:var(--muted)">표의 숫자는 이 페이지를 열 때 브라우저가 훈련 200일로 직접 계산한 값이다.</p><div class="steps"><div><b class="n">1</b><h4>메아리부터 잰다</h4><p>기억 장치를 고르기 전에 과거가 오늘에 얼마나 남는지부터 잰다.</p></div><div><b class="n">2</b><h4>되풀이는 달력에게</h4><p>요일처럼 되풀이되는 흐름은 표 하나로 기억할 수 있다. 긴 창이 필요 없다.</p></div><div><b class="n">3</b><h4>빨리 꺼지면 짧게</h4><p>남은 메아리가 하루에 절반씩 꺼진다면 어제 하나로 충분하다.</p></div></div><div class="bridge field"><h4>업무에 옮기면</h4><p>“작년 같은 달” “지난주 같은 요일”처럼 달력으로 설명되는 부분을 먼저 떼어 낸다. 그러고 남은 부분이 며칠이나 이어지는지 본다. 이 순서만 지켜도 필요 없이 긴 과거를 넣는 일이 준다. 이 기록에서는 요일 평균표와 어제 값 하나로 검증 오차가 <b id="sumBest"></b>만 원이었다. 1-1의 28일 창(2.74만 원)보다 낮다.</p><p class="lim">비유의 한계 · 요일 평균을 빼는 방법은 흐름이 해마다 그대로일 때만 통한다. 흐름 자체가 바뀌는 기록은 다른 손질이 필요하다.</p></div>',
 outro=[('doc','front','오늘의 한 줄이에요. 기억의 길이는 메아리가 정해요. 빨리 꺼지면 짧은 기억이면 돼요.'),('asst','smile','28일 전의 0.62가 요일 되풀이였다는 게 제일 놀라웠어요.'),('fly','coffee','이번엔 내 말이 맞았지. 그런데 안 꺼지는 메아리도 있다며? 그건 좀 궁금한데.'),('robo','meh','달력이 기억해 주는 걸 내가 또 외우고 있었네… 다음엔 진짜 오래 가는 메아리를 찾아오겠어!'),('moa','report','요일 평균표는 제가 서랍에 넣어 둘게요. 숫자 일곱 개라 금방 찾아요.')],
 examples=['매출 기록: 가게 하루 매출(만 원) 300일. 수준 100 + 요일 흐름 + 잡음으로 만든 연습용 데이터 (시드 2026)','이 기록의 잡음은 “하루 뒤 0.5배가 남는” 규칙으로 만들었다. 요일 흐름을 뺀 뒤 잰 0.48은 그 규칙이 표본에서 드러난 값이다','상관 값(0.47, 0.72, −0.49, 0.62, 0.48, 0.26, 0.15)과 오차 값(2.51, 2.71)은 이 기록에서 계산한 값이다','충격 10만 원과 종소리 그림은 설명용 도식이다'],
 refs=['box1970time','ahn2026ts3_1_1'],
 claims=[('claim/acf-box-jenkins','자기상관 그림으로 시계열 모형을 고르는 절차는 Box와 Jenkins(1970)가 체계화했다','#lv1','box1970time','책 전체','concept/autocorrelation')],
 openq=[('question/mem-slow-echo','일정한 비율보다 천천히 꺼지는 메아리도 있을까?','#lv2','1-3에서 장기기억으로 다룬다')],
 nodes=[('concept/autocorrelation','Concept','자기상관','autocorrelation','#lv1','k일 전 값과 오늘 값이 함께 움직이는 정도를 −1에서 +1 사이 숫자로 잰 것.'),
  ('concept/echo','Concept','메아리 (과거의 흔적)','echo of the past','#lv1','이 시리즈에서 자기상관을 부르는 별명. 과거의 값이 오늘 값에 남긴 흔적.'),
  ('concept/lag','Concept','시차 (며칠 전)','lag','#lv1','거슬러 가는 날 수 k.'),
  ('concept/seasonality','Concept','되풀이되는 흐름 (계절성)','seasonality','#lv1','요일·달처럼 일정한 간격으로 되풀이되는 오르내림.'),
  ('concept/short-memory','Concept','단기기억 (빨리 꺼지는 메아리)','short memory','#lv2','메아리가 하루마다 일정한 비율로 줄어 금방 0이 되는 성질.'),
  ('concept/half-life','Concept','반감기','half-life','#lv2','메아리가 절반으로 줄어드는 데 걸리는 날 수.'),
  ('concept/decay-rate','Concept','하루 뒤 남는 비율 (φ)','decay rate','#lv2','하루가 지날 때 메아리가 몇 배로 남는지.'),
  ('method/deseasonalize','Method','요일 평균 빼기','deseasonalizing','#lv2','요일별 평균을 빼서 되풀이되는 흐름을 걷어 내는 손질.'),
  ('sim/1-2-acf','Simulation','날 수별 메아리','autocorrelation explorer','#lv1'),('sim/1-2-impulse','Simulation','충격 하나가 꺼지는 모습','impulse decay','#lv2'),('sim/1-2-duel','Simulation','대결: 어제 하나 vs 28일 창','duel: lag-1 vs 28-day window','#vs')],
 edges=[('concept/lag','partOf','concept/autocorrelation','#lv1'),('concept/echo','broader','concept/autocorrelation','#lv1'),('concept/autocorrelation','prerequisiteOf','concept/short-memory','#lv2'),('concept/seasonality','contrastsWith','concept/short-memory','#lv2'),
  ('concept/decay-rate','prerequisiteOf','concept/half-life','#lv2'),('method/deseasonalize','solves','concept/seasonality','#lv2'),('concept/autocorrelation','demonstratedBy','sim/1-2-acf','#lv1'),('concept/short-memory','demonstratedBy','sim/1-2-impulse','#lv2'),('concept/short-memory','demonstratedBy','sim/1-2-duel','#vs'),('concept/short-memory','raises','question/mem-slow-echo','#lv2')],
 gloss={'메아리':['메아리','이 시리즈의 별명','과거의 값이 오늘 값에 남긴 흔적. 통계 용어로는 자기상관.'],'자기상관':['자기상관','통계','k일 전 값과 오늘 값이 함께 움직이는 정도. −1에서 +1 사이.'],'상관':['상관','통계','두 값이 함께 오르내리는 정도. +1이면 꼭 같이, −1이면 꼭 거꾸로, 0이면 무관.'],
  '요일 흐름':['요일 흐름','데이터','요일마다 되풀이되는 오르내림. 7일 주기.'],'요일 평균':['요일 평균','손질','월요일끼리, 화요일끼리 … 따로 낸 평균. 숫자 7개.'],'반감기':['반감기','성질','메아리가 절반으로 줄어드는 데 걸리는 날 수.'],'남는 비율':['하루 뒤 남는 비율 (φ)','성질','하루가 지날 때 메아리가 몇 배로 남는지. 0.5면 절반.'],
  '단기기억':['단기기억','통계','메아리가 일정한 비율로 줄어 금방 꺼지는 성질.'],'검증 오차':['검증 오차','지표','모델이 본 적 없는 검증 기간에서 평균적으로 빗나간 크기.'],'훈련':['훈련 데이터','평가','모델의 숫자를 정하는 데 쓰는 기록. 앞 200일.'],'창':['창 (window)','설정값','다음 값을 짐작할 때 펼쳐 놓는 과거 구간.'],'산점도':['산점도','그림','두 값을 짝지어 점으로 찍은 그림.']},
 core=['메아리','자기상관','반감기','요일 평균','단기기억'],
 quiz={'why':[dict(q='기억 장치를 고르기 전에 메아리부터 재는 까닭은?',o=['메아리가 클수록 계산이 빨라서','과거가 오늘과 상관없다면 기억할 까닭이 없어서','메아리를 재면 오차가 0이 돼서'],a=1,why='상관이 남아 있는 곳까지만 기억하면 돼요.',hint='기억의 값어치를 떠올려 보세요.',t='concept/echo')],
  'lv1':[dict(q='7일 전과의 상관이 어제와의 상관보다 큰 까닭은?',o=['7일 전 매출이 더 커서','같은 요일끼리 닮아서','기록이 잘못돼서'],a=1,why='이 가게는 요일마다 매출이 달라요. 같은 요일끼리 닮았어요.',hint='7일 전은 무슨 요일일까요?',t='concept/seasonality'),
        dict(q='상관이 0에 가까운 날의 값은 오늘을 짐작하는 데',o=['큰 도움이 된다','거의 도움이 안 된다','거꾸로 쓰면 된다'],a=1,why='함께 움직이지 않으니 알아도 쓸모가 적어요.',hint='0은 “무관”이에요.',t='concept/autocorrelation')],
  'lv2':[dict(kind='계산',q='하루 뒤 남는 비율이 0.5다. 평소보다 20만 원 많았던 날의 흔적은 이틀 뒤에 얼마 남을까?',o=['10만 원','5만 원','2.5만 원'],a=1,why='20 × 0.5 × 0.5 = 5만 원이에요.',hint='0.5를 두 번 곱해요.',t='concept/decay-rate'),
        dict(q='요일 평균을 뺀 뒤 28일 전의 메아리가 거의 0이 된 까닭은?',o=['28일 전의 0.62가 요일이 되풀이된 효과였어서','28일 전 기록을 지워서','계산이 틀려서'],a=0,why='되풀이를 걷어 내니 남은 메아리는 일주일 안에 꺼졌어요.',hint='달력이 기억하는 것과 머리가 기억하는 것을 갈라 보세요.',t='method/deseasonalize')],
  'vs':[dict(q='이 대결에서 28일 창이 진 까닭은?',o=['창이 너무 짧아서','꺼진 메아리 자리의 우연한 출렁임까지 외워서','어제 값을 안 봐서'],a=1,why='메아리가 일주일이면 꺼지는데 28일을 보니, 쓸모없는 자리의 잡음에 숫자를 맞췄어요.',hint='정할 숫자가 29개였어요.',t='concept/short-memory')]},
)
JS=r'''
var Y=makeSeries(2026,300,{}),DS=deseason(Y,200),RE=DS.e,A=[0],AR_=[0],k;
for(k=1;k<=35;k++){A.push(acf(Y,k,0,200));AR_.push(acf(RE,k,0,200));}
var S1=scoreAR(RE,1,200,250),S28=scoreAR(RE,28,200,250);PAGE._T={A:A,Ar:AR_,s1:S1.va,s28:S28.va,phi:S1.m.phi[0]};
/* 칸 ① */
var K=7,cv=$('#c1'),cvb=$('#c1b');
function upd1(){var v=A[K];
  kpis($('#k1'),[[tpl('{0}일 전',K),'고른 날 수','a'],[(v>=0?'+':'−')+f2(Math.abs(v),2),'오늘 값과의 상관',v>0.3?'g':(v<-0.3?'r':'')],[K%7===0?'같은 요일':'다른 요일','요일 관계','m'],[Math.abs(v)>0.5?'뚜렷함':(Math.abs(v)>0.2?'약함':'거의 없음'),'메아리','i']]);
  $('#ins1').innerHTML=K%7===0?tpl('<p class="g">{0}일 전은 오늘과 같은 요일이에요. 상관 {1}. 그날 매출이 높았으면 오늘도 높을 가능성이 커요.</p>',K,f2(v,2)):
    (v<-0.3?tpl('<p class="r">{0}일 전과는 거꾸로 움직여요. 상관 {1}. 주중과 주말이 엇갈리는 간격이에요.</p>',K,f2(v,2)):
    tpl('<p class="a">{0}일 전과의 상관은 {1}이에요. 같은 요일(7의 배수)만큼 뚜렷하지는 않아요.</p>',K,f2(v,2)));drawAll();}
bindRange('r1K',function(v){K=v;upd1();},function(v){return tpl('{0}일 전',v);});
addMod(cv,function(){var H=280,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);
  var o=bars(ctx,W,H,A,K,{y0:-0.7,y1:0.9,ticks:[-0.5,0,0.5],xl:function(i){return i%7===0?i+'일':'';}});
  txt(ctx,'세로축: 상관 (메아리 크기)',o.P.l+4,14,{size:10,color:COL.muted});stamp(ctx,W,'설명용 모형 · 실제 데이터 아님');});
addMod(cvb,function(){var H=260,W=fit(cvb,H),ctx=cvb.getContext('2d');ctx.clearRect(0,0,W,H);
  var rgY=rangeOf([Y.slice(0,200)]),P={l:46,r:14,t:26,b:30},iw=W-P.l-P.r,ih=H-P.t-P.b;
  function X(v){return P.l+(v-rgY[0])/(rgY[1]-rgY[0])*iw;}function Yf(v){return P.t+(1-(v-rgY[0])/(rgY[1]-rgY[0]))*ih;}
  ctx.strokeStyle='rgba(157,155,184,.2)';ctx.strokeRect(P.l,P.t,iw,ih);ctx.fillStyle=A[K]>=0?'rgba(94,227,156,.75)':'rgba(240,96,77,.75)';
  for(var t=K;t<200;t++){ctx.beginPath();ctx.arc(X(Y[t-K]),Yf(Y[t]),2.6,0,7);ctx.fill();}
  txt(ctx,tpl('{0}일 전 매출 →',K),P.l+iw/2,H-10,{size:11,color:COL.muted,align:'center'});txt(ctx,'↑ 그날 매출',P.l+4,P.t+10,{size:11,color:COL.muted});
  txt(ctx,tpl('상관 {0}',f2(A[K],2)),W-P.r-6,P.t+ih-10,{size:13,color:COL.amber,align:'right',w:'700'});stamp(ctx,W,'설명용 모형 · 실제 데이터 아님');});
/* 칸 ② */
var PH=0.5,SH=false,cv2=$('#c2'),cv2b=$('#c2b');
function upd2(){var hl=Math.log(0.5)/Math.log(PH),d10=Math.ceil(Math.log(0.1)/Math.log(PH));
  kpis($('#k2'),[[f2(PH,2),'하루 뒤 남는 비율','a'],[tpl('{0}일',f2(hl,1)),'반감기 (절반이 되는 날 수)','g'],[f2(Math.pow(PH,7)*100,1)+'%','7일 뒤 남는 크기','m'],[tpl('{0}일',d10),'10% 아래로 내려가는 날','r']]);
  var m=tpl('<p>평소보다 10만 원 많았던 날의 흔적은 하루 뒤 {0}만 원, 사흘 뒤 {1}만 원, 일주일 뒤 {2}만 원이 남아요.</p>',f2(10*PH,2),f2(10*Math.pow(PH,3),2),f2(10*Math.pow(PH,7),2));
  if(SH)m+=tpl('<p class="g">초록 점이 이 기록에서 실제로 잰 메아리예요(요일 평균을 뺀 뒤). 어제 {0}, 그제 {1}, 사흘 전 {2}. 남는 비율 0.5 곡선과 거의 겹쳐요.</p>',f2(AR_[1],2),f2(AR_[2],2),f2(AR_[3],2));
  $('#ins2').innerHTML=m;drawAll();}
bindRange('r2P',function(v){PH=v;upd2();},function(v){return f2(v,2);});
$('#b2M').addEventListener('click',function(){SH=!SH;this.setAttribute('aria-pressed',SH?'true':'false');upd2();});
addMod(cv2,function(){var H=280,W=fit(cv2,H),ctx=cv2.getContext('2d');ctx.clearRect(0,0,W,H);var d=[];for(var i=0;i<=30;i++)d.push(Math.pow(PH,i));
  var o=plot(ctx,W,H,{x0:0,x1:30,y0:-0.1,y1:1.05,yn:4,yfmt:function(v){return v.toFixed(2);},xticks:[0,7,14,21,28],xlab:function(v){return v+'일';},lines:[{d:d,color:COL.amber,w:2.2}],marks:[{x:Math.log(0.5)/Math.log(PH),color:COL.info,label:'절반'}]});
  ctx.strokeStyle='rgba(157,155,184,.4)';ctx.beginPath();ctx.moveTo(o.P.l,o.Y(0));ctx.lineTo(W-o.P.r,o.Y(0));ctx.stroke();
  if(SH){ctx.fillStyle=COL.gfp;for(i=1;i<=28;i++){ctx.beginPath();ctx.arc(o.X(i),o.Y(AR_[i]),3.4,0,7);ctx.fill();}txt(ctx,'● 실제로 잰 메아리',W-o.P.r-6,o.P.t+12,{size:11,color:COL.gfp,align:'right'});}
  txt(ctx,'세로축: 남은 비율',W-o.P.r-6,o.Y(0)-10,{size:10,color:COL.muted,align:'right'});stamp(ctx,W,'설명용 도식');});
var ph=0;addMod(cv2b,function(dt){var H=130,W=fit(cv2b,H),ctx=cv2b.getContext('2d');ctx.clearRect(0,0,W,H);if(!REDUCE)ph+=dt;var n=15,gw=(W-20)/n,cur=REDUCE?n:Math.floor(ph/0.35)%(n+5);
  for(var i=0;i<n&&i<=cur;i++){var r=Math.max(1.2,Math.pow(PH,i)*Math.min(30,gw*0.46)),x=10+i*gw+gw/2;ctx.fillStyle='rgba(241,182,70,'+(0.25+0.6*Math.pow(PH,i))+')';ctx.beginPath();ctx.arc(x,60,r,0,7);ctx.fill();
    txt(ctx,i===0?'친 날':i+'일',x,108,{size:10,color:COL.muted,align:'center'});txt(ctx,f2(Math.pow(PH,i)*100,0)+'%',x,20,{size:10,color:COL.amber,align:'center'});}
  stamp(ctx,W,'설명용 도식');});
/* 대결 */
Duel({el:'#duel',higherIsBetter:false,drawMargin:0.05,fmt:function(v){return f2(v,2);},run:function(){return {fly:S1.va,robo:S28.va,metric:'검증 오차'};},
  say:function(f,b){return tpl('검증 오차는 초파리 쪽 어제 하나가 {0}만 원, 주판봇 쪽 28일 창이 {1}만 원이에요. 차이는 큰 값의 {2}%예요.',f2(f,2),f2(b,2),f2(Math.abs(f-b)/Math.max(f,b)*100,1));},
  lessons:{F:'빨리 꺼지는 메아리에는 짧은 기억이면 충분하다. 긴 창은 꺼진 자리의 잡음을 외웠다',D:'메아리가 꺼진 자리는 봐도 안 봐도 같았다',R:'먼 자리에도 쓸 것이 남아 있었다'},
  after:function(){$('#duelNote').innerHTML=tpl('<p>어제 하나를 쓴 쪽이 찾은 남는 비율은 {0}이었어요. 이 기록을 만들 때 쓴 규칙(0.5)과 가까워요.</p><p>28일 창의 훈련 오차는 {1}까지 내려갔어요. 훈련에서만 좋았다는 뜻이에요.</p>',f2(S1.m.phi[0],2),f2(S28.tr,2));}});
/* 정리 */
var note={1:'어제. 여운이 남는다',2:'그제. 절반쯤',3:'주중·주말이 엇갈린다',7:'같은 요일. 되풀이',14:'같은 요일. 되풀이',28:'같은 요일. 되풀이'};
$('#sumTb').insertAdjacentHTML('beforeend',[1,2,3,7,14,28].map(function(l){return '<tr><td class="num">'+l+'일 전</td><td class="num">'+f2(A[l],2)+'</td><td class="num">'+f2(AR_[l],2)+'</td><td>'+note[l]+'</td></tr>';}).join(''));
$('#sumBest').textContent=f2(S1.va,2);
upd1();upd2();
'''
