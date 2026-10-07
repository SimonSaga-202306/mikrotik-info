# -*- coding: utf-8 -*-
"""R66 第 13 波:A-106/A-109/A-112/A-113 四户。"""
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

def rec(code, name, heads, kp, evs, scene, size, sw, risk, email_sal,
        inference='R66 第 13 波具名 KP 金谱', trend='2026-10-08 R66 13 波谱名牌', gap='R66 13 波谱面锁定'):
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 波次二点名**'
    dims = {'业务定位': heads, '产品线与在售品牌': '(波次二补谱面)', '目标行业与场景': scene, '团队与规模': size,
            '决策链与对接人': kb, '技术与认证': '(波次二补)', '采购与供应链信号': '(波次二补)',
            '近期动态与线索': trend, '与我方契合点': '24 口 value PoE 谱链窗口', '风险与注意': risk}
    return {'customer': code, 'fact': name + ':' + heads, 'inference': inference,
            'hypothesis': '24 口 value PoE(' + PRICE + ')具名谱位引路', 'evidence_main': evs[0]['source'],
            'tech': '(波次二补)', 'hr': size, 'contact_found': kb, 'contact_pending': '直发具名需 opt-in',
            'dims': dims, 'evidence': evs, 'followups': fu(),
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': '(待谱面二补)', '③KP 深挖': kb,
                             '④Saga 对标': '24 口 value PoE(' + PRICE + ')', '⑤在乎与偏好': sw[0],
                             '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['直发具名需 opt-in'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': '波次二补', '合作方式': '未知', '缺口证据': '(波次二)'},
                    'gap_proof': gap},
            'kp': [{'name': k[0], 'role': k[1], 'contact': k[2], 'status': k[3], 'source': k[4]} for k in kp],
            'unknowns': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'email': email_sal + '\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-07, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?\n\nBest regards,\nSaga Networks Export Desk'}

def ev(d, q, u):
    return {'dim': d, 'quote': q, 'source': u}

R = []

R.append(rec('A-106', 'DACC Europe Ltd',
    'DACC EUROPE LIMITED(英国 London Docklands,154 Cannon Workshops, 3 Cannon Drive, E14 4AS;公司号 **03297031**;+44 20 7538 8701;dacceurope.com;老牌综合布线/网络基础设施集成商(**FORS & RISQS 批准铁路分部+数据中心分部**;全司 ISO9001+ISO14001;蓝芯片客户谱;147 人(zoominfo 谱)/19 人(GlobalDatabase 件));姊妹 Dacc Europe Mechanical And Electrical Limited/母体 Hutchison Technologies Limited',
    [('Marin Krastev Shkodrov', 'Director+Secretary+PSC(实控人,2014-06 任命;姊妹公司互通人)', 'Companies House 军官名件+Endole PSC 件', O, 'https://find-and-update.company-information.service.gov.uk/company/03297031/officers'),
     ('Jasvinderpal Singh Matharu', 'Director+PSC(Accountant 职;1999-02 首任/2015 退/2019-02 复任)', 'Companies House 军官名件+Endole PSC 件', O, 'https://find-and-update.company-information.service.gov.uk/company/03297031/officers'),
     ('Tony Grace', 'Commercial & Sales Director', 'dacceurope.com Our leadership 官网自署', O, 'https://www.dacceurope.com/'),
     ('David Long', 'Technical Director', 'dacceurope.com Our leadership 官网自署', O, 'https://www.dacceurope.com/'),
     ('Ricky Akers', 'Projects Director', 'dacceurope.com Our leadership 官网自署', O, 'https://www.dacceurope.com/'),
     ('Lee Millar', 'Service Delivery Director', 'dacceurope.com Our leadership 官网自署', O, 'https://www.dacceurope.com/'),
     ('Photis Patsalide', '(原)Director(2022-07~2024-01 已退,留痕)', 'Companies House 军官名件', O, 'https://find-and-update.company-information.service.gov.uk/company/03297031/officers')],
    [ev('决策链与对接人', 'Officers Active: SHKODROV Marin Krastev (Director 2014) / MATHARU Jasvinderpal Singh (Director 2019);Controllers (PSC): Marin Krastev Shkodrov + Jasvinderpal Singh Matharu(Endole)', 'https://open.endole.co.uk/insight/company/03297031-dacc-europe-limited'),
     ev('团队与规模', 'Our leadership: Tony Grace Commercial & Sales Director;David Long Technical Director;Ricky Akers Projects Director;Lee Millar Service Delivery Director(dacceurope.com 官网)', 'https://www.dacceurope.com/'),
     ev('业务定位', 'long-established integrator specialising in structured cabling and associated network infrastructure;FORS & RISQS approved Railway Division;Data Centre Division;ISO9001/ISO14001;147 employees', 'https://www.zoominfo.com/c/dacc-europe-ltd/36557947')],
    '英国伦敦码头区布线/DC 集成商(铁路分部)', '147 人;ISO 双证',
    ('FORS/RISQS 铁路谱+DC 分部', '母体 Hutchison 谱层', 'PSC 双实控+官网四 Director', '大牌布线件链'),
    'PSC 实控+销售/技术/项目/交付四档(opt-in 律)', 'Hi Tony,'))

