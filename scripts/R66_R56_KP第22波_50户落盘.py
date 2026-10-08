# -*- coding: utf-8 -*-
"""R66 第 22 波(50 户扩招批):A-329~A-378 顺延 50 户;公司档 29(FR3+IT11+NL2+BE1+NO1+PT1+ES1+DE1+US2+GR2+SK1+MT1)+人名档 21(东欧/巴尔干/波罗的海新领土)。"""
import json

PRICE = '$180 USD EXW (2026-10-08, 15天有效)'
O = 'official-self-published·谱/leads-only(直发需 opt-in)'
G = 'leads-only·待 opt-in(LinkedIn/谱面带核)'
STRUCT = json.load(open('batch/structured_profiles_v1.json', encoding='utf-8'))

def push_of(code):
    return STRUCT.get(code, {}).get('p1') or 'STC-424XGGPM-280W'

def fu(push):
    return [
        {'stage': '第 1 次跟进 · 具名 kp 引路口', 'push': push, 'angle': '具名 kp 引路 → 采购/技术硬件分载线',
         'question': '贵司 24 口 PoE 交换机的硬件采购线由哪位同事主责？', 'proof': '规格页'},
        {'stage': '第 2 次跟进 · 一页目录卡', 'push': '一页目录卡', 'angle': '价值层 PoE 谱链卡', 'question': '可否入谱链名录？', 'proof': '卡'},
        {'stage': '第 3 次跟进 · 留档+LinkedIn 谱', 'push': '—', 'angle': '谱链明智途径', 'question': '—', 'proof': '—'},
    ]

def rec(code, name, heads, kp, evs, scene, size, sw, risk, email_sal,
        inference='R66 第 22 波具名 KP 金谱', trend='2026-10-08 R66 22 波谱名牌', gap='R66 22 波谱面锁定'):
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 第 22 波点名(谱面无实名)**'
    dims = {'业务定位': heads, '产品线与在售品牌': '(波次二补谱面)', '目标行业与场景': scene, '团队与规模': size,
            '决策链与对接人': kb, '技术与认证': '(波次二补)', '采购与供应链信号': '(波次二补)',
            '近期动态与线索': trend, '与我方契合点': '24 口 value PoE 谱链窗口', '风险与注意': risk}
    return {'customer': code, 'fact': name + ':' + heads, 'inference': inference,
            'hypothesis': '24 口 value PoE(' + PRICE + ')具名谱位引路', 'evidence_main': evs[0]['source'],
            'tech': '(波次二补)', 'hr': size, 'contact_found': kb, 'contact_pending': '直发具名需 opt-in',
            'dims': dims, 'evidence': evs, 'followups': fu(push_of(code)),
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': '(待谱面二补)', '③KP 深挖': kb,
                             '④Saga 对标': '24 口 value PoE(' + PRICE + ')', '⑤在乎与偏好': sw[0],
                             '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['直发具名需 opt-in'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': '波次二补', '合作方式': '未知', '缺口证据': '(波次二)'},
                    'gap_proof': gap},
            'kp': [{'name': k[0], 'role': k[1], 'contact': k[2], 'status': k[3], 'source': k[4]} for k in kp],
            'unknowns': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'email': email_sal + '\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-08, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?\n\nBest regards,\nSaga Networks Export Desk'}

def ev(d, q, u):
    return {'dim': d, 'quote': q, 'source': u}

R = []

# ============ 公司档×29 ============
R.append(rec('A-329', 'GTD International',
    'GTD INTERNATIONAL SAS(法国 Lavelanet(Ariège),Hôtel d\'Entreprise de la Coume;**SIREN 794778977;TVA FR22794778977;2013-08-07 创;SAS cap €1,525,000;20-49 人(23);CA €5.96M(2024);RCS 旧名 Celeres France;GTD 集团 6 实体头(西班牙 GTD 工程集团系)**;**Président: Angel Ramirez Navarro(1959 生,2016-08-31 起;pappers/manageo/verif/infonet 四源 O)**;PELICAN 敏感设施安防关联谱(Hugues Moizan 实控)=敏感段守界注;**p1=STI-288GP 供位谱**',
    [('Angel Ramirez Navarro', 'Président(2016 起;四源一致)', 'pappers.fr 件', O, 'https://www.pappers.fr/entreprise/gtd-international-794778977'),
     ('Ali Merabet Chater', 'Directeur Général(bfmtv 谱面条;HMC IMMO 同址;差旗待核)', 'dirigeants.bfmtv.com 件', G, 'https://dirigeants.bfmtv.com/Ali-MERABET-CHATER-3936103/')],
    [ev('决策链与对接人', 'Dirigeant: RAMIREZ Angel, Président(depuis 31/08/2016;né 1959);dirige 2 entreprises dont GTD INTERNATIONAL(pappers/infonet 件);bfmtv 谱: Ali MERABET CHATER Directeur général(差旗注)', 'https://www.pappers.fr/entreprise/gtd-international-794778977'),
     ev('联系方式与基础画像', 'SIREN 794 778 977;1 Chemin de la Coume, 09300 Lavelanet;SAS €1.525M;CA €5.964.000(2024);resultat net €733.543;groupe 6 entités;旧名 Celeres France;Toulouse/Rueil-Malmaison 2 支局(verif/manageo 件)', 'https://www.verif.com/societe/GTD-INTERNATIONAL-794778977/')],
    '法国阿列日 €6M 编程/工程谱(GTD 系)', '23 人;2013 创',
    ('集团头+敏感设施安防邻谱', '敏感段守界注', 'Ramirez 直达位', '集团链竞谱'),
    'Angel Ramirez 直达(opt-in 律;敏感设施守界)', 'Monsieur Ramirez,',
    trend='2026-10-08 R66 22 波谱名牌(p1=STI-288GP 供位)'))

R.append(rec('A-330', 'NXO France',
    'NXO FRANCE SAS(法国 Rueil-Malmaison,133 Boulevard National, 92500;**SIREN 811934363;cap €12.5M;**CA €293.6M(2023)/€303.9M(2024)**;=FAYAT 集团 477 实体谱(建筑巨头系)**;**换代金谱:Président du directoire Nathalie Magand(1976 生;2023-11-01 接替 Jean-Maurice Fritsch;BODACC O)**;Président du conseil de surveillance Jean-Claude Fayat(2024-08 起)+VP Laurent Fayat;**Statut SIREN Radié 2026-03-30 vs RCS/RNE Active=INSEE 滞后差旗注**;NXO EXPERTS 关联(Magand DG 双职)',
    [('Nathalie Magand', 'Président du directoire(2023-11 换代接棒;BODACC O)', 'pappers.fr/BODACC 件', O, 'https://www.pappers.fr/entreprise/nxo-france-811934363'),
     ('Jean-Claude Fayat', 'Président du conseil de surveillance(FAYAT 集团主)', 'verif.com 件', O, 'https://www.verif.com/societe/NXTO-FRANCE-811934363/'),
     ('Laurent Fayat', 'Vice-président(FAYAT 族)', 'verif/manageo 件', O, 'https://www.manageo.fr/entreprises/811934363.html')],
    [ev('决策链与对接人', 'BODACC: Mme Nathalie MAGAND nommée Président de la société et Président du Directoire(à compter 01/11/2023)en remplacement de M. Jean-Maurice FRITSCH;Conseil de surveillance: Jean-Claude FAYAT(Président)+Laurent FAYAT(VP)(pappers/manageo/verif 件)', 'https://www.pappers.fr/entreprise/nxo-france-811934363'),
     ev('联系方式与基础画像', 'SIREN 811 934 363;133 Bd National, 92500 Rueil-Malmaison;SAS €12.5M;1000-1999 salariés;**CA €293.591M(2023)**;groupe FAYAT 477 entités;7112B Ingénierie;**SIREN Radié(30/03/2026)vs RCS Active=差旗注**(manageo/infonet/verif 件)', 'https://www.manageo.fr/entreprises/811934363.html')],
    '法国吕埃 €294M ICT 工程巨头(FAYAT 系)', '1000-1999 人;€12.5M 资',
    ('€294M 巨头+换代谱=FAYAT 链大户', '集团审批链', 'Magand 新班直达位', '巨头集采竞谱'),
    'Nathalie Magand 新班位(opt-in 律;集团集采谱)', 'Madame Magand,',
    trend='2026-10-08 R66 22 波谱名牌(换代+SIREN 差旗注)'))

R.append(rec('A-331', 'SYNEXIE',
    'SYNEXIE(法国 Toulon(档标 La Valette du Var→Toulon 31 rue Chevalier Paul 迁址谱);**SIREN 449807460;网安专家(ExpertCyber 标;OT/工业控制系统安全谱)**;**换代+并购双窗:Serge Nicod(2014-2022 Gérant)→Matthieu Nicod(1989 生,2021-09)→2022-12-31 退→SAS OLBIA KAPITAL 接任 Président(法人并购接棒;BODACC/lefigaro 件)→谱面现任自然人具名缺→守档准由(OT 安全谱在档)**',
    [],
    [ev('决策链与对接人', 'BODACC/lefigaro 件: démission Serge NICOD(31/12/2022)+Matthieu NICOD cessé;nomination **SAS OLBIA KAPITAL(Président)**;谱面现任自然人具名缺=守档准由(2026-10-08 R66 22 波留痕)', 'https://entreprises.lefigaro.fr/synexie-83/entreprise-449807460'),
     ev('联系方式与基础画像', '31 rue Chevalier Paul, 83000 Toulon;ExpertCyber 标;cybersécurité:systèmes/réseaux sécurisés+**systèmes de contrôle industriels(OT 安全)=守界注**;+33 498080280(solutions-numeriques/zoominfo 件)', 'https://www.solutions-numeriques.com/fiche/synexie/')],
    '法土伦网安谱(法人接棒换代,具名缺)', '中小谱;OT 安全守界',
    ('OT 安全专营=壁垒谱', '具名缺守档', '无守档', '—'),
    '守档:OLBIA KAPITAL 接棒,具名待专批', 'Madame, Monsieur,'))

