# -*- coding: utf-8 -*-
"""R66 B 面 KP 波 3:B-221/B-313/B-343/B-359 四户(kp 直接带结构化列表)。"""
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
        inference='R66 B 面 KP 波 3 具名金谱', trend='2026-10-08 R66-B 波 3 谱名牌', gap='R66-B 波 3 谱面锁定'):
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 波次二点名**'
    dims = {'业务定位': heads, '产品线与在售品牌': '(波次二补谱面)', '目标行业与场景': scene, '团队与规模': size,
            '决策链与对接人': kb, '技术与认证': '(波次二补)', '采购与供应链信号': '(波次二补)',
            '近期动态与线索': trend, '与我方契合点': '24 口 value PoE 谱链窗口', '风险与注意': risk}
    dimensions = {'背景深描': heads, '芯片与在用型号': '(待谱面二补)', '关键人KP': kb,
                  '关注点与资质': sw[0],
                  '优缺点SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3],
                  'Saga产品适配': '24 口 value PoE(' + PRICE + '):' + scene + ';' + risk}
    facts = [{'dim': e['dim'], 'text': e['quote'], 'quote': e['quote'], 'url': e['source']} for e in evs]
    swot_text = ('- **S**:%s\n- **W**:%s\n- **O**:%s\n- **T**:%s' % sw)
    return {'code': code, 'researched_on': '2026-10-08(R66-B 波 1)',
            'fact': name + ':' + heads, 'inference': inference,
            'hypothesis': '24 口 value PoE(' + PRICE + ')具名谱位引路', 'evidence_main': evs[0]['source'],
            'tech': '(波次二补)', 'hr': size, 'contact_found': kb, 'contact_pending': '直发具名需 opt-in',
            'dims': dims, 'dimensions': dimensions, 'evidence': evs, 'facts': facts,
            'followups': fu(), 'swot_text': swot_text, 'unknowns56': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': '(待谱面二补)', '③KP 深挖': kb,
                             '④Saga 对标': '24 口 value PoE(' + PRICE + ')', '⑤在乎与偏好': sw[0],
                             '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['直发具名需 opt-in'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': '波次二补', '合作方式': '未知', '缺口证据': '(波次二)'},
                    'gap_proof': gap},
            'kp': [{'name': k[0], 'role': k[1], 'contact': k[2], 'status': k[3], 'source': k[4]} for k in kp],
            'unknowns': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'email_subject': 'PoE switching for your line',
            'email': email_sal + '\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-07, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?\n\nBest regards,\nSaga Networks Export Desk'}

def ev(d, q, u):
    return {'dim': d, 'quote': q, 'source': u}

R = []

R.append(rec('B-221', 'GCOM',
    'GCOM(格鲁吉亚 Tbilisi;gcom.ge;info@gcom.ge;CSV 域锚=gcom.ge;2026-10-08 R66-B 波 3:美国 GCOM Software, LLC(GovTech,Kamal Bherwani,Georgia WIC 平合件)=异名已排;格鲁吉亚在地谱面命中 Zaza Zviadadze(LinkedIn:Experience GCOM/Tbilisi/Georgian Technical University/500+ 连接)为最大公开谱',
    [('Zaza Zviadadze', '员工/管理层(LinkedIn 谱 GCOM/Tbilisi;波次二其职衔待核)', 'LinkedIn 自署 worksFor GCOM(Tbilisi)', G, 'https://www.linkedin.com/in/zaza-zviadadze-249160109/')],
    [ev('决策链与对接人', 'Zaza Zviadadze — Experience: GCOM;Education: Georgian Technical University;Location: Tbilisi(LinkedIn 谱)', 'https://www.linkedin.com/in/zaza-zviadadze-249160109/'),
     ev('业务定位', 'GCOM Software, LLC(GovTech,11,882 followers,Kamal Bherwani)=美国异名件,排噪', 'https://www.linkedin.com/posts/riyaz-ladkhan-5b94293_a-modern-scalable-platform-for-georgia-wic-activity-7011495956604936192-V8tJ'),
     ev('近期动态与线索', '2026-10-08 R66-B 波 3:域锚 gcom.ge;守档半位;波次二=格鲁吉亚公共登记(napr.gov.ge)按名反查+Zviadadze 职衔核', 'https://napr.gov.ge/')],
    '格鲁吉亚 Tbilisi 网络渠道商(gcom.ge)', '(napr 谱波次二补)',
    ('在地具名谱(Zviadadze)已获', '谱面薄', 'napr 登记册反查可破', '异名噪声高'),
    'Zviadadze 谱位(opt-in 律);napr 反查点名', ''))

