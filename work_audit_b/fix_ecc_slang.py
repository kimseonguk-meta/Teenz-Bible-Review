#!/usr/bin/env python3
"""Ecclesiastes slang cleanup (EN/KO). Run from ~/workspace/teenz-bible-review."""
import json, os

REVIEW = os.path.expanduser('~/workspace/teenz-bible-review')
EN_P = os.path.join(REVIEW, 'fixes/en_Ecclesiastes.json')
KO_P = os.path.join(REVIEW, 'fixes/ko_Ecclesiastes.json')

en = json.load(open(EN_P))
ko = json.load(open(KO_P))
en_by = {c['chapter']: c for c in en}
ko_by = {c['chapter']: c for c in ko}

def sub_en(ch, idx, old, new):
    p = en_by[ch]['paragraphs'][idx]
    assert old in p, f'EN ch{ch} p{idx}: not found: {old[:50]}'
    en_by[ch]['paragraphs'][idx] = p.replace(old, new, 1)
    print(f'EN ch{ch} p{idx} fixed')

def sub_ko(ch, idx, old, new):
    p = ko_by[ch]['paragraphs'][idx]
    assert old in p, f'KO ch{ch} p{idx}: not found: {old[:50]}'
    ko_by[ch]['paragraphs'][idx] = p.replace(old, new, 1)
    print(f'KO ch{ch} p{idx} fixed')

sub_en(1, 3, "God made life pretty tough, no cap.", "God made life pretty tough, honestly.")
sub_ko(1, 2, "모든 게 다 지루하고, 진짜 노잼이라는 거야.", "모든 게 다 지루하고, 진짜 재미없다는 거야.")
en_by[3]['title'] = "There's a Time for Everything"
print('EN ch3 title fixed')
sub_en(3, 2, "we're still lowkey in the dark", "we're still in the dark")
sub_en(4, 0, "It made me think, lowkey, the dead are better off", "It made me think the dead are better off")
sub_en(7, 7, "Endings are lowkey better than beginnings.", "Endings are honestly better than beginnings.")
sub_en(8, 0, "being wise is lowkey the best.", "being wise is honestly the best.")
sub_en(9, 1, "It's lowkey messed up that everyone has the same fate.", "It's messed up that everyone has the same fate.")
sub_en(11, 0, "pays off big time. No cap.", "pays off big time, for real.")
sub_en(11, 5, "waking up to a new day is lowkey the best feeling.", "waking up to a new day is honestly the best feeling.")

json.dump(en, open(EN_P, 'w'), ensure_ascii=False, indent=2)
json.dump(ko, open(KO_P, 'w'), ensure_ascii=False, indent=2)
print('saved.')
