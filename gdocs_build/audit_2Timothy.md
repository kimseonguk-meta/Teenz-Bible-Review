# 2Timothy 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG 26개 유닛 vs EN/KO 전수 대조 (4장, 코디네이터 직접 3단 대조 — 워커 없이 수행). 기계적 완전성 검사 FAIL 0건.
결과: 텍스트 수정 1건(KO). merge/split 신규 후보 0건. 기존 splits/merges 선언 없음.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1:15-18 | "everyone in the **province of Asia** deserted me" | KO 경미한 누락 | "아시아에 있는 사람들은" → "아시아 지방에 있는 사람들은" (EN은 "province of Asia" 보유 — KO 수정 신호 사례) |

### 직접 확인하고 유지로 판정한 사항
- 1:1-2 §헤더 EN "§Be Bold with God's Gifts" (MSG "To Be Bold with God's Gifts") — "To" 생략은 의미 차이 없음. KO "§은사를 담대하게 써라"와 함께 유지.
- 1:3-4 KO "사실 거의 매일인데" (MSG "practically all the time") — 틴 의역 범위, 유지.
- 4:14-15 KO "하나님이 그가 한 만큼 갚아주실 거야" (MSG "God will give him what he's got coming") — 신적 응보 의미 유지, 유지.
- § 헤더 전부 MSG와 1:1 (ch1 To Be Bold with God's Gifts / ch2 Doing Your Best for God / ch3 Difficult Times Ahead, Keep the Message Alive). 창작 헤더 없음.
- 함정 구간 전부 보존: 19개 악덕 목록(ch3, EN/KO 19개 전수), 4중 조건문(ch2 "if we die with him…"), 4:6-8 경주/면류관, 인명 전수(Demas·Crescens·Titus·Tychicus·Carpus·Alexander·Priscilla·Aquila·Erastus·Trophimus·Eubulus·Pudens·Linus·Claudia·Jannes·Jambres·Hymenaeus·Philetus·Onesiphorus·Phygelus·Hermogenes·Lois·Eunice).
- 타이틀 4장 전부 EN/KO 보유 (KO 공란 없음).

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (8/7/6/9). null 배지 0.
- `verseRanges == msg_ranges` 4장 전부 일치. splits/merges 선언 없음.
- EN §헤더 3개(ch1 P1, ch2 P0, ch3 P0/P3)가 별도 행 — MSG 구조와 매칭.

## 3. merge/split 후보
- 신규 후보: **0건**.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (4장 26 MSG 유닛, 코디네이터 직접 3단 대조) |
| ② 이슈 리포트 | 본 문서 |
| ③ 수정 반영 | PASS (KO 1건, merge/split 미적용) |
| ④ validate_translation.py | PASS (4장, exit 0) |
| ⑤ 기계적 완전성 검사 | PASS (26문단, 64 name tokens, 4 number tokens — FAIL 0) |
| ⑥ build_gdocs.py 재빌드 | PASS (VERIFY_DROPPED=0, 30행·26유닛·orphan 0) |
| ⑦ verify_pairing_content.py | PASS (26행·4테이블 OK) |
| ⑧ Google Docs 재업로드 + API 검증 | PASS (테이블 4/4, export-back VERIFIED OK) |

## 5. 검증 범위 및 미확인 경계

- 검증한 것: MSG vs EN vs KO 전수 대조 4장, validator, completeness_check(FAIL 0), DOCX 빌드, 짝지음 내용 검증, Google Docs 재업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함 (API + export-back으로 대체). 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉.
---

## 부록: 2026-09-23 미묘한 슬랭 일괄 수정 (번역 원칙 5)

- 배경: 신약 27권 EN/KO 전수 검사에서 자동 욕설 목록 밖의 미묘한 슬랭·저속 표현 발견. 성욱 지시("B 기준 정하고 한 번에 해")에 따라 아래 확정 6개 Rule로 일괄 수정.
- Rule: ① 채팅 약어·유행 은어(ㅇㅋ·here's the tea·woke·throw shade·GOAT·FOMO·fam·vibe) ② 원칙 5 명시 슬랭(썰·꿀잼·쌩까·드립·뇌절·어그로·인싸춤·뿅·텐션·뇌정지·가오·찢길각) ③ ghosting 계열(ghost·고스팅) ④ 신성한 대상 경량화(찐·대박·인싸/아싸·레전드·흑역사·맛집·핫해·좋아요·게임 체인저·That loser is gone) ⑤ 저속·모욕·첨가 강화 순화(관종·lame·freaking out·working my butt off·맛이 갔네·한심·일진/꼽준다·멘붕·멘탈·올인) ⑥ 유지(chill·bro·왕따 — 변경 없음)
- 수정 원칙: EN primary(MSG 의미 유지), KO는 수정된 EN의 의미·톤 1:1, 의미 축소·본문 구조 변경 금지, 해당 표현만 최소 수정.

- 본 권 수정: **EN 0건, KO 1건** (합계 1건). Rule ⑥(chill·bro·왕따) 변경 없음.

| 장 | 위치 | 언어 | Rule | 기존 | 수정 |
|---|---|---|---|---|---|
| 3 | p4 | KO | ⑤ | 그리스도를 위해 올인하며 살려는 사람은 | 그리스도를 위해 모든 걸 걸고 살려는 사람은 |

**8개 게이트 결과 (2026-09-23)**: 8개 게이트 전부 PASS (2026-09-23)