R.append(rec('B-313', 'Dipol Connect SRL',
    'DIPOL CONNECT SRL(罗马尼亚 București Sector 2,Strada Fabrica De Gheata Nr. 8(行政)/Strada Saltului Nr. 19(注册);**CUI 26051890**;J40/9512/2009;EUID ROONRC.J40/9512/2009;**2009-10-01 创(17 年)**;CAEN 4652 电子/电信件批发;**2025:7 员工/营收 8,185,582 RON(+9.7%)/净利 301,178 RON**;1 独东+1 管理员结构;安防目录页标「firmă de pază:instalare, întreținere 许可」;0314281005',
    [('Nicolau Cristin', 'Administrator(管理员;罗马尼亚安防企业名册件具名)', 'protectiesipaza.ro 名册件具名(administrată de)', G, 'https://www.protectiesipaza.ro/firme-de-paza/dipol-connect-s-r-l-protectie-si-paza/'),
     ('Iulia Diaconu', 'Sales Procurement(**2018-10 起在职 7 年;采购 KPI 天位**;Universitatea Tehnică Iași)', 'LinkedIn 自署 Sales Procurement @ Dipol Connect SRL', G, 'https://www.linkedin.com/in/iulia-diaconu-07a91b47/')],
    [ev('决策链与对接人', 'Dipol Connect S.R.L. administrată de Nicolau Cristin;București Sectorul 2;instalare, întreținere(罗马尼亚安防企业名册件)', 'https://www.protectiesipaza.ro/firme-de-paza/dipol-connect-s-r-l-protectie-si-paza/'),
     ev('决策链与对接人', 'Iulia Diaconu — Sales Procurement, Dipol Connect SRL(Oct 2018 – Present, 7 years;Bucharest;Universitatea Tehnică „Gheorghe Asachi” din Iași)', 'https://www.linkedin.com/in/iulia-diaconu-07a91b47/'),
     ev('团队与规模', 'CUI 26051890;7 angajați (2025);Cifra de afaceri 8.185.582 RON (+9,74%);Profit net 301.178 RON;17 ani din 2009;1 asociat unic+1 administrator(termene.ro 登记册件)', 'https://termene.ro/firma/26051890-DIPOL-CONNECT-SRL')],
    '罗马尼亚布加勒斯特电子件批发+安防安装', '7 人;8.19M RON(2025)',
    ('采购 Diaconu 在职 7 年直达位', '小实体(1 东 1 管)', 'Cristin 管理员名册件', '大牌件链竞谱'),
    'Cristin 管理员+Diaconu 采购(opt-in 律)', 'Bună ziua Iulia,'))

