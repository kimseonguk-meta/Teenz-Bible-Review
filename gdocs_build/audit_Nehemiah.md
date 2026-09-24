# Nehemiah 13장 감사 보고서

**기준**: Eugene Peterson, The Message (MSG)
**범위**: Nehemiah 1–13장 (Teen EN / Teen KO, 각 319문단 — ch11 지명 3문단 추가 후)
**일자**: Sep 24, 2026
**상태**: MSG 전수 대조 완료, 7개 게이트 전부 수행. "완료" 선언은 성욱만 가능 — 본 보고서는 수행 결과 기록.

## 결론

- **MSG 원문 품질**: `msg_Nehemiah.txt` 1–13장 전부 정상 파싱 (154유닛). 장별 유닛 수 6,12,14,13,11,13,10,12,11,9,13,16,14. 각 장 1절~마지막 절 전수 존재, 비정상적으로 작은 장 없음. **재수집 불필요.**
- **핵심 발견**: validator가 통과하던 장을 포함해 13장 전체의 Teen 배지가 MSG 실제 문단 경계와 어긋나 있었음 (p5부터 1유닛씩 밀리는 패턴이 ch2·3·4·5·6·7·8·9·10·13에서 반복). 13장 전체 배지를 MSG 유닛 기준으로 재정렬하고 split 32건을 선언함.
- **실제 누락 복원**: ch3 부칭 20건, ch5 forty shekels, ch6 부칭 5건, ch7 헌금 숫자 3건, ch8 레위인 10명·인용구, ch9 cisterns, ch10 성전세율·Dedication-Offerings·grain, ch11 지명 3건(Zorah·Aijah·Hazor), ch12 음악가 8명·Hashaiah 오타, ch13 창고 물품 세부·부칭 등.
- EN 42개 문단·KO 28개 문단 본문 수정 + EN/KO 각 제목 2건 + 지명 3문단 신규 추가. validator PASS 유지.

## 수정 이슈 표

