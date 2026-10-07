# -*- coding: utf-8 -*-
"""R66 第 14 波:A-114/A-115/A-116/A-118 四户。"""
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
        inference='R66 第 14 波具名 KP 金谱', trend='2026-10-08 R66 14 波谱名牌', gap='R66 14 波谱面锁定'):
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

R.append(rec('A-114', 'Amplitel Technologies',
    'Amplitel Technologies LLC(美国 Kaukauna, Wisconsin,240 W Wisconsin Ave, 54130;+1 920-759-4773;ampliteltech.com;**2007 创(19 年)**;12 员工;$22.1M;谱型=威斯康星 SMB IT 支持/托管服务商(外包 IT 支持+安全聚焦;Appleton/Green Bay 区谱)',
    [('Aaron Lahm', 'CEO(创位 Owner 谱;ampliteltech.com 官网客户证言页署名)', 'ampliteltech.com 官网自署 "Aaron Lahm, CEO"+contactout Owner 谱', O, 'https://ampliteltech.com/'),
     ('Benjamin Boehnlein', 'Vice President', 'zoominfo/RR 双源谱', G, 'https://www.zoominfo.com/pic/amplitel-technologies-llc/346204193'),
     ('Nathan Lahm', 'Senior Account & vCIO Engineer(家族谱)', 'zoominfo 谱', G, 'https://www.zoominfo.com/pic/amplitel-technologies-llc/346204193'),
     ('Chris Glasheen', 'Accounts Manager', 'zoominfo/contactout 双源谱', G, 'https://www.zoominfo.com/pic/amplitel-technologies-llc/346204193'),
     ('Matthew Nolan', 'Technical Engineer', 'zoominfo/RR/contactout 三源谱', G, 'https://www.zoominfo.com/pic/amplitel-technologies-llc/346204193')],
    [ev('决策链与对接人', 'Aaron Lahm, CEO, Amplitel Technologies LLC("Serving Wisconsin Businesses" 官网证言署名);Founded 2007;Kaukauna WI', 'https://ampliteltech.com/'),
     ev('团队与规模', 'Key employees: Benjamin Boehnlein Vice President;Nathan Lahm Senior Account & vCIO Engineer;Chris Glasheen Accounts Manager;Matthew Nolan Technical Engineer;11-50 employees', 'https://www.zoominfo.com/pic/amplitel-technologies-llc/346204193'),
     ev('团队与规模', 'Staff: Aaron Lahm Owner;Chris Glasheen Accounts Manager;Jerad Siewert Data Cabling Technician;Matthew Nolan Technical Engineer;9 employees;$22.1M revenue', 'https://contactout.com/company/Amplitel-Technologies-20142')],
    '美国 WI SMB IT 支持/MSP', '12 人;$22.1M;2007 创',
    ('CEO 官网自署直达', '小实体谱', 'Lahm 家族双位+vCIO 谱', '大牌厂商链竞谱'),
    'A. Lahm CEO/B. Boehnlein VP 谱位(opt-in 律)', 'Hi Aaron,'))

R.append(rec('A-115', 'BCL Enterprises, Inc',
    'BCL Enterprises, inc(美国 Liberty Township, Ohio,5796 Treeside Dr;**dba BCL IT Consulting**;**1993 创(33 年;women-owned 女性拥有经营技术设计-建造公司)**;谱型=Technology Design/Engineering/Build 公司(低压布线/光纤/网络/无线/蜂窝天线 DAS/AV 系统/物理安防;Access Control+监控系统专营;Procore 谱:Telephone Specialties/Commissioning/Technology Design and Engineering);排噪:BCL Enterprises Ltd(印度 Balaji Commercial;金融)+Bloomberg 1985 home builder=异名已排',
    [('Martin Crabill', '业主线/主负责人(Alignable 公司页具名)', 'alignable.com BCL Enterprises Inc dba BCL IT Consulting 页具名', G, 'https://www.alignable.com/middletown-oh/bcl-enterprises-inc-dba-bcl-it-consulting')],
    [ev('决策链与对接人', 'BCL Enterprises Inc dba BCL IT Consulting — Martin Crabill(Alignable 公司页);Technology Design Build Company;founded 1993', 'https://www.alignable.com/middletown-oh/bcl-enterprises-inc-dba-bcl-it-consulting'),
     ev('业务定位', 'Technology Design, Engineering and Build Firm;Low voltage cable infrastructure, fiber, network, wireless, cellular antenna systems, audiovisual systems, and physical security;5796 Treeside Dr, Liberty Township, OH', 'https://www.procore.com/network/p/bcl-enterprises-inc-liberty-township'),
     ev('业务定位', 'woman owned and operated technology design build company;Network design, Network Cabling, Security Access Control, Surveillance cameras or DAS(Alignable 推存件)', 'https://www.alignable.com/middletown-oh/bcl-enterprises-inc-dba-bcl-it-consulting')],
    '美国 OH 女性拥有技术设计建造商(低压/安防)', '1993 创;小实体',
    ('women-owned 33 年谱+低压/DAS/安防全链', '谱面薄(Alignable 独件)', 'Crabill 业主谱位', '大牌件链竞谱'),
    'Crabill 业主谱(opt-in 律);Alignable 独件带核', 'Hi Martin,'))

