#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""D2 2Chronicles 조립: batch 파일 -> fixes/en_2Chronicles.json, fixes/ko_2Chronicles.json
+ MSG 원문(txt verse 라벨) vs 배지 커버리지 대조."""
import json, re, importlib.util, sys

WORK = '/home/hatch/workspace/teenz-bible-review/work_d2'
OUT_EN = '/home/hatch/workspace/teenz-bible-review/fixes/en_2Chronicles.json'
OUT_KO = '/home/hatch/workspace/teenz-bible-review/fixes/ko_2Chronicles.json'
TXT = '/home/hatch/workspace/teenz-bible-review/msg_2Chronicles.txt'

def load_batch(name):
    spec = importlib.util.spec_from_file_location(name, f'{WORK}/{name}.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CHAPTERS

def expand(vr):
    out = set()
    for part in str(vr).split(','):
        part = part.strip()
        if not part: continue
        if '-' in part:
            a, b = part.split('-', 1)
            out.update(range(int(a), int(b) + 1))
        elif part.isdigit():
            out.add(int(part))
    return out

# 1) txt에서 장별 verse 라벨 집합 추출 (검증된 파서)
#   - "NN M-R ..." 또는 "NN ..." (단독 숫자) 로 시작하는 줄이 장 시작 (NN == 이전 장+1)
#   - "M-R ..." 로 시작하는 줄은 현재 장의 절 범위 라벨
#   - line 272의 "21 ..."은 20:21 절 라벨이므로 예외 처리 (수동 검증됨)
txt_labels = {}
VERSE_AS_CHAPTER_EXCEPTIONS = {272}
pat_full = re.compile(r'^(\d{1,2})\s+(\d{1,3}(?:-\d{1,3})?)\s')
pat_single = re.compile(r'^(\d{1,3})\s')
pat_range = re.compile(r'^(\d{1,3})-(\d{1,3})\s')
cur_ch = None
for i, line in enumerate(open(TXT, encoding='utf-8')):
    ln = i + 1
    s = line.strip()
    if not s or s.startswith('###') or s == '* * *':
        continue
    m = pat_full.match(line)
    if m:
        n, vr = int(m.group(1)), m.group(2)
        if cur_ch is None or n == cur_ch + 1:
            cur_ch = n
        a, b = vr.split('-')[0], vr.split('-')[-1]
        txt_labels.setdefault(cur_ch, set()).update(expand(vr))
        continue
    if pat_range.match(line):
        m2 = pat_range.match(line)
        txt_labels.setdefault(cur_ch, set()).update(expand(f"{m2.group(1)}-{m2.group(2)}"))
        continue
    m = pat_single.match(line)
    if m:
        n = int(m.group(1))
        if ln in VERSE_AS_CHAPTER_EXCEPTIONS:
            txt_labels.setdefault(cur_ch, set()).add(n); continue
        if cur_ch is None or n == cur_ch + 1:
            cur_ch = n
            txt_labels.setdefault(cur_ch, set()).add(1); continue
        txt_labels.setdefault(cur_ch, set()).add(n); continue

# 2) batch 병합
chapters = {}
for bn in ['batch1_13_16','batch2_17_20','batch3_21_25','batch4_26_29','batch5_30_33','batch6_34_36']:
    chapters.update(load_batch(bn))

print('chapters:', sorted(chapters))
missing_ch = [c for c in range(1, 37) if c not in chapters]
print('MISSING chapters (no draft):', missing_ch)

# 3) 장별 커버리지 대조
ok = True
for ch in sorted(chapters):
    badge_union = set()
    for u in chapters[ch]['units']:
        badge_union.update(expand(u['badge']))
    lab = txt_labels.get(ch, set())
    miss_badge = sorted(lab - badge_union)   # 원문에 있는데 배지에 없음
    extra_badge = sorted(badge_union - lab)  # 배지에 있는데 원문 라벨에 없음
    if miss_badge or extra_badge:
        ok = False
        print(f'ch{ch}: txt-only {miss_badge} | badge-only {extra_badge} | txt_max={max(lab) if lab else None}')
if ok:
    print('COVERAGE OK: 모든 장 배지 = txt 라벨 합집합')

# 4) JSON 생성
en_list, ko_list = [], []
for ch in sorted(chapters):
    C = chapters[ch]
    paras_en, paras_ko, vrs = [], [], []
    for u in C['units']:
        b = u['badge']
        if u.get('header_en'):
            paras_en.append('§' + u['header_en']); vrs.append(b)
        paras_en.append(u['en']); 
        if not u.get('header_en'): vrs.append(b)
        else: pass
        # KO mirror
        if u.get('header_ko'):
            paras_ko.append('§' + u['header_ko']); 
        paras_ko.append(u['ko'])
    # verseRanges는 paras와 1:1 — 헤더 포함 각 문단마다 배지
    vrs2 = []
    for u in C['units']:
        if u.get('header_en'): vrs2.append(u['badge'])
        vrs2.append(u['badge'])
    assert len(paras_en) == len(vrs2) == len(paras_ko), (ch, len(paras_en), len(vrs2), len(paras_ko))
    lab = sorted(txt_labels.get(ch, set()))
    msg_ranges = [f"{lab[0]}-{lab[-1]}"] if lab else []
    note = ('rechunked_draft: MSG 2Chronicles 13-36장 문단 경계 재청킹 완료(unit 배지 1:1). '
            '이름·숫자 일부 수정 반영. 의미 전수 재감사는 미완료. '
            '1-12장은 MSG 원문 미확보로 미포함(후속 수집 후 추가 예정).')
    en_list.append({'chapter': ch, 'title': C.get('title_en',''), 'review_status': 'rechunked_draft',
                    'note': note, 'paragraphs': paras_en, 'verseRanges': vrs2,
                    'msg_ranges': msg_ranges, 'merges': [], 'splits': [], 'confirmations_needed': []})
    ko_list.append({'chapter': ch, 'title': C.get('title_ko',''), 'review_status': 'rechunked_draft',
                    'note': note, 'paragraphs': paras_ko, 'verseRanges': vrs2,
                    'msg_ranges': msg_ranges, 'merges': [], 'splits': [], 'confirmations_needed': []})

json.dump(en_list, open(OUT_EN,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko_list, open(OUT_KO,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', OUT_EN, OUT_KO, '| chapters:', len(en_list))
