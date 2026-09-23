#!/usr/bin/env python3
"""Extract KO book data from gospelDataKo.ts into msg_work/ko_<Slug>.json files.
The TS file is JSON-compatible object literal; strip the export prefix.
"""
import json, re, sys

src = '/home/hatch/workspace/teenz-fix/client/src/data/gospelDataKo.ts'
t = open(src, encoding='utf-8').read()
start = t.index('=', t.index('gospelDataKo')) + 1
start = t.index('{', start)
end = t.rindex('}')
body = t[start:end + 1]
# strip trailing commas before } or ] (defensive)
body = re.sub(r',(\s*[}\]])', r'\1', body)
data = json.loads(body)
print('books:', len(data))
for slug, key in [('Job', 'Job'), ('Psalms', 'Psalms'), ('Proverbs', 'Proverbs'),
                  ('Ecclesiastes', 'Ecclesiastes'), ('SongOfSongs', 'Song of Solomon')]:
    chs = data[key]
    json.dump(chs, open(f'msg_work/ko_{slug}.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(slug, len(chs), 'chapters')
