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
