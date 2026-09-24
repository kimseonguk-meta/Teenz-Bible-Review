# Malachi 감사 리포트 (2026-09-24) — MSG 전수 감사

기준: Eugene Peterson The Message(MSG) 영어 원문 = 유일한 최종 기준. KJV 미사용.
검수 방법: `msg_Malachi.txt` 파싱(32 units: ch1 11 / ch2 8 / ch3 10 / ch4 3) ↔ EN ↔ KO 문장·이름·숫자·인용구·반복요소 전수 대조.
시드: 앱 소스에서 재시드한 fixes JSON (구 감사본은 git history 참조용 — 기준은 현재 시드 + MSG 원문).
결과: **전수 감사 + 수정 EN 23건 / KO 12건. splits 7건 스탠딩 승인 선언. merges 0건.**
⚠ 27권 감사 컨벤션 준수: fixes JSON에 소제목(§ 헤더) 행 추가 없음. 소제목은 빌더가 MSG 원문에서 독에 삽입.

## 0. MSG 원문 품질 검증

- `parse_msg_txt`: 4장 전부, 32 units. 절 커버리지 ch1 1–14 / ch2 1–17 / ch3 1–18 / ch4 1–6 완전. boilerplate 없음. 장 중간 구간 누락 없음.
- 표본 대조 (BibleGateway MSG 패턴): 1:2-3 "I reduced pretentious Esau to a molehill", 2:16 "I hate divorce", 3:5 "inhospitable to the homeless", 4:1-3 "the sun of righteousness will dawn... healing radiating from its wings" — 전부 일치.

## 1. 장:절별 이슈 및 수정

### EN (본문 23건)

| 장:절 | MSG | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1:2-3 | "I reduced pretentious Esau to a molehill" | 누락 | "I totally wrecked Esau's territory" → "I flattened show-off Esau into a molehill" |
| 1:4 | "When Edom (Esau) said" | 표기 | "the Edomites (Esau's descendants)" → "Edom (Esau)" (MSG/KO 표기 일치) |
| 1:7-8 | "your banker or your senator" | 누락 | "your governor" → "your banker or your senator" (2인 복원) |
| 1:9 | "Get on your knees and pray" | 누락 | "go ahead and beg" → "Get on your knees and beg" (KO는 보유) |
| 1:10 | "silly, empty-headed worship" | 누락 | "empty worship" → "silly, empty-headed worship" (KO는 보유) |
| 1:11 | (없음) | MSG 무첨가 | "From east to west" 추가 삭제 (all over the world와 중복) |
| 2:4-6 | "my covenant with the priests of Levi" | 누락 | "the deal I made with your ancestor Levi" → "my covenant with the priests of Levi" (KO는 보유) |
| 2:4-6 | "He walked with me in peace and uprightness" | 누락 | "He was my boy, always doing the right thing" → "He walked with me in peace, always doing the right thing" |
| 2:7-9 | "truly and impartially" | 누락 | "twist my words instead of teaching them straight up" → "don't teach my revelation straight up and fair" (KO는 "공정하고 진실되게" 보유) |
| 2:11-12 | "falling in love and running off with foreign women" | 누락 | "falling for and marrying" → "falling for, running off with, and marrying" |
| 2:13-15 | "God was there as a witness" | 누락 | "God was there when you made" → "God was right there as your witness when you made" (KO는 "증인" 보유) |
| 2:13-15 | "a second offense" | 누락 | "another thing you're doing wrong" → "the second thing you're doing wrong" (KO는 "두 번째 잘못" 보유; completeness FAIL 실건) |
| 2:17 | "God loves sinners and sin alike. God loves all." | 누락 | "God is cool with sinners and sin." → "+he loves everyone." (KO는 "하나님은 모두를 사랑해" 보유) |
| 3:2-4 | "a cleanser of dirty clothes" | 누락 | "purifying and cleaning everything up" → "purifying silver and scrubbing dirty clothes clean" (KO는 "더러운 옷" 보유) |
| 3:5 | "adulterers" | 모호 | "cheaters" → "people who cheat on their spouses" (KO "간음하는 자"와 일치) |
| 3:5 | "inhospitable to the homeless" | 오역 | "rude to immigrants" → "turn away the homeless" (MSG 기준) |
| 3:8-11 | "defend you against marauders, protect your wheat fields and vegetable gardens against plunderers" | 누락 | "protect your crops from pests, and your fields and gardens won't be raided" → "defend you against raiders and protect your wheat fields and vegetable gardens from plunderers" |
| 3:6-7/8/13 | 인용구 | 따옴표 | P6/P7/P8/P11/P12 닫는 따옴표(”) 5건 추가 |
| 3:14-15 | "When you said" | 표기 | "'It was when you said" → "'When you said" (MSG 표기 일치) |
| 4:1-3 | "healing radiating from its wings" | 누락 | "bringing healing vibes" → "with healing radiating from its wings" (KO는 "날개" 보유) |
| 4:1-3 | (없음) | MSG 무첨가 | "That's a promise from the God of Angel Armies" → "The God of Angel Armies says so." (MSG "says so") |
| 4:4 | "my servant Moses" / "rules and procedures" / "Remember and keep" | 누락 | "my boy Moses" → "my servant Moses"; "procedures" 복원; "Don't forget" → "Remember and keep" (KO는 "내 종 모세"/"규칙이랑 절차"/"기억하고 지켜라" 보유) |

