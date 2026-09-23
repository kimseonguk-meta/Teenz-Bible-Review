#!/usr/bin/env python3
"""Revelation 27 approved paragraph splits (2026-09-22, approved by Seonguk).

Splits merged paragraphs in fixes/en_Revelation.json and fixes/ko_Revelation.json
into MSG's printed paragraph units. No text is added/removed/reordered: each
split cuts only at existing sentence boundaries, verified by reconstruction
assertion. verseRanges badges are duplicated; splits are declared in the
`splits` records (validator check 3). The 27 merge entries and their
confirmations_needed strings are removed and replaced by split records.

DO NOT run build_rev_final.py afterwards (it is stale and regresses KO text).
"""
import json, re, sys

EN_PATH = 'fixes/en_Revelation.json'
KO_PATH = 'fixes/ko_Revelation.json'

# (chapter, para_index_0based, badge, en_end_markers, ko_end_markers, msg_desc)
# end_markers: text each part (except the last) must end with, in order.
SPLITS = [
    (1, 2, '3', ["all the words written in this book!"], ["완전 복 받은 거야!"],
     "two paragraphs ('How blessed the reader!...' + 'Time is just about up.')"),
    (1, 3, '4-7', ["the Ruler of all earthly kings."], ["내려주시길 바래."],
     "two paragraphs (greeting + doxology)"),
    (1, 5, '9-17', ["I turned and saw the voice.", "his face a blinding sun."],
     ["보려고 돌아섰어.", "태양 같았어."],
     "three paragraphs (Patmos vision, the Son of Man, fainting)"),
    (2, 3, '4-5', ["A Lucifer fall!"], ["추락했다고!"],
     "two paragraphs ('But you walked away...' + 'Turn back! Recover...')"),
    (2, 9, '10', ["It won't last forever."], ["열흘이면 끝나."],
     "two paragraphs ('Fear nothing...' + 'Don't quit...')"),
    (3, 1, '1', ["with the other, speaks:"], ["말씀하신다."],
     "two paragraphs (commission + 'I see right through your work')"),
    (3, 2, '2-3', ["turn back to God."], ["하나님께 돌아가."],
     "two paragraphs ('Up on your feet!' + 'If you pull the covers...')"),
    (4, 3, '6-8', ["never taking a break:"], ["밤낮 쉬지 않고 말했어."],
     "two paragraphs (Four Animals description + 'Holy, holy, holy' chant)"),
    (4, 4, '9-11', ["at the foot of the Throne, chanting,"], ["던지며 말했어."],
     "two paragraphs (Elders fall prostrate + 'Worthy, O Master!' chant)"),
    (5, 4, '6-10', ["took the scroll from his right hand."], ["두루마리를 받으셨어."],
     "two paragraphs (Lamb takes scroll + new song)"),
    (5, 5, '11-14', ["Take the honor, the glory, the blessing!", "for age after age after age."],
     ["합당하십니다!”", "영원히 있기를!”"],
     "three paragraphs (angels' song, every creature, Amen)"),
    (7, 4, '9-12', ["Salvation to the Lamb!"], ["양한테 있다!”"],
     "two paragraphs (crowd's song + angels' worship)"),
    (11, 8, '15-18', ["He will rule forever and ever!"], ["다스리실 거야!”"],
     "two paragraphs (heaven's crescendo + elders' song)"),
    (12, 4, '7-12', ["thrown down to earth."], ["그분의 천사들도 함께 내쫓겼어."],
     "two paragraphs (war in heaven + victory song)"),
    (14, 8, '13', ["how blessed to die that way!”"], ["복이야!”"],
     "two paragraphs (voice from Heaven + Spirit's 'Yes')"),
    (15, 2, '2-4', ["stood on the sea of glass."], ["가지고 있었어."],
     "two paragraphs (sea of glass + song)"),
    (16, 4, '4-7', ["they've gotten what they deserve!"], ["받을 겁니다!”"],
     "two paragraphs (Angel of Waters + Altar)"),
    (18, 1, '1-8', ["entrepreneurs made millions exploiting her."], ["되었거든.”"],
     "two paragraphs (angel's dirge + heaven's shout)"),
    (18, 2, '9-10', ["they'll cry their lament:"], ["말할 거야."],
     "two paragraphs (kings' lament + 'Doom, doom')"),
    (18, 3, '11-17',
     ["their terrible traffic in human lives.", "Not a scrap, not a thread to be found!",
      "cried and carried on all the more:"],
     ["사람들의 영혼까지.", "찾지 못할 거야.”", "슬퍼하며 말할 거야."],
     "four paragraphs (traders' cry, 'Everything you've lived for', traders at distance, 'Doom, doom')"),
    (18, 4, '17-19', ["the world had come to an end:"], ["슬퍼하며 외쳤어."],
     "two paragraphs (shipmasters' cry + 'Doom, doom')"),
    (18, 6, '21-24', ["into the sea, saying,"], ["던지며 말했어."],
     "two paragraphs (millstone + 'Heaved and sunk')"),
    (19, 1, '1-3', ["the blood of his servants."], ["갚아주셨거든.”"],
     "two paragraphs (first hallelujah + second hallelujah)"),
    (19, 2, '4', ["God on his Throne, praising,"], ["경배했어."],
     "two paragraphs (Elders fall + 'Amen! Yes! Hallelujah!')"),
    (19, 3, '5', ["a shout, a command:"], ["목소리가 났어."],
     "two paragraphs (shout from Throne + 'Praise our God')"),
    (19, 4, '6-8', ["the sound of strong thunder:"], ["우레소리 같은 것을 들었어."],
     "two paragraphs (massed choirs + marriage song)"),
    (22, 10, '20', ["I'll be there soon!”"], ["갈 거야!”"],
     "two paragraphs (testifier's 'I'm on my way!' + 'Yes! Come, Master Jesus!')"),
]


