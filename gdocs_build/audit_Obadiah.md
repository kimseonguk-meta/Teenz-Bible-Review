# Obadiah 감사 리포트 (2026-09-24, 27권 감사)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. EN primary, KO는 EN과 문단 수·순서·배지·의미 1:1. KJV는 후보 선별용. 구약 수정본은 production 앱에 반영하지 않음.

## 감사 방법
- MSG 원문 품질 검증: `parse_msg_txt`로 1장 5개 MSG 유닛 파싱 (1 / 2-4 / 5-14 / 15-18 / 19-21), 21절 전부 커버, boilerplate 0건. 재조립 불필요.
- MSG ↔ EN 전수 대조: 5개 문단 전부 직접 대조. **시드(앱 소스 재시드)가 압축·생략한 요소 대량 발견 → 5개 문단 전부 복원 수준 재작성.**
- § 헤더 "Your World Will Collapse": 27권 클래스 규칙(배지 off, teen 문단 미생성) 적용 — teen 문단으로 만들지 않음.
- EN 수정 후 KO를 EN에 1:1로 반영. 시드는 KO가 6문단(1절을 2문단으로 분할)이었으나 EN이 5문단이므로 KO P1+P2 병합 → 5:5 parity.

## 발견 이슈 (실제 누락/오역 — 전부 수정 완료)

### 1절
- "Obadiah's Message to Edom from God, the Master" superscription 누락 → "This is Obadiah's message to Edom, from God, the Master." 복원 (Amos 전례와 동일).
- "special messenger" → "A messenger" (special 삭제) → 복원.
- "'On your feet, prepare for battle" → "'Get ready to fight Edom!" (On your feet 누락) → 복원. KO는 "일어나서"를 원래 보유하고 있었음 → EN/KO parity 회복.

### 2-4절
- "the runt of the godless nations, despised" → "the most looked-down-on nation" (runt/godless nations 누락) → 복원.
- "king of the mountain" 누락 → 복원.
- "'Nobody can get to me! Nobody can touch me!'" 중 첫 구절 누락 → 복원.
- "Even if, like an eagle, you hang out on a high cliff-face, Even if you build your nest in the stars" 2개 평행 이미지 모두 누락 → 복원.
- "God's sure Word." → "And that's a promise from God." (유지 가능하나 MSG 표현 그대로 복원).

### 5-14절
- "If they mugged you on the streets at night, they'd pick you clean—isn't that so?" (밤 강도 평행 수사문) 누락 → 복원.
- "they'll take Esau apart, piece by piece, empty his purse and pockets" → "completely wrecked" (구체적 이미지 누락) → 복원.
- "All your old partners will drive you to the edge" → "Your allies will turn on you" (벼랑 끝으로 몬다는 이미지 누락) → 복원.
- "Your old friends will lie to your face" → "betray you" (요약) → 복원.
- "Your old drinking buddies will stab you in the back" 통째 누락 → 복원.
- "when I wipe out all sages from Edom and rid the Esau mountains of its famous wise men" → "get rid of all the wise and powerful people in Edom" — "powerful"은 MSG에 없는 오역, "Esau mountains" 누락 → 복원.
- "Your great heroes will desert you, **Teman**" — 고유명사 Teman 누락 → 복원 (구 감사에서 KO만 보유했던 건).
- "There'll be nobody left in **Esau's** mountains" — Esau's 누락 → 복원.
- "the murderous history compiled against your brother Jacob" → "how you treated your brother" (murderous 삭제) → 복원.
- "You will be looked down on by everyone. You'll lose your place in history." → "You'll be disgraced and forgotten" (압축) → 복원.
- "On that day you stood there and didn't do anything." 누락 (MSG는 "didn't do anything"와 뒤의 "stood there and watched"를 별도 문장으로 반복) → 복원.
- "Strangers took your brother's **army** into exile. **Godless** foreigners invaded and pillaged Jerusalem." → "foreigners attacked Jerusalem and took your brother's people" (Strangers/외국인 병행, army, godless 누락) → 복원.
- "You shouldn't have" 8연속 중 4개 누락 (시드는 1·4·7·8만 압축 보유): ② "laughed and joked at Judah's sons when they were facedown in the mud", ③ "talked so big when everything was so bad", ⑤ "should not have been amused by their troubles, their wrecked nation", ⑥ "taken the shirt off their back when they were knocked flat, defenseless" → 8개 전부 복원. (구 감사가 "7개 항목 각각에 대응 요소가 있어 paraphrase 범위"라고 판정했던 것이 오판 — 실제 4개가 통째로 없었음.)

### 15-18절
- "for all the **godless** nations" → "for all nations" (godless 누락) → 복원.
- "What you did will **boomerang back and hit your own head**" → "It's coming back to hit you" (boomerang 이미지·your own head 누락) → 복원.
- "all the godless nations will **drink God's wrath. They'll drink and drink and drink—they'll drink themselves to death**" → "face God's anger. They'll be completely destroyed." (drink 이미지·3회 반복 누락; 구 감사에서 KO만 보유했던 건) → 복원.
- "there's respite there! a safe and holy place!" → "there will be safety" (respite 누락) → 복원.
- "the family of **Joseph** become fierce flame" 통째 누락 (구 감사에서 KO만 보유했던 건) → 복원.
- "nothing left of Esau but a pile of ashes" → "completely burned up" (재 더미 누락) → 복원.
- "God said it, and it is so." → "God has spoken." (and it is so 누락) → 복원.

