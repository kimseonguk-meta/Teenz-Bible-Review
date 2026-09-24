# 출애굽기 (Exodus) — MSG 전수 감사 리포트

- 감사일: 2026-09-23
- 작업자: C
- 기준: Eugene Peterson, The Message (MSG) 영어 원문 — `msg_Exodus.txt` (bible-history.com MSG 40장 전장)
- 방식: MSG 539개 문단을 1:1로 대조하며 Teen EN 신규 작성 → KO를 EN에 1:1로 번역 (문단 수·배지·순서·소제목 동일)
- 원칙: 의도적 요약 금지 (축약 금지), 소제목은 별도 문단으로 두되 뒤따르는 본문과 절 배지 공유, merge/split은 성욱 컨펌 없이 적용하지 않음

## 요약

- 40장 전체를 MSG 기준으로 전수 대조. 기존 production 텍스트는 사용하지 않고 MSG에서 새로 작성.
- MSG 문단 539개 → Teen EN/KO 문단 539개 + 소제목 행. 누락 문단 0.
- 수정 1건 (4:10), MSG 자체 문단 경계에 따른 절 나눔 선언 6건 (편집적 변경 아님).
- 게이트 1–7 전부 통과.

## 장별 이슈와 수정 내용

### 4:10 — 수신자 누락 복원 (실제 수정 1건)
- MSG 요지: "Moses raised another objection to God" — 모세가 하나님께 또 이의를 제기함.
- 문제 유형: 수신자(to God) 누락. Teen 초안이 "Moses tried another excuse:"로 하나님께 말한다는 점이 희미했음.
- 수정 내용:
  - EN: "Moses tried another excuse on God:"
  - KO: "모세가 하나님께 또 변명을 댐:"
- 발견 경로: 기계적 완전성 검사(completeness_check) 이름 토큰 대조에서 발견 → MSG와 직접 대조 후 수정.

### MSG 자체 문단 경계에 따른 절 나눔 6건 (선언만, 구조 변경 없음)
MSG 원문의 문단 경계가 아래 절들을 가로지르므로, Teen도 MSG 경계를 그대로 유지하고 validator `splits` 필드에 선언함. 편집적 split이 아님. `merge-split-candidates.md`에 Ex1–Ex6으로 pending 기록.
- 6:6 — MSG [2-6]/[6-8] 경계 ("I've remembered my covenant..." / "I am God. I will bring you out...")
- 13:13 — MSG [11-13]/[13-16] 경계 (나귀 첫새끼 속전 / "Redeem every firstborn child among your sons")
- 16:15 — MSG [13-15]/[15-16] 경계 (만나를 보고 "What is it?" / "It's the bread God has given you to eat")
- 17:6 — MSG [5-6]/[6-7] 경계 ("Water will gush out..." / "Moses did what he said")
- 22:3 — MSG [1-3]/[3-4] 경계 ("if it happens after daybreak, there is bloodguilt" / "A thief must make full restitution")
- 29:9 — MSG [5-9]/[9-14] 경계 (제사장 위임 종료 / "This is how you will ordain Aaron and his sons")

### completeness_check 12건 — 전수 대조 결과 모두 오탐으로 판정
아래는 검사기가 토큰 불일치로 지적했으나 MSG와 직접 대조한 결과 의미·수치가 모두 보존된 경우:
- 단복수 토큰 차이: 2:7 Hebrews→"Hebrew woman", 3:9-10 Israelite→"Israelites'", 6:24 Korahites→"Korahite families", 3:7-8·3:16-17·13:4-5 여섯/다섯 족속명 → Teen에 복수형으로 전부 존재 ("Canaanites, Hittites, Amorites, Perizzites, Hivites, Jebusites")
- 숫자 단어형 표기: 4:8-9 "two signs"→"both signs", 12:14-16 "day one"/"Days one and seven" 전부 존재, 18:17-23·18:24-27 "thousands, hundreds, fifties, and tens" 전부 존재, 18:1-4 "One was named Gershom" 존재
- 관용구 paraphrase: 2:14 "Word's got out"→"People know about this" (의미 동일)

## 게이트 결과

1. MSG 전수 대조 감사: 통과 (40장, MSG 539 유닛 전수 대조, 이슈 리포트 본 문서)
2. 수정 반영: 통과 (수정 1건 반영, merge/split 미적용·6건은 선언만)
3. validate_translation.py: PASS — 40개 장 모두 통과 (배지 null 없음, MSG 절 커버리지 완전, EN/KO 문단·배지 1:1, 욕설 스크리닝 통과)
4. 기계적 완전성 검사: PASS — 539문단·이름 토큰 554개·숫자 토큰 277개·인용 4건 대조, 13건 중 1건 실제 수정·12건 오탐 판정 (위 기록)
5. build_gdocs.py: 통과 — 40장·596행·MSG 유닛 539개, teen_without_msg=0, msg_orphans=0, VERIFY_DROPPED=0
6. verify_pairing_content.py: 통과 — 40개 표·539개 데이터행, exit 0 + 실제 셀 내용 짝지음 육안 확인 (1장 앞부분·40장 마지막행)
7. Google Docs 업로드: 통과 — 제목 일치, 표 40개, export-back 검증 (아래 참조)

## 업로드 정보

- 제목: 출애굽기 (Exodus) — Final: MSG + Teen EN + KO
- 폴더 ID: 1I7rLOsUgbr5Ewyq7-IEshCk20scIBtPn
- 결과 파일: `gdocs_build/upload_results_workerC.json` (공유 upload_results.json은 동결되어 있어 workerC 파일에만 기록)

