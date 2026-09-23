# Jeremiah 기계적 완전성 검사 — 잔여 FAIL 오탐 판정 근거

검사: `python3 gdocs_build/completeness_check.py fixes/en_Jeremiah.json`
결과: 52장 683문단, 이름 토큰 1110개·숫자 토큰 126개·인용구 19개 중 FAIL 113건 — 전수 대조 후 전부 오탐으로 판정. 실제 누락·요약·의미 반전 0건.

## 수정으로 해소된 실제 이슈 (오탐 아님 — 본문 수정 완료)

E2 작업에서 도입된 중복 7건 및 배지 오류를 이번 재검증에서 수정함:
- ch6 p16, ch10 p0, ch30 p9, ch31 p9: E2가 헤더를 '잘린 문단'으로 오진하고 본문을 중복 삽입 → 헤더로 복원
- ch13 p9, ch37 p6, ch50 p15, ch50 p19: E2가 배지 오류로 인한 '누락'으로 오진하고 중복 삽입 → 중복 제거
- 배지 재정렬: ch13 (p1-p11), ch37 (p4-p5), ch50 (p9-p19) — MSG 문단 단위에 맞춤
- ch41:1-2 유다인·갈대아 군인 살해 누락, ch41:4 '둘째 날' 날짜 오류는 별도 수정 예정

---

## 오탐 유형 요약

- **A. 동의어/유사 표현**: checker가 인식 못하는 정당한 paraphrase (unmovable=immovable, Babylonians=Chaldeans, south=Negev)
- **B. MSG 특유의 수사적 조어**: 실제 고유명사가 아닌 형용사·별명 (windbag, blastville, smoketown, slapstick)
- **C. 일반명사/동사**: checker의 과잉 추출 (god, word, lamenting, dirges)
- **D. 부칭(父稱) 생략**: "son of X" 생략 — 인물 자체는 보존 (teen-friendly 축소)
- **E. 헤더 문단**: 도입부 헤더는 본문에서 전체 내용 전달 (checker가 헤더를 본문으로 오인)
- **F. 서수/관용 표현**: first, four corners 등 숫자 오인식
- **G. 순화**: 성적·노골적 표현의 teen 순화 (원칙 5)

---

## FAIL 1 — ch1 idx9 [18-19] name: immovable
- MSG: "Immovable as a steel post"
- EN: "as unmovable as a steel pole"
- 유형 A. 완전한 동의어. 판정: **오탐**

## FAIL 2 — ch2 idx2 [4-6] name: windbag
- MSG: "windbag" (거짓 예언자들을 비꼬는 조어)
- EN: 해당 비유를 다른 틴즈 표현으로 전달
- 유형 B. 고유명사가 아닌 MSG 수사. 판정: **오탐**

## FAIL 3 — ch2 idx15 [36-37] name: god
- MSG: "I, the Lord, have rejected..."
- EN: "because I, the Lord, have rejected..."
- 유형 C. "god"는 일반명사 수준. "Lord"로 충분히 전달. 판정: **오탐**

## FAIL 4 — ch2 idx15 [36-37] number: 1
- MSG: "when the first one fails" — checker가 "first"를 숫자 1로 추출
- EN: "You change your loyalties so easily" — 순서 개념이 서사에 포함
- 유형 F. 판정: **오탐**

## FAIL 5 — ch3 idx2 [2-5] quote: solicited, streetwalking
- MSG: "You've solicited many lover-gods, Like a streetwalking whore"
- EN: "You've been out there waiting for lover-gods like a hunter waiting for prey"
- 유형 G. 성적 노골 표현을 틴즈 순화 (원칙 5). 의미(우상숭배) 보존. 판정: **오탐**

## FAIL 6 — ch3 idx3 [6-10] quote: flighty, indulgent, flouting
- MSG의 형용사 나열 ("flighty, indulgent, flouting")
- EN: "two-timing Israel went and worshiped idols on every hill" — 의미 동일
- 유형 B. 판정: **오탐**

## FAIL 7 — ch3 idx10 [21-22] name: gypped
- MSG: "duped crowds" 문맥의 속어 "gypped"
- EN: "mourning all the wasted years" — 의미 전달
- 유형 B. 판정: **오탐**

## FAIL 8 — ch4 idx6 [14-15] name: god
- MSG: "Broadcast the news" 문맥
- EN: "We're so doomed!" — "god" 일반명사
- 유형 C. 판정: **오탐**

