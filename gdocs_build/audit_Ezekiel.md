# 에스겔 (Ezekiel) 감사 보고서 — MSG 기준 전수 검수

**날짜:** 2026-09-24
**기준:** Eugene Peterson, The Message (MSG) 영어 원문
**범위:** 에스겔 48장 전체 (EN 567문단, MSG 512 유닛)

## 수정 통계

### 배지 (verseRanges / msg_ranges) 수정
- **EN:** 177개 문단의 배지 수정 (354개 필드: verseRanges + msg_ranges)
- **KO:** 177개 문단의 배지 수정 (354개 필드)
- **사유:** 기존 배지가 MSG 문단 단위와 systematically 어긋나 있었음. 예: ch7은 [1-2,3-5,6-10...]이었으나 실제 MSG 유닛은 [1-4,5-9,10-13...]. 37개 장에서 배지 shift 발견 및 수정.

### 본문 수정
- **EN:** 5개 문단
  - ch11[0]: "Jaazaniah and Pelatiah" → "Jaazaniah son of Azzur and Pelatiah son of Benaiah" (MSG 이름 복원)
  - ch27[12]: "sheiks from Kedar" → "Bedouin sheiks of Kedar" (MSG "Bedouin" 복원)
  - ch37[6]: "Come from all over" → "Come from the four winds" (MSG 관용구 복원)
  - ch39[7]: "the best of the best" → "the best grain-fed animals from Bashan" (MSG "Bashan" 복원)
  - ch46[0]: "locked on workdays" → "locked on the six workdays" (MSG "six" 복원)
- **KO:** 1개 문단
  - ch11[0]: "야아사냐랑 블라댜" → "앗술의 아들 야아사냐와 브나야의 아들 블라댜" (EN과 일치)

### 구조 선언 (splits)
- **51개 split** 선언 (EN/KO 동일)
- 하나의 MSG 유닛이 여러 Teen 문단으로 나뉜 경우, 각 문단에 전체 MSG 범위 배지를 부여하고 splits에 선언
- 예: ch28 [1-5]를 2개 문단으로 분할, ch31 [18]을 3개 문단으로 분할, ch48 [35]를 3개 문단으로 분할

## 주요 복원 내역 (장별)

- **ch1:** EN[9] 배지 [28]→[25-28] (MSG [25-28] 분할)
- **ch3:** 배지 커버리지 수정 (23-27절 누락 경고 해결), Tel Abib→Tel Aviv
- **ch7:** 전체 배지 재매핑 ([1-4,5-9,10-13,14-16,17-18,19-27])
- **ch8:** EN[0-2] 배지 수정 ([1-4],[5],[6])
- **ch9:** EN[4-7] 배지 수정 (분할 구조 반영)
- **ch11:** 이름 복원 (son of Azzur, son of Benaiah)
- **ch12:** EN[8,9] 분할 선언 [23-25]
- **ch16:** EN[9-21] 13개 문단 배지 shift 수정
- **ch17:** EN[0,1] 분할 [1-6], EN[5-9] shift 수정
- **ch18:** EN[4] 배지 [14-17]→[14-18] (MSG [17-18] 내용 포함 확인)
- **ch19:** EN[0,1] 분할 [1-4], EN[4]→[10-14]
- **ch20:** EN[2-18] 17개 문단 배지 shift 수정, EN[12,13] 분할 [30-31], EN[16,17] 분할 [36-38]
- **ch21:** EN[3,4,5] 3-way 분할 [8-10], EN[14,15] 분할 [28-32]
- **ch22:** EN[2] 분할 [6-12], EN[4-8] shift 수정
- **ch23:** EN[1] 분할 [1-4], EN[8,9,10] 3-way 분할 [31-34]
- **ch24:** 전체 배지 재매핑 (4개 분할 포함)
- **ch25:** EN[0,1] 분할 [1-5]
- **ch26:** EN[1] 분할 [1-2], EN[2,3] 분할 [3-6], EN[6,7] 분할 [16-18]
- **ch27:** EN[0,1] 분할 [1-9], "Bedouin" 복원
- **ch28:** 전체 배지 재매핑 (4개 분할)
- **ch29:** EN[0,1] 분할 [1-6], EN[2]→[6-9]
- **ch30:** 전체 배지 재매핑 (4개 분할)
- **ch31:** EN[0,1] 분할 [1-9], EN[5,6,7] 3-way 분할 [18]
- **ch32:** EN[1] 분할 [1-2], EN[2,3] 분할 [3-10], EN[4,5] 분할 [11-15], EN[7,8] 분할 [17-19]
- **ch33:** EN[7]→[17-19], EN[8]→[20], EN[13]→[27-28]
- **ch34:** EN[7]→[25-27], EN[8]→[28-29], EN[9,10] 분할 [30-31]
- **ch35:** EN[0,1] 분할 [1-4]
- **ch37:** EN[1,2] 분할 [3], "four winds" 복원, EN[13]→[24-27]
- **ch38:** EN[2]→[10-12]
- **ch41:** EN[1] 분할 [1-2], EN[5-9] shift 수정
- **ch43:** EN[5]→[13-14], EN[6]→[14-15], EN[8] 분할 [16-17], EN[12]→[25-26], EN[13]→[27]
- **ch45:** EN[3]→[7-8], EN[4]→[9-12]
- **ch46:** "six workdays" 복원
- **ch47:** EN[2,3] 분할 [6-7], EN[8,9] 분할 [15-17]
- **ch48:** EN[0,1] 분할 [1], EN[8]→[8-9], EN[9]→[10-12], EN[13]→[21-22], EN[14,15] 분할 [23], EN[26,27,28] 3-way 분할 [35]

## 스탠딩 승인으로 처리한 merge/split
- 51개 split 전부: (a) MSG 대비 내용 온전, (b) EN/KO 일치, (c) 가독성 목적의 순수 구조 차이 → 선언 후 진행
- Merge 없음 (Teen이 MSG 유닛을 합친 경우 없음)

## 승인 요청 항목
- **없음.** 내용 누락·오역·EN/KO 불일치는 모두 위에서 복원 완료.

## False Positive 기록
`gdocs_build/completeness_fp_Ezekiel.md`에 기록:
- "god" → "GOD"/"Lord" (대소문자/호칭 차이)
- 숫자 단어 변환 ("six" vs "6", "forty" vs "40")
- Teen-friendly paraphrase ("disgusting things" for "obscenities", "trash the Temple" for "desecrate")
- 분할 배지 페어링 아티팩트 (intro 문단만 검사기에 걸림)

## 게이트 결과
- ✅ `validate_translation.py`: PASS (48개 장 모두 통과)
- ✅ `build_gdocs.py`: 48 tables, 567 rows, 512 MSG units, VERIFY_DROPPED=0, orphans=0
- ✅ `verify_pairing_content.py`: PAIRING CONTENT OK (567 rows)
- ✅ Google Doc 업로드: 기존 문서 업데이트 성공 (1KlzFNz99jYhYusNHSzlE5Hx5Ss5KjH8oqM7XEJh6n-4)
- ✅ 문서 제목: "에스겔 (Ezekiel): MSG + Teen EN + KO" (기존 유지)

## 검증 범위 vs 미검증 경계
- **검증됨:** 48장 전체의 배지-MSG 유닛 정합성, 51개 분할 구조, EN/KO 문단 수·배지 일치, completeness checker 52개 이슈 중 genuine 5건 복원
- **미검증:** 각 문단의 문장별 세부 대조 (567문단 전체를 문장 단위로 수작업 대조하지는 않음. completeness checker의 이름/숫자/인용구 검사가 1차 스크리닝 역할을 함)
