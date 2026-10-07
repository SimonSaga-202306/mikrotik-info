# -*- coding: utf-8 -*-
"""R66 第 5-6 波:英国登记册七户(A-056/057/099/100/103/104/105)具名 KP 落盘。"""
import json

PRICE = '$180 USD EXW (2026-10-07, 15天有效)'

def fu():
    return [
        {'stage': '第 1 次跟进 · 具名 kp 引路口', 'push': 'STC-424XGGPM-280W',
         'angle': '具名 kp 引路 → 采购/技术硬件分载线', 'question': '贵司 24 口 PoE 交换机的硬件采购线由哪位同事主责？',
         'proof': '规格页'},
        {'stage': '第 2 次跟进 · 一页目录卡', 'push': '一页目录卡', 'angle': '价值层 PoE 谱链卡', 'question': '可否入谱链名录？', 'proof': '卡'},
        {'stage': '第 3 次跟进 · 留档+LinkedIn 谱', 'push': '—', 'angle': '谱链明智途径', 'question': '—', 'proof': '—'},
    ]

def rec(code, name, heads, kp_block, evs, dims_extra, sw, email_sal):
    dims = {
        '业务定位': heads, '产品线与在售品牌': dims_extra.get('lineup', '(谱面待 R66 波次二补)'),
        '目标行业与场景': dims_extra.get('scene', '英国 IT/电信谱面'), '团队与规模': dims_extra.get('size', '(谱面待补)'),
        '决策链与对接人': kp_block, '技术与认证': dims_extra.get('tech', '(谱面待补)'),
        '采购与供应链信号': dims_extra.get('supply', '(谱面待补)'), '近期动态与线索': dims_extra.get('news', '2026-10-07 R66 波次点名'),
        '与我方契合点': dims_extra.get('fit', '24 口 value PoE 谱链窗口'), '风险与注意': dims_extra.get('risk', '具名 kp 直发需 opt-in'),
    }
    return {'customer': code, 'fact': name + '(英国;' + heads + ')',
            'inference': 'R66 5-6 波:英国登记册(Companies House)/官网/LinkedIn 具名 KP 金谱',
            'hypothesis': '24 口 value PoE 谱链窗口=(' + PRICE + ')具名谱位引路',
            'evidence_main': evs[0]['source'], 'tech': dims_extra.get('tech', '(谱面待二补)'),
            'hr': dims_extra.get('size', '(谱面待补)'), 'contact_found': kp_block,
            'contact_pending': dims_extra.get('pending', '具名 kp 直发邮箱=R66 波次二/LinkedIn opt-in'),
            'dims': dims, 'evidence': evs, 'followups': fu(),
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': dims_extra.get('lineup', '(待谱面二补)'),
                             '③KP 深挖': kp_block, '④Saga 对标': '24 口 value PoE(' + PRICE + ')',
                             '⑤在乎与偏好': sw[0], '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['具名 kp 直发需 opt-in 手序'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': 'R66 波次二补谱', '合作方式': '未知', '缺口证据': '(谱面待说明)'},
                    'gap_proof': 'R66 波次谱面锁定'},
            'unknowns': dims_extra.get('unk', ['具名 kp 直发邮箱(opt-in)', '硬件采购线在职者']),
            'email': email_sal +
            '\n\nI came across ' + name + ' while mapping UK network and IT suppliers. Behind every deployment sits a switching layer that has to stay cheap, PoE-healthy and well documented.\n\n'
            'We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: ' + PRICE + ', a value unit that rides along with each deployment.\n\n'
            'Could you point me to the colleague who carries the hardware purchasing line, so we route the right spec to the right desk?\n\n'
            'Best regards,\nSaga Networks Export Desk'}

R = []
CH = 'Companies House 免费军官名单(official-self-published 级金谱);'

