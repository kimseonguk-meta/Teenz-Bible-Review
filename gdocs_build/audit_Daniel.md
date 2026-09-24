# 다니엘 (Daniel) MSG 전수 감사 기록

- 감사일: 2026-09-24
- 기준: Eugene Peterson, The Message (MSG) — `msg_Daniel.txt` parsed 177 units
- 대상: `fixes/en_Daniel.json`, `fixes/ko_Daniel.json` (각 12장, 196문단)
- 원칙: TRANSLATION_PRINCIPLES.md 5대 원칙. EN primary, KO는 EN 1:1 반영.
- 상태: validator PASS, build VERIFY_DROPPED=0, pairing OK, Google Docs 업로드·검증 완료

## MSG 원문 품질 검증

- `parse_msg_txt` 정상 파싱. 총 177개 MSG 유닛, 12장 모두 존재.
- 표준 절 기준 장별 절 커버리지 100% (1장 21/21 … 12장 13/13), 장 중간 결손 없음.

## 기계 검사

- `validate_translation.py`: **PASS — 12개 장 모두 통과** (수정 전에도 통과, 수정 후 재통과)
- `completeness_check.py` (EN): 최초 23건 FAIL → 복원 후 9건.
  잔여 9건은 전부 오탐으로 판정, 근거는 `gdocs_build/completeness_fp_Daniel.md`.
- `build_gdocs.py Daniel`: rows=196, msg_units=177, teen_without_msg=0,
  msg_orphans=0, **VERIFY_DROPPED=0**, pairing mismatch 0 (ALL VERIFY OK)
- `verify_pairing_content.py`: 196 data rows / 12 tables — PAIRING CONTENT OK
- Google Docs: 기존 문서 업데이트 (ID `1i7uLZ_e2hfRYobUrQnetmKn7Y4RdmSfOmAuiz9BSFeo`),
  API 테이블 12개, export-back VERIFIED OK,
  제목 `다니엘 (Daniel): MSG + Teen EN + KO` 유지 (기존 em-dash → 콜론으로 정정)

## 구조 정상화 (근본 수정)

각 장의 `msg_ranges`가 Teen `verseRanges`와 동일하게 시드되어 있어
Teen split이 MSG split처럼 보이고 validator가 중복을 원문 overlap으로
오인하던 문제를 수정. parsed MSG 177 유닛 기준으로 전 장 `msg_ranges`를
MSG 유닛 구조로 정상화하고, 가독성 목적의 Teen 분할은 `splits`에 선언
(EN/KO 양쪽 동일). MSG 자체의 인쇄 범위 overlap(1장 17-19/19-20,
2장 5-6/6-9·14-15/15-16·31-36/36-40, 4장 13-15/15-16, 7장 11-13/13-14,
9장 1-4/4-8, 11장 5-6/6-9·21-24/24-26 등)은 원문 overlap으로 유지.

선언된 splits (스탠딩 승인 규칙 적용 — 내용 온전·EN/KO 일치·순수 가독성 구조):

| 장 | MSG 유닛 | Teen 문단 |
|---|---|---|
| 2 | 19-23 | idx 11 (19) / idx 12 (20-23) |
| 2 | 44-45 | idx 20 (44) / idx 21 (44-45) |
| 3 | 24 | idx 7 / idx 8 |
| 3 | 26 | idx 10 / idx 11 |
| 4 | 13-15 | idx 6 (13) / idx 7 (14-15) |
| 4 | 19 | idx 11 / idx 12 / idx 13 |
| 4 | 20-22 | idx 14 / idx 15 (22) |
| 4 | 34-35 | idx 22 / idx 23 |
| 4 | 36-37 | idx 24 / idx 25 (37) |
| 5 | 24-26 | idx 8 / idx 9 (26) |
| 6 | 6-7 | idx 2 / idx 3 |
| 6 | 11-12 | idx 7 / idx 8 (12) |
| 6 | 25-27 | idx 19 / idx 20 (26-27) |
| 7 | 9-10 | idx 7 (9) / idx 8 (9-10) |
| 9 | 1-4 | idx 0 (1-2) / idx 1 (3-4) |
| 10 | 11 | idx 5 / idx 6 |
| 10 | 18-19 | idx 9 / idx 10 (19) |
| 12 | 1-2 | idx 0 / idx 1 (2) |

8장·11장은 split 없음. 1장은 split 없음(MSG 자체 overlap만 존재).
배지 정정 1건: 7장 idx 9 배지 `11-12` → `11-13` (MSG 유닛 [11,12,13]에 맞춤, EN+KO).

## 내용 복원 내역 (MSG 대비)

### 2장
- idx 0: "Babylonian magicians" 복원 ("all the Babylonian magicians, enchanters, sorcerers, and psychics")

### 3장
- idx 1: 악기 6종 전부 복원 — "trumpets, trombones, tubas, baritones, drums, and cymbals"
  (기존 "trumpets, trombones, everything" 축약)
- idx 2: "all the musical instruments of Babylon" 복원
- idx 3: "Babylonian fortune-tellers" 복원, "high positions in the province of Babylon" 복원
- idx 4: "King Nebuchadnezzar was livid" — 이름 복원
- idx 5: "answered King Nebuchadnezzar" — 이름 복원
- idx 6: "tie up ... hands and feet" / "Bound hand and foot, fully dressed from head to toe" 복원
- idx 12: "the fire hadn't so much as touched the three men" — "the three men" 복원

