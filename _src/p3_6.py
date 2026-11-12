# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
from p2_1 import X1C
P=dict(
 title='대결·총정리 — LLM은 어디까지 기억할 수 있을까',chip='시리즈 정리',
 q='LLM은 어디까지 기억할 수 있을까?',
 lead='<p>열여덟 편의 마지막이다. 창에서 출발해 메아리, 메모, 문맥 창, 요약, 쪽지 서랍, 돌보기, 기억 토큰까지 왔다. 처음 질문으로 돌아간다. LLM은 어디까지 기억할 수 있을까? 이 페이지의 답은 세 마디다. <b>얼마나 멀리</b>, <b>얼마나 정확히</b>, <b>얼마나 지금에 맞게</b>. 셋은 서로 다른 장치가 맡는다.</p>',
 objs=['기억을 길이·충실도·갱신 세 축으로 나눠 설명한다','내 일의 성격에 맞는 기억의 층을 고른다','“모델이 기억한다”와 “시스템이 기억하게 해 준다”를 구분한다'],mins=18,
 kpis=[('3축','길이 · 충실도 · 갱신'),('4층','최근 원문 · 요점 · 꺼내 읽기 · 돌보기'),('760조각','네 층을 다 켰을 때 요청에 읽는 글'),('18편','이 시리즈의 대결 수')],
 hero=['마지막 편이에요. 처음 질문에 답할 차례예요. 어디까지 기억할 수 있을까요?','열여덟 편의 성적을 한 표에 모았어요. 대결 전적도요.','모델은 창 안까지만 기억해. 나머지는 사람이 차려 준 거야. 그 구분이 답이지.','서랍을 크게, 창을 크게, 장치를 많이! 기억은 끝이 없다고!'],
 first3=['모델 스스로는 창 안까지만 기억한다. 그 너머는 서랍, 찾기, 돌보기 같은 바깥 장치가 기억하게 해 준다.','“AI가 기억한다”는 말을 들을 때 무엇이, 어디에, 어떻게 기억하는지 물을 수 있게 된다.','AI에게 긴 일을 맡길 때 세 가지를 점검한다. 필요한 과거가 닿는가, 정확한 원문이 들어가는가, 낡은 정보가 섞이지 않는가.'],
 abbr=['LLM','RAG','LSTM'],cast=dict(fly='작은 창에 맞는 층을 겹친다',robo='큰 창에 전부 넣는다',x1='30일 동안 대화한 익명 손님. 오늘은 방청석 맨 앞',x2='방청석의 누군가',x3='방청석의 누군가',moa='열여덟 편의 기록을 모은 사람 · 응원'),
 whyh='왜 세 축으로 답하나',whytag='방법: 길이 · 충실도 · 갱신으로 나눠 보기',prev='3-5 경험으로 배우는 에이전트',
 why=[('한마디로는 답할 수 없다','“한 달 전까지”라고 답하면 틀린다. 창이 작으면 어제 일도 모르고, 서랍이 있으면 일 년 전 일도 꺼낸다.'),('멀리와 정확히는 다르다','요약은 한 달 전까지 닿지만 세부를 잃었다. 원문은 정확하지만 비쌌다.'),('지금에 맞게는 또 다르다','멀리, 정확히 기억해도 낡은 것이면 틀린 답이다.')],
 levels=[dict(id='lv1',no='①',kind='답',title='세 축 — 얼마나 멀리, 얼마나 정확히, 얼마나 지금에 맞게',nav='세 축',tag1='방법: 방식마다 세 축에서 어디에 있는지 보기',tag2='일상: 오래, 또렷이, 틀리지 않게',
  why=('“어디까지 기억하나”에 답하려 한다. 방식이 아홉 가지나 나왔다.','한 가지 잣대로 줄 세우면 1부와 2부에서 봤듯 기록과 가정에 따라 순위가 바뀐다.','잣대를 셋으로 나눈다. <b>길이</b>는 얼마나 먼 과거가 닿는가. <b>충실도</b>는 얼마나 정확한 내용이 닿는가. <b>갱신</b>은 바뀐 사실을 얼마나 빨리 반영하는가. 방식마다 세 축에서 서 있는 자리가 다르다.','사람의 기억도 같다. 오래 기억하는 것, 또렷이 기억하는 것, 바뀐 것을 고쳐 기억하는 것은 서로 다른 일이다.'),whyh='왜 잣대를 셋으로 나누나',
  pair=('어릴 적 집의 분위기는 오래 기억하지만 전화번호는 잊었다(길고 흐리다). 어제 회의 내용은 또렷하지만 다음 달이면 잊는다(짧고 또렷하다). 친구가 이사했는데 옛 주소를 기억한다(낡았다).','모델 스스로 가진 것은 창이다. 창 안은 또렷하지만 짧다. 그 너머의 길이는 서랍이, 충실도는 찾는 법과 원문 보관이, 갱신은 돌보기가 맡는다. “LLM이 기억한다”는 말은 대개 “LLM을 둘러싼 장치가 기억하게 해 준다”는 뜻이다.'),
  talk=[('doc','front','내 일에 맞는 기억을 골라 볼게요. 물음 셋에 답하면 어떤 층이 필요한지 나와요.'),('robo','chart','물어볼 것도 없어! 층을 전부 다 켜면 되지.'),('fly','arms','다 켜면 다 돌봐야 해. 필요한 것만 골라 봐.')],
  panel='<div class="panel"><h3>실험 — 내 일에 맞는 기억 고르기</h3><div class="ctrl">'+tg('gA','① 답이 있는 곳',[('one','자료 한 곳에 적혀 있다'),('many','여러 곳을 맞춰 봐야 한다')])+'</div><div class="ctrl">'+tg('gB','② 정보가 바뀌나',[('no','거의 안 바뀐다'),('yes','자주 바뀐다')])+'</div><div class="ctrl">'+tg('gC','③ 지난 과정이 필요한가',[('no','지금 상태만'),('yes','이력도 필요')])+'</div><div class="insight" id="ins1" aria-live="polite"></div><h3>방식마다 세 축에서 서 있는 자리</h3><div class="tw"><table class="tb"><tr><th>방식 (다룬 편)</th><th>길이 — 얼마나 멀리</th><th>충실도 — 얼마나 정확히</th><th>갱신 — 얼마나 지금에 맞게</th></tr><tr><td>창 / 문맥 창 (1-1, 2-1)</td><td>창 크기까지. 밖은 0</td><td>원문 그대로</td><td>넣는 글을 바꾸면 바로</td></tr><tr><td>큰 창에 전부 (2-2)</td><td>넣은 만큼</td><td>원문이지만 가운데를 놓칠 수 있다</td><td>바로. 대신 요청마다 비싸다</td></tr><tr><td>메모 / 요약 (1-4, 2-4)</td><td>멀리 닿는다</td><td>거듭 줄일수록 세부를 잃는다</td><td>다음 요약 때</td></tr><tr><td>문 달린 메모장 (1-5)</td><td>문을 열어 둔 동안</td><td>칸 수만큼</td><td>배운 규칙대로</td></tr><tr><td>모델 속에 새기기 (2-3)</td><td>모델을 쓰는 내내</td><td>출처를 따지기 어렵다</td><td>다시 학습할 때까지 낡는다</td></tr><tr><td>꺼내 읽기 (2-5)</td><td>서랍에 있는 만큼</td><td>원문. 찾으면 정확하다</td><td>서랍을 고치면 바로</td></tr><tr><td>프로필 (3-2)</td><td>지금 상태만</td><td>정해 둔 칸만큼</td><td>고쳐 쓰면 바로. 이력은 잃는다</td></tr><tr><td>돌본 모음 (3-3)</td><td>서랍에 있는 만큼</td><td>원문 + 날짜</td><td>어긋남을 표시해 지금 것을 가린다</td></tr><tr><td>기억 토큰 (3-4)</td><td>저장된 전체</td><td>세밀한 정보를 잃을 수 있다</td><td>문서를 더하면 반영. 장치는 모델마다 학습</td></tr></table></div>'+note('표는 이 시리즈의 설명용 모형과 참고 자료에서 본 경향을 정리한 것이다. 등급을 매긴 것이 아니다.')+'</div>',
  report='보고드려요. 세 축에서 모두 앞선 방식은 없었어요. 창은 또렷하지만 짧고, 요약은 멀리 닿지만 흐리고, 서랍은 멀고 또렷하지만 찾기와 돌보기에 달려 있어요.',
  stepsh='처음 질문의 답',steps=['모델 스스로는 창 안까지만 기억한다. 대화하는 동안 모델 속 숫자는 바뀌지 않는다.','얼마나 멀리: 바깥 서랍이 닿는 데까지. 서랍은 얼마든지 키울 수 있다.','얼마나 정확히: 원문을 남겨 두었는지, 그리고 맞는 것을 찾아내는지에 달렸다.','얼마나 지금에 맞게: 누가 돌보는지에 달렸다. 돌보지 않으면 멀리, 정확히 기억한 것이 낡은 채로 돌아온다.'],
  lim='세 축은 이 시리즈가 정리를 위해 고른 틀이다. 값(읽는 조각, 시간), 지울 수 있는지, 누가 볼 수 있는지 같은 다른 축도 있다. 다음 칸에서는 층을 직접 켜고 꺼 본다.',
  concepts=['concept/memory-length','concept/memory-fidelity','concept/memory-freshness','concept/system-vs-model-memory']),
 dict(id='lv2',no='②',kind='종합',title='층을 켜고 끄기 — 손님의 한 달을 다시',nav='층 켜고 끄기',tc='m',tag1='방법: 네 층을 따로 켜고 끄며 질문 12개 채점',tag2='일상: 책상, 명함첩, 서류함, 서류함 정리',
  why=('손님과의 30일 대화, 질문 12개(지금 10개, 지난 일 2개)로 돌아간다. 창은 작게 쓰고 싶다.','층 하나로는 빈 곳이 남았다. 최근 원문만으로는 옛말을, 프로필만으로는 지난 일을, 정리 안 한 쪽지만으로는 바뀐 사실을 틀렸다.','네 층을 따로 켜고 끈다. ① 최근 5일 원문 ② 요점 프로필 ③ 쪽지 꺼내 읽기 ④ 쪽지 돌보기. 어느 층이 어느 질문을 맡는지 본다.','책상 위 서류, 명함첩, 서류함, 그리고 서류함 정리. 넷이 다 있어야 한 달 전 일도, 바뀐 연락처도, 지난 이력도 답한다.'),
  math=dict(ask='층을 다 켜면 읽는 글이 얼마나 돼요?',school='덧셈이다. 켠 층의 조각을 더한다.',
   eq='요청에 읽는 조각 = 최근 원문 + 프로필 + 찾아온 쪽지 + 질문',pieces=[('최근 원문','5일 치 600조각'),('프로필','주제 열 칸 100조각'),('찾아온 쪽지','한 장 40조각'),('질문','20조각. 돌보기는 요청할 때 드는 조각이 없다')],
   num='600 + 100 + 40 + 20 = 760조각이다. 30일 원문 전부인 3,600조각의 약 21%다. 견줄 쌍으로는 760 × 760 = 약 58만 쌍, 3,600조각일 때의 약 4%다.',comment='네 층을 다 켜도 전부 넣기의 5분의 1쯤이네요. 돌보기는 읽는 글을 늘리지 않고요.'),
  pair=('책상 위 서류만 있으면 이번 주 일만 안다. 명함첩이 있으면 지금 연락처를 안다. 서류함이 있으면 지난 일도 찾는다. 서류함을 정리해 두지 않으면 옛 서류를 꺼내 틀린다.','층마다 맡는 질문이 다르다. 최근 원문은 흐름을, 프로필은 지금 상태를, 쪽지는 지난 일과 세부를 맡는다. 돌보기는 쪽지와 다른 층이 서로 어긋나지 않게 한다. 층을 끄면 그 층이 맡던 질문이 빈다.'),
  talk=[('doc','think','네 층을 하나씩 꺼 볼게요. 어느 층을 끄면 어느 질문이 비는지 보세요.'),('fly','arms','돌보기는 꺼도 티가 안 날 거야. 읽는 글도 안 드는데. 정말?'),('robo','happy','돌보기를 끄고 프로필도 꺼 봐! 거래처 칸이 어떻게 되는지.')],
  panel='<div class="panel"><h3>실험 — 네 층 켜고 끄기</h3><div class="ctrl"><div class="group" id="g2"><span class="glabel">켠 층</span><button type="button" class="bt" data-k="r" aria-pressed="true">① 최근 원문</button><button type="button" class="bt" data-k="p" aria-pressed="true">② 프로필</button><button type="button" class="bt" data-k="n" aria-pressed="true">③ 쪽지 꺼내 읽기</button><button type="button" class="bt" data-k="m" aria-pressed="true">④ 돌보기</button></div></div><div class="kpis" id="k2"></div>'+cv('c2','질문 12개마다 맞혔는지 표시한 칸. 층을 끄면 그 층이 맡던 질문이 빨강이나 노랑으로 바뀐다')+'<div class="insight" id="ins2" aria-live="polite"></div></div>',
  report='보고드려요. 네 층을 다 켜면 760조각으로 열두 개를 다 맞혀요. 돌보기와 프로필을 함께 끄면 거래처와 회의 요일이 불확실해져요. 쪽지를 끄면 지난 일 두 개와 세부를 못 맞혀요.',
  stepsh='층이 맡은 질문',steps=['최근 원문: 27일, 29일에 고쳐 말한 거래처와 회의 요일.','프로필: 지금 상태를 묻는 질문 열 개 전부.','쪽지 꺼내 읽기: 지난 일을 묻는 두 개와, 프로필에 담지 못한 세부.','돌보기: 쪽지가 옛것을 꺼내 다른 층과 어긋나는 일을 막는다.'],
  lim='이 실험은 층마다 맡은 일이 깔끔하게 나뉜다고 가정한 모형이다. 실제로는 층끼리 어긋날 때 무엇을 믿을지, 찾기가 틀렸을 때 어떻게 알아챌지가 남는다. 열린 질문으로 남겨 둔다.',
  intern=SIA,concepts=['concept/memory-layers','method/hybrid-memory','concept/memory-maintenance'])],
 duel=dict(title='네 층 vs 전부 넣기 — 마지막 대결',metric='맞힐 질문 수 (기대값, 12개 가운데)',tag='일상: 책상·명함첩·서류함·정리 vs 전부 책상에',q='시리즈의 마지막 대결. 질문 12개. 가운데는 절반만 쓰인다고 본다(깊이 0.5). 네 층을 겹친 작은 창과, 30일 원문을 전부 넣은 큰 창 가운데 누가 더 많이 맞힐까?',
  fly=('네 층을 겹친 작은 창 — 760조각','작은 걸 맞게 겹쳤어. 필요한 건 끝자리에 있고.'),robo=('30일 원문 전부 — 3,600조각','옛말도 새말도 원문 그대로 다 있어. 이번엔 이긴다!'),rule='맞힐 질문 수의 기대값(많을수록 좋음). “깊이 0.5”와 “찾기와 돌보기가 제대로 된다”는 가정 위에서만 성립한다.'),
 sumh='정리 — 열여덟 편을 한 장으로',
 sum='<div class="tw"><table class="tb"><tr><th>부</th><th>물음</th><th>답</th></tr><tr><td><b>1부</b> 시계열의 기억</td><td>숫자는 얼마나 멀리 기억하나</td><td>창은 길이만큼만 기억한다. 필요한 길이는 기록의 메아리가 정한다. 펼치지 않고 줄여 담을 수 있고, 남길 것을 고르는 문을 달 수 있다.</td></tr><tr><td><b>2부</b> LLM의 기억</td><td>글은 어떻게 기억하나</td><td>모델은 창 안까지만 안다. 전부 넣으면 비싸고 가운데를 놓친다. 줄이면 세부를 잃고, 꺼내 읽으면 찾기에 달렸다. 그래서 섞어 쓴다.</td></tr><tr><td><b>3부</b> 기억 관리</td><td>기억은 어떻게 돌보나</td><td>가려서 적고, 때와 자리를 고르고, 낡은 것을 표시한다. 글이 아닌 꼴로 넘기는 연구와 에이전트의 경험 기억이 시작됐다.</td></tr></table></div><h3>대결 전적</h3><div class="tw"><table class="tb" id="recTb"><tr><th>부</th><th>초파리 승</th><th>주판봇 승</th><th>무승부</th></tr></table></div><p style="font-size:14px;color:var(--muted)">2부와 3부의 여러 판은 가정에 따라 결과가 달라지는 판이었다. 해당 편의 판정 문장에 가정을 함께 적었다.</p>'+steps3([('모델은 창 안까지','대화하는 동안 모델은 배우지 않는다. 창에 넣어 준 글이 아는 것의 전부다.'),('그 너머는 장치가','멀리는 서랍이, 정확히는 원문과 찾기가, 지금에 맞게는 돌보기가 맡는다.'),('가장 좋은 기억은 없다','기록과 질문의 성격에 맞는 기억이 있을 뿐이다. 1-1부터 3-6까지 되풀이된 결론이다.')])+field('AI에게 일을 맡기기 전에 세 가지를 묻는다. 이 일에 필요한 과거가 AI에게 닿는가? 틀리면 안 되는 값이 원문 그대로 들어가는가? 넣어 주는 정보 가운데 낡은 것이 없는가? 셋 가운데 하나라도 아니면, 모델을 바꾸기 전에 넣어 주는 것을 고친다.','이 시리즈의 숫자는 대부분 설명용 모형에서 나왔다. 실제 모델과 실제 업무에서 재면 값이 달라진다. 가져갈 것은 숫자가 아니라 물음이다.'),
 outro=[('doc','front','시리즈의 한 줄이에요. LLM은 창 안까지 기억하고, 그 너머는 우리가 지어 준 만큼 기억해요.'),('asst','smile','창 밖의 단체 주문이 예측을 0만 원 바꾼 1-1에서, 여기까지 한 줄로 이어진 게 신기해요.'),('fly','coffee','결국 모델이 아니라 넣어 주는 쪽의 일이었군. 작게, 맞게, 낡지 않게. 그게 내 결론이야.'),('robo','happy','크게만 한다고 되는 게 아니었어. 그래도 서랍은 크게, 돌보는 장치는 든든하게! 그건 양보 못 해.'),('moa','report','열여덟 편의 기록을 날짜와 함께 모아 뒀어요. 필요한 편을 말씀하시면 그 장을 꺼내 드릴게요.')],
 examples=['30일 대화, 질문 12개, 쪽지 12장은 2부·3부와 같은 설명용 모형이다','층 켜고 끄기의 채점 규칙: 최근 원문은 27일·29일의 고친 말을 담는다. 프로필은 지금 상태 열 개를 담는다(100조각으로 침). 쪽지 꺼내 읽기는 지난 일 두 개와 지금 상태 열 개를 찾되, 돌보기가 꺼져 있으면 거래처와 회의에서 옛 쪽지를 꺼낸다. 층끼리 어긋나면 그 질문은 “불확실”(0.5)로 쳤다','대결의 “깊이 0.5”는 2-2의 설명용 모형이다. 네 층 쪽은 내용이 창의 끝 가까이에 놓인다고 봤다','세 축 표는 등급이 아니라 이 시리즈에서 본 경향을 글로 정리한 것이다','대결 전적 표는 각 편의 대결 결과를 모은 것이다'],
 refs=['cognee2026llmmemory','langmem2026concepts','fallahpour2026memorilla','liu2024lost','hochreiter1997long','ahn2026ts3_1_1'],
 claims=[('claim/context-not-long-term','문맥 창은 한 번의 추론에서 무엇을 처리할 수 있는지를, 장기 기억은 문맥이 끝난 뒤에도 정보가 남는지를 정한다','#lv1','cognee2026llmmemory','단기·장기 기억 절','concept/system-vs-model-memory'),
  ('claim/write-retrieve-maintain','기억 관리는 쓰기, 검색, 유지의 세 단계로 볼 수 있다','#lv2','cognee2026llmmemory','메모리 관리 3단계','concept/memory-maintenance'),
  ('claim/memorilla-future','Memorilla 저자는 기억과 검색을 결합하는 것을 다음 과제로 든다','#lv1','fallahpour2026memorilla','프로젝트 페이지 향후 방향','concept/memory-fidelity')],
 openq=[('question/mem-layer-conflict','기억의 층끼리 어긋날 때 무엇을 믿게 할까?','#lv2','아직 열린 질문'),('question/mem-detect-miss','찾기가 틀렸다는 것을 시스템이 어떻게 알아챌까?','#lv2','아직 열린 질문'),('question/mem-forgetting-right','지워 달라는 요청을 모든 서랍에서 어떻게 지킬까?','#lv1','모델 속에 새긴 것은 지웠는지 확인하기 어렵다 (2-3)')],
 nodes=[('concept/memory-length','Concept','길이 (얼마나 멀리)','memory length','#lv1','얼마나 먼 과거의 정보가 답에 닿을 수 있는가.'),
  ('concept/memory-fidelity','Concept','충실도 (얼마나 정확히)','memory fidelity','#lv1','닿은 정보가 얼마나 원래 내용 그대로인가.'),
  ('concept/memory-freshness','Concept','갱신 (얼마나 지금에 맞게)','memory freshness','#lv1','바뀐 사실이 얼마나 빨리, 틀림없이 반영되는가.'),
  ('concept/system-vs-model-memory','Concept','모델의 기억과 시스템의 기억','model memory vs system memory','#lv1','모델 스스로 가진 것(가중치와 창)과, 모델을 둘러싼 장치가 넣어 주는 것의 구분.'),
  ('concept/memory-layers','Concept','기억의 층','memory layers','#lv2','최근 원문, 프로필, 쪽지 꺼내 읽기, 돌보기처럼 맡은 일이 다른 기억의 겹.'),
  ('method/hybrid-memory','Method','섞어 쓰기','hybrid memory','#lv2','여러 기억 방식을 한 창에 층으로 겹쳐 쓰는 방법.'),
  ('concept/memory-maintenance','Concept','기억 돌보기 (유지)','memory maintenance','#lv2','어긋난 기억을 찾고, 지금 맞는 것을 표시하고, 이력을 남기는 일.'),
  ('sim/3-6-picker','Simulation','내 일에 맞는 기억 고르기','memory picker','#lv1'),('sim/3-6-layers','Simulation','네 층 켜고 끄기','layer ablation','#lv2'),('sim/3-6-duel','Simulation','대결: 네 층 vs 전부 넣기','duel: four layers vs full history','#vs')],
 edges=[('concept/memory-length','contrastsWith','concept/memory-fidelity','#lv1'),('concept/memory-fidelity','contrastsWith','concept/memory-freshness','#lv1'),('concept/system-vs-model-memory','prerequisiteOf','concept/memory-layers','#lv2'),('concept/memory-layers','partOf','method/hybrid-memory','#lv2'),('concept/memory-maintenance','partOf','method/hybrid-memory','#lv2'),
  ('method/hybrid-memory','raises','question/mem-layer-conflict','#lv2'),('method/hybrid-memory','raises','question/mem-detect-miss','#lv2'),('concept/memory-freshness','raises','question/mem-forgetting-right','#lv1'),
  ('concept/system-vs-model-memory','demonstratedBy','sim/3-6-picker','#lv1'),('concept/memory-layers','demonstratedBy','sim/3-6-layers','#lv2'),('method/hybrid-memory','demonstratedBy','sim/3-6-duel','#vs')],
 gloss={'길이':['길이','이 시리즈의 축','얼마나 먼 과거의 정보가 답에 닿을 수 있는가.'],'충실도':['충실도','이 시리즈의 축','닿은 정보가 얼마나 원래 내용 그대로인가.'],'갱신':['갱신','이 시리즈의 축','바뀐 사실이 얼마나 빨리, 틀림없이 반영되는가.'],'프로필':['프로필','적는 자리','주제마다 한 칸을 두고 새 말이 오면 고쳐 쓰는 기억.'],'쪽지':['쪽지','이 시리즈의 별명','대화에서 나온 말 하나를 날짜와 함께 적어 서랍에 넣은 것.'],
  '돌보기':['돌보기 (유지)','기억 관리','어긋난 기억을 찾고, 지금 맞는 것을 표시하고, 이력을 남기는 일.'],'창':['창 (문맥 창)','생성 AI','한 번에 읽을 수 있는 글의 범위.'],'서랍':['서랍 (바깥 저장소)','이 시리즈의 별명','모델 밖에 기록을 보관하는 곳.'],'기대값':['기대값','확률','가능성을 다 더한 값.']},
 core=['길이','충실도','갱신','돌보기','창'],
 quiz={'why':[Q('“LLM은 한 달 전까지 기억한다”는 답이 틀린 까닭은?',['한 달이 너무 길어서','창이 작으면 어제 일도 모르고, 서랍이 있으면 일 년 전 일도 꺼내서','모델이 날짜를 몰라서'],1,'어디까지 닿는지는 모델이 아니라 둘러싼 장치가 정해요.','세 축을 떠올려 보세요.','concept/system-vs-model-memory')],
  'lv1':[Q('“멀리 닿지만 거듭 줄일수록 세부를 잃는다”는 어느 방식일까?',['문맥 창','요약','꺼내 읽기'],1,'요약은 길이는 길지만 충실도가 떨어져요.','2-4를 떠올려 보세요.','concept/memory-fidelity'),
        Q('멀리, 정확히 기억해도 틀린 답이 나오는 경우는?',['기억이 낡았을 때','창이 클 때','쪽지가 적을 때'],0,'갱신이 안 되면 낡은 것을 정확하게 꺼내요.','세 번째 축이에요.','concept/memory-freshness')],
  'lv2':[Q('최근 원문 600 + 프로필 100 + 쪽지 두 장 80 + 질문 20이면 모두 몇 조각일까?',['760조각','800조각','840조각'],1,'600 + 100 + 80 + 20 = 800조각이에요.','쪽지가 두 장이에요.','concept/memory-layers','계산'),
        Q('돌보기 층을 껐을 때 가장 먼저 흔들리는 질문은?',['한 번도 바뀌지 않은 사실','중간에 바뀐 사실 (거래처, 회의 요일)','방금 한 말'],1,'옛 쪽지와 새 쪽지가 함께 있는 주제예요.','3-3을 떠올려 보세요.','concept/memory-maintenance')],
  'vs':[Q('이 시리즈가 열여덟 번의 대결로 되풀이한 결론은?',['큰 것이 이긴다','작은 것이 이긴다','가장 좋은 기억은 없고, 기록과 질문에 맞는 기억이 있다'],2,'초파리도 주판봇도 늘 이기지는 않았어요.','대결 전적 표를 다시 보세요.','concept/system-vs-model-memory')]},
)
JS=r'''
/* 칸 ① 고르기 */
var PA='one',PBv='no',PCv='no';
function pick(){var L=['<b>최근 원문</b>: 지금 하는 대화의 흐름을 잇는다 (늘 필요)'],why=[];
  if(PA==='one'){L.push('<b>쪽지 꺼내 읽기</b>: 답이 적힌 그 자료를 찾아 원문 그대로 넣는다');why.push('답이 한 곳에 그대로 있다면 찾아 읽기가 가장 정확해요 (2-5, 3-4).');}
  else{L.push('<b>요약 또는 요점 정리</b>: 여러 자료를 미리 맞춰 정리해 둔다');L.push('<b>쪽지 꺼내 읽기</b>: 근거가 되는 원문을 함께 찾는다');why.push('여러 곳을 맞춰 봐야 하면 찾아 읽기만으로는 놓쳐요. 미리 정리한 요점이 필요해요. 줄이면 세부를 잃으니 원문도 함께 둬요 (2-4, 3-4).');}
  if(PBv==='yes'){L.push('<b>돌보기</b>: 자료에 날짜를 붙이고, 바뀐 것은 옛것에 표시한다');why.push('자주 바뀌는 정보는 바깥 서랍에 두고 돌봐야 해요. 모델이 알고 있으리라 기대하면 낡은 답을 받아요 (2-3, 3-3).');}
  else why.push('거의 안 바뀌는 정보라면 돌보는 품을 줄일 수 있어요. 그래도 날짜는 붙여 둬요.');
  if(PCv==='yes'){L.push('<b>모음(이력 보관)</b>: 고쳐 쓰지 않고 날짜와 함께 쌓는다');why.push('지난 과정이 필요하면 덮어쓰면 안 돼요. 쌓아 두고 “지난 것” 표시를 해요 (3-2, 3-3).');}
  else{L.push('<b>프로필</b>: 주제마다 한 칸, 새 정보로 고쳐 쓴다');why.push('지금 상태만 필요하면 한 장에 고쳐 쓰는 프로필이 가볍고 틀릴 일이 적어요 (3-2).');}
  $('#ins1').innerHTML='<p class="g">이 일에 맞는 층</p><ul style="margin:6px 0 10px 18px">'+L.map(function(x){return '<li>'+x+'</li>';}).join('')+'</ul>'+why.map(function(x){return '<p>'+x+'</p>';}).join('');}
toggleGroup('#gA button',function(v){PA=v;pick();});toggleGroup('#gB button',function(v){PBv=v;pick();});toggleGroup('#gC button',function(v){PCv=v;pick();});pick();
/* 칸 ② 층 */
var ON={r:true,p:true,n:true,m:true},cv2=$('#c2'),QL12=QLAB.concat(['전 거래처','전 회의 요일']);
function score(on,dep){var T=(on.r?600:0)+(on.p?100:0)+(on.n?40:0)+20,pe=dep?useProb(Math.max(0.5,(T-60)/T),dep):1,out=[];
  QIDX.forEach(function(i){var ch=FACTS[i].sup!==undefined,src=[];if(on.r&&ch)src.push(1);if(on.p)src.push(1);if(on.n)src.push(ch&&!on.m?0:1);
    if(!src.length){out.push(0);return;}var good=src.filter(function(v){return v;}).length;out.push((good===src.length?1:(good?0.5:0))*pe);});
  out.push(on.n?pe:0);out.push(on.n?pe:0);return {v:out,n:out.reduce(function(a,b){return a+b;},0),cost:T};}
function board12(cvx,vals){var n=12,cols=cvx.clientWidth<520?2:4,rowsN=Math.ceil(n/cols),H=34+rowsN*50,W=fit(cvx,H),ctx=cvx.getContext('2d');ctx.clearRect(0,0,W,H);var gw=(W-16)/cols;txt(ctx,'질문 12개 (앞의 10개 = 지금 · 뒤의 2개 = 지난 일)',8,14,{size:11,color:COL.muted});
  vals.forEach(function(v,i){var x=8+(i%cols)*gw,y=28+Math.floor(i/cols)*50,c=v>=0.999?COL.gfp:(v<=0.001?COL.eye:COL.amber);rr(ctx,x+2,y,gw-4,42,8,'rgba(37,40,58,.9)',c);txt(ctx,QL12[i],x+10,y+14,{size:12,color:i>=10?COL.info:COL.text,w:'700'});txt(ctx,v>=0.999?'맞힘':(v<=0.001?'못 맞힘':'불확실 (층끼리 어긋남)'),x+10,y+29,{size:10,color:c});});stamp(ctx,W,'설명용 모형');}
function upd2(){var s=score(ON,0),names={r:'최근 원문',p:'프로필',n:'쪽지',m:'돌보기'},off=Object.keys(ON).filter(function(k){return !ON[k];}).map(function(k){return names[k];});
  kpis($('#k2'),[[(4-off.length)+'층','켠 층','i'],[s.cost.toLocaleString()+'조각','요청 하나에 읽는 글','a'],[f2(s.n,1)+' / 12','맞힌 질문',s.n>=11.9?'g':'r'],[off.length?off.join(' · '):'없음','끈 층','m']]);
  var m=s.n>=11.9?'<p class="g">열두 개를 다 맞혀요.</p>':'';
  if(!ON.n)m+='<p class="r">쪽지를 끄니 지난 일을 묻는 두 개에 답할 수 없어요. 프로필은 지금 상태만, 최근 원문은 최근 5일만 담고 있어요.</p>';
  if(ON.n&&!ON.m&&(ON.r||ON.p))m+='<p class="a">돌보기를 끄니 거래처와 회의에서 쪽지는 옛것을, 다른 층은 새것을 말해요. 층끼리 어긋나 불확실해요.</p>';
  if(ON.n&&!ON.m&&!ON.r&&!ON.p)m+='<p class="r">쪽지만 켜고 돌보지 않으니 거래처와 회의에서 옛 쪽지를 꺼내 틀려요.</p>';
  if(!ON.p&&!ON.n)m+='<p class="r">프로필도 쪽지도 없으니 최근 5일에 없는 것은 모두 못 맞혀요.</p>';
  $('#ins2').innerHTML=m||'<p>층을 꺼 보세요.</p>';drawAll();}
$$('#g2 button').forEach(function(b){b.addEventListener('click',function(){var k=b.dataset.k;ON[k]=!ON[k];b.setAttribute('aria-pressed',ON[k]?'true':'false');upd2();});});
addMod(cv2,function(){board12(cv2,score(ON,0).v);});
function fullScore(dep){var T=3600,cur=scoreMiddle(T,dep).n,h=[1,3].map(function(i){return useProb(1-factAge(i)/T,dep);});return cur+h[0]+h[1];}
var ALL={r:true,p:true,n:true,m:true};PAGE._T={all0:score(ALL,0).n,all5:score(ALL,0.5).n,cost:score(ALL,0).cost,full5:fullScore(0.5),full0:fullScore(0),noM:score({r:true,p:false,n:true,m:false},0).n,noN:score({r:true,p:true,n:false,m:true},0).n};
/* 대결 */
Duel({el:'#duel',higherIsBetter:true,drawMargin:0.05,fmt:function(v){return f2(v,1)+'개';},run:function(){return {fly:score(ALL,0.5).n,robo:fullScore(0.5),metric:'맞힐 질문 수'};},
  say:function(f,b){return tpl('열두 개 가운데 초파리 쪽 네 층이 {0}개, 주판봇 쪽 전부 넣기가 {1}개를 맞힐 것으로 기대돼요. 읽는 글은 760조각 대 3,600조각이에요.',f2(f,1),f2(b,1));},
  lessons:{F:'맞는 층을 겹친 작은 창이 통째로 넣은 큰 창을 앞섰다. 다만 찾기와 돌보기가 제대로 될 때의 이야기다',D:'이 가정에서는 둘이 비슷했다',R:'통째로 넣은 큰 창이 앞섰다'},
  after:function(){$('#duelNote').innerHTML=tpl('<p>가운데 놓침이 없다고 보면(깊이 0) 네 층 {0}개, 전부 넣기 {1}개로 비겨요. 돌보기와 프로필이 없으면 네 층 쪽은 {2}개로 내려가요. 마지막까지 가정이 승자를 정했어요.</p>',f2(score(ALL,0).n,1),f2(fullScore(0),1),f2(score({r:true,p:false,n:true,m:false},0.5).n,1));}});
/* 대결 전적 */
var REC=[['1부','1-2, 1-6','1-3, 1-5','1-1, 1-4'],['2부','2-2, 2-3, 2-6','2-1, 2-4, 2-5','—'],['3부','3-1, 3-6','3-3, 3-4, 3-5','3-2'],['합계','7승','8승','3무']];
$('#recTb').insertAdjacentHTML('beforeend',REC.map(function(r){return '<tr><td>'+r[0]+'</td><td>'+r[1]+'</td><td>'+r[2]+'</td><td>'+r[3]+'</td></tr>';}).join(''));
upd2();
'''