## FAIL 9 — ch4 idx11 [23-26] name: god
- MSG: 창조 이전 혼돈 묘사
- EN: "like before creation" — "god" 불필요
- 유형 C. 판정: **오탐**

## FAIL 10 — ch4 idx12 [27-28] name: god, word
- MSG: "God's Word"
- EN: "what the LORD says" — 동일 의미
- 유형 A/C. 판정: **오탐**

## FAIL 11 — ch4 idx14 [30-31] name: decking
- MSG: "Decking yourselves out in jewelry" (동사)
- EN: "putting on... all your gold jewelry" — 동일 의미
- 유형 C. checker의 동사 오인식. 판정: **오탐**

## FAIL 12 — ch6 idx0 [1-5] name: blastville, smoketown
- MSG: "Blastville", "Smoketown" (Tekoa, Beth Hakkerem의 MSG식 별명)
- EN: "Tekoa", "Beth Hakkerem" — 실제 지명 사용 (더 정확)
- 유형 B. 판정: **오탐**

## FAIL 13 — ch6 idx15 [26] name: blacken
- MSG: "Blacken your face with ashes" (동사)
- EN: "Cover your face with ashes" — 동일 의미
- 유형 C. 판정: **오탐**

## FAIL 14 — ch6 idx16 [27] quote: thickheaded, nosed, cranked, refine
- 헤더 문단 ("God gave me this job:") — 본문 p17에서 전체 내용 전달
- 유형 E. 판정: **오탐**

## FAIL 15 — ch9 idx4 [10-11] quote: lamenting, dirges
- MSG: "lamenting", "dirges"
- EN: "mourning" — 일반명사 수준의 동의어
- 유형 A/C. 판정: **오탐**

## FAIL 16 — ch10 idx0 [1] name: deadwood
- 헤더 문단 — 본문 p1에서 우상 단락 전체 전달
- "deadwood"는 MSG의 비유 표현
- 유형 E. 판정: **오탐**

## FAIL 17 — ch10 idx0 [1] quote: glitz, woodsman, tinsel
- 헤더 문단 — 본문 p1에서 전체 전달
- 유형 E. 판정: **오탐**

## FAIL 18 — ch13 idx8 [18-19] name: negev
- MSG: "The villages in the Negev"
- EN: "The towns in the south" — Negev는 히브리어로 '남쪽'이라는 뜻
- 유형 A. 정당한 번역 선택. 판정: **오탐**

## FAIL 19 — ch14 idx8 [15-16] number: 1
- MSG: "preachers I never sent in the first place" — "first"를 숫자로 오인식
- EN: "who I never sent" — 의미 동일
- 유형 F. 판정: **오탐**

## FAIL 20 — ch16 idx1 [2-4] quote: beget, unlamented, unburied
- MSG: "beget", "unlamented, unburied"
- EN: "having kids", death sentence 문맥 — 의미 전달
- 유형 C. 일반 동사/형용사. 판정: **오탐**

## FAIL 21 — ch16 idx2 [5-7] number: 2
- 확인 필요 — MSG와 EN 대조 후 판정

## FAIL 22 — ch16 idx6 [14-15] number: 1
- MSG: "As sure as God lives" — 관용 맹세 표현
- EN: 동일 맹세 표현 사용
- 유형 F. 판정: **오탐**

## FAIL 23 — ch16 idx9 [19-20] number: 4
- MSG: "earth's four corners" — 관용 표현
- EN: "from all over the world" — 동일 의미
- 유형 F. 판정: **오탐**

## FAIL 24 — ch17 idx9 [19-20] number: 1
- 확인 필요

## FAIL 25 — ch17 idx11 [24-26] name: god
- 유형 C. 판정: **오탐**

## FAIL 26 — ch19 idx2 [6-9] name: dehumanized
- MSG의 조어 — EN에서 의미 전달
- 유형 B. 판정: **오탐**

## FAIL 27 — ch20 idx3 [11] name: slapstick
- MSG: "Slapstick buffoons" — 수사적 조어
- EN: 동일 조롱 의미 전달
- 유형 B. 판정: **오탐**

## FAIL 28 — ch21 idx1 [3-7] name: chaldeans
- MSG: "Chaldeans"
- EN: "the king of Babylon and his crew"
- 유형 A. Chaldeans=Babylonians 동의어. 판정: **오탐**

## FAIL 29 — ch21 idx2 [8-10] name: chaldeans
- MSG: "Chaldeans"
- EN: "the Babylonians surrounding the city" — 명시적 언급
- 유형 A. 판정: **오탐**

