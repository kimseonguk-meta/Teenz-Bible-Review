# 1Kings completeness_check 오탐(False Positive) 기록

기준: Eugene Peterson MSG 원문. 아래 항목은 검사기가 토큰 미검출로 FAIL 처리했으나,
Teen EN이 의미를 온전히 살린 정당한 paraphrase이므로 수정하지 않음.
(검사: 2026-09-24, `python3 gdocs_build/completeness_check.py fixes/en_1Kings.json`)

## "the one" 대명사 → 숫자 1 오탐 (4건)
검사기가 MSG의 대명사 "the one"을 숫자 1로 추출하나, Teen은 문맥상 생략하거나 풀어씀.
- ch7 idx4 [9-12]: MSG "...just like the one (wall) in the porch of The Temple of God"
  → Teen "...just like the porch of God's Temple." (the one = the wall, 의미 보존)
- ch11 idx14 [37-39]: MSG "I'll build you a kingdom as solid as the one I built for David"
  → Teen "I'll build you a dynasty as solid as David's." (the one = a kingdom, 의미 보존)
- ch12 idx18 [31-33]: MSG "...a festival ... to compete with the one (festival) in Judah"
  → Teen "...to compete with the festival in Judah." (의미 보존)
- ch15 idx5 [18-19]: MSG "Let's make a treaty like the one (treaty) between our fathers"
  → Teen "let's be allies, just like our dads were." (의미 보존)

## "every last one of you" → 숫자 1 오탐 (1건)
- ch12 idx14 [22-24]: MSG "go back home, every last one of you"
  → Teen "Everyone go home." (의미 보존)

## God → 대명사 you 오탐 (2건)
기도문 맥락에서 God을 you로 받는 것은 정당한 paraphrase.
- ch3 idx4 [9]: MSG "Give me a God-listening heart"
  → Teen "Give me a heart that listens to you" (you = God, 솔로몬의 기도 맥락)
- ch8 idx28 [44-51]: MSG "they pray to God toward the city you chose"
  → Teen "they pray to you facing this city you chose" (you = God, 기도문 맥락)

## 표준 번역어 대체 오탐 (1건)
- ch8 idx2 [6-9]: MSG "the Holy of Holies" → Teen "the Most Holy Place" (표준 영어 성경 용어)

## 인용구 핵심어 paraphrase 오탐 (4건)
검사기는 인용구 내 distinctive word의 일정 비율 이상 일치를 요구하나,
아래는 모두 Teen voice의 정당한 바꿔쓰기로 의미가 완전히 보존됨.
- ch9 idx2 [6-9]: MSG "repudiate this Temple I've just sanctified"
  → Teen "reject this Temple I've just made sacred for my Name"
- ch16 idx0 [1-4]: MSG "plodded in the way of Jeroboam" / "make me seethe" / "sweep them away like cinders"
  → Teen "kept doing the same dumb stuff" / "making me seriously angry" / "completely destroy them"
- ch19 idx5 [8-9]: MSG "Nourished by that meal, he walked forty days and nights"
  → Teen "That one meal gave him enough energy to walk for forty days and forty nights"
- ch20 idx9 [12]: MSG "Drunkenly, he ordered"
  → Teen "Super drunk, he just yelled, 'Get 'em!'"
- ch22 idx17 [19-23]: MSG "I saw God enthroned" / "ranged on his right and his left"
  → Teen "I saw God on his throne" / "standing at attention on his right and his left"
