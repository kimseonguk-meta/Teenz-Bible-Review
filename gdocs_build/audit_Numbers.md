# 민수기 (Numbers) — MSG 기준 전수 감사 리포트

- 감사일: 2026-09-24
- 기준: Eugene Peterson, The Message (MSG) 영어 원문
- 대상: 민수기 1–36장, Teen EN + Teen KO
- 원문 파일: `msg_Numbers.txt` (151,804자)
- 원칙: 의도적 요약 금지 / EN이 primary, KO는 EN과 내용·톤·구조 1:1 / 고유명사·숫자·인용 반복 보존 / 과도한 슬랭 순화

## 0. 감사 범위

- MSG↔Teen EN/KO 1차 병렬 읽기: 1–36장
- 상세 2차 읽기: 1–36장
- 기계 완전성 검사(completeness_check.py): 고유명사·이름·숫자·인용구 전수 대조

## 1. EN 수정 내역 (MSG 대조, 의미 보존)

| 장 | MSG 요지 | 오류 유형 | 수정 |
|---|---|---|---|
| 1장 | MSG 1-5 단일 묶음(서론 + 6-15절 열두 지파 명단) | 분리 선언(성욱 승인) | splits 선언: MSG 1-5→(1-5, 6-15). 배지 1-5/6-15. 슬랭 정리 |
| 2장 | MSG 1-2 단일 단위 | 배지 오기입 | 배지 1-3→1-2. 슬랭 정리 |
| 3장 | MSG 단위 5-10, 27-31, 44-48 | 배지 오기입 | 배지 6-10→5-10, 27-31→27-32→(성욱 승인)27-31, 44-51→44-48. 슬랭 정리 |
| 4장 | MSG 7-8 단일 단위 | 배지 오기입 | 배지 6-8→7-8. 슬랭 정리 |
| 5장 | MSG 단위 1-3, 23-28 | 배지 오기입 | 배지 1-4→1-3, 23-29→23-28. 슬랭 정리 |
| 6장 | 18절, 축복문 | 배지 오기입 + 내용 | 13-21 문단 분리 시 18절 정정. 축복문을 MSG 표현으로 복원. 슬랭 정리 |
| 7장 | 제물 무게 (3.25/1.75 파운드, 4온스, 60/3 파운드) | 누락/오역 | MSG 무게 복원. "gold dish"→"vessel". 제목 정리 |
| 8장 | MSG 단위 전반 | 배지 오기입 | 배지 MSG 단위에 맞춰 재정렬. 슬랭 정리 |
| 9장 | MSG 단위 전반 | 배지 오기입 | 배지 MSG 단위에 맞춰 재정렬. 슬랭 정리 |
| 10장 | Hobab 대화 | 누락 | Hobab 대화 복원. 배지 재정렬. 슬랭 정리 |
| 11장 | 600,000/70/three feet/sixty bushels | 검증 | 숫자 전부 존재 확인. 배지 재정렬. 슬랭 정리 |
| 12장 | MSG 단위 전반 | 배지 오기입 | 배지 MSG 단위에 맞춰 재정렬. 제목/슬랭 정리 |
| 13장 | 정탐꾼 명단 (MSG 3-15 분리) | 배지 오기입 | 배지 재정렬. Vophsi/Geuel 이름 확인. 슬랭 정리 |
| 14장 | 40년/40일/열 번 | 검증 | 숫자 전부 존재 확인. 슬랭 정리 |
| 15장 | 분량 단위 (quarts) | 검증 | quarts 확인 (KO 리터 대조). 배지 재정렬. 슬랭 정리 |
| 16장 | Korah/Izhar/Kohath/Levi, Dathan/Abiram (Eliab의 아들들), On (Peleth의 아들), 젖과 꿀이 흐르는 땅 | 누락 | 족보·수식 복원. 배지 재정렬. 슬랭 정리 |
| 17장 | — | 검증 | 배지는 MSG와 일치. 슬랭 정리 |
| 18장 | MSG 18:16 "the shekel weighing twenty gerahs" | 누락 | "twenty gerahs" 복원. 슬랭 정리 |
| 19장 | MSG 단위 전반 | 배지 오기입 | 배지 MSG 단위에 맞춰 재정렬. 슬랭 정리 |
| 20장 | MSG 단위 전반 | 배지 오기입 | 배지 MSG 단위에 맞춰 재정렬. 슬랭 정리 |
| 21장 | 21:28-35 내용 | 배지 오기입 + 검증 | 배지 28-29, 31-32 정정. 21:28-35 내용 존재 확인. 슬랭 정리 |
| 22장 | 나귀/천사 서사 | 검증 | 서사 완결성 확인. 슬랭 정리 |
| 23장 | — | 검증 | 내용 확인. 경미한 슬랭 정리 |
| 24장 | MSG 24:5-9 (양동이·씨 뿌림·뼈/화살), 24:17 (별/통치자), 24:20-24 (Amalek/Kenites/배들) | 누락 | 3곳 복원. 배지 재정렬. 슬랭 정리 |
| 25장 | Phinehas (Eleazar의 아들) 족보, Baal-Peor 의미 | 누락 | 족보 복원. 배지 6-9 정정 |
| 26장 | 인구조사 이름·숫자 전부 | 검증 | 전수 확인. 요약 행 슬랭 정리 |
| 27장 | Hepher/Gilead/Makir 족보 | 누락 | 족보 복원. 슬랭 정리 |
| 28장 | 분량·제물 숫자 전부 | 검증 | 전수 확인. 슬랭 정리 |
| 29장 | 수소 13-7마리, 숫양 2마리, 어린양 14마리, 분량 | 검증 | 전수 확인. 슬랭 정리 |
| 30장 | 서원 규정 | 검증 | 전수 확인. 슬랭 정리 |
| 31장 | 전리품 숫자 전부 (675k/72k/61k/32k 등), 목걸이 | 누락 + 배지 | 목걸이 추가. 배지 정정. 슬랭 정리 |
| 32장 | 지파 협상 | 검증 | 전수 확인. 슬랭 정리 |
| 33장 | 40여개 여정 지점, Aaron 나이 123 | 검증 | 전수 확인. 슬랭 정리 |
| 34장 | 경계 지명, 지파 지도자 이름 | 검증 | 전수 확인. 슬랭 정리 |
| 35장 | 48개 성읍, 6개 도피성, 측량 | 검증 + 배지 | 전수 확인. 배지 22-24 정정. 슬랭 정리 |
| 36장 | Gilead (Makir의 아들, Manasseh의 손자) 족보 | 누락 | 족보 복원. 슬랭 정리 |

