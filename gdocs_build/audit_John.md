# Teenz Bible 의미 감사 리포트 — 요한복음 (John 1–21장)

- 감사일: 2026-09-22
- 범위: 요한복음 전 21장, § 헤더 제외 모든 Teen 본문 문단
- 방법: build_gdocs.py의 `match_msg_for_teen()`으로 각 Teen 문단에 매칭된 MSG 원문을 대조
  1. Teen EN이 MSG의 모든 의미 요소(사실·인명/지명·인용 대사·논리 연결·경고·예언·명령·숫자)를 보존하는지
  2. KO가 EN의 1:1 번역인지 (의미 동등, 임의 추가/삭제 없음)
- 감사 수행: 1–7장 감사 에이전트 A, 8–14장 감사 에이전트 B, 15–21장 감사 에이전트 C — 구간별 독립 감사 후 원문 재확인으로 이슈 전수 검증
- 소스 JSON(`fixes/en_John.json`, `fixes/ko_John.json`)은 **수정하지 않음** (감사만 수행)
- § 헤더 행은 감사 제외, 경미한 스타일 차이는 이슈에서 제외

## 총평: 이슈 5건 (심각 1, 중간 1, 낮음~중간 1, 낮음 2)

요한복음 전체는 MSG 의미 보존이 전반적으로 매우 충실함. 1·2·5·6·7·8·9·10·11·12·13·14·15·16·17·18·19·20·21장의 대다수 문단은 이슈 없음. 이슈는 **3장과 4장**에만 집중됨 (3장 4건, 4장 1건).

---

## 이슈 1 — [요 3장, vr=16-18] KO에서 핵심 문장 통째로 누락 (심각)

- **MSG 원문 (문제 부분):**
  > "God didn't go to all the trouble of sending his Son merely to point an accusing finger, telling the world how bad it was. **He came to help, to put the world right again.** Anyone who trusts in him is acquitted; ..."
- **현행 Teen EN (문제 부분):**
  > "God didn't go through all that trouble of sending his Son just to point fingers and tell the world how messed up it was. **He came to help, to fix the world up again.** Anyone who trusts in him is declared innocent; ..."
- **현행 KO:**
  > "하나님이 아들을 보낸 건, 이 세상이 얼마나 나쁜지 막 손가락질하고 정죄하려고 보낸 게 아니라고요. 누구든지 아들을 믿으면 죄를 용서받지만, 아들을 안 믿는 사람은 이미 옛날에 사형선고 받고도 그걸 모르는 사람이에요. 하나뿐인 하나님의 아들을 알면서도 안 믿었으니까요."
- **누락/문제 내용:** EN/MSG의 "He came to help, to fix the world up again"(아들이 세상을 돕고 다시 바로잡으러 오셨다)는 아들의 사명을 설명하는 핵심 긍정 명제가 KO에 통째로 빠졌다. "보내신 게 아니다"라는 부정만 남고 "왜 보내셨는가"가 사라져 의미가 반쪽이 됨. 요 3:17의 핵심 복음 논리 손실.
- **수정 방향:** KO에 "아들이 오신 이유는 세상을 돕고, 망가진 세상을 다시 바로잡기 위해서다"라는 의미를 반드시 복원할 것. 추가로 "죄를 용서받지만"은 EN의 "declared innocent"(무죄 선언)와 뉘앙스가 다르니 "무죄로 선언된다" 쪽으로 맞출 것.

## 이슈 2 — [요 4장, vr=21-23] EN에서 MSG의 의미 요소 하나 누락 (중간)

- **MSG 원문 (문제 부분):**
  > "But the time is coming—it has, in fact, come—when **what you're called will not matter and** where you go to worship will not matter."
- **현행 Teen EN (문제 부분):**
  > "But the time is coming—in fact, it's already here—**when where you worship won't matter.**"
