# 호세아 (Hosea) MSG 전수 감사 기록

- 감사일: 2026-09-24
- 기준: Eugene Peterson, The Message (MSG) — `msg_Hosea.txt` parsed 66 units
- 대상: `fixes/en_Hosea.json`, `fixes/ko_Hosea.json` (각 14장, 80문단)
- 원칙: TRANSLATION_PRINCIPLES.md 5대 원칙. EN primary, KO는 EN 1:1 반영.
- 상태: validator PASS, build VERIFY_DROPPED=0, pairing OK, Google Docs 업로드·검증 완료

## MSG 원문 품질 검증

- `parse_msg_txt` 정상 파싱. 총 66개 MSG 유닛, 14장 모두 존재.
- 표준 절 기준 장별 절 커버리지 100%
  (1장 1–11, 2장 1–23, 3장 1–5, 4장 1–19, 5장 1–15, 6장 1–11, 7장 1–16,
  8장 1–14, 9장 1–17, 10장 1–15, 11장 1–12, 12장 1–14, 13장 1–16, 14장 1–9).
- 10장 14절 MSG 원문 확인: **Beth-arba** (Beth-arbel 아님).
- BibleGateway 공개 페이지 대조 (4:1–3, 2:2–13, 10:11–15, 13:7–12) — 캐시와 일치.

## 기계 검사

- `validate_translation.py`: **PASS — 14개 장 모두 통과** (수정 후 재통과)
- `completeness_check.py` (EN): 최초 7건 FAIL → 복원 후 3건.
  잔여 3건은 전부 오탐으로 판정, 근거는 `gdocs_build/completeness_fp_Hosea.md`.
  (ch3 Israelite people, ch6 third day, ch9 dissipated/clamor, ch10 thistles/crabgrass
  4건은 실제 누락으로 모두 복원됨)
- `build_gdocs.py Hosea`: rows=80, msg_units=66, teen_without_msg=0,
  msg_orphans=0, **VERIFY_DROPPED=0** (ALL VERIFY OK)
- `verify_pairing_content.py`: 80 data rows / 14 tables — PAIRING CONTENT OK
- Google Docs: 신규 문서 생성 (ID `1tSss6YnS0o-i8Y4sbHKXKXoDNTATjfccQ2biA8Gcr1w`),
  API 테이블 14개, export-back VERIFIED OK,
  제목 `호세아 (Hosea): MSG + Teen EN + KO`
  (upload_ot_a.py 제목 템플릿을 em-dash에서 콜론 형식으로 통일 — upload_ot_f.py 및 최신 업로드 규격과 일치)

## 구조 정상화 (근본 수정)

1차 편집에서 `msg_ranges`가 Teen 분할 기준으로 시드되어 있던 문제를
parsed MSG 66 유닛 기준으로 전 장 정상화하고, 가독성 목적의 Teen 분할은
`splits`에 선언 (EN/KO 양쪽 동일).

- 13장 MSG 유닛 `13-15` / `15-16` overlap은 MSG 원문의 의도적 중복으로 유지.
- 7장: EN과 KO 문단 수가 달랐던 문제 수정 (둘 다 6문단으로 정렬).
  `3-7` → 문단 1-2, `8-10` → 문단 3-4로 split 선언.
- 9장: EN과 KO 문단 수가 달랐던 문제 수정 (둘 다 9문단으로 정렬).
  `1-6` → 문단 0-2, `10-13` → 문단 4-5로 split 선언.

선언된 splits (스탠딩 승인 규칙 적용 — 내용 온전·EN/KO 일치·순수 가독성 구조):

| 장 | MSG 유닛 | Teen 문단 |
|---|---|---|
| 1 | 2 | 문단 1 / 2 |
| 1 | 4-5 | 문단 4 / 5 |
| 1 | 6-7 | 문단 6 / 7 |
| 1 | 8-9 | 문단 8 / 9 |
| 3 | 4-5 | 문단 2 / 3 |
| 7 | 3-7 | 문단 1 / 2 |
| 7 | 8-10 | 문단 3 / 4 |
| 9 | 1-6 | 문단 0 / 1 / 2 |
| 9 | 10-13 | 문단 4 / 5 |
| 11 | 1-9 | 문단 0 / 1 / 2 |
| 11 | 10-12 | 문단 3 / 4 |
| 12 | 1-5 | 문단 0 / 1 |

