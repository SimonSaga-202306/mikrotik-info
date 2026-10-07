# -*- coding: utf-8 -*-
"""R66 第 11 波:A-081/A-082/A-092/A-094 四户(kp 直接带结构化列表)。"""
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
        inference='R66 第 11 波具名 KP 金谱', trend='2026-10-08 R66 11 波谱名牌', gap='R66 11 波谱面锁定'):
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

R.append(rec('A-081', 'Profcon AB',
    'Profcon AB(瑞典 Vansbro(Dalarnas län),Fabriksvägen 8, 786 33;1966 创(60 年谱:今=Profcon Electronics AB+Telefrang AB 合并体);17 员工(2024);谱型=I/O 系统/烟气控制/定制电子/工业 PC/平板/加固手持/网通件/RFID/称重;自有牌 SIOX Solutions+OnControl;profcon.se',
    [('Micael Andersson', 'VD(CEO)+董事(受益所有权 25-50%)', 'bolagsfakta.se 登记册谱+DNB Key Principal', O, 'https://www.bolagsfakta.se/5565787024-Profcon_AB'),
     ('Ulf Gladh', 'Styrelseordförande(董事长)+Owner(受益所有权谱)', 'bolagsfakta.se 登记册谱+LinkedIn', O, 'https://www.bolagsfakta.se/5565787024-Profcon_AB'),
     ('Lars-Uno Olsson', '董事+受益所有权人(50-75%)', 'bolagsfakta.se 登记册谱', O, 'https://www.bolagsfakta.se/5565787024-Profcon_AB'),
     ('Lars Olsson', '董事+受益所有权人(50-75%)', 'bolagsfakta.se 登记册谱', O, 'https://www.bolagsfakta.se/5565787024-Profcon_AB'),
     ('Ingegerd Maria Jansson', '受益所有权人(50-75%)', 'bolagsfakta.se 登记册谱', O, 'https://www.bolagsfakta.se/5565787024-Profcon_AB'),
     ('Owe Westerberg', '董事', 'bolagsfakta.se 登记册谱', O, 'https://www.bolagsfakta.se/5565787024-Profcon_AB'),
     ('Anders Jansson', 'Purchaser(采购 KPI 天位)', 'LinkedIn 自署', G, 'https://se.linkedin.com/company/profcon-ab'),
     ('Gennady Hamizevitsch', 'Manager, Procurement(采购二线)', 'zoominfo 谱', G, 'https://www.zoominfo.com/pic/profcon-ab/433716278'),
     ('Lars Lidmarck', 'President & Founder(Profcon Electronics AB 合并前主体)', 'LinkedIn 自署', G, 'https://se.linkedin.com/company/profcon-ab'),
     ('Mats Koponen', 'Software engineering', 'LinkedIn 自署', G, 'https://se.linkedin.com/company/profcon-ab')],
    [ev('决策链与对接人', 'VD för Profcon AB är Micael Andersson och styrelseordförande är Ulf Gladh;Styrelsen: Lars-Uno Olsson/Owe Westerberg/Lars Olsson/Micael Andersson;Verklig huvudman: Ingegerd Maria Jansson/Lars Olsson/Lars-Uno Olsson (50-75%)/Micael Andersson (25-50%)', 'https://www.bolagsfakta.se/5565787024-Profcon_AB'),
     ev('团队与规模', 'Employees: Ulf Gladh Owner;Anders Jansson Purchaser;Mats Koponen Software engineering;Lars Lidmarck President and founder at Profcon Electronics AB;17 anställda (2024)', 'https://se.linkedin.com/company/profcon-ab'),
     ev('业务定位', 'Profcon AB today consists of the merged companies Profcon Electronics AB and Telefrang AB;I/O-Systems/Smoke Control/Industrial computers/Network and communication products;SIOX Solutions and OnControl registered trademarks;founded 1966', 'https://se.linkedin.com/company/profcon-ab')],
    '瑞典工控电子/网通件分销(自有双牌)', '17 人;1966 创;60 年谱',
    ('60 年工控分销+自有牌', '小实体(17 人)', 'Anders Jansson 采购 KPI 直达位', '大牌工控件链竞谱'),
    'VD+董事长登记册金谱+采购双谱(opt-in 律)', 'Hej Micael,'))

R.append(rec('A-082', 'Microstar sp. z o. o',
    'Microstar sp. z o.o.(波兰 Warszawa,Gizów 6, 01-249;+48 22 836 52 73;传真 +48 22 836 53 78;microstar.com.pl 波兰电脑/电子批发档;ATTO Technology 波兰分销名录页具名联系人;排噪:巴西 Microstar(CB Insights,圣保罗维修)/丹麦 Microstar Logistics(美 Keg 物流)/波兰 Agrosimex 肥料 Microstar Complex 均非本体)',
    [('Piotr Pieczerak', '具名联系人(ATTO 分销名录口径;直邮 piotr.pieczerak@microstar.com.pl)', 'atto.com 分销名录页具名+直邮', G, 'https://www.atto.com/microstar-sp-z-o-o/')],
    [ev('决策链与对接人', 'Microstar sp. z o.o., Gizów 6, 01-249 Warsaw, Poland;Tel: +48 22 836-52-73;Email: piotr.pieczerak@microstar.com.pl(ATTO Technology 分销名录页)', 'https://www.atto.com/microstar-sp-z-o-o/'),
     ev('业务定位', 'MICROSTAR — Gizów 6, 01-249 Warszawa(Wola);22 836 52 73;Computers(名录口径一致)', 'https://www.yelp.com/biz/microstar-warszawa'),
     ev('近期动态与线索', '2026-10-08 R66 11 波:身份锁定=华沙 microstar.com.pl 本体(巴西/美同名件排录);波次二=波兰 KRS/CEIDG 登记册按号反查董事层', 'https://ekrs.ms.gov.pl/')],
    '波兰华沙电脑/网通件批发商', '(KRS 谱波次二补)',
    ('具名直邮已获(Pieczerak)', '实体规模谱面薄', 'KRS 登记册反查可破', '同名噪声高'),
    'Pieczerak 具名直邮(leads-only;opt-in 律);KRS 反查点名', 'Hi Piotr,'))

