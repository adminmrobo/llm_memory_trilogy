# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from h import *
from p2_1 import X1C
P=dict(
 title='언제 적을까 — 대화 중과 대화 뒤, 한 장과 여러 장',chip='쪽지 서랍 앵커',
 q='쪽지는 말하는 도중에 적을까, 끝나고 나서 적을까?',
 lead='<p>무엇을 적을지 정했으니 이제 <b>언제</b>와 <b>어디에</b>다. 대화하는 도중에 바로 적을 수도 있고, 대화가 끝난 뒤 조용히 정리할 수도 있다. 적는 자리도 둘이다. 한 장에 계속 고쳐 쓰는 <b>프로필</b>과, 쪽지를 계속 더하는 <b>모음</b>이다 [[langmem2026concepts]]. 어느 쪽이든 얻는 것과 내주는 것이 있다.</p>',
 objs=['대화 중에 적기와 대화 뒤에 적기의 장단점을 말한다','한 장에 고쳐 쓰기(프로필)와 쪽지 모으기(모음)가 각각 잘 답하는 질문을 구분한다','턴마다 붙는 기다림의 합을 계산한다'],mins=18,
 kpis=[('15초','턴마다 1.5초씩, 열 번 주고받을 때 늘어난 기다림'),('0초','대화 뒤에 적을 때 늘어난 기다림'),('10 / 12','프로필이 맞힌 질문'),('10 / 12','정리 안 한 모음이 맞힌 질문')],
 hero=['오늘은 적는 때와 적는 자리예요. 둘 다 정답이 하나가 아니에요.','질문을 열두 개로 늘렸어요. 지금 상태를 묻는 열 개에, 지난 일을 묻는 두 개를 더했어요.','한 장에 최신 것만 고쳐 쓰면 깔끔해. 옛날 건 왜 들고 있어?','쪽지는 버리는 게 아니야! 전부 모아 두면 옛날 일도 답할 수 있지.'],
 first3=['쪽지를 적는 때는 대화 중과 대화 뒤 둘이고, 적는 자리는 한 장에 고쳐 쓰기와 여러 장 모으기 둘이다.','AI의 기억 기능이 “방금 한 말을 다음 대화에서 모르는” 까닭, “예전 주소를 계속 쓰는” 까닭이 이 선택에서 나온다.','지금 상태만 필요한 정보(연락처, 선호)는 한 장에 고쳐 쓰고, 지난 과정이 필요한 정보(결정 이력)는 날짜와 함께 모은다.'],
 abbr=['LLM'],cast=dict(fly='한 장에 최신 것만',robo='전부 모아 둔다',**X1C),
 whyh='왜 때와 자리를 따지나',whytag='방법: 적는 때 둘, 적는 자리 둘',prev='3-1 무엇을 기억할까',
 why=[('적는 데도 값이 든다','무엇을 적을지 고르는 일은 품이 든다. 대화 도중에 하면 답이 늦어진다.'),('늦게 적으면 늦게 안다','대화 뒤에 적으면 답은 빠르지만, 정리가 끝나기 전의 다음 대화는 그 내용을 모른다.'),('자리가 답할 수 있는 질문을 정한다','한 장에 고쳐 쓰면 지난 일이 지워진다. 모으기만 하면 낡은 것이 섞인다.')],
 levels=[dict(id='lv1',no='①',title='대화 중에 적기와 대화 뒤에 적기',nav='적는 때',tag1='방법: 바로 적기 vs 끝나고 정리하기',tag2='일상: 통화하며 받아 적기 vs 끊고 나서 정리하기',
  why=('손님이 말하는 도중에 중요한 말이 나왔다. 서랍에 적어 둬야 한다.','대화 도중에 적으면 그 대화 안에서도, 바로 다음 대화에서도 쓸 수 있다. 하지만 적을지 말지 고르고 적는 동안 손님은 답을 기다린다. 대화 뒤에 적으면 기다림은 없지만, 정리가 끝날 때까지는 서랍에 없다.','두 방식을 놓고 턴마다 늘어나는 기다림과, 다음 대화에 반영되기까지의 시간을 견준다. 급한 것은 바로, 나머지는 나중에 적는 식으로 섞을 수도 있다.','통화하면서 받아 적으면 말이 끊기고, 끊고 나서 정리하면 그사이에 걸려 온 다음 전화에서는 메모가 아직 없다.'),
  math=dict(ask='턴마다 조금씩 늦어지는 게 그렇게 큰가요?',school='곱셈이다. 한 번의 지연에 횟수를 곱한다.',
   eq='늘어난 기다림의 합 = 턴마다 늘어나는 시간 × 주고받은 횟수',pieces=[('턴마다 늘어나는 시간','적을지 고르고 적는 데 드는 시간'),('주고받은 횟수','한 대화에서 말을 주고받은 횟수'),('대화 뒤에 적기','이 합이 0이다. 대신 반영이 늦다')],
   num='턴마다 1.5초가 는다고 하자. 열 번 주고받으면 1.5 × 10 = 15초다. 대화 뒤에 적으면 0초다. 대신 정리에 2시간이 걸린다면, 그 2시간 안에 시작한 다음 대화는 방금 한 말을 모른다.',comment='바로 적으면 기다림이 쌓이고, 나중에 적으면 한동안 모르는 시간이 생기네요. 둘 중 하나는 내줘야 하고요.'),
  pair=('통화하면서 받아 적는 사람은 중요한 말을 놓치지 않지만 대답이 한 박자씩 늦다. 통화를 끊고 정리하는 사람은 대화가 매끄럽지만, 정리하기 전에 다음 전화가 오면 빈손이다.','대화 중에 적기는 반영이 빠르지만 답이 늦어지고, 모델이 대화와 기록을 한꺼번에 챙겨야 한다. 대화 뒤에 적기는 답이 늦어지지 않고 대화 전체를 돌아보며 고를 수 있지만 반영이 늦다.'),
  talk=[('doc','front','하루에 대화가 세 번 있어요. 9시, 13시, 17시. 대화 뒤 정리에 몇 시간이 걸리면 다음 대화가 그 내용을 모를까요?'),('fly','arms','정리는 금방이지. 다음 대화 전에는 끝나. 정말 그럴까?'),('robo','chart','정리에 걸리는 시간을 5시간으로 밀어 봐. 13시 대화가 9시 일을 아는지!')],
  panel='<div class="panel"><h3>실험 — 적는 때에 따른 값</h3><div class="ctrl">'+rg('r1D','턴마다 늘어나는 시간 (초)',0.5,3,1.5,0.5)+rg('r1H','대화 뒤 정리에 걸리는 시간 (시간)',1,8,2)+'</div><div class="kpis" id="k1"></div>'+cv('c1','하루 시간표. 9시, 13시, 17시에 대화가 있고, 대화 뒤 정리 구간이 띠로 그려진다. 정리 구간이 다음 대화와 겹치면 그 대화는 앞의 내용을 모른다','wide')+'<div class="insight" id="ins1" aria-live="polite"></div></div>',
  report='보고드려요. 턴마다 1.5초면 열 번에 15초가 늘어요. 대화는 한 시간씩이고 다음 대화까지 세 시간이 비어요. 정리가 3시간을 넘기면 다음 대화가 앞의 내용을 모른 채 시작해요.',
  stepsh='무엇을 내주나',steps=['대화 중에 적기: 답이 늦어진다. 대신 바로 다음 대화가 안다.','대화 뒤에 적기: 답은 그대로다. 대신 정리가 끝날 때까지 모른다.','대화 뒤에 적으면 대화 전체를 보고 고를 수 있어 더 잘 가려 적는다.','그래서 “이건 꼭 기억해 줘” 같은 말은 바로 적고, 나머지는 나중에 정리하는 식으로 섞는다.'],
  lim='언제 적을지 정했다. 그러면 어디에 적을까? 같은 주제의 새 말이 오면 고쳐 쓸까, 한 장 더 넣을까? 다음 칸에서 본다.',
  concepts=['concept/hot-path-write','concept/background-write','concept/write-latency']),
 dict(id='lv2',no='②',title='한 장에 고쳐 쓰기와 쪽지 모으기',nav='적는 자리',tc='m',tag1='방법: 프로필(덮어쓰기) vs 모음(더하기)',tag2='일상: 명함첩의 한 칸 vs 편지 묶음',
  why=('손님의 거래처가 초록상사에서 파랑상사로 바뀌었다. 서랍에는 이미 “거래처는 초록상사” 쪽지가 있다.','쪽지를 한 장 더 넣기만 하면 두 장이 함께 남는다. 2-5에서 봤듯 오래된 쪽지를 꺼내면 틀린다.','두 가지 자리를 견준다. <b>프로필</b>은 주제마다 한 칸뿐이라 새 말이 오면 그 칸을 고쳐 쓴다. <b>모음</b>은 새 말이 올 때마다 날짜와 함께 한 장을 더한다.','명함첩에는 사람마다 한 칸이 있어 새 명함으로 바꿔 끼운다. 편지 묶음에는 받은 편지를 차례로 계속 쌓는다.'),whyh='왜 두 자리를 견주나',
  pair=('명함첩을 보면 지금 연락처를 바로 안다. 하지만 예전 회사가 어디였는지는 알 수 없다. 편지 묶음을 보면 언제 무슨 일이 있었는지 다 나온다. 하지만 지금 주소를 알려면 가장 최근 편지를 찾아야 한다.','프로필은 지금 상태를 빠르게 답하고 사람이 직접 열어 고치기도 쉽다. 지난 일은 답하지 못한다. 모음은 지난 일을 답할 수 있고 여러 대화에 걸친 지식을 쌓기 좋다. 대신 새 말과 옛말을 맞춰 정리해 주지 않으면 낡은 것이 섞인다.'),
  talk=[('doc','think','질문 열두 개예요. 열 개는 “지금 어떻죠?”, 두 개는 “전에는 어땠죠?”예요. 프로필과 모음은 각각 몇 개를 맞힐까요?'),('robo','happy','모음이 열두 개 다 맞히지! 전부 들고 있으니까.'),('fly','point','단추를 차례로 눌러 봐. 모음이 “지금”을 묻는 질문에서 어떻게 되는지.')],
  panel='<div class="panel"><h3>실험 — 자리와 질문 열두 개</h3><div class="ctrl">'+tg('g2','적는 자리',[('p','프로필 (고쳐 쓰기)'),('c','모음 (정리 안 함)'),('m','모음 (낡은 것 표시)')])+'</div><div class="kpis" id="k2"></div>'+cv('c2','질문 12개마다 맞혔는지 표시한 칸. 앞의 열 개는 지금 상태를, 뒤의 두 개는 지난 일을 묻는다')+'<div class="insight" id="ins2" aria-live="polite"></div></div>',
  report='보고드려요. 프로필은 지금을 묻는 열 개를 다 맞히고 지난 일 두 개를 못 맞혀 10개예요. 정리 안 한 모음은 지난 일 두 개를 맞히지만 거래처와 회의에서 낡은 쪽지를 꺼내 역시 10개예요.',
  stepsh='자리에 따라 갈리는 답',steps=['“거래처가 어디죠?” 프로필은 파랑상사. 정리 안 한 모음은 초록상사를 꺼낼 수 있다.','“전에는 어디였죠?” 프로필은 모른다. 지웠기 때문이다. 모음은 초록상사라고 답한다.','모음에서 낡은 쪽지에 “27일에 바뀜” 표시를 해 두면 둘 다 맞힌다.','그 표시를 하는 일이 3-3의 주제, 기억 돌보기다.'],
  lim='프로필은 지난 일을 잃고, 모음은 돌보지 않으면 낡은 것이 섞인다. 모음을 쓰려면 낡은 쪽지를 가려내는 일이 따라붙는다. 3-3에서 그 일을 본다.',
  intern=SIA,concepts=['concept/profile-memory','concept/collection-memory','limitation/profile-loses-history'])],
 duel=dict(title='프로필 vs 모음 — 질문 열두 개',metric='맞힌 질문 수',tag='일상: 명함첩 vs 편지 묶음',q='지금 상태를 묻는 질문 열 개와 지난 일을 묻는 질문 두 개. 한 장에 고쳐 쓴 프로필과, 쪽지를 더하기만 한 모음 가운데 누가 더 많이 맞힐까?',
  fly=('프로필 — 주제마다 한 칸, 새 말이 오면 고쳐 쓴다','최신 것 하나면 돼. 옛날 건 지워.'),robo=('모음 — 쪽지 열두 장을 더하기만 한다 (정리 안 함)','하나도 안 버렸어. 옛날 일도 다 답해!'),rule='맞힌 질문 수(많을수록 좋음). 모음은 같은 주제의 쪽지가 여럿이면 먼저 넣은 것을 꺼낸다고 본다.'),
 sumh='정리 — 때와 자리',
 sum='<div class="tw"><table class="tb"><tr><th></th><th>얻는 것</th><th>내주는 것</th><th>알맞은 곳</th></tr><tr><td><b>대화 중에 적기</b></td><td>바로 반영된다</td><td>답이 늦어진다</td><td>“이건 꼭 기억해 줘”라고 한 말</td></tr><tr><td><b>대화 뒤에 적기</b></td><td>답이 늦어지지 않는다. 전체를 보고 고른다</td><td>반영이 늦다</td><td>대화에서 드러난 습관과 흐름</td></tr><tr><td><b>프로필</b></td><td>지금 상태를 바로 안다. 사람이 고치기 쉽다</td><td>지난 일을 잃는다</td><td>이름, 선호, 연락처</td></tr><tr><td><b>모음</b></td><td>지난 일을 안다. 지식이 쌓인다</td><td>돌보지 않으면 낡은 것이 섞인다</td><td>결정 이력, 겪은 일</td></tr></table></div>'+steps3([('때를 고른다','급한 것은 바로, 나머지는 나중에.'),('자리를 고른다','지금만 필요하면 한 장에, 과정이 필요하면 여러 장에.'),('모으면 돌봐야 한다','더하기만 한 모음은 프로필보다 낫지 않았다.')])+field('AI 기억 기능을 쓸 때, 바뀔 수 있는 정보(담당자, 주소)는 “고쳐 달라”고 분명히 말한다. “추가로 기억해 줘”라고만 하면 옛 정보와 새 정보가 함께 남을 수 있다.','실제 서비스의 기억 기능이 어느 방식을 쓰는지는 서비스마다 다르다. 이 페이지의 시간(1.5초, 2시간)은 계산을 위해 정한 숫자다.'),
 outro=[('doc','front','오늘의 한 줄이에요. 언제 적고 어디에 적는지가, 무엇을 답할 수 있는지를 정해요.'),('asst','smile','프로필과 정리 안 한 모음이 똑같이 10개였던 게 뜻밖이었어요. 틀린 질문은 서로 달랐고요.'),('fly','coffee','비겼군. 옛날 일을 묻는 질문은 내가 못 맞혔어. 지운 게 아쉽긴 하네.'),('robo','meh','전부 모았는데 낡은 쪽지 때문에 두 개나 틀렸어… 표시만 해 뒀어도 열두 개였는데!'),('moa','report','거래처와 회의 쪽지에 “바뀜” 표시를 달아 둘게요. 다음 편에서 제대로 정리해요.')],
 examples=['질문 열두 개: 2부의 질문 10개(지금 상태)에 “전에는 거래처가 어디였죠?”, “회의가 원래 무슨 요일이었죠?” 두 개(지난 일)를 더했다','모음(정리 안 함)은 같은 주제의 쪽지 가운데 먼저 넣은 것을 꺼낸다고 가정했다. 실제 검색은 어느 것을 꺼낼지 정해져 있지 않다','턴마다 1.5초, 정리에 2시간, 하루 세 번의 대화(9시·13시·17시)는 계산을 위해 정한 숫자다','채점은 규칙으로 계산한 값이다'],
 refs=['langmem2026concepts','cognee2026llmmemory'],
 claims=[('claim/hot-path-vs-background','대화 중 저장은 즉각 반영되지만 응답 지연이 생기고, 대화 뒤 저장은 응답 지연이 없지만 갱신이 늦다','#lv1','langmem2026concepts','메모리 형성 시점 표','concept/hot-path-write'),
  ('claim/profile-vs-collection','프로필은 현재 상태를 나타내는 단일 문서로 새 정보가 오면 갱신하고, 모음은 개별 기록을 저장해 실행 시점에 검색한다','#lv2','langmem2026concepts','Semantic 메모리의 두 방식','concept/profile-memory')],
 openq=[('question/mem-how-to-maintain','모음에 섞인 낡은 쪽지를 어떻게 가려낼까?','#lv2','3-3에서 다룬다')],
 nodes=[('concept/hot-path-write','Concept','대화 중에 적기','hot-path memory formation','#lv1','대화가 진행되는 동안 바로 기억을 저장하는 방식.'),
  ('concept/background-write','Concept','대화 뒤에 적기','background memory formation','#lv1','대화가 끝난 뒤 돌아보며 기억을 뽑아 저장하는 방식.'),
  ('concept/write-latency','Concept','적느라 늘어나는 기다림','write latency','#lv1','기억을 고르고 저장하는 동안 답이 늦어지는 시간.'),
  ('concept/profile-memory','Concept','프로필 (한 장에 고쳐 쓰기)','profile memory','#lv2','주제마다 한 칸을 두고 새 정보가 오면 그 칸을 고쳐 쓰는 기억.'),
  ('concept/collection-memory','Concept','모음 (쪽지 더하기)','collection memory','#lv2','새 정보가 올 때마다 기록을 하나씩 더하고 필요할 때 찾아 쓰는 기억.'),
  ('limitation/profile-loses-history','Limitation','고쳐 쓰면 지난 일을 잃는다','overwriting loses history','#lv2','프로필은 지금 상태만 남기므로 이전 값을 답할 수 없다.'),
  ('sim/3-2-timing','Simulation','적는 때에 따른 값','write timing tradeoff','#lv1'),('sim/3-2-place','Simulation','자리와 질문 열두 개','profile vs collection','#lv2'),('sim/3-2-duel','Simulation','대결: 프로필 vs 모음','duel: profile vs collection','#vs')],
 edges=[('concept/hot-path-write','contrastsWith','concept/background-write','#lv1'),('concept/hot-path-write','hasLimitation','concept/write-latency','#lv1'),('concept/profile-memory','contrastsWith','concept/collection-memory','#lv2'),('concept/profile-memory','hasLimitation','limitation/profile-loses-history','#lv2'),
  ('concept/collection-memory','raises','question/mem-how-to-maintain','#lv2'),('concept/write-latency','demonstratedBy','sim/3-2-timing','#lv1'),('concept/profile-memory','demonstratedBy','sim/3-2-place','#lv2'),('concept/collection-memory','demonstratedBy','sim/3-2-duel','#vs')],
 gloss={'프로필':['프로필','적는 자리','주제마다 한 칸을 두고 새 말이 오면 고쳐 쓰는 기억. 지금 상태만 남는다.'],'모음':['모음','적는 자리','새 말이 올 때마다 쪽지를 한 장씩 더하는 기억. 지난 일도 남는다.'],'턴':['턴','쓰임','말을 한 번 주고받는 것.'],'쪽지':['쪽지','이 시리즈의 별명','대화에서 나온 말 하나를 날짜와 함께 적어 서랍에 넣은 것.'],'정리':['정리','쓰임','대화가 끝난 뒤 돌아보며 기억할 것을 골라 서랍에 넣는 일.'],'서랍':['서랍 (바깥 저장소)','이 시리즈의 별명','모델 밖에 기록을 보관하는 곳.']},
 core=['프로필','모음','턴','정리'],
 quiz={'why':[Q('대화 뒤에 적을 때 생기는 문제는?',['답이 늦어진다','정리가 끝나기 전의 다음 대화는 그 내용을 모른다','쪽지가 너무 많아진다'],1,'반영이 늦어요.','“늦게 적으면 늦게 안다”를 떠올려 보세요.','concept/background-write')],
  'lv1':[Q('턴마다 2초가 늘고 열두 번 주고받으면 늘어난 기다림은?',['12초','24초','36초'],1,'2 × 12 = 24초예요.','곱셈 한 번이에요.','concept/write-latency','계산'),
        Q('“이건 꼭 기억해 줘”라는 말은 언제 적는 것이 알맞을까?',['대화 중에 바로','다음 달에','적지 않는다'],0,'바로 다음 대화에서도 써야 하니까요.','급한 것과 나머지를 갈라 보세요.','concept/hot-path-write')],
  'lv2':[Q('프로필이 답하지 못하는 질문은?',['지금 거래처가 어디죠?','전에는 거래처가 어디였죠?','커피는 뭘 마시죠?'],1,'고쳐 쓰면서 옛 값을 지웠어요.','명함첩을 떠올려 보세요.','limitation/profile-loses-history'),
        Q('더하기만 한 모음이 “지금 거래처”를 틀릴 수 있는 까닭은?',['쪽지가 없어서','옛 쪽지와 새 쪽지가 함께 있어 옛 것을 꺼낼 수 있어서','모델이 잊어서'],1,'낡은 쪽지가 그대로 남아 있어요.','2-5의 거래처 쪽지 두 장을 떠올려 보세요.','concept/collection-memory')],
  'vs':[Q('비긴 이 대결에서 두 선수가 틀린 질문은',['서로 같다','서로 다르다. 프로필은 지난 일, 모음은 바뀐 지금 상태','둘 다 전부 맞혔다'],1,'점수는 같아도 약한 곳이 달라요.','질문판을 다시 떠올려 보세요.','concept/profile-memory')]},
)
JS=r'''
var DL=1.5,HR=2,cv=$('#c1'),TALKS=[9,13,17];
function upd1(){var miss=0;TALKS.forEach(function(t,i){if(i>0&&TALKS[i-1]+1+HR>t)miss++;});
  kpis($('#k1'),[[f2(DL*10,1)+'초','대화 중에 적기: 열 번 주고받을 때 늘어난 기다림','r'],['0초','대화 뒤에 적기: 늘어난 기다림','g'],[HR+'시간','대화 뒤 정리에 걸리는 시간','a'],[miss+'번','앞 내용을 모른 채 시작한 대화 (하루 세 번 가운데)',miss?'r':'g']]);
  $('#ins1').innerHTML=miss?tpl('<p class="r">정리가 {0}시간 걸려 다음 대화와 겹쳐요. {1}번의 대화가 앞의 내용을 모른 채 시작해요.</p>',HR,miss):tpl('<p class="g">정리가 다음 대화 전에 끝나요. 대화 뒤에 적어도 놓치는 대화가 없어요. 대화 중에 적으면 턴마다 {0}초씩 답이 늦어져요.</p>',f2(DL,1));drawAll();}
bindRange('r1D',function(v){DL=v;upd1();},function(v){return f2(v,1)+'초';});bindRange('r1H',function(v){HR=v;upd1();},function(v){return v+'시간';});
addMod(cv,function(){var H=130,W=fit(cv,H),ctx=cv.getContext('2d');ctx.clearRect(0,0,W,H);var x0=40,x1=W-16,X=function(h){return x0+(h-8)/16*(x1-x0);};
  for(var h=8;h<=24;h+=2){txt(ctx,h+'시',X(h),112,{size:10,color:COL.muted,align:'center'});ctx.strokeStyle='rgba(157,155,184,.15)';ctx.beginPath();ctx.moveTo(X(h),30);ctx.lineTo(X(h),100);ctx.stroke();}
  TALKS.forEach(function(t,i){rr(ctx,X(t+1),64,X(t+1+HR)-X(t+1),20,4,'rgba(214,114,214,.4)',COL.stain);var bad=i>0&&TALKS[i-1]+1+HR>t;rr(ctx,X(t),36,X(t+1)-X(t),24,4,bad?'rgba(240,96,77,.55)':'rgba(94,227,156,.55)',bad?COL.eye:COL.gfp);txt(ctx,bad?'모름':'대화',X(t+0.5),48,{size:10,color:COL.text,align:'center',w:'700'});});
  txt(ctx,'초록·빨강 = 대화 · 보라 = 대화 뒤 정리',x0,16,{size:10,color:COL.muted});stamp(ctx,W,'설명용 도식');});
/* 칸 ② : 질문 12개 = 지금 10 + 지난 일 2 */
var QL12=QLAB.concat(['전 거래처','전 회의 요일']),PL='p',cv2=$('#c2');
function score12(m){var cur=QIDX.map(function(i){if(m==='c')return FACTS[i].sup===undefined?1:0;return 1;}),hist=m==='p'?[0,0]:[1,1];return cur.concat(hist);}
function board12(cvx,vals){var n=12,cols=cvx.clientWidth<520?2:4,rowsN=Math.ceil(n/cols),H=34+rowsN*50,W=fit(cvx,H),ctx=cvx.getContext('2d');ctx.clearRect(0,0,W,H);var gw=(W-16)/cols;txt(ctx,'질문 12개 (앞의 10개 = 지금 · 뒤의 2개 = 지난 일)',8,14,{size:11,color:COL.muted});
  vals.forEach(function(v,i){var x=8+(i%cols)*gw,y=28+Math.floor(i/cols)*50,c=v?COL.gfp:COL.eye;rr(ctx,x+2,y,gw-4,42,8,'rgba(37,40,58,.9)',c);txt(ctx,QL12[i],x+10,y+14,{size:12,color:i>=10?COL.info:COL.text,w:'700'});txt(ctx,v?'맞힘':'못 맞힘',x+10,y+29,{size:10,color:c});});stamp(ctx,W,'설명용 모형');}
function upd2(){var s=score12(PL),n=s.reduce(function(a,b){return a+b;},0),cur=s.slice(0,10).reduce(function(a,b){return a+b;},0);
  kpis($('#k2'),[[{p:'프로필',c:'모음 (정리 안 함)',m:'모음 (낡은 것 표시)'}[PL],'적는 자리','a'],[cur+' / 10','지금을 묻는 질문',cur===10?'g':'r'],[(n-cur)+' / 2','지난 일을 묻는 질문',n-cur===2?'g':'r'],[n+' / 12','모두',n===12?'g':'a']]);
  $('#ins2').innerHTML={p:'<p class="a">지금 상태는 다 맞혀요. 거래처와 회의 요일을 고쳐 썼기 때문이에요. 하지만 고쳐 쓰면서 옛 값을 지워 “전에는?”에 답하지 못해요.</p>',c:'<p class="a">지난 일은 맞혀요. 옛 쪽지가 남아 있으니까요. 하지만 거래처와 회의 요일은 옛 쪽지를 먼저 꺼내 틀려요.</p>',m:'<p class="g">옛 쪽지에 “바뀜” 표시를 해 뒀어요. 지금을 물으면 새 쪽지를, 지난 일을 물으면 옛 쪽지를 꺼내요. 열두 개를 다 맞혀요.</p>'}[PL];drawAll();}
toggleGroup('#g2 button',function(v){PL=v;upd2();});addMod(cv2,function(){board12(cv2,score12(PL));});
function tot(m){return score12(m).reduce(function(a,b){return a+b;},0);}PAGE._T={p:tot('p'),c:tot('c'),m:tot('m')};
/* 대결 */
Duel({el:'#duel',higherIsBetter:true,drawMargin:0.05,fmt:function(v){return v+'개';},run:function(){return {fly:tot('p'),robo:tot('c'),metric:'맞힌 질문 수'};},
  say:function(f,b){return tpl('열두 개 가운데 초파리 쪽 프로필이 {0}개, 주판봇 쪽 모음이 {1}개를 맞혔어요. 프로필은 지난 일 두 개를, 모음은 바뀐 거래처와 회의 요일을 틀렸어요.',f,b);},
  lessons:{D:'프로필은 지금을, 모음은 지난 일을 안다. 점수는 같아도 틀린 곳이 다르다',F:'한 장에 고쳐 쓴 쪽이 앞섰다',R:'모아 둔 쪽이 앞섰다'},
  after:function(){$('#duelNote').innerHTML=tpl('<p>모음의 옛 쪽지에 “바뀜” 표시만 해 두면 {0}개를 다 맞혀요. 모으는 것만으로는 모자라고, 돌봐야 해요.</p>',tot('m'));}});
upd1();upd2();
'''
