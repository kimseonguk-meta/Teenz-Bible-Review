# Nehemiah 기계적 완전성 검사 — 잔여 FAIL 21건 오탐 판정 근거

검사: `python3 gdocs_build/completeness_check.py fixes/en_Nehemiah.json`
결과: 13장 316문단, 이름 토큰 755개·숫자 토큰 113개·인용구 0개 중 FAIL 21건 — 전수 대조 후 전부 오탐으로 판정. 실제 누락·요약·의미 반전 0건.

(참고: 이번 감사에서 실제 누락은 수정 단계에서 이미 복원됨 — ch3 부칭 20건, ch5 forty shekels, ch6 부칭 5건, ch7 헌금 숫자 3건, ch8 레위인 10명·인용구, ch9 cisterns, ch10 세율·Dedication-Offerings·grain, ch11 지명 3건, ch12 음악가 8명·Hashaiah, ch13 창고 물품·부칭 등. 아래 21건은 그와 별개인 checker 아티팩트.)

---

## FAIL 1 — ch1 idx0 [badge 1-2] name: kislev
- MSG 1-2: "It was the month of **Kislev** in the twentieth year"
- EN p1: "So, it was **December**, in the twentieth year of the king's reign"
- 히브리 달력 월명을 teen 독자가 아는 그레고리력 월명으로 의역한 것. 삭제가 아니라 번역 선택.
- 판정: **오탐** (월명 의역)

## FAIL 2 — ch1 idx0 [badge 1-2] number: 1
- MSG 1-2: "Hanani, **one** of my brothers"
- EN p1: "my bro Hanani showed up with some other guys from Judah"
- "one of my brothers" → "my bro Hanani" + "some other guys"로 의미 보존. checker가 "one"을 숫자 1로 추출한 아티팩트.
- 판정: **오탐**

## FAIL 3 — ch1 idx5 [badge 7-9] number: 4
- MSG 7-9: "I'll scatter you to the **four** winds"
- EN p5: "you scattered us all over the world"
- "four winds"는 '사방팔방'이라는 영어 관용구. "all over the world"로 의미 완전 보존 (Matthew FP-4와 동일 클래스).
- 판정: **오탐** (관용구 숫자)

## FAIL 4 — ch2 idx0 [badge 1-2] name: nisan
- MSG 1-2: "It was the month of **Nisan** in the twentieth year"
- EN p0: "So, it was **April**, during the 20th year"
- FAIL 1과 동일. 월명 의역.
- 판정: **오탐** (월명 의역)

## FAIL 5 — ch3 idx1 [badge 3-5] name: tekoites
- MSG 3-5: "the **Tekoites**"
- EN p1: "the guys from **Tekoa**"
- 동일 어근의 다른 형태. 의미 손실 없음.
- 판정: **오탐** (어형 차이)

## FAIL 6 — ch4 idx11 [badge 21] number: 1
- MSG 21: "from **first** light until the stars came out" — checker가 "first"를 숫자 1로 추출
- EN p11: "working from **sunup** until the stars came out"
- "first light" = 새벽·동틀녘. "sunup"으로 의미 보존.
- 판정: **오탐** (서수/관용 표현)

## FAIL 7 — ch7 idx4 [badge 6-60] name: priestly, levitical
- MSG 6-60: "**Priestly** families:" / "**Levitical** families:" (소제목)
- EN p38: "Now for the **priest** families:" / p43: "And the **Levite** families:"
- 동일 어근의 명사형. 소제목·명단 구조 그대로 유지됨.
- 판정: **오탐** (어형 차이)

## FAIL 8 — ch8 idx10 [badge 16-17] name: god
- MSG 16-17: "in the courts of **The Temple of God**"
- EN p10: "in the **Temple** courtyards"
- "God's"는 소유격 수식어. 유대 문맥에서 "Temple"은 자명하게 하나님의 성전 (Matthew FP-1과 동일 클래스 — checker의 BIBLICAL_NAMES 상시 검사 아티팩트).
- 판정: **오탐**

## FAIL 9 — ch8 idx11 [badge 18] number: 1
- MSG 18: "Ezra read ... every day, from the **first** to the last day" — checker가 "first"를 숫자 1로 추출
- EN p11: "Ezra read from the Book of God's Law **every single day** of the seven-day festival"
- "from the first to the last day"는 "every day"의 반복 강조. "every single day"로 의미 보존.
- 판정: **오탐** (서수 순서 표지)

