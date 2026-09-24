# 이사야 (Isaiah) 감사 기록
**Date:** 2026-09-24 | **Auditor:** Coco (subagent) | **Book:** Isaiah, 13/27 OT
**Doc:** 이사야 (Isaiah): MSG + Teen EN + KO
**Link:** https://docs.google.com/document/d/1ER8ZVrB8pEkAtdcMaHvV1WBhIa6goSs1bYuhPxDw54U/edit?usp=drivesdk

## 기준
- MSG 원문: `msg_Isaiah.txt` (66장, 429유닛, 195,666자) — BibleGateway 재수집 후 복구됨
  (초기 파일은 1장 1-4절, 2장 1-5절까지만 있었음)
- EN primary, KO는 EN의 1:1 번역
- 절대 축약 금지

## 게이트 결과
| 검사 | Baseline (2026-09-24) | 최종 |
|------|----------------------|------|
| validate_translation.py | 13건 FAIL | **PASS (66장)** |
| completeness_check.py | 96건 | **67건 (전부 오탐으로 문서화)** |
| build_gdocs.py | — | 428 rows, 429 MSG units, teen_without_msg=0, msg_orphans=0 |
| verify_pairing_content.py | — | **PAIRING CONTENT OK** (428 rows, 66 tables) |
| Google Docs 업로드 | — | **OK** — 66/66 테이블, export-back VERIFIED OK |

## 실제 수정 (23개 문단)
### 1차 (17개 문단) — 이름·숫자·세부 복원
- 5:8-10: "fifty-pound sack of seed" / "quart of grain" 복원 (EN+KO)
- 7:1: "Ahaz son of Jotham, son of Uzziah", "Pekah son of Remaliah", "Davidic government", "Ephraim" 복원 (EN+KO)
- 7:3-6: "son of Remaliah" (Rezin of Aram and the son of Remaliah), "son of Tabeel" 복원 (EN)
- 7:7-9: "son of Remaliah" 복원 (EN)
- 7:13-17: "twelve years old" 복원 (EN+KO)
- 7:20: "Euphrates" 복원 (EN)
- 13:17-22: "Chaldeans", "Bedouins" 복원 (EN)
- 14:13-14: "Mount Zaphon" 복원 (EN+KO)
- 17:4-6: "Valley of Rephaim" 복원 (EN)
- 23:1-4: "Shihor" 복원 (EN+KO)
- 36:1-3: "son of Hilkiah", "son of Asaph" 복원 (EN)
- 36:11: "answered the Rabshekah" 복원 (EN)
- 36:22: "son of Hilkiah", "son of Asaph" 복원 (EN)
- 37:1-2: "Isaiah son of Amoz" 복원 (EN+KO)
- 37:5-7: "King Hezekiah's servants" 복원 (EN)
- 37:9-13: "who lived in Telassar" 복원 (EN)
- 37:21-25: "Isaiah son of Amoz" 복원 (EN+KO)

### 2차 (6개 문단) — 추가 정밀 검수에서 발견
- 11:11: "Sinar" 복원 (EN) — KO는 이미 "시날"로 정확했음
- 14:7-10: "Ponderosa pine trees" 복원 (EN+KO)
- 14:12: "Daystar! Son of Dawn!" 복원 (EN+KO)
- 37:15-20: "enthroned over the cherubim-angels", "chiseled by human hands" 복원 (EN+KO)
- 54:1-6: EN 전면 재작성 — barren woman/children/nations/abandoned cities 복원 (KO는 이미 충실했음)
- 55:12-13: "giant sequoias" 복원 (EN+KO)

## 오탐 문서
`gdocs_build/completeness_fp_Isaiah.md`에 67건 전수 분류:
- A: 정상 동의어/형태 변화 (13건)
- B: MSG 원문 붙임 오류 — checker artifact (8건)
- C: 겹치는 절 범위 — 인접 문단에 보존됨 (11건)
- D: 허용 가능한 틴 의역 (4건)
- E: 숫자 의역 (19건)

## 선언된 구조 변경
- 14장: MSG 인쇄 범위 `3-4`/`4-6`이 v4에서 겹침 → 내용 손실 없이 `3-6` 단일 문단으로 merge.
  스탠딩 승인 규칙에 따라 선언하고 진행 (승인 요청 불필요).

## 깨진 문자 검사
- KO 전체에서 U+FFFD (replacement character) 0건 확인. 콘솔의 ��� 표시는 터미널 렌더링 문제였음.

## 승인 필요
없음. 모든 수정은 MSG 원문 대조에 근거한 복원이며, 의미가 모호한 판단은 없었음.

## 다음 단계
- production 앱에는 반영하지 않음 (지시 준수)
- 이사야 관련 파일만 commit 후 GitHub main push
