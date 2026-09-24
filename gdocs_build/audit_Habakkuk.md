# 하박국 (Habakkuk) MSG 전수 감사 기록

- 감사일: 2026-09-24
- 기준: Eugene Peterson, The Message (MSG) — `msg_Habakkuk.txt` parsed 19 units
- 대상: `fixes/en_Habakkuk.json`, `fixes/ko_Habakkuk.json` (각 3장, 22문단)
- 특이: HEAD의 구(舊) 감사본이 아니라 앱 소스에서 새로 시드한 버전을 감사 대상으로 삼음
  (구 버전은 git history 참조용). 시드본이 이미 구 감사 흔적(완성도 높은 paraphrase)을
  물려받아 있었으나, 이번 감사는 MSG 전수 대조를 처음부터 다시 수행.
- 원칙: TRANSLATION_PRINCIPLES.md 5대 원칙. EN primary, KO는 EN 1:1 반영.
- 상태: validator PASS, build VERIFY_DROPPED=0, pairing OK, Google Docs 업로드·검증 완료

## MSG 원문 품질 검증

- `msg_Habakkuk.txt` (2026-09-22 BibleGateway 캐시): `parse_msg_txt` 파싱 정상.
- 3장 전부 존재: 1장 5유닛(1-17), 2장 10유닛(1-20), 3장 4유닛(1-19). 유닛 수 비정상 장 없음.
- 절 커버리지: 1장 1–17, 2장 1–20, 3장 1–19 — 장 중간 통째 결손 없음, boilerplate 없음.
- 재수집/세정 불필요. `.pre_clean_bak` 생성 안 함.

## 기계 검사

- `validate_translation.py`: **PASS — 3개 장 모두 통과** (수정 후 재통과)
- `completeness_check.py` (EN): FAIL 1건 → 진짜 누락으로 판정, 복원 후 **PASS**
  (Checked 3 chapters, 22 paragraphs, 24 name tokens, 2 number tokens).
  근거는 `gdocs_build/completeness_fp_Habakkuk.md`. 잔여 오탐 0건.
- `build_gdocs.py Habakkuk`: teen_ch=3, msg_chapters=3, rows=22, msg_units=19,
  teen_without_msg=0, msg_orphans=0, **VERIFY_DROPPED=0** (ALL VERIFY OK).
  ※ 최초 빌드에서 PAIRING_MISMATCHES=1 (MSG_SUPERSET: ch2 문단 7 배지 13-14 vs
  MSG 유닛 12-14) — 아래 "배지 수정"으로 해소 후 재빌드에서 경고 소멸.
- `verify_pairing_content.py`: 22 data rows / 3 tables — **PAIRING CONTENT OK**
- Google Docs: 신규 문서 생성 (ID `1nw-CBpfcBrwUj0jb1VUse_iWLQlF1O0PK0VaCdfbO5o`),
  API 테이블 3개, export-back VERIFIED OK,
  제목 `하박국 (Habakkuk): MSG + Teen EN + KO` (Final 없음)
- 업로드 기록: `gdocs_build/upload_results_workerA.json`에 Habakkuk 항목 기록됨.

## 배지 수정 (seed 오류, 1건 — EN/KO 동일)

- 2장 문단 7 배지 `13-14` → `12-14`. 문단 본문이 MSG 2:12
  ("'Who do you think you are— building a town by murder, a city with crime?")
  부터 시작하는데 시드 배지가 2:12를 빠뜨리고 있었음. EN/KO `verseRanges`와
  `msg_ranges` 모두 수정. (Joel 감사 때와 동일한 패턴의 seed 배지 오류)

## EN 본문 수정 (2건)

| # | 위치 | 내용 |
|---|---|---|
| 1 | 3장 문단 5 | "Counting on God's **plan** to win in the end" → "Counting on God's **rule** to win in the end". MSG 3:19 "Counting on God's Rule to prevail"와 직접 대응. KO는 이미 "하나님의 다스림이 결국 이길"이라 EN/KO 1:1 해소. |
| 2 | 3장 문단 4 | "They were **scattered everywhere**" → "They were **scattered to the four winds**". MSG 3:14 "Scattered they were to the four winds—" 이미지 복원 (completeness number 토큰 FAIL 해소). KO "사방으로 흩어져서"와 1:1 일치 유지. |

## EN/KO 1:1 대조

- 문단 수 3장 전부 6/10/6 vs 6/10/6 일치, 순서·배지 일치 (수정 후 validator PASS).
- 의미 1:1: 고유명사(Teman, Mount Paran, Cushan, Midian, King Wicked, Lebanon,
  God-of-the-Angel-Armies→LORD of Heaven's Armies / 만군의 주 하나님) 전부 일치.
- 표제 문단(1장 문단 1, 3장 문단 1, 3장 문단 6)도 EN/KO 동일 처리.

## 스탠딩 승인 규칙 적용 (merges/splits 선언)

- 선언 없음. 시드본의 문단 구조는 이미 MSG와 내용이 온전한 상태였고,
  소제목 리드인 문단(1장 문단 1 등)은 Joel 전례와 동일하게 통상 구조로 취급.
- 2:15-17 "sexual orgies" → EN/KO "술에 취하게 해서 벗은 모습을 보려고"
  순화는 원칙 5(욕·비속어 순화)에 따라 허용, 내용 손실 아님.

## 미확인 경계

- 앱 반영 없음 (구약 수정본은 앱에 반영하지 않는다).
- 독(Google Docs) 화면 렌더는 export-back 검증으로만 확인. 실제 브라우저로
  문서를 열어서 보는 시각 검수는 이 환경에서 불가 → 성욱 확인 필요시 명시.

## 2nd re-audit (Sep 24)

- MSG 문장 단위 union 검사(8 flags) + 절-단위 숫자 검사 + 고유명사/이름 전수 대조 수행.
- 모든 후보는 teen paraphrase로 의미가 보존된 오탐으로 판정 (예: "Brazen in sin"→"so bold in their sin", "Doomsday"→"the end of the world", "Skies are blazing"→"The sky is just blazing").
- 복원 0건. 구조 검증 STRUCT OK (3장, EN/KO 문단·배지 일치, MSG 절 커버리지 전수).
