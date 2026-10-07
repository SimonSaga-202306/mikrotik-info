# -*- coding: utf-8 -*-
"""R65 B 类深挖第 14 批: US/SK/CH 大户7户。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 14 批精修 = R57 转写 + 本轮登记新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-217',
    head='WESTech, spol. s r.o.(Stará Vajnorská 17, 831 04 Bratislava,IČO 35796111, DIČ 2020245557;2000-09-25 创,'
         'ELKO-RIGA/Zero 亲家合资血统;股本 €33.2K;'
         '**Ing. Matej Sršeň = konateľ/CEO(2000 创至今 26 年）**;Ing. Martin Strigač = konateľ(2025-03-24 新任）;Róbert Király 创始 konateľ(2000-2004)',
    kpn='Ing. Matej Sršeň = Konateľ/CEO(2000-至今 26 年）;Ing. Martin Strigač = konateľ(2025-03-24 新任）',
    kp=[{'name': 'Ing. Matej Sršeň', 'role': 'Konateľ / Generálny riaditeľ', 'contact': '经 westech.sk', 'status': 'orsr.sk/foaf.sk/kompass 三源', 'source': 'https://www.foaf.sk/35796111?locale=en'},
        {'name': 'Ing. Martin Strigač', 'role': 'Konateľ(2025-03-24 新任）', 'contact': '同上', 'status': 'foaf.sk 实名', 'source': '同上'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'WESTech s.r.o. Slovenská · IČO 35796111 · 2000-09-25 创 · Matej Sršeň 26 年 konateľ + Martin Strigač 2025-03 新任',
            'quote': 'Ing. Matej Sršeň Od 25.09.2000 … Ing. Martin Strigač Od 24.03.2025 … STARÁ VAJNORSKÁ 17 831 04 BRATISLAVA',
            'url': 'https://www.foaf.sk/35796111?locale=en'}],
    fihadd='斯洛伐克 2000 ELKO 合资老谱；Sršeň 26 年谱主')

put('B-381',
    head='Solution Box LLC(Miami, FL;IT & Telecommunications wholesaler 11-50 员工；'
         '**Eduardo Bicerne = General Manager & Co-owner(crunchbase 自曝)**;Claudio Muñoz = Sales Director(2012-09 至今 13+ 年,Miami;原 Argentina 血统）)',
    kpn='Eduardo Bicerne = GM & Co-owner;Claudio Muñoz = Sales Director(2012 至今 13+ 年）',
    kp=[{'name': 'Eduardo Bicerne', 'role': 'General Manager & Co-owner', 'contact': '经 solutionboxusa.com', 'status': 'crunchbase 自曝', 'source': 'https://www.crunchbase.com/organization/solution-box'},
        {'name': 'Claudio Muñoz', 'role': 'Sales Director(2012 至今 13+ 年）', 'contact': '同上', 'status': 'LinkedIn munozclaudio 自曝', 'source': 'https://www.linkedin.com/in/munozclaudio/'}],
    facts=[{'dim': 'R65 实名', 'text': 'Solution Box LLC Miami · Eduardo Bicerne GM&Co-owner · Claudio Muñoz Sales Director 2012-至今',
            'quote': 'Eduardo Bicerne: General Manager & Co-owner … Claudio Muñoz: Commercial Director Solution Box LLC Sep 2012 - Present 13 years 2 months',
            'url': 'https://www.crunchbase.com/organization/solution-box'}],
    fihadd=' Miami IT/电信批发头；Bicerne 家主谱口')

put('B-346',
    head='EPCOM(8301 NW 27th St Ste 1, Miami, FL 33122;2011 创；'
         '**Joseph Opyrchal = CEO(datanyze)**;Omar Kheir = COO/Chief Engineer;Freddie Crespo = VP-GM;'
         '谱型=security/监控/entry control/fire alarm/网络设备 51-200 员工 $19.1M 营收 ZoomInfo 口径;OXM 门牌线)',
    kpn='Joseph Opyrchal = CEO(datanyze);Omar Kheir = COO/Chief Engineer(prospectoo 口 '
         '径）;Freddie Crespo VP-GM',
    kp=[{'name': 'Joseph Opyrchal', 'role': 'CEO', 'contact': '经 epcom.net/epcom.com.mx 总线', 'status': 'datanyze 自曝', 'source': 'https://www.datanyze.com/companies/epcom/17613993'},
        {'name': 'Omar Kheir', 'role': 'COO/Chief Engineer', 'contact': '@epcom.net(模式提示）', 'status': 'prospectoo 自曝', 'source': 'https://prospectoo.com/company/EPCOM-35714742/'}],
    facts=[{'dim': 'R65 实名', 'text': 'EPCOM Miami 8301 NW 27th St · Joseph Opyrchal CEO · Omar Kheir COO/Chief Engineer · $19.1M 收 51-200 人 · 2011 创',
            'quote': 'Joseph Opyrchal ### CEO … Epcom headquarters are located at 8301 NW 27th St Ste 1, Miami, Florida, 33122, United States … Epcom $19.1M 51-200 2011',
            'url': 'https://www.datanyze.com/companies/epcom/17613993'}],
    fihadd='Miami 安全/监控互销 19M$；Opyrchal CEO 实首')

put('B-298',
    head='Alltron AG(Mägenwil, Switzerland;Competec/Brack.Alltron 集团；'
         '**Andrej Golob = Chief Sales Officer of Brack.Alltron + Executive Director of Alltron AG(2021-02 前 Alltron CEO)+主席谱位**;Stefan Fraude = CEO Brack.Alltron;Markus Mahler Verwaltungsrat 董事（2008 创；曾 Brack+Alltron CEO)；'
         '谱型=瑞士 IT/消费电 280,000+ SKU 批发；Fachhandel/Integrators/Installateurs 航道',
    kpn='Andrej Golob = Chief Sales Officer Brack.Alltron+Executive Director Alltron AG;Stefan Fraude = CEO Brack.Alltron',
    kp=[{'name': 'Andrej Golob', 'role': 'CSO Brack.Alltron/Executive Director Alltron AG', 'contact': '经 alltron.ch / brackalltron.ch', 'status': 'brackalltron.ch 组织页自曝+moneyhouse 管理位', 'source': 'https://brackalltron.ch/%C3%BCber-uns/organisation'},
        {'name': 'Stefan Fraude', 'role': 'CEO Brack.Alltron', 'contact': '同上', 'status': '同源', 'source': '同上'}],
    facts=[{'dim': 'R65 集团联动', 'text': 'Alltron AG Mägenwil · Competec Group 属 · 280K SKU 批发 · Golob CSO/Executive Director · Fraude CEO · Mahler 董事',
            'quote': 'Februar 2021 war ich CEO der Alltron AG … seit September 2024 Chief Sales Officer von Brack.Alltron und Executive Director der Alltron AG … Markus Mahler … seit 2008 Teil von Brack.Alltron',
            'url': 'https://brackalltron.ch/%C3%BCber-uns/organisation'}],
    fihadd='瑞士 Competec 大集团谱;280K SKU 批发')

put('B-221',
    head='GCOM 格鲁吉亚(Tbilisi;R65 搜索缺候选=守档准由；R57 所描 MikroTik 谱谱继续关注）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由（格鲁吉亚小谱业者）')

put('B-304',
    head='H2 HOLDING LLC / fortshpejt.com（科索沃 Prishtina;R57 已描谱；R65 搜索无果=守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote': '(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='科索沃谱守档准由')

put('B-452',
    head='Camacho - Engenheiros（葡萄牙；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote': '(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='葡萄牙谱守档准由')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 14 批（US/斯洛伐克/瑞士 大户 7 户）',
       'scope': 'B-217 WESTech / B-381 Solution Box / B-346 EPCOM / B-298 Alltron / B-221 GCOM / B-304 H2 / B-452 Camacho',
       'records': [by[c] for c in ('B-217', 'B-381', 'B-346', 'B-298', 'B-221', 'B-304', 'B-452')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第14批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 14 批 7 户落盘')