- **현행 KO:** EN을 그대로 따름 ("어디서 예배하느냐가 중요하지 않은 때가") — EN 문제의 파급.
- **누락/문제 내용:** MSG는 "무엇이라 불리느냐(what you're called = 민족·종파적 정체성/호칭)"와 "어디서 예배하느냐" 두 가지가 모두 중요하지 않게 된다고 말하는데, EN은 후자만 남기고 전자를 삭제. 사마리아인 vs 유대인이라는 문맥에서 "호칭/정체성" 요소의 소실은 의미 손실.
- **수정 방향:** EN에 "네가 무엇이라 불리든(사마리아인이든 유대인이든) 중요하지 않게 될 때"라는 요소를 복원할 것. KO는 EN 수정 후 동일하게 반영.

## 이슈 3 — [요 3장, vr=7-8] KO의 자의적 해석 추가 (낮음~중간)

- **MSG 원문 (문제 부분):**
  > "So don't be so surprised when I tell you that you have to be 'born from above'**—out of this world, so to speak.**"
- **현행 Teen EN (문제 부분):**
  > "So, don't be so shocked when I tell you that you've got to be 'born from above'**—like, out of this world, if that makes sense.**"
- **현행 KO (문제 부분):**
  > "그러니까 '위에서부터 태어나야 한다', **다시 말해 이 세상의 가치관 같은 거에서 벗어나야 한다**는 제 말에 너무 놀라지 마세요."
- **누락/문제 내용:** EN의 "out of this world"는 MSG 그대로의 관용적 표현("이 세상 바깥에서" / 놀라움을 나타내는 말버릇)인데, KO가 이를 "이 세상의 가치관에서 벗어나야 한다"로 단정적으로 해석·추가. EN/MSG 어디에도 "가치관"이라는 단어나 '벗어남'의 의미는 없음. 1:1 번역 원칙 위반 (가공/추가).
- **수정 방향:** KO에서 "이 세상의 가치관 같은 거에서 벗어나야 한다"는 해석을 삭제하고, EN의 "out of this world"를 관용 그대로("이 세상 밖에서", 또는 놀라움을 나타내는 말버릇) 옮길 것.

## 이슈 4 — [요 3장, vr=34-36] KO에서 "angry" 수식어 누락 (낮음)

- **MSG 원문 (문제 부분):**
  > "All he experiences of God is darkness, **and an angry darkness at that.**"
- **현행 Teen EN (문제 부분):**
  > "All they experience of God is darkness, **and a really angry darkness at that.**"
- **현행 KO (문제 부분):**
  > "그 사람이 하나님에 대해 경험하는 거라고는 **온통 깜깜한 어둠뿐**이에요."
- **누락/문제 내용:** "angry darkness"(하나님의 진노가 담긴 어둠)라는 수식이 KO에서 빠지고 "깜깜한 어둠"만 남음. 심판의 성격(진노)이 약화됨.
- **수정 방향:** KO에 "화난/진노의" 의미를 복원할 것. 예: "(하나님의) 진노가 담긴 어둠".

## 이슈 5 — [요 3장, vr=5-6] KO에서 "baptism" 단어 누락 (낮음)

- **MSG 원문 (문제 부분):**
  > "Unless a person submits to this original creation—the 'wind-hovering-over-the-water' creation, the invisible moving the visible, **a baptism into a new life**—it's not possible to enter God's kingdom."
- **현행 Teen EN (문제 부분):**
  > "Unless a person totally gives in to this original creation—you know, like when the 'wind hovered over the water' at the very beginning, the invisible stuff moving the visible stuff, **a kind of baptism into a brand new life**—it's impossible to actually enter God's kingdom."
- **현행 KO (문제 부분):**
  > "…보이는 세상을 움직이는 보이지 않는 세상, **새로운 생명으로 들어가는 문을 열어주는 그런 세상** 말이에요."
