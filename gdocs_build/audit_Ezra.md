# Ezra 10장 감사 보고서

**기준**: Eugene Peterson, The Message (MSG)
**범위**: Ezra 1–10장 (Teen EN / Teen KO, 각 192문단)
**일자**: Sep 24, 2026
**상태**: MSG 전수 대조 완료, 7개 게이트 전부 수행. "완료" 선언은 성욱만 가능 — 본 보고서는 수행 결과 기록.

## 결론

- **MSG 원문 결함 발견·복원**: 수집된 msg_Ezra.txt에서 Ezra 3:11 찬양 문구(`Yes! God is good! Oh yes—he'll never quit loving Israel!`)와 3:11-13 본문(환호·울음·멀리 퍼진 소리)이 누락돼 있었음. 공개 MSG 페이지(bible-history.com/msg/ezra-3)에서 본문 존재를 직접 확인하고 msg_work/ezra_ch03.txt에 복원 후 assemble로 msg_Ezra.txt 재조립 (10장, 34,756→35,170자).
- MSG 확보 후 게이트 1–7 전부 수행. 이번 세션에서 EN 20건·KO 8건, 총 28건 수정 반영. validator PASS 유지.
- 이전 세션(슬랭·순화·EN-KO 불일치 16건)과 합산하면 이번 감사 라운드 총 44건 수정.

## 수정 이슈 표

| 장:절 | MSG 요지 / 근거 | 유형 | 수정 내용 |
|---|---|---|---|
| 4:4-5 | — (슬랭 R1) | 슬랭 | EN p2 'kill the vibe' → 'harassing the people of Judah and discouraging them' |
| 6 (제목) | — (슬랭 R1) | 슬랭 | EN/KO 제목 'The King's Decree? No Cap, It's GOATED!' → 'The King's Decree? Green Light to Build!' |
| 4:4-5 | — (슬랭 R5) | 슬랭 | KO p2 '멘탈을 막 흔들기' → '마음을 막 흔들기' |
| 9:3 | — (슬랭 R5) | 슬랭 | KO p1 '완전 멘붕이 온 거임' → '너무 충격받아서 정신이 하나도 없었어' |
| 1:5-6 외 | — (순화, ch4 p11 '걔네'→'그 사람들이' 선례) | 순화 | KO '걔네/걔네들' → '그 사람들' 9건 (ch1 p2, ch4 p0/p7/p9×2/p12, ch9 p0×2) |
| 6:21 | — (순화) | 순화 | KO p15 '이방의 더러운 것들' → '이방의 더러운 풍습' |
| 9:10-12 | EN 확정문 'get strong, enjoy the good things in the land, and leave a solid inheritance' | EN-KO 불일치 | KO p5 '부자가 되고, 자식들에게 물려줄 재산을 쌓을 수 있을 것이다' → '강해지고, 이 땅의 좋은 것을 누리며, 자식들에게 든든한 유산을 남길 수 있을 것이다' |
| 10:4 | EN 'Don't chicken out' | 순화 | KO p2 '쫄지 마세요' → '겁먹지 마세요' |
| 10:17 | 왕宛 편지 하십시오체 (KO ch5 p4 '평안하십시오' 선례) | 순화 | KO p9 '확인 좀 해주셈/알려주셈' → '확인해 주십시오/알려 주십시오' |
| 1:7-10 | MSG '29 silver pans', EN '29 silver pans' | KO 오역 | KO p4 '은제 칼 29개' → '은 쟁반 29개' |
| 3:8-9 | MSG 'Zerubbabel son of Shealtiel ... Jeshua son of Jozadak' | EN 부칭 누락 | EN p4 부칭 복원 |
| 5:1-2 | MSG 'Zerubbabel son of Shealtiel ... Jeshua son of Jozadak' | EN/KO 부칭 누락 | EN p0·KO p0 부칭 복원 ('스알디엘의 아들 스룹바벨이랑 요사닥의 아들 예수아') |
| 5:3 | MSG 'governor of the land beyond the Euphrates' | EN 지명 누락 (KO는 있음) | EN p1 'governor of the area' → 'governor of the land beyond the Euphrates' |
| 5:4 | MSG 'restore it to use' / 'told them the names' | EN/KO 세부 누락 | EN p1·KO p1 'rebuild' → 'rebuild ... and put it back to use' / '다시 짓고 원래대로 쓰라고'; EN 'who was in charge' → 'the names of the guys running' |
| 5:6-7 | MSG 'governor of the land beyond the Euphrates' | EN 지명 누락 (KO는 있음) | EN p3 'Tattenai, the governor' → 'Tattenai, the governor of the land beyond the Euphrates'; KO p3 '총독 다드래' → '유프라테스 강 서쪽 총독 다드래' |
| 5:8 | MSG 'with timbers fitted into the walls' | EN 세부 누락 (KO는 있음) | EN p5 'with huge stones and timbers' → 'with huge stones, with timbers fitted into the walls' |
| 5:9-10 | MSG 'restore it to use' | EN/KO 세부 누락 | EN p6·KO p6에 'put it back to use' / '원래대로 쓰라고' 복원 |
| 5:11-12 | MSG 'A great king of Israel built it, the entire structure' | EN/KO 세부 누락 | EN p7 'built the whole thing' / KO p7 '전체를 다 지었던' 복원 |
| 5:11-12 | MSG 'Nebuchadnezzar, king of Babylon, the Chaldean' | EN/KO 세부 누락 | EN p7 'the Chaldean' / KO p7 '갈대아 사람' 복원 |
| 5:13-16 | MSG 'carted off and put in the Babylon temple ... removed them from the temple of Babylon' | EN/KO 세부 누락 | EN p8·KO p8 바빌론 신전 경유 세부 복원 |
| 6:3-5 | — (슬랭 R1) | 슬랭 | EN p3 'yoinked' → 'took' |
| 6:6-7 | MSG 'you, Shethar-Bozenai, and the rest' | EN 이름 누락 (KO는 있음) | EN p4에 Shethar-Bozenai 복원 |
| 6:13 | MSG 'Tattenai the governor, Shethar-Bozenai, and the rest' | EN 이름 누락 (KO는 있음) | EN p10에 Shethar-Bozenai 복원 |
| 7:6-7 | MSG 'temple slaves' | EN/KO 정합성 (KO '막일꾼' 유지 가능) | EN p1 'temple workers' → 'temple servants' |
| 7:24 | MSG 'temple servant' | EN 정합성 (KO '성전 종' 이미 정확) | EN p7 'temple worker' → 'temple servant' |
| 10:1 | — | EN 정확성 | EN p0 'Israeli men' → 'Israelite men' |
| 10:2-3 | MSG 'Shecaniah son of Jehiel ... the spokesman' | EN 부칭·역할 누락 (KO는 있음) | EN p1 'Shecaniah son of Jehiel ... stepped up as spokesman' 복원 |
| 10:6 | MSG 'Jehohanan son of Eliashib' | EN 부칭 누락 (KO는 있음) | EN p4 부칭 복원 |
| 10:7-8 | MSG 'in compliance with the ruling of the leaders and elders' | EN 누락 (KO는 있음) | EN p5 'the leaders and elders ruled that ...' 복원 |
| 10:15-17 | MSG 'Jonathan son of Asahel and Jahzeiah son of Tikvah' | EN 부칭 누락 (KO는 있음) | EN p10 부칭 복원 |

