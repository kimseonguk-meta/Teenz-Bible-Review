# 열왕기하 (2Kings) MSG 전수 감사 기록

- 감사일: 2026-09-24
- 기준: Eugene Peterson 'The Message' 영어 원문 (MSG)
- Repo: ~/workspace/teenz-bible-review
- 대상: fixes/en_2Kings.json, fixes/ko_2Kings.json (전 25장)
- Production 앱 미반영 (원칙)

## MSG 원문 검증 및 결손 복원

- `gdocs_build/build_gdocs.py`의 `parse_msg_lines` 기준: 25장, 총 421 MSG 유닛 (복원 후)
- **중대 발견**: 로컬 `msg_2Kings.txt`의 19장이 22절에서 끝나고 20장으로 넘어감. 19:23-37 전체가 결손되어 있었음.
  - 기존 "25장 모두 존재" 검사는 장 단위 존재만 확인하고 장 내부 후반부 누락을 잡지 못했음.
  - 2026-09-24 Bible Gateway The Message 열왕기하 19장 페이지에서 19:23-37 원문 확인 후 복원.
  - URL: https://www.biblegateway.com/passage/?search=2%20Kings%2019&version=MSG
  - 복원 내용: 23-24 (산헤립의 자랑), 25-28 (하나님의 주권 선언), 29-31 (히스기야에게 주는 징표), 32-34 (앗수르 왕의 실패 예언), 35 (185,000명 살해), 36-37 (산헤립의 죽음)
  - `msg_2Kings.txt`에 25-26, 27-28, 29, 30-31, 32-34, 35, 36-37 유닛 추가. 기존 `22` 마커를 `22-24`로 정정 (해당 문단이 23-24 내용 포함).
  - `msg_work/2kings_ch19.txt` 재생성 (16 유닛).
- 복원 후 ch19 MSG 유닛: 16개 (기존 9개에서 7개 추가)

## Baseline

- 수정 전 baseline: /tmp/baseline_en_2Kings.json, /tmp/baseline_ko_2Kings.json (2026-09-24 저장)
- 아래 수정 건수는 baseline 대비 의미 단위 비교 기준
- EN: 186문단 본문 수정, 203건 배지 수정
- KO: 94문단 본문 수정, 220건 배지 수정
- (ch1-18은 이전 세션에서 완료, ch19-25는 본 감사에서 완료)

## 주요 복원 내역 (EN/KO)

### ch19 (MSG 결손 구간 23-37 수동 대조)
- 배지 체계 재구성: [22-24]→[22]+[23-24], [25-28]→[25-26]+[27-28], [29-31]→[29]+[29-30]+[31], [32-34]→[32]+[32-34]
- 내용 복원: "Isaiah son of Amoz" (2곳), "the Rabshakeh", "King Hezekiah's crew", "the king of Assyria's suck-up messengers", "I'll afflict him with self-doubt", "Tirhakah king of Cush", "Tel Assar", "raw Assyrian power", "massacred 185,000 Assyrians"
- EN P18의 배지 [29-31]→[27-28] 정정 (내용은 v27-28이었음)

### ch20 (배지 체계적 밀림 수정)
- P2 [7]→[5-6], P3 [8-9]→[7], P4 [10-12]→[8-9] (전체가 한 칸씩 밀려 있었음)
- "Babylonians, Arameans, Moabites, and Ammonites" → "Babylonian, Aramean, Moabite, and Ammonite raiding bands" (MSG 형용사형 복원)
- "the Brook of Egypt" 추가, "Nehushta daughter of Elnathan" 복원

### ch21 (배지 정정)
- P2 [10-12]→[9] (내용은 MSG [9] "But the people didn't listen")
- P6 [19-22]→[17-18] (내용은 MSG [17-18] "The rest of the life and times of Manasseh")

### ch22
- "Shaphan son of Azaliah, the son of Meshullam" 복원
- "Shallum son of Tikvah, the son of Harhas" 복원
- "hit up", "Yo," 순화

