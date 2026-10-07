# -*- coding: utf-8 -*-
"""R65 B 类深挖第 21 批:波黑/斯洛文尼亚/捷克/马耳他 4 户。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 21 批精修 = R57 转写 + 本轮登记新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-277',
    head='Wirac.Net d.o.o.(Gračanica, 75320 BiH;2006 创,20 年老品牌；AS59847 实体；'
         '**Admir Kamarić = Generalni direktor（总经理，隐私政策页自曝）**;'
         '**Samir Zildžić = ovlašteni MikroTik trener(官方 MikroTik 认证教练，MTCNA/MTCRE/MTCSE/MTCTCE 课程讲师，CSV 谱主位）**;'
         '谱型=BiH ISP+网络工程学校+互联客户 20 年',
    kpn='Admir Kamarić = Generalni direktor;Samir Zildžić = ovlašteni MikroTik trener（双向谱）',
    kp=[{'name': 'Admir Kamarić', 'role': 'Generalni direktor（总经理）', 'contact': 'info@wirac.ba', 'status': 'wirac.net 隐私政策页自曝', 'source': 'https://wirac.net/privacy-policy/'},
        {'name': 'Samir Zildžić', 'role': 'ovlašteni MikroTik trener（官方认证教练）', 'contact': '经 wirac.ba / info@wirac.ba', 'status': 'wirac.ba 官网 trainer 自曝', 'source': 'https://wirac.ba/'}],
    facts=[{'dim': 'R65 实名/谱位', 'text': 'Wirac.Net doo Gračanica BiH 2006 20 年品牌 · Kamarić 总+ Zildžić 认证教练 · AS59847 实体 · MTCNA/MTCRE/MTCSE/MTCTCE 谱训',
            'quote': 'Za Wirac.Net d.o.o. Admir Kamarić, Generalni direktor … trainer Samir Zildžić — ovlašteni MikroTik trener … course MTCNA i MTCRE, MTCSE, MTCTCE — MikroTik certifikacije … 20 godina povezani s Vama Od 2006.',
            'url': 'https://wirac.ba/'}],
    fihadd='BiH 20 年 ISP+教练谱；双谱自用：Kamarić 总+ Zildžić 证教')

put('B-219',
    head='PC H.AND d.o.o.(Brezovce 10, 1236 Trzin, Slovenia;MŠ 5304989000, DŠ SI 52070859;1990-01-22 创（36 年！);'
         '**BOLTA MARKO = direktor（董事，marko.bolta@pchand.si）**;HABJAN ANDREJ = prokurist（授权代理，andrej@pchand.si）;'
         'PCH SKUPINA 100% 股权；Temeljni kapital €63,483;015300800 信息号；IBAN SI56 门脸；'
         '谱型=34+ 年 PC/办公设备/AV 全球大厂商分销（SKD G46.510 IT 批发）',
    kpn='BOLTA MARKO = direktor;HABJAN ANDREJ = prokurist',
    kp=[{'name': 'BOLTA MARKO', 'role': 'Direktor（董事，40+ 年行当）', 'contact': 'marko.bolta@pchand.si / 01 530 0800', 'status': 'companywall.si/自曝(vodja-prodaje hiring 直接挂邮箱）', 'source': 'https://www.companywall.si/podjetje/pc-hand-doo/MM1dCsnY'},
        {'name': 'HABJAN ANDREJ', 'role': 'Prokurist（授权代理）', 'contact': 'andrej@pchand.si', 'status': 'companywall.si 实名', 'source': '同上'}],
    facts=[{'dim': 'R65 登记/实名', 'text': 'PC H.AND Trzin 1990 创 36 年 IT 分销；Bolta 董事+ Habjan 授权代理 两名谱口；PCH SKUPINA 100% 股权',
            'quote': 'Trenutni direktor podjetja je BOLTA MARKO - direktor … Prokurist: HABJAN ANDREJ … Lastniki: PCH SKUPINA, NALOŽBENA DEJAVNOST, D.O.O.(100,00%) … marko.bolta@pchand.si',
            'url': 'https://www.companywall.si/podjetje/pc-hand-doo/MM1dCsnY'}],
    fihadd='斯洛文尼亚 34+ 年老谱；Bolto+Habjan 两名谱位')

put('B-194',
    head='AxiLogi s.r.o.(IČO 10964703, Daimlerova 1161/6, 301 00 Plzeň-Skvrňany, Czech Republic;2021-06-23 创；'
         '**法人体制谱：Kolibřík klub invest a.s. + DC Europe system a.s. 双 Jednatel 法人在位（2021-06-23 起至今）——谱为法人家长轴**;'
         'sales@axilogi.cz + servis@axilogi.cz +420 371 420 573',
    kpn='Kolibřík klub invest a.s. + DC Europe system a.s. 双法人 Jednatel(sales/servis 函数口已足）',
    facts=[{'dim': 'R65 登记/联动', 'text': 'AxiLogi s.r.o. IČO 10964703 · Plzeň Daimlerova 1161/6 · 双法人 Jednatel（法人家长轴）· sales/servis 函数口',
            'quote': 'Jednatel: Kolibřík klub invest a. s. Den vzniku funkce: 23. 6. 2021 … Jednatel: DC Europe system a.s. Den vzniku funkce: 23. 6. 2021 … AxiLogi s.r.o. IČO: 10964703 DIČ: CZ10964703 Daimlerova 1161/6, 301 00 Plzeň',
            'url': 'https://axilogi.com/kontakty_d1502.html'}],
    fihadd='法人家长轴型实体（DC Europe 集团属）;plzen 谱位')

put('B-489',
    head='WST Systems Ltd.(Birkirkara, Malta(core 大街）;'
         '**Neville Zahra = Owner（业主）**;Richard Irabor IT Technician(Mellieha)+Giuseppe di Falco Support Technician IT(意大利谱）+Claudio Stagno Salesperson(2025 新聘）;4 员工',
    kpn='Neville Zahra = Owner;Claudio Stagno = Salesperson(2025 新任）',
    kp=[{'name': 'Neville Zahra', 'role': 'Owner（业主）', 'contact': '经 wstsystems.com', 'status': 'rocketreach 自曝', 'source': 'https://rocketreach.co/wst-systems-ltd-management_b71953b5c480316d'}],
    facts=[{'dim': 'R65 实名', 'text': 'WST Systems Malta · Neville Zahra Owner · 4 员工（Richard Irabor + Giuseppe di Falco + Claudio Stagno 2025 sales 新聘）',
            'quote': 'the WST Systems Ltd. management team includes Neville Zahra (Owner), Richard Irabor (IT Technician), and Giuseppe di Falco (Support Technician IT) … Claudio Stagno Salesperson at WST Systems Ltd. 2025 - now',
            'url': 'https://rocketreach.co/wst-systems-ltd-management_b71953b5c480316d'}],
    fihadd='马耳他实体；Neville Zahra 业主谱')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 21 批（波黑/斯洛文尼亚/捷克/马耳他）',
       'scope': 'B-277 Wirac / B-219 PC H.AND / B-194 AxiLogi / B-489 WST',
       'records': [by[c] for c in ('B-277', 'B-219', 'B-194', 'B-489')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第21批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 21 批 4 户落盘')
