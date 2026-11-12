# -*- coding: utf-8 -*-
PID='mem3_1-1'; NUM='1-1'
FILE='1_1_window_is_memory.html'
TITLE='창 밖은 없는 것 — 창 길이가 곧 기억의 길이'
SERIES='기억 3부작 — LLM은 어디까지 기억할 수 있을까'
DESC='모델은 책상에 펼쳐 놓지 않은 과거를 기억할 수 있을까?'
DATE='2026-11-12'
ANCHOR='C'

G={
 '시계열':['시계열','데이터','시간 순서대로 적힌 값의 줄. 순서를 섞으면 뜻이 사라진다.'],
 '창':['창 (window)','설정값','다음 값을 짐작할 때 펼쳐 놓는 과거 구간. 거슬러 보는 날 수(lookback)와 같은 말로 쓴다.'],
 '창 길이':['창 길이','설정값','창에 들어가는 날 수. 이 페이지의 모델에서는 기억의 길이와 같다.'],
 '문맥 창':['문맥 창 (context window)','생성 AI','대화형 AI가 한 번에 읽고 쓸 수 있는 글의 양. 넘친 부분은 모델에게 보이지 않는다.'],
 '자기회귀':['자기회귀 (AR)','통계 모델','자기 과거 값에 정해진 비율을 곱해 더해서 다음 값을 짐작하는 방법.'],
 '비율':['비율 (계수 φ)','통계 모델','과거 값마다 곱하는 정해진 숫자. 훈련이 끝나면 입력이 무엇이든 그대로다.'],
 '기본값':['기본값 (상수 c)','통계 모델','과거 값과 상관없이 늘 더하는 숫자.'],
 '훈련':['훈련 데이터','평가','비율을 정하는 데 쓰는 기록. 이 페이지에서는 앞 200일.'],
 '검증':['검증 데이터','평가','창 길이 같은 설정을 고를 때 쓰는 기록. 모델이 비율을 정할 때는 본 적이 없다.'],
 '검증 오차':['검증 오차','지표','검증 기간에서 예측이 실제와 평균적으로 얼마나 다른지. 단위는 만 원.'],
 '훈련 오차':['훈련 오차','지표','비율을 정할 때 쓴 바로 그 기록에서 잰 오차. 낮다고 실력이 좋은 것은 아니다.'],
 '연습 문제':['연습 문제 (학습 샘플)','데이터','(창, 정답 하루) 한 쌍. 창이 길수록 만들 수 있는 개수가 준다.'],
 '과적합':['과적합','학습','훈련 기록의 우연한 출렁임까지 외워서 처음 보는 기록에서 성적이 떨어지는 현상.'],
 '평균 절대 오차':['평균 절대 오차 (MAE)','지표','예측과 실제의 차이를 크기만 모아 평균 낸 값.'],
 '요일 흐름':['요일 흐름','데이터','요일마다 되풀이되는 오르내림. 7일 주기.'],
 'lookback':['lookback','설정값','거슬러 보는 과거 날 수. 이 페이지의 “창 길이”.'],
}
CORE=['창','문맥 창','자기회귀','검증 오차','과적합','연습 문제']

