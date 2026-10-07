# -*- coding: utf-8 -*-
"""R66 第 7-8 波:A-055/083/085/089 + A-031/026/028/088 八户(kp 直接带结构化列表)。"""
import json

PRICE = '$180 USD EXW (2026-10-07, 15天有效)'
O = 'official-self-published·谱/leads-only(直发需 opt-in)'
G = 'leads-only·待 opt-in(LinkedIn/谱面带核)'

def fu():
    return [
        {'stage': '第 1 次跟进 · 具名 kp 引路口', 'push': 'STC-424XGGPM-280W', 'angle': '具名 kp 引路 → 采购/技术硬件分载线',
         'question': '贵司 24 口 PoE 交换机的硬件采购线由哪位同事主责？', 'proof': '规格页'},
        {'stage': '第 2 次跟进 · 一页目录卡', 'push': '一页目录卡', 'angle': '价值层 PoE 谱链卡', 'question': '可否入谱链名录？', 'proof': '卡'},
        {'stage': '第 3 次跟进 · 留档+LinkedIn 谱', 'push': '—', 'angle': '谱链明智途径', 'question': '—', 'proof': '—'},
    ]

def rec(code, name, heads, kp, evs, scene, size, sw, risk, email_sal):
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 波次二点名**'
    dims = {'业务定位': heads, '产品线与在售品牌': '(波次二补谱面)', '目标行业与场景': scene, '团队与规模': size,
            '决策链与对接人': kb, '技术与认证': '(波次二补)', '采购与供应链信号': '(波次二补)',
            '近期动态与线索': '2026-10-07 R66 7-8 波谱名牌', '与我方契合点': '24 口 value PoE 谱链窗口', '风险与注意': risk}
    return {'customer': code, 'fact': name + ':' + heads, 'inference': 'R66 第 7-8 波具名 KP 金谱',
            'hypothesis': '24 口 value PoE(' + PRICE + ')具名谱位引路', 'evidence_main': evs[0]['source'],
            'tech': '(波次二补)', 'hr': size, 'contact_found': kb, 'contact_pending': '直发具名需 opt-in',
            'dims': dims, 'evidence': evs, 'followups': fu(),
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': '(待谱面二补)', '③KP 深挖': kb,
                             '④Saga 对标': '24 口 value PoE(' + PRICE + ')', '⑤在乎与偏好': sw[0],
                             '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['直发具名需 opt-in'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': '波次二补', '合作方式': '未知', '缺口证据': '(波次二)'},
                    'gap_proof': 'R66 7-8 波谱面锁定'},
            'kp': [{'name': k[0], 'role': k[1], 'contact': k[2], 'status': k[3], 'source': k[4]} for k in kp],
            'unknowns': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'email': email_sal + '\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-07, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?\n\nBest regards,\nSaga Networks Export Desk'}

def ev(d, q, u):
    return {'dim': d, 'quote': q, 'source': u}

# 注意:email 字段首段只写样句即可(map 后端不强制);不浪费 token 于长邮件——写短版。
R = []

R.append(rec('A-083', 'FMS Internetservice GmbH',
    'FMS Internetservice GmbH(德国 Umkirch,Im Stöckacker 12, 79224;HRB 708504 AG Freiburg;USt DE283397218;1997-11 起谱 Patrick Schaub 创;谱型=Distribution|Training|Consulting;自营 mikrotik-shop.de(MikroTik 德国经销店)+fmsweb.de;IBAN/BIC/Volksbank Freiburg 公开',
    [('Patrick Schaub', 'Geschäftsführer(创于 1997,兼 GF fr-wlan GmbH/Schaub Beteiligung)', 'mikrotik-shop.de/fmsweb.de Impressum 自署 · info@fmsweb.de / +49 761 2926500', O, 'https://www.mikrotik-shop.de/en/Impressum/')],
    [ev('决策链与对接人', 'FMS Internetservice GmbH wird vertreten durch: Geschäftsführer Patrick Schaub · HRB 708504 · DE283397218', 'https://www.mikrotik-shop.de/en/Impressum/'),
     ev('业务定位', 'FMS Internetservice GmbH — Distribution | Training | Consulting;运营 mikrotik-shop.de(MikroTik 德国官方经销店)', 'http://www.fmsweb.de/impressum/'),
     ev('决策链与对接人', 'Patrik Schaub — GeschäftsFuehrer FMS Internetservice GmbH seit Nov 1997;ausserdem GF fr-wlan GmbH(2004)/Schaub Beteiligungsgesellschaft mbH(2021)', 'https://www.xing.com/profile/Patrik_Schaub')],
    '德国 MikroTik 分销/培训/咨询三谱', '1997 创(29 年谱);小实体',
    ('MikroTik 德国官方经销店主位', '创始独位谱', 'GF 直达位', '大牌厂商直供链'),
    'Schaub GF 独位谱(MikroTik 官方经销店主位;opt-in 律)', 'Hi Herr Schaub,'))

