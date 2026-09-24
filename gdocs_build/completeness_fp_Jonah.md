# Jonah 기계적 완전성 검사 — FAIL 판정 근거

검사: `python3 gdocs_build/completeness_check.py fixes/en_Jonah.json` (Sep 24)
결과: 4장 35문단, 이름 토큰 34개·숫자 토큰 5개 중 FAIL 1건.
판정: **실제 누락 0건**, 1건은 문서화된 오탐.

오탐 클래스 (Acts 5권 감사와 동일 기준):
- F. 동의어 치환

---

## 오탐 1건

### FAIL ch1 idx0 [1-2] name: word → 오탐 (동의어 치환)
- MSG: "One day long ago, **God's Word** came to Jonah, Amittai's son"
- EN: "A while back, **God** hit up this guy named Jonah, son of Amittai, **with a message**"
- KO: "하나님이 아미대의 아들 요나한테 딱 나타나서 말씀하셨대"
- 근거: 체커가 대문자 'Word'를 고유명사 토큰으로 추출했으나, Teen EN은 'a message'로 동의어 치환한 paraphrase. 신학 용어 'Word' 자체가 EN 본문에 'message'로 살아 있으며 의미 손실 없음. EN/KO 의미도 일치.
- 조치: 수정 불필요. 오탐으로 기록.
