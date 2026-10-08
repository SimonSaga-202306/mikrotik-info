# -*- coding: utf-8 -*-
"""R66 第 19 波(50 户扩招批=新波幅标准):DE12(A-174~186 跳 178)+IT29(189~219 跳 188/196/205)+ES/NL/AT3/CH2/PL2。"""
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
        inference='R66 第 19 波具名 KP 金谱', trend='2026-10-08 R66 19 波谱名牌', gap='R66 19 波谱面锁定'):
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 第 19 波点名(谱面无实名)**'
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

# ============ DE×12(A-174~186 skip A-178) ============
R.append(rec('A-174', 'PKE Deutschland GmbH – Niederlassung Berlin',
    'PKE Deutschland GmbH – Niederlassung Berlin(柏林支铺;**2026-06 SYSDACOM GmbH 并入谱**;**2026-08 Prokura 群全退=权杖换代窗;2026-03 双 GF Bauer+Geier 新到位,Behrends 退**;登记公告连串=活档大年)',
    [('Bauer', 'Geschäftsführer(2026-03 新到位;登记公告)',
      '登记公告谱 2026-03(姓氏谱;待核全名)', G, 'https://www.northdata.com/'),
     ('Geier', 'Geschäftsführer(2026-03 双 GF 次位)', '登记公告谱 2026-03(姓氏谱)', G, 'https://www.northdata.com/'),
     ('Ehresmann-George', '并购后管理层谱(SYSDACOM 并入谱面)', '2026-06 并入公告谱', G, 'https://www.northdata.com/'),
     ('Behrends', '原 Geschäftsführer(退位留痕)', '登记公告(留痕)', G, 'https://www.northdata.com/')],
    [ev('决策链与对接人', '2026-08: Prokura 群退;2026-03: Geschäftsführer Bauer + Geier neu;nicht mehr GF: Behrends;2026-06: Verschmelzung mit SYSDACOM GmbH(登记公告连串谱)', 'https://www.northdata.com/'),
     ev('联系方式与基础画像', 'PKE Deutschland GmbH, Niederlassung Berlin;柏林支铺;Meldedaten + Kopierdienst 谱(UD media 件)', 'https://www.udmedia.de/')],
    '德国柏林支铺+SYSDACOM 并入的通信工程谱', '支铺谱;2026 换血年',
    ('并购换血窗 2026=变服窗', '支铺层级谱', 'Bauer/Geier 新 GF 庆贺位', '大牌件链竞谱'),
    'Bauer/Geier 履新贺(姓氏谱全名待核;opt-in 律)', 'Guten Tag Herr Bauer,'))

R.append(rec('A-175', 'prego services GmbH',
    'prego services GmbH(德国萨尔州 Saarbrücken;**HRB 11703 AG Saarbrücken;183 人/$23.3M**;IT 服务+人员外派(Arbeitnehmerüberlassung)谱;**2025-03 GF Mayerbacher 独任,Tzschoppe-Kölling 退**;Kapper Einkauf 采购位 KPI)',
    [('Mayerbacher', 'Geschäftsführer(2025-03 起独任;登记谱)', '登记公告谱(姓氏谱;待核全名)', G, 'https://www.northdata.com/'),
     ('Kapper', 'Einkauf(采购主管=落位 KPI)', '公司 LinkedIn 员工谱', G, 'https://www.linkedin.com/'),
     ('Jennert', 'Business Development(商务开发)', '公司 LinkedIn 员工谱', G, 'https://www.linkedin.com/'),
     ('Alles', 'Chief IT Architect(总架)', '公司 LinkedIn 员工谱', G, 'https://www.linkedin.com/'),
     ('Tzschoppe-Kölling', '原 Geschäftsführer(退位留痕)', '登记公告(留痕)', G, 'https://www.northdata.com/')],
    [ev('决策链与对接人', 'HRB 11703 Saarbrücken;03/2025: Geschäftsführer Mayerbacher(独任);nicht mehr: Tzschoppe-Kölling(登记公告件)', 'https://www.northdata.com/'),
     ev('团队与规模', '183 employees;$23.3M revenue;Kapper Einkauf;Jennert BD;Alles Chief IT Architect;Lieb(员工谱条)', 'https://www.linkedin.com/')],
    '德国萨尔州 183 人 IT 服务+外派屋', '183 人;$23.3M',
    ('Kapper 采购位直击', '外派型谱', 'Mayerbacher 独任直达位', '大厂链竞谱'),
    'Mayerbacher 独任+Kapper 采购(opt-in 律)', 'Guten Tag Herr Mayerbacher,'))

R.append(rec('A-176', 'Prinzing Elektrotechnik GmbH',
    'Prinzing Elektrotechnik GmbH(德国萨尔茨堡 Salach(格平根县);**HRB 533483 AG Ulm;600 人/€95M** = 主谱(档案名全对位);**副谱对位:Prinzing 谱 Aalen HRB 730890(GF Gruber+Riha)=同姓异体已分层**;电气安装+工业工程总包谱)',
    [('Volker Prinzing', 'Geschäftsführer(Salach 主谱;600 人谱主)', '登记/谱面件', G, 'https://www.northdata.com/'),
     ('Gruber', 'Geschäftsführer(Aalen 异体副谱;HRB 730890)', '登记公告(异体分层留痕)', G, 'https://www.northdata.com/'),
     ('Riha', 'Geschäftsführer(Aalen 异体副谱)', '登记公告(异体分层留痕)', G, 'https://www.northdata.com/')],
    [ev('决策链与对接人', 'Prinzing Elektrotechnik GmbH, Salach;HRB 533483 Ulm;GF Volker Prinzing;600 Mitarbeiter;~95 Mio. Euro Umsatz(登记/规模谱)', 'https://www.northdata.com/'),
     ev('联系方式与基础画像', '双异体对位:Aalen 谱 HRB 730890 GF Gruber+Riha(同姓分层,档案名 Elektrotechnik 全对位 Salach 主谱)', 'https://www.northdata.com/')],
    '德国巴符 600 人电气工程屋(工业安装总包)', '600 人;€95M',
    ('大型安装总包=PoE 谱链大户', '大实体谱', 'Volker Prinzing 直达位', '自家链栈谱'),
    'Volker Prinzing 直达(opt-in 律;Aalen 异体已分层)', 'Guten Tag Herr Prinzing,'))

R.append(rec('A-177', 'RECOS SYSTEM SOLUTIONS GmbH',
    'RECOS SYSTEM SOLUTIONS GmbH(德国;**HRB 204230;2013 创(RECOS Richtmann&Eder 母体子谱)**;**GF 换代:Neu(创期)→Fuhrmann+Alp(现职)**;**Ingram Micro APC Edge 伙伴谱=边缘机柜/电源件链谱**)',
    [('Fuhrmann', 'Geschäftsführer(现职;换代接棒)', '登记公告谱(姓氏)', G, 'https://www.northdata.com/'),
     ('Alp', 'Geschäftsführer(现职双位)', '登记公告谱(姓氏)', G, 'https://www.northdata.com/'),
     ('Neu', '原 Geschäftsführer(创期谱;退位留痕)', '登记公告(留痕)', G, 'https://www.northdata.com/')],
    [ev('决策链与对接人', 'HRB 204230;gegründet 2013(RECOS Richtmann&Eder 子谱);Geschäftsführer: Fuhrmann + Alp(neu);nicht mehr: Neu(登记件)', 'https://www.northdata.com/'),
     ev('技术与认证', 'Ingram Micro APC by Schneider Electric Edge 伙伴谱(边缘机房/微 DC 件链)', 'https://www.ingrammicro.de/')],
    '德国 2013 创系统方案子谱(APC Edge 件链)', '子谱实体',
    ('APC Edge 谱=边缘机柜配套窗', '中小实体谱', 'Fuhrmann/Alp 新 GF 直达位', '一线链竞谱'),
    'Fuhrmann/Alp 直达(opt-in 律)', 'Guten Tag Herr Fuhrmann,'))

# skip A-178 Selos
R.append(rec('A-179', 'Sittig Technologies GmbH',
    'Sittig Technologies GmbH(德国 Nürnberg(纽伦堡);**HRB 43590**;**PAXGuide Cloud 机场公共广播(PA)全球谱**——机场播报系统一件套房;GF 双人谱 Johannes+Thomas Sittig;州府(Bayern)官方件引语;Ingrid Sittig 退位留痕)',
    [('Johannes Sittig', 'Geschäftsführer(州府件官方引语=O)', '巴伐利亚州府件+northdata 双源', O, 'https://www.northdata.com/'),
     ('Thomas Sittig', 'Geschäftsführer(双位谱)', '登记谱', G, 'https://www.northdata.com/'),
     ('Tischler', '管理层谱(项目/交付线)', '员工/谱面件', G, 'https://www.linkedin.com/'),
     ('Ingrid Sittig', '原 Geschäftsführerin(退位留痕)', '登记公告(留痕)', G, 'https://www.northdata.com/')],
    [ev('决策链与对接人', 'HRB 43590 Nürnberg;Geschäftsführung: Johannes Sittig + Thomas Sittig;nicht mehr: Ingrid Sittig;州府件 Johannes Sittig 引语(登记+州府件)', 'https://www.northdata.com/'),
     ev('业务定位', 'PAXGuide Cloud: weltweite automatische Durchsagen an Flughäfen(机场 PA 播报云=关键场所谱)', 'https://www.sittig.de/')],
    '纽伦堡机场 PA 播报系统一件套房', '中型谱;PAXGuide 全球',
    ('机场谱=关键场所守界分', '专精深谱', 'Johannes Sittig 直达位', '自家栈一件套谱'),
    'Johannes Sittig 直达(opt-in 律;关键场所守界)', 'Guten Tag Herr Sittig,'))

R.append(rec('A-180', 'TELCAT MULTICOM GmbH – HQ',
    'TELCAT MULTICOM GmbH(德国;**HRB 6386;1986 创 40 年**;通信工程+网络基础设施谱;官网双 GF 谱:Moritz(Technik 技术口)+Rittmöller(商务口);Ya(s)ya 战略销售+Strell/Rafoth/Schwarz 区域销售面)',
    [('Moritz', 'Geschäftsführer Technik(技术 GF;官网自署)', 'telcat.de 官网谱', O, 'https://www.telcat.de/'),
     ('Rittmöller', 'Geschäftsführer(商务 GF;官网自署)', 'telcat.de 官网谱', O, 'https://www.telcat.de/'),
     ('Yaya', 'Strategischer Vertrieb(战略销售)', '员工谱', G, 'https://www.linkedin.com/'),
     ('Strell / Rafoth / Schwarz', '区域销售谱(三条线)', '员工谱', G, 'https://www.linkedin.com/')],
    [ev('决策链与对接人', 'HRB 6386;gegründet 1986;Geschäftsführung: Moritz(Technik)+ Rittmöller(Kaufmännisch)(官网/登记谱)', 'https://www.telcat.de/'),
     ev('团队与规模', 'Yaya Strategischer Vertrieb;Strell/Rafoth/Schwarz Gebietsleiter(员工谱面条)', 'https://www.linkedin.com/')],
    '德国 40 年通信工程屋(双 GF 分口谱)', '中型谱;1986 创',
    ('40 年工程谱+分口直达', '中实体谱', 'Moritz 技术位直配 PoE 谱', '一线链竞谱'),
    'Moritz 技术 GF(opt-in 律)', 'Guten Tag Herr Moritz,'))

R.append(rec('A-181', 'think about IT GmbH',
    'think about IT GmbH(德国;**HRB 11208;2007 创;€20M 五地谱**;**2024-25 INCAS 并入并谱:INCAS Janke/Pollok/Schmitt 谱并入**;创主 Rados+Kurth(2019 接棒)双谱;Wieners 医疗线=医院段守界注记)',
    [('Rados', 'Gründer/Geschäftsführer(创主谱)', '官网/登记谱', G, 'https://www.northdata.com/'),
     ('Kurth', 'Geschäftsführer(2019 起接棒)', '登记公告谱', G, 'https://www.northdata.com/'),
     ('Janke / Pollok / Schmitt', 'INCAS 并谱管理层(原 INCAS 谱)', '并购并入件', G, 'https://www.northdata.com/')],
    [ev('决策链与对接人', 'HRB 11208;gegründet 2007;Führung: Rados(创主)+ Kurth(seit 2019);INCAS-Zusammenschluss: Janke/Pollok/Schmitt(并购并谱件)', 'https://www.northdata.com/'),
     ev('联系方式与基础画像', 'fünf Standorte;~20 Mio. Euro;Wieners 医疗客户线=医院守界注记(谱面件)', 'https://www.thinkaboutit.de/')],
    '德国五地 MSP 并谱屋(INCAS 并入)', '€20M;五地',
    ('并购并谱=件链重整窗', '中型并谱', 'Rados/Kurth 直达位', '大牌链竞谱'),
    'Rados/Kurth 直达(医疗段守界;opt-in 律)', 'Guten Tag Herr Rados,'))

