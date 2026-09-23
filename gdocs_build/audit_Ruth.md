# Ruth 감사 리포트 (2026-09-23, 작업자 A)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1.
검수 방법: MSG(raw 텍스트) vs EN vs KO 문단별 전수 대조 (4장, 76문단). 1차 감사 변경 이력 확인 후 잔여 이슈 직접 판정.
결과: 텍스트 수정 4건(EN 2, KO 2). merge/split 신규 후보 0건. 결론: **재감사 + 4건 수정**.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1:1-2 | "all Ephrathites from Bethlehem in Judah" | EN·KO 누락 | EN: "This guy from Bethlehem named Elimelech" → "This guy named Elimelech—an Ephrathite from Bethlehem in Judah". KO: "다들 베들레헴 출신 유다 사람들" → "이들은 유다 베들레헴 출신 에브라다 사람들" (4:11-12 에브라다 표기와 통일) |
| 2:12 | "God reward you well ... and with a generous bonus besides ... seeking protection under his wings" | EN 누락 (KO는 보너스·날개 보유) | EN: "May God bless you big time for what you've done. You came to God for protection, and He's got you covered." → "May God bless you big time for what you've done—and with a generous bonus besides. You came to God for protection under his wings, and he's got you covered." |
| 2:21 | "Well, listen to this" (룻의 말) | KO 과도한 슬랭 | KO: "헐, 대박. 그 아저씨가..." → "야, 이거 들어봐. 그 아저씨가..." |

### 1차 감사에서 이미 수정된 사항 (이번 감사에서 직접 확인, 유지)
- MSG 소제목 헤더들 EN/KO 추가 (확인됨)
- 4:18-22 베레스 족보 9대 전수 보존 (Perez→David, EN/KO 모두)

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- "Moabite/Moabitess" → "new girl from Moab"/"the foreigner from Moab": 지시 대상 명확한 의역.
- "connected with Elimelech's family" → "from her husband's side of the family" (2:1): 나오미의 남편=엘리멜렉이 1장에서 확정되어 지시 대상 명확.
- "glean among the sheaves" → "pick up/gather the leftovers" (2:2, 6-7, 15-16 일관): gleaning의 의미를 풀어쓴 틴 의역으로 판정.
- "the two who built the house of Israel" → "who basically built the nation of Israel" (4:11-12): 두 이름(Rachel·Leah) 명시로 "two" 정보 자명.
- "Dip it in the wine" (2:14): MSG 원문이 실제로 "wine"임 — teen 정확.
- "six quarts" (3:17): MSG 원문 표현 그대로 — teen 정확.
- "Kilion" 표기: MSG 원문 표기가 "Kilion" — teen 정확 (Chilion 아님).
- "town gate" → "main town square" (4:1): MSG 원문이 "public square" — teen 정확.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (4장 76문단). null 배지 0.

## 3. merge/split 후보
- 신규 후보: **0건**.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (4장 76문단 전수, 직접 대조) |
| ② 수정 반영 | PASS (EN 2건, KO 2건, merge/split 미적용) |
| ③ validate_translation.py | PASS (exit 0) |
| ④ 기계적 완전성 검사 | PASS (74문단, 67 name tokens — 잔여 FAIL 14건 전부 오탐 문서화: 'elimelech' 2건은 지시 대상 명확한 의역, 'moabite' 3건은 "from Moab" 의역, 'ephrathites'는 실제 복원 후 해소, 숫자 1·2는 MSG "the first"/"the one"/"two daughters-in-law"(인접 문단 보유) 등, 'glean/sheaves/harvesters'는 "leftovers" 일관 의역) |
| ⑤ build_gdocs.py 재빌드 | PASS (VERIFY_DROPPED=0) |
| ⑥ verify_pairing_content.py | PASS + 실제 셀 내용 기준 짝지음 확인 (ch2 표본: 배지별 MSG↔EN 행 일치) |
| ⑦ Google Docs 업로드 + API 검증 | PASS (테이블 4/4, title 일치, export-back VERIFIED OK). Doc: 룻기 (Ruth) — Final: MSG + Teen EN + KO, id 14tmrTTb1rGX0gatBv5khy4tBvEEopS9uD5m3kcEd_LY |

## 5. 검증 범위 및 미확인 경계
- 검증한 것: MSG vs EN vs KO 전수 대조 4장, validator, completeness_check(오탐 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉.

## 6. 재확인 (2026-09-24, 재확인 작업자 — 독립 재검증)
- 7개 게이트 재실행: ③ validate PASS, ⑤ 재빌드 VERIFY_DROPPED=0 (rows=74), ⑥ verify_pairing_content PASS (74행).
- ④ 기계적 완전성 검사 14건 FAIL → 전수 수동 대조 결과 전부 오탐, 텍스트 변경 0건: 'ephrathites'→"an Ephrathite"(단수), 'elimelech' 2건→"her husband's side"/"the rich relative"(1장에서 지시 대상 확립), 'moabite' 3건→"from Moab", 'moabitess'→"Ruth was like"(정체 명확), 숫자 4건→"the first"→나열 순서/"two daughters-in-law"→"both"/"the one"→"the girl"/"the two women"→Rachel·Leah 명시, 인용구 3건→"pick up/gather the leftovers"(gleaning 의역 일관). 1차 감사(작업자 A)의 오탐 문서화와 독립적으로 동일한 결론에 도달.
- 슬랭 6 Rule 재검색: EN "woke up"(3:8, 정상 동사 — 오탐), KO "좋아요"(1:17 "벌하셔도 좋아요", 정상 형용사 — 오탐) 외 위반 없음. R6 chill 1건 유지(변경 금지).
- 파서 경계 버그(Joshua 14:15/15:1) 해당 없음 — Ruth 장 경계 전체 정상 파싱 확인.
- 텍스트 변경 없으므로 Google Docs 재업로드 불필요 (기존 Doc id 14tmrTTb1rGX0gatBv5khy4tBvEEopS9uD5m3kcEd_LY 유지).
