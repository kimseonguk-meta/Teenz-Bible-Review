# Colossians 기계적 완전성 검사 오탐 기록 (2026-09-23)

`completeness_check.py` FAIL 3건 전수 수동 대조 결과 — 전부 오탐. 실제 누락 0건.

## FP1. ch3 idx5 [badge 12-14] — number "2"
- MSG: "content with second place" → checker가 "second"에서 숫자 토큰 "2" 추출.
- EN: "be cool with not being first" — "second place"를 "not being first"로 의역. 개념(1등이 아니어도 괜찮아함) 보존됨.
- 판정: 오탐 (paraphrase equivalent). 의미 손실 없음.

## FP2. ch4 idx2 [badge 2-4] — name "christ"
- MSG: "telling the mystery of Christ"
- EN: "talk about the big secret of Jesus" — "Christ"를 "Jesus"로 호칭. 동일 인물을 가리키며, EN 전체에서 "Jesus" 선호는 틴 문체 선택.
- 판정: 오탐 (동일 인물 호칭 교체). 의미 손실 없음.

## FP3. ch4 idx6 [badge 12-13] — number "1"
- MSG: "Epaphras, who is one of you" → checker가 대명사 "one"에서 숫자 토큰 "1" 추출.
- EN: "Epaphras, who's from your town" — "one of you"(동료 성도)를 "from your town"(출신지)으로 의역. KO도 "너네 고향 사람"으로 동일.
- 판정: 오탐 (대명사 one 오인 — Acts 오탐 문서의 동일 유형). 의미 손실 없음.

## 총괄
- 검사: 4장 41문단, 72 name tokens, 6 number tokens.
- 실제 누락: 0건. 게이트 5 PASS (오탐 문서화).