R.append(rec('A-182', 'Tiefenbach IT GmbH',
    'Tiefenbach IT GmbH(德国 Hochdorf-Assenheim(莱茵-普法尔茨);家族 IT 屋;**GF Ulrike Tiefenbach(女掌门人)+ Prokura 独任谱面 Jens(谱面单名)**;区域 IT 服务谱)',
    [('Ulrike Tiefenbach', 'Geschäftsführerin(登记谱)', '登记/谱面件', G, 'https://www.northdata.com/'),
     ('Jens(谱面单名)', 'Prokurist(独任总代理=采购直达位)', '谱面件(单名待核全名)', G, 'https://www.northdata.com/')],
    [ev('决策链与对接人', 'Geschäftsführerin: Ulrike Tiefenbach;Prokura: Jens(einzeln)(登记/谱面条)', 'https://www.northdata.com/'),
     ev('联系方式与基础画像', 'Hochdorf-Assenheim;区域 IT 服务屋(谱面件)', 'https://www.northdata.com/')],
    '德国莱茵普法尔茨家族 IT 屋', '小实体谱',
    ('Prokura 独任=签字直达', '小微谱', 'Jens 总代理直达位', '区域链竞谱'),
    'Ulrike Tiefenbach+Jens Prokura(opt-in 律)', 'Sehr geehrte Frau Tiefenbach,'))

R.append(rec('A-183', 'TQ-Systems GmbH',
    'TQ-Systems GmbH(德国 Seefeld(拜仁)-Inning;**HRB 105018 AG München;1994 创;1380 人/€266M**;E²MS 电子制造服务+模块件大厂(自有产线);**GF Stefan Schneider(2017 起)+ Detlef Schneider(2001 继创谱同姓)**=家族技术大厂谱)',
    [('Stefan Schneider', 'Geschäftsführer(2017 起;CEO 口)', 'northdata/tq-group 官网双源', G, 'https://www.northdata.com/'),
     ('Detlef Schneider', 'Geschäftsführer/创始谱(2001 继;同姓族谱)', '官网/谱面件', G, 'https://www.tq-group.com/')],
    [ev('决策链与对接人', 'HRB 105018 München;Geschäftsführung: Stefan Schneider(seit 2017)+ Detlef Schneider(seit 2001);gegründet 1994(登记/官网件)', 'https://www.northdata.com/'),
     ev('团队与规模', '1.380 Mitarbeiter;266 Mio. Euro Umsatz;E²MS Dienstleister+Embedded Module(规模谱件)', 'https://www.tq-group.com/')],
    '德国拜仁 1380 人电子制造+嵌入式大厂', '1380 人;€266M',
    ('大厂谱=OEM 件链深度', '大型屋谱', 'Schneider 族谱直达位', '自家产线=带件难谱'),
    'Stefan Schneider 直达(opt-in 律;带件难注记)', 'Guten Tag Herr Schneider,'))

R.append(rec('A-184', 'wp.DATA Kommunikations GmbH',
    'wp.DATA Kommunikations GmbH(德国 Neuss(北威州);**HRB 6960 AG Neuss;1992 创 34 年**;**SAP Gold Partner+SAP Business One 谱**;GF 双人谱 Schumacher+Seifert;通信+ERP 双栈谱)',
    [('Schumacher', 'Geschäftsführer(双位谱首)', 'northdata 登记谱(姓氏)', G, 'https://www.northdata.com/'),
     ('Seifert', 'Geschäftsführer(双位)', 'northdata 登记谱(姓氏)', G, 'https://www.northdata.com/')],
    [ev('决策链与对接人', 'HRB 6960 Neuss;gegründet 1992;Geschäftsführung: Schumacher + Seifert(登记件)', 'https://www.northdata.com/'),
     ev('技术与认证', 'SAP Gold Partner;SAP Business One(伙伴谱件)', 'https://www.wpdata.de/')],
    '德国 Neuss 34 年 SAP+通信双栈屋', '中型谱;1992 创',
    ('34 年谱+SAP 金牌谱', '中实体谱', '双 GF 直达位', '一线链竞谱'),
    'Schumacher/Seifert 直达(opt-in 律)', 'Guten Tag Herr Schumacher,'))

R.append(rec('A-185', 'Ziegler Systemhaus GmbH',
    'Ziegler Systemhaus GmbH(德国 Stuttgart(斯图加特);**HRB 21932 AG Stuttgart;2001 创;140 人**;系统屋谱;**2020-09 GF Bausch 加入=Wirth+Bausch 双驾**)',
    [('Wirth', 'Geschäftsführer(创期谱)', 'northdata 登记谱(姓氏)', G, 'https://www.northdata.com/'),
     ('Bausch', 'Geschäftsführer(2020-09 起)', '登记公告谱(姓氏)', G, 'https://www.northdata.com/')],
    [ev('决策链与对接人', 'HRB 21932 Stuttgart;gegründet 2001;Geschäftsführung: Wirth + Bausch(seit 09/2020);140 Mitarbeiter(登记/规模件)', 'https://www.northdata.com/'),
     ev('联系方式与基础画像', 'Ziegler Systemhaus GmbH, Stuttgart;Systemhaus 谱(谱面件)', 'https://www.google.com/search?q=%22Ziegler+Systemhaus%22')],
    '德国斯图加特 140 人系统屋', '140 人;2001 创',
    ('140 人系统屋谱', '中实体谱', 'Wirth/Bausch 双驾直达位', '一线链竞谱'),
    'Wirth/Bausch 直达(opt-in 律)', 'Guten Tag Herr Wirth,'))

R.append(rec('A-186', 'Zorn Elektrik GmbH',
    'Zorn Elektrik GmbH(德国 Korntal-Münchingen(巴符);**HRB 200691 AG Stuttgart;1971 创 55 年**;电气安装家族屋;**GF 换代:Gunzenhauser(2005~2021)→ Othmar Zorn(现职,业主名回归谱)**)',
    [('Othmar Zorn', 'Geschäftsführer(现职;业主名回归)', '登记/XING 员工谱双源', G, 'https://www.northdata.com/'),
     ('Gunzenhauser', '原 Geschäftsführer(2005~2021 在职谱;退位留痕)', 'XING/登记谱(留痕)', G, 'https://www.xing.com/')],
    [ev('决策链与对接人', 'HRB 200691 Stuttgart;gegründet 1971;Geschäftsführer: Othmar Zorn(neu);nicht mehr: Gunzenhauser(2005-2021)(登记/XING 件)', 'https://www.northdata.com/'),
     ev('联系方式与基础画像', 'Zorn Elektrik GmbH, Korntal;Elektroinstallation 谱(谱面件)', 'https://www.google.com/search?q=%22Zorn+Elektrik+GmbH%22')],
    '德国巴符 55 年电气安装家族屋', '中型谱;1971 创',
    ('55 年谱+业主名回归', '中实体谱', 'Zorn 回归直达位', '区域链竞谱'),
    'Othmar Zorn 直达(opt-in 律)', 'Guten Tag Herr Zorn,'))

# ============ IT×29(A-189~219 skip 188/196/205) ============
R.append(rec('A-189', 'Agomir',
    'Agomir(意大利 Lecco;**GR Informatica 1981 创母体谱**;**P.IVA 06256000156;REA MI-1082254;cap €1M**;**2025 Celtis+Supertronic 并入谱;ISO/IEC 27001**;行业访谈 CEO 姓氏 Goretti=谱面待核全面)',
    [('CEO(姓氏 Goretti=访谈谱,待核全名)', 'Amministratore/CEO 谱(行业访谈件)', '行业访谈件(谱姓名,全名待核)', G, 'https://www.agomir.it/')],
    [ev('决策链与对接人', 'P.IVA 06256000156;REA MI-1082254;capitale €1M;GR Informatica(dal 1981)母体谱;2025: Celtis + Supertronic 并入(登记/并购件)', 'https://www.agomir.it/'),
     ev('技术与认证', 'ISO/IEC 27001 认证谱(谱面件)', 'https://www.agomir.it/')],
    '意大利 Lecco 45 年 IT 谱(并购型)', '中型谱;GR 谱 1981',
    ('2025 双并=件链重整窗', '并购谱', 'CEO 位直达(全名待核)', '大牌链竞谱'),
    'CEO 谱位 opt-in(全名待核,礼节信走总台)', 'Gentile Sig. Amministratore,'))

R.append(rec('A-190', 'Asit SpA',
    'Asit SpA(意大利 Torino(都灵);**P.IVA 06221270017;1992 创;€41.8M;30 人**;**Ganz 家族三层谱:Jacopo/Joris Ganz(兄弟代)+Cristina Ganz**;atoka 管理单 8 名谱;IT 集成+服务屋)',
    [('Jacopo Ganz', 'Amministratore 谱(Ganz 兄弟代)', 'atoka/谱面件', G, 'https://www.atoka.io/'),
     ('Joris Ganz', 'Amministratore 谱(兄弟代)', 'atoka/谱面件', G, 'https://www.atoka.io/'),
     ('Cristina Ganz', '家族管理层谱(上一代)', 'atoka/谱面件', G, 'https://www.atoka.io/')],
    [ev('决策链与对接人', 'Persone in Asit: Jacopo Ganz, Joris Ganz, Cristina Ganz + 5 nomi(atoka 管理单 8 名总谱)', 'https://www.atoka.io/'),
     ev('联系方式与基础画像', 'P.IVA 06221270017;Torino;fondata 1992;fatturato €41.8M;30 dipendenti(登记/规模件)', 'https://www.asit.it/')],
    '意大利都灵 €41.8M IT 集成屋(家族谱)', '30 人;€41.8M',
    ('€41.8M/30 人=高人效谱', '中型谱', 'Ganz 兄弟直达位', '一线链竞谱'),
    'Ganz 兄弟位(opt-in 律)', 'Gentile Sig. Ganz,'))

R.append(rec('A-191', 'Coel Distribution srl',
    'Coel Distribution srl(意大利 Muggiò(蒙扎-布里安扎);**P.IVA 11989650152;2021 登;€15M**;**Fallerini 创主谱+Arianna Fallerini 二代谱;Follari CCO+Renzulli KAM+Brignoli 商务面**;增值分销谱)',
    [('Fallerini(创主谱,全名待核)', 'Fondatore/Amministratore 谱', '谱面件(谱姓名)', G, 'https://www.coel.it/'),
     ('Arianna Fallerini', '二代管理层谱(家族接棒)', '谱面件', G, 'https://www.coel.it/'),
     ('Follari', 'CCO(Chief Commercial Officer)', '谱面件', G, 'https://www.linkedin.com/'),
     ('Renzulli', 'Key Account Manager(KAM=落位 KPI)', '谱面件', G, 'https://www.linkedin.com/'),
     ('Brignoli', '商务谱(区域线)', '谱面件', G, 'https://www.linkedin.com/')],
    [ev('决策链与对接人', 'Fondatore: Fallerini;CCO: Follari;Arianna Fallerini;Renzulli KAM;Brignoli(谱面条总谱)', 'https://www.linkedin.com/'),
     ev('联系方式与基础画像', 'P.IVA 11989650152;Muggiò(MB);registrata 2021;fatturato €15M(登记件)', 'https://www.coel.it/')],
    '意大利蒙扎 2021 创增值分销屋', '€15M;2021 登',
    ('CCO+KAM 双口直击', '新创快谱', 'Fallerini 族谱直达位', '一线链竞谱'),
    'Follari CCO+Renzulli KAM(opt-in 律)', 'Gentile Sig. Follari,'))

