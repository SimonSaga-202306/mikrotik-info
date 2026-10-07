# -*- coding: utf-8 -*-
"""R65 B 类深挖第 5 批:冰岛/拉脱维亚/挪威/土耳其/奥地利/希腊 8 户。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 5 批精修 = R57 转写 + 本轮登记/官网新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-058',
    head='Öruggt Net ehf(dba Secure Net;Köllunarklettsvegur 1, 104 Reykjavik(旧 Kristínargata 1 102);KT 670224-0740,VSK 152122;'
         '**谱型核正:网络安全咨询/服务公司(不是纯分销)**——cybersecurity for Icelandic companies,info@oruggtnet.is,+354-551-5120;双址搬迁',
    kpn='—(冰岛 ehf 董事实名待 rsk.is 登记检索;谱型位置在全岛 SME 安全合规方)',
    facts=[{'dim': 'R65 谱型+登记', 'text': 'Cybersecurity consultancy;KT 670224-0740;双址 104/102 Reykjavik;函 boxinfo@oruggtnet.is',
            'quote': 'We are Öruggt Net ehf, or Secure Net in English … Cybersecurity for Icelandic companies … KT: 670224-0740 VSK: 152122',
            'url': 'https://securenet.is/'}],
    fihadd='谱型核正:安全咨询非纯分销,MikroTik 谱挂服务线')

put('B-178',
    head='GOODSTORE(SIA Goodman Group,Reg.No 41503064521,LV41503064521;Muzeja iela 11(注解法 Vidus iela 32 条带+质保), Daugavpils, LV-5401;'
         '**谱位=Daugavpils 当地综合弱电系统集成商**——设计+施工 视频安防/门禁/火警/低压系统 多年经验,bulk online store 平台 veikals@goodstore.lv;Swedbank HABALV22)',
    kpn='—(SIA Goodman Group valdnieks 拉托维亚登记查询方向)',
    facts=[{'dim': 'R65 谱位/登记', 'text': 'SIA Goodman Group · Daugavpils · 弱电(视频安防/门禁/火警)设计施工一体商 · goodstore.lv 平台;Reg 41503064521',
            'quote': 'SIA "Goodman Group" is a company with extensive experience in the design and construction of low-voltage systems and networks … Muzeja street 11, Daugavpils',
            'url': 'https://goodstore.lv/en/about-us/'}],
    fihadd='弱电系统集成+城 home 平台;footer Miide forte PoE 谱在架有其接口')

put('B-517',
    head='Fiberworks AS(Org.nr 959 977 046,Eikenga 11, 0579 Oslo;1990-12-27 创(1995-02-20 都注册);**瑞典 Sorb Industri AB 全资**(100%);'
         '24 员工;NACE 46.500 ICT 批发;ORing 授权分销(库内信号);Roger Allan Wahlgren(f1973)Daglig leder + Martin Roland Linder(f1972)Styrets leder;+47 23 03 53 30)',
    kpn='Roger Allan Wahlgren = Daglig leder(常务 CEO);Martin Roland Linder = Styrets leder(董事长);Sorb Industri AB 全资母(瑞典集团)',
    kp=[{'name': 'Roger Allan Wahlgren', 'role': 'Daglig leder(常务/CEO)', 'contact': '经 fiberworks.no/1881 总机 23 03 53 30 索取', 'status': '1881.no + proff.no + gulesider.no 三源实名', 'source': 'https://www.1881.no/telematikk-og-telekommunikasjon/telematikk-og-telekommunikasjon-oslo/telematikk-og-telekommunikasjon-oekern/fiberworks-as_100206951S1/'},
        {'name': 'Martin Roland Linder', 'role': 'Styrets leder(董事长)', 'contact': '—', 'status': '同源', 'source': '同 1881.no'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'Org 959977046 · 1990 创 · 24 员工 · Sorb Industri AB(瑞典)100% · Wahlgren=Linder 两实名',
            'quote': 'Daglig leder Roger Allan Wahlgren … Aksjonærer: Sorb Industri AB (100%) … Stiftelsesdato: 27.12.1990',
            'url': 'https://www.1881.no/telematikk-og-telekommunikasjon/telematikk-og-telekommunikasjon-oslo/telematikk-og-telekommunikasjon-oekern/fiberworks-as_100206951S1/'}],
    fihadd='Sorb Industri AB 全资子=ORing 谱中的北欧补位')

put('B-094',
    head="Merpa Bilgi Islem Ltd.Sti.(1990 Genel Mudur Ali Nail Kocyigit Ankara 创立;USD6.7M 收 16 员工 Istanbul 主体;工业信息化 endustriyel bilisim 加 NINOVA 自有品牌 加 MikroTik 土耳其分销 加多个政府项目;merpazar.com 工业特化 35 年品牌)",
    kpn='Ali Nail Koçyiğit = Genel Müdür(总经理,1990 创始人);Mustafa Süzer = Manager;Erhan Işık = 数字营销',
    kp=[{'name': 'Ali Nail Koçyiğit', 'role': 'Genel Müdür(总经理/1990 创始人)', 'contact': '经 merpazar.com 官方联系渠道', 'status': '官网 kimdir 页自曝', 'source': 'https://www.merpazar.com/merpazar-com-kimdir'},
        {'name': 'Mustafa Süzer', 'role': 'Manager', 'contact': '—', 'status': 'RocketReach 自曝', 'source': 'https://rocketreach.co/merpa-bilgi-islem-ltdsti-profile_b405d56afc11f555'}],
    facts=[{'dim': 'R65 官网自曝', 'text': '1990 Ankara 创始 Genel Müdür Ali Nail Koçyiğit;工业 35 年品牌;MikroTik 分销+政府项目实录',
            'quote': 'Şirketimizin temelleri 1990 yılında, Genel Müdürümüz Ali Nail Koçyiğit tarafından … Mikrotik Network ürünlerinin de distribütörlüğünü yapmaktadır',
            'url': 'https://www.merpazar.com/merpazar-com-kimdir'}],
    fihadd='工业 IT 35 年+ MikroTik 政府项目分销=当前谱年谱音最能录')

put('B-108',
    head='AlpenEDV KG(Arbesgasse 6, 6060 Hall in Tirol;Firmenbuch 488347h, Landesgericht Innsbruck;UID ATU73285429;'
         '**Christoph Bernhard Weiler = gewerberechtliche Geschäftsführung(两 GISA 证号 30592162/30592148)**=法定经营负责人;'
         '五人小队(David/Sascha/Christoph/Daniel/Sonja 团队照自曝);IT 服务+B2B 中小客户咨询/机房建设/WLAN/VPN/视频监控/Datenschutz 咨询体;+43 660 2552551, office@alpenedv.at)',
    kpn='Christoph Bernhard Weiler = gewerberechtliche GF(法定经营负责人,WKO Firmendatenbank+top.tirol 双源)',
    kp=[{'name': 'Christoph Bernhard Weiler', 'role': 'Gewerberechtliche Geschäftsführung(法定经营负责人)', 'contact': 'office@alpenedv.at / 0660 2552551', 'status': 'wko.at + top.tirol 双源实名', 'source': 'https://firmen.wko.at/alpenedv-kg-alpenedv/tirol/?firmaid=4476f43c-a580-449a-8aae-66ad660c2e43'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'AlpenEDV KG FB 488347h · Innsbruck 法院 · 双方 GISA 号 · Christoph Bernhard Weiler Gew.-GF 双源实名',
            'quote': 'Gewerberechtliche Geschäftsführung: Christoph Bernhard Weiler GISA-Zahl: 30592162 … GF: Christoph Weiler … 0660/2552551',
            'url': 'https://www.top.tirol/unternehmen/innsbruck-land/alpenedv-kg'}],
    fihadd='奥地 Hall in Tirol 五人小队 IT 服务体;Stammbaum 谱 MikroTik 挂服务配套线')

put('B-111',
    head='Netzware Handels- und IT-Dienstleistungs GmbH(Davidgasse 85-89, A-1100 Wien;FB 413095v, HG Wien, 2014-04-02 注册,Stammkapital €35,000;UID ATU68575437;'
         '**GF 双董事 Florian Ivo(2014 在任)+ Dietmar Guelfenburg(2016-01 在任)**=两人联署;'
         'evi.gv.at 登记源+官网 impressum+karriere.at 三源;11-30 员工;office@netzware.at,+43 1 3577770;MikroTik/Acer/ASUS/HP 等分销',
    kpn='Florian Ivo + Dietmar Guelfenburg = 双 Geschäftsführer(evi.gv.at Firmenbuch 实名+官网 impressum)',
    kp=[{'name': 'Florian Ivo', 'role': 'Geschäftsführer(2014-04-02 在任)', 'contact': 'office@netzware.at / +43 1 3577770', 'status': 'evi.gv.at + impressum 双源实名', 'source': 'https://www.evi.gv.at/f/413095v'},
        {'name': 'Dietmar Guelfenburg', 'role': 'Geschäftsführer(2016-01-29 在任)', 'contact': '同上', 'status': '同源', 'source': '同 evi.gv.at'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'FB 413095v · 2014-04 HG Wien · GF Florian Ivo + Dietmar Guelfenburg 二人联署 · €35K 股本',
            'quote': 'Geschäftsführer: Florian Ivo, Dietmar Guelfenburg … Firmenbuchnummer: 413095v … Eintragungsdatum: 02.04.2014',
            'url': 'https://netzware.at/unternehmen/impressum/'}],
    fihadd='11-30 人维也纳分销;两 GF 2014 创——最像长辈白学的标的物')

put('B-514',
    head='Alpha Motion SA(Pikérmi, Attiki;1994 创(创始人前 Alpha Technologies TD 1992-94/KITCO 1987-92 带);'
         '**Argiris Saninos = Owner-Chairman-Managing Director(1994 至今,Rafina 居住)**;'
         'Dimitris Psichoulas = Technical Director;9-11 员工;info@alpha-motion.gr,+30 210 822 XXXX;'
         '库内原样=HMS/N-Tron·Red Lion 工业自动分销=谱型=工控自动化 VAD',
    kpn='Argiris Saninos = Owner-Chairman-MD(1994 创始);Dimitris Psichoulas = Technical Director',
    kp=[{'name': 'Argiris Saninos', 'role': 'Owner-Chairman-Managing Director(1994 创始)', 'contact': '经 alpha-motion.gr(RocketReach 域 alpha-motion.gr 自曝)', 'status': 'rocketreach+crunchbase 双源', 'source': 'https://rocketreach.co/argiris-saninos-email_31660765'},
        {'name': 'Dimitris Psichoulas', 'role': 'Technical Director', 'contact': '—', 'status': 'rocketreach 自曝', 'source': 'https://rocketreach.co/alpha-motion-sa-profile_b5da2937f42e5697'}],
    facts=[{'dim': 'R65 实名/工业谱', 'text': 'Argiris Saninos Owner 1994-now;Alpha Motion=N-Tron/Red Lion 工控谱=', 'quote': 'Argiris Saninos … 1994 - now Owner - Chairman - Managing Director @ Alpha Motion SA … Industrial Automation', 'url': 'https://www.crunchbase.com/organization/alpha-motion'}],
    fihadd='HMS/N-Tron/Red Lion 同集团工业自动谱系,AEGEE +30 693 242…')

put('B-129',
    head='MARAC Electronics S.A.(Athens 26 V. Konstantinou GR-116 35 + Thessaloniki 12 Polytechniou GR-546 25 双办;1992 创;'
         '1600 m² 自建制造厂 Alexandroupolis(可扩 2500);**希腊国家级微波链路实干龙头**:OTE PDH/SDH 链路+WIND Hellas 近十年 2500+ 链路(5000 终端)统包;'
         '工业制造与装配=谱型=telecom infrastructure 工程商;MikroTik 谱挂=降单供应链)',
    kpn='—(SA 董事会层名册 G.E.MI 台账查询方向;mil/Certified 名单大楼靠)',
    facts=[{'dim': 'R65 谱位实录', 'text': '1992 创;OTE+WIND HELAS 微波链路 2500+ 链路(5000 终端)统包;1600m² 自有工厂 Alexandroupolis',
            'quote': 'Η ΜΑΡΑΚ Ηλεκτρονική ΑΒΕΕ έχει … περισσότερες από 2.500 ζεύξεις (περίπου 5.000 τερματικές συσκευές) … WIND Hellas τα τελευταία 10 χρόνια',
            'url': 'https://www.marac.gr/index.php?pid=20&tid=11'},
            {'dim': 'R65 制造面', 'text': '自 1992 Alexandroupolis 1600m² 工业制造与装配厂(可扩 2500)', 'quote': 'Since 1992, MARAC owns a modern manufacturing plant which covers a 1.600 sq.m. area in Alexandroupolis', 'url': 'https://www.marac.gr/Profile%20Marac.pdf'}],
    fihadd='国家级电信工程商;工业制造自持有=OEM 聊话题性最大')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 5 批(冰岛/拉脱维亚/挪威/土耳其/奥地利/希腊)',
       'scope': 'B-058 / B-178 / B-517 / B-094 / B-108 / B-111 / B-514 / B-129',
       'records': [by[c] for c in ('B-058', 'B-178', 'B-517', 'B-094', 'B-108', 'B-111', 'B-514', 'B-129')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第5批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 5 批 8 户落盘')
