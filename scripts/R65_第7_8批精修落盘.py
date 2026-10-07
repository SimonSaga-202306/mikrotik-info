# -*- coding: utf-8 -*-
"""R65 B 类深挖第 7/8 批:以色列/摩尔多瓦/德国/ALLNET 系/意大利 7 户。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, wave, head=None, kpn=None, kp=None, facts=(), fihadd='', Unk=None):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 %s 批精修 = R57 转写 + 本轮登记/官网新挖)' % wave
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    if Unk: r['unknowns56'] = Unk + r['unknowns56']
    return r

# 第 7 批
put('B-039', 7,
    head='Voicenter LTD(以色列云端电信/VoIP CPaaS 平台;'
         '**Nitsan Gutman = מייסד ומנכ"ל(创始人兼 CEO)**——"חלוץ בתחום התקשורת והטלפוניה בענן בישראל"(以色列云通讯先驱,官网博客自曝);'
         '另 Golan Ashtan 早前 CEO 层(MBA,二代以色列电信业谱:Netvision/012/Partner/HOT 多年高管);'
         'MikroTik 谱挂其电信商平台供应链线',
    kpn='Nitsan Gutman = 创始人&CEO(官网自曝);Golan Ashtan = 早前 CEO(2023 文)',
    kp=[{'name': 'Nitsan Gutman', 'role': 'Founder & CEO', 'contact': '经 voicenter.co.il 总线', 'status': '官网博客自曝', 'source': 'https://voicenter.co.il/%D7%91%D7%9C%D7%95%D7%92/mcp'},
        {'name': 'Golan Ashtan', 'role': 'CEO(2023 早前口径)', 'contact': '同上', 'status': 'ceopro.co.il 专访自曝', 'source': 'https://www.ceopro.co.il/%D7%92%D7%95%D9%84%D7%9F-%D7%90%D7%A9%D7%98%D7%9F-%D7%9E%D7%A0%D7%9B%D7%9C-voicenter/'}],
    facts=[{'dim': 'R65 实名', 'text': 'Nitsan Gutman founder&CEO(以色列云通讯/电话先驱官方口径)',
            'quote': 'ניצן גוטמן מייסד ומנכ״ל Voicenter, חלוץ בתחום התקשורת והטלפוניה בענן בישראל',
            'url': 'https://voicenter.co.il/%D7%91%D7%9C%D7%95%D7%92/mcp'}],
    fihadd='以色列云电信平台;Gutman 创始归位')

put('B-210', 7,
    head='Comitek SRL(dba DOXYTERRA Computer Center;bd. Dacia 27, MD2060 Chișinău;1995 创=31 年老店;'
         '注册号 1002600055526,VAT 0200872,股本 5,400 MDL;'
         '**Dan Potârniche = Director(业主)**;Alexandru Sochircă = 营销总监;Sergiu Corbu = 经理;'
         'Eugeniu Iacub 分销部关联履历;doxyterra.md 平台门脸',
    kpn='Dan Potârniche = Director(业主,Kompass 双源);Alexandru Sochircă 销市总监;Sergiu Corbu 经理',
    kp=[{'name': 'Dan Potârniche', 'role': 'Director/Principal Executive(业主)', 'contact': '经 doxyterra.md 总线', 'status': 'kompass EN/RO 双源实名', 'source': 'https://xk.kompass.com/c/doxyterra-computer-center/md003157/'},
        {'name': 'Alexandru Sochircă', 'role': 'Marketing Director', 'contact': '同上', 'status': '同源', 'source': 'https://md.kompass.com/c/comitek-srl/md003157/'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'Comitek SRL dba DOXYTERRA · 1995 创 · Reg 1002600055526 · Dan Potârniche Director+Alexandru Sochircă Marketing',
            'quote': 'Mr Dan Potirniche Principal Executive/Proprietor (Director) … Year established: 1995 … bd. Dacia, 27',
            'url': 'https://xk.kompass.com/c/doxyterra-computer-center/md003157/'}],
    fihadd='31 年老店 Doxyterra;Potârniche 业主导演')

put('B-153', 7,
    head='hsc solutions e.K.(Am Hang 11, 09337 Hohenstein-Ernstthal OT Wüstenbrand + Solaristurm Neefestraße 88, 09116 Chemnitz;'
         'HRA 9918 Chemnitz 商业登记;UID DE247626561;'
         '**Dipl.-Inf. (FH) Tom Zschockelt = Inhaber(业主,自营个体)**;Rebekka Shepherd 同在 Impressum/Samuel Zschockelt 关联;'
         '「Hardware+Software+Consulting」型服务,ERP/Warenwirtschaft 定制开发 +Rual 硬件+Chemnitz 技术圈;11-50 员工 Xing 口径',
    kpn='Tom Zschockelt = Inhaber(业主,自营个体;Impressum/Xing 双源);Rebekka Shepherd 关联签名人',
    kp=[{'name': 'Tom Zschockelt', 'role': 'Inhaber(业主,Dipl.-Inf. FH)', 'contact': 'hsc-solutions.de 联系页', 'status': 'impressum + xing 双源实名', 'source': 'https://hsc-solutions.de/impressum-hsc-solutions/'}],
    facts=[{'dim': 'R65 实名/登记', 'text': 'Tom Zschockelt e.K. 独营;HRA 9918 Chemnitz;Chemnitz Neefestraße 88 实体店',
            'quote': 'Vertreten durch: Dipl.-Inf. (FH) Tom Zschockelt … Handelsregister: HRA 9918 Registergericht: Amtsgericht Chemnitz',
            'url': 'https://hsc-solutions.de/impressum-hsc-solutions/'}],
    fihadd='e.K. 独营商;IT 服务+硬件双轨')

put('B-510', 7,
    head='Janzen Group(Hamburg 出发的德国全国体:KNX 编程+安防+AV/会议室+布线+MikroTik Support;'
         '**官网两页自曝:MikroTik Support 专页=「zertifizierte MikroTik-Partner / Trainer und Consultants」+ 安防 KNX 双向**;'
         'info@janzen-group.com 公开;Janzen Academy 培训子项目在架',
    kpn='—(未自曝业主/KP 实名;守档准由)',
    facts=[{'dim': 'R65 官网自曝', 'text': '德国 Hamburger MikroTik Support+KNX+安防+AV 一体化;认证 MikroTik Partner 口径;Janzen Academy 培训线',
            'quote': 'Die Janzen Group steht Ihnen als kompetenter Partner für MikroTik Support zur Seite. Unsere zertifizierten Trainer und Consultants … info@janzen-group.com',
            'url': 'https://www.janzen-group.com/leistungen/mikrotik-support/'}],
    fihadd='KNX+MikroTik 双线;培训师 Consultant 未名=守档准由待定',)

# 第 8 批
put('B-138', 8,
    head='ALLNET GmbH Computersysteme(Maistr. 2, 82110 Germering(München);**Wolfgang Marcus Bauer = Geschäftsführer & Inhaber(业主,1991 创立)**;'
         'wer-zu-wem:99 员工(德国)+国际;30,000+ SKU,7 语言,DropShipping 型全品批发;ALLNET 集团丹 B-001/法/意 B-154/希 B-115 母体;family business & Werner Bauer habitual)',
    kpn='Wolfgang Marcus Bauer = Geschäftsführer & Inhaber(业主)+49 89 894222-22(wer-zu-wem/Lieferanten/DnB 三源)',
    kp=[{'name': 'Wolfgang Marcus Bauer', 'role': 'Geschäftsführer & Inhaber(董事总经理/业主)', 'contact': '经 +49 89 894222-22 总线', 'status': 'wer-zu-wem + Lieferanten + DnB 三源实名', 'source': 'https://www.wer-zu-wem.de/firma/allnet-computer.html'}],
    facts=[{'dim': 'R65 集团母实名', 'text': 'ALLNET GmbH 1991·Bauer 业主·99 员工·30K SKU DropShip·国际语言 7',
            'quote': 'Gegründet: 1991 … Familienunternehmen Gesellschafter Wolfgang Marcus Bauer … 30.000 Produkte … DropShipping',
            'url': 'https://www.lieferanten.de/lieferant-840-allnet-gmbh-computersysteme.html'}],
    fihadd='德国母体 Bauer 1991 创立;R56 守档谱性维持(同业守档)')

put('B-154', 8,
    head='ALLNET.ITALIA S.P.A.(Via Renato Fucini 2, 40033 Casalecchio di Reno(BO);P.IVA 00884761206;SDI SN4CSRI;'
         '**2024 财报 €87,915,037 营收/€1.76M 净利(fatturatoitalia)**——ALLNET 集团意大利巨站;'
         'amministrazione@allnet-italia.it,051-0547710;Confindustria Emilia 会员;5G/AV/Cloud 谱向',
    kpn='—(S.p.A. amministratore 收费墙;谱与 B-138 Bauer 同家长径,B-115 希腊同谱;集团联动口径)',
    facts=[{'dim': 'R65 财务+地址', 'text': 'ALLNET.ITALIA S.p.A. · P.IVA 00884761206 · 2024 €87.9M 营收 €1.76M 净利 · Casalecchio di Reno BO · Confindustria 会员',
            'quote': 'Allnet.italia Spa: fatturato 87.915.037 €, utile 1.762.069 € (2024). P.IVA 00884761206 … Via Renato Fucini, 2 40033 Casalecchio di Reno',
            'url': 'https://www.fatturatoitalia.it/allnetitalia-spa-00884761206'},
            {'dim': 'R65 渠道', 'text': 'amministrazione@allnet-italia.it + 051 0547710 公开;Confindustria Emilia 会通员与 Smartwords 5G/AV/Cloud 谱',
             'quote': 'amministrazione@allnet-italia.it … 051 0547710 … 5G, Audio-video solutions, Cloud',
             'url': 'https://www.confindustriaemilia.it/flex/FixedPages/Common/associati.php/L/EN/id/fd02d3c0-c6aa-e811-814b-5065f38b9571'}],
    fihadd='€88M 意大利大站;同业守档谱维持')

put('B-168', 8,
    head='Neostar S.r.l.(Brescia/Bergamo 双 Cash & Carry 门店;谱=Asustor/FSP/Gigabyte/Legrand/Magnoni/MikroTik/NZXT/Thecus/TP-Link/Transcend/Ubiquiti 在架;'
         '**2017 MUM Europe exhibitor(MikroTik 官方名录)**=老谱位确认',
    kpn='—(S.r.l. 董事 registre des entreprises Brescia tribunale 查询方向)',
    facts=[{'dim': 'R65 谱位', 'text': 'Neostar S.r.l. Brescia+ Bergamo 双 Cash & Carry;多品牌谱 MikroTik 在架;2017 MUM Europe exhibitor 官方录',
            'quote':'Neostar S.r.l. - Distributore Asustor, FSP, Gigabyte, Legrand, Magnoni, Mikrotik, NZXT, Thecus, TP-Link, Transcend, Ubiquiti - Cash & carry a Brescia e Bergamo … Neostar (Italy) [2017 MUM EU exhibitor]',
            'url': 'https://mum.mikrotik.com/2017/EU/exhibitors'}],
    fihadd='Brescia Cash&Carry 老谱;2017 MUM 出展座实')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 7/8 批(以色列/摩尔多瓦/德国/ALLNET/意大利)',
       'scope': 'B-039 Voicenter / B-210 Comitek / B-153 hsc / B-510 Janzen Group / B-138 ALLNET / B-154 ALLNET.Italia / B-168 Neostar',
       'records': [by[c] for c in ('B-039', 'B-210', 'B-153', 'B-510', 'B-138', 'B-154', 'B-168')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第7批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 7/8 批 7 户落盘')
