# 열왕기상 (1Kings) MSG 전수 감사 기록

- 감사일: 2026-09-24
- 기준: Eugene Peterson 'The Message' 영어 원문 (MSG)
- Repo: ~/workspace/teenz-bible-review
- 대상: fixes/en_1Kings.json, fixes/ko_1Kings.json (전 22장)
- Production 앱 미반영 (원칙)

## MSG 원문 검증

- `gdocs_build/build_gdocs.py`의 `parse_msg_txt` 기준: 22장, 총 373 MSG 유닛
- `msg_work/1kings_ch01.txt`–`ch22.txt` 전부 존재, 총 117,212 bytes
- 비정상적으로 짧거나 누락된 장 없음 → 원문 재수집 불필요

## Baseline

- 수정 전 baseline: /tmp/baseline_en_1Kings.json, /tmp/baseline_ko_1Kings.json (2026-09-24 저장)
- 아래 수정 건수는 baseline 대비 의미 단위 비교 기준

## 주요 복원 내역 (EN)

### ch1
- "Abishag from Shunem" → "Abishag the Shunammite" (MSG 표기 복원)

### ch2 (이름·족보 10곳)
- "Abner and Amasa" → "Abner son of Ner and Amasa son of Jether"
- "Shimei, son of Gera, from Bahurim" → "Shimei son of Gera the Benjaminite from Bahurim"
- "Asking for Abishag for Adonijah?" → "asking that Abishag the Shunammite be given to Adonijah?"
- Joab → "Joab son of Zeruiah"
- Benaiah → "Benaiah son of Jehoiada" (3곳)
- "the sanctuary" → "the sanctuary of God"
- "Achish, the king of Gath" → "Achish son of Maacah, king of Gath"
- "Solomon said," → "Solomon said to Shimei," (화자 명확화)
- 배지 정정: "Benaiah went back and told the king what Joab had said." [31-33]→[30]
  (MSG [30]의 마지막 문장 "Benaiah went back to the king and reported"에 해당)

### ch5
- "best buds" → "close friends", "Yo," 제거
- "your Sidonian crew is lowkey goated at cutting timber"
  → "there is no one like you Sidonians for cutting timber" (MSG 직역 복원)
- "totally hyped" → "delighted", "Shout out to God" → "Blessed be God"
- "Say less" 제거

### ch6
- "bounced from Egypt" → "left Egypt"
- 누락 복원: "in the month of Ziv (the second month)" (MSG [1-6])
- "Lowkey, that's some next-level planning" → "That's some next-level planning"
- "stairs going up to the second and third floors" → "stairs going up to the second floor, then to the third"
- "7.5 feet high" → "seven and a half feet high" (MSG 표현)
- "God hit Solomon up ... 'Yo," → "God gave Solomon a message: 'About..."
- "the Ark of the Covenant" → "the Ark of the Covenant of God"

### ch7
- "his dad was from Tyre" → "his dad was a Tyrian" (MSG [13-14])
- 배지 정정: Succoth/Zarethan 주물 공장 문단 [48-50]→[45-47] (MSG [45-47] 내용)

### ch9
- "lowkey not impressed" → "not impressed"

### ch11 (이름 6곳 + 슬랭 순화)
- "lowkey obsessed" → "obsessed"
- "It wasn't just Pharaoh's daughter" → "Pharaoh's daughter was only the first" (MSG "was only the first" 복원)
- "from Moab, Ammon, Edom, Sidon, and the Hittites" → "Moabite, Ammonite, Edomite, Sidonian, and Hittite women"
- Hadad 문단 전면 재작성: "bury the dead", "six months", "Edomites" 복원 + "stirred up some drama/start beef/Back in the day/bounced/was cool with" 순화
- "He was from Ephraim" → "He was an Ephraimite from Zeredah"
- "Here's the tea" → "Here's why", "the Millo" 복원, "was a beast" → "stood out ... as strong and able"
- "Peep this" → "Listen"
- "goddess of Sidon, Chemosh of Moab, and Molech of Ammon" → "goddess of the Sidonians, Chemosh, god of the Moabites, and Molech, god of the Ammonites"
- "no cap" 제거

### ch12
- "No cap", "lowkey terrible idea" 제거
- "Jeroboam" → "Jeroboam son of Nebat"
- "the house of David"/"David's family" → "the Davidic dynasty" (2곳, MSG 표현)
- "Tell Rehoboam and everyone" → "Tell Rehoboam son of Solomon, king of Judah, and everyone"
- "the Temple in Jerusalem" → "the Temple of God in Jerusalem"

### ch13–22 (이전 라운드 적용분)
- ch13: "ashes" → "offerings" (MSG "holy offerings"), Bethel 복원, "die far from home" 복원
- ch14: "lowkey" 순화, Jeroboam's family/Asherah/four winds/Temple of God 복원
- ch15: 족보 호칭 복원 (Jeroboam son of Nebat, Ben-Hadad son of Tabrimmon son of Hezion, Baasha son of Ahijah), "major L/Bet/lowkey" 순화
- ch16: Jehu son of Hanani, Ethbaal king of the Sidonians, Hiel 희생의 의식적 의미, "lowkey/No cap" 제거
- ch17: "from among the settlers of Gilead", "no cap" 제거
- ch18: 비, 100명 선지자(50명씩 두 동굴), Jezebel의 Baal/Asherah 선지자, "유일한 선지자" 복원
- ch19: "stand at attention" 복원
- ch20: Ben-Hadad 맹세 대상 "the gods" 정정, "strike the first blow" 복원, "trade base" 조정
- ch21: "king of Samaria", "Naboth the Jezreelite" 반복 복원
- ch22: Zedekiah son of Kenaanah, 하늘 군대, Amon/Joash, "puppet prophets", Ahab 방어 체계, Azubah daughter of Shilhi 복원
- ch14/ch17/ch20 잔여 슬랭: "bounced" → "left", "hit him up" → "spoke to him", "was cool with" → "was fine with"

