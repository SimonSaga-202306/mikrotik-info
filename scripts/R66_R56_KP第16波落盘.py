# -*- coding: utf-8 -*-
"""R66 第 16 波:A-135/A-136/A-137/A-138 四户。"""
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

R.append(rec('A-135', 'Acteos GmbH & Co. KG',
    'Acteos GmbH & Co. KG(德国 Gilching(巴伐利亚),Römerstr. 40, 82205;**1986 创(40 年)**;51-200 人谱(LinkedIn)/11-50 谱;info@acteos.de;+49-810538510;谱型=**Supply Chain Management 软件屋**(WMS 仓储管理/TMS 运输规划/销售规划/库存管理;prozessorientierte 咨询+定制系统解决方案(软件+硬件+通信接入)+服务维护;**法国上市 Acteos SA 100% 子公司=外资谱**)',
    [('Nidal al Safadi', 'Geschäftsführer(执行董事)', '公司 LinkedIn 员工谱+RocketReach 谱', G, 'https://de.linkedin.com/company/acteos-gmbh-&-co-kg'),
     ('Joseph Felfeli', 'Executive Board Member(执行董事会员;Key Principal)', 'DNB Key Principal 谱', G, 'https://www.dnb.com/business-directory/company-profiles/acteos-gmbh--co-kg.4a1f3a36390122c91f49586e3938e1e1.html'),
     ('Sabine Weißling', 'Manager Finance and Accounting(财务主管)', 'RocketReach 谱', G, 'https://rocketreach.co/acteos-gmbh-co-kg-management_b41fc8e9ff6bf766'),
     ('Michael Witzke', 'Senior Account Manager(资深客户经理)', 'RocketReach 谱', G, 'https://rocketreach.co/acteos-gmbh-co-kg-management_b41fc8e9ff6bf766'),
     ('Patrick Bagur', 'Key Account Manager(大客户经理 KPI 相关位)', 'RocketReach 谱', G, 'https://rocketreach.co/acteos-gmbh-co-kg-management_b41fc8e9ff6bf766')],
    [ev('业务定位', 'Acteos GmbH & Co. KG: innovative Lösungen im Bereich Supply Chain Management sowie mobile Erfassung;Beratung+Entwicklung+Implementierung(Software, Hardware, Kommunikationsanbindung);Gilching, Bayern;gegründet 1986;51–200 Beschäftigte(公司 LinkedIn 页)', 'https://de.linkedin.com/company/acteos-gmbh-&-co-kg'),
     ev('决策链与对接人', 'Key Principal: Joseph Felfeli — Executive Board Member(DNB 件);Römerstr. 40, 82205 Gilching;+49-810538510', 'https://www.dnb.com/business-directory/company-profiles/acteos-gmbh--co-kg.4a1f3a36390122c91f49586e3938e1e1.html'),
     ev('团队与规模', 'Nidal al Safadi Geschäftsführer;Sabine Weißling Manager Finance and Accounting;Michael Witzke Senior Account Manager;Patrick Bagur Key Account Manager;100% subsidiary of the French-based, listed Acteos SA(RR+CB 谱)', 'https://rocketreach.co/acteos-gmbh-co-kg-management_b41fc8e9ff6bf766')],
    '德国巴伐利亚 SCM/WMS 软件屋(法上市母谱)', '51-200 人;1986 创',
    ('40 年谱+法上市母台', '中型软件屋谱', 'Safadi GF+Felfeli 董事会位', 'SAP/大牌链竞位'),
    'Safadi GF+Bagur 大客户位(opt-in 律)', 'Guten Tag Herr Safadi,'))