- **누락/문제 내용:** EN/MSG의 "baptism into a new life"(새 생명 안으로의 세례)라는 핵심 어휘가 KO에서 "새로운 생명으로 들어가는 문을 열어주는 세상"으로 바뀌어 "세례(baptism)" 개념이 사라짐. 니고데모 담화 전체가 '다시 태어남/세례' 주제이므로 단어 손실이 아쉬움.
- **수정 방향:** KO에 "세례" 어휘를 복원할 것. 예: "새로운 생명으로 들어가는 세례 같은 것" (EN의 "a kind of baptism into a brand new life"에 맞춤).

---

## 장별 통과 요약

- **1장:** 전 구간 통과. "gift after gift after gift" 수사학적 반복 보존. "before the universe, before time itself"는 MSG "The Word was first"의 허용 가능한 풀어쓰기.
- **2장:** 전 구간 통과. 숫자(20~30갤런, 46년), 대사, 논리 연결 모두 보존.
- **3장:** 이슈 4건 (이슈 1, 3, 4, 5). 그 외 구간 통과. 참고: EN이 MSG에 없는 성경 참조 "(Numbers 21:8-9)"를 추가했으나 MSG 원문 요소가 아니므로 이슈 아님.
- **4장:** 이슈 1건 (이슈 2). 그 외 구간 통과. 사마리아 여인 대화 전체(대사·논리·"그분 오시면 다 알려주실 것") 보존.
- **5장:** 전 구간 통과. 긴 담화(19-47절)의 논리 구조(원인-결과·대조) 모두 보존.
- **6장:** 전 구간 통과. 빵/살/피 담화의 반복 강조("living Bread!") 보존.
- **7장:** 전 구간 통과. 초막절 논쟁의 인용문·대사·시간 순서("명절 절반쯤") 모두 보존.
- **8장:** 전 구간 통과. 간음 현장 여성 이야기(8:1-11)의 대사·행동·주석까지 충실. "not even a taste"(8:52) 수사적 강조 보존.
- **9장:** 전 구간 통과. "never been heard of—ever"(9:32) 강조 보존.
- **10장:** 전 구간 통과.
- **11장:** 전 구간 통과. 나사로 부활 대사·가야바의 예언("한 사람이 백성을 위해 죽는 게 유리하다" → 민족 + 흩어진 자녀를 모아 한 백성), 로마인의 정치 압박 논리, 에브라임 지명 모두 보존.
- **12장:** 전 구간 통과. "First they wouldn't believe, then they *couldn't*"(12:37) 강조 보존.
- **13장:** 전 구간 통과. "glory all around"(13:32) 보존.
- **14장:** 전 구간 통과. "he has nothing on me, no claim on me"(14:30) 보존.
- **15장:** 전 구간 통과. 포도나무/가지 비유, "너희는 이미 깨끗하다" 대조 논리 보존.
- **16장:** 전 구간 통과. 보혜사의 3중 책망(믿지 않음이 근본 죄 / 의는 위에서, 눈과 손이 닿지 않는 곳 / 세상 통치자의 재판과 유죄) 원인-결과 논리 온전.
- **17장:** 전 구간 통과. 대제사장적 기도 전체(기도 요청·영광·보존·연합) 보존.
- **18장:** 전 구간 통과. 기드론 시내·유다의 앞장섬·로마 군인+경찰+등불·횃불·칼, "누구를 찾고 있어?"↔"나사렛 예수" 2회 반복, 군인들의 움찔, "이 사람들은 가게 해줘", 말고의 오른쪽 귀, "아버지가 주신 이 잔", 안나스→가야바(장인 관계), 3회 부인+닭 울음, "죽일 권한 없음"(죽음 방식 예언 확인), "내 나라는 주위에 보이는 것으로 이루어진 게 아니야", "진리가 뭐요?", 바라바(유대인 독립투사) 모두 보존.
- **19장:** 전 구간 통과. 가시 면류관·자주색 옷·"유대인의 왕 만세!"·뺨 때림, "십자가에 못 박아!" 2회, "우리에게는 카이사르 외에 왕이 없소", 팻말 3개 언어(히브리·라틴·그리스), 대제사장들의 문구 수정 요구와 빌라도의 "쓴 것은 쓴 거요", 옷 4등분+이음새 없는 속옷+주사위(성경 확인 주석), 십자가 발치 4명의 여인, "여자여, 여기 당신 아들이에요"/"여기 네 어머니야", "목말라", 신 포도주+해면+창, "다 이루었다", 안식일 준비일+그해 큰 명절, 다리 꺾음(예수님은 이미 죽으심), 옆구리 창+피와 물, "뼈 하나도 꺾이지 않을 것이다"/"찌른 자를 쳐다볼 것이다", 아리마대 요셉(비밀 제자), 니고데모+몰약·침향 약 75파운드, 새 무덤. 숫자(75파운드) 정확.
- **20장:** 전 구간 통과. "주 첫날 이른 아침, 아직 어두울 때", 돌이 옮겨짐, 두 제자의 달리기(먼저 도착한 제자는 들어가지 않음), 삼베+머리 수건 따로 단정히 개켜짐, 두 천사(머리맡·발치), "랍오니!"(히브리어)+뜻풀이, "붙잡지 마… 내 아버지이자 너희 아버지", "성령을 받아라"+죄 용서/불용서 말씀, 도마의 3중 조건(못 자국 보기·손가락 넣어보기·옆구리에 손), "믿지 않는 자가 되지 마. 믿어", "제 선생님! 제 하나님!", "보지 않고 믿는 사람들에게는 더 좋은 복" 모두 보존.
- **21장:** 전 구간 통과. 디베랴 바다(갈릴리 호수), 7명의 제자 명단, "나 고기 잡으러 간다", 밤새 못 잡음, "아침 먹을 거 좀 잡았어?", 배 오른쪽 그물, 약 100야드, 숯불+생선+빵, "방금 잡은 생선 좀 가져와", 153마리 큰 물고기+그물이 찢어지지 않음, 세 번째 나타나심, "요한의 아들 시몬아" 3회 질문(어린 양 먹이기/양 돌보기/양 먹이기), "젊었을 때는… 늙으면 손을 뻗을 거야"(죽음 암시 주석), "나를 따라라", "그가 어떻게 돼요?"→"그게 너와 무슨 상관", 소문 정정, 목격자 기록의 신뢰성, "그런 책 도서관을 담을 만큼 큰 세상". 3회 반복 수사 구조와 숫자(153, 100야드) 정확.