R.append(rec('A-056', 'AA JONES ELECTRIC LIMITED',
    'AA JONES ELECTRIC LIMITED(赫尔 Hull,Unit H, Subway Street, HU3 4EL;公司号 03212967;1996-06-17 注册(30 年);曾用名 JONES ELECTRICAL SUPPLY CO. LIMITED(1996-2010);ACTIVE 谱面',
    '**Anthony Owen Moore = Director(2009-01-29 任命,1948-03 生,原 PSC 至 2023-11)+ Andrew Moulds = Director(2009-01-29 任命)+ Jill Samantha Lomax = Director(2025-01-08 新任命);历史:Neil David Jennings/Ian Andrew Wayman(均 2024-12-13 辞任,Wayman 原 PSC)+ Howard Mark Jones(2009 辞;' + CH + 'Hull 电气批发 30 年谱面**',
    [
        {'dim': '决策链与对接人', 'quote': 'LOMAX, Jill Samantha — Director, Appointed 8 January 2025;MOORE, Anthony Owen — Director, Appointed 29 January 2009 (born March 1948);MOULDS, Andrew — Director Appointed 29 January 2009', 'source': 'https://find-and-update.company-information.service.gov.uk/company/03212967/officers'},
        {'dim': '业务定位', 'quote': 'AA JONES ELECTRIC LIMITED · Company number 03212967 · Unit H, Subway Street, Hull HU3 4EL · Active · Incorporated 17 June 1996 · Previous name JONES ELECTRICAL SUPPLY CO. LIMITED (1996-2010)', 'source': 'https://find-and-update.company-information.service.gov.uk/company/03212967'},
        {'dim': '决策链与对接人', 'quote': 'Persons with significant control: Mr Anthony Owen Moore (ceased 23 November 2023);Mr Ian Andrew Wayman (ceased) —— 家族/老班移交谱谱面', 'source': 'https://find-and-update.company-information.service.gov.uk/company/03212967/persons-with-significant-control'},
    ],
    {'lineup': '电气批发/网络线材谱面(MikroTik 谱库内信号)', 'size': '小实体 Hull 30 年谱', 'tech': '(电气件为主)', 'supply': 'Hull 口电气批发',
     'risk': '家族老班移交(2024-12 双辞任+2025 Lomax 新任命=谱面交替期,新任命 Lomax=天位)', 'pending': 'Jill Samantha Lomax 谱位=R66 首击位(opt-in 律)',
     'unk': ['Lomax 新任命的硬件线职责', 'MikroTik 谱面份额']},
    ('30 年 Hull 电气批发+2025 新任命 Lomax', '老班家族移交期间谱面频变', 'Lomax 新任命位', '大牌电气件'),
    'Hi Jill,'))

R.append(rec('A-057', 'System Devices UK Ltd',
    'System Devices UK Ltd(英国 Manor Park/Runcorn(LinkedIn 口径);1983 创(43 年!);2005 管理层收购(MBO)后由 System Devices Ltd 转为 UK Ltd;**Opto 22 英国唯一授权经销商**(OptoCertified Trainer);工业自动化/控制/机器人谱面,近年扩 Mecademic 高精度工业机器人谱;能源监测谱面',
    '**Martin Stewart = Owner(领英自署 Owner,原 IT Manager 2000-2005,Crewe & Alsager College;2005 MBO 班底)+ Ian Rennell = Director(2012 至今,原财务总监 2005-2010+公司秘书 2010-2012,Royal Naval Reserves 退役;RocketReach 谱)——LinkedIn/RocketReach 双谱实名金谱;43 年 Opto 22 独家谱面**',
    [
        {'dim': '决策链与对接人', 'quote': 'Martin Stewart — Owner, System Devices UK Ltd(LinkedIn;Experience: Owner;IT Manager May 2000 - Aug 2005;Computer Programmer British Airways 1990-1994)', 'source': 'https://www.linkedin.com/in/martin-stewart-b3a9616/'},
        {'dim': '决策链与对接人', 'quote': 'Ian Rennell — Director @ System Devices UK Ltd 2012 - now;Company Secretary 2010-2012;Financial Director 2005-2010;Royal Naval Reserves (Retired)', 'source': 'https://rocketreach.co/ian-rennell-email_37924345'},
        {'dim': '业务定位', 'quote': 'Founded in 1983 ... System Devices Ltd became System Devices UK Ltd following a management buyout in 2005 ... UK only authorised OPTO 22 distributor ... Mecademic partnership', 'source': 'https://systemdevices.co.uk/our-story/'},
    ],
    {'lineup': 'Opto 22 全谱(英国独家)+Mecademic 机器人;工业自动化/能源监测', 'size': '1-10 人(Lusha 口径);43 年谱', 'tech': 'Opto 22 独家授权+OptoCertified Trainer', 'supply': 'Opto 22 英国独家经销口',
     'risk': 'MBO 完班/Martin Stewart 直拿硬件线(43 年谱)', 'pending': 'Martin Stewart Owner 谱位(opt-in 律)',
     'unk': ['MikroTik 谱面信号来源(库档信号)', '自动化工序谱面交换机需求']},
    ('43 年 Opto 22 英国独家+MBO 完班', '小实体 1-10 人', '工业谱面的现场交换件', '大牌(Octo 22 独家)'),
    'Hi Martin,'))

