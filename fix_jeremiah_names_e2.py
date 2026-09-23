#!/usr/bin/env python3
"""Worker E2: Jeremiah name/place restorations (completeness check FAILs).

Restores specific names/places dropped by the teen paraphrase where the
meaning is not recoverable from context. Patronymic chains and synonym
variants (Chaldeans/Babylonians, God/Lord) are left as-is per policy.
"""
import json

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Jeremiah.json', encoding='utf-8'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Jeremiah.json', encoding='utf-8'))
en_by = {c['chapter']: c for c in en}
ko_by = {c['chapter']: c for c in ko}


def fix(ch, lang, idx, old, new, note):
    d = en_by[ch] if lang == 'en' else ko_by[ch]
    t = d['paragraphs'][idx]
    assert old in t, f'ch{ch} idx{idx}: not found: {old[:50]}'
    d['paragraphs'][idx] = t.replace(old, new, 1)
    d['changes'].append(note)


# ch2 idx4 [9-11]: Kedar
fix(2, 'en', 4, "or the deserts in the east",
    "or the Kedar wilderness in the east", "복원: Kedar 지명")
fix(2, 'ko', 4, "동쪽 사막",
    "동쪽 게달 광야", "복원: Kedar 지명 (KO)")

# ch2 idx6 [14-17]: Memphis and Tahpanhes
fix(2, 'en', 6, "Even the Egyptians have crushed you",
    "Even the Egyptians from Memphis and Tahpanhes have crushed you",
    "복원: Memphis, Tahpanhes 지명")
# KO: check first
k2 = ko_by[2]
print('KO ch2 idx6:', k2['paragraphs'][6][:200])

# ch2 idx7 [18-19]: Nile, Euphrates
fix(2, 'en', 7, "A drink from their rivers?",
    "A drink from the Nile or the Euphrates?",
    "복원: Nile, Euphrates 강 이름")

# ch2 idx9 [23-24]: Baal
fix(2, 'en', 9, "I haven't chased after false gods",
    "I haven't chased after the Baal gods",
    "복원: Baal 신명")
EOF
echo "draft written"