### 19-21절
- "take over the **Esau** mountains" → "Edom's mountains" (MSG의 Esau mountains 명칭으로 복원).
- "**Earlier**, Israelite exiles ... to the north at **Zarephath**" — Earlier·to the north 누락 → 복원.
- "Jerusalem exiles from the **far northwest in Sepharad**" — 구 감사가 이미 복원, 유지 확인.
- "The remnant of the saved ... **will go into the mountains of Esau** And rule **justly and fairly**" — 구 감사가 "rule justly and fairly"는 복원했으나 "will go into the mountains of Esau" 이동 표현이 여전히 빠져 있었음 → 복원.

## 주요 복원 (요약)
- 1절: superscription(Obadiah's message to Edom), special messenger, On your feet.
- 2-4절: runt of the godless nations, king of the mountain, 'Nobody can get to me!', cliff-face/nest-in-the-stars 2중 이미지, God's sure Word.
- 5-14절: mugger-at-night 수사문, piece by piece/purse and pockets, drive you to the edge, lie to your face, drinking buddies/stab in the back, sages/Esau mountains, **Teman**, **Esau's** mountains, murderous history, looked down on/lose place in history, stood there and did nothing, Strangers/Godless foreigners/brother's army, **"You shouldn't have" 8연속 전수 복원**.
- 15-18절: godless nations(2회), boomerang back/hit your own head, drink God's wrath + 3회 반복 + drink themselves to death, respite, **Joseph** fierce flame, pile of ashes, God said it, and it is so.
- 19-21절: Esau mountains 명칭, Earlier, to the north, far northwest in Sepharad(유지), go into the mountains of Esau, rule justly and fairly.
- 오역 수정 1건: "wise and **powerful** people" (MSG에 없음) → "all the sages ... famous wise man".
- 욕설/슬랭: 검출 없음.

## 수정량
- EN 본문 5문단 전부 수정 (전면 재작성 수준). 배지: 문단별 verseRanges 5개(1/2-4/5-14/15-18/19-21) 변경 없음, null 0.
- KO 본문 5문단 전부 수정 (EN 1:1 반영) + P1+P2 병합으로 6→5문단 구조 parity. verseRanges 5개 변경 없음.

## split/merge 선언 (스탠딩 승인 규칙 적용)
- merge: 0건. split: 0건. EN/KO 문단 구조가 MSG 유닛(5개)과 이미 1:1이라 선언할 구조 차이 없음.

## 검증 게이트
1. ✅ 의미 전수 감사 — MSG 5유닛(21절) 대 EN 5문단 전수 대조, 누락 20+건 복원.
2. ✅ KO EN 1:1 반영 — 문단 수·순서·verseRanges·의미 parity.
3. ✅ validate_translation.py — PASS (1개 장 모두 통과).
4. ✅ 기계적 완전성 검사 — `completeness_check.py fixes/en_Obadiah.json`: 5문단, 이름 토큰 21개, FAIL 0건. `completeness_fp_Obadiah.md` 불필요 (잔여 오탐 없음).
5. ✅ build_gdocs.py — rows=5, teen_ch=1, msg_chapters=1, VERIFY_DROPPED=0, orphans 0.
6. ✅ verify_pairing_content.py — 1 tables, 5 data rows, PAIRING CONTENT OK (MSG 셀↔Teen 셀 실제 내용 대조).
7. ✅ Google Docs 업로드 — `오바댜 (Obadiah): MSG + Teen EN + KO` (Final 없음), 테이블 1/1, export-back VERIFIED OK. id `1oTijIb0wZTygdOvFnBeNnH7YkkpoEk46w80W7PjtDhY`.
   - https://docs.google.com/document/d/1oTijIb0wZTygdOvFnBeNnH7YkkpoEk46w80W7PjtDhY/edit?usp=drivesdk

## 승인 필요 항목
- 없음. 내용 누락·오역·EN/KO 의미 불일치·방향 모호 사례 없음 (전부 복원 완료).

## 검증 범위 vs 미확인 경계
- 확인함: MSG 파서 출력(5 units) 대 teen EN 전수 대조, EN/KO 문단 수·순서·verseRanges parity, validator, completeness_check(FAIL 0), DOCX export-back 셀 내용 대조, Google Docs 업로드 + API 테이블 수 + export-back 검증.
- 확인하지 못함: KO 본문 5문단 전수 의미 대조 (EN 기준 구조 parity + 스팟체크만 수행), 자동 욕설 목록 밖 미묘한 표현의 뉘앙스, Google Docs 웹 화면의 실제 렌더 (API + export-back DOCX로 대체 검증), production 앱 미접촉 (원칙).

## 생산 반영
- 구약 감사본은 production 앱에 반영하지 않음 (원칙).
