# -*- coding: utf-8 -*-
"""R64 B 类 KP 猎捕第 1 批落盘+注入。"""
import json, glob, sys
sys.path.insert(0, 'scripts')
from R64_KP猎捕 import candidates, mx_of

B1 = [
 dict(code='B-200', domain='oemautomatic.cz',
      persons=[('Jan', 'Drlík', 'Ředitel společnosti(公司董事)+420 241 484 940', 'https://www.info-cechy.cz/eig-oem-automatic/index.html'),
               ('Jakub', 'Hanousek', 'Product Area Manager Machine/Safety/Electronics/Railway(产品口对口)', 'https://www.oemautomatic.cz/kontakty/nas-tym')],
      note='Zdiby Pražská 239,1991 创立;Ilona Kulhánková 供应商订单管理;Adam Stoklasa 商技代表'),
 dict(code='B-295', persons=[],
      note='OEM Automatic AB(瑞典母公司,与 B-200 同集团):集团 KP 借 B-200 Jan Drlík 线;oemautomatic.se MX(outlook)存活'),
 dict(code='B-340', domain='controllerservice.com',
      persons=[('Mark', "O'Day", 'President(2005 至今,三代家族;祖父 1926 创立;Brown AB+Chicago MBA)', 'https://www.dnb.com/business-directory/company-profiles.controller_service__sales_co_inc.65ac94bbcbb878dab554ba6fd7598a67.html'),
               ('Scott', "O'Day", 'VP Sales and Marketing(兄弟共管)', 'https://rocketreach.co/controller-service-sales-inc-management_b5fee96bf60669ae'),
               ('Jim', 'Long', 'Corporate Controller', '同 RocketReach 源')],
      note='Avon MA,38 员工;Michael Sandonato 销售市场总监'),
 dict(code='B-421', domain='pymatek.com',
      persons=[('Ybet', 'Sánchez Vargas de Pattison', 'Director(2014 至今,唯一登记董事)', 'https://www.companiesintheuk.co.uk/ltd/pymatek-automation'),
               ('Martin', 'Pattison', 'Sales Manager', 'https://uk.globaldatabase.com/company/pymatek-automation-ltd'),
               ('Franco', 'Sanchez', 'Jefe De Ventas', '同 GlobalDatabase 源')],
      note='Rugeley Staffordshire,3 人,engineering activities;主域 pymatek.com(非 .co.uk) MX outlook 存活;Kimberly Pinillos Gerente General'),
 dict(code='B-005', domain='nextron.dk',
      persons=[('Håkon', 'Børstad Gutierrez', 'Direktør(丹麦分部主任)', 'https://www.proff.dk/firma/nextron-aps/frederiksberg-c/elektronik-og-telekommunikationsudstyr/0MT1URI10MY'),
               ('Carl Henrik', 'Sibbern', 'Bestyrelsesformand(董事长)', '同源')],
      note='CVR 38306979,Fuglevangsvej 13 Frederiksberg C,7 员工 DKK 10M 毛利;挪威母公司 Nextron AS 更大体'),
 dict(code='B-106', domain='mstronics.com',
      persons=[('Panicos', 'Michael', 'Managing Director', 'https://rocketreach.co/ms-electronics-ltd-profile_b4479492facba323'),
               ('Michalis', 'Pavlou', 'Sales Director', '同源')],
      note='Limassol 1996 年,11 人;Pieris Michael(Product Manager Networking&IT 2016 至今)即库内 pieris@mstronics.com 名录联系人,无需再猜'),
 dict(code='B-307', domain='accdistribution.eu',
      persons=[('Žymantas', 'Baušys', 'Direktorius(2017 至今,前财务总监)', 'https://okredo.com/lt-lt/imone/uab-acc-distribution-135150085'),
               ('Regimantas', 'Buožius', '董事长(1998 创始人,现战略面)', 'https://www.vz.lt/vadyba/is-tarnybos-i/2017/06/02/acc-distribution-turi-nauja-direktoriu')],
      note='ACME Grupė 母;300+ 品牌 28 年'),
 dict(code='B-320', domain='telesystem.ro',
      persons=[('David', 'Marian', 'Administrator(管理方公示名姓)', 'https://www.protectiesipaza.ro/sisteme-de-alarma/telesystem-s-r-l-sisteme-de-alarma/')],
      note='Bacău CUI RO22460883,0728 105 124 移动;office@telesystem.ro 已有;安防主 MikroTik 副牌'),
 dict(code='B-352', domain='ieiworld.com',
      persons=[('Richard', 'Kao', 'Operation Director(Pomona USA)', 'https://www.linkedin.com/in/richard-kao-233a5368/'),
               ('Wendy', 'Wang', 'Office Manager(2005 至今)', 'https://www.linkedin.com/in/wendy-wang-83456826/')],
      note='台湾 IEI Integration 集团美子:Teddy Kuo 创始人/Jordan Jiang GM;集团墙注意,R53 判定已 hold'),
 dict(code='B-436', persons=[],
      note='Qtopia 双创始董事:Dennis van Elk + Jan Geert Hek,Kolstee 5 Zelhem,088-7110500,info@qtopia.nl(入口已有);安全/云架构顾问 2013 创立'),
 dict(code='B-512', domain='mtktechnologies.com',
      persons=[('Kailash', 'Chakravarti', 'President', 'https://www.zoominfo.com/p/Kailash-Chakravarti/1721726706')],
      note='Champaign IL,1996 年 51-200 人;注意 MX 域以 mtk-tech.com 现网为准,k@ 模式=mtktechnologies.com 双域候选'),
 dict(code='B-433', persons=[], note='Fokko van den Bosch / it-support.nl:搜索无有效命中 → 待定(下轮换 Apollo)'),
 dict(code='B-134', persons=[], note='Spiros Potsikas / Tele-Net(希腊):搜索无果 → 待定(希腊 Xpatit/LinkShop 分销圈另起线再查)'),
 dict(code='B-452', persons=[], note='Camacho / Engenheiros(葡萄牙 engenheiros.pt):搜索无果 → 待定'),
]