### KO (본문 12건)

| 장:절 | 문제 유형 | 수정 내용 |
|---|---|---|
| 1:1 | EN 불일치 | "말라기 통해서" → "그분의 선지자 말라기를 통해서" (EN "his prophet"와 일치) |
| 1:7-8 | EN 불일치 | "총독한테" → "은행 사장이나 의원한테" (MSG "banker or senator", EN과 일치) |
| 1:12-13 | 오타 | "코를  하늘로" 이중 공백 수정 |
| 2:1-3 | MSG 무첨가+저속 | "너네 축제 때 나온 똥 말이야" 문장 삭제 (MSG는 "rotting garbage"만) |
| 2:11-12 | 누락 | "사랑에 빠지고 결혼해서" → "사랑에 빠지고 함께 도망쳐서 결혼하는 바람에" (EN과 일치) |
| 3:5 | 오역 (MSG 기준) | "나그네를 박대하는 자" → "집 없는 사람을 박대하는 자" (MSG "homeless") |
| 3:6-7/8/13 | 인용구 | P6/P7/P8/P12 닫는 따옴표(”) 4건 추가 |
| 3:8-11 | 오역 | "너희 밭의 포도나무 열매가 떨어지지 않게" → "너희 밀밭과 채소밭을 노략질로부터 보호해줄게" (MSG "wheat fields and vegetable gardens against plunderers"); "marauders" 복원 |
| 4:1-3 | 오역 | "완전 흑역사 되는 날" → "그들에게는 암울한 날" (MSG "a black day") |
| 4:1-3 | MSG 무첨가 | "이건 확실함" 삭제 (EN도 "That's a promise from" 삭제) |

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)

- "no cap" (2:5, "He taught the truth, no cap") → MSG "taught the truth and did not lie". 틴즈 슬랭 범위 내 의역, 유지.
- "my boy" (2:4-6→"He was my boy") → "He walked with me in peace"로 수정하면서 해소.
- 칭호 표기 장별 상이 (1장 "LORD of Heaven's Armies" / 2·4장 "God of Angel Armies" / 3장 "God-of-the-Angel-Armies"): 생산 시드 그대로, 내용 손실 없음 — 유지. KO는 전 장 "만군의 주 하나님" 통일.
- 1:4 "good as new" → "better than ever": 의역 범위, 유지.
- 2:17 "God loves sinners and sin alike" → "God is cool with sinners and sin": 틴즈 의역, 유지.

## 2. 구조 검사

- EN/KO 문단 수·순서·배지 1:1: ch1 16 / ch2 10 / ch3 15 / ch4 3 (본문만, § 헤더 0). null 배지 0.
- `verseRanges`·`msg_ranges` 시드 그대로 사용 (이미 정확).
- splits 선언 7건 (스탠딩 승인 규칙 (a)(b)(c) 전부 만족 — 내용 손실·추가·오역 없음, EN/KO 일치, 순수 가독성 구조 차이). merges: 0건.

## 3. merge/split 후보 (스탠딩 승인으로 선언)

| 장 | msg_range | Teen 문단 | 내용 |
|---|---|---|---|
| 1 | 2-3 | P2–P4 | God said / people reply / God's answer — Q&A 가독성 분리 |
| 1 | 6 | P7–P10 | v6 Q&A 체인 4문단 분리 |
| 2 | 17 | P8–P10 | statement / question / answer 분리 |
| 3 | 2-4 | P2–P3 | "who can stand?" 질문 / 대답 분리 |
| 3 | 6-7 | P5–P6 | 복귀 명령 / "But how do we return?" 분리 |
| 3 | 8-11 | P7–P9 | 도둑질 지적 / "How have we robbed you?" / 십일조 대답 분리 |
| 3 | 13 | P11–P12 | "hard, rude words" 지적 / "When did we ever do that?" 분리 |

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① MSG 원문 품질 검증 | PASS (32 units, 4장 전 절 커버, boilerplate 0) |
| ② 의미 전수 감사 | PASS (MSG 문장·이름·숫자·인용구·반복요소 전수 대조, EN 23 + KO 12 수정) |
| ③ validate_translation.py | PASS: 4개 장 모두 통과 (exit 0) |
| ④ completeness_check.py | 1차 FAIL 8건 중 1건("second") 실제 누락 → 복원. 재검사 후 잔여 7건은 오탐으로 `completeness_fp_Malachi.md`에 문서화. 실제 갭 0 |
| ⑤ build_gdocs.py | PASS — rows=44, msg_units=32, teen_without_msg=0, msg_orphans=0, VERIFY_DROPPED=0 |
| ⑥ verify_pairing_content.py | PASS — 44 data rows in 4 tables, PAIRING CONTENT OK |
| ⑦ Google Docs 업로드 + API 검증 | PASS — title "말라기 (Malachi): MSG + Teen EN + KO" (Final 없음), 테이블 4/4, export-back VERIFIED OK. Doc id 15jhaXUC8Xzh0KIA9ZOT4AWhWRHsuF8xfe4wsj0Gy9Q4. 결과 `upload_results_workerA.json` 기록 확인 |

