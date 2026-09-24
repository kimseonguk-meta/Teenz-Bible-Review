#!/usr/bin/env python3
"""Apply Nehemiah audit fixes to fixes/en_Nehemiah.json. Run from ~/workspace/teenz-bible-review."""
import json, os

REVIEW = os.path.expanduser('~/workspace/teenz-bible-review')
P = os.path.join(REVIEW, 'fixes', 'en_Nehemiah.json')
en = json.load(open(P, encoding='utf-8'))
by_ch = {c['chapter']: c for c in en}
changes_log = []

def _variants(s):
    vs = [s]
    if '’' in s:
        vs.append(s.replace('’', "'"))
    if "'" in s:
        vs.append(s.replace("'", '’'))
    return vs

def sub(ch, idx, old, new, note):
    c = by_ch[ch]
    p = c['paragraphs'][idx]
    found = None
    for v in _variants(old):
        if v in p:
            found = v
            break
    assert found is not None, f'EN ch{ch} p{idx} NOT FOUND: {old[:70]!r}'
    c['paragraphs'][idx] = p.replace(found, new, 1)
    changes_log.append((ch, idx, note))

def set_badges(ch, badges, msg_ranges, splits, merges=None, note=''):
    c = by_ch[ch]
    assert len(badges) == len(c['paragraphs']), f'ch{ch}: badges {len(badges)} != paras {len(c["paragraphs"])}'
    c['verseRanges'] = badges
    c['msg_ranges'] = msg_ranges
    c['splits'] = splits
    c['merges'] = merges or []
    c['changes'].append('배지 수정: ' + note if note else '배지 수정 (MSG 문단 기준)')

# ============ ch1 ============
set_badges(1, ['1-2','1-2','3','4','5-6','7-9','10-11','10-11'],
           ['1-2','3','4','5-6','7-9','10-11'],
           [{'msg_range':'1-2','paras':[0,1]},{'msg_range':'10-11','paras':[6,7]}],
           note='2-3→1-2, 4→3, 5-6→4, 6-7→5-6 (MSG 문단 기준); 1-2·10-11 split 선언')

# ============ ch2 ============
set_badges(2, ['1-2','2-3','4-5','4-5','6','6','7-8','8-9','10','11-12','13-16','17-18','17-18','19','20'],
           ['1-2','2-3','4-5','6','7-8','8-9','10','11-12','13-16','17-18','19','20'],
           [{'msg_range':'4-5','paras':[2,3]},{'msg_range':'6','paras':[4,5]},{'msg_range':'17-18','paras':[11,12]}],
           note='p5 7-8→6, p6 8-9→7-8, p7 10→8-9, p8 11-12→10 (1유닛씩 밀림 수정); 4-5·6·17-18 split 선언')
sub(2, 1, 'That question lowkey made me even more nervous.', 'That question made me even more nervous.', '슬랭 lowkey 제거')
sub(2, 5, 'and the king was like, “Alright, bet,” and gave me his permission.', 'and the king gave his approval to send me.', '슬랭 bet 제거 (MSG 표현 복원)')
sub(2, 8, 'they were super salty. They were seriously mad', 'they were seriously upset. They were really mad', '슬랭 salty 제거')
sub(2, 14, 'I clapped back,', 'I shot back,', '슬랭 clapped back 제거 (MSG 표현 복원)')

# ============ ch3 ============
set_badges(3, ['1-2','3-5','6-8','9-10','11-12','13','14','15','16','17-18','19-23','24-27','28-30','31-32'],
           ['1-2','3-5','6-8','9-10','11-12','13','14','15','16','17-18','19-23','24-27','28-30','31-32'],
           [], note='p5 13-14→13, p6 15→14, p7 16-17→15, p8 17-18→16, p9 19-23→17-18, p10 21-24→19-23 (1유닛씩 밀림 수정)')
sub(3, 1, 'Meremoth, Uriah’s son, worked next to them. Then there was Meshullam, and after him Zadok,',
    'Meremoth son of Uriah, son of Hakkoz, worked next to them. Then there was Meshullam son of Berekiah, son of Meshezabel, and after him Zadok son of Baana,', '부칭 3건 복원')
sub(3, 1, 'their big-shot leaders were too cool for school and refused to get their hands dirty and help out their master.',
    'their nobles refused to work with their master—they thought they were too important to get their hands dirty with this kind of work.', '슬랭 too cool for school 순화')