R.append(rec('A-136', 'Alarm- und Sicherheitstechnik B.W. GmbH Schwerin',
    'Alarm- und Sicherheitstechnik B.W. GmbH(**总部 Oststeinbek(汉堡圈),Im Hegen 14 b, 22113**;**档案锚=Schwerin 新支谱(Zeppelinstraße 1, 19061 Schwerin;+49 385 2074 7227;官网新闻「Neue Niederlassung in Schwerin」)**;Westfalen 支谱 Halle(Westf.);**HRB 1973 RE Amtsgericht Lübeck**;**资本增资谱:2021-04 €102,500→€1,002,500**;11-50/13 员工谱;alarm-as.de;谱型=安防工程商(入侵/火灾报警、视频监控、对讲、门禁、考勤+电气安装+进口件;北德三地网)**GF 换届谱:2026-07-01 Beckmann 退出、Frank Christian Müller 新入**',
    [('Lutz Heldt', 'Geschäftsführer(执行董事;2016-08 入职位,einzelvertretungsberechtigt,Kisdorf)', 'webvalid 登记册谱', O, 'https://www.webvalid.de/company/Alarm-+und+Sicherheitstechnik+B.W.+GmbH,+Oststeinbek/HRB+1973+RE'),
     ('Frank Christian Müller', 'Geschäftsführer(执行董事;**2026-07-01 新登记**,*1972-12-29,Lippstadt)', 'creditreform 登记公告谱', O, 'https://firmeneintrag.creditreform.de/22113/2390066908/ALARM_UND_SICHERHEITSTECHNIK_B_W_GMBH'),
     ('Thomas Niemann', 'Geschäftsführer 谱位(登记册历史入谱)', 'webvalid 登记册谱(留痕)', O, 'https://www.webvalid.de/company/Alarm-+und+Sicherheitstechnik+B.W.+GmbH,+Oststeinbek/HRB+1973+RE'),
     ('Hans-Olaf Beckmann', '原 Geschäftsführer(2018 变谱;**2026-07-01 Austritt**;DNB Key Principal 旧谱留痕)', 'DNB+creditreform 双源谱(DNB 滞)', O, 'https://firmeneintrag.creditreform.de/22113/2390066908/ALARM_UND_SICHERHEITSTECHNIK_B_W_GMBH'),
     ('Oliver Haase', 'Abteilungsleiter Video(视频监控部长 KPI 天位)', 'LinkedIn 谱', G, 'https://de.linkedin.com/company/alarm--und-sicherheitstechnik-b.w.-gmbh'),
     ('Roland Lange', 'Niederlassungsleiter Westfalen(西法伦支谱长)', 'LinkedIn 谱', G, 'https://de.linkedin.com/company/alarm--und-sicherheitstechnik-b.w.-gmbh')],
    [ev('决策链与对接人', 'GF 谱:Heldt, Lutz (Kisdorf, einzelvertretungsberechtigt, Eintritt 2016);Niemann, Thomas(入谱);Beckmann, Hans-Olaf(2018 变谱 → 01.07.2026 Nicht mehr GF);Wille, Kurt(Austritt);Kapital 102.500→1.002.500 EUR(13.04.2021)', 'https://www.webvalid.de/company/Alarm-+und+Sicherheitstechnik+B.W.+GmbH,+Oststeinbek/HRB+1973+RE'),
     ev('决策链与对接人', 'Registerbekanntmachung 01.07.2026: Nicht mehr GF: Beckmann, Hans-Olaf;GF: Müller, Frank Christian, *29.12.1972, Lippstadt(creditreform 件);wird derzeit von 3 Managern geführt', 'https://firmeneintrag.creditreform.de/22113/2390066908/ALARM_UND_SICHERHEITSTECHNIK_B_W_GMBH'),
     ev('联系方式与基础画像', 'Kontakt Niederlassung Schwerin: Zeppelinstraße 1, 19061 Schwerin;Tel.: +49 (0)385 2074 7227;Niederlassung Hamburg: Im Hegen 14 b, 22113 Oststeinbek;Niederlassung Westfalen: Kleine Heide 4, 33790 Halle (Westfalen)(alarm-as.de 官网)', 'https://www.alarm-as.de/'),
     ev('团队与规模', 'Oliver Haase Abteilungsleiter Video;Robert Valentini Geschäftsführer;Roland Lange Niederlassungsleiter Westfalen;13 Mitarbeiter;Baugewerbe(LinkedIn 谱;Valentini 自署=未核,仅留痕)', 'https://de.linkedin.com/company/alarm--und-sicherheitstechnik-b.w.-gmbh')],
    '北德安防工程商(汉堡 HQ+Schwerin/Westfalen 支谱)', '13-50 人;Saar 谱',
    ('三地支谱+增资谱(×10)', '中型工程商谱', 'Haase 视频部长 KPI 直达', '大牌安防链竞位(ABUS/Bosch)'),
    'Heldt+Müller GF+Haase 视频部长(opt-in 律)', 'Guten Tag Herr Heldt,'))

