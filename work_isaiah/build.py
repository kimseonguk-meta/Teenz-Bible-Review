#!/usr/bin/env python3
"""Isaiah 감사 스펙 -> fixes/en_Isaiah.json, fixes/ko_Isaiah.json 빌드."""
import json, glob, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
en_src = {c['num']: c for c in json.load(open(os.path.join(BASE, 'en_isaiah.json')))}
ko_src = {c['num']: c for c in json.load(open(os.path.join(BASE, 'ko_isaiah.json')))}


def apply_ops(ops, src_paras, ch, lang):
    out = []
    for op in ops:
        if 'keep' in op:
            out.append(src_paras[op['keep']])
        elif 'join' in op:
            parts = []
            for i in op['join']:
                if isinstance(i, dict) and 'new' in i:
                    parts.append(i['new'])
                else:
                    parts.append(src_paras[i])
            out.append(' '.join(parts))
        elif 'new' in op:
            out.append(op['new'])
        else:
            raise ValueError(f'ch{ch} {lang}: unknown op {op}')
    return out


def build_chapter(spec):
    ch = spec['chapter']
    e = en_src[ch]
    k = ko_src[ch]
    en_paras = apply_ops(spec['en_ops'], e['paragraphs'], ch, 'EN')
    ko_paras = apply_ops(spec['ko_ops'], k['paragraphs'], ch, 'KO')
    badges = spec['badges']
    assert len(en_paras) == len(badges), f'ch{ch}: EN paras {len(en_paras)} != badges {len(badges)}'
    assert len(ko_paras) == len(badges), f'ch{ch}: KO paras {len(ko_paras)} != badges {len(badges)}'
    en_ch = {
        'chapter': ch,
        'title': spec.get('title', e['title']),
        'paragraphs': en_paras,
        'verseRanges': badges,
        'msg_ranges': spec.get('msg', badges),
        'merges': spec.get('merges', []),
        'splits': spec.get('splits', []),
        'changes': spec.get('changes', []),
        'confirmations_needed': spec.get('confirmations_needed', []),
    }
    ko_ch = {
        'chapter': ch,
        'title': spec.get('ko_title', k['title']),
        'paragraphs': ko_paras,
        'verseRanges': badges,
        'msg_ranges': spec.get('msg', badges),
        'merges': spec.get('merges', []),
        'splits': spec.get('splits', []),
        'changes': spec.get('ko_changes', []),
        'confirmations_needed': spec.get('confirmations_needed', []),
    }
    return en_ch, ko_ch


def main():
    specs = []
    for f in sorted(glob.glob(os.path.join(BASE, 'specs_*.json'))):
        specs.extend(json.load(open(f)))
    by_ch = {}
    for s in specs:
        by_ch[s['chapter']] = s  # later batch overwrites
    en_out, ko_out = [], []
    for ch in sorted(by_ch):
        en_ch, ko_ch = build_chapter(by_ch[ch])
        en_out.append(en_ch)
        ko_out.append(ko_ch)
    en_path = os.path.join(BASE, '..', 'fixes', 'en_Isaiah.json')
    ko_path = os.path.join(BASE, '..', 'fixes', 'ko_Isaiah.json')
    json.dump(en_out, open(en_path, 'w'), ensure_ascii=False, indent=1)
    json.dump(ko_out, open(ko_path, 'w'), ensure_ascii=False, indent=1)
    print(f'built {len(en_out)} chapters -> {en_path}, {ko_path}')


if __name__ == '__main__':
    main()
