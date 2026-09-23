# Jonah 감사 리포트 (2026-09-23, 작업자 A)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1.
검수 방법: MSG(raw 텍스트) vs EN vs KO 전수 대조 (4장 29문단). 1차 감사 변경 이력 확인 후 잔여 이슈 직접 판정.
결과: 텍스트 수정 1건(EN 1). merge/split 신규 후보 0건. 결론: **재감사 + 1건 수정**.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1:3 | "running away from God" | EN 슬랭 | "trying to ghost God" → "trying to run away from God". KO는 이미 "하나님한테서 도망가려고" |

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- 2:2-9 기도문 9요소 전수 보존 (deep trouble/answered, belly of grave, watery grave, thrown out of sight/Holy Temple, ocean chokehold/abyss/seaweed/mountains take root/gates slamming, pulled up alive, prayer reached Temple, fake gods, thanksgiving+promised+Salvation belongs to God). "god-frauds"는 "fake gods"로 자명.
- 3:7-9 왕의 선포 6요소 전수 보존 (음식 금지 사람+짐승, 베옷 입히기, 하나님께 부르짖기, 악에서 돌이키기, "Who knows? Maybe God will change his mind... let us live").
- 4:1-2 요나의 항변 4요소 보존 (grace and mercy, not easily angered, rich in love, turn punishment into forgiveness).
- 4:11 숫자 120,000·"innocent animals"·"don't yet know right from wrong" 모두 보존.
- 4:1 "public square" (town gate 아님) — teen "main town square" 정확.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (4장 29문단). null 배지 0.

## 3. merge/split 후보
- 신규 후보: **0건**.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (4장 29문단 전수, 직접 대조 — 긴 기도문·선포·요나 항변·하나님 답변 전수 확인) |
| ② 수정 반영 | PASS (EN 1건, merge/split 미적용) |
| ③ validate_translation.py | PASS (exit 0) |
| ④ 기계적 완전성 검사 | PASS (29문단, 38 name tokens — 잔여 FAIL 5건 전부 오탐 문서화: ch1 [1-2] 'tarshish/joppa/word'는 인접 [3] 문단에 보유된 범위 오탐 / 숫자 3~17·ch2 10·ch3 3,4,5,10·ch4 3,4,5,6,9는 인쇄 절 번호, 단 ch3의 실제 숫자 40은 EN "In 40 days"에 보유 확인) |
| ⑤ build_gdocs.py 재빌드 | PASS (VERIFY_DROPPED=0) |
| ⑥ verify_pairing_content.py | PASS + 실제 셀 내용 기준 짝지음 확인 (ch3 표본: 배지별 MSG↔EN 행 일치) |
| ⑦ Google Docs 업로드 + API 검증 | PASS (테이블 4/4, title 일치, export-back VERIFIED OK). Doc: 요나 (Jonah) — Final: MSG + Teen EN + KO, id 1bX0VJYwqJcFANuyatlb9Rh3eIRxIvgSvYaEryCs-qQE |

## 5. 검증 범위 및 미확인 경계
- 검증한 것: MSG vs EN vs KO 전수 대조 4장, validator, completeness_check(오탐 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉.