sub(3, 2, 'The Jeshanah Gate was rebuilt by Joiada and Meshullam.', 'The Jeshanah Gate was rebuilt by Joiada son of Paseah and Meshullam son of Besodeiah.', '부칭 복원')
sub(3, 2, 'Melatiah from Gibeon, Jadon from Meronoth,', 'Melatiah the Gibeonite, Jadon the Meronothite,', 'MSG 칭호 복원')
sub(3, 2, 'Uzziel, a goldsmith, worked on the next section,', 'Uzziel son of Harhaiah, one of the goldsmiths, worked on the next section,', '부칭 복원')
sub(3, 3, 'Rephaiah, who was basically the mayor of half of Jerusalem,', 'Rephaiah son of Hur, who was basically the mayor of half of Jerusalem,', '부칭 복원')
sub(3, 4, 'Malkijah and Hasshub rebuilt another section,', 'Malkijah son of Harim and Hasshub son of Pahath-Moab rebuilt another section,', '부칭 복원')
sub(3, 4, 'Shallum, the mayor of the other half of Jerusalem,', 'Shallum son of Hallohesh, the mayor of the other half of Jerusalem,', '부칭 복원')
sub(3, 6, 'that was rebuilt by Malkijah, the mayor of the Beth Hakkerem district.', 'that was rebuilt by Malkijah son of Recab, the mayor of the Beth Hakkerem district.', '부칭 복원')
sub(3, 7, 'The Fountain Gate was Shallun’s project.', "The Fountain Gate was Shallun son of Col-Hozeh's project.", '부칭 복원')
sub(3, 9, 'under Binnui, the mayor of the other half of Keilah.', 'under Binnui son of Henadad, the mayor of the other half of Keilah.', '부칭 복원')
sub(3, 10, 'Ezer, the mayor of Mizpah,', 'Ezer son of Jeshua, the mayor of Mizpah,', '부칭 복원')
sub(3, 10, 'Baruch son of Zabbai was super motivated and did the part', 'Baruch son of Zabbai did the part', 'MSG에 없는 동기 부여 삭제')
sub(3, 10, 'Meremoth took over from there and finished the wall', 'Meremoth son of Uriah, son of Hakkoz, took over from there and finished the wall', '부칭 복원')
sub(3, 10, 'and Azariah did the same, working right next to his house.', 'and Azariah son of Maaseiah, son of Ananiah, did the same, working right next to his house.', '부칭 복원')
sub(3, 11, 'Next to him was Pedaiah,', 'Next to him was Pedaiah son of Parosh,', '부칭 복원')
sub(3, 12, 'and then Shemaiah, the keeper of the East Gate, did his part. Then came Hananiah and Hanun,',
    'and then Shemaiah son of Shecaniah, the keeper of the East Gate, did his part. Then came Hananiah son of Shelemiah and Hanun, the sixth son of Zalaph,', '부칭·서열 복원')

# ============ ch4 ============
set_badges(4, ['1-2','3','4-5','6','7-9','10','10','11-12','13-14','15-18','19-20','21','22','23'],
           ['1-2','3','4-5','6','7-9','10','11-12','13-14','15-18','19-20','21','22','23'],
           [{'msg_range':'10','paras':[5,6]}],
           note='p5 7-9→10, p8 13-15→13-14, p9 16-19→15-18 (밀림 수정); 10 split 선언')
sub(4, 2, 'because they’ve been dissing the builders to their faces!', "because they've insulted the builders!", '슬랭 dissing 제거·첨가(to their faces) 삭제')
sub(4, 8, 'and fight for your families, your sons,', 'and fight for your brothers, your sons,', 'MSG brothers 복원')
sub(4, 11, 'working from sunup to sundown, with half of us holding spears the whole time.', 'working from sunup until the stars came out, with half of us holding spears the whole time.', 'MSG 밤 요소 복원')

# ============ ch5 ============
set_badges(5, ['1-2','3','4-5','6-7','7-8','7-8','9','10-11','12-13','12-13','12-13','14-16','17-18','19'],
           ['1-2','3','4-5','6-7','7-8','9','10-11','12-13','14-16','17-18','19'],
           [{'msg_range':'7-8','paras':[4,5]},{'msg_range':'12-13','paras':[8,9,10]}],
           note='p1 1-2→3, p2 3-4→4-5, p3 4-5→6-7, p4 6-7→7-8, p9 13-14→12-13, p10 14-16→12-13, p11 16-17→14-16 (밀림 수정); 7-8·12-13 split 선언')
