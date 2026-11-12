# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
P=dict(
 title='꺼지지 않는 메아리 — 통계가 말하는 장기기억',chip='강 수위 앵커',
 q='몇 달 전의 일이 아직도 오늘을 움직이는 기록이 있을까?',
 lead='<p>1-2의 매출 기록에서는 메아리가 하루에 절반씩 꺼졌다. 모든 기록이 그렇지는 않다. 강 수위처럼 몇 달 전의 흔적이 좀처럼 사라지지 않는 기록이 있다. 통계에서는 이런 성질을 <b>장기기억</b>이라 부른다. 이 페이지에서는 가상의 강 두 줄기로 두 메아리를 견준다.</p><p style="font-size:14px;color:var(--muted)">여기서 말하는 장기기억은 기록 자체의 성질이다. 1-5에 나올 신경망 LSTM의 이름에 든 “long”과는 다른 말이다.</p>',
 objs=['곱하기로 줄어드는 메아리와 나누기로 줄어드는 메아리의 차이를 말한다','허스트 지수가 0.5보다 크면 무슨 뜻인지 설명한다','먼 과거가 쓸모 있어지는 때(멀리 내다볼 때)를 든다'],mins=22,
 kpis=[('0.31','강 A의 50일 전 메아리 (이론값)'),('0.00','강 B의 50일 전 메아리 (이론값)'),('29%','강 A에서 최근 20일 평균이 줄인 오차'),('5.9%','강 A에서 20일 창이 어제 하나를 앞선 폭')],
 hero=['오늘은 꺼지지 않는 메아리예요. 1951년에 나일강 기록에서 처음 숫자로 잡힌 현상이에요.','가상의 강 두 줄기를 2000일씩 준비했어요. 어제와의 상관은 둘이 똑같이 맞춰 뒀어요.','어제 상관이 같으면 같은 강이지. 먼 과거가 정말 다를까?','오래 가는 메아리! 이번에야말로 긴 기억이 빛을 볼 차례야.'],
 first3=['어떤 기록은 과거의 흔적이 곱하기가 아니라 나누기로 줄어든다. 그래서 몇 달이 지나도 다 꺼지지 않는다.','기억이 얼마나 길어야 하는지는 기록의 성질이 정한다. 같은 방법이 어떤 기록에서는 이기고 어떤 기록에서는 진다.','다음 달 평균처럼 멀리 내다보는 계획을 세울 때, 이런 기록에서는 최근 몇 주의 수준이 중요한 실마리가 된다.'],
 abbr=['AR','ARFIMA','ACF','MAE'],cast=dict(fly='먼 과거는 다 씻겨 나갔다',robo='먼 과거가 아직 울린다'),
 whyh='왜 꺼지지 않는 메아리를 봐야 할까',whytag='방법: 두 기록의 메아리 견주기',prev='1-2 메아리는 언제 꺼지나',
 why=[('1-2의 결론은 반쪽이다','“메아리는 금방 꺼지니 짧은 기억이면 된다”는 매출 기록에서만 맞았다. 다른 기록에서는 뒤집힌다.'),('오래된 수수께끼','나일강의 수위 기록을 살핀 허스트는 물이 많은 해와 적은 해가 우연이라고 보기 어려울 만큼 길게 이어진다는 것을 찾았다 [[hurst1951long]].'),('기억 장치의 숙제','먼 과거가 쓸모 있는 기록이 있다면, 그것을 싸게 담는 기억 장치가 필요해진다. 1-4부터의 주제다.')],
 levels=[dict(id='lv1',no='①',title='두 메아리 — 곱하기로 줄기와 나누기로 줄기',nav='두 메아리',tag1='방법: 메아리가 줄어드는 모양 견주기',tag2='일상: 종소리와 강물',
  why=('두 강의 수위 기록이 있다. 어제와의 상관은 두 강이 똑같다. 그런데 한 강은 가뭄이 몇 달씩 이어지고 다른 강은 금방 평소로 돌아온다.','1-2의 방법(하루마다 같은 비율로 줄기)은 메아리의 모양이 한 가지뿐이다. 비율을 아무리 바꿔도 몇 달 가는 메아리와 어제 상관을 함께 맞출 수 없다.','메아리가 줄어드는 모양을 하나 더 둔다. 날 수로 “나누어” 줄어드는 모양이다. 이 모양은 처음에는 빨리 줄지만 뒤로 갈수록 좀처럼 줄지 않는다 [[granger1980introduction]].','종소리는 곱하기로 줄어 금방 멎는다. 큰 강의 수위는 나누기로 줄어 오래 남는다.'),
  math=dict(ask='곱하기로 줄든 나누기로 줄든 결국 0으로 가잖아요. 뭐가 그렇게 달라요?',school='지수함수와 반비례 꼴의 차이다. ½을 거듭 곱하는 것과, 날 수의 제곱근으로 나누는 것을 견준다.',
   eq='빨리 꺼지는 메아리 ≈ ½ × ½ × … (k번) &nbsp;·&nbsp; 천천히 꺼지는 메아리 ≈ 1 ÷ √k',pieces=[('k','지난 날 수'),('½을 k번 곱하기','날이 하루 늘 때마다 절반이 된다'),('1 ÷ √k','날 수가 100배가 되어야 10분의 1이 된다. 오래 가는 세기 d가 0.25일 때의 모양이다'),('세기 d','클수록 더 천천히 준다. 이 페이지의 강 A는 0.4다'),('허스트 지수 H','0.5면 기억 없음. 1에 가까울수록 메아리가 오래 간다')],
   num='10일 뒤를 보자. ½을 열 번 곱하면 약 0.001이다. 1 ÷ √10은 약 0.32다. 100일 뒤에는 앞의 것은 0과 구분이 안 되고, 뒤의 것은 1 ÷ √100 = 0.1이 남는다. 이 계산은 세기 0.25일 때의 예다. 강 A는 세기가 0.4라서 이보다 더 천천히 줄어, 100일 뒤에도 0.27이 남는다.',comment='세기 0.25면 100일 뒤 10%, 강 A처럼 0.4면 27%가 남네요. 줄어드는 “모양”이 다르면 끝이 이렇게 달라지는군요.'),
  pair=('종을 치면 소리는 일정한 비율로 작아져 곧 멎는다. 큰 강은 다르다. 비가 많이 온 해에는 땅속과 호수에 물이 쌓이고, 그 물이 몇 달에 걸쳐 조금씩 강으로 흘러든다. 오래된 비가 오늘 수위에 남는다.','천천히 꺼지는 메아리를 담는 방법이 분수 차분이다. 세기를 d라는 숫자 하나로 정한다 [[hosking1981fractional]]. d가 0이면 기억이 없고, 0.5에 가까울수록 메아리가 오래 간다. 허스트 지수로는 H = d + 0.5다.'),
  talk=[('doc','front','두 강은 어제와의 상관이 똑같아요. 50일 전과의 상관도 같을까요?'),('fly','arms','어제가 같으면 50일 전도 같겠지. 둘 다 0일 거야. 정말 다를까?'),('robo','chart','“실제로 잰 메아리”를 눌러 봐! 그리고 세기를 0.4에 놓고 50일 자리를 보라고.')],
  panel='<div class="panel"><h3>실험 — 두 가지로 줄어드는 메아리</h3>'+cv('c1','가로축은 지난 날 수 1일부터 200일, 세로축은 메아리 크기. 한 곡선은 곧 0이 되고 다른 곡선은 200일까지 남는다')+'<div class="ctrl">'+rg('r1D','오래 가는 세기 d',0.05,0.45,0.4,0.05)+bt('b1M','실제로 잰 메아리 겹쳐 보기')+'</div><div class="kpis" id="k1"></div><div class="insight" id="ins1" aria-live="polite"></div><h3>행동으로 보기 — 두 강의 400일</h3>'+cv('c1b','두 강의 수위를 400일 동안 그린 그림. 강 A는 길게 높거나 낮은 구간이 이어지고 강 B는 평소 수위 주변을 빠르게 오간다')+note('위가 강 A(천천히 꺼지는 메아리), 아래가 강 B(빨리 꺼지는 메아리)다. 가는 가로선이 평소 수위다.')+'</div>',
  report='보고드려요. 이론값으로 강 A는 50일 전 0.31, 100일 전 0.27이 남아요. 강 B는 50일 전에 이미 0.00이에요. 실제로 잰 값은 강 A가 이론보다 낮게 나왔지만, 강 B보다는 훨씬 오래 남았어요.',
  stepsh='그림 읽는 법',steps=['두 곡선은 1일 자리에서 만난다. 어제와의 상관을 같게 맞췄기 때문이다.','주황 곡선(곱하기)은 20일쯤이면 0이다.','초록 곡선(나누기)은 처음에 빨리 내려오다가 완만해져서 200일에도 남는다.','실제로 잰 메아리는 이론보다 낮게 나온다. 메아리를 잴 때 기록 전체의 평균을 기준으로 삼는데, 길게 높거나 낮은 구간이 이어지는 기록에서는 그 평균이 구간을 따라 끌려가 먼 과거와의 닮음이 작게 잡히기 때문이다. 기록이 길수록 이론값에 가까워진다.','그래도 두 강의 차이는 분명하다. 10일 전을 보면 강 A는 0.25, 강 B는 0.02다.'],
  lim='메아리가 오래 간다는 것은 알았다. 그런데 하루 뒤를 맞히는 데는 얼마나 도움이 될까? 그리고 더 멀리 내다볼 때는? 다음 칸에서 잰다.',
  concepts=['concept/long-memory','concept/hurst-exponent','method/fractional-differencing','concept/hyperbolic-decay','concept/short-memory']),
 dict(id='lv2',no='②',title='먼 과거가 쓸모 있어지는 때 — 다음 달 평균 맞히기',nav='멀리 내다보기',tc='m',tag1='방법: 최근 평균으로 다음 30일 평균 짐작하기',tag2='일상: 저수지 물 계획',
  why=('저수지를 맡은 사람은 내일 수위보다 다음 한 달의 평균 수위가 궁금하다. 물을 얼마나 내보낼지 정해야 하기 때문이다.','메아리가 빨리 꺼지는 기록에서는 답이 싱겁다. “한 달 뒤면 다 꺼지니 평소 평균으로 돌아간다”가 가장 좋은 답이다.','메아리가 천천히 꺼지는 기록에서는 최근 며칠의 평균 수위가 다음 달에도 남는다. 최근 평균과 평소 평균을 적당히 섞어 짐작한다.','요즘 계속 물이 많았다면 다음 달도 평소보다 많다고 보는 것이다. 얼마나 믿을지는 강마다 다르다.'),
  math=dict(ask='최근 평균을 “적당히 섞는다”는 걸 식으로 쓰면요?',school='일차함수 y = ax + b다. 최근 평균을 넣으면 다음 달 평균 짐작값이 나온다.',
   eq='다음 30일 평균 짐작값 = 기본값 + 믿는 정도 × 최근 평균',pieces=[('최근 평균','지난 며칠의 수위를 더해 날 수로 나눈 값'),('믿는 정도','0이면 최근을 무시하고, 1이면 최근이 그대로 이어진다고 본다'),('기본값','평소 수위 쪽으로 끌어당기는 몫')],
   num='평소 수위가 100cm다. 기본값 50, 믿는 정도 0.5라고 하자. 최근 20일 평균이 110cm였다면 50 + 0.5 × 110 = 105cm다. 평소(100)와 최근(110)의 한가운데다.',comment='최근을 절반만 믿는 거네요. 믿는 정도는 훈련 기록이 정해 주고요.'),
  pair=('저수지 관리인이 지난 몇 주의 수위 기록을 넘겨 본다. 계속 높았다면 다음 달 방류량을 늘려 잡는다. 금방 평소로 돌아오는 강이라면 이런 계산이 소용없다.','다음 30일의 평균을 맞히는 문제에서, “평소 평균만 쓰기”와 “최근 평균을 섞기”의 검증 오차를 견준다. 강 A에서는 차이가 크고 강 B에서는 차이가 작다.'),
  talk=[('doc','think','다음 달 평균 수위를 맞힐 때, 지난 몇 주를 보는 게 도움이 될까요?'),('robo','happy','당연하지! 60일, 100일, 많이 볼수록 정확해!'),('fly','point','강을 B로 바꿔 봐. 그리고 A로 돌아와서 슬라이더를 100까지 밀어 봐.')],
  panel='<div class="panel"><h3>실험 — 최근 며칠을 볼까</h3>'+cv('c2','가로축은 평균을 내는 최근 날 수 1일부터 100일, 세로축은 검증 오차. 점선은 평소 평균만 썼을 때의 오차다')+'<div class="ctrl">'+tg('g2','강',[('a','강 A (천천히 꺼짐)'),('b','강 B (빨리 꺼짐)')])+rg('r2L','최근 며칠 평균',1,100,20)+'</div><div class="kpis" id="k2"></div><div class="insight" id="ins2" aria-live="polite"></div><h3>행동으로 보기 — 한 번의 짐작</h3>'+cv('c2b','최근 150일 수위와 그 뒤 30일. 최근 평균을 낸 구간이 밝게 표시되고, 다음 30일의 실제 평균과 짐작값이 가로선으로 그려진다','wide')+note('밝은 띠가 평균을 낸 구간, 오른쪽 띠가 맞혀야 할 30일이다. 흰 선이 실제 평균, 청록 선이 짐작값, 회색 점선이 평소 평균이다.')+'</div>',
  report='보고드려요. 강 A에서 평소 평균만 쓰면 2.87cm, 최근 20일 평균을 섞으면 2.04cm 빗나갔어요. 29% 줄었어요. 강 B는 1.33에서 1.21로 8% 줄었고요.',
  stepsh='왜 강마다 다른가',steps=['강 B는 메아리가 20일이면 꺼진다. 다음 30일의 대부분은 지금과 상관이 없다.','강 A는 메아리가 몇 달 간다. 지금 수위가 높으면 다음 30일도 높은 쪽에 머문다.','그래서 강 A에서만 최근 평균이 좋은 실마리가 된다.','그렇다고 길수록 좋은 것은 아니다. 강 A에서도 2~3주 근처가 가장 낮고 100일에서는 다시 나빠진다. 최근 평균이 무뎌지기 때문이다.'],
  lim='오래 가는 메아리를 쓰려면 기록을 수십 일씩 펼쳐야 한다. 1-1에서 본 대로 창이 길면 값을 치른다. 메아리의 세기 d도 사람이 골라 줘야 한다. 과거를 펼치지 않고 줄여서 들고 다니는 방법이 있을까? 1-4에서 메모 한 칸으로 해 본다.',
  intern=SIA,concepts=['task/long-horizon-forecast','concept/mean-reversion','concept/long-memory'])],
 duel=dict(title='어제 하나 vs 20일 창 — 강 A에서 다시',metric='검증 오차',tag='일상: 한 쪽 vs 20쪽',q='1-2와 같은 대결을 강 A에서 다시 한다. 내일 수위를 맞히는 문제다. 어제 값 하나만 쓰는 쪽과 20일 창을 쓰는 쪽, 검증 300일에서 누가 덜 빗나갈까?',
  fly=('어제 하나 — 정할 숫자 2개','1-2에서 이겼잖아. 긴 창은 잡음만 외워.'),robo=('20일 창 — 정할 숫자 21개','이 강은 메아리가 안 꺼져. 이번엔 길게 본 쪽이 이겨!'),rule='검증 오차(평균 절대 오차, 낮을수록 좋음). 막대가 짧은 쪽이 이긴다.'),
 sumh='정리 — 두 강의 성적표',
 sum='<div class="tw"><table class="tb" id="sumTb"><tr><th></th><th>강 A (천천히 꺼짐)</th><th>강 B (빨리 꺼짐)</th></tr></table></div><p style="font-size:14px;color:var(--muted)">표의 숫자는 이 페이지를 열 때 브라우저가 직접 계산한 값이다. 단위는 cm다.</p>'+steps3([('기록이 기억의 길이를 정한다','같은 “어제 하나 대 긴 창” 대결이 1-2에서는 초파리, 여기서는 주판봇의 승리였다. 방법이 아니라 기록이 달랐다.'),('멀리 볼수록 차이가 커진다','하루 뒤를 맞힐 때는 5.9% 차이였다. 다음 달 평균을 맞힐 때는 29% 차이였다.'),('이름에 속지 않기','통계의 장기기억은 기록의 성질이다. LSTM의 “long”은 기억 장치의 이름이다. 둘은 다른 말이다.')])+field('수요, 수위, 접속량 같은 기록을 다룰 때 “이 기록의 메아리는 며칠 가는가”를 먼저 본다. 몇 주 전 수준이 아직 남아 있는 기록이라면, 다음 달 계획에 최근 수준을 반영하는 것이 숫자로 이득이다.','이 페이지의 강은 정해진 규칙으로 만든 가상의 기록이다. 실제 기록에서 메아리가 오래 가 보일 때는 추세나 구조 변화가 섞였을 수도 있어 따로 살펴야 한다.'),
 outro=[('doc','front','오늘의 한 줄이에요. 기억이 얼마나 길어야 하는지는 방법이 아니라 기록이 정해요.'),('asst','smile','같은 대결인데 강이 바뀌니 승자가 바뀐 게 신기했어요.'),('fly','coffee','인정. 이 강에서는 먼 과거가 들리더군. 그래도 20쪽씩 펼치는 건 비싸.'),('robo','happy','오래 가는 메아리 만세! …그런데 숫자 21개는 좀 많긴 하네. 줄여 담는 법 없나?'),('moa','report','두 강의 기록은 따로 묶어 뒀어요. 다음 편에서 메모 한 칸으로 다시 볼게요.')],
 examples=['강 A: 가상의 하루 수위(cm) 2000일. 평소 100cm에 “분수 차분 세기 d = 0.4” 규칙의 잡음을 더해 만들었다 (시드 2027, 과거 1000일까지 반영)','강 B: 평소 100cm에 “하루 뒤 0.667배가 남는” 규칙의 잡음을 더해 만들었다 (시드 2027). 어제와의 상관 이론값이 강 A와 같다','훈련 1400일 · 검증 300일 · 시험 300일(봉인). 다음 30일 평균 실험은 검증 구간 안에 30일이 다 들어가는 날만 썼다','이론값(0.31, 0.27)은 규칙에서 계산한 값이고, 실제로 잰 값은 기록이 유한해서 더 낮게 나온다','오차 값(2.87, 2.04, 1.33, 1.21, 2.43, 2.29)은 이 가상 기록에서 계산한 값이다. 실제 나일강 기록이 아니다','수식 상자의 “기본값 50, 믿는 정도 0.5”는 손으로 따라 하기 위한 숫자다'],
 refs=['hurst1951long','granger1980introduction','hosking1981fractional','box1970time'],
 claims=[('claim/hurst-nile','허스트(1951)는 나일강 기록에서 우연으로 보기 어려운 긴 흐름을 찾았다','#why','hurst1951long','논문 전체','concept/hurst-exponent'),
  ('claim/fractional-long-memory','분수 차분으로 천천히 꺼지는 메아리를 가진 시계열 모형을 만들 수 있다','#lv1','granger1980introduction','논문 전체','method/fractional-differencing'),
  ('claim/hosking-d','분수 차분 모형은 세기 d 하나로 메아리의 지속을 정한다','#lv1','hosking1981fractional','논문 전체','method/fractional-differencing')],
 openq=[('question/mem-compress-past','과거를 길게 펼치지 않고 줄여서 들고 다닐 수 있을까?','#lv2','1-4에서 메모 한 칸으로 다룬다')],
 nodes=[('concept/long-memory','Concept','장기기억 (천천히 꺼지는 메아리)','long memory','#lv1','메아리가 날 수의 거듭제곱으로 천천히 줄어 몇 달이 지나도 남는 기록의 성질.'),
  ('concept/short-memory','Concept','단기기억 (빨리 꺼지는 메아리)','short memory','#lv1','메아리가 하루마다 일정한 비율로 줄어 금방 0이 되는 성질.'),
  ('concept/hurst-exponent','Concept','허스트 지수','Hurst exponent','#lv1','메아리가 얼마나 오래 가는지 나타내는 숫자. 0.5면 기억 없음, 1에 가까울수록 오래 간다.'),
  ('concept/hyperbolic-decay','Concept','나누기로 줄기 (거듭제곱 감쇠)','hyperbolic decay','#lv1','메아리가 날 수의 거듭제곱에 반비례해 줄어드는 모양.'),
  ('method/fractional-differencing','Method','분수 차분','fractional differencing','#lv1','천천히 꺼지는 메아리를 세기 d 하나로 담는 방법. ARFIMA의 핵심.'),
  ('task/long-horizon-forecast','Task','멀리 내다보기 (다음 30일 평균)','long-horizon forecasting','#lv2','하루 뒤가 아니라 여러 날 뒤 또는 여러 날의 평균을 맞히는 문제.'),
  ('concept/mean-reversion','Concept','평소로 돌아가기','mean reversion','#lv2','시간이 지나면 값이 평소 수준 쪽으로 돌아오는 성질.'),
  ('limitation/long-window-needed','Limitation','오래 가는 메아리는 긴 창을 요구한다','long memory needs long windows','#lv2','창 모델로 오래 가는 메아리를 쓰려면 수십 일을 펼쳐야 하고, 세기도 사람이 골라야 한다.'),
  ('sim/1-3-two-echoes','Simulation','두 가지로 줄어드는 메아리','two decay shapes','#lv1'),('sim/1-3-avg30','Simulation','최근 며칠을 볼까','recent-average horizon test','#lv2'),('sim/1-3-duel','Simulation','대결: 어제 하나 vs 20일 창 (강 A)','duel: lag-1 vs 20-day window','#vs')],
 edges=[('concept/short-memory','contrastsWith','concept/long-memory','#lv1'),('concept/hyperbolic-decay','partOf','concept/long-memory','#lv1'),('concept/hurst-exponent','partOf','concept/long-memory','#lv1'),('method/fractional-differencing','solves','concept/long-memory','#lv1'),
  ('concept/long-memory','prerequisiteOf','task/long-horizon-forecast','#lv2'),('concept/mean-reversion','contrastsWith','concept/long-memory','#lv2'),('method/fractional-differencing','hasLimitation','limitation/long-window-needed','#lv2'),('limitation/long-window-needed','raises','question/mem-compress-past','#lv2'),
  ('concept/long-memory','demonstratedBy','sim/1-3-two-echoes','#lv1'),('task/long-horizon-forecast','demonstratedBy','sim/1-3-avg30','#lv2'),('concept/long-memory','demonstratedBy','sim/1-3-duel','#vs')],
 gloss={'메아리':['메아리','이 시리즈의 별명','과거의 값이 오늘 값에 남긴 흔적. 통계 용어로는 자기상관.'],'장기기억':['장기기억 (long memory)','통계','메아리가 천천히 줄어 몇 달이 지나도 남는 기록의 성질. 신경망 LSTM의 이름과는 다른 말이다.'],
  '허스트 지수':['허스트 지수 (H)','통계','메아리가 얼마나 오래 가는지 나타내는 숫자. 0.5면 기억 없음, 1에 가까울수록 오래 간다.'],'분수 차분':['분수 차분','통계 모델','천천히 꺼지는 메아리를 세기 d 하나로 담는 방법.'],'상관':['상관','통계','두 값이 함께 오르내리는 정도. −1에서 +1 사이.'],
  '이론값':['이론값','계산','기록을 만든 규칙에서 수학으로 계산한 값. 실제 기록에서 잰 값과 조금 다를 수 있다.'],'최근 평균':['최근 평균','계산','지난 며칠의 값을 더해 날 수로 나눈 값.'],'평소 평균':['평소 평균','계산','훈련 기록 전체의 평균. 기억을 쓰지 않는 가장 쉬운 짐작.'],
  '검증 오차':['검증 오차','지표','모델이 본 적 없는 검증 기간에서 평균적으로 빗나간 크기.'],'창':['창 (window)','설정값','다음 값을 짐작할 때 펼쳐 놓는 과거 구간.'],'훈련':['훈련 데이터','평가','모델의 숫자를 정하는 데 쓰는 기록.']},
 core=['장기기억','허스트 지수','분수 차분','메아리','최근 평균'],
 quiz={'why':[Q('1-2의 “짧은 기억이면 된다”는 결론이 반쪽인 까닭은?',['계산이 틀려서','메아리가 빨리 꺼지는 기록에서만 맞아서','매출 기록이 너무 짧아서'],1,'메아리가 오래 가는 기록에서는 결론이 뒤집혀요.','기록의 성질을 떠올려 보세요.','concept/long-memory')],
  'lv1':[Q('1 ÷ √k 꼴로 줄어드는 메아리는 100일 뒤에 얼마가 남을까?',['0.5','0.1','0.001'],1,'√100 = 10이니 1 ÷ 10 = 0.1이에요.','100의 제곱근은 10이에요.','concept/hyperbolic-decay','계산'),
        Q('허스트 지수가 0.9인 기록은',['과거와 상관이 없다','메아리가 오래 간다','금방 평소로 돌아온다'],1,'0.5보다 클수록 높은 구간, 낮은 구간이 길게 이어져요.','0.5가 “기억 없음”이에요.','concept/hurst-exponent')],
  'lv2':[Q('기본값 50, 믿는 정도 0.5. 최근 평균이 90cm면 다음 달 평균 짐작값은?',['90cm','95cm','100cm'],1,'50 + 0.5 × 90 = 95cm예요.','곱셈 한 번, 덧셈 한 번.','task/long-horizon-forecast','계산'),
        Q('강 B에서 최근 평균이 별 도움이 안 된 까닭은?',['강 B의 수위가 낮아서','메아리가 금방 꺼져 다음 30일 대부분이 지금과 상관없어서','기록이 짧아서'],1,'메아리가 20일이면 꺼지니 한 달 뒤는 평소 평균이 가장 좋은 답이에요.','메아리가 며칠 가는지 떠올려 보세요.','concept/mean-reversion')],
  'vs':[Q('1-2와 같은 대결인데 승자가 바뀐 까닭은?',['20일 창이 28일 창보다 좋아서','기록의 메아리가 오래 가서 먼 자리에도 쓸 것이 남아서','어제 값이 틀려서'],1,'방법은 같고 기록이 달랐어요.','두 기록의 메아리를 견줘 보세요.','concept/long-memory')]},
)
JS=r'''
var XA=makeLong(2027,2000,0.4,{K:1000}),XB=makeSeries(2027,2000,{weekly:[],phi:0.667,sd:3}),TR=1400,VA=1700,k;
var SA=[0],SB=[0];for(k=1;k<=200;k++){SA.push(acf(XA,k,0,TR));SB.push(acf(XB,k,0,TR));}
function avgCurve(y){var C=[0],i;for(i=0;i<y.length;i++)C.push(C[i]+y[i]);
  var out=[null],T=[],tr=[],va=[];for(var t=100;t+30<=VA;t++){T.push((C[t+30]-C[t])/30);if(t+30<=TR)tr.push(T.length-1);else if(t>=TR)va.push(T.length-1);}
  var mu=C[TR]/TR,g=0;va.forEach(function(i){g+=Math.abs(T[i]-mu);});
  for(var L=1;L<=100;L++){var F=[];for(t=100;t+30<=VA;t++)F.push([(C[t]-C[t-L])/L]);var b=linfit(tr.map(function(i){return F[i];}),tr.map(function(i){return T[i];})),s=0;
    va.forEach(function(i){s+=Math.abs(linpred(b,F[i])-T[i]);});out.push({va:s/va.length,b:b});}
  return {cur:out,glob:g/va.length,mu:mu,C:C};}
var CA=avgCurve(XA),CB=avgCurve(XB),D1=scoreAR(XA,1,TR,VA),D20=scoreAR(XA,20,TR,VA),B1=scoreAR(XB,1,TR,VA),B20=scoreAR(XB,20,TR,VA);
PAGE._T={rho50:rhoLong(0.4,50),rho100:rhoLong(0.4,100),sa50:SA[50],sb50:SB[50],sa10:SA[10],sb10:SB[10],ag:CA.glob,a5:CA.cur[5].va,a20:CA.cur[20].va,a100:CA.cur[100].va,bg:CB.glob,b20:CB.cur[20].va,d1:D1.va,d20:D20.va,b1:B1.va,b20v:B20.va,beta20:CA.cur[20].b};
/* 칸 ① */
var Dd=0.4,SH=false,cv=$('#c1'),cvb=$('#c1b');
function upd1(){var r1=rhoLong(Dd,1);
  kpis($('#k1'),[[f2(Dd,2)+' · H '+f2(Dd+0.5,2),'세기 d · 허스트 지수','a'],[f2(r1,2),'어제와의 상관 (두 강 같음)','i'],[f2(rhoLong(Dd,50),2),'50일 전 — 나누기로 줄기','g'],[f2(Math.pow(r1,50),2),'50일 전 — 곱하기로 줄기','r']]);
  var m=tpl('<p>어제와의 상관은 둘 다 {0}이에요. 그래도 100일 전에 남는 크기는 나누기 쪽이 {1}, 곱하기 쪽이 {2}이에요.</p>',f2(r1,2),f2(rhoLong(Dd,100),2),f2(Math.pow(r1,100),2));
  if(SH)m+=Math.abs(Dd-0.4)<1e-9?tpl('<p class="g">점이 두 강에서 실제로 잰 메아리예요. 10일 전: 강 A {0}, 강 B {1}. 50일 전: 강 A {2}, 강 B {3}. 강 A가 이론 곡선보다 낮은 것은 기록이 유한해서 생기는 차이예요.</p>',f2(SA[10],2),f2(SB[10],2),f2(SA[50],2),f2(SB[50],2)):'<p class="a">두 강은 세기 0.4로 만들었어요. 실제로 잰 점은 슬라이더를 0.40에 놓았을 때만 곡선과 견줄 수 있어요.</p>';
  $('#ins1').innerHTML=m;drawAll();}
bindRange('r1D',function(v){Dd=v;upd1();},function(v){return f2(v,2);});
$('#b1M').addEventListener('click',function(){SH=!SH;this.setAttribute('aria-pressed',SH?'true':'false');upd1();});
addMod(cv,function(){var H=290,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var a=[],b=[],r1=rhoLong(Dd,1),p=1;
  for(var i=1;i<=200;i++){p*=(i-1+Dd)/(i-Dd);a.push(p);b.push(Math.pow(r1,i));}
  var o=plot(ctx,W,H,{x0:1,x1:200,y0:-0.1,y1:0.75,yn:4,yfmt:function(v){return v.toFixed(2);},xticks:[1,20,50,100,150,200],xlab:function(v){return v+'일';},lines:[{d:b,x0:1,color:COL.amber,w:2},{d:a,x0:1,color:COL.gfp,w:2.2}],legend:[['나누기로 줄기 (강 A)',COL.gfp],['곱하기로 줄기 (강 B)',COL.amber]]});
  ctx.strokeStyle='rgba(157,155,184,.4)';ctx.beginPath();ctx.moveTo(o.P.l,o.Y(0));ctx.lineTo(W-o.P.r,o.Y(0));ctx.stroke();
  if(SH){for(i=1;i<=200;i+=(i<20?1:4)){ctx.fillStyle='rgba(94,227,156,.8)';ctx.beginPath();ctx.arc(o.X(i),o.Y(SA[i]),2.3,0,7);ctx.fill();ctx.fillStyle='rgba(241,182,70,.8)';ctx.beginPath();ctx.arc(o.X(i),o.Y(SB[i]),2.3,0,7);ctx.fill();}}
  stamp(ctx,W,'설명용 모형 · 실제 데이터 아님');});
addMod(cvb,function(){var H=260,W=fit(cvb,H),ctx=cvb.getContext('2d');ctx.clearRect(0,0,W,H);var a=XA.slice(1000,1400),b=XB.slice(1000,1400),P={l:44,r:12};
  [[a,COL.gfp,'강 A',20],[b,COL.amber,'강 B',136]].forEach(function(z){var y0=z[3],h=104,X=function(i){return P.l+i/399*(W-P.l-P.r);},Yf=function(v){return y0+(1-(v-80)/40)*h;};
    ctx.strokeStyle='rgba(157,155,184,.35)';ctx.setLineDash([3,3]);ctx.beginPath();ctx.moveTo(P.l,Yf(100));ctx.lineTo(W-P.r,Yf(100));ctx.stroke();ctx.setLineDash([]);
    ctx.strokeStyle=z[1];ctx.lineWidth=1.2;ctx.beginPath();z[0].forEach(function(v,i){i?ctx.lineTo(X(i),Yf(clamp(v,80,120))):ctx.moveTo(X(i),Yf(clamp(v,80,120)));});ctx.stroke();
    txt(ctx,z[2],6,y0+h/2,{size:12,color:z[1],w:'700'});});
  stamp(ctx,W,'설명용 모형 · 실제 데이터 아님');});
/* 칸 ② */
var RV='a',L2=20,cv2=$('#c2'),cv2b=$('#c2b');
function cur(){return RV==='a'?CA:CB;}
function upd2(){var c=cur(),r=c.cur[L2],best=1;for(var i=2;i<=100;i++)if(c.cur[i].va<c.cur[best].va)best=i;var imp=(1-r.va/c.glob)*100;
  kpis($('#k2'),[[f2(c.glob,2),'평소 평균만 쓴 오차 (cm)','r'],[f2(r.va,2),tpl('최근 {0}일 평균을 섞은 오차',L2),'g'],[(imp>=0?'−':'+')+f2(Math.abs(imp),0)+'%','오차 변화',imp>15?'g':'a'],[f2(r.b[1],2),'최근 평균을 믿는 정도','m']]);
  $('#ins2').innerHTML=(RV==='a'?tpl('<p class="g">강 A예요. 최근 {0}일 평균을 {1}만큼 믿으면 오차가 {2}% 줄어요. 가장 낮은 곳은 {3}일 근처예요.</p>',L2,f2(r.b[1],2),f2(imp,0),best):tpl('<p class="a">강 B예요. 최근 평균을 믿는 정도가 {0}뿐이에요. 오차는 {1}% 주는 데 그쳐요. 한 달 뒤는 평소로 돌아가기 때문이에요.</p>',f2(r.b[1],2),f2(imp,0)))+(L2>60&&RV==='a'?'<p class="m">너무 길게 평균을 내면 최근 수준이 무뎌져요. 긴 것이 늘 좋지는 않아요.</p>':'');drawAll();}
toggleGroup('#g2 button',function(v){RV=v;upd2();});bindRange('r2L',function(v){L2=v;upd2();},function(v){return tpl('{0}일',v);});
addMod(cv2,function(){var H=270,W=fit(cv2,H),ctx=cv2.getContext('2d');ctx.clearRect(0,0,W,H);var c=cur(),d=[];for(var i=1;i<=100;i++)d.push(c.cur[i].va);var hi=Math.max(c.glob,Math.max.apply(null,d))*1.08,lo=Math.min.apply(null,d)*0.9;
  var o=plot(ctx,W,H,{x0:1,x1:100,y0:lo,y1:hi,yn:4,yfmt:function(v){return v.toFixed(2);},xticks:[1,5,20,40,60,80,100],xlab:function(v){return v+'일';},lines:[{d:d.map(function(){return c.glob;}),x0:1,color:COL.muted,dash:[5,4],w:1.3},{d:d,x0:1,color:RV==='a'?COL.gfp:COL.amber,w:2.2}],legend:[['최근 평균을 섞음',RV==='a'?COL.gfp:COL.amber],['평소 평균만',COL.muted]],marks:[{x:L2,color:COL.info,label:L2+'일'}]});
  stamp(ctx,W,'설명용 모형 · 실제 데이터 아님');});
addMod(cv2b,function(){var H=190,W=fit(cv2b,H),ctx=cv2b.getContext('2d');ctx.clearRect(0,0,W,H);var y=RV==='a'?XA:XB,c=cur(),t=1500,a=t-150,seg=y.slice(a,t+30),rgv=rangeOf([seg]);
  var o=plot(ctx,W,H,{x0:a,x1:t+29,y0:rgv[0],y1:rgv[1],yn:3,xticks:[a,t-100,t-50,t,t+29],xlab:function(v){return v===t?'오늘':(v<t?(t-v)+'일 전':'30일 뒤');},spans:[{a:t-L2-0.5,b:t-0.5,color:'rgba(241,182,70,.16)'},{a:t-0.5,b:t+29.5,color:'rgba(130,184,255,.10)'}],lines:[{d:seg,x0:a,color:'#c9c7dc',w:1.2}]});
  var act=(c.C[t+30]-c.C[t])/30,pr=linpred(c.cur[L2].b,[(c.C[t]-c.C[t-L2])/L2]);
  [[c.mu,COL.muted,[4,4]],[act,COL.text,[]],[pr,COL.robo,[]]].forEach(function(z){ctx.strokeStyle=z[1];ctx.lineWidth=2;ctx.setLineDash(z[2]);ctx.beginPath();ctx.moveTo(o.X(t-0.5),o.Y(z[0]));ctx.lineTo(o.X(t+29.5),o.Y(z[0]));ctx.stroke();ctx.setLineDash([]);});
  txt(ctx,tpl('실제 평균 {0} · 짐작 {1} · 평소 {2}',f2(act,1),f2(pr,1),f2(c.mu,1)),o.P.l+6,o.P.t+10,{size:11,color:COL.muted});stamp(ctx,W,'설명용 모형 · 실제 데이터 아님');});
/* 대결 */
Duel({el:'#duel',higherIsBetter:false,drawMargin:0.05,fmt:function(v){return f2(v,2);},run:function(){return {fly:D1.va,robo:D20.va,metric:'검증 오차'};},
  say:function(f,b){return tpl('검증 오차는 초파리 쪽 어제 하나가 {0}cm, 주판봇 쪽 20일 창이 {1}cm예요. 차이는 큰 값의 {2}%예요.',f2(f,2),f2(b,2),f2(Math.abs(f-b)/Math.max(f,b)*100,1));},
  lessons:{R:'천천히 꺼지는 메아리에는 긴 기억이 값을 한다. 1-2와 같은 대결인데 기록이 달라 승자가 바뀌었다',D:'오래 가는 메아리도 하루 뒤 예측에서는 큰 차이를 못 냈다',F:'오래 가는 메아리 앞에서도 어제 하나가 버텼다'},
  after:function(){$('#duelNote').innerHTML=tpl('<p>같은 대결을 강 B에서 하면 어제 하나 {0}cm, 20일 창 {1}cm예요. 메아리가 빨리 꺼지는 강에서는 긴 창이 덕을 보지 못해요.</p>',f2(B1.va,2),f2(B20.va,2));}});
/* 정리 */
function row(n,a,b){return '<tr><td>'+n+'</td><td class="num">'+a+'</td><td class="num">'+b+'</td></tr>';}
$('#sumTb').insertAdjacentHTML('beforeend',row('10일 전 메아리 (이론값)',f2(rhoLong(0.4,10),2),f2(Math.pow(rhoLong(0.4,1),10),2))+row('10일 전 메아리 (실제로 잰 값)',f2(SA[10],2),f2(SB[10],2))+row('50일 전 메아리 (이론값)',f2(rhoLong(0.4,50),2),f2(Math.pow(rhoLong(0.4,1),50),2))+row('내일 맞히기 — 어제 하나',f2(D1.va,2),f2(B1.va,2))+row('내일 맞히기 — 20일 창',f2(D20.va,2),f2(B20.va,2))+row('다음 30일 평균 — 평소 평균만',f2(CA.glob,2),f2(CB.glob,2))+row('다음 30일 평균 — 최근 20일 평균을 섞음',f2(CA.cur[20].va,2),f2(CB.cur[20].va,2)));
upd1();upd2();
'''
