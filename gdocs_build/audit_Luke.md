# 누가복음 MSG 의미 감사 보고서 (audit_Luke.md)

- 감사 일자: 2026-09-22
- 기준: Eugene Peterson, **The Message (MSG)** 영어 원문 — 최종 권위
- 감사 대상 파일 (수정 없음, 읽기 전용으로 감사):
  - `~/workspace/teenz-bible-review/msg_Luke.txt` (MSG 원문, `parse_msg_txt()`로 파싱)
  - `~/workspace/teenz-bible-review/fixes/en_Luke.json` (Teen EN)
  - `~/workspace/teenz-bible-review/fixes/ko_Luke.json` (Teen KO)
- 매처: `~/workspace/teenz-bible-review/gdocs_build/build_gdocs.py`의 `match_msg_for_teen()` — **그대로 사용, 무수정**
- 감사 코퍼스: `/tmp/audit_corpus_luke.txt` (4,505행) — MSG 단위 → Teen 문단 매핑을 `parse_msg_txt()` + `match_msg_for_teen()`으로 생성, 전 장(1–24) 전 문단 육안 대조 완료
  - 본문 510개 문단 / 헤더 85개, MSG orphan 0건, Teen-without-MSG 0건 (텍스트 탈락 없음 — 의미 보존은 별도 감사)
  - `§` 헤더는 감사 범위에서 제외
  - MSG 한 단위가 여러 Teen 문단에 공유되는 분할 매핑의 경우, 분할된 문단들을 묶어서 의미를 평가 (분할 자체를 누락으로 오판하지 않음)

## 감사 항목

1. Teen EN이 MSG의 모든 사실·인명/지명·인용구·논리/조건·경고·예언·명령·숫자를 요약 없이 보존했는가
2. Teen KO가 Teen EN의 1:1 번역인가 (추가/삭제/의미 변경 없음)

## 등급

- **중대**: 사실·숫자·인용·명령·경고의 누락/변경/다른 성경 문구로의 대체
- **보통**: 의미 좁힘/논리 구조 변경/압축으로 인한 요소 탈락/EN에 없는 내용의 추가
- **경미**: 경미한 표현 차이·소프트닝·주석성 수식어

---

## 장별 결과 요약

| 장 | 결과 |
|---|---|
| 1 | 이슈 없음 |
| 2 | 중대 2건 |
| 3 | 이슈 없음 |
| 4 | 이슈 없음 |
| 5 | 이슈 없음 |
| 6 | 이슈 없음 |
| 7 | 중대 1건 |
| 8 | 중대 1건 |
| 9 | 중대 1건, 보통 2건 |
| 10 | 중대 1건 |
| 11 | 중대 1건, 보통 6건 |
| 12 | 이슈 없음 |
| 13 | 중대 2건 |
| 14 | 이슈 없음 |
| 15 | 경미 1건 |
| 16 | 이슈 없음 |
| 17 | 중대 2건, 보통 2건 |
| 18 | 경미 1건 |
| 19 | 중대 4건, 경미 3건 |
| 20 | 이슈 없음 |
| 21 | 이슈 없음 |
| 22 | 보통 1건, 경미 1건 |
| 23 | 이슈 없음 |
| 24 | 이슈 없음 |

**총: 중대 15건, 보통 11건, 경미 6건**

---

## 상세 이슈

### 중대

#### [2장 22–24절] Teen EN 사실 누락 — "or two young pigeons"
- **MSG**: `"pair of doves or two young pigeons"`
- **현재 Teen EN**: `"a pair of doves"` — They also offered the sacrifice the law prescribed: a pair of doves.
- **누락/문제**: 제물 규정의 두 번째 대안("or two young pigeons")이 삭제됨. 율법이 정한 제물의 선택지(비둘기 한 쌍 또는 어린 집비둘기 두 마리)가 하나만 남음.
- **수정 방향**: EN을 `"a pair of doves or two young pigeons"` 형태로 복원하고, KO(`"비둘기 한 쌍"`)도 이에 맞춰 두 대안 모두 반영.