R.append(rec('A-192', 'COMPUTER TIME S.r.l',
    'COMPUTER TIME S.r.l(意大利 Somma Lombardo(瓦雷泽);ctime.it 站谱=**主谱对位**(档案名全对位);技术谱 Bianchi+Pagani+Rubeo;**副谱分层:Roma 同名体 P.IVA 07225621007(DPO Montanile 谱)=同名异体已分层**)',
    [('Bianchi', '技术谱(ctime.it 主谱)', 'ctime.it 官网谱(姓氏)', G, 'https://www.ctime.it/'),
     ('Pagani', '技术谱(三位面)', 'ctime.it 官网谱(姓氏)', G, 'https://www.ctime.it/'),
     ('Rubeo', '技术谱(三位面)', 'ctime.it 官网谱(姓氏)', G, 'https://www.ctime.it/'),
     ('Montanile', 'Roma 异体 DPO 谱(分层留痕)', 'Roma 体谱面条(留痕)', G, 'https://www.ctime.it/')],
    [ev('决策链与对接人', 'Somma Lombardo 主谱: Bianchi + Pagani + Rubeo(ctime.it 谱面条)', 'https://www.ctime.it/'),
     ev('联系方式与基础画像', '异体分层: Roma COMPUTER TIME P.IVA 07225621007 DPO Montanile(同名异体,主谱按档案名对位 Somma Lombardo)', 'https://www.ctime.it/')],
    '意大利瓦雷泽 IT 技术服务屋', '中小谱',
    ('三技谱面直击', '中小实体谱', 'Bianchi/Pagani/Rubeo 直达位', '区域链竞谱'),
    'Bianchi 技术位(opt-in 律)', 'Gentile Sig. Bianchi,'))

R.append(rec('A-193', 'CONNECT ICS S.R.L',
    'CONNECT ICS S.R.L(意大利 Lecce(萨伦托);**P.IVA 04541830750;2013 创;11 人**;**Mancarella Daniele 技术总监(DT)+Spongano 秘书位;Wildix Bronze Partner 2023(UC 谱);MEPA 谱=市政段守界注记**)',
    [('Daniele Mancarella', 'Direttore Tecnico(DT=技术直达位)', '官网/谱面件', O, 'https://www.connectics.it/'),
     ('Spongano', 'Segreteria(秘书口=礼仪信口)', '谱面件(姓氏)', G, 'https://www.connectics.it/')],
    [ev('决策链与对接人', 'Daniele Mancarella Direttore Tecnico;segreteria Spongano(官网/谱面条)', 'https://www.connectics.it/'),
     ev('联系方式与基础画像', 'P.IVA 04541830750;Lecce;costituita 2013;11 dipendenti;Wildix Partner 2023;MEPA fornitore abilitato(登记/伙伴件)', 'https://www.connectics.it/')],
    '意大利萨伦托 11 人 UC+网络集成屋', '11 人;2013 创',
    ('Wildix 谱=UC 件链窗', '小实体谱', 'Mancarella DT 直达位', '区域链竞谱;MEPA 守界注'),
    'Mancarella DT 直达(opt-in 律;市政段守界)', 'Gentile Dott. Mancarella,'))

R.append(rec('A-194', 'CTC SYSTEMS SRL',
    'CTC SYSTEMS SRL(意大利 Calco(莱科);**P.IVA 03348320130;2011 创;12 人;€2M**;**ISO 9001 双认证谱;Castelli 董事谱+Marmo/Colombo/Orlando 技术面**)',
    [('Castelli', '董事/管理谱(姓氏;Amministratore 谱待核全名)', '谱面条(姓氏)', G, 'https://www.atoka.io/'),
     ('Marmo', '技术谱(三位面)', '谱面条(姓氏)', G, 'https://www.ctcsystems.it/'),
     ('Colombo', '技术谱', '谱面条(姓氏)', G, 'https://www.ctcsystems.it/'),
     ('Orlando', '技术谱', '谱面条(姓氏)', G, 'https://www.ctcsystems.it/')],
    [ev('决策链与对接人', 'Castelli(direzione)+ Marmo/Colombo/Orlando(谱面条总谱)', 'https://www.ctcsystems.it/'),
     ev('联系方式与基础画像', 'P.IVA 03348320130;Calco(LC);costituita 2011;12 dipendenti;€2M;ISO 9001 双重谱(登记/认证件)', 'https://www.ctcsystems.it/')],
    '意大利莱科 12 人 €2M 系统屋', '12 人;€2M',
    ('ISO 双谱=资质窗', '小实体谱', 'Castelli 直达位', '区域链竞谱'),
    'Castelli 位(opt-in 律)', 'Gentile Sig. Castelli,'))

R.append(rec('A-195', 'EMILIA INFORMATICA s.r.l',
    'EMILIA INFORMATICA s.r.l(意大利 Piacenza(皮亚琴察);**P.IVA 01226710331;1997 创;52 人;€6.6M**;**报告站 CESSATA 标记留痕→官网活档(2026 再核):营业谱照走,标记差旗已注;Cerved Group 旗下谱**;官网全谱 Castagnola/A.Corti/Bernazzani/Sanna/F.Corti/Calamari)',
    [('Castagnola', '管理谱(官网谱面首)', '官网/谱面条', G, 'https://www.emiliainformatica.it/'),
     ('A. Corti', '管理谱(Corti 族双线 A)', '官网/谱面条', G, 'https://www.emiliainformatica.it/'),
     ('Bernazzani', '管理/技术谱', '官网/谱面条', G, 'https://www.emiliainformatica.it/'),
     ('Sanna', '管理谱', '官网/谱面条', G, 'https://www.emiliainformatica.it/'),
     ('F. Corti', 'Corti 族谱(二线 F)', '官网/谱面条', G, 'https://www.emiliainformatica.it/'),
     ('Calamari', '谱面条(支持位)', '官网/谱面条', G, 'https://www.emiliainformatica.it/')],
    [ev('决策链与对接人', '官网全谱: Castagnola, A.Corti, Bernazzani, Sanna, F.Corti, Calamari(官网谱面条)', 'https://www.emiliainformatica.it/'),
     ev('联系方式与基础画像', 'P.IVA 01226710331;Piacenza;1997 创;52 dipendenti;€6.6M;**report 站 CESSATA 标记 vs 官网活档=差旗核查注记**;Cerved Group 旗下(acquisizione 谱)', 'https://www.emiliainformatica.it/')],
    '意大利皮亚琴察 52 人 IT 屋(Cerved 系)', '52 人;€6.6M',
    ('CESSATA 差旗已注=守疑谱', '中实体谱', 'Castagnola 直达位', 'Cerved 系链竞谱'),
    'Castagnola 直达(opt-in 律;CESSATA 差旗先核)', 'Gentile Sig. Castagnola,'))

# skip A-196 Evergreen1(换出);A-197:
R.append(rec('A-197', 'FARPOINT SRL',
    'FARPOINT SRL(意大利 Modena(摩德纳),Via Emilia Est 1058/D;**P.IVA 02650830363;4 人;€704k**;**官网联络页全谱带分机手机=O 金谱:Elisabetta Nascimbeni(amministrazione)+Giorgio Bertoni(reti/antivirus)+Sandro Stradi(stampa)+Walter Pelloni(gestionale)+Manuel Di Bona**)',
    [('Elisabetta Nascimbeni', 'Amministrazione(行政直达;官网手机自署)', 'farpoint.it 联络页(O)', O, 'https://www.farpoint.it/'),
     ('Giorgio Bertoni', 'Assistenza reti/antivirus(网络口=落位最合)', 'farpoint.it 联络页(O)', O, 'https://www.farpoint.it/'),
     ('Sandro Stradi', '打印/外围谱', 'farpoint.it 联络页(O)', O, 'https://www.farpoint.it/'),
     ('Walter Pelloni', 'Gestionale(管理软件口)', 'farpoint.it 联络页(O)', O, 'https://www.farpoint.it/'),
     ('Manuel Di Bona', '技术谱(官网条)', 'farpoint.it 联络页(O)', O, 'https://www.farpoint.it/')],
    [ev('决策链与对接人', 'farpoint.it/contatti: Nascimbeni(amministrazione), Bertoni(reti), Stradi(stampa), Pelloni(gestionale), Di Bona——带手机号自署=O 级全谱', 'https://www.farpoint.it/'),
     ev('联系方式与基础画像', 'P.IVA 02650830363;Via Emilia Est 1058/D Modena;4 dipendenti;€704k(登记件)', 'https://www.farpoint.it/')],
    '意大利摩德纳 4 人 IT 服务铺', '4 人;€704k',
    ('联络页 O 级全谱=罕见', '微实体谱', 'Nascimbeni 行政+Bertoni 网络位', '区域链竞谱'),
    'Nascimbeni 行政位(opt-in 律)', 'Gentile Sig.ra Nascimbeni,'))

R.append(rec('A-198', 'Fiore Srl',
    'Fiore Srl(意大利 Paderno Dugnano(米兰北)+Vicenza+Bari 三站;**1983 创 43 年;布线/网络/IP 电话增值分销**;2300㎡ 仓 5000 SKU(自产 19" 机柜);**Amministratore Unico Mauro Iori(TradeManager 专访=O/G 单谱,创始愿景传递谱);ISO 9001+IQNET;Fluke Networks 六年连冠最佳分销商(2018)**)',
    [('Mauro Iori', 'Amministratore Unico(独任 AU;专访官方引语)', 'TradeManager 专访+谱面条', O, 'https://www.trademanager.it/')],
    [ev('决策链与对接人', 'Amministratore Unico: Mauro Iori(TradeManager 专访自署);tre sedi: Paderno Dugnano, Vicenza, Bari;dal 1983', 'https://www.trademanager.it/'),
     ev('技术与认证', 'ISO 9001 + IQNET;Fluke Networks Best Distributor 六年连(2018 颁奖件);magazzino 2300㎡/5000 SKU 自产 armadi 19"', 'https://www.fiorenet.it/')],
    '意大利米兰 43 年布线分销屋(自产机柜)', '11-50 人;1983 创',
    ('43 年分销谱=件链大户', '分销谱', 'Iori AU 独任直达位', '自产线谱'),
    'Mauro Iori 直达(opt-in 律)', 'Gentile Sig. Iori,'))

R.append(rec('A-199', 'GECOPRA SRL',
    'GECOPRA SRL(意大利 Napoli(那不勒斯),Via Francesco Provenzale;**1988 创;28 人**;**EL.C.I. Impianti 集团谱:Massimo Caronte Presidente+Simona Caronte CEO+Francesco Palmieri/+Marcello Caronte/Ivan Cimmino 董事会;新加坡 F1 赛道照明维护=国际谱**;分位谱:Davide Cimmino Direttore Generale+Lorenzo Tornatore CTO+Lucia Cimmino Purchasing(采购 KPI!))',
    [('Davide Cimmino', 'Direttore Generale Gecopra(分谱 DG=落位最合)', '集团/谱面条', G, 'https://www.gecopra.it/'),
     ('Lorenzo Tornatore', 'CTO(技术口)', '集团/谱面条', G, 'https://www.gecopra.it/'),
     ('Lucia Cimmino', 'Purchasing Officer(采购 KPI 直达)', '谱面条', G, 'https://www.linkedin.com/'),
     ('Massimo Caronte', 'Presidente(集团层面)', 'ELCI/谱面件', G, 'https://www.gecopra.it/'),
     ('Simona Caronte', 'CEO(集团层面)', 'ELCI/谱面件', G, 'https://www.gecopra.it/')],
    [ev('决策链与对接人', 'Gecopra division: Davide Cimmino DG;Lorenzo Tornatore CTO;Lucia Cimmino Purchasing Officer;集团谱: Massimo Caronte Presidente + Simona Caronte CEO(集团/谱面条)', 'https://www.gecopra.it/'),
     ev('联系方式与基础画像', 'fondata 1988;28 dipendenti;Napoli;manutenzione illuminazione circuito F1 Singapore(国际谱件)', 'https://www.gecopra.it/')],
    '意大利那不勒斯 1988 创工程屋(集团谱)', '28 人;1988 创',
    ('Purchasing Officer 具名=采购直达', '集团子谱', 'Cimmino DG+Tornatore CTO 双位', '集团链竞谱'),
    'Cimmino DG 直达(opt-in 律)', 'Gentile Ing. Cimmino,'))

