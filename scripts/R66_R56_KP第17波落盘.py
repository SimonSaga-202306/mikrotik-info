# -*- coding: utf-8 -*-
"""R66 第 17 波:A-139/A-140/A-141/A-142 四户。"""
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

R.append(rec('A-139', 'ARCHE Systeme GmbH',
    'ARCHE Systeme GmbH(德国 Wilhelmshaven,Banter Deich 16-18, 26382;**HRB 204011 Amtsgericht Oldenburg,€25,000,LEI 5299001FYEDPIB63GS50;2009-12 创(16 年;前身谱=GF Ristau 2005-2009 Arche AG 董事会)**;+49 4421 9160;谱型=**海事/军工 IT 集成商**(登记目的原文:Production, distribution and integration of maritime and military information technology as well as complex data and communication networks;光纤技术/项目/网络技术;Data Center+Linux 谱);**军谱守界适配:军工线不触发,民用网络线窄段触达**;3 经理人谱(1 GF+2 Prokurist)',
    [('Joachim Ristau', 'Geschäftsführer(执行董事;2009-12-17 起 einzelvertretungsberechtigt;前 Arche AG 董事会 2005-2009)', '官网 Kontakt 页+companyhouse/implisense 登记册谱', O, 'https://www.arche-systeme.de/contact.htm'),
     ('Ingmar Seeberg', 'Einzelprokura+Projektleiter(登记谱授权代理 2021-11-03+官网项目主管)', 'creditreform 登记公告+官网 Kontakt 页', O, 'https://firmeneintrag.creditreform.de/26382/2370281656/ARCHE_SYSTEME_GMBH'),
     ('Julia Hoppe', 'Einzelprokura(授权代理;2021-11-03 登记,Schortens,*1965)', 'creditreform 登记公告谱', O, 'https://firmeneintrag.creditreform.de/26382/2370281656/ARCHE_SYSTEME_GMBH'),
     ('Peter Weinstock', 'Projektleiter(项目主管)', '官网 Kontakt 页', O, 'https://www.arche-systeme.de/contact.htm'),
     ('Michael Meinhardt', 'Projektleiter(项目主管)', '官网 Kontakt 页', O, 'https://www.arche-systeme.de/contact.htm')],
    [ev('决策链与对接人', 'Joachim Ristau Geschäftsführer (joachim.ristau@arche.de);Peter Weinstock Projektleiter;Ingmar Seeberg Projektleiter;Michael Meinhardt Projektleiter;+49(0)4421 9160(arche-systeme.de 官网 Kontakt 页)', 'https://www.arche-systeme.de/contact.htm'),
     ev('决策链与对接人', 'Registerbekanntmachung 03.11.2021: Einzelprokura: Hoppe, Julia (Schortens, *07.12.1965);Seeberg, Ingmar;derzeit von 3 Managern (1 GF + 2 Prokurist) geführt(creditreform 件)', 'https://firmeneintrag.creditreform.de/26382/2370281656/ARCHE_SYSTEME_GMBH'),
     ev('联系方式与基础画像', 'AG Oldenburg HRB 204011;Banter Deich 16-18, 26382 Wilhelmshaven;capital €25,000;date of articles 08.10.2009;Ristau previously board member of Arche AG Dec 2005-Nov 2009(companyhouse/northdata 件)', 'https://www.companyhouse.de/en/ARCHE-Systeme-GmbH-Wilhelmshaven'),
     ev('业务定位', 'Corporate purpose: Production, distribution and integration of maritime and military information technology as well as complex data and communication networks;Lichtwellenleitertechnik/Projekte/Netzwerktechnik(northdata/implisense 件)', 'https://www.northdata.com/ARCHE%20Systeme%20GmbH,%20Wilhelmshaven/Amtsgericht%20Oldenburg%20HRB%20204011')],
    '德国 Wilhelmshaven 海事/军工 IT 集成商(军线守界)', '小实体谱;2009 创;€25k',
    ('军品登记目的=高规格谱', '军谱守界段', 'Ristau GF 直达位', '大牌件链竞谱'),
    'Ristau GF+Seeberg/Hoppe Prokurist(军线守界;opt-in 律)', 'Guten Tag Herr Ristau,'))