R.append(rec('A-109', 'RWL Advanced Solutions',
    'RWL Advanced Solutions Ltd(爱尔兰 Dublin,Park West Industrial Park, Unit 15 Park West Road, Dublin 12;英国分支 RWL ADVANCED SOLUTIONS LIMITED(FC 编号 **FC034521**,2017-08 入册);**32 员工;$5M**;谱型=爱尔兰/英国 IT 品牌代表分销(爱尔兰:Brand-Rex/Excel/Panduit/APC/Fluke Networks/Siemon;**英国=Panduit Data Solutions 独家分销商**;药品/科技/金融/教育/医疗垂直谱);rwlas.com;办室 Dublin/London/Amsterdam',
    [('Robert Walsh', 'MANAGING DIRECTOR(2017-08 CH 入册;Sandyford 谱)', 'Companies House 军官名件(FC034521)+uk.rwlas.com 团队页自署', O, 'https://find-and-update.company-information.service.gov.uk/company/FC034521/officers'),
     ('Sean Kirby', 'SALES DIRECTOR(销售总监 KPI 天位)', 'uk.rwlas.com 团队页自署', O, 'https://uk.rwlas.com/the-team/'),
     ('Kevin Quinn', 'FINANCIAL DIRECTOR+CH Secretary(2017-08)', 'Companies House 军官名件+uk.rwlas.com 团队页自署', O, 'https://find-and-update.company-information.service.gov.uk/company/FC034521/officers'),
     ('Scott Smith', 'Channel Director(UK Team)', 'rwlas.com 团队页自署', O, 'https://www.rwlas.com/rwl-meet-the-team/'),
     ('Joe Reilly', 'Sales Manager(UK Team)', 'rwlas.com 团队页自署', O, 'https://www.rwlas.com/rwl-meet-the-team/'),
     ('Micheál Fadden', 'Group Operations Manager', 'RocketReach 谱', G, 'https://rocketreach.co/rwl-advanced-solutions-ltd-management_b453164ffc83cf50'),
     ('Tracy Snell', 'Group Vendor Relationship Manager(厂商关系 KPI 位)', 'RocketReach 谱', G, 'https://rocketreach.co/rwl-advanced-solutions-ltd-management_b453164ffc83cf50'),
     ('Nick Jackson', 'UK Technical Sales Specialist(Cambridge)', 'RocketReach 谱', G, 'https://rocketreach.co/rwl-advanced-solutions-ltd-management_b453164ffc83cf50')],
    [ev('决策链与对接人', 'RWL ADVANCED SOLUTIONS LIMITED (FC034521): QUINN Kevin (Secretary 2017) / WALSH Robert (Director 2017, Irish)', 'https://find-and-update.company-information.service.gov.uk/company/FC034521/officers'),
     ev('团队与规模', 'Directors: ROBERT WALSH MANAGING DIRECTOR;SEAN KIRBY SALES DIRECTOR;KEVIN QUINN FINANCIAL DIRECTOR(uk.rwlas.com 官网团队页)', 'https://uk.rwlas.com/the-team/'),
     ev('团队与规模', 'UK Team: Scott Smith Channel Director;Joe Reilly Sales Manager;Fran Parrish Customer Liaison;Dan Morgan Stores;Adam Curley Internal Sales;Netherlands: Sean DOUGLAS Internal Sales(rwlas.com 官网团队页)', 'https://www.rwlas.com/rwl-meet-the-team/'),
     ev('业务定位', 'In the UK we solely are distributors for Panduit Data Solutions;suppliers: Pharmaceutical, Technology, Financial, Education and Medical;32 employees;$5M', 'https://rocketreach.co/rwl-advanced-solutions-ltd-profile_b453164ffc83cf50')],
    '爱尔兰/英国 IT 品牌分销(Panduit 英国独家)', '32 人;$5M;三国办',
    ('Panduit 独家谱+三国办室', '品牌谱竞位(Panduit/Excel 大牌)', 'MD/SD/FD 官网三金谱', '大牌厂商直供链'),
    'Walsh MD+Kirby 销售+Quinn 财务三金谱(opt-in 律)', 'Hi Robert,'))

