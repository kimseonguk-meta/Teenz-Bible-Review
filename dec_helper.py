#!/usr/bin/env python3
"""Helper to build decisions_<Book>.json chapters programmatically.
Usage in a script:
  from dec_helper import H
  h = H('Acts')
  h.chapter(2, title='...', changes=[...], confirmations_needed=[...],
            merges=[...], splits=[...])
  h.en_keep(0, '1-4'); h.en_text('5-13', 'new...'); ...
  h.ko_keep(0, '1-4'); h.ko_merge([2,3], '5-13'); ...
  h.save()
"""
import json


class H:
    def __init__(self, book):
        self.slug = book.replace(' ', '')
        self.book = book
        try:
            self.dec = json.load(open(f'decisions_{self.slug}.json', encoding='utf-8'))
        except FileNotFoundError:
            self.dec = {'book': book, 'chapters': {}}
        en_all = json.load(open('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json',
                                encoding='utf-8'))
        ko_all = json.load(open(f'msg_work/ko_{self.slug}.json', encoding='utf-8'))
        self.en_src = {c['num']: c['paragraphs'] for c in en_all[book]}
        self.ko_src = {str(k): v['paragraphs'] for k, v in ko_all.items()}
        self._ch = None

    def chapter(self, n, title, changes=None, confirmations_needed=None,
                merges=None, splits=None):
        self._ch = {'title': title, 'changes': changes or [],
                    'confirmations_needed': confirmations_needed or [],
                    'merges': merges or [], 'splits': splits or [],
                    'en': [], 'ko': []}
        self.dec['chapters'][str(n)] = self._ch
        self._n = n
        return self

    def en_keep(self, i, badge):
        self._ch['en'].append({'badge': badge, 'keep': i})

    def en_text(self, badge, text):
        self._ch['en'].append({'badge': badge, 'text': text})

    def en_merge(self, idxs, badge):
        txt = ' '.join(self.en_src[self._n][i] for i in idxs)
        self._ch['en'].append({'badge': badge, 'text': txt})

    def ko_keep(self, i, badge):
        self._ch['ko'].append({'badge': badge, 'keep': i})

    def ko_text(self, badge, text):
        self._ch['ko'].append({'badge': badge, 'text': text})

    def ko_merge(self, idxs, badge):
        txt = ' '.join(self.ko_src[str(self._n)][i] for i in idxs)
        self._ch['ko'].append({'badge': badge, 'text': txt})

    def save(self):
        json.dump(self.dec, open(f'decisions_{self.slug}.json', 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        print(f'saved decisions_{self.slug}.json: {len(self.dec["chapters"])} chapters')
