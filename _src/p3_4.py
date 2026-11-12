# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
from p2_1 import X1C
P=dict(
 title='16개 토큰에 담기 — Memorilla 논문 읽기',chip='논문 해설',anchor='B',
 q='서랍 전체를 읽고 나서, 질문에 필요한 것만 열여섯 칸에 담아 넘길 수 있을까?',
 lead='<p>지금까지의 기억은 글이었다. 요약도 쪽지도 글 그대로 창에 넣었다. 2026년 10월에 나온 Memorilla 논문은 다른 길을 낸다 [[fallahpour2026memorilla]]. 질문이 오면 서랍 전체를 훑고, 그 질문에 필요한 것만 <b>기억 토큰 16개</b>에 담아 모델에 넘긴다. 글이 아니라 모델이 바로 읽는 숫자 묶음이다. 2부에서 “조각”이라 부른 것의 본래 이름이 토큰이다. 이 페이지에서는 논문의 말을 따라 토큰이라 쓴다. 이 페이지에서는 논문이 무엇을 했고, 무엇을 보고했고, 무엇을 아직 못 했는지를 읽는다.</p><p style="font-size:14px;color:var(--muted)">이 페이지의 논문 수치는 연구진의 프로젝트 페이지에서 그대로 옮긴 저자 보고값이다. arXiv 원문과 직접 대조하지는 못했다. 이 시리즈의 출발점이 된 한국어 소개 글 [[papanubo2026memorilla]]과 다른 곳은 따로 밝힌다.</p>',
 objs=['Memorilla가 요약(2-4), 꺼내 읽기(2-5)와 다른 점 두 가지를 말한다','논문이 보고한 성적표에서 앞선 시험과 뒤진 시험을 구분한다','이 방식의 한계 세 가지를 든다'],mins=22,
 kpis=[('16개','모델에 넘기는 기억 토큰'),('5 / 8','비교 대상 가운데 가장 높았던 시험 (저자 보고)'),('약 4,212배','NarrativeQA에서 줄인 문서 토큰 (67,385 → 16)'),('3 / 8','다른 방법이 더 높았던 시험')],
 hero=['오늘은 논문 한 편을 읽어요. 기억을 글이 아닌 꼴로 넘기는 시도예요. 숫자는 저자가 보고한 그대로 읽을게요.','시험 여덟 개의 성적표를 빠짐없이 옮겨 왔어요. 앞선 것도 뒤진 것도요.','열여섯 칸에 서랍 전체를? 줄이면 세부가 빠지는 건 2-4에서 봤잖아. 정말 될까?','67,385조각을 16개로! 4,212배야. 이건 무조건 이긴 거지!'],
 first3=['질문이 올 때마다 저장해 둔 문서 전체를 훑어, 그 질문에 필요한 것만 16개의 숫자 묶음(기억 토큰)에 담아 모델에 넘기는 연구다.','요약의 “질문을 모르고 줄인다”와 꺼내 읽기의 “몇 장만 골라 본다”를 함께 넘어서려는 시도라서, 앞으로의 AI 기억이 갈 수 있는 방향 하나를 보여 준다.','아직 연구 단계다. 저자가 직접 밝힌 한계가 있고, 정확한 이름이나 숫자가 중요한 일에는 원문을 찾아 읽는 방식이 여전히 낫다.'],
 kpinote='이 숫자들은 연구진이 발표한 <b>저자 보고값</b>이다. 이 페이지에서 다시 실험한 값이 아니다.',abbr=['LLM','RAG','QA'],cast=dict(fly='원문을 다 넣는 쪽을 믿는다',robo='새 방식을 믿는다',**X1C),
 whyh='왜 이 논문을 읽나',whytag='논문: Memorilla — Latent Semantic Memory for LLMs',prev='3-3 낡은 기억 돌보기',
 why=[('요약의 한계','2-4의 요약은 질문이 오기 전에 줄였다. 무엇이 중요한지 모르는 채로 줄였다.'),('꺼내 읽기의 한계','2-5는 가장 가까운 몇 장만 골라 글로 넣었다. 답이 여러 장에 흩어져 있으면 놓치고, 넣을 글이 늘었다.'),('이 논문의 생각','질문을 본 뒤에 줄이고, 몇 장이 아니라 전체를 훑고, 글이 아니라 고정된 수의 기억 토큰으로 넘긴다.')],
 levels=[dict(id='lv1',no='①',kind='방법',title='구조 — 열여섯 칸이 서랍 전체를 읽는다',nav='구조',tag1='논문: 질문 조건부 기억 토큰',tag2='일상: 질문을 듣고 서류함 전체를 훑어 쪽지 열여섯 장으로 추리는 비서',
  why=('모델은 손대지 않고(가중치를 그대로 두고) 바깥에 쌓인 기록을 쓰게 하고 싶다. 기록은 계속 늘어난다.','전부 넣으면 비싸다. 요약은 질문을 모르고 줄인다. 꺼내 읽기는 가까운 몇 장만 보고, 장 수만큼 창을 차지한다.','문서마다 좌표(임베딩)를 한 번만 만들어 저장해 둔다. 질문이 오면 “기억 칸” 16개가 질문을 먼저 읽고, 저장된 좌표 전체를 살펴 필요한 것을 모은다. 그 16칸을 모델이 읽을 수 있는 꼴로 바꿔 질문과 함께 넣는다. 배우는 것은 이 기억 장치뿐이고, 모델과 좌표 만드는 장치는 그대로 둔다.','손님의 질문을 들은 비서가 서류함 전체를 훑고, 그 질문에 답하는 데 필요한 것만 쪽지 열여섯 장으로 추려 건네는 것이다. 서류함이 아무리 커져도 건네는 쪽지는 열여섯 장이다.'),
  math=dict(ask='4,212배 줄였다는 건 어떻게 나온 숫자예요?',school='나눗셈이다. 원래 넣던 양을 줄인 뒤의 양으로 나눈다.',
   eq='줄인 배수 = 전부 넣을 때의 문서 토큰 ÷ 기억 토큰 수',pieces=[('전부 넣을 때의 문서 토큰','NarrativeQA 시험에서 67,385개 (저자 보고)'),('기억 토큰 수','16개'),('배수','클수록 많이 줄인 것')],
   num='67,385 ÷ 16 = 4,211.6이다. 반올림해서 약 4,212배다. 꺼내 읽기로 50장을 넣는 방식(RAG-50)은 같은 시험에서 3,612개를 썼다. 3,612 ÷ 16 = 약 226배다.',comment='같은 시험에서 전부 넣기는 67,385개, 50장 꺼내 읽기는 3,612개, 이 방식은 16개군요.'),
  pair=('비서는 서류를 받을 때마다 한 줄짜리 색인 카드를 만들어 둔다. 손님이 물으면 색인 카드 전체를 훑고, 답에 필요한 것만 쪽지 열여섯 장에 옮겨 적어 사장에게 건넨다. 사장은 서류함을 직접 열지 않는다.','네 가지 요구에서 출발한 설계다. ① 저장된 전체를 살핀다. ② 질문에 따라 꺼내는 것이 달라진다. ③ 저장소가 커져도 넘기는 토큰 수가 같다. ④ 문서의 좌표는 한 번만 만들어 다시 쓴다. 1부의 말로 하면 “질문을 보고 그때그때 쓰는 메모 열여섯 칸”이다.'),
  talk=[('doc','front','네 단계를 차례로 볼게요. 단계 단추를 누르면서 무엇이 움직이는지 보세요.'),('fly','arms','글로 안 넣고 숫자 묶음으로 넣는다고? 모델이 그걸 읽을 수 있어?'),('robo','chart','4단계를 눌러 봐! 열여섯 칸을 모델의 입력 자리에 맞게 바꿔 끼우는 거야.')],
  panel='<div class="panel"><h3>실험 — 네 단계 따라가기</h3><div class="ctrl">'+tg('g1','단계',[('1','① 칸 준비'),('2','② 질문 읽기'),('3','③ 전체 살피기'),('4','④ 모델에 넘기기')])+tg('g1Q','질문',[('a','질문 가'),('b','질문 나')])+'</div>'+cv('c1','왼쪽에 저장된 문서들이 점으로, 가운데에 기억 칸 16개, 오른쪽에 모델이 놓인 그림. 단계에 따라 칸이 켜지고, 칸에서 문서들로 굵기가 다른 선이 이어진다')+'<div class="insight" id="ins1" aria-live="polite"></div><h3>논문이 보고한 줄인 배수</h3><div class="tw"><table class="tb"><tr><th>시험</th><th>전부 넣기 대비 줄인 문서 토큰</th><th>메모</th></tr><tr><td>NarrativeQA</td><td class="num">약 4,212배</td><td>67,385 → 16. 가장 크게 줄인 시험</td></tr><tr><td>PersonaMem-v2</td><td class="num">1,974배</td><td>개인화 시험</td></tr><tr><td>TriviaQA</td><td class="num">743배</td><td></td></tr><tr><td>FactKG</td><td class="num">108배</td><td></td></tr><tr><td>여러 시험의 기하평균</td><td class="num">394배</td><td>RAG-50 대비로는 113배</td></tr></table></div>'+note('모두 저자 보고값이다. 처리 시간은 문서 512개, H100 그래픽카드 한 장에서 전부 넣기 19.9초, Memorilla 0.74초(약 27배)로 보고됐다. 꺼내 읽기 방식의 처리 시간은 재지 않았다.')+'</div>',
  report='보고드려요. 논문 수치를 옮겼어요. NarrativeQA에서 전부 넣기는 문서 토큰 67,385개, RAG-50은 3,612개, Memorilla는 16개예요. 여러 시험의 기하평균으로는 전부 넣기보다 394배 적어요.',
  stepsh='네 단계',steps=['칸 준비: 기억 칸 16개를 서로 다른 값으로 시작한다. 칸마다 다른 것을 담게 하려는 것이다.','질문 읽기: 16칸이 질문의 좌표를 살펴, 지금 무엇을 찾아야 하는지 반영한다.','전체 살피기: 16칸이 저장된 모든 문서의 좌표를 여러 번 살핀다. 몇 장만 고르지 않고 전체에서 모은다.','모델에 넘기기: 16칸을 모델의 입력 자리에 맞는 크기로 바꿔, 질문 글 앞에 붙인다. 모델은 평소처럼 읽는다.'],
  lim='그림의 선 굵기는 구조를 보이려고 지어낸 도식이다. 실제로 어느 칸이 어느 문서를 얼마나 보는지는 학습으로 정해진다. 그리고 구조가 그럴듯하다고 성적이 좋은 것은 아니다. 다음 칸에서 성적표를 읽는다.',
  concepts=['method/memorilla','concept/memory-token','concept/query-conditioned-memory','concept/frozen-llm','concept/embedding'],
  bridges=[('gen','1부·2부와 이으면','1-4의 메모는 줄여 담되 늘 같은 방식으로 줄였다. 1-5의 메모장은 무엇을 남길지 배웠지만 칸 수가 정해져 있었다. Memorilla의 16칸은 “질문을 본 뒤에, 전체를 보고, 그때그때 쓰는 메모”다. 2-4의 요약이 가진 “질문을 모르고 줄인다”는 한계를 겨눈다.','닮은 것은 “정해진 칸 수에 줄여 담는다”는 생각이다. 1부의 메모는 시간 순서대로 읽으며 고쳐 쓰고, Memorilla의 칸은 저장된 전체를 한꺼번에 살핀다. 만드는 방법은 다르다.')]),
 dict(id='lv2',no='②',kind='결과',title='성적표 — 앞선 다섯, 뒤진 셋',nav='성적표',tc='m',tag1='논문: 시험 8개, 같은 모델(Qwen3-8B)로 비교',tag2='일상: 과목마다 다른 등수',
  why=('새 방식이 정말 나은지 알고 싶다. 논문은 시험 여덟 개에서 여러 방식과 견줬다. 모든 방식이 같은 모델(Qwen3-8B)로 답하게 했다.','“16개로 전부 넣기를 이겼다”는 한 줄만 읽으면 전부 이긴 것처럼 들린다. 실제 성적표는 그렇지 않다.','여덟 시험 전부를 놓고 세 가지를 견준다. 전부 넣기, 다른 방식 가운데 가장 높았던 것, Memorilla. 앞선 시험과 뒤진 시험을 가른다.','전교 1등도 과목마다 등수가 다르다. 평균만 보지 않고 과목별 성적표를 편다.'),
  math=dict(ask='평균 49.68은 어떻게 나온 거예요? 시험마다 채점 방식이 다르잖아요.',school='평균이다. 여덟 점수를 더해 8로 나눈다.',
   eq='평균 = 여덟 시험 점수의 합 ÷ 8',pieces=[('여덟 시험 점수','정확도, 문장 겹침 점수 등 시험마다 재는 것이 다르다'),('평균','서로 다른 잣대의 점수를 그냥 더한 것. 크게 보는 용도로만 쓴다')],
   num='Memorilla의 여덟 점수를 더하면 44.60 + 66.65 + 59.00 + 84.33 + 19.31 + 57.00 + 18.15 + 48.37 = 397.41이다. 8로 나누면 49.68이다. 전부 넣기는 같은 식으로 45.37이다.',comment='평균은 4점쯤 높네요. 그런데 잣대가 다른 점수를 더한 거라, 과목별로도 봐야겠어요.'),
  pair=('성적표를 받으면 평균부터 보게 된다. 하지만 평균이 높아도 어떤 과목은 반에서 중간이다. 그 과목이 내게 중요한 과목일 수 있다.','Memorilla는 비교한 방식들 가운데 다섯 시험에서 가장 높았다. 나머지 셋에서는 다른 방식이 더 높았다. 특히 짧은 의학 문서를 읽고 답하는 PubMedQA에서는 전부 넣기(67.00)보다 낮은 59.00이었다. 원문을 그대로 읽는 쪽이 나은 경우가 있다는 뜻이다.'),
  talk=[('doc','think','여덟 시험을 하나씩 넘겨 볼게요. Memorilla가 가장 높지 않은 시험이 있을까요?'),('robo','happy','16개로 4,212배를 줄였는데! 전부 1등이지.'),('fly','point','시험 번호를 3번에 놓아 봐. PubMedQA.')],
  panel='<div class="panel"><h3>실험 — 시험별 성적 (저자 보고값)</h3><div class="ctrl">'+rg('r2B','시험 번호',1,8,1)+'</div><div class="kpis" id="k2"></div>'+cv('c2','고른 시험에서 전부 넣기, 다른 방식 가운데 최고, Memorilla 세 막대를 나란히 그린 그림')+'<div class="insight" id="ins2" aria-live="polite"></div><div class="tw"><table class="tb" id="t2"><tr><th>#</th><th>시험 (재는 것)</th><th>전부 넣기</th><th>다른 방식 가운데 최고</th><th>Memorilla</th><th>가장 높은 쪽</th></tr></table></div>'+note('모든 값은 프로젝트 페이지에 실린 저자 보고값이다. PersonaMem-v2와 PersonalizationV4는 그 시험에 맞춘 추가 학습을 거쳤다고 한다.')+'</div>',
  report='보고드려요. Memorilla가 가장 높은 시험은 PersonaMem-v2, FactKG, TriviaQA, LaMP-4, LaMP-7 다섯 개예요. PersonalizationV4와 NarrativeQA는 MemoRAG가, PubMedQA는 LLMLingua-2가 더 높았어요.',
  stepsh='성적표에서 읽을 것',steps=['앞선 곳: 여러 문서를 맞춰 봐야 하는 문제, 손님의 취향처럼 대화 곳곳에 흩어진 것을 묻는 문제.','뒤진 곳: 짧은 문서에 답이 그대로 적혀 있는 문제. 원문을 직접 읽는 쪽이 낫다.','저자가 밝힌 한계 ①: 정확한 이름 같은 세밀한 정보를 잃을 수 있다.','저자가 밝힌 한계 ②: 모델마다 기억 장치를 따로 학습시켜야 하고, 모델 내부에 직접 넣어야 해서 가중치가 공개된 모델이어야 한다. 한계 ③: 한 계열의 모델과 글에서만 시험했다.'],
  lim='이 성적표는 문서를 읽고 답하는 시험들이다. 스스로 움직이며 겪은 일을 기억해야 하는 경우는 어떨까? 3-5에서 같은 논문의 에이전트 실험과, 직접 만든 작은 미로 실험을 본다.',
  extra='<div class="bridge field"><h4>출발점이 된 소개 글과 다르게 쓴 곳</h4><p>① 소개 글의 성적 표에는 다섯 시험만 실려 있다. 이 페이지에서는 여덟 시험을 모두 싣는다. ② 소개 글에는 에이전트 실험의 기억 토큰 수가 따로 적혀 있지 않다. 프로젝트 페이지에 따르면 그 실험은 8개를 썼다. 3-5에서는 8개로 쓴다. ③ 학습하는 숫자 수(1억 9,412만 3,776개)와 3단계 학습(위키백과 바꿔 쓰기 198만 건 → 여러 과제 134만 건 → 시험별 학습 자료)은 소개 글의 값을 옮겼고 원문에서 확인하지 못했다.</p><p class="lim">확인 필요 · arXiv 원문(2610.21375)과의 직접 대조는 하지 못했다.</p></div>',
  intern=SIA,concepts=['concept/benchmark-reading','limitation/detail-loss','limitation/per-model-training'])],
 duel=dict(title='전부 넣기 vs 16개 토큰 — 저자 보고 성적표에서 몇 번 앞섰나',metric='앞선 시험 수',tag='논문: 저자 보고 성적표',q='논문의 여덟 시험에서 “문서를 전부 넣기”와 “Memorilla의 16개 토큰”을 일대일로 견준다. 어느 쪽이 더 많은 시험에서 앞섰을까?',
  fly=('문서를 전부 넣는 쪽','줄이면 빠져. 원문을 다 읽은 쪽이 여덟 번 다 이길 거야.'),robo=('기억 토큰 16개로 넘기는 쪽','4,212배 줄이고도 이긴다니까! 여덟 번 다 내 거야.'),rule='여덟 시험 가운데 상대보다 점수가 높았던 시험의 수(많을수록 좋음). 저자가 보고한 숫자를 세는 것이다. 이 페이지에서 직접 실험한 결과가 아니다.'),
 sumh='정리 — 논문 한 편에서 가져갈 것',
 sum=steps3([('세 가지를 바꿨다','질문을 본 뒤에 줄인다. 몇 장이 아니라 전체를 살핀다. 글이 아니라 고정된 수의 기억 토큰으로 넘긴다.'),('성적은 엇갈린다','여덟 시험 가운데 다섯에서 가장 높았고 셋에서는 아니었다. 답이 원문에 그대로 있는 문제는 원문을 읽는 쪽이 낫다.'),('대신할 것이 아니라 섞을 것','저자도 꺼내 읽기와 섞는 것을 다음 과제로 든다. 2-6의 섞어 쓰기에 층이 하나 더 생기는 셈이다.')])+field('당장 업무에 쓸 수 있는 도구가 아니라 연구 결과다. 가져갈 것은 물음이다. 우리 일의 질문은 “문서 한 곳에 답이 적혀 있는” 종류인가, “여러 곳을 맞춰 봐야 하는” 종류인가? 앞의 것이면 찾아 읽기가, 뒤의 것이면 줄여 모으기가 맞다.','이 페이지는 논문을 요약해 옮긴 것이다. 성적의 좋고 나쁨을 이 페이지에서 따로 검증하지 않았다. 수치는 저자가 정한 조건(같은 모델, 같은 시험)에서의 값이다.'),
 outro=[('doc','front','오늘의 한 줄이에요. 기억을 글이 아닌 꼴로 넘기는 길이 열리고 있어요. 다만 성적표는 끝까지, 뒤진 과목까지 읽어야 해요.'),('asst','smile','평균만 봤으면 전부 이긴 줄 알았을 거예요. PubMedQA를 넘겨 본 게 도움이 됐어요.'),('fly','coffee','일곱 번 졌군. 인정해. 그래도 내가 이긴 한 번이 “원문에 답이 그대로 있는 문제”라는 건 기억해 둬.'),('robo','happy','일곱 대 하나! …하지만 셋은 다른 방법이 1등이었지. 다 이긴 건 아니야. 섞어 쓰는 게 답이겠어.'),('moa','report','논문 수치는 출처와 읽은 날짜를 함께 적어 뒀어요. 원문 확인이 남았다는 표시도요.')],
 examples=['논문 수치(점수, 배수, 처리 시간)는 모두 연구진 프로젝트 페이지 memory.stanford.edu에 실린 저자 보고값을 2026-11-12에 옮긴 것이다. 이 페이지에서 다시 실험하지 않았다','“네 단계 따라가기” 그림의 문서 점, 칸, 선 굵기는 구조를 설명하려고 지어낸 도식이다. 실제 모델의 값이 아니다','전부 넣기의 여덟 시험 평균 45.37은 보고된 여덟 점수를 이 페이지에서 더해 8로 나눈 값이다','학습하는 숫자 수와 3단계 학습의 자료 수는 한국어 소개 글에서 옮겼고 원문 확인이 필요하다'],
 refs=['fallahpour2026memorilla','papanubo2026memorilla','lewis2020retrieval'],
 claims=[('claim/memorilla-design','Memorilla는 저장된 문서 전체에서 질문에 따라 달라지는 고정 개수의 기억 토큰을 만들어 가중치를 고정한 LLM에 넘긴다','#lv1','fallahpour2026memorilla','프로젝트 페이지 개요','method/memorilla'),
  ('claim/memorilla-5of8','Memorilla는 16개 기억 토큰으로 8개 시험 가운데 5개에서 비교 방식들보다 높은 점수를 보고했다','#lv2','fallahpour2026memorilla','프로젝트 페이지 성적표','concept/benchmark-reading'),
  ('claim/memorilla-token-ratio','NarrativeQA에서 전부 넣기 대비 약 4,212배 적은 문서 토큰(67,385 → 16)을 쓴 것으로 보고됐다','#lv1','fallahpour2026memorilla','프로젝트 페이지 토큰 절감','concept/memory-token'),
  ('claim/memorilla-limits','저자는 세밀한 정보 손실, 모델별 학습 필요, 한 모델 계열에서만 시험한 점을 한계로 든다','#lv2','fallahpour2026memorilla','프로젝트 페이지 한계','limitation/detail-loss'),
  ('claim/blog-five-rows','한국어 소개 글의 성적 표에는 8개 시험 가운데 5개가 실려 있다','#lv2','papanubo2026memorilla','5-1절 표','concept/benchmark-reading')],
 openq=[('question/mem-agent-experience','스스로 움직이는 에이전트는 자기가 겪은 일을 어떻게 기억할까?','#lv2','3-5에서 다룬다'),('question/memorilla-arxiv-check','프로젝트 페이지의 수치는 arXiv 원문과 일치하는가?','#lv2','확인 필요')],
 nodes=[('method/memorilla','Method','Memorilla','Memorilla','#lv1','저장된 문서 전체에서 질문에 필요한 것을 고정된 수의 기억 토큰으로 모아 모델에 넘기는 기억 장치.'),
  ('concept/memory-token','Concept','기억 토큰','memory token','#lv1','글이 아니라 모델의 입력 자리에 바로 넣는 숫자 묶음. Memorilla는 16개를 쓴다.'),
  ('concept/query-conditioned-memory','Concept','질문을 보고 만드는 기억','query-conditioned memory','#lv1','질문이 온 뒤에 그 질문에 맞게 꺼내어 줄이는 기억. 질문을 모르고 미리 줄이는 요약과 다르다.'),
  ('concept/frozen-llm','Concept','손대지 않는 모델','frozen LLM','#lv1','가중치를 바꾸지 않고 그대로 쓰는 모델.'),
  ('concept/embedding','Concept','글의 좌표 (임베딩)','embedding','#lv1','글 하나를 나타내는 숫자 묶음.'),
  ('concept/benchmark-reading','Concept','성적표 끝까지 읽기','reading the full benchmark table','#lv2','평균이나 대표 수치만 보지 않고 시험별로 앞선 곳과 뒤진 곳을 가르는 읽기.'),
  ('limitation/detail-loss','Limitation','줄이면 세밀한 정보를 잃을 수 있다','loss of fine detail','#lv2','고정된 수의 기억 토큰에 담는 과정에서 정확한 이름 같은 세부가 빠질 수 있다.'),
  ('limitation/per-model-training','Limitation','모델마다 따로 학습해야 한다','needs per-model training','#lv2','기억 장치를 쓰려는 모델마다 따로 학습시켜야 하고, 가중치가 공개된 모델이어야 한다.'),
  ('sim/3-4-steps','Simulation','네 단계 따라가기','four-step walkthrough','#lv1'),('sim/3-4-table','Simulation','시험별 성적','per-benchmark scores','#lv2'),('sim/3-4-duel','Simulation','대결: 전부 넣기 vs 16개 토큰','duel: full context vs 16 tokens','#vs')],
 edges=[('concept/memory-token','partOf','method/memorilla','#lv1'),('concept/query-conditioned-memory','partOf','method/memorilla','#lv1'),('concept/frozen-llm','prerequisiteOf','method/memorilla','#lv1'),('concept/embedding','prerequisiteOf','method/memorilla','#lv1'),
  ('method/memorilla','hasLimitation','limitation/detail-loss','#lv2'),('method/memorilla','hasLimitation','limitation/per-model-training','#lv2'),('method/memorilla','raises','question/mem-agent-experience','#lv2'),('concept/benchmark-reading','raises','question/memorilla-arxiv-check','#lv2'),
  ('method/memorilla','demonstratedBy','sim/3-4-steps','#lv1'),('concept/benchmark-reading','demonstratedBy','sim/3-4-table','#lv2'),('concept/benchmark-reading','demonstratedBy','sim/3-4-duel','#vs')],
 gloss={'기억 토큰':['기억 토큰','논문 용어','글이 아니라 모델의 입력 자리에 바로 넣는 숫자 묶음. Memorilla는 16개를 쓴다.'],'좌표':['좌표 (임베딩)','모델','글 하나를 나타내는 숫자 묶음. 뜻이 비슷한 글은 가까이 놓인다.'],'임베딩':['임베딩','모델','글 하나를 나타내는 숫자 묶음(좌표).'],'전부 넣기':['전부 넣기 (전체 문맥)','비교 방식','문서를 줄이지 않고 통째로 창에 넣는 방식.'],
  'RAG-50':['RAG-50','비교 방식','질문과 가까운 문서 50개를 찾아 글로 넣는 꺼내 읽기 방식.'],'저자 보고값':['저자 보고값','읽는 법','논문을 쓴 연구진이 직접 재서 발표한 숫자. 다른 사람이 다시 확인한 값이 아니다.'],'가중치':['가중치','모델','모델 속 숫자. 이 논문에서는 바꾸지 않고 그대로 둔다.'],'기하평균':['기하평균','계산','배수들을 곱해서 평균 내는 방법. 배수가 크게 다를 때 쓴다.']},
 core=['기억 토큰','전부 넣기','저자 보고값','좌표'],
 quiz={'why':[Q('Memorilla가 2-4의 요약과 다른 점은?',['질문을 본 뒤에 줄인다','글자를 더 작게 쓴다','요약을 두 번 한다'],0,'요약은 질문이 오기 전에 줄였어요.','줄이는 시점을 견줘 보세요.','concept/query-conditioned-memory')],
  'lv1':[Q('문서 토큰 3,200개를 기억 토큰 16개로 바꾸면 몇 배 줄어든 것일까?',['20배','200배','2,000배'],1,'3,200 ÷ 16 = 200배예요.','나눗셈 한 번이에요.','concept/memory-token','계산'),
        Q('이 방식에서 학습으로 바뀌는 것은?',['대화 모델의 가중치','기억 장치','문서의 내용'],1,'모델과 좌표 만드는 장치는 그대로 두고 기억 장치만 배워요.','“손대지 않는 모델”을 떠올려 보세요.','concept/frozen-llm')],
  'lv2':[Q('논문이 보고한 8개 시험 가운데 Memorilla가 비교 방식들보다 가장 높았던 것은 몇 개일까?',['8개 전부','5개','1개'],1,'다섯 개예요. 나머지 셋은 다른 방식이 더 높았어요.','성적표의 마지막 열을 세어 보세요.','concept/benchmark-reading'),
        Q('PubMedQA처럼 짧은 문서에 답이 그대로 있는 시험에서 Memorilla가 뒤진 까닭으로 알맞은 것은?',['문서가 너무 많아서','줄이는 과정에서 세부가 빠질 수 있고, 원문을 직접 읽는 쪽이 유리해서','모델이 달라서'],1,'저자도 세밀한 정보 손실을 한계로 들어요.','“저자가 밝힌 한계 ①”을 떠올려 보세요.','limitation/detail-loss')],
  'vs':[Q('이 대결의 숫자를 읽을 때 꼭 붙여야 할 말은?',['이 페이지에서 직접 실험했다','저자가 보고한 값을 센 것이다','모든 모델에서 그렇다'],1,'다시 확인된 값이 아니에요. 한 계열의 모델에서 잰 값이기도 해요.','대결 규칙을 다시 보세요.','concept/benchmark-reading')]},
)
JS=r'''
/* 논문 보고값 (프로젝트 페이지, 2026-11-12 읽음) */
var BM=[['PersonaMem-v2','정확도',27.92,'xRAG',30.90,44.60],['PersonalizationV4','정확도',59.12,'MemoRAG',67.88,66.65],['PubMedQA','정확도',67.00,'LLMLingua-2',69.00,59.00],['FactKG','정확도',80.43,'전부 넣기',80.43,84.33],
  ['NarrativeQA','ROUGE-L',17.99,'MemoRAG',20.51,19.31],['TriviaQA','완전 일치',52.60,'MemoRAG',56.60,57.00],['LaMP-4','ROUGE-L',14.21,'xRAG',16.10,18.15],['LaMP-7','ROUGE-L',43.71,'xRAG',46.84,48.37]];
var avgF=BM.reduce(function(a,b){return a+b[2];},0)/8,avgM=BM.reduce(function(a,b){return a+b[5];},0)/8,top=BM.filter(function(b){return b[5]>b[4]&&b[5]>b[2];}).length,vsF=BM.filter(function(b){return b[5]>b[2];}).length;
PAGE._T={avgF:avgF,avgM:avgM,top:top,vsF:vsF,ratio:67385/16,rag:3612/16};
/* 칸 ① */
var ST=1,QQ='a',cv=$('#c1'),R=rng(31),DOCS=[];for(var i=0;i<60;i++)DOCS.push({x:R(),y:R(),a:R(),b:R()});
var STMSG={1:'<p>기억 칸 16개를 준비해요. 칸마다 시작 값이 달라요. 아직 질문도 문서도 보지 않았어요.</p>',2:'<p class="a">16칸이 질문을 읽었어요. 칸의 색이 질문에 따라 달라져요. 질문 가와 질문 나를 바꿔 보세요.</p>',3:'<p class="g">16칸이 저장된 문서 전체를 살펴요. 몇 장만 고르지 않아요. 굵은 선이 많이 참고한 문서예요. 질문을 바꾸면 굵은 선이 다른 문서로 옮겨 가요.</p>',4:'<p class="g">16칸을 모델의 입력 자리에 맞는 크기로 바꿔 질문 앞에 붙였어요. 모델은 문서를 한 장도 직접 읽지 않고, 16칸과 질문만 읽어요.</p>'};
function upd1(){$('#ins1').innerHTML=STMSG[ST];drawAll();}
toggleGroup('#g1 button',function(v){ST=+v;upd1();});toggleGroup('#g1Q button',function(v){QQ=v;upd1();});
addMod(cv,function(){var H=270,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var dx0=14,dx1=W*0.42,sx=W*0.58,mx=W*0.76,r2=rng(QQ==='a'?5:9);
  function dp(d){return [dx0+d.x*(dx1-dx0),34+d.y*(H-70)];}function sp(k){return [sx,40+k*(H-80)/15];}
  if(ST>=3){for(var k=0;k<16;k++){var s=sp(k);DOCS.forEach(function(d,j){var w=Math.pow(QQ==='a'?d.a:d.b,5)*r2();if(w>0.12){var p=dp(d);ctx.strokeStyle='rgba(94,227,156,'+Math.min(0.7,w)+')';ctx.lineWidth=0.5+w*2.4;ctx.beginPath();ctx.moveTo(p[0],p[1]);ctx.lineTo(s[0],s[1]);ctx.stroke();}});}}
  DOCS.forEach(function(d){var p=dp(d),hot=ST>=3&&Math.pow(QQ==='a'?d.a:d.b,5)>0.35;ctx.fillStyle=hot?COL.gfp:'rgba(157,155,184,.55)';ctx.beginPath();ctx.arc(p[0],p[1],hot?4:2.6,0,7);ctx.fill();});
  for(k=0;k<16;k++){s=sp(k);ctx.fillStyle=ST===1?'rgba(157,155,184,.5)':(QQ==='a'?'rgba(241,182,70,.9)':'rgba(130,184,255,.9)');rr(ctx,s[0]-9,s[1]-5,18,10,3,ctx.fillStyle);}
  rr(ctx,mx,70,W-mx-12,H-140,12,'rgba(37,40,58,.95)',ST===4?COL.doc:'rgba(90,92,116,.6)');txt(ctx,'모델',mx+(W-mx-12)/2,H/2-8,{size:13,color:ST===4?COL.doc:'#6f7396',align:'center',w:'700'});txt(ctx,'(가중치 그대로)',mx+(W-mx-12)/2,H/2+10,{size:10,color:COL.muted,align:'center'});
  if(ST===4){ctx.strokeStyle=COL.amber;ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(sx+12,H/2);ctx.lineTo(mx,H/2);ctx.stroke();}
  txt(ctx,'저장된 문서의 좌표 (전체)',dx0,16,{size:11,color:COL.muted});txt(ctx,'기억 칸 16개',sx,16,{size:11,color:COL.muted,align:'center'});
  if(ST>=2)txt(ctx,QQ==='a'?'질문 가':'질문 나',sx,H-10,{size:11,color:QQ==='a'?COL.amber:COL.info,align:'center',w:'700'});stamp(ctx,W,'설명용 도식 · 실제 값 아님');});
/* 칸 ② */
var BI=0,cv2=$('#c2');
function who(b){return b[5]>b[4]&&b[5]>b[2]?'Memorilla':(b[4]>=b[2]?b[3]:'전부 넣기');}
function upd2(){var b=BM[BI],w=who(b);
  kpis($('#k2'),[[b[0],b[1],'i'],[f2(b[2],2),'전부 넣기','a'],[f2(b[4],2),'다른 방식 가운데 최고 ('+b[3]+')','m'],[f2(b[5],2),'Memorilla',w==='Memorilla'?'g':'r']]);
  $('#ins2').innerHTML=w==='Memorilla'?tpl('<p class="g">{0}에서는 Memorilla가 가장 높아요. 전부 넣기보다 {1}점, 다른 방식 가운데 최고보다 {2}점 높아요.</p>',b[0],f2(b[5]-b[2],2),f2(b[5]-b[4],2)):tpl('<p class="r">{0}에서는 {1} 쪽이 더 높아요. Memorilla는 {2}, {1}는 {3}이에요.{4}</p>',b[0],b[3],f2(b[5],2),f2(b[4],2),b[5]<b[2]?' 전부 넣기('+f2(b[2],2)+')보다도 낮아요.':'');drawAll();}
bindRange('r2B',function(v){BI=v-1;upd2();},function(v){return v+'번';});
addMod(cv2,function(){var H=200,W=fit(cv2,H),ctx=cv2.getContext('2d');ctx.clearRect(0,0,W,H);var b=BM[BI],mx=Math.max(b[2],b[4],b[5])*1.15,x0=Math.min(210,W*0.38),bw=W-x0-80;
  [['전부 넣기',b[2],'rgba(157,155,184,.7)'],['다른 방식 최고 ('+b[3]+')',b[4],'rgba(130,184,255,.7)'],['Memorilla (16개 토큰)',b[5],'rgba(94,227,156,.8)']].forEach(function(z,i){var y=40+i*48;txt(ctx,z[0],8,y+14,{size:12,color:COL.text});rr(ctx,x0,y,z[1]/mx*bw,28,6,z[2]);txt(ctx,f2(z[1],2),x0+z[1]/mx*bw+8,y+14,{size:13,color:COL.text,w:'700'});});
  txt(ctx,b[0]+' · '+b[1]+' (높을수록 좋음)',8,16,{size:11,color:COL.muted});stamp(ctx,W,'논문 보고값 · 저자 보고');});
$('#t2').insertAdjacentHTML('beforeend',BM.map(function(b,i){var w=who(b);return '<tr><td class="num">'+(i+1)+'</td><td>'+b[0]+' ('+b[1]+')</td><td class="num">'+f2(b[2],2)+'</td><td class="num">'+f2(b[4],2)+' ('+b[3]+')</td><td class="num">'+f2(b[5],2)+'</td><td>'+(w==='Memorilla'?'<b>Memorilla</b>':w)+'</td></tr>';}).join('')+'<tr><td></td><td>여덟 시험 평균</td><td class="num">'+f2(avgF,2)+'</td><td class="num">—</td><td class="num">'+f2(avgM,2)+'</td><td></td></tr>');
/* 대결 */
Duel({el:'#duel',higherIsBetter:true,drawMargin:0.05,fmt:function(v){return v+'개';},run:function(){return {fly:8-vsF,robo:vsF,metric:'앞선 시험 수'};},
  say:function(f,b){return tpl('여덟 시험 가운데 전부 넣기가 앞선 것은 {0}개, 16개 토큰이 앞선 것은 {1}개예요. 전부 넣기가 앞선 시험은 PubMedQA예요. 저자 보고값을 센 숫자예요.',f,b);},
  lessons:{R:'보고된 성적표에서는 16개 토큰이 전부 넣기를 대부분 앞섰다. 다만 저자 보고값이고, 한 계열의 모델에서 잰 값이다',D:'보고된 성적표에서 둘이 비슷했다',F:'보고된 성적표에서 전부 넣기가 앞섰다'},
  after:function(){$('#duelNote').innerHTML=tpl('<p>전부 넣기가 아니라 “비교한 모든 방식”과 견주면 Memorilla가 가장 높은 시험은 {0}개예요. 셋은 다른 방식이 1등이에요.</p><p>이 판정은 논문이 보고한 숫자를 그대로 센 것이에요. 이 페이지에서 다시 실험하지 않았어요.</p>',top);}});
upd1();upd2();
'''
