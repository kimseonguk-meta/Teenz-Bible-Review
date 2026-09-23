# Jude 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG(1장 11개 유닛) vs EN vs KO 문단별 전수 대조 (1장, EN/KO 각각 13행). 전수 대조 워커의 지적 사항을 MSG·EN·KO 실제 텍스트로 다시 직접 확인하고 최종 판정.
결과: 텍스트 수정 2건(둘 다 KO). merge/split 신규 후보 0건.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 원문 | EN/KO 기존 | 문제 유형 | 수정 내용 |
|---|---|---|---|---|
| 1:8 | "This is exactly the same program of these latest infiltrators: **dirty sex**, rule and rulers thrown out, glory dragged in the mud." | EN "dirty sex" 유지 / KO "더러운 짓" | KO 의미 완화 (MSG 원문 표현이므로 순화 대상 아님) | KO "더러운 짓, 규칙도 리더도 다 무시" → "더러운 성관계, 규칙도 리더도 다 무시" |
| 1:22-23 | "Go easy on those who hesitate in the faith. **Go after those who take the wrong way.**" | EN "Go after those who take the wrong way." 유지 / KO "찾아가서 데려와" | KO 창작 추가 (EN primary 위반) | KO "잘못된 길로 간 사람들은 찾아가서 데려와." → "잘못된 길로 간 사람들은 찾아가." |

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- 타이틀 EN "Watch Out for the Fakes" / KO "가짜들을 조심하라" — 문법 정상. 2John "Watch Out for the Fakers"와 한 단어 차이의 의도적 병행.
- § 헤더 2개 1:1 ("Fight with All You Have in You" 3-4 앞, "Lost Stars in Outer Space" 5-7 앞).
- 1:5-7 EN/KO 공통 부연 "for us today"/"지금도 우리에게 생생한 경고" — 미세 부연, 유지.
- 1:24-25 KO "아멘!" (EN "Yes!") — doxology affirmation, 유지.
- MSG "* * *" 구분선(19/20-21 사이) — 타이포그래피 구분, 유지.
- 욕·과도 슬랭: EN/KO 모두 0건.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (13행). null 배지 0.
- `verseRanges == msg_ranges` 일치. splits/merges 빈 배열.
- 고유명사 전수: Jude, Jesus Christ, James, God the Father, Egypt, Michael, Devil, Moses, Cain, Balaam, Korah, Enoch, Adam, Sodom, Gomorrah, Judgment Day 전부 등장.

## 3. merge/split 후보
- 신규 후보: **0건**.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (11 MSG 유닛 전수, 직접 대조) |
| ② 이슈 리포트 | PASS (위 2건) |
| ③ 수정 | PASS (KO 2건 적용, 정확한 문자열 매칭) |
| ④ validator | PASS (1개 장 통과) |
| ⑤ 기계적 완전성 | PASS (11문단 FAIL 0) |
| ⑥ Docs 재빌드 | PASS (VERIFY_DROPPED=0, msg_orphans=0, 13 rows, 1 table) |
| ⑦ 실제 내용 짝지음 검증 | PASS (11 data rows, PAIRING CONTENT OK) |
| ⑧ Google Docs 재업로드/API+export-back 검증 | PASS (API table 1/1, export-back VERIFIED OK) |
