# 예레미야애가 (Lamentations) MSG 전수 감사 기록

- 감사일: 2026-09-24
- 범위: 5장 전체 (ch1–ch4 각 22 MSG 유닛, ch5는 MSG 원문 자체가 "5 1-22" 단일 문단)
- 기준: Eugene Peterson The Message(MSG) 원문 — `msg_Lamentations.txt`
- 대상: `fixes/en_Lamentations.json`, `fixes/ko_Lamentations.json` (앱 소스 시드, 미감사 상태 → 감사 완료)
- 이전 기록: Worker E2의 5장 감사 보고서(2026-09-23, 5문단 구조)는 본 전수 감사로 대체됨 (현재 Teen 5장은 8문단)

## 수정 건수

- EN 본문: 33개 문단 수정 (ch1: 6, ch2: 12, ch3: 7, ch4: 4, ch5: 4)
- EN 배지: 2건 정정 (ch4 17번 '20'→'21', 18번 '20'→'22') / KO 배지: 3건 정정 (ch4 6번 '7'→'7-8', 11번 '12-13'→'13', 19번 '21-22'→'22') + msg_ranges EN/KO 각 3건 동일 정정
- KO 본문: 22개 문단 수정 (ch1: 6, ch2: 6, ch3: 2, ch4: 4, ch5: 5 — EN 복원에 대한 1:1 반영 + 슬랭/해석 정정)
- KO 슬랭·해석 정정: '꿀땅'→'소중한 땅', '빌붙기'→'팔아넘김', '맷돌 가는 고된 일'(MSG에 없음)→'여자들이 하던 일'

## 주요 복원 내용 (장:내용)

- 1장: '과부가 된 도시'(1절), '시온의 길이 운다'(4절), '딸 시온' 호칭(6절), '비웃고, 또 비웃었다' 반복(7절), 인용문 'Worthless, cheap, abject!'(11절 — 장 제목과 일치), 'Judgment Day'(21절)
- 2장: '딸 시온/딸 유다' 호칭(1·5·8·10절), '야곱'(3절), '안식일'(6절), '내장이 젤리처럼'(11절), 인용 호칭 'Most Beautiful'/'Best Place to Live'(15절), 인용문 'Here it is!'(16절), '회개하는 시온'(18절), '주님 자신의 성전'(20절), 'gone, gone, gone' 3연 반복(22절)
- 3장: '손을 잡고 칠흑 어둠으로'(1-3), '관 속에 못 박힌 시체'(4-6), '(계속계속 되뇌며)'(22-24), '가장 높으신 하나님의 법정'(34-36), '세상 나라들의 뒷마당'(43-45 — 'for everyone to see' 추가 해석 삭제), '비가 와서 구덩이가 가득 참'(52-54 — '홍수' 정정), '날마다, 날마다, 날마다' 3연 반복(61-63)
- 4장: '수염은 조각한 돌처럼'(7-8), '누더기' + 인용문 '꺼져! 만지지도 마, 병 옮는다!'(14-15), '눈이 빠지게' + '망보는 사람'(17절), '우스 땅에서' + '벌거벗겨진 채로'(21절)
- 5장: '앗시리아와 이집트에 우리 자신을 팔아넘김'(4-6 — 'make deals' 완화 정정), '노예들이 우리를 다스림'(7-8 — 'our own former slaves' 해석 추가 삭제), '아내들이 강간당함' + '여자들이 하던 일'(11-13), '영광의 왕관' + 'Woe! Woe!'(16-18)

## 스탠딩 승인으로 선언한 merge/split 목록

- ch4 merge 2건 (merges 배열 + confirmations_needed 선언):
  - 6번 문단: MSG 4:7 + 4:8 → Teen 1문단 (배지 '7-8')
  - 12번 문단: MSG 4:14 + 4:15 → Teen 1문단 (배지 '14-15')
  - 근거: (a) MSG 대비 내용 온전 — 합쳐진 양쪽 문단 내용 모두 Teen에 반영됨 (b) EN/KO 문단 수·배지·의미 일치 (c) 순수 가독성 목적 구조 차이
- ch5 split 1건 (splits 배열 선언):
  - MSG '5 1-22' 단일 문단 → Teen 8문단 (배지 1-3/4-6/7-8/9-10/11-13/14-15/16-18/19-22)
  - 근거: (a) MSG 22절 전체 내용이 8문단에 빠짐없이 분배됨 (b) EN/KO 1:1 일치 (c) 기도 흐름상 가독성 목적

## 승인 필요 항목

없음. (내용 누락·오역·EN/KO 의미 불일치·판단 모호 사례 없음 — 발견된 모든 누락은 위 복원 목록대로 teen voice로 직접 복원함)

## 게이트 결과

- `validate_translation.py fixes/en_Lamentations.json fixes/ko_Lamentations.json` → **PASS** (5개 장 모두 통과; 감사 전 ch4 배지 불일치 1건 해소)
- `gdocs_build/completeness_check.py fixes/en_Lamentations.json` → 94문단 중 FAIL 3건, 전수 대조 후 전부 오탐 판정 (근거: `gdocs_build/completeness_fp_Lamentations.md`)
  - ch2 idx1 number '2': 절 번호 라벨 오인식 / ch2 idx21 name 'god': "God's wrath"→"your great anger" 정당한 paraphrase / ch5 idx0 quote 토큰 3개: 장 전체 인용문의 귀속 단위 불일치 (각 토큰은 배지 14-15/16-18 문단에 정상 반영)
- `build_gdocs.py Lamentations` → rows=94, msg_units=89, teen_without_msg=0, msg_orphans=0, **VERIFY_DROPPED=0**
- `verify_pairing_content.py gdocs_build/Lamentations.docx Lamentations` → 94 data rows, 5 tables, **PAIRING CONTENT OK**
- Google Docs 업로드 (`upload_ot_f.py Lamentations`) → 기존 Doc 업데이트 (`1XPly-2mqmpBcIZjqb40_zNuPGMyIdlluf208rCADQEg`), API 테이블 수 5/5, export-back **VERIFIED OK**, 제목 `예레미야애가 (Lamentations) — MSG + Teen EN + KO` 유지 확인 (Final 없음)

## 검증 범위 vs 미확인 경계

- 검증됨: MSG 원문 ↔ Teen EN 전 문장·이름·숫자·인용구·반복 요소 대조 (5장 94문단 전수), EN↔KO 1:1 구조·의미 일치, validator·completeness·빌드·pairing·업로드 게이트 전부 통과
- 미확인: 실제 Google Docs 화면 렌더링 (이 환경의 브라우저 제한 — 성욱이 직접 문서 열어 표 5개와 내용 확인 필요), production 앱 미반영 (구약 수정본은 앱에 반영하지 않음 — 원칙 준수)