R.append(rec('A-099', 'MSI WORKS LTD',
    'MSI WORKS LTD(伦敦 3rd Floor, 86-90 Paul Street, EC2A 4NE;公司号 15643579;2024-04-13 注册新实体(2 年谱);私有有限责任公司 ACTIVE',
    '**David James Salisbury = Managing Director(2024-12-30 任命,官方谱面)+ John Robert Dente = Director(2024-04-13 任命,1962-10 生)+ John Paul Hubbard = Director(2024-12-30 任命,1988-12 生);' + CH + '新实体谱面(2 年谱),管理 MD 与双 Director 三员全实名**',
    [
        {'dim': '决策链与对接人', 'quote': 'SALISBURY, David James — Director · Occupation: Managing Director · Appointed 30 December 2024;DENTE, John Robert — Director Appointed 13 April 2024 (born October 1962);HUBBARD, John Paul — Director Appointed 30 December 2024 (born December 1988)', 'source': 'https://find-and-update.company-information.service.gov.uk/company/15643579/officers'},
        {'dim': '业务定位', 'quote': 'MSI WORKS LTD · Company number 15643579 · 3rd Floor, 86-90 Paul Street, London EC2A 4NE · Incorporated 2024-04 · Private limited Company · 3 officers / 0 resignations', 'source': 'https://find-and-update.company-information.service.gov.uk/company/15643579'},
        {'dim': '近期动态与线索', 'quote': '2026-10-07 R66 波次:2 年谱新实体;2024-12 MD Salisbury 上任=谱面定型期', 'source': 'https://find-and-update.company-information.service.gov.uk/company/15643579/officers'},
    ],
    {'lineup': '(新实体谱面待 R66 波次二;MikroTik 库档信号)', 'size': '2024 新实体', 'tech': '(谱面待补)', 'supply': '(谱面待补)',
     'risk': '2 年谱新实体;管理 MD Salisbury=首击位(opt-in 律)', 'pending': 'David James Salisbury MD 谱位(opt-in 律)',
     'unk': ['新实体谱面全谱(波次二)', 'MikroTik 谱面份证']},
    ('新实体 MD+双 Director 三员实名', '2 年谱新实体', 'MD Salisbury 直达位', '新实体谱面未定型'),
    'Hi David,'))

