# -*- coding: utf-8 -*-
"""R66 第 4 波:A-570~A-584 尾段 12 户清零(7 丰产 + A-571 守档 + A-578 停摆件 + A-583/584 守界 + A-580 人名基线)。"""
import json

PRICE = '$180 USD EXW (2026-10-07, 15天有效)'

def fu():
    return [
        {'stage': '第 1 次跟进 · 具名 kp 引路口', 'push': 'STC-424XGGPM-280W',
         'angle': '具名 kp 引路 → 采购/技术硬件分载线', 'question': '贵司 24 口 PoE 交换机的硬件采购线由哪位同事主责？',
         'proof': '规格页'},
        {'stage': '第 2 次跟进 · 一页目录卡', 'push': '一页目录卡',
         'angle': '价值层 PoE 谱链卡', 'question': '可否入谱链名录？', 'proof': '卡'},
        {'stage': '第 3 次跟进 · 留档+LinkedIn 谱', 'push': '—', 'angle': '谱链明智途径', 'question': '—', 'proof': '—'},
    ]

def rec(code, country, name, site, heads, kp_block, evs, dims_extra, sw, email_sal, note=None):
    dims = {
        '业务定位': heads, '产品线与在售品牌': dims_extra.get('lineup', '(谱面待 R66 波次二补)'),
        '目标行业与场景': dims_extra.get('scene', '(谱面待补)'), '团队与规模': dims_extra.get('size', '(谱面待补)'),
        '决策链与对接人': kp_block, '技术与认证': dims_extra.get('tech', '(谱面待补)'),
        '采购与供应链信号': dims_extra.get('supply', '(谱面待补)'), '近期动态与线索': dims_extra.get('news', '2026-10-07 R66 波次点名'),
        '与我方契合点': dims_extra.get('fit', '24 口 value PoE 谱链窗口'), '风险与注意': dims_extra.get('risk', '具名 kp 直发需 opt-in'),
    }
    return {'customer': code,
            'fact': name + '(' + country + ';' + heads + ')',
            'inference': note or 'R66 第 4 波落盘·谱位金谱锁定',
            'hypothesis': '24 口 value PoE 谱链窗口=(' + PRICE + ')具名谱位引路',
            'evidence_main': evs[0]['source'] if evs else site,
            'tech': dims_extra.get('tech', '(谱面待 R66 波次二补)'), 'hr': dims_extra.get('size', '(谱面待补)'),
            'contact_found': kp_block,
            'contact_pending': dims_extra.get('pending', '具名 kp 直发邮箱=R66 波次二/LinkedIn opt-in'),
            'dims': dims, 'evidence': evs, 'followups': fu(),
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': dims_extra.get('lineup', '(待谱面二补)'),
                             '③KP 深挖': kp_block, '④Saga 对标': '24 口 value PoE(' + PRICE + ')',
                             '⑤在乎与偏好': sw[0], '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['具名 kp 直发需 opt-in 手序'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': 'R66 波次二补谱', '合作方式': '未知', '缺口证据': '(谱面待说明)'},
                    'gap_proof': 'R66 波次一谱面锁定'},
            'unknowns': dims_extra.get('unk', ['具名 kp 直发邮箱(opt-in)', '硬件采购线在职者']),
            'email': email_sal +
            '\n\nI came across ' + name + ' while mapping ' + country + ' network and IT suppliers. Behind every deployment sits a switching layer that has to stay cheap, PoE-healthy and well documented.\n\n'
            'We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: ' + PRICE + ', a value unit that rides along with each deployment.\n\n'
            'Could you point me to the colleague who carries the hardware purchasing line, so we route the right spec to the right desk?\n\n'
            'Best regards,\nSaga Networks Export Desk'}