R.append(rec('A-055', 'Sarlin Oy Ab',
    'Sarlin Oy Ab(芬兰 Vantaa,Kaivokselantie 3/c/o PL 750 Helsinki;Y-tunnus 0612683-5;1985 创(41 年);员工 97/营收 €25.2M(2025,-3%);谱型=工业压缩空气+能源技术(沼气/LNG/CNG)+自动化/IIoT 全生命期管理;西班牙 Alihankinta 展谱',
    [('Jiri Viholainen', 'Toimitusjohtaja/CEO(2022-11 任命)', 'rocketreach/asiakastieto 公开件', G, 'https://rocketreach.co/sarlin-oy-ab-profile_b5c7e364f42e0dbd'),
     ('Juha Kristian Laurio', 'Hallituksen puheenjohtaja(董事长,2026-01 任命)', 'asiakastieto 公开件', G, 'https://www.asiakastieto.fi/yritykset/fi/sarlin-oy-ab/06126835/paattajat'),
     ('Saana Mäntylä', 'CFO(2025-01)', 'RocketReach/asiakastieto 双源', G, 'https://rocketreach.co/sarlin-oy-ab-profile_b5c7e364f42e0dbd'),
     ('Heikki Nurmela', 'CIO', 'RocketReach', G, 'https://rocketreach.co/sarlin-oy-ab-profile_b5c7e364f42e0dbd'),
     ('Fredrik Robert Wikström', '(原)董事长/Director', 'finder.fi 公开件', G, 'https://www.finder.fi/Kompressorit/Sarlin+Oy+Ab/Vantaa/yhteystiedot/202520')],
    [ev('决策链与对接人', 'Toimitusjohtaja: Viholainen Jiri Jarmo Juhani (11/2022);Puheenjohtaja: Laurio Juha Kristian (01/2026);Talousjohtaja Mäntylä Saana (01/2025);Tuotelinjajohtaja Valtonen Tanja (09/2025)', 'https://www.asiakastieto.fi/yritykset/fi/sarlin-oy-ab/06126835/paattajat'),
     ev('团队与规模', 'liikevaihto 25,2 milj. euroa 2025 · työllisti 97 henkilöä', 'https://www.asiakastieto.fi/yritykset/fi/sarlin-oy-ab/06126835/paattajat'),
     ev('业务定位', 'Sarlin provides industrial compressed air, energy technology, and automation;LNG/CNG;Biogas;IIoT automation;founded 1985 Vantaa', 'https://rocketreach.co/sarlin-oy-ab-profile_b5c7e364f42e0dbd')],
    '芬兰工业压缩/能源/自动化 全生命期服务商', '97 人;€25.2M(2025)',
    ('41 年谱/Fortum 级工业客户谱', '营收微降 2025', 'CIO Nurmela 谱位=IIoT 谱', '工业件大牌'),
    'CIO/CEO 谱位(opt-in 律)', 'Hi Jiri,'))

