# Amos 감사 리포트 (Sep 24)

기준: Eugene Peterson The Message(MSG). EN primary, KO는 EN 1:1.

## 감사 방법
- MSG 원문 준비: BibleGateway MSG 페이지에서 boilerplate 제거, `### ch1`~`### ch9` 장 마커 추가. 9장 78개 MSG 유닛 파싱, 전 장 절 범위 누락·초과 없음. 9:11-15는 공개 BibleGateway 페이지와 표본 대조.
- 기계적 완전성 검사: 9장 106문단(헤더 제외), 이름 117·숫자 33 토큰 → FAIL 7건 전수 수동 대조.
- EN/KO 구조 parity: validator로 확인 (문단 수·배지 1:1).
- 욕설 스크리닝: validator 검사 7 (원칙 5). EN `whore` 1건 검출 → `sacred prostitute`로 순화 후 PASS.
- 독 짝지음 검증: export-back DOCX 셀 내용 대조 (건별, 표 개수 아님).

## 발견 이슈

### 실제 누락 3건 (수정 완료)
| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 2:1-3 | "burning down the forts of **Kerioth**" | 누락 (고유명사) + EN/KO 비대칭 | EN에 "burning down the forts of Kerioth" 복원. KO는 이미 "케리옷의 요새들을" 보유 → 수정 후 EN/KO parity 회복 |
| 7:1-2 | "the **second** crop was just sprouting" | 누락 (서수) + EN/KO 비대칭 | EN "the next round of crops" → "the **second** round of crops". KO는 이미 "두 번째 작물" 보유 |
| 9:7-8 | "the Arameans from **Qir**" | 철자 불일치 | EN "Kir" → "**Qir**". BibleGateway 실시간 대조로 MSG 철자 확인. 참고: MSG 1:5는 "Kir" — MSG 원문 자체가 장별 철자 불일치. EN은 각 구절 MSG 철자를 따름. KO는 한글 표기 관용상 "기르" 통일 |

### 오탐 4건 (수정 없음)
`completeness_fp_Amos.md`에 전수 문서화. 클래스: 숙어 paraphrase(C) 1건, 동일 지시대상 호칭 교체(D) 3건.
- ch1 [11-12] quote rampages/meanness/timeout → "non-stop, 24/7" / "cruelty" / "never takes a break"
- ch5 [3] "God's Word" → "from God himself"
- ch6 [8] "stands by his Word" → "He's not backing down"
- ch7 [16] "God's Word" → "what God is saying"

## 주요 복원 (감사 전체)
- 1장: on behalf of Israel, visions, Jeroboam II, son of Joash, iron hammers and mauls, crime king, vice boss, people of the land
- 2장: `sacred whore` → `sacred prostitute` / `신성한 창녀` (의미 보존하며 순화)
- 3장: hit with a stone, forts of Assyria/Egypt
- 4장: cows of Bashan, Samaria slopes, indolent/pampered, rope, cattle prods, ruined walls, single file, kick them to kingdom come, 순수한 감사제물, 과수원·텃밭, 좋은 말이 죽임당함, earthquake and fire, Adam, Mountain-Shaper, Wind-Maker
- 5장: bold print, tragic warning, marches out, family of Israel, justice to vinegar, righteousness into mud, rape → sexually assaulted / 성폭행 (의미 보존), fund-raising schemes, PR/image making
- 6장: bloated corpse of righteousness
- 7장: 과도한 슬랭 정리, pruned trees, forced into prostitution, auctioned off, homeless and friendless
- 8장: MSG에 없는 여름 과일 해설 제거, royal singers, arrogance of Jacob, 강물·침수·진흙바다, sunken eyes and bald heads, go anywhere/listen to anyone, Word-thirst/God-thirst 구별, Samaria Sin-and-Sex Center, Dan·Beer-sheba 맹세
- 9장: shrine, no runaways, captured alive, Dragon, mere touch, rock-firm earth, ladles, in our lifetime, But also, `plant them` 반복

## 수정량
- EN 본문 47문단 변경, KO 본문 36문단 변경, EN/KO 배지 각 6개 변경.

