# DOCX MSG 본문 결손 스캔 결과 (2026-09-23)

## 방법
- `gdocs_build/*.docx` 전체(26개)를 열어 모든 테이블 행 검사.
- Teen 행(EN 셀이 절 번호로 시작) 중 MSG 셀이 배지만 있고 본문이 없는 행 = `missing`(진짜 결손).
- MSG 셀이 `↑ 위 MSG(...) 계속` 표시만 있는 행 = `continuation`(의도된 병합 표시, 정상).

## 결과 — 작업자 A 7권
| DOCX | missing (진짜 결손) | continuation (정상) |
|---|---|---|
| Habakkuk.docx | 12 (T0R8:14-16, T0R9:17, T1R4:4, T1R7:9-11, T1R8:12-14, T1R9:15-17, T1R10:18-19, T1R11:20, T2R4:3-7, T2R5:8-16, T2R6:17-18, T2R7:19) | 3 |
| Jonah.docx | 30 (1장 3-17절 대부분, 2장 3-10, 3장 3-11) | 2 |
| Nahum.docx | 11 (1장 7-15, 2장 2-13, 3장 5-19) | 0 |
| Haggai.docx | 23 (1장 2-15, 2장 4-19) | 1 |
| Obadiah.docx | 4 (2-4, 5-14, 15-18, 19-21) | 1 |
| Ruth.docx | **0** | 19 |
| Zephaniah.docx | 13 (1장 2-13, 2장 3-15, 3장 6-20) | 0 |

## 결과 — 그 외 19개 DOCX (신약 등, 다른 작업자)
- `missing`이 있는 파일: **0개**. continuation-by-design 행만 존재.
- 즉 이 빌드 결함은 **작업자 A의 구약 DOCX 6권에만** 나타남 (Ruth 제외).

## 원인 (확정)
- `build_gdocs.py`의 `expand_inline_markers()`가 한 물리적 줄 안의 인라인 절 마커(`* * * 14-16`, `3 But Jonah...` 등)를 분리하지 못함.
- 그 결과: 앞 절의 MSG 본문에 뒤 절들이 통째로 붙고, 뒤 Teen 행의 MSG 셀은 배지만 남고 본문이 비게 됨.
- 기존 verifier는 Teen 문단 누락만 검사하고 MSG 셀 본문 결손을 검사하지 않아 PASS로 통과함.

## 필요한 조치
1. `build_gdocs.py` MSG 파서 근본 수정 (코디네이터와 조율 — 공유 스크립트 독단 수정 금지).
2. verifier에 "배지만 있고 본문 없는 MSG 셀 = FAIL" 게이트 추가.
3. 위 6권 DOCX 재빌드 → Google Doc 재업로드 → workerA 레지스트리 export_back 갱신.
4. Ruth.docx는 구조상 정상이므로 재빌드 불필요 (슬랭 재감사만 별도).