## 참고 (이슈 아님 — 수정 불필요)

- [요 3장, vr=13-15] EN이 MSG에 없는 성경 참조 "(Numbers 21:8-9)"를 추가했으나, KO는 이를 옮기지 않음. MSG 원문 요소가 아니므로 이슈 아님.
- [요 5장, vr=34-36 추정] KO 문장 끝 닫는 따옴표 누락으로 보임. 의미 이슈는 아니나 다음 빌드 시 확인 권장.
- [요 8장, vr=46] KO에서 "a single misleading word, a single sinful act"가 "속임수" 하나로 합쳐졌으나 "말 하나·행동 하나" 구분은 유지되고 도전 취지 전달됨 — 임계값 이하.
- [요 8장, vr=25-26] KO에서 "trustworthiness"→"신실함". 문맥상 지장 없음 — 임계값 이하.
- [요 11장, vr=1-3] EN에서 MSG "so very much"의 "very" 탈락. 미세한 강조 약화이나 의미 요소 손실 아님 — 임계값 이하.
- 공유 MSG unit 구간(16:4, 19:24, 20:13·20, 11:34, 12:36, 13:12, 8:6)은 각 문단별 커버리지 개별 확인 — 전부 정상.

## 감사 범위 한계

- 본 감사는 Teen EN·KO 텍스트의 **의미 완전성**만을 다룸. 절 배지(verseRanges) 정확성, 병합(merge) 컨펌 여부, 구글닥 교체 업로드 상태는 본 리포트 범위가 아님.
- "이슈 없음" 판정은 위의 의미 요소 기준이며, 성욱의 문체 선호(슬랭·톤)에 대한 판단은 포함하지 않음.
