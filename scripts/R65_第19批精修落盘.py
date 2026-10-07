# -*- coding: utf-8 -*-
"""R65 B 类深挖第 19 批:法国 6 户收尾。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 19 批精修 = R57 转写 + 本轮 pappers/verif 新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-524',
    head='HD TECHNOLOGY / HIGH DESIGN TECHNOLOGY(SIREN 390778769;Bron Parc Saint Exupéry 6 rue Maryse Bastié,Lyon 东区；1993-04-05 创，应用软件开发/IT 服务；'
         '**Denis Richard = Directeur Général（2022-08-05 在任，1964-10 生 61 岁）**;503 BROADWAY(SIREN 539109082)= Président 法人（2022-06-30 在任）;10-19 员工，€1-2M 营收 monreseau-it；小老谱 1993',
    kpn='Denis Richard = Directeur Général（2022 在任）;503 BROADWAY 法人主席位)',
    kp=[{'name': 'Denis Richard', 'role': 'Directeur Général（总经理）', 'contact': '经 hdtechnology.fr / +33 472146890', 'status': 'pappers + monreseau-it 双源', 'source': 'https://www.pappers.fr/entreprise/high-design-technology-hd-technology-390778769'}],
    facts=[{'dim': 'R65 登记/实名', 'text': 'HD TECHNOLOGY Bron(Lyon) 390778769 · 1993 创 · Denis Richard DG 2022 · €1-2M/10-19 谱位',
            'quote': 'Denis Richard Directeur général 61 ans - 10/1964 Depuis le 05/08/2022 … High Design Technology - Hd Technology : Édition de logiciels applicatifs … Effectif: 10 à 19 salariés, Chiffres d\'affaires: 1 à 2 M€',
            'url': 'https://www.monreseau-it.fr/revendeur/hd-technology-390778769.htm'}],
    fihadd='Lyon 小老谱；Richard 新掌舵 2022')

put('B-523',
    head='FGET International(SIREN(Genas 69740),1984-01-06 创（42 年老谱！);'
         '**Gil Guedj = Président de SAS（主席，1947 生 79 岁）;Jefferson Guedj = Directeur Général（总经理，1988 生 38 岁，亲家接棒）**;'
         '谱型=电子与电信设备/部件大宗批发（Commerce de gros 4652);10-19 员工，€5.86M 营收；04 72 79 64 15 / info@fget.fr;CJ2L 协调主席',
    kpn='Gil Guedj = Président(79 岁 1947 生）;Jefferson Guedj = DG（1988 生 38 岁接棒）',
    kp=[{'name': 'Gil Guedj', 'role': 'Président de SAS', 'contact': 'info@fget.fr / 04 72 79 64 15', 'status': 'infonet 双源', 'source': 'https://infonet.fr/dirigeants/66a9dcb541b8769963e29093/'},
        {'name': 'Jefferson Guedj', 'role': 'Directeur Général（1988 生二代接棒）', 'contact': '同上', 'status': 'infonet/pappers 双源', 'source': 'https://infonet.fr/dirigeants/66a9dcb541b8769963e290e3/'}],
    facts=[{'dim': 'R65 登记/实名', 'text': 'FGET Genas 1984 42 年老谱 · Gil Guedj 79 主+Jefferson Guedj 38 接棒 · €5.86M 电子通件批发',
            'quote': 'Gil Guedj né en 1947 … Président de SAS … Jefferson Guedj né(e) en 1988 … Directeur Général … CA : 5.86 M',
            'url': 'https://infonet.fr/dirigeants/66a9dcb541b8769963e29093/'}],
    fihadd='Genas 42 年老谱 5.9M€;Guedj 父子接棒位')

put('B-254',
    head='VODENN SAS(SIREN 841882962,60 Impasse du Hameau des Guiols, 83210 La Farlède(Var 普罗旺斯）;2018-08-23 创，SAS €15K 本，1-2 员工微企；'
         '**Dorian Pistolesi = Président（1983-05 生 43 岁）+ Julien Launay = Directeur Général（1984-02 生，2019-05-02 在任）**;'
         '6201 编程/IT 咨询',
    kpn='Dorian Pistolesi = Président;Julien Launay = DG',
    kp=[{'name': 'Dorian Pistolesi', 'role': 'Président', 'contact': '经 vodenn.fr', 'status': 'verif + pappers 双源', 'source': 'https://www.verif.com/societe/VODENN-841882962/'},
        {'name': 'Julien Launay', 'role': 'Directeur Général(2019-05 在任）', 'contact': '同上', 'status': '同源', 'source': '同上'}],
    facts=[{'dim': 'R65 登记/实名', 'text': 'VODENN SIREN 841882962 · La Farlède(Var) 2018 创微企 · Pistolesi 主+ Launay DG',
            'quote': '841882962 Siret … Dorian PISTOLESI Président … Julien LAUNAY Directeur Général … La Farlede … Société par actions simplifiée … Capital 15 000 €',
            'url': 'https://www.verif.com/societe/VODENN-841882962/'}],
    fihadd='Var 建议味 2018 新谱；Pistolesi+Launay 二位'),

put('B-234',
    head='Adnan Rihan(法国谱主位；**REDVISE LTD(Companies House 12906418，英国 Pvt Ltd,2020-09-25 登记,London Covent Garden WC2H 9JQ)任职：Directeur(2020-09-25 在任，France 居民）+PSCs(重点控股）**;',
    kpn='Adnan Rihan = REDVISE LTD Director + PSC,France 居民，Lord Adnan Rihan',
    kp=[{'name': 'Adnan Rihan', 'role': 'REDVISE LTD 董事 + PSC(PSD 法国居民）', 'contact': '经 redvise.fr / 71-75 Shelton Street London WC2H 9JQ', 'status': 'b2bhint/Companies House 实名', 'source': 'https://b2bhint.com/ru/company/gb/redvise-ltd--12906418'}],
    facts=[{'dim': 'R65 联动核正', 'text': 'B-234 Adnan Rihan = REDVISE LTD(UK 12906418)· REDVISE B-251 谱联动：同法人主体双谱口，是法国→英国双实体谱',
            'quote': 'Lord Adnan Rihan Лицо, обладающее значительным контролем … Rihan, Adnan, Lord Директор Страна проживания France … REDVISE LTD 12906418 71-75 Shelton Street',
            'url': 'https://b2bhint.com/ru/company/gb/redvise-ltd--12906418'}],
    fihadd='B-234=B-251 联动谱（一主双实体英+法）')

put('B-251',
    head='REDVISE（法国谱主；**同 B-234 Adnan Rihan = 同主位实体谱**：REDVISE LTD(UK 12906418, London Covent Garden WC2H 9JQ, 2020-09-25 创）= 英侧谱载体）',
    kpn='Adnan Rihan（同 B-234 谱口径）)',
    kp=[{'name': 'Adnan Rihan', 'role': 'Director+PSC', 'contact': '经 redvise.fr', 'status': '同 B-234', 'source': 'https://b2bhint.com/ru/company/gb/redvise-ltd--12906418'}],
    facts=[{'dim': 'R65 谱联动', 'text': 'B-251 Redvise 与 B-234 Adnan Rihan 同主双实体：英国 REDVISE LTD 12906418 谱载体',
            'quote': '（同 B-234 R65 口径）', 'url': 'https://b2bhint.com/ru/company/gb/redvise-ltd--12906418'}],
    fihadd='同 B-234 谱联动，一主双实体')

put('B-230',
    head='ACTN（法国；R65 搜索谱不实净——MICROTIC Cayenne/MIKIT 同名噪声已排除；守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无谱本体净果（Cayenne MICROTIC/Rueil Malmaison MIKIT 同名他人已排除）;R65 守档准由', 'quote':'(web_search 2026-10-07：同名他人盲目排除）', 'url': '（沙箱核验日志）'}],
    fihadd='同名噪声排除后守档准由')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 19 批（法国 6 户收尾）',
       'scope': 'B-524 HD Technology / B-523 FGET / B-254 VODENN / B-234 Adnan Rihan / B-251 Redvise / B-230 ACTN',
       'records': [by[c] for c in ('B-524', 'B-523', 'B-254', 'B-234', 'B-251', 'B-230')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第19批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 19 批 6 户落盘')
