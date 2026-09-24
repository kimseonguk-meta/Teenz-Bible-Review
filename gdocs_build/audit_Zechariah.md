# Zechariah 감사 리포트 (2026-09-24, 작업자) — MSG 전수 감사

기준: Eugene Peterson The Message(MSG) 영어 원문 = 유일한 최종 기준. KJV 미사용.
검수 방법: `msg_Zechariah.txt` 파싱(113 units, 14장) ↔ EN ↔ KO 문장·이름·숫자·인용구·반복요소 전수 대조.
시드: 앱 소스에서 재시드한 fixes JSON (2026-09-23 이전 구 감사본은 git history 참조용 — 배지 정정·복원 내용만 참조, § 헤더는 미추가).
결과: **전수 감사 + 수정 EN 본문 7건(6문단)·배지 13개 / KO 본문 2건·배지 13개. splits 31건 선언 (스탠딩 승인 규칙 (a)(b)(c) 충족 — MSG 대비 내용 온전, EN/KO 일치, 순수 가독성 구조 차이). merges 0건.**

## 0. MSG 원문 품질 검증

- `parse_msg_txt`: 14장 전부, 113 units (ch1 14 / ch2 6 / ch3 6 / ch4 8 / ch5 10 / ch6 9 / ch7 6 / ch8 13 / ch9 5 / ch10 4 / ch11 11 / ch12 7 / ch13 4 / ch14 10).
- 절 커버리지: 14장 전 절 완전 (212절), 누락 구간·boilerplate 없음. 특이사항: ch12/13/14 경계에 `### Washing Away Sins`/`### The Day Is Coming` 소제목이 있으나 파서가 장 전환("13 ", "14 1-2")을 정상 인식 — ch12는 v10-14에서 끝나고, ch13 v1–9·ch14 v1-2 정상 파싱됨 (수동 확인).

## 1. 장:절별 이슈 및 수정

### EN (본문 7건 — 6문단 + 배지 6장 13개 정정)

| 장:절 | MSG | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1:21 | "scatter Judah to the four winds" | 숫자 누락 | "scatter Judah everywhere" → "scatter Judah to the four winds" |
| 6:10 | "the home of Josiah son of Zephaniah" | 고유명사 누락 | "at Josiah's house" → "at Josiah son of Zephaniah's house" |
| 6:11 | "Joshua son of Jehozadak, the high priest" | 고유명사 누락 | "Joshua, the high priest" → "Joshua son of Jehozadak, the high priest" |
| 6:14 | "Hen son of Zephaniah" | 고유명사 누락 | "and Hen will be in charge" → "and Hen son of Zephaniah will be in charge" |
| 7:7 | "the Negev and Shephelah" | 지명 누락 | "the whole area was full of people" → "the whole area—the Negev and Shephelah—was full of people" |
| 7:13 | "I scattered them to the four winds" | 숫자 누락 | "He scattered them all over the place" → "He scattered them to the four winds" |
| 9:10 | "from the four winds to the seven seas" | 숫자 누락 | "from sea to shining sea" → "from the four winds to the seven seas" |

배지 정정 (MSG 단락 기준 오배지 — pairing 정확도 위해, verseRanges·msg_ranges 동시 수정):
| 장 | 문단 | 수정 전 | 수정 후 | 근거 |
|---|---|---|---|---|
| 1 | para5/6/7 | [10],[11],[12] | [9],[10],[11] | "Let me show you."는 MSG v9b, 이후 +1씩 밀림 (구 감사본도 [9],[9],[10],[11]로 정정했었음) |
| 4 | para2 | [2] | [2-3] | MSG v2-3 한 단락 문답 |
| 6 | para1 | [2] | [2-3] | MSG v2-3 |
| 7 | para3/para4 | [7-10]/[10] | [7-8]/[9-10] | MSG 7-10 한 단락을 intro(v7-8)/인용구(v9-10)로 분할 |
| 11 | para5 | [10] | [10-11] | MSG v10-11 (지팡이 꺾음 + 탐욕 주인들 목격) |
| 12 | para1/2/3/7/8 | [2-3]/[4]/[5-6]/[10-12]/[10-14] | [1-2]/[3]/[4-5]/[10-11]/[12-14] | +1 밀림 (구 감사본 정정과 동일) |

### KO (본문 2건 + 배지 EN과 동일 6장 13개)

| 장:절 | 문제 유형 | 수정 내용 |
|---|---|---|
| 7:7 | 지명 누락 (EN 1:1) | "예루살렘이 아직 잘나가고 사람 바글바글할 때" → "예루살렘
...[truncated 3357 chars]
## 2nd re-audit (Sep 24)

2nd-pass, MSG-원문 기준 14장 141문단 전수 재대조.

### checker 후보 4건 분류
- ch1 idx0 [1-4] number `8` → **실제 누락**. MSG "In the eighth month"가 EN에서 "around October"로 바뀌며 숫자 탈락 (KO는 "8월" 유지). EN 복원: "in the eighth month of the second year that Darius was king—around October,"
- ch5 idx3 [3-4] numbers `1, 2` → **실제 누락**. MSG "The first half of the book ... the second half"가 EN에서 "One side ... the other side"로 바뀜. EN 복원: "The first half of the scroll is for the thieves, and the second half is for the liars."
- ch10 idx3 [6-12] name `assyrian` → 오탐. EN "gather them from Assyria in the east", "Flashy Assyria will get exposed"에 2회 등장.
- ch10 idx3 [6-12] quote `brimming, leafy, brash` → **부분 실제 누락**. "leafy Lebanon"→"Lebanon", "brash ocean waves" 탈락 (KO는 유지). EN 복원: "sweet Gilead, back to leafy Lebanon" / "They'll sail through troubled seas, brush aside the brash ocean waves." ("brimming with joy"→"filled with good vibes" 의미 보존.)

