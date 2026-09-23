#!/usr/bin/env python3
"""completeness_check.py -- mechanical completeness gate for Teenz Bible translation.

Read-only checker: NEVER modifies its input JSON files.

For every non-header Teen EN paragraph, gathers the MSG source text for the
paragraph's badge verse-range and verifies that each content-bearing token
found there -- proper nouns / names, numbers, and key words from quoted
speech -- also appears in the Teen text. A missing token means the Teen
paraphrase summarized or dropped MSG content, which violates Seonguk's
standing rule: "do not abbreviate on your own; do not shrink it yourself."

Token -> verse attribution: an MSG unit's verses are its parsed verse set
plus any verse ranges embedded in its text (e.g. Matthew 1's genealogy is
filed under verse 1's unit but its text carries a "2-6" marker). A token
passes when it appears in ANY Teen paragraph whose badge covers one of its
verses (union semantics), so overlapping MSG print ranges (2-6 / 6-11 share
v.6) do not double-count.

Usage:
    python3 completeness_check.py <en_json> [<en_json> ...]

<en_json> is a fixes/en_<Book>.json file (or a split file such as
en_matthew_01-14.json). The book name is inferred from the file name; the
MSG source comes from ~/workspace/teenz-bible-review/ (msg_<Book>.txt,
msg_matthew_raw.json for Matthew, msg_Romans.txt + msg_Romans_supplement.txt
for Romans). Parser functions are reused from build_gdocs.py.

Exit code 0 on PASS, 1 on FAIL.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import build_gdocs as bg  # noqa: E402  (reuse parse_msg_*)

# --------------------------------------------------------------------------
# Word lists
# --------------------------------------------------------------------------

# Lowercase common words: articles, pronouns, conjunctions, prepositions,
# auxiliaries, common verbs/adjectives/adverbs, interjections, contractions.
# A capitalized word that lowercases into this set is NOT treated as a name.
COMMON = set("""
a an the this that these those some any every each all both few many much more
most other another such no not only own same so than too very just even still
also as at by in of on to up down out off over under with from into through
during before after above below between among about against along around behind
beside beyond despite toward towards upon within without except unless until
while though although because since if then when where why how what which who
whom whose whatever whoever and but or nor for yet whether
i me my mine we us our ours you your yours he him his she her hers it its they
them their theirs
am is are was were be been being have has had having do does did doing done
will would shall should can could may might must ought
get got getting go going went gone come coming came make making made take
taking took taken give giving gave given know knowing knew known think thinking
thought see seeing saw seen look looking looked say saying said tell telling
told ask asking asked want wanting wanted like liking liked love loving loved
feel feeling felt seem seemed become becoming became keep keeping kept put
putting let letting hear hearing heard bring brought leave left find found talk
talked walk walked run ran sit sat stand stood eat ate drink drank sleep slept
die died live lived kill killed save saved help helped pay paid buy bought sell
sold send sent show showed teach taught pray prayed work worked play played
wait waited try tried start started stop stopped open opened close closed break
broke build built grow grew fall fell rise rose lead led lose lost win won meet
met mean meant hold held wear wore write wrote read speak spoke spend spent
forget forgot forgive forgave choose chose drive drove throw threw catch caught
call called turn turned follow followed
good better best bad worse worst big bigger biggest small smaller smallest
large little great greater greatest high higher highest low lower lowest long
longer longest short shorter shortest new newer newest old older oldest young
younger youngest first last next real really true truly right wrong sure
certainly probably maybe perhaps always never ever often sometimes usually
quite rather enough less least well far near soon late early fast slow hard easy
whole full empty clean dirty hot cold warm cool bright dark loud quiet quick
strong weak rich poor happy sad glad sorry
yes oh hey hi hello ok okay wow uh um
don't doesn't didn't won't wouldn't can't couldn't shouldn't isn't aren't
wasn't weren't hasn't haven't hadn't i'm you're he's she's it's we're they're
i've you've we've they've i'll you'll he'll she'll it'll we'll they'll that's
there's here's what's who's let's ain't gotta gonna wanna kinda sorta
""".split())

NUMBER_WORDS = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
    'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
    'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
    'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
    'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
    'seventy': 70, 'eighty': 80, 'ninety': 90,
    'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5,
    'sixth': 6, 'seventh': 7, 'eighth': 8, 'ninth': 9, 'tenth': 10,
    'eleventh': 11, 'twelfth': 12, 'thirteenth': 13, 'fourteenth': 14,
    'fifteenth': 15, 'sixteenth': 16, 'seventeenth': 17, 'eighteenth': 18,
    'nineteenth': 19, 'twentieth': 20, 'thirtieth': 30, 'fortieth': 40,
    'fiftieth': 50, 'sixtieth': 60, 'seventieth': 70, 'eightieth': 80,
    'ninetieth': 90, 'hundred': 100, 'thousand': 1000,
}

# Known legitimate synonym pairs (applied symmetrically).
ALIASES = {
    'satan': {'devil'},
    'devil': {'satan'},
    'messiah': {'christ'},
    'christ': {'messiah'},
    'father': {'dad'},
    'dad': {'father'},
    'mother': {'mom'},
    'mom': {'mother'},
    'baptizer': {'baptist'},
    'baptist': {'baptizer'},
    'ninevites': {'nineveh'},
    'nineveh': {'ninevites'},
    'nazarene': {'nazareth'},
    'nazareth': {'nazarene'},
    # place <-> people-adjective pairs (MSG "Syro-Phoenician" / teen "Syro-Phoenicia")
    'phoenician': {'phoenicia'},
    'phoenicia': {'phoenician'},
    'galilean': {'galilee'},
    'galilee': {'galilean'},
    'judean': {'judea'},
    'judea': {'judean'},
    'samaritan': {'samaria'},
    'samaria': {'samaritan'},
}

# Theologically significant terms that must always be checked even though
# they are frequent English words (God, Jesus, ... are never "common words"
# for this gate's purpose).
BIBLICAL_NAMES = {
    'god', 'jesus', 'christ', 'lord', 'satan', 'devil', 'messiah',
    'spirit', 'father', 'son', 'word', 'savior', 'saviour', 'almighty',
    'king',
}

QUOTE_COVERAGE_MIN = 0.4  # stemmed distinctive-word coverage below this => FAIL


def _load_freq_words():
    """Top-30k English word frequencies (data file shipped with the script).
    A capitalized word whose lowercase form is frequent is treated as an
    ordinary word, not a name -- unless it is in BIBLICAL_NAMES."""
    try:
        with open(os.path.join(HERE, 'freq_words.txt'), encoding='utf-8') as f:
            return {line.strip() for line in f if line.strip()}
    except FileNotFoundError:
        return set()


FREQ = _load_freq_words() | COMMON
# A few frequent words missing from the 30k list, observed in MSG text.
FREQ |= {'adoration', 'adorations'}


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def norm_word(w):
    """Lowercase + strip possessive, for comparison on both sides."""
    w = w.lower()
    if w.endswith("'s"):
        w = w[:-2]
    return w.strip("'")


def stem(w):
    """Tiny stemmer (quote-word comparison only). Applied to both sides, so
    over-stemming is harmless; it only needs to be consistent."""
    if len(w) > 6 and w.endswith('ing'):
        w = w[:-3]
    elif len(w) > 5 and w.endswith('ed'):
        w = w[:-2]
    if len(w) > 5 and w.endswith('ful'):
        w = w[:-3]
    if len(w) > 4 and w.endswith('ly'):
        w = w[:-2]
    if len(w) > 5 and w.endswith('en'):
        w = w[:-2]
    if len(w) > 4 and w.endswith('y'):
        w = w[:-1] + 'i'
    if len(w) > 3 and w.endswith('s') and not w.endswith('ss'):
        w = w[:-1]
    return w


def parse_badge(s):
    """'2-6' -> {2..6}; '1' -> {1}; None when unparseable."""
    try:
        vset = set()
        for atom in str(s).split(','):
            atom = atom.strip()
            m = re.fullmatch(r'(\d+)(?:-(\d+))?', atom)
            if not m:
                return None
            a = int(m.group(1))
            b = int(m.group(2)) if m.group(2) else a
            if b < a or b - a > 300:
                return None
            vset.update(range(a, b + 1))
        return vset or None
    except Exception:
        return None


def embedded_verses(text):
    """Verse ranges printed inside MSG text, e.g. '...son: 2-6 Abraham had...'."""
    out = set()
    for a, b in re.findall(r'(\d{1,3})\s*-\s*(\d{1,3})', text):
        a, b = int(a), int(b)
        if a <= b and b - a < 200:
            out.update(range(a, b + 1))
    return out


def strip_artifacts(text):
    """Remove embedded verse-range markers and Psalm numbers before token
    extraction so they are not mistaken for content numbers. Also removes
    the 'twenty-twenty' idiom (means 'perfect', not the number 20)."""
    text = re.sub(r'\b\d{1,3}\s*-\s*\d{1,3}\b', ' ', text)
    text = re.sub(r'[Pp]salm\s+\d+', 'Psalm', text)
    text = re.sub(r'\btwenty-twenty\b', ' ', text, flags=re.I)
    return text


def extract_names(text):
    """Capitalized words that are not ordinary frequent English words.
    Biblical names are always tokens even when the word itself is frequent
    ('God', 'Christ', ...). Sentence-initial ordinary words ('Banter ...',
    'Pursue life') are excluded via the frequency list."""
    out, seen = [], set()
    for m in re.finditer(r"[A-Za-z][a-zA-Z']*", text):
        w = m.group()
        # strip possessives: "Jesus's"/"Jesus'" -> "Jesus"; other
        # apostrophe words are contractions ("I'd", "They'd") -> skip
        w = re.sub(r"'s$", '', w)
        w = re.sub(r"s'$", 's', w)
        if "'" in w:
            continue
        if not w[0].isupper():
            continue
        nw = norm_word(w)
        if len(nw) < 2 or nw in seen or nw in NUMBER_WORDS:
            continue
        if nw not in FREQ or nw in BIBLICAL_NAMES:
            seen.add(nw)
            out.append(nw)
    return out


def _parse_num_seq(words, i):
    total, cur, started = 0, 0, False
    last_v = None
    n = len(words)
    while i < n:
        w = words[i]
        if w in ('a', 'an'):
            if not started:
                cur, started = 1, True
                i += 1
                continue
            break
        if w == 'and' and started and i + 1 < n and words[i + 1] in NUMBER_WORDS:
            i += 1
            continue
        if w not in NUMBER_WORDS:
            break
        v, started = NUMBER_WORDS[w], True
        if v == last_v and v < 100:
            # reduplication ("twenty twenty") -- count once
            i += 1
            continue
        last_v = v
        if v == 100:
            cur = (cur or 1) * 100
        elif v == 1000:
            cur = (cur or 1) * 1000
            total, cur = total + cur, 0
        else:
            cur += v
        i += 1
    if not started:
        return None, i
    return total + cur, i


def _one_is_numeric(cwords, lowers, i):
    # 'no one' / 'one another' are pronouns, never the number 1.
    if i > 0 and lowers[i - 1] == 'no':
        return False
    if i + 1 < len(lowers) and lowers[i + 1] == 'another':
        return False
    # 'one of ...' is numeric; 'the One' (a title) is numeric;
    # 'one and only ...' is numeric.
    # Bare 'one' ('handed him one', 'one and all', 'One poor widow',
    # 'One day') is a pronoun / idiom / indefinite, not numeric content.
    if i + 1 < len(lowers) and lowers[i + 1] == 'of':
        return True
    if i > 0 and lowers[i - 1] == 'the':
        return True
    if (i + 2 < len(lowers) and lowers[i + 1] == 'and'
            and lowers[i + 2] == 'only'):
        return True
    return False


def extract_numbers(text):
    nums = set()
    # protect thousand separators: "1,000" -> "1000"
    t = re.sub(r'(\d),(\d{3})(?!\d)', r'\1\2', text)
    for m in re.finditer(r'\d+', t):
        nums.add(int(m.group()))
    # Parse number-word sequences clause by clause, so adjacent phrases
    # ("one of the Twelve, one who eats") don't merge into one number.
    for clause in re.split(r'[,.!?;:—""()\[\]]+', t):
        cwords = re.findall(r'[a-zA-Z]+', clause)
        lowers = [w.lower() for w in cwords]
        i, n = 0, len(lowers)
        while i < n:
            w = lowers[i]
            if w == 'one' and not _one_is_numeric(cwords, lowers, i):
                i += 1
                continue
            if w in NUMBER_WORDS or (w in ('a', 'an') and i + 1 < n
                                     and lowers[i + 1] in ('hundred', 'thousand')):
                val, i = _parse_num_seq(lowers, i)
                if val:
                    nums.add(val)
                continue
            i += 1
    return nums


def quote_spans(text):
    spans = []
    for m in re.finditer(r'"([^"]+)"|“([^”]+)”', text):
        spans.append(m.group(1) or m.group(2))
    return spans


def distinctive_words(span, covered_names):
    """Uncommon words inside a quote -- the paraphrase-resistant core of
    quoted speech. Names/numbers are checked separately; ordinary frequent
    words are excluded so legitimate rewording does not fail."""
    out = []
    for m in re.finditer(r"[A-Za-z][a-zA-Z']*", span):
        nw = norm_word(m.group())
        if len(nw) < 5 or nw in FREQ or nw in NUMBER_WORDS:
            continue
        if nw in covered_names or nw in out:
            continue
        out.append(nw)
    return out


def infer_book(path):
    base = os.path.basename(path)
    if base.endswith('.json'):
        base = base[:-5]
    if base.startswith('en_'):
        base = base[3:]
    base = re.sub(r'_(\d+)-(\d+)$', '', base)
    # strip any other trailing suffix (e.g. _negtest, _all) for matching
    for key in bg.BOOK_MAP:
        kl = key.lower()
        if base.lower() == kl or base.lower().startswith(kl + '_'):
            return key
    raise SystemExit(f'cannot infer book from file name: {path!r}')


def load_msg_units(book):
    if book == 'Matthew':
        return bg.parse_msg_matthew()
    if book == 'Romans':
        return bg.parse_msg_romans()
    return bg.parse_msg_txt(os.path.join(REVIEW, f'msg_{book}.txt'))


# --------------------------------------------------------------------------
# Core check
# --------------------------------------------------------------------------

def check_file(path):
    book = infer_book(path)
    units = load_msg_units(book)
    by_ch = {}
    for u in units:
        by_ch.setdefault(u['chapter'], []).append(u)

    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    failures, warnings = [], []
    stats = {'chapters': 0, 'paras': 0, 'names': 0, 'numbers': 0, 'quotes': 0}

    for ch in data:
        chno = ch.get('chapter')
        paras = ch.get('paragraphs', [])
        # Pair badges with checkable (non-header, non-empty) paragraphs.
        # Some files give § headers no badge (len(badges) == len(checkable));
        # others give every paragraph a badge (len(badges) == len(paras)).
        # Try msg_ranges first, then verseRanges: a teen-side split (e.g.
        # one MSG paragraph rendered as two) makes msg_ranges shorter than
        # the checkable list while verseRanges still aligns per paragraph.
        checkable = []
        for i, p in enumerate(paras):
            t = p if isinstance(p, str) else p.get('text', '')
            if not t or not t.strip() or t.lstrip().startswith('§'):
                continue  # headers and empties are not checked
            checkable.append((i, t))
        pairs = None
        tried = []
        for badges in (ch.get('msg_ranges'), ch.get('verseRanges')):
            if not badges:
                continue
            tried.append(len(badges))
            if len(badges) == len(checkable):
                pairs = [(i, t, badges[k]) for k, (i, t) in enumerate(checkable)]
                break
            if len(badges) == len(paras):
                pairs = [(i, t, badges[i]) for (i, t) in checkable]
                break
        if pairs is None:
            warnings.append(
                f'ch{chno}: STRUCTURAL -- {len(paras)} paragraphs, '
                f'badge lists tried {tried}; cannot align, chapter skipped')
            continue
        pinfos = []
        for i, t, vr in pairs:
            vset = parse_badge(vr)
            if vset is None:
                warnings.append(f'ch{chno} idx{i}: unparseable badge {vr!r} -- skipped')
                continue
            pinfos.append({'idx': i, 'badge': vr, 'vset': vset, 'text': t})
        if not pinfos:
            continue
        stats['chapters'] += 1
        stats['paras'] += len(pinfos)
        for pi in pinfos:
            pi['words'] = {norm_word(w)
                           for w in re.findall(r"[A-Za-z][a-zA-Z']*", pi['text'])}
            pi['stemmed'] = {stem(w) for w in pi['words']}
            pi['nums'] = extract_numbers(pi['text'])

        for u in by_ch.get(chno, []):
            raw_text = ' '.join(u['blocks'])
            if not raw_text.strip():
                continue
            attr = set(u['verses']) | embedded_verses(raw_text)
            covering = [pi for pi in pinfos if pi['vset'] & attr]
            if not covering:
                warnings.append(
                    f'ch{chno}: MSG verses {sorted(attr)} have no covering teen paragraph')
                continue
            union_words = set().union(*[pi['words'] for pi in covering])
            union_stemmed = set().union(*[pi['stemmed'] for pi in covering])
            union_nums = set().union(*[pi['nums'] for pi in covering])
            first = min(covering, key=lambda p: p['idx'])
            msg_ex = raw_text[:160].replace('\n', ' ')
            teen_ex = first['text'][:160].replace('\n', ' ')

            def fail(kind, missing):
                failures.append({
                    'ch': chno, 'idx': first['idx'], 'badge': first['badge'],
                    'kind': kind, 'missing': missing,
                    'msg_ex': msg_ex, 'teen_ex': teen_ex,
                })

            clean = strip_artifacts(raw_text)
            names = extract_names(clean)
            stats['names'] += len(names)
            missing_names = [t for t in names
                             if t not in union_words
                             and not (ALIASES.get(t, set()) & union_words)]
            if missing_names:
                fail('name', missing_names)

            nums = extract_numbers(clean)
            stats['numbers'] += len(nums)
            missing_nums = sorted(n for n in nums if n not in union_nums)
            if missing_nums:
                fail('number', [str(n) for n in missing_nums])

            name_set = set(names)
            for span in quote_spans(clean):
                dw = distinctive_words(span, name_set)
                if len(dw) < 3:
                    continue
                stats['quotes'] += 1

                def qpresent(w):
                    if stem(w) in union_stemmed:
                        return True
                    if ALIASES.get(w, set()) & union_words:
                        return True
                    # inflectional variant ("inconvenienced"/"inconvenience"):
                    # same first 6+ letters on both sides
                    need = min(6, len(w))
                    for tw in union_words:
                        if len(tw) >= need and tw[:need] == w[:need]:
                            return True
                    return False

                missing = [w for w in dw if not qpresent(w)]
                if (len(dw) - len(missing)) / len(dw) < QUOTE_COVERAGE_MIN:
                    fail('quote', missing[:8])

    return book, failures, warnings, stats


def main(argv):
    if not argv:
        print('usage: python3 completeness_check.py <en_json> [<en_json> ...]',
              file=sys.stderr)
        return 2
    all_failures, all_warnings = [], []
    total = {'chapters': 0, 'paras': 0, 'names': 0, 'numbers': 0, 'quotes': 0}
    for path in argv:
        book, failures, warnings, stats = check_file(path)
        print(f'--- {book}: {os.path.basename(path)} ---')
        for k in total:
            total[k] += stats[k]
        all_failures.extend([(path, f) for f in failures])
        all_warnings.extend([(path, w) for w in warnings])

    for _path, f in all_failures:
        print(f"FAIL ch{f['ch']} idx{f['idx']} [badge {f['badge']}] "
              f"{f['kind']}: {', '.join(f['missing'])}")
        print(f"  MSG : {f['msg_ex']}")
        print(f"  TEEN: {f['teen_ex']}")
    for _path, w in all_warnings:
        print(f'WARN {w}')

    print(f"Checked {total['chapters']} chapters, {total['paras']} paragraphs, "
          f"{total['names']} name tokens, {total['numbers']} number tokens, "
          f"{total['quotes']} quoted spans.")
    if all_failures:
        print(f"FAIL: {len(all_failures)} issue(s)")
        return 1
    print(f"PASS: {total['paras']}개 문단")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
