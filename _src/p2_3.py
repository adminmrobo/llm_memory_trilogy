# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
from p2_1 import X1C
P=dict(
 title='기억 서랍 셋 — 모델 속, 창 안, 바깥',chip='서랍 앵커',
 q='대화형 AI의 기억은 어디에 들어 있을까?',
 lead='<p>지금까지는 창 하나만 봤다. 대화형 AI가 답할 때 쓰는 정보는 세 군데에 나뉘어 있다. <b>모델 속 숫자</b>, <b>창 안의 글</b>, <b>바깥 저장소</b>다 [[cognee2026llmmemory]]. 이 페이지에서는 셋을 서랍 세 개로 놓고, 무엇을 어디에 둬야 하는지 따진다. 가르는 기준은 하나다. 얼마나 쉽게 고칠 수 있는가.</p>',
 objs=['세 서랍(모델 속·창 안·바깥)이 어디에 있고 언제까지 남는지 구분한다','자주 바뀌는 정보를 어느 서랍에 둬야 하는지 이유와 함께 말한다','답 하나에 세 서랍이 함께 쓰이는 모습을 예로 든다'],mins=18,
 kpis=[('3개','기억이 들어 있는 서랍'),('5개','이 페이지의 모형에서 매주 바뀌는 사실'),('7.5%','4주마다 다시 학습할 때 평균 낡은 답'),('0%','바깥 서랍을 바로 고칠 때 낡은 답')],
 hero=['오늘은 기억의 자리를 셋으로 갈라요. 모델 속, 창 안, 바깥이에요.','사실 100가지가 매주 5개씩 바뀌는 상황을 준비했어요. 손님의 거래처가 바뀐 것처럼요.','모델을 다시 학습시키는 건 큰일이야. 종이에 적어 두면 될 일을 정말 그렇게까지 해야 할까?','제대로 기억하려면 모델에 새겨야지! 한번 새기면 어느 대화에서나 쓸 수 있어.'],
 first3=['대화형 AI가 쓰는 정보는 모델 속 숫자, 창 안의 글, 바깥 저장소 세 곳에 나뉘어 있다. 남는 기간과 고치는 방법이 서로 다르다.','“AI가 왜 옛날 정보를 말하지?” “왜 어제 한 말을 모르지?” 같은 질문은 그 정보가 어느 서랍에 있었는지를 알면 풀린다.','가격, 담당자, 규정처럼 자주 바뀌는 정보는 바깥 서랍에 두고 필요할 때 창에 넣어 준다. 모델이 알고 있으리라 기대하지 않는다.'],
 abbr=['LLM','RAG'],cast=dict(fly='바깥에 적어 두면 된다',robo='모델에 새겨야 진짜다',**X1C),
 whyh='왜 서랍을 가르나',whytag='방법: 어디에 있고, 언제까지 남고, 어떻게 고치나',prev='2-2 창을 키우면 될까',
 why=[('창만으로는 모자랐다','창은 키우면 비싸고, 가운데를 놓친다. 창 밖에 둘 자리가 필요하다.'),('기억의 자리마다 성질이 다르다','모델 속 지식은 어느 대화에서나 쓰이지만 고치기 어렵다. 창 안의 글은 바로 쓰이지만 대화가 끝나면 사라진다.'),('고칠 수 있어야 기억이다','세상의 사실은 바뀐다. 바뀐 것을 반영하지 못하면 오래 남는 기억일수록 해롭다.')],
 levels=[dict(id='lv1',no='①',title='세 서랍 — 어디에 있고 어떻게 고치나',nav='세 서랍',tag1='방법: 남는 기간과 고치는 방법으로 가르기',tag2='일상: 몸에 밴 습관, 책상 위 서류, 서류함',
  why=('손님의 거래처가 초록상사에서 파랑상사로 바뀌었다. AI가 앞으로 어느 대화에서든 파랑상사라고 답하게 하고 싶다.','모델 속 숫자에 새기려면 다시 학습시켜야 한다. 시간이 들고, 새긴 것 하나만 골라 지우기도 어렵다. 창 안에 적어 두면 바로 쓰이지만 그 대화가 끝나면 사라진다.','모델 밖에 저장소를 둔다. 바뀐 사실은 거기서 바로 고친다. 답할 때 필요한 것만 찾아 창에 넣어 준다. 모델은 그대로 둔다.','몸에 밴 습관은 고치기 어렵다. 책상 위 서류는 퇴근하면 치워진다. 서류함에 넣어 둔 것은 언제든 꺼내 고칠 수 있다.'),
  math=dict(ask='다시 학습하기 전까지 낡은 답이 얼마나 쌓이는지 셀 수 있어요?',school='일정하게 늘어나는 등차수열과 평균이다.',
   eq='낡은 사실 수 = 매주 바뀌는 수 × 마지막으로 반영한 뒤 지난 주 수',pieces=[('매주 바뀌는 수','이 페이지에서는 100가지 가운데 5가지'),('지난 주 수','마지막으로 다시 학습한 뒤 흐른 주'),('평균','주마다의 낡은 수를 더해 주 수로 나눈 값')],
   num='4주마다 다시 학습한다고 하자. 학습한 주에는 0개, 그다음 주부터 5개, 10개, 15개가 낡는다. 평균은 (0 + 5 + 10 + 15) ÷ 4 = 7.5개, 100가지 가운데 7.5%다. 가장 나쁜 주에는 15%가 낡은 답이다.',comment='다시 학습하기 직전이 제일 위험하네요. 바깥 서랍은 바뀐 날 바로 고치니까 0이고요.'),
  pair=('<b>몸에 밴 습관</b>은 어디서나 저절로 나오지만 고치려면 오래 걸린다. <b>책상 위 서류</b>는 지금 보면서 일하지만 퇴근하면 치워진다. <b>서류함</b>은 찾으러 가야 하지만 언제든 넣고, 고치고, 버릴 수 있다.','<b>모델 속 숫자</b>(가중치)는 학습으로 얻은 지식이다. 요청마다 쓰이지만 고치려면 다시 학습하거나 편집해야 하고, 사실 하나만 지웠는지 확인하기 어렵다. <b>창 안의 글</b>은 이번 요청에만 있다. <b>바깥 저장소</b>는 모델과 따로 남고, 기록을 직접 고치고 지울 수 있다. 다만 답하기 전에 찾아오는 단계가 하나 더 든다.'),
  talk=[('doc','front','사실 100가지 가운데 매주 5개가 바뀌어요. 모델을 4주마다 다시 학습시키면 낡은 답은 얼마나 나올까요?'),('robo','chart','4주마다면 충분히 부지런한 거지! 낡은 답은 거의 없어.'),('fly','arms','정말? 다시 학습하는 간격을 바꿔 봐. 톱니가 어디까지 올라가는지.')],
  panel='<div class="panel"><h3>실험 — 바뀌는 사실과 낡은 답</h3>'+cv('c1','가로축은 1주부터 12주, 세로축은 낡은 답의 비율. 모델에 새기는 쪽은 다시 학습할 때마다 0으로 떨어지는 톱니 모양이고, 바깥 서랍은 0에 붙어 있다')+'<div class="ctrl">'+rg('r1P','다시 학습하는 간격 (주)',1,12,4)+'</div><div class="kpis" id="k1"></div><div class="insight" id="ins1" aria-live="polite"></div><h3>행동으로 보기 — 세 서랍 견주기</h3><div class="tw"><table class="tb"><tr><th></th><th>모델 속 숫자</th><th>창 안의 글</th><th>바깥 저장소</th></tr><tr><td>어디에</td><td>모델의 가중치</td><td>이번 요청에 넣은 글</td><td>문서, 표, 검색 색인 같은 곳</td></tr><tr><td>언제까지</td><td>모델을 쓰는 내내</td><td>이번 요청 동안</td><td>지울 때까지</td></tr><tr><td>고치려면</td><td>다시 학습 · 편집</td><td>글을 바꿔 넣기</td><td>기록을 직접 고치기</td></tr><tr><td>출처를 따질 수 있나</td><td>어렵다</td><td>넣은 글이 곧 출처</td><td>출처와 날짜를 함께 둘 수 있다</td></tr><tr><td>하나만 지우기</td><td>지웠는지 확인하기 어렵다</td><td>넣지 않으면 된다</td><td>그 기록을 지우면 된다</td></tr><tr><td>드는 품</td><td>따로 찾는 단계 없음</td><td>창 자리를 차지</td><td>답하기 전에 찾는 단계</td></tr></table></div>'+note('표는 참고 글 [[cognee2026llmmemory]]의 구분을 이 시리즈의 말로 옮긴 것이다.')+'</div>',
  report='보고드려요. 4주마다 다시 학습하면 평균 7.5%, 가장 나쁜 주에는 15%가 낡은 답이에요. 12주에 한 번이면 평균 27.5%까지 올라가요. 바깥 서랍은 바뀐 주에 바로 고쳐서 0%였어요.',
  stepsh='무엇을 어디에',steps=['언어 실력, 일반 상식처럼 좀처럼 바뀌지 않는 것은 모델 속에 있어도 된다.','지금 하는 대화, 방금 준 지시는 창 안에 있다.','가격, 담당자, 일정, 손님의 사정처럼 바뀌는 것은 바깥 서랍에 둔다.','바깥 서랍의 것은 저절로 쓰이지 않는다. 답할 때 찾아서 창에 넣어 줘야 한다.'],
  lim='서랍을 갈랐지만, 실제 답 하나에는 세 서랍이 섞여 들어간다. 다음 칸에서 질문 하나를 따라가 본다.',
  concepts=['concept/parametric-memory','concept/contextual-memory','concept/external-memory','concept/staleness']),
 dict(id='lv2',no='②',title='답 하나에 세 서랍이 함께 — 질문을 따라가 보기',nav='세 서랍이 함께',tc='m',tag1='방법: 질문마다 어느 서랍이 답을 대는지 보기',tag2='일상: 일 하나에 습관·서류·서류함을 다 쓰기',
  why=('손님이 묻는다. “우리 거래처에 보낼 견적서 인사말을 써 줘요.” 이 한마디에 답하려면 여러 가지가 필요하다.','서랍 하나로는 답이 안 된다. 모델 속 지식만으로는 거래처 이름을 모른다. 창 안의 글만으로는 30일 전의 말을 모른다.','세 서랍이 한 요청 안에서 함께 쓰인다. 글 쓰는 솜씨는 모델 속에서, 지금 받은 부탁은 창에서, 거래처 이름은 바깥 서랍에서 찾아 창에 넣어서 온다.','견적서를 쓸 때 문장력은 몸에 밴 것을, 오늘 받은 지시는 책상 위 쪽지를, 거래처 주소는 서류함을 쓴다.'),
  whyh='왜 함께 쓰나',
  pair=('한 가지 일을 하면서도 몸에 밴 솜씨, 책상 위의 쪽지, 서류함에서 꺼낸 서류를 함께 쓴다. 서류함에서 꺼낸 것은 책상 위에 올려놓아야 볼 수 있다.','바깥 서랍의 정보도 결국 창을 거쳐야 모델에 닿는다. 그래서 2-1, 2-2에서 본 창의 한계가 그대로 따라온다. 또 하나. 찾아온 정보와 모델 속 지식이 서로 다를 때 어느 쪽이 답을 이끌지는 정해져 있지 않다. 찾아왔다고 반드시 그것이 쓰이는 것은 아니다.'),
  talk=[('doc','think','질문 셋을 준비했어요. 질문마다 어느 서랍이 답을 댈까요?'),('fly','arms','서랍 하나면 되는 질문도 있겠지. 셋 다 쓰는 게 정말 흔할까?'),('robo','happy','질문 단추를 차례로 눌러 봐! 불이 켜지는 서랍을 보라고.')],
  panel='<div class="panel"><h3>실험 — 질문을 따라가 보기</h3><div class="ctrl">'+tg('g2','질문',[('a','“견적서 인사말 써 줘요”'),('b','“방금 뭐라고 했죠?”'),('c','“우리 거래처가 어디죠?”')])+'</div>'+cv('c2','왼쪽에 서랍 세 개, 가운데에 창, 오른쪽에 답. 질문에 따라 쓰이는 서랍에서 창으로 선이 이어진다')+'<div class="insight" id="ins2" aria-live="polite"></div></div>',
  report='보고드려요. 인사말 질문은 세 서랍을 다 썼어요. “방금 뭐라고 했죠?”는 창 안의 글만으로 됐고, 거래처 질문은 바깥 서랍에서 찾아 창에 넣어야 했어요.',
  stepsh='따라가 본 길',steps=['질문이 창에 들어온다.','대화 프로그램이 바깥 서랍에서 관련된 기록을 찾아 창에 함께 넣는다.','모델이 창 안의 글 전부를 읽고, 모델 속 지식으로 문장을 쓴다.','바깥 서랍에 없는 것, 창에 넣지 않은 것은 답에 쓰일 수 없다.'],
  lim='바깥 서랍에 넣고 꺼내는 일은 누군가 해야 한다. 무엇을 넣을지, 어떻게 줄일지, 어떻게 찾을지다. 2-4에서 줄이는 법(압축), 2-5에서 찾는 법(꺼내 읽기)을 본다.',
  intern=('moa','report','서류함은 제가 맡을게요. 넣을 때 날짜를 꼭 같이 적어 둘게요.'),concepts=['concept/memory-combination','concept/external-memory','limitation/retrieval-not-guaranteed'])],
 duel=dict(title='바깥에 적기 vs 모델에 새기기 — 매주 바뀌는 사실',metric='낡은 답의 비율',tag='일상: 서류함 vs 몸에 밴 습관',q='사실 100가지 가운데 매주 5개가 바뀐다. 12주 동안 낡은 답을 평균 몇 %나 내게 될까? 바깥 서랍에 적어 바로 고치는 쪽과, 4주마다 모델을 다시 학습시키는 쪽을 견준다.',
  fly=('바깥 서랍에 적고 바뀐 주에 바로 고친다','적어 두고 고치면 끝이야. 모델은 건드릴 필요 없어.'),robo=('모델 속에 새기고 4주마다 다시 학습시킨다','새겨야 진짜 기억이지. 4주면 충분히 자주야!'),rule='12주 동안 낡은 답의 평균 비율(낮을수록 좋음). 막대가 짧은 쪽이 이긴다.'),
 sumh='정리 — 세 서랍',
 sum=steps3([('모델 속','어디서나 쓰이지만 고치기 어렵다. 좀처럼 바뀌지 않는 것을 둔다.'),('창 안','바로 쓰이지만 요청이 끝나면 사라진다. 지금 필요한 것을 둔다.'),('바깥','오래 남고 고치기 쉽다. 바뀌는 것을 둔다. 쓰려면 찾아서 창에 넣어야 한다.')])+field('AI에게 맡길 일에 필요한 정보를 셋으로 가른다. 모델이 이미 알 만한 것, 이번 요청에 적어 줄 것, 따로 보관해 두고 찾아 넣을 것. 가격이나 규정처럼 바뀌는 정보를 모델이 알고 있으리라 기대하면 낡은 답을 받는다.','“매주 5개가 바뀐다”는 계산을 쉽게 하려고 정한 숫자다. 다시 학습하는 데 드는 실제 시간과 값은 이 페이지에서 다루지 않았다.'),
 outro=[('doc','front','오늘의 한 줄이에요. 기억은 세 서랍에 나뉘어 있고, 바뀌는 것은 고치기 쉬운 서랍에 둬요.'),('asst','smile','다시 학습하기 직전 주가 가장 위험하다는 톱니 그림이 기억에 남아요.'),('fly','coffee','적어 두고 고치는 게 이겼지. 그런데 서류함이 커지면 찾는 게 일이야. 그건 다음 문제군.'),('robo','meh','새기는 게 멋있긴 한데 고치기가 어렵네… 서류함을 아주 크게 만들면 되겠어!'),('moa','report','거래처가 바뀐 날, 서류함의 기록도 그날 바로 고쳐 뒀어요.')],
 examples=['“사실 100가지, 매주 5개가 바뀐다”는 계산을 쉽게 하려고 정한 설명용 모형이다. 바뀌는 사실은 주마다 서로 다른 5개라고 가정했다','모델에 새기는 쪽은 다시 학습한 주에 그때까지의 변화가 모두 반영된다고 가정했다. 실제 재학습은 이보다 훨씬 복잡하다','질문 따라가기의 선은 설명용 도식이다. 실제 서비스에서 어떤 정보가 어디서 오는지는 서비스마다 다르다'],
 refs=['cognee2026llmmemory','lewis2020retrieval'],
 claims=[('claim/three-memories','LLM의 기억은 가중치에 담긴 것, 문맥에 있는 것, 외부 저장소에 있는 것으로 나눌 수 있다','#lv1','cognee2026llmmemory','메모리 유형 표','concept/external-memory'),
  ('claim/parametric-hard-to-edit','가중치에 담긴 지식은 수정이 어렵고 개별 사실의 삭제를 확인하기 어렵다','#lv1','cognee2026llmmemory','파라메트릭 대 외부 표','concept/parametric-memory'),
  ('claim/retrieval-not-dominant','외부에서 가져온 정보와 가중치 속 지식이 충돌할 때 어느 쪽이 응답을 이끌지는 보장되지 않는다','#lv2','cognee2026llmmemory','FAQ','limitation/retrieval-not-guaranteed')],
 openq=[('question/mem-how-to-store','바깥 서랍에 무엇을, 어떻게 줄여서 넣을까?','#lv2','2-4에서 대화 압축으로 다룬다')],
 nodes=[('concept/parametric-memory','Concept','모델 속 기억 (가중치)','parametric memory','#lv1','학습으로 모델의 숫자에 담긴 지식. 고치려면 다시 학습하거나 편집해야 한다.'),
  ('concept/contextual-memory','Concept','창 안의 기억','contextual memory','#lv1','이번 요청에 넣은 글. 요청이 끝나면 사라진다.'),
  ('concept/external-memory','Concept','바깥 기억 (외부 저장소)','external memory','#lv1','모델 밖의 문서·표·색인에 보관한 정보. 모델과 따로 남고 직접 고칠 수 있다.'),
  ('concept/staleness','Concept','낡은 답','staleness','#lv1','세상의 사실이 바뀌었는데 예전 사실로 답하는 것.'),
  ('concept/memory-combination','Concept','세 서랍을 함께 쓰기','combining memory types','#lv2','답 하나에 모델 속 지식, 창 안의 글, 바깥에서 찾아온 정보가 함께 쓰이는 것.'),
  ('limitation/retrieval-not-guaranteed','Limitation','찾아왔다고 반드시 쓰이지는 않는다','retrieved is not the same as used','#lv2','바깥에서 가져온 정보와 모델 속 지식이 다를 때 어느 쪽이 답을 이끌지 정해져 있지 않다.'),
  ('sim/2-3-stale','Simulation','바뀌는 사실과 낡은 답','staleness sawtooth','#lv1'),('sim/2-3-trace','Simulation','질문을 따라가 보기','tracing a question','#lv2'),('sim/2-3-duel','Simulation','대결: 바깥에 적기 vs 모델에 새기기','duel: external vs parametric','#vs')],
 edges=[('concept/parametric-memory','contrastsWith','concept/external-memory','#lv1'),('concept/contextual-memory','contrastsWith','concept/external-memory','#lv1'),('concept/parametric-memory','hasLimitation','concept/staleness','#lv1'),('concept/external-memory','solves','concept/staleness','#lv1'),
  ('concept/external-memory','prerequisiteOf','concept/memory-combination','#lv2'),('concept/external-memory','hasLimitation','limitation/retrieval-not-guaranteed','#lv2'),('concept/memory-combination','raises','question/mem-how-to-store','#lv2'),
  ('concept/staleness','demonstratedBy','sim/2-3-stale','#lv1'),('concept/memory-combination','demonstratedBy','sim/2-3-trace','#lv2'),('concept/staleness','demonstratedBy','sim/2-3-duel','#vs')],
 gloss={'모델 속 숫자':['모델 속 숫자 (가중치)','모델','모델이 학습으로 얻은 숫자들. 여기에 담긴 지식은 요청마다 쓰이지만 고치기 어렵다.'],'가중치':['가중치','모델','모델 속 숫자. 학습으로 정해진다.'],'바깥 저장소':['바깥 저장소 (외부 메모리)','쓰임','모델 밖에 정보를 보관하는 곳. 문서, 표, 검색 색인 등.'],'창':['창 (문맥 창)','생성 AI','한 번에 읽을 수 있는 글의 범위.'],
  '낡은 답':['낡은 답','현상','세상의 사실이 바뀌었는데 예전 사실로 내는 답.'],'다시 학습':['다시 학습 (재학습)','학습','새 자료로 모델 속 숫자를 다시 정하는 일.'],'서랍':['서랍','이 시리즈의 별명','기억이 들어 있는 자리. 모델 속, 창 안, 바깥 셋이 있다.']},
 core=['모델 속 숫자','바깥 저장소','창','낡은 답'],
 quiz={'why':[Q('세 서랍을 가르는 가장 중요한 기준은?',['크기','얼마나 쉽게 고칠 수 있는가','이름'],1,'바뀌는 사실을 반영할 수 있어야 해요.','“고칠 수 있어야 기억이다”를 떠올려 보세요.','concept/external-memory')],
  'lv1':[Q('매주 5개가 바뀌고 3주마다 다시 학습한다. 낡은 사실의 평균은 몇 개일까?',['5개','7.5개','10개'],0,'(0 + 5 + 10) ÷ 3 = 5개예요.','학습한 주는 0개에서 시작해요.','concept/staleness','계산'),
        Q('담당자 이름처럼 자주 바뀌는 정보는 어느 서랍이 알맞을까?',['모델 속','바깥','어디든 같다'],1,'바깥 서랍은 기록을 바로 고칠 수 있어요.','고치기 쉬운 서랍을 찾으세요.','concept/external-memory')],
  'lv2':[Q('바깥 서랍에서 찾아온 정보가 모델에 닿으려면',['모델 속 숫자를 바꿔야 한다','창 안에 넣어 줘야 한다','아무것도 안 해도 된다'],1,'바깥의 것도 결국 창을 거쳐요.','서류함의 서류는 책상에 올려야 볼 수 있어요.','concept/memory-combination')],
  'vs':[Q('모델에 새기는 쪽이 진 까닭은?',['새긴 지식이 틀려서','다시 학습하기 전까지 바뀐 사실이 반영되지 않아서','바깥 서랍이 더 커서'],1,'바뀐 사실이 다음 학습 때까지 낡은 채로 남아요.','톱니 그림을 떠올려 보세요.','concept/staleness')]},
)
JS=r'''
var PD=4,CH=5,WK=12,cv=$('#c1');
function stale(p){var a=[];for(var w=0;w<WK;w++)a.push(CH*(w%p));return a;}
function avg(a){return a.reduce(function(x,y){return x+y;},0)/a.length;}
function upd1(){var s=stale(PD),mx=Math.max.apply(null,s);
  kpis($('#k1'),[[PD+'주','다시 학습하는 간격','a'],[f2(avg(s),1)+'%','12주 평균 낡은 답 (모델에 새김)','r'],[mx+'%','가장 나쁜 주','m'],['0%','바깥 서랍 (바뀐 주에 고침)','g']]);
  $('#ins1').innerHTML=PD===1?'<p class="g">매주 다시 학습하면 낡은 답이 0이에요. 다만 매주 모델을 다시 학습시키는 값은 이 그림에 들어 있지 않아요.</p>':tpl('<p class="r">{0}주마다 다시 학습하면 그 직전 주에 {1}%가 낡은 답이에요. 12주 평균은 {2}%예요.</p>',PD,mx,f2(avg(s),1))+'<p>바깥 서랍은 바뀐 기록을 그 주에 고치면 돼요. 모델은 그대로 둬요.</p>';drawAll();}
bindRange('r1P',function(v){PD=v;upd1();},function(v){return v+'주';});
addMod(cv,function(){var H=250,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var s=[0].concat(stale(PD));
  var o=bars(ctx,W,H,s,-1,{y0:0,y1:60,ticks:[0,15,30,45,60],fmt:function(v){return v+'%';},col:function(){return 'rgba(240,96,77,.75)';},xl:function(i){return i+'주';}});
  ctx.strokeStyle=COL.gfp;ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(o.P.l,o.Y(0)-1);ctx.lineTo(W-o.P.r,o.Y(0)-1);ctx.stroke();
  txt(ctx,'빨강 막대 = 모델에 새김 · 초록 선 = 바깥 서랍',o.P.l+4,14,{size:10,color:COL.muted});stamp(ctx,W,'설명용 모형');});
PAGE._T={s4:avg(stale(4)),s12:avg(stale(12)),mx4:Math.max.apply(null,stale(4)),s3:avg(stale(3).slice(0,3))};
/* 칸 ② */
var QS='a',cv2=$('#c2'),USE={a:[1,1,1],b:[1,1,0],c:[1,1,1]},MSG={a:'<p class="g">세 서랍이 다 쓰였어요. 인사말을 쓰는 솜씨는 모델 속에서, “인사말을 써 달라”는 부탁은 창에서, 거래처 이름 “파랑상사”는 바깥 서랍에서 찾아 창에 넣어 왔어요.</p>',
  b:'<p class="a">바로 앞의 말은 창 안에 있어요. 바깥 서랍을 찾을 필요가 없어요. 모델 속 지식은 답 문장을 쓰는 데 쓰여요.</p>',c:'<p class="g">거래처 이름은 모델 속에 없어요. 27일에 한 말이라 작은 창에도 없을 수 있어요. 바깥 서랍에서 “거래처: 파랑상사 (27일에 바뀜)”를 찾아 창에 넣어야 답할 수 있어요.</p>'};
var EX={a:['글 쓰는 솜씨','“인사말 써 줘요”','거래처: 파랑상사'],b:['문장 만드는 솜씨','바로 앞의 대화','(쓰지 않음)'],c:['문장 만드는 솜씨','“거래처가 어디죠?”','거래처: 파랑상사']};
toggleGroup('#g2 button',function(v){QS=v;$('#ins2').innerHTML=MSG[QS];drawAll();});
addMod(cv2,function(){var H=250,W=fit(cv2,H),ctx=cv2.getContext('2d');ctx.clearRect(0,0,W,H);var bw=Math.min(210,W*0.3),wx=W*0.45,wy=74,ww=Math.min(170,W*0.24),names=['모델 속 숫자','창 안의 글','바깥 저장소'],cols=[COL.doc,COL.amber,COL.gfp];
  rr(ctx,wx,wy,ww,104,10,'rgba(241,182,70,.10)',COL.amber);txt(ctx,'창',wx+ww/2,wy+16,{size:12,color:COL.amber,align:'center',w:'700'});txt(ctx,'모델이 읽는 글',wx+ww/2,wy+34,{size:10,color:COL.muted,align:'center'});
  names.forEach(function(n,i){var y=18+i*78,on=USE[QS][i];rr(ctx,8,y,bw,58,10,on?'rgba(37,40,58,.95)':'rgba(37,40,58,.4)',on?cols[i]:'rgba(90,92,116,.5)');
    txt(ctx,n,18,y+18,{size:12,color:on?cols[i]:'#6f7396',w:'700'});txt(ctx,EX[QS][i],18,y+40,{size:11,color:on?COL.text:'#6f7396'});
    if(on&&i!==0){ctx.strokeStyle=cols[i];ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(8+bw,y+29);ctx.lineTo(wx,wy+52);ctx.stroke();}});
  var mx=wx+ww+24;ctx.strokeStyle=COL.doc;ctx.lineWidth=2;ctx.setLineDash([5,4]);ctx.beginPath();ctx.moveTo(8+bw/2,76);ctx.bezierCurveTo(8+bw/2,6,mx+30,0,mx+40,wy+30);ctx.stroke();ctx.setLineDash([]);
  ctx.strokeStyle=COL.amber;ctx.beginPath();ctx.moveTo(wx+ww,wy+52);ctx.lineTo(mx,wy+52);ctx.stroke();rr(ctx,mx,wy+26,Math.max(60,W-mx-10),52,10,'rgba(37,40,58,.95)',COL.info);txt(ctx,'답',mx+12,wy+52,{size:13,color:COL.info,w:'700'});
  stamp(ctx,W,'설명용 도식');});
$('#ins2').innerHTML=MSG[QS];
/* 대결 */
Duel({el:'#duel',higherIsBetter:false,drawMargin:0.05,fmt:function(v){return f2(v,1)+'%';},run:function(){return {fly:0,robo:avg(stale(4)),metric:'낡은 답의 평균 비율'};},
  say:function(f,b){return tpl('12주 동안 낡은 답의 평균은 초파리 쪽 바깥 서랍이 {0}%, 주판봇 쪽 모델에 새기기가 {1}%예요. 가장 나쁜 주에는 15%였어요.',f2(f,1),f2(b,1));},
  lessons:{F:'바뀌는 사실은 고치기 쉬운 서랍에 둬야 한다. 새겨 넣은 기억은 다음 학습 때까지 낡은 채로 남는다',D:'둘이 비슷했다',R:'새겨 넣은 쪽이 앞섰다'},
  after:function(){$('#duelNote').innerHTML='<p>이 대결은 “낡은 답” 한 가지만 쟀어요. 바깥 서랍은 찾는 단계가 필요하고, 찾아온 것이 답에 반드시 쓰이는 것도 아니에요. 그 값은 2-5에서 따져요.</p>';}});
upd1();
'''