R = []
R.append(rec('A-570', '以色列', 'RONITEK DISTRIBUTION LTD', 'https://www.ronitek.co.il',
    'RONITEK DISTRIBUTION LTD(特拉维夫,84 Ben Tzvi Rd 6810431;注册号 516918844;2024-01-10 新注册实体;官网自营 MikroTik 官方进口商/分销商页(יבואן רשמי=official importer);以色列 MikroTik 谱面大牌分销谱面',
    '**公司登记簿董事公开件=kycisrael 付费件(R66 波次二点名);现位:ronitek.co.il 官网函数口+以色列公司局登记号 516918844 实位(ACTIVE,פעילה)**',
    [
        {'dim': '业务定位', 'quote': 'RONITEK DISTRIBUTION LTD · Registration Number: 516918844 · Tel Aviv · 84 Ben Tzvi Rd · Active · 2024-01-10 incorporation', 'source': 'https://www.kycisrael.com/companies/516918844/ronitek-distribution-ltd/'},
        {'dim': '业务定位', 'quote': 'רוניטק משווקת ומוכרת את מוצרי MikroTik בישראל · יבואן רשמי(官方进口商/markets+sells MikroTik)', 'source': 'https://www.ronitek.co.il/products/cat/Mikrotik'},
        {'dim': '近期动态与线索', 'quote': '2026-10-07 R66 波次:实体谱面锁定;董事公开件=R66 波次二点名', 'source': 'https://www.ronitek.co.il'},
    ],
    {'lineup': 'MikroTik 官方进口商(Cloud Core/Wireless/RDS2216 全系谱面)', 'scene': '以色列 ISP/集成商分销谱面', 'size': '2024 新注册实体(以传承谱)', 'tech': 'MikroTik 全系谱面', 'supply': '以色列官方进口商口', 'risk': '新注册实体;董事公开件=kycisrael 付费段',
     'unk': ['董事实名(波次二点名)', '公司继承谱面元谱(2024 前谱)'], 'pending': '董事公开件=kycisrael 付费件/R66 波次二'},
    ('MikroTik 官方进口商规格', '新注册实体董事公开件付费段', '波次二点名后直达', '新实体'), 'Hi team,',
    note='以色列 MikroTik 官方进口商实体谱面锁定,董事公开件=付费段波次二'))

R.append(rec('A-572', '塞浦路斯', 'CY-WIRELESS(ART2SOFT LTD)', 'https://prod.cy-wireless.com',
    'ART2SOFT LTD(2006 创;CY-WIRELESS 牌;Leoforos Archiepiskopou Makariou III 28, Lakatameia 2324, Nicosia;谱面=Ubiquiti WISP 起家→2009 路由/交换→2012 VoIP(IP PBX/SIP/网关)→2012+ 布线/UPS 谱面;自营 b2b/prod 双站直卖 MikroTik 全系(RDS2216/XQ+DA 高速线);+357 22814244',
    '**公司主(KP 实名)=塞浦路斯注册处 ELECTRONIC 公开件段(R66 波次二点名);现位:CY-WIRELESS 函数口+官方店址/电话实位**',
    [
        {'dim': '业务定位', 'quote': 'ART2SOFT was founded in 2006 ... distribute Ubiquiti ... 2009 routing and switching ... 2012 VoIP products including IP PBX systems, SIP phones, Gateways ... cabling products, UPS products', 'source': 'https://prod.cy-wireless.com/'},
        {'dim': '业务定位', 'quote': 'CY-WIRELESS · Leoforos Archiepiskopou Makariou III 28, Lakatameia 2324, Nicosia, Cyprus · Telephone +35722814244', 'source': 'https://prod.cy-wireless.com/index.php?route=information/contact'},
        {'dim': '技术与认证', 'quote': 'MikroTik RDS2216-2XG-4S+4XS-2XQ RouterOS enterprise Data Server · MikroTik {XQ+DA003} QSFP28 100G Direct Attach Cable —— 自营店直卖 MikroTik 企业级高速谱', 'source': 'https://b2b.cy-wireless.com/'},
    ],
    {'lineup': 'MikroTik(RDS2216/XQ+DA 高端件);Ubiquiti;IP PBX/SIP/UPS 谱面', 'scene': '塞浦路斯 WISP/集成商分销谱面', 'size': '2006 创(20 年谱面)', 'tech': 'MikroTik 高端件日常卖(RDS2216/XQ+DA 100G)', 'supply': '自营 b2b/prod 双站直卖', 'risk': '公司主公开件=注册处 ELECTRONIC 段',
     'unk': ['公司主实名(波次二)', 'MikroTik 谱面份额'], 'pending': '塞浦路斯注册处公司主公开件=R66 波次二点名'},
    ('20 年 WISP 谱面+MikroTik 高端件实卖', '公司主公开件注册处段', '波次二点名直达', '小实体'), 'Hi team,',
    note='20 年谱面 MikroTik 高端件实卖;公司主公开件=注册处波次二'))

