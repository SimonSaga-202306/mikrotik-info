#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R65:B 类深挖户渲染为 v2 骨架（仅对既有 STRUCT 条目的 B 户,逐档输出)。

用法:python3 scripts/B类_v2渲染.py [B-001 B-106 ...]  (省略 = ENRICH_B 全部)
纪律:只写 profile/B 档;A/C 一概不碰;数据缺失照样渲染、缺失段如实「待定」。
"""
import csv, glob, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = '客户名单_反向信号_2026-09.csv'
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

from render_v2 import STRUCT, render  # noqa: E402
import make_profiles as mp  # noqa: E402  (取 ENRICH_B / without_contact_evidence / emails / phones / scenarios)


def _r56fu(rec):
    if not rec:
        return None
    fus = rec.get('followups') or rec.get('followup_plan')
    if not fus:
        return None
    out = []
    for f in fus:
        _st = re.sub(r'^第\s*[一二三四五六七八九十\d]+\s*次跟进\s*·\s*', '', f.get('stage', ''))
        out.append({'stage': _st, 'product': f.get('push') or f.get('product', '—'),
                    'angle': f.get('angle', ''), 'question': f.get('question', ''),
                    'proof': f.get('proof', '—')})
    return out or None


def _r56em(rec):
    if not rec or not rec.get('email'):
        return None
    return (rec.get('email_subject') or 'PoE switching for your line', rec['email'])


def csv_rows():
    with io.open(os.path.join(ROOT, CSV), encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f))
    hdr = rows[0]
    return hdr, [dict(zip(hdr, r)) for r in rows[1:]]


def safe(s):
    s = re.sub(r'[\\/:*?"<>|]+', '-', s or '').strip().strip('.')
    return (s[:60] or 'unnamed')


def main(codes):
    hdr, recs = csv_rows()
    by_code = {r['档案编号']: r for r in recs}
    targets = codes or sorted(mp.ENRICH_B)
    out = []
    for code in targets:
        r = by_code.get(code)
        if not r or r['评级'] != 'B' or code not in STRUCT:
            print('跳过(评级/行/STRUCT 不满足):', code)
            continue
        name, country, city, site = r['公司名'], r['国家'], r['城市'], r['网站']
        typ, signal, ownbrand, angle, sku = r['类型'], r['信号（在卖什么品牌）'], r['是否自有品牌'], r['切入点'], r['首推Saga型号']
        contact, prio, status, src, note, why = (r['入口/联系方式'], r['优先级'], r['状态'],
                                                 r['来源'], r['备注'], r['评级依据'])
        analysis_note = mp.without_contact_evidence(note or '')
        person = ''
        company = name
        if ' / ' in name:
            person, company = name.split(' / ', 1)
        mails = mp.emails((contact or '') + ' ' + analysis_note)
        tels = mp.phones(contact or '')
        e = STRUCT[code]
        rec_b = mp.ENRICH_B.get(code)
        ctx = dict(name=name, country=country, city=city, site=site, typ=typ,
                   signal=signal, ownbrand=ownbrand, angle=angle, sku=sku,
                   contact=contact, prio=prio, status=status, src=src, note=note or '',
                   why=why, rec=None, rec55=rec_b,
                   person=person, person_disp=(person or None), company=company,
                   mails=mails, tels=tels,
                   custom_followup=_r56fu(rec_b),
                   custom_email=_r56em(rec_b))
        fname = '%s-%s-%s.md' % (code, safe(name), safe(country))
        path = os.path.join(ROOT, 'profile', 'B', fname)
        L = render(e, ctx)
        open(path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
        out.append(fname)
        print('渲染:', fname, f'({len(L)} 行)')
    print(f'共 {len(out)} 档')


if __name__ == '__main__':
    main(sys.argv[1:])
