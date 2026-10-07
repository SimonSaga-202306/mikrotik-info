# -*- coding: utf-8 -*-
"""R65 B 类深挖第 9 批:希腊/意大利/奥地利/匈牙利顾问群 8 户。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd='', Unk=None):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 9 批精修 = R57 转写 + 本轮 LinkedIn/登记新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    if Unk: r['unknowns56'] = Unk + r['unknowns56']
    return r

put('B-163',
    head='FASTNET / Matrix Computers 相关域(Ancona, Marche;**谱型回正=FASTNET S.p.A. 马尔凯 EE 电信体**(Fiberwide S.p.A. 集团):'
         'Filippo Loretoni = Amministratore Delegato(CEO);Giorgio Marchetti = Responsabile Commerciale/Sales Manager;Octavio Melendres = Senior Network Engineer;'
         '2026-03 TV Centro Marche 专访 Open Fiber 战略协议;Università Politecnica delle Marche 在校谱)',
    kpn='Filippo Loretoni = Amministratore Delegato(CEO);Giorgio Marchetti = Sales Manager;Octavio Melendres = Senior Network Engineer',
    kp=[{'name': 'Filippo Loretoni', 'role': 'Amministratore Delegato(首席执行官)', 'contact': '经 fastnet.it', 'status': 'fiberwide.com/TV Centro Marche 报道自曝', 'source': 'https://fiberwide.com/fastnet-protagonista-dellinnovazione-online-lo-speciale-tv-sullaccordo-strategico-con-open-fiber/'},
        {'name': 'Giorgio Marchetti', 'role': 'Sales Manager/商务总监', 'contact': '@fastnet.it(模式提示)', 'status': 'rocketreach 自曝+fiberwide 同源', 'source': 'https://rocketreach.co/giorgio-marchetti-email_127258904'}],
    facts=[{'dim': 'R65 谱型+KP', 'text': 'FASTNET S.p.A.(Gruppo Fiberwide)· Open Fiber 战略协议 2026-03 · Loretoni CEO · Marchetti Sales · Melendres NE',
            'quote': 'Filippo Loretoni (Amministratore Delegato di Fastnet), Giorgio Marchetti (Responsabile Commerciale) e Octavio Melendres (Senior Network Engineer)… accordo strategico con Open Fiber',
            'url': 'https://fiberwide.com/fastnet-protagonista-dellinnovazione-online-lo-speciale-tv-sullaccordo-strategico-con-open-fiber/'}],
    fihadd='意大利电信马尔支队型;Open Fiber 战略合作 + Fiberwide 集团')

put('B-155',
    head='Matrix Computers di Somma Andrea(Via Madonnina 28, 20814 Varedo(MB);0362 287146 可查;'
         '**个体商号(ditta individuale)=业主 Andrea Somma 本人**;PagineGialle 黄页实名',
    kpn='Andrea Somma = 个体商号业主本人(diritta individuale)',
    kp=[{'name': 'Andrea Somma', 'role': '个体业主本人', 'contact': '径 matrixcomputers.it / 0362 287146', 'status': 'PagineGialle 实名', 'source': 'https://www.paginegialle.it/varedo-mb/informatica/matrix-computers-di-somma-andrea'}],
    facts=[{'dim': 'R65 商号谱位', 'text': 'Matrix Computers di Somma Andrea · Varedo MB · 0362 287146(黄页认证)',
            'quote': 'Matrix Computers di Somma Andrea si trova in Via Madonnina, 28 20814 Varedo (MB) … 0362 287146',
            'url': 'https://www.paginegialle.it/varedo-mb/informatica/matrix-computers-di-somma-andrea'}],
    fihadd='单体商号 And 头;MB 地区店')

put('B-121',
    head='EXA Solutions(Heraklion Idomeneos 5, 71202 + Athens Dorylaiou 6, 11521 双办;'
         '**谱型=希腊 SME 托管 IT/云托管/ERP/WMS 一体化集成商**:managed IT/cybersecurity/cloud/ERP/WMS integrations;'
         'FnA Company / ELMEPA 等多家 openly 宣传口碑;+30 28130 15000, info@exasolutions.gr',
    kpn='George Alexander Kontaxakis(名录口径;R65 搜出同名**医疗图像研究员**/Aegean Airlines 同名——**为污染噪音,不采信**;登记方向=雅典 G.E.MI 台账)',
    facts=[{'dim': 'R65 谱位/双办', 'text': 'Heraklion+Athens 双办;managed IT/cyber/云/ERP/WMS 一体化,ELMEPA 等专 case',
            'quote': 'EXA Solutions delivers managed IT, cybersecurity, cloud infrastructure, ERP and WMS integrations for businesses across Greece … Heraklion Idomeneos 5, 71202 / Athens Dorylaiou 6, 11521 / +30 28130 15000 / info@exasolutions.gr',
            'url': 'https://exasolutions.gr/en/'},
            {'dim': 'R65 同名噪音注', 'text': 'Georgios Kontaxakis(Aegean Airlines 雇员 / ResearchGate 医疗图像)=同名他人,不采信',
             'quote':'(LinkedIn / ResearchGate 2026-10-07 搜出同名画像,与 EXA Solutions 无关)',
             'url': '(沙箱谱位核验日志)'}],
    fihadd='希腊 SME 托管 IT 集成商;KP 未按名型沈,同同名噪音已区分证')

put('B-080',
    head='LazyBear Kft.(7626 Pécs, Felsővámház utca 23;F.Cg 02-09-086615, Adószám 27795613-2-02, 2022-03-21 创立;'
         '**核心谱位:Németh András István = 三业主之一(与 Pista Izabella Judit ügyvezető(UUID) 并列)**;'
         'Törő Zsófia Ágnes 第三业主;303337694 总线,lazybearkft@gmail.com 自曝;tevékenység 5630 = 餐饮/宾饮属业务厚(谱型疑主业非纯 IT——MikroTik 谱挂 IT 咨询/技术博客户 lazybear.hu 侧)',
    kpn='Németh András István = 业主(名录口径);Pista Izabella Judit = ügyvezető(法定代表人);Törő Zsófia Ágnes 第三业主',
    kp=[{'name': 'Pista Izabella Judit', 'role': 'Ügyvezető(法定代表人)', 'contact': 'lazybearkft@gmail.com(gmail 自曝)', 'status': 'companywall.hu 实名', 'source': 'https://www.companywall.hu/v%C3%A1llalat/lazybear-kft/MMHKiQlR'},
        {'name': 'Németh András István', 'role': '业主(名录口径,技术本体)', 'contact': '同上', 'status': '同源', 'source': '同 companywall.hu'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'LazyBear Kft · Pécs 2022-03 创 · Cg 02-09-086615 · Pista Izabella Judit ügyvezető + Németh András István+Törő Zsófia Ágnes 三业主',
            'quote': 'Lazybear Kft. amely a Felsővámház utca 23., 7626, Pécs … 2022. 03. 21. … Ügyvezető: Pista Izabella Judit … Tulajdonos: Németh András István, Törő Zsófia Ágnes',
            'url': 'https://www.companywall.hu/v%C3%A1llalat/lazybear-kft/MMHKiQlR'}],
    fihadd='Pécs 小 Kft,5630 餐饮 tevékenység 与 lazybear.hu 同名联合体(疑多面家);技术扁平位')

put('B-110',
    head='Gunther Engetsberger(Stadtgemeinde Oberndorf bei Salzburg 市公局 **Leiter IT(IT 主管)**,兼 Radiofabrik Salzburg 2023 董事会成员;'
         '1999-2020 年 20+ 年 Jugendzentrum 技术志愿;BHAK Oberndorf bei Salzburg 培养;sei-ned.org (SEI/KNX 智装能野) 关联域;'
         '个体 MikroTik 顾问/培训师血统=市政 IT 权威位',
    kpn='Gunther Engetsberger = Stadt Oberndorf Leiter IT(日报绍尔兹奥地利中部政企 IT 位;LinkedIn+gov 双源)',
    kp=[{'name': 'Gunther Engetsberger', 'role': 'Leiter IT(市公局 IT 主管)', 'contact': '经 oberndorf.salzburg.at 市政办公 / LinkedIn', 'status': 'oberndorf.salzburg.at 市政职员页+LinkedIn 双源', 'source': 'https://www.oberndorf.salzburg.at/Stadtamtsleitung'}],
    facts=[{'dim': 'R65 实名/职位', 'text': 'Gunther Engetsberger = Stadtgemeinde Oberndorf Leiter IT(市政 IT)· Radiofabrik 董事会成员 2023',
            'quote': 'Gunther Engetsberger (Leiter IT) … Board: Susanne Imhof … Gunther Engetsberger [Radiofabrik 2023]',
            'url': 'https://www.oberndorf.salzburg.at/Stadtamtsleitung'}],
    fihadd='市政 IT 权威度=奥地利中部政企 IT 权威位;20 年我是年口')

put('B-127',
    head='Konstantinos Analytis / Alfa-Tech(alfa-tech.gr;R65 检索无果,守档准由:希腊雅典/帖萨隆尼卡桥小型顾问)',
    kpn='—(R65 询问无果,守档准由)',
    facts=[{'dim': 'R65 查询注', 'text': 'alfa-tech.gr 本体无公开沟他件;守档准由', 'quote':'(web_search 2026-10-07:无有效结果)', 'url': '(沙箱日志)'}],
    fihadd='搜索无果,守档准由')

put('B-131',
    head='Nikolaos Giovanopoulos(Edessa, Central Macedonia;ien.gr 无公开相关条;'
         '**LinkedIn 同名画像存在但职业=机械工程师/HSE Consultant(21 年 Edessa)与 Mic 谱本体不完全同款**——同名人保不能保证,守档准由',
    kpn='—(同名 LinkedIn 机械工程师/HSE 或同谱,不保确;R65 守档准由)',
    facts=[{'dim': 'R65 同名混淆注', 'text': 'LinkedIn「Nikolaos Giovanopoulos Mechanical Engineer/HSE, Imperial College」同名画像与 ien.gr 不联;不采信',
            'quote': '(LinkedIn 搜索 2026-10-07:同名 HSE consultant,与 ien.gr / MikroTik 无关联证据)',
            'url': '(沙箱核验日志)'}],
    fihadd='同名 HSE 保但不能证=守档准由')

put('B-124',
    head='Georgios Papageorgiou / DSlab(dslab.gr;R65 检索多同名画像——KMicro Tech 软件工程师/爱琴海大学 ISLab 数据新闻 PhD/MIT 神经科学；不采信;守档准由)',
    kpn='—(多同名画像但均职业不同=不采信守档准由)',
    facts=[{'dim': 'R65 同名注', 'text':'「Georgios Papageorgiou」多重同名者(KMicro/爱琴海/MIT)；与 dslab.gr 无关联；不采信',
            'quote':'(LinkedIn 搜索 2026-10-07：三处同名画像，皆与 DSlab 不联)', 'url': '(沙箱核验日志)'}],
    fihadd='同名多问占画，守档准由')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 9 批（希腊/意大利/奥地利/匈牙利顾问群）',
       'scope': 'B-163 Fastnet/Marchetti / B-155 Matrix Somma / B-121 EXA Solutions / B-080 LazyBear / B-110 Engetsberger / B-127 Analytis / B-131 Giovanopoulos / B-124 DSlab',
       'records': [by[c] for c in ('B-163', 'B-155', 'B-121', 'B-080', 'B-110', 'B-127', 'B-131', 'B-124')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第9批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 9 批 8 户落盘')