R.append(rec('A-200', 'GIS s.r.l',
    'GIS s.r.l(**三异体群未锁主谱**——GIS International srl(1993 起;G-MS Industry 4.0 safety/CSA STAR registry=ISO27001 谱) / Gestione Integrata Servizi(Roma,P.IVA IT07030151000) / Global Informatica(MN,P.IVA 01897680201);档案名「GIS s.r.l」无域锚→**守档准由:谱面未见具名决策人,锚异体群留档待点名**)',
    [],
    [ev('联系方式与基础画像', '异体群锚: GIS International(1993,safety 平台,CSA STAR) / Gestione Integrata Servizi Roma P.IVA IT07030151000 / Global Informatica MN P.IVA 01897680201(三条登记锚)', 'https://www.northdata.com/'),
     ev('决策链与对接人', '公开谱面未见具名决策人=守档准由;2026-10-08 再核实留痕(R66 第 19 波点名)', 'https://www.northdata.com/'),
     ev('近期动态与线索', 'R66 19 波档案点名:三异体群主谱未锁(笔名短==搜索噪声大),守档待专批', 'https://www.northdata.com/')],
    '意大利 GIS 三异体群(主谱未锁)', '守档案',
    ('CSA STAR 谱线索(GIS International)', '短名异体群', '无守档', '—'),
    '守档:谱面无实名(待专批点名)', 'Gentile Direzione,'))

R.append(rec('A-201', 'Goretti Technological System S.r.l',
    'Goretti Technological Systems S.r.l(意大利 Corciano(佩鲁贾),Via Palazzeschi 16/A;**P.IVA 03178850545;REA 269651;2011-01-26 登;15-17 人;€2.7M(+16-40%);Utile €85-95k**;**Amministratore Unico Alessio Goretti(xrayfinance 谱)+Filippo Goretti 成员谱;Cagnoni/Borscia/Cianella/Viscardi 队谱;G&M 1992 起 GDO 谱=大链零售件谱**',
    [('Alessio Goretti', 'Amministratore Unico(xrayfinance 谱)', 'xrayfinance/atoka 件', G, 'https://www.xrayfinance.com/'),
     ('Filippo Goretti', '成员谱(族谱)', '谱面条', G, 'https://www.gtstec.com/'),
     ('Cagnoni', '队谱(技术位)', '谱面条(姓氏)', G, 'https://www.gtstec.com/'),
     ('Borscia / Cianella / Viscardi', '队谱(三条面)', '谱面条(姓氏)', G, 'https://www.gtstec.com/')],
    [ev('决策链与对接人', 'Amministratore Unico: Alessio Goretti;m.fucelli@gtstec.com(联络谱);Filippo Goretti 成员(xrayfinance/官网件)', 'https://www.xrayfinance.com/'),
     ev('联系方式与基础画像', 'P.IVA 03178850545;REA PG 269651;Corciano(PG);costituita 26/01/2011;15-17 dipendenti;fatturato €2.7M(+16-40%);utile €85-95k;G&M dal 1992 GDO 谱(登记/账谱件)', 'https://www.gtstec.com/')],
    '意大利翁布里亚零售技术屋(GDO 谱)', '17 人;€2.7M',
    ('GDO 零售链=件铺谱窗', '小实体谱', 'Alessio Goretti AU 直达位', '区域链竞谱'),
    'Alessio Goretti AU 直达(opt-in 律)', 'Gentile Sig. Goretti,'))

R.append(rec('A-202', 'IFI Consulting Srl',
    'IFI Consulting Srl(意大利 Modena(摩德纳),Via F. Lamborghini 79(现)+Via Zucchi 31(旧)双址留痕;**51-200 人/$7.4M**;**Allied Telesis 伙伴页+Arcserve 页伙伴双谱=网络件链谱**;Emanuela Rossi(arcserve 页具名联络=O)+Director 谱(Anghoura,zoominfo 谱面)',
    [('Emanuela Rossi', '合作伙伴页具名联络(厂商页 O)', 'arcserve 伙伴页(O)', O, 'https://www.arcserve.com/'),
     ('Director 谱(Anghoura 姓氏条)', 'Director(zoominfo 谱面条;全名待核)', 'zoominfo 谱面条', G, 'https://www.zoominfo.com/')],
    [ev('决策链与对接人', 'Emanuela Rossi(arcserve partner locator 具名);Director: Anghoura 姓氏条(zoominfo 谱面)', 'https://www.arcserve.com/'),
     ev('联系方式与基础画像', 'Via F. Lamborghini 79 Modena(现址);旧址 Via Carlo Zucchi 31 留痕;51-200 dipendenti;$7.4M;Allied Telesis 伙伴谱(伙伴页/规模件)', 'https://www.alliedtelesis.com/')],
    '意大利摩德纳 IT 集成屋(Allied/Arcserve 双伙伴)', '51-200 人;$7.4M',
    ('Allied 伙伴=网络件同营谱', '中实体谱', 'Rossi 联络直达位', 'Allied 自家链谱'),
    'Emanuela Rossi 位(opt-in 律)', 'Gentile Sig.ra Rossi,'))

R.append(rec('A-203', 'JM CONSULTING SRL',
    'JM CONSULTING SRL(意大利 Gossolengo(皮亚琴察),Via Donatori Sangue 3;**P.IVA 01268690334;REA PC-147985;1999 创;~40 专业人士/800+ 客户/80 代理商网**;**Adiuto WMS 流程软件自产谱(2001 起);Innovation Wind 谱=创新资助谱**;公开谱面未见具名决策人→**守档准由(锚全名缺)**)',
    [],
    [ev('联系方式与基础画像', 'P.IVA 01268690334;REA PC147985;Gossolengo(PC);fondata 1999;40 professionisti;800+ clienti;rete 80 rivenditori;Adiuto dal 2001(登记/官网件)', 'https://www.jmconsulting.it/'),
     ev('决策链与对接人', '公开谱面未见具名决策人=守档准由;锚全(P.IVA/REA/年创/规模)名缺;2026-10-08 再核实留痕', 'https://www.jmconsulting.it/'),
     ev('近期动态与线索', 'R66 19 波档案点名:Adiuto WMS 生态谱+80 代理商网=生态件链谱,守档待专批点名', 'https://www.jmconsulting.it/')],
    '意大利皮亚琴察 WMS 流程软件屋(生态 80 代理)', '40 人;800 客',
    ('Adiuto WMS 自产谱', '生态谱', '无守档', '—'),
    '守档:谱面无实名(锚全;待专批点名)', 'Gentile Direzione,'))

R.append(rec('A-204', 'Localnet Firenze Srl',
    'LOCALNET FIRENZE SRL(意大利 Firenze,Via V. Dei Benedetto 64;**2008-02 创(Local Net Toscana 谱);2-10 人;电话/安防/结构化布线工程**;**Alessio Angioli AD(兼 Globalnet italia 技术总监=同铺集团谱)+Simone Azzarri Co-Owner+Riccardo Ridolfi 业主谱;Risco Partner Gold 2022(Wise 分销颁奖照件=具名金谱)**)',
    [('Alessio Angioli', 'Amministratore Delegato(兼 Globalnet Italia 技术总监=集团谱)', 'LinkedIn 谱面条', G, 'https://www.linkedin.com/'),
     ('Simone Azzarri', 'Co-Owner(同业主谱;Risco 颁奖照件具名)', 'globalnetitalia.it 2022 颁奖件', O, 'https://www.globalnetitalia.it/2022/09/29/localnet-firenze-nominato-risco-partner-gold-2022/'),
     ('Riccardo Ridolfi', 'Proprietario(业主谱)', 'contactout 谱面条', G, 'https://contactout.com/'),
     ('Luca Chelucci', 'Tecnico specializzato(技术谱;颁奖照件具名)', 'globalnetitalia.it 颁奖件', O, 'https://www.globalnetitalia.it/2022/09/29/localnet-firenze-nominato-risco-partner-gold-2022/')],
    [ev('决策链与对接人', 'Risco Partner Gold 2022 颁奖照件: Simone Azzarri(Co-Owner)+ Luca Chelucci(tecnico)+ Alessandro Bachi(Wise)+ Risco 官员(globalnetitalia.it 件)', 'https://www.globalnetitalia.it/2022/09/29/localnet-firenze-nominato-risco-partner-gold-2022/'),
     ev('联系方式与基础画像', 'Via V. Dei Benedetto 64, 50127 Firenze;fondata febbraio 2008;AD Alessio Angioli(兼 Globalnet Italia);2-10 dipendenti;impianti telefonici/TVCC/antintrusione/cablaggio(LinkedIn/reteimprese 件)', 'https://www.linkedin.com/company/localnet-firenze-srl')],
    '意大利佛罗伦萨 2008 创通信+安防工程铺', '2-10 人;2008 创',
    ('Risco Gold 2022=安防通道谱', '小实体谱', 'Azzarri 同业主直达位', '区域链竞谱'),
    'Azzarri 共业主位(opt-in 律)', 'Gentile Sig. Azzarri,'))

R.append(rec('A-206', 'N&C TELECOMUNICAZIONI S.p.a',
    'N&C TELECOMUNICAZIONI S.p.A.(意大利 Veglie(莱切),Via Bosco S.N.;**Allied Telesis 伙伴页具名具址=网络件同营谱**;Antonio Nestola(GESTIONALI 口=管理软件位,LinkedIn 谱);S.p.A. 形制=股份公司谱)',
    [('Antonio Nestola', 'Gestionali 位(管理软件口;LinkedIn 具名谱)', 'LinkedIn 谱面条', G, 'https://www.linkedin.com/in/antonio-nestola-6740354a/')],
    [ev('联系方式与基础画像', 'N&C TELECOMUNICAZIONI S.p.A., Via Bosco S.N., Veglie LE 73010;+39 0832 970190(Allied Telesis 伙伴页官谱)', 'https://www.alliedtelesis.com/us/en/nc-telecomunicazioni-spa'),
     ev('决策链与对接人', 'Antonio Nestola(GESTIONALI,N&C Telecomunicazioni;可引 7 人@N&C S.p.A.——LinkedIn 谱面条)', 'https://www.linkedin.com/in/antonio-nestola-6740354a/')],
    '意大利萨伦托 S.p.A. 电信屋(Allied 谱)', '中型谱',
    ('Allied 伙伴页=同营件链', '中实体谱', 'Nestola 具名位', 'Allied 链竞谱'),
    'Nestola 位(opt-in 律)', 'Gentile Sig. Nestola,'))

R.append(rec('A-207', 'NA.EL Srl',
    'NA.EL. S.R.L.(意大利 Napoli,Via Ferrante Imparato 190;**P.IVA 02077090617;CF 05841550634;REA 701083;1992-10-15 创 34 年;账谱 0 dip(2023)=小型谱;€861k(2021,+utile €106k)**;**军/大客档谱:C.DO 10° RGT MANOVRA Persano+SCUOLA TELC FF.AA+(科威特)C.AMM.VO D\'INTENDENZA Kuwait City ICT/LAN+BOEING DB 托管=军谱守界加厚**;Cosimo Cantatore Owner(LinkedIn 谱))',
    [('Cosimo Cantatore', 'Owner(业主位;LinkedIn 具名谱)', 'LinkedIn 公司页员工谱', G, 'https://it.linkedin.com/company/na-el')],
    [ev('决策链与对接人', 'Cosimo Cantatore Owner(linkedin.com/company/na-el 员工谱条)', 'https://it.linkedin.com/company/na-el'),
     ev('联系方式与基础画像', 'P.IVA 02077090617;REA 701083;Via Ferrante Imparato 190 Napoli;iscritta 15/10/1992;fatturato €860.993(2021);dipendenti 0(2023 账谱)=微谱注记(ufficiocamerale 件)', 'https://www.ufficiocamerale.it/5001/nael-srl'),
     ev('近期动态与线索', '官网介绍 PDF 档: C.DO 10° RGT MANOVRA Persano+SCUOLA TELECOMUNICAZIONI FF.AA+C.AMM.VO Kuwait City(ICT/LAN)+BOEING banche dati+Comuni(Forio/Volla)——**军谱守界加厚(nael.it 自档)**', 'https://www.nael.it/wp-content/uploads/2015/05/PRESENTAZIONE-NAEL-28.02.2026.pdf')],
    '意大利那不勒斯 34 年 IT 安装屋(军客谱)', '微-小谱;1992 创',
    ('军/BOEING 客档=最高守界', '军线守界段', 'Cantatore 直达位', '军件链竞谱'),
    '军谱守界:仅民窄段试探(opt-in 律)', 'Gentile Sig. Cantatore,'))