R.append(rec('A-332', 'Adrianet Snc',
    'ADRIANET S.R.L.(旧体 SNC DI ABBINANTE MUZIO & C.)(意大利 Valenzano(BA),Via dell\'Indipendenza 10;**P.IVA 06075650728;REA 460897;2004-01-19 登;2 人(2025);cap €30k;通信设备安装维护(951029)**;**客户全公共谱:Politecnico di Bari/Arpa Puglia/Comune di Bari/Regione Puglia/Tecnopolis/Aeroporto Bari-Palese e Brindisi/Porto di Bari/scuole=公段守界加厚**;MePA 2024 供应商(机电/软件档=公采守界);**Muzio Abbinante(旧体全称业主谱)+Michele Perrino(官网页脚署名)**',
    [('Muzio Abbinante', '业主名谱(旧体 SNC 全称: di Abbinante Muzio & C.)', 'MePA/amministrazionicomunali 件', O, 'https://www.amministrazionicomunali.it/puglia/valenzano/adrianet-snc-di-abbinante-muzio-e-c'),
     ('Michele Perrino', '网站实现者(官网页脚署名「Realizzato da」)', 'adrianetsrl.it 页脚', G, 'https://www.adrianetsrl.it/')],
    [ev('联系方式与基础画像', 'ADRIANET SRL;P.IVA 06075650728;Via dell\'Indipendenza 10, 70010 Valenzano (BA);080 467 2023;info@adrianetsrl.it;PEC adrianetsrl@pec.it;2 dipendenti(ufficiocamerale/官网件)', 'https://www.ufficiocamerale.it/2267/adrianet-snc-di-abbinante-muzio-c'),
     ev('目标行业与场景', '客户谱(官网自署): Politecnico di Bari/Arpa Puglia/Comune di Bari/Regione Puglia/Aeroporto Bari-Palese/Porto di Bari/scuole=**公共段全覆盖=守界加厚**;MePA 供应商档', 'https://www.adrianetsrl.it/')],
    '意巴里 2 人通信安装铺(全公客户守界)', '2 人;2004 登',
    ('MePA 公采谱+旧体业主名', '**公共段守界加厚**', 'Abbinante 位(旧体谱)', '公采链竞谱'),
    'Muzio Abbinante 位(opt-in 律;**公段守界**)', 'Gentile Sig. Abbinante,'))

R.append(rec('A-333', 'C.G.T. Elettronica SpA',
    'C.G.T. ELETTRONICA S.p.A.(意大利 Roma(法址 Via della Giuliana 80, 00195;办 Via Adriano Olivetti 24/26+Viterbo);**P.IVA 01668611005;C.F. 07018000583;1985 创 41 年;42 人;€15M;电信+安防系统工程(43.21.02)**;**Amministratore Delegato: Michele Grifa(1954-05-06 生 Foggia;Ing. 创主=唯一签名代表;**difesa.it 国防部合同 PDF 签名页=O 级官方件!)**;**军产谱最高守界:核电站顾问史/罗马-那不勒斯列车控制/Aeronautica Militare ISMA(佛罗伦萨军事科学院多媒体教室)/Caserma 军营改建=军防 KRITIS 最高守界;**p1=STC-28DGGPM 供位谱**;成员谱 Anna Maria Grifa(族)+Ferrazzani/Landi/Maurizi/Fracasini/Ottaviani(atoka)',
    [('Michele Grifa', 'Amministratore Delegato/Ing. 创主(1985;国防部合同签名件 O)', 'difesa.it 合同 PDF 签名页(O)', O, 'https://www.difesa.it/assets/allegati/51507/scrittura_privata_n_06-2024_cgt_controfir..2024.04.26.15.12.07.741.pdf'),
     ('Anna Maria Grifa', '成员谱(Grifa 族)', 'atoka 成员件', G, 'https://atoka.io/public/it/azienda/cgt-elettronica-compagnia-generale-telecomunicazioni-ed-elet-ronica-spa-in-breve-cgt-spa/70056bb4d935')],
    [ev('决策链与对接人', '「la C.G.T. ELETTRONICA S.P.A.…rappresentata dal **Sig. Michele GRIFA**(Cod. Fisc. GRFMHL54E06D643Z), nato a Foggia il 06/05/1954, nella sua qualità di **Amministratore Delegato**」(difesa.it 合同签名页=O 官方件;established 1985 by Ing. Michele Grifa 官网史)', 'https://www.difesa.it/assets/allegati/51507/scrittura_privata_n_06-2024_cgt_controfir..2024.04.26.15.12.07.741.pdf'),
     ev('联系方式与基础画像', 'P.IVA 01668611005;Via della Giuliana 80, 00195 Roma(+Viterbo 01100);+39 06 65793119;42 dipendenti;€15M;43.21.02 电子安装(atoka/amministrazionicomunali 件);**客户谱: Difesa(军)/Aeronautica Militare ISMA/核电史/列车控制史=军防最高守界**', 'https://atoka.io/public/it/azienda/cgt-elettronica-compagnia-generale-telecomunicazioni-ed-elet-ronica-spa-in-breve-cgt-spa/70056bb4d935')],
    '意罗马 41 年军系电信工程屋(**最高守界**)', '42 人;1985 创',
    ('国防部签名件 O+41 年谱=金谱', '**军防 KRITIS 最高守界**', 'Grifa AD 唯一直达位', '军供链竞谱'),
    'Michele Grifa AD 位(opt-in 律;**军防守界:24 口二轨窄针,不触军段**)', 'Gentile Ing. Grifa,',
    trend='2026-10-08 R66 22 波谱名牌(p1=28D 供位;军谱)'))

R.append(rec('A-334', 'CAMELI SAT',
    'Cameli Sat di Burgalassi Agnese(意大利 Donoratico(Castagneto Carducci, LI),Via V. Veneto 24;**IMPRESA INDIVIDUALE 个体户**;**收银机/商铺设备/安防器材小店(0565 774391)**;**业主: Agnese Burgalassi(商号即业主名;informazione-aziende/CRIBIS 件)**;档谱 Allied 代理注;无公开站点',
    [('Agnese Burgalassi', 'Titolare(个体户业主;商号具名)', 'informazione-aziende.it/CRIBIS 件', G, 'https://www.informazione-aziende.it/Azienda_CAMELI-SAT-DI-BURGALASSI-AGNESE')],
    [ev('联系方式与基础画像', 'Cameli Sat di Burgalassi Agnese;Via V. Veneto 24, 57022 Donoratico (LI);0565 774391;IMPRESA INDIVIDUALE;Registratori di cassa/forniture e attrezzature per negozi(informazione-aziende/paginegialle 件)', 'https://www.informazione-aziende.it/Azienda_CAMELI-SAT-DI-BURGALASSI-AGNESE'),
     ev('近期动态与线索', '档录类型: 集成商/代理(Allied Telesis 谱);无公开站点;R66 22 波谱面核验:主业收银/商铺器材,网络件链谱待二批(2026-10-08 留痕)', 'https://www.paginegialle.it/donoratico-li/registratori-di-cassa/burgalassi-agnese_3')],
    '意托斯卡纳个体商铺器材铺', '个体铺谱',
    ('业主名谱=直达', '微实体谱;主业偏', 'Burgalassi 唯一直达位', '区域链竞谱'),
    'Agnese Burgalassi 直达(opt-in 律)', 'Gentile Sig.ra Burgalassi,'))

R.append(rec('A-335', 'Dps Informatica S.n.c',
    'DPS INFORMATICA S.N.C. DI PRESELLO GIANNI & C.(意大利 Fagagna(UD),Piazza Marconi 11, 33034;**P.IVA 01486330309;CCIAA UD 176440;SNC 合伙谱**;**业主名谱: Gianni Presello(全称 di Presello Gianni & C.;摩德纳省府采购件 O-ish)**;**Riello UPS 官方伙伴页 O;dps@dpsinformatica.it;INPS 用工谱**',
    [('Gianni Presello', 'Socio 名谱(SNC 全称具名)', 'provincia.modena 公采件', O, 'http://visualizzatoreatti.provincia.modena.it/AttiVisualizzatore/download/determina/2065375?fId=2067106')],
    [ev('决策链与对接人', 'Ragione sociale: DPS INFORMATICA S.N.C. DI PRESELLO GIANNI & C.;C.F./P.IVA 01486330309;PEC DPSINFORMATICA@LEGALMAIL.IT(省府采购决定件)', 'http://visualizzatoreatti.provincia.modena.it/AttiVisualizzatore/download/determina/2065375?fId=2067106'),
     ev('联系方式与基础画像', 'Piazza Marconi 11, 33034 Fagagna (UD);+39 0432 801790;dps@dpsinformatica.it;**Riello UPS 官方伙伴**(riello-ups.it 伙伴页 O);MePA/省府直销谱(bergamo/modena 件)', 'https://www.riello-ups.it/partners/91-dps-informatica-snc')],
    '意弗留利 SNC 电脑小铺(Riello 伙伴)', '小铺谱',
    ('全称业主+Riello 伙伴=直达', '小微谱', 'Presello 直达位', '区域链竞谱'),
    'Gianni Presello 直达(opt-in 律)', 'Gentile Sig. Presello,'))

R.append(rec('A-336', 'EULOGIC NT Spa',
    'Eulogic(**NT SpA 运营体**;意大利 Bari,Via Giovanni Amendola 191/S(旧体 SRL 址);**2010 创;11-50 人;IT 安全/网络+MePA 2024 供应商(通信设备+ICT 咨询=公采守界注)**;**Corp IT Distretto Puglia 委员 2025:Claudio Tinelli(Co-Founder)接任 Salvatore Latronico 项;RR 谱:Antonello Giordano Amministratore+Luigi Uva Sales Manager+Vincenzo Servedio PDM**;**差旗注:旧体 Eulogic S.R.L.(P.IVA 07006180728)Stato Cessata 已注销→NT SpA 新体承接;Vito Virgilio Managing Partner(LI 旧体谱)**',
    [('Antonello Giordano', 'Amministratore(RR 谱面条)', 'rocketreach 谱面条', G, 'https://rocketreach.co/luigi-uva-email_170774091'),
     ('Claudio Tinelli', 'Co-Founder+Distretto Informatica 委员(LI/Distretto 件)', 'linkedin.com/company/eulogic-srl 件', O, 'https://it.linkedin.com/company/eulogic-srl'),
     ('Luigi Uva', 'Sales Manager(销售口 KPI)', 'rocketreach 谱面条', G, 'https://rocketreach.co/luigi-uva-email_170774091')],
    [ev('决策链与对接人', 'RR: Antonello Giordano(Amministratore)+Luigi Uva(Sales manager at Eulogic NT SpA)+Vincenzo Servedio(PDM);LI: Claudio Tinelli(Co-Founder;Distretto Informatica Puglia Comitato Direttivo 2025 接任)+Vito Virgilio(MP,旧体谱)', 'https://rocketreach.co/luigi-uva-email_170774091'),
     ev('联系方式与基础画像', 'Bari;2010 founded;11-50;network/cyber security;MePA 2024 供应商(Beni 通信设备+Servizi ICT 咨询);**旧体 SRL Cessata→NT SpA 承接谱**(amministrazionicomunali/registroaziende/linkedin 件)', 'https://www.amministrazionicomunali.it/puglia/bari/eulogic')],
    '意巴里 15 年 IT 安全屋(新旧体承接谱)', '11-50 人;2010 创',
    ('Distretto 委员 Co-Founder 谱', '体承接差旗注+公采守界', 'Giordano AD+Uva 销售直达位', '区域链竞谱'),
    'Antonello Giordano+Luigi Uva 位(opt-in 律;公采守界)', 'Gentile Sig. Giordano,'))

