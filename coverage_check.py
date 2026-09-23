#!/usr/bin/env python3
"""Substantive coverage check: every MSG verse must be covered by >=1 EN badge.
Usage: python3 coverage_check.py Joshua
"""
import json, re, sys

def expand(rng):
    vs = set()
    for part in rng.split(','):
        part = part.strip()
        if '-' in part:
            a, b = part.split('-'); vs.update(range(int(a), int(b)+1))
        elif part.isdigit():
            vs.add(int(part))
    return vs

def check(book):
    slug = book.replace(' ', '')
    patch = json.load(open(f'fixes/en_{slug}.json'))
    msg = json.load(open(f'msg_{slug}_parsed.json'))['chapters']
    problems = []
    for ch in patch:
        n = str(ch['chapter'])
        msg_verses = set()
        for m in msg[n]:
            msg_verses |= expand(m['range'])
        covered = set()
        for b in ch['verseRanges']:
            covered |= expand(b)
        missing = sorted(msg_verses - covered)
        extra = sorted(covered - msg_verses)
        if missing: problems.append(f"ch{n}: MSG verses NOT covered by badges: {missing}")
        if extra: problems.append(f"ch{n}: badge verses beyond MSG: {extra}")
        # splits must share msg_range: check declared split paras' badges intersect the range
        for s in ch.get('splits', []):
            sv = expand(s['msg_range'])
            for p in s['paras']:
                if not (expand(ch['verseRanges'][p]) & sv):
                    problems.append(f"ch{n}: split {s['msg_range']} para {p} badge {ch['verseRanges'][p]} doesn't touch range")
    if problems:
        print(f'{book}: {len(problems)} PROBLEMS')
        for p in problems: print(' -', p)
    else:
        print(f'{book}: all MSG verses covered, splits consistent')

if __name__ == '__main__':
    check(sys.argv[1])
