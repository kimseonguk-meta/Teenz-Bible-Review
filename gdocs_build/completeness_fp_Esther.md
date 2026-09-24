# completeness_check false positives — Esther (2026-09-24)

검사 실행: `python3 gdocs_build/completeness_check.py fixes/en_Esther.json`
최종 결과: 94개 문단 중 3건의 FAIL, 전부 검사기 오탐으로 판정. 아래 사유로 수정 불필요.

## 1. ch1 idx5 [badge 12-15] name: seething — 오탐
- MSG: "Seething with anger over her insolence, the king called in his counselors..."
- 검사기가 문장 첫머리에 대문자로 나온 일반 단어 "Seething"을 고유명사로 오인.
- "seethe"는 일반 동사/형용사(끓어오르다)이며, Teen EN에 "He was absolutely fuming"으로 의미가 살아 있음.
- 조치: 수정 없음.

## 2. ch9 idx7 [badge 16-19] number: 27 — 오탐
- MSG: "...since the Jews had banded together on both the thirteenth and fourteenth days..."
- 검사기의 number-word 파서가 "thirteenth and fifteenth"류 구문을 하나의 숫자로 합산(13+14=27)함.
- 실제로는 13일과 14일 두 개의 날짜이며, Teen EN에 "both the 13th and 14th"로 둘 다 정확히 존재.
- 조치: 수정 없음.

## 3. ch9 idx8 [badge 20-22] number: 29 — 오탐
- MSG: "calling for an annual celebration on the fourteenth and fifteenth days of Adar"
- 검사기가 "fourteenth and fifteenth"를 합산(14+15=29)함.
- 실제로는 14일과 15일 두 개의 날짜이며, Teen EN에 "the 14th and 15th of Adar"로 둘 다 정확히 존재.
- 조치: 수정 없음.

## 검사기가 잡아내어 실제로 수정한 항목 (참고)
- ch1 p2: "one-of-a-kind" → "every single cup was one of a kind" (number 1 복원)
- ch1 p6: 인용구 속 "King Xerxes" 복원 (MSG 1:17)
- ch1 p7: "the laws of the Persians and Medes", "permanently banned from King Xerxes' presence" 복원 (MSG 1:19) — 배지 오기(16-19) 정정 후 올바른 문단(p7)에 귀속됨
- ch1 배지 정정: p2 4-8→4-7, p6 16-19→16-18, p7 20-21→19-20 (MSG 유닛과 일치)
- ch2 p0: "second thoughts" 복원 (MSG 2:1)
- ch2 p2: "a Benjaminite" 복원 (MSG 2:5)
