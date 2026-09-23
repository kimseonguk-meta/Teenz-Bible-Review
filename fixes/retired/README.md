# retired — Matthew superseded chunk

- `en_matthew_01-14.json` (retired 2026-09-23): earlier consolidation of Matthew ch 1-14,
  superseded by the newer per-range pieces which are the canonical source:
  - `fixes/en_matthew_01-03.json` (ch 1-3)
  - `fixes/en_matthew_04-07.json` (ch 4-7)
  - `fixes/en_matthew_08-10.json` (ch 8-10)
  - `fixes/en_matthew_11-14.json` (ch 11-14)
  - `fixes/en_matthew_15-28.json` (ch 15-28)
  - `fixes/ko_matthew_01-14.json` (ch 1-14)
  - `fixes/ko_matthew_15-28.json` (ch 15-28)

Evidence: piece files carry later mtimes than the 01-14 consolidation,
`gdocs_build/build_gdocs.py` builds the Matthew doc from the pieces (not 01-14),
and slang fixes were applied to the pieces. Do not use this file for builds.
Git history preserved via `git mv`.
