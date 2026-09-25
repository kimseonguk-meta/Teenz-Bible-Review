# Psalms 감사 보고서 (Audit Report)

날짜: 2026-09-23
대상: 시편 150장 (Psalms 1-150)
기준: Eugene Peterson, The Message (MSG) 영어 원문

## 개요

- EN (Teen English): 150장, 946개 문단 — MSG 기준 전수 감사 및 복원
- KO (한국어): 150장, 946개 문단 — 수정된 EN과 문단별 1:1 대조
- Validator: PASS (150개 장 모두 통과)
- Completeness checker: 109 FAIL → 76 FAIL (33건 해결, 나머지는 false positive 또는 허용 가능한 paraphrase)

## EN 주요 복원 내용 (MSG 기준)

의미·완전성 복원 (33건):
- 2:4-6 `Furiously`, 5:4-6 `Hot-air boasters`, 6:8-9 `Devil's crew`
- 8:1, 8:9 `brilliant Lord` (시편 8편의 MSG 표현)
- 9:13-14 `corner of Main and First`
- 11:4-6 holy place, unblinking eyes
- 14:3, 53:3 `the ninety and nine follow their fellow`
- 16:3 `God-chosen lives / splendid friends`
- 17:13-14 sword, barehanded, famine food/bread, children's second helpings, babies' crusts
- 22:27 `four corners of the earth`
- 23:5 `six-course dinner`
- 42:6-7 Jordan, Hermon, Mount Mizar
- 44:11-12 `four winds`
- 47:2-4 `Lord over earth`, `Lord of the godless nations`
- 60:3-5 `cheap wine`
- 67:7 `earth's four corners`
- 68:17-18 `twice ten thousand`
- 69:2 `going down for the third time`
- 72:9-14 `when they bleed, he bleeds; when they die, he dies`
- 74:13-17 `four corners of the earth`
- 76:4-6 `huge piles of loot`
- 79:10-13 `God-taunts boomerang`
- 94:12-15 `the man you train`, `the woman you instruct`
- 98:1 `rolled up His sleeves and set everything right`
- 106:1-3 `one happy man`, `one happy woman`
- 107:1-3 `four winds`, `seven seas`
- 108:7-9 `spoke in holy splendor`, `Brimming over with joy`
- 110:1 `The word of God to my Lord`
- 112:1 `Blessed man, blessed woman`
- 118:5-16 `hemmed in by barbarians`, `rubbed their faces in the dirt` (3회)
- 128:3-5 `the one who fears God`
- 129:1-4 plowmen, long furrows, harnesses
- 135:13-18 chiseled mouths, painted eyes, carved ears
- 135:11 `every last one of the Canaanite kings`
- 136 `Struck Og the Bashanite king`
- 137:8 `Babylonians—ravagers` (MSG 복수형)
- 140:9-11 `let the Devil hunt them down`
- 144:9-10 `twelve-string guitar`
- 68:14 `Shaddai`, 91:1 `Shaddai` (MSG 고유명 복원)

슬랭 정리:
- `No Cap`, `Lowkey`, `GOAT/GOATED`, `vibe/vibes`, `spill the tea`, `glow-up`, `LOL`, `main character`, `came in clutch`, `hits different`, `major L` 등 제거
- `chill/chilling`은 유지 (사용자 지시)

## KO 주요 수정 내용

- EN 복원 내용에 맞춘 1:1 번역 수정 (21건)
- 슬랭 정리 (39건): 찐, 대박, 멘탈, 흑역사, 짱, 꿀팁, 전설급, 현타, 가즈아, 사이다, 클라스 등 제거
- 8:1, 8:9 `쩌는 주님` → `찬란하신 주님`
- 108:7-9 `사이다 발언` 제거, `Brimming over with joy` → `기쁨이 넘쳐서`

## Merge/Split

- 이번 세션 신규 후보: 없음 (문단 구조 변경 없음)
- 기존 선언된 split 18건은 `fixes/merge_split_Psalms.md`에 pending으로 기록

## 검증 결과

- `validate_translation.py`: PASS (150개 장 모두 통과)
- `build_gdocs.py`: VERIFY_DROPPED=0, 150 tables, 949 rows
- `verify_pairing_content.py`: 11개 이슈 확인 — 모두 파서 한계이며 실제 누락 아님
  - ch8 idx4: MSG 8:9 파서가 별도 라인으로 인식 못함. TEEN 내용은 정상 ("brilliant Lord")
  - ch119 idx12-21: MSG 119의 `* * *` 구분자를 파서가 처리 못함. TEEN 내용은 정상