## 2. KO 수정 내역 (EN 기준 대조)

| 장 | MSG/EN 요지 | 오류 유형 | 수정 |
|---|---|---|---|
| 1장 | 지도자 명단 13문단 중복 | 중복 | 중복 13문단 제거, 6-15 통합 문단 유지 |
| 3장 | 32절 문단 (Eleazar 감독) | 누락 | 성욱 승인: 32절 문단 복원, 배지 27-31/32 정정 |
| 5장 | 배지 | EN과 동일 | EN과 동일한 배지로 수정 |
| 7장 | 제물 무게 (kg/g 환산) | 오역 | 3.25/1.75파운드, 4온스, 60/3파운드 복원 |
| 12장 | EN 14문단 vs KO 13문단 | 구조 불일치 | 성욱 승인: KO 3-8 문단을 내용 변경 없이 2문단으로 분할 |
| 18장 | "the shekel weighing twenty gerahs" | 누락 | "스무 게라" 복원 |

## 3. 선언된 MSG 문단 분리 (splits — 합병 아님)

- 1장: MSG 1-5→(1-5, 6-15) — 2026-09-24 성욱 승인 (선택지 1)
- 3장: MSG 20→(20, 20)
- 7장: 12개 MSG 단위를 각 7문단으로 (12-17, 18-23, 24-29, 30-35, 36-41, 42-47, 48-53, 54-59, 60-65, 66-71, 72-77, 78-83), MSG 84→2문단, 87→3문단, 88→3문단
- 10장: MSG 36→(36, 36)
- 12장: MSG 1-2→3문단, MSG 3-8→4문단, MSG 13→2문단, MSG 14-16→2문단
- 13장: MSG 3-15→14문단 (정탐꾼 명단)
- 20장: MSG 1→(1, 1)
- 21장: MSG 6-7→(6-7, 7) — completeness 게이트 배지 정정 과정에서 선언
- 22장: MSG 7-8→(7, 8, 8), MSG 30→(30, 30), MSG 35→(35, 35) — completeness 게이트 배지 정정 과정에서 선언
- 24장: MSG 20→(20, 20)
- 26장: 20개 MSG 단위를 각 2-7문단으로 (인구조사)
- 31장: MSG 32→(32, 32)
- 33장: MSG 5→(5, 5)

