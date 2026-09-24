# 요엘 (Joel) MSG 전수 감사 기록

- 감사일: 2026-09-24
- 기준: Eugene Peterson, The Message (MSG) — `msg_Joel.txt` parsed 26 units
- 대상: `fixes/en_Joel.json`, `fixes/ko_Joel.json` (각 3장, 27문단)
- 원칙: TRANSLATION_PRINCIPLES.md 5대 원칙. EN primary, KO는 EN 1:1 반영.
- 상태: validator PASS, build VERIFY_DROPPED=0, pairing OK, Google Docs 업로드·검증 완료

## MSG 원문 품질 검증

- ⚠ 발견 문제: `msg_Joel.txt`가 세정되지 않은 BibleGateway 원시 스크랩
  (JS boilerplate 포함)으로 입고되어 있었음. `parse_msg_txt`가
  boilerplate의 숫자를 장 표지로 오인해 1장 1개 유닛·2장 39개·3장
  절 구간 왜곡으로 파싱됨 (2Kings 19:23-37 결손 사례와 같은 계열의
  소스 품질 문제).
- 근본 수정: 본문 구간(첫 번째 `###` 소제목 ~ "Next Hosea 14Amos 1Next" 내비게이션 직전)만
  추출하고 `### ch1/ch2/ch3` 장 표지를 삽입해 `msg_Hosea.txt`와 동일한 규격으로 세정.
  원본은 `msg_Joel.txt.pre_clean_bak`에 보존.
- 세정 후 `parse_msg_txt`: 26개 MSG 유닛, 3장 모두 존재.
- 장별 절 커버리지 100% (1장 1–20, 2장 1–32, 3장 1–21). 중간 결손 없음.
- 추가 수정: 스크랩 공백 결손 "Judgment ValleyAnd" → "Judgment Valley And"
  (3:2). 다른 `소문자대문자` 연결은 정상(문장 경계 스타일)으로 판정.
- BibleGateway 공개 페이지 표본 대조 (1:1–12 MSG 전 구간) — 캐시와 정확히 일치.

## 기계 검사

- `validate_translation.py`: **PASS — 3개 장 모두 통과** (수정 후 재통과)
- `completeness_check.py` (EN): 최초 4건 FAIL → 복원 후 3건.
  잔여 3건은 전부 오탐으로 판정, 근거는 `gdocs_build/completeness_fp_Joel.md`.
  (진짜 누락 1건: ch2 p5 "consecrate the congregation" — KO에는 있었으나
  EN에 없어 복원)
- `build_gdocs.py Joel`: teen_ch=3, msg_chapters=3, rows=27, msg_units=26,
  teen_without_msg=0, msg_orphans=0, **VERIFY_DROPPED=0** (ALL VERIFY OK)
- `verify_pairing_content.py`: 27 data rows / 3 tables — PAIRING CONTENT OK
- Google Docs: 신규 문서 생성 (ID `1DrXxje1viaiW3QyWDXFKJJxa30Ffs4yD6eumplwuaNc`),
  API 테이블 3개, export-back VERIFIED OK,
  제목 `요엘 (Joel): MSG + Teen EN + KO`
- 업로드 기록: `gdocs_build/upload_results_workerA.json`에 Joel 항목 기록됨
  (⚠ minor-prophets wave는 upload_ot_a.py 사용 — 결과 파일은 workerA이며,
  작업 지시의 workerF 파일이 아님. Hosea도 workerA에 기록되어 있음.)

## 배지 수정 (seed 오류, 1건)

- 2장 문단 1 배지 `5-6` → `4-6` (EN/KO 동일). 문단 본문이 MSG 2:4
  ("The locust army seems all horses—galloping horses")를 렌더링하는데
  시드 배지가 2:4를 빠뜨리고 있었음. build의 PAIRING_MISMATCHES=1 경고를
  해소. build/validator 재통과.

## EN 본문 수정 (7건)