R.append(rec('A-337', 'I&SI S.p.A',
    'I.&S.I. S.p.A.(Ingegneria & Software Industriale)(意大利 Roma(法址 Via della Scrofa 57, 00186)+Aprilia(LT)运营址 Via della Meccanica 2b, 04011;**1984 创 42 年;工业软件/电气工程(SGSI 安全管理体系谱)**;**Direzione Aziendale: Paolo Graziosi(2024-12-02 公司政策文件签署=官网 O)**;ingesw.com first@ 88% 邮箱式',
    [('Paolo Graziosi', 'Direzione Aziendale(公司政策文件签署)', 'ingesw.com 政策页(O)', O, 'http://www.ingesw.com/ingesw/politica-aziendale/')],
    [ev('决策链与对接人', 'Politica aziendale 签署: 「Aprilia, 02.12.2024 — **Paolo Graziosi (Direzione Aziendale)**」(ingesw.com 官网件)', 'http://www.ingesw.com/ingesw/politica-aziendale/'),
     ev('联系方式与基础画像', 'Sede legale: Via della Scrofa 57, 00186 Roma;Sede operativa: Via della Meccanica 2b, 04011 Aprilia (LT);+39-06 928651;founded 1984;SGSI 体系谱(Ingegneria&Software Industriale)(ingesw/salary.com 件)', 'https://www.salary.com/research/company/i-si-spa-overview')],
    '意罗马-阿普里利亚 42 年工业软件屋', '中型谱;1984 创',
    ('42 年老牌+SGSI 体系', '谱面薄', 'Graziosi 位(O 件)', '区域链竞谱'),
    'Paolo Graziosi 直达(opt-in 律)', 'Gentile Sig. Graziosi,'))

R.append(rec('A-338', 'Irene',
    'IRENE S.R.L.(意大利 Genova,Via Giovanni Opisso 89/91 RR, 16155;**P.IVA 01002040093;REA SV 106235;**1991-07-23 创 35 年**;<25 人;$2M;46.51 电脑批发**;**Key Principal/President: Giovanni Pozzo(D&B 件)**;**工业 rack/wall-mount PC+panel PC+**医疗计算平台(point-of-care/医疗监视器)=医疗段守界注**+容错服务器 24x7/嵌入式板谱**',
    [('Giovanni Pozzo', 'President(D&B Key Principal)', 'D&B 件', G, 'https://www.dnb.com/business-directory/company-profiles.irene_srl.792d9c1ea8a07b8e089780950ecc4828.html')],
    [ev('决策链与对接人', 'Key Principal: GIOVANNI POZZO, President(D&B 件)', 'https://www.dnb.com/business-directory/company-profiles.irene_srl.792d9c1ea8a07b8e089780950ecc4828.html'),
     ev('联系方式与基础画像', 'IRENE SRL;P.IVA 01002040093;Via Opisso 89/91 RR, 16155 Genova;010 6972264;founded 1991;**medical computing platform+industrial rack PC+fault tolerant server 24x7**(informazione-aziende/rocketreach 件)', 'https://rocketreach.co/irene-srl-profile_b419a08fff3a9a4c')],
    '意热那亚 35 年工业/医疗计算件铺', '<25 人;1991 创',
    ('35 年+医疗计算平台=缝隙谱', '**医疗段守界注**', 'Pozzo 直达位', '区域链竞谱'),
    'Giovanni Pozzo 直达(opt-in 律;医疗段守界)', 'Gentile Sig. Pozzo,'))

R.append(rec('A-339', 'ML Software S. r. l',
    'ML SOFTWARE S.R.L.(意大利 Catania,Via Roccaromana 32/A, 95124;**P.IVA 04656500875;REA 310635;2009-02-03 登;4 人(2025);€1.45M(2024) 盈利 €242.8k**;**MePA 供应商(软件许可+信息安全)**;网络管理/数据恢复/异地备份/远程桌面/VoIP;**双体注:旧个体体 ML SOFTWARE DI LUCA MASSIMO(P.IVA 03095830877)已注销→SRL 体承接;Massimo Luca 名谱(旧体差旗)**',
    [('Massimo Luca(名谱)', '旧个体体名(已注销差旗注;SRL 体现任具名待专批)', 'ufficiocamerale 件', G, 'https://www.ufficiocamerale.it/8171/ml-software-di-luca-massimo')],
    [ev('决策链与对接人', '旧体: ML SOFTWARE DI LUCA MASSIMO(Cessata 注);现体: ML SOFTWARE S.R.L.(2009 登;4 人 €1.45M);SRL 现任具名未锁=半守档注;旧主名谱 Massimo Luca(ufficiocamerale 双体件)', 'https://www.ufficiocamerale.it/3625/ml-software-srl'),
     ev('联系方式与基础画像', 'Via Roccaromana 32/A, 95124 Catania;PEC mlsoftware@pec.mlsoftware.it;fatturato €1.450.338(2024);utile €242.806;62.20.1 IT 咨询;VoIP/备份/网管谱;MePA 供应商谱=公采守界注(amministrazionicomunali/crunchbase 件)', 'https://www.amministrazionicomunali.it/sicilia/catania/ml-software-s-r-l')],
    '意卡塔尼亚 17 年 IT 咨询铺(双体承接)', '4 人;2009 登',
    ('盈利稳谱+MePA 档', '现任具名缺半守档', '旧主名谱(差旗)', '区域链竞谱'),
    'Massimo Luca 位(差旗待核;opt-in 律;公采守界)', 'Gentile Sig. Luca,'))

R.append(rec('A-340', 'Net Engineering SpA',
    'Net Engineering Srl(档头 SpA 注;意大利 Milano/Sesto San Giovanni;**1991 创 35 年;51-200 人;电信/网络/布线/VoIP 集成**;**三异体分层注:net-e.it NET Engineering S.r.l.(Padova,1971,130 人 €15M,土木/水利工程,Furlan 父女)/Engineering SpA(Pandozy,意 IT 巨头)=各已排离;档对位=米兰电信体(netengineering.it)**;**LI 员工谱:Massimo Dell\'Avvocato(Responsabile Voice Department=语音部主管)+Emiliano Savorani(Wireless Network Engineer=无线工程师谱!)+Massimo Lodola(account manager)**',
    [("Massimo Dell'Avvocato", 'Responsabile Voice Department(语音部主管;LI 谱)', 'linkedin.com/company/net-engineering-srl', G, 'https://it.linkedin.com/company/net-engineering-srl'),
     ('Emiliano Savorani', 'Wireless Network Engineer(无线工程谱)', 'linkedin.com/company/net-engineering-srl', G, 'https://it.linkedin.com/company/net-engineering-srl')],
    [ev('决策链与对接人', "LI 员工谱: Massimo Dell'Avvocato(Responsabile Voice Department)+Emiliano Savorani(Wireless Network Engineer)+Massimo Lodola(account manager)+Nazario Trovalusci;**Padova 工程体/Engineering SpA 巨头=异体已分层**", 'https://it.linkedin.com/company/net-engineering-srl'),
     ev('联系方式与基础画像', 'Milano;founded 1991;51-200 dipendenti;Telecomunicazioni/Networking/Cabling/VoIP(netengineering.it;LI 件)', 'https://it.linkedin.com/company/net-engineering-srl')],
    '意米兰 35 年电信布线集成屋', '51-200 人;1991 创',
    ('电信/无线工程员工谱在', 'GF 具名未锁+异体噪', "Dell'Avvocato 语音部直达位", '区域链竞谱'),
    "Massimo Dell'Avvocato 位(opt-in 律)", 'Gentile Sig. Dell\'Avvocato,'))

R.append(rec('A-341', 'Securcrea Snc',
    'Securcrea(**现全称 Securcrea di Cianchi Michele & C. s.a.s.**;GDPR 页示 s.n.c. di Cianchi & Burgassi;意大利 Follonica(GR),Via Bicocchi 12, 58022;**P.IVA 01564970539;网安/IT 咨询(Kerio 10+ 年伙伴;20+ 年安全经验)**;**业主名谱: Michele Cianchi(全称具名=O 级)+Burgassi(合伙人姓谱;Editor Claudia Viale 页脚)**;服务:防火墙/邮件服务/man down/服务器供装/基础设施监控预障',
    [('Michele Cianchi', 'Socio 业主(全称具名 di Cianchi Michele & C.)', 'securcrea.com 页脚+GDPR 页(O)', O, 'http://www.securcrea.com/'),
     ('Burgassi(合伙姓谱)', 'Socio(s.n.c. di Cianchi & Burgassi GDPR 页)', 'securcrea.com GDPR 页', O, 'http://www.securcrea.com/informativa-sul-trattamento-dei-dati-personali-gdpr.html')],
    [ev('决策链与对接人', '©2022 Securcrea di **Cianchi Michele** & C. s.a.s.;GDPR 页: Titolare = Securcrea s.n.c. di Cianchi & Burgassi;Editor: Claudia Viale(官网页脚/隐私页)', 'http://www.securcrea.com/'),
     ev('联系方式与基础画像', 'Via Bicocchi 12, 58022 Follonica (GR);+39.0586.1713210;info@securcrea.com;P.IVA 01564970539;Kerio partner 10+ anni;sicurezza informatica 20+ anni;firewall/mail/man down server 谱(官网/atoka 件)', 'https://atoka.io/public/it/azienda/securcrea-di-cianchi-michele-c-sas/36820c2890d6')],
    '意格罗塞托 20+ 年网安小铺', '小铺谱',
    ('全称业主 O+Kerio 老伙伴谱', '小微谱', 'Cianchi 直达位', '区域链竞谱'),
    'Michele Cianchi 直达(opt-in 律)', 'Gentile Sig. Cianchi,',
    trend='2026-10-08 R66 22 波谱名牌(波 18 旧嵌升级)'))