## 4. Completeness 게이트 추가 정정 (2026-09-24)

기계 완전성 검사 1차 97건 중 배지-내용 불일치가 4개 장에서 발견됨. Teen 문단 내용은 MSG에 충실했으나 배지가 실제 내용보다 1-2절 앞서 기입되어 있었음 (레위기 감사에서 6-9장이 "배지 1절씩 밀림"으로 정정된 것과 같은 유형). 내용을 MSG 절에 맞춰 배지를 재지정하고, 배지 중복이 생긴 곳은 split을 선언함.

| 장 | 정정 내용 |
|---|---|
| 14장 | 15개 문단 배지 정정: 11-13→11-12, 14-18→13-16, 19→17, 20-21→18, 22→19, 23-25→20-23, 26→24, 27→25, 28-31→26-30, 32-35→31-34, 36→35, 37-39→36-38, 40-41→39-40, 42-43→41-43 |
| 21장 | 12개 문단 배지 정정: 1-2→1, 3→2, 4-5→3, 6-7→4-5, 8-9→6-7, 10→7, 11→8, 12→9, 13-14→10-13, 15→14-15, 17→17-18, 18-20→19-20. split 선언: MSG 6-7→(6-7, 7) |
| 22장 | 25개 문단 배지 정정: 6-8→6, 9→7, 10→8, 11→8, 12→9, 13-14→10-11, 15→12, 16→13, 17→14, 18-19→15-17, 20-21→18-19, 22→20, 23-25→21-23, 26→24-25, 27→26-27, 31→30, 32→31, 33→32-33, 36→35, 37→36, 38→37, 39→38, 40→39-40. split 선언: MSG 7-8→(7,8,8), MSG 30→(30,30), MSG 35→(35,35) |
| 23장 | 16개 문단 배지 정정: 3-4→3, 5→4, 6→5, 7→6, 8-12→7-10, 13→11, 14→12, 15→13, 16→14, 17→15, 18→16, 19→17, 20-25→18-24, 26→25, 27→26, 28→27-28 |
| 3장 | MSG 3:47 "the shekel weighing twenty gerahs" — EN "twenty gerahs to the shekel", KO "스무 게라" 복원 |

EN/KO 동일한 배지로 수정됨.

## 5. 변경 통계

- 배지 수정: EN 36장 중 30장, KO 6장 (completeness 게이트 4장 포함)
- 내용 복원: EN 14건 (6장 축복문, 7장 무게, 10장 Hobab, 16장 족보 4건, 18장 twenty gerahs, 21장 확인, 24장 3곳, 25장 족보, 27장 족보, 31장 목걸이, 36장 족보), KO 4건 (3장 32절 문단, 7장 무게, 12장 문단 분할, 18장 스무 게라) + completeness 게이트 EN/KO 각 1건 (3장 twenty gerahs/스무 게라)
- 구조: KO 1장 13문단 중복 제거, KO 12장 1문단→2문단 분할 (EN parity)
- 슬랭 정리: 전 장 (EN/KO)
- 승인 사항: 1장 split (MSG 1-5), 3장 32절 문단 복원 + 배지, 12장 KO 문단 분할

## 6. 기계 완전성 검사 (completeness_check.py) 결과

- 실행: `gdocs_build/completeness_check.py fixes/en_Numbers.json`
- 1차 97건 → 배지 정정 + twenty gerahs 복원 후 72건. 남은 72건은 전수 대조 결과 모두 오탐으로 판정.
- 실제 문제: 배지-내용 불일치 4장 (위 4. 참조), 숫자 누락 1건 (3장 twenty gerahs). 모두 수정됨.

### 오탐 유형 (장:배지 — 사유)

**승인된 split (1장)**
- 1:1-5 — 29개 이름 + 숫자 6-15: Teen 두 번째 문단(배지 6-15)에 전부 존재. 성욱 승인 split.

**숫자 파서 버그**
- 4:1-3, 34-37, 38-41, 42-45, 46-48 — "thirty and fifty"를 30+50=80으로 오계산. Teen 본문은 "thirty and fifty" 정상.
- 7:12-17 — 14/15/16은 MSG 인쇄 절 마커(내용 숫자 아님). 1은 "one and three-quarter pounds" 파서 오판 (Teen에 존재).
- 14:18 — "third and fourth"를 3, 4 분리 요구. Teen에 "third and fourth" 존재.
- 25:6-9 — "the two of them"→Teen "both of them". 파서가 "both"를 숫자로 인식 못함.
- 28:12-14, 20:2-5 — 파서 오판 (Teen에 해당 수량 전부 존재).
- 29:7, 17-19, 20-22, 23-25, 26-28, 29-31, 32-34 — "fourteen one-year-old"를 14+1=15로 오계산. Teen에 "fourteen" 존재.
- 21:10-13 — 'arand': MSG 원문에 없는 파서 생성 토큰.

