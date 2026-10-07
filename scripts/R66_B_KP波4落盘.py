# -*- coding: utf-8 -*-
"""R66 B 面 KP 波 4:B-191/B-194/B-201/B-456 四户(kp 直接带结构化列表)。"""
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
        inference='R66 B 面 KP 波 4 具名金谱', trend='2026-10-08 R66-B 波 4 谱名牌', gap='R66-B 波 4 谱面锁定'):
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

R.append(rec('B-191', 'AT Computers a.s',
    'AT Computers a.s.(捷克 Ostrava HQ+Prague/Brno/Bratislava/Žilina 分支;**捷克-斯洛伐克最大 ICT 批发分销商(1998 起 28 年;2024 推测 ¥35 mld Kč;330 员工;77,921 品/263 全球厂商;捷克最大 PC 生产商;波兰 AB Group 成员(华沙上市)=中东欧最大分销集团,欧洲前十)**;atcomp.cz;XaaS/gaming(X-Play)/Eaton 官方分销商',
    [('Aleš Kilnar', 'předseda představenstva(董事会主席)', '公司 LinkedIn 官方 About 页署名', O, 'https://www.linkedin.com/company/at-computers'),
     ('Martin Harazím', 'Purchasing Director(**采购总监 KPI 天位**)', 'Crunchbase 谱', G, 'https://www.crunchbase.com/organization/at-computers'),
     ('Martin Wanke', 'Marketing Director', 'Crunchbase+rmol.cz 采访双源', G, 'https://www.crunchbase.com/organization/at-computers'),
     ('Petr Vaněk', 'obchodní ředitel(销售总监)', 'rmol.cz XaaS 采访件', G, 'https://www.rmol.cz/distributor/at-computers?paginator-page=13'),
     ('Rostislav Vybíral', 'člen představenstva(董事)+IT oddělení 部长', 'kariera.atcomp.cz 官网自署 vybiral@atcomp.cz', O, 'https://kariera.atcomp.cz/'),
     ('Lukáš Neuwirth', 'vedoucí reklamačního oddělení(售后索赔部长)', 'kariera.atcomp.cz 官网自署 neuwirth@atcomp.cz', O, 'https://kariera.atcomp.cz/'),
     ('Peter Majdak', 'Networking(产品线口)', 'LinkedIn 谱', G, 'https://www.linkedin.com/company/at-computers'),
     ('Martin Hrabal', 'Financial officer / Payment manager', 'LinkedIn 谱', G, 'https://www.linkedin.com/company/at-computers')],
    [ev('决策链与对接人', 'Aleš Kilnar, předseda představenstva(公司 LinkedIn About 页署名捷克最大 ICT 批发分销+30 mld Kč 谱)', 'https://www.linkedin.com/company/at-computers'),
     ev('决策链与对接人', 'Martin Harazím Purchasing Director;Martin Wanke Marketing Director(Crunchbase employee 件);annual sales CZK 23 billion;part of Polish AB Group', 'https://www.crunchbase.com/organization/at-computers'),
     ev('团队与规模', 'Rostislav Vybíral člen představenstva - IT oddělení;Lukáš Neuwirth vedoucí reklamačního oddělení;Marcel Kurovec správce IT(kariera.atcomp.cz 官网员工故事页)', 'https://kariera.atcomp.cz/'),
     ev('团队与规模', 'Petr Vaněk a Martin Wanke (AT Computers): Když se XaaS pojme správně...(rmol.cz 采访件,Vaněk=obchodní ředitel)', 'https://www.rmol.cz/distributor/at-computers?paginator-page=13')],
    '捷克一线 ICT 批发分销(AB Group 成员)', '330 人;35 mld Kč(2024)',
    ('中欧前十分销+AB Group 平台', '大平台采购链层(AB Group)', 'Harazím 采购总监 KPI 直达', '大牌厂商直供链'),
    'Harazím 采购+Kilnar 董事会谱位(opt-in 律)', 'Dobrý den Martine,'))