R.append(rec('A-208', 'Net System Innovazione srl',
    'NET SYSTEM INNOVAZIONE SRL(意大利 Vignolo(库内奥),Via Cuneo 36/A;**P.IVA 03886990047;2020 创;0-9 人;€963k(2024,-;utile €71-78k,7.4%);电脑/周边/软件零售铺;MePA 2024 Abilitato(视频监控/门禁/入侵标段)=市政谱**;公开谱面未见具名决策人→**守档准由**)',
    [],
    [ev('联系方式与基础画像', 'P.IVA 03886990047;Via Cuneo 36/A Vignolo(CN);costituita 2020;0-9 dipendenti;fatturato €963k(2024);utile €71.4k(registroaziende/reportaziende 件)', 'https://registroaziende.it/azienda/net-system-innovazione-srl-vignolo'),
     ev('决策链与对接人', '公开谱面未见具名决策人=守档准由(ReportAziende 治理位打码条,未点名);2026-10-08 留痕', 'https://www.reportaziende.it/net_system_innovazione_srl_cn'),
     ev('近期动态与线索', 'MePA 2024: lotto Videosorveglianza/controllo accessi/antintrusione Abilitato(amministrazionicomunali.it 件)', 'https://www.amministrazionicomunali.it/piemonte/vignolo/net-system-innovazione')],
    '意大利库内奥 0-9 人 IT 零售铺(MePA 谱)', '0-9 人;€963k',
    ('MePA 视频监控段=边界谱', '微实体谱', '无守档', '—'),
    '守档:谱面无实名(锚全;待专批点名)', 'Gentile Direzione,'))

R.append(rec('A-209', 'NEWSOFT Technology SRL',
    'NEWSOFT TECHNOLOGY SRL(意大利 Saluzzo(库内奥),Via del Mattatoio 42;**P.IVA 03999770047;REA CN-329104;1998 创谱→2022-04-01 新体登记;4 人;€1.02M(2023);cap €50k**;**Carlo Geuna Fondatore/owner(LinkedIn+BNI Visol 谱)+Raffaella Bruno Franco Amministrazione;Polo ICT 谱;新铺具花园/健身房/Fucina 培养坊=扩张窗**)',
    [('Carlo Geuna', 'Fondatore/owner(创主直达;LinkedIn 自署+BNI 谱)', 'linkedin.com/in/carlogeuna+BNI Visol 件', G, 'https://www.linkedin.com/in/carlogeuna/'),
     ('Raffaella Bruno Franco', 'Amministrazione(行政口)', 'LinkedIn 公司页员工谱', G, 'https://it.linkedin.com/company/newsoft-technology-srl')],
    [ev('决策链与对接人', 'Carlo Geuna owner/fondatore(LI 自署:「Fondatore della Newsoft con sede a Saluzzo」);Raffaella Bruno Franco AMMINISTRAZIONE;BNI Visol 成员谱(2025 迎入件)', 'https://it.linkedin.com/company/newsoft-technology-srl'),
     ev('联系方式与基础画像', 'P.IVA 03999770047;REA CN329104;Via del Mattatoio 42 Saluzzo;iscritta 01/04/2022(25 年传承谱自 1998);4 dipendenti;fatturato €1.022.686(2023);capitale €50k(ufficiocamerale/poloict 件)', 'https://www.ufficiocamerale.it/9872/newsoft-technology-srl')],
    '意大利皮埃蒙特 25 年 IT 服务铺(新体 2022)', '4 人;€1.02M',
    ('新铺扩张窗(Fucina 坊)', '小实体谱', 'Geuna 创主直达位', '区域链竞谱'),
    'Carlo Geuna 直达(opt-in 律)', 'Gentile Sig. Geuna,'))

R.append(rec('A-210', 'OMNICONNECT srl',
    'OMNICONNECT SRL(意大利 Pontedera(比萨),Via Salvo d\'Acquisto 40/V(法址;Calcinaia Via Tosco Romagnola 9 运营留痕);**P.IVA 01586840504;2001 创;10-19 人;集成商谱(电信+数传+DC 基建+视频监控+网安)**;**MePA 25 项 abilitazioni=PA 谱大户**;公开谱面未见具名决策人→**守档准由**)',
    [],
    [ev('联系方式与基础画像', 'P.IVA 01586840504;Via Salvo d\'Acquisto 40/V Pontedera(PI);fondata 2001;10-19 dipendenti;System Integrator telefonia/DC/reti/videosorveglianza(官网+impresaitalia 件)', 'https://www.omniconnect.it/'),
     ev('近期动态与线索', 'MePA scheda: 25 abilitazioni attive(lotti comunicazione/ICT supporto/video-sorveglianza;amministrazionicomunali.it 件)=PA 谱大户', 'https://www.amministrazionicomunali.it/toscana/pontedera/omniconnect-srl'),
     ev('决策链与对接人', '公开谱面未见具名决策人=守档准由;2026-10-08 留痕', 'https://www.omniconnect.it/')],
    '意大利托斯卡纳 2001 创集成商(MePA 25 项)', '10-19 人;2001 创',
    ('MePA 25 项=PA 谱大户', '中小实体谱', '无守档', '—'),
    '守档:谱面无实名(锚全;待专批点名)', 'Gentile Direzione,'))

R.append(rec('A-211', 'PAM UFFICIO Srl',
    'PAM UFFICIO SRL(意大利 Messina,C.da Filangeri snc(Pistunina);**P.IVA 01261820839;REA ME-113569;1983-07-29 创 43 年;2-5 人;€626-714k(2024;utile €107k,-24% trend)**;办公设备+IT 铺;**MePA 60 项 abilitazioni 大谱(网络设备段已含)**;Amministratore Unico 位在册(atoka 打码条)→公开谱面未点名=**守档准由**)',
    [],
    [ev('联系方式与基础画像', 'P.IVA 01261820839;REA ME113569;C.da Filangeri snc, Messina;costituita 29/07/1983;2-5 dipendenti;fatturato €714.400(2024);utile €107.067;41+ 年谱(fatturatoitalia/atoka 件)', 'https://www.fatturatoitalia.it/pam_ufficio_s_r_l-01261820839'),
     ev('近期动态与线索', 'MePA scheda: 60 abilitazioni(lotto Apparati di rete 含;amministrazionicomunali.it 件)=西西里 PA 谱大户', 'https://www.amministrazionicomunali.it/sicilia/messina/pam-ufficio-srl'),
     ev('决策链与对接人', 'Amministratore Unico 在册(atoka 打码条)——公开谱面未见具名=守档准由;2026-10-08 留痕', 'https://atoka.io/public/it/azienda/pam-ufficio-s-r-l/02e236615994')],
    '意大利墨西拿 43 年办公+IT 铺(MePA 60 项)', '2-5 人;1983 创',
    ('MePA 60 项含网络段=PA 谱窗', '小实体谱', '无守档', '—'),
    '守档:AU 在册未具名(满锚;待专批点名)', 'Gentile Direzione,'))

R.append(rec('A-212', 'S.C.E Telecomunicazioni S.r.l',
    'S.C.E. - TELECOMUNICAZIONI S.R.L.(意大利 Pomezia(罗马),Via Urbano Rattazzi 3;**P.IVA 08399381006;REA 1091781;2005-05-23 创;2 人;€1.41M(2025,-3.9%;utile €79k,+)**;**营业谱=军事用电信/电话/数传设备批发(ats 条原文:in ambito militare)=商军边界守界加厚**;排噪:SCE srl 工业自动化 Corradini(45 年艾米利亚体)=同名异体已分层;公开谱面未见具名→**守档准由**)',
    [],
    [ev('联系方式与基础画像', 'P.IVA 08399381006;REA 1091781;Via Urbano Rattazzi 3 Pomezia(RM);costituita 23/05/2005;2 dipendenti;fatturato €1,41 Mln(2025,-3.9%);utile €79k(reportaziende/ufficiocamerale 件)', 'https://www.reportaziende.it/sce_telecomunicazioni_srl_o_in_forma_abbreviata_scesrl_rm_08399381006'),
     ev('近期动态与线索', 'Oggetto sociale: commercio apparecchiature elettriche/elettroniche/informatiche **in ambito militare**;progettazione produzione apparati TLC militari(atoka 条原文)=商军边界守界注记', 'https://atoka.io/public/it/azienda/sce-telecomunicazioni-srl-o-in-forma-abbreviata-sce-srl/97eb68904abb'),
     ev('决策链与对接人', 'Amministratore Unico 位在册(atoka 打码)——公开谱面未见具名=守档准由;SCE Elettronica Automazione(Corradini 45 年体)同名异体分层;2026-10-08 留痕', 'https://atoka.io/public/it/azienda/sce-telecomunicazioni-srl-o-in-forma-abbreviata-sce-srl/97eb68904abb')],
    '意大利拉齐奥军用电讯设备批发铺', '2 人;€1.41M',
    ('军事件边界=最高守界', '军商边界段', '无守档', '—'),
    '守档:军件谱守界(锚全;待专批点名)', 'Gentile Direzione,'))

R.append(rec('A-213', 'Sfera Informatica & Strumentazione S.r.l',
    'SFERA INFORMATICA & STRUMENTAZIONE S.R.L.(意大利 Modugno(巴里),Trav. Sx Via VV.FF. Caduti in Servizio 6/8;**P.IVA 06036770722;1998 创;11-50(队谱 8);MePA 32 项 abilitazioni**;新铺(四年)实验室+仓+展厅培训;**Gianvito Brandonisio Cofounder/Amministratore Unico&Technical Director(D&B 谱)+Luigi Ruoto Co-Owner&Sales Manager(LI 谱);Francesco Proia 营销+Francesca Calabrese HR+Davide Liberio ICT;Confindustria BAT 成员**)',
    [('Gianvito Brandonisio', 'Amministratore Unico / Technical Director(D&B 具名谱)', 'D&B 公司档+LI 谱双源', G, 'https://www.dnb.com/business-directory/company-profiles.sfera_informatica__strumentazione_srl.47c34f656b277e2e72dbe45fc83aceef.html'),
     ('Luigi Ruoto', 'Co-Owner & Sales Manager(销售直达)', 'LinkedIn 谱面条', G, 'https://www.linkedin.com/company/sfera-informatica-strumentazione-srl'),
     ('Francesco Proia', 'Marketing e Comunicazione(营销口)', 'RocketReach 队谱', G, 'https://rocketreach.co/sfera-informatica-strumentazione-srl-management_b79785a7c24e9e8e'),
     ('Francesca Calabrese', 'Responsabile risorse umane(HR)', 'RocketReach 队谱', G, 'https://rocketreach.co/sfera-informatica-strumentazione-srl-management_b79785a7c24e9e8e'),
     ('Davide Liberio', 'Tecnico di supporto IT(技术谱)', 'RocketReach 队谱', G, 'https://rocketreach.co/sfera-informatica-strumentazione-srl-management_b79785a7c24e9e8e')],
    [ev('决策链与对接人', 'Key Principal: GIANVITO BRANDONISIO Sole Administrator(D&B 件);Luigi Ruoto Co-Owner & Sales Manager;队谱 Proia(Mkt)/Calabrese(HR)/Liberio(IT)(D&B+LI+RR 三源)', 'https://www.dnb.com/business-directory/company-profiles.sfera_informatica__strumentazione_srl.47c34f656b277e2e72dbe45fc83aceef.html'),
     ev('联系方式与基础画像', 'P.IVA 06036770722;Modugno(BA);fondata 1998;MePA 32 abilitazioni;nuova sede(laboratorio+magazzino+showroom/formazione)(Confindustria BAT+amministrazionicomunali 件)', 'https://confindustria.babt.it/associato/sfera-informatica-strumentazione-srl/')],
    '意大利巴里 1998 创 IT+仪器屋(MePA 32)', '11-50 人;1998 创',
    ('AU+Co-Owner 双谱直击', '中小实体谱', 'Ruoto 销售口最合', 'MePA 谱'),
    'Brandonisio AU+Ruoto 销售位(opt-in 律)', 'Gentile Sig. Brandonisio,'))

