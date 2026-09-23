# John 기계적 완전성 검사 — 잔여 FAIL 6건 오탐 판정 근거 (2026-09-22)

검사: `python3 gdocs_build/completeness_check.py fixes/en_John.json`
대상: 21장 414문단, 이름 토큰 507개, 숫자 토큰 128개
결과: FAIL 6건 — 전수 독해(MSG 원문·Teen EN 전문 대조) 결과 전부 오탐. 실제 누락·요약·의미 반전 0건.

별도 실수 1건(오탐 아님)은 수정으로 해소: ch8 idx5 [badge 11] MSG 편집자 주석 "John 7:53–8:11" 번호가 Teen 주석에서 빠져 있어 EN/KO 주석에 복원
- EN: "(Note: John 7:53–8:11 — this story isn't in the earliest handwritten copies of John's Gospel.)"
- KO: "(참고: 요한복음 7:53–8:11 — 이 이야기는 가장 오래된 필사본에는 없어요.)"
- 근거: en_Mark.json 주석이 "Mark 16:9-20" 번호를 보존하는 선례와 일치.

## 오탐 1 — ch1 idx1 [badge 1-2] number: 1
- MSG: "The Word was **first**, the Word present to God..."
- checker가 서수 "first"를 숫자 1로 추출.
- EN: "Before anything existed—before the universe, before time itself—the Word was already there."
- "말씀이 맨 처음이었다"는 의미가 풀어쓰기로 완전 보존됨. 서수 paraphrase는 1John·Hebrews 감사에서 이미 오탐으로 문서화된 클래스.
- 판정: **오탐**

## 오탐 2 — ch1 idx11 [badge 22] name: exasperated
- MSG: "**Exasperated**, they said, \"Who, then?..."
- EN: "**Frustrated**, they said, \"Then who ARE you?!..."
- 감정 기술어의 teen paraphrase. 의미 손실 없음. Hebrews #4/#6("Exasperated" → "furious")과 동일한 오탐 클래스.
- 판정: **오탐**

## 오탐 3 — ch2 idx13 [badge 20-22] number: 2
- MSG: "...They then put **two and two together** and believed..."
- checker가 관용구 "two and two together"(추론하다)를 숫자 2로 추출.
- EN: "Then it clicked, and they believed both what was written in Scripture and what Jesus had said."
- 관용구의 실제 의미(깨닫다)가 완전 보존됨. 진짜 숫자 "forty-six years"·"three days"는 EN에 그대로 있음.
- 판정: **오탐** (관용구 paraphrase — checker 알려진 오탐 클래스)

## 오탐 4 — ch7 idx10 [badge 25-27] number: 1
- MSG: "Isn't this **the one** they were out to kill? ... and **no one** is stopping him."
- checker의 `_one_is_numeric` 규칙이 "the one"을 숫자 1로 추출.
- EN: "Isn't this **the guy** they wanted to kill? ... and **nobody's** stopping him."
- 대명사 paraphrase. 1John FAIL 1/3("the one" → "someone"/"anyone"), Hebrews #18("Each one" → "All")과 동일한 오탐 클래스.
- 판정: **오탐**

## 오탐 5 — ch8 idx1 [badge 1-2] name: swarms
- MSG: "**Swarms** of people came to him."
- checker가 문장 첫머리 대문자 단어 "Swarms"를 이름 토큰으로 취급.
- EN: "Crowds of people **swarmed** to him." — 어근 "swarm"이 동사형으로 그대로 존재. 내용 손실 없음.
- 판정: **오탐** (문두 대문자 오인 — 어근 보존)

## 오탐 6 — ch8 idx23 [badge 42-47] number: 1
- MSG: "Why can't you understand **one word** I say? ... Can **any one** of you convict me..."
- EN: "Why can't you understand **a word** I say? ... Can **any of you** convict me..."
- "one word" → "a word", "any one" → "any of you"는 부정/불정 대명사 paraphrase. 의미 완전 동일. Hebrews #8("No one elects himself" → "you don't just decide"), #18("Not one" → "None")과 동일한 오탐 클래스.
- 판정: **오탐**

결론: 6건 모두 오탐. 실제 이슈 0건. 감사 리포트(audit_John.md)의 이슈 5건(3:16-18, 4:21-23, 3:7-8, 3:34-36, 3:5-6)은 현행 JSON에 모두 반영되어 있음(각각 MSG 대조로 재확인).
