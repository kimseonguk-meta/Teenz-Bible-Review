# completeness_check false positives — 1 Peter (2026-09-22)

Checker run: `python3 gdocs_build/completeness_check.py fixes/en_1Peter.json`
Result: 2 FAILs, both false positives. Chapters 1/3/5 skipped by checker's
structural guard (§ headers share badges with body paragraphs, so the
paragraph-vs-badge count mismatches) — those chapters were verified by manual
full read of MSG↔EN↔KO instead.

## FP 1 — ch4 idx6 [badge 12-13] name: christ
- MSG: "…you are in the very thick of what Christ experienced."
- TEEN: "…you're getting a taste of what Jesus went through."
- Standalone "Christ" rendered as "Jesus" — allowed teen-voice paraphrase per the
  confirmed name rule (only compound "Christ Jesus"/"Jesus Christ" drops are real
  issues). Not a drop.

## FP 2 — ch4 idx7 [badge 14-16] number: 2
- MSG: "…don't give it a second thought."
- TEEN: "…don't even sweat it."
- The "2" comes from the ordinal in the idiom "a second thought", not a content
  number. Same FP class as documented ordinals ("second place" etc.).
