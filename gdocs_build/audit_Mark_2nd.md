# Teenz Bible 2차 심층 재검토 리포트 — 마가복음 (Mark)

- 검토일: 2026-09-25
- 검토 범위: 마가복음 1~16장 전 장, § 헤더 제외 본문 문단 전수
- 기준: MSG(The Message, Eugene Peterson) → Teen EN (의미 요소 축약/생략 금지) → Teen KO (EN의 1:1 번역)
- 방법: `build_gdocs.match_msg_for_teen()`으로 MSG–EN–KO 나란히 출력한 pairing 덤프(`/tmp/review/Mark_dump.txt`, ~293KB)를 16장 전장 직접 읽고 판정. 1차 감사(audit_Mark.md, 2026-09-22) 지적분은 현재 JSON에 이미 복원 반영돼 있으므로 현재 텍스트 기준으로 재판정.
- 소스 JSON 수정: **2건** (EN만, KO는 이미 MSG/KO에 있었음)

## 요약

| 구분 | 건수 |
|---|---|
| EN 복원 (MSG 누락 복구) | 2 |
| KO 수정 | 0 |
| checker 후보 중 실제 누락 | 1 → 복원 (ch16 "God's") |
| checker 후보 중 오탐(동의어·동등표현) | 5 (판정 확정) |
| MSG_SUPERSET 구조 차이 (내용 온전) | 7 (순수 구조, 승인 없이 선언) |
| 성욱 판단 필요 (내용 누락·오역·방향 모호) | 0 |

## 복원 2건 (commit 대상)

### 막 2:15-16 — EN에서 "religion scholars" 누락 (KO는 있음)
- MSG: "The religion scholars and Pharisees saw him keeping this kind of company and lit into his disciples: 'What kind of example is this, acting cozy with the misfits?'"
- 수정 전 EN: "The Pharisees saw this and asked his disciples, 'Why does he eat with outcasts?'"
- 수정 후 EN: "The religion scholars and Pharisees saw this and asked his disciples, 'Why does he eat with outcasts?'"
- KO(수정 불필요): "바리새인파의 율법학자들이 예수님이 그런 사람들이랑 어울리는 걸 보고 제자들한테 따졌어요." — 두 집단을 이미 포함.
- 근거: 구약 2차 스윕에서도 반복된 "KO에는 있는데 EN만 빠진 비대칭" 패턴. 집단 명칭은 이름 클래스 복원 대상.

### 막 16:14-16 — EN에서 "God's" 누락 (KO는 있음)
- MSG: "announce the Message of God's good news to one and all."
- 수정 전 EN: "Then he said, 'Go into the entire world and preach the Good News to absolutely everyone.'"
- 수정 후 EN: "Then he said, 'Go into the entire world and preach God's Good News to absolutely everyone.'"
- KO(수정 불필요): "이 기쁜 소식, 바로 하나님의 메시지를 전파하세요" — '하나님의' 이미 있음.

## completeness checker 후보 6건 판정

| # | 위치 | 후보 | 판정 |
|---|---|---|---|
| 1 | ch1 idx7 [9-11] | name: god | 오탐 — MSG "God's Spirit" → EN/KO "Holy Spirit/성령" (동등). |
| 2 | ch3 idx13 [28-30] | repudiating / severing / perversity | 오탐 — EN "reject/cut off/twisted" 동의어. 3중 비유 + 경고 이유 현재 EN/KO 모두 보존됨 (1차 [중요] 복원 확인). |
| 3 | ch4 idx11 [16-17] | number: 1 ("first") | 오탐 — MSG "When they first hear the Word" → EN "get super pumped right away" (의미 보존). |
| 4 | ch7 idx5 [9-13] | denouncing / scrawl | 오탐 — "called out their hypocrisy"(비판), "writes on the ground"(쓰다) 동의어. |
| 5 | ch7 idx14 [20-23] | obscenities / lusts / adulteries / carousing | 오탐 — "dirty thoughts/cravings/cheating on partners/wild partying" 동의어. |
| 6 | ch16 idx7 [14-16] | name: god | **실제 누락 → 복원** ("God's Good News"). |

## MSG_SUPERSET 구조 차이 7건 (순수 구조, 내용 온전)

`build_gdocs.py` PAIRING_MISMATCHES 7건 전부 [MSG_SUPERSET] (MSG 문단이 teen 배지보다 넓은 절 범위 커버). 스탠딩 규칙 ① MSG 대비 내용 온전 ② EN/KO 일치 ③ 가독성 목적 구조 차이를 모두 만족하므로 승인 없이 선언하고 진행:

| # | 위치 | 내용 | 확인 |
|---|---|---|---|
| 1 | ch1 idx22-23 [40-42/43-45] | MSG v40-45 한 문단 → teen 2문단 분할 | "leper healed" 전 내용 양쪽 보존 |
| 2 | ch3 idx1-2 [1-2/3-4] | MSG v1-4 한 문단 → teen 2문단 분할 | 안식일 손 마른 사람 치유 전 내용 보존 |
| 3 | ch13 idx13-15 [14/15/16-17] | MSG v14-18 문단 → teen 3문단 (배지 번호만 MSG와 1절 어긋남) | "winter praying" 포함 전 내용 보존; v18 내용은 teen v16-17 문단에 있음 |
| 4 | ch14 idx46-47 [55-56/57-58] | MSG v55-59 문단 → teen 2문단 (v59 내용은 teen v57-58 문단에 있음) | "couldn't agree exactly" 보존 |
| 5 | ch15 idx16-17 [25-27/29-30] | MSG v25-30 문단 → teen 2문단 (MSG v28 = "Along with him, they crucified two criminals" 내용은 teen v25-27 문단에 있음) | 전 내용 보존 |

※ ch1 idx22/23이 두 줄로 카운트돼 총 7건.

## 1차 감사 지적분 재확인 (현재 JSON 기준)

1차에서 [중요]/[경미]로 지적된 항목 중 현재 JSON에 이미 복원된 것 (이번에 전수 재확인 — 내용 온전):
1:7-8 "will change your life" + "from the inside out" / 1:40-42 "his skin smooth and healthy" / 2:1-2 "He was teaching the Word" / 2:15-16 "had already become his followers" / 3:28-30 삼중 비유 + 경고 이유 / 5:25-29 "from behind" / 9:43-48 "godless" / 12:30·12:32-33 EN식 4중 표현 / 14:43 "leaders" / 14:64 "condemned... one and all" / 15:25-27 좌/우 / 15:46 "linen shroud" / 16:1-3 향료 구매 시점 순서 / KO 따옴표 4건 — 전수 확인, 모두 정상 반영.

## 게이트 결과 (2026-09-25, 수정 후)

- validator: PASS (16개 장 모두 통과)
- build_gdocs.py Mark: `VERIFY_DROPPED=0`, msg_orphans=0, teen_without_msg=0, `ALL VERIFY OK`
- completeness: 5건 모두 오탐 판정 (위 표)
- pairing 표본: 수정 2행 (ch2 idx10, ch16 idx7) 덤프에서 직접 확인 — MSG–EN–KO 일치

## Google Docs

- Doc ID: `19ySnH_Vrv5oiqoLryeaXXOEmpsD7UV-jsx6P59sKIi0` (기존, 16 tables)
- reupload + export-back 검증 결과: (아래 실행 후 기입)
