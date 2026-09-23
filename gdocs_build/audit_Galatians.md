# Galatians MSG 의미 전수 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG vs EN vs KO 문단별 전수 대조 (6장, 55 MSG 유닛 / 61 Teen 행). 워커 3명이 ch1–2 / ch3–4 / ch5–6으로 나눠 1차 대조, 본인이 MSG 원문 전권 완독 후 각 이슈를 직접 재확인하고 판정.
결과: 텍스트 수정 2건(EN 타이틀 오타 1, KO 타이틀 정렬 1) + § 헤더 구조 수정 3건(이동 1, 제거 2) + 메타데이터 정규화.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1:1–5 앞 | MSG "### The Message" §는 1:1–5 뒤·1:6–9 앞에 위치 | § 헤더 위치 오류 | §"The Real Message"를 6–9 문단 앞으로 이동, 배지 '6–9' 부여 (EN/KO). 2Cor ch11 전례 |
| 4장 앞 | MSG 4장에는 ### 헤더 없음 | Teen 창작 헤더 | §"Children of God" 제거 (EN/KO). ch5 창작 헤더 제거 전례 + Acts/1Cor/2Cor 1:1 컨벤션 |
| 6:6 앞 | MSG 6장에는 "### Nothing but the Cross" 하나뿐 | Teen 창작 헤더 | §"Do Good to Everyone" 제거 (EN/KO). 기존 keep 결정을 1:1 일관성 이유로 번복 |
| 4장 타이틀 | heirship 주제 (4:1 "the heir", 4:7 "you're also an heir") | EN 타이틀 오타 | "From Kid to honored" → "From Kid to Heir" |
| 4장 타이틀 | EN primary | KO 타이틀 불일치 | "어린 상속자에서 어른으로" → "꼬마에서 상속자로" (원칙 4) |

### 워커 "정상" 판정 직접 검증 (본인 확인)
- ch5:19–21 육의 열매 15개 항목, ch5:22–23 성령의 열매 9개 항목 — EN/KO 전부 보존 확인.
- 숫자/이름: three years, fifteen days, fourteen years, Arabia, Damascus, Syria and Cilicia, Barnabas, Titus, James/Peter/John, 430 years, "the noun, note, is singular" — 전부 확인.
- 인용구: "All nations will be blessed in you", "Utterly cursed is every person…", "Cursed is everyone who hangs on a tree", Habakkuk 2종, Isaiah 전문 4행, "Expel the slave mother with her son…" — 전부 보존.
- 5:12 "castrate themselves" → "cut themselves off completely" — 틴 순화 paraphrase로 의미 보존, 유지.
- 6:11 "bold scrawls of my personal handwriting" → "bold scrawls of my own handwriting" — 보존.

## 2. 메타데이터 수정

1. **ch1 § 헤더 이동** (2Cor ch11 전례): para 0(배지 1-5) → 6-9 문단 앞(배지 6-9). 본문 순서 변경 없음.
2. **ch4/ch6 창작 헤더 제거**: Teen § ↔ MSG § 1:1 컨벤션 복원 (MSG § 6개 = Teen § 6개).
3. **전 장 `msg_ranges` 정규화**: `msg_ranges == verseRanges` (1Cor/2Cor/Acts 컨벤션, § 헤더 슬롯 포함).
4. **splits paras 인덱스 재확인**: ch1 v16 [4,5] — 헤더 이동 후에도 [4]=13-16, [5]=16-20으로 유효.

## 3. merge/split 후보 (성욱 컨펌 전 구조 변경 금지)

아래 4건은 모두 MSG 자체의 겹침 범위(v16/v21/v18/v23)를 Teen이 두 문단으로 나눈 것으로, `splits`에 선언済. 내용 손실 없음. `merge-split-candidates.md`에 pending으로 추가.
1. ch1 — MSG 13-16 / 16-20 (v16 공유) → 2문단
2. ch2 — MSG 19-21 / 21 (v21 공유) → 2문단
3. ch3 — MSG 15-18 / 18-20 (v18 공유) → 2문단
4. ch5 — MSG 22-23 / 23-24 (v23 공유) → 2문단

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (6장 55 MSG 유닛 전수, 워커 1차 + 본인 직접 재확인) |
| ② 이슈 리포트 | 본 문서 |
| ③ 수정 반영 | PASS (위 1–2절, merge/split 미적용) |
| ④ validate_translation.py | PASS (6장, exit 0) |
| ⑤ 기계적 완전성 검사 | PASS — 1건 오탐 문서화 (ch5 2-3 "any **one** of you"의 "one"을 숫자 토큰으로 추출, Teen "any of you"와 의미 동일) |
| ⑥ build_gdocs.py 재빌드 | PASS (61행, 55 MSG 유닛, orphan 0, VERIFY_DROPPED=0) |
| ⑦ verify_pairing_content.py | PASS (6 테이블 55행, PAIRING CONTENT OK) |
| ⑧ Google Docs 재업로드 + API 검증 | PASS (테이블 6/6, export-back VERIFIED OK) |

## 5. 검증 범위 및 미확인 경계

- 검증한 것: MSG vs EN vs KO 전수 대조 6장, validator, completeness_check(오탐 1건 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 재업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 실제 브라우저 화면 확인은 미확인으로 남김.