QUIZ={
 'why':[{'q':'이 시리즈가 “창”에서 시작하는 까닭으로 맞는 것은?','o':['창이 가장 성능 좋은 기억이라서','펼친 만큼만 본다는 가장 단순한 기억이라서','대화형 AI에는 창이 없어서'],'a':1,'why':'단순한 기억이 어디서 막히는지 알아야 다음 방법이 왜 나왔는지 보여요.','hint':'가장 단순한 것부터 시작해요.'}],
 'lv1':[
  {'kind':'계산','q':'기본값 20, 어제 비율 0.5, 그제 비율 0.3인 2일 창. 어제 80만 원, 그제 100만 원이면 내일 짐작값은?','o':['90만 원','100만 원','110만 원'],'a':0,'why':'20 + 0.5×80 + 0.3×100 = 20 + 40 + 30 = 90이에요.','hint':'곱셈 두 번, 덧셈 두 번이에요.'},
  {'q':'14일 창을 쓰는 모델에서, 20일 전에 매출이 크게 뛴 일은 오늘 예측을 얼마나 바꿀까?','o':['뛴 만큼 그대로 바꾼다','조금 바꾼다','전혀 바꾸지 않는다'],'a':2,'why':'20일 전 값은 창 밖이라 계산에 들어갈 자리가 없어요.','hint':'식에 20일 전 값이 들어갈 자리가 있나요?'}],
 'lv2':[
  {'kind':'계산','q':'훈련 기록이 200일이고 창이 30일이면 연습 문제는 몇 개?','o':['200개','170개','30개'],'a':1,'why':'200 − 30 = 170개예요. 맨 앞 30일은 정답으로 쓸 수 없어요.','hint':'연습 문제 수 = 200 − 창 길이.'},
  {'q':'100일 창에서 훈련 오차는 0인데 검증 오차가 크게 나온 까닭은?','o':['먼 과거가 쓸모없어서','문제보다 정할 숫자가 많아 훈련 기록을 통째로 외워서','검증 기록이 잘못돼서'],'a':1,'why':'문제 100개에 숫자 101개라 훈련 문제는 다 맞히게 끼워 맞출 수 있지만, 처음 보는 날에는 통하지 않아요.','hint':'연습 문제 수와 정할 숫자 수를 견줘 보세요.'}],
 'vs':[{'q':'7일 창과 80일 창이 비긴 결과에서 얻을 교훈은?','o':['창 길이는 성적과 상관없다','기억을 늘리면 얻는 것과 잃는 것이 함께 있다','언제나 짧은 창이 낫다'],'a':1,'why':'긴 창은 더 멀리 보지만 연습 문제가 줄고 외울 숫자가 늘어요. 둘 사이의 28일 창은 두 선수보다 나았어요.','hint':'28일 창의 성적을 떠올려 보세요.'}],
}

# ---- 지식 그래프 ----
def N(id,typ,ko,en,anchor,d=None,**kw):
    n={'id':id,'type':typ,'label':{'ko':ko,'en':en},'page':PID,'anchor':anchor,'domain':['ai','stats'],'status':kw.pop('status','known'),'confidence':kw.pop('confidence','high')}
    if d: n['definition']={'ko':d}
    n.update(kw); n['level']=1; return n