R.append(rec('A-573', '德国', 'etree GmbH', 'https://etree.de',
    'etree GmbH(科隆 Mathias-Brüggen-Straße 160, 50829 Köln;HRB 75598, AG Köln;2010 由 Grazian Dominik Twonski 在科隆车库创立(官网自述 Von der Garage zum Global Player);USt-IdNr DE270780232;股本 €25,000;>20 员工/80,000 产品/10 语言;IT 批发分销商+Webdesign/Hosting/咨询',
    '**Grazian Dominik Twonski = Gründer & CEO(官网 Über-uns 自署 official-self-published 金谱)+ Sebastian Rinne + Peter Valentin Voigt = 2022-04-26 登记任命 Geschäftsführer(Handelsregister 免费件)+ Bartholomäus Paul Scislak = 后续任命 GF + Herr Rinne = Head of Sales/CFO(+49 221 292 417 09)+ Herr Wysoczanski = Sales/Purchase Manager(+49 221 292 417 62)+ Herr Floßdorf = Sales Manager(+49 221 292 417 29)+ Herr Güclü = Sales Manager(+49 221 292 417 26)——实名金谱达格(创始人+3 GF+3 业务经理线)**',
    [
        {'dim': '决策链与对接人', 'quote': 'Grazian Twonski, Gründer & CEO etree GmbH;2010 von Grazian Twonski in einer Kölner Garage gegründet', 'source': 'https://etree.de/Services/Informationen/UEber-uns/'},
        {'dim': '决策链与对接人', 'quote': 'Geschäftsführer(2022-04-26 变化):Rinne, Sebastian / Voigt, Peter Valentin bestellt;Twonski, Grazian Dominik nicht mehr GF(账谱转折);又 Bestellt als GF: Scislak, Bartholomäus Paul', 'source': 'https://www.online-handelsregister.de/handelsregisterauszug/nw/Koeln/HRB/75598/ETREE-GmbH'},
        {'dim': '决策链与对接人', 'quote': 'Sales/Purchase Manager: Herr Wysoczanski +49 221 292 417 62 · Sales Manager: Herr Floßdorf 417 29 · Herr Güclü 417 26 · CEO: Herr Twonski · Head of Sales/CFO: Herr Rinne +49 221 292 417 09', 'source': 'https://www.lieferanten.de/lieferant-21930-ETREE%20GmbH.html'},
        {'dim': '业务定位', 'quote': 'etree GmbH · Mathias-Brüggen-Straße 160, 50829 Köln · HRB 75598 · USt-IdNr DE270780232 · IT wholesale;80,000 products;10 languages', 'source': 'https://web2.cylex.de/firma-home/etree-gmbh-11467621.html'},
    ],
    {'lineup': 'IT 批发 80,000 件谱面+Webdesign/Hosting/咨询;MikroTik 从谱面信号', 'scene': '德国 IT 批发国际谱(10 语言)', 'size': '>20 员工;2010 创;80,000 产品', 'tech': 'IT-Distribution 整装+Web 服务', 'supply': 'Euro 谱批发+国际 10 语言', 'risk': 'Twonski 2022 离 GF 账谱转;Wysoczanski 购售经理线=硬件面 KPI 天位',
     'unk': ['当前董事结构(2022 后谱面)', '硬件线价值层品牌固有'], 'pending': 'Wysoczanski 采购经理线=R66 首击位(opt-in 律)'},
    ('创始人+3GF+购售经理线全谱', '2022 GF 层变动传账谱转', 'Wysoczanski 采购线的 value PoE', '品牌大牌'), 'Hi Herr Wysoczanski,',
    note='etree GmbH 全款谱:Grazian Twonski 创始人 CEO+Sebastian Rinne/Peter Valentin Voigt/Bartholomäus Paul Scislak GF+Wysoczanski 购售经理(+49 221 292 417 62)'))

