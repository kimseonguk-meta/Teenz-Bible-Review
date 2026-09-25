# Luke 기계적 완전성 검사 — 2차 심층 재검토 판정 (2026-09-25)

검사: `python3 gdocs_build/completeness_check.py fixes/en_Luke.json`
대상: 24장 510문단, 이름 토큰 569개, 숫자 토큰 181개, 인용구 3개
1차 잔여 FAIL 19건 → **2차 재검토에서 실제 누락 5건 복원**, 잔여 FAIL 15건.

## 2차에서 복원한 5건 (축약 금지 기준 + KO 비대칭)

1. **ch1 idx3 [badge 8-12] name: god** — MSG "enter the sanctuary **of God**" → EN "the main Temple sanctuary" (of God 탈락, KO "하나님의 성소"에는 있음). EN 복원: "the main sanctuary **of God**".
2. **ch1 idx12 [badge 29-33] name: lord** — MSG "**The Lord God** will give him the throne" → EN "God will give him" (Lord 탈락, KO "주 하나님께서"에는 있음). EN 복원: "**the Lord God** will give him the throne".
3. **ch2 idx1 [badge 1-5] name: galilean** — MSG "the **Galilean** town of Nazareth up to Bethlehem **in Judah**" → EN "from Nazareth ... to Bethlehem" (Galilean/in Judah 탈락, KO "갈릴리 나사렛 ... 유대 베들레헴 ... 올라갔어요"에는 있음). EN 복원: "hiked up from the **Galilean** town of Nazareth all the way to Bethlehem **in Judah**".
4. **ch2 idx7 [badge 15-18] name: god** — MSG "see for ourselves what **God** has revealed to us" → EN "see this!" (God 탈락, KO "하나님이 우리한테 보여주신 거"에는 있음). EN 복원: "see what **God** has revealed to us!"
5. (보너스, checker 외 판독 발견) **ch24 idx2 [badge 4-8] name: jesus** — MSG "Then they remembered **Jesus'** words." → EN "They remembered his words." (KO "예수님이 하셨던 말씀"에는 있음). EN 복원: "They remembered **Jesus'** words."

## 잔여 FAIL 15건 — 전부 오탐 (2차 전수 판독으로 재확인)

### 오탐 1–11 — ch1 idx2/3/4/6/8/17/22/23/24/26, ch3 idx1 — name: zachariah (11건)
- MSG 표기 "Zachariah" / Teen 표기 "Zechariah" — 동일 인물(세례 요한의 아버지)의 두 표준 영어 철자.
- Teen은 누가복음 전체에서 "Zechariah"로 일관 표기. 인명 누락 0건.
- 판정: **오탐** (철자 변형 — checker ALIASES 미등록 클래스)

### 오탐 12 — ch1 idx0 [badge 1-4] name: word
- MSG: "eyewitnesses who served this **Word** with their very lives"
- EN: "the original eyewitnesses — the people who gave their whole lives to serving **this message**."
- "Word"(복음 메시지) → "this message". 의미 완전 동일, teen-friendly 표현.
- 판정: **오탐**

### 오탐 13 — ch4 idx11 [badge 16-17] name: unrolling
- MSG: "**Unrolling** the scroll, he found..." (문장 첫머리 대문자 동사)
- EN: "**He unrolled it** and found this exact spot:" — 어근 "unroll" 동사형으로 존재.
- 판정: **오탐** (문두 대문자 오인)

### 오탐 14 — ch24 idx7 [badge 17-18] number: 1
- MSG: "Then **one of them**, his name was Cleopas"
- EN: "**One guy**, Cleopas, said" — 수량 의미("둘 중 한 사람") 완전 보존.
- 판정: **오탐** (bare-"one" 휴리스틱)

### 오탐 15 — ch24 idx19 [badge 45-49] name: word, god
- MSG: "open their understanding of **the Word of God**"
- EN: "opened their minds so they could finally fully understand **the Bible**."
- "Word of God" → "the Bible". 10대에게 동일한 의미로 전달되는 teen 표현. KO도 "성경".
- 판정: **오탐**

## 결론
15건 모두 오탐. 실제 누락 0건. 2차에서 복원한 5건(EN 6행 중 1건은 판독 발견분)은 GitHub commit에 기록.
checker 공유 도구는 수정하지 않음.
