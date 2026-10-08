# -*- coding: utf-8 -*-
"""R66 第 18 波(30 户扩招批):A-143..A-173(跳 A-153 同系)。"""
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

R.append(rec('A-143', 'buerodata AG',
    'buerodata AG(德国 Stadtlohn,Vredener Str. 119;**HRB 3051 AG Coesfeld;1988 创 38 年;日本 Ricoh 集团全资谱**;10-49 人;IT 咨询+云/DC+ERP;领域洞察「专人固定联络人」运营模)',
    [('Reinhold Laurich', 'Vorstand/CEO(1986 起 40 年在任;兼 condata GmbH & Co. KG GF)', 'wer-zu-wem/DNB/XING/implisense 四源谱', G, 'https://www.wer-zu-wem.de/firma/buerodata.html'),
     ('Christian Rothering', 'IT 咨询固定联络人(官网业务页具名 crothering@buerodata.de)', 'buerodata.de 官网业务页', O, 'https://www.buerodata.de/Mobile/Layout/ContentPages/frmITSupportOutsourcing.aspx')],
    [ev('决策链与对接人', 'Geschäftsführung: Reinhold Laurich;Eigentümer: Ricoh (Japan);HRB 3051 Coesfeld;gegründet 1988;10-49 Mitarbeiter;Bis 10 Mio. Umsatz', 'https://www.wer-zu-wem.de/firma/buerodata.html'),
     ev('团队与规模', 'Ihr Ansprechpartner: Christian Rothering +49 2563 9305 400 crothering@buerodata.de(官网 IT Outsourcing 页具名)', 'https://www.buerodata.de/Mobile/Layout/ContentPages/frmITSupportOutsourcing.aspx')],
    '德国西法伦 38 年 IT 咨询屋(Ricoh 全资)', '10-49 人;1988 创',
    ('日资母台 38 年谱', '小实体谱', 'Laurich 老铺直达位', '大牌件链竞谱'),
    'Laurich Vorstand+Rothering 联络人(opt-in 律)', 'Guten Tag Herr Laurich,'))

R.append(rec('A-144', 'CompData Computer GmbH',
    'CompData Computer GmbH(德国 Albstadt,Eschachstr. 9;**HRB 400221 AG Stuttgart;USt DE144848633;1976 创 50 年;80+ 人/€15M(2022,+10%)**;工业中型客谱:Ai;烘焙行业 ERP 专谱(BACKHAUS MAHL 等背书);TOP100 2021 创新谱)',
    [('Reiner Veit', 'geschäftsführender Gesellschafter(高管合伙人;TOP100/back.intern 官方引语)', 'compdata.de Impressum+TOP100+back.intern 三源', O, 'https://www.compdata.de/impressum'),
     ('Stefan Baumann', '「Make IT simple」技术谱', '公司 LinkedIn 员工谱', G, 'https://de.linkedin.com/company/compdata-computer-gmbh'),
     ('Alexandra Krebs', 'Personalwesen(人事)', '公司 LinkedIn 员工谱', G, 'https://de.linkedin.com/company/compdata-computer-gmbh')],
    [ev('决策链与对接人', 'Geschäftsführender Gesellschafter: Reiner Veit;HRB 400221 Stuttgart;Eschachstr. 9, 72459 Albstadt;+49 7431 950-0(官网 Impressum)', 'https://www.compdata.de/impressum'),
     ev('团队与规模', 'Compda 2022 Umsatz 15 Mio. Euro(+10%);über 80 Mitarbeiter;gegründet 1976;Reiner Veit 引语(back.intern/top100 件)', 'https://www.back-intern.de/2023/02/02/compdata-bleibt-auf-wachstumskurs/')],
    '德国巴符 50 年 IT 系统+烘焙 ERP 屋', '80+ 人;€15M;1976 创',
    ('50 年谱+行业纵深(烘焙)', '中型屋谱', 'Veit 合伙人直达位', '大牌件链竞谱'),
    'Veit 合伙人+50 年谱问候(opt-in 律)', 'Guten Tag Herr Veit,'))

R.append(rec('A-145', 'dainox GmbH',
    'dainox GmbH(德国 Bad Wörishofen,Hans-Böckler-Str. 5;**HRB 20193 AG Memmingen;2013-04 Neueintragung;€25k;31 员工**;**2025 CWIX 军演=FMN Comms/FMN Core Services 联络,BAAINBw+NATO ACT 直客谱!军谱守界加厚**;网络/电信工程+软件开发;安全顾问谱)',
    [('Alfred Brodt', 'Geschäftsführer + Network Architect(einzelvertretungsberechtigt;Impressum 四 GF 首谱)', 'dainox.net Impressum+creditreform 登记谱', O, 'https://www.dainox.net/impressum/'),
     ('Andreas Dempfle', 'Geschäftsführer(四 GF 编)', 'dainox.net Impressum', O, 'https://www.dainox.net/impressum/'),
     ('Stefan Haselhoff', 'Geschäftsführer', 'dainox.net Impressum', O, 'https://www.dainox.net/impressum/'),
     ('Dr. Artavazd Tarhanjan', 'Geschäftsführer', 'dainox.net Impressum', O, 'https://www.dainox.net/impressum/'),
     ('Bernd Kohler', 'Security Consultant', 'XING 员工谱', G, 'https://www.xing.com/pages/dainoxgmbh/employees')],
    [ev('决策链与对接人', 'Vertretungsberechtigte Geschäftsführer: Alfred Brodt, Andreas Dempfle, Stefan Haselhoff, Dr. Artavazd Tarhanjan(dainox.net Impressum 法定自署)', 'https://www.dainox.net/impressum/'),
     ev('团队与规模', 'Juni 2025: Experten-Team im Auftrag von BAAINBw und NATO ACT bei CWIX in FMN Comms (PCN) und FMN Core (Audio/Video Collaboration) federführend(XING 公司页);31 Mitarbeiter', 'https://www.xing.com/pages/dainoxgmbh'),
     ev('联系方式与基础画像', 'HRB 20193 Memmingen;Neueintragung 25.10.2022(Brodt, Alfred einzelvertretungsberechtigt);Erbringung von IT-Dienstleistungen Netzwerk/Telekom(creditreform 件)', 'https://firmeneintrag.creditreform.de/86825/8270305508/DAINOX_GMBH')],
    '德国下巴伐利亚 31 人军谱网络工程屋(BAAINBw/NATO 守界)', '31 人;2013 创',
    ('军谱核心=最高守界', '军线守界段', '四 GF 谱全位', '大牌军件链竞谱'),
    '军谱守界:仅民窄段试探(opt-in 律)', 'Guten Tag Herr Brodt,'))

R.append(rec('A-146', 'Dallmeier Electronics GmbH',
    'Dallmeier electronic GmbH & Co.KG(Regensburg,Bahnhofstr. 16(总部)+Cranachweg 1(产基);**HRA 6827/HRB 9085 AG Regensburg;USt DE813790649;1984 创 42 年;400+ 人现场产**;**全球 CCTV/IP 视频安全一件套商(自家全景厂 made in Germany;银行/赌场/机场/加油站/城市监控)**;**家族名:现年 CEO 与创始人同姓父子谱;评根:带堡垒类客户谱**',
    [('Thomas Dallmeier', 'CEO/Geschäftsführer(Impressum 法定自署)', 'dallmeier.com Impressum + GIT SICHERHEIT 访谈', O, 'https://www.dallmeier.com/de/impressum'),
     ('Dieter Dallmeier', 'Gründer(创始谱;GIT 访谈留痕)', 'git-sicherheit.de 访谈件(留痕)', O, 'https://www.git-sicherheit.de/firmen/dallmeier-electronic-gmbh-co-kg'),
     ('Georg Martin M.A.', 'Chief Communications Officer(CCO;Impressum 编辑责任自署)', 'dallmeier.com Impressum+XING about-us', O, 'https://www.dallmeier.com/de/impressum')],
    [ev('决策链与对接人', 'Vertreten durch den Geschäftsführer Thomas Dallmeier CEO;Georg Martin CCO;HRA 6827/HRB 9085 Regensburg;DE813790649;Dallmeier GmbH persönlich haftende Gesellschafterin(官网 Impressum)', 'https://www.dallmeier.com/de/impressum'),
     ev('团队与规模', '1984 创;400 Employees (site);einer der weltweit führenden Anbieter von netzwerkbasierter Videosicherheitstechnik;cassette/Banken/Casinos/Airports/Tankstellen/Stadtüberwachung(keytobavaria 件)', 'https://www.keytobavaria.com/company-details/dallmeier-electronic-gmbh-cokg-17051'),
     ev('决策链与对接人', 'Top Player Videosicherheit – Thomas Dallmeier, CEO Dallmeier electronic(GIT SICHERHEIT Interview);Dieter Dallmeier, Gründer und CEO(旧访留痕)', 'https://www.git-sicherheit.de/firmen/dallmeier-electronic-gmbh-co-kg')],
    '德国 42 年全球视频安全一件套商(Regensburg)', '400+ 人;1984 创',
    ('一线厂全件自产', '大型屋谱', 'Dallmeier 家族直达位', '自家链栈=不占',
     '带元难谱(一件套商)'),
    'Thomas Dallmeier CEO 谱位(opt-in 律)', 'Guten Tag Herr Dallmeier,'))