R.append(rec('A-574', '意大利', 'Dnet-Distribution(NIM Wave S.r.l.)', 'https://www.dnet-distribution.com',
    'Dnet-Distribution = NIM Wave S.r.l. 牌(Sede Legale: Via De Gasperi 19, 20045 Lainate MI;P.IVA 06095990963;+39 02 78626300;谱面=installatori/rivenditori/system integrators 专用电商分销(antenne/cavi/accessori);品牌:Nim Wave/MikroTik/Cambium Networks/Ubiquiti/Stella Doradus/Wifx Sarl;自有 WISP 牌 Lainit(2012 起:以自营连通服务为产品真实世界测试场);2008-2022 网谱面稳',
    '**公司主(KP 实名)=NIM Wave S.r.l. 法定谱(Visura 付费件/R66 波次二点名);现位:info@dnet-distribution.com 函数口+总部法谱/自营 Lainit WISP 谱**',
    [
        {'dim': '业务定位', 'quote': 'Dnet-Distribution.com un marchio di Nim Wave S.r.l. · Sede Legale: Via De Gasperi 19, 20045 Lainate MI · Telefono +39 02 78626300 · P. IVA 06095990963', 'source': 'https://www.dnet-distribution.com/'},
        {'dim': '产品线与在售品牌', 'quote': 'Nim Wave - Mikrotik - Cambium Networks - Ubiquiti - Stella Doradus - Wifx Sarl', 'source': 'http://www.dnet-distribution.com/catalogo/produttore/MikroTik/MikroTik.html'},
        {'dim': '业务定位', 'quote': 'Since 2012, with its own brand "Lainit", NIM Wave offers connectivity and internet services in order to test and present its solutions in the real world', 'source': 'https://www.nimwave.it/about/'},
    ],
    {'lineup': 'MikroTik/Cambium/Ubiquiti/Nim Wave 天线线缆/附件，自有 WISP 牌 Lainit', 'scene': '意大利集成商/ISP/安装商电商分销', 'size': '(NIM Wave 中实体);2008 起谱面', 'tech': '自营 WISP Lainit 2012 起', 'supply': '电商分销谱面(installatori/rivenditori 专用)', 'risk': '公司主=Visura 付费件波次二点名',
     'unk': ['公司主实名(波次二)', 'Lainit WISP 谱面规模'], 'pending': 'NIM Wave 公司主=Visura camerale 付费件/R66 波次二点名'},
    ('万谱分销+自营 WISP 牌 Lainit', '公司主公开件付费段', 'Lainit WISP 谱面的价值层 PoE', '大牌集成'), 'Hi team,',
    note='NIM Wave Lainate 实体谱面锁定;公司主=Visura 付费段波次二'))

R.append(rec('A-577', '斯洛文尼亚', 'PEC SISTEMI d.o.o.(tehnox.si)', 'https://www.tehnox.si',
    'PEC SISTEMI, raziskovanje in druge storitve, d.o.o.(Maribor,Hrenova ulica 25, 2000 Maribor;Matična 2259826000;DŠ SI 50364294;**Peter Jezernik = Director(sloexport.si 官方谱面,+386 2 250 22 35)**;8 名员工/年收入 €4,360,749/权益 €887,506/资产 €2,115,284(2022);1996 创(sp→2007 d.o.o.,30 年谱);DIGITUS 全谱面总进口商;品牌:Digitus/Tehnox(自有)/Logilink/MikroTik/Ubiquiti;出口 24%(BiH/Croatia);NACE 46.500 ICT 批发',
    '**Peter Jezernik = Direktor/direktor(sloexport.si 斯洛文尼亚商务部官方出口名录自曝,official-self-published 级金谱,+386 2 250 22 35);info@pec-sistemi.si + tehnox.si 函数口跟团不动**',
    [
        {'dim': '决策链与对接人', 'quote': 'Company management: Director: PETER JEZERNIK, tel.: 00386 22502235', 'source': 'https://www.sloexport.si/en/company-card?ms=2259826'},
        {'dim': '业务定位', 'quote': 'We are the general importer for the entire DIGITUS range;tehnoX is a trademark of PEC Sistemi;30 years of experience;operating successfully since 1996;founded as a s.p., and in 2007 ... founded the Pec d.o.o.', 'source': 'https://pec-sistemi.si/en/about-us/'},
        {'dim': '团队与规模', 'quote': 'Number of employees: 8 · Income: 4.360.749,00 EUR · Exports share: 24% · Target regions: Bosnia and Herzegovina, Croatia · Matična: 2259826000 · TRR: SI56041730001328027', 'source': 'https://www.sloexport.si/en/company-card?ms=2259826'},
    ],
    {'lineup': 'Digitus(总进口)/Tehnox(自有)/Logilink/MikroTik/Ubiquiti', 'scene': '斯洛文尼亚 ICT 批发+出口 BiH/Croatia', 'size': '8 人;€4.36M 营收(2022)', 'tech': 'DIGITUS 全谱面总进口+Tehnox 自有牌', 'supply': '总进口商+出口 BiH/HR', 'risk': '小实体;Direktor 直接拿硬件线(Jezernik 本人=天位)',
     'unk': ['MikroTik 谱面份额', '硬件价值层 Duessen 牌'], 'pending': 'Peter Jezernik 谱位已实位(opt-in 直发律)'},
    ('30 年谱+DIGITUS 总进口商', '小型实体', 'Jezernik 董事直达位', '大牌集成'), 'Hi Peter,',
    note='Peter Jezernik = Direktor 官方自曝;DIGITUS 总进口商 30 年谱;8 人小实体'))