#### [2장 36–38절] KO 숫자·인물 전기 변경 — "a widow for eighty-four" → 84세
- **MSG / Teen EN**: `She had been married seven years and a widow for eighty-four.` (결혼 7년 후 **84년 동안 과부**)
- **현재 Teen KO**: `결혼하고 7년 만에 남편이 죽고 84살이 될 때까지 과부로 살았대요` — 84년을 **나이**로 바꿔버림.
- **누락/문제**: MSG의 "과부로 산 기간 84년"이 "84세까지"로 변경. 안나의 나이가 아니라 과부 생활 기간인데, KO는 연령으로 오역.
- **수정 방향**: KO를 `남편과 7년 살고 84년 동안 과부로 살았대요` 식으로 기간으로 복원.

#### [7장 36–39절] KO 정체성 누락 — "the town harlot"
- **MSG / Teen EN**: `Just then a woman of the village, the town harlot, having learned that Jesus was a guest in the home of the Pharisee, came with a bottle of very expensive perfume…` / When the Pharisee saw this, he said to himself, `"If this man was the prophet I thought he was, he would have known what kind of woman this is who is falling all over him."`
- **현재 Teen KO**: `마침 그 동네에 소문이 안 좋은 한 여자가 있었는데…` — "town harlot"이 "소문이 안 좋은 한 여자"로 축소.
- **누락/문제**: 바리새인이 "이런 여자인 줄 알았을 텐데" 하며 판단하는 이유인 명시적 정체(성매매 여성)가 삭제됨. 이어지는 예수님의 교훈의 근거가 약해짐.
- **수정 방향**: KO에 MSG/EN의 명시적 표현을 10대 톤으로 살릴 것. 예: `그 동네에서 몸 파는 여자로 소문난 여자` (순화하되 정체성은 명시).

#### [8장 30–31절] KO 장소 변경 — "the bottomless pit" → 지옥
- **MSG / Teen EN**: `And they begged Jesus desperately not to order them to the bottomless pit.`
- **현재 Teen KO**: `귀신들은 자기들을 지옥으로만 보내지 말아 달라고 예수님께 빌었지.`
- **누락/문제**: MSG의 "the bottomless pit"(무저갱/심연)이 "지옥"으로 변경됨. MSG가 고른 특정 장소 개념이 다른 단어로 교체됨.
- **수정 방향**: KO를 `"끝없는 구덩이"/"무저갱"` 계열로 복원.

#### [9장 23–27절] KO 논리 변경 및 EN에 없는 추가
- **MSG / Teen EN**: `"Anyone who intends to come with me has to let me lead. You're not in the driver's seat — I am. Don't run from suffering; embrace it. Follow me and I'll show you how."`
- **현재 Teen KO**: `"누구든지 저를 따라오려면, 자기를 내려놓고 날마다 자기 십자가를 지고 저를 따라오세요. 고난을 피하려고 애쓰지 마세요. …"`
- **누락/문제**: ① EN의 핵심 논리 "let me lead / You're not in the driver's seat — I am"(주도권을 나에게 넘겨라/운전석에 앉은 건 나다)이 KO에 없음. ② EN에 없는 `"날마다 자기 십자가를 지고"`가 추가됨 (표준 성경 문구이지 현재 Teen EN/MSG의 문구가 아님).
- **수정 방향**: KO에서 "날마다 자기 십자가를 지고" 삭제, EN의 "주도권을 내게 넘기라 / 운전석은 내가 차지한다" 논리를 복원.

#### [10장 33–35절] KO 숫자 누락 — "two silver coins"
- **MSG / Teen EN**: `In the morning he took out two silver coins and gave them to the innkeeper…`
- **현재 Teen KO**: `다음 날 아침에는 돈을 꺼내서 여관 주인한테 주면서 말했지요.` — "two silver coins"가 "돈"으로 축소.
- **누락/문제**: MSG가 명시한 구체적 금액(은화 두 개)이 사라짐. Teen EN/MSG 모두 숫자를 살렸는데 KO만 삭제.
- **수정 방향**: KO에 `은화 두 개` 복원.

#### [11장 10–13절] KO 사실 대체 — "spider" → 전갈
- **MSG / Teen EN**: `If your little girl asks for an egg, do you trick her with a spider?`
- **현재 Teen KO**: `계란 달라고 하는데 전갈을 주겠어요?`
- **누락/문제**: MSG의 "spider"가 "전갈"로 교체됨. 다른 성경 역본의 문구이지 MSG/Teen EN 기준이 아님.
- **수정 방향**: KO를 `거미`로 수정 (MSG/EN 기준 준수).

