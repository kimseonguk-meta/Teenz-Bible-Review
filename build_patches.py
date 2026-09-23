#!/usr/bin/env python3
"""Build en_<Slug>.json / ko_<Slug>.json patch files from a per-book spec.

Spec (spec_<Slug>.py) format:
  BOOK = 'Philippians'            # key in allBibleData.json / gospelDataKo
  SLUG = 'Philippians'            # output file slug (no spaces)
  CHAPTERS = {
    <num>: {
      'en_ops': [ ('keep', base_idx, new_badge_or_None),
                  ('new', badge, text), ... ],
      'ko_title': '...',
      'ko_ops':  [ ('keep', ko_base_idx), ('new', text), ... ],
      'splits': [ {'msg_range': '18-21', 'paras': [7,8], 'note': '...'} ],
      'merges': [ {'para': 1, 'msg_ranges': ['1','2-6'], 'note': '...'} ],
      'changes': ['...'],
      'confirmations': ['...'],
    }, ...
  }
Every chapter of the book must appear in CHAPTERS (unchanged chapters use
all-('keep', i, None) ops and mirrored ko ops).
"""
import json, sys, importlib.util, re

WS = '/home/hatch/workspace'


def strip_embedded_badge(text):
    """KO 베이스의 문단 선두 '1-2' 같은 배지 중복 라인을 제거한다."""
    return re.sub(r'^\d+(?:-\d+)?\s*\n', '', text, count=1)


def load_spec(slug):
    path = f'{WS}/teenz-bible-review/specs/spec_{slug}.py'
    spec = importlib.util.spec_from_file_location('spec_' + slug, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build(slug):
    mod = load_spec(slug)
    book, chapters = mod.BOOK, mod.CHAPTERS
    en_base = {c['num']: c for c in
               json.load(open(f'{WS}/teenz-fix/client/src/data/allBibleData.json'))[book]}
    ko_base = {c['num']: c for c in
               json.load(open(f'/tmp/ko_base_{slug}.json', encoding='utf-8'))}
    en_out, ko_out = [], []
    for num in sorted(en_base):
        spec = chapters.get(num)
        if spec is None:
            raise SystemExit(f'{slug} ch{num}: spec missing')
        base = en_base[num]
        kb = ko_base[num]
        # --- EN ---
        paras, vrs = [], []
        for op in spec['en_ops']:
            if op[0] == 'keep':
                _, bi = op[0], op[1]
                nb = op[2] if len(op) > 2 else None
                paras.append(base['paragraphs'][bi])
                vrs.append(nb if nb is not None else base['verseRanges'][bi])
            elif op[0] == 'new':
                _, badge, text = op
                paras.append(text)
                vrs.append(badge)
            else:
                raise SystemExit(f'bad en op {op}')
        # --- KO ---
        kparas = []
        for op in spec['ko_ops']:
            if op[0] == 'keep':
                kparas.append(strip_embedded_badge(kb['paragraphs'][op[1]]))
            elif op[0] == 'new':
                kparas.append(op[1])
            else:
                raise SystemExit(f'bad ko op {op}')
        if len(kparas) != len(paras):
            raise SystemExit(f'{slug} ch{num}: EN {len(paras)} vs KO {len(kparas)} mismatch')
        en_out.append({
            'chapter': num, 'title': base.get('title', ''),
            'paragraphs': paras, 'verseRanges': vrs, 'msg_ranges': list(vrs),
            'merges': spec.get('merges', []), 'splits': spec.get('splits', []),
            'changes': spec.get('changes', []),
            'confirmations_needed': spec.get('confirmations', []),
        })
        ko_out.append({
            'chapter': num, 'title': spec.get('ko_title', base.get('title', '')),
            'paragraphs': kparas, 'verseRanges': list(vrs), 'msg_ranges': list(vrs),
            'merges': spec.get('merges', []), 'splits': spec.get('splits', []),
            'changes': spec.get('changes', []),
            'confirmations_needed': spec.get('confirmations', []),
        })
    with open(f'{WS}/teenz-bible-review/fixes/en_{slug}.json', 'w', encoding='utf-8') as f:
        json.dump(en_out, f, ensure_ascii=False, indent=1)
    with open(f'{WS}/teenz-bible-review/fixes/ko_{slug}.json', 'w', encoding='utf-8') as f:
        json.dump(ko_out, f, ensure_ascii=False, indent=1)
    print(f'{slug}: wrote {len(en_out)} chapters')


if __name__ == '__main__':
    build(sys.argv[1])
