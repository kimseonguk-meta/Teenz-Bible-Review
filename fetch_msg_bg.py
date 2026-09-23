#!/usr/bin/env python3
"""Fetch The Message (MSG) chapters from BibleGateway and write msg_work/<slug>_ch<NN>.txt
in the canonical per-chapter format used by assemble_msg_book.py:

    ### Section Header

    <ch> <range> <text>

    <range> <text>

    * * *

Usage:
    python3 fetch_msg_bg.py leviticus 1 27        # chapters 1..27
    python3 fetch_msg_bg.py leviticus 6 6 --stdout  # single chapter to stdout

Slug map: leviticus, numbers, deuteronomy, 1samuel, 2samuel
"""
import html as htmlmod
import os
import random
import re
import subprocess
import sys
import time

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

BG_BOOK = {
    'leviticus': 'Leviticus', 'numbers': 'Numbers',
    'deuteronomy': 'Deuteronomy', '1samuel': '1+Samuel', '2samuel': '2+Samuel',
    '1kings': '1+Kings', '2kings': '2+Kings', '1chronicles': '1+Chronicles',
    'ezra': 'Ezra', 'nehemiah': 'Nehemiah', 'isaiah': 'Isaiah',
    'lamentations': 'Lamentations', 'ezekiel': 'Ezekiel', 'daniel': 'Daniel',
}


def fetch(url: str) -> str:
    out = subprocess.run(
        ['curl', '-sL', '--max-time', '20', '-A', UA, url],
        capture_output=True, text=True)
    if out.returncode != 0 or not out.stdout:
        raise RuntimeError(f'curl failed rc={out.returncode} for {url}')
    return out.stdout


def clean_text(raw: str) -> str:
    # drop footnote superscripts and crossref spans entirely
    raw = re.sub(r'<sup class="footnote".*?</sup>', '', raw, flags=re.S)
    raw = re.sub(r'<span class="crossreference".*?</span>', '', raw, flags=re.S)
    raw = re.sub(r'<sup class="crossreference".*?</sup>', '', raw, flags=re.S)
    # drop versenum/chapternum markers (handled separately)
    raw = re.sub(r'<su[pb] class="(verse|chapter)num".*?</su[pb]>', '', raw, flags=re.S)
    raw = re.sub(r'<span class="chapternum".*?</span>', '', raw, flags=re.S)
    # strip remaining tags
    raw = re.sub(r'<[^>]+>', '', raw)
    t = htmlmod.unescape(raw)
    t = t.replace('\xa0', ' ')
    # normalize to straight quotes (repo convention)
    t = t.replace('\u201c', '"').replace('\u201d', '"')
    t = t.replace('\u2018', "'").replace('\u2019', "'")
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def parse_chapter(page: str, ch: int) -> str:
    # normalize escaped quotes (content is embedded with \' escapes)
    page = page.replace("\\'", "'").replace('\\"', '"')
    m = re.search(r'passage-content passage-class-0\'?>(.*?)</div>\s*<div',
                  page, re.S)
    if not m:
        # fallback: grab from marker to end of version div
        i = page.find('passage-content passage-class-0')
        if i < 0:
            raise RuntimeError('passage-content block not found')
        m2 = re.search(r'version-MSG result-text-style-normal text-html">(.*)',
                       page[i:], re.S)
        if not m2:
            raise RuntimeError('version-MSG block not found')
        body = m2.group(1)
    else:
        body = m.group(1)

    # cut off anything after the passage (copyright / footnotes section)
    cut = re.search(r'<div class=.(passage-other|footnotes|copyright)', body)
    if cut:
        body = body[:cut.start()]

    blocks = []
    # walk h3 / p in document order
    for tm in re.finditer(
            r'<h3[^>]*>(.*?)</h3>|<p([^>]*)>(.*?)</p>', body, re.S):
        if tm.group(1) is not None:  # h3 header
            hdr = clean_text(tm.group(1))
            if hdr:
                blocks.append(('h', hdr))
            continue
        attrs, inner = tm.group(2), tm.group(3)
        if 'center' in attrs and '* * *' in inner:
            blocks.append(('sep', None))
            continue
        # verse-range badge
        vm = re.search(r'<sup class="versenum"[^>]*>(.*?)</sup>', inner, re.S)
        badge = clean_text(vm.group(1)).strip() if vm else ''
        text = clean_text(inner)
        if not text:
            continue
        blocks.append(('p', badge, text))

    # build canonical chapter text
    lines = []
    first_para = True
    for b in blocks:
        if b[0] == 'h':
            lines.append(f'### {b[1]}')
            lines.append('')
        elif b[0] == 'sep':
            lines.append('* * *')
            lines.append('')
        else:
            _, badge, text = b
            if first_para:
                prefix = f'{ch} {badge} ' if badge else f'{ch} '
                first_para = False
            else:
                prefix = f'{badge} ' if badge else ''
            lines.append(prefix + text)
            lines.append('')
    return '\n'.join(lines).strip() + '\n'


def fetch_chapter(book_q: str, ch: int, retries: int = 4) -> str:
    """Fetch one chapter with captcha detection + backoff."""
    url = (f'https://www.biblegateway.com/passage/?search={book_q}+{ch}'
           f'&version=MSG')
    for attempt in range(retries):
        page = fetch(url)
        if 'passage-content passage-class-0' in page.replace("\\'", "'"):
            return page
        # captcha / error page
        wait = 60 * (attempt + 1)
        print(f'  [attempt {attempt+1}] challenge page for ch{ch}, '
              f'sleeping {wait}s...', flush=True)
        time.sleep(wait)
    raise RuntimeError(f'ch{ch}: still challenged after {retries} attempts')


def chapter_path(slug: str, ch: int) -> str:
    return f'msg_work/{slug}_ch{ch:02d}.txt'


def main():
    args = [a for a in sys.argv[1:] if a != '--stdout']
    to_stdout = '--stdout' in sys.argv
    slug, start, end = args[0], int(args[1]), int(args[2])
    book_q = BG_BOOK[slug]
    for ch in range(start, end + 1):
        fn = chapter_path(slug, ch)
        if not to_stdout and os.path.exists(fn) and os.path.getsize(fn) > 100:
            print(f'SKIP {fn} (exists)')
            continue
        page = fetch_chapter(book_q, ch)
        text = parse_chapter(page, ch)
        if to_stdout:
            sys.stdout.write(text)
        else:
            open(fn, 'w', encoding='utf-8').write(text)
            print(f'OK {fn} ({len(text)} chars)', flush=True)
        if not to_stdout and ch < end:
            time.sleep(random.uniform(8, 13))


if __name__ == '__main__':
    main()
