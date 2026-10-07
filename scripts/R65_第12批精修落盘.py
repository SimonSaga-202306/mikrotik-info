# -*- coding: utf-8 -*-
"""R65 B 类深挖第 12 批:英国 4 + 荷兰 5。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 12 批精修 = R57 转写 + 本轮 Companies House/KvK 新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-531',
    head='IVORY EGG (UK) LIMITED(KNX 智建技术型分销商;**Colin Price = founder(KNX 血统,首代把 KNX 推入英国)**;'
         'Mark Warburton = Technical Director UK(2020 起 director 角色兼电气时报 KNX 课程主讲);Romesh Anandaraja = NZ Exec Director;Craig Chapman = Group CEO;'
         '集团英国/澳大利亚/新西兰三国架',
    kpn='Colin Price = Founder(KNX 血统);Mark Warburton = Technical Director/UK Director;Craig Chapman = Group CEO',
    kp=[{'name': 'Colin Price', 'role': 'Founder(创始人/KNX 首代引进者)', 'contact': '经 ivoryegg.co.uk', 'status': 'ivoryegg.co.uk 自曝', 'source': 'https://ivoryegg.co.uk/about'},
        {'name': 'Mark Warburton', 'role': 'Technical Director(UK Ltd)', 'contact': '同上', 'status': 'knxtoday + Electrical Times 双源', 'source': 'https://www.knxtoday.com/2020/08/16329/ivory-egg-gets-fit-for-the-future.html'},
        {'name': 'Craig Chapman', 'role': 'Group CEO', 'contact': '同上', 'status': 'ivoryegg.co.uk 自曝', 'source': 'https://ivoryegg.co.uk/about'}],
    facts=[{'dim': 'R65 谱位', 'text': 'Ivory Egg KNX 技术型分销;Colin Price founder;Mark Warburton UK Technical Director;英/澳/新三国架',
            'quote': 'Ivory Egg founder Colin Price adopted KNX as the control platform of choice … Romesh Anandaraja Executive Director [NZ] … Craig Chapman Chief Executive Officer [Group]',
            'url': 'https://ivoryegg.co.uk/about'}],
    fihadd='KNX 语族首代分销;Colin Price 所创/README 英国 KNX 推广者')

put('B-532',
    head='M.A.C. Solutions (UK) Limited(Companies House 03762835,1996 创;'
         '**David Porter = Chief Executive Officer;Ian Bailey = Director(1980 生，2020-09 在任)+ John Edward Bailey = Director(1953 生,2020-09 在任)**;'
         '工业自动化/过程连接 cyber 英国老谱——mac-solutions.net 主域;Moxa/Anybus 等工业通讯线谱涵',
    kpn='David Porter = CEO(ZoomInfo);Ian Bailey + John Edward Bailey = 双 Directors(Companies House FL)',
    kp=[{'name': 'Ian Bailey', 'role': 'Director(2020-09 在任)', 'contact': '经 mac-solutions.net', 'status': 'Companies House 03762835 实名', 'source': 'https://find-and-update.company-information.service.gov.uk/company/03762835/officers'},
        {'name': 'John Edward Bailey', 'role': 'Director(2020-09 在任)', 'contact': '同上', 'status': '同上', 'source': '同上'},
        {'name': 'David Porter', 'role': 'Chief Executive Officer', 'contact': '同上', 'status': 'ZoomInfo 自曝', 'source': 'https://www.zoominfo.com/c/mac-solutions/354379890'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'MAC Solutions UK Ltd 03762835 · 1996 创 · 工业自动化/过程连接 cyber · Ian Bailey + John E Bailey 双董事 · David Porter CEO',
            'quote': 'BAILEY, Ian Role Active: Director Appointed on: 30 September 2020 … BAILEY, John Edward Role Active: Director … David Porter, Chief Executive Officer at MAC Solutions',
            'url': 'https://find-and-update.company-information.service.gov.uk/company/03762835/officers'}],
    fihadd='工业自动化英国 1996 创;Bailey 双董事血统')

put('B-533',
    head='MILLBECK COMMUNICATIONS LIMITED(Companies House 04501248;Wetherby 西约克郡;2002 年 **Paul Graham Finder = 创始董事总经理(1960 生,2002-08 在任至今)**;'
         '谱型=英国商业通信服务/VoIP/宽带/OLT(Fibre/ADSL/EFM/移动 4G);Daniel Finder(1991 生)+Benjamin Finder(1994 生)2024-11 新任董事——富二代接棒家族谱',
    kpn='Paul Graham Finder = Founder & Managing Director(核查处 1960 生);Daniel/Benjamin Finder = 2024-11 新任双董事',
    kp=[{'name': 'Paul Graham Finder', 'role': 'Founder & Managing Director', 'contact': '经 millbeck.co.uk', 'status': 'Companies House + Tracxn 双源', 'source': 'https://find-and-update.company-information.service.gov.uk/company/04501248/officers'},
        {'name': 'Daniel Finder', 'role': 'Director(2024-11 新任)', 'contact': '同上', 'status': '同上', 'source': '同上'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'Millbeck Communications Ltd 04501248 · Wetherby 2002 · Paul Finder 创始 MD+2024 年 Daniel/Benjamin Finder 新董事',
            'quote': 'FINDER, Paul Graham Role Active: Director Date of birth: August 1960 … Founded in 2002 by Paul Finder … The founders of Millbeck Communications is Paul Finder',
            'url': 'https://tracxn.com/d/companies/millbeck-communications/__txNX05Uaoy5lfW7NMbICWfCeiasg7vXQEi5eN4DW-C0'}],
    fihadd='Wetherby 电信 VoIP 老谱 2002;Finder 家族富二代 2024 接棒')

put('B-425',
    head='TELASYS LTD(Companies House 09975808,2016-01-28 创,Cardiff Gate Business Park 注册/Bridgend 5 Raven Close 实际办;'
         '**Lee Gardner Bennett = Director(1987 生,2018-04 在任)+ Craig John Matthews-Clark = Director(1988 生,2017-02 在任)**;'
         '61900 Other telecommunications activities;Bridgend 出/入口汇汇(295 出/55 入船)',
    kpn='Lee Gardner Bennett(1987 生,2018 在任)+ Craig John Matthews-Clark(1988 生,2017 在任)= 双 Director',
    kp=[{'name': 'Lee Gardner Bennett', 'role': 'Director', 'contact': '经 telasys.co.uk', 'status': 'Companies House 09975808 实名', 'source': 'https://find-and-update.company-information.service.gov.uk/company/09975808/officers'},
        {'name': 'Craig John Matthews-Clark', 'role': 'Director', 'contact': '同上', 'status': '同上+companycheck 双源', 'source': '同上'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'Telasys Ltd 09975808 · 2016 创 · Cardiff/Bridgend · Lee Bennett+Craig Matthews-Clark 双董事 · 进出口汇 295/55 船',
            'quote': 'BENNETT, Lee Gardner Role Active: Director Date of birth: July 1987 … MATTHEWS-CLARK, Craig John Role Active: Director',
            'url': 'https://find-and-update.company-information.service.gov.uk/company/09975808/officers'}],
    fihadd='Cardiff 电信 2016;Bennett+Matthews-Clark 双董事名位')

put('B-434',
    head='Interstroom Informatietechnologie B.V.(KvK 52775054,1995 创，Hengelo Demmersweg 3;'
         '**Joris Trooster = Owner 1995-至今(31 年!)**——前荷兰代表 Olympisch roeier(1997-2000 奥运赛艇)+University of Twente 力量训练师；'
         '谱型=IT 咨询互联网应用+iVoIP(品牌)+Outlet Management(多手门商业名)',
    kpn='Joris Trooster = Owner 1995-至今(@interstroom.nl RocketReach 提示+RocketReach 自曝)',
    kp=[{'name': 'Joris Trooster', 'role': 'Owner/Eigenaar(31 年业主,前奥监羶人数)', 'contact': '@interstroom.nl(模式提示)', 'status': 'rocketreach 自曝', 'source': 'https://rocketreach.co/joris-trooster-email_116562226'}],
    facts=[{'dim': 'R65 实名', 'text': 'Interstroom BV KvK 52775054 Hengelo 1995 创；Joris Trooster Owner 1995-至今，多手门商业名+奥运赛艇人血统',
            'quote': '1995 - now Owner @ Interstroom informatietechnologie b.v. … 2000 - 2015 Voorzitter @ Stichting NLroei … Interstroom - iVoIP - Outlet Management … Demmersweg 3 7556BN Hengelo',
            'url': 'https://rocketreach.co/joris-trooster-email_116562226'}],
    fihadd='Trooster 31 年谱主位;iVoIP 品牌谱')

put('B-440',
    head='GPE Networks B.V.(KvK 99477238,Wateringweg 133, 2031EG Haarlem;'
         '**Maurice van der Grijspaarde = Contact persoon/业主(stagemarkt 自曝+实体名)——GPE Holding B.V. Algemeen bestuurder 2026 谱位**;'
         '谱型=电脑咨询+IT 设备批发+电脑设施运维 (SBI 62200/46500/62900)',
    kpn='Maurice van der Grijspaarde = Contactpersoon/KvK 实体业主位',
    kp=[{'name': 'Maurice van der Grijspaarde', 'role': 'Contact persoon（实体业主口径）', 'contact': 'info@gpe-networks.com', 'status': 'stagemarkt + detelefoongids 双自曝', 'source': 'https://stagemarkt.nl/leerbedrijven/profiel_f6268e9d-75e0-4b81-b440-8fe9a3941f5a'}],
    facts=[{'dim': 'R65 实名+登记位', 'text': 'GPE Networks B.V. KvK 99477238 · Haarlem Wateringweg 133 · Maurice van der Grijspaarde· GPE Holding 2026 管理口径',
            'quote': 'Contact persoon: Maurice van der Grijspaarde … GPE Networks B.V. Wateringweg 133 2031EG Haarlem … GPE Holding B.V., Algemeen bestuurder Van 2026',
            'url': 'https://companyinfo.nl/organisatieprofiel/activiteiten-op-het-gebied-van-computerconsultancy-en-beheer-van-computerfaciliteiten/gpe-networks-b-v-haarlem-99477238-000040775445'}],
    fihadd='Grijspaarde 实体谱位置=业主讳;info@ 官方自曝')

put('B-444',
    head='RvdB ICT(rvdbict.nl;**Robbin van den Berg = 实体谱主位（官网自己名在同自曝）**;'
         '谱型=一人系 ICT 全包（netwerkbeheer/firewall/VDSL/光纤/IPTV/备份）;LinkedIn 专长自曝：MikroTik, Ubiquiti UniFi, pfSense firewall, Zabbix',
    kpn='Robbin van den Berg = 实体谱主位（rvdbict.nl 官网+LinkedIn 双自曝)',
    kp=[{'name': 'Robbin van den Berg', 'role': 'Eigenaar/谱主位实体', 'contact': '经 rvdbict.nl', 'status': 'rvdbict.nl+LinkedIn 双自曝', 'source': 'https://rvdbict.nl/'}],
    facts=[{'dim': 'R65 实名/专长', 'text': 'RvdB ICT · Robbin van den Berg 一人 ICT 全包 · MikroTik/UniFi/pfSense/Zabbix 专长',
            'quote': '# RVDBICT, alles op gebied van ICT # Robbin van den Berg … Specialties: • Mikrotik • Ubiquiti Unifi • Pfsense firewall • Zabbix',
            'url': 'https://www.linkedin.com/in/robbin-van-den-berg-03469038/'}],
    fihadd='Rvdb 一人实体；MikroTik/UniFi/pfSense/Zabbix 技谱型注自曝')

put('B-438',
    head='Jeroen Bleuel(荷兰；R65 搜索无果——溴名通 digifotopro 等同名噪声=守档准由)',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜出同名噪声（digifotopro 同名，不采信）;R65 守档准由', 'quote':'(web_search 2026-10-07：同名者 digifotopro 用户，与 MikroTik 无联）', 'url': '(沙箱核验日志)'}],
    fihadd='同名噪声=守档准由')

put('B-433',
    head='Fokko van den Bosch(荷兰深谱；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果）', 'url': '(沙箱日志）'}])

put('B-435',
    head='JPK Consulting(荷兰；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote': '(web_search 无果）', 'url': '(沙箱日志）'}])

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 12 批（英国 4 + 荷兰 5)',
       'scope': 'B-531 Ivory Egg / B-532 MAC Solutions / B-533 Millbeck / B-425 Telasys / B-434 Interstroom / B-440 GPE / B-444 RvdB ICT / B-438 Bleuel / B-433 Bosch / B-435 JPK',
       'records': [by[c] for c in ('B-531', 'B-532', 'B-533', 'B-425', 'B-434', 'B-440', 'B-444', 'B-438', 'B-433', 'B-435')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第12批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 12 批 10 户落盘')
