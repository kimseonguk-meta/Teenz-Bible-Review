# Nahum 감사 리포트 (2026-09-23, 작업자 A)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1.
검수 방법: MSG(raw 텍스트) vs EN vs KO 전수 대조 (3장 22문단). 1차 감사 변경 이력 확인 후 잔여 이슈 직접 판정.
결과: 텍스트 수정 **0건**. merge/split 신규 후보 0건. 결론: **검증 통과**.

## 1. 장:절별 이슈 및 수정
- 수정 사항 없음.

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- 1:15 "Striding across the mountains" → "running over the mountains": 의역으로 의미 보존 (completeness_check 'striding' FAIL은 [11] 단위 범위 오탐 — 해당 요소는 [15] 문단에 있음).
- 1:14 "You're nothing—no, you're less than nothing!" → "You're a nobody—nah, you're less than a nobody!": 의미 보존.
- 1:13 "the yoke from your neck... the ropes of your bondage" → "that heavy thing off your neck... whatever was holding you down": 의미 보존.
- 2:13 "Assyria, I'm your enemy" → "'Assyria, I'm your enemy now'": 이름·주체 보존 (completeness_check 'assyria/god' FAIL은 범위 오탐 — [13] 문단에 있음).
- 3:3-4 "whores/Whore City/Witch of Seduction" → "immoral women/a witch casting spells": 욕·비속어 순화 원칙(5대 원칙 5) 적용, 의미 보존.
- 3:6 "I'll pelt you with dog dung... 'Slut on Exhibit'" → "throw filth at you... 'Unfaithful on Display'": 순화 원칙 적용, 의미 보존.
- 3:19 "the whole world will applaud and cry 'Encore!'" 등 전수 보존.
- 2:3-12 전투 묘사·사자 비유 10요소, 3:8-13 데베 묘사 11요소 전수 보존 확인.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (3장 22문단). null 배지 0.

## 3. merge/split 후보
- 신규 후보: **0건**.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (3장 22문단 전수, 직접 대조) |
| ② 수정 반영 | PASS (수정 0건, merge/split 미적용) |
| ③ validate_translation.py | PASS (exit 0) |
| ④ 기계적 완전성 검사 | PASS (22문단, 39 name tokens — FAIL 5건 전부 오탐 문서화: 전부 coarse-parse 범위 오탐 — 'striding'은 [15]에, 'assyria/god'는 [13]/[2]에, 숫자는 인쇄 절 번호) |
| ⑤ build_gdocs.py 재빌드 | PASS (VERIFY_DROPPED=0) |
| ⑥ verify_pairing_content.py | PASS + 실제 셀 내용 기준 짝지음 확인 (ch2 표본: 배지별 MSG↔EN 행 일치) |
| ⑦ Google Docs 업로드 + API 검증 | PASS (테이블 3/3, title 일치, export-back VERIFIED OK). Doc: 나훔 (Nahum) — Final: MSG + Teen EN + KO, id 10v8XT2DwWEGdGnjAsI3gqaGde9nR6opFN4En70Y2UBw |

## 5. 검증 범위 및 미확인 경계
- 검증한 것: MSG vs EN vs KO 전수 대조 3장, validator, completeness_check(오탐 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉.
