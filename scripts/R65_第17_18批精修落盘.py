# -*- coding: utf-8 -*-
"""R65 B 类深挖第 18 批:芬兰/黑山/阿联酋/马耳他 4 户。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 18 批精修 = R57 转写 + 本轮登记新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-397',
    head='Fiseg Oy(Y-tunnus 3246003-6,Tampere Aurinkokuja 5 B(Kotipaikka Espoo);2021-11-10 创;'
         '**Tero Henrik Närhi = Toimitusjohtaja(CEO)**;5 员工；2024-12 €3.14M 营收(2-10M€ 级）;2025 €755K 营业利润；'
         '谱型=工业自动化产品进口/仓储/销售/组装/咨询（NACE 46641 电气批发）;Idem Safety/Antaira/Gefran 谱涵；'
         'myynti@fiseg.fi / 050 572 6268 脱明自曝',
    kpn='Tero Henrik Närhi = Toimitusjohtaja',
    kp=[{'name': 'Tero Henrik Närhi', 'role': 'Toimitusjohtaja(CEO)', 'contact': 'myynti@fiseg.fi / 050 572 6268', 'status': 'finder.fi + proff.fi 双源', 'source': 'https://www.finder.fi/Maahantuonti/Fiseg+Oy/Tampere/yhteystiedot/3691455'}],
    facts=[{'dim': 'R65 登记/实名', 'text': 'Fiseg Oy Y-tunnus 3246003-6 · Tampere/Espoo · 2021 创 · Tero Närhi CEO · €3.14M 营收 · Idem Safety/Antaira/Gefran',
            'quote': 'Yhtiön toimitusjohtaja on Tero Henrik Närhi … FISEG Oy 3246003-6 … Aurinkokuja 5b, 33420 Tampere … myynti@fiseg.fi … Idem Safety Antaira Gefran',
            'url': 'https://www.finder.fi/Maahantuonti/Fiseg+Oy/Tampere/yhteystiedot/3691455'}],
    fihadd='芬兰工业自动化进口实体；Närhi CEO 2021 创')

put('B-491',
    head="NETMONT d.o.o.(Jovana Tomaševića br. 30, Bar, Crna Gora;PIB 03157601, Reg 50807339;2017-10-10 创；"
         '**Vasilije Mišević = Izvršni direktor(执行董事） & 50% 业主；Slobodan Lalić = 50% 业主 & Ovlašćeni zastupnik(授权代表）**;'
         '谱型=Kdžičd 6120 Bežične telekomunikacije（黑山无线电信——Montenegro MikroTik 谱波长对应！)',
    kpn='Vasilije Mišević = Izvršni direktor(50%);Slobodan Lalić = 业主（50%)& Ovlašćeni zastupnik',
    kp=[{'name': 'Vasilije Mišević', 'role': 'Izvršni direktor(50% 业主）', 'contact': '经 netmont.me', 'status': 'companywall.me 实名', 'source': 'https://www.companywall.me/firma/netmont/MMxsQfYC'},
        {'name': 'Slobodan Lalić', 'role': 'Vlasnik(50%)+Ovlašćeni zastupnik', 'contact': '同上', 'status': '同上', 'source': '同上'}],
    facts=[{'dim': 'R65 凶件/实名', 'text': 'NETMONT d.o.o. Bar 2017-10-10 创 · PIB 03157601 · Mišević 50% exek + Lalić 50% 代表 · šifra 6120 无线电信',
            'quote': 'Trenutni direktor tvrtke je VASILIJE MIŠEVIĆ. Vlasnik tvrtke je SLOBODAN LALIĆ(50,00%) … Vlasnik VASILIJE MIŠEVIĆ(50,00%), Osnivač … Osnovna djelatnost registrirana pod šifrom 6120 - Bežične telekomunikacije',
            'url': 'https://www.companywall.me/firma/netmont/MMxsQfYC'}],
    fihadd='黑山 Bar 无线电信实体双 50% 业主')

put('B-485',
    head='I C T INTERNATIONAL L.L.C(206 Sobha Ivory 1, Dubai, UAE;+971 4 2216756;'
         '**Mazhar Ali = Business Development Manager;Fakhar Mirza = Technical Director(zoominfo 双谱）**;11-50 员工；Abdullah Mustafa 同 BDM',
    kpn='Mazhar Ali = BDM;Fakhar Mirza = Technical Director',
    kp=[{'name': 'Mazhar Ali', 'role': 'Business Development Manager', 'contact': '+971 4 2216756 总线', 'status': 'zoominfo 自曝', 'source': 'https://www.zoominfo.com/c/i-c-t-international-llc/435477221'},
        {'name': 'Fakhar Mirza', 'role': 'Technical Director', 'contact': '同上', 'status': '同上', 'source': '同上'}],
    facts=[{'dim': 'R65 实名', 'text': 'ICT International Dubai · Mazhar Ali BDM + Fakhar Mirza Technical Director · 11-50 员工',
            'quote': 'Mazhar Ali Business Development Manager … Fakhar Mirza Technical Director … I C T International contact info: Phone number: +971 42216756 Website: www.ict-international.ae',
            'url': 'https://www.zoominfo.com/c/i-c-t-international-llc/435477221'}],
    fihadd='迪拜实体 BD+Technical 两口谱口开工'),

put('B-487',
    head='Accreda Ltd(Valletta, Malta + London UK,2006 创，€2005 6847;'
         '**谱型大校=niche 风险管理尽调顾问（不计 IT 分销）**——R57 档案归销售商，R65 判定：**R57 谱型分类可能误配或该司已转型**;'
         'Accreda Administration 业首谱 Directory;Konrad Abela 2010-2019 前 Director(2020 后 FIAU Malta 局长)',
    kpn='Konrad Abela 前身 Director (2010-2019)/Konrad 近期去 FIAU;R57 归销售商谱位日档影集疑计',
    facts=[{'dim': 'R65 谱型校注', 'text': 'Accreda Ltd Malta 2006 创=niche 风险尽调顾问，非 IT 分销；R57 归谱或也有同姓名重载；守档准由注',
            'quote': 'Accreda is a niche risk management firm specializing in the provision of research and due diligence solutions to the professional services, financial services, real estate and igaming sectors',
            'url': 'https://rocketreach.co/accreda-ltd-profile_b5ceb9dcf42e09a8'}],
    fihadd='误标谱险；实体=风险尽调顾问_收音守档')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 18 批（芬兰/黑山/阿联酋/马耳他）',
       'scope': 'B-397 Fiseg / B-491 Netmont / B-485 ICT Intl / B-487 Accreda',
       'records': [by[c] for c in ('B-397', 'B-491', 'B-485', 'B-487')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第17批补18.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 18 批 4 户落盘')
