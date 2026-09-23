# Obadiah 감사 리포트 (2026-09-23, 작업자 A)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG(raw 텍스트) vs EN vs KO 문단별 전수 대조 (1장, 7문단). 1차 감사 변경 이력(`changes` 필드) 확인 후 잔여 이슈 직접 판정.
결과: 텍스트 수정 5건(EN). merge/split 신규 후보 0건. 결론: **재감사 + 5건 수정** (이전 감사가 KO에만 있던 MSG 요소를 EN에서 빠뜨림).

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1 | "Obadiah's Message to Edom from God, the Master" (byline) | EN 누락 | EN 도입부 "So, here's the deal with Edom, straight from God" → "So, here's the deal with Edom — this is Obadiah's message, straight from God." |
| 5-14 | "Your great heroes will desert you, Teman" | EN 누락 (KO는 데만아 보유) | "Your heroes will abandon you" → "Your heroes will abandon you, Teman" |
| 15-18 | "They'll drink and drink and drink—they'll drink themselves to death" | EN 누락 (KO는 보유) | "They'll be completely destroyed" → "They'll drink and drink and drink—they'll drink themselves to death" |
| 15-18 | "the family of Joseph become fierce flame ... nothing left of Esau but a pile of ashes" | EN 누락 (KO는 요셉·재더미 보유) | "They'll be like a fire, and Esau's family will be like straw, completely burned up" → "Jacob's family will catch fire, Joseph's family will become a fierce flame, and Esau's family will be like straw, completely burned up—nothing left but a pile of ashes" |
| 19-21 | "rule justly and fairly" | EN 누락 (KO는 공정하고 공평하게 보유) | "will rule over the mountains of Esau" → "will go into the mountains of Esau and rule justly and fairly" |

### 1차 감사에서 이미 수정된 사항 (이번 감사에서 직접 확인, 유지)
- MSG 소제목 헤더 "Your World Will Collapse" 추가 (EN/KO, 배지 1 공유)
- MSG v1을 2개 문단으로 split 선언 (EN/KO parity)
- EN 2-4 "even if you built your nest in the stars" 복원
- EN 19-21 "Jerusalem exiles from the far northwest in Sepharad" 복원

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- EN 5-14의 "You shouldn't have" 7연속 압축 ("celebrated their suffering" 등 4개 절로): MSG 7개 항목 각각에 대응 요소가 있어 틴 paraphrase 범위로 판정. KO는 7개 전부 보존.
- MSG "God's sure Word" → EN "that's a promise from God" / KO "하나님이 확실하게 하신 말씀": 의역, 내용 보존.
- EN 5-14 "empty his purse and pockets" → "completely wrecked": 동일 의미 압축.
- 소제목 1개가 MSG와 1:1 ("Your World Will Collapse" / "너희 세상은 무너질 거야"). 창작 헤더 없음.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (7문단). null 배지 0.
- verseRanges 7개 전부 MSG 커버.
- splits 1건 선언 유지 (v1 → 2문단).

## 3. merge/split 후보
- 신규 후보: **0건**.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (1장 7문단 전수, 직접 대조) |
| ② 수정 반영 | PASS (EN 5건, merge/split 미적용) |
| ③ validate_translation.py | PASS (exit 0). 비고: '전염병' substring 오탐으로 FAIL 나던 validator 버그를 근본 수정 (`염병` 매칭에 `(?<!전)` lookbehind 추가) — 7개 장 전부가 '전염병'(plague 정상 번역)이었음 |
| ④ 기계적 완전성 검사 | PASS (6문단, 12 name tokens — 잔여 FAIL 2건 전부 오탐 문서화: 복수형/형용사형 stemming 이슈 'israelite'/'canaanite', 인용 키워드 의역 'word'/'pillaged'/'gloated'/'facedown'/'traitorously') |
| ⑤ build_gdocs.py 재빌드 | PASS (VERIFY_DROPPED=0) |
| ⑥ verify_pairing_content.py | PASS + 실제 셀 내용 기준 짝지음 확인 (배지별 MSG↔EN↔KO 행 일치, 소제목 행은 제목만 표시) |
| ⑦ Google Docs 업로드 + API 검증 | PASS (테이블 1/1, title 일치, export-back VERIFIED OK). Doc: 오바댜 (Obadiah) — Final: MSG + Teen EN + KO, id 1fp-bW_iBIzpfjVTrh9mL0XxpwXb2Ry-k5v3leLleUCw |

## 5. 검증 범위 및 미확인 경계
- 검증한 것: MSG vs EN vs KO 전수 대조 1장, validator, completeness_check(오탐 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉.
