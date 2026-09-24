# 학개 (Haggai) MSG 전수 감사 기록 (2026-09-24, 27권 감사)

- 감사일: 2026-09-24
- 기준: Eugene Peterson, The Message (MSG) — `msg_Haggai.txt` parsed 22 units
- 대상: `fixes/en_Haggai.json`, `fixes/ko_Haggai.json` (각 2장, 30문단)
- 특이: HEAD의 구(舊) 감사본(2026-09-23, 작업자 A)이 아니라 앱 소스에서 새로 시드한 버전을
  감사 대상으로 삼음 (구 버전은 git history 참조용; 구 `audit_Haggai.md` 1차 기록은 이 파일로 대체).
  시드본은 완성도 높은 paraphrase였으나, MSG 전수 대조에서 이름·세부·4연타 병렬문장 누락 다수
  확인되어 복원. 구 감사에서 이미 수정됐던 2:9 'wholeness' 등은 시드본에 다시 사라져 있었음 —
  앱 시드가 구 감사본을 덮어쓴 구조이므로 이번 감사는 처음부터 전수 재수행.
- 원칙: TRANSLATION_PRINCIPLES.md 5대 원칙. EN primary, KO는 EN 1:1 반영.
- 소제목(§) 컨벤션: fixes JSON에는 소제목 행 없음 (27권 감사 컨벤션 — 빌더가 MSG에서 독에 삽입).
- 상태: validator PASS, build VERIFY_DROPPED=0, pairing OK, Google Docs 업로드·검증 완료

## MSG 원문 품질 검증

- `msg_Haggai.txt` (2026-09-22 BibleGateway 캐시): `parse_msg_txt` 파싱 정상.
- 2장 전부 존재: 1장 10유닛(1–15), 2장 12유닛(1–23). 유닛 수 비정상 장 없음.
- 절 커버리지: 1장 1–15, 2장 1–23 — 장 중간 통째 결손 없음, boilerplate 없음.
- 재수집/세정 불필요. `.pre_clean_bak` 생성 안 함.

## 기계 검사

- `validate_translation.py`: **PASS — 2개 장 모두 통과** (수정 후 재통과)
- `completeness_check.py` (EN): FAIL 1건 (`name: word`, ch2 1-3) → 진짜 누락으로 판정,
  "the Word of God" 복원 후 **PASS**
  (Checked 2 chapters, 30 paragraphs, 48 name tokens, 18 number tokens, 1 quoted span).
  근거는 `gdocs_build/completeness_fp_Haggai.md`. 잔여 오탐 0건.
- `build_gdocs.py Haggai`: teen_ch=2, msg_chapters=2, rows=30, msg_units=22,
  teen_without_msg=0, msg_orphans=0, **VERIFY_DROPPED=0** (ALL VERIFY OK).
- `verify_pairing_content.py`: 30 data rows / 2 tables — **PAIRING CONTENT OK**
- Google Docs: 신규 문서 생성 (ID `1ikghBU4QsiTWHbEEb_M2nuACeJ8UikB6p06NH-f9arA`),
  API 테이블 2/2, export-back VERIFIED OK,
  제목 `학개 (Haggai): MSG + Teen EN + KO` (Final 없음)
- 업로드 기록: `gdocs_build/upload_results_workerA.json`에 Haggai 항목 기록됨 (status OK).

## 본문 복원 (EN 14문단 · KO 14문단)

### EN (changes 15건 기록)

1. 1:1 — 'King Darius of Persia', 'Zerubbabel son of Shealtiel', 'Joshua son of Jehozadak' 복원
2. 1:5-6 — 'drinking and drinking and drinking' 3연타 복원, 'rusted-out' 복원
3. 1:9-11 — 'stunting vegetables and fruit' 복원, 'not man or woman' 복원 (KO에는 이미 있었음)
4. 1:12 — 'son of Shealtiel'/'son of Jehozadak' 복원, 'listened, really listened' 반복 복원
5. 2:1-3 — 'son of Shealtiel'/'son of Jehozadak' 복원, 'the Word of God' 복원 (MSG 고유 호칭)
6. 2:5 — 'the word I covenanted' 복원 (promise로 약화돼 있었음)
7. 2:8 — 'I own all the silver/gold' → 'I own the silver, I own the gold' (MSG에 없는 'all' 제거)
8. 2:9 — 'wholeness' 복원 (peace로 오역), 'This new Temple' → 'This Temple' ('new' 제거)
9. 2:10-12 — 'meat that is set apart for sacrifice on the altar' 복원,
   'a loaf of bread, a dish of stew, a bottle of wine or oil' 세부 복원
