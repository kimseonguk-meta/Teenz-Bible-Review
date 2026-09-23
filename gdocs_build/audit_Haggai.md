# Haggai 감사 리포트 (2026-09-23, 작업자 A)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1.
검수 방법: MSG(raw 텍스트) vs EN vs KO 문단별 전수 대조 (2장, 29문단). 1차 감사 변경 이력 확인 후 잔여 이슈 직접 판정.
결과: 텍스트 수정 6건(EN 4, KO 2). merge/split 신규 후보 0건. 결론: **재감사 + 6건 수정**.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 요지 | 문제 유형 | 수정 내용 |
|---|---|---|---|
| 2:1-3 | "Tell Governor Zerubbabel son of Shealtiel and High Priest Joshua son of Jehozadak" | EN·KO 누락 | EN: "Governor Zerubbabel, High Priest Joshua" → "Governor Zerubbabel son of Shealtiel, High Priest Joshua son of Jehozadak". KO: "스룹바벨 총독이랑 여호수아 대제사장" → "스알디엘의 아들 스룹바벨 총독이랑 여호사닥의 아들 여호수아 대제사장" (1:1에 "son of Shealtiel/Jehozadak" 둘 다 있던 것을 2장에서 빠뜨림) |
| 2:5 | "Put into action the word I covenanted with you" | EN·KO 의미 약화 | EN: "Live out the promise I made with you" → "Live out the covenant I made with you". KO: "내가 했던 약속" → "내가 맺었던 언약" |
| 2:9 | "a place in which I will hand out wholeness and holiness" | EN 누락 (KO는 완전함 보유) | EN: "a place where I give out peace and holiness" → "a place where I give out wholeness and holiness" |
| 2:21-23 | "I will take you, O Zerubbabel son of Shealtiel, as my personal servant" | EN 누락 (KO는 스알디엘의 아들 보유) | EN: "I will take you, Zerubbabel, my servant" → "I will take you, Zerubbabel son of Shealtiel, my personal servant" |

### 1차 감사에서 이미 수정된 사항 (이번 감사에서 직접 확인, 유지)
- MSG 소제목 2개 추가 ("Caught Up with Taking Care of Your Own Houses", "This Temple Will End Up Better Than It Started Out", EN/KO)
- 1:1 도입부에 "son of Shealtiel"/"son of Jehozadak" 복원됨

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- "bushels of wealth" → EN "tons of wealth": 동일 의미 틴 의역.
- "blight" → EN "disease"/KO "병충해": 의미 보존.
- "the sign of my sovereign presence and authority" → EN "a symbol of my authority": 핵심 보존.
- 소제목 2개가 MSG와 1:1. 창작 헤더 없음.
- 챕터 타이틀 ("God's Calling You Out: Stop Making Excuses" / "하나님께서 너를 부르신다" 계열): 틴 스타일 창작 타이틀, 허용 범위.

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (ch1 11문단, ch2 18문단). null 배지 0.

## 3. merge/split 후보
- 신규 후보: **0건**.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (2장 29문단 전수, 직접 대조) |
| ② 수정 반영 | PASS (EN 4건, KO 2건, merge/split 미적용) |
| ③ validate_translation.py | PASS (exit 0) |
| ④ 기계적 완전성 검사 | PASS (27문단, 16 name tokens — 잔여 FAIL 5건 전부 오탐 문서화: 'word'는 MSG 파서가 학개 1장을 통째로 1개 유닛으로 묶어 [13]의 "That's God's Word"를 union에서 제외한 파서 아티팩트; 숫자 7·12·13/8·13·14는 MSG 인쇄본 절 번호; 'bushels'는 "tons of wealth" 의역; 'wholeness'는 [9] 문단이 attr에서 빠져 union 미포함된 파서 아티팩트 — 실제 EN에 "wholeness" 존재 확인) |
| ⑤ build_gdocs.py 재빌드 | PASS (VERIFY_DROPPED=0) |
| ⑥ verify_pairing_content.py | PASS + 실제 셀 내용 기준 짝지음 확인 (배지별 MSG↔EN↔KO 행 일치) |
| ⑦ Google Docs 업로드 + API 검증 | PASS (테이블 2/2, title 일치, export-back VERIFIED OK). Doc: 학개 (Haggai) — Final: MSG + Teen EN + KO, id 1RWLSEl-afs-exYFJLuCMpukSoLRg1FCl3IxBI0JGFXk |

## 5. 검증 범위 및 미확인 경계
- 검증한 것: MSG vs EN vs KO 전수 대조 2장, validator, completeness_check(오탐 문서화), DOCX 빌드, 짝지음 내용 검증, Google Docs 업로드 + API 테이블 수 + export-back 검증.
- 미확인: Google Docs 웹 화면은 이 환경에서 직접 보지 못함. 자동 욕설 목록 밖 미묘한 뉘앙스. production 앱 미접촉.
