# -*- coding: utf-8 -*-
"""R64（2026-10-07）A 类 KP(关键人)猎捕批 · 第 1 波 = R63 新升 12 户。

方法（用户 2026-10-06/07 指令「着重抓 KP 想一切办法搞到」）:
  1. web_search 搜 KP 人名/职位(领英公开摘要/RocketReach/D&B/contactout/工商登记)
  2. 邮箱排列组合生成候选(first@/first.last@/f.last@/firstlast@/flast@)
  3. 域 MX 核验(沙箱 SMTP 用户级不可验——「有 MX ≠ 邮箱存在」,一律标 guessed 不进群发)
  4. 结果落 batch/KP猎捕_A_R64_第1波.json + profile 追 R64 节

纪律(沿用库规):
  - 猜测邮箱 tier = leads-only-guessed-mx-ok:**不进群发**,仅供用户手动/小批量试探
  - SMTP 不可验如实标注;查不出写待定
  - 乌克兰守界户不参与
"""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path('/home/user/mikrotik-info')

def ascii_fold(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()

def candidates(first, last, domain):
    f, l = ascii_fold(first), ascii_fold(last)
    if not f and not l:
        return {}
    if not f:
        return {'last@': f'{l}@{domain}'}
    if not l:
        return {'first@': f'{f}@{domain}'}
    return {
        'first@': f'{f}@{domain}',
        'first.last@': f'{f}.{l}@{domain}',
        'f.last@': f'{f[0]}.{l}@{domain}',
        'firstlast@': f'{f}{l}@{domain}',
        'flast@': f'{f[0]}{l}@{domain}',
        'last@': f'{l}@{domain}',
    }

# 2026-10-07 web_search 战果(来源见引用 URL)
KP = [
  dict(code='A-570', domain='ronitek.co.il',
       persons=[('Tomer', 'Shitrit', 'Ronitek Distribution Ltd 任职(疑业主/负责人)',
                 'https://www.linkedin.com/in/tomer-shitrit-b317593/')],
       note='公司注册号 ח.פ 516918844,2024-01-10 注册,84 Derech Ben Tzvi Tel Aviv;KYC 名录口径'),
  dict(code='A-571', domain='triple-core.com', persons=[], note='KP 人名未取得→待定'),
  dict(code='A-572', domain='art2soft.com',
       persons=[('Thomas', 'Thoma', 'Managing Director(2006 至今)',
                 'https://rocketreach.co/thomas-thoma-email_51793668')],
       alt_domains=['cy-wireless.com'],
       note='MikroTik 官方 reseller 名录曾列 thomas.thoma@art2soft.com'),
  dict(code='A-573', domain='etree.de',
       persons=[('Grazian', 'Twonski', 'Founder & CEO(2010 创立)',
                 'https://etree.de/en/Services/Informations/About-Us/'),
                ('Sebastian', 'Rinne', 'CEO/Geschäftsführer(公开邮箱 sr@konsultec.de,集团关联)',
                 'https://www.etree.de/en/Kontakt/'),
                ('', 'Wysoczanski', 'Sales/Purchase Manager +49 221 292 417 62',
                 'https://www.lieferanten.de/lieferant-21930-etree-gmbh.html')],
       note='联合创始人 Peter Voigt(Crunchbase)'),
  dict(code='A-574', domain='dnet-distribution.com',
       persons=[('Eugenia', 'Zito', 'Presidente(Nim Wave S.r.l. 母体)',
                 'https://contactout.com/company/Nim-Wave-Srl-91231'),
                ('Alessandro', 'Monti', 'Specialista di prodotto(产品对接口)',
                 'https://contactout.com/company/Nim-Wave-Srl-91231')],
       alt_domains=['nimwave.com'],
       note='Dnet=Nim Wave S.r.l. 品牌,P.IVA 06095990963;Viviana Vaghi 行政'),
  dict(code='A-577', domain='tehnox.si',
       persons=[('Peter', 'Jezernik', 'Director & 50% 持股业主',
                 'https://www.companywall.si/podjetje/pec-sistemi-doo/MM1dLgOD')],
       alt_domains=['pec-sistemi.si'],
       note='Elizabeta Jezernik 另一 50%;8 员工,营收 €4.36M,出口 BiH/克罗地亚 24%'),
  dict(code='A-578', domain='takopi.ge', persons=[], note='KP 人名未取得→待定'),
  dict(code='A-579', domain='edox.com',
       persons=[('Lionel', 'Weckerle', '采购部负责人(responsable service achats,3 人团队)',
                 'https://www.linkedin.com/in/lionel-weckerle/'),
                ('David', 'Hugueny', '商务(3 年+在职,MikroTik 技术培训常客)',
                 'https://www.linkedin.com/in/david-hugueny/')],
       note='采购 KP=Lionel Weckerle 最对口'),
  dict(code='A-580', domain='poniatowski.pl',
       persons=[('Piotr', 'Poniatowski', '本人=业主(R57 已落 piotr@poniatowski.pl)',
                 'https://mbum.pl/index.php')],
       known_email='piotr@poniatowski.pl', note='邮箱已有,本轮只复核 MX'),
  dict(code='A-582', domain='vodanetsystems.com',
       persons=[('Albert', 'Krakus', 'Founder(2013,计算机工程师)',
                 'https://www.vodanetsystems.com/about-us'),
                ('Alper', 'Karakus', 'President',
                 'https://www.zoominfo.com/c/vodanet-systems-llc/370619677'),
                ('Ihsan', 'Aslan', 'Purchase Manager(采购经理,领英员工栏)',
                 'https://www.linkedin.com/company/vodanet-systems')],
       note='采购 KP=İhsan Aslan 最对口;Moonachie/Pompton Plains NJ'),
  dict(code='A-583', domain='allness.net',
       persons=[('Barry', 'Higgins', 'Owner(UK 独立 MikroTik Trainer since 2016)',
                 'http://allness.it/?page=about')],
       alt_domains=['allness.it'],
       note='Kidderminster;WISP 运营 2009 起'),
  dict(code='A-584', domain='mikrotiktraining.co.uk',
       persons=[('Ron', 'Touw', '本人=业主(UK 首位 MikroTik Trainer 2009)',
                 'https://mikrotiktraining.co.uk/')],
       note='2009 旧帖记 ron.touw@gmail.com(过旧,标历史源不采信);Guernsey 关联 Nest Wireless'),
]

def mx_of(domain):
    try:
        import dns.resolver
        ans = dns.resolver.resolve(domain, 'MX')
        return sorted(str(r.exchange).rstrip('.') for r in ans)
    except Exception as e:
        return f'FAIL:{type(e).__name__}'

def main():
    out = {'date': '2026-10-07', 'round': 'R64',
           'scope': 'A 类 KP 猎捕第 1 波 = R63 新升 12 户;web_search 找人 + 排列组合 + MX 域核验',
           'discipline': 'SMTP 用户级沙箱不可验;guessed 邮箱不进群发;查不出写待定',
           'records': []}
    for rec in KP:
        entry = {'code': rec['code'], 'domain': rec['domain'], 'note': rec['note'],
                 'persons': [], 'mx': {}}
        domains = [rec['domain']] + rec.get('alt_domains', [])
        for d in domains:
            entry['mx'][d] = mx_of(d)
        if rec.get('known_email'):
            entry['persons'].append({'name': f"{rec['persons'][0][0]} {rec['persons'][0][1]}",
                                     'role': rec['persons'][0][2], 'source': rec['persons'][0][3],
                                     'email': rec['known_email'], 'email_state': 'official-existing(R57 已落)'})
        for (first, last, role, src) in rec['persons']:
            p = {'name': f'{first} {last}'.strip(), 'role': role, 'source': src}
            if not rec.get('known_email'):
                cands = {}
                for d in domains:
                    if isinstance(entry['mx'][d], list):  # 域 MX 存活才生成
                        for pat, em in candidates(first, last, d).items():
                            cands[f'{pat}({d})'] = em
                p['email_candidates'] = cands
                p['email_state'] = 'guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发)'
            entry['persons'].append(p)
        out['records'].append(entry)
    dst = ROOT / 'batch' / 'KP猎捕_A_R64_第1波.json'
    dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    print('落盘', dst, f"{len(out['records'])} 户")
    for e in out['records']:
        np = len(e['persons'])
        nc = sum(len(p.get('email_candidates', {})) for p in e['persons'])
        print(e['code'], f'KP {np} 人,候选邮箱 {nc} 个,MX {list(e["mx"].keys())}')

if __name__ == '__main__':
    main()