R.append(rec('A-100', 'NETWORKOLOGY LTD',
    'NETWORKOLOGY LTD(威尔特郡 Unit 11 Forest Gate, Chippenham SN15 3RS(2025-04 由 Calne 迁址);公司号 08680414;2013-09-06 注册;网络安全/IP 网络建筑咨询谱面(Defence 方向为主,ADS Group 会员;ISO27001:2022+Cyber Essentials/Cyber Essentials PLUS);客户=Defence/Government/Finance/Energy/Maritime/IoT/Oil&Gas',
    '**James Douglas Morgan = Director(2018-04 任命,ADS Group 官网姓谱 James Morgan)** + David John Owen = Director(2018,DnB Key Principal 双源)+ Stefan Nicholas Wallington = Director(2019)+ Stuart Andrew Monteith = Director(2024-10)+ Robert Kevin Jelley = Director(2024-10);5 实名董事/全员 40-50 代;' + CH + 'Defence 网络咨询谱面**',
    [
        {'dim': '决策链与对接人', 'quote': 'JELLEY, Robert Kevin / MONTEITH, Stuart Andrew / MORGAN, James Douglas / OWEN, David John / WALLINGTON, Stefan Nicholas —— 五员 Active Director(2013-2024 任命链)', 'source': 'https://find-and-update.company-information.service.gov.uk/company/08680414/officers'},
        {'dim': '决策链与对接人', 'quote': 'ADS Group member: James Morgan —— Director(官网联系人页谱);ISO27001:2022/Cyber Essentials/Cyber Essentials PLUS', 'source': 'https://www.adsgroup.org.uk/members/networkology-ltd-1/'},
        {'dim': '业务定位', 'quote': 'NETWORKOLOGY LTD · 08680414 · HARTHAM PARK CORSHAM SN13 0RP → Unit 11 Forest Gate Chippenham SN15 3RS(2025-04 迁址);Defence/government/public-sector 网络+安全建筑咨询', 'source': 'https://open.endole.co.uk/insight/company/08680414-networkology-ltd'},
    ],
    {'lineup': 'Cyber/IP 网络建筑(Defence 方向);ADS Group 会员', 'size': '5 董事小实体;2013 创', 'tech': 'ISO27001:2022;Cyber Essentials PLUS', 'supply': '咨询谱面(Defence/Gov)',
     'risk': '咨询实体不接硬谱面;James Morgan ADS 姓谱=opt-in 天位', 'pending': 'James Douglas Morgan 谱位(ADS Group 姓谱;opt-in 律)',
     'unk': ['Defence 方向交换机采用件(受限谱)', 'MikroTik 库档信号来源']},
    ('Defence 网络咨询5董事+ISO27001', '咨询实体硬谱面受体受限', '工业/Defence 受限场谱的价值层', '大牌集成商锁谱'),
    'Hi James,'))

R.append(rec('A-103', 'Bechtle direct Ltd(UK)',
    'Bechtle direct Ltd(英国 HQ:Village Green Methuen Park, Chippenham SN14 0GF;**Bechtle AG(德国 DAX 上市 IT 批发集团)英国子**;1997 创(29 年);4 办(Chippenham/London/Manchester/Northampton);模式=面向企业/个人的互联网邮购电脑与配件直卖(Bechtle 集团 E-commerce 臂)+2023-03 收购 Tangible Benefit(Tim Trotman 固守期过渡);集团 70+ 点/14 国;Year £101m+ turnround CRN 2022 Reseller of the Year 谱面',
    '**James Napp = Managing Director Bechtle direct UK(bechtle.com 官网自曝,official-self-published 级金谱)+ Konstantin Ebert = Executive VP France/Benelux/UK Bechtle AG(集团层谱)+ Tim Trotman = Tangible Benefit 创始人(固守期过渡)+ Nicholas Barrett + Stuart Wohlman(Tangible Benefit 高管留任)——英国子谱面+集团层双谱面实名金谱**',
    [
        {'dim': '决策链与对接人', 'quote': 'Bechtle Limited ... James Napp — Managing Director;Founded in: 1997;4 offices(Chippenham, London, Manchester, Northampton)', 'source': 'https://www.bechtle.com/pt/a-bechtle/a-empresa/filiais/bechtle-direct-UK'},
        {'dim': '决策链与对接人', 'quote': 'James Napp, Managing Director, Bechtle direct UK:"I am excited to work with ... Tangible Benefit";says Konstantin Ebert, Executive Vice President for France, Benelux and the UK, Bechtle AG', 'source': 'https://www.tangiblebenefit.com/bechtle-acquisition-bechtle-on-track-to-become-one-of-the-top-10-it-solutions-providers-in-the-uk/'},
        {'dim': '业务定位', 'quote': 'Bechtle direct Ltd operates as a mail order company, sells computers and accessories via the internet to business and individual consumers in the UK and western Europe', 'source': 'https://www.bloomberg.com/profile/company/1749840Z:LN'},
    ],
    {'lineup': 'IT 全谱面邮购(Bechtle 集团 E-commerce 臂);MikroTik 库档信号', 'size': 'Bechtle 集团 70+ 点/14 国;英国 4 办/£101m+', 'tech': 'Bechtle AG 集团谱/CRN 2022 Reseller of the Year', 'supply': '集团供应链巨型谱面',
     'risk': '集团谱面大/MikroTik 在 Bechtle 谱面占比低;James Napp MD=opt-in 但集团层难直达',
     'pending': 'James Napp MD 谱位(官网金谱;opt-in 律)',
     'unk': ['英国子层采购线主责(谱面大层级)', 'MikroTik 谱面实份']},
    ('Bechtle 集团英国 MD 官网金谱', '集团大层级难直达', 'value PoE 邮购谱面片', '集团大牌谱面'),
    'Hi James,'))

