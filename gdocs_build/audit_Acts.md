# Acts 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG). EN primary, KO는 EN 1:1.

## 감사 방법
- 기계적 완전성 검사: 28장 407문단(헤더 제외), 이름 649·숫자 152 토큰 → FAIL 23건 전수 수동 대조.
- 문장 수 parity (MSG 문단 단위, soft gate): 0건 플래그.
- EN/KO 구조 parity: validator로 확인 (문단 수·배지 1:1).
- 욕설 스크리닝: validator 검사 7 (원칙 5).

## 발견 이슈

### 실제 이슈 1건 (수정 완료)
| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 13:50-52 | "brimming with joy and the Holy Spirit, **two happy disciples**" | 누락 (숫자) + EN/KO 비대칭 | EN에 ", two happy disciples" 복원. KO는 이미 "두 제자" 보유 → 수정 후 EN/KO parity 회복 |

### 오탐 22건 (수정 없음)
`completeness_fp_Acts.md`에 전수 문서화. 클래스: 대명사 one 오인(A) 4건, 서수/관용구(B) 2건, 숙어 paraphrase(C) 3건, 호칭 교체(D) 4건, 지명 형용사→지명(E) 7건, 동의어(F) 3건, checker 아티팩트(G) 2건(일부 중복 분류).

### merge/split 후보
- 신규 후보: **0건**. 이번 감사에서 새로 발견된 merge/split 필요 없음.
- 기존 적용분 (2026-09-22 1차 감사에서 이미 적용, splits 선언됨): ch1 (1-5→1-3/4-5), ch5 (7-8, 12-16), ch6 (1-4), ch27 (9-12, 성욱 승인). → `merge-split-candidates.md`에 증거와 함께 기록, 22권 종료 후 일괄 컨펌 요청 예정.

## 검증 게이트
1. ✅ 의미 전수 감사 — MSG 전 문단 대 teen 전수 대조 (checker + 수동). 실제 누락 1건 수정.
2. ✅ 이슈 리포트 작성 — 본 문서 + completeness_fp_Acts.md.
3. ✅ 수정 반영 — EN 1건. merge/split 신규 적용 없음.
4. ⏳ validate_translation.py — 수정 후 재실행 예정.
5. ⏳ 기계적 완전성 검사 — 수정 후 재실행 예정 ("two" FAIL 해소 확인).
6. ⏳ build_gdocs.py 재빌드 (Acts), VERIFY_DROPPED=0.
7. ⏳ 독 짝지음 검증 — export-back DOCX 셀 내용 대조 (건별, 표 개수 아님).
8. ⏳ Google Docs 재업로드 + API 테이블 수 (28) 검증.

## 검증 범위
- 확인함: MSG 파서 출력(403 units) 대 teen 전수 토큰 대조, 문단 단위 문장 parity, EN/KO 배지·문단 parity, 욕설 자동 스크리닝.
- 확인하지 못함: KO 본문 458문단 전수 의미 대조 (EN 기준 구조 parity + 스팟체크만 수행. 1차 감사에서 KO를 EN 1:1로 재구성한 것을 신뢰), 자동 욕설 목록 밖 미묘한 표현의 뉘앙스, Google Docs 웹 화면의 실제 렌더 (API + export-back DOCX로 대체 검증).