R.append(rec('A-092', 'Titan Security Group',
    'Titan Security Group(美国 Chicago,600 W Jackson Blvd Suite 300 IL 60661;法定名 Titan Prudential Security, LLC;1994 创(家族所有 30 年谱;前身 Prudential Security 1977 起);5K-10K 员工;$2B(zoominfo);谱型=芝加哥最大区安防服务商(人员安防+电子安防系统集成单源双轨;35,000 小时/周执勤;1,000+ 安防员);Quad-C Management 成长投资;**2024-09 与 Marksman Security 战略合并**(全国足迹精品安防商)',
    [('David S. Pack', 'President & CEO(家族企业二代;合并后继续 CEO)', 'PRNewswire 官方合并公告+Quad-C 投资公告引语', O, 'https://www.prnewswire.com/'),
     ('Mark Radi', 'President(合并后高级领导组)', 'PRNewswire 官方合并公告引语', O, 'https://www.prnewswire.com/'),
     ('Zeke Kaufman', 'CAO(合并后高级领导组)', 'PRNewswire 官方合并公告引语', O, 'https://www.prnewswire.com/'),
     ('Ross McCarthy', 'Chief Human Resources Officer', 'zoominfo 谱', G, 'https://www.zoominfo.com/c/titan-security-group/353923263'),
     ('Jason Sikora', 'Chief Revenue Officer', 'zoominfo 谱', G, 'https://www.zoominfo.com/c/titan-security-group/353923263'),
     ('Mark Apel', 'President(分部)', 'zoominfo 谱', G, 'https://www.zoominfo.com/c/titan-security-group/353923263'),
     ('Niko Jones', 'President(分部)', 'zoominfo 谱', G, 'https://www.zoominfo.com/c/titan-security-group/353923263'),
     ('Carlyle Clark', 'Director, Compliance & SOC Operations(Great Lakes)', 'zoominfo 员工目录谱', G, 'https://www.zoominfo.com/pic/titan-security-group/353923263')],
    [ev('近期动态与线索', 'Titan Security Group and Marksman Security Corporation Announce Strategic Merger(2024-09-16):Dave Pack as CEO, Mark Radi as President, and Zeke Kaufman as CAO will comprise the senior leadership team(PRNewswire 官方公告)', 'https://www.securityinfowatch.com/'),
     ev('决策链与对接人', 'David Pack President & CEO;Ross McCarthy CHRO;Jason Sikora CRO;Mark Apel President;Niko Jones President;Abigail Gualberto VP Talent Acquisition;5K-10K employees;$2B', 'https://www.zoominfo.com/c/titan-security-group/353923263'),
     ev('业务定位', 'legal name Titan Prudential Security, LLC;funder Quad-C Management;started 1977 (Prudential);35,000 hours per week;1,000+ security staff;electronic security systems design/implementation/maintenance', 'https://www.crunchbase.com/organization/titan-security-group')],
    '美国芝加哥安防服务巨头(电子集成臂)', '5K-10K 人;$2B;1994 创;Quad-C 持',
    ('电子安防集成臂+全国合并谱', '巨头谱(决策链长;value 档窄位)', 'Pack/Radi/Kaufman 官方公告三金谱', '大牌安防厂商链'),
    '巨头级:走 SOC/合规 Director 层窄口(opt-in 律)', 'Hi Carlyle,'))

R.append(rec('A-094', 'VELOCIgroup ApS',
    'VELOCIgroup ApS(丹麦 Roskilde,Jernbanegade 23B c/o Businesshouse, 4000;2026-10-08 R66 第 11 波:公开面仅 Yelp 地址件锁 Denmark Roskilde 本体(Computers 类);人名谱零命中)',
    [],
    [ev('业务定位', 'VELOCIGROUP — Jernbanegade 23B, c/o Businesshouse, 4000 Roskilde, Denmark(Computers)', 'https://www.yelp.com/biz/velocigroup-roskilde'),
     ev('近期动态与线索', '2026-10-08 R66 11 波:守档;波次二=丹麦 CVR 登记册(virk.dk)按名反查,补董事层+注册号', 'https://virk.dk/'),
     ev('团队与规模', '(CVR 谱波次二补);ApS=丹麦私营有限责任公司形态', 'https://virk.dk/')],
    '丹麦 Roskilde 电脑类 ApS(谱面薄)', '(CVR 谱波次二补)',
    ('CSV 已有谱名+地址锁', '谱面极薄(Yelp 独件)', 'CVR 登记册反查可破', '零人名命中'),
    '守档:身份=Roskilde Jernbanegade 23B 本体已锁;R66 波次二点名(CVR 反查)', '',
    inference='R66 第 11 波守档(谱面薄)', trend='2026-10-08 R66 11 波守档', gap='R66 11 波谱面薄'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第11波.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 11 波:Profcon(SE 登记册双金谱+采购)+Microstar PL(具名直邮)+Titan US(官方合并公告三金谱)+VELOCIgroup(守档)四户',
               'scope': 'SE/PL/US/DK 谱;Microstar 同名噪声排录;Titan=巨头谱窄口;VELOCIgroup CVR 点名',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 11 波 4 户落盘')