R.append(rec('A-137', 'Alco Vertrieb Datentechnischer Geräte GmbH',
    'ALCO Vertrieb datentechnischer Geräte GmbH(德国 Idstein(黑森 Hochtaunus),Buchwiese 16, 65510;**HRB 18821 Amtsgericht Wiesbaden**;**1988 创(37 年;Kompass 谱;2008-02-11 北data 登记公报 GF 谱)**;0612693600;info@alcoidstein.de;谱型=**IT 系统屋/存储与打印方案分销**(Vertrieb von Computer-Systemen und Geräten jeder Art;Storagelösungen/Drucklösungen+打印机&服务器维修服务+融资方案;Kompass:NAC08 4614 机器技术商贸代理;Exportregion Westeuropa;"Investitionssicherheit für den Projektzeitraum" 官网理念)',
    [('Jörg Alberti', 'Geschäftsführer(执行董事)', '官网 Impressum 法代自署+northdata 2008 登记公报双源', O, 'https://www.alcoidstein.de/impressum/'),
     ('Heike Kasteleiner', 'ppa / Prokurist(授权代理谱)', 'northdata 登记公报谱', O, 'https://www.northdata.de/Alco%20Vertrieb%20datentechnischer%20Ger%C3%A4te%20GmbH,%20Idstein/Amtsgericht%20Wiesbaden%20HRB%2018821')],
    [ev('决策链与对接人', 'Vertreten durch: Jörg Alberti;Buchwiese 16, 65510 Idstein;Tel: 0612693600;info@alcoidstein.de;AG Wiesbaden HRB 18821(官网 Impressum)', 'https://www.alcoidstein.de/impressum/'),
     ev('决策链与对接人', '11.02.2008 Publikation: GF: Jörg Alberti;ppa: Heike Kasteleiner;Der Vertrieb von Computer-Systemen und Geräten jeder Art(northdata 登记公报)', 'https://www.northdata.de/Alco%20Vertrieb%20datentechnischer%20Ger%C3%A4te%20GmbH,%20Idstein/Amtsgericht%20Wiesbaden%20HRB%2018821'),
     ev('联系方式与基础画像', 'Gründungsjahr 1988;Führungskräfte: Jörg Alberti Geschäftsführung;Storagelösungen/Drucklösungen, Reparaturservice Drucker/Server, Finanzierungskonzepte;Export Westeuropa(Kompass 件)', 'https://de.kompass.com/c/alco-vertrieb-datentechnischer-gerate-gmbh/de687836/')],
    '德国 Idstein 存储/打印分销系统屋 37 年谱', '小实体谱;1988 创',
    ('37 年谱+西欧出口', '小实体谱', 'Alberti GF 直达位', '大牌件链竞谱'),
    'Alberti GF+Kasteleiner Prokurist(opt-in 律)', 'Guten Tag Herr Alberti,'))

