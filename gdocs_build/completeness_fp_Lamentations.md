# Lamentations 기계적 완전성 검사 — 잔여 FAIL 오탐 판정 근거

검사: `python3 gdocs_build/completeness_check.py fixes/en_Lamentations.json`
결과: 5장 94문단, 이름 토큰 36개·숫자 토큰 2개·인용구 1개 중 FAIL 3건 — 전수 대조 후 전부 오탐으로 판정. 실제 누락·요약·의미 반전 0건.

## 수정으로 해소된 실제 이슈 (오탐 아님 — 본문 수정 완료)

감사 과정에서 MSG 대조로 직접 복원한 내용 (fixes/en_Lamentations.json, fixes/ko_Lamentations.json 반영됨):
- ch1: '과부' 이미지(1절), '시온의 길이 운다' 의인화(4절), '딸 시온' 호칭(6절), '비웃고 또 비웃었다' 반복(7절), 인용문 'Worthless, cheap, abject!'(11절), 'Judgment Day'(21절)
- ch2: '딸 시온/딸 유다' 호칭(1·5·8·10절), '야곱'(3절), '안식일'(6절), '내장이 젤리처럼'(11절), 인용 호칭 'Most Beautiful'/'Best Place to Live'(15절), 인용문 'Here it is!'(16절), '회개하는 시온'(18절), '주님 자신의 성전'(20절), 'gone, gone, gone' 3연 반복(22절)
- ch3: '손을 잡고 칠흑 어둠으로'(1-3), '관 속에 못 박힌 시체'(4-6), '(계속계속 되뇌며)'(22-24), '가장 높으신 하나님의 법정'(34-36), '세상 나라들의 뒷마당'(43-45), '비가 와서 구덩이가 가득 참'(52-54), '날마다, 날마다, 날마다'(61-63)
- ch4: 배지 오기 정정 (EN 17번 '20'→'21', 18번 '20'→'22' / KO 6번 '7'→'7-8', 11번 '12-13'→'13', 19번 '21-22'→'22') + msg_ranges 동일 정정. '수염은 조각한 돌처럼'(7-8), '누더기'+인용문 '꺼져! 만지지도 마, 병 옮는다!'(14-15), '눈이 빠지게'+'망보는 사람'(17절), '우스 땅에서'+'벌거벗겨진 채로'(21절) 복원. MSG 7-8, 14-15 병합은 스탠딩 승인으로 merges 선언.
- ch5: MSG 단일 문단('5 1-22')→Teen 8문단 분할은 스탠딩 승인으로 splits 선언. '앗시리아와 이집트에 우리 자신을 팔아넘김'(4-6), '노예들이 우리를 다스림'(7-8, 해석 추가 삭제), '아내들이 강간당함'+'여자들이 하던 일'(11-13), '영광의 왕관'+'Woe! Woe!'(16-18) 복원. KO '꿀땅'→'소중한 땅', '빌붙기'→'팔아넘김', '맷돌 가는 일'(MSG에 없음)→'여자들이 하던 일' 정정.

---

## FAIL 1 — ch2 idx1 [badge 2] number: 2 (오탐)
- MSG: "2 The Master, without a second thought, took Israel in one gulp. ..."
- TEEN: "God didn't even hesitate. He just swallowed Israel whole, ..."
- 판정: 오탐. 체커가 MSG 파싱 텍스트 앞의 절 번호 라벨 "2"를 내용 숫자로 오인식. Teen 문단에 절 번호를 표기하지 않는 것은 정상 (배지로 표시).

## FAIL 2 — ch2 idx21 [badge 22] name: god (오탐)
- MSG: "...on the big day of God's wrath no one would get away."
- TEEN: "...on the day of your great anger, nobody escaped."
- 판정: 오탐. 하나님께 직접 말하는 기도문이라 "God's wrath" → "your great anger"는 정당한 teen paraphrase (동의어/인칭 전환). 의미 손실 없음.

## FAIL 3 — ch5 idx0 [badge 1-3] quote: dirges, toppled, heartsick (오탐)
- MSG 5장은 전체가 하나의 인용문("5 1-22 "..."")이라 체커가 장 전체의 핵심어(dirges=15절, toppled=16절, heartsick=17절)를 0번 문단(배지 1-3)에 귀속시킴.
- 실제 Teen 반영: "dirges" → 5번 문단(배지 14-15) "funeral marches", "toppled" → 6번 문단(배지 16-18) "The crown of glory has fallen", "heartsick" → 6번 문단 "heartbroken".
- 판정: 오탐. 인용구 귀속 단위(장 전체 인용문)와 Teen 문단 분할(8문단)의 단위 불일치로 인한 것. 각 토큰은 해당 배지 문단에 정상 반영됨.