R.append(rec('A-104', 'Centerprise International Limited',
    'CENTERPRISE INTERNATIONAL LIMITED(贝辛斯托克 Hampshire International Business Park, RG24 8GQ;公司号 01738519;42 年谱(1983 谱面);公共部门 specialist+system building;51-100 人(Crunchbase);CI Group 谱面(Jon Atherton CI Group Director)',
    '**Rafi Arif Abdul Razzak = Founder & Chairman(1991-01 任命 35 年在位,Crunchbase 谱 Founder/Chairman)+ Jez Nash (Jeremy Shane Nash) = CEO/Director of Sales(2016)+ Rebecca Razzak = Director(1991)+ Samantha Louise Lailey = HR & Support Director(2012)+ Sharon Ann Allen = Finance Director(2012,兼 Secretary)+ Peter Fearn/Andrew John Finney/Michael Geoffrey Keegan = Directors(2017-18)+ Michael Jonathan Elliott = Director(2021)+ Marc Allen Woosnam + John Richard Collyer = 2024 新任 Directors + Jon Atherton = CI Group Director(Crunchbase)+ Duncan Templeton = Director — 12 实名董事全谱金谱**',
    [
        {'dim': '决策链与对接人', 'quote': 'Rafi Razzak: Founder and Chairman;Jez Nash(Jeremy Nash): CEO/Director of Sales;Sharon Allen: Finance Director;Samantha Lailey: Human Resources & Support Director;Jon Atherton: CI Group Director;Duncan Templeton: Director', 'source': 'https://www.crunchbase.com/organization/centerprise-international'},
        {'dim': '决策链与对接人', 'quote': '12 current directors incl. Rafi Arif Abdul Razzak(1991)/Rebecca Razzak(1991)/Samantha Louise Lailey(2012)/Sharon Ann Allen(2012)/Jeremy Shane Nash(2016)/Peter Fearn(2017)/Andrew John Finney(2017)/Michael Geoffrey Keegan(2018)/Michael Jonathan Elliott(2021)/Marc Allen Woosnam(2024)/John Richard Collyer(2024)', 'source': 'https://www.companycheck.co.uk/company/01738519/CENTERPRISE-INTERNATIONAL-LIMITED/companies-house-data'},
        {'dim': '业务定位', 'quote': 'Centerprise International specialises in public sector services and system building, delivering IT solutions;51-100 employees', 'source': 'https://www.crunchbase.com/organization/centerprise-international'},
    ],
    {'lineup': '公共部门 IT 方案+system building;MikroTik 库档信号', 'size': '51-100 人;1983 谱', 'tech': '公共部门 specialist', 'supply': '公共部门谱面+CI Group 谱',
     'risk': 'Rafi Razzak 35 年在位 Founder/Chairman=直达位;公共部门采购节奏菌', 'pending': 'Rafi Arif Abdul Razzak 谱位(35 年在位 Founder;opt-in 律)',
     'unk': ['公共部门谱面交换机采购线', 'MikroTik 谱面实份']},
    ('35 年在位 Founder+12 董事全谱', '公共部门采购节奏菌', 'Rafi Razzak 直达位', '公共部门大牌'),
    'Hi Rafi,'))