R.append(rec('B-343', 'Distrigo Inc',
    'Distrigo Inc(美国;sales@distrigoinc.com;CSV 域锚=distrigoinc.com;2026-10-08 R66-B 波 3:**Stellantis DISTRIGO(Stellantis 多品牌汽车件分销网,148 hubs+289 Relay;2023 起并 Fiat/Jeep/Alfa Romeo 等 14 牌;distrigoparts.co.uk/Stellantis 官方稿)=异名已排**;distrigoinc.com 本体公开谱面薄,人名零命中)',
    [],
    [ev('业务定位', 'Distrigo is STELLANTIS multi-brand spare parts distribution network;148 DISTRIGO hubs and 289 DISTRIGO Relay(Stellantis 官方稿,异名排噪)', 'https://www.media.stellantis.com/uk-en/corporate/press/stellantis-announces-new-expanded-distrigo-parts-distribution-structure-in-europe'),
     ev('业务定位', 'Distrigo Parts Distribution(Tracxn 谱,66 employees,2013)=欧洲件,与 distrigoinc.com 异体排噪', 'https://tracxn.com/d/companies/distrigo-parts-distribution/__LwtAQ2SsHZIMYQwrC3jvoc5hoZJf84XjkTX2DtnmOZc'),
     ev('近期动态与线索', '2026-10-08 R66-B 波 3:守档排噪;波次二=distrigoinc.com 官网谱面+州务卿注册反查', 'https://distrigoinc.com/')],
    '美国 Distrigo Inc(身份待锁)', '(未锁定)',
    ('CSV 域锚已获', '实体身份未锁定', '官网谱面+州注册反查可破', 'Stellantis 同名噪声重'),
    '守档:Stellantis 件排录;R66 波次二点名(官网谱面+州注册)', '',
    inference='R66 B 面 KP 波 3 守档(身份未锁)', trend='2026-10-08 R66-B 波 3 守档', gap='R66-B 波 3 身份未锁'))

R.append(rec('B-359', 'Leverify LLC',
    'Leverify LLC(美国 Bellevue/Redmond WA,2331 130TH Ave NE Ste 110A Bellevue 98005 + 6825 176TH Ave NE Ste 135A Redmond 98052;**DBA=Stockyfy(stockyfy.com)**;leverify.com / brands@leverify.com;谱型=**电子产品批发分销商(consumer electronics wholesale;101-250 人;altostrat 列 MikroTik Reseller 谱)**;排噪:getleverify.com(德州 Austin BPO 客服外包,Matt Gandy)=异名已排',
    [('Raza Ul-Mustafa', 'Founder / Key Principal / Member(创办位+主负责人)', 'Crunchbase founders 件+DNB Key Principal 双源谱', G, 'https://www.crunchbase.com/organization/leverify-707f')],
    [ev('决策链与对接人', 'Leverify LLC — founders: Raza Ul-Mustafa;AKA Stockyfy;Bellevue, Washington;101-250;electronics wholesale distributor(Crunchbase 件)', 'https://www.crunchbase.com/organization/leverify-707f'),
     ev('决策链与对接人', 'Key Principal: Raza Ul-Mustafa;Raza Ul-Mustafa Member;Leverify LLC Doing Business As: Stockyfy(DNB 件)', 'https://www.dnb.com/business-directory/company-profiles.leverify_llc.93e834f722a9ec18d8ea9dc618bd9237.html'),
     ev('业务定位', 'an electronics wholesale distributor providing exceptional partner experiences to resellers and businesses;stockyfy.com;2331 130TH Ave NE Ste 110A Bellevue WA', 'https://www.dnb.com/business-directory/company-profiles.leverify_llc.3be4dd7729ac1958030a358ec6fefb27.html')],
    '美国 WA 电子产品批发分销(MikroTik 经销商谱)', '101-250 人;Stockyfy 牌',
    ('电子批发分销+品牌线 brands@', 'DNB 谱面带核(直发须核)', 'Ul-Mustafa 创办位直达', '大牌厂商链竞谱'),
    'Ul-Mustafa 创办位(opt-in 律);brands@ 谱位复合', 'Hi Raza,'))

with open('batch/B类深挖_2026-10-08_R66_BKP波3.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 B 面 KP 波 3:GCOM(格鲁吉亚 Zviadadze 谱)+Dipol Connect(RO 管理员+采购 7 年)+Distrigo(Stellantis 排噪)+Leverify(WA Stockyfy Ul-Mustafa)四户',
               'scope': 'GE/RO/US 谱;GCOM/Distrigo/Leverify 异名排录;乌克兰守界不动',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 B 面 KP 波 3 四户落盘')