R.append(rec('B-194', 'AxiLogi',
    'Axilogi s.r.o.(捷克 Plzeň,Daimlerova 1161/6, 301 00;**IČO 10964703**(C 123877 Krajský soud v Brně;资本 2,000,000 Kč;**2021-06-23 注册(5 年)**);6 员工;谱型=网络技术件+光伏/太阳能批发分销(安全摄像头/智能家居/电源件;axilogi.com);**股东:DC Europe system a.s.(Plzeň 集团)+Ing. Milan Harmáček(akcionář)**;živnost 电气电子电信设备制造安装维修(řemeslná)',
    [('Ing. Milan Harmáček', 'CEO(2023 起)+Akcionář/člen správní rady(股东+监事会;前 DISCOMP s.r.o. CEO 1999-2024 25 年谱)', 'podnikatel.cz 登记册谱+RocketReach CEO 谱', O, 'https://www.podnikatel.cz/rejstrik/axilogi-s-r-o-10964703/'),
     ('Patrik Kříž', 'Key Principal(主负责人)', 'DNB Key Principal 谱', G, 'https://www.dnb.com/business-directory/company-profiles.axilogi_sro.8f534121236895f8af25304b2e442fad.html'),
     ('Tomáš Bubeník', 'Obsahový specialista(内容专员;前 pilsfree.net 谱)', 'RocketReach 谱', G, 'https://rocketreach.co/axilogi-s-r-o-profile_b6cf87abc782c61f')],
    [ev('决策链与对接人', 'Kapitál: DC Europe system a.s. + Ing. Milan Harmáček Akcionář, Člen správní rady(podnikatel.cz 捷克商事登记谱);základní kapitál 2 000 000 Kč', 'https://www.podnikatel.cz/rejstrik/axilogi-s-r-o-10964703/'),
     ev('决策链与对接人', 'Key Principal: Patrik Kříž(DNB 件);CEO Milan Harmacek(2023-now;1999-2024 CEO @ DISCOMP s.r.o.;ZČU Plzeň Ing. 2000)', 'https://rocketreach.co/milan-harmacek-email_99105918'),
     ev('团队与规模', 'Top employees: Milan Harmacek CEO;Tomáš Bubeník Obsahový specialista;6 employees;Network Technologies/Photovoltaic/Security Cameras/Smart Home(RR 谱)', 'https://rocketreach.co/axilogi-s-r-o-profile_b6cf87abc782c61f')],
    '捷克 Plzeň 网络件+光伏批发分销', '6 人;2021 创;DC Europe 集团',
    ('Harmáček 25 年分销谱(Discomp→Axilogi)', '小实体(6 人)', 'CEO 股东直达位', '大牌件链竞谱'),
    'Harmáček CEO/股东+Kříž 负责人(opt-in 律)', 'Dobrý den pane Harmáčku,'))

R.append(rec('B-201', 'PCV Computers, s.r.o',
    'PCV Computers, s.r.o.(捷克 České Budějovice(Za Otýlií 2874/6)+Praha Rybná 682/14 注册;**IČ 26084121,DIČ CZ26084121,datová schránka jumsm2k**;**2005 创(21 年)**;11-15 员工;$2M;+420 380 420 700;**谱型=捷克组网/VoIP IT 分销商:WISP 专营 MikroTik/Grandstream/Thecus/ADEX/Nenshi 官方分销商!TP-Link/Ubiquiti 二级分销;+IS 实施(Altus VARIO Pro/IS KARAT 企业档)**;pcvcomp.cz;adam@pcvcomp.cz(商户名录件)',
    [('Ing. Jan Duda', 'jednatel(执行董事)+obchod(商务;2005-04 起董事会位)', 'verif.com 高管谱+zivefirmy.cz 联人件双源', G, 'https://www.verif.com/en/company/PCV-Computers-s--r--o--68d9e0941299230338adfe56/'),
     ('Adam Truszyk', 'obchod(商务;adam@pcvcomp.cz 商户名录邮箱件)', 'zivefirmy.cz 联人件+RR Obchodník 谱+nen.nipez.cz 商户名录 adam@ 件', G, 'https://www.zivefirmy.cz/pcv-computers_f347429'),
     ('Zdeněk Valdman', 'Vedoucí prodeje(销售主管 KPI 天位)', 'RocketReach 谱', G, 'https://rocketreach.co/pcv-computers-sro-profile_b4140fccff88a4ad'),
     ('Michaela Koryčanská', 'Product Manager', 'RocketReach 谱', G, 'https://rocketreach.co/pcv-computers-sro-profile_b4140fccff88a4ad'),
     ('Petra Pavlíčková', 'Product Manager', 'RocketReach 谱', G, 'https://rocketreach.co/pcv-computers-sro-profile_b4140fccff88a4ad'),
     ('Augustin Uhlíř', 'Produktový manažer(产品经理)', 'RocketReach+LinkedIn 双源谱', G, 'https://rocketreach.co/pcv-computers-sro-profile_b4140fccff88a4ad'),
     ('Miloslav Melichar', 'VoIP specialista(VoIP 专员)', 'RocketReach+LinkedIn 双源谱', G, 'https://rocketreach.co/pcv-computers-sro-profile_b4140fccff88a4ad'),
     ('Zdenka Dorazilová', 'ERP konzultant', 'RocketReach+LinkedIn 双源谱', G, 'https://rocketreach.co/pcv-computers-sro-profile_b4140fccff88a4ad')],
    [ev('决策链与对接人', 'Kontaktní osoby: Jan Duda - obchod, jednatel;Adam Truszyk - obchod;Ing. Jan Duda tel.: 380 420 700(zivefirmy.cz 商户页)', 'https://www.zivefirmy.cz/pcv-computers_f347429'),
     ev('决策链与对接人', 'Who is running the company: managed by Jan Duda — Most senior leader since 04/01/2005, Member of the Board of Directors(verif.com 件)', 'https://www.verif.com/en/company/PCV-Computers-s--r--o--68d9e0941299230338adfe56/'),
     ev('业务定位', 'IT distributor specialized for networking and VoIP;Distributor: Mikrotik, Grandstream, Thecus, ADEX, Nenshi;Subdistributor: TP-Link, Ubiquiti;11-50 employees;České Budějovice;founded 2005(LinkedIn 官方 About 页)', 'https://cz.linkedin.com/company/pcv-computers-s-r-o-'),
     ev('团队与规模', 'Michaela Koryčanská/Petra Pavlíčková/Augustin Uhlíř Product Managers;Zdeněk Valdman Vedoucí prodeje;Miloslav Melichar VoIP specialista;Zdenka Dorazilová ERP konzultant;15 employees;$2M', 'https://rocketreach.co/pcv-computers-sro-profile_b4140fccff88a4ad')],
    '捷克 WISP 组网/VoIP IT 分销(MikroTik 官方)', '11-15 人;$2M;2005 创',
    ('MikroTik 官方分销+21 年谱', '小实体谱', 'Valdman 销售主管+Duda 董事直达', '大牌厂商链竞谱'),
    'Duda jednatel+Valdman 销售主管+adam@ 商务线(opt-in 律)', 'Dobrý den pane Dudo,'))

