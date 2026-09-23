# 1 John 기계적 완전성 검사 — 잔여 FAIL 3건 오탐 판정 근거

검사: `python3 gdocs_build/completeness_check.py fixes/en_1John.json`
결과: 5장 49문단, 이름 토큰 99개 FAIL 0, 숫자 토큰 11개 중 FAIL 3건 — 전부 문서화된 오탐.

## FAIL 1 — ch2 idx3 [badge 4-6] number: 1
- MSG 4-6: "...But **the one who** keeps God's word is the person in whom we see God's mature love."
- checker가 "the one"을 숫자 1로 추출 (`_one_is_numeric`: 앞 단어가 'the'면 numeric 판정).
- EN: "But when **someone** keeps God's word, we see God's love growing mature in them."
- 여기서 "one"은 대명사("the one who" = "그 사람")이지 숫자 1이 아님. teen-voice "someone"으로 바꾸는 건 의미 손실이 아님.
- 판정: **오탐** (대명사 one의 숫자 오인 — checker 알려진 오탐 클래스).

## FAIL 2 — ch2 idx7 [badge 12-13] number: 2
- 숫자 2는 badge 12-13 문단 자체가 아니라, v13을 공유하는 MSG 13-14 문단의 "**a second reminder**, dear children"에서 옴 (union semantics).
- EN idx8 [badge 13-14]: "**One more reminder**, dear children: you know the Father from personal experience."
- "second reminder" → "one more reminder"는 서수 표현의 정당한 teen paraphrase. 의미 완전 보존 (두 번째로 상기시킨다는 뜻 그대로).
- 판정: **오탐** (서수 paraphrase — checker 알려진 오탐 클래스).

## FAIL 3 — ch3 idx4 [badge 9-10] number: 1
- MSG 9-10: "...**The one who** won't practice righteous ways isn't from God, nor is **the one who** won't love brother or sister. A simple test."
- checker가 "The one"을 숫자 1로 추출 (FAIL 1과 동일한 "the one" 규칙).
- EN: "anyone who doesn't practice what is right isn't from God — and neither is anyone who won't love a brother or sister."
- 여기서 "one"은 대명사지 숫자 1이 아님. "anyone" 치환은 의미 동일.
- 판정: **오탐** (대명사 one의 숫자 오인 — checker 알려진 오탐 클래스).

결론: 3건 모두 오탐. 실제 누락·요약·의미 반전 0건.