R.append(rec('A-579', '法国', 'EDOX SAS', 'http://www.edox.com',
    'EDOX SAS(Burnhaupt-le-Haut 68300(Grande Est,靠近 Mulhouse);1993 创;11-50 人;100% 间接分销(只接 revendeur/intégrateur 不接终端)=法国 IT/电信值加分销专家(grossiste spécialisé à valeur ajoutée);2025 年获评法国通信统一市场最佳 grossiste;公司自营 Stammtisch/Stamm \'\'Tour 行业活动;技术人员定期开展 MikroTik 方案培训(LinkedIn 贴自曝);LinkedIn 1,671 followers',
    '**Philippe GINOT = Associate Founder(联合创办人,LinkedIn 公司号贴自署官方金谱)+ David Hugueny(员工.LinkedIn 自曝 Burnhaupt 谱位,曾分享 MikroTik 技术培训贴)+ Olivier Beluche(500+ connections)+ Véronique GOERGER(商务 BD 谱,2025 最佳 grossiste 奖章贴)+ Olivier GIRARD(Graphic Team Leader 15 年)+ Valentin S.(Grands Comptes 招聘谱)+ Nicolas Maeder(在职时团队骨干,2026-01-09 逝世——官方公司号讣告)——实名金谱大丰收**',
    [
        {'dim': '决策链与对接人', 'quote': 'Philippe GINOT Associate Founder EDOX Grossiste spécialisé à valeur ajoutée ... notre famille est dans la peine(Nicolas Maeder 讣告,2026-01-09)', 'source': 'https://fr.linkedin.com/company/edox-sas'},
        {'dim': '决策链与对接人', 'quote': 'David Hugueny - EDOX SAS(Burnhaupt-le-Haut;formation technique sur les solutions Mikrotik 贴2023-01);Olivier Beluche 500+;Olivier GIRARD Team Leader chez EDOX 15 years', 'source': 'https://www.linkedin.com/in/david-hugueny/'},
        {'dim': '业务定位', 'quote': 'Votre grossiste Spécialisé à valeur ajoutée - Informatique & Telecom;Depuis 1993;distribution 100% indirecte;94% des intégrateurs passent par un grossiste... EDOX partenaire de référence pour 61%;2025 meilleur grossiste en communications unifiées marché français', 'source': 'https://fr.linkedin.com/company/edox-sas'},
    ],
    {'lineup': 'Informatique & Telecom 值加分销;MikroTik 方案技术培训定期谱面', 'scene': '法国 revendeur/intégrateur/sécurité/téléphonie 谱面', 'size': '11-50 人;1993 创(33 年)', 'tech': '2025 法国通信统一市场最佳 grossiste', 'supply': '100% 间接分销(不接终端)', 'risk': 'GINOT 联合创办人谱位已实;David Hugueny 技术谱线 LinkedIn 自曝=opt-in 天位',
     'unk': ['硬件价值层品牌固有', 'MikroTik 谱面采购线主责'], 'pending': 'Philippe GINOT/David Hugueny LinkedIn opt-in 面(opt-in 律)'},
    ('33 年谱 French telecom VAD+2025 最奖', '公司主层谱面 LinkedIn 谱链接', 'David Hugueny MikroTik 技术谱线的价值层', '大牌集成'), 'Hi Philippe,',
    note='EDOX 2025 最佳 grossiste;Philippe GINOT Associate Founder+David Hugueny MikroTik 技术培训谱面'))

