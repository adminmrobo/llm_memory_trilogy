# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
from p2_1 import X1C
P=dict(
 title='경험으로 배우는 에이전트 — 가 본 방을 기억하기',chip='미로 앵커',anchor='B',
 q='스스로 움직이는 AI는 자기가 한 일을 기억해야 할까?',
 lead='<p>지금까지의 기억은 남이 한 말을 기억하는 것이었다. 이번에는 <b>자기가 한 일</b>을 기억한다. 스스로 방을 옮겨 다니며 목표를 찾는 AI, 곧 에이전트의 이야기다. 어느 방에 가 봤는지 기억하지 못하면 같은 곳을 맴돈다. 이 페이지에서는 작은 미로로 직접 실험하고, Memorilla 논문이 글로 하는 게임에서 한 실험을 함께 읽는다 [[fallahpour2026memorilla]].</p>',
 objs=['가 본 방을 기억하는 에이전트와 기억하지 않는 에이전트의 성공률 차이를 설명한다','경험 기억(3-1)이 에이전트에게 왜 필요한지 말한다','논문의 에이전트 실험이 보고한 숫자와 그 한계를 구분한다'],mins=18,
 kpis=[('27.5%','방 36개 미로, 50턴, 기억 없는 에이전트의 성공률'),('95.5%','같은 조건, 가 본 방을 기억하는 에이전트'),('18.6% → 24.2%','논문 보고: 글로 하는 게임의 평균 성공률'),('8개','논문의 에이전트 실험이 쓴 기억 토큰')],
 hero=['오늘은 자기가 한 일을 기억하는 이야기예요. 미로를 하나 만들었어요.','방 36개짜리 미로 200개를 준비했어요. 두 에이전트를 50턴씩 걷게 했어요.','50턴이면 넉넉해. 아무 문이나 열다 보면 찾지. 정말 기억이 필요할까?','가 본 방을 다 적어 둬야지! 같은 방을 또 가는 건 낭비야.'],
 first3=['스스로 움직이는 AI가 지나온 길을 기억하면 같은 곳을 맴돌지 않는다. 작은 미로 실험과 논문 실험으로 확인한다.','AI에게 여러 단계의 일을 맡기는 일이 늘고 있다. 그런 AI가 “아까 해 본 것”을 잊으면 같은 실패를 되풀이한다.','AI에게 긴 작업을 맡길 때 “지금까지 해 본 것과 결과”를 적은 기록을 함께 넘기면, 같은 시도를 되풀이하는 일이 준다.'],
 kpinote='앞의 두 숫자는 이 페이지의 <b>설명용 미로</b>에서 계산한 값이고, 뒤의 두 숫자는 논문의 <b>저자 보고값</b>이다. 환경이 달라 나란히 견줄 수 없다.',abbr=['LLM'],cast=dict(fly='기억 없이도 찾는다',robo='가 본 방을 다 적는다',x1='방청석의 누군가 · 오늘은 미로 앞에서 구경',x2='방청석의 누군가',x3='방청석의 누군가',moa='지나온 방을 받아 적는 사람 · 응원'),
 whyh='왜 자기 경험을 기억해야 하나',whytag='방법: 지나온 길을 적어 두고 다음 걸음에 쓰기',prev='3-4 16개 토큰에 담기',
 why=[('말이 아니라 걸음','손님의 말은 한 번 적으면 된다. 에이전트의 경험은 걸음마다 새로 생긴다. 금방 창을 넘는다.'),('맴돌기','지나온 길을 잊으면 이미 막힌 길을 또 간다. 턴은 정해져 있다.'),('경험 기억','3-1의 세 종류 가운데 “그때 이렇게 했더니 이렇게 됐다”가 여기에 쓰인다.')],
 levels=[dict(id='lv1',no='①',title='미로 실험 — 가 본 방을 기억하면',nav='미로 실험',tag1='방법: 방문 기록을 적고 안 가 본 방 먼저 가기',tag2='일상: 주차장에서 내 차 찾기',
  why=('에이전트가 미로의 첫 방에 있다. 어딘가에 목표 방이 있다. 정해진 턴 안에 찾아야 한다. 방마다 이웃 방으로 가는 문만 보인다.','기억이 없으면 문을 아무거나 고른다. 방금 온 방으로 되돌아가기도 하고, 막다른 길을 여러 번 들어간다.','가 본 방을 적어 둔다. 문을 고를 때 안 가 본 방을 먼저 고르고, 없으면 온 길로 되돌아간다. 같은 막다른 길에 두 번 들어가지 않는다.','넓은 주차장에서 차를 찾을 때, 이미 본 줄을 기억하는 사람과 기억하지 못하는 사람의 차이다.'),
  math=dict(ask='성공률은 한 번 해 보고 알 수 있는 게 아니죠?',school='비율이다. 여러 번 해 보고, 성공한 횟수를 전체 횟수로 나눈다.',
   eq='성공률 = 턴 안에 목표를 찾은 판 수 ÷ 전체 판 수 × 100',pieces=[('한 판','미로 하나에서 에이전트 하나가 정해진 턴만큼 걷는 것'),('전체 판 수','이 실험에서는 서로 다른 미로 200개'),('턴','방 하나를 옮기는 한 걸음')],
   num='200판 가운데 55판에서 목표를 찾았다면 55 ÷ 200 × 100 = 27.5%다. 191판에서 찾았다면 95.5%다.',comment='한 판은 운이 좋을 수도 나쁠 수도 있으니까 200판을 해 보고 비율로 말하는 거군요.'),
  pair=('주차장에서 차를 찾는다. 본 줄을 기억하지 못하면 같은 줄을 몇 번이고 다시 걷는다. 본 줄에 표시를 해 두면 남은 줄만 보면 된다. 주차장이 넓을수록 차이가 커진다.','기억하는 에이전트가 쓰는 것은 “가 본 방 목록”과 “온 길” 둘뿐이다. 대단한 지능이 아니다. 그런데도 같은 턴 안에 찾는 비율이 크게 달라진다. 에이전트에게 기억은 똑똑함보다 먼저 필요한 것이다.'),
  talk=[('doc','front','방 36개 미로에서 50턴을 줘요. 기억 없이 아무 문이나 여는 에이전트는 200판 가운데 몇 판을 성공할까요?'),('fly','arms','50턴이면 방 수보다 많잖아. 절반은 넘게 찾겠지. 정말 그럴까?'),('robo','chart','“한 판 보기”를 눌러 봐! 왼쪽 에이전트가 어디를 맴도는지.')],
  panel='<div class="panel"><h3>실험 — 두 에이전트의 미로 찾기</h3><div class="ctrl">'+tg('g1','미로 크기',[('6','방 36개'),('5','방 25개'),('8','방 64개')])+rg('r1T','턴 제한',20,100,50,5)+'<div class="group"><button class="bt primary" type="button" id="b1P">▶ 한 판 보기</button><button class="bt" type="button" id="b1N">다른 미로</button></div></div><div class="kpis" id="k1"></div>'+cv('c1','같은 미로 두 개가 나란히 있다. 왼쪽은 기억 없는 에이전트, 오른쪽은 가 본 방을 기억하는 에이전트의 걸음이 그려진다. 여러 번 지나간 방일수록 진하다')+'<div class="insight" id="ins1" aria-live="polite"></div></div>',
  report='보고드려요. 방 36개, 50턴에서 기억 없는 에이전트는 200판 가운데 27.5%, 기억하는 에이전트는 95.5%를 성공했어요. 방을 64개로 늘리면 11.5% 대 65.5%예요.',
  stepsh='왜 이렇게 벌어지나',steps=['기억 없는 에이전트는 방금 온 방으로 되돌아가는 일이 잦다. 걸음의 많은 부분이 제자리걸음이다.','막다른 길에 들어갔다 나와도, 거기가 막다른 길이었다는 것을 모른다. 또 들어간다.','기억하는 에이전트는 걸음마다 새 방을 연다. 막힌 길은 한 번만 간다.','미로가 클수록, 턴이 빠듯할수록 차이가 커진다.'],
  lim='이 미로의 에이전트는 규칙대로 움직이는 장난감이다. 실제 에이전트는 방 이름과 물건 설명 같은 글을 읽고 다음 행동을 글로 정한다. 지나온 일이 쌓이면 그 기록이 창을 넘는다. 다음 칸에서 그런 환경의 실험을 읽는다.',
  concepts=['concept/agent','concept/experience-memory','concept/visited-set','concept/revisiting'],
  code=[('visited.add(room)','지금 방을 가 본 방 목록에 넣는다'),('unvisited = [n for n in doors if n not in visited]','문 너머 방 가운데 안 가 본 방만 고른다')],codenote='기억하는 에이전트의 규칙을 보인 예다.'),
 dict(id='lv2',no='②',kind='논문',title='논문의 실험 — 글로 하는 게임에서',nav='논문의 실험',tc='m',tag1='논문: TextWorld 환경, 기억 토큰 8개',tag2='일상: 방 탈출 게임',
  why=('글로 하는 게임(TextWorld)이 있다 [[cote2018textworld]]. 에이전트는 방 설명을 글로 읽고 행동을 글로 적는다. 여러 방을 다니며 물건을 찾아 목표를 이뤄야 한다.','지나온 일을 전부 창에 넣는 방식이 기준선이다. 기록은 걸음마다 길어진다. 넣어 준다고 다 쓰이지도 않는다(2-2).','논문은 지나온 기록 전체를 기억 토큰 8개로 줄여, 기록과 함께 넣었다. 그리고 그 기억 장치를 게임의 성공·실패를 신호로 학습시켰다.','방 탈출 게임에서 지나온 방과 써 본 열쇠를 한 줄 메모로 정리해 가며 푸는 것이다.'),
  math=dict(ask='18.6%에서 24.2%가 되면 얼마나 좋아진 거예요?',school='뺄셈과 나눗셈이다. 차이를 구하고, 그 차이가 처음 값의 몇 %인지 본다.',
   eq='늘어난 폭 = 뒤 값 − 앞 값 &nbsp;·&nbsp; 늘어난 비율 = 늘어난 폭 ÷ 앞 값 × 100',pieces=[('%p (퍼센트포인트)','두 퍼센트 값의 차이'),('늘어난 비율','처음 값을 기준으로 얼마나 늘었는지')],
   num='24.2 − 18.6 = 5.6이다. 5.6%p 늘었다. 5.6 ÷ 18.6 × 100 = 약 30%다. 처음 성공률의 30%쯤이 더해진 셈이다. 그래도 네 판 가운데 세 판은 여전히 실패다.',comment='30% 좋아졌다고 하면 커 보이는데, 성공률 자체는 24.2%네요. 두 숫자를 같이 봐야겠어요.'),
  pair=('방 탈출 게임을 여럿이 한다. 지나온 방과 써 본 것을 전부 외워서 말하는 팀과, 한 줄 메모로 추려 가며 하는 팀이 있다. 방이 많아질수록 전부 외우는 쪽은 헷갈리기 시작한다.','논문이 보고한 설정은 이렇다. 에이전트는 가중치를 고정한 Qwen3-4B, 방은 최대 65개, 턴 제한은 50, 기억 토큰은 8개다. 기준선은 지나온 기록 전체를 넣은 것이고, 비교 대상은 거기에 기억 토큰 8개를 더한 것이다. 학습하지 않은 기억 장치를 붙이면 오히려 기준선보다 낮았다고 한다.'),
  talk=[('doc','think','논문의 숫자를 볼게요. 기억 토큰 8개를 더하니 성공률이 얼마나 달라졌을까요?'),('robo','happy','미로 실험처럼 27%에서 95%쯤 됐겠지!'),('fly','point','막대를 봐. 그렇게까지는 아니야. 그리고 뭐가 다른지 설정도 읽어 봐.')],
  panel='<div class="panel"><h3>논문이 보고한 숫자 (저자 보고값)</h3>'+cv('c2','세 가지 지표마다 두 막대. 지나온 기록만 넣은 것과 기억 토큰 8개를 더한 것. 세 지표 모두 기억을 더한 쪽이 높다')+'<div class="tw"><table class="tb"><tr><th>지표</th><th>지나온 기록 전체만</th><th>+ 기억 토큰 8개</th></tr><tr><td>평균 성공률</td><td class="num">18.6%</td><td class="num">24.2%</td></tr><tr><td>3회 시도 안에 완료</td><td class="num">25.0%</td><td class="num">37.5%</td></tr><tr><td>턴 제한 전에 끝난 판</td><td class="num">29%</td><td class="num">42%</td></tr></table></div><div class="insight"><p>세 지표 모두 기억 토큰을 더한 쪽이 높게 보고됐다. 연구진은 지나온 방을 되풀이해 찾는 일이 줄었다고 풀이한다.</p><p>미로 실험(27.5% → 95.5%)과 폭이 크게 다르다. 미로는 규칙이 단순한 장난감이고, 논문은 글을 읽고 물건을 다루는 훨씬 어려운 환경이다. 두 숫자를 나란히 견줄 수 없다.</p></div></div><div class="bridge field"><h4>출발점이 된 소개 글과 다르게 쓴 곳</h4><p>소개 글 [[papanubo2026memorilla]]에는 이 실험의 기억 토큰 수와 에이전트 모델이 따로 적혀 있지 않아, 앞의 실험과 같은 16개·Qwen3-8B로 읽히기 쉽다. 이 페이지에서는 프로젝트 페이지를 따라 <b>기억 토큰 8개, Qwen3-4B</b>로 쓴다. 성공률 숫자(18.6%, 24.2%, 25.0%, 37.5%, 29%, 42%)는 두 곳이 같다.</p><p class="lim">확인 필요 · arXiv 원문(2610.21375)과의 직접 대조는 하지 못했다.</p></div>',
  report='보고드려요. 논문 보고값은 평균 성공률 18.6%에서 24.2%, 3회 시도 안 완료 25.0%에서 37.5%, 턴 제한 전 종료 29%에서 42%예요. 늘어난 폭은 5.6%p예요.',
  stepsh='숫자를 읽는 법',steps=['방향: 세 지표 모두 기억을 더한 쪽이 높다.','크기: 평균 성공률은 5.6%p 올랐다. 올라도 24.2%다.','조건: 게임 한 묶음, 최대 50턴, 한 계열의 모델에서 잰 값이다. 저자도 여러 환경이나 오랜 기간의 쓰임은 아직 보이지 못했다고 밝힌다.','출처: 저자가 보고한 값이다. 다른 사람이 다시 재 본 값이 아니다.'],
  lim='에이전트의 기억은 이제 막 재기 시작한 영역이다. 한 환경, 50턴까지의 결과다. 며칠, 몇 달에 걸친 일에서 어떻게 될지는 아직 모른다. 3-6에서 시리즈 전체를 정리하며 “어디까지 기억할 수 있을까”에 답해 본다.',
  intern=SIA,concepts=['concept/textworld','concept/memory-token','limitation/single-environment'])],
 duel=dict(title='기억 없이 vs 가 본 방 기억하기 — 방 36개, 50턴',metric='성공률',tag='일상: 맴돌기 vs 표시하며 찾기',q='방 36개짜리 미로 200개. 턴 제한은 50이다. 아무 문이나 여는 에이전트와 가 본 방을 기억하는 에이전트 가운데 누가 더 자주 목표를 찾을까?',
  fly=('기억 없이 아무 문이나 연다 — 들고 다니는 것 없음','50턴이면 방 수보다 많아. 돌아다니다 보면 찾아.'),robo=('가 본 방과 온 길을 적어 둔다','적어 두면 같은 방을 또 안 가. 턴이 아깝잖아!'),rule='200판의 성공률(높을수록 좋음). 이 페이지에서 직접 돌린 미로 실험이다.'),
 sumh='정리 — 경험을 기억한다는 것',
 sum='<div class="tw"><table class="tb" id="sumTb"><tr><th>미로 크기 · 턴 제한</th><th>기억 없는 에이전트</th><th>가 본 방을 기억하는 에이전트</th></tr></table></div><p style="font-size:14px;color:var(--muted)">표의 숫자는 이 페이지를 열 때 브라우저가 미로 200개씩을 직접 돌려 계산한 값이다.</p>'+steps3([('맴돌지 않으려면','스스로 움직이는 AI에게는 지나온 길의 기억이 먼저 필요하다.'),('경험은 금방 쌓인다','걸음마다 기록이 생긴다. 전부 넣으면 창을 넘고, 넣어도 다 쓰이지 않는다.'),('아직 초입이다','논문의 결과는 한 환경, 50턴까지다. 방향은 보였지만 크기는 작고, 다시 확인되지 않았다.')])+field('AI에게 여러 단계의 일을 맡길 때 “지금까지 한 일, 결과, 실패한 시도”를 적은 작업 기록을 함께 준다. 중간에 새 대화로 넘어갈 때는 그 기록부터 넘긴다. 같은 실패를 되풀이하는 일이 준다.','미로의 “가 본 방 목록”은 틀릴 일이 없는 단순한 기록이다. 실제 작업 기록은 무엇을 적을지(3-1), 낡은 것을 어떻게 할지(3-3)가 함께 따라온다.'),
 outro=[('doc','front','오늘의 한 줄이에요. 스스로 움직이려면 먼저 자기가 지나온 길을 기억해야 해요.'),('asst','smile','가 본 방 목록이라는 단순한 메모 하나로 27.5%가 95.5%가 되는 게 놀라웠어요.'),('fly','coffee','졌어. 아무 문이나 여는 건 맴돌 뿐이더군. 그래도 논문의 24.2%는 아직 갈 길이 멀다는 뜻이지.'),('robo','happy','기억의 승리! …논문 쪽은 5.6%p였지. 큰 숫자는 아니야. 그래도 시작이잖아.'),('moa','report','에이전트가 지나온 방은 제가 걸음마다 받아 적었어요. 다음 편에서 시리즈 기록을 전부 꺼내 올게요.')],
 examples=['미로: 가로세로 같은 칸 수의 방을 무작위로 이어 만든 설명용 미로다. 두 방 사이의 길이 하나뿐인(고리가 없는) 구조이고, 미로마다 시드가 다르다. 출발은 왼쪽 위 방, 목표는 무작위 방이다','기억 없는 에이전트: 이웃 방 가운데 하나를 같은 가능성으로 고른다. 기억하는 에이전트: 안 가 본 이웃 방을 먼저 가고, 없으면 온 길로 한 칸 되돌아간다','성공률은 서로 다른 미로 200개에서 잰 값이다. 시드가 고정돼 있어 열 때마다 같은 값이 나온다','논문 수치(18.6%, 24.2%, 25.0%, 37.5%, 29%, 42%)와 설정(Qwen3-4B, 최대 65개 방, 50턴, 기억 토큰 8개)은 프로젝트 페이지의 저자 보고값이다. 이 페이지의 미로 실험과는 환경이 전혀 다르다'],
 refs=['fallahpour2026memorilla','cote2018textworld','papanubo2026memorilla','langmem2026concepts'],
 claims=[('claim/textworld-result','TextWorld에서 지나온 기록 전체만 넣은 에이전트의 평균 성공률 18.6%가 기억 토큰을 더하자 24.2%로 보고됐다','#lv2','fallahpour2026memorilla','프로젝트 페이지 TextWorld 실험','concept/textworld'),
  ('claim/textworld-setup','TextWorld 실험은 가중치를 고정한 Qwen3-4B 에이전트, 최대 65개 방, 50턴 제한, 기억 토큰 8개로 이루어졌다','#lv2','fallahpour2026memorilla','프로젝트 페이지 TextWorld 실험','concept/memory-token'),
  ('claim/textworld-limit','저자는 단일 게임 묶음과 최대 50턴이라는 조건 때문에 여러 환경이나 장기 사용은 아직 입증되지 않았다고 밝힌다','#lv2','fallahpour2026memorilla','프로젝트 페이지 한계','limitation/single-environment'),
  ('claim/episodic-examples','일화 기억은 성공한 상호작용을 본보기로 보존한다','#why','langmem2026concepts','메모리 유형 절','concept/experience-memory')],
 openq=[('question/mem-long-horizon-agents','며칠, 몇 달에 걸쳐 일하는 에이전트의 기억은 어떻게 재고 어떻게 돌볼까?','#lv2','아직 열린 질문')],
 nodes=[('concept/agent','Concept','에이전트','agent','#lv1','스스로 다음 행동을 정하며 여러 단계의 일을 해 나가는 AI.'),
  ('concept/experience-memory','Concept','경험 기억','experience memory','#lv1','자기가 한 행동과 그 결과를 적어 두고 다음 행동에 쓰는 기억.'),
  ('concept/visited-set','Concept','가 본 방 목록','visited set','#lv1','지나온 곳을 적어 둔 가장 단순한 경험 기억.'),
  ('concept/revisiting','Concept','맴돌기','revisiting','#lv1','지나온 곳을 기억하지 못해 같은 곳을 되풀이해 가는 것.'),
  ('concept/textworld','Concept','글로 하는 게임 (TextWorld)','TextWorld','#lv2','방 설명을 글로 읽고 행동을 글로 적어 목표를 이루는 게임 환경.'),
  ('concept/memory-token','Concept','기억 토큰','memory token','#lv2','글이 아니라 모델의 입력 자리에 바로 넣는 숫자 묶음.'),
  ('limitation/single-environment','Limitation','한 환경, 50턴까지의 결과','single environment, short horizon','#lv2','논문의 에이전트 실험은 게임 한 묶음과 최대 50턴에서만 이루어졌다.'),
  ('sim/3-5-maze','Simulation','두 에이전트의 미로 찾기','maze with and without memory','#lv1'),('sim/3-5-paper','Simulation','논문이 보고한 숫자','reported TextWorld results','#lv2'),('sim/3-5-duel','Simulation','대결: 기억 없이 vs 가 본 방 기억하기','duel: memoryless vs visited memory','#vs')],
 edges=[('concept/experience-memory','partOf','concept/agent','#lv1'),('concept/visited-set','broader','concept/experience-memory','#lv1'),('concept/experience-memory','solves','concept/revisiting','#lv1'),('concept/memory-token','partOf','concept/textworld','#lv2',),
  ('concept/textworld','hasLimitation','limitation/single-environment','#lv2'),('limitation/single-environment','raises','question/mem-long-horizon-agents','#lv2'),
  ('concept/revisiting','demonstratedBy','sim/3-5-maze','#lv1'),('concept/textworld','demonstratedBy','sim/3-5-paper','#lv2'),('concept/experience-memory','demonstratedBy','sim/3-5-duel','#vs')],
 gloss={'에이전트':['에이전트','생성 AI','스스로 다음 행동을 정하며 여러 단계의 일을 해 나가는 AI.'],'턴':['턴','쓰임','에이전트의 한 걸음. 이 미로에서는 방 하나를 옮기는 것.'],'성공률':['성공률','지표','정해진 턴 안에 목표를 찾은 판의 비율.'],'기억 토큰':['기억 토큰','논문 용어','글이 아니라 모델의 입력 자리에 바로 넣는 숫자 묶음.'],
  '경험 기억':['경험 기억 (일화 기억)','기억의 종류','자기가 한 행동과 그 결과를 적어 두고 다음에 쓰는 기억.'],'저자 보고값':['저자 보고값','읽는 법','논문을 쓴 연구진이 직접 재서 발표한 숫자.'],'퍼센트포인트':['퍼센트포인트 (%p)','계산','두 퍼센트 값의 차이.'],'미로':['미로','설명용 모형','방들을 문으로 이은 장난감 환경.']},
 core=['에이전트','성공률','경험 기억','기억 토큰'],
 quiz={'why':[Q('에이전트의 경험이 손님의 말보다 다루기 어려운 까닭은?',['글자가 작아서','걸음마다 새로 생겨 금방 쌓여서','비밀이라서'],1,'기록이 걸음마다 길어져요.','“말이 아니라 걸음”을 떠올려 보세요.','concept/experience-memory')],
  'lv1':[Q('200판 가운데 131판을 성공했다. 성공률은?',['13.1%','65.5%','131%'],1,'131 ÷ 200 × 100 = 65.5%예요.','성공한 판을 전체 판으로 나눠요.','concept/agent','계산'),
        Q('기억 없는 에이전트가 턴을 낭비하는 가장 큰 까닭은?',['걸음이 느려서','방금 온 방이나 막다른 길을 되풀이해 가서','미로가 어두워서'],1,'어디를 가 봤는지 모르니까요.','“맴돌기”를 떠올려 보세요.','concept/revisiting')],
  'lv2':[Q('성공률이 20%에서 25%가 됐다. 몇 %p 늘었고, 처음 값의 몇 %가 늘었나?',['5%p, 25%','5%p, 5%','25%p, 5%'],0,'25 − 20 = 5%p, 5 ÷ 20 × 100 = 25%예요.','차이를 구한 뒤 처음 값으로 나눠요.','concept/textworld','계산'),
        Q('논문의 에이전트 실험이 쓴 기억 토큰은 몇 개일까?',['8개','16개','512개'],0,'프로젝트 페이지에 따르면 8개예요. 문서 시험의 16개와 달라요.','“다르게 쓴 곳” 상자를 다시 보세요.','concept/memory-token')],
  'vs':[Q('미로 실험의 차이(27.5% → 95.5%)와 논문의 차이(18.6% → 24.2%)를 나란히 견주면 안 되는 까닭은?',['환경과 에이전트가 전혀 달라서','논문이 틀려서','미로가 더 어려워서'],0,'미로는 규칙이 단순한 장난감이고, 논문은 글을 읽고 물건을 다루는 환경이에요.','두 실험의 설정을 떠올려 보세요.','limitation/single-environment')]},
)
JS=r'''
var GG=6,TT=50,SEED=1010,cv=$('#c1'),MZ,RA,RB,ST,step=0,playing=false;
function setup(){MZ=makeMaze(SEED,GG);RA=runAgent(MZ,TT,false,5000+SEED-1000);RB=runAgent(MZ,TT,true,9000+SEED-1000);step=REDUCE?TT:0;playing=false;$('#b1P').textContent='▶ 한 판 보기';}
function stats(){ST=mazeStats(GG,TT,200);}
function upd1(){kpis($('#k1'),[[GG*GG+'개 · '+TT+'턴','방 수 · 턴 제한','i'],[f2(ST.none,1)+'%','기억 없는 에이전트 성공률 (200판)','r'],[f2(ST.mem,1)+'%','가 본 방을 기억하는 에이전트','g'],[f2(ST.mem-ST.none,1)+'%p','차이','a']]);
  function res(r,n){return r.turns>0?tpl('{0}: {1}턴 만에 찾음',n,r.turns):tpl('{0}: {1}턴 안에 못 찾음',n,TT);}
  var da=uniq(RA.path),db=uniq(RB.path);
  $('#ins1').innerHTML=tpl('<p>지금 보이는 미로에서 — {0} (서로 다른 방 {1}개를 감) · {2} (서로 다른 방 {3}개를 감)</p>',res(RA,'기억 없음'),da,res(RB,'기억함'),db)+'<p>200판 전체의 성공률은 위 숫자예요. 미로 크기와 턴 제한을 바꾸면 다시 계산해요.</p>';drawAll();}
function uniq(p){var s={};p.forEach(function(v){s[v]=1;});return Object.keys(s).length;}
toggleGroup('#g1 button',function(v){GG=+v;setup();stats();upd1();});bindRange('r1T',function(v){TT=v;if(MZ){setup();stats();upd1();}},function(v){return v+'턴';});
$('#b1P').addEventListener('click',function(){if(step>=TT)step=0;playing=!playing;this.textContent=playing?'❚❚ 멈춤':'▶ 한 판 보기';});
$('#b1N').addEventListener('click',function(){SEED=1000+((SEED-1000+7)%200);setup();upd1();});
var acc=0;addMod(cv,function(dt){var H=Math.min(330,cv.clientWidth*0.52+40),W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);
  if(playing&&!REDUCE){acc+=dt;if(acc>0.09){acc=0;step++;if(step>=TT){step=TT;playing=false;$('#b1P').textContent='▶ 다시 보기';}}}
  var gap=24,side=Math.min((W-gap-16)/2,H-44),cs=side/GG;
  [[RA,'기억 없음',COL.fly,8],[RB,'가 본 방을 기억함',COL.robo,8+side+gap]].forEach(function(z){var r=z[0],x0=z[3],y0=30,cnt={},n=Math.min(step,r.path.length-1),i;for(i=0;i<=n;i++)cnt[r.path[i]]=(cnt[r.path[i]]||0)+1;
    txt(ctx,z[1]+(r.turns>0&&n>=r.turns?' — 찾음!':''),x0,16,{size:12,color:z[2],w:'700'});
    for(i=0;i<GG*GG;i++){var cx=x0+(i%GG)*cs,cy=y0+Math.floor(i/GG)*cs,c=cnt[i]||0;rr(ctx,cx+2,cy+2,cs-4,cs-4,4,c?'rgba('+(z[2]===COL.fly?'239,91,91':'87,208,220')+','+Math.min(0.85,0.18+c*0.14)+')':'rgba(37,40,58,.8)','rgba(70,72,96,.6)');
      if(i===MZ.goal)txt(ctx,'★',cx+cs/2,cy+cs/2,{size:Math.max(10,cs*0.5),color:COL.amber,align:'center'});}
    ctx.strokeStyle='rgba(157,155,184,.55)';ctx.lineWidth=Math.max(2,cs*0.12);MZ.adj.forEach(function(nb,a){nb.forEach(function(b){if(b>a){ctx.beginPath();ctx.moveTo(x0+(a%GG+0.5)*cs,y0+(Math.floor(a/GG)+0.5)*cs);ctx.lineTo(x0+(b%GG+0.5)*cs,y0+(Math.floor(b/GG)+0.5)*cs);ctx.stroke();}});});
    var cur=r.path[n];ctx.fillStyle=COL.text;ctx.beginPath();ctx.arc(x0+(cur%GG+0.5)*cs,y0+(Math.floor(cur/GG)+0.5)*cs,Math.max(3,cs*0.2),0,7);ctx.fill();});
  txt(ctx,tpl('{0} / {1}턴 · ★ = 목표 · 진할수록 여러 번 간 방',Math.min(step,TT),TT),8,H-8,{size:10,color:COL.muted});stamp(ctx,W,'설명용 모형');});
setup();stats();PAGE._T={s6:mazeStats(6,50,200),s8:mazeStats(8,50,200),s5:mazeStats(5,50,200)};
/* 칸 ② */
var cv2=$('#c2'),PB=[['평균 성공률',18.6,24.2],['3회 시도 안에 완료',25.0,37.5],['턴 제한 전에 끝난 판',29,42]];
addMod(cv2,function(){var H=230,W=fit(cv2,H),ctx=cv2.getContext('2d');ctx.clearRect(0,0,W,H);var x0=Math.min(190,W*0.34),bw=W-x0-70;
  PB.forEach(function(z,i){var y=34+i*62;txt(ctx,z[0],8,y+20,{size:12,color:COL.text,w:'700'});rr(ctx,x0,y,z[1]/50*bw,20,5,'rgba(157,155,184,.6)');txt(ctx,z[1]+'%',x0+z[1]/50*bw+8,y+10,{size:12,color:COL.muted});
    rr(ctx,x0,y+24,z[2]/50*bw,20,5,'rgba(94,227,156,.8)');txt(ctx,z[2]+'%',x0+z[2]/50*bw+8,y+34,{size:12,color:COL.gfp,w:'700'});});
  txt(ctx,'회색 = 지나온 기록 전체만 · 초록 = 기억 토큰 8개를 더함',8,14,{size:10,color:COL.muted});stamp(ctx,W,'논문 보고값 · 저자 보고');});
/* 대결 */
Duel({el:'#duel',higherIsBetter:true,drawMargin:0.05,fmt:function(v){return f2(v,1)+'%';},run:function(){var s=mazeStats(6,50,200);return {fly:s.none,robo:s.mem,metric:'성공률'};},
  say:function(f,b){return tpl('200판의 성공률은 초파리 쪽 기억 없는 에이전트가 {0}%, 주판봇 쪽 기억하는 에이전트가 {1}%예요.',f2(f,1),f2(b,1));},
  lessons:{R:'지나온 길을 적어 두는 것만으로 맴돌기가 사라진다. 움직이는 AI에게 기억은 먼저 갖춰야 할 것이다',D:'기억이 있으나 없으나 비슷했다',F:'기억 없이도 충분했다'},
  after:function(r){var s=mazeStats(6,50,200);$('#duelNote').innerHTML=tpl('<p>성공한 판만 보면 기억 없는 쪽은 평균 {0}턴, 기억하는 쪽은 평균 {1}턴에 찾았어요. 기억 없는 쪽이 성공한 판은 목표가 가까이 있던 판이에요.</p><p>이 대결은 이 페이지에서 직접 돌린 미로 실험이에요. 논문의 실험과는 다른 환경이에요.</p>',f2(s.tn,1),f2(s.tm,1));}});
$('#sumTb').insertAdjacentHTML('beforeend',[[5,50],[6,30],[6,50],[6,100],[8,50],[8,100]].map(function(a){var s=mazeStats(a[0],a[1],200);return '<tr><td>방 '+a[0]*a[0]+'개 · '+a[1]+'턴</td><td class="num">'+f2(s.none,1)+'%</td><td class="num">'+f2(s.mem,1)+'%</td></tr>';}).join(''));
upd1();
'''