#### [13장 20–21절] KO 숫자 누락 — "three loaves"
- **MSG / Teen EN**: `It's like yeast that a woman works into enough dough for three loaves of bread — and waits while the dough rises.`
- **현재 Teen KO**: `그건 마치 여자가 빵 만들려고 반죽에 넣는 누룩 같은 거예요. 그냥 놔두면 반죽 전체가 부풀어 오르는 것처럼 말이죠.` — "three loaves" 탈락.
- **누락/문제**: MSG가 명시한 분량(세 덩어리 분)이 사라짐.
- **수정 방향**: KO에 `빵 세 덩어리 분량` 복원.

#### [13장 23–25절] KO 인용문 전체 누락 — "Sorry, you're not on my guest list."
- **MSG / Teen EN**: `…you'll find the door locked and the Master saying, 'Sorry, you're not on my guest list.'`
- **현재 Teen KO**: `…여러분이 문 두드리면서 들어가고 싶다고 해도 문은 잠겨있을 거고,` — 여기서 문단이 끝나고, 주인의 인용 대사가 통째로 없음 (26–27절 KO에도 없음).
- **누락/문제**: 구원의 문 앞에서 주인이 직접 말하는 결정적 선고(인용구)가 삭제됨. 경고의 핵심이 사라짐.
- **수정 방향**: KO에 `'미안하지만, 너는 내 손님 명단에 없어'` 계열의 인용 복원.

#### [17장 34–35절] KO 사실 대체 — "in the same boat fishing" → 한 침대
- **MSG / Teen EN**: `"On that Day, two men will be in the same boat fishing — one taken, the other left. Two women will be working in the same kitchen — one taken, the other left."`
- **현재 Teen KO**: `"그날 밤에 두 사람이 한 침대에 있다가 한 명은 데려가고 한 명은 남을 거예요. 여자 둘이 한 부엌에서 일하다가도 한 명은 데려가고 한 명은 남을 거고요."`
- **누락/문제**: "같은 배에서 고기 잡는 두 남자"가 "한 침대에 있는 두 사람"으로 교체됨. 표준 역본의 문구이지 MSG/Teen EN의 문구가 아님. ("그날 밤에"의 "밤"도 EN에 없음.)
- **수정 방향**: KO를 `"그날, 같은 배에서 고기 잡는 남자 둘이 있다가…"` 계열로 MSG/EN 기준 복원.

#### [17장 37절] KO 문장 전체 누락 — "The action will begin around my dead body."
- **MSG / Teen EN**: `He told them, "Watch for the circling of the vultures. They'll spot the corpse first. The action will begin around my dead body."`
- **현재 Teen KO**: `"독수리들이 맴도는 곳을 잘 보세요. 독수리들이 시체를 제일 먼저 찾을 거거든요."` — 마지막 문장(`The action will begin around my dead body.`) 통째로 없음.
- **누락/문제**: 예수님의 답변의 결론 문장이 삭제됨.
- **수정 방향**: KO에 `"모든 일은 내 시체 주변에서 시작될 거예요"` 계열 복원.

#### [19장 16절] KO 숫자 변경 — "doubled your money" → 열 배
- **MSG / Teen EN**: `"The first said, 'Master, I doubled your money.'`
- **현재 Teen KO**: `첫 번째 종이 와서 '주인님, 주신 돈으로 열 배로 불렸습니다'라고 보고했지요.`
- **누락/문제**: "두 배(doubled)"가 "열 배"로 변경. 뒤따르는 24절("doubled my stake")·25절("already has double")과도 일관되게 깨짐.
- **수정 방향**: KO를 `두 배로 불렸습니다`로 수정 (16·24·25절 일괄).

#### [19장 18절] KO 숫자 변경 — "fifty percent profit" → 다섯 배
- **MSG / Teen EN**: `"The second said, 'Master, I made a fifty percent profit on your money.'`
- **현재 Teen KO**: `"두 번째 종이 와서 '주인님, 주신 돈으로 다섯 배로 불렸습니다'라고 했어요.`
- **누락/문제**: "50% 수익"이 "다섯 배"로 변경됨.
- **수정 방향**: KO를 `50퍼센트 수익을 냈습니다`(또는 `절반만큼 더 불렸습니다`)로 수정.