| 장:절 | MSG 요지 / 근거 | 유형 | 수정 내용 |
|---|---|---|---|
| 전장 | MSG 문단 경계와 Teen 배지 불일치 (ch2·3·4·5·6·7·8·9·10·13에서 1유닛씩 밀림) | 배지 | 13장 전체 verseRanges·msg_ranges를 MSG 유닛 기준으로 재정렬, split 32건 선언 (아래 목록) |
| 2:1-2 | — (슬랭 R1) | 슬랭 | EN p1 'lowkey' 제거 |
| 2:6 | MSG "the king gave his approval to send me" | 슬랭 | EN p5 '"Alright, bet,"' → 'gave his approval to send me' |
| 2:10 | MSG "very upset" | 슬랭 | EN p8 'super salty' → 'seriously upset' |
| 2:20 | MSG "I shot back" | 슬랭 | EN p14 'clapped back' → 'shot back' |
| 3:1-2 | MSG "Meremoth son of Uriah, the son of Hakkoz ... Meshullam son of Berekiah, the son of Meshezabel ... Zadok son of Baana" | EN 부칭 누락 (KO는 있음) | EN p1 부칭 3건 복원 |
| 3:1-2 | MSG "their nobles ... refused to get their hands dirty" | 슬랭 | EN p1 'too cool for school' → 'thought they were too important to get their hands dirty' / KO p1 '지들 주인' → '자기 주인' |
| 3:3-5 | MSG "Joiada son of Paseah ... Meshullam son of Besodeiah ... Melatiah the Gibeonite, Jadon the Meronothite ... Uzziel son of Harhaiah" | EN 부칭·칭호 누락 (KO는 있음) | EN p2 복원 |
| 3:6-8 | MSG "Rephaiah son of Hur" | EN 부칭 누락 (KO는 있음) | EN p3 복원 |
| 3:9-10 | MSG "Malkijah son of Harim ... Hasshub son of Pahath-Moab ... Shallum son of Hallohesh" | EN 부칭 누락 (KO는 있음) | EN p4 복원 |
| 3:14 | MSG "Malkijah son of Recab" | EN 부칭 누락 (KO는 있음) | EN p6 복원 |
| 3:15 | MSG "Shallun son of Col-Hozeh" | EN 부칭 누락 (KO는 있음) | EN p7 복원 |
| 3:19-23 | MSG "Binnui son of Henadad ... Ezer son of Jeshua ... Baruch son of Zabbai ... Meremoth ... Azariah son of Maaseiah, son of Ananiah" | EN 부칭 누락 (KO는 일부 있음) | EN p9·p10 복원. EN p10 'was super motivated' (MSG에 없는 첨가) 삭제 / KO p10 '완전 의욕 넘쳐서' 삭제, '학고스의 손자'·'마아세야의 손자이자 아나냐의 아들' 추가 |
| 3:24-27 | MSG "Pedaiah son of Parosh ... Shemaiah son of Shecaniah ... Hananiah son of Shelemiah ... Hanun, the sixth son of Zalaph" | EN 부칭·서열 누락 (KO는 있음) | EN p11·p12 복원 |
| 4:3 | MSG "they have insulted the builders" | 슬랭·첨가 | EN p2 'dissing ... to their faces' → 'insulted the builders' |
| 4:13-14 | MSG "fight for your brothers" | EN 오역 | EN p8 'your families' → 'your brothers' |
| 4:21 | MSG "from first light until the stars came out" | EN 세부 누락 | EN p11 'from sunup to sundown' → 'from sunup until the stars came out' |
| 5 (제목) | — (슬랭 R1) | 슬랭 | EN/KO 제목 'Nehemiah Goes OFF on the Rich Bullies' → 'Nehemiah Calls Out the Rich Bullies' |
| 5:14-16 | MSG "forty shekels of silver (about a pound) a day" | EN 숫자 누락 (KO는 있음) | EN p11 'forty shekels of silver (about a pound)' 복원 |
| 6:10 | MSG "Shemaiah son of Delaiah, the son of Mehetabel, at his house" | EN/KO 부칭·장소 누락 | EN p8·KO p8 복원 ('들라야의 아들이자 므헤다벨의 손자인 스마야') |
| 6:17-19 | MSG "son-in-law of Shecaniah son of Arah ... his son Jehohanan had married the daughter of Meshullam son of Berekiah" | EN 부칭·이름 누락 (KO는 있음) | EN p14 복원 |
| 7:1-2 | — (슬랭 R1) | 슬랭 | EN p0 'no cap' 제거 |
| 7:70-72 | MSG "1,000 drachmas of gold (about 19 pounds), 50 bowls, 530 garments ... 20,000 drachmas of gold and 2,200 minas of silver (about 1⅓ tons) ... 20,000 drachmas of gold (about 375 pounds), 2,000 minas of silver, 67 garments" | EN 숫자·단위 누락 (KO는 있음) | EN p72 3건 복원 |
| 8:5-6 | MSG "Oh yes! Yes!" | EN/KO 인용구 오역 | EN p3·KO p3 ''Amen! For real!''/''아멘! 아멘!'' → ''Oh yes! Yes!''/''오 그래! 그래!'' |
| 8:7-8 | MSG "Jeshua, Bani, Sherebiah, Jamin, Akkub, Shabbethai, Hodiah, Maaseiah, Kelita, Azariah, Jozabad, Hanan, and Pelaiah" | EN 이름 10명 누락 (KO는 있음) | EN p4 복원 |
| 9:1-3 | — (슬랭 R1) | 슬랭 | EN p0 'unfriended' → 'cut off all ties' |
| 9:16-19 | MSG "Moses, your servant" | 슬랭 | EN p4 'your boy Moses' → 'Moses, your servant' |
| 9:24-25 | MSG "cisterns" | EN 오역 (KO '물탱크'는 정확) | EN p7 'wells' → 'cisterns' |
| 10:9-13 | — (슬랭 R1) | 슬랭 | EN p2 'their boys' → 'their fellow Levites' |
| 10:31 | — (슬랭 R1) | 슬랭 | EN p8 'No cap' 제거 |
| 10:32-33 | MSG "one-third of a shekel (about an eighth ounce)" / "the Dedication-Offerings" | EN 세율·제물 누락 (KO는 있음) | EN p9 복원 |
| 10:37-39 | MSG "the best of our grain" | EN/KO 오역 | EN p12·KO p11 'dough'/'밀가루 반죽' → 'grain'/'곡식' |
| 11:25-30 | MSG "Zorah" (25-30 목록) | EN/KO 지명 누락 | EN p28·KO p28 'Zorah'/'소라' 문단 신규 추가 |
| 11:31-36 | MSG "Aijah" (31-36 목록) | EN/KO 지명 누락 | EN p37·KO p37 'Aijah'/'아이야' 문단 신규 추가 |
| 11:31-36 | MSG "Hazor" (31-36 목록) | EN/KO 지명 누락 | EN p41·KO p41 'Hazor'/'하솔' 문단 신규 추가 |
| 12:40-42 | MSG "Hashaiah" | EN/KO 오타 | EN p55·KO p55 'Hoshaiah'/'호세야' → 'Hashaiah'/'하사야' |
| 12:40-42 | MSG "his brothers Shemaiah, Azarel, Milalai, Gilalai, Maai, Nethanel, Judah, and Hanani" | EN/KO 이름 8명 누락 | EN p55·KO p55 복원 |
| 13 (제목) | — (슬랭 R1) | 슬랭 | EN/KO 제목 'Nehemiah Cleans House, No Cap' → 'Nehemiah Cleans House' |
| 13:1-3 | — (슬랭 R1) | 슬랭 | EN p0 'GOAT'·''Aight, bet,'' 제거 → 'God flipped the curse into a blessing' / 'they excluded all the foreigners from Israel' |
| 13:4-5 | MSG "the grain offerings, incense, worship vessels, and the tithes of grain, wine, and oil for the Levites, singers, and security guards, plus the offerings for the priests" | EN 세부 누락 (KO는 있음) | EN p1 복원. 'boys with this dude Tobiah' → 'close friends with Tobiah' / KO p1 '도비야라는 애랑' → '도비야라는 사람이랑' |
| 13:10-13 | MSG "Why has God's Temple been abandoned?" / "Hanan son of Zaccur, the son of Mattaniah" | 슬랭·EN/KO 부칭 누락 | EN p3 'ghosted' → 'abandoned', 부칭 복원 / KO p3 '삭굴의 아들이자 맛다냐의 손자인 하나냐' 복원 |
| 13:17-18 | — (슬랭 R1) | 슬랭 | EN p6 'dissing the Sabbath' → 'profaning the Sabbath' |
| 13:19 | MSG "As the gates of Jerusalem were darkened by the shadows of the approaching Sabbath" | EN 첨가 (Friday) | EN p7 'as the sun started to set on Friday' → MSG 표현 복원 (KO는 원래 정확) |
| 13:20-21 | — (슬랭 R1) | 슬랭 | EN p8 'went off on them' → 'confronted them' |
| 13:29 | MSG "how they defiled the priesthood" | 슬랭 | EN p14 'trashed' → 'defiled' (KO '더럽혔습니다'는 정확) |
| — | — (순화, 에스라 '걔네'→'그 사람들' 선례) | 순화 | KO '걔네/걔가/걔네들' → '그 사람들/그 사람이' 13건 (ch4 p4/p7/p9, ch6 p8/p9/p11/p13/p14×2, ch9 p5, ch13 p0/p8/p12), '애들' → '사람들' 4건 (ch6 p0, ch9 p4, ch10 p4, ch13 p1/p3), '녀석' → '새끼' 1건 (ch10 p10), '대박' 2건 (ch2 p7 삭제, ch7 p37 '진짜 많네'), '지들' 1건 (ch3 p1) |

