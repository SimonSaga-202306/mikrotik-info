# -*- coding: utf-8 -*-
"""R65 B 类深挖第 16 批:瑞典 3 + 西班牙 DMI。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 16 批精修 = R57 转写 + 本轮调研新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-527',
    head='EG Electronics AB(Fagerstagatan 3, Spånga 16353, Stockholm;KONECTA 集团属；'
         '**Anders Nilsson = Subsidiary CEO / Anders Jacobsson = Group CEO(集团口径）**;Jouni Telio KAM/Jonas Kallsten/Johan Bjorkman 等 81 员工；'
         '谱型=北欧电子/机电部件分销 100+ 年血统，工业/运输/医疗/防务跨度；2025-10-01 收购 Acte Solutions 显示与系统业务；美国+中国办',
    kpn='Anders Nilsson = EG Electronics AB Subsidiary CEO(contactout/DnB);Anders Jacobsson = Group CEO(2025-10 收购新闻稿）',
    kp=[{'name': 'Anders Nilsson', 'role': 'Subsidiary CEO(EG Electronics AB)', 'contact': '经 egelectronics.com', 'status': 'contactout + DnB 双源（DnB 名： Karl Olof Johnny Hedlund 管理层口径同步）', 'source': 'https://contactout.com/company/EG-Electronics-96339'},
        {'name': 'Anders Jacobsson', 'role': 'Group CEO(KONECTA)', 'contact': '同上', 'status': 'egelectronics.com 2025-10-01 自曝', 'source': 'https://egelectronics.com/news/expands-and-acquires-business-in-displays-and-system-solutions/'}],
    facts=[{'dim': 'R65 集团/收购', 'text': 'EG Electronics AB Spånga 81 人/跨工业医疗防务；2025-10-01 收购 Acte Solutions 显示系统业务；KONECTA 大谱',
            'quote': '"says Anders Jacobsson, CEO, EG Electronics AB" … The acquisition takes effect on October 1, 2025 … EG Electronics AB is a leading Nordic supplier of advanced electronic and electromechanical components',
            'url': 'https://egelectronics.com/news/expands-and-acquires-business-in-displays-and-system-solutions/'}],
    fihadd='KONECTA 北欧大谱 81 人；Nilsson+Jacobsson CEO 两谱线')

put('B-528',
    head='HighTech Nordic AB(Gaddvägen 3, SE-761 48 Norrtälje, Sweden;2017 创 KONECTA/PrimoTech Group 2024-05-13 收购；'
         '**Keith Jeminen + Andreas Luther = 联合创始（30+ 年合并经验），Andreas Luther = Co-Founder & CEO**;'
         '谱型=工业 PC/Embedded/数位标牌/医疗电脑/展示备件门——年 3,000+ 定制系，-40°C 北地到沙坚谱在各业（基础/工业/国防/海事/零售/自动化）;info@hightechnordic.com / +46(0)10-177 58 00',
    kpn='Andreas Luther = Co-Founder & CEO(PrimoTech 收购同位）;Keith Jeminen = Co-Founder',
    kp=[{'name': 'Andreas Luther', 'role': 'Co-Founder & CEO', 'contact': 'info@hightechnordic.com', 'status': 'Tracxn + imap 双源实名', 'source': 'https://tracxn.com/d/companies/hightech-nordic/__h-gXUOxgKfE5SzYDWYemsjeX6xhGPO-AQIwa3ruQCRc'},
        {'name': 'Keith Jeminen', 'role': 'Co-Founder', 'contact': '同上', 'status': '同上', 'source': '同上'}],
    facts=[{'dim': 'R65 收购/实名', 'text': 'HighTech Nordic AB · Norrtälje 2017 创 · Luther+Jeminen 30+年谱联创 · 2024-05-13 PrimoTech 收购；工业 PC/Embedded 亿级定制',
            'quote': 'HighTech Nordic is an acquired company based in Norrtalje (Sweden), founded in 2017 by Keith Jeminen and Andreas Luther … Andreas Luther: Co-Founder & CEO … Acquired by Primotech (May 13, 2024)',
            'url': 'https://tracxn.com/d/companies/hightech-nordic/__h-gXUOxgKfE5SzYDWYemsjeX6xhGPO-AQIwa3ruQCRc'}],
    fihadd='PrimoTech 收购 2024-05;Luther 实首工业 PC 谱')

put('B-296',
    head='Sanuk Systems AB(Bangkok/Rayong/Hua Hin 泰国+Stockholm 瑞典双杆；AS138616 APNIC 泰国实体；'
         '**谱型=瑞典泰两谱「酒店/社群宽带/光纤/WiFi/全球互联网服务」运营商+MikroTik reseller 官方自曝**;MikroTik 装备多年部署自认(Broadcast sites/remote offices/central hubs/operator environments);'
         '官网自述 MikroTik Reseller',
    kpn='—(AB aktiebolagsregistret 收费墙；R65 谱位+双域名谱自曝足档；泰国实体 AS138616 档案挂靠）',
    facts=[{'dim': 'R65 谱自曝', 'text': 'Sanuk Systems=瑞/泰双谱酒店宽带运营；MikroTik Reseller 官方自曝；多年部署 operator 环境档',
            'quote': 'We have an extensive practical knowledge of particularly MikroTik network equipment from our many deployments, and both resell hardware and provide consulting … Mikrotik Reseller … Sanuk Systems are based in Rayong and Hua Hin, Thailand and Stockholm, Sweden',
            'url': 'https://www.sanuksystems.com/business/'}],
    fihadd='瑞/泰双谱酒店谱型=瑞泰国宽带双线实体')

put('B-462',
    head='DMI Computer(西班牙 IT 大国批发；1989 创，100% 西班牙资本，CIF A-79522702;2025 年营收 €164M/120+ 职业；'
         '**Emilio Sánchez-Clemente = CEO(esanchez@dmi.es)**;José Antonio Rodríguez = Director de negocio(jarodriguez@dmi.es);Javier Martín Martín = Compras Coordinador(jmartin@dmi.es);La Coruña/Málaga/Valencia/Pcolon 4 移办);'
         '**谱涵:MikroTik/Ubiquiti/Tp-Link/Netgear/Digitus 等连通谱；DMI PRO 子缋谱=', 
    kpn='Emilio Sánchez-Clemente = CEO;José Antonio Rodríguez = Director de negocio;Javier Martín Martín = Compras Coordinador',
    kp=[{'name': 'Emilio Sánchez-Clemente', 'role': 'CEO', 'contact': 'esanchez@dmi.es', 'status': 'channelpartner.es + Quiz自曝双源', 'source': 'https://channelpartner.es/guia-canal-tic/quien-es-quien/1098536047802/dmi-computer.1.html'},
        {'name': 'José Antonio Rodríguez', 'role': 'Director de negocio（业务总监）', 'contact': 'jarodriguez@dmi.es', 'status': '同上', 'source': '同上'},
        {'name': 'Javier Martín Martín', 'role': 'Coordinador de Compras（采购协调）', 'contact': 'jmartin@dmi.es', 'status': '同上', 'source': '同上'}],
    facts=[{'dim': 'R65 谱/体量', 'text': 'DMI Computer 1989 创 165M 2025 营收 120 职业；MikroTik 谱涵+Ubiquiti/Tp-Link/Netgear 等；西班牙纯资 100%',
            'quote': 'Responsable Emilio Sánchez-Clemente, CEO … Facturación anual: 164 millones de euros de facturación en 2025 … Conectividad: Tp-Link, Ubiquiti, Gembird, Mikrotik, Digitus by Assmann, Aisens, Netgear, Lanberg',
            'url': 'https://guiacanaltic.channelpartner.es/dmi-computer/'}],
    fihadd='西班牙 IT 批为 €164M 巨号;DMI MikroTik 谱位谱全开')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 16 批（瑞典 3+ 西班牙 DMI)',
       'scope': 'B-527 EG Electronics / B-528 HighTech Nordic / B-296 Sanuk Systems / B-462 DMI Computer',
       'records': [by[c] for c in ('B-527', 'B-528', 'B-296', 'B-462')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第16批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 16 批 4 户落盘')
