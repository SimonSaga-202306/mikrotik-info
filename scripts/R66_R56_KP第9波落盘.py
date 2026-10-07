# -*- coding: utf-8 -*-
"""R66 第 9 波:A-107/A-108/A-110/A-117 四户(kp 直接带结构化列表)。"""
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
            '近期动态与线索': '2026-10-07 R66 9 波谱名牌', '与我方契合点': '24 口 value PoE 谱链窗口', '风险与注意': risk}
    return {'customer': code, 'fact': name + ':' + heads, 'inference': 'R66 第 9 波具名 KP 金谱',
            'hypothesis': '24 口 value PoE(' + PRICE + ')具名谱位引路', 'evidence_main': evs[0]['source'],
            'tech': '(波次二补)', 'hr': size, 'contact_found': kb, 'contact_pending': '直发具名需 opt-in',
            'dims': dims, 'evidence': evs, 'followups': fu(),
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': '(待谱面二补)', '③KP 深挖': kb,
                             '④Saga 对标': '24 口 value PoE(' + PRICE + ')', '⑤在乎与偏好': sw[0],
                             '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['直发具名需 opt-in'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': '波次二补', '合作方式': '未知', '缺口证据': '(波次二)'},
                    'gap_proof': 'R66 9 波谱面锁定'},
            'kp': [{'name': k[0], 'role': k[1], 'contact': k[2], 'status': k[3], 'source': k[4]} for k in kp],
            'unknowns': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'email': email_sal + '\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-07, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?\n\nBest regards,\nSaga Networks Export Desk'}

def ev(d, q, u):
    return {'dim': d, 'quote': q, 'source': u}

R = []

R.append(rec('A-107', 'Esotec Ltd',
    'Esotec Ltd(英国 Sunbury-on-Thames,Security House The Summit, Hanworth Road TW16 5DB;公司号 10074925;2016-03 注册;谱型=CCTV/安防系统集成商(政府/历史建筑/高端客户威胁评估+turn-key 设计安装支持;esotec.co.uk;11-50 人;$38.66M(D&B);2024-2025 董事层密集换血)',
    [('Peter Schieser', 'Director(2025-04 任命;德国籍·卢森堡居;Key Principal 谱)', 'Companies House 军官名件+D&B Key Principal', O, 'https://find-and-update.company-information.service.gov.uk/company/10074925/officers'),
     ('Craig Flanagan', 'Director(2024-07 任命)', 'Companies House 军官名件', O, 'https://find-and-update.company-information.service.gov.uk/company/10074925/officers'),
     ('Michele Bennett', 'Director(2025-07 任命)', 'Companies House 军官名件', O, 'https://find-and-update.company-information.service.gov.uk/company/10074925/officers')],
    [ev('决策链与对接人', 'ESOTEC LTD. Officers: BENNETT Michele (Director appointed 25 July 2025) / FLANAGAN Craig (24 July 2024) / SCHIESER Peter (4 April 2025, German, Luxembourg)', 'https://find-and-update.company-information.service.gov.uk/company/10074925/officers'),
     ev('决策链与对接人', 'Key Principal: Peter Schieser;ESOTEC LTD. Sunbury-on-Thames TW16 5DB;Revenue $38.66M', 'https://www.dnb.com/business-directory/company-profiles.esotec_ltd.dcb8b1dd43268f43d3cf0006c1217184.html'),
     ev('业务定位', 'esotec is a trusted systems integrator specializing in advanced surveillance and security capabilities ... government entities and historic sites;over 35,000 employees daily', 'https://www.zoominfo.com/c/esotec/507396295')],
    '英国政要/历史建筑安防系统集成商', '11-50 人;$38.66M;2016 注册',
    ('政府/历史资产集成商谱', '2025 董事层换血(谱位需复验)', 'Schieser Key Principal+双董事', '大牌安防厂商链'),
    '董事层 2025 换血(谱位复核;opt-in 律)', 'Hi Peter,'))

