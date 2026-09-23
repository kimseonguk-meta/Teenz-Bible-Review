#!/usr/bin/env python3
"""Psalms slang cleanup. Run from ~/workspace/teenz-bible-review."""
import json, os, re

REVIEW = os.path.expanduser('~/workspace/teenz-bible-review')
EN_P = os.path.join(REVIEW, 'fixes/en_Psalms.json')
KO_P = os.path.join(REVIEW, 'fixes/ko_Psalms.json')

en = json.load(open(EN_P))
ko = json.load(open(KO_P))
en_by = {c['chapter']: c for c in en}
ko_by = {c['chapter']: c for c in ko}

def sub_en(ch, idx, old, new):
    p = en_by[ch]['paragraphs'][idx]
    assert old in p, f'EN ch{ch} p{idx}: NOT FOUND: {old[:60]}'
    en_by[ch]['paragraphs'][idx] = p.replace(old, new, 1)

def sub_ko(ch, idx, old, new):
    p = ko_by[ch]['paragraphs'][idx]
    assert old in p, f'KO ch{ch} p{idx}: NOT FOUND: {old[:60]}'
    ko_by[ch]['paragraphs'][idx] = p.replace(old, new, 1)

# ---- ghosting -> plain expressions (context-specific) ----
sub_en(10, 0, "you're ghosting me", "you're ignoring me")
sub_en(28, 0, "don't ghost me", "don't ignore me")
sub_en(31, 0, "Please don't ghost me.", "Please don't turn away from me.")
sub_en(36, 0, "who ghosts God", "who turns away from God")
sub_en(42, 5, "why'd you ghost me?", "why have you forgotten me?")
sub_en(44, 2, "you've just ghosted us", "you've abandoned us")
sub_en(50, 5, "You ghost me whenever I call", "You ignore me whenever I call")
sub_en(60, 0, "you totally ghosted us", "you've abandoned us")
sub_en(69, 20, "Don't ghost me;", "Don't turn away from me;")
sub_en(80, 4, "we won't ghost you again", "we won't turn away from you again")
sub_en(83, 0, "don't ghost me", "don't ignore me")
sub_en(94, 4, "God's not gonna ghost his people. He'll never leave them on read.",
       "God's not gonna abandon his people. He'll never ignore them.")
sub_en(102, 0, "Don't ghost me right when I need you the most.", "Don't ignore me right when I need you the most.")
sub_en(132, 2, "don't ghost your chosen one", "don't turn away from your chosen one")
sub_en(143, 3, "Don’t ghost me,", "Don’t turn away from me,")

# ---- systematic filler removal: no cap / lowkey ----
def clean_fillers(text):
    # "no cap" variants
    text = re.sub(r',?\s*no cap\.', '.', text, flags=re.I)
    text = re.sub(r'no cap,\s*', '', text, flags=re.I)
    text = re.sub(r'\s*no cap\b', '', text, flags=re.I)
    # "lowkey"/"low-key" as filler adverb -> remove
    text = re.sub(r'\blow-?key\s+', '', text, flags=re.I)
    return text

n_filler = 0
for ch in en_by:
    e = en_by[ch]
    for i, p in enumerate(e['paragraphs']):
        if p.lstrip().startswith('§'):
            continue
        new = clean_fillers(p)
        if new != p:
            e['paragraphs'][i] = new
            n_filler += 1
print(f'filler cleanup applied to {n_filler} paras')

json.dump(en, open(EN_P, 'w'), ensure_ascii=False, indent=2)
json.dump(ko, open(KO_P, 'w'), ensure_ascii=False, indent=2)
print('saved.')

# ---- other specific slang (run after filler pass; see fix_psalms_slang2.py) ----