## KO 수정 내역

- 원칙: EN의 문단 수·순서·배지·의미 1:1 반영
- ch1: 배지 [1-2],[3-4] → [1-4],[1-4] (EN과 동일)
- ch2: "아도니야한테 아비삭을 주라고요?" → "아도니야한테 수넴 여자 아비삭을 주라고요?", 배지 [31]→[30]
- ch4: KO 36문단 → 27문단. 관리 명단 중복 조각 9개(K3–K11) 제거, 배지를 EN 구조로 정렬
- ch5: 배지 [1-3],[4-6] → [1-4],[5-6], "완전 절친/완전 신나/알겠음" 톤 조정
- ch6: "진짜 계획이 장난 아니었던 거지" → "계획이 정말 대단했던 거지"
- ch7: KO 33문단 → 18문단. 목록 중복 조각 15개(K14–K22, K26–K31) 제거, 배지 EN과 동일하게 정렬
- ch8: KO 배지 40개를 MSG 단위와 일치하는 EN 배지로 전면 정렬 (내용 순서 동일)
- ch9: 배지 [18-19] → [17-19]
- ch12: KO 20문단 → 19문단. K9+K10(백성들의 외침) 병합, "예루살렘에 있는 성전" → "예루살렘에 있는 하나님의 성전"
- 그 외 EN 복원 지점(KO가 이미 충실했던 ch11 족보·이름 등)은 KO 변경 없음

## Merge / Split 선언

내용 온전 + EN/KO 일치 + 순수 가독성 목적의 구조 차이만 해당. splits 배열에 선언됨.
- ch2: '14', '15-16', '20', '30', '46'
- ch4: '1-2', '7-19', '22-23'
- ch7: '40-45', '48-50'
- ch12: '16-17'
- (그 외 장의 splits도 배지 중복 기준으로 배열에 선언됨)
- merges: 없음

## 기계 검사 결과

- `validate_translation.py`: PASS (22개 장 모두 통과)
- `completeness_check.py`: 13건 FAIL → 전건 정당한 오탐으로 판정, 근거를 `gdocs_build/completeness_fp_1Kings.md`에 기록
  - "the one" 대명사→숫자 1 오탐 4건, "every last one of you" 1건
  - 기도문 God→you 대명사 2건, "Holy of Holies"→"Most Holy Place" 1건
  - 인용구 paraphrase 5건 (repudiate/sanctified, plodded/seethe/cinders, nourished, drunkenly, enthroned/ranged)

## 문서 빌드·업로드

- `build_gdocs.py 1Kings`: 22 tables, 453 rows, VERIFY_DROPPED=0, orphans=0, teen_without_msg=0
- `verify_pairing_content.py`: 453 data rows, 22 tables — PAIRING CONTENT OK
- Google Docs: "열왕기상 (1Kings): MSG + Teen EN + KO"
  - ID: 1ZcxehWVE_fGo6N_8ka33uVLq-AVpeHms9ayB5dGmK8c
  - API table count 22/22, export-back VERIFIED OK
  - 검증 경계: 실제 Docs 웹 렌더링(브라우저 표시)은 미확인

## 수정 건수 (baseline 대비)

- EN: 80개 문단 변경
- KO: 40개 문단 변경 (중복 조각 제거 포함)
- 배지 정정: EN 2건(ch2 [30], ch7 [45-47]), KO 구조 병합 3개 장(ch4/ch7/ch12)

## 승인 필요

- 없음. 내용 누락·오역·EN/KO 의미 불일치는 모두 해소했고, 잔여 13건은 근거 있는 오탐으로 기록함.

## 2nd re-audit (Sep 24)

- MSG 문장 단위 union 검사(68 flags) + 절-단위 숫자 검사 전수 수행. 13건 토큰 후보는 전부 오탐(teen paraphrase로 의미 보존).
- 실제 누락 4건 복원 (KO에는 이미 있었고 EN에만 빠져 있던 케이스 3건):
  1. ch6 idx0 배지 1-6: MSG 6:3 현관 "thirty-foot width" 복원 → EN "It had this cool 30-foot-wide porch stretching across the front, going out 15 feet."
  2. ch12 idx14 배지 22-24: "and anyone else who is around" 복원 → EN "…and everyone in Judah and Benjamin, and anyone else who's around"
  3. ch12 idx18 배지 31-33: "holy New Year festival" 명칭 복원 + "He staffed Bethel with priests from the local shrines he had made." 문장 복원
  4. KO ch6 idx0: "the second month" gloss 복원 → "시브월, 곧 두 번째 달에"
- 구조 검증: STRUCT OK (22장, EN/KO 문단·배지 일치, MSG 절 커버리지 전수)
- 빌드: VERIFY_DROPPED=0, teen_without_msg=0, msg_orphans=0
- DOCX pairing: 복원 4건 전부 PASS
- Google Docs 재업로드: API table count 22/22, export-back VERIFIED OK
