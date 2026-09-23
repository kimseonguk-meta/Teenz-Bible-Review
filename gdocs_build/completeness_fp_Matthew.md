# Matthew 기계적 완전성 검사 — 잔여 FAIL 18건 오탐 판정 근거

검사: `python3 gdocs_build/completeness_check.py fixes/en_matthew_01-03.json fixes/en_matthew_04-07.json fixes/en_matthew_08-10.json fixes/en_matthew_11-14.json fixes/en_matthew_15-28.json`
결과: 28장 454문단, 이름 토큰 581개·숫자 토큰 175개·인용구 2개 중 FAIL 18건 — 전수 대조 후 전부 오탐으로 판정. 실제 누락·요약·의미 반전 0건.

수정으로 해소된 2건 (오탐 아님):
- ch15 idx1 [1-2] name: pharisees — MSG "Pharisees and religion scholars"에서 EN "Some religious experts"가 "Pharisees"를 누락한 실제 이슈. EN→"Some Pharisees and religious experts", KO→"바리새파와 율법학자들이"로 수정 완료.
- ch28 idx5 [18-20] name: jesus — EN4(도입부 "dropped this bombshell")가 MSG 18절 도입부("Jesus, undeterred, went right ahead and gave his charge")를 렌더링하는데 배지/msg_ranges가 '16-17'이어서 checker/doc 매칭에서 제외된 실제 모델링 이슈. EN/KO verseRanges 및 msg_ranges를 '16-20'으로 정정 (선언된 split 18-20→paras[4,5]와 일치).

---

## FAIL 1 — ch1 idx15 [badge 24-25] name: god
- MSG 24-25: "He did exactly what **God's angel** commanded in the dream"
- EN: "did exactly what **the angel** told him to do"
- "God's"는 소유격 수식어이며, 꿈속 천사·명령이라는 문맥에서 의미 손실 없음. checker의 BIBLICAL_NAMES 상시 검사 아티팩트.
- 판정: **오탐**

## FAIL 2 — ch2 idx8 [badge 13] name: god
- MSG 13: "**God's angel** showed up again in Joseph's dream"
- EN: "**an angel** showed up in Joseph's dream again"
- FAIL 1과 동일. 꿈·명령 문맥에서 "하나님의 천사"임이 자명.
- 판정: **오탐**

## FAIL 3 — ch4 idx0 [badge 1-3] number: 1
- MSG 1-3: "which the Devil took advantage of in **the first test**" — checker가 "first"를 숫자 1로 추출.
- EN: "Then the devil moved in" — 세 가지 시험이 순서대로 전부 서술되어 "첫 번째"라는 순서 정보가 서사 순서로 보존됨.
- 판정: **오탐** (서수 순서 표지 — 서사 순서로 보존)

## FAIL 4 — ch6 idx7 [badge 7-13] number: 3
- MSG 7-13 (주기도문): "Keep us alive with **three square meals**."
- EN: "Keep us alive with **enough food to eat every day**."
- "three square meals"는 '하루 세 끼'라는 영어 관용구이지 사실적 숫자 3이 아님. "매일 먹을 충분한 음식"으로 의미 완전 보존.
- 판정: **오탐** (관용구 숫자)

## FAIL 5 — ch11 idx1 [badge 2-3] number: 1
- MSG 2-3: "Are you **the One** we've been expecting" — checker가 "the One"을 숫자 1로 추출 (`_one_is_numeric`: 앞 단어가 'the'면 numeric).
- EN: "Are you really **the Messiah** we've been waiting for" — "the One"의 정확한 teen paraphrase (Messiah=그리스도).
- 판정: **오탐** (칭호 'the One'의 숫자 오인 — 1John FP-1과 동일 클래스)

## FAIL 6 — ch12 idx24 [badge 43-45] quote: defiling, bedevil, spotlessly
- MSG 43-45 인용 전체와 EN idx24+idx25를 문장 단위로 대조:
  - "defiling evil spirit" → "nasty, evil spirit" / "expelled" → "kicked out" / "drifts" → "wanders" / "oasis" → "a place to rest" / "bedevil" → "mess with" / "old haunt" → "old place" / "spotlessly clean, but vacant" → "sparkling clean, but totally empty inside" / "rounds up seven other spirits" → "gathers seven other spirits" / "whooping it up" → "throwing a huge party" / "far worse off" → "way worse off"
  - 결론부 "That's what this generation is like…"는 EN idx25에 의미 그대로 존재.
- 정당한 teen paraphrase이며 의미 요소 전부 보존. checker의 고유단어 커버리지 임계값(0.4) 아티팩트.
- 판정: **오탐**

