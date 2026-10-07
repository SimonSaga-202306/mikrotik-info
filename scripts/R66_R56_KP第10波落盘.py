# -*- coding: utf-8 -*-
"""R66 第 10 波:A-032/A-047/A-054/A-058 四户(kp 直接带结构化列表)。"""
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
        inference='R66 第 10 波具名 KP 金谱', trend='2026-10-07 R66 10 波谱名牌', gap='R66 10 波谱面锁定'):
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

R.append(rec('A-032', 'Aikom Technology S.r.l.',
    'AIKOM TECHNOLOGY SRL(意大利 Riccione(Rimini),Viale Lambrusco 1, 47838;+39 0541 648894;aikomtech.com;2021-02 起 MikroTik 意大利全国分销商(channelcity 载:全谱 160+ 品·Cloud Core/RouterBOARD 企业级→家用/LTE/FWA→铜纤交换+IoT/LoRa;工程级免费售后为卖点);25-99 人(D&B)',
    [('Sabrina Vescovi', 'President(总裁)', 'D&B Key Principal 谱', G, 'https://www.dnb.com/business-directory/company-profiles/aikom-technology-srl.1e5071df720517b638b23d670b407e5e'),
     ('Mauro Renzi', 'General Manager(总经理;30 年 ICT 谱)', 'D&B+LinkedIn 双源谱', G, 'https://www.dnb.com/business-directory/company-profiles/aikom-technology-srl.1e5071df720517b638b23d670b407e5e'),
     ('Matteo Del Bianco', 'Product Manager(无线产品线)', '公司新闻稿自署(channelcity/channeltech/toptrade 三贸易件转载)', O, 'https://www.channelcity.it/news/18351/aikom-technology-distribuisce-mikrotik.html')],
    [ev('决策链与对接人', 'Key Principal: SABRINA VESCOVI (President);MAURO RENZI is the General Manager of AIKOM TECHNOLOGY SRL', 'https://www.dnb.com/business-directory/company-profiles/aikom-technology-srl.1e5071df720517b638b23d670b407e5e'),
     ev('决策链与对接人', 'Matteo del Bianco, Product manager dell’area Wireless di Aikom Technology(MikroTik 分销协议公司新闻稿引语)', 'https://www.channelcity.it/news/18351/aikom-technology-distribuisce-mikrotik.html'),
     ev('业务定位', 'Aikom Technology distribuisce MikroTik in Italia ... oltre 160 i prodotti a listino ... garanzia per i partner di una pronta consegna', 'https://www.toptrade.it/featured/aikom-technology-distribuisce-le-soluzioni-mikrotik/'),
     ev('团队与规模', 'Mauro Renzi — Opero da 30 anni nel settore ICT;Location Riccione;Aikom Technology S.r.l.', 'https://www.linkedin.com/in/maurorenzi/')],
    '意大利 MikroTik 全国分销商(工程级售后谱)', '25-99 人;Riccione',
    ('MikroTik 全谱 160+ 品分销位', 'President/GM 为 D&B 谱(谱面带核)', 'Del Bianco 无线 PM 直达位', '大牌厂商直供链竞谱'),
    'Vescovi/Renzi 谱面带核+Del Bianco 直达(opt-in 律)', 'Hi Matteo,'))

R.append(rec('A-047', 'CSI S.A',
    'CSI S.A(希腊;2026-10-07 R66 第 10 波排噪:公开面检索命中 Stavros Maragoudakis/Hellascom/Linkshop.gr/DC ELECTRONICS/Intercept MSV 等多家希腊 MikroTik 渠道异名实体,均非 CSV 入档『CSI S.A』本体;实体身份未锁)',
    [],
    [ev('业务定位', 'CSI S.A — CSV 入档名;希腊 MikroTik 渠道面检索仅返回 Hellascom/Linkshop.gr/MikroTik Training Center in Greece(Stavros Maragoudakis)等异名实体', 'https://mikrotik.com/consultants/europe'),
     ev('业务定位', 'gr.linkedin MikroTik Training Center in Greece: Trainer Stavros Maragoudakis(Hellascom/Linkshop.gr Managing director)+Eleftherios Liodakis(DC ELECTRONICS GM)——均非 CSI S.A 本体', 'https://gr.linkedin.com/company/mikrotiktraining'),
     ev('近期动态与线索', '2026-10-07 R66 10 波:守档排噪;波次二=希腊 GEMI 登记册(ΓΕΜΗ)按号反查定名', 'https://www.businessregistry.gr/')],
    '希腊网络渠道商(身份待锁)', '(未锁定)',
    ('CSV 已有谱名', '实体身份未锁定', 'GEMI 登记册反查可破', '同名噪声高'),
    '守档:排噪准由已录;R66 波次二点名(GEMI 登记册按号反查)', '',
    inference='R66 第 10 波排噪守档', trend='2026-10-07 R66 10 波排噪守档', gap='R66 10 波身份未锁'))