C='lab:concept/'; M='lab:method/'; S='lab:section/1-1/'
NODES=[
 N(C+'time-series','Concept','시계열','time series','#why',G['시계열'][2],family='sequence'),
 N(C+'lookback','Concept','창 길이 (lookback)','lookback','#lv1',G['lookback'][2]+' '+G['창 길이'][2],family='sequence',altLabel={'ko':['룩백','거슬러 보는 날 수']}),
 N(C+'sliding-window','Concept','창 (window)','sliding window','#lv1',G['창'][2],family='sequence'),
 N(C+'memory-horizon','Concept','기억의 길이','memory horizon','#lv1','모델의 예측에 영향을 줄 수 있는 가장 먼 과거까지의 거리. 창 모델에서는 창 길이와 같다.',family='memory'),
 N(C+'context-window','Concept','문맥 창','context window','#lv1',G['문맥 창'][2],family='memory'),
 N(C+'overfitting','Concept','과적합','overfitting','#lv2',G['과적합'][2],family='evaluation'),
 N(C+'validation-set','Concept','검증 데이터','validation set','#lv2',G['검증'][2],family='evaluation'),
 N(C+'training-sample','Concept','연습 문제 (학습 샘플)','training sample','#lv2',G['연습 문제'][2],family='sequence'),
 N(M+'ar-model','Method','자기회귀 (AR)','autoregressive model','#lv1',G['자기회귀'][2],family='sequence'),
 N(M+'naive-forecast','Method','어제 값 그대로 (나이브 예측)','naive forecast','#lv1','내일 값을 오늘 값으로 두는 가장 쉬운 기준선.',family='sequence'),
 N('lab:metric/mae','Metric','평균 절대 오차 (MAE)','mean absolute error','#lv2',G['평균 절대 오차'][2],family='evaluation'),
 N('lab:task/one-step-forecast','Task','다음 날 예측','one-step-ahead forecasting','#lv1','직전 창으로 바로 다음 하루를 맞히는 문제.',family='sequence'),
 N('lab:limitation/window-blindness','Limitation','창 밖은 보이지 않는다','no access outside the window','#lv1','창 밖의 값은 계산에 들어갈 길이 없어, 아무리 큰 사건이어도 예측을 바꾸지 못한다.',family='memory'),
 N('lab:limitation/window-cost','Limitation','창을 늘리는 값','cost of a longer window','#lv2','창을 하루 늘릴 때마다 연습 문제가 하나 줄고 정할 숫자가 하나 늘어, 어느 지점부터 과적합이 생긴다.',family='memory'),
 N('lab:analogy/desk-pages','Analogy','책상에 펼친 쪽만 보는 계산원','pages open on the desk','#lv1','창을 책상에 펼친 매출 기록 쪽수로 비유. 한계: 사람은 서랍을 열 수 있지만 창 모델은 열 수 없다.',family='memory'),
 N('lab:sim/1-1-outside-event','Simulation','창 밖에서 일어난 일','event outside the window','#lv1'),
 N('lab:sim/1-1-length-score','Simulation','창 길이별 성적표','validation error by window length','#lv2'),
 N('lab:sim/1-1-duel','Simulation','대결: 7일 창 vs 80일 창','duel: 7-day vs 80-day window','#vs'),
 N('lab:claim/box-jenkins-arima','Claim','자기회귀를 포함한 ARIMA 방법론은 Box와 Jenkins(1970)가 체계화했다','','#lv1',evidence=['F01'],source=[{'work':'box1970time','loc':'책 전체','verified':True}]),
 N('lab:claim/context-window-limit','Claim','문맥 창은 한 번의 추론에서 처리할 수 있는 글의 양을 제한한다','','#lv1',evidence=['F02'],source=[{'work':'cognee2026llmmemory','loc':'컨텍스트 윈도우 절','verified':True}]),
 N('lab:claim/window-outside-zero','Claim','이 페이지의 자기회귀 모델에서 창 밖 사건은 예측을 0만 원 바꾼다','','#lv1',evidence=['F03'],confidence='high',source=[{'work':'ahn2026ts3_1_1','loc':'계산 방법(AR 최소제곱)','verified':True}]),
 N('lab:question/mem-1-1-core','Question','모델은 책상에 펼쳐 놓지 않은 과거를 기억할 수 있을까?','','#top','이 페이지의 핵심 질문'),
 N('lab:question/mem-how-fast-fades','Question','과거의 영향은 얼마나 빨리 꺼질까?','','#lv2','1-2에서 자기상관으로 잰다',status='open'),
 N('lab:question/mem-other-memory','Question','창을 늘리지 않고 먼 과거를 기억하는 방법이 있을까?','','#sum','1-4, 1-5에서 읽으며 고쳐 쓰는 메모로 다룬다',status='open'),
 N(S+'why','Section','왜 “창”에서 시작할까','','#why'),
 N(S+'big','Section','큰 그림 — 열여덟 편의 길','','#big'),
 N(S+'lv1','Section','창 = 기억의 길이','','#lv1'),
 N(S+'lv2','Section','창을 늘리면 다 기억할까','','#lv2'),
 N(S+'vs','Section','대결 — 7일 vs 80일','','#vs'),
 N(S+'sum','Section','정리','','#sum'),
 N('lab:work/box1970time','Work','Time Series Analysis: Forecasting and Control','Time Series Analysis: Forecasting and Control','#src-box1970time'),
 N('lab:work/cognee2026llmmemory','Work','LLM Memory (cognee)','LLM Memory (cognee)','#src-cognee2026llmmemory'),
 N('lab:work/ahn2026ts3_1_1','Work','시계열 3부작 1-1 — lookback과 window, 같은 말일까?','','#src-ahn2026ts3_1_1'),
]
for sec,qs in QUIZ.items():
    for i,q in enumerate(qs):
        NODES.append(N('lab:quiz/mem-1-1-%s-%d'%(sec,i+1),'QuizItem',(q['q'][:34]+'…') if len(q['q'])>34 else q['q'],'','#'+sec))
