#!/usr/bin/env python3
"""KO 감사본 빌드: work3/ko_specs_{book}.py 의 KO_CHAPTERS를 읽어
staging/ko_{book}_ch{ch}.json 생성. 구조(verseRanges/msg_ranges/merges/splits/
confirmations_needed)는 EN staging과 동일, paragraphs/changes는 KO 스펙."""
import json, sys, importlib.util

REVIEW = '/home/hatch/workspace/teenz-bible-review/'

def load_ko_specs(book):
    path = f'{REVIEW}work3/ko_specs_{book}.py'
    spec = importlib.util.spec_from_file_location(f'ko_specs_{book}', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.KO_CHAPTERS

def build(book, chs):
    kos = load_ko_specs(book)
    import os
    os.makedirs(f'{REVIEW}staging', exist_ok=True)
    for ch in chs:
        en = json.load(open(f'{REVIEW}staging/en_{book}_ch{ch}.json'))
        kd = kos[ch]
        assert len(kd['paragraphs']) == len(en['paragraphs']), f'ch{ch} KO/EN 문단 수 불일치'
        # KO용 merges/splits/confirmations: EN 것을 KO 문장으로 변환
        merges = []
        for m in en.get('merges', []):
            merges.append({'para': m['para'], 'msg_ranges': m['msg_ranges'],
                           'note': m['note'].replace('EN 문단', 'KO 문단')})
        splits = []
        for s in en.get('splits', []):
            splits.append({'para': s.get('para'), 'msg_range': s['msg_range'], 'paras': s['paras'],
                           'note': s['note'].replace('EN 가독성', 'KO 가독성')})
        confs = [c.replace('EN 문단', 'KO 문단') for c in en.get('confirmations_needed', [])]
        new_ch = {
            'chapter': ch,
            'title': '',
            'paragraphs': kd['paragraphs'],
            'verseRanges': list(en['verseRanges']),
            'msg_ranges': list(en['msg_ranges']),
            'merges': merges,
            'splits': splits,
            'changes': kd.get('changes', [f'{book} {ch}장: EN 구조에 맞춰 KO 문단·배지 재구성']),
            'confirmations_needed': confs,
            'review_status': 'msg_audited',
        }
        json.dump(new_ch, open(f'{REVIEW}staging/ko_{book}_ch{ch}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print(f'KO {book} ch{ch}: {len(new_ch["paragraphs"])} paras')

if __name__ == '__main__':
    build(sys.argv[1], [int(x) for x in sys.argv[2:]])
