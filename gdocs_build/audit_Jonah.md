# Jonah 감사 리포트 (Sep 24 — 27권 전수 감사)

기준: Eugene Peterson The Message(MSG). EN primary, KO는 EN 1:1.
절대: 구약 수정본은 앱에 반영하지 않음 (문서 감사만).
(2026-09-23 작업자 A 구 감사 기록은 git history에 보관. 이번 감사는 확립된 절차대로 앱 소스 재시드본 + MSG 기준 전수 재감사.)

## MSG 원문 품질 검증
- `msg_Jonah.txt` (2026-09-22 BibleGateway 캐시): 56줄, `parse_msg_txt` 파싱 → 30 MSG 유닛.
  - ch1: 14유닛 (1-2, 3, 4-6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17) — 절 커버리지 1–17 완전.
  - ch2: 2유닛 (1-9, 10) — 기도 시편 한 덩어리 + 물고기 토출. 절 1–10 완전.
  - ch3: 6유닛 (1-2, 3, 4, 5, 6-9, 10) — 절 1–10 완전. (왕의 회개 6-9가 MSG에서 한 유닛)
  - ch4: 8유닛 (1-2, 3, 4, 5, 6, 7-8, 9, 10-11) — 절 1–11 완전.
- boilerplate (`passage-text">` 잔재)는 파서에서 제외됨. 의심 구간 없음 → 재수집/재조립 불필요.

## 시드 상태 (감사 전)
- `fixes/en_Jonah.json` / `fixes/ko_Jonah.json`: 앱 소스에서 재시드 (HEAD의 구 감사본은 참조용 — `§` 소제목 문단 포함, 현재 시드 구조와 상이).
- baseline validator FAIL 2건: ch2 EN 3문단 vs KO 4문단 불일치 (+배지 불일치).

## 발견 이슈

### 실제 수정 3건 (본문 내용 복원 0건 — MSG 대비 본문은 온전했음)

| # | 장 | 문제 | 조치 |
|---|---|---|---|
| 1 | ch2 | KO 문단 4개 vs EN 3개. KO에 "기도 내용은 이랬대." 단독 문단 존재 (MSG의 "He prayed:" 해당). EN primary 1:1 원칙 위반 | KO P1(기도 인트로) 제거 → KO 3문단으로 EN과 일치. verseRanges/msg_ranges KO `['1','2-9','2-9','10']` → `['1','2-9','10']`. "He prayed:"는 EN P0의 "prayed"와 중복되는 프레이밍이라 EN도 미보유 — 내용 손실 없음 |
| 2 | ch3 P5 | 배지 `7-9` — MSG 유닛은 {6,7,8,9}(왕의 회개+포고령). v6 내용("왕이 왕좌에서 일어나…")은 본문에 있으나 배지에 6 미포함 → 절 커버리지 누락 표기 | EN/KO verseRanges + msg_ranges `7-9` → `6-9` (본문 변경 없음) |
| 3 | ch4 P6–P8 | 배지 오정렬: P6(하나님의 질문)=9 ✓, P7(요나 대답 "Yeah, I do!")=`10` ✗ (v9 후반), P8(하나님 설교)=`11` ✗ (v10-11) | EN/KO verseRanges + msg_ranges → `['1-2','3','4','5','6','7-8','9','9','10-11']` (본문 변경 없음). v9 split 선언 추가 |

### 오탐 1건 (수정 없음)
- `completeness_fp_Jonah.md`에 문서화. 클래스 F (동의어 치환): ch1 [1-2] "God's **Word**" → EN "with a **message**" / KO "말씀하셨대". 대문자 Word 토큰 오탐, 의미 손실 없음.

