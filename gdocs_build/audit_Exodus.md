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