슬랭 스캔 결과 유지 판정: EN의 chill(8:32-34)·bro(다수)·왕따 없음은 R6에 따라 변경 금지로 유지. ch6 p15 'ate the Passover meal'의 ate는 정상 용법으로 유지.

## 게이트 통과 여부

| 게이트 | 결과 | 비고 |
|---|---|---|
| 1. MSG 전수 대조 | 수행 | 1–10장 전수 수동 대조 + 고유명사/숫자 기계 검사. MSG 원문 결함 1건 발견·복원(아래 참조) |
| 2. 수정 반영 | 수행 | EN 20건·KO 8건(총 28건) 반영, merge/split 신규 적용 없음 |
| 3. validate_translation.py | PASS | "10개 장 모두 통과" |
| 4. 기계적 완전성 | PASS | MSG 고유명사/숫자 전수 추출 후 Teen EN 대조. 실제 누락은 전부 수정 반영, 나머지 32건은 오탐(절 번호·문장 첫 단어·정당한 teen paraphrase) |
| 5. build_gdocs.py | OK | 192행, msg_units=105, teen_without_msg=0, msg_orphans=0, VERIFY_DROPPED=0 |
| 6. verify_pairing_content.py | OK | 192 data rows, PAIRING CONTENT OK (마태 1장식 짝지음 사고 없음) |
| 7. Google Docs 업로드 + API 검증 | OK | 신규 Doc 생성 '에스라 (Ezra): MSG + Teen EN + KO', 테이블 10/10, export-back VERIFIED OK |

## 검증 범위 (확인한 것)

- validator PASS (배지 null/커버리지/중복/EN-KO parity/merge 컨펌/욕설 스크리닝).
- 슬랭 6 Rule 전수 스캔: EN 192문단+제목 10건, KO 192문단+제목 10건, R1–R6 패턴 + 추가 슬랭 패턴(no cap/GOATED/slay/lowkey 등) + KO 비속/은어 패턴.
- EN-KO parity: 장 수 10=10, 문단 수 192=192, 장 순서 일치, verseRanges 1:1 일치, 제목 동기화.
- msg_ranges 10장 전부가 build_ezra_patch.py 문서의 MSG 문단 경계(2026-09-22 BibleGateway 직접 확인 기록)와 일치 — ch2의 61 분리(제사장 가문) 포함.
- 이전 세션 MSG 대조 변경 로그(changes[]) 전수 열람 — 배지 수정·복원 내역이 일관되게 기록됨. 단, 아래 "5가지 누락" 목록 자체는 작업 디렉토리에서 특정하지 못함.

## MSG 원문 결함 복원 (이번 세션 발견)

- 수집된 msg_Ezra.txt에 Ezra 3:11 찬양 문구와 3:11-13 본문이 빠져 있었음 (HTML 추출기 결함).
- 공개 MSG 페이지(bible-history.com/msg/ezra-3)에서 `Yes! God is good! Oh yes—he'll never quit loving Israel!` 및 11-13절 본문(환호·울음·멀리 퍼진 소리) 존재를 직접 확인.
- msg_work/ezra_ch03.txt에 복원 후 `assemble_msg_book.py ezra 10`으로 재조립 → msg_Ezra.txt 10장, 35,170자. (commit 전)

## 미확인 경계 (확인하지 못한 것)

1. **문장 단위 뉘앙스** — 게이트 1은 전수 수동 대조이나, teen paraphrase의 문체·어휘 선택 자체는 감사 대상 아님.
2. **KO '다드래' 표기** — Tattenai의 KO 음역이 5장·6장에서 '다드래'로 고정돼 있음. 책 내 일관성은 유지되나 표준 음역('닷드내' 등)과의 대조는 하지 않음.
3. **"And Sheshbazzar did it"(5:16)** — Teen이 'So Sheshbazzar laid the foundation...'으로 통합. 전이 문장이라 의도적 축소로 판단하지 않음.
4. **production 반영** — 구약 감사본은 앱에 반영하지 않음 (지시).
5. **완료 선언** — 7개 게이트를 통과했으나, "완료/final" 선언은 성욱만 가능.