그 외 장은 split 없음. merges 없음.

## 편집 과정 중 발견·수정한 정렬 오류

1차 편집 스크립트가 잘못된 문단 인덱스에 덮어써서 3·4·5장에
정렬 결함이 생겼던 것을 전수 재대조 과정에서 발견하고 전면 재작성으로 복구함:

- 3장: 1절 문단이 2-3절 문단 자리에 중복 기입되고 2-3절 내용이 통째로 빠짐
  → 2-3절 복원 (보호막 제거·종교 없는 위로·하나님 없고 기도 없는 삶).
- 4장: 1-3절 문단이 4-6절 자리에 중복 기입, 4-10절 혼합
  → 4개 문단(1-3 / 4-6 / 7-10 / 11-19) 전부 MSG 유닛에 맞춰 재작성.
- 5장: 8-10절·11-12절이 각각 한 칸씩 밀려 13-15절 결말이 통째로 빠짐
  → 5개 문단(1-2 / 3-7 / 8-10 / 11-12 / 13-15) 재작성, 13-15절 복원.

## 내용 복원 내역 (MSG 대비)

### 1장
- `plot twist`, `unstoppable force` 등 원문 없는 첨가 표현 제거.
  MSG "There'll be no stopping them" 원문 의미로 복원.

### 2장
- MSG 고유 이미지 복원: 말라붙은 가죽(dried leather), 황무지와 뼈(badlands/bones),
  와인-식사/옷 입히기/향유 바르기(wine-and-dine/dress-and-caress/perfume-and-adorn),
  엉겅퀴와 막다른 골목(thistles/dead-end alley), 도시 유행 옷과 보석(city fashions/jewelry),
  란제리와 드레스(lingerie/gowns), 정원과 분수(gardens/fountains),
  쓰레기장과 길 잃은 동물들(garbage grounds/stray animals), 바알 숭배 상세.

### 3장
- 2-3절: 보호막 제거(stripped of security), 종교 없는 위로(without religion),
  하나님 없고 기도 없는 삶(godless and prayerless) 복원.
- 1절: MSG 원문 "love the Israelite people" 정확히 반영 (completeness).

### 4장
- 4개 문단 전부 MSG 유닛(1-3 / 4-6 / 7-10 / 11-19)에 맞춰 재작성.
  거짓말·살인·도둑질·간음 고발, 제사장의 멍청함, 하나님을 잊은 어머니 비유 복원.

### 5장
- 13-15절 결말 복원 (앗수르 대왕에게 도움 청하기, 하나님이 자리를 지키심,
  고난 중에 하나님을 찾는 백성).
