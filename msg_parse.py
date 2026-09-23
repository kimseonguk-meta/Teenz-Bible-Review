import re, json

def parse_msg_sections(text, chapter, max_verse):
    """Parse BibleGateway MSG page text into [(range_str, header, text)]."""
    sections = []
    cur_range, cur_lines, cur_header = None, [], None
    pending_header = None
    for raw in text.split('\n'):
        line = raw.strip()
        if not line or line in ('---', '* * *'):
            continue
        if line.startswith('####'):
            break
        if line.startswith('###'):
            pending_header = line.lstrip('#').strip()
            continue
        m = re.match(r'^(?:(\d+)\s+)?(\d+(?:-\d+)?)\s+(.*)$', line)
        if m:
            chap_no = m.group(1)
            rng = m.group(2)
            rest = m.group(3)
            start_v = int(rng.split('-')[0])
            if chap_no is not None and int(chap_no) != chapter:
                continue
            if start_v < 1 or start_v > max_verse:
                # not a verse marker, treat as continuation
                if cur_range is not None:
                    cur_lines.append(line)
                continue
            if cur_range is not None:
                sections.append((cur_range, cur_header, ' '.join(cur_lines)))
            cur_range, cur_lines = rng, [rest]
            cur_header = pending_header
            pending_header = None
        else:
            if cur_range is not None:
                cur_lines.append(line)
            elif pending_header:
                pass  # header with no following section yet
    if cur_range is not None:
        sections.append((cur_range, cur_header, ' '.join(cur_lines)))
    return sections


def range_to_set(r):
    if not r:
        return set()
    out = set()
    for part in str(r).split(','):
        part = part.strip().replace('~', '-')
        m = re.match(r'^(\d+)\s*-\s*(\d+)$', part)
        if m:
            out.update(range(int(m.group(1)), int(m.group(2)) + 1))
        elif re.match(r'^\d+$', part):
            out.add(int(part))
    return out


if __name__ == '__main__':
    sample = """1 The family tree of Jesus Christ, David's son, Abraham's son: 2-6 Abraham had Isaac,

Isaac had Jacob,

6-11 David had Solomon (Uriah's wife was the mother),

17 There were fourteen generations from Abraham to David,

### The Birth of Jesus

18-19 The birth of Jesus took place like this. His mother, Mary, was engaged to be married to Joseph."""
    for rng, hdr, txt in parse_msg_sections(sample, 1, 25):
        print(f'[{rng}] hdr={hdr} :: {txt[:70]}')
