# -*- coding: utf-8 -*-
"""批 B/C 类深挖块幂等插入 MD(2026-09-29 · R57-BC 轻量对齐 A)。
用法: python3 scripts/enrich_bc.py [批JSON...]
块插在「## 七、跟进记录」之前(无此节则追加到档注线之前);已存在的同标记块先删后插(幂等)。
评级/CSV 原文不动;只加深挖块。"""
import json, re, sys
from pathlib import Path

ROOT = Path('/home/user/mikrotik-info')
MARK_RE = re.compile('(?m)^## 备护深挖.*?<!-- BDEEP:[^>]+-->\n?', re.S)

def render_block(r, batch_name, date):
    w = []
    w.append('\n## 备护深挖(%s · R57-BC 轻量对齐 A · 评级不动、不出信）\n' % date)
    w.append('**深挖三层**')
    w.append('- 【事实】%s' % r['fact'])
    w.append('- 【推断】%s' % r['inference'])
    w.append('- 【假设】%s' % r['hypothesis'])
    w.append('')
    s = r.get('swot') or {}
    if s:
        w.append('**SWOT 速描**')
        for k, label in (('S','S'), ('W','W'), ('O','O'), ('T','T')):
            if s.get(k):
                w.append('- **%s**: %s' % (label, s[k]))
        w.append('')
    if r.get('evidence'):
        w.append('**证据（quote → 来源）**')
        for e in r['evidence']:
            w.append('- 「%s」 — %s' % (e['quote'], e['source']))
        w.append('')
    w.append('**判位备档**(参考位，评级仍 %s · 不出信）' % 'B')
    w.append('- 参考 P1: `%s` — %s' % (r['p1'], r['p1_reason']))
    w.append('- 第一问: %s' % r['question'])
    w.append('- 标签: %s' % (r.get('tag') or '—'))
    w.append('')
    em = r.get('email') or ''
    if em:
        w.append('**备养出信稿（未触发，供后续用户启用参考）**')
        if em.startswith('【'):
            w.append('> %s' % em)
        else:
            w.append('```text\n%s\n```' % em)
        w.append('')
    if r.get('unknowns'):
        w.append('**待补证清单**')
        for i, u in enumerate(r['unknowns'], 1):
            w.append('%d. %s' % (i, u))
        w.append('')
    if r.get('followups'):
        w.append('**跟进建议（守档节奏）**')
        for f in r['followups']:
            w.append('- %s' % f)
        w.append('')
    if r.get('note'):
        w.append('> 备注: %s' % r['note'])
        w.append('')
    w.append('<!-- BDEEP:%s -->' % batch_name)
    w.append('')
    return '\n'.join(w)

def find_md(code):
    for td in ('B', 'C'):
        hits = list((ROOT / 'profile' / td).glob('%s-*.md' % code))
        if hits:
            return hits[0]
    return None

def main():
    files = sys.argv[1:] or sorted(str(p) for p in (ROOT / 'batch').glob('B类深挖_2026-09-29_R57-BC_第*波.json'))
    changed = []
    for f in files:
        d = json.loads((ROOT / f if not f.startswith('/') else Path(f)).read_text(encoding='utf-8'))
        bname = Path(f).stem
        for r in d['records']:
            md = find_md(r['code'])
            if md is None:
                print('❌ 无 MD: %s' % r['code'])
                continue
            txt = md.read_text(encoding='utf-8')
            prev = None
            while prev != txt:  # 幂等:循环删净所有旧块(累积多块场景)
                prev = txt
                txt = MARK_RE.sub('', txt)
            block = render_block(r, bname, d.get('date', '2026-09-29'))
            if '\n## 七、跟进记录' in txt:
                txt = txt.replace('\n## 七、跟进记录', block + '## 七、跟进记录', 1)
            elif '\n---\n\n*建档日期' in txt:
                txt = txt.replace('\n---\n\n*建档日期', block + '---\n\n*建档日期', 1)
            else:
                txt = txt.rstrip('\n') + '\n' + block
            md.write_text(txt, encoding='utf-8')
            changed.append(r['code'])
    print('enrich OK:%d 家已注入深挖块' % len(changed))
    print(' '.join(changed))

if __name__ == '__main__':
    main()