R.append(rec('B-456', 'TRUENET',
    'TRUENET, LDA(葡萄牙 Porto,Rua Mosteiro 89, Leça do Balio 4465-703;**NIF 513514139**;**2015 创(11 年)**;公司资本 €50,000;33 员工;+351 22 011 9696;comercial@truenet.pt;谱型=葡萄牙数据通信网服商(WiFi/routing/switching/统一通信+helpdesk 管服+NAC 入侵检测+软件开发;认证技师谱 20+ 年;NOS Comunicações Empresarial 合作谱)',
    [('Orlando Carlos Lopes da Silva', 'Manager(Sócio-Gerente 股东经理)', 'Kompass 法定高管谱+RR Gerente 谱', G, 'https://gb.kompass.com/c/truenet-lda/pt150369/'),
     ('Daniela Costa e Silva', 'Founder and CFO(创位+财务总监;家族谱)', 'RocketReach 谱', G, 'https://rocketreach.co/truenet-lda-management_b44becedfcf1cc86'),
     ('Antero Vasconcelos', 'Chief Technology Officer(技术总监)', 'RocketReach 谱', G, 'https://rocketreach.co/truenet-lda-management_b44becedfcf1cc86'),
     ('Helder Oliveira', 'Consultor Técnico NOS Comunicações - Empresarial(企业线顾问)', 'RocketReach 谱', G, 'https://rocketreach.co/truenet-lda-management_b44becedfcf1cc86'),
     ('Pedro Rocha', 'Network System Engineer', 'RocketReach 谱', G, 'https://rocketreach.co/truenet-lda-management_b44becedfcf1cc86'),
     ('Ricardo Lopes', 'Project Manager - Corporate Solutions @ NOS', 'RocketReach 谱', G, 'https://rocketreach.co/truenet-lda-management_b44becedfcf1cc86')],
    [ev('决策链与对接人', 'Executives: Orlando Carlos Lopes da Silva — Manager (Sócio-Gerente);N. FISCAL 513514139;Rua Mosteiro, 89, 4465-703 LEÇA DO BALIO;Corporate capital 50,000 EUR;established 2015(Kompass 件)', 'https://gb.kompass.com/c/truenet-lda/pt150369/'),
     ev('团队与规模', 'Antero Vasconcelos CTO;Daniela Costa e Silva Founder and CFO;Orlando Silva Gerente;Helder Oliveira Consultor NOS;Sara Ferreira PM;Nuno Caldeira;Manuel Mendes;Ricardo Lopes PM NOS;Pedro Rocha Network System Engineer;33 employees(RR 谱)', 'https://rocketreach.co/truenet-lda-management_b44becedfcf1cc86'),
     ev('业务定位', 'DATA COMMUNICATION NETWORKS (WIFI, Routing, Switching, Unified Communication);HELPDESK;NETWORK SECURITY (Firewall, NAC, Intrusion Detection);SOFTWARE DEVELOPMENT;certified technicians 20+ years', 'https://www.lusha.com/business/c90320f3cb3065cd/')],
    '葡萄牙 Porto 数据通信网服商(NOS 合作谱)', '33 人;2015 创;€50k',
    ('股东经理+创始 CFO 家族谱', '小实体谱', 'Vasconcelos CTO 技术谱直达', '大牌件链竞谱'),
    'Orlando 股东经理+Daniela 创始 CFO(opt-in 律)', 'Boa tarde Orlando,'))

with open('batch/B类深挖_2026-10-08_R66_BKP波4.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 B 面 KP 波 4:AT Computers(CZ 最大 ICT 分销,采购总监 KPI)+Axilogi(Harmáček 25 年谱)+PCV(MikroTik 官方分销 8 人谱)+TRUENET(PT 家族谱+CTO)四户',
               'scope': 'CZ×3/PT 谱;PCV/Axilogi 捷克商事登记谱;AT Computers AB Group 平台层注记',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 B 面 KP 波 4 四户落盘')
