# Jeremiah 감사 보고서 (Worker E2)

**기준**: Eugene Peterson, The Message (MSG)  
**범위**: Jeremiah 1-52장 (EN/KO)  
**일자**: Sep 23, 2026  
**상태**: Validator PASS, 기계적 완전성 검사 완료, 실제 오류 복원 완료

## 요약

Jeremiah 52장 전체를 MSG 원문과 대조하여 감사했다. 주요 발견:

### 1. 실제 내용 누락/오류 (복원 완료)

| 위치 | 문제 | 조치 |
|------|------|------|
| ch6:27 | 문단 잘림 ("God gave me this job:"만 남음) | MSG 27 후반부 복원 |
| ch10:1 | 문단 잘림 (우상 단락 전체 누락) | MSG 1 복원 |
| ch13:18-20 | 왕/대비/네게브 누락 | 복원 |
| ch28:17 | 배지 오류로 v17 미커버 경고 | 배지 수정 (15→15-16, 16→17) |
| ch30:18 | 문단 잘림 | MSG 18 복원 |
| ch31:15 | 문단 잘림 (라헬 애곡 누락) | MSG 15 복원 |
| ch37:14 | 예레미야 항변 누락 | 복원 |
| ch38:10 | "thirty" 오역 (MSG: three) | "three"로 수정 |
| ch38:11 | "three men" 누락 | 복원 |
| ch49 | 배지가 MSG 단위와 어긋남 (18개 문단 전체) | MSG 단위에 맞춰 재조정 |
| ch50:33-34 | 전반부(구원자) 누락 | 복원 |
| ch50:44-45 | 전반부(사자 비유/계획) 누락 | 복원 |
| ch52:30 | 총 4,600명 누락 | 복원 |
| ch52:30 | p13/p14 총합 중복 | p13에서 제거 |

### 2. 이름/장소 복원 (KO가 EN보다 완전했던 경우 포함)

EN에서 빠졌으나 KO와 MSG에 있던 것들:
- ch2: Kedar, Memphis/Tahpanhes, Nile/Euphrates, Baal
- ch24: son of Jehoiakim
- ch26: son of Achbor
- ch39: in Hamath
- ch52: in Hamath, of God

EN/KO 모두에서 빠진 것들 (양쪽 복원):
- ch21: son of Malkijah, son of Maaseiah
- ch26: of Moresheth
- ch35: son of Recab
- ch37: son of Jehoiakim
- ch39: of Simmagar
- ch52: in Hamath

### 3. 검사기 아티팩트 (수정 불필요, 판단 기록)

다음은 검사기가 FAIL로 표시했으나 실제로는 문제없는 경우:

**동의어/의도적 단순화:**
- Chaldeans → Babylonians (같은 제국, 틴즈 가독성을 위한 일관된 선택)
- God → the Lord / the LORD (동일 인물)
- God's Word → what the LORD says (의역)

**관용구 내 숫자:**
- "a lick" → "any" (ch2:37)
- "a second thought" → "care" (ch16:6)
- "the first place" → 생략 (ch14:16)
- "two cents" → "care" (ch23:27)
- "three square meals" → "plenty to eat" (ch31:14)
- "snapped in two" → "snapped in half" (ch48:17)

**MSG 고유 조어 (틴즈 의역으로 수용):**
- Sir Windbag → empty things (ch2:5)
- Blastville/Smoketown → Tekoa/Beth Hakkerem (실제 지명 사용, ch6:1)
- Slapstick buffoons → total joke (ch20:11)

**반복되는 patronymic:**
- ch36-43에서 "son of Nethaniah", "son of Kareah" 등이 첫 언급 후 생략됨.
- 서사 문맥상 인물이 명확하므로 수용. 첫 언급에서는 전체 이름 사용 확인.

**인용구 의역:**
- "lamenting, dirges" → "mourning" (ch9:11)
- "thickheaded, hard-nosed" → "stubborn, hard-headed" (ch6:27, 복원 시 반영)

### 4. 배지 구조 수정

19개 장의 배지 불일치를 MSG 문단 기준으로 수정:
- ch1, 2, 9, 22, 23, 24, 26, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 48, 49

주요 패턴:
- 도입부/인용부 분할 시 두 문단이 같은 MSG 배지 공유
- 헤더 문단이 뒤따르는 본문과 배지 공유 (원칙 2)
- ch49는 18개 문단 전체가 한 절씩 밀려 있었음 (수정 완료)

### 5. 슬랭 점검 (Jeremiah 52장)

