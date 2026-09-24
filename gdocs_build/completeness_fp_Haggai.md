# Haggai completeness_check 오탐(False Positive) 기록

- 대상: `fixes/en_Haggai.json` (MSG = `msg_Haggai.txt`, parsed 22 units)
- 검사일: 2026-09-24
- 검사기: `gdocs_build/completeness_check.py`
- 최종 상태: 검사 중 발견된 FAIL 1건은 고유명사 호칭 누락으로 판정해 직접 복원함.
  복원 후 재검사 PASS (Checked 2 chapters, 30 paragraphs, 48 name tokens, 18 number tokens, 1 quoted spans).
- validator: `PASS: 2개 장 모두 통과`

## 복원한 FAIL (오탐 아님)

1. ch2 idx0 [badge 1-3] `name: word`
   - MSG: "On the twenty-first day of the seventh month, the Word of God came through the prophet Haggai:"
   - TEEN (수정 전): "On the 21st day of the 7th month, a message from God came through the prophet Haggai."
   - 복원: "On the 21st day of the 7th month, the Word of God came through the prophet Haggai."
   - 사유: MSG의 고유 호칭 "Word of God"은 검사기가 name 토큰으로 인식했고,
     의미상 "message from God"과 동일하지만 MSG 고유 표현이므로 teen voice 유지한 채로 복원.
     KO도 "하나님의 말씀이 학개 예언자를 통해서 전해졌대"로 1:1 반영.

## 오탐 판정 목록

없음. (잔여 FAIL 0건)
