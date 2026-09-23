# Philippians 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG vs EN vs KO 문단별 전수 대조 (4장, 37 MSG 유닛 / 46 Teen 행). 워커 2명이 ch1–2 / ch3–4로 나눠 1차 대조, 본인이 MSG 원문 전권 + Teen EN 전권 + KO 전수 확인 후 각 이슈를 직접 재확인하고 판정. 기계적 완전성 검사 FAIL 10건은 전수 수동 대조 후 오탐으로 문서화 (completeness_fp_Philippians.md).
결과: 텍스트 수정 13건(EN 8 + KO 5) + 메타데이터 1건. merge/split 신규 후보 0건.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1:7-8 | "He knows how much I **love and miss** you" | EN 경미한 누락 | "He knows I miss you guys like crazy" → "He knows I **love and** miss you guys like crazy" (KO는 "사랑하고 그리워하는지"로 이미 복원돼 있었음) |
| 1:19-21 | "Through your **faithful** prayers and the **generous** response of the Spirit" | EN 희석 | "With your prayers and the help of Jesus's Spirit" → "With your **faithful** prayers and the **generous help** of Jesus's Spirit" (KO는 "신실한 기도/아낌없이"로 이미 복원) |
| 1:22-26 | "As long as I'm alive **in this body**" | EN 경미한 누락 | "As long as I'm alive" → "As long as I'm alive **in this body**" |
| 2:12-13 | "keep on doing what you've done **from the beginning**" | EN 경미한 누락 | "Just keep doing what you've been doing" → "...what you've been doing **from the beginning**" (KO는 "처음부터 해오던 대로"로 이미 복원) |
| 1:12-14 | "my imprisonment has had the **opposite of its intended effect**" | KO 누락 | "내가 여기 갇힌 게 오히려 반대 결과를 낳았어" → "내가 여기 갇힌 게 **걔들이 원했던 거랑은 정반대로** 됐어" (EN에는 "what my haters wanted"로 살아 있음) |
| 1:12-14 / 1:19-21 | — | KO 오타 | "눌리기는컨녕"→"눌리기는커녕", "내 입을 막기는컨녕"→"막기는커녕" |
| 1:18 / 1:19-21 / 1:27-30 | — | KO 오타 | "걀들"→"걔들" 5곳 ("걀들 동기"·"걀들 중"·"걀들은"·"걀들한테"×2) |
| 3:2-6 | "**we** can list what many might think are impressive credentials" (이어 "You know **my** pedigree") | EN 의미전환/희석 | "even though **some people** flash what look like impressive credentials" → "even though **we've got** what most people would call impressive credentials" (주체가 '어떤 사람들'로 바뀌면서 바울 자신의 스펙 포기라는 논리 연결이 흐려짐) |
| 3:2-6 | "filling the air with Christ's praise **as we do it**" | EN 꼬리 누락 | "...Christ's praise" → "...Christ's praise**, like we always do**" (KO는 "우리가 늘 하듯이"로 이미 복원) |
| 3:2-6 | 위와 동일 | KO 의미전환 | "사람들이 아무리 대단해 보이는 스펙을 들이밀어도" → "**우리가 내세울 만한 스펙이 많아도**" (EN 수정과 동기화) |
| 3:7-9 | "everything…is insignificant—**dog dung**" | EN 의도적 표현 순화 | "insignificant — total trash" → "insignificant — **dog dung**" ("dog dung"은 욕/비속어가 아닌 MSG의 의도적 충격 표현. 마태 감사에서 "Dungface"를 복원한 전례와 동일. 의미 유지 원칙) |
| 3:7-9 | "I **didn't want** some petty, inferior **brand of righteousness**" (과거 회고) | EN 시제 전환 + 용어 약화 | "I **don't** want some weak, rule-based **'goodness.'** I **want**…" → "I **didn't** want some weak, rule-based **brand of righteousness.** I **wanted**…" (KO는 "갖고 싶었어"/"의로움"으로 이미 MSG에 가까움) |
| 3:7-9 | 위와 동일 | KO 1:1 동기화 | "그냥 하찮은 쓰레기야" → "그냥 **개똥**이야" (EN 1:1) |

### 메타데이터 수정
- ch1 `splits[0]` (msg_range "18-21")의 `paras: [9, 10]` → `[8, 9]` 정정 (0-based 기준 실제 분할 문단. 1-based 기재 오류. 렌더에는 영향 없음 — 빌드는 badge 기준)

### 워커 "애매" 판정 직접 검증 (본인 판단)
- **4:8-9** "I'd say you'll do best by" 생략 → EN이 바로 명령형으로 진입. 의미 손실 없음, teen voice 스타일 선택 — 수정 안 함.
- **4:3** "since you're right there to help them work things out" → EN "since you're right there with them, do your best to help them work…" — 중재 역할 살아 있음 — 수정 안 함.
- **"쫄다" 수위** (KO 1:12-14 "쫄지 않고 당당하게", 1:27-30 "쫄지나 피하지 마"): MSG "fearlessly" / "not flinching or dodging", EN "not afraid" / "Don't back down or get scared"의 틴 번역. 과도한 슬랭 목록(썰·찢길 각·꿀잼·쌩까고) 수준이 아니고 의미 유지 — 유지.
- **2:5-8 "slave"→"servant"**: 틴 paraphrase 범위. § 헤더는 MSG 원문 "He Took on the Status of a Slave" 유지 — 수정 안 함.

## 2. 구조 검사
- § 헤더 8개 MSG와 1:1 (ch1 A Love That Will Grow / They Can't Imprison the Message, ch2 He Took on the Status of a Slave / Rejoicing Together, ch3 To Know Him Personally / Focused on the Goal, ch4 Pray About Everything / Content Whatever the Circumstances). 위치·배지 일치, 창작 헤더 없음.
- EN/KO 문단 수·순서·배지 1:1 (12/11/10/13). null 배지 0. `verseRanges == msg_ranges` 4장 전부 일치.
- KO가 EN보다 MSG에 가까웠던 6곳(1:7-8 love and miss, 1:19-21 faithful/generous, 1:22-26 in this body, 2:12-13 from the beginning, 3:2-6 as we do it, 3:9 과거시제/의로움)은 EN 수정으로 대칭 회복.

## 3. merge/split 후보
- 신규 후보: **0건**.
- 기존 선언분: ch1 18-21 → 2문단 (splits 선언됨, 본인 직접 확인 — 내용 손실 없음).

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (4장 37 MSG 유닛 전수, 워커 1차 + 본인 직접 재확인) |
| ② 이슈 리포트 | 본 문서 |
| ③ 수정 반영 | PASS (위 13건 + 메타 1건, merge/split 미적용) |
| ④ validate_translation.py | PASS (4장, exit 0) |
| ⑤ 기계적 완전성 검사 | PASS (46문단, 77 name tokens, 5 number tokens — FAIL 10건 전부 오탐 문서화) |
| ⑥ build_gdocs.py 재빌드 | PASS (VERIFY_DROPPED=0) |
| ⑦ verify_pairing_content.py | PASS |
| ⑧ Google Docs 재업로드 + API 검증 | PASS (테이블 4/4, export-back VERIFIED OK) |

## 5. 검증 범위 및 미확인 경계

- 검증한 것: MSG vs EN vs KO 전수 대조 4장, validator, completeness_check(오탐 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 재업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 실제 브라우저 화면 확인은 미확인으로 남김. 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉.
