# 2 John 기계적 완전성 검사 — 잔여 FAIL 2건 판정 근거

검사: `python3 gdocs_build/completeness_check.py fixes/en_2John.json`
결과: 1장 7문단, 이름 토큰 13개 중 FAIL 1건, 숫자 토큰 1개 중 FAIL 1건.
(검사 전 수정 1건: badge 7 "Jesus"→"Jesus Christ" 복원 — 확정 이름 규칙에 따라 실제 이슈로 처리,
`fixes/en_2John.json` changes 로그에 기록. 수정 후 "christ" 토큰 해소됨.)

## FAIL 1 — ch1 idx2 [badge 4-6] number: 1
- MSG 4-6: "This is the **first** thing you heard, and nothing has changed."
- EN: "You've known this **from the jump**, nothing's new here."
- KO: "너희가 **처음부터** 들었던 거, 바뀐 게 하나도 없어."
- "first"는 서수(첫 번째로 들은 것)이며, EN "from the jump"(처음부터)와 KO "처음부터"가
  의미를 완전히 보존. 1 John의 "a second reminder"→"One more reminder" 오탐과 동일 클래스.
- 판정: **오탐** (서수 paraphrase — checker 알려진 오탐 클래스).

## FAIL 2 — ch1 idx4 [badge 7] name: deceiver
- MSG 7: "Give them their true title: **Deceiver**! Antichrist!"
- EN: "Let's call them what they are: **Fakers** and Anti-Christs. Total posers."
- KO: "걔네들한테 진짜 이름을 붙여주자: **속이는 자**! 적그리스도! 그냥 완전 가짜야."
- "Deceiver"(속이는 자)를 teen voice "Fakers"(사기꾼/가짜)로 paraphrase.
  문맥("smooth-talking con artists... trying to sell you the lie")에서 의미 동일 —
  거짓을 팔아 속이는 자 = faker. KO는 "속이는 자"로 직역 유지.
  확정 이름 규칙(복합명 일부 탈락)은 "Jesus Christ" 건에만 해당하며 이미 복원됨.
- 판정: **허용 paraphrase** (의미 완전 보존, teen voice).

결론: 잔여 2건 모두 실제 누락·요약·의미 반전 아님. 수정 1건("Jesus Christ" 복원) 반영 완료.
