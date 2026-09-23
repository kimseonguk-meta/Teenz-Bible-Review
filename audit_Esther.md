# Esther 감사 리포트 (작업자 D, 2026-09-23)

## 범위
- MSG: `msg_Esther.txt` 1–10장 전수 대조 (문단 단위)
- EN: `fixes/en_Esther.json` 10장 전수 (전 문단 전문 확인)
- KO: `fixes/ko_Esther.json` 10장 전수 (전 문단 전문 확인)
- 이름 대조: 하만의 열 아들 10명(9:10) MSG↔EN↔KO 일치 확인

## 발견 이슈 및 수정 (총 EN 21건 + KO 20건)

### A. 의미 오류 (심각)
1. **8:11 EN/KO 정정** — MSG: "killing anyone who threatened them or their women and children, and confiscating for themselves anything owned by their enemies"
   (유대인·그들의 처자를 위협하는 자를 죽이고, 원수들의 소유물을 몰수).
   기존 EN: "take the attackers' wives, children, and belongings as spoil" — 적의 처자를 전리품으로 삼는다는 정반대 의미였음. EN/KO 모두 정정.
2. **5:2, 8:3 KO "지팡이" → "홀"** — MSG "gold scepter". EN은 "scepter" 유지, KO만 "금으로 된 지팡이"로 오역. 2곳 정정.
3. **9:22 KO "서로 음식을 나눠 먹고" → "서로 선물을 주고받고"** — MSG "the sending and receiving of presents". 오역 정정.
4. **9:12 KO "대단하네" 삭제** — MSG에 없는 왕의 감탄사 첨가. 삭제.
5. **7:8 EN/KO "went pale/핏기가 싹 가셨대" → "the servants covered Haman's face/신하들이 하만의 얼굴을 가려버렸대"** — MSG는 신하들이 하만의 얼굴을 가리는 장면. 의미 정정.
6. **7:7 EN "he was toast" → "he was finished"**, **7:9 EN "Yo, check it out!" → "Look at this!"** — 슬랭 정리.

### B. 슬랭 6-Rule 정리
- EN: `Ghosted→Rejected`(ch1 타이틀), `flex/flex-fest→showing off/display`, `Glow-Up→Rise`(ch2 타이틀), `vibes with→pleases`, `snitched→told`, `shook→shocked/terrified`(ch4, ch7), `What's up→What do you desire`, `Epic Fail→Humiliation/Downfall`(ch6·7 타이틀), `OMG` 제거, `hater→adversary`(MSG 7:6), `total boss→magnificent`, `lowkey→quietly`
- KO: `썰→얘기`, `플렉스 모드→자랑 모드`, `인스타 감성→화려하게`, `현타→후회`, `뷰티→피부 관리`, `룰→규칙`, `"죽는 거죠 뭐"→"죽는 거예요"`, `타이밍 엄청난→타이밍이 절묘했지`, `대박→(삭제)`, `쪽팔려→창피해서`, `쫄다→벌벌 떨다`, `애들→사람들`(관리 지칭), `인기 짱→인기가 많았고`
- 유지: `chilling`(사용자 허용), `싹 다`( mild 구어, 허용 범위)

### C. 완전성 검사(completeness_check) 후속 수정 17건
- 누락 복원: `one-of-a-kind`(1:7), `King Xerxes's`(1:9, 1:14, 6:2, 8:13), `Persian and Mede officials`(1:18),
  `second thoughts`(2:1), `twelve months`(2:12), `a second harem`(2:14), `On one of the occasions`(2:19),
  `bulletins`(3:13), `a single rule`(4:11), `thirty days`(4:11), `The one exception`(4:11),
  `Haman the Agagite`(8:3), `the bulletins authorizing the plan of Haman son of Hammedatha the Agagite`(8:5),
  `Haman son of Hammedatha`(9:10), `127 provinces of Xerxes' kingdom`(9:30)
- 잔여 5건은 checker artifact로 판단 (아래 별도 기록)

### D. checker artifact (수정 불필요, 근거 있음)
1. ch1 `seething` — 문두 형용사("Seething with anger")를 고유명사로 오인. Teen "fuming"은 유의어.
2. ch1 `xerxes` (16-18) — 왕에게 직접 말하는 화법 "your provinces". 의미 동일.
3. ch1 `medes, xerxes` (19-20) — "Persia and Media"(지명) vs "Persians and Medes"(민족명). 의미 동일. "your presence"도 직접 화법.
4. ch9 `27` — checker가 "thirteenth and fourteenth"를 합산(13+14)하는 버그. Teen은 13th·14th·15th·75,000 개별 표기.
5. ch9 `29` — 동일 버그("fourteenth and fifteenth" → 29). Teen은 14th·15th 개별 표기.

## 구조 (merge/split)
- 병합(merge): 10장 전체에서 0건. validator merge 게이트 PASS.
- 분할(split): 12건, 모두 teen 작성 시점부터 존재하는 구조 → `merge-split-candidates.md`에 E1–E12로 `applied-pre` 기록.
- 배지: null 없음. 분할 문단은 배지 공유 (예: ch7 7-8 → 3문단 모두 배지 7-8).

## MSG 소스 이슈
- `msg_Esther.txt` ch5 9-13에 "invited me…" 문장 1회 중복 (수집 오류). 공식 페이지 대조 후 중복 제거 필요 — 본 감사에서는 teen 텍스트에 영향 없음(teen에 중복 없음).

## 게이트 결과
1. ✅ 의미 전수 감사 (본 문서)
2. ✅ 수정 반영 (EN 18 / KO 19건, changes 메타 기록)
3. ✅ `validate_translation.py` PASS (10장)
4. ✅ `completeness_check.py` — 실질 이슈 0건 (artifact 5건 문서화)
5. ✅ `build_gdocs.py Esther` — 93 rows, VERIFY_DROPPED=0
6. ✅ `verify_pairing_content.py` — PAIRING CONTENT OK (10 tables, 헤더/셀 실측 확인, 8:11 수정본 짝지음 확인)
7. ✅ Google Docs 업로드 — 신규 생성 `에스더 (Esther) — Final: MSG + Teen EN + KO`
   (https://docs.google.com/document/d/1tuVsF6HDNB_s6o9wFI3oVqtrptK_WxgSDeJA4CKW-Lg/edit?usp=drivesdk),
   API 제목 일치 + 테이블 10/10 + export-back 검증 OK (빈 틴 셀 없음, 누락 문단 없음)