슬랭 스캔 결과 유지 판정: EN의 bro(다수)·chill 등은 정상 문맥으로 유지. KO의 '쟤네'(인용구 내 지시어)는 유지.

## merge/split 목록

- merge: 없음 (0건).
- split: 32건 선언 (아래). 전부 (a) MSG 대비 내용 온전, (b) EN/KO 일치, (c) 가독성 목적의 순수 구조 차이를 만족하는 스탠딩 승인 규칙에 따라 선언 후 진행.
  - ch1: 1-2→p0-1, 10-11→p6-7
  - ch2: 4-5→p2-3, 6→p4-5, 17-18→p11-12
  - ch4: 10→p5-6
  - ch5: 7-8→p4-5, 12-13→p8-10
  - ch6: 9→p6-7, 10→p8-9
  - ch7: 6-60→p4-65, 61-63→p66-69
  - ch10: 1-8→p0-1, 28-30→p4-6, 31→p7-8, 37-39→p12-13
  - ch11: 4-6→p2-3, 7-9→p4-5, 10-14→p6-7, 15-18→p8-9, 19→p10-11, 25-30→p16-34, 31-36→p35-45
  - ch12: 1-7→p0-8, 8-9→p9-11, 10-11→p12-17, 12-21→p18-38, 23-24→p40-44, 25-26→p45-52
  - ch13: 20-21→p8-9, 22→p10-11, 30-31→p15-16

