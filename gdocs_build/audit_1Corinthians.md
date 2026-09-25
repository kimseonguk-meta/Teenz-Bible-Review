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
---

## 부록: 2026-09-23 미묘한 슬랭 일괄 수정 (번역 원칙 5)

- 배경: 신약 27권 EN/KO 전수 검사에서 자동 욕설 목록 밖의 미묘한 슬랭·저속 표현 발견. 성욱 지시("B 기준 정하고 한 번에 해")에 따라 아래 확정 6개 Rule로 일괄 수정.
- Rule: ① 채팅 약어·유행 은어(ㅇㅋ·here's the tea·woke·throw shade·GOAT·FOMO·fam·vibe) ② 원칙 5 명시 슬랭(썰·꿀잼·쌩까·드립·뇌절·어그로·인싸춤·뿅·텐션·뇌정지·가오·찢길각) ③ ghosting 계열(ghost·고스팅) ④ 신성한 대상 경량화(찐·대박·인싸/아싸·레전드·흑역사·맛집·핫해·좋아요·게임 체인저·That loser is gone) ⑤ 저속·모욕·첨가 강화 순화(관종·lame·freaking out·working my butt off·맛이 갔네·한심·일진/꼽준다·멘붕·멘탈·올인) ⑥ 유지(chill·bro·왕따 — 변경 없음)
- 수정 원칙: EN primary(MSG 의미 유지), KO는 수정된 EN의 의미·톤 1:1, 의미 축소·본문 구조 변경 금지, 해당 표현만 최소 수정.

- 본 권 수정: **EN 1건, KO 2건** (합계 3건). Rule ⑥(chill·bro·왕따) 변경 없음.

| 장 | 위치 | 언어 | Rule | 기존 | 수정 |
|---|---|---|---|---|---|
| 6 | p1 | EN | ⑤ | how lame this is | how wrong this is |
| 6 | p2 | KO | ④ | 완전 흑역사가 될 거임. | 정말 부끄러운 일이 될 거야. |
| 15 | p16 | KO | ⑤ | 주님의 일에 올인하라고! | 주님의 일에 전부를 걸라고! |

**8개 게이트 전부 PASS (2026-09-23)**
- ①수정반영: 부록 3건 old→new 쌍 JSON 반영 확인 (신규 문자열 존재·구 문자열 소멸 grep 검증). ②validator: 16장 전부 통과. ③완전성: git HEAD 대비 FAIL 집합 byte-identical — 슬랭 수정으로 인한 신규 이슈 0건 (기존 FAIL 2건은 감사 시 문서화된 오탐, completeness_fp_1Corinthians.md). ④Docs재빌드: rows=158, teen_without_msg=0, msg_orphans=0. ⑤짝지음: 148 data rows / 16 tables PAIRING CONTENT OK. ⑥재업로드: 기존 Doc ID 유지. ⑦API 테이블 수: 16/16. ⑧export-back: VERIFIED OK.

---

## 2차 심층 재검토 (2026-09-25)

- 방법: MSG `msg_1Corinthians.txt` 전 문단 ↔ EN 전 문단 장별 1:1 육안 대조 (16장 148문단 전수), 1차의 오탐(FP-1 "any one" 대명사) 판정 유지.
- 복원 **1건** (EN/KO 비대칭 — KO는 보유, EN만 누락):
  - ch2 idx1 (badge 3-5): MSG "not to some fancy mental or emotional footwork **by me or anyone else**" → EN에 "or anyone else's fancy footwork" 복원. KO는 "나나 다른 누구의 멋진 말재주나 감성 자극"으로 이미 보유 → KO 변경 없음.
- 모호 케이스: ch1 idx10 "Jews treat this like an *anti*-miracle—and Greeks pass it off as absurd" → EN "Some treat this like an anti-miracle, and others write it off as absurd" — 직후 "Jews and Greeks alike"로 지시 대상 명확, 지칭 생략이므로 누락 아님. ch4 idx3 "who do you think you are?" — teen 의역, 내용 손실 없음.
- 게이트: validator PASS 16/16, completeness FAIL 1건(기존 오탐 FP-1 문서화), build_gdocs ALL VERIFY OK (VERIFY_DROPPED=0, teen_without_msg=0, msg_orphans=0), pairing 148 rows OK, Google Doc 16/16 export-back VERIFIED OK.