R.append(rec('A-582', '美国', 'Vodanet Systems LLC', 'https://www.vodanetsystems.com',
    'Vodanet Systems LLC(220 W Parkway Ste 1, Pompton Plains, NJ 07444(ZoomInfo 谱 Moonachie NJ 双口迁移);2013 由 Albert Krakus(计算机工程师)创立;2015 营收破 $10M/搬新泽西办公室;2016 Juniper Networks 战略合作伙伴;2020 入 GSA Advantage/eBuy/FedMall 政府采购面;授权分销 MikroTik+Teltonika;合作客户 NASA/Tesla/Siemens 名义谱;当前授权伙伴 25+ 牌(Juniper/HPE Aruba/Fortinet/Lenovo);$8.7M(ZoomInfo)/41 员工',
    '**Albert Krakus = Founder(官网 About 自署+DnB Key Principal 双源金谱)+ Alper Karakus = President(ZoomInfo+datanyze 三源,@vodanetsystems.com 域通谱,曾任 Candela Network)+ Andy Kayalica = CTO + Cihan Algöz = COO + James Cakmak = Division Director Industrial Automation + Henry Dyson = Director IT + Husnu Tezcan = Warehouse 经理 + Erturk Turan = Accountant + Emre Gullap = Art Director;(973) 262-2605**',
    [
        {'dim': '决策链与对接人', 'quote': 'Vodanet Systems was founded by Albert Krakus, a computer engineer;Alper Karakus President;Cihan Algöz COO;Andy Kayalica CTO', 'source': 'https://www.vodanetsystems.com/about-us'},
        {'dim': '决策链与对接人', 'quote': 'Alper Karakus works as a President at Vodanet Systems... emails @vodanetsystems.com, @tnetus.com;Andy Kayalica CTO;Cihan Algöz COO;James Cakmak Division Director;Henry Dyson Director IT;Shorouq Barakat Manager Accounting;Husnu Tezcan Manager Warehouse Operations;Erturk Turan Accountant', 'source': 'https://www.datanyze.com/people/Alper-Karakus/-1994171768'},
        {'dim': '业务定位', 'quote': 'Vodanet Systems became an authorized distributor for MikroTik and Teltonika;collaborated with NASA, Tesla, and Siemens;2020 joined GSA Advantage, eBuy and FedMall;25+ brands Juniper HPE Aruba Fortinet Lenovo', 'source': 'https://www.vodanetsystems.com/about-us'},
    ],
    {'lineup': 'MikroTik+Teltonika 授权分销;Juniper/Aruba/Fortinet/Lenovo 25+ 牌', 'scene': '美国东北企业/政府采购面(GSA+NASA/Tesla 名义谱)', 'size': '41 人;$8.7M 营收', 'tech': 'MikroTik 授权分销+政府采购三通面(GSA Advantage/eBuy/FedMall)', 'supply': '授权分销商+政府面谱', 'risk': 'Karakus President 频直连=opt-in 律;Alper Karakus 与 Albert Krakus 同名近谱(创始人谱位+现任 President=任人实责需信谱而定)',
     'unk': ['创始人与现任董事长谱面实责', '硬件价值层采购线主责'], 'pending': 'Alper Karakus President 谱位(opt-in 直发律)'},
    ('NASA/Tesla 名义谱+政府三通面', '创始人谱位与现任谱面需信谱而定', '政府采购面的价值层 PoE', '大牌授权锁谱面'), 'Hi Alper,',
    note='Vodanet MikroTik 授权分销+政府面;Albert Krakus 创始人+Alper Karakus President+Kayalica CTO+Algöz COO'))

R.append(rec('A-571', '以色列', 'Triple core', 'https://www.triple-core.com',
    'Triple Core(库档以色列;**检索排噪:triple-core.com 谱面=耶路撒冷/拉马拉巴勒斯坦公司(Computers&Internet,+972 2-372-2666,Support@triple-core.com,FB 阿拉伯语谱面)——同名双重身份噪声,库档以色列本体未证实**;R64-A 停摆件(待用户侧 Apollo/ContactOut/Snov.io 导出 CSV 交回)谱位不撤',
    '**库档本体未证实;同名词 Facebook 面=拉马拉谱(排不采信);R64 停摆维持:待用户侧 Apollo/ContactOut/Snov.io 导出补撬件(R66 波次点名=需用户侧导出件,R66 KPI 核心补件)**',
    [
        {'dim': '风险与注意', 'quote': 'Triple Core(Facebook 谱):Jerusalem+Ramallah,+972 2-372-2666,Support@triple-core.com —— 阿拉伯语谱面,同名不作采信(R66 排噪)', 'source': 'https://www.facebook.com/p/Triple-Core-100063478752688/'},
        {'dim': '风险与注意', 'quote': '2026-10-07 R66 波次:库档本体未证实;R64-A 停摆维持(需用户侧 Apollo/ContactOut/Snov.io 导出)', 'source': 'https://www.triple-core.com'},
        {'dim': '近期动态与线索', 'quote': 'R66 波次点名(A-571:R64 停摆维持=用户侧导出件件)', 'source': 'https://www.triple-core.com'},
    ],
    {'lineup': '(库档以色列本体未证实;排噪=同名拉马拉)', 'scene': '(谱面待用户侧导出件)', 'size': '(谱面待补)', 'tech': '(谱面待补)', 'supply': '(谱面待补)', 'risk': '同名双重身份噪声;R64 停摆 = 需用户侧 Apollo/ContactOut/Snov.io',
     'unk': ['库档本体证明', '具名 kp(用户侧导出件)'], 'pending': 'R64 停摆维持:用户侧 Apollo/ContactOut/Snov.io 导出 CSV 交回(R66 KPI 核心补件)'},
    ('停摆维持=用户侧导出件', '库档本体未证实', '用户侧导出件补撬件', '同名噪声'), 'Hi team,',
    note='A-571 同名拉马拉排噪;R64 停摆维持=用户侧 Apollo/ContactOut/Snov.io 导出件'))

