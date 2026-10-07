# -*- coding: utf-8 -*-
"""R65 B 类深挖第 6 批:摩尔多瓦/马其顿/匈牙利 4 户。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd='', Unk=None):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 6 批精修 = R57 转写 + 本轮登记新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    if Unk: r['unknowns56'] = Unk + r['unknowns56']
    return r

put('B-211',
    head='PRIDE SYSTEM SRL(Chisinau, +373 60 844-266, office@pride.md;'
         '**谱型:摩尔多瓦 IT&C 品牌总代大团**——Microsoft/Cisco/MikroTik/Dell 等 leading suppliers B2B 门户;'
         'pride.md 是其官方 e-commerce 平台(B2B 为主);Chișinău Studentilor 7/10 门店',
    kpn='—(SRL PRIDE SYSTEM 董事实名待 e-gap/registru.md 检索)',
    facts=[{'dim': 'R65 谱位', 'text': '摩尔多瓦 IT&C 品牌总代:Microsoft/Cisco/MikroTik/Dell 全文安置;B2B 平台 pride.md',
            'quote': 'B2B platform for IT&C solutions … PRIDE SYSTEM … Microsoft, Cisco, MikroTik, Dell … office@pride.md +373 (60) 844-266',
            'url': 'https://e-catalog.md/ro/stores/pride'}],
    fihadd='摩多瓦 IT&C 大国总代=MikroTik 谱与 Cisco/Dell 共位')

put('B-510',
    head='Fallon Systems(马其顿/科索沃域;fallon.com.mk;**检索大噪音**——MikroTik 维基命中/多校准噪音,MikroTik 谱本体公开信亡);'
         'R57 守档准由=南巴尔干小谱商注意事项',
    kpn='—(搜索噪音高;未证实 David/Sere 项者,守档准由)',
    facts=[{'dim': 'R65 检索噪音注', 'text': 'Fallon Systems 名字被 MikroTik 泛义更替,上源多发上下文消牘;R65 未得有效谱位',
            'quote':'(web_search 2026-10-07:三条结果全为 MikroTik 本体信息,与 Fallon Systems 无关)',
            'url': '(沙箱噪声日志)'}],
    fihadd='搜索噪音要注:面谱本体 PubMedMikroTik 两记,守档准由不查通',
    Unk=['南巴尔干(马其顿/科索沃)谱位主体(语言/登记障)','KP 线索待 Apollo/AI 外源'])

put('B-081',
    head='CompMarket Hungary Zrt.(1044 Budapest, Megyeri út 53;Cg. 01-10-046934,Adószám 23126806-2-41;'
         '2011-01-20 创立,20M HUF 股本;**2025 财报营收 13.33 亿 HUF ≈ €34M**;ICT 批发大分销;'
         '**董事 Szabó Balázs + Tóth Zoltán(companywall.hu 实名)**;01/2731055, info@compmarket.hu)',
    kpn='Szabó Balázs + Tóth Zoltán = igazgatósági tag(董事会两成员,companywall.hu 实名)',
    kp=[{'name': 'Szabó Balázs', 'role': 'Igazgatósági tag(董事会成员)', 'contact': 'info@compmarket.hu / 01/2731055', 'status': 'companywall.hu 实名', 'source': 'https://www.companywall.hu/v%C3%A1llalat/compmarket-hungary-zrt/MMC0DERq'},
        {'name': 'Tóth Zoltán', 'role': 'Igazgatósági tag(董事会成员)', 'contact': '同上', 'status': '同源', 'source': '同 companywall.hu'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'Cg 01-10-046934 · 2011 创 · 20M HUF 股本 · 2025 营收 13.33 亿 HUF(≈€34M) · Szabó/Tóth 两董事',
            'quote': 'Net revenue: 13 332 897 800 … A vállalat jelenlegi igazgatói: Szabó Balázs, Tóth Zoltán',
            'url': 'https://www.ceginformacio.hu/cr9318296185_EN'}],
    fihadd='€34M 级匈牙利 ICT 大分销,两董事实名=B-005 走年谱口')

put('B-084',
    head='EXPERT Kereskedelmi és Informatikai Zrt.(1043 Budapest, Aradi utca 16-20;Adószám 14241499-2-44, Cg. 01-10-045926;'
         '2008 创立;**Balázs Attila vezérigazgató(CEO 总裁, 1025 Budapest Cimbalom 12 住所谱)+ Francia Róbert cégvezető(经理)**;'
         '50-99 员工;ICT 批发+web 商城:Tesco International 跨国 4 国供应合同,营收超100万产品 abszes()',
    kpn='Balázs Attila = vezérigazgató(CEO);Francia Róbert = cégvezető(经理)',
    kp=[{'name': 'Balázs Attila', 'role': 'Vezérigazgató(总裁/CEO)', 'contact': 'info@expert.hu / 01/4502440', 'status': 'nemzeticegtar.hu + companywall.hu + 官网 ceginformacio 三源实名', 'source': 'https://www.nemzeticegtar.hu/expert-zrt-e10481872.html'},
        {'name': 'Francia Róbert', 'role': 'Cégvezető(经理)', 'contact': '同上', 'status': '同源', 'source': '同 nemzeticegtar.hu'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'Expert Zrt.adoszám 14241499-2-44, 2008 创;Balázs Attila vezérigazgató + Francia Róbert cégvezető 两实名',
            'quote': 'Balázs Attila (an: Szabó Ilona) vezérigazgató … Francia Róbert (an: Kanyó Gizella) cégvezető … 50 - 99 Fő',
            'url': 'https://www.nemzeticegtar.hu/expert-zrt-e10481872.html'},
            {'dim': 'R65 国际化位', 'text': 'Tesco International 4 国供应合同;SKU 100万件仓储位;匈牙利 top 500 商口',
             'quote': 'Tesco International szerződés, 4 országra szállítás … Expert Zrt bekerült a magyar top 500 cégbe',
             'url': 'https://www.expert.hu/ceginformacio-hceginfo.html'}],
    fihadd='top 500 匈牙利 ICT 分销;4 国 Tesco 国际合同=谱口在 Ma 尔')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 6 批(摩尔多瓦/马其顿/匈牙利)',
       'scope': 'B-211 Pride.md / B-510 Fallon Systems / B-081 CompMarket Hungary / B-084 Expert Zrt',
       'records': [by[c] for c in ('B-211', 'B-510', 'B-081', 'B-084')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第6批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 6 批 4 户落盘')