R.append(rec('A-054', 'Direktronik AB',
    'Direktronik Aktiebolag(瑞典 Nynäshamn,Konsul Johnsons väg 15, 149 45;Org.nr 556281-9663;1986-09 注册(40 年谱);28 员工;$7.5M;SNI 46502 电子元件批发;**Lagercrantz Group AB (publ) 子公司**(母链 Control 分部);2025-08 收购 Qvintus AB(温度/压力测量仪表);direktronik.se;+46 8 524 007 00;info@direktronik.se',
    [('Henrik Johan Ringstedt', 'Extern verkställande direktör(外部任 CEO,1989 生)', 'allabolag.se 登记册谱+DNB Key Principal', O, 'https://www.allabolag.se/foretag/direktronik-aktiebolag/nyn%C3%A4shamn/elektronik-och-telekommunikationsutrustning-grossist/2JZYJ4FI63IFS'),
     ('Mats Johan Rydén', 'Ordförande(董事长,1966 生;官方新闻稿 CEO 位)', 'allabolag.se 登记册谱+Lagercrantz 集团官方新闻稿(2025-08 Qvintus 收购 CEO 署名)', O, 'https://www.inderes.dk/en/releases/lagercrantz-acquires-aktiebolaget-qvintus'),
     ('Lars Andreas Heder', 'Board Member+Head of Division Control(Lagercrantz 集团)', 'DNB+Lagercrantz 官方新闻稿联系人', O, 'https://www.inderes.dk/en/releases/lagercrantz-acquires-aktiebolaget-qvintus'),
     ('Mats Backlund', 'CTO and Business Development Specialist', 'RocketReach 谱', G, 'https://rocketreach.co/direktronik-ab-profile_b5d44236f42e3fbf'),
     ('Susanne Carlsson', 'Acting CIO', 'RocketReach 谱', G, 'https://rocketreach.co/direktronik-ab-profile_b5d44236f42e3fbf'),
     ('Jonas Wahlström', 'Product Sales Manager', 'RocketReach 谱', G, 'https://rocketreach.co/direktronik-ab-profile_b5d44236f42e3fbf'),
     ('Anders Hedin', 'Sortimentsansvarig(品列负责人)', 'RocketReach 谱', G, 'https://rocketreach.co/direktronik-ab-profile_b5d44236f42e3fbf'),
     ('Marius Hæggernæs', 'Contact(分销谱名列)', 'coax-connectors 分销页', G, 'https://coax-connectors.com/distributors/nexlan-as-en-del-av-direktronik-ab-copy/')],
    [ev('决策链与对接人', 'Extern verkställande direktör Henrik Johan Ringstedt (f 1989);Ordförande Mats Johan Rydén (f 1966);Moderbolaget är Lagercrantz Group Aktiebolag', 'https://www.allabolag.se/foretag/direktronik-aktiebolag/nyn%C3%A4shamn/elektronik-och-telekommunikationsutrustning-grossist/2JZYJ4FI63IFS'),
     ev('近期动态与线索', 'Lagercrantz acquires Qvintus: "With Qvintus, Direktronik can develop its business within industrial measurement and control", says Mats Rydén, CEO of Direktronik AB(2025-08-19 官方发布);Andreas Heder Head of Division Control', 'https://www.inderes.dk/en/releases/lagercrantz-acquires-aktiebolaget-qvintus'),
     ev('团队与规模', 'Top employees: Mats Backlund CTO and Business Development;Susanne Carlsson Acting CIO;Jonas Wahlström Product Sales Manager;Anders Hedin Sortimentsansvarig;28 employees;$7.5M revenue', 'https://rocketreach.co/direktronik-ab-profile_b5d44236f42e3fbf')],
    '瑞典电子件批发分销(Lagercrantz 集团子)', '28 人;$7.5M;1986 创;集团母链',
    ('40 年分销+集团 Control 分部', '集团采购链层(谱位在总部)', 'extern VD+董事长双谱直达', '大牌厂商直供链竞谱'),
    '集团母链:采购决策或在 Lagercrantz 层(opt-in 律)', 'Hej Henrik,'))