R.append(rec('A-112', 'BRS Networks AB',
    'BRS Networks AB(瑞典 Visby(Gotland),Broväg 10 c, 621 40 Visby;Org.nr **556822-1567**(2010-10-28 注册;**BRS Holding AB 集团属**);63 员工-allabolag 谱/官网谱=110+ 员工;SNI 43210 Elinstallationer+62900 IT 业;谱型=瑞典光纤合同一线商(Gotland 四先锋起家;Skåne/Småland/Norrtälje 办室+Estonia/**Germany(Wedemark-Hannover 办)**;光纤规划/熔接/montage/调测/维排+Datacenter/Secura/IT 服务;010-600 5600;info@brsnetworks.se;brsnetworks.com/se',
    [('Lars Bo Johansson', 'Extern verkställande direktör(外部任 VD/CEO,1975 生)', 'allabolag.se 登记册谱', O, 'https://www.allabolag.se/foretag/brs-networks-ab/visby/it-%C3%B6vrigt/2K36B9BI63IHH'),
     ('Marcus Mats Johan Larsson', 'Ordförande(董事长,1977 生)', 'allabolag.se 登记册谱', O, 'https://www.allabolag.se/foretag/brs-networks-ab/visby/it-%C3%B6vrigt/2K36B9BI63IHH'),
     ('Henrik Ringbom', 'Koncern-VD(集团 CEO;Data Centres/Secure Buildings)', 'brsnetworks.se Våra medarbetare 官网自署 henrik.ringbom@brsnetworks.se / 010-600 56 51', O, 'https://brsnetworks.se/vara-medarbetare/'),
     ('Per Jordeglans', 'Marknad- och Försäljningschef(销售与市场经理;Fiber Contracts/Urban Networks/DC)', 'brsnetworks.se 官网自署 per.jordeglans@brsnetworks.se / 010-600 57 01', O, 'https://brsnetworks.se/vara-medarbetare/'),
     ('Seila Jusic', 'IT-Chef(IT 主管,Mälardalen)', 'brsnetworks.se 官网自署', O, 'https://brsnetworks.se/vara-medarbetare/'),
     ('Marcus Eklund', 'Regionchef Gotland / Manager IT-services', 'brsnetworks.se 官网自署 marcus.eklund@brsnetworks.se', O, 'https://brsnetworks.se/vara-medarbetare/'),
     ('Pontus Barck', 'Manager Fibre construction(光纤建设经理)', 'brsnetworks.se 官网自署 pontus.barck@brsnetworks.se', O, 'https://brsnetworks.se/vara-medarbetare/'),
     ('Martin Larsson', 'Responsible for planning Fibre Projects(光纤项目规划)', 'brsnetworks.se 官网自署 martin.larsson@brsnetworks.se', O, 'https://brsnetworks.se/vara-medarbetare/'),
     ('Mihaly Ribar', 'Betriebsleiter(德国办运营主管)', 'brsnetworks.se/international 官网自署 mihaly.ribar@brsnetworks.com', O, 'https://brsnetworks.se/international/'),
     ('Johan Carlström', 'Chief Information Security Officer', 'RocketReach 谱', G, 'https://rocketreach.co/brs-networks-management_b44cf011fd4be6d3'),
     ('Martin Kejval', 'Co-Founder(四先锋之一)', 'RocketReach 谱+官网四先锋后文', G, 'https://rocketreach.co/brs-networks-management_b44cf011fd4be6d3')],
    [ev('决策链与对接人', 'Extern verkställande direktör Lars Bo Johansson (f 1975);Ordförande Marcus Mats Johan Larsson (f 1977);Del av BRS Holding AB;63 anställda(allabolag.se 登记册谱)', 'https://www.allabolag.se/foretag/brs-networks-ab/visby/it-%C3%B6vrigt/2K36B9BI63IHH'),
     ev('团队与规模', 'Ledning: Henrik Ringbom Koncern-VD henrik.ringbom@brsnetworks.se;Per Jordeglans Marknad- och Försäljningschef;Seila Jusic IT-Chef;Marcus Eklund Regionchef Gotland;Marcus Gozzi Regionchef Mälardalen(官网 Våra medarbetare 全员直邮谱)', 'https://brsnetworks.se/vara-medarbetare/'),
     ev('团队与规模', 'BRS International (Germany): Joachim Pettersson Geschäftsführer;Mihaly Ribar Betriebsleiter;Palitha Lisin-Emmerig Projeklassistenz;Katharina Trautwein Projektleitung;Aueweg 2, 30900 Wedemark – Hannover(官网)', 'https://brsnetworks.se/international/'),
     ev('业务定位', 'among the leaders in fibre contracts in Sweden;110 employees;offices Skåne, Småland and Norrtälje as well as Estonia and Germany(brsnetworks.com about-us)', 'https://brsnetworks.com/about-us/')],
    '瑞典光纤合同一线商(德国办)', '63-110 人;2010 创;Gotland 谱',
    ('光纤一线+德国分部+全员直邮谱', '集团(BRS Holding)谱层', 'Koncern-VD/销售/IT 主管官网金谱', '大牌光纤件链'),
    'Ringbom 集团 VD+Jordeglans 销售金谱(opt-in 律)', 'Hej Henrik,'))