R.append(rec('A-138', 'AMRO IT-Systeme GmbH',
    'AMRO IT-Systeme GmbH(德国 Weißenburg i. Bay(中弗兰肯),Treuchtlinger Straße 1, 91781;**HRB 2516 Amtsgericht Ansbach,€30,000,USt DE241783909;1996-12-04 创(30 年;原名 AMRO Soft- & Hardware Verwaltungs-GmbH)**;09141/9019-0;谱型=微软认证谱系统屋(Microsoft Certified Professionals;定制/标准软件开发+网络软硬件集成运维+电信件贸+电子元件 Konfektionierung+DV 咨询,Micro enterprise);**官网 Team 页全员邮箱直连谱**',
    [('Jürgen Reutelhuber', 'Geschäftsführer(执行董事;einzelvertretungsberechtigt,Alesheim)', '官网 Team/Datenschutz 自署+webvalid/implisense 登记册谱', O, 'https://www.amro.de/unser-team/'),
     ('Tobias Blobner', 'Prokurist+Technik(登记册 Prokurist 入谱+官网 Team 谱)', 'webvalid 登记册谱+官网 Team 页', O, 'https://www.amro.de/unser-team/'),
     ('Jörg Kaußler', 'Softwareentwicklung/Buchhaltung(软件开发+财务直通线)', '官网 Team 页(9019-24)', O, 'https://www.amro.de/unser-team/'),
     ('Florian Wagner', 'Technik(技术线)', '官网 Team 页(9019-34)', O, 'https://www.amro.de/unser-team/'),
     ('Maximilian Kraft', 'Technik(技术线)', '官网 Team 页', O, 'https://www.amro.de/unser-team/'),
     ('Ludwig Amler', '原 Geschäftsführer/Prokurist(谱系留痕;2011 变谱)', 'webvalid 登记册谱(留痕)', O, 'https://www.webvalid.de/company/AMRO+IT-Systeme+GmbH,+Wei%C3%9Fenburg/HRB+2516')],
    [ev('决策链与对接人', 'Jürgen Reutelhuber Geschäftsführer (09141/9019-0, j.reutelhuber@amro.de);Jörg Kaußler Softwareentwicklung/Buchhaltung (j.kaussler@amro.de);Tobias Blobner Technik (t.blobner@amro.de);Florian Wagner Technik;Maximilian Kraft Technik(amro.de 官网 Team 页)', 'https://www.amro.de/unser-team/'),
     ev('决策链与对接人', 'Bestellt: GF: Reutelhuber, Jürgen, Alesheim, einzelvertretungsberechtigt;Eintritt Prokurist: Blobner, Tobias;Ausgeschieden: GF Amler/Rottler 谱系(webvalid 件);HRB 2516 AG Ansbach;gegründet 04.12.1996;€30,000(implisense)', 'https://www.webvalid.de/company/AMRO+IT-Systeme+GmbH,+Wei%C3%9Fenburg/HRB+2516'),
     ev('业务定位', 'nichthandwerkliche Konfektionierung elektronischer Bauelemente;Entwicklung Individual-/Standardsoftware;Netzwerk-, Hard- und Softwarebetreuung;Handel/Vertrieb Hardware, Software, Telekommunikation;DV 咨询;Microsoft Certified Professionals', 'https://app.implisense.com/en/companies/amro-it-systeme-gmbh-weissenburg--DES8P3CP3R61')],
    '德国中弗兰肯微软认证谱 30 年微系统屋', 'Micro;1996 创;€30k',
    ('30 年谱+微软认证', '微实体谱', 'Reutelhuber GF 直达位', '大牌件链竞谱'),
    'Reutelhuber GF+Blobner Prokurist/Technik(opt-in 律)', 'Guten Tag Herr Reutelhuber,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第16波.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 16 波:Acteos(Safadi+法上市母谱)/Alarm-as B.W.(Schwerin 支谱+GF 2026 换届)/ALCO(37 年 Alberti/Kasteleiner)/AMRO(Reutelhuber+团谱邮箱直连)四户',
               'scope': 'DE×4 谱;HRB 1973RE/18821/2516 锚;Alarm-as Schwerin 档案锚已对位;Beckmann 2026-07 退出留痕',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 16 波四户落盘')
