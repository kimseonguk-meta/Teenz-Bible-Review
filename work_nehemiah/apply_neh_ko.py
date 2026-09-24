#!/usr/bin/env python3
"""Apply Nehemiah audit fixes to fixes/ko_Nehemiah.json. Run from ~/workspace/teenz-bible-review."""
import json, os

REVIEW = os.path.expanduser('~/workspace/teenz-bible-review')
PK = os.path.join(REVIEW, 'fixes', 'ko_Nehemiah.json')
PE = os.path.join(REVIEW, 'fixes', 'en_Nehemiah.json')
ko = json.load(open(PK, encoding='utf-8'))
en = json.load(open(PE, encoding='utf-8'))
be = {c['chapter']: c for c in en}
bk = {c['chapter']: c for c in ko}
changes_log = []

def _variants(s):
    vs = [s]
    if '’' in s:
        vs.append(s.replace('’', "'"))
    if "'" in s:
        vs.append(s.replace("'", '’'))
    return vs

def sub(ch, idx, old, new, note):
    c = bk[ch]
    p = c['paragraphs'][idx]
    found = None
    for v in _variants(old):
        if v in p:
            found = v
            break
    assert found is not None, f'KO ch{ch} p{idx} NOT FOUND: {old[:70]!r}'
    c['paragraphs'][idx] = p.replace(found, new, 1)
    changes_log.append((ch, idx, note))

# ---- badges: copy EN scheme (already verified paragraph counts match, except ch11 handled below) ----
for ch in range(1, 14):
    if ch == 11:
        continue
    e, k = be[ch], bk[ch]
    assert len(e['paragraphs']) == len(k['paragraphs']), f'ch{ch} count mismatch'
    k['verseRanges'] = list(e['verseRanges'])
    k['msg_ranges'] = list(e['msg_ranges'])
    k['splits'] = json.loads(json.dumps(e['splits']))
    k['merges'] = json.loads(json.dumps(e.get('merges', [])))
    k['changes'].append('배지 수정: EN과 동일 (MSG 문단 기준)')

# ---- ch11: insert 3 towns into KO ----
c11 = bk[11]
e11 = be[11]
assert c11['paragraphs'][27].startswith('엔 림몬'), c11['paragraphs'][27][:20]
c11['paragraphs'].insert(28, '소라')
assert c11['paragraphs'][36].startswith('믹마스'), c11['paragraphs'][36][:20]
c11['paragraphs'].insert(37, '아이야')
assert c11['paragraphs'][40].startswith('놉과 아나냐'), c11['paragraphs'][40][:20]
c11['paragraphs'].insert(41, '하솔')
changes_log.append((11, 28, '지명 소라 복원'))
changes_log.append((11, 37, '지명 아이야 복원'))
changes_log.append((11, 41, '지명 하솔 복원'))
c11['verseRanges'] = list(e11['verseRanges'])
c11['msg_ranges'] = list(e11['msg_ranges'])
c11['splits'] = json.loads(json.dumps(e11['splits']))
c11['merges'] = []
c11['changes'].append('배지 수정: EN과 동일 (MSG 문단 기준), 지명 3문단 추가')
assert len(c11['paragraphs']) == 46 == len(c11['verseRanges'])

# ---- titles ----
bk[5]['title'] = be[5]['title']
changes_log.append((5, 'title', '제목 EN과 동일하게 변경'))
bk[13]['title'] = be[13]['title']
changes_log.append((13, 'title', '제목 EN과 동일하게 변경'))

# ---- ch2 ----
sub(2, 7, '심지어 왕은 기병대 호위까지 붙여줬음. 대박.', '심지어 왕은 기병대 호위까지 붙여줬음.', '대박 제거')

# ---- ch3 ----
sub(3, 1, '지들 주인 일을 돕기 싫다고', '자기 주인 일을 돕기 싫다고', '지들 순화')
sub(3, 10, '삽배의 아들 바룩은 완전 의욕 넘쳐서, 그 모퉁이부터', '삽배의 아들 바룩은 그 모퉁이부터', 'EN과 일치 (의욕 첨가 삭제)')
sub(3, 10, '우리야의 아들 므레못은', '학고스의 손자이자 우리야의 아들인 므레못은', '부칭 복원 (EN과 일치)')
sub(3, 10, '아사랴는 자기 집 옆에서 일했음.', '마아세야의 손자이자 아나냐의 아들인 아사랴는 자기 집 옆에서 일했음.', '부칭 복원 (EN과 일치)')