#### [19장 24절] KO 숫자 변경 — "doubled my stake" → 열 배로 불린
- **MSG / Teen EN**: `'Take the money from him and give it to the servant who doubled my stake.'`
- **현재 Teen KO**: `'이 종의 돈 뺏어서 열 배로 불린 종한테 주세요.'`
- **누락/문제**: 16절과 같은 변경 ("doubled" → "열 배").
- **수정 방향**: KO를 `두 배로 불린 종한테`로 수정.

#### [19장 25절] KO 숫자 변경 — "already has double" → 열 배나
- **MSG / Teen EN**: `"They said, 'But Master, he already has double . . .'`
- **현재 Teen KO**: `사람들이 '아니, 주인님, 그 종은 이미 열 배나 있는데요…'라고 했지요.`
- **누락/문제**: "이미 두 배인데"가 "이미 열 배나"로 변경.
- **수정 방향**: KO를 `이미 두 배나 있는데요`로 수정.

---

### 보통

#### [9장 28–31절] KO 해석적 축소 — "his exodus" → 즉 그분의 죽음
- **MSG / Teen EN**: `They talked over his exodus, the one Jesus was about to complete in Jerusalem.`
- **현재 Teen KO**: `그들은 예수님이 예루살렘에서 이루실 일, 즉 그분의 죽음에 대해 이야기를 나누고 있었대.`
- **누락/문제**: MSG가 일부러 쓴 "exodus"(출애굽/탈출이라는 넓은 구원 사건)가 "죽음"으로만 축소됨.
- **수정 방향**: KO를 `"그분의 출애굽(exodus), 곧 예루살렘에서 이루실 일"` 계열로 복원.

#### [9장 46–48절] KO 2단계 논리 붕괴 — "accepts me" 탈락
- **MSG / Teen EN**: `"Whoever accepts this child as if the child were me, accepts me," he said. "And whoever accepts me, accepts the One who sent me."`
- **현재 Teen KO**: `"누구든지 이 아이를 저라고 생각하고 받아들이는 사람은, 곧 저를 보내신 분을 받아들이는 거예요.`
- **누락/문제**: 아이 받음 → 나 받음 → 나를 보내신 분 받음의 2단계 연결이, 중간 단계("나를 받아들임") 없이 한 단계로 붕괴됨.
- **수정 방향**: KO에 `"이 아이를 받아들이는 사람은 곧 나를 받아들이는 거고, 나를 받아들이는 사람은 곧 나를 보내신 분을 받아들이는 거예요"` 계열로 2단계 복원.

#### [11장 5–8절] KO 사실 누락 — "knocking and waking all the neighbors"
- **MSG / Teen EN**: `if you stand your ground, knocking and waking all the neighbors, he'll finally get up and get you whatever you need.`
- **현재 Teen KO**: `여러분이 계속 끈질기게 문 두드리면 결국엔 일어나서 필요한 걸 줄 거예요.`
- **누락/문제**: "이웃들까지 다 깨우며"라는 끈질김의 정도를 보여주는 구체적 묘사가 삭제됨.
- **수정 방향**: KO에 `이웃들까지 다 깨울 정도로 계속 두드리면` 계열 복원.

#### [11장 14–16절] KO 추가 및 대체 — 바알세불·하늘에서 오는 기적
- **MSG / Teen EN**: 비방자들은 `"Black magic,"` / `"Some devil trick he's pulled from his sleeve."`라고 했고, 회의론자들은 `waiting around for him to prove himself with a spectacular miracle`였음.
- **현재 Teen KO**: `몇몇은 삐딱하게 "저거 마귀 왕 바알세불 힘 빌려서 쇼하는 거예요" 이러는 거. 또 다른 사람들은 예수님을 시험하려고 하늘에서 오는 기적 한 번 보여달라고 했대.`
- **누락/문제**: ① EN의 "Black magic / devil trick"이 "마귀 왕 바알세불 힘"으로 대체됨 (바알세불은 뒤 문단(17–20절) 예수님의 반박에 나오는 이름으로, 이 문단 MSG/EN에는 없음). ② "spectacular miracle"에 EN에 없는 "하늘에서 오는"이 추가됨.
- **수정 방향**: KO를 `"흑마술이야" / "악마의 잔꾀야"` 계열과 `"엄청난 기적"` 계열로 EN 기준 복원.

