# 2Peter 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG(3장 25개 유닛) vs EN vs KO 문단별 전수 대조 (3장, EN/KO 각각 32행). 3개 워커(ch1/ch2/ch3)가 전수 대조 후 지적 사항을 MSG·EN·KO 실제 텍스트로 다시 직접 확인하고 최종 판정.
결과: 텍스트 수정 1건(KO 타이틀). merge/split 신규 후보 0건.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| ch3 타이틀 | MSG 3장: 심판(3:10 "The Day of God's Judgment") + 새 창조(3:11-13 "the promised new heavens and the promised new earth") | KO 타이틀이 EN primary 및 MSG 주제와 어긋남 | KO "세상이 무너지는 날" → "하나님이 모든 것을 새롭게 하시는 날" (EN: "The Day God Makes Everything New"). KO는 심판 절반만 담은 다른 프레임이었을 뿐 아니라, 본문 §헤더 "§하늘이 무너지는 날"과 거의 동일해 챕터 제목과 절 헤더 혼동 위험도 있었음. |

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- ch1: MSG 7개 본문 문단 + 헤더 2개("Don't Put It Off", "The One Light in a Dark Time")가 EN/KO에 1:1. 8가지 덕목 chain, Transfiguration 3요소, 예언 해석 원칙 전부 존재.
- ch2: MSG 10개 본문 문단 + 헤더 2개("Lying Religious Leaders", "Predators on the Prowl") 1:1. 2:4-5(지옥/노아 8명), 2:12-14(거짓 교사 묘사 전 문장), 2:20-22 두 속담 인용 전부 존재.
- ch3: § 헤더 "In the Last Days"(1-2), "The Day the Sky Will Collapse"(8-9) 1:1. 고유명사·숫자·인용 전부 존재.
- 17-18 doxology: EN MSG 그대로("Yes!"), KO "아멘" 자연화 — 의미 손실 없음. 유지.
- "Christ → Jesus" 호칭: 동일 인물 틴 문체. 유지.
- 욕·과도한 슬랭: EN/KO 모두 0건.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (3장 32행). null 배지 0.
- `verseRanges == msg_ranges` 일치 (선언된 split 1건 포함: 17-18 권면+doxology).
- 고유명사 전수: Simon Peter, Noah, Sodom, Gomorrah, Lot, Balaam, Beor, Paul 전부 등장.

## 3. merge/split 후보
- 신규 후보: **0건**.
- 기존 선언분: 17-18 (splits, MSG 구조와 일치 확인).

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (3장 25 MSG 유닛 전수, 직접 대조) |
| ② 이슈 리포트 | PASS (위 1건) |
| ③ 수정 | PASS (KO 타이틀 1건 적용) |
| ④ validator | PASS (3개 장 모두 통과) |
| ⑤ 기계적 완전성 | PASS (26문단 FAIL 0 — 오탐 문서 불필요) |
| ⑥ Docs 재빌드 | PASS (VERIFY_DROPPED=0, 32 rows, 3 tables) |
| ⑦ 실제 내용 짝지음 검증 | PASS (26 data rows, PAIRING CONTENT OK) |
| ⑧ Google Docs 재업로드/API+export-back 검증 | PASS (API table 3/3, export-back VERIFIED OK) |
