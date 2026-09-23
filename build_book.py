#!/usr/bin/env python3
"""decisions_<Book>.json -> fixes/en_<Book>.json + fixes/ko_<Book>.json
Usage: python3 build_book.py Acts

decisions format:
{
  "book": "Acts",
  "chapters": {
    "1": {
      "title": "...",
      "merges": [{"para": i, "msg_ranges": ["6","7-8"], "note": "..."}],
      "splits": [{"msg_range": "1-5", "paras": [1,2], "note": "..."}],
      "en": [{"badge": "1-5", "text": "..."} | {"badge": "1-5", "keep": 1}],
      "ko": [...same...],
      "changes": [...],
      "confirmations_needed": [...]
    }
  }
}
"keep" = index into the existing source paragraphs (EN: allBibleData.json, KO: gospelDataKo.ts extract).
msg_ranges is set per paragraph (= verseRanges), following the Philippians precedent.
"""
import json
import sys


def resolve(specs, src_paras, lang, ch):
    paras, badges = [], []
    for s in specs:
        badges.append(s['badge'])
        if 'text' in s:
            paras.append(s['text'])
        elif 'keep' in s:
            paras.append(src_paras[s['keep']])
        else:
            raise ValueError(f'ch{ch} {lang}: spec needs text or keep: {s}')
    return paras, badges


def main():
    book = sys.argv[1]
    slug = book.replace(' ', '')
    dec = json.load(open(f'decisions_{slug}.json', encoding='utf-8'))
    en_all = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json',
                            encoding='utf-8'))
    ko_all = json.load(open(f'msg_work/ko_{slug}.json', encoding='utf-8'))
    en_src = {c['num']: c['paragraphs'] for c in en_all[book]}
    ko_src = {str(k): v['paragraphs'] for k, v in ko_all.items()}

    en_out, ko_out = [], []
    for n in sorted(int(k) for k in dec['chapters'].keys()):
        c = dec['chapters'][str(n)]
        en_paras, en_badges = resolve(c['en'], en_src[n], 'EN', n)
        ko_paras, ko_badges = resolve(c['ko'], ko_src[str(n)], 'KO', n)
        assert len(en_paras) == len(ko_paras), f'ch{n}: EN/KO para count mismatch'
        assert en_badges == ko_badges, f'ch{n}: EN/KO badge mismatch: {en_badges} vs {ko_badges}'
        assert all(b and str(b).lower() != 'none' for b in en_badges), f'ch{n}: null badge'
        base = {
            'chapter': n,
            'title': c['title'],
            'merges': c.get('merges', []),
            'splits': c.get('splits', []),
            'changes': c.get('changes', []),
            'confirmations_needed': c.get('confirmations_needed', []),
        }
        en_out.append({**base, 'paragraphs': en_paras, 'verseRanges': en_badges,
                       'msg_ranges': list(en_badges)})
        ko_out.append({**base, 'paragraphs': ko_paras, 'verseRanges': ko_badges,
                       'msg_ranges': list(ko_badges)})
    json.dump(en_out, open(f'fixes/en_{slug}.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)
    json.dump(ko_out, open(f'fixes/ko_{slug}.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)
    print(f'{book}: wrote fixes/en_{slug}.json ({len(en_out)} ch), fixes/ko_{slug}.json')


if __name__ == '__main__':
    main()
