# Daniel completeness_check 오탐(False Positive) 기록

- 대상: `fixes/en_Daniel.json` (MSG = `msg_Daniel.txt`, parsed 177 units)
- 검사일: 2026-09-24
- 검사기: `gdocs_build/completeness_check.py`
- 최종 상태: FAIL 9건 전부 오탐으로 판정. 진짜 누락은 모두 복원 완료
  (복원 내역은 `gdocs_build/audit_Daniel.md` 참조).
- validator: `PASS: 12개 장 모두 통과`

## 오탐 판정 목록

1. ch2 idx6 [badge 12-13] `name: babylonian`
   - MSG: "the whole company of Babylonian wise men"
   - TEEN: "all the wise men in Babylon"
   - 사유: 표현 대응(paraphrase). 바빌론 지칭 의미 보존됨.

2. ch2 idx9 [badge 17-18] `name: babylonian`
   - MSG: "along with the whole company of Babylonian wise men"
   - TEEN: "along with all the other wise men in Babylon"
   - 사유: 1번과 동일, 표현 대응.

3. ch2 idx16 [badge 29-30] `name: revealer`
   - MSG: "The Revealer of Mysteries"
   - TEEN: "The God who reveals mysteries"
   - 사유: 칭호 paraphrase. 의미 동일.

4. ch3 idx2 [badge 7] `name: nebuchadnezzar`
   - MSG: "the gold statue that King Nebuchadnezzar had set up"
   - TEEN: "the gold statue the king had set up"
   - 사유: 절(clause) 자체는 보존됨. 문맥상 "the king" = 느부갓네살로 모호하지 않음.

5. ch3 idx3 [badge 8-12] `name: nebuchadnezzar`
   - MSG: "They said to King Nebuchadnezzar, 'Long live the king!'"
   - TEEN: "went to the king to snitch... They were like, 'Hey, King, hope you live forever!'"
   - 사유: 호칭 대상이 문맥상 명확. 의미 손실 없음.

6. ch9 idx8 [badge 20-21] `number: 1`
   - MSG: "the humanlike Gabriel, the one I had seen in an earlier vision"
   - TEEN: "Gabriel, the humanlike guy I'd seen in an earlier vision"
   - 사유: "one"은 대명사(관계대명사 선행사), 수량이 아님. 관계절 의미 보존됨.

7. ch11 idx11 [badge 21-24] `name: arbitrarily`
   - MSG: "Arbitrarily and impulsively, he'll invade the richest provinces."
   - TEEN: "He'll just randomly invade the richest areas."
   - 사유: "Arbitrarily"는 문장 첫머리 대문자 부사이지 고유명사가 아님. 의미 대응됨.

8. ch11 idx17 [badge 36-39] `name: contemptuous`
   - MSG: "Contemptuous of every god and goddess, the king of the north will puff himself up..."
   - TEEN: "He'll look down on every god and goddess and hype himself up..."
   - 사유: "Contemptuous"는 문장 첫머리 대문자 형용사이지 고유명사가 아님. 의미 대응됨.

9. ch11 idx18 [badge 40-45] `name: unleashing`
   - MSG: "Unleashing chariots and horses and an armada of ships, he'll blow away anything in his path."
   - TEEN: "with chariots, horses, and a whole fleet of ships, destroying everything in his way."
   - 사유: 분사구문 → 전치사구 paraphrase. 전차·기병·함대 요소 전부 보존됨.

## 참고: 검사 과정에서 실제 복원한 항목 (오탐 아님)

- 3장: 악기 6종 전부 복원(trumpets, trombones, tubas, baritones, drums, cymbals),
  "all the musical instruments of Babylon", "Babylonian fortune-tellers" 복원
- 4장: "witches", "divine Holy Spirit", "Then your good life will continue"(maybe 삭제),
  "twelve months later", "four corners of the Earth/world" 2곳 복원
- 5장: "heaven's dew" 복원
- 7장: "tens of thousands attended him" 복원 (EN+KO)
- 8장: "charging first west" 복원
- 9장: EN/KO 전면 재작성 (NIV식 paraphrase → MSG teen voice, Holy of Holies → 지성소 등)
- 10장: "no seasoning", "great Tigris", "Stand at attention", "Master," 복원
- 11장: "the two of them", "his rule, reputation, and authority already in shreds",
  "and the citadel", "cleanse", "like dominoes" 복원
