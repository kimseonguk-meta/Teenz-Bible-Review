#!/usr/bin/env python3
"""Leviticus fixes base builder — MSG 감사 전 베이스 조립.
Sources:
  EN: /home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json (Phase 1 반영됨)
  KO: /home/hatch/workspace/teenz-fix/client/src/data/gospelDataKo.ts
  MSG units: msg_Leviticus.txt (parse via build_gdocs.parse_msg_lines)
Writes: fixes/en_Leviticus.json, fixes/ko_Leviticus.json
"""
import json, re, sys

REVIEW = '/home/hatch/workspace/teenz-bible-review'
SRC = '/home/hatch/workspace/teenz-fix/client/src/data'
sys.path.insert(0, f'{REVIEW}/gdocs_build')
from build_gdocs import parse_msg_lines


def vr_str(vs):
    vs = sorted(vs)
    return f'{vs[0]}-{vs[-1]}' if len(vs) > 1 else f'{vs[0]}'


# ---------- EN ----------
_en = json.load(open(f'{SRC}/allBibleData.json'))['Leviticus']
EN = {c['num']: c for c in _en}

# ---------- KO ----------
_txt = open(f'{SRC}/gospelDataKo.ts').read()
_est_start = _txt.index('"Leviticus": [')
_seg = _txt[_est_start:]
_st = _seg.index('[')
_depth, _in, _esc = 0, False, False
for _j, _ch in enumerate(_seg[_st:], _st):
    if _in:
        if _esc:
            _esc = False
        elif _ch == '\\':
            _esc = True
        elif _ch == '"':
            _in = False
    else:
        if _ch == '"':
            _in = True
        elif _ch == '[':
            _depth += 1
        elif _ch == ']':
            _depth -= 1
            if _depth == 0:
                _arr = _seg[_st:_j + 1]
                break
_arr = re.sub(r',(\s*[\]\}])', r'\1', _arr)
KOJ = {c['num']: c for c in json.loads(_arr)}
assert len(KOJ) == 27, f'KO chapters: {len(KOJ)}'

# ---------- MSG units per chapter ----------
units = parse_msg_lines(open(f'{REVIEW}/msg_Leviticus.txt', encoding='utf-8').read())
MSG = {}
for u in units:
    MSG.setdefault(u['chapter'], []).append(vr_str(u['verses']))
assert sorted(MSG.keys()) == list(range(1, 28))


def expand(vr):
    if '-' in vr:
        a, b = vr.split('-')
        return set(range(int(a), int(b) + 1))
    return {int(vr)}


def build_side(EN_, KOJ_):
    out = []
    for ch in range(1, 28):
        c = EN_ if EN_ is EN else None
        src = EN[ch] if EN_ is EN else KOJ[ch]
        paras = list(src['paragraphs'])
        vrs = list(src['verseRanges'])
        assert len(paras) == len(vrs), f'ch{ch}: paras {len(paras)} != vrs {len(vrs)}'
        # splits: duplicate verse coverage across paras
        seen = {}
        splits = []
        for i, b in enumerate(vrs):
            for v in expand(b):
                if v in seen:
                    pi = seen[v]
                    key = (min(pi, i), max(pi, i))
                    splits.append((key, b, pi, i))
                else:
                    seen[v] = i
        split_objs = []
        done = set()
        for (a, b_), badge, pi, i in splits:
            if (a, b_) in done:
                continue
            done.add((a, b_))
            # find the msg_range containing the shared verse
            shared = expand(vrs[a]) & expand(vrs[b_])
            mr = None
            for m in MSG[ch]:
                if shared & expand(m):
                    mr = m
                    break
            split_objs.append({'msg_range': mr, 'paras': [a, b_]})
        out.append({
            'chapter': ch,
            'title': src['title'],
            'paragraphs': paras,
            'verseRanges': vrs,
            'msg_ranges': MSG[ch],
            'merges': [],
            'splits': split_objs,
            'changes': [],
            'confirmations_needed': [],
        })
    return out


en_out = build_side(EN, None)
ko_out = []
for ch in range(1, 28):
    c = KOJ[ch]
    paras = list(c['paragraphs'])
    vrs = list(c['verseRanges'])
    assert len(paras) == len(vrs)
    seen = {}
    split_objs, done = [], set()
    for i, b in enumerate(vrs):
        for v in expand(b):
            if v in seen:
                key = (min(seen[v], i), max(seen[v], i))
                if key not in done:
                    done.add(key)
                    shared = expand(vrs[seen[v]]) & expand(vrs[i])
                    mr = next((m for m in MSG[ch] if shared & expand(m)), None)
                    split_objs.append({'msg_range': mr, 'paras': [key[0], key[1]]})
            else:
                seen[v] = i
    ko_out.append({
        'chapter': ch,
        'title': c['title'],
        'paragraphs': paras,
        'verseRanges': vrs,
        'msg_ranges': MSG[ch],
        'merges': [],
        'splits': split_objs,
        'changes': [],
        'confirmations_needed': [],
    })

json.dump(en_out, open(f'{REVIEW}/fixes/en_Leviticus.json', 'w'), ensure_ascii=False, indent=1)
json.dump(ko_out, open(f'{REVIEW}/fixes/ko_Leviticus.json', 'w'), ensure_ascii=False, indent=1)
print('wrote fixes/en_Leviticus.json (27 ch), fixes/ko_Leviticus.json (27 ch)')
# report EN/KO structure diffs
for ch in range(1, 28):
    e, k = en_out[ch-1], ko_out[ch-1]
    if len(e['paragraphs']) != len(k['paragraphs']) or e['verseRanges'] != k['verseRanges']:
        print(f'ch{ch}: EN {len(e["paragraphs"])}p {e["verseRanges"]} | KO {len(k["paragraphs"])}p {k["verseRanges"]}')