R.append(rec('A-342', 'T.net S.p.A',
    'T.NET S.P.A.(意大利 Milano,Via Roberto Lepetit 8/10, 20124(+Via Caldera 21 Milano/Piazza del Popolo 18 Roma/Viale Africa 84 Catania 多址);**P.IVA 03979950874;REA MI2045456;2002-08-02 创;创新型 SME;€1.53M(2021);IoT/数字转型/智慧城市(smart farming/mobility/ITS)**;**President & CEO+创始人+大股东: Francesco Mazzola(官网股东页 O);Elisa Giacone: 共同创始人/董事/HR GM(AV Investment 唯一董事;官网 O)**;**股东谱:Quaenet Italia 27%(Ossama Bessada CEO 进 Cda)+Ignitus 增资+Natale Lia=国际化谱;EIT Digital 股权池谱(2018 加速器进)**',
    [('Francesco Mazzola', 'President & CEO/创始人/大股东(官网股东页自署)', 'tnet.it 股东页(O)', O, 'https://www.tnet.it/en/shareholders/'),
     ('Elisa Giacone', '共同创始人/Member of the Board/HR(官网股东页)', 'tnet.it 股东页(O)', O, 'https://www.tnet.it/en/shareholders/'),
     ('Ossama Bessada', 'CEO Quaenet(27% 股东方;Cda 新席)', 'zerounoweb/tnet.it 件', G, 'https://www.zerounoweb.it/iot/iot-tnet-mira-allinternazionalizzazione-quaenet-e-ignitus-entrano-in-cda/')],
    [ev('决策链与对接人', 'Shareholders 页: 「T.net is an innovative SME born in 2002 on the initiative of Elisa Giacone and Francesco Mazzola, the current President and CEO」;Giacone=Co-founder/Board/HR GM;Quaenet Italia 27%(tnet.it 官网)', 'https://www.tnet.it/en/shareholders/'),
     ev('联系方式与基础画像', 'P.IVA 03979950874;Via Roberto Lepetit 8/10, 20124 Milano;data inizio 02/08/2002;fatturato €1.526.727(2021);62.01 software;smart farming/mobility/ITS/smart city;**EIT Digital Equity Portfolio**;datacenter EU 分布谱(reportaziende/cbinsights/LI 件)', 'https://www.reportaziende.it/tnet_spa_mi_03979950874'),
     ev('近期动态与线索', '2024: Quaenet+Ignitus 进 Cda(Bessada+Natale Lia);增资+转 SpA;CEO Mazzola:「naturale evoluzione…EIT Digital」国际化谱(zerounoweb 件)', 'https://www.zerounoweb.it/iot/iot-tnet-mira-allinternazionalizzazione-quaenet-e-ignitus-entrano-in-cda/')],
    '意米兰 IoT 集成创新 SME(EIT 谱)', '中小谱;2002 创',
    ('创始双驾+Quaenet 国际化窗', 'IoT 专谱', 'Mazzola CEO 直达位', '资本链竞谱'),
    'Francesco Mazzola 直达(opt-in 律)', 'Gentile Sig. Mazzola,',
    trend='2026-10-08 R66 22 波谱名牌(Quaenet 增资窗)'))

R.append(rec('A-343', 'Techno Center S.p.A',
    'TECHNO CENTER S.P.A.(意大利 Roma,Via Gino Funaioli 54-56(新法址 Via Antonio Bertoloni 26B);**P.IVA 09319261005;2007-02-08 登;cap €250k;€7.89M(2018);集团 ~120 专才 UCC/VoIP/Networking/Sicurezza/IT;MePA 2024 供应商(网络设备/视频监控档=公采守界)**;**Co-Founder & Amministratore Delegato: Gianluca Zignani(LI 自署;**背景差旗:前意大利陆军通信学校教官(退役中尉)=军系人脉谱;2024-04 起 AD=新设换代窗;同名 COO 谱差旗注**)**;梯队 Adele Megna Sales Manager+Andrea Scacco Network&Delivery Specialist+Massimo de Persio Senior Presales;Consorzio Innovo 关联谱;**PAC/PAL 客户=军警公段守界注**',
    [('Gianluca Zignani', 'Co-Founder & Amministratore Delegato(2024-04 起;LI 自署)', 'linkedin.com/in/gianluca-zignani(O)', O, 'https://www.linkedin.com/in/gianluca-zignani-2528b5278/'),
     ('Adele Megna', 'Sales Manager(销售口)', 'rocketreach 谱面条', G, 'https://rocketreach.co/davide-rocco-email_230701799'),
     ('Massimo de Persio', 'Senior Presales(售前口)', 'rocketreach 谱面条', G, 'https://rocketreach.co/davide-rocco-email_230701799')],
    [ev('决策链与对接人', '「Attualmente è Co-Fiunder della Techno Center Spa e Amministratore Delegato, un Gruppo di imprese, System Integrator, che consta circa 120 risorse specializzate in UCC/Voip, Networking e Sicurezza」;**前 Esercito Italiano 通信教官(退役 Tenente)=军系谱注**(LI 自署)', 'https://www.linkedin.com/in/gianluca-zignani-2528b5278/'),
     ev('联系方式与基础画像', 'P.IVA 09319261005;Via Gino Funaioli 54-56, Roma;0662279692;2007 登;cap €250k;€7.89M(2018);62.09.09;MePA 供应商(Apparati di rete+Videosorveglianza 档)=公采守界;**PAC/PAL 客户谱=军警公段守界注**(amministrazionicomunali/bigprofiles 件)', 'https://www.amministrazionicomunali.it/lazio/roma/techno-center')],
    '意罗马 120 人系统集成集团(2024 换代窗)', '~120 人;2007 创',
    ('Co-Founder AD 新设窗+120 专才', '**军警公段守界注**', 'Zignani AD 直达位', '一线链竞谱'),
    'Gianluca Zignani AD 位(opt-in 律;PAC/PAL 守界)', 'Gentile Sig. Zignani,',
    trend='2026-10-08 R66 22 波谱名牌(2024 AD 新设窗)'))

R.append(rec('A-344', 'World Technology di Luigi Boi',
    'WORLD TECHNOLOGY DI LUIGI BOI(意大利 Cagliari,Via Montenero 15, 09122;**P.IVA 03196380921;Impresa Individuale 个体户;IT 咨询/软件开发**;**MePA 供应商 12 标段(Apparati di rete/Server/Infrastrutture ICT/Enterprise&Specialized/Licenze software/Sicurezza informatica/PC 外设/办公机/复印耗材=公采大户谱=守界注)**;业主 Luigi Boi(商号具名);070 2346452;无公开站点',
    [('Luigi Boi', 'Titolare(个体户业主;商号具名)', 'amministrazionicomunali/virgilio 件', G, 'https://www.amministrazionicomunali.it/sardegna/cagliari/world-technology-di-luigi-boi')],
    [ev('联系方式与基础画像', 'World Technology di Luigi Boi;P.IVA 03196380921;Via Montenero 15, 09122 Cagliari;070 2346452;Impresa Individuale;informatica consulenza e sviluppo software(amministrazionicomunali/virgilio 件)', 'https://www.amministrazionicomunali.it/sardegna/cagliari/world-technology-di-luigi-boi'),
     ev('采购与供应链信号', '**MePA 2024 供应商 12 标段全谱**(rete/server/ICT infra/software/sicurezza 等 abilitato 件)=公采守界档', 'https://www.amministrazionicomunali.it/sardegna/cagliari/world-technology-di-luigi-boi')],
    '意撒丁岛个体 IT 咨询铺(MePA 公采档)', '个体铺谱',
    ('MePA 12 标段=公采通道谱', '**公采守界注**', 'Boi 唯一直达位', '公采链竞谱'),
    'Luigi Boi 直达(opt-in 律;公采守界)', 'Gentile Sig. Boi,'))

R.append(rec('A-345', 'Avelution',
    'Avelution(荷兰 Schijndel/Veghel(北布拉班特);**2020 创;2-10 人;智能楼宇 OT 网络全包(OT-netwerk 设计/配置/交档/运维;sustainable+healthy+smart 数据驱动楼宇)**;**姊妹/母谱:RJ Networks & Security — Directeur & Eigenaar Roel Jansen(LI/RR 双源;avelution.nl 邮域同)**;+Bram Schats(Avelution Insights IoT 楼宇)+Jesper Pennings(Sales Manager RJ)+Dorinda Spierings;**楼宇 OT 网=守界注;p1=CONSULT-OEM 谱**',
    [('Roel Jansen', 'Directeur & Eigenaar RJ Networks & Security/Avelution 双牌(LI 自署)', 'linkedin.com/company/avelution', O, 'https://nl.linkedin.com/company/avelution'),
     ('Bram Schats', 'Avelution Insights/IoT 楼宇( Gebouwinzicht 谱)', 'linkedin.com/company/avelution', G, 'https://nl.linkedin.com/company/avelution'),
     ('Jesper Pennings', 'Sales Manager(RJ 谱)', 'rocketreach 谱面条', G, 'https://rocketreach.co/rj-networks-security-profile_b454c98bfc93304f')],
    [ev('决策链与对接人', '「Roel Jansen Directeur RJ Networks & Security Everything Connected」(LI Avelution 员工谱);RR: Roel Jansen Directeur and Eigenaar+Bram Schats(Avelution)+Jesper Pennings Sales Manager', 'https://nl.linkedin.com/company/avelution'),
     ev('联系方式与基础画像', 'Schijndel;opgericht 2020;2-10 medewerkers;**Avelution neemt het OT-netwerk volledig uit handen: ontwerp/configuratie/opleverdossier/beheer**;smart building ready(avelution.nl/LI 件)', 'https://avelution.nl/netwerkarchitectuur-en-connectiviteit/')],
    '荷布拉班特 2020 创楼宇 OT 网全包铺', '2-10 人;2020 创',
    ('楼宇 OT-backbone 专营=强契', '**楼宇 OT 守界注**', 'Jansen 双牌直达位', '区域链竞谱'),
    'Roel Jansen 直达(opt-in 律;OT 守界)', 'Geachte heer Jansen,'))