R.append(rec('A-140', 'Bachert Datentechnik GmbH',
    'Bachert Datentechnik GmbH(德国 Wetzlar(黑森,近法兰克福),Schanzenfeldstraße 14, 35578;**HRB 1066 Amtsgericht Wetzlar(老号!)USt DE 112597233;1989 创(37 年;官网「seit über 30 Jahren immer einen Schritt voraus」)**;11-50 人;+49 6441 4478-0;info@/vertrieb@/support@bachert.de;谱型=通信系统屋(布线/有源网络/无线/会议技术/数据中心/监控系统;医疗设备场景谱;**LANCOM Solution Partner 多年+BSI 认证高安网(NSA 议题 Newsletter 件)**=德式数据主权文化)',
    [('Thomas Bachert', 'Geschäftsführung(执行董事;业主姓,Bachert=姓氏下档)', '官网 Team 页+XING Impressum 双源', O, 'https://www.bachert.de/ueber-uns/unser-team/'),
     ('Bruno Werner', 'Vertriebsleitung(销售主管 SKU 位;06441-4478-124)', '官网 Team 页', O, 'https://www.bachert.de/ueber-uns/unser-team/'),
     ('Isabella Ender', 'Leitung Einkauf und Auftragsabwicklung(**采购主管 KPI 天位**;4478-141)', '官网 Team 页', O, 'https://www.bachert.de/ueber-uns/unser-team/'),
     ('Jonas Friedrich', 'Sachbearbeitung Einkauf und Auftragsabwicklung(采购组)', '官网 Team 页 Übersicht', O, 'https://www.bachert.de/ueber-uns/unser-team/uebersicht/'),
     ('Jorge Vieira', 'Technischer Leiter / Projektleitung(技术总监)', '官网 Team 页', O, 'https://www.bachert.de/ueber-uns/unser-team/'),
     ('André Diegel', 'Obermonteur(首席安装工)', '官网 Team 页', O, 'https://www.bachert.de/ueber-uns/unser-team/'),
     ('Christine Zipp', 'Personalwesen(人事)', '官网 Team 页', O, 'https://www.bachert.de/ueber-uns/unser-team/')],
    [ev('决策链与对接人', 'Thomas Bachert Geschäftsführung (thomas.bachert@bachert.de);Bruno Werner Vertriebsleitung;Isabella Ender Leitung Einkauf und Auftragsabwicklung;Jorge Vieira Technischer Leiter;bsi-team(bachert.de Team 页全谱邮箱)', 'https://www.bachert.de/ueber-uns/unser-team/'),
     ev('联系方式与基础画像', 'Vertretungsberechtigter Geschäftsführer: Thomas Bachert;HRB 1066 AG Wetzlar;Ust DE 112597233;Schanzenfeldstraße 14, 35578 Wetzlar;+49 6441 44780;gegründet 1989(XING Impressum 件)', 'https://www.xing.com/pages/bachertdatentechnikgmbh/about_us'),
     ev('业务定位', 'Bachert Datentechnik ist langjähriger LANCOM Solution Partner;BSI-zertifizierte Hochsicherheit gegen Abhören für kritische Infrastrukturen(Newsletter 件);Zukunftsweisende Netzwerkverkabelung, Konferenztechnik, Rechenzentren, Überwachungssysteme, Drahtlos', 'https://bachert.de/news/?cHash=324c967fe0ade40341c51374a99fdf40&tx_ttnews%5Btt_news%5D=1170')],
    '德国 Wetzlar 37 年通信系统屋(LANCOM 高安谱)', '11-50 人;1989 创',
    ('37 年谱+LANCOM 高安位', '小实体谱', 'Ender 采购主管 KPI 直达', 'LANCOM/大牌链竞位'),
    'Bachert GF+Ender 采购主管+Werner 销售(opt-in 律)', 'Guten Tag Frau Ender,'))