R.append(rec('A-116', 'Gemellaro Systems Integration (GSI)',
    'Gemellaro Systems Integration®(美国 Troy(Southeast Michigan),1055 W Square Lake Rd, 48098;+1 248-585-5535;securityandnetworks.com;**DBA=WILTECH TECHNOLOGIES(DNB 件)**;63 员工(RR 谱;signalhire 500-1000 异文);$38.9M(RR 谱；prospeo $5.4M 异文);谱型=网络基础设施+物理安防双层集成商(Ford Network Services 大客户账户谱;CAD/设计工程/管服 RC DD/DCDC/ESS 认证谱)',
    [('Marc J Gemellaro', 'Key Principal(创办家族名位)', 'DNB Key Principal 谱', G, 'https://www.dnb.com/business-directory/company-profiles.gemellaro_systems_integration_inc.987bd81e4b2588fb4bf7ca76ab2a8756.html'),
     ('Mike Newman', 'Owner & Vice President', 'RR/prospeo/signalhire 三源谱', G, 'https://rocketreach.co/gemellaro-systems-integration-profile_b551e6a5f9826f72'),
     ('Sharon Pfeiffer Gemellaro', 'Chief Financial Officer(家族谱)', 'RocketReach 谱', G, 'https://rocketreach.co/gemellaro-systems-integration-profile_b551e6a5f9826f72'),
     ('Charles Cassavoy', 'Director – Ford Network Services Account(大客户账户 KPI 位)', 'signalhire/prospeo 双源谱', G, 'https://www.signalhire.com/companies/gemellaro-systems-integration'),
     ('James J. Miller', 'Director of CAD Operations', 'RR/prospeo/getprospect 三源谱', G, 'https://rocketreach.co/gemellaro-systems-integration-profile_b551e6a5f9826f72'),
     ('Andrew H. Krull', 'Director of Operational Systems', 'RR/prospeo 双源谱', G, 'https://rocketreach.co/gemellaro-systems-integration-profile_b551e6a5f9826f72'),
     ('Ron McPherson', 'Director of Design And Engineering', 'signalhire/prospeo 双源谱', G, 'https://www.signalhire.com/companies/gemellaro-systems-integration'),
     ('Bill Ferguson', 'Security and Network Technician', 'signalhire/getprospect 双源谱', G, 'https://getprospect.com/business-directory/gemellaro-systems-integration')],
    [ev('决策链与对接人', 'Key Principal: Marc J Gemellaro;Gemellaro Systems Integration, Inc. Doing Business As: WILTECH TECHNOLOGIES(DNB 件)', 'https://www.dnb.com/business-directory/company-profiles.gemellaro_systems_integration_inc.987bd81e4b2588fb4bf7ca76ab2a8756.html'),
     ev('团队与规模', 'Mike Newman Owner & VP;Sharon Pfeiffer Gemellaro CFO;James Miller Director CAD Operations;Andrew Krull Director Operational Systems;Charles Cassavoy Director Ford Network Services Account;63 employees;$38.9M', 'https://rocketreach.co/gemellaro-systems-integration-profile_b551e6a5f9826f72'),
     ev('业务定位', 'GSI brings together high-level expertise in network infrastructure and physical security;1055 W Square Lake Rd, Troy MI 48098;Ingredient: Ford Network Services Directorship 谱', 'https://www.signalhire.com/companies/gemellaro-systems-integration')],
    '美国 MI 网络+安防双层集成商(Ford 账户谱)', '63 人;$38.9M',
    ('Gemellaro 家族+Ford 大客户账户', '谱件异文(规模/营收)', 'Newman(Owner/VP)+Cassavoy(Ford 账户)双位', '大牌安防件链'),
    '家族+四 Director 谱位(opt-in 律)', 'Hi Mike,'))

