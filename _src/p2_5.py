# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
from p2_1 import X1C
P=dict(
 title='꺼내 읽기 — 버리지 않고 두었다가 필요할 때 찾아오기',chip='쪽지 서랍 앵커',
 q='한 달 치 기록에서 지금 필요한 한 장을 어떻게 찾을까?',
 lead='<p>2-4의 요약은 질문이 오기 전에 미리 줄였다. 이번에는 순서를 바꾼다. 원문을 버리지 않고 바깥 서랍에 <b>쪽지</b>로 넣어 둔다. 질문이 오면 그 질문에 맞는 쪽지만 찾아 창에 넣는다. 꺼내 읽기, 영어 약어로 RAG라 부르는 방식이다 [[lewis2020retrieval]]. 성패는 한 가지에 달렸다. 맞는 쪽지를 찾아내는가.</p>',
 objs=['꺼내 읽기의 세 단계(넣어 두기 · 찾기 · 창에 넣기)를 말한다','낱말로 찾기가 놓치는 질문과, 뜻으로 찾기가 그것을 잡는 까닭을 설명한다','같은 주제의 낡은 쪽지와 새 쪽지가 함께 나올 때의 문제를 든다'],mins=20,
 kpis=[('12장','서랍에 넣어 둔 쪽지'),('60조각','요청 하나에 읽는 글 (질문 + 쪽지 한 장)'),('0 / 10','다른 말로 물었을 때 낱말로 찾기'),('10 / 10','다른 말로 물었을 때 뜻으로 찾기')],
 hero=['오늘은 꺼내 읽기예요. 원문은 서랍에 두고, 질문이 오면 맞는 쪽지만 꺼내요.','손님이 한 중요한 말 열두 가지를 날짜와 함께 쪽지로 넣어 뒀어요.','같은 낱말이 든 쪽지를 찾으면 되지. 간단한 게 좋아. …돌려 물으면 어쩌지?','뜻으로 찾아야지! 낱말이 달라도 같은 얘기면 찾아내는 큰 장치를 쓰자.'],
 first3=['대화 원문을 바깥 서랍에 두고, 질문이 올 때마다 관련된 쪽지만 찾아 창에 넣는 방식이다.','창은 작게 유지하면서 한 달 전의 정확한 원문을 쓸 수 있다. 다만 못 찾으면 없는 것과 같다.','사내 문서 검색형 AI가 엉뚱한 답을 할 때는 모델보다 “찾기”가 틀린 경우가 많다. 무엇을 찾아왔는지부터 본다.'],
 abbr=['RAG','LLM'],cast=dict(fly='같은 낱말로 찾는다',robo='뜻으로 찾는다',**X1C),
 whyh='왜 꺼내 읽나',whytag='방법: 넣어 두기 → 찾기 → 창에 넣기',prev='2-4 대화 압축',
 why=[('요약은 원문을 버렸다','빠진 세부는 되찾을 수 없었다. 무슨 질문이 올지 모르고 줄였기 때문이다.'),('전부 넣기는 비쌌다','3,600조각을 요청마다 읽었다. 그 가운데 질문 하나에 필요한 것은 한두 문장이다.'),('질문을 보고 고른다','원문을 두고, 질문이 온 뒤에 필요한 것만 고른다. 고르는 일이 곧 찾기다.')],
 levels=[dict(id='lv1',no='①',title='낱말로 찾기 — 같은 말이 든 쪽지 꺼내기',nav='낱말로 찾기',tag1='방법: 질문과 겹치는 낱말이 있는 쪽지 고르기',tag2='일상: 서류함에서 제목으로 찾기',
  why=('손님이 묻는다. “거래처 이름이 뭐였죠?” 답은 6일에 한 말에 있다. 창에는 최근 며칠 치만 있다.','요약에는 거래처 이름이 빠졌을 수 있다. 원문 전부를 넣기에는 창이 작다.','손님의 중요한 말을 날짜와 함께 쪽지로 서랍에 넣어 둔다. 질문이 오면 질문과 같은 낱말이 든 쪽지를 찾는다. 찾은 쪽지를 질문과 함께 창에 넣는다.','서류함에서 “거래처”라고 적힌 서류철을 찾아 책상에 올려놓는 것이다.'),
  math=dict(ask='“겹치는 낱말”은 어떻게 세요?',school='두 묶음에 함께 든 것을 세는 집합의 교집합이다.',
   eq='겹침 수 = 질문의 낱말과 쪽지의 낱말에 함께 있는 것의 수',pieces=[('질문의 낱말','질문에서 뜻을 가진 낱말들'),('쪽지의 낱말','쪽지에 적힌 낱말들'),('겹침 수가 1 이상','찾았다. 그 쪽지를 창에 넣는다'),('겹침 수가 0','못 찾았다. 쪽지가 서랍에 있어도 꺼내지 못한다')],
   num='질문 “거래처 이름이 뭐였죠?”의 낱말은 {거래처, 이름}이다. 쪽지 “거래처는 초록상사예요”의 낱말은 {거래처, 초록상사}다. 함께 든 것은 “거래처” 하나, 겹침 수 1이다. 찾았다. 질문이 “견적서를 어디로 보내죠?”라면 낱말은 {견적서, 어디로}다. 겹침 수 0이다. 못 찾는다.',comment='같은 걸 묻는데 말을 바꾸니 겹침이 0이 됐네요. 쪽지는 서랍에 그대로 있는데요.'),
  pair=('서류함에 서류철이 열두 개 있다. 등에 제목이 적혀 있다. “거래처”를 찾으라고 하면 금방 찾는다. “견적서 보낼 곳”을 찾으라고 하면, 같은 서류철인데도 제목이 달라 지나친다.','낱말로 찾기는 빠르고, 이름이나 번호처럼 정확한 말을 찾는 데 강하다. 반면 질문과 쪽지의 표현이 다르면 놓친다 [[papanubo2026memorilla]]. 찾아온 쪽지는 글 그대로 창에 들어가므로, 여러 장을 넣을수록 창을 차지한다.'),
  talk=[('doc','front','같은 것을 두 가지로 물어볼게요. “거래처 이름이 뭐였죠?”와 “견적서를 어디로 보내죠?” 둘 다 찾을까요?'),('fly','arms','“거래처”라는 말이 있으면 찾지. 두 번째는… 정말 못 찾을까?'),('robo','chart','묻는 법을 “다른 말로”로 바꿔 봐. 초록 불이 몇 개나 꺼지는지!')],
  panel='<div class="panel"><h3>실험 — 쪽지 서랍에서 찾기</h3><div class="ctrl">'+rg('r1Q','질문 번호',1,10,4)+tg('g1A','묻는 법',[('dq','같은 낱말로'),('iq','다른 말로')])+tg('g1N','겹칠 때',[('old','오래된 것 먼저'),('new','최신 먼저')])+'</div><div class="kpis" id="k1"></div>'+cv('c1','서랍 속 쪽지 12장을 날짜순으로 늘어놓은 그림. 질문과 낱말이 겹치는 쪽지는 밝게, 꺼낸 쪽지는 테두리로 표시된다')+'<div class="insight" id="ins1" aria-live="polite"></div></div>',
  report='보고드려요. 같은 낱말로 물으면 쪽지를 다 찾았어요. 다만 거래처와 회의는 쪽지가 두 장씩 나와서, 오래된 것을 먼저 꺼내면 틀렸어요. 다른 말로 물으면 열 개 모두 못 찾았어요.',
  stepsh='꺼내 읽기의 세 단계',steps=['넣어 두기: 손님의 말을 날짜와 함께 쪽지로 서랍에 넣는다. 원문을 버리지 않는다.','찾기: 질문이 오면 질문과 가까운 쪽지를 고른다.','창에 넣기: 고른 쪽지를 질문 앞에 붙여 모델에 보낸다. 모델은 그것을 읽고 답한다.','못 찾으면 2번에서 끝난다. 쪽지가 서랍에 있어도 모델은 그것을 읽지 못한다.'],
  lim='사람은 같은 것을 여러 가지 말로 묻는다. 낱말이 겹쳐야만 찾는 방식은 돌려 묻는 질문에 약하다. 다음 칸에서 뜻으로 찾는다.',
  concepts=['method/rag','concept/lexical-search','concept/note-store','limitation/vocabulary-mismatch']),
 dict(id='lv2',no='②',title='뜻으로 찾기 — 말이 달라도 가까운 쪽지',nav='뜻으로 찾기',tc='m',tag1='방법: 글을 좌표로 바꿔 가까운 것 찾기 (임베딩)',tag2='일상: 제목 대신 내용으로 서류 찾기',
  why=('손님이 “점심으로 떡볶이 어때요?”라고 묻는다. 서랍에는 “저는 매운 걸 못 먹어요”라는 쪽지가 있다. 겹치는 낱말은 하나도 없다.','낱말로 찾기는 이 쪽지를 못 찾는다. 모델은 손님이 매운 걸 못 먹는다는 것을 모른 채 답한다.','글을 숫자 묶음(좌표)으로 바꾸는 장치를 쓴다. 뜻이 비슷한 글은 가까운 좌표에 놓이도록 만든 장치다. 질문의 좌표와 가장 가까운 쪽지를 고른다. 이 좌표를 임베딩이라 부른다.','서류철 등에 적힌 제목이 아니라, 안에 든 내용이 무엇에 관한 것인지를 보고 찾는 것이다.'),
  math=dict(ask='뜻이 “가깝다”는 걸 어떻게 숫자로 재요?',school='두 점 사이의 거리다. 피타고라스 정리로 구한다.',
   eq='거리 = √( (가로 차이)² + (세로 차이)² )',pieces=[('좌표','글 하나를 나타내는 숫자 묶음. 실제로는 수백~수천 개의 숫자다'),('거리가 가깝다','뜻이 비슷하다고 본다'),('가장 가까운 쪽지','질문과 함께 창에 넣을 쪽지')],
   num='숫자 두 개짜리 좌표로 해 보자. 질문이 (1, 2), 쪽지 가가 (4, 6), 쪽지 나가 (2, 2)에 있다. 가까지의 거리는 √(3² + 4²) = √25 = 5다. 나까지는 √(1² + 0²) = 1이다. 쪽지 나가 더 가깝다. 나를 꺼낸다.',comment='낱말이 하나도 안 겹쳐도 좌표가 가까우면 찾는군요. “떡볶이”와 “매운 걸 못 먹어요”가 가까이 놓이는 거네요.'),
  pair=('신입 직원은 서류철 제목만 보고 찾는다. 오래 일한 직원은 “견적서 보낼 곳”이라는 말을 듣고 거래처 서류철을 꺼낸다. 무엇에 관한 서류인지 알기 때문이다.','이 페이지에서는 진짜 좌표를 계산하지 않는다. 쪽지마다 사람이 “뜻 꼬리표”(음식, 일정, 거래 …)를 붙여 두고, 꼬리표가 같으면 가깝다고 친다. 실제 장치가 하는 일을 손으로 흉내 낸 것이다.'),
  talk=[('doc','think','다른 말로 물은 질문 열 개를 뜻으로 찾으면 몇 개를 찾을까요?'),('fly','arms','뜻이라는 게 믿을 만할까? 엉뚱한 걸 가까이 놓기도 할 텐데.'),('robo','happy','찾는 법을 “뜻으로”로 바꿔 봐! 그리고 “최신 먼저”도 켜고.')],
  panel='<div class="panel"><h3>실험 — 찾는 법과 묻는 법</h3><div class="ctrl">'+tg('g2M','찾는 법',[('word','낱말로'),('tag','뜻으로')])+tg('g2A','묻는 법',[('iq','다른 말로'),('dq','같은 낱말로')])+tg('g2N','겹칠 때',[('new','최신 먼저'),('old','오래된 것 먼저')])+'</div><div class="kpis" id="k2"></div>'+cv('c2','질문 10개마다 맞는 쪽지를 찾았는지 표시한 칸')+'<div class="insight" id="ins2" aria-live="polite"></div><div class="tw"><table class="tb" id="t2"><tr><th>찾는 법</th><th>같은 낱말로 물을 때</th><th>다른 말로 물을 때</th></tr></table></div></div>',
  report='보고드려요. 다른 말로 물은 질문 열 개를 낱말로는 0개, 뜻으로는 10개 찾았어요. 다만 “오래된 것 먼저”로 두면 거래처와 회의에서 낡은 쪽지를 꺼내 8개가 돼요.',
  stepsh='찾기에서 생기는 세 가지 일',steps=['맞는 쪽지를 찾는다. 모델이 정확한 원문을 읽고 답한다.','못 찾는다. 쪽지가 있어도 모델은 모른다.','낡은 쪽지를 찾는다. 거래처가 바뀌기 전의 쪽지를 읽고 자신 있게 틀린 답을 한다.','세 번째가 가장 위험하다. 틀렸다는 표시가 어디에도 없다.'],
  lim='꺼내 읽기는 쪽지를 “찾아서 읽는” 방식이다. 답이 쪽지 한 장에 있으면 강하다. 여러 장을 맞춰 봐야 나오는 답에는 약하고, 넣는 쪽지가 늘수록 창이 찬다. 그리고 서랍에 낡은 쪽지가 쌓인다. 2-6에서 2부를 정리하고, 3부에서 서랍을 돌보는 법을 본다.',
  intern=SIA,concepts=['concept/embedding','concept/semantic-search','limitation/stale-retrieval'])],
 duel=dict(title='낱말로 찾기 vs 뜻으로 찾기 — 돌려 묻는 질문 10개',metric='맞는 쪽지를 찾은 질문 수',tag='일상: 제목으로 vs 내용으로',q='손님이 쪽지와 다른 말로 열 가지를 묻는다. 낱말이 겹치는 쪽지를 찾는 쪽과 뜻이 가까운 쪽지를 찾는 쪽, 누가 더 많이 찾을까? 둘 다 겹치면 최신 쪽지를 먼저 꺼낸다.',
  fly=('낱말로 찾기 — 준비할 것 없음','겹치는 말이 있으면 찾고 없으면 말지. 헷갈릴 일이 없어.'),robo=('뜻으로 찾기 — 글을 좌표로 바꾸는 장치가 필요','말이 달라도 같은 얘기면 찾아내지. 큰 장치의 힘이야!'),rule='맞는 쪽지를 찾은 질문 수(많을수록 좋음). 막대가 긴 쪽이 이긴다.'),
 sumh='정리 — 꺼내 읽기의 성적',
 sum='<div class="tw"><table class="tb" id="sumTb"><tr><th>방법</th><th>요청에 읽는 조각</th><th>같은 낱말로 물을 때</th><th>다른 말로 물을 때</th></tr></table></div><p style="font-size:14px;color:var(--muted)">꺼내 읽기의 숫자는 “맞는 쪽지를 찾았는가”를 센 것이다. 찾은 쪽지를 모델이 제대로 썼는지는 따로 따져야 한다.</p>'+steps3([('질문을 보고 고른다','원문을 버리지 않고, 질문이 온 뒤에 필요한 것만 창에 넣는다.'),('찾기가 전부다','못 찾으면 없는 것과 같다. 낡은 것을 찾으면 틀린 답이 나온다.'),('찾는 법마다 강한 곳','낱말로 찾기는 정확한 이름과 번호에, 뜻으로 찾기는 돌려 묻는 질문에 강하다.')])+field('문서 검색형 AI의 답이 이상하면 먼저 “무엇을 찾아왔는지”를 확인한다. 찾아온 문서가 틀렸다면 모델을 바꿔도 소용없다. 문서에 날짜를 붙여 두고 최신 것을 먼저 쓰게 하는 것만으로도 낡은 답이 준다.','이 페이지의 “뜻으로 찾기”는 사람이 붙인 꼬리표로 흉내 낸 것이다. 실제 장치는 엉뚱한 글을 가깝다고 볼 때도 있고, 정확한 이름을 놓칠 때도 있다. 그래서 두 방법을 함께 쓰는 경우가 많다.'),
 outro=[('doc','front','오늘의 한 줄이에요. 꺼내 읽기는 찾기가 전부예요. 못 찾으면 없는 것이고, 낡은 것을 찾으면 틀려요.'),('asst','smile','쪽지가 서랍에 그대로 있는데도 말을 바꾸니 못 찾는 게 인상적이었어요.'),('fly','coffee','졌군. 낱말만으로는 돌려 묻는 걸 못 잡아. 그래도 이름이나 번호는 내 쪽이 정확해.'),('robo','happy','뜻으로 찾기의 승리! …그런데 거래처 쪽지가 두 장 나온 건 좀 찜찜해. 서랍 정리가 필요하겠어.'),('moa','report','쪽지마다 날짜를 적어 둬서 다행이에요. 거래처 쪽지 두 장은 따로 표시해 둘게요.')],
 examples=['쪽지 12장: 손님이 30일 동안 한 중요한 말 열두 가지를 한 장씩 적은 것이다 (설명용 모형). 쪽지 한 장은 40조각, 질문은 20조각으로 쳤다','낱말로 찾기: 쪽지마다 정해 둔 핵심 낱말이 질문에 있으면 찾은 것으로 쳤다. “다른 말로 묻기” 질문은 핵심 낱말이 하나도 겹치지 않게 지었다','뜻으로 찾기: 진짜 임베딩을 계산하지 않았다. 쪽지와 질문에 사람이 붙인 뜻 꼬리표가 같으면 찾은 것으로 쳤다','좌표 (1, 2), (4, 6), (2, 2)는 손으로 따라 하기 위한 숫자다','채점은 “맞는 쪽지를 꺼냈는가”까지다. 실제 모델의 답을 받아 채점한 것이 아니다'],
 refs=['lewis2020retrieval','cognee2026llmmemory','papanubo2026memorilla'],
 claims=[('claim/rag-definition','RAG는 외부 문서 저장소에서 질문과 관련된 정보를 찾아 모델의 입력에 더하는 방식이다','#lv1','lewis2020retrieval','논문 전체','method/rag'),
  ('claim/rag-misses-paraphrase','유사한 내용을 중심으로 찾기 때문에 질문과 직접 겹치는 단어가 없는 정보는 놓칠 수 있다','#lv1','papanubo2026memorilla','1-2절 RAG','limitation/vocabulary-mismatch'),
  ('claim/search-kinds','찾는 방식에는 벡터 유사도, 어휘 검색, 메타데이터 필터, 그래프 탐색, 이들을 섞은 방식이 있다','#lv2','cognee2026llmmemory','RAG와의 관계 절','concept/semantic-search')],
 openq=[('question/mem-stale-notes','서랍에 쌓인 낡은 쪽지는 누가, 언제 치울까?','#lv2','3-3에서 기억 돌보기로 다룬다')],
 nodes=[('method/rag','Method','꺼내 읽기 (RAG)','retrieval-augmented generation','#lv1','바깥 저장소에서 질문과 관련된 글을 찾아 창에 넣고 답하게 하는 방식.'),
  ('concept/lexical-search','Concept','낱말로 찾기','lexical search','#lv1','질문과 같은 낱말이 든 글을 찾는 방법.'),
  ('concept/note-store','Concept','쪽지 서랍','note store','#lv1','대화에서 나온 말을 날짜와 함께 한 장씩 보관한 바깥 저장소.'),
  ('limitation/vocabulary-mismatch','Limitation','말이 다르면 못 찾는다','vocabulary mismatch','#lv1','질문과 쪽지의 표현이 다르면 낱말로 찾기는 쪽지를 놓친다.'),
  ('concept/embedding','Concept','글의 좌표 (임베딩)','embedding','#lv2','글 하나를 나타내는 숫자 묶음. 뜻이 비슷한 글은 가까운 좌표에 놓인다.'),
  ('concept/semantic-search','Concept','뜻으로 찾기','semantic search','#lv2','질문의 좌표와 가까운 좌표를 가진 글을 찾는 방법.'),
  ('limitation/stale-retrieval','Limitation','낡은 쪽지를 꺼낼 수 있다','stale retrieval','#lv2','같은 주제의 옛 쪽지와 새 쪽지가 함께 있으면 옛 것을 꺼내 틀린 답을 할 수 있다.'),
  ('sim/2-5-notes','Simulation','쪽지 서랍에서 찾기','keyword retrieval over notes','#lv1'),('sim/2-5-modes','Simulation','찾는 법과 묻는 법','retrieval mode grid','#lv2'),('sim/2-5-duel','Simulation','대결: 낱말 vs 뜻','duel: lexical vs semantic','#vs')],
 edges=[('concept/note-store','partOf','method/rag','#lv1'),('concept/lexical-search','partOf','method/rag','#lv1'),('concept/lexical-search','hasLimitation','limitation/vocabulary-mismatch','#lv1'),('limitation/vocabulary-mismatch','addressedBy','concept/semantic-search','#lv2'),
  ('concept/embedding','prerequisiteOf','concept/semantic-search','#lv2'),('method/rag','hasLimitation','limitation/stale-retrieval','#lv2'),('limitation/stale-retrieval','raises','question/mem-stale-notes','#lv2'),
  ('concept/lexical-search','demonstratedBy','sim/2-5-notes','#lv1'),('concept/semantic-search','demonstratedBy','sim/2-5-modes','#lv2'),('limitation/vocabulary-mismatch','demonstratedBy','sim/2-5-duel','#vs')],
 gloss={'쪽지':['쪽지','이 시리즈의 별명','대화에서 나온 말 하나를 날짜와 함께 적어 서랍에 넣은 것.'],'꺼내 읽기':['꺼내 읽기 (RAG)','쓰임','바깥 저장소에서 관련된 글을 찾아 창에 넣고 답하게 하는 방식.'],'임베딩':['임베딩','모델','글 하나를 나타내는 숫자 묶음(좌표). 뜻이 비슷한 글은 가까이 놓인다.'],'좌표':['좌표 (임베딩)','모델','글 하나를 나타내는 숫자 묶음.'],
  '뜻 꼬리표':['뜻 꼬리표','설명용 설정','이 페이지에서 임베딩을 흉내 내려고 쪽지마다 사람이 붙인 주제 이름.'],'창':['창 (문맥 창)','생성 AI','한 번에 읽을 수 있는 글의 범위.'],'원문':['원문','쓰임','줄이지 않은 대화 그대로.'],'서랍':['서랍 (바깥 저장소)','이 시리즈의 별명','모델 밖에 기록을 보관하는 곳.']},
 core=['쪽지','꺼내 읽기','임베딩','서랍'],
 quiz={'why':[Q('꺼내 읽기가 요약과 다른 점은?',['원문을 버리고 미리 줄인다','원문을 두고, 질문이 온 뒤에 필요한 것만 고른다','창을 더 크게 쓴다'],1,'질문을 보고 고르니 무엇이 필요한지 알고 골라요.','줄이는 시점을 견줘 보세요.','method/rag')],
  'lv1':[Q('질문 낱말 {출장, 어디}와 쪽지 낱말 {출장, 부산}의 겹침 수는?',['0','1','2'],1,'함께 든 것은 “출장” 하나예요.','두 묶음에 모두 있는 낱말을 세요.','concept/lexical-search','계산'),
        Q('쪽지가 서랍에 있는데도 모델이 모르는 경우는?',['찾기 단계에서 그 쪽지를 고르지 못했을 때','쪽지가 너무 짧을 때','모델이 바쁠 때'],0,'못 찾으면 창에 들어가지 않아요. 모델은 창 안의 글만 읽어요.','세 단계 가운데 어디서 끊기는지 보세요.','limitation/vocabulary-mismatch')],
  'lv2':[Q('점 (0, 0)과 (3, 4) 사이의 거리는?',['5','7','12'],0,'√(3² + 4²) = √25 = 5예요.','피타고라스 정리예요.','concept/embedding','계산'),
        Q('찾기에서 가장 위험한 경우는?',['못 찾는 것','낡은 쪽지를 찾아 자신 있게 틀리는 것','쪽지가 많은 것'],1,'틀렸다는 표시가 어디에도 없어요.','거래처 쪽지 두 장을 떠올려 보세요.','limitation/stale-retrieval')],
  'vs':[Q('낱말로 찾기가 뜻으로 찾기보다 나을 수 있는 경우는?',['돌려 묻는 질문','정확한 이름이나 번호를 찾을 때','언제나'],1,'정확한 표현이 문서에 그대로 있으면 낱말로 찾기가 강해요.','“거래처”처럼 꼭 그 말이어야 하는 경우를 떠올려 보세요.','concept/lexical-search')]},
)
JS=r'''
var QN=3,ASK='dq',NEW=false,cv=$('#c1');
function find(i,mode,qk){var f=FACTS[i],c=[];FACTS.forEach(function(g,j){var m=mode==='tag'?g.tag===f.tag:(qk==='dq'&&g.kw.some(function(w){return f.kw.indexOf(w)>=0;}));if(m)c.push(j);});return c;}
function upd1(){var c=find(QN,'word',ASK),pick=c.length?(NEW?c[c.length-1]:c[0]):-1,ok=pick===latestOf(QN);
  kpis($('#k1'),[['“'+FACTS[QN][ASK]+'”','질문 '+(QN+1)+'번','i'],[c.length+'장','낱말이 겹치는 쪽지',c.length?'g':'r'],[pick<0?'없음':FACTS[pick].d+'일 쪽지','꺼낸 쪽지',ok?'g':'r'],[pick<0?'못 찾음':(ok?'맞는 쪽지':'낡은 쪽지'),'결과',ok?'g':'r']]);
  $('#ins1').innerHTML=pick<0?'<p class="r">겹치는 낱말이 하나도 없어요. 쪽지는 서랍에 있지만 꺼내지 못했어요. 모델은 이 정보 없이 답해요.</p>':
    (ok?tpl('<p class="g">“{0}” 쪽지를 꺼냈어요. 질문 20조각과 쪽지 40조각, 60조각만 창에 넣으면 돼요.</p>',FACTS[pick].t):tpl('<p class="r">겹치는 쪽지가 {0}장이에요. 오래된 쪽지 “{1}”부터 꺼냈어요. 그 뒤에 고쳐 말한 “{2}” 쪽지가 있는데도요.</p>',c.length,FACTS[pick].t,FACTS[latestOf(QN)].t));drawAll();}
bindRange('r1Q',function(v){QN=v-1;upd1();},function(v){return v+'번';});toggleGroup('#g1A button',function(v){ASK=v;upd1();});toggleGroup('#g1N button',function(v){NEW=v==='new';upd1();});
addMod(cv,function(){var cols=cv.clientWidth<560?1:2,rowsN=Math.ceil(12/cols),H=24+rowsN*30,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var c=find(QN,'word',ASK),pick=c.length?(NEW?c[c.length-1]:c[0]):-1,gw=(W-16)/cols;
  FACTS.forEach(function(f,j){var x=8+Math.floor(j/rowsN)*gw,y=20+(j%rowsN)*30,hit=c.indexOf(j)>=0;rr(ctx,x+2,y,gw-4,25,6,hit?'rgba(94,227,156,.16)':'rgba(37,40,58,.7)',j===pick?COL.amber:(hit?COL.gfp:'rgba(70,72,96,.7)'));
    txt(ctx,f.d+'일',x+10,y+13,{size:11,color:COL.muted});txt(ctx,f.t,x+44,y+13,{size:12,color:hit?COL.text:'#8f8da8'});if(j===pick)txt(ctx,'꺼냄',x+gw-12,y+13,{size:10,color:COL.amber,align:'right',w:'700'});});
  txt(ctx,'서랍 속 쪽지 12장 (초록 = 낱말이 겹침)',8,10,{size:10,color:COL.muted});stamp(ctx,W,'설명용 모형');});
/* 칸 ② */
var MD='word',A2='iq',N2=true,cv2=$('#c2');
function upd2(){var r=scoreRetrieve(MD,A2,N2);
  kpis($('#k2'),[[MD==='word'?'낱말로':'뜻으로','찾는 법','a'],[A2==='dq'?'같은 낱말로':'다른 말로','묻는 법','i'],[r.n+' / 10','맞는 쪽지를 찾은 질문',r.n===10?'g':(r.n?'a':'r')],['60조각','요청 하나에 읽는 글','m']]);
  $('#ins2').innerHTML=r.n===0?'<p class="r">하나도 못 찾았어요. 질문과 쪽지에 겹치는 낱말이 없어요.</p>':(r.n===10?'<p class="g">열 개 모두 맞는 쪽지를 찾았어요.</p>':'<p class="a">거래처와 회의에서 틀렸어요. 같은 주제의 쪽지가 두 장인데 오래된 것을 꺼냈어요. 서랍에 낡은 쪽지가 그대로 있기 때문이에요.</p>');drawAll();}
toggleGroup('#g2M button',function(v){MD=v;upd2();});toggleGroup('#g2A button',function(v){A2=v;upd2();});toggleGroup('#g2N button',function(v){N2=v==='new';upd2();});
addMod(cv2,function(){drawBoard(cv2,scoreRetrieve(MD,A2,N2).ok,'마지막 날의 질문 10개 — 맞는 쪽지를 찾았나');});
$('#t2').insertAdjacentHTML('beforeend',[['word','낱말로 찾기'],['tag','뜻으로 찾기']].map(function(m){return '<tr><td>'+m[1]+'</td><td class="num">'+scoreRetrieve(m[0],'dq',true).n+' / 10 (오래된 것 먼저면 '+scoreRetrieve(m[0],'dq',false).n+')</td><td class="num">'+scoreRetrieve(m[0],'iq',true).n+' / 10 (오래된 것 먼저면 '+scoreRetrieve(m[0],'iq',false).n+')</td></tr>';}).join(''));
PAGE._T={wd:scoreRetrieve('word','dq',true).n,wdo:scoreRetrieve('word','dq',false).n,wi:scoreRetrieve('word','iq',true).n,ti:scoreRetrieve('tag','iq',true).n,tio:scoreRetrieve('tag','iq',false).n};
/* 대결 */
Duel({el:'#duel',higherIsBetter:true,drawMargin:0.05,fmt:function(v){return v+'개';},run:function(){return {fly:scoreRetrieve('word','iq',true).n,robo:scoreRetrieve('tag','iq',true).n,metric:'맞는 쪽지를 찾은 질문 수'};},
  say:function(f,b){return tpl('돌려 묻는 질문 열 개 가운데 초파리 쪽 낱말로 찾기는 {0}개, 주판봇 쪽 뜻으로 찾기는 {1}개를 찾았어요.',f,b);},
  lessons:{R:'사람은 같은 것을 여러 말로 묻는다. 말이 달라도 찾으려면 뜻으로 찾아야 한다',D:'두 방법이 비슷했다',F:'낱말로 찾기가 앞섰다'},
  after:function(){$('#duelNote').innerHTML=tpl('<p>같은 낱말로 물으면 낱말로 찾기도 {0}개를 찾아요. 정확한 이름이나 번호를 찾을 때는 낱말로 찾기가 더 믿을 만한 경우가 많아요.</p><p>이 페이지의 뜻으로 찾기는 사람이 붙인 꼬리표로 흉내 낸 것이라 틀리지 않았어요. 실제 장치는 엉뚱한 글을 가깝다고 볼 때가 있어요.</p>',scoreRetrieve('word','dq',true).n);}});
function row(n,c,a,b){return '<tr><td>'+n+'</td><td class="num">'+c+'</td><td class="num">'+a+'</td><td class="num">'+b+'</td></tr>';}
$('#sumTb').insertAdjacentHTML('beforeend',row('그냥 자르기 (창 1,000)','1,000','3 / 10','3 / 10')+row('요약하며 가기 (창 1,000)','720','5.9 / 10 (기대값)','5.9 / 10 (기대값)')+row('낱말로 꺼내 읽기','60',scoreRetrieve('word','dq',true).n+' / 10',scoreRetrieve('word','iq',true).n+' / 10')+row('뜻으로 꺼내 읽기','60',scoreRetrieve('tag','dq',true).n+' / 10',scoreRetrieve('tag','iq',true).n+' / 10')+row('원문 전부 (창 3,600)','3,600','10 / 10','10 / 10'));
upd1();upd2();
'''