### ch23
- "The Temple of God" (2곳), "from Geba to Beersheba" 복원
- "Nathan-Melech, the warden" 복원
- "Chemosh of the Moabites", "Milcom of the Ammonites" (명사형 복원)
- "Jeroboam son of Nebat" 복원
- "just as at Bethel" 추가
- "God's Revelation" 복원
- "at the Euphrates River" 복원
- "at Riblah in the country of Hamath" 복원
- "nearly four tons of silver and seventy-five pounds of gold" 복원 (기존 "crazy amount"는 의도적 요약이었음)
- "Zebidah daughter of Pedaiah" 복원

### ch24 (배지 밀림 수정)
- P2 [7]→[5-6], P3 [8-9]→[7], P4 [10-12]→[8-9]
- "between the Brook of Egypt and the Euphrates River" 복원
- "Nehushta daughter of Elnathan" 복원

### ch25 (배지 정정)
- P9 [27-30]→[26] (내용은 MSG [26] "they all took off for Egypt")
- "ninth year and tenth month", "fourth month... ninth day", "two walls", "King's Garden", "Arabah Valley road", "at Riblah" 복원
- "on the seventh day of the fifth month" 복원
- "in the land of Hamath" 복원
- "Gedaliah son of Ahikam, the son of Shaphan" 복원
- "Seraiah son of Tanhumeth the Netophathite" 복원
- "Ishmael son of Nethaniah, the son of Elishama" 복원
- KO: "엘리사마의 손자" → "엘리사마의 아들" 정정

### ch3, ch7, ch8 (잔여 FAIL 수정)
- ch3: "Elisha son of Shaphat... Elijah's right-hand man" 복원, "When Moab entered" (단수형) 복원
- ch7: "First they ate and drank" 복원 ("first"→1 숫자 토큰)
- ch8: "country of Philistia" (장소명) 복원, "Ahaziah son of Jehoram" 복원

## Merge/Split 선언 (스탠딩 승인)

내용 온전, EN/KO 일치, 순수 가독성 구조 차이로 승인 없이 선언:

- ch19: '22-24'→[22]+[23-24], '25-28'→[25-26]+[27-28], '29-31'→[29]+[29-30]+[31], '32-34'→[32]+[32-34]
- ch20: '2-3' (3-way), '7' (2-way), '15' (3-way)
- ch21: 없음 (배지 정정만)
- ch22: '18-20' (2-way, 기존)
- ch23: '17' (2-way, 기존)
- ch25: '18-21' (2-way)

## 승인 필요 항목

없음.

## 게이트 결과

- validator: PASS (25개 장 모두 통과)
- completeness: PASS (512개 문단, 0 FAIL, 0 WARN)
- build: 25 tables, 512 rows, VERIFY_DROPPED=0, teen_without_msg=0, msg_orphans=0
- pairing: PAIRING CONTENT OK (512 data rows in 25 tables)
- PAIRING_MISMATCHES=4 (아래 참조, 내용 누락 아님)

### Pairing Mismatches (4건, 모두 구조적 차이)

1. ch4 teen_idx=[29] badges=['26'] msg_verses=[25,26]: MSG [25-26]을 teen이 [26]으로만 배지. 내용 대조 결과 teen에 25-26 내용 모두 포함됨을 확인. 배지는 [25-26]으로 정정 권장 (후속).
2. ch19 teen_idx=[11,12] badges=['16-19','16-19'] msg_verses=[16]: MSG [16] 유닛이 실제로 16-19절 기도문 전체를 포함. Teen 배지 [16-19]가 정확함. MSG 소스 유닛 분할 문제 (원문 구조상 단일 문단).
3. ch19 teen_idx=[20] badges=['29-30'] msg_verses=[29,30,31]: MSG [30-31]과 teen [29-30]이 30절에서 겹침. 내용 모두 포함됨.
4. ch19 teen_idx=[21] badges=['31'] msg_verses=[30,31]: 위와 동일.

## 검증 범위와 미확인 경계