# ---- ch4 ----
sub(4, 4, '걔네를 막았지.', '그 사람들을 막았지.', '걔네 순화')
sub(4, 7, '“걔네가 우리를 포위했어요! 공격할 거예요!”', '"그 사람들이 우리를 포위했어요! 공격할 거예요!"', '걔네 순화')
sub(4, 9, '하나님이 걔네 계획을 망쳐놨다는 걸', '하나님이 그 사람들 계획을 망쳐놨다는 걸', '걔네 순화')

# ---- ch6 ----
sub(6, 0, '우리를 싫어하던 나머지 애들이', '우리를 싫어하던 나머지 사람들이', '애들 순화')
sub(6, 8, '그러다가 스마야라는 사람을 몰래 만났는데, 걔네 집에서 만났음. 걔가 나한테 말하는 거임.',
    '그러다가 들라야의 아들이자 므헤다벨의 손자인 스마야를 몰래 만났는데, 그 사람 집에서 만났음. 그 사람이 나한테 말하는 거임.', '부칭 복원·걔네 순화 (EN과 일치)')
sub(6, 9, '걔네가 당신 죽이러 올 거예요.', '그 사람들이 당신 죽이러 올 거예요.', '걔네 순화')
sub(6, 11, '걔네가 돈 주고 고용한 거임.', '그 사람들이 돈 주고 고용한 거임.', '걔네 순화')
sub(6, 13, '걔네는 완전 기가 죽어버렸음.', '그 사람들은 완전 기가 죽어버렸음.', '걔네 순화')
sub(6, 14, '왜냐면 걔가 아라의 아들 스가냐의 사위였고, 걔 아들 여호하난은',
    '왜냐면 그 사람이 아라의 아들 스가냐의 사위였고, 그 사람 아들 여호하난은', '걔 순화')
sub(6, 14, '내가 한 말을 그대로 걔한테 가서 일러바쳤음.', '내가 한 말을 그대로 그 사람한테 가서 일러바쳤음.', '걔 순화')

# ---- ch7 ----
sub(7, 37, '스나아 출신 3,930명. 대박 많네.', '스나아 출신 3,930명. 진짜 많네.', '대박 순화')

# ---- ch8 ----
sub(8, 3, "'아멘! 아멘!' 하고 대답하면서", "'오 그래! 그래!' 하고 대답하면서", 'MSG 인용구 복원 (EN과 일치)')

# ---- ch9 ----
sub(9, 4, '그들을 쫓던 애들은 깊은 바다에 던져버렸는데', '그들을 쫓던 사람들은 깊은 바다에 던져버렸는데', '애들 순화')
sub(9, 5, '심지어 걔네들이 송아지 상을 만들어서', '심지어 그 사람들이 송아지 상을 만들어서', '걔네 순화')

# ---- ch10 ----
sub(10, 4, '문지기, 노래하는 애들, 성전 일꾼들', '문지기, 노래하는 사람들, 성전 일꾼들', '애들 순화')
sub(10, 10, '우리 가축의 첫 녀석, 우리 소 떼와 양 떼의 첫 녀석를', '우리 가축의 첫 새끼, 우리 소 떼와 양 떼의 첫 새끼를', '녀석 순화')
sub(10, 11, '또 우리 밀가루 반죽의 첫 부분,', '또 우리 곡식의 첫 부분,', '오역 반죽→곡식 수정 (EN과 일치)')

# ---- ch12 ----
sub(12, 55, '호세야랑 유다 지도자 절반이', '하사야랑 유다 지도자 절반이', '오타 수정 (EN과 일치)')
sub(12, 55, '랑 그 형제들이 다윗의 악기를 연주하면서 따라갔어.',
    '랑 그 형제들인 스마야, 아사렐, 밀랄래, 길랄래, 마아이, 느다넬, 유다, 하나니가 다윗의 악기를 연주하면서 따라갔어.', '이름 8명 복원 (EN과 일치)')

# ---- ch13 ----
sub(13, 0, '걔네가 옛날에 이스라엘 백성들한테', '그 사람들이 옛날에 이스라엘 백성들한테', '걔네 순화')
sub(13, 1, '도비야라는 애랑 친해가지고', '도비야라는 사람이랑 친해가지고', '애 순화')
sub(13, 3, '그리고 하나냐라는 애를 오른팔로 붙여줬지.',
    '그리고 삭굴의 아들이자 맛다냐의 손자인 하나냐라는 사람을 오른팔로 붙여줬지.', '부칭 복원 (EN과 일치)')
sub(13, 8, '근데 내가 걔네들한테 경고했어.', '근데 내가 그 사람들한테 경고했어.', '걔네 순화')
sub(13, 12, '근데 걔네 자식들 절반은', '근데 그 사람들 자식들 절반은', '걔네 순화')

json.dump(ko, open(PK, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KO saved. changes:', len(changes_log))
for ch, idx, note in changes_log:
    print(f'  ch{ch} p{idx}: {note}')