R.append(rec('A-346', 'Kappa Data Nederland',
    'Kappa Data Nederland(=Kappa Data Group 荷兰分支;**Atoomweg 63, 3542 AA Utrecht;+31 88 52772 00;sales@kappadata.nl**;集团:1997/1998 创 De Pinte;40-50 人;Benelux 网络/安全/IoT VAD 分销;2021-11 收 Exer 进法国;€100M 目标;PE-backed 谱);**CEO Kappa Data Group: Patrick Casteels(官网团队页 O;波 18 谱:InvestLink 后股比 22%→35% 唯一 CEO)**;**Chris Willems: Managing Partner(2021 法国扩张新闻稿引语 O;前 Co-CEO→M&A 主责谱)**',
    [('Patrick Casteels', 'CEO Kappa Data Group(官网团队页自署)', 'kappadata.be 团队页(O)', O, 'https://www.kappadata.be/ons-bedrijf/ons-team/'),
     ('Chris Willems', 'Managing Partner(2021 扩法新闻稿引语)', 'kappadata.be 新闻稿 PDF(O)', O, 'https://www.kappadata.be/wp-content/uploads/2021/11/Persbericht-NL-Kappa-Data-breidt-uit-naar-Frankrijk.pdf')],
    [ev('决策链与对接人', '「Patrick Casteels — CEO Kappa Data Group」(官网团队页);「Chris Willems, Managing Partner Kappa Data」(2021-11 法国扩张新闻稿引语;集团 €100M 目标)', 'https://www.kappadata.be/ons-bedrijf/ons-team/'),
     ev('联系方式与基础画像', 'Netherlands: Atoomweg 63, 3542 AA Utrecht;+31 88 52772 00;sales@kappadata.nl;集团 HQ Grote Steenweg 18, 9840 De Pinte(BE);founded 1997;network/security/IoT VAD;France 2021 扩张谱(kappadata.be 新闻稿/runzero 件)', 'https://www.runzero.com/partner-directory/kappa-data/')],
    '荷乌得勒支 Kappa NL 分支(集团谱)', '集团 40-50 人',
    ('集团 CEO/MP 官网 O 双谱', '分支体谱', 'Casteels/Willems 集团位', '一线链竞谱'),
    'Patrick Casteels+Chris Willems 位(opt-in 律)', 'Geachte heer Casteels,',
    trend='2026-10-08 R66 22 波谱名牌(波 1/18 谱升级对齐)'))

R.append(rec('A-347', 'Kappa Data Belgium',
    'Kappa Data Belgium(=**Kappa Data Group 原生总部**;比利时 De Pinte,Grote Steenweg 18, 9840;+32 9 243 42 10;sales@/info@kappadata.be;**1997 创 29 年;40-50 人;Benelux VAD 原生谱;pitchbook: PE-Backed**);**CEO Group: Patrick Casteels(官网团队页 O)**;**Chris Willems: Managing Partner(2021 扩法稿引语;M&A 主责谱)**;Koert Martens 技术总监谱(波 18 档);Michel Grunspan(Exer CEO,集团管理增补谱)',
    [('Patrick Casteels', 'CEO Kappa Data Group(官网团队页自署)', 'kappadata.be 团队页(O)', O, 'https://www.kappadata.be/ons-bedrijf/ons-team/'),
     ('Chris Willems', 'Managing Partner(扩法新闻稿引语)', 'kappadata.be 新闻稿 PDF(O)', O, 'https://www.kappadata.be/wp-content/uploads/2021/11/Persbericht-NL-Kappa-Data-breidt-uit-naar-Frankrijk.pdf')],
    [ev('决策链与对接人', '官网团队页: Patrick Casteels CEO Kappa Data Group;新闻稿: Chris Willems Managing Partner(「sterke positie op de Franse markt…€100 miljoen」)', 'https://www.kappadata.be/ons-bedrijf/ons-team/'),
     ev('联系方式与基础画像', 'HQ: Grote Steenweg 18, 9840 De Pinte;+32 (0)9 243 42 10;info@kappadata.be;founded 1997;40 total employees(pitchbook);Unattributed VC/PE-Backed 谱;IT infra/security/IoT 分销+培训/活动谱(cbinsights/pitchbook/runzero 件)', 'https://pitchbook.com/profiles/company/484207-66')],
    '比 De Pinte Kappa 原生总部(PE 谱)', '40-50 人;1997 创',
    ('原生总部+VAD 培训谱=件链窗', 'PE 资本谱', 'Casteels/Willems 直达位', '一线链竞谱'),
    'Patrick Casteels 直达(opt-in 律)', 'Geachte heer Casteels,'))

R.append(rec('A-348', 'nLogic',
    'NLOGIC AS(挪威 Oslo(Skøyen),Karenslyst allé 20, 0278;**Org.nr 821 678 102;2018-09-25 创体(史谱 2007:挪威头部 IT 司资深人创办;NSN(网络/安全/数据中心)增值集成+咨询);46-49 人; aksjekapital 800k**;**Daglig leder: Erlend Bonesvoll(1968 生,兼 Styremedlem;1881/proff/gulesider 三源 O)**;**Styrets leder: Arne Giæver(1970 生)**;Styremedlem Marcus Erik Wahlberg;**股东:Nlogic Group AS(68%)+Nlogic Invest AS(32%;Group 832305332=2023-10 集团化谱)**;Nlogic Group 同 Bonesvoll 任 DL',
    [('Erlend Bonesvoll', 'Daglig leder(CEO;三源登记+1881 谱)', 'proff.no 登记件', O, 'https://www.proff.no/selskap/nlogic-as/oslo/it-konsulenter-og-r%C3%A5dgivning/IDL7EVQ03DC'),
     ('Arne Giæver', 'Styrets leder(董事长)', '1881.no/proff.no 件', O, 'https://www.1881.no/konsulenter-system-og-programvare/konsulenter-system-og-programvare-oslo/konsulenter-system-og-programvare-skoeyen/nlogic-as_106343012S1/'),
     ('Marcus Erik Wahlberg', 'Styremedlem(董事)', '1881.no 件', O, 'https://www.1881.no/konsulenter-system-og-programvare/konsulenter-system-og-programvare-oslo/konsulenter-system-og-programvare-skoeyen/nlogic-as_106343012S1/')],
    [ev('决策链与对接人', 'Daglig leder: Erlend Bonesvoll(f 1968);Styrets leder: Arne Giæver(f 1970);Styremedlem: Bonesvoll+Marcus Erik Wahlberg;Aksjonærer: Nlogic Group AS(68%)+Nlogic Invest AS(32%)(1881/proff 件)', 'https://www.1881.no/konsulenter-system-og-programvare/konsulenter-system-og-programvare-oslo/konsulenter-system-og-programvare-skoeyen/nlogic-as_106343012S1/'),
     ev('联系方式与基础画像', 'Org.nr 821 678 102;Karenslyst allé 20, 0278 Oslo;406 18 888;stiftet 25.09.2018;46-49 ansatte;**15+ 年网络/安全/数据中心谱(「vi har i mer enn 15 år vært med på å bygge nettverksinfrastruktur i Norge」)**(1881/proff 件)', 'https://www.proff.no/selskap/nlogic-as/oslo/it-konsulenter-og-r%C3%A5dgivning/IDL7EVQ03DC')],
    '挪奥斯陆 15+ 年网安/DC 集成屋', '46-49 人;2018 创体',
    ('DL+董事长双 O 登记谱', '集团化 2023 窗', 'Bonesvoll 直达位', '一线链竞谱'),
    'Erlend Bonesvoll+Arne Giæver 位(opt-in 律)', 'Dear Mr. Bonesvoll,'))

R.append(rec('A-349', 'C2F Copper2Fiber',
    'Copper2Fiber – Soluções de Conectividade, Lda(葡萄牙 Barcarena(里斯本),R. Comendador Álvaro Vilela 19, Tercena, 2730-051;**2013-10 创 13 年;3 人 $6.9M;电信分销 B2B 专营(end-to-end 方案)**;**Bruno Formiga: Dep. Logístico/Comercial(2014-01 起 11 年=物流/商务件链口 KPI,LI 自署)**;官网无决策人具名',
    [('Bruno Formiga', 'Dep. Logístico/Comercial(物流商务口 KPI;LI 自署)', 'linkedin.com/in/bruno-formiga 件', G, 'https://www.linkedin.com/in/bruno-formiga-0b18261aa/')],
    [ev('决策链与对接人', 'LI: Bruno Formiga — Dep. Logistico/Comercial na COPPER2FIBER(jan 2014 - present, 11 anos)(LI 自署);决策人谱面未具名=守界注', 'https://www.linkedin.com/in/bruno-formiga-0b18261aa/'),
     ev('联系方式与基础画像', 'R. Comendador Álvaro Vilela 19, Tercena, 2730-051 Barcarena;criada Outubro 2013;distribuição soluções telecomunicações mercado profissional;3 employees;$6.9M(官网/RR 件)', 'https://www.c2f.pt/')],
    '葡里斯本 13 年电信分销微铺', '3 人;2013 创',
    ('物流/商务口 11 年老员=件链 KPI', '微实体谱;决策人缺', 'Formiga 口(G 谱)', '区域链竞谱'),
    'Bruno Formiga 位(opt-in 律)', 'Estimado Sr. Formiga,'))

