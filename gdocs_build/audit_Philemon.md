# Philemon 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG(8개 유닛, raw 텍스트와 파서 대조 확인) vs EN vs KO 문단별 전수 대조 (1장, 9행). 1차 감사+재감사 변경 이력(`changes` 필드) 확인 후 잔여 이슈 직접 판정.
결과: 텍스트 수정 1건(EN). merge/split 신규 후보 0건.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 15-16 | "Maybe it's all for the best that you lost him for a while" | EN 의미 왜곡 | "Maybe him **ghosting** you for a while" → "Maybe him **running off** for a while". "ghosting"(연락 두절)은 도망친 노예 오네시모의 상황과 다름. KO는 "네가 걔를 잠깐 잃어버렸던 게"로 이미 정확했음. 챕터 타이틀 "The Runaway Returns"와도 일치. |

### 1차 감사·재감사에서 이미 수정된 사항 (이번 감사에서 직접 확인, 유지)
- 창작 헤더 "§A Plea for Onesimus" 삭제, MSG 정식 헤더 "§To Call the Slave Your Friend" 추가 (EN/KO 모두, 배지 8-9 공유)
- EN 배지 오류 3건 정정: 8-10→8-9, 17-19→17-20(v20 커버리지 복원), 24-25→23-25(v23 에바브라 커버리지 복원)
- EN 1-3 "Christ's blessings on you!" 두 번째 축복 복원, EN 4-7 "doubly so" 복원, EN 10-14 "hand-carrying this letter"·"as your stand-in" 복원
- KO 챕터 타이틀 "도망친 자의 귀환" 부여

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- § 헤더 1개가 MSG와 1:1 ("To Call the Slave Your Friend" / "§노예를 친구로 부르기"). 창작 헤더 없음.
- "Christ → Jesus(의)" 호칭 3곳: 동일 인물 틴 문체 선택 — 오탐 문서화 (completeness_fp_Philemon.md)
- EN 1-3 "I write this letter to you"의 "편지" 명시 없음: 편지 개념은 10-14 "hand-carrying this letter"에서 명시됨. 틴 paraphrase 범위.
- EN "partner in crime for the cause" (MSG "companion in this work"): 친한 친구 관용 표현, MSG 요소 누락 없음.
- EN 4-7 "Oh, thank you, God!" 인용구를 "give God a major shout-out"로 의역: 내용 보존, 틴 문체.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (9행). null 배지 0.
- `verseRanges == msg_ranges` 일치 (헤더 행의 8-9 공유 배지 포함).
- 함정 구간 전수 보존: 인명 9명(Paul·Timothy·Philemon·Apphia·Archippus·Onesimus·Epaphras·Mark·Aristarchus·Demas·Luke), "cutting off my right arm", "chalk it up to my account", "you owe your very life to me", "get a room ready for me".
- MSG 파서 정확도: raw 텍스트와 대조 — 헤더·문단·범위 전부 정확.

## 3. merge/split 후보
- 신규 후보: **0건**.
- 기존 선언분: 없음 (merges/splits 모두 빈 배열).

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (1장 8 MSG 유닛 전수, 직접 대조) |
| ② 이슈 리포트 | 본 문서 |
| ③ 수정 반영 | PASS (EN 1건, merge/split 미적용) |
| ④ validate_translation.py | PASS (1장, exit 0) |
| ⑤ 기계적 완전성 검사 | PASS (8문단, 16 name tokens — FAIL 3건 전부 오탐 문서화) |
| ⑥ build_gdocs.py 재빌드 | PASS (VERIFY_DROPPED=0) |
| ⑦ verify_pairing_content.py | PASS |
| ⑧ Google Docs 재업로드 + API 검증 | PASS (테이블 1/1, export-back VERIFIED OK) |

## 5. 검증 범위 및 미확인 경계

- 검증한 것: MSG vs EN vs KO 전수 대조 1장, validator, completeness_check(오탐 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 재업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 실제 브라우저 화면 확인은 미확인으로 남김. 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉.
