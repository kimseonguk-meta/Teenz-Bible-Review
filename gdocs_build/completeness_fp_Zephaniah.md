# Zephaniah completeness_check 오탐(False Positive) 기록

- 대상: `fixes/en_Zephaniah.json` (MSG = `msg_Zephaniah.txt`, parsed 20 units: ch1 6 / ch2 6 / ch3 8)
- 검사일: 2026-09-24
- 검사기: `gdocs_build/completeness_check.py`
- 최종 상태: FAIL 1건을 오탐으로 판정. 진짜 누락/오역은 전부 복원 완료
  (복원 내역은 `gdocs_build/audit_Zephaniah.md` 참조).
- validator: `PASS: 3개 장 모두 통과`

## 오탐 판정 목록

1. ch1 idx5 [badge 7-13] `name: moneymaking`
   - MSG: "Moneymaking has had its day."
   - TEEN: "'cause your money-making days are over."
   - 사유: 동일한 단어의 하이픈 표기 차이("Moneymaking" vs "money-making").
     의미·단어 모두 Teen EN에 존재함. checker의 하이픈 정규화 한계.

## (참고) 검사 중 복원한 토큰

- ch1 idx5 [badge 7-13] `name: reverent` — 1차 검사에서 FAIL.
  MSG "Reverent silence before me" → TEEN이 "Show some respect"로만
  풀어썼던 것을 "'Yo, quiet now! Reverent silence before God, the Master."로
  복원하여 재검사에서 통과. (오탐이 아닌 실제 복원)