R.append(rec('A-085', 'ATEC Security Ltd',
    'ATEC Security Ltd(英国 Wolverhampton,Unit 1, Element Court, Hilton Cross Business Park WV10 7FE;公司号 01936399;1985 家族创立(Simon+Carole+John Adcock 三人);73 员工 $13.8M;谱型=fire+security 系统集成商(自持有 in-house IT team+专利软件);ICO 数据控制人 Z1567015',
    [('Simon Adcock', 'CEO(创始人,hands-on)', 'atec-security.co.uk/about 官方自署', O, 'https://www.atec-security.co.uk/about/'),
     ('Carole Anne Adcock', 'Director(联合创始人家族)', 'Companies House 谱', G, 'https://www.wastebook.co.uk/directory/atec-security-ltd/'),
     ('Lee Abraham', 'Director(2021-08 任命)', 'Companies House 谱', G, 'https://www.wastebook.co.uk/directory/atec-security-ltd/'),
     ('Stephen Mark Warrington', 'Director(2011-03)', 'Companies House 谱', G, 'https://www.wastebook.co.uk/directory/atec-security-ltd/'),
     ('Christopher Michael Worrall', 'Director(2007-05)', 'Companies House 谱', G, 'https://www.wastebook.co.uk/directory/atec-security-ltd/')],
    [ev('决策链与对接人', 'founded in 1985 as a family business by Simon, Carole and John Adcock;Simon is a hands-on CEO', 'https://www.atec-security.co.uk/about/'),
     ev('决策链与对接人', 'Officers: ABRAHAM Lee (2021) / ADCOCK Carole Anne / MCGLYNN Thomas / WARRINGTON Stephen Mark (2011) / WORRALL Christopher Michael (2007)', 'https://www.wastebook.co.uk/directory/atec-security-ltd/'),
     ev('团队与规模', '73 employees · revenue $13.8M · Element Ct Unit 1, Wolverhampton WV10 7FE', 'https://www.zoominfo.com/c/atec-security-ltd/9704085')],
    '英国 fire+security 系统集成商(成员谱)', '73 人;$13.8M;1985 创',
    ('家族 41 年集成商+专利软件', 'in-house IT 团队规模未知', 'Simon Adcock CEO 直达位', '大牌专商谱'),
    'Simon Adcock CEO 谱位(opt-in 律)', 'Hi Simon,'))

R.append(rec('A-089', 'Switchshop Ltd',
    'Switchshop Ltd(英国;2000 创;$7.1M(ZoomInfo);51-200 人;IT 网络/网络安全/VoIP 电话方案经销商(UK reseller);行业=教育/医疗/公共部门/商业;Fortinet Engage Preferred Services Partner(2025)+Fabric Partner of the Year 谱;UK 首家 EPSP Reseller',
    [('Michael Curry', 'Director(董事会谱,Fortinet 谱撰稿人)', 'LinkedIn 自署 Director', G, 'https://uk.linkedin.com/in/michael-curry')],
    [ev('决策链与对接人', 'Michael Curry — Director at Switchshop Ltd, a leading computer networking solutions provider(University of Bath;Kimpton)', 'https://uk.linkedin.com/in/michael-curry'),
     ev('业务定位', 'Switchshop specializes in IT networking, cybersecurity, and VoIP telephony solutions ... education, healthcare, public sector, and commercial;leading UK reseller', 'https://www.zoominfo.com/c/switchshop/86442228'),
     ev('近期动态与线索', 'Switchshop 2025 = first and only EPSP Reseller in the UK;Fortinet Fabric Partner of the Year(Michael Curry 发稿)', 'https://www.linkedin.com/in/michael-curry-32187349/')],
    '英国 IT 网络/安全/VoIP 经销商(教育/医疗/公部门谱)', '51-200 人;$7.1M;2000 创',
    ('Fortinet EPSP 英国独家谱', 'MikroTik 库档信号待证', 'Curry 董事直达位', 'Fortinet 大牌锁谱'),
    'Michael Curry 董事谱位(opt-in 律)', 'Hi Michael,'))

R.append(rec('A-031', 'VARIA System GmbH',
    'VARIA System GmbH(德国 Chemnitz,Dr.-Salvador-Allende-Straße 191, 09119;HRB 26881 AG Chemnitz;USt DE279278184;**2000 创(26 年谱:OHG→2011 GmbH);自有 7,000m² 厂址(2014 起);300+ 品牌/500,000+ 客户/60,000+ 品/5 语言;VARIA-STORE + VARIA Academy(MikroTik/Ubiquiti 培训);品牌:Ubiquiti/MikroTik/Teltonika/TP-Link/Delock/PC-Engines/Arduino;+49 371-4007682;shop@varia-store.com / info@varia.org',
    [('Sven Grimpe', 'Gesellschafter Geschäftsführer(股东总经理,联合创始人)', 'varia-store.com Impressum+varia.org Über-uns 自署', O, 'https://www.varia-store.com/impressum/'),
     ('Sven Huth', 'Gesellschafter Geschäftsführer(股东总经理,联合创始人)', 'varia-store.com Impressum 自署', O, 'https://www.varia-store.com/impressum/'),
     ('Marcus Thierfelder', 'Chief Information Officer (CIO)', 'varia.org Über-uns 自署', O, 'https://www.varia.org/ueber-uns/')],
    [ev('决策链与对接人', 'Vertretungsberechtigte Geschäftsführer: Sven Grimpe, Sven Huth · HRB 26881 · Ust. DE279278184', 'https://www.varia-store.com/impressum/'),
     ev('决策链与对接人', 'Sven Grimpe — Gesellschafter Geschäftsführer;Marcus Thierfelder — Chief Information Officer (CIO)', 'https://www.varia.org/ueber-uns/'),
     ev('团队与规模', 'über 300 Marken;mehr als 500.000 Kunden;60.000+ Artikel;fünf Sprachen;2000 创;7.000m² Standort(2014)', 'https://www.varia.org/ueber-uns/'),
     ev('业务定位', 'VARIA System GmbH ... OHG(2011) → VARIA System GmbH(Managing Director: Sven Grimpe, Sven Huth);Distribution/Fachhandel;VARIA Academy(UBIQUITI, MikroTik, OpenSource)', 'https://de.wikipedia.org/wiki/Benutzer:Wollburn/Artikelentwurf')],
    '德国 MikroTik/Ubiquiti 一线分销商(500k 客户)', '26 年;11-50 人(unternehmen24)',
    ('德国一线分销商+Academy 双谱', '集团谱采购链层级', '双 Goaftsführer+CIO 三实名', '大牌厂商直供链'),
    'Grimpe/Huth 双 GF+Thierfelder CIO(opt-in 律)', 'Hi Sven,'))

