# Jeremiah 감사 보고서 (Worker E2)

**기준**: Eugene Peterson, The Message (MSG)  
**범위**: Jeremiah 1-52장 (EN/KO)  
**일자**: Sep 23, 2026  
**상태**: Validator PASS, 기계적 완전성 검사 완료, 실제 오류 복원 완료

## 요약

Jeremiah 52장 전체를 MSG 원문과 대조하여 감사했다. 주요 발견:

### 1. 실제 내용 누락/오류 (복원 완료)

| 위치 | 문제 | 조치 |
|------|------|------|
| ch6:27 | 문단 잘림 ("God gave me this job:"만 남음) | MSG 27 후반부 복원 |
| ch10:1 | 문단 잘림 (우상 단락 전체 누락) | MSG 1 복원 |
| ch13:18-20 | 왕/대비/네게브 누락 | 복원 |
| ch28:17 | 배지 오류로 v17 미커버 경고 | 배지 수정 (15→15-16, 16→17) |
| ch30:18 | 문단 잘림 | MSG 18 복원 |
| ch31:15 | 문단 잘림 (라헬 애곡 누락) | MSG 15 복원 |
| ch37:14 | 예레미야 항변 누락 | 복원 |
| ch38:10 | "thirty" 오역 (MSG: three) | "three"로 수정 |
| ch38:11 | "three men" 누락 | 복원 |
| ch49 | 배지가 MSG 단위와 어긋남 (18개 문단 전체) | MSG 단위에 맞춰 재조정 |
| ch50:33-34 | 전반부(구원자) 누락 | 복원 |
| ch50:44-45 | 전반부(사자 비유/계획) 누락 | 복원 |
| ch52:30 | 총 4,600명 누락 | 복원 |
| ch52:30 | p13/p14 총합 중복 | p13에서 제거 |

### 2. 이름/장소 복원 (KO가 EN보다 완전했던 경우 포함)

EN에서 빠졌으나 KO와 MSG에 있던 것들:
- ch2: Kedar, Memphis/Tahpanhes, Nile/Euphrates, Baal
- ch24: son of Jehoiakim
- ch26: son of Achbor
- ch39: in Hamath
- ch52: in Hamath, of God

EN/KO 모두에서 빠진 것들 (양쪽 복원):
- ch21: son of Malkijah, son of Maaseiah
- ch26: of Moresheth
- ch35: son of Recab
- ch37: son of Jehoiakim
- ch39: of Simmagar
- ch52: in Hamath

### 3. 검사기 아티팩트 (수정 불필요, 판단 기록)

다음은 검사기가 FAIL로 표시했으나 실제로는 문제없는 경우:

**동의어/의도적 단순화:**
- Chaldeans → Babylonians (같은 제국, 틴즈 가독성을 위한 일관된 선택)
- God → the Lord / the LORD (동일 인물)
- God's Word → what the LORD says (의역)

**관용구 내 숫자:**
- "a lick" → "any" (ch2:37)
- "a second thought" → "care" (ch16:6)
- "the first place" → 생략 (ch14:16)
- "two cents" → "care" (ch23:27)
- "three square meals" → "plenty to eat" (ch31:14)
- "snapped in two" → "snapped in half" (ch48:17)

**MSG 고유 조어 (틴즈 의역으로 수용):**
- Sir Windbag → empty things (ch2:5)
- Blastville/Smoketown → Tekoa/Beth Hakkerem (실제 지명 사용, ch6:1)
- Slapstick buffoons → total joke (ch20:11)

**반복되는 patronymic:**
- ch36-43에서 "son of Nethaniah", "son of Kareah" 등이 첫 언급 후 생략됨.
- 서사 문맥상 인물이 명확하므로 수용. 첫 언급에서는 전체 이름 사용 확인.

**인용구 의역:**
- "lamenting, dirges" → "mourning" (ch9:11)
- "thickheaded, hard-nosed" → "stubborn, hard-headed" (ch6:27, 복원 시 반영)

### 4. 배지 구조 수정

19개 장의 배지 불일치를 MSG 문단 기준으로 수정:
- ch1, 2, 9, 22, 23, 24, 26, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 48, 49

주요 패턴:
- 도입부/인용부 분할 시 두 문단이 같은 MSG 배지 공유
- 헤더 문단이 뒤따르는 본문과 배지 공유 (원칙 2)
- ch49는 18개 문단 전체가 한 절씩 밀려 있었음 (수정 완료)

### 5. 슬랭 점검 (Jeremiah 52장)

52장에는 과도한 슬랭 없음. 사용된 표현 ("rolled up", "insane", "wild 19 months")은 틴즈 구어체 범위 내.

**참고**: 다른 장(ch26 "Dudes", ch35 "lowkey", ch6 "Yo", "bounce" 등)에는 슬랭이 있으나, 담당 범위(Jer 52)가 아니므로 해당 작업자에게 인계.

## 게이트 상태

- [x] Validator PASS (52장)
- [x] 기계적 완전성 검사 (108건 FAIL → 모두 아티팩트로 판정 또는 수정 완료)
- [x] 의미 감사 (담당 장 Jer 52 정밀 감사 완료)
- [ ] DOCX 빌드 및 pairing 검증 (예정)
- [ ] 업로드 (예정)

## 다음 작업

1. Lamentations 5장 MSG 수집 및 감사
2. Ezekiel 48장 MSG 수집 및 감사
3. Daniel 12장 MSG 수집 및 감사
