# 1John 감사 리포트 (2026-09-23)

기준: Eugene Peterson The Message(MSG) 영어 원문 = 최종 기준. Teen EN은 MSG 기준, KO는 EN과 문단·배지·의미 1:1. KJV는 후보 선별용.
검수 방법: MSG(5장 49개 유닛) vs EN vs KO 문단별 전수 대조 (5장, EN/KO 각각 60행). 3개 워커(ch1-2/ch3-4/ch5)가 전수 대조 후 지적 사항을 MSG·EN·KO 실제 텍스트로 다시 직접 확인하고 최종 판정.
결과: 텍스트 수정 8개 작업 단위(EN 3건, KO 타이틀 5건). merge/split 신규 후보 0건.

## 1. 장:절별 이슈 및 수정

| 장:절 | MSG 원문 | EN/KO 기존 | 문제 유형 | 수정 내용 |
|---|---|---|---|---|
| 2:7-8 | "freshly minted as it is **in both Christ and you**" | EN "because of what Christ is doing in you" / KO "그리스도와 너희 안에서 새롭게 피어나는 거거든" (살아 있음) | EN 축소 (KO에 있는데 EN에 없는 MSG 요소) | EN → "it is new in a fresh way — **freshly minted in both Christ and in you**: the darkness is fading..." |
| 3:16-17 | "This is how we've come to **understand and experience love**" | EN "This is how we've come to understand love" / KO "우리가 사랑을 알게 되고 경험하게 된 건" (살아 있음) | EN 축소 (KO에 있는데 EN에 없는 MSG 요소) | EN → "This is how we've come to **understand and experience love**: Christ gave up his life for us." |
| ch3 타이틀 | — | EN "honored ones in God's Squad" (소문자 h 시작) | 타이틀 표기 불일치 (다른 4장은 Title Case) | EN → "Honored Ones in God's Squad" |
| KO ch1~5 타이틀 | EN 타이틀 5개 | 전부 빈 문자열 `""` | EN-KO 구조 불일치 (원칙 4) | ch1 "진짜 MVP" / ch2 "진짜를 알아보는 법" / ch3 "하나님 팀의 영광받은 자들" / ch4 "가짜들을 알아봐" / ch5 "최고의 승리" |

### 직접 확인하고 유지로 판정한 사항 (수정 안 함)
- ch1: "Walk in the Light"(5절 앞) § 헤더 1:1. 1:8-10 "calling God a liar" 핵심 온전.
- ch2: § 헤더 4개 1:1("The Only Way to Know We're in Him", "Loving the World", "Antichrists Everywhere You Look", "Live Deeply in Christ"). KO "dear children" → "얘들아/사랑하는 아이들아" 혼용은 허용 범위.
- ch3: § 헤더 "When We Practice Real Love"(18-20 앞) 1:1. 타이틀 "Squad"는 허용 범위 틴 슬랭.
- ch4: § 헤더 3개 1:1. MSG "will, of course, not listen to us" → EN "simply won't listen" 유지.
- ch5: § 헤더 2개 1:1. "a fellow believer" / "death-defeating death" vs KO "죽음을 죽이는 죽음" 유지. doxology 온전.
- 욕·과도 슬랭: EN/KO 모두 0건 (이전 패스 정리 상태 유지).

## 2. 구조 검사
- EN/KO 문단 수·순서·배지 1:1 (5장 60행). null 배지 0.
- `verseRanges == msg_ranges` 일치 (EN/KO 동일). ch2 선언 splits(1-3, 12-14)는 MSG 절 겹침 그룹핑 허용 선언으로 구조와 일치.
- 고유명사 전수: Father/Son/Jesus Christ/Priest-Friend/Holy One/Evil One/Antichrist/Cain 전부 등장.

## 3. merge/split 후보
- 신규 후보: **0건**.
- ch2 splits(1-3, 12-14) 선언분은 MSG 구조와 일치 확인.

## 4. 검증 게이트 통과 현황

| 게이트 | 결과 |
|---|---|
| ① 의미 전수 감사 | PASS (5장 49 MSG 유닛 전수, 직접 대조) |
| ② 이슈 리포트 | PASS (위 8개 작업 단위) |
| ③ 수정 | PASS (EN 3건 + KO 타이틀 5건 적용, 정확한 문자열 매칭) |
| ④ validator | PASS (5개 장 모두 통과) |
| ⑤ 기계적 완전성 | FAIL 3건 → 전수 판정 후 **전부 오탐**: (a) ch2[3] badge 4-6 숫자 "1" — MSG "the one who keeps God's word" → EN "someone keeps God's word" 대명사 paraphrase (b) ch2 badge 12-13/13-14 숫자 "2" — MSG "a second reminder" → EN "One more reminder" paraphrase (c) ch3[4] badge 9-10 숫자 "1" — MSG "The one who won't practice righteous ways" → EN "anyone who doesn't practice what is right" paraphrase. 모두 의미 완전 보존 |
| ⑥ Docs 재빌드 | PASS (VERIFY_DROPPED=0, 60 rows, 5 tables) |
| ⑦ 실제 내용 짝지음 검증 | PASS (49 data rows, PAIRING CONTENT OK) |
| ⑧ Google Docs 재업로드/API+export-back 검증 | PASS (API table 5/5, export-back VERIFIED OK) |
