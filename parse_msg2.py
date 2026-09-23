#!/usr/bin/env python3
"""Parse cached BibleGateway MSG text into per-chapter [(range, header, text)] sections.

Handles:
 - '###' / '####' headers (pending section header; #### is a subtitle, not a break)
 - '##' chapter-group headers (ignored)
 - line-start verse lines: 'CH RANGE text', 'RANGE text', lone-number lines
   (lone number N == current_chapter+1 -> chapter N verse 1; else verse N)
 - mid-line chapter transitions: closing quote + 2 spaces + 'CH RANGE'
Usage: python3 parse_msg2.py msg_<Slug>.txt msg_paras_<Slug>.json
"""
import re, json, sys


def preprocess(text):
    text = re.sub(r'([”"])\s{2,}(\d{1,3})\s+(\d+(?:-\d+)?)\s+([“A-Za-z])',
                  r'\1\n\2 \3 \4', text)
    return text


def parse(path):
    text = preprocess(open(path, encoding='utf-8').read())
    chapters = {}
    cur_ch = None
    cur_range, cur_lines, cur_header = None, [], None
    pending_header = None

    def flush():
        nonlocal cur_range, cur_lines, cur_header
        if cur_range is not None and cur_ch is not None:
            chapters.setdefault(cur_ch, []).append(
                {'range': cur_range, 'header': cur_header,
                 'text': ' '.join(cur_lines).strip()})
        cur_range, cur_lines, cur_header = None, [], None

    for raw in text.split('\n'):
        line = raw.strip()
        if not line or line in ('---', '* * *'):
            continue
        if line.startswith('####'):
            pending_header = line.lstrip('#').strip()
            continue
        if line.startswith('###'):
            pending_header = line.lstrip('#').strip()
            continue
        if line.startswith('##'):
            continue
        m = re.match(r'^(\d+)\s+(\d+(?:-\d+)?)\s+(.*)$', line)
        if m and not re.match(r'^\d+-\d+$', m.group(1)):
            flush()
            cur_ch = int(m.group(1))
            cur_range, cur_lines = m.group(2), [m.group(3)]
            cur_header = pending_header
            pending_header = None
            continue
        m2 = re.match(r'^(\d+(?:-\d+)?)\s+(.*)$', line)
        if m2:
            tok, rest = m2.group(1), m2.group(2)
            flush()
            if '-' in tok:
                cur_range, cur_lines = tok, [rest]
            else:
                n = int(tok)
                if cur_ch is None or n == cur_ch + 1:
                    cur_ch = n
                    cur_range, cur_lines = '1', [rest]
                else:
                    cur_range, cur_lines = tok, [rest]
            cur_header = pending_header
            pending_header = None
            continue
        if cur_range is not None:
            cur_lines.append(line)
    flush()
    return chapters


if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    chapters = parse(src)
    json.dump(chapters, open(dst, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    for ch in sorted(chapters, key=int):
        print(f'ch{ch}: {len(chapters[ch])} paras :: ' +
              ', '.join(p['range'] for p in chapters[ch]))
