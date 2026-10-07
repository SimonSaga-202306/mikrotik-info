# -*- coding: utf-8 -*-
"""R65 B 类深挖第 22 批:捷克 2+芬兰 1+斯洛伐克 1+格鲁吉亚 1+保加利亚 1。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 22 批精修 = R57 转写 + 本轮登记新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-201',
    head='PCV Computers, s.r.o.(Za Otýlií 2874/6, 370 01 České Budějovice（捷克布杰约维采）;+420 380 420 700;'
         '谱型=电商+实体店 PC/IT 整机配件谱（Heureka 认证 2017 起）——次日达老客谱',
    kpn='—(s.r.o. jednatel OR České Budějovice 收费墙；R65 谱位+地址件已足）',
    facts=[{'dim': 'R65 谱/地址', 'text': 'PCV Computers · Č. Budějovice Za Otýlií 2874/6 · +420 380 420 700 · pcvcomp.cz 电商实体 + Heureka 认证',
            'quote': 'PCV Computers, s.r.o. Za Otýlií 2874/6 České Budějovice, 37001 Tel.: +420 380 420 700 Web: www.pcvcomp.cz',
            'url': 'https://obchody.heureka.cz/pcvcomp-cz/recenze/'}],
    fihadd='České Budějovice 电商实体谱位')

put('B-520',
    head='TECON CZ s.r.o.(Chotyně,Wassermannova 1043/7 布拉格分社;IČ 25447424;'
         '**Ing. Pavel Hlavizna = jednatel(zivefirmy 实名）**;482 723 373/603 563 521,info@teconcz.cz;teconcz.cz',
    kpn='Ing. Pavel Hlavizna = jednatel(TECON CZ)',
    kp=[{'name': 'Ing. Pavel Hlavizna', 'role': 'Jednatel（董事）', 'contact': 'info@teconcz.cz / 482 723 373', 'status': 'zivefirmy.cz 实名', 'source': 'https://www.zivefirmy.cz/tecon-cz_f1147224'}],
    facts=[{'dim': 'R65 实体映射', 'text': 'B-520 TECON = TECON CZ s.r.o. Chotyně（次项：TECON s.r.o. Ústí nad Labem IČ 60277157 Ing. Josef Kinovič / TECON spol. Hostinné IČ 60932091 同名他人已排除）',
            'quote': 'Ing. Pavel Hlavizna - jednatel … TECON CZ s.r.o. IČ 25447424 DIČ CZ25447424 … Wassermannova 1043/7, Hlubočepy, Praha',
            'url': 'https://www.zivefirmy.cz/tecon-cz_f1147224'}],
    fihadd='TECON CZ 实体映射主候选；Hlavizna 实名上位')

put('B-398',
    head='LocalNet Finland / Local Loop Oy(Espoo;20+ 年互联运营商——**Leo Koivulehto = toimitusjohtaja & Founder（创始人/CEO)**;'
         '谱型=芬兰全国企业/住宅光纤谱（valokuitu），2025-01 营收近 €2M/2026-01 预算 €3M+；小职业增长潜力口；Mottomme timanttista asiakaspalvelua(「超值减价谱」)',
    kpn='Leo Koivulehto = Founder & Toimitusjohtaja',
    kp=[{'name': 'Leo Koivulehto', 'role': 'Toimitusjohtaja & Founder', 'contact': '0400 555 011 / linkedin.com/in/leokoivulehto', 'status': 'tyopaikkailmoitukset.fi + LinkedIn + X 三源', 'source': 'https://tyopaikkailmoitukset.fi/tekninen-asiakaspalvelija-localnet-finland-tyopaikat/'}],
    facts=[{'dim': 'R65 谱/实名', 'text': 'LocalNet Finland(Local Loop Oy)Espoo 20+ 年 ISP;Leo Koivulehto Founder CEO;€2M-3M 量级光纤谱',
            'quote': 'LocalNet Finland (virallisesti Local Loop Oy) on jo yli 20 vuotta vanha internetoperaattori … Lisätietoja antaa toimitusjohtaja Leo Koivulehto … Vuoden 2025 liikevaihto lähenee 2 miljoonaa euroa',
            'url': 'https://tyopaikkailmoitukset.fi/tekninen-asiakaspalvelija-localnet-finland-tyopaikat/'}],
    fihadd='芬兰 20+年 ISP;Koivulehto Founder/CEO 实体')

put('B-215',
    head='Alfa Centauri spol. s r.o.(Pri strelnici 3, 821 04 Bratislava,Slovakia;IČO 35 862 301, DIČ 2020290426;Vložka 29289/B;'
         '**谱型=网络/服务器管理外包+咨询+软件硬件审计+布线实体**;alfac@alfac.sk / 02 4342 7175;'
         'CSV 谱主位 Michal Petkáč = 顾问（R65 与 Alfa Centauri 实体联动口径）',
    kpn='Michal Petkáč = 顾问（CSV 谱主位；Alfa Centauri 实体谱联动）',
    kp=[{'name': 'Michal Petkáč', 'role': '顾问/谱主位（Alfa Centauri 联口）', 'contact': 'alfac@alfac.sk / 02 4342 7175', 'status': 'CSV 谱 + alfac.sk 官网自曝', 'source': 'https://www.alfac.sk/kontakt'}],
    facts=[{'dim': 'R65 实体映射', 'text': 'Alfac = Alfa Centauri spol. s r.o. Bratislava Pri strelnici 3 IČO 35862301；网络托管/咨询/审计谱',
            'quote': 'Alfa Centauri spol. s.r.o. Pri strelnici 3, 821 04 Bratislava IČO: 35 862 301 … Správa sietí a serverov, outsourcing, poradenstvo, softvérový a hardvérový audit, realizácia kabeláže siete … alfac@alfac.sk',
            'url': 'https://www.alfac.sk/kontakt'}],
    fihadd='Alfa Centauri Bratislava 网络托管谱')

put('B-222',
    head='LTD "Intellcom Group"(42 Tereverko St., Tbilisi 0159（展厅/服务）/ 5 Shalva Gogidze St.(仓储）, Georgia;+995 32 298 9849, sale@intellcom.net;'
         '**Lali Mekvabishvili = Managing Director(DnB 实名）**;'
         '谱型=格鲁吉亚 IT/安防/太阳能/光 大谱批发——MikroTik/Ubiquiti/Uniview/KSTAR/Leoch/Fortinet/Sumitomo/DRAKA/ZTT/Mirsan 等多品牌谱开 + 自建太阳能 UPS WiFi 设计服务谱位',
    kpn='Lali Mekvabishvili = Managing Director',
    kp=[{'name': 'Lali Mekvabishvili', 'role': 'Managing Director', 'contact': 'sale@intellcom.net / +995 32 298 9849', 'status': 'DnB 实名 + intellcom.ge 官网双源', 'source': 'https://www.dnb.com/business-directory/company-profiles.intellcom_ltd.c9b2e76df80f45ef07f0094466b87605.html'}],
    facts=[{'dim': 'R65 实体/实名', 'text': 'LTD Intellcom Group Tbilisi 42 Tereverko St.;MikroTik/Ubiquiti 多谱批发；Mekvabishvili MD 实名',
            'quote': 'Intellcom Ltd … Key Principal: Lali Mekvabishvili, Managing Director … LTD "Intellcom Group" 42 Tereverko St. Tbilisi 0159 Georgia sale@intellcom.net +995 32 298 9849',
            'url': 'https://www.intellcom.ge/en/contact/'}],
    fihadd='格鲁吉亚 IT 大院谱；Mekvabishvili MD 实名')

put('B-043',
    head='Georgi Vasilev(Sofia 保加利亚 LinkedIn 血谱：**DXC Technology 员工**,Technical University of Sofia 2023+ Dev Ninjas;'
         '**已获 MikroTik Certified Routing Engineer(MTCRE, 2024-11 谱；本人 LinkedIn 自曝）**——谱型=技艺无限大谱；Oracle Cloud Foundations Associate 2024;谱位=高技 MikroTik 同时兼任 DXC',
    kpn='Georgi Vasilev = DXC Technology 员工 + MTCRE 持证（LinkedIn 自曝）',
    kp=[{'name': 'Georgi Vasilev', 'role': 'DXC Technology 员工 / MTCRE 持证', 'contact': 'linkedin.com/in/vasilevgeorgi', 'status': 'LinkedIn 自曝', 'source': 'https://www.linkedin.com/in/vasilevgeorgi/'}],
    facts=[{'dim': 'R65 核正', 'text': 'Georgi Vasilev(DXC, TU Sofia）持有 MTCRE 2024 证书；Oracle CI Foundations 2024;IT 2003 至今',
            'quote': 'Happy to share my achievement - MikroTik Certified Routing Engineer … Successfully obtain Oracle Cloud Infrastructure 2024 Foundations Associate … Experience: DXC Technology … Education: Technical University of Sofia',
            'url': 'https://www.linkedin.com/in/vasilevgeorgi/'}],
    fihadd='MTCRE 持证 DXC 员工实体谱！专业技术谱位')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 22 批（克/芬兰/斯洛伐克/格鲁吉亚/保加利亚）',
       'scope': 'B-201 PCV / B-520 TECON / B-398 LocalNet / B-215 Alfac / B-222 Intellcom / B-043 Georgi Vasilev',
       'records': [by[c] for c in ('B-201', 'B-520', 'B-398', 'B-215', 'B-222', 'B-043')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第22批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 22 批 6 户落盘')
