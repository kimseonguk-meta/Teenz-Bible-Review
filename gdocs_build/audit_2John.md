# 2John 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG(1장 7개 유닛) vs EN vs KO 문단별 전수 대조 (1장, EN/KO 각각 8행). 전수 대조 워커의 지적 사항을 MSG·EN·KO 실제 텍스트로 다시 직접 확인하고 최종 판정.
결과: 텍스트 수정 0건. merge/split 신규 후보 0건.

## 1. 장:절별 이슈 및 수정

수정 필요 항목 없음.

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- MSG "Deceiver! Antichrist!" → EN "Fakers and Anti-Christs" (틴 gloss, KO "속이는 자! 적그리스도!" 정확). 유지.
- EN 8-9 주체 미세 드리프트 ("Don't let them scam you out of...") — 경고 본질 보존. 유지.
- EN 7 "flesh-and-blood" → "real guy, like, a legit human being" 이중 강조. 유지.
- EN 10-11 "anyone" → "one of these fakers" — 문맥상 동일 대상. 유지.
- EN "Total posers." / KO "그냥 완전 가짜야." 창작 클로징 — restatement로 새 사실 없음. 유지.
- EN "woke" (따옴표) → MSG "gets so progressive in his thinking" 번역 표시. 유지.
- § 헤더 "Don't Walk Out on God" 1:1 (배지 "7" 공유).
- 챕터 타이틀 EN "Watch Out for the Fakers" / KO "가짜를 조심해" 문법 정상, 서로 대응.
- 욕·과도 슬랭: EN/KO 모두 0건.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (8행). null 배지 0.
- `verseRanges == msg_ranges` 일치. splits 선언 빈 배열과 실제 구조 일치.
- 고유명사 전수: God the Father / Jesus Christ / Son of the Father / Antichrist / Deceiver(→Fakers) 전부 등장.

## 3. merge/split 후보
- 신규 후보: **0건**.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (7 MSG 유닛 전수, 직접 대조) |
| ② 이슈 리포트 | PASS (수정 필요 0건) |
| ③ 수정 | N/A (수정 사항 없음) |
| ④ validator | PASS (1개 장 통과) |
| ⑤ 기계적 완전성 | FAIL 2건 → 근본 수정 1건 + 오탐 1건: (a) name "deceiver" — EN의 "Fakers"가 챕터 타이틀+본문에 걸친 의도적 틴 gloss이므로 검사기 ALIASES에 `deceiver ↔ fakers` 추가 (근본 수정, 2Thess 선례와 동일 방식) 후 PASS (b) number "1" (ch1[2] badge 4-6) — MSG "This is the **first** thing you heard" → EN "You've known this **from the jump**" — 관용구가 "first/from the beginning" 의미를 완전히 보존하므로 오탐으로 문서화 |
| ⑥ Docs 재빌드 | PASS (VERIFY_DROPPED=0, 8 rows, 1 table) |
| ⑦ 실제 내용 짝지음 검증 | PASS (7 data rows, PAIRING CONTENT OK) |
| ⑧ Google Docs 재업로드/API+export-back 검증 | PASS (API table 1/1, export-back VERIFIED OK) |
---

## 부록: 2026-09-23 미묘한 슬랭 일괄 수정 (번역 원칙 5)

- 배경: 신약 27권 EN/KO 전수 검사에서 자동 욕설 목록 밖의 미묘한 슬랭·저속 표현 발견. 성욱 지시("B 기준 정하고 한 번에 해")에 따라 아래 확정 6개 Rule로 일괄 수정.
- Rule: ① 채팅 약어·유행 은어(ㅇㅋ·here's the tea·woke·throw shade·GOAT·FOMO·fam·vibe) ② 원칙 5 명시 슬랭(썰·꿀잼·쌩까·드립·뇌절·어그로·인싸춤·뿅·텐션·뇌정지·가오·찢길각) ③ ghosting 계열(ghost·고스팅) ④ 신성한 대상 경량화(찐·대박·인싸/아싸·레전드·흑역사·맛집·핫해·좋아요·게임 체인저·That loser is gone) ⑤ 저속·모욕·첨가 강화 순화(관종·lame·freaking out·working my butt off·맛이 갔네·한심·일진/꼽준다·멘붕·멘탈·올인) ⑥ 유지(chill·bro·왕따 — 변경 없음)
- 수정 원칙: EN primary(MSG 의미 유지), KO는 수정된 EN의 의미·톤 1:1, 의미 축소·본문 구조 변경 금지, 해당 표현만 최소 수정.

- 본 권 수정: **EN 1건, KO 1건** (합계 2건). Rule ⑥(chill·bro·왕따) 변경 없음.

| 장 | 위치 | 언어 | Rule | 기존 | 수정 |
|---|---|---|---|---|---|
| 1 | p5 | EN | ① | Anyone who gets too "woke" and ditches what Christ taught is basically ghosting God. | Anyone who gets too far ahead and ditches what Christ taught is basically running off from God. |
| 1 | p5 | KO | ① | 너무 '깨어 있다'며 그리스도의 가르침을 버리는 사람은 결국 하나님을 버리는 거야. | 너무 앞서 나가며 그리스도의 가르침을 버리는 사람은 결국 하나님한테서 도망치는 거야. |

**8개 게이트 결과 (2026-09-23)**: ① PASS (EN·KO 각 1건 old→new grep 확인) ② PASS (1개 장 통과) ③ FAIL (1건 — 수정 전 baseline과 동일 1건, 슬랭 수정과 무관한 기존 이슈) ④ PASS (1 table, no dropped paragraphs) ⑤ PASS (7 rows pairing OK) ⑥ PASS (기존 Doc ID 재업로드) ⑦ PASS (API table 1/1) ⑧ PASS (export-back VERIFIED OK)