R.append(rec('A-108', 'Road Tech Computer Systems Ltd',
    'ROAD TECH COMPUTER SYSTEMS LIMITED(英国 Watford,First Floor Radius House, 51 Clarendon Road WD17 1HP(注册)+Shenley Hall, Rectory Lane, Shenley WD7 9AN(军官通信);公司号 02017435;1986-05 创(40 年谱);SIC 58290 软件出版;谱型=英国公路货运/物流 IT 服务市场领导者(软件+硬件全面方案;roadrunner.uk.com / roadtech.co.uk;01923 460000);Road Tech Holdings Ltd 100% 股东;67-69 人;£20k 资本',
    [('Adrian Paul Barrett', 'Director(2017-12 起)', 'Companies House 军官名件', O, 'https://find-and-update.company-information.service.gov.uk/company/02017435/officers'),
     ('Bernadette Beevor', 'Director+Company Secretary(1992 起秘书;创始家族谱)', 'Companies House 军官名件', O, 'https://find-and-update.company-information.service.gov.uk/company/02017435/officers'),
     ('David Monahan', 'Director/General Manager(2024-09 任命;General Manager 职衔)', 'Companies House 军官名件', O, 'https://find-and-update.company-information.service.gov.uk/company/02017435/officers'),
     ('Tony Paul Jeffree', 'Director(2017-12 起)', 'Companies House 军官名件', O, 'https://find-and-update.company-information.service.gov.uk/company/02017435/officers'),
     ('Philip David Thornhill', 'Director(2017-12 起)', 'Companies House 军官名件', O, 'https://find-and-update.company-information.service.gov.uk/company/02017435/officers'),
     ('Diane Alice Dooling', 'Director(2017-12 起)', 'Companies House 军官名件', O, 'https://find-and-update.company-information.service.gov.uk/company/02017435/officers'),
     ('Tony Burton', 'Infrastructure And Support Engineer(@roadtech.co.uk)', 'GlobalDatabase 谱面', G, 'https://uk.globaldatabase.com/company/road-tech-computer-systems-limited'),
     ('Fergus Ewen', 'IT Engineer(@roadtech.co.uk)', 'GlobalDatabase 谱面', G, 'https://uk.globaldatabase.com/company/road-tech-computer-systems-limited')],
    [ev('决策链与对接人', 'ROAD TECH COMPUTER SYSTEMS LIMITED Officers Active: BARRETT Adrian Paul / BEEVOR Bernadette / DOOLING Diane Alice / JEFFREE Tony Paul / MONAHAN David (Occupation: General Manager, appointed 25 September 2024) / THORNHILL Philip David', 'https://find-and-update.company-information.service.gov.uk/company/02017435/officers'),
     ev('业务定位', 'Road Tech are the market-leaders in IT services for the haulage and logistics sectors, providing a comprehensive range of software and hardware solutions to the industry', 'https://www.companiesintheuk.co.uk/ltd/road-tech-computer-systems'),
     ev('团队与规模', 'Tony Burton Infrastructure And Support Engineer @roadtech.co.uk · Fergus Ewen IT Engineer;currently 67 employees', 'https://uk.globaldatabase.com/company/road-tech-computer-systems-limited')],
    '英国公路货运/物流 IT 市场领导者(软件+硬件)', '67-69 人;1986 创;40 年谱',
    ('物流 IT 市场 领导者+40 年谱', 'Holding 100% 持股(集团决策链)', 'General Manager Monahan 新任命=实干位', '大牌厂商链'),
    '六董事+GM 谱位(opt-in 律)', 'Hi David,'))

R.append(rec('A-110', 'Senseco Systems Ltd',
    'SENSECO SYSTEMS LIMITED(英国 Gillingham;公司号 06840964;2009-03 创(团队 25 年谱);英国首家碳中和认证 fire&security 公司;Fire and Security Holdings Ltd 母公司子;2024-04 营业额 £13.3M;102 员工;净资产 £5M;谱型=fire detection/gaseous suppression/安防设计供应安装调试维护一体化)',
    [('Stephen Thomas', 'Director(2009-03 创位)+CEO(Senseco Systems Group/Fire & Security Holdings)', 'Companies House 军官名件+LinkedIn/集团页', O, 'https://pomanda.com/company/06840964/senseco-systems-limited'),
     ('Michael Duhan', 'Director(2010-11)+COO', 'Companies House 军官名件+集团 LinkedIn 谱', O, 'https://pomanda.com/company/06840964/senseco-systems-limited'),
     ('Lee Thompson', 'Director(2020-11)+Chief Revenue Officer/Group Director of Strategic Development', 'Companies House 军官名件+集团 LinkedIn 谱', O, 'https://pomanda.com/company/06840964/senseco-systems-limited'),
     ('Steve Butler', 'Director(2023-06)+CFO', 'Companies House 军官名件+theorg C 谱', O, 'https://pomanda.com/company/06840964/senseco-systems-limited'),
     ('George Whittaker', 'Director(2019-12)', 'Companies House 军官名件', O, 'https://pomanda.com/company/06840964/senseco-systems-limited'),
     ('Lawrence Yeo', 'Managing Director', 'theorg C 谱', G, 'https://theorg.com/org/senseco-systems'),
     ('Jamie Anderson', 'Chief Commercial Officer (CCO)', 'theorg C 谱', G, 'https://theorg.com/org/senseco-systems'),
     ('James Plumb', 'Head of Security(Snodland)', 'RocketReach 谱', G, 'https://rocketreach.co/senseco-systems-limited-profile_b5ee7977f42e75ea'),
     ('Georgie Cazaly', 'Head Of Service(Gillingham)', 'RocketReach 谱', G, 'https://rocketreach.co/senseco-systems-limited-profile_b5ee7977f42e75ea')],
    [ev('决策链与对接人', 'Directors: Stephen Thomas (Mar 2009) / Michael Duhan (Nov 2010) / George Whittaker (Dec 2019) / Lee Thompson (Nov 2020) / Steve Butler (Jun 2023);parent Fire & Security Holdings Limited', 'https://pomanda.com/company/06840964/senseco-systems-limited'),
     ev('决策链与对接人', 'Steve Thomas CEO at Senseco Systems Group/Fire and Security Holdings Ltd;Michael Duhan COO;Lee Thompson Group Director of Strategic Development', 'https://uk.linkedin.com/company/fire-and-security-holdings-limited'),
     ev('团队与规模', 'James Plumb Head of Security · Georgie Cazaly Head Of Service;102 employees · £13.3M turnover (April 2024)', 'https://rocketreach.co/senseco-systems-limited-profile_b5ee7977f42e75ea')],
    '英国首家碳中和 fire&security 一体化商', '102 人;£13.3M(2024);2009 创',
    ('碳中和首创+集团持家', '并购整合中(北部收购待定)', 'CEO/COO/CFO/CRO 四 C 实名', '大牌消防件链'),
    '集团 C 谱+并购扩张(opt-in 律)', 'Hi Steve,'))