sub(5, 11, 'taxing them about a pound of silver a day for food and wine,', 'taxing them forty shekels of silver (about a pound) a day for food and wine,', '숫자 forty shekels 복원')
by_ch[5]['title'] = 'Nehemiah Calls Out the Rich Bullies'
changes_log.append((5, 'title', '슬랭 Goes OFF → Calls Out'))

# ============ ch6 ============
set_badges(6, ['1-2','2-3','4','5-6','6-7','8','9','9','10','10','11','12-13','14','15-16','17-19'],
           ['1-2','2-3','4','5-6','6-7','8','9','10','11','12-13','14','15-16','17-19'],
           [{'msg_range':'9','paras':[6,7]},{'msg_range':'10','paras':[8,9]}],
           note='p1 3-4→2-3, p2 5-6→4, p4 7-8→6-7, p5 9→8, p6 10→9, p8 12-13→10, p10 14→11, p11 15-16→12-13, p12 17-19→14, p13 17-19→15-16 (밀림 수정); 9·10 split 선언')
sub(6, 8, 'Then I went to have a secret meeting with this guy Shemaiah.', 'Then I secretly met with Shemaiah son of Delaiah, the son of Mehetabel, at his house.', '부칭·장소 복원')
sub(6, 14, 'because he was the son-in-law of Shecaniah, and his own son had married the daughter of Meshullam.',
    'because he was the son-in-law of Shecaniah son of Arah, and his son Jehohanan had married the daughter of Meshullam son of Berekiah.', '부칭·이름 3건 복원')

# ============ ch7 ============
b7 = ['1-2','3','4','5'] + ['6-60']*62 + ['61-63']*4 + ['64-65'] + ['66-69'] + ['70-72'] + ['73']
set_badges(7, b7,
           ['1-2','3','4','5','6-60','61-63','64-65','66-69','70-72','73'],
           [{'msg_range':'6-60','paras':list(range(4,66))},{'msg_range':'61-63','paras':[66,67,68,69]}],
           note='p1 1-2→3, p2 1-2→4, p3 3→5, p4 4→6-60, p61-65 61-63/64-65→6-60, p66-69 66-69→61-63, p70 70-72→64-65, p71 70-72→66-69 (밀림 수정); 6-60·61-63 split 선언')
sub(7, 0, 'a super solid dude who, no cap, respected God more than pretty much anyone.', 'a super solid dude who respected God more than pretty much anyone.', '슬랭 no cap 제거')
sub(7, 72, 'The governor himself donated about 19 pounds of gold, 50 bowls, and 530 sets of clothes for the priests.',
    'The governor himself donated 1,000 drachmas of gold (about 19 pounds), 50 bowls, and 530 sets of clothes for the priests.', '숫자 1,000 drachmas 복원')
sub(7, 72, 'Other family heads gave about 20,000 drachmas of gold and over a ton of silver.',
    'Other family heads gave 20,000 drachmas of gold and 2,200 minas of silver (about one and a third tons).', '단위 2,200 minas 복원')
sub(7, 72, 'The rest of the people pitched in about 375 pounds of gold, 2,000 minas of silver, and 67 sets of priest clothes.',
    'The rest of the people pitched in 20,000 drachmas of gold (about 375 pounds), 2,000 minas of silver, and 67 sets of priest clothes.', '숫자 20,000 drachmas 복원')

# ============ ch8 ============
set_badges(8, ['1','2-3','4','5-6','7-8','9','10','11','12','13-15','16-17','18'],
           ['1','2-3','4','5-6','7-8','9','10','11','12','13-15','16-17','18'],
           [], note='p0 1-2→1, p1 3-4→2-3, p2 5-6→4, p3 6-7→5-6 (밀림 수정)')
sub(8, 3, "yelled back, 'Amen! For real!'", "shouted back, 'Oh yes! Yes!'", 'MSG 인용구 복원')
sub(8, 4, 'The Levites—Jeshua, Bani, Sherebiah, and the rest of the crew—went around',
    'The Levites—Jeshua, Bani, Sherebiah, Jamin, Akkub, Shabbethai, Hodiah, Maaseiah, Kelita, Azariah, Jozabad, Hanan, and Pelaiah—went around', '레위인 10명 이름 복원')

# ============ ch9 ============
set_badges(9, ['1-3','4-5','5-6','7-8','9-15','16-19','20-23','24-25','26-31','32-37','38'],
           ['1-3','4-5','5-6','7-8','9-15','16-19','20-23','24-25','26-31','32-37','38'],
           [], note='p1 1-3→4-5, p2 4-5→5-6, p3 4-5→7-8, p4 7-9→9-15, p5 9-15→16-19, p6 16-19→20-23, p7 20-23→24-25, p8 23-26→26-31, p9 31-33→32-37, p10 37-38→38 (밀림 수정)')
