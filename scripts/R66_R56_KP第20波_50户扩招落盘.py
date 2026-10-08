# -*- coding: utf-8 -*-
"""R66 第 20 波(50 户扩招批):A-229~A-278 顺延 50 户;公司档 25+人名司名同体培训谱档 25。"""
import json

PRICE = '$180 USD EXW (2026-10-07, 15天有效)'
O = 'official-self-published·谱/leads-only(直发需 opt-in)'
G = 'leads-only·待 opt-in(LinkedIn/谱面带核)'
STRUCT = json.load(open('batch/structured_profiles_v1.json', encoding='utf-8'))
def push_of(code):
    # 供位口径:STRUCT p1=CONSULT-OEM 户(训练/OEM 探询,无量产报价)一阶 push 记 CONSULT-OEM
    return 'CONSULT-OEM' if STRUCT.get(code, {}).get('p1') == 'CONSULT-OEM' else 'STC-424XGGPM-280W'

def fu(push='STC-424XGGPM-280W'):
    return [
        {'stage': '第 1 次跟进 · 具名 kp 引路口', 'push': push, 'angle': '具名 kp 引路 → 采购/技术硬件分载线',
         'question': '贵司 24 口 PoE 交换机的硬件采购线由哪位同事主责？', 'proof': '规格页'},
        {'stage': '第 2 次跟进 · 一页目录卡', 'push': '一页目录卡', 'angle': '价值层 PoE 谱链卡', 'question': '可否入谱链名录？', 'proof': '卡'},
        {'stage': '第 3 次跟进 · 留档+LinkedIn 谱', 'push': '—', 'angle': '谱链明智途径', 'question': '—', 'proof': '—'},
    ]

