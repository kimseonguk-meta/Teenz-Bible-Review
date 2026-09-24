# Zephaniah 감사 리포트 (2026-09-24, 작업자 A) — MSG 전수 감사

기준: Eugene Peterson The Message(MSG) 영어 원문 = 유일한 최종 기준. KJV 미사용.
검수 방법: `msg_Zephaniah.txt` 파싱(20 units: ch1 6 / ch2 6 / ch3 8) ↔ EN ↔ KO 문장·이름·숫자·인용구·반복요소 전수 대조.
시드: 앱 소스에서 재시드한 fixes JSON (2026-09-23 구 감사본은 git history 참조용 — § 헤더 배치만 참조).
결과: **전수 감사 + 수정 EN 18건 / KO 13건. merge/split 신규 후보 0건.**

## 0. MSG 원문 품질 검증

- `parse_msg_txt`: 3장 전부, 20 units. 절 커버리지 ch1 1–18 / ch2 1–15 / ch3 1–20 완전. boilerplate 없음.
- 공개 MSG(Zephaniah)와 대조: 1:14 "It's countdown time: . . . seven, six, five, four . . .",
  2:15 "I'm the Number-One City! I'm King of the Mountain!", 3:18-20 "God's Promise." 등 표본 일치.

## 1. 장:절별 이슈 및 수정

### EN (본문 18건 + § 헤더 7건 추가)

| 장:절 | MSG | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1:4-6 | "sex-and-religion Baal shrines" | 축소 | "weird Baal shrines" → "Baal shrines that mixed sex with religion" |
| 1:4-6 | "star gods and goddesses" | 축소 | "worship stars" → "worship the star gods and goddesses" |
| 1:4-6 | "other king-gods" | 축소 | "other gods" → "other king-gods" |
| 1:4-6 | "dumped God altogether" | 슬랭+누락 | "totally ghosted God" → "totally dumped God"; "or a prayer" 복원 |
| 1:7-13 | "pagan prayers and practices" | 누락 | "weird prayers" → "their weird prayers and practices" |
| 1:7-13 | "Reverent silence" | 토큰 | "Show some respect" → "quiet now! Reverent silence before God" (completeness 토큰 복원) |
| 1:14-18 | "a day of darkness at noon" | 누락 | "darkness and storms" → "darkness at noon, a day of black storm clouds" |
| 2:8-12 | "a field of rocks" | 오역 | "a field of weeds" → "a field of rocks" |
| 2:8-12 | "shrivel up and blow away" | 축소 | "shrivel up and disappear" → "shrivel up and blow away" |
| 2:8-12 | "God-of-the-Angel-Armies" | 표기 | "Lord of Angel Armies" → "God-of-the-Angel-Armies" (MSG 표기) |
| 2:13-15 | "raccoons and coyotes" | 오역 | "Desert owls and jackals" → "raccoons and coyotes" (MSG 동물명) |
| 2:13-15 | "I'm King of the Mountain!" | 누락 | 자랑 인용구에 "'I'm the Number-One City! I'm King of the Mountain!'" 복원 |
| 3:1-5 | "out every morning prowling" | 누락 | judges 문단에 "out every morning" 복원 |
| 3:1-5 | "At evening he's still at it, strong as ever" | 축소 | "He never stops" → "At evening he's still at it, strong as ever" |
| 3:1-5 | "without conscience and without shame" | 누락 | "with zero shame" → "without conscience and without shame" |
| 3:7 | "find a way of escape from the trouble she's in" | 누락 | MSG 이중 절 중 첫째 복원 |
| 3:9-13 | "What's left of Israel that's really Israel" | 누락 | "what's left of Israel, the real Israel" 복원 |
| 3:9-13 | "Content with who they are and where they are" | 축소 | "They'll be content" → "Content with who they are and where they are" |
| 3:14-15 | "Daughter Zion / Daughter Jerusalem" | 반복요소 누락 | "So sing, Zion!" → "So sing, Daughter Zion!"; "Daughter Jerusalem, be happy!" |
| 3:18-20 | "they will be venerated" | 오역 | "they will be famous" → "they will be venerated" |
| § | MSG ### 소제목 7건 | 누락 | EN에 § 헤더 7건 추가 (No Longer Giving God a Thought or a Prayer / A Day of Darkness at Noon / Seek God / All Earth-Made Gods Will Blow Away / Sewer City / God Is in Charge at the Center / God Is Present Among You) |

### KO (본문 13건 + § 헤더 7건 추가)