def E(s,p,o,a,**kw):
    e={'s':s,'p':'lab:'+p,'o':o,'anchor':a,'confidence':'high'}; e.update(kw); return e
EDGES=[
 E(C+'time-series','prerequisiteOf',C+'sliding-window','#why'),
 E(C+'lookback','partOf',C+'sliding-window','#lv1'),
 E(C+'sliding-window','prerequisiteOf',C+'memory-horizon','#lv1'),
 E(C+'memory-horizon','prerequisiteOf',C+'context-window','#lv1'),
 E(M+'ar-model','solves','lab:task/one-step-forecast','#lv1'),
 E(M+'naive-forecast','contrastsWith',M+'ar-model','#lv1'),
 E(M+'ar-model','hasLimitation','lab:limitation/window-blindness','#lv1'),
 E(M+'ar-model','hasLimitation','lab:limitation/window-cost','#lv2'),
 E('lab:limitation/window-cost','raises','lab:question/mem-how-fast-fades','#lv2'),
 E('lab:limitation/window-blindness','raises','lab:question/mem-other-memory','#sum'),
 E(C+'sliding-window','raises','lab:question/mem-1-1-core','#top'),
 E('lab:analogy/desk-pages','analogyOf',C+'sliding-window','#lv1'),
 E(C+'context-window','broader',C+'sliding-window','#lv1',confidence='medium'),
 E(C+'training-sample','partOf',C+'sliding-window','#lv2'),
 E(C+'overfitting','demonstratedBy','lab:sim/1-1-length-score','#lv2'),
 E('lab:limitation/window-blindness','demonstratedBy','lab:sim/1-1-outside-event','#lv1'),
 E('lab:limitation/window-cost','demonstratedBy','lab:sim/1-1-duel','#vs'),
 E('lab:metric/mae','partOf',C+'validation-set','#lv2',confidence='medium'),
 E('lab:claim/box-jenkins-arima','supports',M+'ar-model','#lv1',evidence=['F01']),
 E('lab:claim/box-jenkins-arima','assertedIn','lab:work/box1970time','#lv1',evidence=['F01']),
 E('lab:claim/context-window-limit','supports',C+'context-window','#lv1',evidence=['F02']),
 E('lab:claim/context-window-limit','assertedIn','lab:work/cognee2026llmmemory','#lv1',evidence=['F02']),
 E('lab:claim/window-outside-zero','supports','lab:limitation/window-blindness','#lv1',evidence=['F03']),
 E('lab:claim/window-outside-zero','assertedIn','lab:work/ahn2026ts3_1_1','#lv1',evidence=['F03']),
]
SEC={ 'why':[C+'time-series'], 'lv1':[C+'lookback',C+'sliding-window',C+'memory-horizon',C+'context-window',M+'ar-model',M+'naive-forecast','lab:task/one-step-forecast','lab:limitation/window-blindness','lab:analogy/desk-pages'],
 'lv2':[C+'overfitting',C+'validation-set',C+'training-sample','lab:metric/mae','lab:limitation/window-cost'] }