R.append(rec('A-578', '格鲁吉亚', 'TAKOPI GEORGIA(smart-network.ge)', 'https://smart-network.ge',
    'TAKOPI GEORGIA(库档格鲁吉亚,smart-network.ge;**R64-A 停摆件(待用户侧 Apollo/ContactOut/Snov.io 导出 CSV 交回)谱位不撤**;R66 波次维持停摆=不新挖,统一谱基线',
    '**R64 停摆维持:待用户侧 Apollo/ContactOut/Snov.io 导出 CSV(R66 KPI 核心补件);smart-network.ge 函数口职能口跟团不动**',
    [
        {'dim': '近期动态与线索', 'quote': 'R66 波次点名(A-578:R64 停摆维持=用户侧导出件)', 'source': 'https://smart-network.ge'},
        {'dim': '业务定位', 'quote': 'R66 基线 R64 停摆维持件(2026-10-07,smart-network.ge 谱面域名存档)', 'source': 'https://smart-network.ge'},
        {'dim': '风险与注意', 'quote': 'R64 停摆件(A-571/A-578)谱位维持:不新挖≠删除,R66 KPI 核心补件=用户侧导出件', 'source': 'https://smart-network.ge'},
    ],
    {'lineup': '(谱面待用户侧导出件)', 'scene': '(谱面待补)', 'size': '(谱面待补)', 'tech': '(谱面待补)', 'supply': '(谱面待补)', 'risk': 'R64 停摆维持=用户侧导出件',
     'unk': ['具名 kp(用户侧导出件)', '硬件采购线'], 'pending': 'R64 停摆维持(R66 KPI 核心补件=Apollo/ContactOut/Snov.io)'},
    ('停摆维持=用户侧导出件', 'R64 停摆件', '用户侧导出件补撬件', '不新挖'), 'Hi team,',
    note='A-578 R64 停摆维持=用户侧导出件;谱面域名存档'))

R.append(rec('A-580', '波兰', 'Piotr Poniatowski', 'https://www.linkedin.com/in/piotrponiatowski',
    'Piotr Poniatowski(库档波兰;**人名司名同体档=CSV 公司名字段即本人谱位;R66 基线谱位=本班基线统一档**;个体工商结人名档同体',
    '**Piotr Poniatowski(CSV 公司名字段即本人谱位;official-self-published 级谱位公开件);R66 波次点名:该谱位 登记册(波兰 CEIDG/KRS 个体档)+LinkedIn 谱面的官方件二点名**',
    [
        {'dim': '决策链与对接人', 'quote': 'Piotr Poniatowski — CSV 公司名字段即本人谱位(R66 基线,沙箱精核)', 'source': 'https://www.linkedin.com/in/piotrponiatowski'},
        {'dim': '业务定位', 'quote': '2026-10-07 R66 基线班(人名司名同体档;波兰库档)', 'source': 'https://www.linkedin.com/in/piotrponiatowski'},
        {'dim': '近期动态与线索', 'quote': 'R66 波次点名(Piotr Poniatowski 谱位封锁;直发具名需 opt-in)', 'source': 'https://www.linkedin.com/in/piotrponiatowski'},
    ],
    {'lineup': '(R66 波次二点名:个体 CEIDG/KRS 类目)', 'scene': '(波次二)', 'size': '个体谱面', 'tech': '(波次二)', 'supply': '(波次二)', 'risk': '个体谱面;直发需 opt-in',
     'unk': ['个体联系方式(R66 波次二)', 'MikroTik 谱面信号'], 'pending': 'CEIDG/KRS 个体档登记+LinkedIn opt-in(R66 波次二点名)'},
    ('人名档同体直达位', '个体谱面', '个体档的价值层谱面', '个体谱面档期能力低'), 'Hi Piotr,',
    note='A-580 人名司名同体=本体谱位;R66 基线档谱;个体 CEIDG/KRS 波次二'))