def main():
    out = {'date': '2026-10-07', 'round': 'R64',
           'scope': 'B 类 KP 猎捕第 1 批:4 无邮箱户 + 10 大户;web_search 公开源+排列组合+MX',
           'records': []}
    for rec in B1:
        entry = {'code': rec['code'], 'note': rec['note'], 'persons': [], 'mx': {}}
        domains = [rec['domain']] if rec.get('domain') else []
        for d in domains:
            entry['mx'][d] = mx_of(d)
        for (first, last, role, src) in rec['persons']:
            p = {'name': f'{first} {last}', 'role': role, 'source': src}
            cands = {}
            for d in domains:
                if isinstance(entry['mx'][d], list):
                    for pat, em in candidates(first, last, d).items():
                        cands[f'{pat}({d})'] = em
            if cands:
                p['email_candidates'] = cands
            p['email_state'] = 'guessed-leads-only(域 MX 存活;SMTP 未验;不进群发)' if cands else '—'
            entry['persons'].append(p)
        out['records'].append(entry)

    json.dump(out, open('batch/KP猎捕_B_R64_第1批.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('B 第1批落盘', len(out['records']), '户')

    for e in out['records']:
        fns = glob.glob(f"profile/B/{e['code']}-*.md")
        if not fns:
            print('档缺:', e['code'])
            continue
        fn = fns[0]
        t = open(fn, encoding='utf-8').read()
        L = ['', '## 2026-10-07 R64 KP 猎捕（B 类第 1 批）', '',
             f"**结论**:{e['note']}"]
        if e.get('mx'):
            L.append(f"**域 MX**:{json.dumps(e['mx'], ensure_ascii=False)}")
        for p in e['persons']:
            L.append(f"- **{p['name']}** — {p['role']}（源:{p['source']}）")
            for pat, em in list(p.get('email_candidates', {}).items())[:6]:
                L.append(f"  - `{em}`({pat})")
        t = t.rstrip() + '\n' + '\n'.join(L) + '\n'
        open(fn, 'w', encoding='utf-8').write(t)
        print('注入:', fn.split('/')[-1])


if __name__ == '__main__':
    main()
