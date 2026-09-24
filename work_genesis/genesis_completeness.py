#!/usr/bin/env python3
"""Genesis mechanical completeness using the checker's own token extractors,
aligned by verseRanges (authoritative per-paragraph badges) with union semantics."""
import json, re, sys
sys.path.insert(0, 'gdocs_build')
import build_gdocs as bg
import completeness_check as cc

units = bg.parse_msg_txt('msg_Genesis.txt')
by_ch = {}
for u in units: by_ch.setdefault(u['chapter'], []).append(u)
en = json.load(open('fixes/en_Genesis.json'))

issues = []
for ch in en:
    c = ch['chapter']
    paras = ch['paragraphs']; vrs = ch['verseRanges']
    verse_texts = {}
    for i, p in enumerate(paras):
        if p.lstrip().startswith('§') or not p.strip(): continue
        for v in cc.parse_badge(vrs[i]) or []:
            verse_texts.setdefault(v, []).append(p)
    for u in by_ch[c]:
        txt = ' '.join(u['blocks'])
        if not txt.strip(): continue
        attr = set(u['verses']) | cc.embedded_verses(txt)
        cov = []
        for v in attr:
            cov.extend(verse_texts.get(v, []))
        vr = f"{min(attr)}-{max(attr)}" if len(attr) > 1 else str(min(attr))
        if not cov:
            issues.append(('WARN', c, vr, 'NO-COVERAGE', txt, '')); continue
        blob = ' '.join(cov)
        names = cc.extract_names(txt)
        nums = cc.extract_numbers(txt)
        blob_words = {cc.norm_word(w) for w in re.findall(r"[A-Za-z][a-zA-Z']*", blob)}
        blob_stem = {cc.stem(w) for w in blob_words}
        blob_nums = cc.extract_numbers(blob)
        for n in names:
            if n not in blob_words and cc.stem(n) not in blob_stem and not (cc.ALIASES.get(n,set()) & blob_words):
                issues.append(('FIX', c, vr, f'name:{n}', txt, blob))
        for n in nums:
            if n not in blob_nums:
                issues.append(('FIX', c, vr, f'num:{n}', txt, blob))
        for q in cc.quote_spans(txt):
            dw = cc.distinctive_words(q, set(names))
            if len(dw) < 3: continue
            missing = [w for w in dw if not (cc.stem(w) in blob_stem or any(len(tw)>=min(6,len(w)) and tw[:min(6,len(w))]==w[:min(6,len(w))] for tw in blob_words))]
            if (len(dw)-len(missing))/len(dw) < cc.QUOTE_COVERAGE_MIN:
                issues.append(('FIX', c, vr, f'quote:{ "|".join(missing[:6])}', txt, blob))

with open('/tmp/gen_adj.txt','w',encoding='utf-8') as f:
    f.write(f"total: {len(issues)}\n")
    for t,c,vr,tok,msg,blob in issues:
        f.write(f"\n{'='*70}\n{t} ch{c} [{vr}] {tok}\nMSG : {msg}\nTEEN: {blob}\n")
print(f"total: {len(issues)}")
