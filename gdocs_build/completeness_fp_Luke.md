# Luke 기계적 완전성 검사 — 잔여 FAIL 19건 오탐 판정 근거 (2026-09-22)

검사: `python3 gdocs_build/completeness_check.py fixes/en_Luke.json`
대상: 24장 510문단, 이름 토큰 569개, 숫자 토큰 181개, 인용구 3개
결과: FAIL 19건 — 전수 독해(MSG 원문·Teen EN 전문 대조) 결과 전부 오탐. 실제 누락·요약·의미 반전 0건.

오탐 클래스별 근거 (John/Hebrews/1John 감사에서 문서화된 클래스와 동일):

## 오탐 1–11 — ch1 idx2/3/4/6/8/17/22/23/24/26, ch3 idx1 — name: zachariah (11건)
- MSG 표기 "Zachariah" / Teen 표기 "Zechariah" — 동일 인물(세례 요한의 아버지)의 두 표준 영어 철자.
- Teen은 전 권에서 "Zechariah"로 일관되게 표기. 인명 자체는 한 건도 누락 없음.
- 판정: **오탐** (철자 변형 — checker ALIASES 미등록 클래스)

## 오탐 12 — ch1 idx0 [badge 1-4] name: word
- MSG: "eyewitnesses who served this **Word** with their very lives"
- EN: "the original eyewitnesses — the people who gave their whole lives to serving **this message**."
- "Word"(복음을 가리키는 칭호) → "this message". 의미 완전 동일, teen-friendly 표현.
- 판정: **오탐**

## 오탐 13 — ch1 idx3 [badge 8-12] name: god
- MSG: "carrying out his priestly duties **before God** ... enter the sanctuary **of God**"
- EN: "go inside the **main Temple sanctuary** and burn incense."
- "Temple"이라는 단어 자체가 '하나님의 성소' 의미를 내포. 성전 앞에서 드리는 제사라는 사실관계 보존.
- 판정: **오탐** (teen 압축 — 감사 게이트 1 육안 대조 통과)

## 오탐 14 — ch1 idx12 [badge 29-33] name: lord
- MSG: "**The Lord God** will give him the throne of his father David"
- EN: "**God** will give him the throne of his ancestor David."
- 칭호 "Lord"가 단순화됐으나 행위 주체(하나님)와 내용(다윗의 왕위 수여)은 그대로. 논리 영향 없음.
- 판정: **오탐** (칭호 단순화 — 감사 게이트 1 육안 대조 통과)

## 오탐 15 — ch2 idx1 [badge 1-5] name: galilean
- MSG: "Joseph went from the **Galilean** town of Nazareth"
- EN: "hiked from **Nazareth** all the way to Bethlehem"
- 지리적 수식어 "Galilean" 탈락이나, 이동 경로(나사렛→베들레헴)의 사실관계는 완전 보존.
- 판정: **오탐** (수식어 압축 — 감사 게이트 1 육안 대조 통과)

## 오탐 16 — ch2 idx7 [badge 15-18] name: god
- MSG: "see for ourselves **what God has revealed to us**"
- EN: "Let's go to Bethlehem right now and **see this!**" + 뒷문장 "what the **angels had said** about this child"
- 계시의 내용(천사들이 알린 아기)이 뒷문장에 그대로 보존됨. "see this"의 지시 대상이 명확.
- 판정: **오탐** (문맥상 보존된 압축 — 감사 게이트 1 육안 대조 통과)

## 오탐 17 — ch4 idx11 [badge 16-17] name: unrolling
- MSG: "**Unrolling** the scroll, he found..." (문장 첫머리 대문자 동사)
- EN: "**He unrolled it** and found this exact spot:" — 어근 "unroll"이 동사형으로 그대로 존재.
- 판정: **오탐** (문두 대문자 오인 — John #5 "Swarms"와 동일한 클래스)

## 오탐 18 — ch24 idx2 [badge 4-8] name: jesus
- MSG: "Then they remembered **Jesus'** words."
- EN: "Then it clicked. They remembered **his** words." ("the Living One... He isn't here; he has risen!" 직후라 지시 대상 명확)
- 판정: **오탐** (대명사 paraphrase — John #4/#6와 동일한 클래스)

## 오탐 19a — ch24 idx7 [badge 17-18] number: 1
- MSG: "Then **one of them**, his name was Cleopas"
- EN: "**One guy**, Cleopas, said" — 수량 의미("둘 중 한 사람") 완전 보존.
- checker의 bare-"one" 제외 휴리스틱(_one_is_numeric)에 걸린 것.
- 판정: **오탐** (John #4 "the one" 클래스와 동일)

## 오탐 19b — ch24 idx19 [badge 45-49] name: word, god
- MSG: "open their understanding of **the Word of God**"
- EN: "opened their minds so they could finally fully understand **the Bible**."
- "Word of God" → "the Bible". 10대에게 동일한 의미로 전달되는 teen 표현.
- 판정: **오탐**

---

## 결론
19건 모두 오탐. 실제 이슈 0건.
감사 리포트(audit_Luke.md)의 이슈 32건(중대 15·보통 11·경미 6)은 현행 JSON에 모두 반영되어 있음(각 문단 MSG 대조로 재확인).
checker 공유 도구는 수정하지 않음(타 권 워커와 공유 중 — ALIASES 등록은 별도 판단 필요).