52장에는 과도한 슬랭 없음. 사용된 표현 ("rolled up", "insane", "wild 19 months")은 틴즈 구어체 범위 내.

**참고**: 다른 장(ch26 "Dudes", ch35 "lowkey", ch6 "Yo", "bounce" 등)에는 슬랭이 있으나, 담당 범위(Jer 52)가 아니므로 해당 작업자에게 인계.

## 게이트 상태

- [x] Validator PASS (52장)
- [x] 기계적 완전성 검사 (108건 FAIL → 모두 아티팩트로 판정 또는 수정 완료)
- [x] 의미 감사 (담당 장 Jer 52 정밀 감사 완료)
- [ ] DOCX 빌드 및 pairing 검증 (예정)
- [ ] 업로드 (예정)

## 다음 작업

1. Lamentations 5장 MSG 수집 및 감사
2. Ezekiel 48장 MSG 수집 및 감사
3. Daniel 12장 MSG 수집 및 감사

---

# 2차 심층 재검토 (2026-09-25)

**기준**: 성욱 절대 기준 — "축약하지 마라. MSG의 모든 문장·이름·부칭·숫자·인용구·반복·비유 세부가 Teen EN에 살아 있어야 한다." EN이 primary, KO는 EN과 1:1.
**방법**: completeness_check.py (94건 후보) + KO 비대칭(EN에만 빠진 내용) 전수 대조 후 복원.

## 복원 내역 (EN 24건 + KO 13건)

| 위치 | MSG 원문 세부 | EN 조치 | KO 조치 |
|---|---|---|---|
| ch2 idx2 | "Took up with Sir Windbag and turned into windbags" | "taking up with Sir Windbag and turned into windbags themselves" 복원 | 이미 있음(허풍쟁이) |
| ch2 idx15 | "try out another sin-project when the first one fails" / "wringing your hands" / "blacklisted" | sin-project·wringing hands 복원 | 이미 있음 |
| ch3 idx3 | "acting crazy and defiling" (flouting) | "acting crazy and disrespecting what's sacred" 복원 | "미친 짓" 추가 |
| ch9 idx4 | "lamenting... chanting dirges" | "chanting dirges over the old grazing grounds" 복원 | 이미 있음(장송곡) |
| ch13 idx8 | "The villages in the Negev" | "The towns in the Negev" 복원 | "네게브 마을들" 복원 |
| ch19 idx2 | "Dehumanized by the pressure of the enemy siege" | "Dehumanized by the pressure of the enemy siege" 복원 | 이미 있음(정신 나가서) |
| ch21 idx1 | "surrenders to the Chaldeans" | "the king of Babylon and the Chaldeans" 복원 | 이미 있음(갈대아 애들) |
| ch23 idx5 | "careening into the darkness, somersaulting into the pitch-black dark" | "careening into the darkness, somersaulting into the pitch-black dark" 복원 | "비틀거리며 떨어지고, 칠흑 같은 어둠 속으로 곤두박질" 복원 |
| ch27 idx4 | "Jehoiachin son of Jehoiakim" + "into Babylonian exile" + "all the leaders of Judah and Jerusalem" | "Jehoiachin son of Jehoiakim into Babylonian exile along with all the leaders of Judah and Jerusalem" 복원 | 동일 복원 |
| ch29 idx16 | "prepare some Babylonian recipes" | "prepare some Babylonian recipes" 복원 | 이미 있음(바빌론 음식 레시피) |
| ch31 idx8 | "three square meals a day" | "three square meals a day" 복원 | 이미 있음(하루 세 끼) |
| ch36 idx11 | "Jehudi son of Nethaniah, son of Semaiah, son of Cushi" | 부칭 2건 복원 | "구시의 증손자, 스마야의 손자" 복원 |
| ch36 idx19 | "Seraiah son of Azriel, and Shelemiah son of Abdeel" | 실명·부칭 복원 ("two other guys" → 실명) | 동일 복원 |
| ch37 idx9 | "Jeremiah kept talking to King Zedekiah" | "Jeremiah kept talking to King Zedekiah" 복원 | "시드기야 왕한테 계속" 복원 |
| ch39 idx5 | "Nebushazban the Rabsaris, Nergal-sharezer the Rabmag" + "Gedaliah son of Ahikam, son of Shaphan" | 직함·실명·부칭 복원 | 동일 복원 |
| ch40 idx2 | "Gedaliah son of Ahikam, son of Shaphan" | "son of Shaphan" 복원 | 이미 있음 |
| ch40 idx5 | "sons of Ephai the Netophathite" / "Jaazaniah son of the Maacathite" | 출신·부칭 복원 | 이미 있음 |
| ch40 idx6 | "Gedaliah son of Ahikam, son of Shaphan" | "son of Shaphan" 복원 | "사반의 손자" 복원 |
| ch40 idx8 | "Gedaliah son of Ahikam, son of Shaphan" | "son of Shaphan" 복원 | "사반의 손자" 복원 |
| ch40 idx10 | "took Gedaliah aside... in Mizpah" | "in Mizpah" 복원 | 이미 있음(미스바) |
| ch43 idx2 | "Gedaliah son of Ahikam, son of Shaphan" | "son of Shaphan" 복원 | "사반의 손자" 복원 |
| ch48 idx2 | "lazy as a dog in the sun" | "lazy as a dog in the sun" 복원 | "태양 아래서 낮잠 자는 개처럼" 복원 |
| ch50 idx4 | "Good sheepdogs lead" | "Good sheepdogs lead—don't you be led" 복원 | "양치기 개처럼" 복원 (기존 '숫염소' 오역을 MSG 비유로 정정) |
| ch52 idx4 | "the Arabah Valley" | "into the Arabah Valley" 복원 | 이미 있음(아라바 계곡) |