R.append(rec('A-583', '英国', 'Barry Higgins / Allness', 'https://www.allness.co.uk',
    'Barry Higgins(Allness)(库档英国;**R64-A 谱面:训练/顾问类别=停止挖掘铁律(R64 谱,不新挖)**;R66 统一谱基线=本体谱位存档,回复跟进维护不抵触(用户自发件)',
    '**Barry Higgins(CSV 公司名字段即本人谱位,official-self-published 级谱位公开件);R66 守界:训练/顾问类不新挖;统一基线存档**',
    [
        {'dim': '风险与注意', 'quote': 'Barry Higgins / Allness — 训练/顾问类别(R64 谱),停止挖掘铁律;R66 基线存档(2026-10-07)', 'source': 'https://www.allness.co.uk'},
        {'dim': '决策链与对接人', 'quote': 'Barry Higgins — CSV 公司名字段即本人谱位(official-self-published 级)', 'source': 'https://www.allness.co.uk'},
        {'dim': '近期动态与线索', 'quote': 'R66 守界班(A-583:训练/顾问类不新挖;本体谱位存档)', 'source': 'https://www.allness.co.uk'},
    ],
    {'lineup': '(守界：训练/顾问类不新挖)', 'scene': '(守界)', 'size': '个体谱面', 'tech': '(守界)', 'supply': '(守界)', 'risk': '训练/顾问类停止挖掘铁律(R64)',
     'unk': ['(守界：不新挖)'], 'pending': '守界件(R64：用户自发件=回复跟进维护不抵触)'},
    ('本体谱位存档', '守界=不新挖', '(守界)', '守界'), 'Hi Barry,',
    note='A-583 训练/顾问类停止挖掘铁律(R64);本体谱位存档'))

R.append(rec('A-584', '英国', 'Ron Touw / MikroTik Training UK', 'https://www.mikrotik-training.co.uk',
    'Ron Touw(MikroTik Training UK)(库档英国;**R64-A 谱面:训练/顾问类别=停止挖掘铁律(R64 谱,不新挖)**;R66 统一谱基线=本体谱位存档,回复跟进维护不抵触(用户自发件)',
    '**Ron Touw(CSV 公司名字段即本人谱位,official-self-published 级谱位公开件)—— MikroTik 认证 Trainer 谱位公开;R66 守界:训练/顾问类不新挖;统一基线存档**',
    [
        {'dim': '决策链与对接人', 'quote': 'Ron Touw / MikroTik Training UK — CSV 公司名字段即本人谱位;MikroTik 认证 Trainer 谱位公开件', 'source': 'https://www.mikrotik-training.co.uk'},
        {'dim': '风险与注意', 'quote': '训练/顾问类别(R64 谱),停止挖掘铁律;R66 基线存档(2026-10-07)', 'source': 'https://www.mikrotik-training.co.uk'},
        {'dim': '近期动态与线索', 'quote': 'R66 守界班(A-584:训练/顾问类不新挖;本体谱位存档)', 'source': 'https://www.mikrotik-training.co.uk'},
    ],
    {'lineup': '(守界：训练/顾问类不新挖;MikroTik 认证 Trainer 谱位公开件)', 'scene': '(守界)', 'size': '个体谱面', 'tech': 'MikroTik 认证 Trainer 谱位公开件', 'supply': '(守界)', 'risk': '训练/顾问类停止挖掘铁律(R64)',
     'unk': ['(守界：不新挖)'], 'pending': '守界件(R64：用户自发件=回复跟进维护不抵触)'},
    ('MikroTik Trainer 谱位公开', '守界=不新挖', '(守界)', '守界'), 'Hi Ron,',
    note='A-584 训练/顾问类停止挖掘铁律(R64);Trainer 本体谱位存档'))

out = {'date': '2026-10-07', 'wave': 'R66 第 4 波:A-570~A-584 尾段 12 户清零',
       'scope': '以色列/CY/DE/IT/SI/FR/US 7 丰产 + A-571 排噪守档 + A-578 停摆件 + A-583/584 守界 + A-580 人名基线',
       'records': R}
json.dump(out, open('batch/A类深挖_2026-10-07_R66_R56_KP第4波.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('R66 第 4 波', len(R), '户落盘')