for sec,ids in SEC.items():
    for i in ids: EDGES.append(E(i,'explainedIn',S+sec,'#'+sec))
QA={'why':[C+'sliding-window'],'lv1':[M+'ar-model','lab:limitation/window-blindness'],'lv2':[C+'training-sample',C+'overfitting'],'vs':['lab:limitation/window-cost']}
for sec,ids in QA.items():
    for i,t in enumerate(ids): EDGES.append(E('lab:quiz/mem-1-1-%s-%d'%(sec,i+1),'assesses',t,'#'+sec))

V=lambda t,a,y,v,d,p:{'title':t,'authors':a,'year':y,'venue':v,'doi':d,'pages':p}
REFS=[
 {'id':'box1970time','type':'book','title':'Time Series Analysis: Forecasting and Control','author':[{'family':'Box','given':'George E. P.'},{'family':'Jenkins','given':'Gwilym M.'}],'issued':{'date-parts':[[1970]]},'publisher':'Holden-Day',
  'lab':{'role':'background','verified':V(True,True,True,True,True,True),'checkedBy':'저자 지식 (표준 교과서)','note':'자기회귀 모형을 포함한 ARIMA 방법론의 원전. 판별 쪽수는 확인하지 않음','work':'lab:work/box1970time','supports':['lab:claim/box-jenkins-arima'],'locs':[{'claim':'lab:claim/box-jenkins-arima','loc':'책 전체'}]}},
 {'id':'cognee2026llmmemory','type':'webpage','title':'LLM Memory','author':[{'literal':'cognee'}],'issued':{'date-parts':[[2026]]},'URL':'https://www.cognee.ai/llm-memory','accessed':{'date-parts':[[2026,11,12]]},
  'lab':{'role':'background','verified':V(False,True,False,True,False,False),'checkedBy':'웹 읽기 2026-11-12','note':'글 제목 표기와 게시 연도는 원문 확인 필요','work':'lab:work/cognee2026llmmemory','supports':['lab:claim/context-window-limit'],'locs':[{'claim':'lab:claim/context-window-limit','loc':'컨텍스트 윈도우 절'}]}},
 {'id':'ahn2026ts3_1_1','type':'webpage','title':'시계열 3부작 1-1 — lookback과 window, 같은 말일까?','author':[{'family':'안','given':'상선'}],'issued':{'date-parts':[[2026,10,29]]},'container-title':'시계열 3부작 — ARIMA와 LSTM','URL':'https://adminmrobo.github.io/timeseries-trilogy/1_1_lookback_window.html',
  'lab':{'role':'primary','verified':V(True,True,True,True,False,False),'checkedBy':'저장소 확인 2026-11-12','note':'이 페이지가 이어받은 앞 글. 같은 매출 기록과 계산 방법','work':'lab:work/ahn2026ts3_1_1','supports':['lab:claim/window-outside-zero'],'locs':[{'claim':'lab:claim/window-outside-zero','loc':'계산 방법(AR 최소제곱)'}]}},
]
META={'id':'ahn2026mem3_1_1','title':'기억 3부작 1-1 — '+TITLE,'series':SERIES,'number':NUM,'creator':[{'name':'안상선','role':'author'}],'contributor':[{'name':'AI 보조 제작','role':'assistant'}],
 'date':DATE,'version':'1.0','language':['ko'],'license':'','url':'https://adminmrobo.github.io/llm_memory_trilogy/'+FILE,
 'about':[C+'sliding-window',C+'memory-horizon',C+'context-window',M+'ar-model',C+'overfitting'],'educationalLevel':'입문','learningResourceType':'interactive explainer',
 'basedOn':['box1970time','cognee2026llmmemory','ahn2026ts3_1_1'],'registryVersion':'mem3-reg-1.0',
 'suggestedCitation':'안상선 (2026). 기억 3부작 1-1 — '+TITLE+'. '+SERIES+' 1-1, v1.0.'}
