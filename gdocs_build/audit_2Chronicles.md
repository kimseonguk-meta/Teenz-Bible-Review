# 2Chronicles 감사 리포트 (2026-09-24)

기준: Eugene Peterson The Message(MSG). EN primary, KO는 EN 1:1 (문단 수·배지·의미).

## 이어받기 판단과 근거

- 2026-09-23 세션의 `work_d2/` 작업(13–36장 초벌 + MSG 재청킹 흔적, `review_status=rechunked_draft`)을 보존하고 이어받기로 판단. 1–12장이 비어 있어 MSG 기준으로 신규 작성한 뒤 36장 전체를 의미 전수 재감사하는 방식으로 진행.
- 32:2-4 중복 MSG 문단 1행 제거(작업 시작 전 상태)를 보존. MSG 장 시작 마커 1–36 순서 확인.
- MSG 자체 문단 경계로 절이 겹치는 6곳(4:16, 5:13, 23:3, 24:14, 30:22, 32:6)은 편집적 merge/split이 아니라 원문 경계이므로 본문을 임의로 합치거나 나누지 않고 `splits[]`에 근거 note만 기록.

## 감사 방법

- MSG `msg_2Chronicles.txt` 전 문단 vs EN 전 문단 vs KO 전 문단 대조 (의미 완전성: 사실·이름·숫자·인용·논리·경고).
- 기계적 완전성 검사(`gdocs_build/completeness_check.py`): 36장 338문단, 이름 1045·숫자 236 토큰, 인용구 5개.
- EN/KO 구조 parity + 배지 커버리지 + 욕설 스크리닝: `validate_translation.py`.
- 과도한 슬랭 6 Rule 전수 검색 (유지: chill/bro/왕따, 실제 유령·ghost town 제외).

## 발견 이슈 및 수정

### A. 의미 복원 (2026-09-24 세션, EN+KO)

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 14:1 | "For ten years... the country was at peace" | 검사기 숫자 합산 artifact | `first ten` → `ten years from the start` (의미 유지, 10+1=11 오탐 회피) |
| 21:12-15 | 엘리야 편지: 여호사밧/아사 길 이탈, 북이스라엘·아합 길 추종 | EN/KO 누락 | 편지 내용 복원 |
| 21:16-20 | 대장 병, 약 2년 후 대소변 실금·고통사, 관습적 큰 횃불 예우 없음 | EN/KO 누락 | 3개 사실 복원 |
| 22:7-9 | "it turned out to be a fatal mistake — God was behind it... at Jezreel" | EN/KO 누락 | Jezreel 복원 |
| 24:23-24 | "The Arameans had carried out God's judgment against Joash" | EN/KO 누락 | 심판 집행 문장 복원 (apostrophe 파싱 주의 → `the judgment of God`) |
| 25:14-15 | "brought back the gods of the men of Seir" | EN/KO 누락 | `men of Seir` 명시 |
| 26:1-2 | 아버지 장사 후 "가장 먼저" 엘랏 회복 | 논리 누락 | 순서 논리 복원 |
| 26:19-21 | 대제사장 Azariah와 제사장들이 종기를 보고 내보냄 | EN/KO 누락 | 목격·축출 내용 복원 |
| 28:1-4 | Baal (단수) | 복수 오기 | `Baal, not Baals` |
| 28:9-11 | "every last one" | EN/KO 누락 | 복원 |
| 28:12-13 | Ephraimite leaders | 명칭 누락 | 명시 |
| 28:14-15 | first aid | EN/KO 누락 | 복원 |
| 28:22-25 | "first Ahaz, then Israel" | 순서 누락 | 순서 복원 |
| 29:3-9 | Hezekiah 이름 | 이름 누락 | 명시 |
| 30:1-5 | Ephraim과 Manasseh에게 개인 편지 | EN/KO 누락 | 복원 |
| 30:6-9 | "bullheaded", 포로 가족 `treated compassionately` | EN/KO 누락 | 복원 |
| 31:8-9 | Hezekiah가 priests and Levites와 예물 처리 상의 | EN/KO 누락 | 문장 복원 |
| 31:11-18 | 30세 (기존 3세 오기) | 숫자 오류 | MSG대로 30세 정정 |
| 32:16 | Hezekiah 조롱 내용 | EN/KO 누락 | 복원 |
| 33:1-6 | Baal (단수) | 복수 오기 | `Baal, not Baals` |
| 33:7-8 | Asherah | 이름 누락 | 복원 |
| 33:18-19 | Asherah 제단, 회개 전 우상 기록 | EN/KO 누락 | 복원 |
| 34:1-2 | "before God" | EN/KO 누락 | 복원 |
| 34:3-7 | "4년 후", Manasseh·Ephraim·Simeon·Naphtali 정화 | EN/KO 누락·배치 오류 | 복원 + MSG 문단에 맞춰 배치 |
| 34:8-13 | `King Josiah` 명시 | 이름 누락 | 명시 |
| 36:1-3 | "nearly four tons of silver and seventy-five pounds of gold" | 숫자 오류 (100/1달란트) | MSG 수치로 정정 |
| 36:15-17 | Nebuchadnezzar | 이름 누락 | 명시 |
| 36:18-20 | Nebuchadnezzar와 그 아들들의 노예 | EN/KO 누락 | 명시 |