#### [11장 29–30절] KO 대폭 압축 — 세대의 진단 요소 다수 탈락
- **MSG / Teen EN**: `"The mood of this age is all wrong. Everybody's looking for proof, but you're looking for the wrong kind. All you're looking for is something to titillate your curiosity, satisfy your lust for miracles. But the only proof you're going to get is the Jonah-proof given to the Ninevites, which looks like no proof at all. What Jonah was to Nineveh, the Son of Man is to this age."`
- **현재 Teen KO**: `"이 세대는 진짜 답이 없어요. 맨날 기적만 보여달라고 조르는데, 여러분한테 보여줄 기적은 요나의 기적밖에 없어요. 요나가 니느웨 사람들에게 하나님의 메시지 그 자체였던 것처럼, 인자도 이 세대한테 그런 존재예요."`
- **누락/문제**: ① "이 시대의 분위기가 완전히 잘못됐다"(시대 진단), ② "증거는 찾는데 잘못된 종류를 찾는다", ③ "호기심을 자극하고 기적에 대한 탐욕을 채우려는 것", ④ "요나의 증거는 증거 같지도 않아 보이는 증거" — 네 요소가 삭제/압축됨.
- **수정 방향**: KO에 위 네 요소를 EN 기준으로 복원 (틴즈 톤 유지).

#### [11장 33–36절] KO 다른 문구로 대체 — wide-eyed / squinty-eyed / musty cellar
- **MSG / Teen EN**: `If you live wide-eyed in wonder and belief, your body fills up with light. If you live squinty-eyed in greed and distrust, your body is a musty cellar. Keep your eyes open, your lamp burning, so you don't get musty and murky.`
- **현재 Teen KO**: `여러분의 눈이 맑으면 온몸이 밝을 거고, 눈이 나쁘면 온몸이 어두울 거예요. …`
- **누락/문제**: MSG의 대비 구조("경이와 믿음으로 눈을 크게 뜨고" vs "탐욕과 불신으로 눈을 가늘게 뜨고", "곰팡내 나는 지하실")가 일반적인 "눈이 맑으면/나쁘면" 문구로 대체됨. EN의 구체적 이미지와 도덕적 대비가 사라짐.
- **수정 방향**: KO를 `"경이와 믿음으로 눈을 크게 뜨고 살면… / 탐욕과 불신으로 눈을 찡그리면… 곰팡내 나는 지하실"` 계열로 복원.

#### [11장 42절] KO 추가 및 논리 변경 — 박하·운향·채소 / 십일조도 해야 하지만
- **MSG / Teen EN**: `You keep meticulous account books, tithing on every nickel and dime you get, but manage to find loopholes for getting around basic matters of justice and God's love. Careful bookkeeping is commendable, but the basics are required.`
- **현재 Teen KO**: `여러분은 박하, 운향, 온갖 채소의 십일조는 칼같이 내면서, 정의랑 하나님 사랑 같은 더 중요한 건 무시하잖아요. 십일조도 해야 하지만, 더 중요한 걸 놓치면 안 되지요.`
- **누락/문제**: ① "박하, 운향, 온갖 채소"는 다른 역본의 구체 항목이지 MSG/EN("meticulous account books, tithing on every nickel and dime")이 아님. ② "find loopholes for getting around"(교묘히 피해가는 구멍) 논리 탈락. ③ "Careful bookkeeping is commendable, but the basics are required"(꼼꼼한 장부는 칭찬할 만하지만 기본은 필수)가 "십일조도 해야 하지만"으로 변경.
- **수정 방향**: KO를 `"장부는 꼼꼼하게 쓰면서 한 푼도 빠짐없이 십일조 내지만, 정의와 하나님 사랑 같은 기본은 교묘히 피해가요. 꼼꼼한 장부는 칭찬할 만하지만, 기본은 필수예요"` 계열로 복원.

#### [11장 43–44절] KO 다른 역본 문구 — 회당 높은 자리 / 시장에서 인사
- **MSG / Teen EN**: `You love sitting at the head table at church dinners, love preening yourselves in the radiance of public flattery.`
- **현재 Teen KO**: `회당에서 높은 자리에 앉는 거 좋아하고, 시장에서 인사받는 거 좋아하고.`
- **누락/문제**: MSG의 "교회 만찬의 상석 / 공개적인 아첨의 빛"이 표준 역본식 "회당 높은 자리 / 시장에서 인사"로 대체됨.
- **수정 방향**: KO를 `"교회 만찬에서 상석에 앉는 거, 사람들 앞에서 아첨받으며 으스대는 거"` 계열로 EN 기준 복원.

