# -*- coding: utf-8 -*-
"""R66 B 面 KP 波 1:B-058/B-129/B-296/B-469 四户(kp 直接带结构化列表)。"""
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
        inference='R66 B 面 KP 波 1 具名金谱', trend='2026-10-08 R66-B 波 1 谱名牌', gap='R66-B 波 1 谱面锁定'):
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

R.append(rec('B-058', 'Öruggt Net ehf(Secure Net)',
    'Öruggt Net ehf(冰岛 Reykjavik,Kristínargata 1, 102;KT 670224-0740,VSK 152122;**2024-02-21 冰岛税局注册(2 年谱)**;DBA=Secure Net;小网络安全咨询坊(20+ 年 IT/网络/安全经验;ISO 27001 培训;欧洲/美国安全社群活跃);securenet.is;info@oruggtnet.is / +354-551-5120',
    [('Sigurður G. Bjarnason', 'Founder(又称 Siggi Bjarnason / Siggi Supergeek;1980s 起谱;曾居西雅图)', 'securenet.is/about-us 官网 about 自署', O, 'https://securenet.is/about-us/our-founder-and-us/')],
    [ev('决策链与对接人', 'Both companies were founded by Sigurður G. Bjarnason (also known as Siggi Bjarnason / Siggi Supergeek);registered 21 February 2024(Icelandic tax authority)', 'https://securenet.is/about-us/our-founder-and-us/'),
     ev('业务定位', 'We are Öruggt Net ehf, or Secure Net in English;Cybersecurity for Icelandic companies;ISO 27001 training;KT: 670224-0740 VSK: 152122', 'https://securenet.is/'),
     ev('近期动态与线索', '2026-10-08 R66-B 波 1:创办人官网自署金谱锁位;冰岛 RSK 登记册谱=KT 670224-0740 已录', 'https://securenet.is/')],
    '冰岛小网络安全咨询坊(创办人直达)', '2024 创;微实体(创办人谱)',
    ('创办人官网自署金谱', '微实体(一人谱)', 'Siggi 直达位(英语通行)', '大牌厂商链竞谱'),
    'Siggi 一人谱(opt-in 律)', 'Hi Siggi,'))

R.append(rec('B-129', 'MARAC Electronics S.A',
    'Marac Electronics S.A.(希腊 Perama/Piraeus,165 Marias Kiouri & Tripoleos Str., 188 63 + 455 Dimokratias Avenue;**1976 创(50 年谱)**;51-100 人;谱型=希腊/巴尔干一线系统集成商(电信/IT/环境/海事/能源/安防-民防/遥测;无线传输接入网微波/光链路/WiMAX;**军警谱位:Hellenic Police/Army/Navy/Air Force/S.H.A.P.E.(NATO);MOD 军工安全认证+国防电子产品国家制造商名录**);自有仓+认证实验室+车队;marac.gr;+30 210 4314361',
    [],
    [ev('业务定位', 'Provider of telecommunications products and services;founded 1976;455 Dimokratias Avenue, Perama 188 63;51-100 employees', 'https://pitchbook.com/profiles/company/159696-28'),
     ev('业务定位', 'main contractor/subcontractor for armed forces(army/navy/air force/coast guard/police);clients Hellenic Police/S.H.A.P.E.(NATO);MOD certified;listed as official National manufacturer of Defense electronic products', 'https://www.epicos.com/company/10012/marac-electronics-sa'),
     ev('近期动态与线索', '2026-10-08 R66-B 波 1:身份锁定(marac.gr 1976 Perama 本体);人名谱零命中→守档;波次二=希腊 GEMI 登记册反查董事层', 'https://www.businessregistry.gr/')],
    '希腊军警/电信系统集成商(50 年谱)', '51-100 人;1976 创',
    ('军警谱位+NATO 客户谱', '人名谱零命中', 'GEMI 登记册反查可破', '军工采购链层严'),
    '守档:身份已锁;军警谱位机会大但具名谱未破;R66 波次二点名(GEMI 反查)', '',
    inference='R66 B 面 KP 波 1 守档(身份锁定)', trend='2026-10-08 R66-B 波 1 守档', gap='R66-B 波 1 人名未破'))

R.append(rec('B-296', 'Sanuk Systems AB',
    'Sanuk Systems AB(瑞典 Älvsjö(Stockholm),Herr Stens väg 49A, SE-12530;Org.no **556757-2721**,VAT SE556757272101;2008-04-01 创于泰国 Rayong+瑞典 Stockholm 双地;**2 员工/营收 1,837 KSEK(2025,+67%)**;谱型=酒店/业委会/商户宽带+光纤+WiFi 安装与全球互联网服务(泰国自有网建);sanuksystems.com;mail@sanuksystems.com / +46 70 6966660',
    [('Rickard Kristiansson', 'Verklig huvudman(100% 实益拥有人)+Styrelseledamot(董事;创办人直达)', 'bolagsfakta.se 登记册谱(100% 控制)', O, 'https://www.bolagsfakta.se/5567572721-Sanuk_Systems_AB'),
     ('Karin Elisabeth Kristiansson', 'Styrelsesuppleant(候补董事;家族谱)', 'bolagsfakta.se 登记册谱', O, 'https://www.bolagsfakta.se/5567572721-Sanuk_Systems_AB')],
    [ev('决策链与对接人', 'Verklig huvudman: Rickard Kristiansson 100%;Styrelseledamot: Rickard Kristiansson (59);Styrelsesuppleant: Karin Elisabeth Kristiansson (62)', 'https://www.bolagsfakta.se/5567572721-Sanuk_Systems_AB'),
     ev('团队与规模', '2 anställda;Omsättning 1 837 KSEK (+67,0%);Senaste bokslut 2025', 'https://www.bolagsfakta.se/5567572721-Sanuk_Systems_AB'),
     ev('业务定位', 'Sanuk Systems was founded on April 1, 2008, in Rayong, Thailand and Stockholm, Sweden;we build fixed and wireless IP networks...for hotels and communities(官网 contact 自署 Org.no/VAT)', 'https://www.sanuksystems.com/contact/')],
    '瑞典/泰国酒店宽带小微建网商', '2 人;1.84M SEK(2025)',
    ('创办人 100% 拥有人直达', '微实体(2 人;采购偶发)', '酒店 WiFi/PoE 场景正谱', '大牌厂商链竞谱'),
    'Rickard 一人决策谱(opt-in 律)', 'Hej Rickard,'))

