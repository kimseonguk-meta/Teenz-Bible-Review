# Habakkuk completeness_check 오탐(False Positive) 기록

- 대상: `fixes/en_Habakkuk.json` (MSG = `msg_Habakkuk.txt`, parsed 19 units)
- 검사일: 2026-09-24
- 검사기: `gdocs_build/completeness_check.py`
- 최종 상태: 검사 중 발견된 FAIL 1건은 오탐이 아니라 진짜 누락으로 판정해 직접 복원함.
  복원 후 재검사 PASS (Checked 3 chapters, 22 paragraphs, 24 name tokens, 2 number tokens).
- validator: `PASS: 3개 장 모두 통과`

## 복원한 FAIL (오탐 아님)

1. ch3 idx3 [badge 8-16] `number: 4`
   - MSG: "Scattered they were to the four winds—"
   - TEEN (수정 전): "They were scattered everywhere—and ended up as shark food!"
   - 복원: "They were scattered to the four winds—and ended up as shark food!"
   - 사유: "four winds"는 관용어이나 MSG가 명시한 이미지이므로 teen voice 유지한 채로 복원.
     KO는 이미 "사방으로 흩어져서"라 1:1 일치.

## 오탐 판정 목록

없음. (잔여 FAIL 0건)