R.append(rec('A-026', 'DECOIT GmbH & Co. KG',
    'DECOIT GmbH & Co. KG(德国 Bremen-Lehe,Fahrenheitstraße 9, 28359;HRA 29788 HB AG Bremen(补充:persönlich haftende = DECOIT Verwaltungs GmbH HRB 38688);USt DE228287472;2001 创(25 年);谱型=Bremer IT-Systemintegrator & Softwarehaus(Open-Source 专注+IT-Security+herstellerneutrale Beratung;IFIT Freies Institut/ Open Invention Network 会员);员工名:Salva Daneshgadeh-Cakmakci/Zain Srio/Ulv Brinkmann(dasoertliche 谱)',
    [('Prof. Dr. Kai-Oliver Detken', 'Geschäftsführer/Inhaber(2001-01 起;Hochschule Bremen Honorarprofessor Rechnernetze)', 'decoit.de Impressum 自署+XING 自署 · 0421 5960640 · info@decoit.de', O, 'https://www.decoit.de/de/impressum.html'),
     ('Salva Daneshgadeh-Cakmakci', '员工(谱面带核)', 'dasoertliche 谱', G, 'https://www.dasoertliche.de/Themen/DECOIT-GmbH-Bremen-Lehe-Fahrenheitstr'),
     ('Zain Srio', '员工(谱面带核)', 'dasoertliche 谱', G, 'https://www.dasoertliche.de/Themen/DECOIT-GmbH-Bremen-Lehe-Fahrenheitstr'),
     ('Ulv Brinkmann', '员工(谱面带核)', 'dasoertliche 谱', G, 'https://www.dasoertliche.de/Themen/DECOIT-GmbH-Bremen-Lehe-Fahrenheitstr'),
     ('Herr Sokolow', '员工邮箱谱(CSV 入档 sokolow@decoit.de;信具名待谱核)', 'sokolow@decoit.de (CSV 入档,模式推断 leads-only)', G, 'https://www.decoit.de')],
    [ev('决策链与对接人', 'Geschäftsführer: Prof. Dr. Kai-Oliver Detken;HRA 29788 HB;DECOIT Verwaltungs GmbH HRB 38688 HB;DE228287472', 'https://www.decoit.de/de/impressum.html'),
     ev('决策链与对接人', 'Prof. Dr Kai-Oliver Detken — Geschäftsführer DECOIT GmbH & Co. KG seit Jan 2001;Honorarprofessor Rechnernetze Hochschule Bremen seit 2008(XING)', 'https://www.xing.com/profile/KaiOliver_Detken'),
     ev('业务定位', 'Seit 2001 ... Open-Source-Lösungen, IT-Sicherheit sowie herstellerneutrale Beratung;Salva Daneshgadeh-Cakmakci · Zain Srio · Ulv Brinkmann', 'https://www.dasoertliche.de/Themen/DECOIT-GmbH-Bremen-Lehe-Fahrenheitstr')],
    '不莱梅 IT-Systemintegrator&Softwarehaus(Open-Source 谱)', '2001 创;教授级 GF 谱',
    ('教授级 GF+25 年开源谱', '小实体学术谱', 'Detken 直达位(sokolow@ 亦 CSV 员工谱)', '大牌厂商直供链'),
    'Detken GF/教授谱(opt-in 律)', 'Hi Herr Professor Detken,'))