- 창녀의 숨결(prostitute's breath), 오만(arrogance), 사생아 자식(bastard offspring),
  쇼파르/나팔(shofar/bugle), 고름/곪은 상처(pus/oozing sore) 복원.

### 6장
- `on the third day` 복원 ("In a day or two… Then on the third day we'll be right up").
- 아담에서의 언약 위반(covenant at Adam), 붕대(bandages), 종교적 매춘 의미
  (종교 매춘굴 → teen-safe 표현 "religious brothel" 계열) 복원.

### 7장
- 11-12절 누락분 복원 (앗수르·이집트에 구걸, 그물로 잡힘).
- 피 흘리며 몸 베기(bloody self-cutting), 풍향계(weather vane),
  세상 사람들의 조롱(world-opinion ridicule) 복원.
- `bird-brained` / KO `새대가리` 순화 (어리석다는 의미 유지).

### 8장
- lover 비유 복원. KO `엉망통` → `쓰레기 더미`.
- KO 과도 슬랭 정리 (`1도 안 알려줌`, `실화냐`, `따끔하게 혼내줄` 등).

### 9장
- 돼지/오물/진창(pig/filth/mud), `washed his hands` 복원.
- 10-11절: "their beauty dissipated in confusion and clamor" 원문 반영 (completeness).
- EN/KO 문단 수 9개로 정렬.

### 10장
- Beth-arba/벧아르바 (MSG 원문 확인).
- 기브아 반복(Gibeah plus Gibeah), "righteousness ripe for harvest" 복원.
- 7-8절: "Thistles and crabgrass will decorate their ruined altars" 원문 반영 (completeness).

### 11장
- 인간적인 속박(human bondage), "in your very midst" 복원.
- 과도 슬랭 정리 (`gave me a shout-out`, `murder rate is insane`, `hell-bent`,
  `this Baal guy`, KO `떡상` 등).

### 12장
- 이집트와의 내통(inside track with Egypt) 복원.
- 슬랭 전수 정리 (`콩고물`, `참교육`, `까불지 마라` 등 제거).

### 13장
- 종이/연기 비유(paper/smoke), 창자/코요테/까마귀(guts/coyotes/crows),
  `Nah` 첨가 제거, 죽음/무덤을 향한 질문(Death/Tomb questions),
  황폐한 성읍, 임산부 찢김 복원.
- 과도 슬랭 정리 (`God's like, 'Yo'` 등).

### 14장
- 회개의 기도를 배상(restitution)으로 드린다는 표현, "answers and satisfies" 복원.
- 과도 슬랭 정리 (`God's like`, `love them like crazy`, `so over those fake gods` 등).

## EN-KO 정렬 특이사항

- 7장·9장: KO 문단이 EN보다 적었던 것을 EN에 맞춰 추가·정렬 (7장 6문단, 9장 9문단).
- 6장 "third day": EN "on the third day" / KO "셋째 날에는".
- 9장 "dissipated in confusion and clamor": KO "혼란과 아우성 속에 흩어져 버렸지".
- 10장 "Thistles and crabgrass": KO "엉겅퀴랑 바랭이".
- 3장 "the Israelite people": KO "이스라엘 백성".
- 6장 "religious whorehouse": validator를 통과하지만("whore"가 합성어 안에 포함)
  순화 원칙에 따라 teen-safe 표현으로 교체. 뜻(종교적 매춘)은 보존.

## 슬랭 점검

- EN: no cap, plot twist, bird-brained, hell-bent, God's like, love them like crazy,
  gave me a shout-out 등 과도 슬랭·첨가 표현 전수 제거. teen voice는 유지.
- KO: 떡상, 새대가리, 엉망통, 1도 안 알려줌, 실화냐, 따끔하게 혼내줄,
  콩고물, 참교육, 까불지 마라 등 과도 슬랭 전수 제거.
- 욕·저속 표현: profanity 스크리닝(validator) 통과 + 수동 순화.

## 승인 필요 항목

없음. 발견된 모든 누락·오역·EN/KO 불일치는 위와 같이 복원/정렬했고,
merge/split은 스탠딩 승인 규칙(내용 온전·EN/KO 일치·순수 가독성 구조)에 따라
선언 후 진행. 성욱 컨펌 대기 중인 항목 없음.

## 변경 통계 (원본 대비)

- EN: 80문단 중 50문단 수정, 배지 변경 2건 (7장·9장 EN/KO 문단 수 정렬)
- KO: 80문단 중 43문단 수정, 문단 수 변경 2건 (7장 +1, 9장 +2 — EN과 정렬)
- 문단 순서 변경 없음

## 검증 범위와 미확인 경계

- 검증: MSG parsed 66 유닛 ↔ EN/KO 80문단 전수 대조(수동 정독 1-14장 2회),
  validator, completeness_check (잔여 3건 오탐 근거 문서화),
  build_gdocs(VERIFY_DROPPED=0), verify_pairing_content,
  Google Docs API 테이블 수·export-back·제목.
- 미확인 경계: 앱 화면 렌더링은 이번 감사 범위에 포함되지 않음
  (구약은 production 앱에 반영하지 않음).