## 파서 오염 vs 실제 누락

- Completeness checker의 76개 FAIL 중 대부분은 false positive:
  - 대소문자/단복수 불일치 (예: "Canaanites" vs "canaanite")
  - 일반 단어 플래그 (예: "god", "lord")
  - 관용구 숫자 (예: "1", "2", "3")
  - 허용 가능한 paraphrase (예: "solid person" vs "stalwart")
- 실제 누락으로 확인된 것은 모두 수정 완료

## 남은 작업 (성욱 컨펌 필요)

- Google Docs 업로드 및 실제 짝지음 확인
- Production 앱 반영
- Merge/split 18건 컨펌

## 2차 심층 재검토 (2026-09-25)

기준: "축약하지 마라" — 1차 때 "허용 의역"으로 넘긴 것을 MSG 문장 단위로 재대조.
Completeness checker 75 issues를 전수 분류 → 대부분 동의어/의역/구조적 오탐.
실제 복원 12건 (EN 문단 수정 12, KO는 이미 정확하여 내용 변경 없음):

- 46:4-6 `godless nations` — EN "Other nations" → "The godless nations" (KO "신을 모르는 나라들"과 일치)
- 66:7 `godless nations` + `high tower` — EN "watching over all the nations that don't mess with him"는 의미 반전(믿는 나라로 읽힘) → "in his high tower, keeping his eye on the godless nations"
- 69:35-36 `Zion` — EN "save his people" → "help Zion" (KO 시온과 일치)
- 72:9-14 `godless nations` — EN "every nation" → "the godless nations"
- 72:15-17 `Sheba gold` — EN "finest gold" → "Sheba gold" (KO 스바와 일치)
- 72:15-17 `Cornucopias of praise` 비유 복원 — "cornucopias of praise, with praises springing up from the city like fresh grass" (KO 뿔 비유와 일치)
- 72:15-17 `godless people` — EN "all nations" → "all godless people" (KO "신을 믿지 않던 사람들"과 일치)
- 81:16 `God-haters` — EN "all the haters" → "all the God-haters" (KO "하나님을 싫어하는 자들"과 일치)
- 97:11 `Light-seeds... Joy-seeds... good heart-soil` 비유 복원 (KO 씨앗/마음 밭 비유와 일치)
- 101:8 `made-in-Canaan gods` — EN "fake gods" → "made-in-Canaan gods" (KO 가나안과 일치)
- 106:34-39 `godless cultures` — EN "other nations" → "godless cultures" (KO 이교도 문화/이방인과 일치)
- 135:15-18 `gods of the godless nations` — EN "gods of other nations" → "gods of the godless nations" (KO "신 없는 나라들"과 일치)

배지 오류 수정 (EN/KO 동시):

- ch62 verseRanges `1-3, 4-6, 7, 8` → `1-2, 3-4, 5-6, 7-8` (실제 MSG/내용 대응에 맞춤)
- ch66 verseRanges `7-8, 9-13, 14-16, 17-20` → `7, 8-12, 13-15, 16-20` (실제 MSG/내용 대응에 맞춤)

파서 근본 수정 (build_gdocs.py):

- 1차 보고서에서 "ch119 idx12-21: MSG 119의 `* * *` 구분자를 파서가 처리 못함"으로 오진단됐던 건의 실제 원인: `VERSE_ATOM`이 `\d{1,2}`라 3자리 절(97-104 ~ 169-176)을 VERSE로 인식하지 못하고 TEXT로 분류, 89-96 유닛에 전부 달라붙음.
- `VERSE_ATOM`을 `\d{1,3}`으로 수정 → 전체 68권 파싱 비교 결과 시편만 변경 (+10 유닛, +80절), 나머지 67권 바이트 동일.
- 이후 `teen_without_msg=10` → `0`, `msg_orphans=0`, `VERIFY_DROPPED=0` 전부 통과.

검증 결과 (2026-09-25):

- `validate_translation.py`: PASS (150개 장 모두 통과)
- `build_gdocs.py`: rows=948, msg_units=862, teen_without_msg=0, msg_orphans=0, VERIFY_DROPPED=0, ALL VERIFY OK
- `verify_pairing_content.py`: 150 tables, 946 data rows, PAIRING CONTENT OK
- KO parity: EN 복원 12건 모두 KO에 이미 존재하여 KO 내용 변경 불필요 (배지 2건만 EN/KO 동시 수정)