- MSG 문장 단위 대조: ch1-25 전장 완료. 특히 19:23-37은 Bible Gateway 원문과 수동 대조.
- EN/KO 1:1 pairing: validator PASS로 확인.
- 문서 pairing: verify_pairing_content.py로 512행 실제 내용 대조 완료.
- Google Docs 업로드: DOCX 빌드 완료 (`gdocs_build/2Kings.docx`). API 업로드 및 웹 렌더링 확인은 본 환경에서 불가 → 상위 에이전트에서 수행 필요.
- 제목: `열왕기하 (2Kings): MSG + Teen EN + KO` (확정)

## Commit

- (상위 에이전트에서 commit/push 수행)

## 2nd re-audit (Sep 24)
- completeness_check.py: PASS clean (25 chapters, 512 paragraphs, 1,108 name tokens, 210 number tokens).
- Chapter-level epithet/name/number/sentence scans: 14 MSG omissions restored across 8 chapters (EN), 5 of them also restored in KO (KO already preserved the rest):
  1. ch2 idx28 [24]: "forty-two children in all" — EN "forty-two of them" → "forty-two of those kids" (KO already had "그 아이들 중 42명").
  2. ch11 idx2 [5-8]: "on the Sabbath" (x2) dropped from the guard-change orders — EN restored "your Sabbath shift"; KO made explicit for both clauses.
  3. ch11 idx3 [9-11]: Sabbath duty detail + "from one end of The Temple to the other" dropped — EN/KO restored.
  4. ch11 idx5 [13-14]: MSG "king standing beside the throne" mistranslated as "royal pillar" — EN/KO fixed to "throne/왕좌"; "Treason! Treason!" repetition restored (EN had "Treason! This is a coup!"; KO already had the repetition).
  5. ch14 idx5 [9-10]: thistle parable gutted — "in Lebanon" (x3) and "'Give your daughter to my son in marriage'" dropped — EN restored (KO already complete).
  6. ch14 idx8 [13-14]: "from the Ephraim Gate to the Corner Gate" dropped — EN restored (KO already had it).
  7. ch14 idx14 [26-27]: "No one was exempt, whether slave or citizen" reduced to "everyone" — EN restored "slave or citizen" (KO already had "노예든 자유인이든").
  8. ch18 idx2 [7-8]: "whether in sentry outposts or fortress cities ... to Gaza and its borders" — EN/KO restored.
  9. ch18 idx14 [28-32]: Rabshakeh's offer gutted — "your own plot of ground—a garden and a well", "a land of grain and wine, bread and vineyards, olive orchards and honey", "You only live once—so live, really live!" dropped — EN/KO restored.
  10. ch19 idx17 [25-26]: "fragile as grass, insubstantial as wind-blown chaff" dropped — EN restored (KO already had the triplet).
  11. ch23 idx3 [12-15]: "east of Jerusalem on the south slope of Abomination Hill" dropped — EN restored (KO already had "'멸망의 산' 남쪽 비탈").
  12. ch23 idx14 [28-30]: "at the Plain of Megiddo" reduced to "at Megiddo"; "was anointed" dropped — EN restored both (KO already had "므깃도 평야" and "기름 부음").
  13. ch24 idx9 [18]: "the daughter of Jeremiah" dropped — EN restored (KO already had "예레미야의 딸").
  14. ch25 idx0 [1-7]: "in the Plains of Jericho" reduced to "in Jericho" — EN restored (KO already had "예리코 평야").
- False positives (left unchanged): "Shaggy"→"all hairy", "Chronicles of the Kings of Israel"→"official records", "Good!"→"Perfect!", "Never!"→"No way!", "Holy Man"→"man of God", "Gazelle"→"Zibiah" (actual name), "The Revelation"→"God's Law/rules", "Compensation/Absolution Offerings"→"guilt and sin offerings", "Binding House" gloss, "ripped open"→"brutally killed" (teen softening).
- Gates: STRUCT OK (25 ch, EN/KO paragraph+range parity, no null badges), build_gdocs.py VERIFY_DROPPED=0 / teen_without_msg=0 / msg_orphans=0 (4 pre-existing pairing notes in untouched rows), DOCX pairing spot-check 10/10 restored rows, reupload VERIFIED OK (25/25 tables).
