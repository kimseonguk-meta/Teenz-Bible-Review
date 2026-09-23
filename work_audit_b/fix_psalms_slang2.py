#!/usr/bin/env python3
"""Psalms slang part 2: specific replacements. Run from ~/workspace/teenz-bible-review."""
import json, os

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
    print(f'EN ch{ch} p{idx}: replaced')

def sub_ko(ch, idx, old, new):
    p = ko_by[ch]['paragraphs'][idx]
    assert old in p, f'KO ch{ch} p{idx}: NOT FOUND: {old[:60]}'
    ko_by[ch]['paragraphs'][idx] = p.replace(old, new, 1)
    print(f'KO ch{ch} p{idx}: replaced')

sub_en(30, 2, "Ayo, all you believers!", "Hey, all you believers!")
sub_en(33, 0, "Write a whole new banger for him", "Write a whole new song for him")
sub_en(42, 6, "I just need to lock in and focus on God.", "I just need to focus on God.")
sub_en(43, 0, "you've left me on read?", "you've ignored me?")
sub_en(50, 5, "'new bestie!'", "'best friend!'")
sub_en(55, 0, "Don't just leave me on read.", "Don't just ignore me.")
sub_en(66, 0, "Aight, everyone,", "Alright, everyone,")
sub_en(69, 0, "OMG, God, you gotta save me!", "God, you gotta save me!")
sub_en(81, 4, "Aight, listen up, fam", "Alright, listen up, everyone")
sub_en(96, 0, "Ayo, drop a brand-new banger for God!", "Hey, sing a brand-new song for God!")
sub_en(106, 0, "Ayy, let's go! Give it up for God!", "Hey, let's go! Give it up for God!")
sub_en(106, 2, "snatched them from the enemy's grip", "rescued them from the enemy")
sub_en(108, 0, "write a banger for You", "write a song for You")
sub_en(117, 0, "Ayo, shout out to God, everybody!", "Hey, shout out to God, everybody!")
sub_en(134, 0, "Aight, everyone who serves God,", "Alright, everyone who serves God,")
sub_en(135, 0, "Ayo, praise God's name!", "Hey, praise God's name!")
sub_en(149, 0, "Ayy, let's go! Sing a brand-new banger for God,", "Hey, let's go! Sing a brand-new song for God,")
sub_en(149, 1, "Ayy, let's go!", "Hey, let's go!")

# KO slang: 노잼, 꿀잼
sub_ko(37, 6, "'허, 쟤네 진짜 노잼 개그하네' 하고 비웃으신대", "'허, 쟤네 진짜 재미없는 장난하네' 하고 비웃으신대")
sub_ko(111, 1, "진짜 꿀잼!", "진짜 즐거워!")

json.dump(en, open(EN_P, 'w'), ensure_ascii=False, indent=2)
json.dump(ko, open(KO_P, 'w'), ensure_ascii=False, indent=2)
print('saved.')