## 승인 필요 항목

- 없음. 내용 방향이 모호한 수정 없음. merge 후보 없음.

## 게이트 통과 여부

| 게이트 | 결과 | 비고 |
|---|---|---|
| 1. MSG 전수 대조 | 수행 | 1–13장 전수 수동 대조 + 고유명사/숫자 기계 검사. MSG 원문 결함 없음 (재수집 불필요) |
| 2. 수정 반영 | 수행 | EN 42문단·KO 28문단 본문 수정 + 제목 2건 + 지명 3문단 신규 추가. changes[]에 전건 기록 |
| 3. validate_translation.py | PASS | "13개 장 모두 통과" |
| 4. 기계적 완전성 | PASS | 316문단·이름 755개·숫자 113개 검사. FAIL 21건 전수 대조 후 전부 오탐으로 판정 (completeness_fp_Nehemiah.md) |
| 5. build_gdocs.py | OK | 316행, msg_units=154, teen_without_msg=0, msg_orphans=0, VERIFY_DROPPED=0 |
| 6. verify_pairing_content.py | OK | 316 data rows, PAIRING CONTENT OK (마태 1장식 짝지음 사고 없음) |
| 7. Google Docs 업로드 + API 검증 | OK | 신규 Doc 생성 '느헤미야 (Nehemiah): MSG + Teen EN + KO', 테이블 13/13, export-back VERIFIED OK |

- Docs 링크: https://docs.google.com/document/d/1oMSWLcCvKhj0L6ayEUQBhPU07fMcRUjXL82d3_QCSl4/edit?usp=drivesdk

## 검증 범위 (확인한 것)

- validator PASS (배지 null/커버리지/중복/EN-KO parity/merge 컨펌/욕설 스크리닝).
- 슬랭 전수 스캔: EN 319문단+제목 13건, KO 319문단+제목 13건.
- EN-KO parity: 장 수 13=13, 문단 수 319=319, 장 순서 일치, verseRanges 1:1 일치, 제목 동기화, msg_ranges/splits/merges 1:1 일치.
- msg_ranges 13장 전부가 MSG 실제 문단 경계와 일치 (parse_msg_txt 기준).
- ch11 지명 3문단 추가 후 EN/KO 인덱스·배지·split 동기화 확인 (25-30→p16-34, 31-36→p35-45).
- ch12 중복 문단 없음 확인 (p12 족보 1회만 존재 — 요약본이 아닌 MSG 원문 기준 1회).

## 미확인 경계 (확인하지 못한 것)

1. **문장 단위 뉘앙스** — 게이트 1은 전수 수동 대조이나, teen paraphrase의 문체·어휘 선택 자체는 감사 대상 아님.
2. **월명 의역** — Kislev→December(ch1), Nisan→April(ch2)은 teen 의역으로 유지 (FP-1·FP-4).
3. **"Temple of God" → "Temple"** — 소유격 'of God' 생략 3건(ch8 p10, ch11 p9, ch13 p1)은 문맥상 자명하여 오탐 판정 (FP-8·13·19).
4. **production 반영** — 구약 감사본은 앱에 반영하지 않음 (지시).
5. **완료 선언** — 7개 게이트를 통과했으나, "완료/final" 선언은 성욱만 가능.