### 전수 대조 추가 발견 (checker 외)
- ch2 idx3 [6-7]: KO "북쪽 땅에서"는 MSG/EN에 없는 추가 ("far exile"/"far-off land"). KO → "먼 유배지에서 돌아와라."
- ch2 idx4 [8-9]: MSG "bloodies my nose, blackens my eye"가 EN "poking me in the eye"로 축소. EN/KO 복원: "it bloodies my nose, blackens my eye." / "내 코피를 터뜨리고 내 눈에 멍을 들게 하는 것이다."
- ch3 idx4 [8-9]: MSG "your friends are in on this, too"가 EN "you guys are a sign"으로 대체. EN/KO 복원: "you guys are in on this, too. You're a sign of what's coming." / "너희도 이 일에 함께하고 있어."
- ch4 idx6 [6-7]: MSG "set the Cornerstone in place"가 EN "lay the final stone"으로 오역 (v8-10 "last stone"과 혼동). EN → "set the Cornerstone in place". KO 환호 "진짜 큰! 진짜 큰!"은 EN/KO 불일치 → "가자! 가자! 해내자!"
- ch4 idx12 [14]: MSG "stand beside the Master of the whole earth and supply golden lamp oil worldwide"가 EN에서 "anointed to serve ... supplying his light"로 바뀜. EN 복원 (KO는 이미 유지): "stand beside the Lord of all the earth, supplying golden lamp oil to the whole world."
- ch5 idx3 [3-4]: MSG "tear it down, timbers and stones"가 EN "wreck the place, from the roof to the foundation"으로 바뀜 (KO는 "목재랑 돌까지" 유지). EN 복원: "tear the place down—timbers and stones."
- ch5 idx11 [11]: MSG "They will build a garage to house it"가 EN "build a special place"로 바뀜. EN 복원: "build a garage to house it". KO "보관할 집" → "보관할 창고".
- ch8 idx12 [9-10]: EN 인용문 닫는 따옴표 누락 (깨진 텍스트). 닫는 `"` 추가.
- ch11 idx0 [1-4]: MSG "Open your borders to the immigrants, proud Lebanon!"에서 "to the immigrants"가 EN/KO 모두 탈락. EN/KO 복원.
- ch11 idx3/idx5/idx8: 지팡이 이름 오역 — MSG "Lovely"/"Harmony"가 EN/KO에서 "Grace"/"Unity"("은총"/"연합"). EN/KO 복원: 'Lovely'/'Harmony' ("사랑스러움"/"화합").
- ch11 idx4 [9]: MSG "Whoever survives can eat what's left"가 EN "eat each other"로 의미 변경 (KO도 동일). EN/KO 복원: "Whoever survives can just eat what's left." / "살아남은 자는 남은 것을 먹어라."
- ch13 idx3 [7-9]: MSG "The back of my hand against even the lambs!"가 EN "turn my back on the little lambs"로 관용구 오역 (때린다→외면한다). EN/KO 복원: "turn my hand against the little lambs" / "어린 양들에게조차 내 손을 돌릴 것이다."
- ch6 idx5/idx7 왕관: MSG "fashion crowns ... Place one on the head ... The other crown" — EN "make some crowns. Put one on ... The other crown"이 MSG와 일치. 수정 불필요 (1차 노트 정정).

### 슬랭 순화
- EN: ch2 idx0 "no cap"/"dude" → "saw a guy"; ch3 idx1 "fresh new fit" → "a clean new outfit"; ch3 idx5 "vibing" → "hanging out"; ch6 idx0 "totally wild" → "crazy"; ch6 idx2 "angel dude" → "angel"; ch7 idx2 "Lowkey, no" → "Honestly, no"; ch13 idx1 "'Dude, you're done" → "'You're done"; ch14 idx6 "gnarly plague" → "horrible plague"
- KO: ch1 idx15 "뭐임" → "도대체 뭐예요"; ch5 idx0 "대박" → "놀라운"; ch11 idx1 "더 대박인 건" → "더 충격인 건"; ch11 idx2 "서바이벌 게임" → "적자생존"; ch14 idx3 "대박" → "엄청날"

### 복원 결과
- MSG 복원 13건 (ch1 1건, ch2 2건, ch3 1건, ch4 3건, ch5 3건, ch8 1건, ch10 1건, ch11 4건, ch13 1건 — EN/KO 쌍 기준), 슬랭 순화 EN 8건/KO 5건. 나머지 전 문단 MSG 대비 내용 온전, EN/KO 일치.

### 게이트
- STRUCT OK: 14장 141문단, verseRanges/msg_ranges/splits parity
- completeness_check 잔여 1건 (ch10 assyrian) 오탐
- build: rows=141, msg_units=113, teen_without_msg=0, msg_orphans=0, VERIFY_DROPPED=0 (PAIRING_MISMATCH 1건: ch8 idx15 badge 13 vs MSG v12-13 superset — v12 내용은 idx13/idx14에서 처리, 내용 온전)
- DOCX spot-check: 12개 복원 행 페어링 확인 (ch1/ch2/ch4/ch5/ch10/ch11/ch13)
- Google Docs: 신규 문서 생성 (Zechariah 미등록이었음) — ID 1yqJotsvrkTGVAUsoj-pBFAuzKeSEBzxKPA45_kffwoI, API 테이블 14/14, export-back VERIFIED OK