R.append(rec('A-147', 'Daten- und Telekommunikations-GmbH Dessau',
    'Daten- und Telekommunikations-GmbH Dessau(「DATEL」;Dessau-Roßlau,Albrechtstr. 48;**HRB 15048 Stendal;€50k;1997-12-22 创;USt DE192067013;402 人/€274.6M(集团谱口径)**;**Stadtwerke Dessau 子公司=地方 FTTH/电视/固定网运营商(B2C+市政);谱面对其自营城集团+自家市民服务;距接入链=FTTH 谱**;datel-dessau.de',
    [('Dino Wolfgang Höll', 'Geschäftsführer(现任;登记谱 2018+)', 'implisense/webvalid 登记册谱', O, 'https://app.implisense.com/en/companies/daten-und-telekommunikations-gmbh-dessau-dessau-rosslau--DEJ5ILDOVM07'),
     ('Torsten Henze', 'Einzelprokura(独代理,2022-12-12 在册)', 'webvalid 登记公告谱', O, 'https://www.webvalid.de/company/Daten-+und+Telekommunikations-GmbH+Dessau,+Dessau-Ro%C3%9Flau/HRB+15048'),
     ('Fred Kitzing', 'Einzelprokura(2022-12-12 在册)', 'webvalid 登记公告谱', O, 'https://www.webvalid.de/company/Daten-+und+Telekommunikations-GmbH+Dessau,+Dessau-Ro%C3%9Flau/HRB+15048')],
    [ev('决策链与对接人', 'Geschäftsführer: Dino Wolfgang Höll(implisense);12.12.2022: Ausgeschieden GF Zänger, Thomas;Einzelprokura: Henze, Torsten + Kitzing, Fred(webvalid 件)', 'https://app.implisense.com/en/companies/daten-und-telekommunikations-gmbh-dessau-dessau-rosslau--DEJ5ILDOVM07'),
     ev('联系方式与基础画像', 'Albrechtstr. 48, 06844 Dessau-Roßlau;HRB 15048 Stendal;gegründet 22.12.1997;€50,000;Stadtwerke Dessau 子公司;FTTH 1.000 Mbit/s + WebTV/BasisTV(viaductus/implisense 件)', 'https://www.viaductus.de/firma/DE-W1215-HRB-15048-daten-und-telekommunikations-gmbh-dessau-dessau-rosslau')],
    '德国 SA 市政 FTTH/电视运营商(Stadtwerke 子)', '集团 402 人;1997 创',
    ('城网运营谱', '电网子内治守界', 'Höll GF 直达位', '大牌骨干链竞谱'),
    'Höll GF+Henze/Kitzing Prokurist(opt-in 律;市政守界)', 'Guten Tag Herr Höll,'))

R.append(rec('A-148', 'Döhler DatenSysteme GmbH',
    'Döhler DatenSysteme GmbH(德国 Köln-Lindenthal,Wittgensteinstr. 23;**HRB 20554 AG Köln;€11,111.11;30+ 年谱;10-19 人**;「DDS」;谱型=Köln 型 IT 房(PC/服务器订配+维修+长期 IT 维护;客户群=保险/法治/教育/中产企业);dds-computer.de',
    [('Dipl.-Ing. Klaus Döhler', 'Geschäftsführer(业主姓;Nachrichtentechnik)', '官网 dds-computer.de+Kompass+LinkedIn 三源', O, 'https://dds-computer.de/'),
     ('Manfred Eßer', 'Mitgeschäftsführer(联席执行长)', '官网 dds-computer.de 自署', O, 'https://dds-computer.de/')],
    [ev('决策链与对接人', 'Geführt von Dipl.-Ing. Klaus Döhler und Mitgeschäftsführer Manfred Eßer;Seit mehr als 30 Jahren in Köln-Lindenthal;Kunden: Versicherungen, Rechtswesen, Bildung(dds-computer.de 官网)', 'https://dds-computer.de/'),
     ev('联系方式与基础画像', 'HRB 20554 Köln;€11.111,11;Wittgensteinstr. 23, 50931 Köln;10-19 Mitarbeiter;Geschäftsführung: Klaus Döhler(implisense/kompass 件)', 'https://de.kompass.com/c/dohler-datensysteme-gmbh/de889958/')],
    '德国 Koeln 30 年 IT 维护房', '10-19 人;30+ 年',
    ('双业主 30 年谱', '小实体谱', 'Döhler/Eßer 双直达位', '大牌件链竞谱'),
    'Döhler+Eßer 双 GF(opt-in 律)', 'Guten Tag Herr Döhler,'))

R.append(rec('A-149', 'Dresdner ProSoft GmbH',
    'Dresdner ProSoft GmbH(德国 Dresden,Zellescher Weg 3;**HR B 1104 AG Dresden;USt DE 140125400;1990 创 36 年**;11-50 人;谱型=Dresden 城区 IT 系统房(VERTIV 伙伴：USV/机柜/机房件;Datacenter+网络方案;同系 ProSoft Krippner GmbH(Krippner/Wohlfeld GF 独立屋）=姊妹谱)',
    [('Uwe Mees', 'Geschäftsführer(双 GF;uwe.mees@)', '官网 Impressum+DS-GVO 页 双源', O, 'https://www.dresdner-prosoft.com/impressum/'),
     ('Frank Kwasny', 'Geschäftsführer(双 GF;geschäftsführender Gesellschafter)', '官网 Impressum+XING+prosoft-krippner Standorte', O, 'https://www.dresdner-prosoft.com/impressum/'),
     ('Michael Hentschel', 'Externer Datenschutzbeauftragter (TÜV) + IT-Consultant/Projektmanager', 'XING+官网 DS 页', G, 'https://www.dresdner-prosoft.com/datenschutzerklaerung/'),
     ('Sarah Lange', 'Marketing', 'XING 员工谱', G, 'https://de.linkedin.com/company/dresdner-prosoft-gmbh')],
    [ev('决策链与对接人', 'Geschäftsführer: Uwe Mees, Frank Kwasny;HR B 1104 Dresden;USt DE 140125400;Zellescher Weg 3, 01069 Dresden(官网 Impressum)', 'https://www.dresdner-prosoft.com/impressum/'),
     ev('团队与规模', 'Michael Hentschel: Externer DSB (TÜV)/IT-Consultant;Sarah Lange Marketing;gegründet 1990;VERTIV Partner;ProSoft Krippner 同系谱(Standorte 件)', 'https://www.dresdner-prosoft.com/datenschutzerklaerung/')],
    '德国 Dresden 36 年系统房(VERTIV 伙伴)', '11-50 人;1990 创',
    ('36 年谱+VERTIV 机件', '小实体谱', '双 GF 直达位', '一线链竞谱'),
    'Mees/Kwasny 双 GF(opt-in 律)', 'Guten Tag Herr Mees,'))

R.append(rec('A-150', 'Eckmann Spezialkabel GmbH',
    'Eckmann Spezialkabel GmbH(德国 Quickborn,Friedrich-List-Str. 7;**2000 创 26 年;Eckmann Unternehmensgruppe(甲 Eckmann datacom 姊妹谱)**;5-50 人;$2.8M;谱型=**家族电缆/数据/广播/多媒体专批商**(Marine & Offshore/Petrochemie/工业特缆;Data Center+Netzwerk 全谱;旧谱 Frankfurt Oehleckerring+Saarbrücken 曾两店=史谱)',
    [('Kai Eckmann', 'Geschäftsführer(业主姓;kai.eckmann@)', '官网 Team 页+XING+RR 三源', O, 'https://www.eckmann-spezialkabel.co/unser-team'),
     ('Michael Kramer', 'Technischer Vertrieb Multimedia/Netzwerk/Verkabelung(技术销售=KPI 相关位)', '官网 Team 页', O, 'https://www.eckmann-spezialkabel.co/unser-team'),
     ('Olaf Weigel', 'Technischer Vertrieb 同上', '官网 Team 页', O, 'https://www.eckmann-spezialkabel.co/unser-team'),
     ('Stefanie Hönkhaus', 'Technischer Vertrieb Kabel/Leitungen(电缆线销售)', '官网 Team 页', O, 'https://www.eckmann-spezialkabel.co/unser-team'),
     ('Sarah Schenk', 'Vertriebsinnendienst(销售内勤)', '官网 Team 页', O, 'https://www.eckmann-spezialkabel.co/unser-team')],
    [ev('决策链与对接人', 'Kai Eckmann Geschäftsführer (kai.eckmann@eckmann.de);Michael Kramer/Olaf Weigel/Stefanie Hönkhaus Technischer Vertrieb;Sarah Schenk Vertriebsinnendienst(+49 4106 12120-0;官网 Unser Team 全谱)', 'https://www.eckmann-spezialkabel.co/unser-team'),
     ev('联系方式与基础画像', 'Friedrich-List-Str. 7, 25451 Quickborn;gegründet 2000;Eckmann Unternehmensgruppe 中程 datacom 姊妹;Marine & Offshore/Studiotechnik/Industrie & Raffinerie/Netzwerktechnik(lieferanten/RR/XING 件)', 'https://www.lieferanten.de/lieferant-25601-eckmann-spezialkabel-gmbh.html')],
    '德国 Quickborn 26 年特缆专批商(家族)', '5-50 人;€2.8M;2000 创',
    ('家族 26 年谱+海洋件', '小实体谱', 'Kramer 技术销售 KPI 直达', '大牌线缆链竞谱'),
    'Kramer/Weigel 技术销售+Schenk 内勤(opt-in 律)', 'Guten Tag Herr Kramer,'))