#### [11장 47–51절] KO 집단 축소 — "every drop of righteous blood" → 모든 예언자의 피
- **MSG / Teen EN**: `What it means is that every drop of righteous blood ever spilled from the time earth began until now, from the blood of Abel to the blood of Zechariah…`
- **현재 Teen KO**: `세상이 창조된 이후로 흘린 모든 예언자의 피 값을 이 세대가 다 치르게 될 거예요.`
- **누락/문제**: "의로운 피(righteous blood)"가 "예언자의 피"로 축소됨. MSG는 예언자만이 아니라 땅이 시작된 이래 흘린 모든 의로운 피를 말함.
- **수정 방향**: KO를 `땅이 시작된 이래 흘린 모든 의로운 피` 계열로 복원.

#### [17장 6절] KO 다른 역본 문구 + 문장 추가 — "뿌리째 뽑혀서 바다에 심겨져라"
- **MSG / Teen EN**: `If you have a bare kernel of faith, say the size of a poppy seed, you could say to this sycamore tree, 'Go jump in the lake,' and it would do it.`
- **현재 Teen KO**: `…이 뽕나무에게 '뿌리째 뽑혀서 바다에 심겨져라!'라고 말하면, 그대로 될 것입니다. 여러분이 말하는 대로 그냥 되는 거예요.`
- **누락/문제**: ① MSG의 "Go jump in the lake"(호수에 뛰어들어라)가 다른 역본식 "뿌리째 뽑혀서 바다에 심겨져라"로 대체됨. ② EN에 없는 문장(`여러분이 말하는 대로 그냥 되는 거예요`)이 추가됨.
- **수정 방향**: KO를 `'(뽕나무야,) 호수에 뛰어들어라!'` 계열로 복원하고, 마지막 추가 문장 삭제.

#### [17장 20–21절] KO 의미 이동 — "already among you" → 이미 여러분 안에
- **MSG / Teen EN**: `Because God's kingdom is already among you.`
- **현재 Teen KO**: `왜냐고요? 하나님 나라는 이미 여러분 안에 있거든요.`
- **누락/문제**: "among you"(너희 가운데/사이에)가 "여러분 안에"(너희 속에)로 변경됨. MSG의 "너희 사이에 이미 와 있다"는 의미가 내면화됨.
- **수정 방향**: KO를 `이미 여러분 가운데 있거든요`로 수정.

#### [22장 27–30절] KO 압축 — "be strengthened" 탈락
- **MSG / Teen EN**: `Now I confer on you the royal authority my Father conferred on me so you can eat and drink at my table in my kingdom and be strengthened as you take up responsibilities among the congregations of God's people.`
- **현재 Teen KO**: `이제 제 아버지가 저에게 주신 왕의 권위를 여러분에게 줍니다. 그래서 여러분은 제 나라에서 제 식탁에 앉아 먹고 마시면서, 하나님 백성들 사이에서 리더 역할을 하게 될 거예요.`
- **누락/문제**: ① "be strengthened"(힘을 얻으며)가 삭제됨. ② "take up responsibilities among the congregations"(회중 사이에서 책임을 맡으며)가 "리더 역할"로 축소됨.
- **수정 방향**: KO에 `"힘을 얻으며 하나님 백성의 모임들 사이에서 책임을 맡게 될 거예요"` 계열 복원.

---

### 경미

#### [15장 7절] KO 주석성 수식어 추가 — "회개한"
- **MSG / Teen EN**: `there will be more rejoicing in heaven over one sinner's rescued life than over ninety-nine good people in no need of rescue.`
- **현재 Teen KO**: `'저는 구원 필요 없는데요?' 하는 의인 99명보다, 회개한 죄인 한 명 때문에 하늘나라에서는 더 기뻐한답니다.`
- **누락/문제**: EN에 없는 "회개한"이 추가됨. "rescued life"(구원받은 삶)가 "회개한 죄인"으로 해석 고정됨. 낮은 우선순위이나 1:1 원칙상 수정 권장.
- **수정 방향**: KO를 `구원받은 죄인 한 명` 계열로 조정.