R.append(rec('A-214', 'SI.EL.CO. S.R.L',
    'SI.EL.CO. S.R.L(意大利;**短名搜索噪声大(法科级噪声主导),谱面未见具名决策人+锚未锁→守档准由**;R66 波次二点名待与档案二次对位)',
    [],
    [ev('决策链与对接人', '公开谱面未见具名决策人=守档准由(短体名噪声位);2026-10-08 再核实留痕', 'https://www.google.com/search?q=%22SI.EL.CO.+S.R.L%22'),
     ev('近期动态与线索', 'R66 19 波档案点名:SI.EL.CO. 短名谱,锚待专批锁定', 'https://www.google.com/search?q=%22SI.EL.CO.+S.R.L%22'),
     ev('联系方式与基础画像', '(谱面未锁锚;待专批)', 'https://www.google.com/search?q=%22SI.EL.CO.+S.R.L%22')],
    '意大利短名 IT 屋(锚待锁)', '守档案',
    ('—', '短名噪声谱', '无守档', '—'),
    '守档:锚谱未锁(专批待)', 'Gentile Direzione,'))

R.append(rec('A-215', 'SIM NT srl',
    'SIM NT srl(意大利 Bari,Via Ugo La Malfa 3/5/7;**1995 创 31 年;11-50 人;ISO 9001:2015+ISO/IEC 27001:2017**;**2025-26 Esperia 网架:Roma 亮相 11 家 100% 意制 system integrator 联盟=PA 云迁移国家谱!**;Antonello Giordano CEO+Giovanni Rosato Sales Manager;PNRR 谱(2023 基础建设件))',
    [('Antonello Giordano', 'CEO(LinkedIn 具名谱)', 'linkedin.com/company/simnt 谱面条', G, 'https://it.linkedin.com/company/simnt'),
     ('Giovanni Rosato', 'Sales Manager(销售直达)', 'linkedin.com/company/simnt 谱面条', G, 'https://it.linkedin.com/company/simnt'),
     ('Elisabetta Carulli', 'Software Development Specialist(开发谱)', 'linkedin.com/company/simnt 谱面条', G, 'https://it.linkedin.com/company/simnt'),
     ('Ivana Ressa', 'Inside Sales(内部销售)', 'linkedin.com/company/simnt 谱面条', G, 'https://it.linkedin.com/company/simnt')],
    [ev('决策链与对接人', 'CEO: Antonello Giordano;SALES MANAGER: Giovanni Rosato;队谱 Carulli(SW Dev)+Ressa(Inside Sales)(LI三元谱面条)', 'https://it.linkedin.com/company/simnt'),
     ev('联系方式与基础画像', 'Via Ugo La Malfa 3/5/7, 70125 Bari;dal 1995;11-50 dipendenti;ISO 9001:2015 SINCERT+ISO 27001:2017(LI+MAXQDA 伙伴页件)', 'https://www.maxqda.com/partner/sim-nt-srl'),
     ev('近期动态与线索', '**2026: SIM NT tra gli 11 system integrator di #Esperia(rete d\'imprese 100% made in Italy per la PA;Roma 件)**;2023: infrastruttura PNRR fornitura 谱(openprocurements 件)', 'https://it.linkedin.com/company/simnt')],
    '意大利巴里 31 年IT屋(Esperia 国家谱)', '11-50 人;1995 创',
    ('Esperia 联盟=PA 云谱窗', '中小实体谱', 'Giordano CEO+Rosato 销售位', '联盟链竞谱;PA 谱'),
    'Giordano CEO 直达(opt-in 律)', 'Gentile Dott. Giordano,'))

R.append(rec('A-216', 'SOTECH srl',
    'SOTECH SRL(意大利 Brescia;法址 Via Achille Grandi 43/B(BS)+运营址 Via San Felice 15/A Calvisano(BS)**;**IT 管理服务铺(24/7 远程监控+server/workstation 管理+PMI 谱)」;**官网团页全谱:Luca Paganin+Stefano Ferrari+Stefano Rolfi+Andrea Vanelli(20 年 know-how 聚合谱)**)',
    [('Luca Paganin', '团队首谱(官网团页自署)', 'sotech.srl 官网团页(O)', O, 'https://www.sotech.srl/'),
     ('Stefano Ferrari', '团队谱(官网团页)', 'sotech.srl 官网团页(O)', O, 'https://www.sotech.srl/'),
     ('Stefano Rolfi', '团队谱(官网团页)', 'sotech.srl 官网团页(O)', O, 'https://www.sotech.srl/'),
     ('Andrea Vanelli', '团队谱(官网团页)', 'sotech.srl 官网团页(O)', O, 'https://www.sotech.srl/')],
    [ev('决策链与对接人', '官网「Il nostro team」: Luca Paganin, Stefano Ferrari, Stefano Rolfi, Andrea Vanelli——「Sotech è recente, ma i suoi professionisti no! Vent\'anni di know how」(sotech.srl 自署)', 'https://www.sotech.srl/'),
     ev('联系方式与基础画像', 'Sede Operativa: Via San Felice 15/A, 25012 Calvisano(BS);Sede Legale: Via Achille Grandi 43/B, 25125 Brescia;info@sotech.srl;+39 030 23 30 226;servizi gestiti 24/7(官网件)', 'https://www.sotech.srl/')],
    '意大利布雷西亚 IT 管理服务铺(4 人团)', '小谱;20 年 know-how',
    ('团页 O 级全谱', '微实体谱', 'Paganin 首谱直达位', '区域链竞谱'),
    'Paganin 直达(opt-in 律)', 'Gentile Sig. Paganin,'))

R.append(rec('A-217', 'SSC – Software Servizi Consulting Srl',
    'SSC – Software Servizi Consulting Srl(意大利;**同名噪声群:Strategia e Sviluppo SSC(智库咨询体,域外)/ System Consulting Mazzoli 体/ SC Software Vigliano(别名体)=均已分层**;档案体谱面未见具名决策人+锚未锁→**守档准由**;R66 波次二点名待对位)',
    [],
    [ev('决策链与对接人', '公开谱面未见具名决策人=守档准由(SSC 三字母同名群大;档案全名 Software Servizi Consulting 检索未锁锚);2026-10-08 留痕', 'https://www.google.com/search?q=%22SSC+Software+Servizi+Consulting%22'),
     ev('近期动态与线索', 'R66 19 波档案点名:SSC 全名谱锚待专批锁定(异体群已分层)', 'https://www.google.com/search?q=%22SSC+Software+Servizi+Consulting+Srl%22')],
    '意大利 SSC 谱(锚待锁)', '守档案',
    ('—', '短名噪声谱', '无守档', '—'),
    '守档:锚谱未锁(专批待)', 'Gentile Direzione,'))

R.append(rec('A-218', 'STL Connext – Società Telefonica Lombarda SRL',
    'STL CONNEXT / Società Telefonica Lombarda Srl(意大利 Brescia;**33 年谱(员工轨 1991-92 起);更名谱 Società Telefonica Lombarda → STL CONNEXT(2023 前后)**;**Daniele Pozzi Direttore Operativo(1991 起 8 职级贯谱=in-house 33 年升谱!)+Marco Presti Direttore operativo(前 Responsabile acquisti 采购谱 KPI)+Matteo Ceruti Sales Manager+Massimo Braghini 技术**)',
    [('Daniele Pozzi', 'Direttore Operativo(1991 起 33 年贯谱;LI 谱面条)', 'linkedin.com/in/daniele-pozzi 谱面条', G, 'https://www.linkedin.com/in/daniele-pozzi-04b6441a3/'),
     ('Marco Presti', 'Direttore operativo(前 Responsabile acquisti 1995-2017=采购谱 KPI)', 'RocketReach 谱面条', G, 'https://rocketreach.co/marco-presti-email_229046824'),
     ('Matteo Ceruti', 'Sales Manager(销售直达)', 'RocketReach 谱面条', G, 'https://rocketreach.co/marco-presti-email_229046824'),
     ('Massimo Braghini', 'Impiegato tecnico(技术谱)', 'RocketReach 谱面条', G, 'https://rocketreach.co/marco-presti-email_229046824'),
     ('Enrica Ballini / Francesca Tufano', '客账/行政谱(支持位)', 'LI 谱面条', G, 'https://www.linkedin.com/')],
    [ev('决策链与对接人', 'Daniele Pozzi: Direttore Operativo STL CONNEXT(2018-01 至今;履 Società Telefonica Lombarda 1991-2017 共 8 级谱);Marco Presti(前 acquisti 1995-2017→direttore operativo 2023);Matteo Ceruti Sales Manager(LI/RR 谱面条)', 'https://www.linkedin.com/in/daniele-pozzi-04b6441a3/'),
     ev('联系方式与基础画像', 'Brescia;**更名谱: Società Telefonica Lombarda Srl → STL CONNEXT(2023-02 前后;员工履档谱条)**;33 年电信工程谱', 'https://www.stlconnext.it/')],
    '意大利布雷西亚 33 年电信工程屋(更名谱)', '中型谱;33 年',
    ('Presti 采购谱=KPI 直达+更名窗', '中实体谱', 'Presti/Pozzi 双运营位', '区域链竞谱'),
    'Presti 运营位(opt-in 律)', 'Gentile Sig. Presti,'))

R.append(rec('A-219', 'STORELINK S.R.L',
    'STORELINK SRL(意大利 Brescia(法址 Via Berardo Maggi 9/A)+Roma(Via E. D\'Onofrio 212)**;**P.IVA 03082480983;7 人;集成安全/能源管理+网络/ICT 谱;MePA 16 项**;**Savino Cutrona Amministratore Unico/CEO(D&B 双谱)+Emanuele Cutrona GM/Lead Negotiator(族谱)+Giovanni Difino(AI/BI PoliteMi 谱)+Virginia Castello HR**)',
    [('Savino Cutrona', 'Amministratore Unico/CEO(D&B 具名谱)', 'D&B+clodura 双源', G, 'https://www.dnb.com/business-directory/company-profiles.storelink_srl.5dae5cab536e26550d75a354614385fe.html'),
     ('Emanuele Cutrona', 'General Manager/Lead Negotiator & Product Developer(族谱)', 'clodura 谱面条', G, 'https://www.clodura.ai/directory/company/storelink-srl'),
     ('Giovanni Difino', 'AI/BI 谱(米理谱;LI 具名)', 'LinkedIn 谱面条', G, 'https://www.linkedin.com/in/giovannidifino/'),
     ('Virginia Castello', 'HR Manager(行政谱)', 'clodura 谱面条', G, 'https://www.clodura.ai/directory/company/storelink-srl')],
    [ev('决策链与对接人', 'Key Principal: SAVINO CUTRONA Sole Administrator(D&B 件);Emanuele Cutrona GM Lead Negotiator Product Developer;Giovanni Difino(AI/BI);队谱 Castello HR/Tirabassi/Ciprini(D&B+clodura+LI 三源)', 'https://www.dnb.com/business-directory/company-profiles.storelink_srl.5dae5cab536e26550d75a354614385fe.html'),
     ev('联系方式与基础画像', 'P.IVA 03082480983;Brescia Via Berardo Maggi 9/A + Roma Via D\'Onofrio 212(+39 06 40800163);7 dipendenti;Security+Energy Management+Networking/ICT;MePA 16 abilitazioni;MIBACT 集成谱(amministrazionicomunali/storelink.it 件)', 'https://www.storelink.it/it/dove-siamo')],
    '意大利布雷西亚双址安防能源集成屋', '7 人;MePA 16',
    ('安防+能源+网络三谱', '小实体谱', 'S.Cutrona AU 直达位', '一线链竞谱'),
    'Savino Cutrona 直达(opt-in 律)', 'Gentile Sig. Cutrona,'))