### 주요 내용 확인 (MSG 전 문장·이름·숫자·인용구·반복 대조 — 누락 없음)
- ch1: Amittai의 아들 요나, 니느웨/다시스/욥바, 파도, 배 분해, 선원 기도·화물 투하, 요나 꿀잠·선장 4문장, 제비뽑기, 5문 질문, "I'm a Hebrew…", sailors realized, "Throw me overboard…", 노 젓기 실패, "O God! Don't let us drown…", 바다가 잠잠, 예배·제물·서원, 큰 물고기·3일 밤낮 — 전부 온전.
- ch2: 기도 2-9 전 10연(무덤 뱃속/물 무덤/성전 재언급/목 조름/심연/해초/산기슭/영원히 닫히는 문/O God, my God/기도가 성전까지/hollow gods, god-frauds/감사 예배/서원 이행/구원은 하나님께) — 전부 온전. v10 물고기 토출 ✓.
- ch3: 두 번째 부르심, "to the letter", 3일 도시/하루 설교, "In forty days Nineveh will be smashed", 도시 금식·베옷, rich and poor… 명단 전체, 왕의 4동작(왕좌·왕복·베옷·잿더미), 포고령 4항(금식/베옷+부르짖음/180도 회개/폭력 중단), "Who knows? Maybe God will…let us live!", 마음 돌이킴 — 전부 온전.
- ch4: "I knew it…sheer grace and mercy…", "kill me! I'm better off dead!", "What do you have to be angry about?", 동쪽 그늘막, 넓은 잎 나무(화 가라앉음), 벌레·시듦·동쪽 뜨거운 바람·기절, "Plenty of right…angry enough to die!", 120,000 childlike people + innocent animals — 전부 온전.

## 수정량
- EN 본문 변경 0문단, KO 본문 1문단 삭제(기도 인트로). EN/KO 배지 변경: ch3 각 1건, ch4 각 3건.

## split/merge 선언 (스탠딩 승인 규칙 적용 — 승인 요청 없이 선언 후 진행)
모두 (a) MSG 대비 내용 온전, (b) EN/KO 문단·배지·의미 일치, (c) 순수 가독성 구조 차이.
- merge: 0건.
- split 4건 (splits[].paras는 0-based index, EN/KO 동일):
  - ch1: 2건 — 4-6→[2,3] (폭풍 / 배+선원+요나 수면), 7→[4,5] (제비뽑기 제안 / 실제 뽑기)
  - ch2: 0건
  - ch3: 1건 — 3→[1,2] (요나 출발·순종 / 니느웨 규모 묘사)
  - ch4: 1건 — 9→[6,7] (하나님의 질문 / 요나의 대답)

## 게이트 결과
- `validate_translation.py` → PASS: 4개 장 모두 통과.
- `completeness_check.py` → FAIL 1건 = 오탐 문서화 (`gdocs_build/completeness_fp_Jonah.md`), 실제 누락 0.
- `build_gdocs.py Jonah` → rows=35, msg_units=30, teen_without_msg=0, msg_orphans=0, VERIFY_DROPPED=0. ALL VERIFY OK.
- `verify_pairing_content.py Jonah.docx` → checked 35 data rows in 4 tables. PAIRING CONTENT OK.
- 욕설 스크리닝: validator 내장 검사 통과 (욕·비속어 없음. teen 슬랭 "freaking out", "chokehold", "lowkey" 등은 비속어 아님).

## Google Docs 업로드
- `upload_ot_a.py Jonah` → OK. 제목: `요나 (Jonah): MSG + Teen EN + KO` (Final 없음). API title_ok=True, tables 4/4, export-back VERIFIED OK.
- `gdocs_build/upload_results_workerA.json` 기록 확인됨 (id 1eDnb7KIkJKb_84g9KGwUbYQJiDtWm5Xi4MbIyFxcdgg).

## 승인 필요 항목
- 없음.

## 검증 범위 vs 미확인 경계
- 검증됨: MSG↔EN 전 문장 대조(4장 30유닛 전수), EN↔KO 1:1(문단·배지·의미), validator/완전성/빌드/페어링/독 업로드+export-back.
- 미확인: Google Docs 웹 렌더링 화면은 이 환경에서 직접 보지 못함 — export-back 자동 검증으로 대체. 앱 반영은 의도적으로 하지 않음 (구약).