## FAIL 7 — ch19 idx12 [badge 17] number: 1
- MSG 17: "**God** is **the One** who is good" — "the One" 숫자 오인.
- EN: "**Only God** is truly good" — 의미 동일.
- 판정: **오탐** (FAIL 5와 동일 클래스)

## FAIL 8 — ch20 idx4 [badge 24-28] number: 2
- MSG 24-28: "thoroughly disgusted with **the two brothers**"
- EN: "thoroughly disgusted with **James and John**" — 두 형제를 실명으로 지칭 (더 구체적, 정보 손실 없음).
- 판정: **오탐** (실명 지칭이 숫자 'two'를 대체)

## FAIL 9 — ch21 idx1 [badge 10-14] name: unnerved
- MSG 10: "**Unnerved**, people were asking" — 문장 첫머리 대문자로 시작된 일반 형용사.
- checker의 extract_names가 빈도 목록에 없는 대문자 단어를 인명으로 오인. "Unnerved"는 사람이 아님.
- 판정: **오탐**

## FAIL 10 — ch21 idx2 [badge 15-17] name: god, word
- MSG 15-16: "haven't you read in **God's Word**, 'From the mouths of children…'"
- EN: "Haven't you ever read **the scripture** that says, 'From the mouths of children…'" — "God's Word"=성경. 의미 동일.
- 판정: **오탐**

## FAIL 11 — ch25 idx3 [badge 14-18] number: 4000
- MSG 14-18: "to **a third one thousand**" — checker의 `_parse_num_seq`가 서수 "third"(3)와 금액 "one thousand"를 합쳐 4000으로 오추출 (**checker 파싱 버그**).
- 실제 숫자 5000/2000/1000은 EN에 "$5,000/$2,000/$1,000"으로 전부 존재. "The first guy"/"The second guy"의 서수 1·2도 EN에 존재.
- 판정: **오탐** (checker 버그 — 서수와 금액의 오결합)

## FAIL 12 — ch25 idx4 [badge 19-25] number: 1
- MSG 19-25: "**The one** given five thousand dollars" — "the one" 대명사를 숫자 1로 오인.
- EN: "**The guy** with the $5,000" — 의미 동일.
- 판정: **오탐** (대명사 one의 숫자 오인 — 1John FP-1과 동일 클래스)

## FAIL 13 — ch25 idx9 [badge 41-46] number: 1
- MSG 45: "Whenever you failed to do **one of** these things" — 관용구 "one of"를 숫자 1로 추출.
- EN: "whenever you failed to help someone who was overlooked" — 의미 동일.
- 판정: **오탐** (관용구 "one of")

## FAIL 14 — ch27 idx0 [badge 1-2] number: 1
- MSG 1-2: "In the **first** light of dawn" — 시간 관용구의 서수.
- EN: "As soon as the sun was up" — 의미 동일.
- 판정: **오탐** (시간 관용구 서수)

## FAIL 15 — ch27 idx1 [badge 3-10] number: 1 (a)
- MSG 3-4: "Judas, **the one who** betrayed him" — 대명사.
- EN: "Judas, **the friend who** betrayed him" — 의미 동일.
- 판정: **오탐** (대명사 one의 숫자 오인)

## FAIL 16 — ch27 idx1 [badge 3-10] number: 1 (b)
- MSG 6-10: "The price of **the one** priced by some sons of Israel" — 대명사.
- EN: "the price set **on him** by the people of Israel" — 의미 동일.
- 판정: **오탐** (대명사 one의 숫자 오인)

## FAIL 17 — ch27 idx3 [badge 15-23] number: 2
- MSG 21: "Which of **the two** do you want me to pardon?"
- EN: "'Who should I release? **Barabbas, or Jesus**, the so-called Christ?'" — 두 사람을 실명으로 지칭.
- 판정: **오탐** (실명 지칭이 숫자 'two'를 대체 — FAIL 8과 동일 클래스)

## FAIL 18 — ch28 idx0 [badge 1-4] number: 1
- MSG 1-4: "as the **first** light of the new week dawned" — 시간 관용구의 서수.
- EN: "at the crack of dawn on Sunday" — 의미 동일.
- 판정: **오탐** (시간 관용구 서수 — FAIL 14와 동일 클래스)

---

결론: 18건 모두 오탐 (checker 알려진 오탐 클래스: 대명사 one, 칭호 the One, 관용구 숫자/서수, 문장 첫머리 대문자, 정당한 teen paraphrase, 실명 지칭, checker 파싱 버그). 실제 누락·요약·의미 반전 0건.
