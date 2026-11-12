# 표지 지시문 모음 — 기억 3부작 (목차 1장 + 부마다 1장)

네 장 모두 판 L (16:9, 가로 1920 이상). 참고 이미지로 네 캐릭터 기본 그림 4장을 함께 올린다 (`adminmrobo/fruitfly-lab-expressions`). `cover_index`를 먼저 받아 그림체를 확인한 뒤, 나머지 석 장에 참고 그림으로 함께 올린다. 각 부의 첫 편은 큰 표지, 나머지 편은 같은 그림을 낮은 띠로 쓴다.

공통 지시 (Genspark에 붙여 넣기):
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.
```

공통 캐릭터 묘사 (영어 프롬프트의 {FOUR}에 넣는다):
```
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, {박사 포즈};
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, {조수 포즈};
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, {초파리 포즈};
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, {주판봇 포즈}.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

| 키 | 장소 | 주제 은유 (글자 없이) | 박사 / 조수 / 초파리 / 주판봇 | 대체 글 |
|---|---|---|---|---|
| `cover_index` | 방이 줄지은 연구실 복도, 밤 | 복도 왼쪽 끝의 작은 빛나는 창틀에서 오른쪽 끝의 큰 서랍장까지 빛줄기 하나가 이어진다 | 가운데 뒤에서 빛줄기를 가리킴 / 오른쪽 옆에서 기록 묶음을 안음 / 작은 창틀을 듦 / 서랍 손잡이를 잡음 | 밤의 연구실 복도. 작은 창틀에서 큰 서랍장까지 빛줄기가 이어지고 네 식구가 그 길에 서 있다 |
| `cover_ch1` | 연구실 옆 회계실, 밤 | 책상 위 긴 기록 띠 가운데 빛나는 창틀 안쪽만 밝고, 창틀 밖은 어둠 속 서랍으로 이어진다 | 턱에 손을 대고 창틀을 봄 / 기록 띠 끝을 잡음 / 작은 창틀을 듦 / 아주 긴 창틀을 밂 | 밤의 회계실. 긴 매출 기록 띠에서 빛나는 창틀 안만 밝다 |
| `cover_ch2` | 손님 응대 창구가 있는 연구실 방, 저녁 | 창구 위로 길게 풀린 대화 두루마리가 창틀을 지나며, 창틀을 벗어난 앞부분이 바닥으로 떨어진다 | 두루마리를 손끝으로 짚음 / 떨어진 두루마리를 주워 듦 / 쪽지 한 장을 집게로 듦 / 두루마리를 통째로 끌어안음 | 저녁의 응대 창구. 긴 대화 두루마리의 앞부분이 창틀 밖으로 떨어진다 |
| `cover_ch3` | 벽 한 면이 서랍장인 기록실, 새벽 | 열린 서랍마다 쪽지가 꽂혀 있고, 몇 장에는 빛바랜 색과 새 색이 섞여 있다. 책상 위에는 작은 빛 구슬 열여섯 개가 한 줄로 놓여 있다 | 빛 구슬을 들여다봄 / 쪽지에 도장을 찍음 / 낡은 쪽지를 골라 듦 / 서랍을 한꺼번에 여러 개 엶 | 새벽의 기록실. 서랍마다 쪽지가 꽂혀 있고 책상에 빛 구슬 열여섯 개가 놓여 있다 |

**영어 장면 문장 (Scene / Visual metaphor에 넣는다)**
- cover_index: `Scene: a long research lab corridor at night with doors on both sides. Visual metaphor: a single warm beam of light runs from a small glowing rectangular frame at the far left to a tall wall of wooden drawers at the far right.`
- cover_ch1: `Scene: a small accounting room next to a research lab at night, a long wooden desk in front of a wall of closed drawers. Visual metaphor: a very long paper ribbon with a plain wavy line (no digits) crosses the desk; only the part inside the glowing frames is lit in warm amber, the rest fades into darkness toward an open drawer.`
- cover_ch2: `Scene: a lab room with a service counter in the evening. Visual metaphor: a long paper scroll of speech-bubble shapes (no text) unrolls across the counter through a glowing rectangular frame; the earliest part of the scroll has slipped out of the frame and falls to the floor in shadow.`
- cover_ch3: `Scene: an archive room at dawn, one wall entirely made of small wooden drawers, several open with paper slips standing in them. Visual metaphor: some slips are faded and some are fresh; on the desk, sixteen small glowing beads sit in a single row.`

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

**받은 뒤:** `assets/img/{키}.webp`(1600×900, 220KB 이하)와 `{키}_960.webp`, 공유 미리보기 `og_index.jpg`·`og_ch1~3.jpg`(1200×630 자르기)로 저장하고 `cover_manifest.json`의 `status`를 `ok`로 바꾼다.