## 5. 검증 범위 및 미확인 경계

- 검증한 것: MSG 원문 품질(파싱+표본 대조), MSG↔EN↔KO 전수 대조 4장, validator, completeness_check(오탐 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함(브라우저 불가). production 앱 미접촉 (구약 수정본 앱 미반영 원칙 준수).

## 6. 승인 필요 항목

- 없음 (스탠딩 승인 규칙으로 splits 7건만 선언하고 계속 진행).

## 7. 이전 감사본과의 관계

- HEAD 버전은 구(舊) 감사본이었으나 본 감사는 앱 소스 재시드 기준으로 전수 재검증. 구 감사본은 git history에 참조용으로 보존. 구 감사본의 § 배치·헤더는 참조하지 않음 (27권 감사 컨벤션: 헤더 제외 집계).

## 2nd re-audit (Sep 24)

- 기준: 동일 작업 지시 6권 배치(Esther·Hosea·Joel·Amos·Zechariah·Malachi)의 두 번째 정밀 감사. 선행 커밋 4b44665(당일 08:29 UTC, EN 23건·KO 12건)의 수정 위에 MSG 4장 전수 재대조.
- 선행 감사에서 누락된 실제 결함 2건 발견·수정:
  1. KO ch1 idx14 [12-13]이 EN/KO 불일치 — v7-8 내용(제단·눈 멀고 병든 동물·은행 사장/의원)의 거의 그대로 복제였고, 실제 v12-13("All except you... you profane me") 번역이 아니었음. EN/MSG 기준으로 KO 전면 재작성.
  2. EN ch1 idx12 [10]에서 MSG 반복("I am not pleased. The God-of-the-Angel-Armies is not pleased.")이 1회로 축소되어 있었음. EN에 반복 복원 ("I'm not happy. The LORD of Heaven's Armies is not happy."). KO는 선행 감사에서 이미 2회 반영되어 있어 EN만 맞춤.
- 과도한 슬랭 정리 (뜻 유지, 틴즈 voice 유지):
  - EN: "here's the 411"→"here's the deal" (1:1), "Dude, just look at history"→"Just look at history" (1:2-3), "btw" 삭제 (2:1-3), "no cap"→"no lies, ever" (2:4-6), "Yo, check it!"→"Look!" + "bam, out of nowhere"→"suddenly, out of nowhere" (3:1), "Yo, for real"→"Count on it:" (4:1-3).
  - KO: "이딴 바보 같고/이딴 소위"→"이런 바보 같고/이런 소위" (1:10), "정체를 싹 다 까발리는"→"정체가 뭔지 낱낱이 드러내는" (2:7-9), "징징대면서"→"투덜대면서" (2:13-15), "잘 살피셈"→"잘 살펴" (2:16), "야, 봐봐!"→"봐봐!" (3:1), "앞날도 기대하셈"→"앞날도 준비해" (4:5-6).
- 오탐 아님 확인: "에돔(에서)"는 Edom(Esau)의 정상 표기 — 수정 불필요.
- completeness_check.py 잔여 7건 전부 오탐으로 분류 (선행 감사 문서 `completeness_fp_Malachi.md`와 일치): "god" 4건은 God-of-the-Angel-Armies→LORD of Heaven's Armies 일관 렌더링, "word" 1건은 God's Word→message 의미 유지, "desecrating"은 절 헤더 출신, 숫자 "1"은 "the one" 대명사, 인용구 "colts/frolicking/tromp"는 이미지·의미 유지 paraphrase (KO는 "망아지"/"밟고 다닐"으로 직역 유지).
- 게이트: STRUCT OK (4장, EN/KO 44문단, verseRanges·msg_ranges parity), build rows=44 msg_units=32 teen_without_msg=0 msg_orphans=0 VERIFY_DROPPED=0, DOCX 복원 행 python-docx 육안 확인, Google Docs 기존 문서(15jhaXUC8Xzh0KIA9ZOT4AWhWRHsuF8xfe4wsj0Gy9Q4) 재업로드 후 테이블 4/4 + export-back VERIFIED OK.
- splits 7건은 선행 감사 선언 유지, 추가 구조 변경 없음.
