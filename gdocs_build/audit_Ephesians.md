# Ephesians MSG 의미 전수 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG vs EN vs KO 문단별 전수 대조 (6장, 53 MSG 유닛 / 62 Teen 행). 워커 3명이 ch1–2 / ch3–4 / ch5–6으로 나눠 1차 대조, 본인이 MSG 원문 전권 완독 + Teen EN 전권 완독 + KO 샘플 전수 확인 후 각 이슈를 직접 재확인하고 판정.
결과: 텍스트 수정 3건(KO 2건 + KO 타이틀 6장) + merge/split 후보 2건 pending 누적.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 6:5-8 | "regardless of whether you are slave or free" | KO 의미 드리프트 | "일하는 사람이든 아니든" → "종이든 자유인이든 상관없이" (사회적 신분 대조가 근로 여부로 바뀜 — 원문 논리 희석) |
| 3:14-19 | "this magnificent Father who parcels out all heaven and earth" | KO↔EN 불일치 | "하늘과 땅의 모든 것에 이름을 주시는" → "하늘과 땅을 나누어 주시는" (원칙 1 MSG 기준 + 원칙 4 EN primary; KO가 KJV/원전 쪽을 따랐던 것을 정정) |
| 전 장 | KO title 6장 전부 빈 문자열 | KO 타이틀 누락 | 틴 톤 KO 타이틀 6장 부여 (원칙 4, Gal 전례): 1 "하나님의 궁극 변신 프로젝트" / 2 "제로에서 히어로로" / 3 "하나님의 비밀 계획, 드디어 공개!" / 4 "우리 팀을 키워라" / 5 "남 따라 하지 마, 오리지널이 돼" / 6 "최종 보스전" |

### 워커 "정상/경미" 판정 직접 검증 (본인 확인)
- ch1:1-2 "apostle" → EN "God's chosen crew, a special agent" (MSG 자체가 "an apostle, a special agent"로 풀어씀; KO는 "사도" 명시). 삭제 아님 — 수정 불필요.
- ch4 KO "아이돌 군무처럼" (EN "moving rhythmically and easily") — 추가된 비유, 삭제·요약 아님 — 이슈 아님.
- ch5:3-4 KO "bullying greed" → "욕심 많은 탐욕" — 경미한 뉘앙스 약화, paraphrase 범위 — 수정 불필요, 기록만.
- § 헤더 8개 MSG와 1:1 (ch1 The God of Glory / ch2 He Tore Down the Wall / ch3 The Secret Plan of God / ch4 To Be Mature·The Old Way Has to Go / ch5 Wake Up from Your Sleep·Relationships / ch6 A Fight to the Finish). 위치·이름·배지 전부 일치. 창작 헤더 없음.
- 핵심 함정 구간 전수 보존 확인: ch1 축복 목록(택하심·입양·구속·기업·성령 인침), ch2 벽 허뭄("fine print and footnotes"·"a new kind of human being"), ch3 4중 영광 선포, ch4 은사 4종(사도·선지자·복음전하는 자·목사-교사)+시편 인용, ch5 가정 윤리 전 지시, ch6 전신갑주 5부위+기도 5요소+두기고.

## 2. 메타데이터 수정

1. **KO title 6장 부여** (위 표). EN/KO parity 복원.
2. ch2 1-6 split, ch3 v8 splits 선언 — 이미 존재, 실제 문단과 일치 확인. 변경 없음.
3. `verseRanges == msg_ranges` 6장 전부 일치 (EN/KO). null 배지 0.

## 3. merge/split 후보 (성욱 컨펌 전 구조 변경 금지)

`merge-split-candidates.md`에 E1·E2로 pending 누적:
1. ch2 — MSG 1-6 단일 문단 → Teen 2문단 (죄의 삶 묘사 / 자비로 살리심).
2. ch3 — MSG 7-8 / 8-10 (v8 공유) → Teen 2문단 (MSG 자체 문단 구분).
- 둘 다 내용 손실 없음. 본문 구조 변경 없음.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (6장 53 MSG 유닛 전수, 워커 1차 + 본인 직접 재확인) |
| ② 이슈 리포트 | 본 문서 |
| ③ 수정 반영 | PASS (위 1–2절, merge/split 미적용) |
| ④ validate_translation.py | PASS (6장, exit 0) |
| ⑤ 기계적 완전성 검사 | PASS (54문단, 106 name tokens, 9 number tokens — 누락 0) |
| ⑥ build_gdocs.py 재빌드 | PASS (62행, 53 MSG 유닛, orphan 0, VERIFY_DROPPED=0) |
| ⑦ verify_pairing_content.py | PASS (6 테이블 54행, PAIRING CONTENT OK) |
| ⑧ Google Docs 재업로드 + API 검증 | PASS (테이블 6/6, export-back VERIFIED OK) |

## 5. 검증 범위 및 미확인 경계

- 검증한 것: MSG vs EN vs KO 전수 대조 6장, validator, completeness_check(누락 0), DOCX 빌드, 짝지음 내용 검증, Google Docs 재업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 실제 브라우저 화면 확인은 미확인으로 남김.
