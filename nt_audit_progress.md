# 신약 나머지 22권 MSG 재감사 — 진행 현황 (2026-09-22~)

## 7-게이트 정식 감사 (2026-09-23~, AUDIT_PROMPT 기준)
| 책 | 게이트 1-8 | 이슈 | 수정 | merge/split 후보(신규) | Docs |
|---|---|---|---|---|---|
| Acts | 1-8 전부 통과 | 실제 1건(13:50-52 EN "two" 누락→복원), 오탐 22건 문서화 | EN 1건 | 0건 (기존 적용분 4+승인 1은 merge-split-candidates.md 기록) | 재업로드, API 28/28, export-back 407행 내용 대조 OK |
| Ephesians | 1-8 전부 통과 | 실제 3건(KO 2건: 6:5-8 'slave or free' 드리프트→복원, 3:14-19 'parcels out' EN primary 정정 / KO 타이틀 6장 부여), § 1:1 OK, 경미 3건 관찰 기록 | 텍스트 3건 | 2건 (ch2 1-6·ch3 v8 splits, pending 누적) | 재업로드, API 6/6, export-back VERIFIED OK |
| 1Corinthians | 1-8 전부 통과 | 실제 9건(EN 4건: 2:6-10 'on a cross'·2:14-16 'Isaiah'·1:22-25 Jews/Greeks 복원, 16:12 따옴표 / KO 5건: 14:20-25 의미반전·16:10-11 누락+반전·14:13-17 드리프트·13:1 오타·9:8-12 인용구), 오탐 1건 문서화, 메타 20건(msg_ranges=verseRanges) | 텍스트 9건 + 메타 20건 | 1건 (8:7 merge) | 재업로드, API 16/16, export-back 148행 내용 대조 OK |


## 역할 분리 (2026-09-22 13:30 SGT~)
- **내 담당 17권**: Acts, 1Corinthians, 2Corinthians, Galatians, Ephesians, 2Timothy, Titus, Philemon, Hebrews, James, 1Peter, 2Peter, 1John, 2John, 3John, Jude, Revelation
- **다른 총괄(824012c5) 담당 5권**: Philippians, Colossians, 1Thessalonians, 2Thessalonians, 1Timothy — 이 5권의 patch 파일은 손대지 않음
- 아래 "완료" 표의 Philippians/Colossians/1Thessalonians/2Thessalonians 4권은 역할 분리 전에 내 팀이 완료한 것 (validator PASS) — 824012c5에 인계
- 1Timothy는 내 감사 워커를 분리 직후 중지. 중지 시점에 en_1Timothy.json/ko_1Timothy.json이 이미 6장 전체·validator PASS 상태로 남아 있음 — 단, 해당 워커는 4대 원칙 기준으로 작업했고 원칙 5 미적용. 824012c5가 채택/재작업 판단할 것

## 완료 (validator PASS, 원칙 5 재점검 완료)
| 책 | 장 | 문단(EN/KO) | 복원 | 배지수정 | 삭제 | merge후보 |
|---|---|---|---|---|---|---|
| Titus | 3 | 17/17 | 1 | 9 | 5 | 0 |
| 2Timothy | 4 | 30/30 | 24 | 11 | 4 | 0 |
| Philemon | 1 | 9/9 | 2 | 3 | 2(창작헤더) | 0 |
| Jude | 1 | 13/13 | 13 | 10+ | 2 | 0 |
| 2John | 1 | 8/8 | 2 | 3 | 4 | 0 |
| 3John | 1 | 10/10 | 5 | 4 | 3 | 0 |
| James | 5 | 53/53 | 다수(2장이 최대) | null 6개 제거+정정 | 11(지어낸 헤더 7+임의 소제목 4) | 0 |
| 1Peter | 5 | 49/49 | 6 | 13 | 5 | 0 |
| 2Peter | 3 | 32/32 | 12 | 10 | 1 | 0 |
| 1John | 5 | 60/60 | ~45 | 9 | 4 | 0 |
| Galatians | 6 | 63/63 | 31 | 29 | 8 | 0 |
| Hebrews | 13 | 118/118 | 다수(11장·12장 전면 재구축) | null 제거+정정 | 가공 헤더 삭제 | 0 |
| Ephesians | 6 | 62/62 | 다수(4장 인용문·5장 찬송 복원 등) | 전 장 구조 재작성 | 지어낸 헤더 7 삭제 | 0 |
| 2Corinthians | 13 | 103/103 | 20 | 31 | 1 | 0 |
| Revelation | 22 | 233/233 | 다수(Whore→Prostitute 순화 등) | 배지 정정 | — | 0 (27건 2026-09-22 성욱 승인 → split 적용, 독 재업로드 완료) |
| 1Corinthians | 16 | 158/158 | 다수(13~15장 대규모 복원) | 배지 정정 | 지어낸 헤더 삭제 | 0 |
| Acts | 28 | 458/458 | 15 | 56 | 2 | 0 |
| ~~2Thessalonians~~ | 3 | 21/21 | 8 | 7 | 4 | 0 → 824012c5 인계 |
| ~~1Thessalonians~~ | 5 | 39/39 | 24 | 13 | 12 | 1 (4장 4-5+6-7, 분리 유지·컨펌 대기) → 824012c5 인계 |
| ~~Philippians~~ | 4 | 55/55 | 14 | 17 | 0 | 1 (3장 1절+무번호문단, 분리 유지·컨펌 대기) → 824012c5 인계 |
| ~~Colossians~~ | 4 | 46/46 | 8 | 11 | 8 | 0 → 824012c5 인계 |

원칙 5 재점검 (2026-09-22 13:30): 위 9권 patch의 본문 문단 전수 스캔 — 욕설·비속어·과도한 슬랭(썰/찢길/꿀잼/쌩까/놈들 등) 본문 내 잔류 0건. '쌩까'·'지랄' 등의 grep 히트는 changes 메모(제거 기록)에만 존재, 본문은 clean. validator(검사 7 포함) 9권 전부 PASS 재확인.

## 진행 중 (내 17권)
| 책 | 상태 |
|---|---|
| 전체 | 17권 전부 완료 — validator 전수 PASS |

## 대기 (내 17권 중)
Ephesians, 1Corinthians, Acts, Revelation — MSG 확보 후 감사팀 투입