R.append(rec('A-117', 'Griffon Security Technologies, LLC',
    'Griffon Security Technologies LLC(美国 Kennebunk, Maine;14 Fletcher St / 5 Fletcher St(2017 两件购入 $1.1M);2002 创(Timothy Barrett 地下室起家;Anchor Light Properties LLC 三线所有权);19 员工;$4.2M;谱型=南缅因安防系统集成商(视频监控/门禁/资产人员追踪/通讯;医院病人追踪/温度监控;工程+安装+项目+技术+维保全链;griffonsecurity.com)',
    [('Timothy Barrett', 'Founder / Principal / President(2002 创位;兼 Phoenix Welding Principal/COO)', 'mainebiz 公开受访+konaequity 谱+LinkedIn', G, 'https://www.mainebiz.biz/article/security-companys-growth-warrants-two-moves-in-under-a-year-in-downtown-kennebunk'),
     ('David Douin', 'Principal(联合所有权 2011 加入;CPA;原 Principal & CFO)', 'mainebiz 公开受访+LinkedIn/zoominfo 谱', G, 'https://www.mainebiz.biz/article/security-companys-growth-warrants-two-moves-in-under-a-year-in-downtown-kennebunk'),
     ('T.J. Tigerman', 'General Manager(关键员工)', 'LinkedIn+zoominfo+datanyze 三源', G, 'https://www.linkedin.com/company/griffon-security'),
     ('Jenn Louf', 'Purchasing Coordinator(硬件采购 KPI 天位)', 'datanyze 谱', G, 'https://www.datanyze.com/companies/griffon-security-technologies/347172761'),
     ('Sean Perkins', 'Manager, Information Technology', 'LinkedIn+datanyze 双源', G, 'https://www.datanyze.com/companies/griffon-security-technologies/347172761'),
     ('Mark Fréchette', 'Manager, Engineering & Technical Services', 'datanyze 谱+LinkedIn', G, 'https://www.datanyze.com/companies/griffon-security-technologies/347172761')],
    [ev('决策链与对接人', 'founder and President Timothy Barrett ... in 2002 I started Griffon Security;David Douin took on as business partner in 2011 (CPA);principals Timothy Barrett and David Douin ... Anchor Light Properties LLC', 'https://www.mainebiz.biz/article/security-companys-growth-warrants-two-moves-in-under-a-year-in-downtown-kennebunk'),
     ev('决策链与对接人', 'T.J. Tigerman General Manager;Sean Perkins IT Manager;Timothy Barrett Founder/Principal/President;David Douin Principal', 'https://www.linkedin.com/company/griffon-security'),
     ev('团队与规模', 'Executives: Timothy Barrett President;T.J. Tigerman General Manager;Jenn Louf Purchasing Coordinator;Sean Perkins IT;Mark Fréchette Engineering;19 employees · $4.2M revenue', 'https://www.datanyze.com/companies/griffon-security-technologies/347172761')],
    '美国南缅因安防系统集成商(医院谱)', '19 人;$4.2M;2002 创',
    ('创办人直达+2 件地产扩张谱', '小体量谱(19 人)', 'Jenn Louf 采购协调 KPI 天位', '大牌安防件链'),
    'Barrett/Douin 业主+Louf 采购(opt-in 律)', 'Hi T.J.,'))

with open('batch/A类深挖_2026-10-07_R66_R56_KP第9波.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-07',
               'wave': 'R66 第 9 波:Esotec+Roadtech+Senseco+Griffon 四户(英 CH 军官名件+美缅因谱)',
               'scope': 'UK CH 10074925/02017435/06840964 + US ME Griffon;公司型名薄 KP 队列 154 优先段',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 9 波 4 户落盘')