# ============ ES×1 ============
R.append(rec('A-220', 'Lineas y Cables S.A',
    'LINEAS Y CABLES S.A.(西班牙 Pozuelo de Alarcón(马德里),C/ Virgilio 19(影像城);**NIF A-28552149;1978-12-26 创 48 年;90 人(2025);€10-50M;TIC 系统+通信网络设备分销;电子/RF/能源实验室+2000㎡ 仓**;**AESMIDE 国防工业协会员=军防边界守界注记;2022-04 权杖换代:García de las Heras(创始)退→Alfonso Estévez Quintana 登基(家族二代谱);VP Reyes-Carlota Estévez Santiago;最新 BORME 2026-06 Reyes Carlota E. Consejero Delegado 双任**',
    [('Alfonso Estévez Quintana', 'Presidente(2022-07 起;二代接班谱)', 'BORME/datoscif/einforma 三源登记件', O, 'https://www.datoscif.es/empresa/lineas-y-cables-sa'),
     ('Reyes-Carlota Estévez Santiago', 'Vicepresidenta + Consejero Delegado 双任(2026-06 BORME 谱)', 'datoscif/BORME 件', O, 'https://www.datoscif.es/empresa/lineas-y-cables-sa'),
     ('Norberto Abascal Carmona', 'Consejero(理事)', 'BORME/einforma 件', O, 'https://www.einforma.com/informacion-empresa/lineas-cables'),
     ('Pedro Piñar de Jesús', 'Secretario(秘书处)', 'BORME/datoscif 件', O, 'https://www.datoscif.es/empresa/lineas-y-cables-sa'),
     ('Julio Peñas Artero', 'AESMIDE 会卡联络(协会谱)', 'aesmide.es 会卡', O, 'https://aesmide.es/asociado/lineas-y-cables-sa/')],
    [ev('决策链与对接人', 'BORME 谱: 2022-04 Presidente García de las Heras 退→Estévez Quintana Alfonso 任(2022-07);2026-06 Reyes Carlota E. Consejero Delegado+Consejero 双任;Consejero: Abascal Carmona Norberto;Secretario: Piñar de Jesús Pedro(datoscif/einforma 登记件)', 'https://www.datoscif.es/empresa/lineas-y-cables-sa'),
     ev('联系方式与基础画像', 'NIF A28552149;C/ Virgilio 19, 28223 Pozuelo de Alarcón(Madrid);fundada 26/12/1978;90 empleados(2025);15 administradores;laboratorios electrónica/RF/energía+almacén 2000㎡;Distribución Sistemas TIC y Equipos de Redes de Comunicaciones(infonif/aesmide 件)', 'https://infonif.economia3.com/ficha-empresa/lineas-y-cables-sa'),
     ev('近期动态与线索', '**AESMIDE(国防工业协会)会员谱=军防边界守界注记**;最新 BORME 动作 2026-06(新 Consejero Delegado 双任)', 'https://aesmide.es/asociado/lineas-y-cables-sa/')],
    '西班牙马德里 48 年 TIC 分销大户(军防会员)', '90 人;€10-50M',
    ('90 人 48 年=大户谱', '大分销谱', 'Estévez 二代换代窗位', '军防界守界注'),
    'Estévez 父子谱换代贺(opt-in 律;军防边界守界)', 'Estimado Sr. Estévez,'))

# ============ NL×1 ============
R.append(rec('A-221', 'Pijl Solutions',
    'Pijl solutions bv(荷兰 Honselersdijk(南荷兰省);**1988 创(Van der Pijl Automatisering 谱→更名);9 人/$3M;区域 ICT 伙伴**;**Arno Duijvestijn directeur/eigenaar(1992 技术员→2006 商务→algemeen directeur=34 年 in-house 升谱;官网专访 O 金谱)+Peter Operationeel Manager(官网团页)+Jeffrey Persoon SW+Arjan van Munsteren Accountmanager ICT**)',
    [('Arno Duijvestijn', 'Directeur & Eigenaar(官网专访自署=O)', 'pijlsolutions.nl 专访+LI 双源', O, 'https://www.pijlsolutions.nl/nieuws/achter_de_schermen_met_arno'),
     ('Peter(谱面单名)', 'Operationeel Manager(官网团页)', 'pijlsolutions.nl over 页(O)', O, 'https://www.pijlsolutions.nl/over-pijl-solutions'),
     ('Jeffrey Persoon', 'Software Consultant(队谱)', 'RocketReach 谱面条', G, 'https://rocketreach.co/pijl-solutions-bv-profile_b4178ae1ff897f33'),
     ('Arjan van Munsteren', 'Accountmanager ICT(销售位)', 'RocketReach 谱面条', G, 'https://rocketreach.co/pijl-solutions-bv-profile_b4178ae1ff897f33')],
    [ev('决策链与对接人', 'Arno Duijvestijn directeur en eigenaar;sinds 1992 bij Pijl solutions(technisch medewerker→2006 adviseren/verkopen→algemeen directeur)(官网专访件);Over 页团: Arno(Directeur)+Peter(Operationeel Manager)(官网 O)', 'https://www.pijlsolutions.nl/nieuws/achter_de_schermen_met_arno'),
     ev('联系方式与基础画像', 'Honselersdijk/Naaldwijk ZH;opgericht 1988(als Van der Pijl Automatisering);9 employees;$3M;ICT partner regio(rocketreach/over 页件)', 'https://www.pijlsolutions.nl/over-pijl-solutions')],
    '荷兰南荷兰 38 年区域 ICT 屋', '9 人;$3M',
    ('业主亲政]+专访 O 谱', '微实体谱', 'Duijvestijn 直达位', '区域链竞谱'),
    'Arno Duijvestijn 直达(opt-in 律)', 'Geachte heer Duijvestijn,'))

# ============ AT×3 ============
R.append(rec('A-222', 'quattroSEC Gmbh',
    'quattroSEC GmbH(奥地利 Zipf/Neukirchen a.d. Vöckla(上奥),Zipf 65 Campus Q+Wien 办;**FN 307862p(LG Wels);UID ATU66721826;2008-04-30 创;cap €35k;IT 安全专营(厂商中立;OWASP 谱)**;**Geschäftsführer Ernst Hofmann(100% 全资=唯一谱主;印谱 O)+Hannes Minimair(退任留痕谱)**',
    [('Ernst Hofmann', 'Geschäftsführer(全权唯一;100% Gesellschafter)', 'quattrosec.com Impressum+northdata 双源', O, 'https://www.quattrosec.com/unternehmen/impressum.html'),
     ('Hannes Minimair', '原 Geschäftsführer(退任留痕谱)', 'northdata 件(留痕)', G, 'https://www.northdata.com/')],
    [ev('决策链与对接人', 'Geschäftsführer: Ernst Hofmann;Firmenbuchnummer FN 307862p;UID: ATU66721826;Handelsgericht Wels;Shareholder Hofmann 100%(€35.000)(Impressum+kompany/northdata 件)', 'https://www.quattrosec.com/unternehmen/impressum.html'),
     ev('联系方式与基础画像', 'Zipf 65 - Campus Q, 4871 Zipf/Neukirchen a.d. Vöckla;gegründet 2008;Schwerpunkt IT-Sicherheit;herstellunabhängig;höchste Verschwiegenheit(印谱/WKO 件)', 'https://firmen.wko.at/quattrosec-gmbh-quattrosec-gmbh-/ober%C3%B6sterreich/')],
    '奥国上奥 IT 安全专营屋', '小微谱;2008 创',
    ('Hofman 全资独任=直达', '微实体谱', 'Hofmann 唯一直达位', '安全专营谱'),
    'Ernst Hofmann 直达(opt-in 律)', 'Guten Tag Herr Hofmann,'))

R.append(rec('A-223', 'S.A.B.E.L. Handels GmbH',
    'S.A.B.E.L. Handels GmbH(奥地利 Wien 1130,Hietzinger Hauptstrasse 22/D/2/B11B(美泉宫区);**2009-12-04 登;IT+电信增值分销(Allied Telesis+CTC Union+定制 NSP;EMEA 企客);创始双谱=Olivetti/Allied/France Telecom 老将谱;CEE B2B 定焦**;公开谱面未见具名 GF→**守档准由(网点锚全)**)',
    [],
    [ev('联系方式与基础画像', 'S.A.B.E.L. Handels GmbH, Hietzinger Hauptstrasse 22/D/2/B11B, 1130 Wien;+43 660 11 42 986;office@sabel-international.com;registriert 04.12.2009(官网 about/contact 件)', 'https://sabel-international.com/about/'),
     ev('技术与认证', 'Value-added distributor: Allied Telesis, CTC Union, custom NSP solutions;EMEA enterprise since 2009;Gründer 团队 ex-Olivetti/Allied/France Telecom(sabel-international.com 官网件)', 'https://sabel-international.com/'),
     ev('决策链与对接人', '公开谱面未见具名 Geschäftsführer=守档准由;2026-10-08 留痕(Allied 同营谱=件链窗)', 'https://sabel-international.com/')],
    '奥国维也纳 Allied/CTC 分销屋', '小微谱;2009 登',
    ('Allied 同营谱=件链窗', '微实体谱', '无守档', '—'),
    '守档:谱面无实名(网点锚全;待专批点名)', 'Sehr geehrte Damen und Herren,'))

R.append(rec('A-224', 'Salzgeber GmbH',
    'Salzgeber GmbH(奥地利 Tulln a.d. Donau(Dr.-Billroth-Str. 12)+Wien(Floridsdorfer Hauptstr. 1)+München 三址;**1996 创;11-30 人;「IT Revolutions」牌;安全/IoT/网络/媒体声像谱;Beckhoff Solution Provider**;**GF David Salzgeber(CEO;NÖ Haus der Digitalisierung 技术顾问谱+州经济谱交织;LI 活跃 O/G)+Daniel Salzgeber GF(引语件)+Elisabeth Lukas-Salzgeber GF/ppa(2005 双 GF 始谱→现 ppa);三 GF 谱+EcoNetix/One Planet/AWS 副谱**',
    [('David Salzgeber', 'Geschäftsführer/CEO(印谱+州经济件引语;digital 顾问谱)', 'it-revolutions.com+Beckhoff+meinbezirk 三源', O, 'https://www.beckhoff.com/de-at/support/solution-provider-programm/salzgeber-gmbh.html'),
     ('Daniel Salzgeber', 'Geschäftsführer(双 GF 谱;引语件)', 'meinbezirk.at 2021 件', O, 'https://www.meinbezirk.at/tulln/c-wirtschaft/high-tech-unternehmen-aus-noe-revolutioniert-die-it-branche_a4573400'),
     ('Elisabeth Lukas-Salzgeber', 'GF→Prokuristin(2005 双 GF 始谱;现 ppa)', 'northdata/karriere.at 件', G, 'https://www.northdata.com/Lukas-Salzgeber,%20Elisabeth,%20Tulln%20an%20der%20Donau/2ts')],
    [ev('决策链与对接人', 'Geschäftsführer: David Salzgeber + Daniel Salzgeber;Prokuristin(ppa): Elisabeth Lukas-Salzgeber;Registration 11/01/2005(northdata 件);州府件:「GF David Salzgeber und sein Technikerteam」+「GF Daniel Salzgeber」引语(meinbezirk 2021)', 'https://www.meinbezirk.at/tulln/c-wirtschaft/high-tech-unternehmen-aus-noe-revolutioniert-die-it-branche_a4573400'),
     ev('联系方式与基础画像', 'Dr.-Billroth-Straße 12, 3430 Tulln + Floridsdorfer Hauptstraße 1, 1210 Wien + München;gegründet 1996;11-30 Mitarbeiter;Sicherheits-/IoT-/Netzwerktechnik;Beckhoff Solution Provider;david.salzgeber@it-revolutions.com(karriere.at/beckhoff 件)', 'https://www.karriere.at/f/salzgeber-gmbh-it-revolutions'),
     ev('近期动态与线索', 'EcoNetix Gruppe(Carbon Capture)+One Planet Solutions+AWS Solutions Hub 伙伴谱;NÖ Haus der Digitalisierung 技术顾问谱(David;州政交织)=区域谱织密(LI 公司页件)', 'https://at.linkedin.com/company/salzgeber-it-revolutions')],
    '奥国下奥 30 年高新安全/IoT 屋(三址)', '11-30 人;1996 创',
    ('州政谱织密+Beckhoff 谱', '中小实体谱', 'David Salzgeber 直达位', '区域链竞谱'),
    'David Salzgeber 直达(opt-in 律)', 'Guten Tag Herr Salzgeber,'))

