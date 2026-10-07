# -*- coding: utf-8 -*-
"""R65 B 类深挖第 11 批:法国 5 + 西班牙 2。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 11 批精修 = R57 转写 + 本轮登记/媒体新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-252',
    head='SEWAN(法国电信 ETI 大户;2007 年 Alexis de Goriaïnoff + 3 名联合创始人联合创立——从同一运营商 4 人「全员辞职」创办起家;'
         '谱型=Cloud+Télécoms 生态/自创 SaaS「Sophia」;300-1000 员工/75M€ 收；总部巴黎+贝尔福/蒙彼利埃；西班牙/德/意/荷国际化);'
         '**Alexis de Goriaïnoff = PDG & 联合创始人**;Philippe Moutinho 同站 PDG 口径(疑子站/分公司)',
    kpn='Alexis de Goriaïnoff = PDG & Cofondateur(官网 + LesEchos/BFM 双源);Philippe Moutinho 同城站 PDG 位',
    kp=[{'name': 'Alexis de Goriaïnoff', 'role': 'PDG et Cofondateur(集团 CEO/联合创始人)', 'contact': '经 sewan.fr 联系页', 'status': 'sewan.fr + business.lesechos.fr 双源', 'source': 'https://business.lesechos.fr/entrepreneurs/success-stories/sewan-pixopolitan-et-opendatasoft-sur-l-entreprise-bfm-les-chos-316692.php'}],
    facts=[{'dim': 'R65 体量+位', 'text': 'Sewan 2007 创 · 4 创始人同人离职创办 · 300-1000 员工 · 75M€ 收 · Sophia 生态 · 西班牙已并入 · 德/意/荷在望',
            'quote': 'Alexis de Goriaïnoff a créé Sewan en 2007 … 75 millions d’euros de chiffre d’affaires et emploie 300 personnes … Sophia … Nourrissant des ambitions européennes',
            'url': 'https://business.lesechos.fr/entrepreneurs/success-stories/sewan-pixopolitan-et-opendatasoft-sur-l-entreprise-bfm-les-chos-316692.php'}],
    fihadd='SEWAN 法国 ETI 巨号;同代电信云族 75M€/自建 Sophia')

put('B-248',
    head='Osmozis S.A.(Montpellier;2005 年 Gérard Tremblay + Yves Boulot 联合创;'
         '谱型=露营地/度假村 WiFi & IoT 数字化欧洲头号专家——2600+ sites/108 员工/2023 €12.8M;2017 Euronext 上市(FR0013231180),2024-05 被 Passman 集团收购 €15/股 OPA;'
         '**KP:Gérard Tremblay+Yves Boulot 联合创始人;Pierre-Benoit Labbé 总经理(现任)**',
    kpn='Gérard Tremblay + Yves Boulot = 联合创始人;Pierre-Benoit Labbé = Directeur Général(现任, Passman 收购在架仍原位)',
    kp=[{'name': 'Gérard Tremblay', 'role': 'Co-fondateur', 'contact': '经 osmozis.com', 'status': 'gazette-du-midi 图照双源', 'source': 'https://gazette-du-midi.fr/au-sommaire/entreprises/osmozis-specialiste-de-la-digitalisation-des-campings-accelere-son'},
        {'name': 'Yves Boulot', 'role': 'Co-fondateur', 'contact': '同上', 'status': '同源', 'source': '同上'},
        {'name': 'Pierre-Benoit Labbé', 'role': 'Directeur Général(总经理)', 'contact': '同上', 'status': '同源', 'source': '同上'}],
    facts=[{'dim': 'R65 谱位+收购', 'text': 'Osmozis 露营度假 WiFi 欧洲一号 2600+ 站 · 108人/12.8M€(2023) · 2017 Euronext 上市 FR0013231180 · 2024-05 Passman 15€/股 收购',
            'quote': 'Osmozis, spécialiste de la transition digitale des campings … équipe plus de 2 600 sites en Europe … 108 personnes … 12,8 M€ … annonce rejoindre le groupe Passman … Gérard Tremblay et Yves Boulot, cofondateurs d’Osmozis',
            'url': 'https://gazette-du-midi.fr/au-sommaire/entreprises/osmozis-specialiste-de-la-digitalisation-des-campings-accelere-son'}],
    fihadd='露营 WiFi 全欧大户;Passman 收购在架')

put('B-231',
    head='ALLNET France SAS(SIREN 979508009,2023-09-14 创立,SAS €50K 本，Carcassonne 96 Rue Lamarck;'
         '**Bastien Gonon = Président & CEO & Co-Fondateur(TU Delft aerospace+航天咨询转电信血统)；Thierry, Antoine, Raymond Gonon 曾 Président→Directeur Général(gramps/亲联络链)；'
         'Tjorben Teunissen 联合创始人；Gabriel Janicot Head of Product;1-10 员工谱注「Votre distributeur pour tout ce qui concerne les réseaux, les télécommunications et l\'IoT」(谱型注:R65 登记 SIREN 979508009 显示 2023 新创——谱/B-138 Bauer 1991 母体「ALLNET」同属不明，谱位作同族候选标记)',
    kpn='Bastien Gonon = Président/CEO/Co-Fondateur(TU Delft 航空+咨询血统);Tjorben Teunissen 联合创始人;Thierry Gonon 家族谱位',
    kp=[{'name': 'Bastien Gonon', 'role': 'Président / CEO / Co-Fondateur', 'contact': '经 allnet.de/allnet France 页', 'status': 'intch + lefigaro 双源自曝', 'source': 'https://entreprises.lefigaro.fr/allnet-france-11/entreprise-979508009'},
        {'name': 'Tjorben Teunissen', 'role': 'Co-Founder', 'contact': '同上', 'status': 'prospeo 自曝', 'source': 'https://prospeo.io/c/allnet-france'}],
    facts=[{'dim': 'R65 登记+KP', 'text': 'ALLNET France SAS · SIREN 979508009 · 2023-09-14 创 · Carcassonne · Bastien Gonon P+CEO+CoF · 1-10 员工',
            'quote': 'Président : GONON Bastien ; Directeur général : GONON Thierry … Date d\'immatriculation : 14/09/2023 … Votre distributeur pour tout ce qui concerne les réseaux, les télécommunications et l\'IoT',
            'url': 'https://entreprises.lefigaro.fr/allnet-france-11/entreprise-979508009'}],
    fihadd='Gonon 家族新创 2023;谱与德国母体联动候选(供联动判断;不证不动)')

put('B-246',
    head='NETCOM GROUP(法国;R65 检索多名合项：**Pantin NETCOM GROUP(SIRET 453006314 00042)= Jamal Assraoui Président+Mohamed/Said Benamrouche 双 Directeurs Généraux 通讯/安全谱**——口径高度匹配谱本体；'
         '另有：Paris 75010 75020 SARL 同名/45 通讯 多同六，均非谱本体（R65 均不采信）',
    kpn='候选：Jamal Assraoui = Président;Mohamed Benamrouche+Said Benamrouche = 双 DG(Pantin 谱位；候选，未最终确证）',
    kp=[{'name': 'Jamal Assraoui', 'role': 'Président(Pantin NETCOM GROUP, 候选）', 'contact': '经 58 Rue Denis Papin 93500 Pantin 总线', 'status': 'edecideur 候选，未最终证', 'source': 'https://edecideur.info/edecideur.php?q=198020130215benmoh-benamrouche-mohamed-directeur-general-4652z-45300631400042-netcom-group-58-rue-denis-papin-93500-pantin'}],
    facts=[{'dim': 'R65 候选谱', 'text': 'Pantin NETCOM GROUP SIRET 453006314 = Assraoui prez + Benamrouche 双 DG 位通讯谱；候选未最终证（Paris 75010/75020 同名他人已排除）',
            'quote': 'Dirigeant(s) de NETCOM GROUP sont : JAMAL ASSRAOUI Président, Mohamed BENAMROUCHE Directeur général, Said BENAMROUCHE Directeur général',
            'url': 'https://edecideur.info/edecideur.php?q=198020130215benmoh-benamrouche-mohamed-directeur-general-4652z-45300631400042-netcom-group-58-rue-denis-papin-93500-pantin'}],
    fihadd='KP 候选（Pantin 双 Benamrouche 谱）；未最终证=守档准由')

put('B-522',
    head='APLUS Systeme Automation SA(SIREN 345398556,1988-05-15 创，SAS €811.8K 本，Saint-Michel-sur-Orge;'
         '**Carlos Cabanita = Président Directeur Général;béatrice Cabanita 财务总监；Delphine Dassibat 采购总监；Vincent Chevillot DSI;'
         '谱型=工业计算机/工控大屏（affichage-digital/aplus-defense 子站） ISO 9001+AQAP 2110 认证；2024 €15.26M 营收；20-49 员工',
    kpn='Carlos Cabanita = PDG(Presdir Directeur Général);Béatrice Cabanita 财务总监',
    kp=[{'name': 'Carlos Cabanita', 'role': 'Président Directeur Général', 'contact': '经 aplus-sa.com', 'status': 'pappers/manageo/kompass 三源实名', 'source': 'https://www.manageo.fr/entreprises/345398556.html'}],
    facts=[{'dim': 'R65 谱+体量', 'text': 'APLUS SA 1988 创 · €15.26M 2024 营收(20-49 员工） · Saint-Michel-sur-Orge · 工控大屏/defense 三站 · ISO 9001/AQAP 2110 · Cabanita 总统',
            'quote': 'Capital social · 811 800 EURO … Dernier chiffre d\'affaires connu · 15 263 854 € (2024) … Cabanita Carlos · Président Directeur Général · AQAP 2110 : Expire le 30/12/2029 · ISO: 9001',
            'url': 'https://www.manageo.fr/entreprises/345398556.html'}],
    fihadd='工控大屏大三子 15M€;Cabanita 总统');

put('B-482',
    head='Todo Telecom S.L.(Denia, Alicante;Pol. Ind. Juyarco 40A;16+ 年谱；'
         '**谱型=Ubiquti/Tp-Link/MikroTik/Iris/Fte/Strong/Technisat 多品牌电信摄像 CCTV WiFi 分销；谱本体站「Distribuidor oficial MikroTik」自曝**;'
         'webinfo@todotelecom.com',
    kpn='—(S.L. administrador registre mercantil Alicante 收费墙；R65 谱位+地址件已足）',
    facts=[{'dim': 'R65 谱/自曝', 'text': 'Todo Telecom S.L. Denia(Alicante)16 年 · multi-brand official MikroTik distributor 自曝 · Madrigueres Sud/P.I. Juyarco 40A · webinfo@todotelecom.com',
            'quote': 'Distribuidor oficial: TodoTelecom … Distribuidores oficiales de MikroTik en España … Pol.Ind.Juyarco 40A / Denia (Alicante) webinfo@todotelecom.com',
            'url': 'https://mikrotikspain.es/contacto.html'}],
    fihadd='西班牙官方 MikroTik 分销名录;Alicante Denia 址谱')

put('B-469',
    head='Infortisa S.L.(C/ del Pozo 1, 46115 Alfara del Patriarca, Valencia;+34 961 309 006;'
         '**谱型=Valencia IT/技术 mayorista 龙头——MikroTik/Ubiquiti 等多品牌 official majorista 自曝**(谱本体站 fabricante/mikrotik 栏:「distribuidor oficial y mayorista para comprar al por mayor」)',
    kpn='—(S.L. administrador registre mercantil Valencia 收费墙；R65 谱位+地址件已足）',
    facts=[{'dim': 'R65 谱/地址', 'text': 'Infortisa S.L. Alfara del Patriarca(Valencia)· 961 309006 · MikroTik mayorista 自曝',
            'quote': 'In Infortisa, mayorista, proveedor y distribuidor oficial … INFORTISA Mayorista de informática y tecnología Infortisa, S.L.,(+34) 961 309 006, C/ del Pozo, 1, 46115 Alfara del Patriarca, Valencia',
            'url': 'https://www.infortisa.com/fabricante/mikrotik/'}],
    fihadd='Valencia majorista 巨口;self-staged official')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 11 批（法国 5 + 西班牙 2)',
       'scope': 'B-252 Sewan / B-248 Osmozis / B-231 ALLNET France / B-246 NETCOM / B-522 APLUS / B-482 Todo Telecom / B-469 Infortisa',
       'records': [by[c] for c in ('B-252', 'B-248', 'B-231', 'B-246', 'B-522', 'B-482', 'B-469')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第11批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 11 批 7 户落盘')
