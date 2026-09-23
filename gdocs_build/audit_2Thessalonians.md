# 2Thessalonians 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG vs EN vs KO 문단별 전수 대조 (3장, 18 MSG 유닛 / 22 Teen 행). 워커 2명이 ch1–2 / ch3로 나눠 1차 대조, 본인이 MSG 원문 전권 + Teen EN 전권 + KO 전권을 직접 대조해 각 이슈를 재확인하고 판정. 기계적 완전성 검사 FAIL 3건은 전수 수동 대조 후 오탐으로 문서화 (completeness_fp_2Thessalonians.md).
결과: 텍스트 수정 9건(EN 5 + KO 4) + 메타데이터 0건. merge/split 신규 후보 1건 (기존 적용분, pending 기록).

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 1:1-2 | "Our God gives you everything you need" — 주어는 God the Father | EN/KO 의미반전(경미) | EN "He's the one who hooks you up…" → "The Father's the one who hooks you up…" ("He's"가 직전 명사 Jesus Christ를 가리켜 공급자가 성부→예수님으로 바뀜). KO "그분이" → "하나님 아버지가" |
| 2:3-5 | "He'll defy and then **take over** every **so-called** god or altar" | EN/KO 의미변경 | EN "dissing every other god and trashing their temples" → "defying every so-called god and taking over their altars" ("take over"→"trashing"은 장악→파괴로 의미 변경, "so-called" 누락). KO "온갖 신들을 대적하고 신전들을 다 뒤집어엎는" → "소위 신이라는 것들을 모조리 대적하고 제단을 차지하는" |
| 2:3-5 | "he'll then set himself up in God's Temple as **'God Almighty'**" — 왕좌 언급 없음 | EN/KO 창작 요소 + 인용구 희석 | EN "sit on the throne, and be like, 'I'm God now'" → "and set himself up, declaring, 'I am God Almighty.'" (MSG에 없는 "sit on the throne" 삭제, 인용구 "God Almighty" 복원). KO "왕좌에 앉아서 '이제 내가 하나님이야'" → "'내가 전능하신 하나님이야'라고 선언" |
| 2:9-12 | "God **rubs their noses in it** — gives them what they want" (적극적 심판 뉘앙스) | EN/KO 희석 | EN "God gives them exactly what they want" → "God rubs their noses in it — gives them exactly what they want". KO "그들이 원하는 걸 그대로 주셔" → "그 악을 그들 코앞에 들이밀어 주셔 — 그들이 원하는 걸 그대로 주시는 거야" |
| 3:8 | "We didn't sit around on our hands **expecting others** to take care of us" | EN 희석(경미) + 원칙④ | EN "expecting **you** to take care of us" → "expecting **everyone else** to take care of us" (MSG의 "others"를 "you"로 좁힘. KO는 "남들이 챙겨 주길"로 MSG에 정확했음 — KO 수정 불필요) |

### 워커 지적 중 유지로 판정한 항목 (본인 판단)
- **1:11-12** "our God giving himself freely, the Master, Jesus Christ, giving himself freely" 2회 반복 → EN "the free gift of grace from our God and the Lord, Jesus Christ" 1회. 두 인격이 명명되고 "freely"("free gift")가 양쪽에 적용되므로 의미 보존. 수사적 반복의 축소는 teen-voice 범위 — 수정 안 함.
- **3:13** MSG "Friends, don't slack off in doing your duty." 한 문장에 EN이 "Don't burn out doing the right thing — keep going." 덧붙임. 완전성 위반 아니고 KJV("be not weary in well doing")와도 부합하는 동일 문장 내 teen-voice 확장 — 유지.
- **"That loser", "ghosted God"** 등 teen 표현: 과도 슬랭 목록 수준 아님, 의미 유지 — 유지.

## 2. 구조 검사
- § 헤더 3개 MSG와 1:1 (ch1 "Justice Is on the Way", ch2 "The Anarchist", ch3 "Those Who Are Lazy"). 위치·배지 일치, 창작 헤더 없음.
- EN/KO 문단 수·순서·배지 1:1 (5/7/10). null 배지 0.
- ch1 기존 수정("in a blaze of fire" 복원, 배지 3-4) MSG 정합 재확인.
- ch2 MSG ranges '1-3'/'3-5' 겹침은 MSG 자체 구조 — EN 배지도 MSG 그대로 유지, 구조 이슈 아님.
- ch3 10-13 → 2문단(10-12/13) 분할은 `splits`에 선언됨. MSG 단일 문단을 teen이 나눈 것이므로 merge-split-candidates.md에 pending 후보로 기록 (T1).

## 3. merge/split 후보
- 신규 적용: **0건**.
- 기존 적용분 중 컨펌 필요: **T1** ch3 10-13 → (10-12)/(13) split — `merge-split-candidates.md`에 pending으로 기록. 내용 손실 없음.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (3장 18 MSG 유닛 전수, 워커 1차 + 본인 직접 재확인) |
| ② 이슈 리포트 | 본 문서 |
| ③ 수정 반영 | PASS (위 9건, merge/split 미적용) |
| ④ validate_translation.py | PASS (3장, exit 0) |
| ⑤ 기계적 완전성 검사 | PASS (19문단, 33 name tokens, 2 number tokens — FAIL 3건 전부 오탐 문서화). 검사기 자체 버그 수정: split이 있는 장을 통째로 건너뛰던 문제 → verseRanges 폴백으로 수정 (gdocs_build/completeness_check.py) |
| ⑥ build_gdocs.py 재빌드 | PASS (VERIFY_DROPPED=0, 22행·18 MSG 유닛·orphan 0) |
| ⑦ verify_pairing_content.py | PASS (19 data rows, 3 tables — PAIRING CONTENT OK) |
| ⑧ Google Docs 재업로드 + API 검증 | PASS (테이블 3/3, export-back VERIFIED OK) |

## 5. 검증 범위 및 미확인 경계

- 검증한 것: MSG vs EN vs KO 전수 대조 3장, validator, completeness_check(오탐 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 재업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 실제 브라우저 화면 확인은 미확인으로 남김. 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉.
