#!/usr/bin/env python3
"""Apply Numbers ch7-12 audit fixes."""
import json

REVIEW = '/home/hatch/workspace/teenz-bible-review'
en = json.load(open(f'{REVIEW}/fixes/en_Numbers.json', encoding='utf-8'))
ko = json.load(open(f'{REVIEW}/fixes/ko_Numbers.json', encoding='utf-8'))
FAILED = []
def rep(ch, lang, para, old, new):
    bk = en if lang == 'en' else ko
    p = bk[ch-1]['paragraphs'][para]
    if old not in p:
        FAILED.append((ch, lang, para, old[:60])); return
    bk[ch-1]['paragraphs'][para] = p.replace(old, new, 1)
def repall(ch, lang, old, new):
    bk = en if lang == 'en' else ko
    n = 0
    for i, p in enumerate(bk[ch-1]['paragraphs']):
        if old in p:
            bk[ch-1]['paragraphs'][i] = p.replace(old, new)
            n += 1
    print(f"  ch{ch} {lang}: replaced {n}x: {old[:50]!r}")
def badge(ch, lang, para, nb):
    (en if lang=='en' else ko)[ch-1]['verseRanges'][para] = nb
def title(ch, lang, nt):
    (en if lang=='en' else ko)[ch-1]['title'] = nt
def log(ch, lang, t):
    (en if lang=='en' else ko)[ch-1].setdefault('changes', []).append(t)

# ==================== CHAPTER 7 ====================
title(7, 'en', "The 12-Day Dedication Offerings")
title(7, 'ko', "12일간의 봉헌 예물")
repall(7, 'en',
    'a silver plate that weighed over three pounds and a silver bowl that was almost two pounds (using the official Sanctuary weights), both filled with fine flour mixed with oil for a Grain-Offering;',
    'a silver plate weighing three and a quarter pounds and a silver bowl weighing one and three-quarter pounds (according to the standard Sanctuary weights), each filled with fine flour mixed with oil as a Grain-Offering;')
repall(7, 'en',
    'a gold dish weighing four ounces, full of incense;',
    'a gold vessel weighing four ounces, filled with incense;')
repall(7, 'ko',
    '성소의 세겔로 1.5킬로그램 나가는 은 쟁반 하나랑 800그램 나가는 은 그릇 하나. 둘 다 고운 가루에 기름 섞은 소제물을 가득 채웠고,',
    '성소 표준 무게로 3.25파운드 나가는 은 쟁반 하나랑 1.75파운드 나가는 은 그릇 하나. 둘 다 고운 가루에 기름 섞은 소제물을 가득 채웠고,')
repall(7, 'ko',
    '114그램 나가는 금 그릇 하나. 향을 가득 채웠고,',
    '4온스 나가는 금 그릇 하나. 향을 가득 채웠고,')
rep(7, 'en', 90, 'twelve gold dishes.', 'twelve gold vessels.')
rep(7, 'en', 91, 'Each silver plate weighed over three pounds and each bowl was almost two pounds.',
    'Each plate weighed three and a quarter pounds and each bowl one and three-quarter pounds.')
rep(7, 'en', 91, 'the silver stuff weighed about sixty pounds',
    'the plates and bowls together weighed about sixty pounds')
rep(7, 'en', 91, 'The twelve gold dishes full of incense weighed four ounces each',
    'The twelve gold vessels filled with incense weighed four ounces each')
rep(7, 'en', 91, 'the gold dishes weighed about three pounds.',
    'the gold vessels weighed about three pounds.')
rep(7, 'ko', 91,
    '은 쟁반은 각각 1.5킬로그램이고 은 그릇은 각각 800그램이었어. 그래서 은으로 된 그릇들 무게를 다 합치면 (성소 공식 무게로) 약 27킬로그램이었대. 향을 가득 채운 금 그릇 열두 개는 각각 (성소 공식 무게로) 114그램이었고, 금 그릇들 무게를 다 합치면 약 1.4킬로그램이었어.',
    '은 쟁반은 각각 3.25파운드, 은 그릇은 각각 1.75파운드였어. 은 그릇들을 다 합치면 (성소 공식 무게로) 약 60파운드였대. 향을 가득 채운 금 그릇 열두 개는 각각 (성소 공식 무게로) 4온스였고, 금 그릇들을 다 합치면 약 3파운드였어.')
log(7, 'en', 'Restored MSG weights: 3.25/1.75 pounds, 4 ounces, 60/3 pounds; gold dish->vessel; titles cleaned')
log(7, 'ko', 'Restored MSG weights/units: 3.25/1.75파운드, 4온스, 60/3파운드 (was kg/g conversions)')

print("FAILED:", FAILED if FAILED else "none")
json.dump(en, open(f'{REVIEW}/fixes/en_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ko, open(f'{REVIEW}/fixes/ko_Numbers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("written")