## FAIL 10 — ch9 idx3 [badge 7-8] name: abramand
- MSG 7-8: "chose **Abram and** brought him" — checker 토크나이저가 "Abram and"를 "abramand"로 병합한 버그
- EN p3: "picked **Abram**, brought him all the way from Ur of the Chaldees, and changed his name to Abraham"
- 판정: **오탐** (checker 토크나이저 버그)

## FAIL 11 — ch9 idx3 [badge 7-8] number: 1
- MSG 7-8: "You're **the one**, God, the God who chose Abram" — checker가 "the one"을 숫자 1로 추출
- EN p3: "You're **the God** who picked Abram"
- "the one"은 강조 관용구. "the God who picked Abram"으로 의미 보존 (Matthew FP-5와 동일 클래스).
- 판정: **오탐** (칭호/강조어의 숫자 오인)

## FAIL 12 — ch9 idx4 [badge 9-15] name: fireto
- MSG 9-15: "a pillar of **fire, to** show them" — checker 토크나이저가 "fire, to"를 "fireto"로 병합한 버그
- EN p4: "with a **pillar of fire**, to show them which way to go"
- 판정: **오탐** (checker 토크나이저 버그)

## FAIL 13 — ch11 idx8 [badge 15-18] name: god
- MSG 15-18: "in charge of the outside work of **The Temple of God**"
- EN p9 (동일 split): "handled the **Temple's** external affairs"
- FAIL 8과 동일. 소유격 수식어 아티팩트.
- 판정: **오탐**

## FAIL 14 — ch11 idx14 [badge 22-23] number: 1
- MSG 22-23: "Uzzi was **one** of Asaph's descendants"
- EN p14: "This Uzzi guy was from Asaph's family line"
- "one of X's descendants" → "from X's family line"으로 의미 보존. checker의 "one" 숫자 추출 아티팩트.
- 판정: **오탐**

## FAIL 15 — ch11 idx16 [badge 25-30] name: judeans
- MSG 25-30: "Some of the **Judeans** lived in the villages"
- EN p16: "Some of the **people from Judah** lived in villages near their farms"
- 동일 의미의 풀어쓰기. 지명·인명 목록 자체는 p17-p33에 전수 보존 (Zorah 복원 포함).
- 판정: **오탐**

## FAIL 16 — ch11 idx35 [badge 31-36] name: levitical
- MSG 31-36: "some of the **Levitical** groups of Judah"
- EN p45: "some of the **Levite** groups from Judah"
- FAIL 7과 동일. 어형 차이.
- 판정: **오탐** (어형 차이)

## FAIL 17 — ch12 idx61 [badge 47] name: aaronites
- MSG 47: "what was dedicated to the **Aaronites**, the priests, and the Levites"
- EN p61: "set aside the dedicated portion for the Levites, and the Levites did the same for the **descendants of Aaron**"
- "Aaronites" = "Aaron의 자손". "descendants of Aaron"으로 의미 완전 보존.
- 판정: **오탐**

## FAIL 18 — ch13 idx0 [badge 1-3] name: ammonite, moabite
- MSG 1-3: "no **Ammonite** or **Moabite**"
- EN p0: "no one from **Ammon** or **Moab**"
- FAIL 5와 동일. 어형 차이.
- 판정: **오탐** (어형 차이)

## FAIL 19 — ch13 idx1 [badge 4-5] name: god
- MSG 4-5: "storerooms of **The Temple of God**"
- EN p1: "the **Temple's** storage rooms"
- FAIL 8·13과 동일. 소유격 수식어 아티팩트.
- 판정: **오탐**

## FAIL 20 — ch13 idx2 [badge 6-9] name: god
- MSG 6-9: "I asked ... the king" / EN p2: "I asked **God** if I could go back"
- EN에 "God"이 대문자로 존재하나 checker가 소문자 "god" 토큰과 매칭 실패한 대소문자 아티팩트.
- 판정: **오탐** (대소문자)

## FAIL 21 — ch13 idx5 [badge 15-16] name: tyrians, judeans
- MSG 15-16: "**Tyrians** ... selling it to the people of **Judah**"
- EN p5: "people from **Tyre** ... selling it to the **people of Judah**"
- FAIL 5·15와 동일. 어형 차이 / 풀어쓰기.
- 판정: **오탐**
