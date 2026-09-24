# Joel completeness_check 오탐(False Positive) 기록

- 대상: `fixes/en_Joel.json` (MSG = `msg_Joel.txt`, parsed 26 units)
- 검사일: 2026-09-24
- 검사기: `gdocs_build/completeness_check.py`
- 최종 상태: FAIL 3건 전부 오탐으로 판정. 진짜 누락/오역 12건(EN 본문 수정
  12항: ch1 메뚜기 4종 명칭·like it or not·dressed in black·Who needs them,
  ch2 clouds with no silver lining·consecrate the congregation·MSG식 메뚜기 4종,
  ch3 godless nations 오역·no cap 순화·Get your act together·stars burn out 오역·
  Egypt weeds in a vacant lot)은 모두 복원 완료
  (복원 내역은 `gdocs_build/audit_Joel.md` 참조).
- validator: `PASS: 3개 장 모두 통과`

## 오탐 판정 목록

1. ch2 idx2 [badge 7-11] `name: undaunted`
   - MSG: "Undaunted and fearless, unswerving, unstoppable."
   - TEEN: "They're fearless, unstoppable, and they just keep coming."
   - 사유: "undaunted"는 "fearless"의 동의어. TEEN의 "fearless, unstoppable,
     just keep coming"에 의미("주눅들지 않고 계속 밀고 옴")가 전부 녹아 있음.
     checker의 동의어 매칭 한계.

2. ch2 idx5 [badge 15-17] `name: consecrate`
   - MSG: "Get everyone there. Consecrate the congregation."
   - TEEN: "The whole community needs to be there—consecrated, set apart for this."
   - 사유: 감사 과정에서 TEEN에 "consecrated, set apart for this"를 복원 완료.
     검사기 토큰 변형 매칭이 "consecrated"를 잡지 못한 오탐.

3. ch3 idx7 [badge 18-21] `name: judean`
   - MSG: "the brutalities to the Judean people"
   - TEEN: "the messed-up things they did to the people of Judah"
   - 사유: "Judean people" = "the people of Judah". 동일 의미의 다른 표현.
     checker의 alias 매칭 한계.