R.append(rec('A-151', 'GBS TEMPEST & Service GmbH',
    'GBS TEMPEST & Service GmbH(德国 Diepholz,von-Braun-Straße 6;**HRB 201609 AG Walsrode;€25k;2009-01-19 创;DE815044502;IHK Hannover**;**BSI 官方认定的 TEMPEST/SDIP 27 认证屋+四 BSI 认可放射测实验室=军密/国安器乐段,守界最高级**;11-50 人)',
    [('Ömer Cevik', 'Gesellschafter-Geschäftsführer(业主兼执行长;2009 起 einzelvertretungsberechtigt,Köln)', '官网 Imprint+wirtschaftsforum+webvalid 登记册三源', O, 'https://www.gbs-tempest.de/en/imprint.php'),
     ('Marco Husmann', 'Prokurist + Key Account Manager(2017-09-07 Einzelprokura,Drebber)', 'webvalid 登记公告+LinkedIn 员工谱', O, 'https://www.webvalid.de/company/GBS+TEMPEST+&+Service+GmbH,+Diepholz/HRB+201609'),
     ('Andrea Meyer', 'Vertriebsassistentin(销售助理)', '公司 LinkedIn 员工谱', G, 'https://de.linkedin.com/company/gbs-tempest-service-gmbh')],
    [ev('决策链与对接人', 'Chief Executive: Ömer Cevik;HRB 201609 Walsrode;DE815044502;von-Braun-Straße 6, 49356 Diepholz(官网 Imprint)', 'https://www.gbs-tempest.de/en/imprint.php'),
     ev('决策链与对接人', 'Einzelprokura: Husmann, Marco, Drebber, Eintritt 07.09.2017(webvalid 件);BSI anerkanntes Unternehmen;vier BSI-anerkannte Abstrahlprüflabore;TEMPEST/SDIP 27(wirtschaftsforum 件)', 'https://www.wirtschaftsforum.de/gbs-tempest-service-gmbh')],
    '德国 NI BSI 认定 TEMPEST 认证屋(涉密守界)', '11-50 人;2009 创',
    ('军密段位=最高守界', '涉密段不触界', 'Cevik 业主直达位(仅民窄)', '军件链=不竞'),
    '守界最高级:民窄试探+明示界(opt-in 律)', 'Guten Tag Herr Cevik,'))

R.append(rec('A-152', 'Gretsch-Unitas GmbH Baubeschläge',
    'Gretsch-Unitas GmbH Baubeschläge(Ditzingen;**HRB 202061 AG Stuttgart;资本 €8,000,000(2008 增资);GmbH 2006-03-08 创(GU 牌 1907 源)**;**GU 集团门类:窗门五金/门禁/自动开闭/楼宇管理+烟排 RWA;三代家族 of Resch 族谱(2023-11 老铺故 → 其弟继位)**;集团下 GU Automatic/BKS GmbH/Ferco S.A.S.',
    [('Dr.-Ing. Jörg Teunissen', 'Geschäftsführer(**2025-04-01 新任**;Elektrotechnik 博士;Bielefeld)', 'glaswelt/baulinks 行业报+online-handelsregister 登记公告', O, 'https://www.glaswelt.de/fenster/neue-fuehrungsspitze-dr-teunissen-jetzt-gf-der-unit-baubeschlaege-bei-gretsch-unitas'),
     ('Michael Helmut Edler von Resch', 'Geschäftsführer(2023-12-06 起;GU 集团三代业主+CEO)', 'online-handelsregister 登记公告+glaswelt 专文', O, 'https://www.online-handelsregister.de/handelsregisterauszug/bw/Stuttgart/HRB/202061/Gretsch-Unitas-GmbH-Baubeschlaege'),
     ('Manfred Künzel', 'Geschäftsführer(companyhouse 谱位)', 'companyhouse 谱', G, 'https://www.companyhouse.de/Gretsch-Unitas-GmbH-Baubeschlaege-Ditzingen'),
     ('Christian Choffat', 'Gesamtprokurist(2025-04-10 总代理)', 'online-handelsregister 登记公告', O, 'https://www.online-handelsregister.de/handelsregisterauszug/bw/Stuttgart/HRB/202061/Gretsch-Unitas-GmbH-Baubeschlaege')],
    [ev('决策链与对接人', 'Zum 1. April 2025: Dr.-Ing. Jörg Teunissen neuer GF, gemeinsam mit Michael von Resch;Julius von Resch †23.11.2023 → Bruder Michael übernimmt;GU-Gruppe drifdritt Generation Familie von Resch(glaswelt 件)', 'https://www.glaswelt.de/fenster/neue-fuehrungsspitze-dr-teunissen-jetzt-gf-der-unit-baubeschlaege-bei-gretsch-unitas'),
     ev('联系方式与基础画像', 'HRB 202061 Stuttgart;Stammkapital €8.000.000;Gründung 08.03.2006;Prokura: Choffat (Gesamtprokura 10.04.2025)/Faller(17.04.2025)(online-handelsregister 件)', 'https://www.online-handelsregister.de/handelsregisterauszug/bw/Stuttgart/HRB/202061/Gretsch-Unitas-GmbH-Baubeschlaege')],
    '德国 GU 集团五金门牌商(三代家族)', '集团大谱;2006 创(牌 1907)',
    ('三代家族+新 GF 谱', '集团层谱', 'Teunissen 新 GF 庆贺位', '自家链栈=合作段'),
    'Teunissen 履新贺卡+von Resch 集团位(opt-in 律)', 'Guten Tag Herr Dr. Teunissen,'))

R.append(rec('A-154', 'GU BKS SERVICE GmbH',
    'GU BKS SERVICE GmbH(Velbert,Heidestraße 71, 42549;**HRB 33137 AG Wuppertal;DE146887533;1980-02-21 创 46 年(选址变 19 次);51-200 人**;**GU 集团 BKS 牌=安全/关门技术服务商**(ts;scan 服;马 Messtechniker 乐队谱;系也商谱:同体 of Resch 业谱)',
    [('Florian Rabe', 'Geschäftsführer(**2024-02-20 履新**;Impressum 法定首谱)', 'gu-bks.de Impressum+webvalid 登记公告', O, 'https://www.gu-bks.de/de/impressum.html'),
     ('Josef Haumann', 'Geschäftsführer(2023-06 起)', 'companyhouse 谱+webvalid 历改谱', G, 'https://www.companyhouse.de/GU-BKS-SERVICE-GmbH-Velbert'),
     ('Niklas Menke', 'Geschäftsführer(companyhouse 现任谱)', 'companyhouse 谱', G, 'https://www.companyhouse.de/GU-BKS-SERVICE-GmbH-Velbert'),
     ('Oliver Büchner', 'Prokurist(2024-02-20 在册)', 'companyhouse+webvalid 双源', O, 'https://www.companyhouse.de/GU-BKS-SERVICE-GmbH-Velbert')],
    [ev('决策链与对接人', 'Geschäftsführer Florian Rabe(gu-bks.de Impressum);Heidestraße 71, 42549 Velbert;HRB 33137 Wuppertal;DE146887533', 'https://www.gu-bks.de/de/impressum.html'),
     ev('决策链与对接人', 'Management: Josef Haumann, Florian Rabe, Niklas Menke;Zeichnungsberechtigte: Oliver Büchner, Jochen Wolfgang Hanselmann, Tino Schmecht, Claudia Stoltenberg;Klaus-Michael Büntig GF since 2007(companyhouse 谱)', 'https://www.companyhouse.de/GU-BKS-SERVICE-GmbH-Velbert')],
    '德国 NRW GU 集团 46 年安全服务商', '51-200 人;1980 创',
    ('集团谱+新 GF 2024 谱面', '中实体谱', 'Rabe 新 GF 庆贺位', '自家链栈=合作段'),
    'Rabe 履新+Haumann 共谱(opt-in 律)', 'Guten Tag Herr Rabe,'))

