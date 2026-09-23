#!/usr/bin/env python3
"""staging의 감사 완료 장을 fixes/{lang}_{book}.json에 반영."""
import json, sys, shutil, os

REVIEW = '/home/hatch/workspace/teenz-bible-review/'

def finalize(book, chs):
    for lang in ['en', 'ko']:
        fp = f'{REVIEW}fixes/{lang}_{book}.json'
        bak = fp + '.pre_audit_bak'
        if not os.path.exists(bak):
            shutil.copy(fp, bak)
            print(f'backup: {bak}')
        data = json.load(open(fp))
        idx = {c['chapter']: i for i, c in enumerate(data)}
        for ch in chs:
            st = json.load(open(f'{REVIEW}staging/{lang}_{book}_ch{ch}.json'))
            assert st['review_status'] == 'msg_audited'
            assert 'note' not in st, f'{lang} {book} ch{ch}: note 잔존'
            data[idx[ch]] = st
            print(f'{lang} {book} ch{ch} 반영 ({len(st["paragraphs"])} paras)')
        json.dump(data, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

if __name__ == '__main__':
    finalize(sys.argv[1], [int(x) for x in sys.argv[2:]])