R.append(rec('A-350', 'Landatel',
    'LANDATEL COMUNICACIONES S.L.(西班牙 Madrid(Alcorcón/旧 Getafe Río Odiel 14);**2001/2002 创 25 年;37 人;€25.5M;70+ 国电商谱(landashop/landamex);Landatel de México 2012=拉美门谱;**Ubiquiti/MikroTik 欧洲销冠+Cambium/TP-Link/Radwin 官方**;Netonix 谱档**;**Founder&CEO&BD Manager: Manuel Arroyo(Cepyme500 专访+PRNewswire 引语+contactout manuel@landatel.com 多源 O)**;**差旗注:RocketReach 条「Empresa cerrada en 2026 tras 25 años」=关铺孤证差旗,官网/工商活档为准待核**',
    [('Manuel Arroyo', 'Founder/CEO/Business Development Manager(专访+引语多源 O)', 'cepyme500 专访+contactout 件', O, 'https://www.cepyme500.com/entrevista/manuel-arroyo')],
    [ev('决策链与对接人', '「Manuel Arroyo is the Founder, Chief Executive Officer and Business Development Manager」(rocketreach/contactout:「email manuel@landatel.com」);Cepyme500 专访+PRNewswire 2015 件引语「comenta Manuel Arroyo, CEO de Landatel」', 'https://contactout.com/company/Landatel-Comunicaciones-36551'),
     ev('联系方式与基础画像', 'Calle Cenicientos 15, 28925 Alcorcón (Madrid);911 461 700;info@/marketing@landatel.com;70+ países e-commerce 谱;37 empleados;€25.535.036;founded 2001/2002;Landatel de México SA de CV(2012)(cepyme500/guiacanaltic/prnewswire 件)', 'https://guiacanaltic.channelpartner.es/landatel-comunicaciones/'),
     ev('近期动态与线索', '**RR 差旗:「Empresa cerrada en 2026 tras 25 años de actividad」=关铺孤证,官网活档,差旗待核**;MikroTik/Ubiquiti 欧销冠;Teltonika/Netonix 牌谱(rocketreach 件)', 'https://rocketreach.co/landatel-comunicaciones-profile_b5e0f8a3f42e69b4')],
    '西马德里 25 年无线件分销大户(70 国)', '37 人;€25.5M',
    ('€25.5M+70 国电商=件链大户', '关铺差旗注(孤证)', 'Arroyo CEO 直邮直达位', '一线链竞谱'),
    'Manuel Arroyo 直邮直达(opt-in 律;关铺差旗待核)', 'Estimado Sr. Arroyo,',
    trend='2026-10-08 R66 22 波谱名牌(关铺差旗注)'))

R.append(rec('A-351', 'meconet',
    'meconet e.K.(德国 Siegen(北威),Eiserntalstraße 133, 57080(旧 Kreuztal Bottenbacher Str. 78);**HRA 8315 Amtsgericht Siegen;专业网络方案商(企业/大学/酒店/网络运营商;IT 咨询+硬软件贸易)**;**Inhaber(业主): Lutz-Martin Kleemann(webvalid 登记件)**;**异体分层注:Meconet Deutschland GmbH(慕尼黑,HRB285802,金属冲压制造,GF Markku Kuismin+Tomi Parmasuo;芬兰 Meconet Oy 集团)=与 meconet.de 网络体不同,已分层**',
    [('Lutz-Martin Kleemann', 'Inhaber(业主;HRA 8315 登记件)', 'webvalid 登记件', O, 'https://www.webvalid.de/company/meconet+e.K.,+Siegen/HRA+8315')],
    [ev('决策链与对接人', 'HRA 8315: Inhaber: Kleemann, Lutz-Martin(Kreuztal);positioniert als Lösungsanbieter für professionelle Anwender, Firmen, Universitäten, Hotels und Netzbetreiber(webvalid 件)', 'https://www.webvalid.de/company/meconet+e.K.,+Siegen/HRA+8315'),
     ev('联系方式与基础画像', 'Eiserntalstraße 133, 57080 Siegen;IT-Beratung+Handel/Vertrieb Hard- und Software;**异体: Meconet Deutschland GmbH München(金属件,芬兰 Meconet Oy 系)=已分层**(webvalid/northdata 件)', 'https://www.northdata.com/Meconet+Deutschland+GmbH,+M%C3%BCnchen/HRB+285802')],
    '德锡根专业网络方案商(单业主谱)', '小铺谱',
    ('单业主登记件=直达', '小异体噪已分层', 'Kleemann 直达位', '区域链竞谱'),
    'Lutz-Martin Kleemann 直达(opt-in 律)', 'Guten Tag Herr Kleemann,'))

R.append(rec('A-352', 'MHz Shop',
    'MHz Shop(=**Megahertz Wireless Group EURL**;法国 Marquixanes(东比利牛斯 66),5 Avenue Roger Roquefort, 66320;**SIRET 484713052;cap €118,000;2005 创 21 年;WiFi/WiMAX/UMTS/GSM 无线电件网店专营**;**Gérant/创始人: Daniel Doguet(业余无线电 F4AKQ;Active+ Software 创主谱;官网 Qui sommes-nous 自署+mentions légales 印谱双 O!)**;Printemps du WiFi 乡区活动谱',
    [('Daniel Doguet', 'Gérant/创始人(官网自署+印谱+kompass 三源)', 'mhzshop.com 官网(O)', O, 'https://www.mhzshop.com/Qui-sommes-nous/')],
    [ev('决策链与对接人', '「Megahertz Wireless est le fruit de la réflexion d\'un jeune créateur d\'entreprise, **Daniel Doguet**…radioamateur licencié (F4AKQ)…fondateur d\'Active+ Software」;Mentions légales: Directeur de la publication: Daniel Doguet(官网自署)', 'https://www.mhzshop.com/Qui-sommes-nous/'),
     ev('联系方式与基础画像', 'Megahertz Wireless Group EURL;capital €118.000;484.713.052 RCS Perpignan;5 avenue Roger Roquefort, 66320 Marquixanes;depuis 2005;WiFi antennas 2.4/5GHz/radio 专营网店(mhzshop.com 印谱/kompass 件)', 'https://www.mhzshop.com/Mentions-legales/')],
    '法国南乡 21 年无线电件网店(创主谱)', '小微谱;2005 创',
    ('印谱创主直达+业余电谱', '微实体谱', 'Doguet 直达位', '区域链竞谱'),
    'Daniel Doguet 直达(opt-in 律)', 'Monsieur Doguet,'))

R.append(rec('A-353', 'ELMAT',
    'ELMAT S.p.A.(意大利 Padova,Via Uruguay 15, 35127(+Roma 点);**1997 创 29 年;21-30 人;Cabling&Networking 分销(Video/Voice/Cabling/Networking/Energy/AV/Wireless;**Aruba WLAN Enterprise 专谱**;Netonix 谱档)**;**升谱: Michele Scapolo=Amministratore delegato(旧档 Responsabile Commerciale 升;RR 谱)+Andrea Rizzo=Co-CEO(旧档 marketing 升;RR 谱)**;**Pierpaolo Amadori Direttore commerciale(商总=件链 KPI)+Sara Viola Product Management+Maurizio Madeo Responsabile Area**;elmat@elmat.com;选品策展「explorers」+活动/培训谱',
    [('Michele Scapolo', 'Amministratore delegato(AD 升谱)', 'rocketreach 谱面条', G, 'https://rocketreach.co/elmat-spa-profile_b4435394fa04d7bd'),
     ('Andrea Rizzo', 'Co-CEO(联席 CEO 升谱)', 'rocketreach 谱面条', G, 'https://rocketreach.co/elmat-spa-profile_b4435394fa04d7bd'),
     ('Pierpaolo Amadori', 'Direttore commerciale(商务总监=件链 KPI)', 'rocketreach 谱面条', G, 'https://rocketreach.co/elmat-spa-profile_b4435394fa04d7bd'),
     ('Sara Viola', 'Product Management(产品经理)', 'rocketreach 谱面条', G, 'https://rocketreach.co/elmat-spa-profile_b4435394fa04d7bd')],
    [ev('决策链与对接人', 'RR 谱: Michele Scapolo Amministratore delegato+Andrea Rizzo Co-Ceo+Pierpaolo Amadori Direttore commerciale+Sara Viola Product Management(TradeManager 旧档: Scapolo=Responsabile Commerciale/Rizzo=marketing=升谱注)', 'https://rocketreach.co/elmat-spa-profile_b4435394fa04d7bd'),
     ev('联系方式与基础画像', 'Via Uruguay 15, 35127 Padova;049 7623011;elmat@elmat.com;sul mercato del Cabling&Networking dal 1997;**Aruba 专谱(WLAN Enterprise)**;21-30 dipendenti;wisp/system integrator/installatori 客群(smau/官网/X 件)', 'https://www.smau.it/padova/2011/partners/elmat')],
    '意帕多瓦 29 年布线网络分销(Aruba 专)', '21-30 人;1997 创',
    ('AD+Co-CEO 双升谱+商总 KPI', '牌链专谱', 'Scapolo/Rizzo/Amadori 直达位', 'Aruba 链竞谱'),
    'Scapolo AD+Amadori 商总位(opt-in 律)', 'Gentile Sig. Scapolo,'))

R.append(rec('A-354', 'NTS Direct',
    'NTS Direct, Inc.(美国 Bolton, MA 01740,41 Main St;**1990 创 36 年;25-31 人;$8.8M;通信转售/硬件分销(NAICS 517911);$150k funding 谱;**Teltonika 授权档**;paragonnt.com 关联谱**;**Michael P. Prefontaine: Chief Executive Officer and President(D&B Key Principal+zoominfo+buzzfile 三源)**;**Ammar Rezek: President(RR/contactout/zoominfo 双头谱差旗注)**;Chris Turcotte 决策人谱',
    [('Michael P. Prefontaine', 'CEO & President(D&B Key Principal 三源)', 'dnb.com 件', O, 'https://www.dnb.com/business-directory/company-profiles.nts_direct_inc.cf28835b4c01f9c9c299defe093a9cc4.html'),
     ('Ammar Rezek', 'President(双头谱差旗注)', 'contactout/rocketreach 件', G, 'https://contactout.com/company/NTSDirect-7160')],
    [ev('决策链与对接人', 'Key Principal: Michael P Prefontaine, Chief Executive Officer and President(D&B);**Ammar Rezek President(RR/contactout)=双头谱差旗注**;decision makers: Chris Turcotte 等', 'https://www.zoominfo.com/c/nts-direct/347616523'),
     ev('联系方式与基础画像', '41 Main St, Bolton, MA 01740;(508) 656-1070/(877) 483-5393;shop.ntsdirect.com;founded 1990;25-31 employees;$8.8M revenue;Telecommunications 转售/分销;Teltonika 授权档(dnb/buzzfile/RR 件)', 'https://www.buzzfile.com/business/NTS-Direct,-Inc.-508-656-1070')],
    '美麻省 36 年通信硬分销商', '25-31 人;1990 创',
    ('CEO+President 双具名', '双头差旗注', 'Prefontaine CEO 直达位', '一线链竞谱'),
    'Prefontaine CEO 位(opt-in 律)', 'Dear Mr. Prefontaine,'))