## split/merge 선언
- merge: 0건.
- split 19건 (splits[].paras는 0-based index, EN/KO 동일):
  - ch1: 6건 — 2→[1,2], 3-5→[3,4], 6-8→[5,6], 9-10→[7,8], 11-12→[9,10], 13-15→[11,12]
  - ch2: 3건 — 1-3→[0,1], 4-5→[2,3], 6-8→[4,5]
  - ch3: 1건 — 12→[5,6]
  - ch4: 0건
  - ch5: 3건 — 3→[2,3], 4-5→[4,5], 16-17→[12,13]
  - ch6: 1건 — 8→[3,4]
  - ch7: 4건 — 3→[2,3], 6→[6,7], 8-9→[9,10,11,12], 10→[13,14]
  - ch8: 1건 — 2→[1,2,3]
  - ch9: 1건 — 7-8→[2,3] (이번 감사에서 추가; MSG 7-8이 한 문단)
- 모두 순수 가독성 구조 차이 (MSG 대비 내용 온전, EN/KO 일치) → 승인 없이 선언하고 진행.

## 배지 수정
- 3장 마지막 문단: 14-15 → 13-15
- 6장 P5: 10-11 → 9-10
- 6장 P6: 12 → 11
- 7장 P9, P10, P12: 8 또는 9 → 8-9 (MSG 7:8-9가 하나의 범위이므로 관련 문단 4개 모두 8-9로 통일)
- EN/KO verseRanges == msg_ranges 유지.

## 검증 게이트
1. ✅ 의미 전수 감사 — MSG 전 문단 대 teen 전수 대조 (checker + 수동). 실제 누락 3건 수정.
2. ✅ 이슈 리포트 작성 — 본 문서 + completeness_fp_Amos.md.
3. ✅ 수정 반영 — EN 47문단·KO 36문단·배지 각 6개. split 1건 추가 (ch9 7-8).
4. ✅ validate_translation.py — PASS: 9개 장 모두 통과.
5. ✅ 기계적 완전성 검사 — 잔여 FAIL 4건 전수 문서화 (정당한 오탐).
6. ✅ build_gdocs.py — rows=106, tables 9/9, VERIFY_DROPPED=0.
7. ✅ 독 짝지음 검증 — verify_pairing_content.py: 106 data rows, PAIRING CONTENT OK.
8. ✅ Google Docs 업로드 — `아모스 (Amos): MSG + Teen EN + KO`, tables 9/9, export_back VERIFIED OK.
   - https://docs.google.com/document/d/1yS_ri68a6HL-sL4zvowfm4ol4IkN6YdfyUU85VVVJjw/edit?usp=drivesdk

## 승인 필요 항목
- 없음. 내용 누락·오역·EN/KO 의미 불일치·방향 모호 사례 없음.

## 검증 범위
- 확인함: MSG 파서 출력(78 units) 대 teen 전수 토큰 대조, EN/KO 문단 수·순서·배지 parity, verseRanges == msg_ranges, split 구조 EN/KO 동일, 욕설 자동 스크리닝, DOCX export-back 셀 내용 대조.
- 확인하지 못함: KO 본문 117문단 전수 의미 대조 (EN 기준 구조 parity + 스팟체크만 수행), 자동 욕설 목록 밖 미묘한 표현의 뉘앙스, Google Docs 웹 화면의 실제 렌더 (API + export-back DOCX로 대체 검증).

## 생산 반영
- 구약 감사본은 production 앱에 반영하지 않음 (원칙).

---

## 2nd re-audit (Sep 24)

2nd-pass, MSG-원문 기준 9장 106문단 전수 재대조.

### checker 후보 4건 분류
- ch1 idx9 [11-12] quote `rampages, meanness, timeout` → 오탐. EN "'Their anger is just non-stop, 24/7. Their cruelty never takes a break." 의미 보존.
- ch5 idx2 [3] name `word` → **실제 누락**. MSG "This is the Message, God's Word:"가 EN에서 "This is the real deal, from God himself:"로 바뀌며 칭호 탈락 (KO는 "하나님의 말씀" 유지). EN 복원: "This is the Message, God's Word:"
- ch6 idx3 [8] name `word` → 오탐 ("solemnly stands by his Word" → "He's not backing down" 의미 보존)
- ch7 idx18 [16] name `word` → 오탐 ("So listen to God's Word" → "So listen to what God is saying" 의미 보존)

### 복원 결과
- MSG 복원 1건 (ch5 idx2 EN 칭호). 나머지 전 문단 MSG 대비 내용 온전, EN/KO 일치.

### 게이트
- STRUCT OK: 9장 106문단
- completeness_check 잔여 3건 모두 오탐
- build: rows=106, msg_units=78, teen_without_msg=0, msg_orphans=0, VERIFY_DROPPED=0
- DOCX spot-check: 5장 idx2 복원 행 페어링 확인
- Google Docs: 신규 문서 생성 (Amos 미등록이었음), API 테이블 9/9, export-back VERIFIED OK