R.append(rec('A-113', 'A3 Communications',
    'A3 Communications, Inc.(美国 Irmo(South Carolina);**1990 创(36 年谱)**;130+ 员工/201-500 谱;$5-20M;**2019 被 The Cook & Boardman Group, LLC(全国最大商业门件/五金分销平台)收购**(子公司存续;分支 Raleigh NC 等);谱型=美国一线系统集成商(企业组网/无线/IP 视频监控/门禁/结构化布线/统一通信/虚拟化存储/电气/AV/网安/管服);a3communications.com;(803) 744-xxxx;salesteam@a3communications.com',
    [('Brian Thomas', 'President & CEO(2012 起在位;收购后继续续任 President;2018 起连续六年全国最快成长集成商)', 'Cook & Boardman 官方收购公告具名+(上镜)多源', O, 'https://www.securityinfowatch.com/integrators/dealers-integrators-installing-companies/press-release/21074509/cook-boardman-group-a3-communications-acquired-by-cook-boardman-group'),
     ('Scott Grainger', 'Vice President of Physical Security', 'craft.co 高管谱', G, 'https://craft.co/a3-communications/executives'),
     ('Chad Hendrix', 'Vice President of Infrastructure(基础设施 VP=PoE 谱位)', 'craft.co 高管谱', G, 'https://craft.co/a3-communications/executives'),
     ('Darrin Anderson', 'Chief Executive Officer, The Cook & Boardman Group(母体 CEO;公告引语)', 'C&B 官方收购公告引语', G, 'https://www.securitysales.com/news/a3-communications-acquired-cook-boardman/92390/')],
    [ev('决策链与对接人', 'A3 is led by Brian Thomas, the Company’s President and CEO since 2012;Brian will continue to serve as President of A3 under C&B’s ownership(C&B 官方公告 2019)', 'https://www.securitysales.com/news/a3-communications-acquired-cook-boardman/92390/'),
     ev('团队与规模', 'President, CEO is Brian Thomas;Scott Grainger Vice President of Physical Security;Chad Hendrix Vice President of Infrastructure(craft.co 高管谱);130+ employees', 'https://craft.co/a3-communications/executives'),
     ev('业务定位', 'Founded in 1990, A3 provides a broad range of IT and security solutions:unified communications;virtualization and storage;structured cabling;enterprise networking and wireless;IP video surveillance and access control;network security;201-500 employees', 'https://seamless.ai/b/a3-communications-inc-12913712')],
    '美国 SC 一线系统集成商(C&B 集团子)', '130+ 人;1990 创;C&B 母体',
    ('36 年集成巨头谱+官方公告金谱', '母体平台采购链层', 'Thomas CEO 续任续谱+Infra VP Hendrix', '大牌安防件链'),
    'Brian Thomas 续任 CEO 金谱(opt-in 律)', 'Hi Brian,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第13波.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 13 波:DACC(PSC 双实控+官网四 Director)+RWL(MD/SD/FD 官网三金谱)+BRS(登记册+官网全员直邮谱)+A3(C&B 官方收购公告 Thomas 金谱)四户',
               'scope': 'UK/IE/SE/US 谱;BRS brsnetworks.se 官网全员列名页;RWL uk.rwlas.com 团队页',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 13 波 4 户落盘')