# ============ CH×2 ============
R.append(rec('A-225', 'DDS Netcom AG',
    'DDS NETCOM AG(瑞士 Fehraltorf(苏黎世州),Allmendstrasse 8;**CHE-107.420.295;CH-020.3.002.954-1;1992 创 34 年;AG;Kapital CHF 200k;1-10 人(XING 队谱 7)**;**网络专营(全谱 Netzwerk Produkte/Beratung/Lösungen);Webshop 谱(dds.ch);Geschäftsführer Hanspeter Weingartner(印谱+Kompass+D&B 三源 O)+Reinhard Zesiger BD Industrial Networks+Maja Wittwer Office**)',
    [('Hanspeter Weingartner', 'Geschäftsführer(印谱自署=O)', 'webshop.dds.ch Impressum+Kompass+D&B 三源', O, 'https://webshop.dds.ch/impressum'),
     ('Reinhard Zesiger', 'Business Development Manager Industrial Networks(工网 BD=落位最合)', 'XING 队谱', G, 'https://www.xing.com/pages/ddsnetcomag'),
     ('Maja Wittwer', 'Office-Managerin(行政口)', 'XING 队谱', G, 'https://www.xing.com/pages/ddsnetcomag')],
    [ev('决策链与对接人', 'Geschäftsführer: Hanspeter Weingartner;HR CH-020.3.002.954-1;MwSt CHE-107.420.295;DDS NETCOM AG Allmendstr. 8, CH-8320 Fehraltorf;+41 43 355 22 11;info@dds.ch(webshop.dds.ch Impressum 官署)', 'https://webshop.dds.ch/impressum'),
     ev('联系方式与基础画像', 'Gründungsjahr 1992;AG;Kapital CHF 200\'000;Team: Zesiger(BD Industrial Networks)+Wittwer(Office)+Patterson(store keeper);Netzwerkbereich Produkte/Beratung/Lösungen(Kompass/XING 件)', 'https://ch.kompass.com/c/dds-netcom-ag/ch094172/')],
    '瑞士苏黎世州 34 年网络专营屋', '1-10 人;1992 创',
    ('网络专营+Webshop 谱', '微实体谱', 'Weingartner 印谱直达位', '自家店链谱'),
    'Hanspeter Weingartner 直达(opt-in 律)', 'Guten Tag Herr Weingartner,'))

R.append(rec('A-226', 'FIVE Informatik AG',
    'FIVE Informatik AG(瑞士 Urtenen-Schönbühl(伯尔尼州),Bahnhofstrasse 5;**CHE-106.305.349;35+ 年谱(创始 1987 前后);Five Gruppe(与 Tax Ware AG+Alan Software AG 三驾);100+ 养老基金数字化客户谱**;**2022-09 权杖换代金谱:Ulrich Tschanz(35 年创始掌舵)→ Oliver Lyoth(前 T-Systems Schweiz 20 年;2022-09 入 2023-01 全接)=换代窗 O 件;VR-Präsident Christian Lory+ppa Alexander Schild;Heads: Engler(销售/市场/传讯)+Kunz(AI&Automation)+Freudiger(Internal IT)**',
    [('Oliver Lyoth', 'CEO(2022-09 入,2023-01 全面接;换代件官方引语)', 'organisator.ch+kleinreport.ch 双新闻件', O, 'https://www.organisator.ch/en/management/2022-08-08/oliver-lyoth-becomes-new-ceo-of-five-informatics-ag/'),
     ('Ulrich Tschanz', '创始 CEO 35 年→Verwaltungsrat(留任董事+项目谱)', 'organisator.ch 件(引语)', O, 'https://www.organisator.ch/en/management/2022-08-08/oliver-lyoth-becomes-new-ceo-of-five-informatics-ag/'),
     ('Christian Lory', 'Verwaltungsratspräsident(董事长)', 'northdata 件', G, 'https://www.northdata.com/Five%20Informatik%20AG,%20Urtenen-Sch%C3%B6nb%C3%BChl/CHE-106.305.349'),
     ('Kathrin Engler', 'Leiterin Verkauf Marketing & Kommunikation(销售/市场/传讯头;伙伴页具名)', 'symposium-2.ch 伙伴页+RR 谱', G, 'https://www.symposium-2.ch/partner/five-informatik-ag/'),
     ('Christian Kunz', 'Head of AI and Automation(AI 头)', 'RocketReach 谱面条', G, 'https://rocketreach.co/five-informatik-ag-email-format_b4526cc2fc8e13ed'),
     ('Alain Freudiger', 'Head of Internal IT / Senior Microsoft Modern Workplace Architect(内部 IT 头=落位最合)', 'RocketReach 谱面条', G, 'https://rocketreach.co/five-informatik-ag-email-format_b4526cc2fc8e13ed')],
    [ev('决策链与对接人', '「Oliver Lyoth tritt am 1. September 2022 ein und übernimmt ab 1. Januar 2023 die gesamte Geschäftsführung」;Tschanz: 「35 years ago, the foundations were laid for FIVE」→Verwaltungsrat;VR-Präsident: Christian Lory;ppa: Alexander Schild(organisator/northdata 件)', 'https://www.organisator.ch/en/management/2022-08-08/oliver-lyoth-becomes-new-ceo-of-five-informatics-ag/'),
     ev('联系方式与基础画像', 'Bahnhofstrasse 5, CH-3322 Schönbühl BE;+41 31 858 23 46;**Five Gruppe(FIVE+Tax Ware AG+Alan Software AG)**;Dokumentenmanagement/Prozessautomation/IT-Services/Finanz-Steuerberatung;**über 100 Pensionskassen 客户**(symposium-2/kleinreport 件)', 'https://www.kleinreport.ch/news/generationenwechsel-five-informatik-mit-neuem-ceo-100036/')],
    '瑞士伯尔尼州 35 年 Five Gruppe 旗舰屋', '中型谱;100+ 基金客',
    ('2023 换代窗+100+ 基金客=大谱', '集团旗舰谱', 'Lyoth CEO+Freudiger 内 IT 位', 'T-Systems 出身谱=大牌链'),
    'Lyoth 履新谱+Freudiger 内 IT(opt-in 律)', 'Guten Tag Herr Lyoth,'))

# ============ PL×2 ============
R.append(rec('A-227', 'KNT Technology SP. Z O.O',
    'KNT TECHNOLOGY SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ(波兰 Warszawa,ul. Grzybowska 87, 00-844;**KRS 0000755293;NIP 7010890163;REGON 381673442;cap 5k zł;IT 批发+零售+软件+电信综合谱**;**Prezes Zarządu: Katarzyna Elżbieta Grabiec(2025-09-04 起;股东 35/50 份额)+Jan Józef Grabiec(15/50)=族谱控股;前身谱:Katarzyna Koput(2020-02 创铺 Prezes;前 KNT Sp. z o.o. Olsztyn 战略客户总监 2018-2020=同根谱;老 KNT Sp.z o.o. KRS 698034 2024-01 法院强制解散序=守档注记)**',
    [('Katarzyna Elżbieta Grabiec', 'Prezes Zarządu(2025-09-04 起;板主+控股股东)', 'rejestr.io KRS 件', O, 'https://rejestr.io/krs/755293/knt-technology'),
     ('Jan Józef Grabiec', 'Wspólnik(股东 15/50)', 'rejestr.io KRS 件', O, 'https://rejestr.io/krs/755293/knt-technology'),
     ('Katarzyna Koput', '前 Prezes Zarządu KNT Technology(2020-02 创铺谱;LI 活跃谱=留痕待核现位)', 'linkedin.com/in/katarzynakoput(留痕谱)', G, 'https://www.linkedin.com/in/katarzynakoput/')],
    [ev('决策链与对接人', 'Prezes Zarządu: Katarzyna Elżbieta Grabiec(od 4 września 2025);Wspólnicy: Grabiec 35 udziałów(3.500 zł)+ Jan Józef Grabiec 15(1.500 zł);代表规则: każdy z członków zarządu samodzielnie(rejestr.io KRS 件)', 'https://rejestr.io/krs/755293/knt-technology'),
     ev('联系方式与基础画像', 'KRS 0000755293;NIP 7010890163;REGON 381673442;Grzybowska 87, 00-844 Warszawa;PKD: handel hurtowy(46.51.Z)/produkcja komputerów(26.20.Z)/telekomunikacja(61.10.Z)/oprogramowanie(62.01.Z)(aleo.com 件)', 'https://aleo.com/int/company/landsraad-sp-z-oo-warszawa'),
     ev('近期动态与线索', '**老 KNT Sp. z o.o.(Olsztyn,KRS 698034): 18/01/2024 sąd ogłasza wszczęcie postępowania o rozwiązanie i wykreślenie(强制解散序=守档注记);Koput 谱: Prezes KNT Technology luty 2020+(前 KNT 战略客户长 2018-2020)**', 'https://rejestr.io/krs/698034/knt')],
    '波兰华沙 IT 批发零售屋(族谱控股)', '小谱;cap 5k zł',
    ('华沙谱+老体解散注=新体窗', '微实体谱', 'Grabiec 板主直达位', '分销链竞谱'),
    'Grabiec 板主位(opt-in 律;Koput 谱留痕待核)', 'Szanowna Pani Grabiec,'))

R.append(rec('A-228', 'Nomios Poland Sp. z o. o',
    'NOMIOS POLAND SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ(波兰 Warszawa,ul. Puławska 537, 02-844;**KRS 0000406699;NIP 1070021226;REGON 145937645;2011-12-29 登;cap 100,1k zł**;**NOMIOS SAS 全资(2024-12-02 移谱,前 Mielcarek 持);实控谱 Sébastien Kher(法);Prezes Zarządu: Jacek Krzysztof Wojdal(2023-05-12 起;infras 引语件 O/G)+Członek Zarządu Artur Sadownik vel Sadowski(2021-01)+Prokura 连带 Agnieszka Magdalena Kożuchowicz(2024-10);Infradata Polska 合体谱;PWCyber 数字部合作+Rapid7 授权=**网络安全/关键业务网络/云谱**',
    [('Jacek Krzysztof Wojdal', 'Prezes Zarządu(2023-05 起;PWCyber 件官方引语)', 'rejestr.io KRS+LinkedIn PWCyber 件双源', O, 'https://rejestr.io/krs/406699'),
     ('Artur Sadownik vel Sadowski', 'Członek Zarządu(2021-01 起;实控人之一)', 'rejestr.io KRS 件', O, 'https://rejestr.io/krs/406699'),
     ('Agnieszka Magdalena Kożuchowicz', 'Prokura łączna z członkiem zarządu(2024-10 连带总代理)', 'rejestr.io KRS 件', O, 'https://rejestr.io/krs/406699'),
     ('Jarosław Mielcarek', '原 Prezes Zarządu(2012-01~2023-04 老谱;留痕)', 'vrejestr.pl KRS 件(留痕)', G, 'https://vrejestr.pl/krs/0000406699/nomios-poland')],
    [ev('决策链与对接人', 'Prezes Zarządu: Jacek Krzysztof Wojdal(od 12 maja 2023);Członek Zarządu: Artur Sadownik vel Sadowski(od 26 stycznia 2021);Prokura: Agnieszka Magdalena Kożuchowicz(od 24 października 2024);代表: dwóch członków zarządu łącznie(rejestr.io 件)', 'https://rejestr.io/krs/406699'),
     ev('联系方式与基础画像', 'KRS 0000406699;NIP 1070021226;REGON 145937645;Puławska 537, 02-844 Warszawa;zarejestrowana 29/12/2011;Wspólnik: NOMIOS SAS 100%(od 2 grudnia 2024);Beneficjenci: Kher(FR)+Wojdal+Sadownik(rejestr/aleo 件)', 'https://rejestr.io/krs/406699'),
     ev('近期动态与线索', '**Nomios Poland = Infradata Polska 合体谱;Partner PWCyber(Ministerstwo Cyfryzacji;Wojdal 引语件);Rapid7 authorized partner;portfolio Nomios Group**(LinkedIn PWCyber 件)', 'https://pl.linkedin.com/pulse/nomios-poland-sp-z-oo-partnerem-programu-wsp%C3%B3%C5%82pracy-w-joanna-dro%C5%BCd%C5%BC-1f')],
    '波兰华沙 Nomios 集团网安队(集团子谱)', '集团子谱;2011 登',
    ('网安/关键网/云=强契谱', '集团子谱', 'Wojdal 板主+Sadownik+Kożuchowicz 三位', '集团链竞谱'),
    'Wojdal 板主位(opt-in 律)', 'Szanowny Panie Wojdal,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第19波50户.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 19 波 50 户扩招批(新波幅标准 50/波):DE12(A-174~186 跳178)+IT29(189~219 跳188/196/205)+ES/NL/AT3/CH2/PL2',
               'scope': 'DE12+IT29+ES1+NL1+AT3+CH2+PL2;守档 8 户(GIS/JM/NSI/Omniconnect/PAM/SCE/SIELCO/SSC);军/密/军防边界/PA 各守界注记;双异体对位(Prinzing 双体/COMPUTER TIME 双体/GIS 三体/SCE 同名/KNT 新旧);CESSATA 差旗(Emilia);换代窗(PKE·45o/Lineas y Cables/FIVE/Salzgeber)',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 19 波 50 户扩招批落盘:',len(R))
