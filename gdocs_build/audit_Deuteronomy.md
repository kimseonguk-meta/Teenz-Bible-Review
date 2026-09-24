# 신명기 (Deuteronomy) — MSG 기준 전수 감사 리포트

- 감사일: 2026-09-24
- 기준: Eugene Peterson, The Message (MSG) 영어 원문
- 대상: 신명기 1–34장, Teen EN + Teen KO
- 원문 파일: `msg_Deuteronomy.txt`
- 원칙: 의도적 요약 금지 / EN이 primary, KO는 EN과 내용·톤·구조 1:1 / 고유명사·숫자·인용 반복 보존 / 과도한 슬랭 순화

## 0. 감사 범위

- MSG↔Teen EN/KO 전수 대조: 1–34장
- 기계 완전성 검사(completeness_check.py): 고유명사·이름·숫자·인용구 전수 대조
- validator (`validate_translation.py`): PASS (34장)

## 1. MSG 원문 검증·정정

- 5:7-33(십계명), 32:6-52(모세의 노래) 복원분을 BibleGateway MSG 원문과 대조 → 일치 확인
- **33:29 오염 발견·정정**: 복원 과정에서 RSV("Happy are you, O Israel!...")가 혼입되어 있었음. 진짜 MSG("Lucky Israel! Who has it as good as you?...")로 원문 파일 정정, Teen EN/KO 마지막 문단도 MSG 기준으로 재작성
- MSG 자체 라벨 겹침 확인 (BibleGateway 대조): 21장 1-8/8-9, 26장 5-10/10-11, 28장 47-48/48-52 — Teen이 1:1로 따른 것이므로 validator 오탐 면제 처리

## 2. validator 보강

- 비속어 목록에 slut·whore 추가 (정당한 누락 수정)
- Genesis·Leviticus·Numbers 재실행 → 전부 PASS, 기존 책 영향 없음

## 3. 성욱 승인 구조 선언 (2026-09-24)

- **건 A — 5장 merge 1건**: MSG 십계명 10개 묶음(7, 8-10, 11, 12-15, 16, 17, 18, 19, 20, 21)을 Teen이 '7-21' 한 문단으로 합친 기존 구조. 계명 10개 전부 포함 확인됨. merges 선언 + confirmations_needed 기재
- **건 B — splits 30건 (현행 유지)**: MSG 한 묶음을 Teen이 2~3문단으로 나눈 기존 구조. 내용 손실 없음
  - 5장: 23-24 → v23 서술 / v24-26 인용
  - 6장: 쉐마(4) → "Attention, Israel!" / "God, our God! God the one and only!"
  - 7장: 1-2(3문단), 5(2문단), 12-15(v12/v13/v14-15)
  - 8장: 11-16, 9장: 1-2, 14장: 21, 15장: 12-15·18, 16장: 1-4, 19장: 1-3, 23장: 7
  - 26장: 12-14, 16-19
  - 27장: 14-26 저주+아멘 25문단
  - 28장: 1-6 축복 선언(3문단), 15-19
  - 31장: 14-15
  - 33장: 지파별 축복 11건 (지파명 문단 / 본문 문단 분리: 르우벤·유다·레위·베냐민·요셉·스불론/잇사갈·갓·단·납달리·아셀) + 서론 1-5

## 4. 빌드·짝지음 검증

- `build_gdocs.py Deuteronomy`: 34장, 440행, VERIFY_DROPPED=0, teen_without_msg=0, msg_orphans=0
- PAIRING_MISMATCHES 2건 — 둘 다 [MSG_SUPERSET] (선언된 split의 정상 렌더링):
  - ch5 '23': MSG 셀에 23-24 단위 표시 (split 선언됨)
  - ch7 '14-15': MSG 셀에 13-15 단위 표시 (split 선언됨)
- `verify_pairing_content.py`: 440행 전수 OK

## 5. Google Docs

- 신규 생성: "신명기 (Deuteronomy): MSG + Teen EN + KO"
- API 테이블 수 34/34, export-back VERIFIED

## 미확인 경계

- 실제 Docs 웹 화면 렌더링은 환경상 직접 확인 불가 (API 테이블 수 + export-back으로 검증)