| 장:절 | 문제 유형 | 수정 내용 |
|---|---|---|
| 1:1 | 누락 | "아몬의 아들 요시야" 복원 (son of Amon) |
| 1:2 | MSG 무첨가 | "완전 믿기 힘든 일임" 첨가 삭제 |
| 1:3 | 누락 | "남자고 여자고" (Men and women) 복원 |
| 1:4-6 | 누락 | "성과 종교를 뒤섞은 바알 신전" / "별의 신들" / "다른 왕신들" 복원 (EN과 동일) |
| 1:7-13 | 누락 | "초대받은 손님들도 다 거룩하게 준비됐음" (made holy); "여제사장" "의식"(practices) 복원 |
| 2:1-2 | 누락 | "바람에 날아가는 나뭇잎처럼 날아가 버리기 전에" (MSG 첫째 before 절) 복원 |
| 2:8-12 | 누락 | "달 표면처럼" (moonscape); "바람에 날아갈 거고" (blow away) 복원 |
| 2:13-15 | 과도한 슬랭 | "꿀잼 도시" → "신나는 도시" (MSG "Fun City", 2026-09-23 구 감사 전례 유지) |
| 3:1 | MSG 무첨가 | "예루살렘은 이제 망했대" 첨가 삭제 → "반역의 도시, 압제자들의 소굴 — 이제 끝장이야" |
| 3:1 | 오역 | "사람들 영혼을 다치게 했대" → "사람들의 영혼을 베고 죽였대" (MSG "maim and kill souls") |
| 3:7 | **중복 문단** | 3:7 문단("나는 생각했지...")이 2개 중복 삽입돼 있던 시드 버그 — 중복본 삭제, EN 8문단과 1:1 일치 (validator 기준 ch3 EN 8 vs KO 9 불일치의 원인) |
| § | MSG ### 소제목 7건 | KO에 § 헤더 7건 추가 (EN과 동일 위치·순서) |

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)

- 1:7 "hellholes" → EN "a mess" / KO "지옥 구덩이": 욕 순화 범위 내 의역.
- 1:12 "The god Money is dead" → "The god of money is dead": 의미 보존.
- 3:7 "she/her" (도시 지칭) 유지 — EN "Surely she'll honor me now".
- 3:8 "I'll be there with the evidence": teen 의역으로 의미 보존.
- KO 1:1 족보 순서 역전(히스기야→구시 순): 관계 동일, 의역 범위.

## 2. 구조 검사

- EN/KO 문단 수·순서·배지 1:1: ch1 8 / ch2 8 / ch3 11 (본문+§). null 배지 0.
- `verseRanges`·`msg_ranges` 신규 부여 (시드에는 없던 감사 메타데이터).
- splits 선언: 0건. merges: 0건. (전부 MSG 단락 1:1 대응 — 스탠딩 승인 규칙 (a)(b)(c) 해당 구조 변경 없음)

## 3. merge/split 후보

- 신규 후보: **0건**. § 헤더 추가는 구조 선언이 아니라 MSG ### 소제목의 Teen 반영 (타 감사본 Titus/Zechariah/Matthew 전례와 동일).

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① MSG 원문 품질 검증 | PASS (20 units, 3장 전 절 커버, boilerplate 0) |
| ② 의미 전수 감사 | PASS (MSG 문장·이름·숫자·인용구·반복요소 전수 대조, EN 18 + KO 13 수정) |
| ③ validate_translation.py | PASS: 3개 장 모두 통과 (exit 0) |
| ④ completeness_check.py | 1차 FAIL 1건(reverent) → 복원 후 재검사, 잔여 1건(moneymaking)은 하이픈 오탐으로 `completeness_fp_Zephaniah.md`에 문서화. 실제 갭 0 |
| ⑤ build_gdocs.py | PASS — rows=27, msg_units=20, teen_without_msg=0, msg_orphans=0, VERIFY_DROPPED=0 |
| ⑥ verify_pairing_content.py | PASS — 20 data rows in 3 tables, PAIRING CONTENT OK |
| ⑦ Google Docs 업로드 + API 검증 | PASS — title "스바냐 (Zephaniah): MSG + Teen EN + KO" (Final 없음), 테이블 3/3, export-back VERIFIED OK. Doc id 12B-iqjOj6wAUswd7jEmluoMsY9JdO-EoPb4Sw8jVHYc. 결과 `upload_results_workerA.json` 기록 확인 |

## 5. 검증 범위 및 미확인 경계

- 검증한 것: MSG 원문 품질(파싱+표본 대조), MSG↔EN↔KO 전수 대조 3장, validator, completeness_check(오탐 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함(브라우저 불가). 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉 (구약 수정본 앱 미반영 원칙 준수).

## 6. 이전 감사(2026-09-23)와의 관계

- 2026-09-23 구 감사는 의미 감사 3건(1:6 ghosted→dumped, 1:14 bloodcurdling, 2:15 꿀잼→신나는 도시)이었으나, 이후 앱 소스 재시드로 시드가 교체되면서 본 감사에서 전수 재검증함. 구 감사본은 git history(6883679 이전)에 참조용으로 보존. § 헤더 문구·배치는 구 감사본을 참조.
- 2026-09-23 업로드 Doc(제목에 "Final", id 1e_p0097DuMSyoH_IC55C_zrdCYVcaRCBT26i-0F5y4E)은 구 감사본 기준 문서로 남아 있음. 본 감사 문서는 별도 신규 Doc(위 ⑦).