def split_text(text, markers, label):
    parts, rest = [], text
    for m in markers:
        i = rest.find(m)
        assert i != -1, f'{label}: marker not found: {m!r}'
        assert rest.count(m) == 1, f'{label}: marker not unique: {m!r}'
        parts.append(rest[:i + len(m)])
        rest = rest[i + len(m):]
        assert rest[:1] == ' ', f'{label}: expected single space after {m!r}, got {rest[:3]!r}'
        rest = rest[1:]
    parts.append(rest)
    assert all(p.strip() for p in parts), f'{label}: empty part produced'
    assert parts[0] + ''.join(' ' + p for p in parts[1:]) == text, \
        f'{label}: reconstruction mismatch (text added/lost)'
    return parts


def apply(path, lang):
    data = json.load(open(path))
    by_ch = {c['chapter']: c for c in data}
    targets = sorted(SPLITS, key=lambda s: (s[0], s[1]))
    for ch in sorted({s[0] for s in targets}):
        c = by_ch[ch]
        ps, vrs = c['paragraphs'], c['verseRanges']
        mr = c.get('msg_ranges', [])
        # content-paragraph ordinal -> msg_ranges index
        hdr_before = [i for i, p in enumerate(ps) if p.lstrip().startswith('§')]
        shift = 0
        for (tch, pidx, badge, en_m, ko_m, desc) in [s for s in targets if s[0] == ch]:
            markers = en_m if lang == 'EN' else ko_m
            ai = pidx + shift
            assert vrs[ai] == badge, f'ch{ch} p{pidx}: badge {vrs[ai]!r} != {badge!r}'
            label = f'{lang} ch{ch} p{pidx}[{badge}]'
            parts = split_text(ps[ai], markers, label)
            n = len(parts)
            ps[ai:ai + 1] = parts
            vrs[ai:ai + 1] = [badge] * n
            # msg_ranges: one label per content paragraph (headers excluded)
            ci = ai - sum(1 for h in hdr_before if h < ai)
            assert mr[ci] == badge, f'{label}: msg_ranges[{ci}]={mr[ci]!r} != {badge!r}'
            mr[ci:ci + 1] = [badge] * n
            new_idx = list(range(ai, ai + n))
            c.setdefault('splits', []).append({
                'msg_range': badge,
                'paras': new_idx,
                'note': f"Split approved 2026-09-22 (Seonguk): MSG prints {badge} as {desc}; "
                        f"split into {n} {lang}/{'KO' if lang=='EN' else 'EN'} paragraphs following MSG",
            })
            # remove the merge entry for this badge
            mg = c.get('merges', [])
            before = len(mg)
            c['merges'] = [m for m in mg
                           if not (m.get('msg_ranges') == [badge]
                                   and 'kept as one EN paragraph' in m.get('note', ''))]
            assert len(c['merges']) == before - 1, f'{label}: expected 1 merge removed, got {before - len(c["merges"])}'
            # remove its confirmations_needed strings: match MSG <ch>:<badge> or
            # MSG <badge> (digit-guarded), and only strings that mention a merge
            cn = c.get('confirmations_needed', [])
            nospace = lambda s: re.sub(r'\s+', '', s)
            pats = [re.compile(r'MSG' + str(ch) + r':' + re.escape(badge) + r'(?![0-9])'),
                    re.compile(r'MSG' + re.escape(badge) + r'(?![0-9])')]
            keep, dropped = [], []
            for s in cn:
                ns = nospace(s)
                if any(p.search(ns) for p in pats) and 'merg' in s:
                    dropped.append(s)
                else:
                    keep.append(s)
            assert len(dropped) == 1, f'{label}: expected 1 confirmation dropped, got {len(dropped)}: {dropped}'
            c['confirmations_needed'] = keep
            shift += n - 1
        # sanity: paragraphs/verseRanges/msg_ranges alignment
        assert len(ps) == len(vrs), f'ch{ch}: paras({len(ps)}) != verseRanges({len(vrs)})'
        nonhdr = [b for i, b in enumerate(vrs) if not ps[i].lstrip().startswith('§')]
        assert mr == nonhdr, f'ch{ch}: msg_ranges out of sync after split'
    json.dump(data, open(path, 'w'), ensure_ascii=False, indent=2)
    print(f'{lang}: applied {len(targets)} splits -> {path}')


if __name__ == '__main__':
    apply(EN_PATH, 'EN')
    apply(KO_PATH, 'KO')
