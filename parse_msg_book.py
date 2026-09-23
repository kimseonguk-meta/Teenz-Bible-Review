#!/usr/bin/env python3
"""Parse cached BibleGateway MSG page text into structured chapters.

Usage: python3 parse_msg_book.py msg_Joshua.txt -> writes msg_Joshua_parsed.json
Output: {"book": ..., "chapters": {chapter_num: [{"range": "1-9", "header": str|None, "text": str}, ...]}}
"""
import re, json, sys

def parse_file(path):
    lines = open(path).read().split('\n')
    # Build event stream: ('hdr', text) | ('exp', A, Brange, rest) | ('amb', A, rest) | ('vonly', Brange, rest) | ('txt', line)
    events = []
    for ln in lines:
        s = ln.strip()
        if not s or s in ('---', '* * *'):
            continue
        if s.startswith('####'):
            break
        if s.startswith('###'):
            events.append(('hdr', s.lstrip('#').strip()))
            continue
        if s.startswith('|'):
            events.append(('txt', s))
            continue
        m = re.match(r'^(\d{1,2}) (\d+(?:-\d+)?) (.*)$', s)
        if m:
            events.append(('exp', int(m.group(1)), m.group(2), m.group(3)))
            continue
        m = re.match(r'^(\d{1,2}) (\D.*)$', s)
        if m:
            events.append(('amb', int(m.group(1)), m.group(2)))
            continue
        m = re.match(r'^(\d+(?:-\d+)?) (.*)$', s)
        if m:
            events.append(('vonly', m.group(1), m.group(2)))
            continue
        events.append(('txt', s))

    chapters = {}   # ch -> list of sections
    cur = 0
    cur_secs = []
    cur_range, cur_lines, cur_header = None, [], None
    pending_header = None
    last_verse_end = 0

    def rng_start(r):
        return int(str(r).split('-')[0])

    def rng_end(r):
        p = str(r).split('-')
        return int(p[1]) if len(p) > 1 else int(p[0])

    def flush_section():
        nonlocal cur_range, cur_lines, cur_header
        if cur_range is not None:
            cur_secs.append({'range': cur_range, 'header': cur_header,
                             'text': ' '.join(cur_lines)})
        cur_range, cur_lines, cur_header = None, [], None

    def next_verse_start(idx):
        """Lookahead: start of next verse marker event (skip headers/txt)."""
        for j in range(idx + 1, len(events)):
            e = events[j]
            if e[0] == 'hdr' or e[0] == 'txt':
                continue
            if e[0] == 'exp':
                return rng_start(e[2])
            if e[0] == 'vonly':
                return rng_start(e[1])
            if e[0] == 'amb':
                return e[1]
        return None

    for i, e in enumerate(events):
        kind = e[0]
        if kind == 'hdr':
            pending_header = e[1]
            continue
        if kind == 'txt':
            if cur_range is not None:
                cur_lines.append(e[1])
            continue
        if kind == 'exp':
            A, B, rest = e[1], e[2], e[3]
            if A == cur + 1 and rng_start(B) == 1:
                flush_section()
                if cur:
                    chapters[cur] = cur_secs
                cur = A
                cur_secs = []
                last_verse_end = 0
                cur_range, cur_lines = B, [rest]
                cur_header = pending_header
                pending_header = None
                last_verse_end = rng_end(B)
            elif A == cur:
                # new MSG paragraph of the current chapter. Badges may overlap
                # (e.g. "12-13" followed by "13-14") or nest (e.g. "36" after
                # "34-36"); every explicit badge line is its own paragraph.
                flush_section()
                cur_range, cur_lines = B, [rest]
                cur_header = pending_header
                pending_header = None
                last_verse_end = max(last_verse_end, rng_end(B))
            else:
                # unexpected; treat as continuation text
                if cur_range is not None:
                    cur_lines.append(' '.join(str(x) for x in e[1:]))
            continue
        if kind == 'amb':
            A, rest = e[1], e[2]
            if A == cur + 1:
                # chapter start (implied v1) OR verse A of current chapter? use lookahead
                nxt = next_verse_start(i)
                if nxt is not None and nxt > A:
                    # next verse continues from A -> verse A of current chapter
                    # (e.g. ch2 "3 The king of Jericho sent word" followed by "4-7")
                    flush_section()
                    cur_range, cur_lines = str(A), [rest]
                    cur_header = pending_header
                    pending_header = None
                    last_verse_end = A
                elif A > last_verse_end and nxt == A:
                    # e.g. ch14 "15 The name of Hebron" followed by ch15 "15 The lot...":
                    # first 15 is verse 15 of current chapter (H2 would leave vv2..14
                    # of the new chapter without markers -> impossible)
                    flush_section()
                    cur_range, cur_lines = str(A), [rest]
                    cur_header = pending_header
                    pending_header = None
                    last_verse_end = A
                else:
                    # new chapter, implied verse 1
                    flush_section()
                    if cur:
                        chapters[cur] = cur_secs
                    cur = A
                    cur_secs = []
                    last_verse_end = 0
                    cur_range, cur_lines = '1', [rest]
                    cur_header = pending_header
                    pending_header = None
                    last_verse_end = 1
            elif rng_end(str(A)) > last_verse_end:
                # single-verse marker of current chapter (A may equal cur, e.g. ch6 v6,
                # or exceed it, e.g. ch2 v14)
                flush_section()
                cur_range, cur_lines = str(A), [rest]
                cur_header = pending_header
                pending_header = None
                last_verse_end = A
            else:
                if cur_range is not None:
                    cur_lines.append(' '.join(str(x) for x in e[1:]))
            continue
        if kind == 'vonly':
            B, rest = e[1], e[2]
            # new section if it extends past the last verse seen (this also catches
            # MSG's overlapping badges like "12-13" followed by "13-14")
            if cur_range is None or rng_end(B) > last_verse_end:
                flush_section()
                cur_range, cur_lines = B, [rest]
                cur_header = pending_header
                pending_header = None
                last_verse_end = rng_end(B)
            else:
                if cur_range is not None:
                    cur_lines.append(e[1] + ' ' + rest)
            continue
    flush_section()
    if cur:
        chapters[cur] = cur_secs
    return chapters


def main():
    path = sys.argv[1]
    book = path.split('msg_')[1].split('.txt')[0]
    chapters = parse_file(path)
    out = {'book': book, 'chapters': {str(k): v for k, v in chapters.items()}}
    opath = path.replace('.txt', '_parsed.json')
    json.dump(out, open(opath, 'w'), ensure_ascii=False, indent=1)
    print(f'{book}: {len(chapters)} chapters -> {opath}')
    for k in sorted(chapters):
        secs = chapters[k]
        cov = sorted({int(x) for s in secs for x in expand(s["range"])})
        print(f'  ch{k}: {len(secs)} sections, verses {cov[0]}-{cov[-1]} ({len(cov)}), hdrs={[s["header"] for s in secs if s["header"]]}')


def expand(r):
    out = set()
    for part in str(r).split(','):
        part = part.strip()
        if '-' in part:
            a, b = part.split('-')
            out.update(range(int(a), int(b) + 1))
        elif part.isdigit():
            out.add(int(part))
    return out


if __name__ == '__main__':
    main()
