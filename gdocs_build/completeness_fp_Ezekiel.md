# Ezekiel Completeness Checker — False Positive 기록

## 개요
`completeness_check.py`는 MSG 이름/숫자/인용구를 Teen 텍스트에서 기계적으로 찾는다.
아래는 genuine omission이 아닌 것으로 확인된 케이스들이다.

## 카테고리별 False Positive

### 1. 호칭/대소문자 차이 (name: god)
- MSG "God" → Teen "GOD", "Lord", "the Master" 등
- 의미 동일, Teen voice의 자연스러운 변형
- 해당: ch5, ch17, ch46, ch47 등 다수

### 2. 숫자 표기 차이 (number)
- MSG "six" → Teen "6", MSG "forty" → Teen "40" 등
- 숫자의 값이 동일하면 OK
- 해당: ch40 (측량 수치), ch45 등
- 단, 숫자가 완전히 생략된 경우는 genuine (ch46 "six workdays" → 수정됨)

### 3. Teen-friendly paraphrase (quote)
- "obscenities" → "disgusting things", "nasty stuff"
- "desecrate" → "trash", "disrespect", "violate"
- "seduces" → "lures", "tempts"
- "furiously" → "super angry", "fuming"
- MSG의 강한 표현을 10대가 읽기 편하게 순화한 것으로, 의미가 유지되면 OK (원칙 5)

### 4. 분할 배지 페어링 아티팩트
- 하나의 MSG 유닛이 여러 Teen 문단으로 나뉜 경우, 검사기는 각 문단을 독립적으로 전체 MSG 유닛과 비교
- 예: ch25 [1-5] 분할에서 intro 문단("God's message hit me up:")만 검사하면 "Ammon"이 없다고 나오지만, 다음 문단에 있음
- 예: ch7 [1-4] 분할에서 첫 문단만 검사하면 "Endtime"이 없다고 나오지만, 둘째 문단에 있음
- 해당: ch7, ch25, ch37 [3] 등

### 5. 이름 포함 확인됨 (checker 오탐)
- ch8 Asherah: Teen에 "Asherah" 명시됨 ("pagan goddess, Asherah")
- ch16 Canaanites: "your roots are in Canaan" — 의미 동등
- ch44 Israelite: "a virgin from the people of Israel" — 의미 동등
- ch48 Zadokites: "descendants of Zadok" — 의미 동등

### 6. 불명확한 토큰화 (name 붙음)
- "lebanonand", "ethiopiawhen", "rotand" 등 — checker의 토큰 분리 오류
- 실제 텍스트에는 정상적으로 포함됨

## Genuine으로 확인되어 수정한 케이스
1. ch11: "son of Azzur", "son of Benaiah" 생략 → 복원
2. ch27: "Bedouin" 생략 → 복원
3. ch37: "four winds" → "from all over" → "four winds"로 복원
4. ch39: "Bashan" 생략 → 복원
5. ch46: "six" (six working days) 생략 → 복원