sub(9, 0, 'They basically unfriended all the foreigners', 'They cut off all ties with the foreigners', '슬랭 unfriended 순화')
sub(9, 4, 'Through your boy Moses,', 'Through Moses, your servant,', '슬랭 your boy 순화')
sub(9, 7, 'fully-furnished houses, wells, vineyards,', 'fully-furnished houses, cisterns, vineyards,', 'MSG cisterns 복원')

# ============ ch10 ============
set_badges(10, ['1-8','1-8','9-13','14-27','28-30','28-30','28-30','31','31','32-33','34','35-36','37-39','37-39'],
           ['1-8','9-13','14-27','28-30','31','32-33','34','35-36','37-39'],
           [{'msg_range':'1-8','paras':[0,1]},{'msg_range':'28-30','paras':[4,5,6]},{'msg_range':'31','paras':[7,8]},{'msg_range':'37-39','paras':[12,13]}],
           note='p2 1-8→9-13, p3 9-13→14-27, p4 14-27→28-30, p7 14-27→31, p9 14-27→32-33, p10 28-30→34, p11 30-32→35-36, p12 33-38→37-39 (밀림 수정); 1-8·28-30·31·37-39 split 선언')
sub(10, 2, 'and their boys:', 'and their fellow Levites:', '슬랭 boys 순화')
sub(10, 8, 'cancel all debts. No cap.', 'cancel all debts.', '슬랭 No cap 제거')
sub(10, 9, 'We’ll pay a yearly tax to cover the costs', 'We’ll pay a yearly tax of one-third of a shekel (about an eighth of an ounce) to cover the costs', '세율 복원')
sub(10, 9, 'the sin offerings to make things right for Israel, and basically', 'the dedication offerings, the sin offerings to make things right for Israel, and basically', 'Dedication-Offerings 복원')
sub(10, 12, 'the best of our dough,', 'the best of our grain,', '오역 dough→grain 수정')

# ============ ch11 ============
b11 = ['1-2','3-4','4-6','4-6','7-9','7-9','10-14','10-14','15-18','15-18','19','19','20','21','22-23','24'] + ['25-30']*18 + ['31-36']*9
set_badges(11, b11,
           ['1-2','3-4','4-6','7-9','10-14','15-18','19','20','21','22-23','24','25-30','31-36'],
           [{'msg_range':'4-6','paras':[2,3]},{'msg_range':'7-9','paras':[4,5]},{'msg_range':'10-14','paras':[6,7]},{'msg_range':'15-18','paras':[8,9]},{'msg_range':'19','paras':[10,11]},{'msg_range':'25-30','paras':list(range(16,34))},{'msg_range':'31-36','paras':list(range(34,43))}],
           note='p2 3-4→4-6 (밀림 수정); 4-6·7-9·10-14·15-18·19·25-30·31-36 split 선언')
# restore dropped towns: Zorah (after En Rimmon), Aijah (after Micmash), Hazor (after Nob and Ananiah)
c11 = by_ch[11]
assert c11['paragraphs'][27] == 'En Rimmon', c11['paragraphs'][27]
c11['paragraphs'].insert(28, 'Zorah')
c11['verseRanges'].insert(28, '25-30')
changes_log.append((11, 28, '지명 Zorah 복원 (MSG 25-30 목록)'))
# re-check indices after insert
assert c11['paragraphs'][36] == 'Micmash', c11['paragraphs'][36]
c11['paragraphs'].insert(37, 'Aijah')
c11['verseRanges'].insert(37, '31-36')
changes_log.append((11, 37, '지명 Aijah 복원 (MSG 31-36 목록)'))
assert c11['paragraphs'][40] == 'Nob and Ananiah', c11['paragraphs'][40]
c11['paragraphs'].insert(41, 'Hazor')
c11['verseRanges'].insert(41, '31-36')
changes_log.append((11, 41, '지명 Hazor 복원 (MSG 31-36 목록)'))
# fix split para indices after 3 inserts
c11['splits'] = [{'msg_range':'4-6','paras':[2,3]},{'msg_range':'7-9','paras':[4,5]},{'msg_range':'10-14','paras':[6,7]},{'msg_range':'15-18','paras':[8,9]},{'msg_range':'19','paras':[10,11]},{'msg_range':'25-30','paras':list(range(16,37))},{'msg_range':'31-36','paras':list(range(37,46))}]
assert len(c11['paragraphs']) == 46 and len(c11['verseRanges']) == 46