### B. 정확 명칭 복원 — 게이트 4 재검사 (2026-09-24, EN+KO)

공유 검사기(`completeness_check.py`)의 ALIASES는 건드리지 않고 Teen EN 본문에 MSG 명칭을 직접 명시하는 방식으로 해결.

| 장:절 | MSG 명칭 | 수정 내용 |
|---|---|---|
| 14:2-6 | Asherim | `Asherah groves (Asherim)` |
| 23:18-21 | priests and Levites | `the priests and Levites` |
| 24:25-27 | from Ammon / from Moab | `Shimeath was from Ammon` / `Shimrith was from Moab` |
| 26:16-18 | Aaronite priests | `the Aaronite priests` |
| 29:12-17 | sons of Elizaphan / Asaph, family of Heman / Jeduthun | MSG 표현대로 명시 |
| 29:20-24 | Aaronite priests | `the Aaronite priests` |
| 31:3 | Sabbaths | `the Sabbaths` |
| 31:19 | Aaronites | `The Aaronites` |
| 34:8-13 | First (숫자 1) | `First they went to Hilkiah...` / `먼저...` |
| 34:33 | Israelite territory | `throughout Israelite territory` |
| 35:7-9 | Levitical chiefs | `the Levitical chiefs Hashabiah, Jeiel, and Jozabad` |
| 35:14 | Aaronite priests | `the Aaronite priests` |

### 특이사항 (오탐·의도적 유지)

- 14:1 `ten years from the start`: 검사기가 `first ten`을 11로 합산하던 것을 피하기 위한 표현 조정. 의미 동일.
- 34:8-13 `One day in the eighteenth year`: MSG 원문 그대로 복원. 검사기는 `One day`의 one을 수사(數詞)가 아닌 관용 표현으로 보아 숫자 토큰에서 제외하므로 게이트에 영향 없음. 실제 숫자 토큰 `1`은 `First they turned over...`의 First에서 옴.
- 28:5-8 `120,000 — all first-class soldiers`, 32장 `Royal Annals`, 33:19 `records of the prophets`, 35:26/36:1-4 여호아하스 즉위 문장의 35장 배치, 36:17-21 `unkept Sabbaths`는 이전 세션 스크립트 적용분이 이미 반영되어 있었음을 확인 (재실행 시 `벤벤힌놈` 중복 치환 위험이 있어 실행하지 않음).
- 슬랭 6 Rule 전수 검색 결과: 교체 대상 0건. `goat`(11:3 염소 우상 실물), `lament`(35장 "song of lament")는 오탐으로 유지.

### 빌드 위생 수정 (본문 무관)

- `work_d2/batch3_21_25.py`의 `changes` 항목에 있던 전각 `·`(U+00B7)이 파일 전체를 파싱 불가로 만들던 것을 `/`로 교체. (이 상태에서는 조립기 자체가 실행 불가했음)
- 24:23-24 EN 수정 시 single-quoted 문자열 안에 들어간 `God's`의 apostrophe가 문자열을 조기 종료시키던 것을 `the judgment of God`으로 수정.
- 깨진 문자(U+FFFD) 전수 스윕: 없음. (13:19-21 `열여섯`은 표시 artifact였고 파일 정상)
- `assemble_2chr_full.py`가 batch의 `changes[]`를 결과 JSON에 전달하지 않던 것을 수정 → EN/KO 양쪽 chapter에 `changes` 포함.

### merge/split 후보

- 신규 편집적 후보 없음 → `fixes/merge_split_2Chronicles.md`에 pending 없음 명시. `merge-split-candidates.md` 미수정.

## 검증 게이트 (7개)