R.append(rec('A-357', 'Digital Sima S.A',
    'DIGITAL SIMA S.A.(=ΝΤΙΤΖΙΤΑΛ ΣΙΜΑ;希腊 Athens(Neos Kosmos),Ilia Iliou 54, 11744;**1988 创 38 年;16-37 人;$1-5M;计算机/网络安全设备贸易(SA)**;**Chairperson/CEO: Dimitrios Konstantinos Stefanopoulos(D&B+contactout 双源 O-ish;dstef@digitalsima.gr)**;**ACCI 商会联络 jnikor@digitalsima.gr**;梯队 Dimitris Kandil Senior Network Engineer+Sotiris Sarantos Sales Engineer+John Daskalopoulos Security Solutions Supervisor+Charalampos Tassis Cloud;**WatchGuard NDR/FireCloud 技术会谱(LI)=网安专营**',
    [('Dimitrios Konstantinos Stefanopoulos', 'Chairperson/CEO(D&B+contactout 双源)', 'dnb.com 件', O, 'https://www.dnb.com/business-directory/company-profiles/digital-sima-sa.f916400d99c26f10e9a584fdf29a08b7'),
     ('Dimitris Kandil', 'Senior Network Engineer(高级网络工程师谱)', 'rocketreach 谱面条', G, 'https://rocketreach.co/digital-sima-sa-profile_b443ea94fddad9fd'),
     ('Sotiris Sarantos', 'Sales Engineer(售前/销售工程)', 'linkedin.com/in/sotirissarantos', G, 'https://www.linkedin.com/in/sotirissarantos/')],
    [ev('决策链与对接人', 'Key Principal/Chairperson: Dimitrios Konstantinos Stefanopoulos(D&B);CEO email dstef@digitalsima.gr(contactout);员工谱: Kandil(Sr Network Engineer)+Sarantos(Sales Engineer;WatchGuard NDR 会)', 'https://www.dnb.com/business-directory/company-profiles/digital-sima-sa.f916400d99c26f10e9a584fdf29a08b7'),
     ev('联系方式与基础画像', 'Ilia Iliou 54, 11744 Athens;+30 2109010401;ACCI 联络 jnikor@digitalsima.gr;founded 1988;16-37 employees;Computer and Network Security 贸易;WatchGuard NDR/FireCloud 组合谱(dnb/acci/RR/LI 件)', 'https://directory.acci.gr/companies/details/259103')],
    '希雅典 38 年网安件贸易屋', '16-37 人;1988 创',
    ('D&B Chairperson 具名+商会箱=双直达', '网安专营谱', 'Stefanopoulos CEO 直达位', '一线链竞谱'),
    'Stefanopoulos CEO 位(opt-in 律)', 'Dear Mr. Stefanopoulos,',
    trend='2026-10-08 R66 22 波谱名牌(希腊首拓)'))

R.append(rec('A-358', 'LEXIS S.A',
    'LEXIS ΠΛΗΡΟΦΟΡΙΚΗ Α.Ε.(希腊 Gerakas(阿提卡),Κλεισθένους 401, 15344(法定 Καρπάθου 2-4 & Εθν. Αντιστάσεως)+Thessaloniki 分社(Μαυρομιχάλη 32);**电信网研究+集成老牌(vres:「 από τις πιο πεπειραμένες」);Cyber Security/VPN/有无线电信网/VoIP/UPS 专营;Fortinet FortiGate 谱**;**Υπεύθυνος/Γενικός Διευθυντής(总经理): Theodoros Filopoulos(ΦΙΛΟΠΟΥΛΟΣ ΘΕΟΔΩΡΟΣ;vres.gr 名录件)**;+30 210 6777007;lexis@lexis.gr',
    [('Theodoros Filopoulos(Θεόδωρος Φιλόπουλος)', 'Γενικός Διευθυντής(总经理;希腊名录件)', 'vres.gr 名录件', G, 'https://www.vres.gr/lexis-pliroforiki-ae')],
    [ev('决策链与对接人', 'Υπεύθυνος: ΓΕΝΙΚΟΣ ΔΙΕΥΘΥΝΤΗΣ **ΦΙΛΟΠΟΥΛΟΣ ΘΕΟΔΩΡΟΣ**(vres.gr 希腊工商名录件)', 'https://www.vres.gr/lexis-pliroforiki-ae'),
     ev('联系方式与基础画像', 'Head Office: Κλεισθένους 401, 15344 Γέρακας;+30 210 6777007;lexis@lexis.gr;分社 Θεσσαλονίκη;lexis.gr: Cyber Security/VPN/wired&wireless telecom networks/VoIP/UPS;Fortinet FortiGate 系列谱(lexis.gr 官网 GDPR/contactus 件)', 'https://www.lexis.gr/en/gdpr')],
    '希雅典近郊电信网集成老牌屋', '中小谱',
    ('总经理名录具名=直达', '牌链专谱', 'Filopoulos 直达位', '区域链竞谱'),
    'Theodoros Filopoulos 直达(opt-in 律)', 'Dear Mr. Filopoulos,'))

R.append(rec('A-363', 'SOS electronic',
    'SOS electronic s.r.o.(斯洛伐克 Košice,Pri prachárni 16, 040 11;**IČO 31703186;IČ DPH SK2020484158;1991/1995 创 30+ 年;68-88 人;$22.12M;工业电子元件分销(Lantronix/Traco Power/Wago/Euroclamp/TechNexion 等嵌件牌谱)**;**CEO|Konateľ: Ing. Ján Seszták(官网 Kontakty 页自署 j.sesztak@sos.sk=O 金谱)**;**官网梯队全谱:Ján Michalko 国际商务经理(件链 KPI)+Branislav Kňazovický 营销+Ladislav Rybár IT+Mária Sesztáková HR(族谱)+Ladislav Horvat 技商(东斯区)**;D&B: Renáta Tančaková FD;**2020「最佳分销商」奖+Conrad Electronic M&A 谱**;Hirschmann 授权档',
    [('Ing. Ján Seszták', 'CEO/Konateľ(官网联络页自署邮箱)', 'soselectronic.com Kontakty(O)', O, 'https://www.soselectronic.com/sk-sk/kontakty'),
     ('Ing. Ján Michalko', 'Medzinárodný obchodný manažér(国际商务经理=件链 KPI)', 'soselectronic.com Kontakty(O)', O, 'https://www.soselectronic.com/sk-sk/kontakty'),
     ('Branislav Kňazovický', 'Manažér marketingového oddelenia(营销经理)', 'soselectronic.com Kontakty(O)', O, 'https://www.soselectronic.com/sk-sk/kontakty'),
     ('Renáta Tančaková', 'Financial Director(D&B 谱)', 'dnb.com 件', G, 'https://www.dnb.com/business-directory/company-profiles.sos_electronic_sro.2bbfecf5afc6341343f4aac3b94d9fcd.html')],
    [ev('决策链与对接人', '官网 Kontakty: **CEO | Konateľ Ing. Ján Seszták j.sesztak@sos.sk**+Ing. Ján Michalko(Medzinárodný obchodný manažér)+Mária Sesztáková(HR)+Branislav Kňazovický(marketing)+Ladislav Rybár(IT)+Ladislav Horvat(tech-obch 东斯)', 'https://www.soselectronic.com/sk-sk/kontakty'),
     ev('联系方式与基础画像', 'IČO 31703186;Pri prachárni 16, 040 11 Košice;+421-557860416;68 employees;$22.12M(dnb);founded 1991/1995;electronic components distributor(industrial/embedded/IoT)(dnb/官网件)', 'https://www.dnb.com/business-directory/company-profiles.sos_electronic_sro.2bbfecf5afc6341343f4aac3b94d9fcd.html'),
     ev('近期动态与线索', '2020「Najlepší distribútor」奖(Electronic Assembly 件);**Conrad Electronic International M&A 谱(pitchbook Acquired)**;TechNexion:「kľúčový distribútor pre embedded systémy vo východnej Európe」', 'https://sos.sk/referencie-o-nas')],
    '斯洛伐克科希策 30+ 年电子元件分销', '68-88 人;$22M',
    ('CEO 官网自署+梯队全谱=O 金谱', 'Conrad 并购谱注', 'Seszták+Michalko 国际线直达位', '一线链竞谱'),
    'Ján Seszták+Ján Michalko 位(opt-in 律)', 'Vážený pán Seszták,',
    trend='2026-10-08 R66 22 波谱名牌(斯洛伐克首拓)'))

R.append(rec('A-365', 'Nexus Networks',
    'Nexus Networks(马耳他 Zebbiegh,199 Triq Sir Temi Zammit;**1-10 人;nexus.com.mt;+356 27220337**;**档谱:MikroTik 官方分销(马耳他)=MT 自家链唯一档!**;谱面检索未锁具名决策人(美/印/英同名异体已分层)→**守档准由:MikroTik 官方马耳他谱在档,具名待专批(nexus.com.mt Whois/站点页)**',
    [],
    [ev('决策链与对接人', '公开谱面未锁具名决策人=守档准由;Nexus Networks Malta(zoominfo 件;1-10 人);**档谱 MikroTik 官方分销**(2026-10-08 R66 22 波留痕)', 'https://www.zoominfo.com/c/nexus-networks/467685148'),
     ev('联系方式与基础画像', '199 Triq Sir Temi Zammit, Zebbiegh, Malta;+356 27220337;nexus.com.mt;**MikroTik 官方马耳他谱(自家链 KPI)**', 'https://www.nexus.com.mt')],
    '马耳他 MikroTik 官方谱(具名缺)', '1-10 人',
    ('MT 官方马耳他唯一点=链窗', '具名缺守档', '无守档', '—'),
    '守档:MT 官方谱在档,具名待专批', 'Dear Sir or Madam,',
    trend='2026-10-08 R66 22 波谱名牌(MT 官方谱)'))

