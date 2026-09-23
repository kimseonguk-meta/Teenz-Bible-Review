# 3John 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG(1장 8개 유닛) vs EN vs KO 문단별 전수 대조 (1장, EN/KO 각각 10행). 전수 대조 워커의 지적 사항을 MSG·EN·KO 실제 텍스트로 다시 직접 확인하고 최종 판정.
결과: 텍스트 수정 1건(EN 타이틀 표기). merge/split 신규 후보 0건. **독 빌드 짝지음 버그 1건 발견 → 빌더 근본 수정.**

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 원문 | EN/KO 기존 | 문제 유형 | 수정 내용 |
|---|---|---|---|---|
| ch1 타이틀 | — | EN "A Shout-Out to My honored" (소문자 h) | 타이틀 표기 불일치 (다른 모든 장 타이틀은 Title Case; 히브리서 "Honored One"도 대문자) | EN → "A Shout-Out to My Honored" |

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- 1-4 "my spiritual kids" (MSG "my children") — teen paraphrase. 유지.
- 12 "to anyone" (MSG "lightly") — 의미 동등. 유지.
- KO 5-8 "'그 이름'" 따옴표 — 무해한 강조. 유지.
- § 헤더 "Model the Good" 1:1 (배지 "5-8" 공유).
- 욕·과도 슬랭: EN/KO 모두 0건.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (10행). null 배지 0.
- `verseRanges == msg_ranges` 일치.
- 고유명사 전수: Gaius, Diotrephes, Demetrius, the Name, "Pen and ink", "by name" 전부 등장.

## 3. merge/split 후보
- 신규 후보: **0건**.
- 선언분 검증: 5-8 = 진짜 split (MSG 단일 문단 → 틴 2문단, 선언 note와 실제 일치). 9-10 / 13-14 = MSG가 원래 각각 두 문단이라 1:1 매핑 (선언 note "map 1:1"이 실제와 일치). 선언과 실제 불일치 없음.

## 4. 독 빌드 짝지음 버그 — 근본 수정 (게이트 7에서 발견)
- **증상**: 재빌드된 3John 독에서 MSG의 두 번째 "9-10" 유닛("As if that weren't bad enough...")과 두 번째 "13-14" 유닛("Peace to you...")이 틴 문단과 짝지어지지 않고 "(확인 필요: 대응 틴즈 문단 없음)" 행으로 빠짐. `msg_orphans=2`.
- **근본 원인**: `build_gdocs.py`의 `match_msg_for_teen` greedy coverage가 verse set이 완전히 동일한 서로 다른 MSG 유닛(3John은 "9-10" 문단이 2개, "13-14" 문단이 2개)을 중복으로 취급해 첫 번째 유닛에만 collapse시키고 나머지를 orphan 처리. 데이터 문제가 아니라 빌더 매칭 로직의 결함.
- **수정**: `match_msg_for_teen`에 positional pairing 추가 — 동일 verse set을 가진 MSG 유닛이 2개 이상이고, 같은 배지의 틴 문단 수가 MSG 유닛 수와 정확히 일치할 때만 k번째 틴 문단 → k번째 MSG 유닛으로 순서대로 짝지음. 개수가 안 맞으면 기존 greedy 유지. (공유 split 로직에는 영향 없음)
- **검증**: 수정 후 재빌드 → `msg_orphans=0`, "확인 필요" 행 0개, 10개 데이터 행 전수 육안 확인 (9-10a↔틴4, 9-10b↔틴5, 13-14a↔틴8, 13-14b↔틴9 모두 1:1; 5-8 split 계속 행 표시 정상). 전체 빌드 독 스캔 결과 다른 권에는 동일 결함 없음 (3John만 해당).
- **경계**: `verify_pairing_content.py`는 "확인 필요" 행을 건너뛰고 PASS를 냄 ("checked 9 data rows"). 짝지음 검증기는 불량 행을 실패로 처리해야 하는데 현재는 스킵 — 별도 개선 후보로 기록 (이번 감사 범위에서는 빌더 수정으로 실결함 해소됨).

## 5. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (8 MSG 유닛 전수, 직접 대조) |
| ② 이슈 리포트 | PASS (위 1건 + 빌더 버그 1건) |
| ③ 수정 | PASS (EN 타이틀 1건 + 빌더 근본 수정) |
| ④ validator | PASS (1개 장 통과) |
| ⑤ 기계적 완전성 | PASS (9문단 FAIL 0) |
| ⑥ Docs 재빌드 | PASS (빌더 수정 후 재빌드, VERIFY_DROPPED=0, msg_orphans=0, 10 rows, 1 table) |
| ⑦ 실제 내용 짝지음 검증 | PASS (9 data rows PAIRING CONTENT OK + 10행 전수 육안 확인) |
| ⑧ Google Docs 재업로드/API+export-back 검증 | PASS (API table 1/1, export-back VERIFIED OK) |