## 검증 범위와 미확인 경계

- 검증함: MSG 텍스트 40장 전수 대조, validator exit 0, DOCX 빌드 무누락, 표 40개·행 단위 pairing 내용 대조, Docs API 제목·표 개수 확인, export-back DOCX 재검증 (표 40개·빈 Teen 셀 없음·무누락).
- 미확인: Google Docs 웹 화면의 실제 렌더링 (API/export 검증까지만 수행 — 이 환경에서 브라우저 화면 확인 불가).
- MSG 출처: bible-history.com MSG 페이지 (작업 시작 전 확보된 `msg_Exodus.txt`, 40장). KJV 미사용.

---

# Exodus 2차 재감사 기록 (2026-09-25)

담당: subagent (Exodus + Joshua). 기준: msg_Exodus.txt (수정 없음).

## 방법
1. `python3 gdocs_build/completeness_check.py fixes/en_Exodus.json` → 11건 후보 전수 분류
2. MSG ↔ Teen EN 문장 단위 전수 수동 대조 (40장, 539 MSG 유닛 vs 596 teen 행)

## 결과: 복원 0건

### 체커 11건 — 전부 오탐 (의미 동등)
| 위치 | 체커 지적 | 판정 |
|---|---|---|
| ch2 [8] hebrews | "from the Hebrews" → "a Hebrew woman" | 의미 동등 |
| ch2 [15] word | "Word's gotten out" → "People know about this" | 의미 동등 |
| ch3 [7-8] 6 nations | 단수/복수 토큰 불일치 | 전부 존재 (복수형) |
| ch3 [9-10] israelite | "The Israelites' cry" | 존재 |
| ch3 [16-17] 6 nations | 단수/복수 토큰 불일치 | 전부 존재 (복수형) |
| ch6 [25] korahites | "Korahite families" | 의미 동등 |
| ch12 [14-16] number 1 | "first day" → "day one" | 존재 |
| ch13 [4-5] 5 nations | 단수/복수 토큰 불일치 | 전부 존재 (복수형) |
| ch18 [1-4] number 1 | "The name of the one" → "One was named" | 존재 |
| ch18 [17-23] 10/50/100/1000 | "thousands, hundreds, fifties, tens" 단어형 | 전부 존재 |
| ch18 [24-27] 10/50/100/1000 | 동상 | 전부 존재 |

### 수동 대조 — 누락 없음
- 족보(ch6): 12명/137년/133년/137년, Korah 3형제, Elisheba(Amminadab 딸·Nahshon 누이), Putiel 딸 등 호칭 전부 존재
- 10재앙: 인용구·반복("Just as God had said")·숫자(600전차, 7일, 430년, 600,000명) 전부 존재
- 성막 지시/제작(ch25-40): 치수·재료·보석 4행(12종)·은 6,437파운드/603,550명/100밑받침 등 숫자 전부 존재
- 비대칭(KO만 있고 EN 없음) 패턴 미발견
- 모호 케이스: 없음

## 게이트
- validate_translation.py → PASS (40장)
- build_gdocs.py Exodus → 40 tables, VERIFY_DROPPED=0, msg_orphans=0, teen_without_msg=0
- verify_pairing_content.py → PAIRING CONTENT OK (539 rows, 40 tables)
- docx 재빌드 → 내용 동일 (rsid 메타데이터만 차이) → 원상복구, 커밋/Doc 재업로드 불필요

JSON 변경 없음. 커밋 없음 (0건 복원 → 빈 커밋 금지). Google Doc(40 tables) 변경 없음.

### 2026-09-25 추가 — 위 "0건" 판정 정정: 사용자 제공 후보 5건 재검증 결과 실제 5건 복원
(9-24 체커 11건 분류 때는 후보로 올라오지 않았던 것들로, MSG·EN·KO 직접 대조로 확정.)

| 장:절 | MSG | 문제 | 수정 |
|---|---|---|---|
| 13:19 | "God will surely hold you accountable" | EN "God will surely come to your aid" — 의미가 다름 (실제 오역) | EN: "God will surely hold you accountable" / KO: "하나님이 반드시 너희에게 책임을 물으실 것이니" |
| 16:1-3 | "lamb stew" | EN "meat stew" / KO "고기 가마" — lamb 세부 누락 | EN: "lamb stew" / KO: "양고기 가마" |
| 17:4 | "Any minute now they'll kill me!" | EN "they'll stone me!" / KO "돌로 칠 것 같아요" — MSG에 없는 구체성 추가 | EN: "they'll kill me!" / KO: "저를 죽일 것 같아요" |
| 25:37-38 | "Make seven of these lamps for the Table." | EN "Make seven of these lamps." / KO "이 등잔 7개를 만들어라." — "for the Table" 누락 | EN: "Make seven of these lamps for the Table." / KO: "이 등잔 7개를 상을 위해 만들어라." |
| 37:7-9 | "two winged angel-cherubim" | EN 첫 문장 "two angel-cherubim" — 반복 세부(winged) 누락 | EN: "two winged angel-cherubim" / KO: "날개 달린 천사 그룹" |

수정 후 게이트 재실행 예정: validate → build → pairing → docx 재빌드 → Doc 재업로드(40/40 + export-back VERIFIED OK) → "Final" 제목 제거 확인 → Exodus 4파일 커밋·push.

