# Philemon 기계적 완전성 검사 오탐 기록 (2026-09-23)

`completeness_check.py` FAIL 3건 전수 수동 대조 결과 — 전부 오탐. 실제 누락 0건.

## FP1. ch1 idx1 [badge 4-7] — name "christ"
- MSG: "people recognize Christ in all of it"
- EN: "so everyone can see Jesus's transformation in us" — "Christ"를 "Jesus's"로 호칭. 동일 인물, 틴 문체 선택.
- 판정: 오탐 (동일 인물 호칭 교체 — Colossians FP2와 동일 유형). 의미 손실 없음.

## FP2. ch1 idx3 [badge 8-9] — name "christ"
- MSG: "As Christ's ambassador"
- EN: "As Jesus's top agent" — "Christ's"를 "Jesus's"로 호칭. 동일 인물.
- 판정: 오탐 (동일 인물 호칭 교체). 의미 손실 없음.

## FP3. ch1 idx6 [badge 17-20] — name "christ"
- MSG: "You'll be doing it for Christ"
- EN: "You'll be doing it for Jesus" — "Christ"를 "Jesus"로 호칭. 동일 인물.
- 판정: 오탐 (동일 인물 호칭 교체). 의미 손실 없음.

## 총괄
- 3건 전부 "Christ → Jesus(의)" 동일 인물 호칭 교체. MSG 요소 누락 없음.
- EN 전체에서 "Jesus" 선호는 의도적 틴 문체 (Philemon은 예수님 직접 언급이 잦은 편지 특성상 자연스러움).