R.append(rec('A-155', 'H & G Hansen & Gieraths EDV Vertriebs GmbH',
    'H & G Hansen & Gieraths EDV Vertriebsgesellschaft mbH(Bonn,Bornheimer Str. 42-52;**HRB 4027 AG Bonn(EUID DER3201.HRB4027;LEI 529900ZLJD9UWIJ96Y95);USt DE122121252;1985-12-26 创 40 年;175 人(2023)**;**股东=H&G Hansen & Gieraths IT Solutions GmbH 母谱;Hansen 家族三代:Dr. Heinz Hellmuth Hansen 老铺 2024-01 让位**;hug.de',
    [('Holger Hansen', 'Geschäftsführer(2024-01-12 任命;Bonn)', 'creditreform 登记公告+implisense+DNB', O, 'https://firmeneintrag.creditreform.de/53111/5030068909/H_G_HANSEN_GIERATHS_EDV_VERTRIEBSGESELLSCHAFT_MBH'),
     ('Dr. Heinz Hellmuth Hansen', '原 Geschäftsführer(至 2024-01-12;K/2 Physiker)', 'creditreform 登记公告(留痕)', O, 'https://firmeneintrag.creditreform.de/53111/5030068909/H_G_HANSEN_GIERATHS_EDV_VERTRIEBSGESELLSCHAFT_MBH'),
     ('Heinz H. Hansen', 'Prokurist(剩谱)', 'northdata 公报谱', O, 'https://www.northdata.de/H+&+G+Hansen+&+Gieraths+EDV+Vertriebsgesellschaft+mbH,+Bonn/HRB+4027'),
     ('Svenja Hansen', 'Prokurist(族谱)', 'northdata 公报谱', O, 'https://www.northdata.de/H+&+G+Hansen+&+Gieraths+EDV+Vertriebsgesellschaft+mbH,+Bonn/HRB+4027')],
    [ev('决策链与对接人', '12.01.2024: Nicht mehr GF: Dr. Hansen, Heinz Hellmuth, Physiker, Sankt Augustin;Bestellt zum GF: Hansen, Holger, Bonn(creditreform 件);Gesellschafter: H&G Hansen & Gieraths IT Solutions GmbH;Prokura: Heinz H. Hansen, Svenja Hansen(northdata 件)', 'https://firmeneintrag.creditreform.de/53111/5030068909/H_G_HANSEN_GIERATHS_EDV_VERTRIEBSGESELLSCHAFT_MBH'),
     ev('联系方式与基础画像', 'HRB 4027 Bonn;gegründet 26.12.1985;175 Mitarbeiter (2023);DE122121252;dd:Vertrieb/Reparatur/Wartung/Herstellung elektronischer Geräte, IT-Security, Managed Services, Netzwerk-,Speicherlösungen, Konferenztechnik(implisense 件)', 'https://app.implisense.com/en/companies/h-g-hansen-gieraths-edv-vertriebsgesellschaft-mbh-bonn--DEPJ95MWJE86')],
    '德国 Bonn 40 年 IT 批发屋(家族三代)', '175 人;1985 创',
    ('40 年谱+三代接棒位', '中型批发屋谱', 'Holger Hansen 新 GF 庆贺位', '大牌件链竞谱'),
    'Holger 接棒+Svenja/Heinz 代庆(opt-in 律)', 'Guten Tag Herr Holger Hansen,'))

R.append(rec('A-156', 'Hamburger Meldetechnik GmbH & Co. KG',
    'Hamburger Meldetechnik GmbH & Co. KG(「HMT」;Hamburg,Mörkenstr. 7, 22767;**HRA 116788 AG Hamburg;Verwaltungs GmbH HRB 128423 个人担责**;**2003 创 22 年;0-9 人**;谱型=汉堡区安全工程屋(报警/视频/门禁装维+旧件维护;合 040-280.976.70+info@hmt-hamburg.com)',
    [('Erk Foth', 'Geschäftsführer(2003 创铺即任至今=业主级直达)', '官网官网 unternehmen+openregister+Kompass+northdata 四源', O, 'https://www.hmt-hamburg.com/ueber-uns/unternehmen')],
    [ev('决策链与对接人', 'HMT Hamburger Meldetechnik wurde 2003 von dem derzeitigen Geschäftsführer Erk Foth gegründet;Mörkenstr. 7, 22767 Hamburg;040/280 976 70(官网 unternehmen 件)', 'https://www.hmt-hamburg.com/ueber-uns/unternehmen'),
     ev('联系方式与基础画像', 'Hamburger Meldetechnik GmbH & Co. KG: HRA116788 Hamburg;Verwaltungs GmbH HRB 128423;Erk Foth Geschäftsführer seit 15.01.2004(独谱;0-9 Mitarbeiter(openregister/Kompass/cylex 件)', 'https://openregister.de/company/DE-HRB-K1101-128423')],
    '德国汉堡 22 年安全工程房', '0-9 人;2003 创',
    ('单人业主 22 年谱', '微实体谱', 'Foth 单一直达位', '大牌安防链竞谱'),
    'Foth 直达(opt-in 律)', 'Guten Tag Herr Foth,'))

R.append(rec('A-157', 'Human Art Computersysteme GmbH',
    'Human Art Computersysteme GmbH(柏林 Rosenthal,Dammsmühler Str. 37, 13158;**HRB 54775 B AG Charlottenburg;€60k;USt DE170898522;1988 创 38 年**;11-50 人;谱型=柏林 38 年系统屋(打印/复印/IT 安全/工业/显示方案)',
    [('Harald Dahm', 'Geschäftsführer(法定代表)', '官网 Impressum+XING+webvalid 三源', O, 'https://www.human-art.de/impressum'),
     ('Manuel Siegfried Wagner', 'Prokurist(2007-11-29 在册)', 'webvalid 登记公告+XING 员工谱', O, 'https://www.webvalid.de/company/Human+Art+Computersysteme+GmbH,+Berlin/HRB+54775+B'),
     ('Dennis Berger', 'Projektvertrieb(项目销售)', 'XING 员工谱', G, 'https://www.xing.com/pages/humanartcomputersystemegmbh')],
    [ev('决策链与对接人', 'Vertretungsberechtigter Geschäftsführer: Harald Dahm;HRB 54775;USt DE170898522;Dammsmühler Str. 37, 13158 Berlin(官网 Impressum)', 'https://www.human-art.de/impressum'),
     ev('决策链与对接人', '29.11.2007: Eintritt Prokurist Wagner, Manuel Siegfried(webvalid 件);Manuel Wagner Prokurist(XING 员工谱原位)', 'https://www.webvalid.de/company/Human+Art+Computersysteme+GmbH,+Berlin/HRB+54775+B')],
    '德国柏林 38 年系统屋', '11-50 人;1988 创',
    ('38 年谱', '小实体谱', 'Dahm GF 直达位', '大牌件链竞谱'),
    'Dahm GF+Wagner Prokurist(opt-in 律)', 'Guten Tag Herr Dahm,'))

R.append(rec('A-158', 'Inducio GmbH',
    'inducio GmbH(德国 Traunstein,Kotzinger Str. 21;**HRB 20442 AG Traunstein;2010-09-24 创 16 年**;谱型=**IT 网管软件屋(自家 COD 平台=关键基础设施网管(医疗/能源)=KRITIS 谱,守界注记)**;Odoo 集成谱(odoo.inducio-services.net)',
    [('Siegmund Volker Gromotka', 'Gründer & Geschäftsführer(2010 起;COD 引语自署)', 'handelsregister.ai 登记谱+it-management.today 专文+经济协会成员页', O, 'https://handelsregister.ai/de/organizations/traunstein/erbringung-von-beratungsleistungen-auf-dem-gebiet-der-informationstechnologie/inducio-gmbh-2cdd290d0d88e09113f6d982bcc9caa5'),
     ('Lukas Parzinger', 'Head of Information Technology(2024-09 起;兼 extocode GmbH CTO)', 'contactout 谱', G, 'https://contactout.com/lukas-parzinger-12956')],
    [ev('决策链与对接人', 'Siegmund Volker Gromotka seit 2010 Geschäftsführer;HRB 20442 Traunstein;Kotzinger Str. 21, 83278 Traunstein;2010-09-24 Eintragung(handelsregister.ai 件)', 'https://handelsregister.ai/de/organizations/traunstein/erbringung-von-beratungsleistungen-auf-dem-gebiet-der-informationstechnologie/inducio-gmbh-2cdd290d0d88e09113f6d982bcc9caa5'),
     ev('团队与规模', 'COD 平台: KRITIS-sector 医疗+能源网管;Gromotka「Gründer der inducio GmbH」引语(it-management.today 件);Lukas Parzinger Head of IT(contactout 件)', 'https://www.it-management.today/inducio-gmbh-revolutioniert-die-netzwerkverwaltung-mit-cod-die-zukunftssichere-it-loesung-fuer-kritische-infrastrukturen/')],
    '德国 Chiemgau 16 年 KRITIS 网管软件屋', '小实体谱;2010 创',
    ('COD 自家谱 KRITIS 守界', 'KRITIS 段守界', 'Gromotka 创始直达位', '大牌管软链竞谱'),
    'Gromotka 创始(KRITIS 守界;opt-in 律)', 'Guten Tag Herr Gromotka,'))