R.append(rec('A-141', 'BAIEN GmbH',
    'BAIEN GmbH(德国 Böhl-Iggelheim(莱法州莱茵-普法尔茨圈),Eisenbahnstraße 24-26, 67459;**HRB 66432 Amtsgericht Ludwigshafen a.Rhein**;**2000 创(26 年;官网「25 Jahre BAIEN」+VISION 2030)**;11-50 人;baien.de;谱型=IT Reseller→IT Service Provider 升级谱(硬件/软件/网络/服务/咨询;**Digital Transformation Partner;客户面=企业/组织/公共部门三线谱**;「the human company」谱面)',
    [('Beate Ender', 'Geschäftsführung (CEO)', 'Kompass 法定高管谱(单源,G 位;待强化)', G, 'https://de.kompass.com/c/baien-gmbh/de891102/')],
    [ev('决策链与对接人', 'Führungskräfte BAIEN GmbH: Beate Ender Geschäftsführung (CEO);Eisenbahnstrasse 24, 67459 Böhl-Iggelheim(Kompass 件)', 'https://de.kompass.com/c/baien-gmbh/de891102/'),
     ev('联系方式与基础画像', 'BAIEN GmbH;HR-Nr. HRB 66432;Amtsgericht Ludwigshafen a.Rhein;Eisenbahnstraße 24-26, 67459 Böhl-Iggelheim(cylex 件)', 'https://web2.cylex.de/firma-home/baien-gmbh-13747543.html'),
     ev('团队与规模', 'Vom IT Reseller zum IT Service Provider. BAIEN feiert 25 Jahre Firmengeschichte;Als Digital Transformation Partner für Unternehmen, Organisationen und den öffentlichen Sektor;11-50 Beschäftigte;gegründet 2000(官网+LinkedIn 谱)', 'https://baien.de/')],
    '德国莱法 26 年 IT 转服商(公共部门谱)', '11-50 人;2000 创',
    ('26 年谱+VE 公共面', '小实体谱', 'Ender GF 谱位', '大牌件链竞谱'),
    'Ender GF 单源谱(待强化;opt-in 律)', 'Guten Tag Frau Ender,'))

R.append(rec('A-142', 'bod networks GmbH',
    'bod networks GmbH(德国 Chemnitz(萨克森),Schönherrstraße 8, 09113(Schönherrfabrik 厂区租户谱);**HRB 9168 Amtsgericht Chemnitz(官网 Impressum 记 9186=一字异文留痕);VAT DE159286113;资本 €51,200;原名 Beyer & Otto Datennetze GmbH(2003 创 Taura,2017-04 更名 bod networks)**;0371 431440;mail@bod-networks.de;谱型=化学品工业区谱小网技术屋(IT 基础设施「vom Kabel bis zum Server 从线缆到服务器」全段;0-9 人)',
    [('Udo Beyer', 'Geschäftsführer(Ing. für Informatik;创位谱 Beyer & Otto 联合创始)', '官网 Impressum 法代自署+Kompass 高管谱+Schönherrfabrik 租户页三源', O, 'https://www.bod-networks.com/impressum/'),
     ('Stephan Otto', '原 Geschäftsführer(2017-01-03 Austritt=Beyer & Otto 另一名联合创始)', 'northdata 登记系谱(留痕)', O, 'https://www.northdata.com/bod%20networks%20GmbH,%20Chemnitz/HRB%209168')],
    [ev('决策链与对接人', 'Vertreten durch: Udo Beyer, Ing. für Informatik;bod networks GmbH, Schönherrstr. 8, 09113 Chemnitz;AG Chemnitz HRB(官网为 9186;creditreform/northdata 为 9168=异文留痕)', 'https://www.bod-networks.com/impressum/'),
     ev('联系方式与基础画像', 'Ansprechpartner: Udo Beyer;Telefon: 0371 431440;mail@bod-networks.de;Wir sind eine Netzwerktechnik-Firma aus Chemnitz. Unsere Leistungen: IT-Infrastruktur - vom Kabel bis zum Server!(Schönherrfabrik 租户页)', 'https://www.schoenherrfabrik.de/de/Unsere-Mieter/Alle-Branchen_1366.html?shf_tenant1677.id=1'),
     ev('决策链与对接人', '24 Apr 2017: Name bod networks GmbH;Capital €51,200;3 Jan 2017: No longer MD: Stephan Otto;7 Oct 2003 创为 Beyer & Otto Datennetze GmbH(Seat Taura);Udo Beyer CEO Geschäftsführung(Kompass);0-9 Employees;VAT DE159286113', 'https://www.northdata.com/bod%20networks%20GmbH,%20Chemnitz/HRB%209168')],
    '德国萨克森化厂区 23 年谱小网络技术屋', '0-9 人;2003 创;€51.2k',
    ('23 年谱+厂区租户节', '微实体谱', 'Beyer GF 直达位', '大牌件链竞谱'),
    'Beyer GF 直达(微谱;opt-in 律)', 'Guten Tag Herr Beyer,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第17波.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 17 波:ARCHE(军工谱守界)/Bachert(Ender 采购+LANCOM)/BAIEN(Ender GF 单源)/bod(Beyer 原名谱+HRB 异文)四户',
               'scope': 'DE×4 谱;HRB 204011/1066/66432/9168 锚;ARCHE 军线守界注记;bod HRB 9186/9168 异文留痕',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 17 波四户落盘')
