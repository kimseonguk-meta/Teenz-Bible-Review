#!/usr/bin/env node
// 4권 EN/KO 원본 추출 -> work_<book>/en_<book>.json, ko_<book>.json
const fs = require('fs');
const path = require('path');
const BASE = path.dirname(__dirname);

const enAll = JSON.parse(fs.readFileSync('/home/hatch/workspace/teenz-fix/client/src/data/allBibleData.json', 'utf8'));
let koSrc = fs.readFileSync('/home/hatch/workspace/teenz-fix/client/src/data/gospelDataKo.ts', 'utf8');
koSrc = koSrc.replace(/^export const gospelDataKo[^=]*=/, '').trim().replace(/;\s*$/, '');
const koAll = eval('(' + koSrc + ')');

const books = [
  ['Jeremiah', 'work_jeremiah'],
  ['Lamentations', 'work_lamentations'],
  ['Ezekiel', 'work_ezekiel'],
  ['Daniel', 'work_daniel'],
];
for (const [book, dir] of books) {
  const enCh = enAll[book];
  const koCh = koAll[book];
  if (!enCh || !koCh) { console.error('MISSING', book); process.exit(1); }
  const enOut = enCh.map(c => ({num: c.num, title: c.title, paragraphs: c.paragraphs, verseRanges: c.verseRanges || c.paragraphs.map(() => null)}));
  const koOut = koCh.map(c => ({num: c.num, title: c.title, paragraphs: c.paragraphs, verseRanges: c.verseRanges || c.paragraphs.map(() => null)}));
  fs.writeFileSync(path.join(BASE, dir, `en_${book.toLowerCase()}.json`), JSON.stringify(enOut, null, 1));
  fs.writeFileSync(path.join(BASE, dir, `ko_${book.toLowerCase()}.json`), JSON.stringify(koOut, null, 1));
  console.log(book, enOut.length, 'chapters extracted');
  // EN/KO 문단 수·배지 parity 사전 점검
  for (let i = 0; i < enOut.length; i++) {
    const e = enOut[i], k = koOut[i];
    if (e.paragraphs.length !== k.paragraphs.length)
      console.log(`  PARITY ch${e.num}: EN ${e.paragraphs.length} vs KO ${k.paragraphs.length}`);
    if (JSON.stringify(e.verseRanges) !== JSON.stringify(k.verseRanges))
      console.log(`  BADGE ch${e.num}: EN ${JSON.stringify(e.verseRanges)} vs KO ${JSON.stringify(k.verseRanges)}`);
    if (e.verseRanges.some(b => !b))
      console.log(`  NULLBADGE EN ch${e.num}`);
    if (k.verseRanges.some(b => !b))
      console.log(`  NULLBADGE KO ch${e.num}`);
  }
}