### 4장
- idx 2: "witches" 복원 (MSG: magicians, enchanters, fortunetellers, witches)
- idx 3: "full of the divine Holy Spirit" (MSG 원문 표현으로 정정)
- idx 5: "from the four corners of the Earth" 복원 (기존 "anywhere on Earth")
- idx 14: "from the four corners of the world" 복원 (기존 "everywhere")
- idx 18: "Then your good life will continue." — 임의 추가된 "maybe" 삭제
- idx 19: "Just twelve months later" — 숫자 12 복원 (기존 "A year later"; KO는 이미 12개월)

### 5장
- idx 6: "soaked by heaven's dew" 복원 (기존 "rain"; KO는 이미 "하늘의 이슬")

### 7장
- idx 8: "tens of thousands attended him" 복원 (EN+KO)
  — MSG "Thousands upon thousands served him, tens of thousands attended him"의 두 번째 집단

### 8장
- idx 1: "charging first west" — "first" 복원

### 9장 — 전면 재작성
- 기존 EN/KO가 NIV식 표현에 치우쳐 MSG 고유 표현("throttle rebellion",
  "put rebellion in a chokehold", "you've got skin in the game",
  "the Holy of Holies" 등)이 다수 누락·변형되어 있었음.
- MSG 12개 유닛 기준으로 EN 13문단 전면 재작성(teen voice 유지),
  KO도 새 EN에 1:1 대응 재작성.
- KO 9:24: "지극히 거룩한 이"(사람처럼 읽힘) → "지성소"(장소 의미로 MSG 정렬)

### 10장
- idx 1: "no seasoning" 복원 (EN+KO, 기존 "no fancy food" 일반화)
- idx 2: "the great Tigris River" — "great" 복원
- idx 5: "Stand at attention." 복원
- idx 8: messenger에게 "Dude," → "Master," (MSG "master" 기준, 문맥상 호칭 정정)

### 11장
- idx 3: "the two of them will make a deal" — "the two of them" 복원
- idx 10: "his rule, reputation, and authority already in shreds" — 세 요소 복원
  (기존 reputation만; KO는 이미 세 요소 있음)
- idx 15: "desecrate the Sanctuary and the citadel" — "and the citadel" 복원
  (KO는 이미 "성소와 성채")
- idx 16: "refine, cleanse, and purify" — "cleanse" 복원 (KO는 이미 3요소)
- idx 18: "people will fall before him like dominoes" — "like dominoes" 복원
  (KO는 이미 "도미노처럼")

### 1·6·12장
- 내용 누락 없음. 구조 정상화(splits 선언·msg_ranges 정정)만 적용.

## EN-KO 정렬 특이사항

- 1장 KO "환관장/아스부나스" vs EN "head of the palace staff": 한국어 성경 전통 용어로
  의미 차이 없음. 용어 선택으로 보고 유지.
- 4장 KO "거룩한 파수꾼" vs EN "holy messenger": 의미 대응으로 보고 유지.
- 3장 idx 4: EN "second chance" / KO "두 번째 기회"로 MSG에 맞춤 (기존 "one more chance"/"마지막으로 한 번 더").

## 슬랭 점검

- EN teen voice 유지 (no cap, goated, W/L 등). 저속·모욕 표현 없음.
  10장 messenger 호칭 "Dude"는 "Master"로 정정.
- KO 과도한 표현(쌩까고·빡침·압살·진짜임 등) 전수 점검 — 3장 KO "쌩까고" 포함
  거친 표현은 이미 정리된 상태로 확인됨. 추가 수정 없음.

## 승인 필요 항목

없음. 발견된 모든 누락·오역·EN/KO 불일치는 위와 같이 복원/정렬했고,
merge/split은 스탠딩 승인 규칙(내용 온전·EN/KO 일치·순수 가독성 구조)에 따라
선언 후 진행. 성욱 컨펌 대기 중인 항목 없음.

## 변경 통계 (원본 대비)

- EN: 196문단 중 39문단 수정 (9장 재작성 13문단 포함), 배지 변경 1건 (7장 11-12→11-13)
- KO: 196문단 중 16문단 수정 (9장 재작성 13문단 포함), 배지 변경 1건 (동일)
- 문단 수·순서 변경 없음 (EN/KO 모두 196문단 유지)

## 검증 범위와 미확인 경계

- 검증: MSG parsed 177 유닛 ↔ EN/KO 196문단 전수 대조(수동 정독 1-12장),
  validator, completeness_check, build_gdocs(VERIFY_DROPPED=0),
  verify_pairing_content, Google Docs API 테이블 수·export-back·제목.
- 미확인 경계: 앱 화면 렌더링은 이번 감사 범위에 포함되지 않음
  (구약은 production 앱에 반영하지 않음).

## 2nd re-audit (Sep 24)
- completeness_check: 9 candidates → 5 false positives (Babylonian→"in Babylon", "Revealer of Mysteries"→"God who reveals mysteries", "Arbitrarily"/"contemptuous"/"unleashing" paraphrases, number extractor artifacts).
- Sentence-count scan flagged 19 spots; all verified as teen-side splits with full coverage in sequence (ch1, ch2, ch4, ch5, ch6, ch7, ch9, ch10, ch11).
- 4 MSG omissions restored in EN (KO already had all of them — EN brought to parity):
  - ch3 idx2 (badge 7): "the gold statue the king had set up" → "the gold statue that King Nebuchadnezzar had set up" (name drop).
  - ch3 idx3 (badge 8-12): "Hey, King," → "Hey, King Nebuchadnezzar,"; "You made a rule" → "You gave strict orders"; "a furnace" → "a roaring furnace"; "the gold statue" → "the gold statue you set up"; also fixed typo "you.hey're" → "you. They're".
- Gates: STRUCT OK (12 ch, EN/KO parity); build VERIFY_DROPPED=0, teen_without_msg=0, msg_orphans=0; docx pairing spot-check OK; reupload API tables 12/12 VERIFIED OK.
