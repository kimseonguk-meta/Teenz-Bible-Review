# Zechariah 감사 리포트 (2026-09-24, 작업자) — MSG 전수 감사

기준: Eugene Peterson The Message(MSG) 영어 원문 = 유일한 최종 기준. KJV 미사용.
검수 방법: `msg_Zechariah.txt` 파싱(113 units, 14장) ↔ EN ↔ KO 문장·이름·숫자·인용구·반복요소 전수 대조.
시드: 앱 소스에서 재시드한 fixes JSON (2026-09-23 이전 구 감사본은 git history 참조용 — 배지 정정·복원 내용만 참조, § 헤더는 미추가).
결과: **전수 감사 + 수정 EN 본문 7건(6문단)·배지 13개 / KO 본문 2건·배지 13개. splits 31건 선언 (스탠딩 승인 규칙 (a)(b)(c) 충족 — MSG 대비 내용 온전, EN/KO 일치, 순수 가독성 구조 차이). merges 0건.**

## 0. MSG 원문 품질 검증

- `parse_msg_txt`: 14장 전부, 113 units (ch1 14 / ch2 6 / ch3 6 / ch4 8 / ch5 10 / ch6 9 / ch7 6 / ch8 13 / ch9 5 / ch10 4 / ch11 11 / ch12 7 / ch13 4 / ch14 10).
- 절 커버리지: 14장 전 절 완전 (212절), 누락 구간·boilerplate 없음. 특이사항: ch12/13/14 경계에 `### Washing Away Sins`/`### The Day Is Coming` 소제목이 있으나 파서가 장 전환("13 ", "14 1-2")을 정상 인식 — ch12는 v10-14에서 끝나고, ch13 v1–9·ch14 v1-2 정상 파싱됨 (수동 확인).

## 1. 장:절별 이슈 및 수정

### EN (본문 7건 — 6문단 + 배지 6장 13개 정정)

| 장:절 | MSG | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1:21 | "scatter Judah to the four winds" | 숫자 누락 | "scatter Judah everywhere" → "scatter Judah to the four winds" |
| 6:10 | "the home of Josiah son of Zephaniah" | 고유명사 누락 | "at Josiah's house" → "at Josiah son of Zephaniah's house" |
| 6:11 | "Joshua son of Jehozadak, the high priest" | 고유명사 누락 | "Joshua, the high priest" → "Joshua son of Jehozadak, the high priest" |
| 6:14 | "Hen son of Zephaniah" | 고유명사 누락 | "and Hen will be in charge" → "and Hen son of Zephaniah will be in charge" |
| 7:7 | "the Negev and Shephelah" | 지명 누락 | "the whole area was full of people" → "the whole area—the Negev and Shephelah—was full of people" |
| 7:13 | "I scattered them to the four winds" | 숫자 누락 | "He scattered them all over the place" → "He scattered them to the four winds" |
| 9:10 | "from the four winds to the seven seas" | 숫자 누락 | "from sea to shining sea" → "from the four winds to the seven seas" |

배지 정정 (MSG 단락 기준 오배지 — pairing 정확도 위해, verseRanges·msg_ranges 동시 수정):
| 장 | 문단 | 수정 전 | 수정 후 | 근거 |
|---|---|---|---|---|
| 1 | para5/6/7 | [10],[11],[12] | [9],[10],[11] | "Let me show you."는 MSG v9b, 이후 +1씩 밀림 (구 감사본도 [9],[9],[10],[11]로 정정했었음) |
| 4 | para2 | [2] | [2-3] | MSG v2-3 한 단락 문답 |
| 6 | para1 | [2] | [2-3] | MSG v2-3 |
| 7 | para3/para4 | [7-10]/[10] | [7-8]/[9-10] | MSG 7-10 한 단락을 intro(v7-8)/인용구(v9-10)로 분할 |
| 11 | para5 | [10] | [10-11] | MSG v10-11 (지팡이 꺾음 + 탐욕 주인들 목격) |
| 12 | para1/2/3/7/8 | [2-3]/[4]/[5-6]/[10-12]/[10-14] | [1-2]/[3]/[4-5]/[10-11]/[12-14] | +1 밀림 (구 감사본 정정과 동일) |

### KO (본문 2건 + 배지 EN과 동일 6장 13개)

| 장:절 | 문제 유형 | 수정 내용 |
|---|---|---|
| 7:7 | 지명 누락 (EN 1:1) | "예루살렘이 아직 잘나가고 사람 바글바글할 때" → "예루살렘
...[truncated 3357 chars]