10. 2:14 — 4문장 병렬 복원 ('Their nation is contaminated' 누락이었음; 'offer me' → 'do for me' 오역 수정)
11. 2:15-17 — 'Think back' 복원, 'the first foundation stones' 복원,
    'half the grain you were used to, half the wine' 구체 수치 복원
12. 2:18-19 — 'Now think ahead from this same date' 복원
13. 2:21-23 — 'from top to bottom' 복원, 'armaments' 복원, 'killing one another' 복원,
    'O Zerubbabel son of Shealtiel, as my personal servant' 복원,
    'the sign of my sovereign presence and authority' 복원,
    'I've looked over the field' 복원, 'The Message of God-of-the-Angel-Armies' 마감 복원
14. 장 전체 — 'the God of the Angel Armies' → 'God-of-the-Angel-Armies'로 통일 (MSG 고유명)

### KO (changes 13건 기록, EN 1:1 반영)

1. 1:1 — '페르시아 다리우스', '스알디엘의 아들 스룹바벨', '여호사닥의 아들 여호수아' 복원
2. 1:5-6 — '마시고 또 마시고 또 마셔도' 3연타 복원
3. 1:9-11 — '만군의 여호와의 메시지'로 통일 (본문은 EN보다 이미 완전했음)
4. 1:12 — '스알디엘의 아들'/'여호사닥의 아들' 복원
5. 장 전체 — '만군의 하나님' → '만군의 여호와'로 통일 (EN 'God-of-the-Angel-Armies' 대응)
6. 2:1-3 — '스알디엘의 아들'/'여호사닥의 아들' 복원, '하나님의 말씀' 복원
7. 2:4 — '여호사닥의 아들' 복원 (EN에는 있었음)
8. 2:5 — '너네랑 맺은 언약의 말씀' 복원 (약속으로 약화돼 있었음)
9. 2:10-12 — '빵 한 덩어리, 국 한 그릇, 포도주나 기름 한 병' 세부 복원
10. 2:14 — 4문장 병렬 복원 ('나를 위해 하는 것'으로 수정 — 바치는 것이 아님)
11. 2:15-17 — '첫 기초석' 복원, '곡식의 절반, 포도주도 절반' 구체 수치 복원
12. 2:21-23 — '무기와 병기' 복원, '내 개인 종' 복원, '내 주권과 권위의 징표' 복원, '밭을 다 둘러보고' 복원

## 스탠딩 승인 규칙 적용

- 선언한 merges/splits: **없음** (구조 변경 없이 본문 복원만으로 완료)
- 승인 필요 항목: **없음**

## 검증 범위 vs 미확인 경계

- 검증됨: MSG 원문 전 유닛(22) ↔ EN 전 문단(30) 전수 대조, EN↔KO 1:1 (문단 수·순서·배지·의미),
  validator/completeness/build/pairing/업로드·export-back 전부 PASS.
- 미확인: Google Docs에서 실제 눈으로 본 렌더링(표 안 한글/영어 줄바꿈) — API 검증은 통과.
  구약 수정본은 앱에 반영하지 않음 (지시).

## 2nd re-audit (Sep 24)
- 기준: MSG 원문 문장 단위 전수 대조 (30문단). completeness_check PASS에 더해 문장별 독립 대조 수행.
- 복원 1건 (EN/KO): ch2 [15-17] "halfhearted efforts at rebuilding the Temple of God" — EN/KO 모두 rebuild 목적어에서 "of God" 누락 → "rebuild the Temple of God"/"하나님의 성전 짓는 거" 복원 (MSG는 "my Temple … the Temple of God"으로 반복하므로 충실히 반영).
- 나머지 29문단은 MSG 문장·이름·숫자·인용·반복 전부 보존 확인 ("Word of God" 1:13 포함).
- 게이트: STRUCT OK, build VERIFY_DROPPED=0 / teen_without_msg=0 / msg_orphans=0, docx pairing 육안 확인, GDocs 2/2 VERIFIED OK.
- 판단 보류(성욱용): 없음.