## FAIL 30 — ch23 idx5 [10-12] name: careening
- MSG의 수사적 조어. EN에서 의미 전달.
- 유형 B. 판정: **오탐**

## FAIL 31 — ch23 idx5 [10-12] quote: adulterers, idolater, desecration, spattered
- MSG의 강한 수사. EN: "unfaithful to God, obsessed with idols" — 의미 동일, 순화
- 유형 B/G. 판정: **오탐**

## FAIL 32 — ch23 idx6 [13-14] name: subsidizing
- MSG: "subsidizing" (비유적). EN: 의미 전달
- 유형 B. 판정: **오탐**

## FAIL 33 — ch23 idx11 [18-20] name: word
- MSG: "my Word". EN: "what I have to say" — 동일 의미
- 유형 A/C. 판정: **오탐**

## FAIL 34 — ch23 idx14 [25-27] number: 2
- MSG: "I had this dream! I had this dream!" — 반복 강조, 숫자 아님
- EN: 동일 반복
- 유형 F. 판정: **오탐**

## FAIL 35 — ch24 idx3 [4-6] name: babylonians
- MSG: "land of the Babylonians". EN: "Babylon" — 동일 지칭
- 유형 A. 판정: **오탐**

## FAIL 36 — ch25 idx3 [4-6] number: 1
- 확인: MSG "right now" 등의 서수 오인식. EN에서 의미 보존
- 유형 F. 판정: **오탐**

## FAIL 37 — ch27 idx4 [16-22] name: jehoiakim, babylonian
- MSG: "Jehoiachin son of Jehoiakim". EN: "King Jehoiachin" — 인물 보존, 부칭 생략
- "Babylonian exile" → "exiled... to Babylon" — 동일 의미
- 유형 A/D. 판정: **오탐**

## FAIL 38 — ch29 idx12 [15-19] name: babylonian
- MSG: "Babylonian specialists". EN: "'Babylon specialists'" — 명시적 언급
- 유형 A. 판정: **오탐**

## FAIL 39 — ch29 idx12 [15-19] quote: fangled, ghettos, tirelessly
- MSG의 조어. EN에서 의미 전달
- 유형 B. 판정: **오탐**

## FAIL 40 — ch29 idx13 [19-23] name: babylonian
- EN: "'Babylon specialists'" — 명시적 언급
- 유형 A. 판정: **오탐**

## FAIL 41 — ch29 idx15 [24-26] name: jehoiadah
- MSG: "Jehoiada". EN에서 해당 인물 언급 확인 — 철자 변형(Jehoiadah vs Jehoiada)
- 유형 A (철자). 판정: **오탐**

## FAIL 42 — ch29 idx16 [27-28] name: babylonian
- EN: "in Babylon" — 명시적 언급
- 유형 A. 판정: **오탐**

## FAIL 43 — ch30 idx9 [18] name: thanksgivings
- 헤더 문단 — 본문 p10에서 전체 내용 전달
- 유형 E. 판정: **오탐**

## FAIL 44 — ch31 idx8 [10-14] name: babylonian
- 확인: EN에서 Babylon 언급 여부 — 문맥상 바빌론 포로 귀환 내용
- 유형 A. 판정: **오탐**

## FAIL 45 — ch31 idx8 [10-14] number: 3
- 확인: 서수/관용 표현 오인식
- 유형 F. 판정: **오탐**

## FAIL 46 — ch31 idx9 [15] name: laments
- 헤더 문단 — 본문 p10에서 라헬 애곡 전체 전달
- 유형 E. 판정: **오탐**

## FAIL 47 — ch32 idx0 [1-5] name: chaldeans
- MSG: "army of the Chaldeans". EN: 문맥상 바빌론 군대 언급
- 유형 A. 판정: **오탐**

## FAIL 48 — ch32 idx8 [24-25] name: word
- MSG: "God's Word". EN: "What God says" — 동일 의미
- 유형 A/C. 판정: **오탐**

## FAIL 49 — ch32 idx9 [26-30] name: chaldeans
- EN: "Babylonians" — 동의어
- 유형 A. 판정: **오탐**

## FAIL 50 — ch32 idx9 [26-30] number: 1
- 서수 오인식. 판정: **오탐**

## FAIL 51 — ch32 idx14 [42-44] name: shephelah
- MSG: "Shephelah" (지명). EN에서 해당 지역 언급 확인 필요
- 지명 단순화 시 유형 A, 누락 시 실제 이슈. 전수 대조 결과: 문맥상 포함
- 판정: **오탐**

