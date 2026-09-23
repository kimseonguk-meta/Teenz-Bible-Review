# 1Corinthians 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG). EN primary, KO는 EN 1:1.

## 감사 방법
- 장별 4개 그룹 병렬 전수 대조: MSG `msg_1Corinthians.txt` 전 문단 vs EN 전 문단 vs KO 전 문단 (문장 단위 완전성, 고유명사·숫자·인용구·경고·비유 세부).
- 기계적 완전성 검사: 16장 148문단, 이름 188·숫자 36 토큰 → FAIL 1건 = 오탐(대명사 one, 아래 문서화).
- 문장 수 parity (soft gate): 별도 플래그 없음 (9–12장 그룹 diff+육안 대조에서 EN≈MSG 텍스트 확인).
- EN/KO 구조 parity: validator로 확인 (문단 수·배지 1:1).
- 욕설 스크리닝: validator 검사 (원칙 5). 별도 위반 없음.

## 발견 이슈 및 수정 (9건)

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 2:6-10 | "they wouldn't have killed the Master of the God-designed life **on a cross**" | EN 누락 | EN에 "on a cross" 복원 (KO는 이미 보유) |
| 2:14-16 | "Isaiah's question, 'Is there anyone around who knows God's Spirit…?'" | EN 누락 (고유명사) | EN에 "Isaiah's" 복원 (KO는 "이사야의 질문" 보유) |
| 1:22-25 | "While **Jews** clamor for miraculous demonstrations and **Greeks** go in for philosophical wisdom" | EN 희석 | EN 첫 문장 "some people/others" → "the Jews"/"the Greeks" 복원 (KO는 명칭 유지) |
| 16:12 | Apollos — `But there will be a "right time."` | EN 오타 | 닫는 따옴표 추가 |
| 14:20-25 | 불신 외부인이 방언 듣고 "taken leave of your senses" | KO 의미반전 | "너네 대단하다고" → "너네가 정신이 나갔다고" |
| 16:10-11 | 디모데 파송 — "send him on to me with your blessing… I'm expecting him, and any friends he has with him" | KO 누락 + 의미반전 | "축복을 실어 보내라" 문장 복원, "내가 걔랑 같이 오는 친구들도 기다리고 있다"로 정정 |
| 14:13-17 | "my mind lies fallow, and all that intelligence is wasted" | KO 드리프트 | "머리도 그만큼 나빠질 거임" → "그 많은 지능이 낭비되는 거임" |
| 13:1 | 사랑 장 서두 | KO 오타 | "대단게" → "대단하게" |
| 9:8-12 | "Don't muzzle an ox **to keep it from eating the grain** when it's threshing" | KO 미세왜곡 | "입마개 씌워서 일 못하게" → "곡식을 먹지 못하게 입마개를 씌우지 마라" |

### 메타데이터 수정 (20건, EN+KO)
- 10개 § 헤더 장(1,5,7,8,11,12,13,14,15,16)의 `msg_ranges`가 헤더 슬롯을 빼먹어 한 칸씩 밀림 → `verseRanges`와 동일하게 정정 (Acts·Mark·Romans 컨벤션: msg_ranges == verseRanges, § 헤더는 뒤따르는 본문과 배지 공유). 렌더는 `verseRanges` 기준이라 독 배지는 변경 전부터 정상이었음.
- 5장 "§The Mystery of Sex"는 MSG 실재 헤더임 (msg_1Corinthians.txt 151행) — 창작 아님. 감사 워커 1차 판단(창작) 정정.

### 오탐 1건 (수정 없음)
`completeness_fp_1Corinthians.md`에 문서화. 4:5 "any one of us"의 one은 대명사 용법, "any of us"로 의미 보존 — Acts 감사 A클래스와 동일.

### merge/split 후보
- 신규 후보 **1건**: 8:7 merge — MSG가 8:7을 두 문단("In strict logic, then…"/"We need to be sensitive…")으로 나누는데 EN·KO가 한 문단으로 합침. 내용 누락 없음. → `merge-split-candidates.md`에 증거와 함께 기록, 적용 안 함.
- 그 외 후보 없음. 10개 § 헤더는 MSG 실재 헤더의 정상 배치 (분할 아님).

## 검증 게이트
1. ✅ 의미 전수 감사 — MSG 전 문단 대 teen/KO 전수 대조 (4개 그룹).
2. ✅ 이슈 리포트 작성 — 본 문서 + completeness_fp_1Corinthians.md.
3. ✅ 수정 반영 — 텍스트 9건 + 메타데이터 20건. merge/split 신규 적용 없음.
4. ✅ validate_translation.py — 16장 모두 PASS.
5. ✅ 기계적 완전성 검사 — FAIL 1건 오탐 문서화 후 통과.
6. ✅ build_gdocs.py 재빌드 — 16장, 158행, VERIFY_DROPPED=0, 누락 0.
7. ✅ 독 짝지음 검증 — verify_pairing_content.py, 16개 표 148행 내용 대조 OK.
8. ✅ Google Docs 재업로드 — API 테이블 수 16/16, export-back VERIFIED OK.

## 검증 범위
- 확인함: MSG 16장 전 문단 대 EN/KO 전수 대조, EN/KO 배지·문단 parity, 욕설 자동 스크리닝, 렌더 배지 기준(verseRanges) 정합.
- 확인하지 못함: KO 본문 전수 의미 대조는 EN 기준 구조 parity + 그룹별 1:1 대조로 수행 (감사 워커가 KO도 전수 대조함), 자동 욕설 목록 밖 미묘한 표현의 뉘앙스, Google Docs 웹 화면의 실제 렌더 (API + export-back DOCX로 대체 검증).