R.append(rec('A-058', 'AGL Industrial Solutions',
    'António Guedes Lopes, Sociedade Unipessoal, Lda(葡萄牙 Covilhã,Avenida Anil 6 7ºDto, 6200-502 + Lisboa Rua Braamcamp 84 3ºDto;葡 Sociedade **Unipessoal**=单一股东实体;2011-01-14 创(15 年谱);CAE 46501 电脑/外设/软件批发;DBA=AGL - Industrial Solutions;guedeslopes.pt(工业 PC/EDGE AI/触控/工业通信/IoT 网关/工业电源;Kvaser 伙伴;Portugal leading value-added distributor);邮箱模式 first@guedeslopes.pt(33%)',
    [('Pedro Jorge Rodrigues Lopes', 'Managing Partner(管理合伙人;Key Principal)', 'D&B Key Principal 谱', G, 'https://www.dnb.com/business-directory/company-profiles/ant%C3%B3nio_guedes_lopes_sociedade_unipessoal_lda.dfc3d510b30cbe803c591a2f38908775.html'),
     ('António Guedes Lopes', '同名创位推定(Unipessoal 公司名即创位姓;身份待里斯本注册局谱核)', '公司名件推定(leads-only)', G, 'https://www.iberinform.pt/empresa/24441781/antonio-guedes-lopes-sociedade-unipessoal-lda')],
    [ev('决策链与对接人', 'Key Principal: Pedro Jorge Rodrigues Lopes — Managing Partner;Doing Business As: AGL - INDUSTRIAL SOLUTIONS(AVENIDA ANIL, 6 7ºDTO. 6200-502 COVILHÃ)', 'https://www.dnb.com/business-directory/company-profiles/ant%C3%B3nio_guedes_lopes_sociedade_unipessoal_lda.dfc3d510b30cbe803c591a2f38908775.html'),
     ev('业务定位', 'Razão Social: António Guedes Lopes, Sociedade Unipessoal, Lda;Designação comercial: AGL - INDUSTRIAL SOLUTIONS;CAE 46501 Comércio por grosso de computadores;fundada 2011/01/14', 'https://www.iberinform.pt/empresa/24441781/antonio-guedes-lopes-sociedade-unipessoal-lda'),
     ev('业务定位', 'AGL Industrial Solutions — Specialists in Industrial EDGE AI Computers, Embedded Systems, Panel PCs, Touch Monitors, industrial communication devices;Portugal leading company in distribution of value-added systems(Kvaser 伙伴页)', 'https://kvaser.com/company/agl-industrial-solutions/')],
    '葡萄牙工业 PC/EDGE AI 价值分销(Kvaser 伙伴)', '2011 创;Unipessoal 独资;小实体',
    ('葡萄牙 value-added 工业件一线', '小实体独资(决策=一人)', 'Lopes Managing Partner 直达位', '大牌工业件链竞谱'),
    'Lopes 独资直达(opt-in 律)', 'Hi Pedro,'))

with open('batch/A类深挖_2026-10-07_R66_R56_KP第10波.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-07',
               'wave': 'R66 第 10 波:Aikom(MikroTik 意分销)+CSI(排噪守档)+Direktronik(Lagercrantz 子)+AGL(葡 Unipessoal)四户',
               'scope': 'IT/SE/PT 谱;CSI S.A 希腊身份未锁守档;公司型名薄 KP 队列续',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 10 波 4 户落盘')
