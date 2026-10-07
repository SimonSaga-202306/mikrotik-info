# -*- coding: utf-8 -*-
"""R65 B 类深挖第 17 批:比利时/爱沙尼亚/立陶宛/爱尔兰。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 17 批精修 = R57 转写 + 本轮登记新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-225',
    head='Foxconcept BV(BE 0872.787.192,Rue Mathias 9, 5140 Sombreffe, Belgium;2005-03-24 创;'
         '谱型=ICT 服务/咨询/软件(Nacebel 62200),komalyse 2076e（毛利 €471,759);foxconcept.be 2001-12 幔幔 24 年域',
    kpn='—(BV 实体名行政登记 trendstop 未披露；R65 谱位+财务数据足档）',
    facts=[{'dim': 'R65 登记/财务', 'text': 'Foxconcept BE 0872.787.192 · Sombreffe Rue Mathias 9 · ICT 服务 62200 · 毛利 €471.7K',
            'quote': 'Foxconcept BV Besloten vennootschap … BE 0872.787.192 - Rue Mathias 9, 5140 SOMBREFFE … brutomarge van 471.759 euro is Foxconcept 2076e in de sector ICT',
            'url': 'https://trendstop.knack.be/nl/detail/872787192/foxconcept.aspx'}],
    fihadd='比利时 ICT 咨询实体 2005;Sombreffe 谱位')

put('B-285',
    head='ELKO Eesti OÜ(Registrikood 10674202, Pärnu mnt 141, Kesklinna linnaosa, Tallinn 11314;2000-05-30 创（26 年，ELKO Grupa AS 全子，股 2 556 EUR);'
         '**Adam Leemet = juhatuse liige(董事会成员，1969-11 生，2013-04-22 任）**;**Martins Pavlovskis = juhatuse liige(2026-03-11 新任！46 岁）**;'
         '谱型=波罗的海 IT 批发 ELKO 集团大谱；elko@elko.ee / +372 6509444',
    kpn='Adam Leemet = juhatuse liige(2013-至今 13 年）;Martins Pavlovskis = juhatuse liige(2026-03-11 新任）',
    kp=[{'name': 'Adam Leemet', 'role': 'Juhatuse liige', 'contact': 'elko@elko.ee / +372 6509444', 'status': 'aripaev/infopank/e-krediidiinfo 三源', 'source': 'https://www.infopank.ee/ettevote/31722/elko-eesti-ou'},
        {'name': 'Martins Pavlovskis', 'role': 'Juhatuse liige(2026-03-11 新任）', 'contact': '同上', 'status': '同源', 'source': '同上'}],
    facts=[{'dim': 'R65 登记/新任', 'text': 'ELKO Eesti OÜ 10674202 · Tallinn 2000 创 · ELKO Grupa 全子 · Adam Leemet 13 年 juhatus + Martins Pavlovskis 2026-03-11 新板装位',
            'quote': 'Adam Leemet (56) Juhatus … Martins Pavlovskis (46) Juhatus … Seos alates 11.03.2026 … ELKO Grupa AS',
            'url': 'https://radar.aripaev.ee/ettevote/31722/elko-eesti-ou'}],
    fihadd='波罗的海 ELKO 集团大谱；Pavlovskis 2026-03 新板装最新引口')

put('B-311',
    head='UAB ELKO Lietuva(Įmonės kodas 110604815, Algirdo g. 32A, Kaunas LT-50153,Kaunas,Europos pr. 32 从行;1994-03-21 创（32 年 ELKO 大谱老牌）;'
         '**Miglė Rudminė = Vadovas(CEO)**;PVM LT106048113;14 员工；+370 37 302450 / info@elko.lt;'
         '谱型=计算机硬件/软件大批发（Kompiuterinė įranga - didmeninė prekyba)',
    kpn='Miglė Rudminė = Vadovas（首席）',
    kp=[{'name': 'Miglė Rudminė', 'role': 'Vadovas(CEO)', 'contact': 'info@elko.lt / +370 37 302450', 'status': 'imoniubaze.lt 实名', 'source': 'https://imoniubaze.lt/uab-elko-lietuva/'}],
    facts=[{'dim': 'R65 登记/实名', 'text': 'UAB ELKO Lietuva 110604815 · Kaunas Algirdo 32A · 1994-03 创 32 年 · Miglė Rudminė vadovas · 14 员工',
            'quote': 'Vadovas: Miglė Rudminė … Įmonės kodas: 110604815 … Adresas: Algirdo g. 32A, Kaunas … El. paštas: info@elko.lt … Tel.: (+370 37) 302450',
            'url': 'https://imoniubaze.lt/uab-elko-lietuva/'}],
    fihadd='ELKO 立陶宛 32 年实体；Rudminė 实名首')

put('B-283',
    head='gCnTech Limited / gCn Tech(1a Dwarf Oaks, Church Road, Ballybrack Village, Co Dublin A96 D653;'
         '**Greg = 业主（greg@gcntech.ie 官自曝；087 7682964)**;Simon 交付/销售（simon@gcntech.ie,01 2821306,087 4887471);'
         '谱型=爱尔兰 trade-only 电脑 IT 分销；openlogic.ie 同址门脸；只卖 resellers，亦收 PayPal',
    kpn='Greg = 业主（greg@gcntech.ie);Simon 交付/销售',
    kp=[{'name': 'Greg', 'role': 'Owner（业主邮箱+电话自曝）', 'contact': 'greg@gcntech.ie / 087 7682964 / 01 2820458', 'status': 'gcntech.ie/contact 自曝', 'source': 'https://gcntech.ie/contact/'},
        {'name': 'Simon', 'role': 'Delivery/Sales（交付销售）', 'contact': 'simon@gcntech.ie / 087 4887471', 'status': '同上', 'source': '同上'}],
    facts=[{'dim': 'R65 谱/联络', 'text': 'gCnTech · Ballybrack Dublin · trade-only IT 分销 · greg@/simon@ 自曝信息双谱口',
            'quote': '1a, Dwarf Oaks Church Road Ballybrack Village Co Dublin A96 D653 … Email: greg@gcntech.ie … Greg 087 7682964 … Simon (Delivery/Sales Queries) 01 2821306 simon@gcntech.ie … We are a Trade only supplier',
            'url': 'https://gcntech.ie/contact/'}],
    fihadd='都柏林 trade-only 实体；Greg+simon 邮箱自曝')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 17 批（比利时/爱沙尼亚/立陶宛/爱尔兰）',
       'scope': 'B-225 Foxconcept / B-285 ELKO Eesti / B-311 ELKO Lietuva / B-283 gCnTech',
       'records': [by[c] for c in ('B-225', 'B-285', 'B-311', 'B-283')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第17批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 17 批 4 户落盘')