R.append(rec('A-159', 'Insight Technology Solutions GmbH',
    'Insight Technology Solutions GmbH(德国 Raunheim,Am Prime-Parc 9(旧 Garching Parkring 35);**HRB 103112 AG Darmstadt;DE812242281;1988 创(原名 Corporate Software GmbH)**;**137 人/€122M;Insight Enterprises Inc.(NASDAQ:NSIT)全资=美资全球整合商;16×Microsoft Gold 谱(安全含)**',
    [('Thomas Kühlewein', 'Geschäftsführer(2020-10 起德国区)', '官网 Impressum+de.insight.com 法人公告', O, 'https://insightportal.de/impressum'),
     ('Glynis Ann Bryan', 'Geschäftsführer(现任谱)', 'insightportal.de Impressum', O, 'https://insightportal.de/impressum'),
     ('James Morgado', 'Geschäftsführer(谱面留痕)', 'de.insight.com Impressum 件(留痕)', O, 'https://de.insight.com/de_DE/knowledge-base/impressum.html')],
    [ev('决策链与对接人', 'Geschäftsführer: Thomas Kühlewein, Glynis Ann Bryan;HRB 103112 AG Darmstadt;DE812242281;Am Prime-Parc 9, 65479 Raunheim(insightportal.de Impressum)', 'https://insightportal.de/impressum'),
     ev('联系方式与基础画像', 'THOMAS KÜHLEWEIN ÜBERNIMMT DIE GESCHÄFTSFÜHRUNG… Oktober 2020 法人公告;Insight Enterprises (NASDAQ: NSIT);16 Microsoft Gold Competencies;137 Mitarbeiter/€122M(de.insight.com 新闻室+DDW 件)', 'https://de.insight.com/de_DE/about/newsroom/')],
    '德国 Raunheim 38 年美资全球 IT 整合商', '137 人;€122M;1988 创',
    ('上市母台 38 年谱', '大实体谱', 'Kühlewein 德区 GF 直达位', '自家链栈=不占'),
    'Kühlewein 德区 GF(opt-in 律)', 'Guten Tag Herr Kühlewein,'))

R.append(rec('A-160', 'ISIMKO GmbH',
    'ISIMKO GmbH(德国 Cottbus(Brande),Guhrower Str. 5;**HRB 472 CB AG Cottbus(老号);€200k;1990-09-28 创 36 年;120+ 人(Cottbus/Berlin/Dresden/Spremberg 四店)**;**原名 G. Fleischhauer Ingenieur-Büro Cottbus GmbH(2017-01 更名)**;谱型=手艺 IT/安全/媒体/通信技术房(铜/光纤工业网;公家+医院+中端;移动/固定+Telematik;YellowFox 伙伴谱)',
    [('Ralph Hannemann', 'Geschäftsführer(舗系;Hannemann 家族(G. Fleischhauer 期的 Peter Hannemann 前谱))', '官网 Impressum+goyellow+webvalid 三源', O, 'https://www.isimko.de/impressum/'),
     ('Diego Noack', 'Geschäftsführer(2018-01 由 Prokurist 晋 GF,Drebkau)', '官网 Impressum+online-handelsregister 登记公告', O, 'https://www.isimko.de/impressum/'),
     ('Falk Noack', 'Einzelprokura(2018-01 在册,Berlin)', 'webvalid/online-handelsregister 登记公告', O, 'https://www.online-handelsregister.de/handelsregisterauszug/br/Cottbus/HRB/472CB/ISIMKO-GmbH'),
     ('Markus Menzel', '伙伴联络人(YellowFox 合作线)', 'yellowfox.de 伙伴页', G, 'https://www.yellowfox.de/partneruebersicht/isimko-gmbh/')],
    [ev('决策链与对接人', 'Vertreten durch: Ralph Hannemann, Diego Noack (beide Geschäftsführer);HRB 472 Cottbus;Guhrower Str. 5, 03044 Cottbus(官网 Impressum)', 'https://www.isimko.de/impressum/'),
     ev('联系方式与基础画像', 'gegründet 28.09.1990;€200.000;120+ Mitarbeiter;Standorte Cottbus/Berlin/Dresden/Spremberg;Ehemals G. Fleischhauer Ingenieur-Büro GmbH(2017 更名);Einzelprokura Falk Noack(登记公告件)', 'https://www.online-handelsregister.de/handelsregisterauszug/br/Cottbus/HRB/472CB/ISIMKO-GmbH')],
    '德国 Brandenburg 36 年手艺 IT 房', '120+ 人;1990 创',
    ('36 年谱+医院/公家面=守界分', '中实体谱', 'Hannemann/Noack 双 GF 直达位', '大牌件链竞谱'),
    '双 GF+Menzel 伙伴线(opt-in 律;公家/医院段守界)', 'Guten Tag Herr Hannemann,'))

R.append(rec('A-161', 'JOTT Consulting GmbH',
    'JOTT Consulting GmbH(德国 Köln,Klosterstraße 37, 50931(Lindenthal 区);**HRB 121343 AG Köln;€25k**;小实体谱;谱型=Köln SMB IT 咨询(150+ 客户/40,000+ 服务小时/1,000+ 服务器管理;BNI 会员谱;25+ 年经验)',
    [('Klaus Jettkant', 'Geschäftsführer(业主直达;BNI 谱)', 'jott.consulting 官网+BNI+northdata+creditreform 四源', O, 'https://www.jott.consulting/'),
     ('Katrin Deckstein', 'Unternehmensentwicklung(企发)', '官网 Team 谱', O, 'https://www.jott.consulting/'),
     ('Julius Steffens', 'IT-Service', '官网 Team 谱', O, 'https://www.jott.consulting/')],
    [ev('决策链与对接人', 'Klaus Jettkant Geschäftsführer(官网 Team 位「Weil Menschen IT verständlich machen」);Team: Julius Steffens/Daniel Eilers IT-Service;Katrin Deckstein Unternehmensentwicklung;Stefani Grimm-Ellieroth Buchhaltung(jott.consulting 件)', 'https://www.jott.consulting/'),
     ev('联系方式与基础画像', 'Klosterstraße 37, 50931 Köln;HRB 121343;+49 221 32078567;info@jott.consulting;BNI Stadion 会员谱(creditreform/bni 件)', 'https://firmeneintrag.creditreform.de/50931/5190789965/JOTT_CONSULTING_GMBH')],
    '德国 Köln SMB IT 咨询屋(BNI 谱)', '小实体谱',
    ('150+ 客 25 年谱', '微实体谱', 'Jettkant 直达位', '大牌件链竞谱'),
    'Jettkant 直达(opt-in 律)', 'Guten Tag Herr Jettkant,'))

R.append(rec('A-162', 'KWS Partner GmbH',
    'KWS Partner GmbH(德国 Frankenberg/Sa.(萨克森),Freiberger Str. 39;**HRB 19449 AG Chemnitz;€25k;2001-12-11 创 24 年;4 人(2018 谱)**;USt DE813388501;谱型=双工程师 IT 屋(硬件+TK+办公设备批云安全;B2B+公家机构谱)',
    [('Dipl.-Informatiker (FH) Andreas Werner', 'Geschäftsführer(双)', 'kws-partner.de Impressum+XING+implisense 三源', O, 'https://kws-partner.de/impressum/'),
     ('Dipl.-Ingenieur Jens Krenkel', 'Geschäftsführer(双)', 'kws-partner.de Impressum+implisense 登记谱', O, 'https://kws-partner.de/impressum/')],
    [ev('决策链与对接人', 'Vertretungsberechtigte Geschäftsführer: Dipl.-Informatiker (FH) Andreas Werner, Dipl.-Ingenieur Jens Krenkel;Handelsregister Chemnitz 19449;Ust DE 813 388 501(kws-partner.de Impressum)', 'https://kws-partner.de/impressum/'),
     ev('联系方式与基础画像', 'HRB 19449 Chemnitz;gegründet 11.12.2001;€25,000;Freiberger Str. 39, 09669 Frankenberg/Sa.;Micro 4 Mitarbeiter(implisense 件)', 'https://app.implisense.com/en/companies/kws-partner-gmbh-frankenberg-sa--DEQXQKVS0G13')],
    '德国萨克森 24 年双工程师 IT 屋', '4 人;2001 创',
    ('双工程师直达谱', '微实体谱', 'Werner/Krenkel 双直达位', '大牌件链竞谱'),
    '双 GF 直达(opt-in 律)', 'Guten Tag Herr Werner,'))