# ============ ch12 ============
c12 = by_ch[12]
b12 = list(c12['verseRanges'])
assert b12[61] == '45-47', b12[61]
b12[61] = '47'
c12['verseRanges'] = b12
c12['msg_ranges'] = ['1-7','8-9','10-11','12-21','22','23-24','25-26','27-29','30','31-36','37','38-39','40-42','43','44-46','47']
c12['splits'] = [{'msg_range':'1-7','paras':list(range(0,9))},{'msg_range':'8-9','paras':[9,10,11]},{'msg_range':'10-11','paras':list(range(12,18))},{'msg_range':'12-21','paras':list(range(18,39))},{'msg_range':'23-24','paras':list(range(40,45))},{'msg_range':'25-26','paras':list(range(45,53))}]
c12['merges'] = []
c12['changes'].append('배지 수정: p61 45-47→47 (MSG 문단 기준); 1-7·8-9·10-11·12-21·23-24·25-26 split 선언')
sub(12, 55, 'Hoshaiah and half of Judah’s leaders', "Hashaiah and half of Judah's leaders", '오타 Hoshaiah→Hashaiah (MSG)')
sub(12, 55, 'and his crew, playing the instruments of David, the man of God.',
    'and his brothers Shemaiah, Azarel, Milalai, Gilalai, Maai, Nethanel, Judah, and Hanani, playing the instruments of David, the man of God.', '이름 8명 복원')

# ============ ch13 ============
set_badges(13, ['1-3','4-5','6-9','10-13','14','15-16','17-18','19','20-21','20-21','22','22','23-27','28','29','30-31','30-31'],
           ['1-3','4-5','6-9','10-13','14','15-16','17-18','19','20-21','22','23-27','28','29','30-31'],
           [{'msg_range':'20-21','paras':[8,9]},{'msg_range':'22','paras':[10,11]},{'msg_range':'30-31','paras':[15,16]}],
           note='p5 15-17→15-16, p6 18-19→17-18, p7 20-21→19, p8 22→20-21, p9 23-27→20-21, p10 23-27→22, p11 23-27→22 (밀림 수정); 20-21·22·30-31 split 선언')
sub(13, 0, 'But God, being the GOAT, flipped the curse into a blessing.', 'But God flipped the curse into a blessing.', '슬랭 GOAT 제거')
sub(13, 0, "As soon as the people heard this, they were like, 'Aight, bet,' and kicked all the foreigners out of Israel.",
    'When the people heard the reading of the Law, they excluded all the foreigners from Israel.', '슬랭 Aight/bet 제거 (MSG 표현 복원)')
sub(13, 1, 'He was boys with this dude Tobiah and gave him a huge room that was supposed to be for all the holy stuff—like offerings, incense, and all the supplies for the Levites and priests.',
    'He was close friends with Tobiah and gave him a large room that was supposed to store the grain offerings, incense, worship vessels, and the tithes of grain, wine, and oil for the Levites, singers, and security guards, plus the offerings for the priests.', '슬랭 boys 순화·창고 내용물 세부 복원')
sub(13, 3, "called out the officials, like, 'Why is God's Temple being ghosted?'", "called out the officials, like, 'Why has God's Temple been abandoned?'", '슬랭 ghosted 제거 (MSG 표현 복원)')
sub(13, 3, 'And I made Hanan, the son of Zaccur, their right-hand man.', 'And I made Hanan son of Zaccur, the son of Mattaniah, their right-hand man.', '부칭 복원')
sub(13, 6, 'piling up more anger on Jerusalem by dissing the Sabbath.', 'piling up more anger on Jerusalem by profaning the Sabbath.', '슬랭 dissing 제거')
sub(13, 7, 'So, as the sun started to set on Friday, right before the Sabbath began,',
    'So, as the gates of Jerusalem were darkened by the shadows of the approaching Sabbath,', 'MSG 표현 복원 (Friday 첨가 삭제)')
sub(13, 8, 'But I went off on them.', 'But I confronted them.', '슬랭 went off 순화')
sub(13, 14, 'for how they trashed the priesthood', 'for how they defiled the priesthood', '슬랭 trashed 순화')
by_ch[13]['title'] = 'Nehemiah Cleans House'
changes_log.append((13, 'title', '슬랭 No Cap 제거'))

json.dump(en, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('EN saved. changes:', len(changes_log))
for ch, idx, note in changes_log:
    print(f'  ch{ch} p{idx}: {note}')
