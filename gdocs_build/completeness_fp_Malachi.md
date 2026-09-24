# Malachi completeness_check 오탐(False Positive) 기록

- 대상: `fixes/en_Malachi.json` (MSG = `msg_Malachi.txt`, parsed 32 units, 4장)
- 검사일: 2026-09-24
- 검사기: `gdocs_build/completeness_check.py`
- 최종 상태: 검사 중 발견된 FAIL 8건 중 1건은 실제 누락으로 판정해 직접 복원함 (아래 "복원한 FAIL" 참조).
  복원 후 재검사 결과 잔여 FAIL 7건은 모두 오탐으로 판정 (검사 로직의 기계적 한계).
- validator: `PASS: 4개 장 모두 통과`

## 복원한 FAIL (오탐 아님)

1. ch2 idx5 [badge 13-15] `number: 2`
   - MSG: "And here’s a second offense: You fill the place of worship..."
   - TEEN (수정 전): "And here's another thing you're doing wrong: You flood the temple..."
   - 복원: "And here's the second thing you're doing wrong: You flood the temple..."
   - KO는 원래 "그리고 두 번째 잘못이 있음."으로 MSG와 일치했음.

## 오탐 (False Positive) — 수정 없음

1. ch1 idx0 [badge 1] `name: word`
   - MSG: "A Message. God’s Word to Israel through Malachi:"
   - TEEN: "Alright, so here's the 411. God has a message for the people of Israel, and he's delivering it through his prophet, Malachi."
   - 근거: "God's Word" → teen voice "God has a message"는 정당한 paraphrase. 내용 손실 없음.

2. ch1 idx6 [badge 6] `name: god`
   - MSG: "God-of-the-Angel-Armies is calling you on the carpet"
   - TEEN: "The LORD of Heaven's Armies is calling you out, you priests."
   - 근거: 동일 칭호의 다른 teen 표현. 내용 동일. (1장 시드는 "LORD of Heaven's Armies" 표기 사용 — 2장 "God of Angel Armies", 3장 "God-of-the-Angel-Armies"와 장별 표기 상이하나 내용 손실 아님.)

3. ch1 idx10 [badge 7-8] `name: god`
   - MSG: "The altar of God is not important anymore"
   - TEEN: "The Lord's altar isn't a big deal anymore"
   - 근거: 동일 지시 대상("Lord's" = God's). 내용 동일.

4. ch1 idx12 [badge 10] `name: god`
   - MSG: "The God-of-the-Angel-Armies is not pleased."
   - TEEN: "the LORD of Heaven's Armies" ("I'm not happy," says the LORD of Heaven's Armies.)
   - 근거: #2와 동일. 칭호 paraphrase.

5. ch1 idx15 [badge 14] `name: god, desecrating`
   - MSG 유닛 텍스트에 소제목 "Desecrating the Holiness of God"이 붙어 파싱됨.
   - 근거: 27권 감사 컨벤션상 소제목(§ 헤더)은 fixes JSON에 포함하지 않고 빌더가 MSG 원문에서 독에 삽입. 헤더 토큰은 검사 대상 아님. "god" 토큰도 #2~#4와 같은 칭호 paraphrase ("I'm a great King," says the LORD of Heaven's Armies).

6. ch3 idx0 [badge 1] `number: 1`
   - MSG v1 본문에 숫자 없음. 배지(verse number) 자체를 토큰으로 잡은 것으로 보임.
   - 근거: 내용 토큰이 아님.

7. ch4 idx0 [badge 1-3] `quote: colts, frolicking, tromp`
   - MSG: "like colts frisky and frolicking. And you'll tromp on the wicked."
   - TEEN: "like a young horse just let out to play. And you'll totally crush the wicked"
   - 근거: 정당한 teen paraphrase ("colts frisky and frolicking" → "young horse just let out to play", "tromp" → "crush"). 내용 손실 없음.