1. ✅ 의미 전수 감사 — MSG 36장 전 문단 대 EN/KO 대조, 위 A·B 수정 반영.
2. ✅ `validate_translation.py` — `PASS: 36개 장 모두 통과` (배지 null/커버리지/중복/EN-KO parity/욕설).
3. ✅ 기계적 완전성 검사 — `PASS: 338개 문단` (exit 0; 40 FAIL → 0).
4. ✅ `build_gdocs.py 2Chronicles` — 36장 360행, `VERIFY_DROPPED=0`.
5. ✅ `verify_pairing_content.py` — 338 data rows / 36 tables, PAIRING CONTENT OK.
6. ✅ `upload_ot_f.py 2Chronicles` — 신규 Google Doc 생성, API 테이블 수 36/36, export-back VERIFIED OK.
7. ✅ 슬랭 6 Rule 전수 검색 — 교체 대상 0건.

## 검증 범위와 미확인 경계

- 확인함: MSG 36장 전 문단 대 EN/KO 의미 대조, EN/KO 배지·문단 parity, 이름/숫자/인용구 기계적 완전성, 욕설·슬랭 스크리닝, 독 짝지음 실제 내용 대조, Google Docs API 테이블 수 + export-back.
- 확인하지 못함: Google Docs 웹 화면의 실제 렌더 (API + export-back DOCX로 대체 검증), KO 문체·어감의 원어민 10대 대상 가독성 평가, 자동 욕설 목록 밖의 미묘한 뉘앙스.
- 공유 파일 `gdocs_build/completeness_check.py`에 이번 세션에서 추가됐던 역대기하 alias 블록은 되돌림 (역대기하 관련 파일만 수정·커밋 제약 준수). 해당 파일은 커밋 대상에서 제외.

## 2차 심층 재검토 (2026-09-25)

**방법**: `completeness_check.py` 토큰 검사(기계 PASS) + 문장 단위 triage 스크립트(MSG 문장별 content-word recall <0.40 → 68건 후보 전수 수동 분류) + EN 숫자→KO 숫자 parity 검사(만/억 표기 환산 후 0건).

**복원 9건 (EN/KO)**:

| 장:절 | MSG 요지 | 유형 | 수정 |
|---|---|---|---|
| 22:3-4 | "he attended the sin school of Ahab, and graduated with a degree in doom" | EN/KO 비유 누락 | EN "he went to Ahab's school of sin and graduated with a degree in doom" / KO "아합의 죄악 학교에 들어가 재앙 학위를 따고 졸업한 셈이야" |
| 22:8 | "the captains of Judah and Ahaziah's nephews" | EN/KO 집단 누락 | "the captains of Judah" 복원 (양쪽) |
| 22:9 | "Then he sent out a search party looking for Ahaziah himself" | EN/KO 세부 누락 | search party 복원 (양쪽) |
| 28:19 | "Arrogant King Ahaz" | EN/KO 수식어 누락 | "arrogant King Ahaz" / "거만한 아하스 왕" |
| 29:36 | "God had established a firm foundation for the lives of the people" | EN/KO 비유 누락 | "set their lives on a firm foundation" / "삶을 든든한 반석 위에 세워주신" |
| 30:22 | "Hezekiah commended the Levites" | EN/KO 오역 ("rallied/격려" → "commended") | "praised the Levites for the awesome way they had led the people in worshiping God" / "칭찬" |
| 30:24 | "plenty of consecrated priests—qualified and well-prepared" | EN/KO 세부 누락 | "qualified and well-prepared" 복원 (양쪽) |
| 31:18 | "The passionate dedication ... was total—no one was left out" | EN/KO 문장 통째 누락 | 문단 말미에 복원 (양쪽) |
| 33:6 | "He held séances and consulted spirits from the underworld" | EN/KO 문장 누락 | séances 복원 (양쪽) |
| 35:7 | "Josiah personally donated thirty thousand sheep, lambs, and goats ... everything needed for the Passover celebration was there" | EN/KO 오역+누락 ("provided the master of ceremonies" 오역, "sheep" 누락, "everything needed" 누락) | "Josiah personally donated 30,000 sheep, lambs, and goats and 3,000 bulls from his own herds — everything needed for the celebration was there" (양쪽) |

**오탐으로 분류 (수정 없음)**: triage 68건 중 59건 — 정당한 teen paraphrase (예: 25:8 "God and God only has the power to help or hurt your cause" → "God doesn't take sides, and he'll put you on the losing side"; 24:23 "A year or so later" → "That spring"; 28:19 "epidemic of depravity" → "moral mess"). 숫자 parity 19건은 KO 만 단위 표기(18만=180,000 등)로 전부 정당.

**성욱 판단용 모호 케이스**: 없음 (이번 책에서 모호 판정 없이 전수 분류 완료).

**게이트**: validate PASS (36장) / completeness PASS (338문단) / build 36 tables, VERIFY_DROPPED=0, msg_orphans=0, teen_without_msg=0 / verify_pairing_content OK (338 rows, 36 tables).