R.append(rec('A-163', 'M IT-Systemhaus GmbH',
    'M IT-Systemhaus GmbH(德国 Mühldorf a. Inn(Bahnhofstr. 25/Leisederstr. 4);**HRB 27859 AG Traunstein;2019-04-24 创 7 年**;**「Master\'s IT-Systemhaus」组合谱(团谱面 30,000 客/260,000 品/200 项目=自夸谱再校）;KMU+学校线(双沙oc区线：KMU 管服+学校谱面);谱管理人 2020-12 谱变=Stellmach 退→双掌柜**',
    [('Claus Franz Josef Uretschläger', 'Geschäftsführer / Vertrieb(2019-04-24 起 alleinvertretungsberechtigt;兼 CU Beratung UG+ITSicherheit24)', 'm-itsysteme.de Ansprechpartner+companyhouse+LinkedIn 三源', O, 'https://m-itsysteme.de/ansprechpartner'),
     ('Christian Dufek', 'Geschäftsführer / Technik(2022-07-06 起;前 Prokurist)', 'm-itsysteme.de Ansprechpartner+companyhouse 登记系谱', O, 'https://m-itsysteme.de/ansprechpartner'),
     ('Bernd Grimm', 'Leiter MSP(管服主管=落位最合)', 'm-itsysteme.de Ansprechpartner 页', O, 'https://m-itsysteme.de/ansprechpartner')],
    [ev('决策链与对接人', 'Geschäftsführer/Vertrieb: Claus Uretschläger (claus.uretschlaeger@m-itsysteme.de);GF/Technik: Christian Dufek;Leiter MSP: Bernd Grimm(m-itsysteme.de Ansprechpartner 全谱)', 'https://m-itsysteme.de/ansprechpartner'),
     ev('联系方式与基础画像', 'HRB 27859 Traunstein;gegründet 2019;Uretschläger seit 24.04.2019 alleinvertretungsberechtigt;Dufek GF seit 06.07.2022(vorher Prokurist);Heinz Stellmach 史谱(Gilgenberg am Weilhart/Österreich)(companyhouse 件)', 'https://www.companyhouse.de/M-IT-Systemhaus-GmbH-Muehldorf-a-Inn')],
    '德国下巴伐利亚 7 年 MSP 屋(KMU+学校)', '中实体谱;2019 创',
    ('MSP 专职谱(Grimm)', '小实体谱', 'Uretschläger/Dufek 双直达位', '大牌件链竞谱'),
    'Grimm MSP 主管+Uretschläger 谱位(opt-in 律)', 'Guten Tag Herr Grimm,'))

R.append(rec('A-164', 'm² IT Solutions e. K',
    'm² IT Solutions e. K.(德国 Tübingen,Alte Landstr. 42;**HRA 721502 AG Stuttgart;USt DE230302730;2003-09 创 22 年单人业主铺**;1-10 人;谱型=Tübingen 单铺网络/虚拟化顾问(虚拟化 VMware/服务器/存储/网络;**USE-Software 德区经销+服务伙伴**)',
    [('Martin Mayer', 'Inhaber / Geschäftsführer(单人业主=唯一直达;CEO & Founder 自署)', '官网 Impressum+XING 自署谱', O, 'https://www.m2-it-solutions.de/impressum/')],
    [ev('决策链与对接人', 'Inhaber: Martin Mayer;HRA 721502 Stuttgart;USt DE230302730;Alte Landstr. 42, 72072 Tübingen;mail@m2-it-solutions.de(官网 Impressum)', 'https://www.m2-it-solutions.de/impressum/'),
     ev('业务定位', 'Lösungen Virtualisierung und Netzwerktechnik;deutscher Vertriebs- und Servicepartner der USE-Softwarelösungen;Server-/Storage/Networking/ERP/PPS/CRM;Martin Mayer seit Sep 2003(XING about-us 件)', 'https://www.xing.com/pages/m-itsolutionse-k/about_us')],
    '德国 Tübingen 22 年单铺 IT 顾问', '1-10 人;2003 创',
    ('单人业主 22 年谱', '微实体谱', 'Mayer 唯一直达位', '大牌件链竞谱'),
    'Mayer 直达(opt-in 律)', 'Guten Tag Herr Mayer,'))

R.append(rec('A-165', 'MECO Systemhaus GmbH & Co. KG',
    'MECO Systemhaus GmbH & Co. KG(德国 Boppard(莱茵),Unten in der Aab 16, 56154;**1990 创 36 年**;5 人谱;谱型=Boppard SMB MSP(管理服+Print/Desktop/Mail 服务;it-service.network 网盟谱)',
    [('Peter Kaiser', 'Geschäftsführender Gesellschafter(高盛合伙人)', 'it-service.network+XING 双源谱', G, 'https://it-service.network/boppard-bad-salzig'),
     ('Dirk J. Simonis', 'Geschäftsführender Gesellschafter(CEO technisch;Uni Koblenz)', 'XING+LinkedIn 双源谱', G, 'https://www.xing.com/pages/mecosystemhausgmbh-co-kg')],
    [ev('决策链与对接人', 'Ansprechpartner: Peter Kaiser, MECO Systemhaus GmbH;gegründet 1990;Managed Services Spezialist(it-service.network 件)', 'https://it-service.network/boppard-bad-salzig'),
     ev('团队与规模', 'Peter Kaiser+Dirk J. Simonis geschäftsführende Gesellschafter;Simonis「CEO im technischen Bereich」;5 Mitarbeiter(XING/LinkedIn 件)', 'https://www.xing.com/pages/mecosystemhausgmbh-co-kg')],
    '德国莱茵 36 年 SMB MSP 屋', '5 人;1990 创',
    ('36 年谱+网盟位', '微实体谱', 'Kaiser/Simonis 双直达位', '大牌件链竞谱'),
    'Kaiser 谱位(opt-in 律)', 'Guten Tag Herr Kaiser,'))

R.append(rec('A-166', 'Michael Schmidt IT GmbH',
    'schmidt IT — Michael Schmidt IT GmbH(德国 Spardorf(埃尔朗根圈;多 Buckenhofer Str. 16),91080;**2001 创个体→2005 GmbH=25 年谱;7 人/~$2M**;**Dipl.-Inf. Michael Schmidt 兼有 Certified Ethical Hacker (CEH)=安全专铺;Sophos 客户谱;公家( Erlangen 圈内 Gemeinde)线守界分**',
    [('Dipl.-Inf. Michael Schmidt', 'Geschäftsführer(业主直达;CEH 认证=安全铺)', 'msit-gmbh.de 官网 über+RR 双源', O, 'https://www.msit-gmbh.de/ueber-michael-schmidt-it-gmbh-ihr-it-systemhaus-fuer-erlangen-und-nuernberg/'),
     ('Fidan Feta', 'Assistent der Geschäftsleitung(高管助理;客户证言具名)', '官网证言件', G, 'https://www.msit-gmbh.de/it-consulting/')],
    [ev('决策链与对接人', 'Dipl.-Inf. Michael Schmidt, Geschäftsführer;Certified Ethical Hacker (CEH) 2016 zertifiziert;2001 创单铺 → 2005 GmbH;20 Jahre 2021(官网 über-MSIT 件)', 'https://www.msit-gmbh.de/ueber-michael-schmidt-it-gmbh-ihr-it-systemhaus-fuer-erlangen-und-nuernberg/'),
     ev('联系方像', 'Buckenhofer Str. 16, 91080 Spardorf;+49 9131 920860;7 Mitarbeiter;Kundenstimmen: Evosys Laser/Gemeinde Spardorf 谱(msit-gmbh.de/RR 件)', 'https://rocketreach.co/michael-schmidt-it-gmbh-profile_b43c96a7c1d742fd')],
    '德国埃朗根圈 25 年 CEH 安全系统屋', '7 人;2001 创',
    ('CEH 谱+公家线(守界分)', '微实体谱', 'Schmidt 直达位', 'Sophos/大牌链竞谱'),
    'Schmidt 直达(公家线守界;opt-in 律)', 'Guten Tag Herr Schmidt,'))

