# Hosea completeness_check 오탐(False Positive) 기록

- 대상: `fixes/en_Hosea.json` (MSG = `msg_Hosea.txt`, parsed 66 units)
- 검사일: 2026-09-24
- 검사기: `gdocs_build/completeness_check.py`
- 최종 상태: FAIL 3건 전부 오탐으로 판정. 진짜 누락 4건(ch3 p0 Israelite people, ch6 p0 third day,
  ch9 p4 dissipated/clamor, ch10 p3 thistles/crabgrass)은 모두 복원 완료
  (복원 내역은 `gdocs_build/audit_Hosea.md` 참조).
- validator: `PASS: 14개 장 모두 통과`

## 오탐 판정 목록

1. ch4 idx0 [badge 1-3] `number: 1`
   - MSG: "No one knows the first thing about God."
   - TEEN: "no knowledge of God anywhere in this country"
   - 사유: 서수(ordinal) "first"에서 추출된 숫자. 내용상 숫자(수량·번호)가 아님.
     의미("하나님을 아는 지식이 전혀 없음")는 보존됨.

2. ch4 idx1 [badge 4-6] `number: 1`
   - MSG: "You, priest, are the one in the dock."
   - TEEN: "Your priests are the main problem!"
   - 사유: 관용 표현 "the one in the dock"에서 추출된 숫자. 내용상 숫자가 아님.

3. ch8 idx0 [badge 1-3] `name: predictably`
   - MSG: "Predictably, Israel cries out, 'My God! We know you!'"
   - TEEN: "And what's their response? They cry out, 'My God! We know you!'"
   - 사유: 부사 "Predictably"를 고유명사로 오분류. 의미("예상대로/뻔뻔하게")는
     TEEN의 "And what's their response?" 구조에 녹아 있음.