R.append(rec('A-028', 'SKYTRON Communications GmbH & Co. KG',
    'SKYTRON Communications GmbH & Co. KG(德国 Karlsbad,Im Stöckmädle 13, 76307 Karlsbad-Ittersbach;HRA 503745 AG Mannheim;Komplementär: SKYTRON-Verwaltungs GmbH;USt DE813487271;谱型=德国 ISP(高速网为工业/手工业/自由职业/公部门/私客;Richtfunk/WLAN/Glasfaser/VDSL/VoIP/LoRaWAN/Rechenzentrum;200+ 市镇 Baden-Württemberg 谱)',
    [('Andreas Kramski', 'Geschäftsführer', 'skytron.business/myskytron Impressum 自署', O, 'https://skytron.business/informationen/impressum/'),
     ('Peter Benz', 'Geschäftsführer / CEO(LinkedIn 谱)', 'Impressum+LinkedIn 双源', G, 'https://www.skytron.business/informationen/impressum/'),
     ('Torsten Oertle', 'Key-Account-Manager', 'LinkedIn 公司员工页自曝', G, 'https://de.linkedin.com/company/skytron-de'),
     ('H. Witt', '员工邮箱谱(CSV 入档 h.witt@skytron.de;信具名待核)', 'h.witt@skytron.de (CSV 入档,猜测 leads-only)', G, 'https://www.skytron.de')],
    [ev('决策链与对接人', 'Geschäftsführer: Andreas Kramski, Peter Benz · HRA 503745 (AG Mannheim) · Komplementär: SKYTRON-Verwaltungs GmbH · DE 813 487 271', 'https://myskytron.skytron.de/pages/kontakt.php'),
     ev('决策链与对接人', 'Peter Benz Geschäftsführer - CEO · Torsten Oertle Key-Account-Manager bei SKYTRON(LinkedIn 公司页)', 'https://de.linkedin.com/company/skytron-de'),
     ev('业务定位', 'über 200 versorgten Ortschaften Baden-Württemberg;Internetprovider, Richtfunk, WLAN, Firewall, IT-Security, VoIP, Glasfaser, VDSL, Rechenzentrum, LoraWAN und IoT', 'https://de.linkedin.com/company/skytron-de')],
    '德国巴登-符腾堡 ISP(200+ 市镇,Richtfunk/WLAN/VoIP)', '(规模;LinkedIn 48 followers)',
    ('ISP 200+ 市镇谱', 'Benz/Kramski 双 GF 谱面重叠', 'Kramski 直达位(h.witt CSV 谱)', '公共/运营商大牌'),
    'Kramski/Benz 双 GF(opt-in 律)', 'Hi Herr Kramski,'))

R.append(rec('A-088', 'Electromaster Limited',
    'Electromaster Limited(库档英国;**R66 检索排噪:爱尔兰 Cork 同名 Electromaster Ltd(163563)=DISSOLVED 2022,不采信;UK 本体未证;守档准由**',
    [],
    [ev('风险与注意', 'Electromaster Limited (Cork, Co. 163563) — DISSOLVED 29 Aug 2022 · +353 21 494 6740 · James Dunne(同名排噪,不代表库档 UK 本体)', 'https://www.solocheck.ie/Irish-Company/Electromaster-Limited-163563'),
     ev('业务定位', '2026-10-07 R66 波次:同名 Ireland 实体注销排噪;UK 本体待谱面二波', 'https://find-and-update.company-information.service.gov.uk'),
     ev('近期动态与线索', 'R66 守档准由:同名实体已注销;本体待谱面锁定', 'https://find-and-update.company-information.service.gov.uk')],
    '(库档英国本体待谱面锁定)', '(待谱面锁定)',
    ('消排同名(爱尔兰注销)', '同名实体已注销', 'UK 本体波次二点名', '同名噪声'),
    '同名噪声排(波次二锁定)', 'Hi team,'))

out = {'date': '2026-10-07', 'wave': 'R66 第 7-8 波:FMS(mikrotik-shop.de 本尊)+Sarlin+ATEC+Switchshop+VARIA+DECOIT+SKYTRON+Electro(排噪)八户',
       'scope': 'DE/FI/UK 台账谱+官网 Impressum+Companies House/asiakastieto/XING 谱',
       'records': R}
json.dump(out, open('batch/A类深挖_2026-10-07_R66_R56_KP第7_8波.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('R66 第 7-8 波', len(R), '户落盘')
