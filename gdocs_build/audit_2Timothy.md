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