#### [18장 13절] KO 추가 — "가슴을 치면서"
- **MSG / Teen EN**: `"Meanwhile the tax man, slumped in the shadows, his face in his hands, not daring to look up, said, 'God, give mercy. Forgive me, a sinner.'"`
- **현재 Teen KO**: `근데 세리는 저쪽 구석에 쭈그려 앉아서 얼굴도 못 들고 가슴을 치면서 말했어요.`
- **누락/문제**: MSG/EN에 없는 "가슴을 치면서"(다른 역본의 묘사)가 추가됨.
- **수정 방향**: "가슴을 치면서" 삭제.

#### [19장 5절] KO 의미 이동 — "be a guest in your home" → 자야겠어요
- **MSG / Teen EN**: `"Zacchaeus, hurry down. Today is my day to be a guest in your home."`
- **현재 Teen KO**: `"삭개오님, 빨리 내려오세요. 오늘 제가 여러분의 집에서 자야겠어요"`
- **누락/문제**: "be a guest"(손님이 되다)가 "자다"(숙박)로 좁혀짐.
- **수정 방향**: KO를 `오늘 제가 당신 집 손님이 될 거예요` 계열로 복원.

#### [19장 8절] KO 조건 누락 — "if I'm caught"
- **MSG / Teen EN**: `"Master, I give away half my income to the poor — and if I'm caught cheating, I pay four times the damages."`
- **현재 Teen KO**: `"주님, 제 재산 절반을 가난한 사람들한테 다 줄게요. 그리고 제가 누구한테 사기 친 거 있으면, 그 돈의 네 배로 갚겠습니다"`
- **누락/문제**: "if I'm caught cheating"(속인 게 들키면)의 "들키면" 조건이 탈락하고 "사기 친 거 있으면"으로 바뀜.
- **수정 방향**: KO에 `속인 게 들키면` 조건 복원.

#### [19장 10절] KO 축소 — "restore the lost" → 구해주려고
- **MSG / Teen EN**: `For the Son of Man came to find and restore the lost.`
- **현재 Teen KO**: `인자는 잃어버린 사람을 찾아서 구해주려고 온 것입니다.`
- **누락/문제**: "restore"(회복시키다)가 "구해주다"로 축소됨. MSG의 "찾고 회복" 두 동사 중 하나가 희석됨.
- **수정 방향**: KO를 `찾아서 회복시키려고` 계열로 복원.

#### [22장 21–22절] KO 소프트닝 — "this is doomsday" → 화가 있을 거예요
- **MSG / Teen EN**: `But for the one who turns him in, turns traitor to the Son of Man, this is doomsday.`
- **현재 Teen KO**: `그런데 인자를 배신해서 넘겨줄 그 사람에게는 화가 있을 거예요!`
- **누락/문제**: "this is doomsday"(이건 종말이다)가 "화가 있을 거예요"로 약화됨.
- **수정 방향**: KO를 `그 사람에게는 이게 종말이에요` 계열로 강화.

---

## 감사 방법 검증 기록

- `parse_msg_txt()`, `match_msg_for_teen()` 무수정 사용 확인 (파일 미수정, 감사 전용 코퍼스만 `/tmp`에 생성)
- 원본 JSON 3개 파일 미수정 확인:
  - `fixes/en_Luke.json` (md5 `3a3ca7250300da40ace0790a037d4c23`, 2026-09-22 03:50)
  - `fixes/ko_Luke.json` (md5 `4b3870650c3ccbee31c7aa5f9b1d298b`, 2026-09-22 03:50)
  - `msg_Luke.txt` (md5 `8bec2e2663e382ce4e225042671dca99`)
- 본 보고서는 감사 보고서이며, **어떤 원본 파일도 수정하지 않았음**. 수정 작업은 별도 승인 후 진행.
---

## 부록: 2026-09-23 미묘한 슬랭 일괄 수정 (번역 원칙 5)