R.append(rec('B-469', 'Infortisa',
    'INFORTISA SL(西班牙 Alfara del Patriarca(Valencia),Calle del Pozo 1, 46115;NIF **B46466421**;1989-06-07 注册(1986 起谱,40 年);**84 员工(2025);西班牙全国 3000 强/Valencia 150 强/CNAE 4650 全国 50 强**;$14.2M;谱型=西班牙 ICT 分销一线(8,000+ 活跃品/140+ 品牌/进口出口双谱;自有牌 **iggual**;InfortisaLABS 服务臂:电商技术支持/ERP/数字化/定制 Web);infortisa.com;ventas@infortisa.com / 961 309 006',
    [('Miguel Ángel M…', 'Administrador Único(唯一管理人,**2025-07-04 新任命**;einforma 登记册件名截断,BORME 全名波次二)', 'einforma 登记册谱(名截断)', G, 'https://www.einforma.com/informacion-empresa/infortisa'),
     ('Andrés Pastor', 'Director General(现任;einforma 登记册现任谱;注:finalscout 谱标 Director Financiero 异文,RocketReach 同 DG)', 'einforma 登记册谱+RocketReach 双源', G, 'https://www.einforma.com/informacion-empresa/infortisa'),
     ('Juan José Contell Garcia', '(原)Director General/Propietario(业主;谱面 2021-2026 谱;einforma 2025 谱=非现任;**直邮 juanjo@infortisa.com(channelpartner 名录件)**)', 'channelpartner 名录件+直邮', G, 'https://guiacanaltic.channelpartner.es/infortisa/'),
     ('Belén Lasheras Gracia', 'Departamento de Compras(采购部 KPI 天位)', 'finalscout 谱', G, 'https://finalscout.com/company/infortisa'),
     ('Juan José Alfonso', 'Director Logística(物流总监)', 'finalscout 谱', G, 'https://finalscout.com/company/infortisa'),
     ('Fernando López Bonafont', 'Director InfortisaLABS(服务臂总监)', 'finalscout 谱', G, 'https://finalscout.com/company/infortisa'),
     ('Raquel Inglés', 'Responsable de Marketing(市场负责)', 'channelpartner guía 谱', G, 'https://guiacanaltic.channelpartner.es/infortisa/'),
     ('María Amparo Serres Peris', 'Responsable de Recursos Humanos', 'finalscout 谱', G, 'https://finalscout.com/company/infortisa'),
     ('Ramiro Belles Albalat', 'IT Project Manager', 'finalscout 谱', G, 'https://finalscout.com/company/infortisa'),
     ('Monica Benedicto Formenti', 'Product Manager', 'finalscout 谱', G, 'https://finalscout.com/company/infortisa')],
    [ev('决策链与对接人', 'Órgano de administración: Administrador Único MIGUEL ANGEL M... (04/07/2025);Director General ANDRES P...(现任);Director Financiero DAVID S...;Compras JUAN G...;Comercial/Exportación GRAU J...(einforma 登记册件)', 'https://www.einforma.com/informacion-empresa/infortisa'),
     ev('决策链与对接人', 'CONTACTO: Juan José Contell | CEO — juanjo@infortisa.com;Raquel Inglés, Responsable de Marketing(channelpartner 官方名录 guía)', 'https://guiacanaltic.channelpartner.es/infortisa/'),
     ev('团队与规模', 'Juan José Contell Garcia Propietario y Director General;Juan José Alfonso Director Logística;Belén Lasheras Gracia Departamento de Compras;Andrés Pastor Director Financiero;Fernando López Bonafont Director InfortisaLABS;84 empleados (2025)', 'https://finalscout.com/company/infortisa'),
     ev('业务定位', 'mayorista con más de 30 años;8.000 referencias activas;140 marcas;marca propia iggual;InfortisaLABS;NIF B46466421', 'https://www.channelpartner.es/mayoristas/infortisa-mayorista-con-mas-de-30-anos-de-experiencia/')],
    '西班牙 ICT 分销一线(自有牌+服务臂)', '84 人;$14.2M;1989 注册;全国 3000 强',
    ('西班牙一线分销+自有牌 iggual', '2025-07 管理人换任(谱位复验)', 'Belén(Compras)+Alfonso(Logística)双 KPI 天位', '大牌厂商直供链竞谱'),
    '管理人 2025 换任;BORME 全名波次二点名(opt-in 律)', 'Hola Belén,'))

with open('batch/B类深挖_2026-10-08_R66_BKP波1.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 B 面 KP 波 1:Secure Net(IS 创办人官网金谱)+MARAC(军警谱位守档)+Sanuk(SE 登记册 100% 拥有人)+Infortisa(ES 分销一线 10 人谱)四户',
               'scope': 'IS/GR/SE/ES 谱;乌克兰守界不动;Infortisa 2025-07 管理人换任谱位复验',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 B 面 KP 波 1 四户落盘')