def rec(code, name, heads, kp, evs, scene, size, sw, risk, email_sal,
        inference='R66 第 20 波具名 KP 金谱', trend='2026-10-08 R66 20 波谱名牌', gap='R66 20 波谱面锁定'):
    _push = push_of(code)
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 第 20 波点名(谱面无实名)**'
    dims = {'业务定位': heads, '产品线与在售品牌': '(波次二补谱面)', '目标行业与场景': scene, '团队与规模': size,
            '决策链与对接人': kb, '技术与认证': '(波次二补)', '采购与供应链信号': '(波次二补)',
            '近期动态与线索': trend, '与我方契合点': '24 口 value PoE 谱链窗口', '风险与注意': risk}
    return {'customer': code, 'fact': name + ':' + heads, 'inference': inference,
            'hypothesis': '24 口 value PoE(' + PRICE + ')具名谱位引路', 'evidence_main': evs[0]['source'],
            'tech': '(波次二补)', 'hr': size, 'contact_found': kb, 'contact_pending': '直发具名需 opt-in',
            'dims': dims, 'evidence': evs, 'followups': fu(_push),
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

# ============ 公司档×25 ============
R.append(rec('A-229', 'Stovaris Sp. z o.o',
    'STOVARIS SP. Z O.O.(波兰 Warszawa,ul. Staniewicka 12, 03-310;**KRS 0000758346;NIP PL5242877169;REGON 381832975;cap 240k zł;2018-11-19 登**;**创始三董事均 ex-Alstor Sp.j. 合伙人/前 SDS 部总监=Alstor 系资深分销谱!**;DMS/安全/DC/存储/网络增值分销;**Prokura Katarzyna Kamień 在册**',
    [('Tomasz Paweł Szukała', 'Członek Zarządu(2018 创始董事,股份 80/240)', 'rejestr.io KRS 件', O, 'https://rejestr.io/krs/758346/stovaris'),
     ('Jarosław Adam Kupiec', 'Członek Zarządu(2018 创始董事,80/240)', 'rejestr.io KRS 件', O, 'https://rejestr.io/krs/758346/stovaris'),
     ('Marcin Cichecki', 'Członek Zarządu(2018 创始董事;前 Alstor SDS 销售总监,80/240)', 'rejestr.io+b2b.stovaris.pl 双源', O, 'https://rejestr.io/krs/758346/stovaris'),
     ('Katarzyna Kamień', 'Prokura(总代理)', 'KRS 件', O, 'https://rejestr.io/krs/758346/stovaris')],
    [ev('决策链与对接人', 'Zarząd: Tomasz Paweł Szukała + Jarosław Adam Kupiec + Marcin Cichecki(od 19 listopada 2018;dotychczasowi Wspólnicy Alstor Sp.j. + dyrektor sprzedaży działu Alstor SDS);Prokura: Katarzyna Kamień(rejestr/b2b 件)', 'https://rejestr.io/krs/758346/stovaris'),
     ev('联系方式与基础画像', 'KRS 0000758346;NIP PL5242877169;REGON 381832975;Staniewicka 12, 03-310 Warszawa;kapitał 240.000 zł;rozwiązania DMS/bezpieczeństwo IT/infrastruktura i Data Center/pamięci masowe/sieci(b2b.stovaris.pl 自署)', 'https://b2b.stovaris.pl/o-firmie,10')],
    '波兰华沙 Alstor 系资深分销屋', '中型谱;2018 登',
    ('Alstor 系三驾=资深谱', '中小实体谱', '三董事等权+Kamień 总代直达位', '分销链竞谱'),
    'Szukała/Kupiec/Cichecki 董事位(opt-in 律)', 'Szanowni Państwo,'))

R.append(rec('A-230', '4service s.r.o',
    '4service s.r.o.(捷克 České Budějovice,Novohradská 745/21(法址)+F.A. Gerstnera 2151/6(运营);**IČO 28066235;DIČ CZ28066235;2007-05-11 创 19 年;IT 外包/网管/培训谱;Bošilec 木工车间副谱**;**双 jednatel 2008-08-14 起:Lukáš Janáček+Rostislav Šachl;官网 Vedení 直接邮箱 sachl@/janacek@4service.cz=O 级金谱**',
    [('Rostislav Šachl', 'Jednatel(2008 起;官网 Vedení 自署邮箱 sachl@4service.cz)', '4service.cz 联络页(O)', O, 'https://www.4service.cz/kontakty'),
     ('Lukáš Janáček', 'Jednatel(2008 起;官网 Vedení 自署邮箱 janacek@4service.cz)', '4service.cz 联络页(O)', O, 'https://www.4service.cz/kontakty')],
    [ev('决策链与对接人', 'Statutární orgán: Lukáš Janáček, jednatel(od 14.8.2008)+ Rostislav Šachl, jednatel(od 14.8.2008);Vedení: sachl@4service.cz, janacek@4service.cz(官网联络页自署+podnikatel.cz 登记件)', 'https://www.4service.cz/kontakty'),
     ev('联系方式与基础画像', 'IČ: 28066235;DIČ: CZ28066235;Novohradská 745/21, České Budějovice;helpdesk@4service.cz +420 739 338 766;it@4service.cz;obchod@4service.cz(商务箱 KPI)(官网联络页)', 'https://www.4service.cz/kontakty')],
    '捷克南波西米亚 19 年 IT 外包屋', '小谱;2007 创',
    ('双 jednatel 官网邮箱自署=O 金谱', '小实体谱', 'obchod@ 商务箱+双签直达位', '区域链竞谱'),
    'Šachl/Janáček 直达(opt-in 律)', 'Vážení pánové,'))

R.append(rec('A-231', 'Specto Remote AS',
    'SPECTO REMOTE AS(挪威 Oslo,Nils Hansens vei 5, 0667;**Org.nr 993 433 802;2008-11-27 创;8 人;原名 Brenna i AS(更名谱);养殖/船载定制 ICT 通信谱**;**Daglig leder Christian Larsen(1977 生,兼董事)+Styrets leder Pål Tajet(1956 生)+Prosjektleder Robin Alstad(15 年行业谱,引语件)+Ole Gjermundshaug 董事**',
    [('Christian Larsen', 'Daglig leder(CEO;proff/gulesider 双登记+2018 报件引语)', 'proff.no 登记件', O, 'https://www.proff.no/selskap/specto-remote-as/oslo/bygg-og-anleggsleverand%C3%B8rer/IGFGQFE0CVG'),
     ('Pål Tajet', 'Styrets leder(董事长)', 'proff.no/gulesider 登记件', O, 'https://www.proff.no/selskap/specto-remote-as/oslo/bygg-og-anleggsleverand%C3%B8rer/IGFGQFE0CVG'),
     ('Robin Alstad', 'Prosjektleder(项目长;15 年行业谱;行业报引语)', 'norskebransjemagasinet.no 2018 件', O, 'https://www.norskebransjemagasinet.no/nyheter/artikel/Specto_RemoteAS'),
     ('Ole Gjermundshaug', 'Styremedlem(董事)', 'gulesider 登记件', O, 'https://www.gulesider.no/specto+remote+as+oslo/86107755/bedrift')],
    [ev('决策链与对接人', 'Daglig leder Christian Larsen(f 1977);Styrets leder Pål Tajet(f 1956);styremedlem: Larsen + Ole Gjermundshaug;Prosjektleder Robin Alstad(「Vi leverer det meste av IKT-tjenester」引语)(proff/gulesider/norskebransjemagasinet 件)', 'https://www.proff.no/selskap/specto-remote-as/oslo/bygg-og-anleggsleverand%C3%B8rer/IGFGQFE0CVG'),
     ev('联系方式与基础画像', 'Org.nr 993 433 802;Nils Hansens vei 5, 0667 Oslo(+Bodø 运营谱);stiftet 27.11.2008;8 ansatte;historisk navn Brenna i AS;skreddersydde kommunikasjonssystemer(船/养殖通信)(proff/purehelp 件)', 'https://www.purehelp.no/m/company/details/spectoremoteas/993433802')],
    '挪威 Oslo 8 人定制通信工程屋', '8 人;2008 创',
    ('养殖/海事通信专谱', '小实体谱', 'Larsen CEO+Tajet 董直达位', '区域链竞谱'),
    'Larsen 直达(opt-in 律)', 'Dear Mr. Larsen,'))

R.append(rec('A-232', 'Databox',
    'Databox, Informática S.A.(葡萄牙 Massamá(里斯本);**1985 创 41 年;95-250 人;IT 渠道分销大户**;**Expo TI Databox 官网具名双 CEO: André Reis & João Pedro Reis(族谱双驾=O 金谱);Susana Pereira Networking Product & BD Manager(网络品线 KPI!)+Jorge Matos 产品&库存+José Neves Diretor Comercial+Delfim Gaspar BUM+Jose Aguincha Director+Vitor Gama**;Expo TI 16 届(2026-05-07 Estoril)谱',
    [('André Reis', 'CEO(Expo TI 官网自署双 CEO 谱)', 'expotidatabox.pt 官网(O)', O, 'https://expotidatabox.pt/'),
     ('João Pedro Reis', 'CEO(双 CEO 谱次位)', 'expotidatabox.pt 官网(O)', O, 'https://expotidatabox.pt/'),
     ('Susana Pereira', 'Networking Product & Business Development Manager(网络品线 KPI)', 'rocketreach 谱面条', G, 'https://rocketreach.co/databox-informatica-sa-email-format_b47fa9e7fc4b95ae'),
     ('Jorge Matos', 'Gestor de Produto and Stock(产品&库存=件链口)', 'rocketreach 谱面条', G, 'https://rocketreach.co/jorge-matos-email_76250898'),
     ('José Neves', 'Diretor Comercial / GM Marketing(商务总监)', 'rocketreach 谱面条', G, 'https://rocketreach.co/databox-informatica-sa-email-format_b47fa9e7fc4b95ae')],
    [ev('决策链与对接人', 'Boas-vindas Databox: **André Reis & João Pedro Reis CEOs**(expotidatabox.pt 首屏自署);rocketreach 谱: Susana Pereira(Networking PM/BD)+Jorge Matos(Gestor Produto&Stock)+José Neves(Diretor Comercial)+Delfim Gaspar(BU Manager)+Vladimiro Bordalo(Retail SM)', 'https://expotidatabox.pt/'),
     ev('联系方式与基础画像', 'fundada 1985;95-250 employees;Massamá/Lisboa;+351 21 430 8400;databox@databox.pt;Expo TI Databox 16ª edição 07/05 Centro de Congressos do Estoril(crunchbase/expotidatabox 件)', 'https://www.crunchbase.com/organization/databox-ec20')],
    '葡萄牙里斯本 41 年 IT 渠道分销大户', '95-250 人;1985 创',
    ('双 CEO 族谱+网络品线 PM 具名', '大分销谱', 'Reis 双驾+Pereira 网络 PM 位', '一线链竞谱'),
    'Reis 双 CEO 位+Pereira 网络 PM(opt-in 律)', 'Exmos. Sres.,'))

R.append(rec('A-233', 'Young B.T.S. Ltd',
    'YOUNG B.T.S. Kft.(匈牙利 Budapest,Schweidel u. 11(现)/Frangepán u. 26(留痕);**Adószám 12014347-2-43;Cégjegyzékszám 01-09-367760;1996-09-20 创 30 年;24 人;安防+网络件分销(2N/Ascom/Hikvision/Planet/Excel/Canovate)**;**ügyvezető 双:Orbán Előd István(业主)+Tóth Tibor(Service Manager);官网 Kapcsolat 全谱带姓名邮箱电话=O 金谱**',
    [('Orbán Előd István', 'Ügyvezető+业主(登记谱龟首)', 'nemzeticegtar.hu 登记件', O, 'https://www.nemzeticegtar.hu/young-bts-kft-e10267080.html'),
     ('Tóth Tibor', 'Ügyvezető+Service Manager(双签)', 'nemzeticegtar.hu 登记件', O, 'https://www.nemzeticegtar.hu/young-bts-kft-e10267080.html'),
     ('Várady Gábor', 'Értékesítési menedzser(销售经理;官网联络自署)', 'young.hu Kapcsolat 页(O)', O, 'https://www.young.hu/rolunk/elerhetosegeink'),
     ('Pásztor András', 'Termékmenedzser(产品经理 2N/Ascom/Hikvision 品线=落位 KPI)', 'young.hu Kapcsolat 页(O)', O, 'https://www.young.hu/rolunk/elerhetosegeink'),
     ('Szpodnyi Marianna', 'Gazdasági igazgató(经济总监 CFO)', 'young.hu Kapcsolat 页(O)', O, 'https://www.young.hu/rolunk/elerhetosegeink')],
    [ev('决策链与对接人', 'Cégjegyzésre jogosultak: Orbán Előd István(ügyvezető)+ Tóth Tibor(ügyvezető);官网谱: Várady Gábor 销售经理+Pásztor András 产品经理(pasztor.andras@young.hu)+Szőke Árpád 物流+Tuza Éva 客服+Szpodnyi Marianna 经济总监(nemzeticegtar/young.hu 件)', 'https://www.young.hu/rolunk/elerhetosegeink'),
     ev('联系方式与基础画像', 'Alapítás 1996.09.20;24 employees;Budapest Schweidel u. 11;4690 混合批发;**2N 门禁/Ascom/Hikvision/Uniview 分销+Planet/Excel/Canovate 网络件**;BBB bonus 评(nemzeticegtar/rocketreach/securifocus 件)', 'https://www.nemzeticegtar.hu/young-bts-kft-e10267080.html')],
    '匈牙利布达佩斯 30 年安防+网络分销屋', '24 人;1996 创',
    ('官网联络页 O 级全谱+采购线名分', '分销谱', 'Várady 销售+Pásztor 品线直达位', '一线链竞谱'),
    'Várady 销售经理+Pásztor 产品(opt-in 律)', 'Tisztelt Várady Úr!',
    trend='2026-10-08 R66 20 波谱名牌(官网联络全谱)'))

R.append(rec('A-234', 'Varia Group',
    'VARIA Group / VARIA System GmbH(德国 Chemnitz,Dr.-Salvador-Allende-Str. 191, 09119;**2000-01-01 创 26 年;GmbH**;**网络技术/嵌入式/电信分销+自产牌「VARIA Group」+varia-academy 培训谱**;**GF 双创: Sven Huth+Sven Grimpe(2019 Scalcom 件 Grimpe 引语=60/80GHz SIKLU 分销签约语)**;**异体排噪:Varia Group AG(Baar ZUG,瑞士,Lukas Thoma)=已分层**',
    [('Sven Grimpe', 'Geschäftsführer(联创;2019 SIKLU 分件官方引语)', 'scalcom.de 新闻件(引语)', O, 'https://www.scalcom.de/blog/post/varia-group-siklu-richtfunk/'),
     ('Sven Huth', 'Geschäftsführer(联创双驾)', 'wikipedia 草稿谱/官网件', G, 'https://www.varia.org/en/portfolio/varia/')],
    [ev('决策链与对接人', 'Leitung: Sven Huth, Sven Grimpe(VARIA System GmbH, Chemnitz);「Mit Siklu haben wir diesen gefunden… so Sven Grimpe, Geschäftsführer Varia Group」(SCALCOM 2019 分件引语)', 'https://www.scalcom.de/blog/post/varia-group-siklu-richtfunk/'),
     ev('联系方式与基础画像', 'VARIA System GmbH, Dr.-Salvador-Allende-Str. 191, 09119 Chemnitz;gegründet 01.01.2000;Distribution: Embedded/Netzwerk/Wireless/GPS/IoT/Videoüberwachung/Smart Home/LWL;varia.org/varia-store.com/varia-academy.de;**异体 Varia Group AG Baar(Thoma)已分层**(varia.org/wiki 草稿件)', 'https://www.varia.org/en/portfolio/varia/')],
    '德国萨克森 26 年无线/嵌入式分销屋', '中型谱;2000 创',
    ('SIKLU 60/80GHz 谱=毫米波件链', '分销谱', 'Grimpe 引语直达位', '一线链竞谱'),
    'Sven Grimpe 直达(opt-in 律)', 'Guten Tag Herr Grimpe,'))

R.append(rec('A-238', 'Infinite Technology',
    'Infinite Technology Limited(爱尔兰 Dublin,Unit E3 Block E Centre Point Business Park, Oak Road, Dublin 12;**IE269984;1997-07-30 创 29 年;27-33 人 ICT MSP(Microsoft/IBM/Lenovo/Dell/Cisco/HP 盟谱)**;**Key Executive: Michael Corr(Mr Corr=28 年在任 Director 谱;Owner 谱)+Angela Corr Director+Pat Henderson Director;Gougane Holdings 集团谱**',
    [('Michael Corr', 'Owner/Director(1997 创铺即在;vision-net Key Executive+RR Owner 双谱)', 'vision-net.ie 件', O, 'https://www.vision-net.ie/Company-Info/Infinite-Technology-Limited-269984'),
     ('Angela Corr', 'Director(族谱)', 'globaldatabase 件', G, 'https://ie.globaldatabase.com/company/infinite-technology-limited'),
     ('Pat Henderson', 'Director', 'globaldatabase 件', G, 'https://ie.globaldatabase.com/company/infinite-technology-limited'),
     ('Neil Edmonds', 'Technical Operations Manager(技术运营)', 'rocketreach 谱面条', G, 'https://rocketreach.co/infinite-technology-profile_b5cfada8f42e0a16')],
    [ev('决策链与对接人', 'Key Executive: Mr Corr(company director since 1997;5 他社 Director 谱);Leadership: MICHAEL CORR Director+ANGELA CORR Director+Pat Henderson Director;Neil Edmonds Technical Operations Manager(vision-net/gd/RR 件)', 'https://www.vision-net.ie/Company-Info/Infinite-Technology-Limited-269984'),
     ev('联系方式与基础画像', 'established 30/07/1997;Unit E3 Block E Centre Point Business Park, Dublin 12;+353 1 293 9000;27-33 employees;ICT Managed Services/Cloud/Cyber;Irish owned MSP(GD/crunchbase 件);**排噪:zoominfo 东南亚异体(Wanna/Chungpanich)分层**', 'https://www.crunchbase.com/organization/infinite-technology-e4d6')],
    '爱尔兰都柏林 29 年 ICT MSP 屋', '27-33 人;1997 创',
    ('29 年 Owner 亲政谱', 'MSP 谱', 'Corr Owner 直达位', '一线盟链竞谱'),
    'Michael Corr 直达(opt-in 律)', 'Dear Mr. Corr,'))

R.append(rec('A-242', 'Mikrotik Warsaw Training Center',
    'MikroTik Warsaw Training Center(MWTC)(波兰 Warszawa,ul. Ogrodowa 58(4 楼),00-876;**NIP 1132330628;2016 创;2-10 人;波兰最大 MikroTik 培训中心(官方全证谱 MTCNA..MTCUME+Zabbix ZCS/ZCP/ZCE 双证;UE/PARP/KFS 资助课;Proxmox/Windows 副谱)**;**官网 Trainers 页全谱:Michał Filipek(MikroTik+Zabbix+Ubiquiti 三证师)+Piotr Wasyk(**Właściciel 业主**,华沙理工 2004 入行;PARP BUR 件)+Ihor Hreskiv(塔尔诺波尔工大;MBUM/MUM 2019 演讲谱)+Iwona Wasyk(Frontend 族谱)**',
    [('Piotr Wasyk', 'Network Architect/Trener/**Właściciel**(业主;官网教练页+RR+PARP 件三源)', 'mwtc.pl/aboutUs.php+RR 双源', O, 'https://mwtc.pl/aboutUs.php'),
     ('Michał Filipek', 'Network Architect/MikroTik+Zabbix+Ubiquiti Trainer(三证教练)', 'mwtc.pl 教练页(O)', O, 'https://mwtc.pl/aboutUs.php'),
     ('Ihor Hreskiv', 'Certified MikroTik Trainer(乌克兰谱;MUM 2019 演讲者)', 'mwtc.pl 教练页(O)', O, 'https://mwtc.pl/aboutUs.php'),
     ('Iwona Wasyk', 'Frontend Developer(族谱)', 'LinkedIn 公司页员工谱', G, 'https://pl.linkedin.com/company/mikrotik-warsaw-training-center')],
    [ev('决策链与对接人', 'Trainers: Michał Filipek(Zabbix/MikroTik/Ubiquiti Trainer 全证);Piotr Wasyk(Właściciel;MikroTik+Ubiquiti Trainer;Pw BM 2004 起);Ihor Hreskiv(MikroTik Trainer;MBUM/MUM 演讲谱);Iwona Wasyk Frontend(mwtc.pl 教练页自署+LI/RR/PARP BUR 件)', 'https://mwtc.pl/aboutUs.php'),
     ev('联系方式与基础画像', 'Ogrodowa 58, 00-876 Warszawa(Wola);NIP 1132330628;+48 796 171 971;info@mwtc.pl;**największe centrum szkoleniowe MikroTik w Polsce**;MTCNA/MTCRE/MTCSE/MTCWE/MTCTCE/MTCIPv6E/MTCSWE/MTCEWE/MTCUME/MTCINE 全证;UE/PARP/KFS dofinansowanie(schoolandcollege/LI/PARP 件)', 'https://pl.linkedin.com/company/mikrotik-warsaw-training-center')],
    '波兰华沙最大 MikroTik 培训中心', '2-10 人;2016 创',
    ('培训中心谱=课程对照单元窗', '培训谱', 'Wasyk 业主直达位', 'MikroTik 官方课链'),
    'Wasyk 业主+Filipek 教练位(opt-in 律;OEM 探询)', 'Szanowny Panie Wasyk,'))

R.append(rec('A-253', 'Noriak Distribution',
    'MICRO TECH DISTRIBUTION(=NORIAK DISTRIBUTION)(法国 Cesson-Sévigné(雷恩东),9 rue de la Frébardière ECOPOLE SUD EST, 35510;**SIREN 489533711;TVA FR96489533711;28 人;4652 电信电子件批发**;**Président/Gérant: Stéphane Crocq(2017-05 起 Président;2014 Gérant 谱;tel: 02 99 04 32 50)**;**Network Critical(NPB/TAP)法国独家分销**;联络 myriam.chaibddera@noriak-distri.com 具名',
    [('Stéphane Crocq', 'Président(2017-05 起;前 Gérant 2014 谱;pappers/BODACC 双件)', 'pappers.fr 件', O, 'https://www.pappers.fr/entreprise/micro-tech-distribution-489533711'),
     ('Myriam Chaib Ddera', '商务联络具名(@noriak-distri.com)', 'rocketlead 谱面条', G, 'https://rocketlead.fr/annuaire/micro-tech-distribution-48953371100037')],
    [ev('决策链与对接人', 'Dirigeant: Crocq Stéphane, Président(depuis 04/05/2017;Gérant BODACC 2014 留痕);contacter: myriam.chaibddera@noriak-distri.com(pappers/rocketlead 件)', 'https://www.pappers.fr/entreprise/micro-tech-distribution-489533711'),
     ev('联系方式与基础画像', '9 rue de la Frébardière, 35510 Cesson-Sévigné;SIREN 489 533 711;28 salariés;02 99 04 32 50;**Network Critical: Noriak Distribution = distributeur exclusif pour la France(NPB/TAP/Packet Broker)**(verif/noriak-reseau.com 件)', 'https://www.noriak-reseau.com/Partenaires/Network-critical_238.html')],
    '法国布列塔尼 28 人网络可视线分销屋', '28 人;2006 前史谱',
    ('NC 法国独家=网可视专谱', '分销谱', 'Crocq 直达位', '一线链竞谱'),
    'Stéphane Crocq 直达(opt-in 律)', 'Monsieur Crocq,'))

R.append(rec('A-254', 'Connect Data',
    'CONNECT DATA(法国 Bièvres(埃松省);**SIREN 321239287;TVA FR78321239287;19 人;€11.7M;无线+有线方案分销(ISP/电信运营商+Voix Data 集成商;法国本土+海外省+非洲)**;**2022 Connect Data+Sintel France 同集团合并=现 Connect Data(GLOBE TECH 层谱)**;**Président: Dominique Renaudie(2024-08-07 起;FINANCIERE CONNECT DATA 382731370 独东谱;contactout 谱「Dominique Claude-Renaudie Managing Partner」)**',
    [('Dominique Renaudie(Claude-Renaudie)', 'Président(2024-08 起;Managing Partner 谱)', 'pappers.fr+contactout 双源', O, 'https://www.pappers.fr/entreprise/connect-data-522513399'),
     ('Fateh Ziani', 'Gérant principal(首席经理;contactout 谱面条)', 'contactout 谱面条', G, 'https://contactout.com/company/Connect-Data-85564'),
     ('Ladislas Mollet', 'Directeur des opérations(运营总监=件链口 KPI)', 'contactout 谱面条', G, 'https://contactout.com/company/Connect-Data-85564'),
     ('Laurent Monnet', 'Sales Engineer(售前工程)', 'contactout 谱面条', G, 'https://contactout.com/company/Connect-Data-85564'),
     ('Rachid Benamrouche', "Chargé d'affaires CFO/CFA(商务)", 'contactout 谱面条', G, 'https://contactout.com/company/Connect-Data-85564')],
    [ev('决策链与对接人', 'Président: RENAUDIE Dominique(depuis 07/08/2024);FINANCIERE CONNECT DATA(382731370)Associé unique 谱;2022: Connect Data et Sintel France fusionnent au sein de leur maison-mère renommée Connect Data;队谱: Fateh Ziani(Gérant principal)+Ladislas Mollet(Directeur des opérations)+Laurent Monnet(Sales Engineer)(pappers/contactout 件)', 'https://www.pappers.fr/entreprise/connect-data-522513399'),
     ev('联系方式与基础画像', 'Bièvres;19 employés;11.677 K€ CA;distributeur de solutions Wireless et filaires pour Opérateurs Télécoms/ISP/intégrateurs Voix Data;France métropolitaine+Outremer+Afrique(verif/contactout 件)', 'https://www.verif.com/societe/CONNECT-DATA-321239287/')],
    '法国埃松 19 人 ISP 无线分销屋(非洲谱)', '19 人;€11.7M',
    ('ISP 件链+非洲谱=出口窗', '分销谱', 'Renaudie+Mollet 运营口直达位', '一线链竞谱'),
    'D. Renaudie+Mollet 运营位(opt-in 律)', 'Monsieur Renaudie,'))

R.append(rec('A-255', 'The Junction',
    'THE JUNCTION(挪威;档锚 thejunction.eu;R66 检索两轮未锁主谱(同名群噪大:医疗 Junction/LNU 网架等)→**守档准由:谱面未见具名决策人,档锚留档待二批专查**)',
    [],
    [ev('决策链与对接人', '公开谱面检索两轮未锁具名决策人=守档准由;档锚 https://thejunction.eu(2026-10-08 R66 20 波留痕)', 'https://thejunction.eu/'),
     ev('近期动态与线索', 'R66 20 波档案点名:The Junction 挪威谱,待专批域名锚深查(thejunction.eu Whois/站点页)', 'https://thejunction.eu/'),
     ev('联系方式与基础画像', '档录类型: 公司/工作室(有官网);工程/集成项目制(档案基础画像行)', 'https://thejunction.eu/')],
    '挪威 The Junction 谱(锚待专查)', '守档案',
    ('—', '短名噪声谱', '无守档', '—'),
    '守档:锚在名缺(待专批 thejunction.eu 深查)', 'Dear Sir or Madam,'))

R.append(rec('A-256', 'Timeless Technology',
    'Timeless Technology / Timeless Group Oy(芬兰 Pori,Keulantie 1 D 30, 28190;**Y-tunnus 3139264-1;FI31392641;史 2012,现体 2020-06-01(aputoiminimi=Timeless Technology+Mansimar);1-2 人(2024)**;**ICT/工业 IoT/测量技术增值进口分销;CEO Kari Ruhanen(官方 viralliset tiedot PDF 自署=O 金谱;Yrittäjä 谱);Profitap 网络可视线谱;Suomen Yrittäjät 会员**',
    [('Kari Ruhanen', 'CEO/Yrittäjä(官方公司信息 PDF 自署+itewiki 双源)', 'timeless.fi 官方 PDF(O)', O, 'https://timeless.fi/wp-content/uploads/2023/12/Timeless-Technology-viralliset-tiedot-2023.pdf')],
    [ev('决策链与对接人', '**CEO: Kari Ruhanen**(Timeless-Technology-viralliset-tiedot-2023.pdf 官方自署);itewiki 谱: Kari Ruhanen CEO Yrittäjä(双源一致)', 'https://timeless.fi/wp-content/uploads/2023/12/Timeless-Technology-viralliset-tiedot-2023.pdf'),
     ev('联系方式与基础画像', 'Timeless Group Oy;aputoiminimet: Timeless Technology + Mansimar;Keulantie 1 D 30, 28190 Pori;Y-tunnus 3139264-1;+358 44 9988238;info@timeless.fi;tilikaudella 05/2024: 1 työntekijä=小微谱注;ICT/teollinen IoT/mittaustekniikka maahantuoja(timeless.fi/finder.fi/fonecta 件)', 'https://timeless.fi/yritys/'),
     ev('近期动态与线索', 'Profitap verkkoVisibility 谱;Suomen Yrittäjät jäsenyys;perustettu 2012(itewiki 历史)→2020-06-01 现体(finder.fi 件)', 'https://www.itewiki.fi/timeless-technology')],
    '芬兰 Pori 1-2 人 ICT/IoT 进口商', '1-2 人;谱史 2012',
    ('CEO 官方 PDF 自署=O 金谱', '微实体谱', 'Ruhanen 唯一直达位', '区域链竞谱'),
    'Kari Ruhanen 单铺直达(opt-in 律)', 'Dear Mr. Ruhanen,'))

R.append(rec('A-257', 'DSSI',
    'DSSI - Tecnologias de Informação, Lda(葡萄牙 Agualva-Cacém,Zoom Business Park Ed. E Piso 1 Esc. 3, Estrada de Paço de Arcos, 2735-307;**PT 509371655;2010-04-27 创 16 年;7-11 人;增值分销(Ubiquiti/Sophos/Riverbed/Solarwinds/Nakivo/Retrospect/Code42/ownCloud/Hitachi/SpectraLogic)**;**Managing Partner Gonçalo Filipe Mello(Fialho Nunes de Mello;Director 2010 创始;northdata+itchannel 联络具名;dssi.co.ao/.mz 安哥拉/莫桑米格牌=葡语非洲谱)+Patrícia Rodrigues Director+Alexandra Matos 销售+Pedro Gomes 技术**',
    [('Gonçalo Filipe Mello', 'Managing Partner/Director(2010 创始;itchannel 目录联络具名=E-mail 直线)', 'itchannel.pt 目录件+RR 双源', O, 'https://www.itchannel.pt/directorio/distribuidores/dssi---tecnologias-de-informacao-lda'),
     ('Patrícia Cristina Cebola Romão Rodrigues', 'Director(2010 双董事谱)', 'northdata 件', O, 'https://www.northdata.com/Dssi%20-%20Tecnologias%20de%20Informa%C3%A7%C3%A3o%20Lda%C2%B7,%20Cac%C3%A9m/PT%20509371655'),
     ('Alexandra Matos', 'Sales and Assistent Marketing(销售口)', 'rocketreach 谱面条', G, 'https://rocketreach.co/dssi-data-systems-portugal-management_b5e68ee2f42e589c'),
     ('Pedro Gomes', 'IT Technical Support(技术谱)', 'rocketreach 谱面条', G, 'https://rocketreach.co/dssi-data-systems-portugal-management_b5e68ee2f42e589c')],
    [ev('决策链与对接人', 'Managing Partner: Gonçalo Filipe Mello;Director(2): Fialho Nunes de Mello + Romão Rodrigues(northdata 2010 件);Contacto: Gonçalo Mello(itchannel 目录自署);队谱: Alexandra Matos(Sales)+Pedro Gomes(IT Support)+Magno Gandorini+Pedro Pena(RR 谱面条)', 'https://www.itchannel.pt/directorio/distribuidores/dssi---tecnologias-de-informacao-lda'),
     ev('联系方式与基础画像', 'PT 509371655(2010-04-27 登);Zoom Business Park, Agualva-Cacém;218 051 560;www.dssi.pt;Principais Marcas: Riverbed, Sophos, **Ubiquiti**, Solarwinds, Nakivo, Hitachi, SpectraLogic;**dssi.co.ao(安哥拉)+dssi.co.mz(莫桑)=葡非扩展谱**(itchannel/RR/ensun 件)', 'https://www.itchannel.pt/directorio/distribuidores/dssi---tecnologias-de-informacao-lda')],
    '葡萄牙 Cacém 7-11 人增值分销屋(葡非谱)', '7-11 人;2010 创',
    ('Ubiquiti 谱+葡非牌=邻链窗', '分销谱', 'Mello MP+Matos 销售直达位', '一线链竞谱'),
    'Gonçalo Mello 直达(opt-in 律)', 'Estimado Sr. Mello,'))

R.append(rec('A-262', 'NetHighTech',
    'NETHIGHTECH(葡萄牙 Lisboa;**MikroTik 官方培训页具名主谱:MTCNA/MTCRE/MTCSWE/MTCIPv6E 英文班(mikrotik.com/training/europe=O)**;**官方 AI 转型谱:NetHighTech-3 AI BI 平台+NetHighTech-7 租车 AI 平台(2025-10 LinkedIn 公司帖;寻战略投资谱)**;DC/服务供应商方案;档谱「培训交付」印谱对位;**谱面暂未见具名决策人→守档准由注记(培训实体主谱在档)**',
    [],
    [ev('联系方式与基础画像', 'MikroTik Training Schedule: Portugal, Lisboa — NetHighTech(MTCNA/MTCRE/MTCSWE/MTCIPv6E, English)(mikrotik.com/training/europe 官方页)', 'https://mikrotik.com/training/europe'),
     ev('近期动态与线索', '2025-10 LinkedIn 公司帖: NetHighTech-3(AI BI 平台)+NetHighTech-7(AI 租车平台)寻 strategic investors/partners(LI 公司页件)', 'https://www.linkedin.com/in/nethightech-company/'),
     ev('决策链与对接人', '谱面暂未检索到具名决策人=守档准由;2026-10-08 再核实留痕(R66 20 波点名)', 'https://www.nethightech.com/')],
    '葡里斯本 MikroTik 官训商+AI 新谱', '小谱;转型窗',
    ('官训主谱+AI 引资窗', '转型谱', '无守档', '—'),
    '守档:培训主谱在档,具名待专批点名', 'Exmos. Sres.,'))

R.append(rec('A-263', 'ATYS Co Controll Enginering',
    'ATYS-CO Kft.(匈牙利 Budapest,Fertő u. 14, 1107(+Algyő JURA 工业园谱);**Adószám 12060991-2-42;Cégjegyzékszám 01-09-462105;1995/1997 创 30+ 年;工业设备安装/控制工程(irányítástechnika);nettó árbevétel 6,36 Md Ft(2025)=~€16M 中大型谱;电气工程师/程序员实习谱**;**ügyvezető 双:Jász Ottó(印谱 ifj.jasz.otto@atysco.hu=O 直邮!)+Szedlák-Jász Ágnes(夫妇/家族谱);Csapkovics Roxána HR 联络具名**',
    [('Jász Ottó', 'Ügyvezető igazgató(印谱自署邮箱=O 级直邮)', 'atysco.hu impresszum+nemzeticegtar 双源', O, 'https://www.atysco.hu/hu/karrier/aktualis-poziciok'),
     ('Szedlák-Jász Ágnes', 'Ügyvezető(业主;家族谱)', 'nemzeticegtar.hu 登记件', O, 'https://www.nemzeticegtar.hu/atys-co-kft-e10290068.html'),
     ('Csapkovics Roxána', '联络具名(科教实习口;csapkovics.roxana@atysco.hu)', 'u-szeged 实习目录件', O, 'https://home.inf.u-szeged.hu/hallgatoknak/szakmai-gyakorlat/cegek/atys-co-kft'),
     ('Ágh Zsolt / Bódis István / Világos Csaba', '管理层员工谱(登记谱)', 'nemzeticegtar.hu 登记件', O, 'https://www.nemzeticegtar.hu/atys-co-kft-e10290068.html')],
    [ev('决策链与对接人', 'Ügyvezető: Jász Ottó + Szedlák-Jász Ágnes;员工谱: Ágh Zsolt/Bódis István/Világos Csaba;Impresszum: Ügyvezető Igazgató Jász Ottó, ifj.jasz.otto@atysco.hu(nemzeticegtar/atysco.hu 件)', 'https://www.nemzeticegtar.hu/atys-co-kft-e10290068.html'),
     ev('联系方式与基础画像', '1107 Budapest Fertő u. 14;Adószám 12060991-2-42;alapítás 1995;**nettó árbevétel 6 365 412 ezer Ft(2025)**;3320 ipari gép üzembe helyezése;telephely: Algyő JURA Ipari Park;30+ 年(opten/companywall 件)', 'https://webshop.opten.hu/atys-co-kft-e10290068.html')],
    '匈布达佩斯 30 年工业控制工程屋(€16M)', '中大型谱;1995 创',
    ('€16M 工业安装=件链大户', '工业工程谱', 'Jász Ottó 独任印谱直邮位', '工业链竞谱'),
    'Jász Ottó 直达(opt-in 律)', 'Tisztelt Jász Úr!'))

R.append(rec('A-264', 'Cogent Distribution',
    'Cogent Distribution Ltd(英国 Newbury(Berkshire),Technology House, Kennetside, Bone Lane, RG14 5PX;**2015 创 11 年;无线/网络增值分销 UK&I+欧陆+非洲中东;品牌谱 RADWIN/SAF Tehnika/Teltonika/Peplink/RF elements/Perle/Siklu Ceragon/Nextivity/Kymata/CableFree**;**MD Jim Kernahan(官网 about+Business Voice Q&A+海事新闻件三 O 引语)+Solutions Manager Mark Turvey(solutions@=O)+Marketing Manager Louisa Mamakou+Sales Director Anita Mistry(CableFree 件引语);2022-11 RADWIN 分约;2025 海事连通线+UK Ports 会员谱**',
    [('Jim Kernahan', 'Managing Director(官网+媒体三件引语=O)', 'cogentdistribution.com about 页(O)', O, 'https://www.cogentdistribution.com/about/'),
     ('Mark Turvey', 'Solutions Manager(solutions@cogentdistribution.com)', '官网新闻件署名(O)', O, 'https://www.cogentdistribution.com/latest-news/cogent-distribution-launches-maritime-connectivity-solutions/'),
     ('Louisa Mamakou', 'Marketing Manager(louisa.mamakou@=O)', '官网新闻件署名(O)', O, 'https://www.cogentdistribution.com/latest-news/cogent-distribution-launches-maritime-connectivity-solutions/'),
     ('Anita Mistry', 'Sales Director(CableFree 伙件引语)', 'cbinsights 件(引语)', O, 'https://www.cbinsights.com/company/cogent-distribution')],
    [ev('决策链与对接人', 'MD: Jim Kernahan(官网 about 自署;Business Voice Q&A 2025-03;海事 launch 件 2025-04:「Our team has extensive experience working with the maritime…」);Contacts: Mark Turvey Solutions Manager + Louisa Mamakou Marketing;Sales Director Anita Mistry(CableFree 伙件)', 'https://www.cogentdistribution.com/about/'),
     ev('联系方式与基础画像', 'Technology House, Kennetside, Bone Lane, Newbury RG14 5PX;+44 1635 917 722;enquiries@cogentdistribution.com;founded 2015;VAD: RADWIN/SAF Tehnika/Teltonika/Peplink/RF elements/Perle/Siklu/Nextivity/Kymata/CableFree;UK Ports member 2025(官网/X 件)', 'https://www.cogentdistribution.com/about/')],
    '英国伯克希尔无线增值分销屋(海事谱)', '中型谱;2015 创',
    ('全品牌谱=件链大户;海事 2025 窗', '分销谱', 'Kernahan MD+Turvey 方案位', '一线链竞谱'),
    'Jim Kernahan+Mark Turvey 位(opt-in 律)', 'Dear Jim,'))

R.append(rec('A-265', 'Sphinx Connect',
    'SPHINX CONNECT FRANCE(法国 Boufféré/Montaigu-Vendée(旺代),Parc de la Bretonnière, 85600;**SIREN 439398462;TVA FR27439398462;2001-10-01 创 25 年;SARL→2015-11-24 转 SAS;cap €150k;20-49 人;€5.58M(2014)**;**Moxa 法国谱(别名录 MOXA FRANCE/MOXANET=工业网络强契!)+A2-LINE 谱**;**Président=SOENNO(SARL,RCS 518740634)代表 Hervé Mathé(创始人/实控受益人;Noellia Mathé Personnel Manager 族谱)**',
    [('Hervé Mathé', 'Founder/实控受益人(SOENNO Président 代表;2015 SAS 转制件)', 'pappers.fr/BODACC 件', O, 'https://www.pappers.fr/entreprise/sphinx-connect-france-439398462'),
     ('Noellia Mathé', 'Personnel Manager(族谱;D&B Key Principal)', 'D&B/verif 件', G, 'https://www.dnb.com/business-directory/company-profiles.sphinx_connect_france.1b707273841a0223db6298ea0c684e6a.html')],
    [ev('决策链与对接人', 'Président: SOENNO représentée par Hervé Mathé(2015-11-24 SAS 转制公告);bénéficiaires effectifs: Hervé MATHE(A2-LINE 谱);Noellia MATHE Personnel Manager(pappers/verif/D&B 件)', 'https://www.pappers.fr/entreprise/sphinx-connect-france-439398462'),
     ev('联系方式与基础画像', 'SIREN 439 398 462;création 01/10/2001;Parc de la Bretonnière, 85600 Boufféré/Montaigu-Vendée;cap €150.000;20-49 salariés;NAF 4651Z;**alias: MOXA FRANCE/MOXATECH/MOXANET**(pappers 件)=Moxa 工业网络谱', 'https://www.pappers.fr/entreprise/sphinx-connect-france-439398462')],
    '法国旺代 25 年工业网络件分销屋(Moxa)', '20-49 人;2001 创',
    ('Moxa 法国谱=工业件链', '分销谱', 'Mathé 族直达位', 'Moxa 自家链谱'),
    'Hervé Mathé 直达(opt-in 律)', 'Monsieur Mathé,'))

R.append(rec('A-266', 'Andisa IT',
    'ANDISA IT CONSULTANTS LTD(英国 Harrogate(N. Yorkshire),Suite 1, 1 Cardale Park, HG3 1RY;**Companies House 04994671;2003-12-15 创 22 年;3 人 IT 咨询(62020)**;**MD Andrew Charles David Morrison(2003 创始;PSC 25-50%;LI 500+连;Rotary 谱)+Jayne Isabel Morrison Director+Secretary(2010 任;PSC 25-50%=夫妇同权谱)+Ashley Hill IT Consultant**',
    [('Andrew Charles David Morrison', 'Managing Director(2003 创主;PSC 个体 25-50%)', 'Companies House 件(O)', O, 'https://find-and-update.company-information.service.gov.uk/company/04994671/officers'),
     ('Jayne Isabel Morrison', 'Director+Company Secretary(2010 任;PSC 25-50%)', 'Companies House 件(O)', O, 'https://find-and-update.company-information.service.gov.uk/company/04994671/officers'),
     ('Ashley Hill', 'IT Consultant(Leeds 谱)', 'rocketreach 谱面条', G, 'https://rocketreach.co/andisa-it-consultants-ltd-profile_b40d1a46ffbf1c5d')],
    [ev('决策链与对接人', 'Directors: MORRISON Andrew Charles David(appointed 15/12/2003;individual PSC 25-50%)+ MORRISON Jayne Isabel(06/04/2010;PSC 25-50%;Secretary since 2003);Affinity: 夫妇同权谱(companieshouse 官件)', 'https://find-and-update.company-information.service.gov.uk/company/04994671/officers'),
     ev('联系方式与基础画像', 'Suite 1, 1 Cardale Park, Harrogate HG3 1RY;04994671;incorporated 2003-12-15;3 employees;SIC 62020 IT consultancy;RocketReach: Andrew Morrison MD + Ashley Hill(CH/RR/LI 件)', 'https://companycheck.co.uk/company/04994671/ANDISA-IT-CONSULTANTS-LTD/companies-house-data')],
    '英国哈罗盖特 22 年 IT 咨询双人铺', '3 人;2003 创',
    ('夫妇同权谱=决策直达', '微实体谱', 'Morrison MD 直达位', '区域链竞谱'),
    'Andrew Morrison 直达(opt-in 律)', 'Dear Andrew,'))

R.append(rec('A-267', 'IndustrialComms',
    'IndustrialComms / Industrial Communication Products Ltd(英国 Toddington(Bedfordshire);**2008 创 18 年;2-10 人;工业级通信件 B2B 专营(UK&Eire 工业/公用事业)**;**CEO Graham Bull(Advantech 2021 XII 分件官方引语=O)**;品牌谱 **Hirschmann/RuggedCom/Advantech/Siemens Scalance/ATOP(IEC 61850 变电站+EN50155 轨交谱)**;SHDSL/VDSL/以太延长谱;水电交通=公用守界注',
    [('Graham Bull', 'CEO(Advantech 2021 分件官方引语)', 'designsolutionsmag.co.uk 件(引语)', O, 'https://designsolutionsmag.co.uk/advantech-chooses-industrialcomms-as-uk-distributor/')],
    [ev('决策链与对接人', '「IndustrialComms CEO, Graham Bull, said: IndustrialComms is pleased to have access to the comprehensive range of Advantech industrial communication products」(Advantech 2021 分约件引语)', 'https://designsolutionsmag.co.uk/advantech-chooses-industrialcomms-as-uk-distributor/'),
     ev('联系方式与基础画像', 'Toddington, Beds;founded 2008;2-10 employees;020 3086 9569;**specialist distributor: Hirschmann/RuggedCom/Advantech/Siemens Scalance/ATOP(IEC 61850-3 substation+EN 50155 rail)**;UKs leading b2b supplier of Industrial Grade Communication Products(linkedin/facebook 件)', 'https://uk.linkedin.com/company/industrial-communication-products-ltd')],
    '英国贝德福德 18 年工业通信件专营分销', '2-10 人;2008 创',
    ('变电站/轨交认证件谱=OT 强契', '专营分销谱', 'Bull CEO 直达位', '一线牌链竞谱'),
    'Graham Bull 直达(opt-in 律;水电公用守界)', 'Dear Graham,'))

R.append(rec('A-268', '5Gstore',
    '5Gstore(.com)(美国 Crystal Lake, Illinois;**2019-02 创(前体 3Gstore 2005;再前 MDG Connected Solutions 1988=38 年电商老将谱);11-50 人**;**CEO/Founder Michael Ginsberg(theorg+CB+X 三源一致;Northern Illinois University 谱)**;**4G/5G 蜂窝件链:Peplink warranties/licenses+Sierra Wireless licenses+Accelerated cloud+Simply Bonding+onsite installation 谱**',
    [('Michael Ginsberg', 'CEO/Founder(theorg/CB/X 自署三源)', 'theorg.com 件(O)', O, 'https://theorg.com/org/5gstore/org-chart/michael-ginsberg')],
    [ev('决策链与对接人', 'CEO and Founder: Michael Ginsberg(5Gstore 2019-02 创;3Gstore 2005;MDG Connected Solutions 1988)(theorg/crunchbase/success.ai 件)', 'https://theorg.com/org/5gstore/org-chart/michael-ginsberg'),
     ev('联系方式与基础画像', 'Crystal Lake, IL;11-50 employees;Services: Peplink Warranties & Licenses/Sierra Wireless Licenses/Accelerated cloud/Simply Bonding/onsite installation(crunchbase 件)=蜂窝路由件链专营', 'https://www.crunchbase.com/organization/5gstore')],
    '美伊利诺伊 4G/5G 蜂窝件链专营店', '11-50 人;2019 创',
    ('Peplink/Sierra 谱=MR 件链窗', '专营店谱', 'Ginsberg 直达位', 'Peplink 链竞谱'),
    'Michael Ginsberg 直达(opt-in 律)', 'Dear Michael,'))

R.append(rec('A-269', 'Micro Technology Consultants',
    'Micro Technology Consultants, Inc. (MTC)(美国 Warner Robins, Georgia,132 Osigian Blvd Suite 200, 31088;**1990 创 36 年;14,000 平写字楼+服务中心+仓;网络/服务器/备份/安防/门禁一件套集成**;**Founder: Randy Smith(官网 about 自署=O)+Key Principal: Charles R Smith(D&B=代际谱注)**;**佐治亚 100+ 学校 ERATE 谱+25+ 新建校 turnkey=K-12 公段守界加厚**',
    [('Randy Smith', 'Founder(1990 创始;官网 about 自署)', 'microtechnology.net/about(O)', O, 'https://www.microtechnology.net/about'),
     ('Charles R Smith', 'Principal(D&B Key Principal;Smith 族代际谱)', 'D&B 件', G, 'https://www.dnb.com/business-directory/company-profiles.micro_technology_consultants_inc.6275bd998a99fbdddadd132d94a75814.html')],
    [ev('决策链与对接人', '「Micro Technology Consultants, Inc. (MTC), was founded in 1990 by Randy Smith」(官网 about 自署);Key Principal: CHARLES R SMITH(D&B 件)=Smith 族双代谱', 'https://www.microtechnology.net/about'),
     ev('联系方式与基础画像', '132 Osigian Blvd, Warner Robins GA 31088;(478) 953-1921;founded 1990;**ERATE services to over 100 schools in Georgia;25+ new-construction school turnkey**;in-house 全包不外包谱;14,000 sqft 铺(官网/yelp/pitchbook 件)', 'https://www.microtechnology.net/about')],
    '美佐治亚 36 年学区 IT 集成屋(ERATE 谱)', '中型谱;1990 创',
    ('K-12 百校 ERATE=公段大户', '公立 K-12 守界段', 'Smith 族直达位', '一线链竞谱'),
    'Randy Smith 直达(opt-in 律;学区段守界)', 'Dear Mr. Smith,'))

R.append(rec('A-270', 'Data Connect',
    'Data Connect Enterprise, Inc.(DCE)(美国 Olney, Maryland;**1989-01 创 37 年;www.data-connect.com 主谱对位(档案锚)**;**Founder/President & CEO: Barry Patton(LI 自署 36 年;并购扩建「DCE 网络 inter-related 公司」战略谱)**;Connectivity/Network Access/VoIP/Triple Play 件链;**排噪:Data Connect Corporation(Centennial CO,展会软件;Tim Hobbs CEO)同名异体已分层**',
    [('Barry Patton', 'Founder/President & CEO(1989 创始;LI 自署 36 年)', 'linkedin.com/in/barry-patton(O)', O, 'https://www.linkedin.com/in/barry-patton-1990198/')],
    [ev('决策链与对接人', '「I am the Founder and President of Data Connect Enterprise… President & CEO DCE Jan 1989 - Present 36 years;www.data-connect.com / www.dataconnectus.com」(linkedin.com/in/barry-patton 自署)', 'https://www.linkedin.com/in/barry-patton-1990198/'),
     ev('联系方式与基础画像', 'DCE, Olney, Maryland;build Data Connect into a network of inter-related companies through mergers & acquisitions;Connectivity/Network Access/VoIP/Triple Play solutions(LI 自署);**同名排噪: Data Connect Corporation CO/ Data Connect Group UK 各已分层**', 'https://www.linkedin.com/in/barry-patton-1990198/')],
    '美马里兰 37 年连接件链并购屋', '中型谱;1989 创',
    ('Patton 36 年亲历=直达', '并购谱', 'Patton 直达位', '一线链竞谱'),
    'Barry Patton 直达(opt-in 律)', 'Dear Mr. Patton,'))

R.append(rec('A-276', 'Neobits',
    'Neobits, Inc.(美国 Santa Clara, CA,3350 Scott Blvd Ste 4601, 95054;**2002-07-26 创 24 年;9 人;$6M;BBB 24 年档(2003 档起);旧名 Avami Systems Inc.=更名谱**;**CEO Arvind Goel(Wharton MBA 1999;ex-McKinsey/Infospace;BBB 件+LI 需求帖=O)+Co-Founder Knut Magnus Ugland Jacobsen(LI 双创谱)+Helen Nguyen 售前+Ryan Ventura 运营**;B2B 技术/AV/无线基建/MRO 混谱',
    [('Arvind Goel', 'CEO(BBB 件 Principal+LI 自帖需求件=O)', 'bbb.org 件', O, 'https://www.bbb.org/us/ca/santa-clara/profile/online-retailer/neobits-1216-218227'),
     ('Knut Magnus Ugland Jacobsen', 'Co-Founder(Kredd/Neobits 双创;LI 谱)', 'linkedin.com/company/neobits', G, 'https://www.linkedin.com/company/neobits'),
     ('Helen Nguyen', 'Presales Customer Service(售前口)', 'linkedin.com/company/neobits', G, 'https://www.linkedin.com/company/neobits'),
     ('Ryan Ventura', 'Operations and People Management(运营)', 'linkedin.com/company/neobits', G, 'https://www.linkedin.com/company/neobits')],
    [ev('决策链与对接人', 'Principal Contacts: Mr. Arvind Goel, CEO(BBB 件);LI 谱: Arvind Goel CEO + Knut Magnus Ugland Jacobsen Co-Founder + Helen Nguyen Presales + Ryan Ventura Operations(BBB/LI 双源)', 'https://www.bbb.org/us/ca/santa-clara/profile/online-retailer/neobits-1216-218227'),
     ev('联系方式与基础画像', 'established 2002;Santa Clara CA;+1 408-530-0063;$6M;9 employees;B2B supplier: technology products/AV systems/Telecom/IT & Data Center/Wireless Infrastructure;alternate name Avami Systems Inc.(BBB/rocketreach/LI 件)', 'https://rocketreach.co/neobits-profile_b5c44599f42e0dfa'),
     ev('近期动态与线索', '2026 LI CEO 自帖: urgent need of 50+ Kramer VM-4UHD HDMI DAs「Please contact me directly」(LI 件=CEO 亲采件链谱)', 'https://www.linkedin.com/company/neobits')],
    '美硅谷 24 年 B2B 技术供应铺', '9 人;$6M',
    ('CEO 亲采件链谱(需求自帖)', '小实体谱', 'Goel 直达位', '一线链竞谱'),
    'Arvind Goel 直达(opt-in 律)', 'Dear Mr. Goel,'))

R.append(rec('A-277', 'Modelec Data-Industrie',
    'MODELEC Data-Industrie B.V.(荷兰 Ede(Gelderland),Galvanistraat;**1977 创 49 年;21-50 人;「Your OT Network. Our Expertise」=OT 网络+网安专营(电网/水务/监狱/智能交通=KRITIS 守界加厚)**;**品牌谱 Moxa/Westermo/TXOne/Robustel;SPIE 站台自动化长期伙伴件**;**Contactinfo: Stefan Barten stefan@modelec.nl(SecurityDelta 伙伴页=O)+Bart Jan Witteveen bartjan@modelec.nl(Energy Storage NL+SPIE 案例件)+Sergio Alonso Owner(prospeo 谱)**',
    [('Stefan Barten', 'Contactinfo(伙伴页具名 stefan@modelec.nl +31 318-626262)', 'securitydelta.nl 伙伴页(O)', O, 'https://securitydelta.nl/partners/overview-partners/modelec'),
     ('Bart Jan Witteveen', '联络/案例件具名(bartjan@modelec.nl;SPIE 案例照件)', 'energystoragenl.nl+modelec.nl 双源', O, 'https://www.energystoragenl.nl/en/lid/modelec-data-industrie-bv/'),
     ('Sergio Alonso', 'Owner(业主谱)', 'prospeo.io 谱面条', G, 'https://prospeo.io/c/modelec')],
    [ev('决策链与对接人', 'Contactinfo: Stefan Barten stefan@modelec.nl 0318-626262(SecurityDelta 伙伴页);Contact: Bart Jan Witteveen bartjan@modelec.nl(Energy Storage NL 会员页);案例件照: Bart Jan Witteveen(MODELEC)+SPIE 项目位;Owner: Sergio Alonso(prospeo 谱)', 'https://securitydelta.nl/partners/overview-partners/modelec'),
     ev('联系方式与基础画像', 'Ede, Gelderland;founded 1977;21-50 employees;+31 318 636262;**OT network & cybersecurity specialist for energy/utilities/water/penitentiary/traffic**;Partners: Moxa, Westermo, TXOne, Robustel(securitydelta/prospeo/psychiatrie 件)', 'https://securitydelta.nl/partners/overview-partners/modelec'),
     ev('近期动态与线索', '2025: SPIE×MODELEC 「Samen Sterk」站台自动化长期件(案例页);Energy Storage NL 网络安全 workshop Ede 主办谱(modelec.nl/energystoragenl 件)', 'https://www.modelec.nl/case/samen-sterk-modelec-en-spie-bundelen-hun-krachten-voor-de-lange-termijn/')],
    '荷兰 Ede 49 年 OT 网络网安屋(KRITIS)', '21-50 人;1977 创',
    ('OT/电网专营=最高守界', 'KRITIS 守界段', 'Barten/Witteveen 联络直达位', 'Moxa/Westermo 链谱'),
    'Stefan Barten 直达(opt-in 律;KRITIS 守界)', 'Geachte heer Barten,'))

R.append(rec('A-278', 'Cayman Wireless',
    'Cayman Wireless, Inc.(美国 Harlingen, Texas,2910 Pine Valley Dr, 78550;**2004 创(VAR distributor)/2006 法人/2007 Owner 接管谱;5-10 人;$150k;Nevada 注册德南运营**;**family business: Gary Shield Owner/President(LI 自署「Owner of Cayman Wireless since 2007」MBA)+Tyler Shield VP/President(buzzfile 新谱 President 注=二代换代差旗;manta VP 留谱)**;**WISP 件链 VAR 专营(无线天线/电台/放大器/滤波)+出口谱**',
    [('Gary Shield', 'Owner/President(2007 起;LI 自署)', 'linkedin.com/in/gary-shield(O)', O, 'https://www.linkedin.com/in/gary-shield-890a933/'),
     ('Tyler Shield', 'VP→President buzzfile 新谱(二代换代差旗注)', 'buzzfile/manta 件', G, 'https://www.buzzfile.com/business/Cayman-Wireless,-Inc.-956-825-0710')],
    [ev('决策链与对接人', '「Masters in Business. Owner of Cayman Wireless since 2007.」(linkedin.com/in/gary-shield 自署);buzzfile 件: Tyler Shield President(差旗);manta 件: Gary Owner+Tyler VP=Shield 家族双代谱', 'https://www.linkedin.com/in/gary-shield-890a933/'),
     ev('联系方式与基础画像', '2910 Pine Valley Dr, Harlingen TX 78550;956-825-0711(Gary)/0712(Tyler);founded 2004(VAR WISP community, domestic+abroad);5-9 employees;**family business owned and operated**;export activities(buzzfile/manta/zoominfo 件)', 'https://www.buzzfile.com/business/Cayman-Wireless,-Inc.-956-825-0710')],
    '美德州 WISP 件链家族专营铺', '5-10 人;2004 创',
    ('WISP 谱=我方主场件链', '家族铺谱', 'Shield 家族直达位', '区域链竞谱'),
    'Gary Shield 直达(opt-in 律)', 'Dear Mr. Shield,'))

# ============ 人名司名同体培训谱档×25(档谱=本人谱位,official-self-published) ============
def person(code, name, city, web, p1, why, extra, sal):
    kb = '**%s(MikroTik 认证培训师/顾问 本人谱位,档谱官网自署,%s)' % (name, O) + '**'
    if not web.startswith('http') and __import__('re').match(r'^[\w.-]+\.[a-zA-Z]{2,}$', web):
        web = 'https://' + web  # 裸域补 scheme,审计取 http 源;无站户保持原样走仓内源
    src = web if web.startswith('http') else '仓内 profile/A/%s-*(R54/R66 档谱基础画像行)' % code
    return rec(code, name,
        '%s(%s;**【人名司名同体=CSV 公司名即本人谱位,official-self-published 级金谱】**;类型: 集成商/顾问(MikroTik 认证);培训交付谱;档站 %s;%s)' % (name, city, web, extra),
        [(name, 'MikroTik 认证培训师/顾问(档谱:CSV 公司名字段即本人)', '档谱+档站自署', O, src),
        ],
        [ev('联系方式与基础画像', '国家/城市: %s;网站: %s;类型: 集成商/顾问(MikroTik 认证)(档案基础画像行=事实)', src),
         ev('近期动态与线索', '档定首触角: %s' % p1, src),
         ev('目标行业与场景', '档定值得跟: %s' % why, src)],
        '培训交付谱(MTCSWE 谱链)', '单铺/工作室谱',
        ('MTCSWE/交换认证谱=对口窗', '单铺谱', '%s 本人直达位' % name, 'MikroTik 官方课链'),
        sal + '(opt-in 律)',
        sal)

R.append(person('A-235', 'László Kalapos', '匈牙利／Miskolc', 'https://mindenamimikrotik.hu',
    '课程对照单元教具角($180 锚点一致);训练通道判', '有明确交换/供电需求(交换认证 MTCSWE、PoE/监控/门禁),且有具体人直联',
    'mindenamimikrotik.hu=匈语 MikroTik 培训门户谱', 'Tisztelt Kalapos Úr!'))
R.append(person('A-236', 'Leo De Geer', '瑞典／Kristianstad', 'satelithuset.se',
    'MikroTik 元老顾问探询($180 锚点一致);DNS 双层核验', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'satelithuset.se=瑞典本地网件铺谱;**MikroTik 元老级顾问谱(档定)**', 'Dear Mr. De Geer,'))
R.append(person('A-237', 'Philippe ROBERT', '瑞士／Genève', 'https://www.engitech.ch',
    'PoE 密度升级替补窄针($180 锚点一致);生态店判', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'engitech.ch=日内瓦 IT 工程铺谱', 'Monsieur Robert,'))
R.append(person('A-239', 'Patrik Schaub', '德国／Freiburg', 'https://www.fmsweb.de',
    '转售商二轨窄口($180 锚点一致);**Stadtwerke 半公共守界**+Schaub 具名', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'fmsweb.de=弗莱堡 IT 谱;Stadtwerke 客谱守界注', 'Guten Tag Herr Schaub,'))
R.append(person('A-240', 'Khalil Chamseddine', '奥地利／Wien', 'https://aulaf.com',
    'MTCSWE 实验对照单元($180 锚点一致);训练通道判(Khalil 口)', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'aulaf.com=维培训门户谱', 'Guten Tag Herr Chamseddine,'))
R.append(person('A-241', 'Martin Polainer', '奥地利／Weiz', 'https://www.triotronik.com',
    '二轨价值槽正位($180 锚点一致);M. Polainer 具名直口', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'triotronik.com=施泰尔马克 IT 铺谱', 'Guten Tag Herr Polainer,'))
R.append(person('A-243', 'Tadeusz Ruchlewicz', '波兰／Rzeszów', 'https://csidet.edu.pl',
    'MTCSWE 对照单元($180 锚点一致);**CS Edu Idet 全 10 证讲师+EU 资助课(公立院校教授线)**;A-252 同主体双行注', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'csidet.edu.pl=热舒夫培训机构;公立院校谱(教授个人顾问线);**A-252 Kajetan Tadra 同主体双行注记**', 'Szanowny Panie Ruchlewicz,'))
R.append(person('A-244', 'Bartłomiej Rodek', '波兰／Gliwice', 'https://interprojekt.pl',
    '交期/价位缺口二轨替补窄口($180 锚点一致);守界前句+排他风险注', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'interprojekt.pl=Gliwice 工程铺谱', 'Szanowny Panie Rodek,'))
R.append(person('A-245', 'Jaromir Cihak', '捷克／Praha', 'https://www.sys-data.com',
    'POP 边缘/客户现场件窄针($180 锚点一致);obchod=商务口;**Sys-Data 捷克区域 ISP(60GHz/10G 自营网)**', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'sys-data.com=布拉格区域 ISP 谱(60GHz/10G 自营)', 'Vážený pane Cihak,'))
R.append(person('A-246', 'Fredrik Hellgren', '瑞典／Älvsjö', 'https://axbyte.se',
    '托管/共置接入层窄位($180 锚点一致)', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'axbyte.se=斯德哥尔摩南 IT 铺谱', 'Dear Mr. Hellgren,'))
R.append(person('A-247', 'Marco Boschini', '意大利／Lonato(BS)', 'https://corsimikrotik.it',
    'MTCSWE 对照单元($180 锚点一致);**corsimikrotik.it=意大利首个 MikroTik 在线培训门户(HC Tech)**', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    '意首个 MikroTik 在线培训门户谱', 'Gentile Sig. Boschini,'))
R.append(person('A-248', 'Victor Bolaños Guerra', '西班牙／Las Palmas de Gran Canaria', 'https://www.lo0.es',
    '交换课对照单元($180 锚点一致);**lo0 西班牙多厂商培训厂(MikroTik/Huawei/Ubiquiti/Grandstream 同墙);心态最开放**', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'lo0.es=加那利群岛多厂商培训厂谱(心态最开放)', 'Estimado Sr. Bolaños,'))
R.append(person('A-249', 'Flavio Gomes Figueira Camacho', '葡萄牙／Aveiro', '—（无公开站点）',
    '**无站无邮箱——建档供位待用户补(A-205/A-212 先例)**;$180 锚点一致', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Estimado Sr. Camacho,'))
R.append(person('A-250', 'Péter Major', '匈牙利／Budapest', 'https://macsoft.hu',
    '项目随单($180 锚点一致);**beszerzes@=匈语采购箱直达(工程/集成项目制)**', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'macsoft.hu=布达佩斯项目制集成铺谱;beszerzes 采购箱 KPI', 'Tisztelt Major Úr!'))
R.append(person('A-251', 'Dávid Csongrádi', '匈牙利／Budapest', '—（无公开站点）',
    '**无站无邮箱——建档供位待用户补(A-205/A-212 先例)**;$180 锚点一致', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Tisztelt Csongrádi Úr!'))
R.append(person('A-252', 'Kajetan Tadra', '波兰／Rzeszów', 'https://csidet.edu.pl',
    'MTCSWE 对照单元($180 锚点一致);**CS Edu Idet 机构箱行(同 A-243 主体);错峰注免同日双发**', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'csidet.edu.pl=热舒夫培训机构;**A-243 Tadeusz Ruchlewicz 同主体双行注记(错峰发)**', 'Szanowny Panie Tadra,'))
R.append(person('A-258', 'Daniel Świtalski', '波兰／Poznań', '—（无公开站点）',
    '**无站无邮箱——建档供位待用户补(A-205/A-212 先例)**;$180 锚点一致', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Szanowny Panie Świtalski,'))
R.append(person('A-259', 'Henk Veldkamp', '荷兰／Zwolle', 'https://www.mikrotrain.nl',
    'MTCSWE 对照单元($180 锚点一致);**mikrotrain.nl=荷兰 MikroTik 培训专营铺(交换专长,三星重点)**', '有明确交换/供电需求(交换认证 MTCSWE、交换专长),三星重点',
    'mikrotrain.nl=荷 MikroTik 培训专营谱', 'Geachte heer Veldkamp,'))
R.append(person('A-260', 'Maurice Van Der Grijspaarde', '荷兰／Haarlem', 'https://gpe-networks.com',
    '换代随单($180 锚点一致);存量共存话术;**gpe-networks 工程/集成制**', '有明确交换/供电需求(交换认证 MTCSWE、交换专长),三星重点',
    'gpe-networks.com=哈勒姆集成铺谱', 'Geachte heer Van der Grijspaarde,'))
R.append(person('A-261', 'Joost Van De Weijer', '荷兰／Bladel', 'https://iptechniek.nl',
    '顾问项目随件窄口($180 锚点一致);训练通道判', '有明确交换/供电需求(交换认证 MTCSWE、交换专长),三星重点',
    'iptechniek.nl=布拉班特 IP 技术铺谱', 'Geachte heer Van de Weijer,'))
R.append(person('A-271', 'Michiel Visser', '荷兰／Deventer', 'https://interstellar.nl',
    '私营段随单窄针($180 锚点一致);**Gemeente Katwijk 公共守界**', '【人工定级】A——自动规则已跳过;信息待人工补齐(档注)',
    'interstellar.nl=德文特 IT 铺谱;市政客谱守界注', 'Geachte heer Visser,'))
R.append(person('A-272', 'Alexandr Mensenin', '捷克／Ostrava', '—（无公开站点）',
    '**建档不出信(无站无邮箱,参照 A-205/A-212 先例);用户补邮箱→CONSULT-OEM 候选供位**', '【人工定级】A——自动规则已跳过;信息待人工补齐(档注)',
    '个体顾问无官网档;建档供位待用户补邮箱(CONSULT-OEM 候选)', 'Vážený pane Mensenin,'))
R.append(person('A-273', 'Kevin Myers', '美国／Flowood, MS', 'https://iparchitechs.com',
    'commodity hardware 降本哲学同频,对照库规格单元($180 锚点一致);**iparchitechs=美 IP 架构顾问名牌谱;顾问主权话术**', '【人工定级】A——自动规则已跳过;信息待人工补齐(档注)',
    'iparchitechs.com=密西西比 IP 架构顾问名牌谱(培训交付)', 'Dear Kevin,'))
R.append(person('A-274', 'Nathael Leblanc', '加拿大／Montréal', 'https://joustsec.com',
    '顾问+代管机架双窄针($180 锚点一致);**joustsec 网安顾问谱**', '【人工定级】A——自动规则已跳过;信息待人工补齐(档注)',
    'joustsec.com=蒙特利尔网安顾问铺谱', 'Bonjour Monsieur Leblanc,'))
R.append(person('A-275', 'Philippe Lachapelle', '加拿大／Montréal', 'https://canservers.com',
    '装机柜客户新类目窄针($180 锚点一致);**canservers 加拿大服务器/机架件铺谱**', '【人工定级】A——自动规则已跳过;信息待人工补齐(档注)',
    'canservers.com=蒙特利尔服务器件铺谱', 'Bonjour Monsieur Lachapelle,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第20波50户.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 20 波 50 户扩招批:A-229~A-278 顺延 50 户(公司档 25+人名司名同体培训谱档 25)',
               'scope': 'PL2/CZ2/NO1+守1/PT3(守1)/HU3/DE2/IE1/FR3/FI1/UK4/US5/NL6(公司9+人名5)/CH1/SE2/AT2/ES1/CA2/IT1 公司谱;人名档 25(MTCSWE 培训谱链);守档 3(The Junction/NetHighTech 具名/其余个体无站 4 户建档供位);KRITIS/学区/市政/半公共各守界注',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 20 波 50 户扩招批落盘:', len(R))