R.append(rec('A-167', 'my ITService Wolfgang Deibe',
    'my ITservice Wolfgang Deibel e.K.(德国 Wiehl(Bergisches Land),Im Weierhof 4, 51674;**HRA 38706 AG Köln(Eintragung 2026-03-23;USt DE-214354489);档名『Deibe』=登记名 Deibel 一字异文留痕**;谱型=Wiehl 单铺 IT 房(IT 咨询+服务+软硬零售;SIEMENS/Fujitsu/AGFEO 伙伴谱;**为多家公司任外部 Datenschutzbeauftragter(多处 DSB 聘任谱:Campus Martinsried/Holzem & Hartmann 等）=B2B 安全谱**)',
    [('Wolfgang Deibel', 'Inhaber(单人业主=唯一直达)', 'cylex+salmar-agentur+DSB 聘任页 三源', O, 'https://web2.cylex.de/firma-home/my-itservice--inhaber-wolfgang-deibel-4975578.html')],
    [ev('决策链与对接人', 'Geschäftsleitung: Wolfgang Deibel, 02262/717738;Im Weierhof 4, 51674 Wiehl;info@my-itservice.com;SIEMENS/Fujitsu/AGFEO(cylex 件)', 'https://web2.cylex.de/firma-home/my-itservice--inhaber-wolfgang-deibel-4975578.html'),
     ev('团队与规模', 'externer DSB für mehrere Unternehmen: Campus Martinsried + Ingenieurbüro Holzem & Hartmann(Wolfgang Deibel 为 dsb@my-itservice.com 联络位);Planegg/Martinsried 触点', 'https://campusmartinsried.de/datenschutz/')],
    '德国 Berg 单铺 IT 房+外部 DSB 服务', '单人谱;2026 e.K. 重记',
    ('DSB 多家谱=B2B 谱节', '微实体谱', 'Deibel 唯一直达位', '荷我=多厂牌件链竞谱'),
    'Deibel 直达(opt-in 律)', 'Guten Tag Herr Deibel,'))

R.append(rec('A-168', 'N+P Informationssysteme GmbH',
    'N+P Informationssysteme GmbH(德国 Meerane(萨克森),An der Hohen Straße 1, 08393;**HRB 1746 AG Chemnitz(老号);USt DE 141 380 688;1990 创 36 年二代家族**;120-130 人/€6.2-18M;支谱 Berlin/Dresden/Kassel/Magdeburg/Nürnberg/Stuttgart;谱型=**工业+建筑数字化 ERP 屋**(CAD/CAM/ERP/MES/PDM/PLM 全链;2,000+ 客/年;INDUSTRIEVEREIN SACHSEN 1828 成员)',
    [('Jens Hertwig', 'Geschäftsführender Gesellschafter(业主二代;V.i.S.d.P.)', '官网 unternehmen+Impressum+industrieverein 三源', O, 'https://www.nupis.de/Unternehmen'.replace('Unternehmen','unternehmen')),
     ('Paul Hertwig', 'Geschäftsführender Gesellschafter(业主二代)', '官网 unternehmen+Impressum 双源', O, 'https://www.nupis.de/unternehmen'),
     ('Andreas Thieme', 'Geschäftsführer(三位 GF)', '官网 unternehmen+Impressum 双源', O, 'https://www.nupis.de/unternehmen'),
     ('Björn Schuster', 'Authorized signatory / VP Business Development(总代+业务发展 BD KPI 位)', 'RocketReach 员工谱', G, 'https://rocketreach.co/np-informationssysteme-gmbh-profile_b5fcaabbf9b773f3')],
    [ev('决策链与对接人', 'Unsere Geschäftsführung: Jens Hertwig / Paul Hertwig geschäftsführende Gesellschafter;Till Hertwig Gesellschafter;Andreas Thieme Geschäftsführer(nupis.de 官网 unternehmen 件);Impressum: GF Jens Hertwig, Paul Hertwig, Andreas Thieme;HRB 1746 Chemnitz', 'https://www.nupis.de/unternehmen'),
     ev('联系方式与基础画像', 'gegründet 1990;100% Familienunternehmen 二代;120-130 Mitarbeiter;Digitalisation Industrie+Bauwesen;2.000 Kunden/Jahr;CAD/CAM/ERP/MES/PDM/PLM(industrieverein 1828 成员件)', 'https://www.industrieverein.org/index.php/firmendetails/np-informationssysteme-gmbh.html')],
    '德国萨克森 36 年二代工业数字化 ERP 屋', '120-130 人;1990 创',
    ('二代家族+ERP 全链谱', '中实体谱', 'Schuster 总代 BD 位占场', '大牌 ERP 链竞谱'),
    'Schuster BD 总代+Hertwig 双谱(opt-in 律)', 'Guten Tag Herr Schuster,'))

R.append(rec('A-169', 'Netz16 GmbH',
    'Netz16 GmbH(德国 Augsburg(Sheridanpark 新址谱);**2009 创 17 年;~200 人集团谱(四店:Augsburg/München/Herbrechtingen/Nordenham;集团 2022 营收 €20M+)**;**Netz16 集团:Netz16/Digisoolut/PARIT/Fundwerk/alphasystems 并购谱**;**FC Augsburg FCA-Supplier 主赞;kununu 4×Top Company 谱**;谱型=南德中端 MSP/安全+BI 并购扩张谱',
    [('Dr. Andreas Herch', 'Geschäftsführer(创始双 GF;FCA/并购引语多源)', 'netz16.de 官网 über-uns+FCA 件+并购件三源', O, 'https://www.netz16.de/ueber-uns/'),
     ('Christian Popp', 'Geschäftsführer(创始双 GF;technischer GF)', 'netz16.de 官网 über-uns+alphasystems 并购件', O, 'https://www.netz16.de/ueber-uns/'),
     ('Henning Krebel', 'PARIT GF(2023 并购留任;集团会员谱)', 'netz16.de 并购件', O, 'https://www.netz16.de/netz16-waechst-weiter-uebernahme-der-parit-gmbh/'),
     ('Jörn Steinhauer', 'alphasystems GF(并购留任谱)', 'alphasystems.com 并购件', O, 'https://www.alphasystems.com/alphasystems-und-netz16-gehen-gemeinsame-wege/')],
    [ev('决策链与对接人', 'Die Netz16 Gruppe: Netz16, Digisoolut, Parit und Fundwerk;Führung: Katja Wörner / Dr. Andreas Herch / Christian Popp / Jörn Steinhauer / Henning Krebel;gegründet 2009;~200 Mitarbeiter(netz16.de über-uns 件)', 'https://www.netz16.de/ueber-uns/'),
     ev('团队与规模', 'zum 01.01.2023 übernimmt Netz16 Mehrheit an PARIT GmbH(Henning Krebel 留任 GF);Gruppenumsatz 2022 erstmals über 20 Mio. Euro;FC Augsburg Supplier;Kununu Top Company 4×(并购/FCA/kununu 件)', 'https://www.netz16.de/netz16-waechst-weiter-uebernahme-der-parit-gmbh/')],
    '德国奥格斯堡 17 年并购型 MSP 集团', '~200 人;€20M+;2009 创',
    ('并购扩张谱 FCA 赞助', '中实体谱', 'Herch/Popp 双龙直达位', '一线链竞谱'),
    'Herch/Popp 直接(opt-in 律)', 'Guten Tag Herr Dr. Herch,'))

R.append(rec('A-170', 'NiTo IT Systeme GmbH',
    'NiTo IT Systeme GmbH →【**2026-06-22 更名:IPTGA Projekt Konzept GmbH**】(柏林,Storkower Str. 115A, 10407;**HRB 216686 B AG Charlottenburg;DE329092725;2020-04-14 创**;谱型=柏林小微 IT 咨询屋(安全/可扩展方案/软件编程/接口;媒体/IT 管理;Videokonferenz/视频软件线)**档名 NiTo 已过时实体,谱带应台账对位现名 IPTGA**;**GF 换位谱全接:Oldenburg(2020)→Silvia Müller(2023)→Torsten Uwe Müller(2025-12)→Joel Can Müller(2026-06)**',
    [('Torsten Uwe Müller', 'Geschäftsführer(**2025-12-02 起在职**;*1963,Berlin)', 'webvalid/creditreform 2025-12-02 登记公告', O, 'https://firmeneintrag.creditreform.de/10407/2012948573/NITO_IT_SYSTEME_GMBH'),
     ('Joel Can Müller', 'Geschäftsführer(2026-06 更名时谱=IPTGA 名下;族谱 Jr 代)', 'webvalid 2026-06-22 登记公告谱', O, 'https://www.webvalid.de/company/NiTo+IT+Systeme+GmbH,+Berlin/HRB+216686'),
     ('Silvia Müller', '原 Geschäftsführer(2023-01~2025-12;Impressum 遗留自署=滞后谱)', 'nitoit.de Impressum(留痕)+登记公告', O, 'https://nitoit.de/impressum/'),
     ('Nils Christian Oldenburg', '原 Geschäftsführer(2020 创铺至 2023-01)', '登记公告+it-in-germany 件(留痕)', O, 'https://www.it-in-germany.de/firma/NiTo+IT+Systeme+GmbH/6041748/64641/deu')],
    [ev('决策链与对接人', '02.12.2025: Nicht mehr GF: Silvia Müller;GF: Torsten Uwe Müller, *15.06.1963, Berlin;22.06.2026: Firma geändert alt NiTo IT Systeme GmbH → neu IPTGA Projekt Konzept GmbH;GF: Joel Can Müller(webvalid/creditreform 登记公告件)', 'https://www.webvalid.de/company/NiTo+IT+Systeme+GmbH,+Berlin/HRB+216686'),
     ev('联系方式与基础画像', 'Storkower Str. 115A, 10407 Berlin;HRB 216686 B Berlin-Charlottenburg;DE329092725;gegründet 14.04.2020(nitoit.de Impressum=Silvia Müller 遗留滞后谱)', 'https://nitoit.de/impressum/')],
    '柏林 6 年微 IT 咨询(已更名 IPTGA)', '微实体谱;2020 创',
    ('更名锚+GF 年换谱', '微实体谱', 'Müller 族谱直达位', '大牌件链竞谱'),
    'Torsten Müller 现任(现名 IPTGA 谱;opt-in 律)', 'Guten Tag Herr Müller,'))

