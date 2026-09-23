# Ezra 10장 감사 보고서

**기준**: Eugene Peterson, The Message (MSG)
**범위**: Ezra 1–10장 (Teen EN / Teen KO, 각 192문단)
**일자**: Sep 24, 2026
**상태**: MSG 원문 부재로 전수 대조 미완 — 아래 "미확인 경계" 참조. "완료" 아님.

## 결론

- msg_Ezra.txt가 작업 디렉토리에 존재하지 않음 (작업 지시의 "존재하지만" 전제와 다름). msg_work/ezra_chNN.txt 수집은 코디네이터 별도 진행 중 — 본 보고서를 통해 코디네이터에게 보고함.
- MSG 없이 수행 가능한 감사(슬랭 6 Rule 전수, EN-KO parity, 배지/msg_ranges 정합성, validator)는 수행했고, 총 16건 수정 반영. validator PASS 유지.
- 게이트 1(MSG 전수 대조)·4(기계적 완전성)·5(빌드)·6(짝지음)·7(업로드)은 MSG 소스 부재로 미수행 — MSG 확보 후 후속 작업 필요.

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

슬랭 스캔 결과 유지 판정: EN의 chill(8:32-34)·bro(다수)·왕따 없음은 R6에 따라 변경 금지로 유지. ch6 p15 'ate the Passover meal'의 ate는 정상 용법으로 유지.

## 게이트 통과 여부

| 게이트 | 결과 | 비고 |
|---|---|---|
| 1. MSG 전수 대조 | 미수행 | msg_Ezra.txt 없음. 이전 세션(9-22) MSG 대조 changes[] 로그의 정합성만 리뷰 |
| 2. 수정 반영 | 수행 | 16건 반영, merge/split 신규 적용 없음 |
| 3. validate_translation.py | PASS | 수정 전·후 모두 "10개 장 모두 통과" |
| 4. completeness_check.py | 미수행 | MSG 소스 필요 |
| 5. build_gdocs.py (VERIFY_DROPPED=0) | 미수행 | msg_Ezra.txt 필요 (FileNotFound로 빌드 불가) |
| 6. verify_pairing_content.py | 미수행 | 빌드 산출물 필요 |
| 7. Google Docs 업로드 + API 검증 | 미수행 | docx 산출물 필요 |

## 검증 범위 (확인한 것)

- validator PASS (배지 null/커버리지/중복/EN-KO parity/merge 컨펌/욕설 스크리닝).
- 슬랭 6 Rule 전수 스캔: EN 192문단+제목 10건, KO 192문단+제목 10건, R1–R6 패턴 + 추가 슬랭 패턴(no cap/GOATED/slay/lowkey 등) + KO 비속/은어 패턴.
- EN-KO parity: 장 수 10=10, 문단 수 192=192, 장 순서 일치, verseRanges 1:1 일치, 제목 동기화.
- msg_ranges 10장 전부가 build_ezra_patch.py 문서의 MSG 문단 경계(2026-09-22 BibleGateway 직접 확인 기록)와 일치 — ch2의 61 분리(제사장 가문) 포함.
- 이전 세션 MSG 대조 변경 로그(changes[]) 전수 열람 — 배지 수정·복원 내역이 일관되게 기록됨. 단, 아래 "5가지 누락" 목록 자체는 작업 디렉토리에서 특정하지 못함.

## 미확인 경계 (확인하지 못한 것)

1. **MSG 전수 대조 자체** — msg_Ezra.txt가 없어서 MSG 문장 단위 완전성 검사를 수행하지 못함. 이전 세션의 MSG 대조(9-22) 결과를 신뢰 전제로만 둠.
2. **KO ch1 p4 [7-10] '은제 칼 29개' vs EN '29 silver pans'** — EN-KO 불일치. MSG 확인 후 KO를 EN(MSG)에 맞출지 결정 필요. 이번 세션에서는 변경하지 않음.
3. **EN ch10 p1 [2-3] 'Shecaniah' — 'son of Jehiel' 누락 여부** — KO에는 '여히엘 아들 스가냐'로 있음. EN-KO 비대칭, MSG 확인 필요.
4. **EN ch10 p10 [15-17] 'Jonathan / Jahzeiah' — 부친명('son of Asahel', 'son of Tikvah') 누락 여부** — KO에는 부친명 포함. MSG 확인 필요.
5. **체크포인트의 "이전에 지정된 5가지 누락"** — 어떤 5건인지 지목된 목록을 찾지 못함. changes[]의 복원 기록(Zechariah son of Iddo ×2, 'wept loudly for joy', Shethar-Bozenai, 에스라 계보 복원 등)이 해당할 가능성이 있으나 확정하지 않음.
6. **게이트 5–7 (빌드/짝지음/업로드)** — MSG 확보 후 수행 필요.

## 다음 단계 (코디네이터용)

- msg_work/ezra_chNN.txt 수집 완료 후 assemble → msg_Ezra.txt 생성되면, 본 작업자(또는 후속 세션)가 게이트 1·4·5·6·7 수행 + 위 미확인 2–4번 해소 가능.
- 그때까지 fixes/en_Ezra.json, fixes/ko_Ezra.json은 현 상태로 동결 권장.
