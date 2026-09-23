#!/usr/bin/env python3
"""Normalize worker-E raw MSG transcriptions into canonical msg_<Key>.txt.

Raw format (worker_e/raw/<Key>.txt):
  @@@CHAPTER <N>@@@
  ### <section header>        (verbatim from bible-history.com)
  paragraphs separated by blank lines; wrapped lines kept as-is
  * * *                       (kept as its own line)

Paragraph splitting is driven ONLY by blank lines / headers / separators,
so wrapped text lines that happen to start with a number can never cause a
spurious split. The chapter prefix ("<ch> ") is ensured on the first
paragraph of each chapter (bible-history omits it when a chapter opens with
a single verse), making chapter boundaries unambiguous for
build_gdocs.parse_msg_txt.

Usage: python3 normalize.py Jeremiah
"""
import re, sys, os

REVIEW = '/home/hatch/workspace/teenz-bible-review'
sys.path.insert(0, os.path.join(REVIEW, 'gdocs_build'))
import build_gdocs as bg

EXPECTED_CHAPTERS = {'Jeremiah': 52, 'Lamentations': 5, 'Ezekiel': 48, 'Daniel': 12}


def norm_ws(s):
    return re.sub(r'\s+', ' ', s).strip()


def ensure_ch_prefix(ch, first_line):
    """Make the chapter's first paragraph an unambiguous TWO_NUM line.

    bible-history.com prints "<ch>" alone (verse 1's number omitted) when a
    chapter opens with a single verse (e.g. Jer 3: "3 God's Message came to
    me as follows:" = ch3 v1; Eze 1 / Lam 1 likewise), and "<ch> <range>"
    when it opens with a range. Normalize the lone-number form to
    "<ch> 1 <text>" so build_gdocs.parse_msg_txt files it as ch:v1
    deterministically (no reliance on the nn==cur_ch+1 inference).
    """
    m = re.match(r'^(\d{1,3})\s+(\d{1,3}(?:-\d{1,3})?(?:,\s*\d{1,3}(?:-\d{1,3})?)*)\s+(.*)$', first_line)
    if m and int(m.group(1)) == ch:
        return first_line  # already "<ch> <range> ..."
    m2 = re.match(r'^(\d{1,3})\s+(.*)$', first_line)
    if m2 and int(m2.group(1)) == ch:
        return f"{ch} 1 {m2.group(2)}"  # lone chapter number -> verse 1
    if m2:
        return first_line  # unexpected; keep verbatim for manual review
    return f"{ch} {first_line}"  # "<range> <text>" without chapter


def process_chapter(ch, lines):
    out_lines = []
    para = []            # line buffer for current paragraph
    para_is_first = True

    def flush():
        nonlocal para_is_first
        if not para:
            return
        text = norm_ws(' '.join(para))
        if para_is_first:
            text = ensure_ch_prefix(ch, text)
            para_is_first = False
        out_lines.append(text)
        para.clear()

    for ln in lines:
        s = ln.strip()
        if not s:
            flush()
            continue
        if s.startswith('###') or s == '* * *':
            flush()
            out_lines.append(s)
            continue
        para.append(ln.strip())
    flush()
    return out_lines


def main():
    key = sys.argv[1]
    raw_path = os.path.join(REVIEW, 'worker_e', 'raw', f'{key}.txt')
    raw = open(raw_path, encoding='utf-8').read()
    chapters, cur_ch, cur_lines = {}, None, []
    for ln in raw.split('\n'):
        m = re.match(r'^@@@CHAPTER\s+(\d+)@@@\s*$', ln.strip())
        if m:
            if cur_ch is not None:
                chapters[cur_ch] = cur_lines
            cur_ch, cur_lines = int(m.group(1)), []
        elif cur_ch is not None:
            cur_lines.append(ln)
    if cur_ch is not None:
        chapters[cur_ch] = cur_lines

    expected = EXPECTED_CHAPTERS[key]
    missing = [c for c in range(1, expected + 1) if c not in chapters]
    if missing:
        print(f'MISSING chapters: {missing}')
        sys.exit(1)

    canon = []
    for ch in range(1, expected + 1):
        canon.extend(process_chapter(ch, chapters[ch]))
        canon.append('')
    text = '\n'.join(canon).strip() + '\n'
    out_path = os.path.join(REVIEW, f'msg_{key}.txt')
    open(out_path, 'w', encoding='utf-8').write(text)

    units = bg.parse_msg_txt(out_path)
    by_ch = {}
    for u in units:
        by_ch.setdefault(u['chapter'], []).append(u)
    problems = []
    for ch in range(1, expected + 1):
        us = by_ch.get(ch, [])
        if not us:
            problems.append(f'ch{ch}: no units parsed')
            continue
        covered = set()
        for u in us:
            covered |= set(u['verses'] or set())
        mx = max(covered) if covered else 0
        gap = [v for v in range(1, mx + 1) if v not in covered]
        if gap:
            problems.append(f'ch{ch}: verse gaps {gap} (units={len(us)})')
    print(f'{key}: {len(by_ch)}/{expected} chapters, {len(units)} units')
    if problems:
        print('PROBLEMS:')
        for p in problems:
            print(' -', p)
    else:
        print('coverage OK (1..max contiguous per chapter)')


if __name__ == '__main__':
    main()