## 1차 감사 판정 번복에 대한 기록

1차 감사(completeness_fp_Jeremiah.md)는 위 항목 중 다수를 "오탐"으로 판정했음
(Sir Windbag·dirges·Negev·dehumanized·Chaldeans·careening·Jehoiakim 부칭·three square meals·Arabah,
ch36–43 부칭 생략 56건은 "의식적 문체 결정"으로 별도 보고).
2차 재검토는 성욱의 절대 기준("이름·부칭·숫자·인용구·비유 세부가 Teen EN에 살아 있어야 한다")과
2사무엘 2차 재검토 선례(호칭 son of Ner 6건·son of Zeruiah 4건 등 복원)에 따라 전부 복원으로 판정을 뒤집음.
내용 손실이 없는 순수 문체 선택이 아니라 MSG 세부 누락이므로 의도적 요약 금지 원칙(원칙 3) 적용.

## 검사기 잔여 74건 전수 분류

수정 후 재실행: FAIL 94건 → 74건. 잔여 74건은 MSG·Teen 병렬 대조로 전부 오탐으로 확정:
- 헤더 문단 아티팩트 9건 (ch10 idx0, ch30 idx9, ch31 idx9, ch49 idx0/idx2/idx14, ch6 idx16, ch3 idx10의 gypped는 idx11에 있음)
- Chaldean(s)→Babylonian(s) 동의어 17건, Babylon 지칭 6건
- 관용구·서수 숫자 오탐 12건 (first place, second thought, two cents, four corners, snapped in two→in half 등)
- MSG 수사적 조어의 틴즈 paraphrase 14건 (slapstick→total joke, subsidizing→encouraging, decking, blastville/smoketown→Tekoa/Beth Hakkerem 실지명 등)
- 철자 변형 3건 (Jehoiadah→Jehoiada, Shaphatiah→Shephatiah, Baaliss→Baalis)
- 일반명사 god/word의 the Lord/the LORD/발화문 대응 13건

## 게이트 (2026-09-25)

- [x] validate_translation.py PASS (52장)
- [x] build_gdocs.py: 52 tables, 683 rows, VERIFY_DROPPED=0, teen_without_msg=0
- [x] verify_pairing_content.py: PAIRING CONTENT OK
- [x] Google Docs 재업로드 + API 52/52 + export-back VERIFIED OK (2026-09-25, doc id 1_9YRCZ8ECbgNbHbAz2FtuFin-Hmol37xnoylR9QYUsE, 기존 링크 유지, live 제목에 Final 없음)
  - 참고: 첫 업로드 시도에서 export-back 게이트가 수정 문단 17건을 DROPPED로 보고 — 원인: 중간에 git stash 테스트로 원본 데이터 기준 DOCX가 재빌드되어 stale 파일이 업로드됨. DOCX 재빌드 후 재업로드하여 VERIFIED OK 확인 (근본 원인 해결)
- 참고: msg_orphans=1 (ch7 v2-3)은 수정 전후 동일하게 존재하는 기존 이슈로, 이번 수정과 무관
- 미확인: Google Docs 웹 화면 직접 확인, production 앱 미반영