R.append(rec('A-171', 'Nutz GmbH',
    'Nutz GmbH(德国 Ampfing(上巴伐利亚),Adlerstraße 1, 84539;**HRB 1966 AG Traunstein;USt DE 129 264 383;1978 创(车库)48 年;333+ 人/~€34-63M**;**异体排噪:Nutz GmbH & Co. KG(Villingen,电批发 1921)=不同实体已分层**;谱型=**建筑自动化/电气数据安全技术总包商**(安防/数据/电气/楼宇管理;Global 谱;Professional Services 对外;DC+Pharma 线;医院守界分)',
    [('Christian Gruber', 'CEO(1984 学徒→1994 入管→2018 全权接棒=接班谱)', 'nutz.com about-us+Impressum+LinkedIn 三源', O, 'https://nutz.com/en/company/about-us'),
     ('Patrick Nutz', 'Geschäftsführung(业主二代)', 'nutz.com Impressum 自署', O, 'https://nutz.com/en/das-impressum-der-nutz-gmbh'),
     ('Thomas Wimmer', 'CFO(伙伴 CFO)', 'nutz.com Impressum+RR 双源', O, 'https://nutz.com/en/das-impressum-der-nutz-gmbh'),
     ('Andreas Bauer', 'COO Sicherheitstechnik(安全技术 COO=落位最合)', 'RocketReach 员工谱', G, 'https://rocketreach.co/nutz-gmbh-profile_b5d872c9f42e53fd'),
     ('Alexander Thimm', 'Head of Sales(销售主管 KPI 位)', 'RocketReach 员工谱', G, 'https://rocketreach.co/nutz-gmbh-profile_b5d872c9f42e53fd')],
    [ev('决策链与对接人', 'Impressum: Geschäftsführung Christian Gruber, Patrick Nutz, Thomas Wimmer;Nutz GmbH, Adlerstraße 1, 84539 Ampfing;HRB 1966 Traunstein;DE 129 264 383(nutz.com Impressum)', 'https://nutz.com/en/das-impressum-der-nutz-gmbh'),
     ev('决策链与对接人', 'Manfred Nutz starts 1978 in garage;Christian Gruber 学徒 1984 → 1994 Management → 2018 übernimmt als CEO;Thomas Wimmer CFO + Christian Eder mit密切 GF;333 Mitarbeiter/€34M(nutz.com about-us)', 'https://nutz.com/en/company/about-us'),
     ev('团队与规模', 'Andreas Bauer COO Sicherheitstechnik;Alexander Thimm Head of Sales;Andreas Huber Head of IT;Dirk Schiller Sales Manager Data Center and Pharma/Healthcare(RocketReach 谱)', 'https://rocketreach.co/nutz-gmbh-profile_b5d872c9f42e53fd')],
    '德国上巴伐利亚 48 年建筑技术总包商', '333+ 人;1978 创',
    ('三代并购谱+COO 线', '大型屋谱', 'Bauer 安全 COO+Thimm 销售位', '自家链栈=不占'),
    'Bauer COO+Thimm 销售(opt-in 律;医院段守界)', 'Guten Tag Herr Bauer,'))

R.append(rec('A-172', 'OAS AG',
    'OAS AG(德国 Bremen,Caroline-Herschel-Str. 1, 28359;**1982 创 44 年;~260 人(4 店)/€40M+**;谱型=**工厂自动化/称重/堆场管理/IT 解决方案全球厂商**(Hidden Champions 定制客户;OAS Automation GmbH 子谱;**2024-03 女性二代继承:父亡 → Kerstin Schwimmbeck(2013 起 Vorstand IT&Organisation)升 Vorstandsvorsitzende=变革窗！**;监事会 Dr. Patrick Wendisch)',
    [('Kerstin Schwimmbeck', 'Vorstandsvorsitzende(**2024-03 新任主席;Dipl.-Kff.;2013 起 Vorstand IT&Org**)', 'schuettgut 行业报+LinkedIn 公司页官方升级双源', O, 'https://www.schuettgut.vogel.de/neue-vorstandsvorsitzende-der-oas-ag-a-897c103c7191615f47c03902000f3a52/'),
     ('Dr. Patrick Wendisch', 'Aufsichtsratsvorsitzender(监事会主席;换代公告称道)', 'schuettgut 行业报', O, 'https://www.schuettgut.vogel.de/neue-vorstandsvorsitzende-der-oas-ag-a-897c103c7191615f47c03902000f3a52/'),
     ('Detlef Kremer', 'Geschäftsführer OAS Automation GmbH(子公司 10 年谱)', 'oas.de 40 周年页', O, 'https://www.oas.de/loesungen/40-jahre-oas-die-taetigkeitsfelder-der-oas-ag-automation'),
     ('Otto A. Schwimmbeck', 'Firmengründer(创始谱;2023 亡=接棒记)', 'schuettgut 行业报(留痕)', O, 'https://www.schuettgut.vogel.de/neue-vorstandsvorsitzende-der-oas-ag-a-897c103c7191615f47c03902000f3a52/')],
    [ev('决策链与对接人', 'Neue Vorstandsvorsitzende: Kerstin Schwimmbeck,Diplom-Kauffrau, folgt auf Firmengründer Otto A. Schwimmbeck(verstorben 2023);seit 2013 Vorstand Ressorts IT und Organisation;Aufsichtsratschef Dr. Patrick Wendisch(schuettgut 件)', 'https://www.schuettgut.vogel.de/neue-vorstandsvorsitzende-der-oas-ag-a-897c103c7191615f47c03902000f3a52/'),
     ev('联系方式与基础画像', 'gegründet 1982;~260 Mitarbeiter 4 Standorte;Umsatz über 40 Millionen Euro (2022/23);Anlagentechnik/Produktionssteuerung/Wägetechnik/Yard Management/IT;Detlef Kremer GF OAS Automation(schuettgut/oas.de 件)', 'https://www.oas.de/loesungen/40-jahre-oas-die-taetigkeitsfelder-der-oas-ag-automation')],
    '德国 Bremen 44 年工厂自动化方案商', '~260 人;€40M;1982 创',
    ('**二代继承窗 2024=变服窗**', '大型屋谱', 'Schwimmbeck 新主席庆贺位', '自家链栈=不占'),
    'Schwimmbeck 履新贺+IT 谱位(opt-in 律)', 'Sehr geehrte Frau Schwimmbeck,'))

R.append(rec('A-173', 'Phoenix IT Solutions',
    'PHOENIX IT SOLUTIONS(德国 Brackenheim(巴符),Südstraße 4, 74336;**单铺 30+ 年**;office@phoenix-itsolutions.de;+49 7135 937676-0;谱型=Brackenheim 单铺 IT 顾问(自僱/公司 1-100 人客户谱;云/基础设施/软件/IT 安全/电话&DSL 一件套)**排噪:phoenix-IT GmbH Haan(Zils 异体,2025-01 清算)+Phoenix Payroll(Köln)+Phoenix Solution(Bad Dürkheim)各已在案**',
    [('Uwe Herczeg', 'Inhaber(单铺主=唯一直达;Certified Netware Engineer)', '官网 phoenix-itsolutions.de 自署', O, 'https://www.phoenix-itsolutions.de/')],
    [ev('决策链与对接人', 'Inhaber: UWE HERCZEG, Certified Netware Engineer;Südstraße 4, 74336 Brackenheim;Tel: +49 (0)7135 937676-0;office@phoenix-itsolutions.de;über 30-jährige Erfahrung(官网首版面署)', 'https://www.phoenix-itsolutions.de/')],
    '德国巴符 30 年单铺 IT 顾问', '单铺谱;30+ 年',
    ('单铺主 30 年谱', '微实体谱', 'Herczeg 唯一直达位', '大牌件链竞谱'),
    'Herczeg 直达(opt-in 律)', 'Guten Tag Herr Herczeg,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第18波30户.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 18 波 30 户扩招批:A-143..A-173(A-153 同系合并;30 户全谱名牌)',
               'scope': 'DE×30 谱;军/密/KRITIS/医院各守界注记;NiTo→IPTGA 更名锚;Gretsch/GU 集团谱分层;各族谱(GU/Nutz/Hansen/Hertwig)对位',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 18 波 30 户扩招批落盘:',len(R))