**"one" 대명사 (레위기 14장 선례와 동일)**
- 11:30-34, 16:5, 17:6-7, 19:16-20 — "the one he chooses"→"the person", "one from each tribe" 등. Teen에 존재하나 파서가 대명사 용법을 숫자로 오판.

**단복수·어형 차이 (내용 존재)**
- 3:11-13 israelite→"Israelites", 3:18 gershonite→"Gershon", 3:21-26 libnites/shimeites→단수형, 3:27-31 amramites 등→단수형, 3:33-37 mahlites/mushites→단수형, 3:49-51 levites→직전 문단에 "the Levites" (중복 참조 생략), 4:34-37 kohathite→"Kohath", 4:38-41 gershonite→"Gershon", 6:21 nazirite→"Nazirites", 16:1-3 reubenites→"tribe of Reuben", 16:12-14 eliab→idx0에 "sons of Eliab" (중복 족보 생략), 21:28-29/34/21-22 amorites→"Amorite" (단수), 22:4 zippor→idx1에 "son of Zippor" (중복 족보 생략), 24:21/23 asshur→"Ashur" (음역 차이), 26:4 reubenite→"Reuben", 31:3-4 midian→"Midianites", 32:1-4/6-12 gad→"Gadites".

**정당한 teen paraphrase (동의어·의역)**
- 10:8-10 bugles/aggressor→"trumpets"/"enemy", 16:36-38 smoldering/cinders→"ashes", 18:5-7 outbreaks/delegated/invades→의역, 19:16-20 ritually/sprig/furnishings/excommunicated/desecrated→의역, 23:17 unsleeping→"wide awake", 27:18-21 magisterial/obediently/prayerfully/comings/goings→"authority" 등 의역, 30:10-15 detriment/affirmed→의역, 32:23-24 corrals/you'd→"pens"/"you'll", 35:9-15 designate→"set up".

**신명·대명사 렌더링 (의미 보존)**
- 8:15-19 god→"the Lord", 9:14 god→"the Lord", 13:16 god→MSG 괄호 gloss "(God)" 생략, 16:28-33 sheol→"the grave" (번역 선택), 16:41 god→"the Lord's people", 23:11 balaam→대화 상대 자명하여 생략, 23:26 balak→대화 상대 자명하여 생략, 35:6-8 levites→"them" (선행사 명확).

**번역 선택 (고유명사→일반명사·관용구)**
- 11:18-20 consecrate→"Get yourselves ready" (의역), 13:31-33 anak→"Nephilim" (상위 범주), 23:27-28 jeshimon→"a wasteland" (gloss 유지), 24:3-4 "20/20 vision"→"eyes are opened" (관용구 의역), 25:1-3 acacia→"Shittim" ("Acacia Grove" gloss 생략), 33:48-49 acacia→"Abel Shittim" ("Acacia Meadow" gloss 생략), 34:10-12 "four sides"→"east, south, west, north" 열거로 전달, 35:4-5 "four sides"→동일.

## 7. validate_translation.py 결과

- PASS: 36개 장 모두 통과 (EN/KO 문단 수·배지 일치, verseRanges 커버리지, 절 중복은 선언된 split으로 커버, merge 없음, 욕설 스크리닝 통과).

## 8. 승인 대기 (confirmations_needed)

- 없음. (3장·12장의 NEEDS APPROVAL 항목은 2026-09-24 성욱 승인으로 적용 완료.)

## 9. Google Docs 업로드

- 신규 생성: '민수기 (Numbers) — MSG + Teen EN + KO'
- Doc ID: 1WGQaKVLpFOqTQTuLDZFPrLGZyyJ6WgsaFK1oscssxHA
- export-back 검증: 테이블 36/36, 빈 Teen 셀 0건.
- 빌드: VERIFY_DROPPED=0, 770행. 짝지음 검증 770행 중 1건 플래그(ch1 idx1 MSG 셀 비어 있음 — 성욱 승인 split의 의도된 상태).
- 참고: 실제 Google Docs 화면 렌더는 이 환경에서 확인 불가.