R.append(rec('A-373', 'Network Devices Inc',
    'Network Devices Inc.(美国 Sugar Land, TX 77478,3134 Amesbury Ct;**2014 创 12 年;「fastest-growing」网络硬件现货转售;**10,000+ 客户/50+ 国;$10M 现货库存(NJ+TX 双仓);Cisco C1000 等大牌现货谱;独立 IT 硬件零售分销**;**Mathew Cohen: Managing Director(rocketreach 件 G)**;sales@networkdevicesinc.com;+1 201-559-1474;**错峰注:A-369 档「与 A-373 同人错峰主发」=关联谱照抄,错峰免同日双发**',
    [('Mathew Cohen', 'Managing Director(RR 谱面条)', 'rocketreach 谱面条', G, 'https://rocketreach.co/network-devices-inc-profile_b45d9376fc6069ee')],
    [ev('决策链与对接人', 'Mathew Cohen is the Managing Director of Network Devices Inc(rocketreach 件);**错峰注:与 A-369 同人错峰主发(ARCH 档注照抄)**', 'https://rocketreach.co/network-devices-inc-profile_b45d9376fc6069ee'),
     ev('联系方式与基础画像', '3134 Amesbury Ct, Sugar Land, TX 77478;+1 201-559-1474;sales@networkdevicesinc.com;founded 2014;10,000+ customers in 50+ countries;**$10M in-stock(NJ+TX warehouses)**;factory-sealed Cisco 谱(networkdevicesinc.com/RR/X 件)', 'https://networkdevicesinc.com/pages/about-us')],
    '美德州 12 年硬件现货转售铺(50 国)', '小微谱;$10M 库存',
    ('现货库存+50 国客=件链铺', 'RR 单具名', 'Cohen MD 直达位', '一线现货链竞谱'),
    'Mathew Cohen 直达(opt-in 律;错峰注)', 'Dear Mathew,',
    trend='2026-10-08 R66 22 波谱名牌(错峰注)'))

# ============ 人名司名同体培训谱档×21(东欧/巴尔干/波罗的海新领土) ============
def person(code, name, city, web, p1, why, extra, sal):
    kb = '**%s(MikroTik 认证培训师/顾问 本人谱位,档谱官网自署,%s)' % (name, O) + '**'
    if not web.startswith('http') and __import__('re').match(r'^[\w.-]+\.[a-zA-Z]{2,}$', web):
        web = 'https://' + web
    src = web if web.startswith('http') else '仓内 profile/A/%s-*(R54/R66 档谱基础画像行)' % code
    return rec(code, name,
        '%s(%s;**【人名司名同体=CSV 公司名即本人谱位,official-self-published 级金谱】**;类型: 集成商/顾问(MikroTik 认证);培训交付谱;档站 %s;%s)' % (name, city, web, extra),
        [(name, 'MikroTik 认证培训师/顾问(档谱:CSV 公司名字段即本人)', '档谱+档站自署', O, src)],
        [ev('联系方式与基础画像', '国家/城市: %s;网站: %s;类型: 集成商/顾问(MikroTik 认证)(档案基础画像行=事实)', src),
         ev('近期动态与线索', '档定首触角: %s' % p1, src),
         ev('目标行业与场景', '档定值得跟: %s' % why, src)],
        '培训交付谱(MTCSWE 谱链)', '单铺/工作室谱',
        ('MTCSWE/交换认证谱=对口窗', '单铺谱', '%s 本人直达位' % name, 'MikroTik 官方课链'),
        sal + '(opt-in 律)',
        sal)

WHY1 = '有明确交换/供电需求(交换专长 MTCSWE),且有具体人直联'
WHY2 = '【人工定级】A——自动规则已跳过(档注)'
R.append(person('A-355', 'Ahababian V', '乌克兰／Kyiv', 'https://www.mikrotikls.com.ua',
    '顾问对照单元;**民用商业限定前句**;—(合作探询,无量产报价);**p1=CONSULT-OEM 谱**', WHY1,
    'mikrotikls.com.ua=乌克兰 MikroTik 学习站官方域谱;**战区民用商业限定守界句**', 'Dear Sir,'))
R.append(person('A-356', 'Pournaras Athanasios', '希腊／Αθήνα', 'https://www.xpatit.gr',
    '店目录替补对照行正口($180 锚点一致)', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'xpatit.gr=希腊 IT 件店谱', 'Dear Mr. Pournaras,'))
R.append(person('A-359', 'Scornici Vadim', '乌克兰／Kyiv', 'https://mikrotik.coach',
    'MTCSWE 课堂旁对照行;**民用商业限定前句;Telegram 主渠道注**;—(合作探询,无量产报价);**p1=CONSULT-OEM 谱**', WHY1,
    'mikrotik.coach=本人教练品牌域谱;**战区民用限定+Telegram 主渠道注**', 'Dear Vadim,'))
R.append(person('A-360', 'Andrii Sychov', '乌克兰／Kyiv', 'http://www.mikrotik.net.ua/',
    '**建档供位;触发=站恢复+MX 复核**;—(合作探询,无量产报价)', '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联',
    'mikrotik.net.ua=乌克兰 MikroTik 门户谱(站态待复核);**建档供位待站恢复+MX 复核触发**', 'Dear Andrii,'))
R.append(person('A-361', 'Michal Dobšovič', '斯洛伐克／Bratislava', 'https://www.itlearning.sk',
    '课程对照行($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    'itlearning.sk=斯洛伐克 IT 培训门户谱', 'Vážený pán Dobšovič,'))
R.append(person('A-362', 'Ivan Dolnak', '斯洛伐克／Žilina', 'http://www.connet-group.sk/',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    'connet-group.sk=日利纳网络集团谱', 'Vážený pán Dolnak,'))
R.append(person('A-364', 'Olisian Sulaj', '阿尔巴尼亚／Tirana', '—（无公开站点）',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    '个体顾问无官网档;低密探询角', 'I nderuar z. Sulaj,'))
R.append(person('A-366', 'Robertas Stauskas - Magit', '立陶宛／Vilnius', 'magit.lt',
    '托管现场随单窄位($180 锚点一致)', WHY1,
    'magit.lt=维尔纽斯 IT 铺谱', 'Gerb. p. Stauskai,'))
R.append(person('A-367', 'Petar Dimitrov', '保加利亚／Sofia', 'mikrotikbg.shop',
    '预算缝低密窄针($180 锚点一致);诚实角不抢 MT 主位', WHY1,
    'mikrotikbg.shop=保加利亚 MikroTik 件店域谱', 'Уважаеми г-н Димитров,'))
R.append(person('A-368', 'Kęstutis Viselga - MikroTik Training Lietuva', '立陶宛／Alytus', 'mikrotik-training.lt',
    'MTCSWE 课堂对照单元($180 锚点一致);—(合作探询,无量产报价);**p1=CONSULT-OEM 谱**', WHY2,
    'mikrotik-training.lt=立陶宛 MikroTik 培训官方域谱', 'Gerb. p. Viselga,'))
R.append(person('A-369', 'Veaceslav Samburschii - Academia MikroTik', '罗马尼亚／Brașov', 'academia-mikrotik.ro',
    '顾问对照单元($180 锚点一致);**与 A-373 同人错峰主发**;—(合作探询,无量产报价)', WHY2,
    'academia-mikrotik.ro=罗马尼亚 MikroTik 学院域谱;**A-373 NDI 同人错峰注(免同日双发)**', 'Stimate d-le Samburschii,'))
R.append(person('A-370', 'Oltion Nikolla - Router.al', '阿尔巴尼亚／Tirana', 'router.al',
    '预算缝+咨询对照行双角低密针($180 锚点一致);诚实角', WHY1,
    'router.al=阿尔巴尼亚路由件域谱', 'I nderuar z. Nikolla,'))
R.append(person('A-371', 'Martin Soovares', '爱沙尼亚／Tartu', '—（无公开站点）',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    '个体顾问无官网档;塔尔图谱', 'Lugupeetud hr Soovares,'))
R.append(person('A-372', 'Domagoj Bikic', '克罗地亚／Split', 'https://www.pondi.hr',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价);**p1=CONSULT-OEM 谱**', WHY2,
    'pondi.hr=斯普利特 IT 铺谱', 'Poštovani gospodine Bikic,'))
R.append(person('A-374', 'Rein Põdra', '爱沙尼亚／Tallinn', '—（无公开站点）',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价);**p1=CONSULT-OEM 谱**', WHY2,
    '个体顾问无官网档;塔林谱', 'Lugupeetud hr Põdra,'))
R.append(person('A-375', 'Jānis Jaunošāns', '拉脱维亚／Rīga', '—（无公开站点）',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价);**p1=CONSULT-OEM 谱**', WHY2,
    '个体顾问无官网档;里加谱', 'Cien. Jaunošāns kungs,'))
R.append(person('A-376', 'Jernej Suhadolc', '斯洛文尼亚／Ljubljana', 'https://www.virtua-it.si',
    '托管现场随单+课堂对照行双角($180 锚点一致)', WHY1,
    'virtua-it.si=卢布尔雅那 IT 托管铺谱', 'Spoštovani gospod Suhadolc,'))
R.append(person('A-377', 'Ivan Jezerinac', '克罗地亚／Čakovec', 'infiniti.hr',
    '双牌课程对照行($180 锚点一致);—(合作探询,无量产报价);**p1=CONSULT-OEM 谱**', WHY2,
    'infiniti.hr=查科韦茨 IT 铺谱;双牌课程谱', 'Poštovani gospodine Jezerinac,'))
R.append(person('A-378', 'David Blažević', '克罗地亚／Osijek', '—（无公开站点）',
    '**建档供位;用户补邮箱→启用顾问对照单元**;—(合作探询,无量产报价);**p1=CONSULT-OEM 谱**', WHY2,
    '个体顾问无官网档;**建档供位待用户补邮箱**', 'Poštovani gospodine Blažević,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第22波50户.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 22 波 50 户扩招批:A-329~A-378 顺延 50 户(公司档 29+人名档 21;东欧/巴尔干/波罗的海新领土首拓)',
               'scope': 'FR4/IT13/NL2/BE1/NO1/PT1/ES1/DE1/US2/GR2/SK1/MT1 公司谱 31+人名档 19(UA3/GR1/SK2/AL2/LT2/BG1/RO1/EE2/LV1/HR3/SI1);守档 2(SYNEXIE 法人接棒/Nexus 马耳他具名缺);换代窗 4(NXO/GTD/Techno Center/SYNEXIE);军防守界 2(CGT 加厚/Techno Center PAC-PAL);公采/MePA 守界 5(Adrianet/World Tech/ML Software/Eulogic/Techno Center);医疗守界 1(Irene);关铺差旗 1(Landatel RR 孤证);民用限定守界 2(UA 户);错峰注 1(A-369/A-373)',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 22 波 50 户扩招批落盘:', len(R))