R.append(rec('A-105', 'Cisilion Ltd',
    'Cisilion Ltd(萨里 Leatherhead,CISILION HOUSE, Guildford Road, KT22 9UT;2000 由 Roger Paul 创立;185 员工(2026-08);$26.1M 营收(RocketReach);谱面=IT 网络/安全/云/数据中心服务(Cisco/Microsoft/Dell 合作谱),Next-gen IT infrastructure;五年目标 £100M turnover(Nick Paul 2025-02 说话)',
    '**Roger Paul = Founder/Owner & Chairman(2000 创立,Crunchbase+Tracxn 双源金谱)+ Nick Paul(Nicholas Paul) = CEO(RocketReach/Tracxn/Owler 三源,+44 7843 27XXXX/+44 20 7220 XXXX 谱位)+ Nicola Jane Orford = CEO(Tracxn 谱双 CEO 面,波次二点名)+ Rob Quickenden = CTO(Crunchbase)+ Paul Johnson = Account Director — 家族式 CEO 谱面+CTO 谱面实名金谱**',
    [
        {'dim': '决策链与对接人', 'quote': 'Roger Paul: Founder;Nicola Jane Orford: CEO;Nicholas Paul: CEO(Tracxn 2026-09 谱面)', 'source': 'https://tracxn.com/d/companies/cisilion/__zLNxi1SOPObkXy_ubzhmfoICMSFYdVG7ty6Cd9-8kv4'},
        {'dim': '决策链与对接人', 'quote': 'Roger Paul: Owner and Chairman;Rob Quickenden: Chief Technology Officer;Paul Johnson: Account Director;Cisilion founded 2000;Nick Paul is the CEO(acc. RocketReach 2026)', 'source': 'https://www.crunchbase.com/organization/cisilion'},
        {'dim': '业务定位', 'quote': '185 employees(2026-08);$26.1M revenue;Registered CISILION HOUSE, GUILDFORD ROAD, LEATHERHEAD, SURREY, KT22 9UT;Cisco/Microsoft/Dell 合作谱;next 2 years £100M turnover 目标(Nick Paul 2025-02)', 'source': 'https://tracxn.com/d/companies/cisilion/__zLNxi1SOPObkXy_ubzhmfoICMSFYdVG7ty6Cd9-8kv4'},
    ],
    {'lineup': 'IT 网络/安全/云/Datacenter 服务;Cisco/Microsoft/Dell 谱面;MikroTik 库档信号', 'size': '185 人;$26.1M', 'tech': 'Cisco/Microsoft/Dell 巨头合作谱', 'supply': '集成谱面(大企业客户)',
     'risk': '家族 Paul 谱面/CEO+CTO 实名金谱;MikroTik 谱面份额未定证', 'pending': 'Nick Paul CEO 谱位(opt-in 律);£100M 目标期的价值层谱',
     'unk': ['MikroTik 谱面实份', '硬件采购线 Account Director 链']},
    ('Founder+CEO+CTO 家族谱面金谱', '185 人集成谱面硬谱面占比低', '£100M 目标期的价值层谱', 'Cisco/Microsoft 大牌锁谱'),
    'Hi Nick,'))

out = {'date': '2026-10-07', 'wave': 'R66 第 5-6 波:英国 Companies House 登记册七户具名 KP 突入',
       'scope': 'A-056/057/099/100/103/104/105 英国 Ltd 军官名单+官网/LinkedIn/Crunchbase 金谱',
       'records': R}
json.dump(out, open('batch/A类深挖_2026-10-07_R66_R56_KP第5_6波.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('R66 第 5-6 波', len(R), '户落盘')
