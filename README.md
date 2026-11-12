# 기억 3부작 — LLM은 어디까지 기억할 수 있을까

시계열의 창(lookback)에서 출발해 LLM의 문맥 창, 대화 압축, 바깥 저장소, 기억 돌보기, 기억 토큰까지 넓혀 가는 연구실 해설 시리즈입니다. 「시계열 3부작」의 후속입니다.

- 보기: https://adminmrobo.github.io/llm_memory_trilogy/
- 구성: 3부 × 6편 = 18편과 목차 (구성표: `docs/PLAN_series.md`)
- 독자: AI를 처음 접하는 직장인. 코드·수식을 몰라도 읽을 수 있습니다.

| 부 | 편 |
|---|---|
| 1부 시계열의 기억 | [1-1 창 밖은 없는 것](1_1_window_is_memory.html) · [1-2 메아리는 언제 꺼지나](1_2_fading_echo.html) · [1-3 꺼지지 않는 메아리](1_3_long_memory.html) · [1-4 읽으며 기억하기](1_4_reading_state.html) · [1-5 지우개 달린 메모장](1_5_eraser_notepad.html) · [1-6 1부 대결·정리](1_6_duel_summary.html) |
| 2부 LLM의 기억 | [2-1 문맥 창 = 글의 창](2_1_context_window.html) · [2-2 창을 키우면 될까](2_2_bigger_window.html) · [2-3 기억 서랍 셋](2_3_three_drawers.html) · [2-4 대화 압축](2_4_compaction.html) · [2-5 꺼내 읽기](2_5_retrieval.html) · [2-6 2부 대결·정리](2_6_duel_summary.html) |
| 3부 기억 관리 | [3-1 무엇을 기억할까](3_1_what_to_remember.html) · [3-2 언제 적을까](3_2_when_to_write.html) · [3-3 낡은 기억 돌보기](3_3_maintain.html) · [3-4 16개 토큰에 담기](3_4_memorilla.html) · [3-5 경험으로 배우는 에이전트](3_5_agent_experience.html) · [3-6 대결·총정리](3_6_duel_wrapup.html) |

각 페이지는 서버·설치 없이 열리는 단일 HTML입니다. 실험의 숫자는 설명용 모형에서 브라우저가 직접 계산하고, 페이지 끝의 「온톨로지·서지 꾸러미」에서 지식 그래프와 참고문헌을 내려받을 수 있습니다. 3-4와 3-5의 논문 수치는 저자 보고값을 옮긴 것입니다.

글 · 안상선 ((주)M-Robo 대표) · https://adminmrobo.github.io/who_am_i/who_am_i.html
