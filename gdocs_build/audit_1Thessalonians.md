# 1Thessalonians 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG(34 유닛) vs EN vs KO (5장, 39 Teen 행) 문단별 전수 대조. 본인이 MSG 원문 전권 + Teen EN 전권 + KO 전수 직접 확인. 기계적 완전성 검사는 FAIL 0건. MSG raw 텍스트(`msg_1Thessalonians.txt`)와 parsed 유닛 대조로 파서 정확도도 확인 — 헤더 5개·문단 전부 정확히 파싱됨.
결과: 텍스트 수정 **0건**, 메타데이터 수정 0건. merge/split 신규 후보 0건.

## 1. 장:절별 이슈 및 수정
없음. 전수 대조 결과 누락·요약·의미반전·짝지음 오류 0건.

주요 함정 구간 직접 확인 (전부 보존):
- ch1 족보 없음. 고유명사: Paul, Silas, Timothy, Thessalonica, Macedonia, Achaia, Philippi, Athens, Judea, Jesus Christ, Master — 전부 EN 보존.
- ch2 9-12 "working our fingers to the bone, up half the night, moonlighting" — EN "working our fingers to the bone, up half the night, moonlighting" 그대로. KO "뼈 빠지게 일하고, 밤새도록 투잡 뛰면서" — 1:1.
- ch4 15-18 "Archangel thunder! God's trumpet blast!" — EN 그대로, KO "천사장의 우레 같은 외침! 하나님의 나팔 소리!" — 1:1.
- ch5 1-3 인용구 "We've sure got it made! Now we can take it easy!" — EN/KO 보존.
- ch5 6 "dressed up in faith, love, and the hope of salvation" — EN "dressed up in faith, love, and the hope of salvation" 그대로.

## 2. 구조 검사
- § 헤더 5개 MSG와 1:1, 위치·배지 일치, 창작 헤더 없음 (Convictions of Steel / No Hidden Agendas / You're God-Taught / The Master's Coming / The Way He Wants You to Live).
- EN/KO 문단 수·순서·배지 1:1 (body 4/4, 7/7, 5/5, 8/8, 10/10; 헤더 1/1, 1/1, 0/0, 2/2, 1/1). null 배지 0.
- verseRanges vs msg_ranges 차이 4장: 헤더 행이 뒤따르는 본문 배지를 공유하는 컨벤션 (§ 헤더는 본문과 배지 공유 — 원칙 2). validator 통과.
- 기존 splits 선언 2건 (ch1 v5 paras [2,3], ch5 v13 paras [4,5]) — MSG 원문이 해당 절을 두 문단에 걸쳐 사용하는 구조를 EN이 그대로 따른 것. 내용 손실 없음, 변경 없음.

## 3. merge/split 후보
- 신규 후보: **0건**.
- 기존 선언분: 위 splits 2건 (적용 아님 — 이미 선언된 구조, 본인 직접 확인).

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (5장 34 MSG 유닛 전수, 본인 직접 대조) |
| ② 이슈 리포트 | 본 문서 |
| ③ 수정 반영 | PASS (수정사항 없음, merge/split 미적용) |
| ④ validate_translation.py | PASS (5장, exit 0) |
| ⑤ 기계적 완전성 검사 | PASS (34문단, 59 name tokens, 4 number tokens — FAIL 0) |
| ⑥ build_gdocs.py 재빌드 | PASS (rows=39, msg_units=34, orphans=0, VERIFY_DROPPED=0) |
| ⑦ verify_pairing_content.py | PASS (34 data rows, 5 tables — MSG 셀↔EN/KO 셀 내용 대조 OK) |
| ⑧ Google Docs 재업로드 + API 검증 | PASS (테이블 5/5, export-back VERIFIED OK) |

## 5. 검증 범위 및 미확인 경계
- 검증한 것: MSG raw vs parsed 파서 정확도, MSG vs EN vs KO 전수 대조 5장, validator, completeness_check, DOCX 빌드, 짝지음 내용 검증, Google Docs 재업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉.