| # | 위치 | 내용 |
|---|---|---|
| 1 | 1장 문단 2 | MSG 1:4 메뚜기 4종 명칭 복원 — chewing/gobbling/munching/chomping locust가 "Whatever one type of locust"로 일반화되어 있었음. |
| 2 | 1장 문단 3 | "Your supply of booze is cut off. You're on the wagon, like it or not"의 "like it or not" 복원. |
| 3 | 1장 문단 4 | "Weep like a young virgin dressed in black"의 "dressed in black" 복원. |
| 4 | 1장 문단 7 | "Who needs them? The crops have failed!" 수사 의문문 복원. |
| 5 | 2장 문단 0 | "A black day! A Doomsday! Clouds with no silver lining!"의 "clouds with no silver lining" 이미지 복원. |
| 6 | 2장 문단 5 | **누락 복원**: "Consecrate the congregation" (MSG 2:16). KO에는 이미 있었음. |
| 7 | 2장 문단 8 | MSG 2:25 메뚜기 4종 명칭을 KJV식(swarving/hopping/stripping/cutting)에서 MSG식(savage/deadly/fierce/of doom)으로 교체. |
| 8 | 3장 문단 0 | **오역 수정**: "all the nations that don't mess with me" → "all the godless nations" (MSG 3:2). 정반대 의미로 번역되어 있었음. |
| 9 | 3장 문단 1 | 과도한 슬랭 "no cap" 제거 ("guaranteed"로 교체). |
| 10 | 3장 문단 2 | "Get your act together" (MSG 3:11) 복원. |
| 11 | 3장 문단 6 | **오역 수정**: "the stars are out" → "the stars burn out" (MSG 3:15). 별이 '뜬다'는 정반대 의미였음. |
| 12 | 3장 문단 7 | "Egypt will be reduced to weeds in a vacant lot" 이미지 복원 ("wasteland" 일반화 수정). |

## KO 본문 수정 (5건)

| # | 위치 | 내용 |
|---|---|---|
| 1 | 1장 문단 0 | 고유명사 오기 수정: 브두엘 → 브드엘 (Pethuel). |
| 2 | 1장 문단 2 | MSG 1:4 메뚜기 4종 명칭 복원 (씹는/게걸스럽게 먹는/우적우적/우두둑 먹는 메뚜기). |
| 3 | 1장 문단 8 | 의미 변형 수정: "제발 도와주세요!" → "소리 질러 외칠게요!" (MSG "I pray, I cry out to you"). |
| 4 | 2장 문단 8 | MSG 2:25 메뚜기 4종 명칭 복원 (사나운/죽음의/흉포한/파멸의 메뚜기). |
| 5 | 3장 문단 0 | 비속어 순화: "남자는 창녀랑 바꾸고" → "남자는 매춘부랑 바꾸고" (EN은 이미 "prostitute"로 순화되어 있었음). |

## 구조 선언 (splits/merges)

- 이번 감사에서 새로 선언한 split/merge 없음. 기존 시드 구조(9/10/8 문단,
  배지 26개 유닛 대응)는 MSG 커버리지와 EN/KO 일치가 확인되어 유지.
- 1장 MSG 유닛 1:1-3을 Teen 문단 0(배지 `1`)과 문단 1(배지 `2-3`)로 나눈 것은
  시드 구조이며 build pairing에 의해 정상 매칭 확인됨 — 변경 없음.

## 승인 필요 항목

- 없음. (스탠딩 승인 규칙 조건 (a)(b)(c)를 모두 만족하는 구조 차이도 이번에는 발생하지 않음.)

## 미확인 경계

- Teen 음성(render) 검증: 이번 작업은 텍스트 감사이며, 앱 화면 렌더링은
  구약 수정본이 앱에 반영되지 않는 정책상 별도 확인 대상이 아님.
- KO의 EN 1:1 의미 일치는 전 문단 수작업 대조로 확인 (checker는 EN만 커버).
- MSG 3장 절 번호는 KJV 절 번호 기준(1–21)과 동일하게 표기됨.

---

## 2nd re-audit (Sep 24)

2nd-pass, MSG-원문 기준 3장 27문단 전수 재대조.

### checker 후보 3건 분류 (전부 오탐)
- ch2 idx2 [7-11] name `undaunted` → EN "They're fearless, unstoppable" 의미 보존
- ch2 idx5 [15-17] name `consecrate` → EN "consecrated, set apart for this" 존재
- ch3 idx7 [18-21] name `judean` → "the people of Judah" 존재 (토큰 변형)

### 복원 결과
- MSG 누락 0건. 전 문단 MSG 대비 내용 온전, EN/KO 일치.
- 메타데이터 1건: ch2 msg_ranges idx1 `5-6` → `4-6` 정정 (MSG 유닛 기준, EN/KO).

### 게이트
- STRUCT OK, completeness_check 잔여 3건 모두 오탐
- build: rows=27, teen_without_msg=0, msg_orphans=0, VERIFY_DROPPED=0
- DOCX spot-check: 2장(7-11·28-32), 3장(18-21) 페어링 확인
- Google Docs: 신규 문서 생성 (Joel 미등록이었음), API 테이블 3/3, export-back VERIFIED OK