- 배경: 신약 27권 EN/KO 전수 검사에서 자동 욕설 목록 밖의 미묘한 슬랭·저속 표현 발견. 성욱 지시("B 기준 정하고 한 번에 해")에 따라 아래 확정 6개 Rule로 일괄 수정.
- Rule: ① 채팅 약어·유행 은어(ㅇㅋ·here's the tea·woke·throw shade·GOAT·FOMO·fam·vibe) ② 원칙 5 명시 슬랭(썰·꿀잼·쌩까·드립·뇌절·어그로·인싸춤·뿅·텐션·뇌정지·가오·찢길각) ③ ghosting 계열(ghost·고스팅) ④ 신성한 대상 경량화(찐·대박·인싸/아싸·레전드·흑역사·맛집·핫해·좋아요·게임 체인저·That loser is gone) ⑤ 저속·모욕·첨가 강화 순화(관종·lame·freaking out·working my butt off·맛이 갔네·한심·일진/꼽준다·멘붕·멘탈·올인) ⑥ 유지(chill·bro·왕따 — 변경 없음)
- 수정 원칙: EN primary(MSG 의미 유지), KO는 수정된 EN의 의미·톤 1:1, 의미 축소·본문 구조 변경 금지, 해당 표현만 최소 수정.

- 본 권 수정: **EN 0건, KO 21건** (합계 21건). Rule ⑥(chill·bro·왕따) 변경 없음.

| 장 | 위치 | 언어 | Rule | 기존 | 수정 |
|---|---|---|---|---|---|
| 3 | p13 | KO | ④ | 완전 찐 메시지였지! | 완전 진짜 메시지였지! |
| 3 | p4 | KO | ④ | 세례가 완전 핫해지니까 | 세례가 완전 인기를 얻으니까 |
| 5 | p13 | KO | ④ | 우리 평생에 이런 건 진짜 처음 본다. 대박. | 우리 평생에 이런 건 진짜 처음 본다. 믿기지가 않아. |
| 6 | p15 | KO | ④ | 인싸가 되는 게 아니라고요. | 인기인이 되는 게 아니라고요. |
| 6 | p15 | KO | ④ | 가짜 예언자들한테 ‘좋아요’를 눌러줬는지 | 가짜 예언자들을 추켜세웠는지 |
| 7 | p10 | KO | ④ | 하나님의 찐 심부름꾼이에요! | 하나님의 진짜 심부름꾼이에요! |
| 7 | p3 | KO | ④ | 진짜로 종이 싹 나아 있었대. 대박이지? | 진짜로 종이 싹 나아 있었대. 놀랍지 않아요? |
| 8 | p13 | KO | ④ | 더 찐한 거죠. | 더 진한 거죠. |
| 8 | p3 | KO | ④ | 대박 풍년을 이뤘대. | 엄청난 풍년을 이뤘대. |
| 10 | p12 | KO | ④ | 근데 진짜 대박인 건, | 근데 정말 놀라운 건, |
| 12 | p11 | KO | ④ | 완전 대박 난 거예요. | 엄청난 풍년을 맞은 거예요. |
| 13 | p13 | KO | ⑤ | 하나님이랑 함께하는 삶에 올인하세요. | 하나님이랑 함께하는 삶에 전부를 거세요. |
| 16 | p6 | KO | ④ | 여기서 대박인 게 뭔지 아세요? | 여기서 놀라운 게 뭔지 아세요? |
| 18 | p1 | KO | ② | 썰을 하나 풀어주셨어요. | 이야기를 하나 들려주셨어요. |
| 18 | p5 | KO | ② | 다음 썰을 풀어주셨어요. | 다음 이야기를 들려주셨어요. |
| 20 | p19 | KO | ② | 하나님이랑 완전 꿀잼으로 친하게 지낼 거거든요 | 하나님이랑 정말 즐겁게 친하게 지낼 거거든요 |
| 20 | p3 | KO | ④ | 요한을 찐 예언자로 믿는 | 요한을 진짜 예언자로 믿는 |
| 20 | p3 | KO | ② | 완전 찢길 각인데. | 완전히 끝장인데. |
| 24 | p8 | KO | ④ | 찐 희망이라고 믿고 있었는데 | 진짜 희망이라고 믿고 있었는데 |
| 24 | p8 | KO | ④ | 근데 더 대박인 건, | 근데 더 놀라운 건, |
| 24 | p8 | KO | ⑤ | 우리를 완전 멘붕에 빠뜨렸어요. | 우리를 완전히 당황하게 했어요. |

**8개 게이트 결과 (2026-09-23)**: 8개 게이트 전부 PASS — 특이사항: ① 21/21 반영, ② validator 24장 모두 통과, ③ completeness FAIL 19건 모두 completeness_fp_Luke.md 문서화 오탐과 1:1 일치, ④ 재빌드 Luke.docx에 21/21 반영·옛 문자열 0건, ⑤ PAIRING CONTENT OK(510행/24테이블), ⑥ 재업로드 완료, ⑦ API 테이블 24/24, ⑧ export-back VERIFIED OK.