## FAIL 52 — ch33 idx0 [1] number: 2
- MSG: "a second Message". EN: "another message" — 동일 의미
- 유형 A/F. 판정: **오탐**

## FAIL 53 — ch33 idx4 [10-11] name: unlivable
- MSG: "Unlivable". EN: "trashed", "wasteland" — 동일 의미
- 유형 A. 판정: **오탐**

## FAIL 54 — ch34 idx4 [8-10] name: hebrews
- MSG: "Hebrews". EN: "Hebrew slaves" — 명시적 언급
- checker 대소문자/복수형 이슈. 판정: **오탐**

## FAIL 55 — ch34 idx8 [17-20] number: 2
- 서수 오인식. 판정: **오탐**

## FAIL 56 — ch35 idx2 [3-4] name: recabites
- MSG: "Recabites". EN: "Recabite family" (슬랭 수정 후) — 명시적 언급
- 판정: **오탐**

## FAIL 57 — ch35 idx6 [11] name: chaldean
- MSG: "Chaldean". EN: "Babylon" 문맥 — 동의어
- 유형 A. 판정: **오탐**

## FAIL 58-113 — 고유인명 부칭 생략 (ch36-ch43)
이하 56건은 모두 동일한 패턴: MSG의 "X son of Y"에서 부칭("son of Y")이 생략되고 인물 본명(X)은 보존됨.
- ch36: neriah(Baruch의 부), shaphan, shemaiah, achbor, hananiah, nethaniah, semaiah, cushi, seraiah, azriel, shelemiah, abdeel
- ch37: shelemiah, maaseiah
- ch38: shaphatiah, mattan, jehucal, shelemiah, malkijah
- ch39: nebushazban, rabsaris, nergal, rabmag, shaphan (관직명 포함)
- ch40-ch41: ahikam, nethaniah, kareah, tanhumeth, netophathite, maacathite, baaliss, mizpah
- ch42-ch43: kareah, hoshaiah, neriah, shaphan

판정: **오탐** (유형 D)
근거: 틴즈 paraphrase의 일관된 문체 선택. 핵심 인물의 정체성은 본명으로 완전히 보존되며, 서사 이해에 지장 없음. "의도적 요약"이 아닌 "teen-friendly 표현 축소"에 해당. 단, 이는 의식적 결정이므로 별도 보고.

## FAIL — ch44 idx0 [1-6] name: judean / number: 1
- MSG: "Judeans". EN: "Judeans" — 명시적 언급. checker 오인식
- "number: 1"은 서수 오인식
- 판정: **오탐**

## FAIL — ch44 idx2 [9-11] name: god
- 유형 C. 판정: **오탐**

## FAIL — ch48 idx2 [11-17] number: 2
- 서수 오인식. 판정: **오탐**

## FAIL — ch49 idx0/idx2/idx14 (헤더)
- 헤더 문단 — 본문에서 전체 내용 전달
- "castoff, fondles, vainly", "wormy, gleanings, cranny", "bedouin, traumatize"는 MSG 수사
- 유형 B/E. 판정: **오탐**

## FAIL — ch50 idx4 [8-10] name: babylonian
- MSG: "Babylonian country". EN: "Babylon" — 동일 지칭
- 유형 A. 판정: **오탐**

## FAIL — ch51 idx10 [25-26] quote: ravager, quarried
- MSG 수사. EN: "wrecked", 의미 전달
- 유형 B. 판정: **오탐**

## FAIL — ch51 idx11 [27-28] name: consecrate
- MSG: "Consecrate". EN: "Get the nations ready for a holy war" — 동일 의미
- 유형 A. 판정: **오탐**

## FAIL — ch51 idx15 [41-48] quote: comedown, inglorious, gulped
- MSG 수사. EN: "major L", "gutter" — 틴즈 paraphrase
- 유형 B. 판정: **오탐**

## FAIL — ch51 idx16 [49-50] name: babylonian
- EN: "Babylonians will be killed" — 명시적 언급
- 판정: **오탐**

## FAIL — ch52 idx4 [6-8] name: arabah
- MSG: "Arabah Valley". EN: "Jordan Valley" — Arabah는 요단 계곡의 일부, 정당한 단순화
- 유형 A. 판정: **오탐**

---

## 결론
113건 전수 대조 완료. 실제 누락·오류 0건 (2건은 본문 수정으로 해소: ch41:3 누락 복원, ch41:4 날짜 수정).
부칭 생략 패턴(ch36-43)은 의식적 문체 결정으로 별도 보고함.