R.append(rec('A-118', 'Heartland Business Systems',
    'Heartland Business Systems, LLC(HBS;美国;hbs.net;**被 GenNx360 Capital Partners 收购**(成长型PE);Avastone Technologies 资产合并(单源 consulting/design/delivery 形);501-1000 人(leadiq 652;RR 544/787 联系人);$72M(leadenear 谱);谱型=美国中大 IT 综合商(SLED WI/MI/AZ 政府教育谱+管服/方案架构/vCIO/CISO 全链)',
    [('Jimmy Buddenberg', 'Chief Executive Officer(现位)', 'Crunchbase+RocketReach 双源谱', G, 'https://www.crunchbase.com/organization/heartland-business-systems'),
     ('Peter Helander', 'Founder and President(创位;官方合并公告引语 "says Peter Helander, Principal at Heartland Business Systems")', 'Avastone 合并官方公告引语+Crunchbase', O, 'https://www.crunchbase.com/organization/heartland-business-systems'),
     ('Kevin Carr', 'Co-Founder & Chief Executive Officer(共同创位;leadenear 谱)', 'leadnear 谱', G, 'https://www.leadnear.com/company/us/heartland-business-systems'),
     ('Chad Gustafson', 'Chief Information Officer(Strategic Technologist)', 'leadnear 谱', G, 'https://www.leadnear.com/company/us/heartland-business-systems'),
     ('Ben Turner', 'Chief Operating Officer', 'leadnear 谱', G, 'https://www.leadnear.com/company/us/heartland-business-systems'),
     ('Pieter Lesterhuis', 'Chief Financial Officer', 'leadnear 谱', G, 'https://www.leadnear.com/company/us/heartland-business-systems'),
     ('Steve Kjenner', 'Chief Information Security Officer', 'leadnear 谱', G, 'https://www.leadnear.com/company/us/heartland-business-systems'),
     ('Ryan Keele', 'Vice President of Managed Services(管服 VP=PoE 谱位)', 'RocketReach 谱', G, 'https://rocketreach.co/heartland-business-systems-profile_b5c106b3f42e0882'),
     ('Troy Day', 'Vice President Finance', 'RocketReach+leadiq 双源谱', G, 'https://rocketreach.co/heartland-business-systems-profile_b5e74d56f42e5aa8')],
    [ev('决策链与对接人', 'Jimmy Buddenberg CEO;Peter Helander Founder and President;acquired by GenNx360 Capital Partners;merger of Avastone Technologies(Crunchbase 件)', 'https://www.crunchbase.com/organization/heartland-business-systems'),
     ev('团队与规模', 'Kevin Carr Co-Founder & CEO;Chad Gustafson CIO;Ben Turner COO;Pieter Lesterhuis CFO;Steve Kjenner CISO;Tracy Presteen CHRO;~300 employees;$72M', 'https://www.leadnear.com/company/us/heartland-business-systems'),
     ev('团队与规模', 'Jimmy Buddenberg CEO;Ryan Keele VP Managed Services;Chris Thurman VP;Troy Day VP Finance;544 employees(RR 谱)', 'https://rocketreach.co/heartland-business-systems-profile_b5e74d56f42e5aa8')],
    '美国中大 IT 综合商(SLED 谱+GenNx360)', '544-652 人;$72M',
    ('SLED 政府教育谱+PE 收购资金谱', '巨头谱(CEO 层异文:Carr/Buddenberg/Schmidt,谱位需复核)', '管服 VP Keele=PoE 落位', '大牌厂商链'),
    'CEO 层异文需复核(PE 收购后谱位);Keele 管服 VP 窄口(opt-in 律)', 'Hi Ryan,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第14波.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 14 波:Amplitel(官网 CEO 自署)+BCL(OH women-owned)+GSI(Gemellaro 家族+Ford 账户)+HBS(GenNx360 PE+CEO 层异文复核)四户',
               'scope': 'US 谱(WI/OH/MI/SC);BCL 印/建筑排噪;HBS CEO 层 Carr/Buddenberg/Schmidt 三源异文留痕',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 14 波 4 户落盘')
