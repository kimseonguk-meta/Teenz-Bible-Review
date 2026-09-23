# completeness_check 오탐 기록 — 1Timothy (2026-09-23)

checker: `gdocs_build/completeness_check.py` → `../fixes/en_1Timothy.json`
결과: 6장 38문단, name 47 / number 10 토큰 검사, FAIL 5건 → 전수 수동 대조 후 전부 오탐으로 판정. 실제 누락 0건.

## 오탐 1: ch1 idx0 [badge 1-2] name "christ"
- MSG: "an apostle on special assignment for **Christ**, our living hope"
- TEEN: "an apostle on a special mission for **Jesus**, the guy who gives us major hope"
- 판정: 오탐. 동일인물 호칭 ("Christ"→"Jesus"). Colossians 감사에서 동일 케이스를 오탐으로 문서화한 전례.

## 오탐 2: ch1 idx6 [badge 15-19] number "2"
- MSG (19-20): "Hymenaeus and Alexander are **two** of them. ... to be taught a lesson or **two**"
- TEEN (union of paras 6,7,8,9): "Hymenaeus and Alexander are **a couple** of them. I let them wander off to Satan so they'd learn their lesson..."
- 판정: 오탐. ① checker가 MSG 19-20을 badge 15-19 문단들(6,7,8)과 19-20(9)의 union으로 검사 — pairing 아티팩트. ② "two of them"→"a couple of them"은 동등 표현. ③ "a lesson or two"의 "or two"는 관용적 덧붙임, 핵심("교훈을 얻게")은 보존.

## 오탐 3: ch4 idx2 [badge 6-10] name "workouts", "savior"
- MSG: "**Workouts** in the gymnasium are useful... **Savior** of all men and women"
- TEEN: "Hitting the **gym** is cool and all... the GOAT who **saves** everyone"
- 판정: 오탐. "workouts"→"hitting the gym" 의역, "savior"→"who saves" 동사형 — 의미 보존, 형태소 불일치일 뿐.

## 오탐 4: ch5 idx1 [badge 1-2] name "reverently"
- MSG: "**Reverently** honor an older woman as you would your mother"
- TEEN: "Show some **major respect** to the older women like they're your mom"
- 판정: 오탐. 부사 "reverently"가 "major respect"에 흡수 — 경외의 태도 보존.

## 오탐 5: ch5 idx4 [badge 11-15] number "1"
- MSG: "I'd rather the young widows go ahead and get married in the **first** place"
- TEEN: "it's better for the young widows to **just** get married"
- 판정: 오탐. 서수 "first"의 숫자 토큰 추출 아티팩트 (Acts 감사 "서수/관용구" 오탐 전례). "차라리"의 의미는 "it's better... just"에 보존.
