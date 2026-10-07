# -*- coding: utf-8 -*-
"""R65 B 类深挖第 13 批:爱尔兰/葡萄牙/罗马尼亚/波兰/捷克 7 户。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 13 批精修 = R57 转写 + 本轮登记新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-279',
    head='Irish Wireless / BluePrint Wireless Ltd(2001 年由 **Stephen Hall + Gurmukh Neote 双创立**，Smithstown Industrial Estate, Shannon, County Clare;'
         '谱型=25 年爱尔兰无线专业商：天线/室内外设备/电缆全品+培训咨询;Mission「Making Wireless EASY」;$3M 收 3 员工精干;'
         'RocketReach：Stephen Hall Owner；矿井/学校/酒店/郡大网实绩',
    kpn='Stephen Hall = 合伙人/Owner(2001 创);Gurmukh Neote = 联合创始人',
    kp=[{'name': 'Stephen Hall', 'role': 'Co-founder/Owner', 'contact': '经 irishwireless.net', 'status': 'irishwireless.net about_us + rocketreach 双自曝', 'source': 'https://irishwireless.net/about_us'},
        {'name': 'Gurmukh Neote', 'role': 'Co-founder', 'contact': '同上', 'status': '同源', 'source': '同上'}],
    facts=[{'dim': 'R65 实名', 'text': 'Irish Wireless(BluePrint Wireless Ltd)2001 = Stephen Hall + Gurmukh Neote 创立;Shannon Clare;无线+培训咨询 25 年',
            'quote': 'Irish Wireless (BluePrint Wireless Ltd) was established in 2001 by Networking and IT Specialists Stephen Hall and Gurmukh Neote. Based in Smithstown, Shannon, County Clare, Ireland',
            'url': 'https://irishwireless.net/about_us'}],
    fihadd='爱尔兰 25 年老谱 Stephen Hall 本位确认$3M/3人精干')

put('B-456',
    head='TRUENET / Truenet, Lda.(NIF 513514139, Rua do Mosteiro 89, 4465-703 Leça do Balio, Portugal;'
         '**2019 MUM Portugal 官方 exhibitor(MikroTik User Meeting 名录)+ LigoWave 葡萄牙官方分销(+351 936 794 301)**;'
         'tub 谱型=葡萄牙无线/天线专业分销线',
    kpn='—(Lda. sócio gerente conservatória do registo Porto 收费墙;R65 谱位+exhibitor 档案已足）',
    facts=[{'dim': 'R65 谱/档案', 'text': 'Truenet Lda NIF 513514139 · 2019 MUM PT exhibitor · LigoWave Portugal 官方分销',
            'quote': 'Truenet (Portugal) [2019 MUM PT exhibitor] … TRUENET Distributor in Portugal Tel: +351 936 794 301 [ligowave.com 官方名录] … NIF 513514139 Rua do Mosteiro, 89 4465-703 Leça do Balio',
            'url': 'https://mum.mikrotik.com/2019/PT/exhibitors/PT'}],
    fihadd='葡萄牙 MikroTik 官方 MUM 谱位+LigoWave 分销联动')

put('B-313',
    head='Dipol Connect SRL(CIF RO26051890, J40/9512/2009;2009-10-01 创,București Sector 2 Str. Fabrica de Gheață 8/Carol Ghica Tei 81 老址桥；'
         '谱型=IT 网络监控 TV/Satelit+光纤电缆制造+电子维修(CAE 4652/2731/3313);2024 营收 7,459,353 RON ≈€1.5M/净利 356K RON/6 员工;'
         'office@dipolnet.ro / +40 31 428 1005',
    kpn='—(SRL adminstrator ONRC București 收费墙;R65 谱位+财务档案已足）',
    facts=[{'dim': 'R65 登记/财务', 'text': 'Dipol Connect SRL CIF 26051890 · 2009-10-01 创 · 2024 营收 7.46M RON/净利 356K · 6 员工 · 光纤电缆制造+电子维修谱',
            'quote': 'Fiscal Code 26051890 … cifră de afaceri 2024: 7.459.353 RON … 6 [employees] … Fabricarea de cabluri cu fibră optică … Repararea echipamentelor electronice și optice',
            'url': 'https://www.totalfirme.ro/dipol-connect-srl-26051890'}],
    fihadd='București 制造实体 1.5M€/6 人谱支')

put('B-274',
    head='ELTROX Sp. z o.o.(Częstochowa ul. Warszawska 74;NIP 6462490527, KRS 0000175807, REGON 276916481；股本 560K zł;'
         '**Zbigniew Dąbrowski = Prezes Zarządu(董事会主席)**;Barbara Otolińska 大股东（504/560 股=90%);Wiktor Dąbrowski 小股东；Michał Piotr Dawid 理事；电信设备配件谱',
    kpn='Zbigniew Dąbrowski = Prezes Zarządu(董事会主席);Barbara Otolińska 大股东（90%)',
    kp=[{'name': 'Zbigniew Dąbrowski', 'role': 'Prezes Zarządu（主席）', 'contact': '经 eltrox.pl/finanse@eltrox.pl', 'status': 'aleo/KRS 双源实名', 'source': 'https://aleo.com/int/company/eltrox-pl'},
        {'name': 'Barbara Otolińska', 'role': '大股东（90%)', 'contact': '同上', 'status': '同源', 'source': '同上'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'ELTROX KRS 0000175807 · NIP 6462490527 · Częstochowa Warszawska 74 · Z.Dąbrowski Prezes+ B.Otolińska 90% 大股东',
            'quote': 'Zbigniew Dąbrowski Prezes Zarządu … Barbara Otolińska 504 udziały … ELTROX sp. z o.o. z siedzibą w Częstochowie (KRS, 0000175807 NIP 6462490527)',
            'url': 'https://aleo.com/int/company/eltrox-pl'}],
    fihadd='Częstochowa 大国谱；Otolińska 家族结构 90% 股主')

put('B-263',
    head='FYR-SYSTEMS Sp. z o.o.(Warszawa ul. A. Felińskiego 46/2;NIP 5252863223, KRS 0000900908, REGON 388992660；股本 50K zł;'
         '**Rafał Artur Siewicz = Prezes Zarządu（董事会主席，80/100 股=80%)+ Katarzyna Anna Grochowska Siewicz 理事（20/100)**;'
         '谱型=IT 系统集成商；Krzysztof Krawczyk 公开面谱谱口（o-nas 页面）',
    kpn='Rafał Artur Siewicz = Prezes Zarządu(80%);Katarzyna Grochowska Siewicz 理事（20%);Krzysztof Krawczyk 公开 IP 面谱',
    kp=[{'name': 'Rafał Artur Siewicz', 'role': 'Prezes Zarządu', 'contact': 'kontakt@fyr-systems.pl / +48 513 130 332', 'status': 'aleo/KRS + 官网 o-nas 双源', 'source': 'https://aleo.com/int/company/fyr-systems-spolka-z-ograniczona-odpowiedzialnoscia-warszawa'},
        {'name': 'Krzysztof Krawczyk', 'role': '对外面谱（Integrator/O NAS 页主导）', 'contact': '同上', 'status': 'fyr-systems.pl 官网自曝', 'source': 'https://fyr-systems.pl/o-nas/'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'FYR-SYSTEMS KRS 0000900908 · NIP 5252863223 · Warszawa Felińskiego 46/2 · R. Siewicz Prezes 80% · Krzysztof Krawczyk 官网自曝',
            'quote': 'Rafał Artur Siewicz Prezes Zarządu … kontakt@fyr-systems.pl +48 513 130 332 … KRS: 0000900908 NIP: 5252863223',
            'url': 'https://fyr-systems.pl/o-nas/'}],
    fihadd='Warszawa 集成商实体；Siewicz 家族结构')

put('B-192',
    head='ATEsystem s.r.o.(Ostrava,IČO 01392042;2013-02 创；'
         '**Michal Harhaj = jednatel 2013-至今(13 年)**;Ing. Dušan Šelong = jednatel(2025-12-08 新任）；Petr Bilík 前 jednatel(2013-2025-12-08);'
         '谱型=自动测试/机检/illumination 系统组件；data schránka jxtq5qi',
    kpn='Michal Harhaj = jednatel(2013-至今，13 年）;Ing. Dušan Šelong = jednatel(2025-12-08 新任）',
    kp=[{'name': 'Michal Harhaj', 'role': 'Jednatel(13 年核心）', 'contact': '经 atesystem.cz', 'status': 'rejstrik.penize.cz 实名', 'source': 'https://rejstrik.penize.cz/01392042-atesystem-s-r-o'},
        {'name': 'Ing. Dušan Šelong', 'role': 'Jednatel(2025-12 新任)', 'contact': '同上', 'status': '同源', 'source': '同上'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'ATEsystem s.r.o. Ostrava IČO 01392042 · Harhaj jednatel 2013· Šelong jednatel 2025-12-08 新任；自動测试/机检谱',
            'quote': 'Jednatel Michal Harhaj Den vzniku funkce: 8. únor 2013 … Ing. Dušan Šelong Hrabyně 264 … jednatel 8. 12. 2025 … Jsme specialisté na automatické testování, kamerové inspekce',
            'url': 'https://rejstrik.penize.cz/01392042-atesystem-s-r-o'}],
    fihadd='Ostrawa 自动测试机检谱；Harhaj 13 年 Jednatel')

put('B-208',
    head="eD system a.s.(=B-208「eD's system Czech」**实体映射核正**;Ostrava 大 IT 分销商；"
         "**Petr Slouka = výkonný ředitel(执行长）**;Tomáš Jungmann = obchodní ředitel(商务总监 2020-01 增，Asbis 高级位) ;Patrik Kajúch SK chem 商务总监（2021-01 任）;"
         '谱型=捷克 IT 大国分销；Canon 2019 年度最佳分销商获；多地下块',
    kpn='Petr Slouka = výkonný ředitel(执行长）;Tomáš Jungmann = obchodní ředitel(商务总监）',
    kp=[{'name': 'Petr Slouka', 'role': 'Výkonný ředitel(Executive Director)', 'contact': '经 edsystem.cz', 'status': 'edsystem.cz 官网多源自曝', 'source': 'https://www.edsystem.cz/2018/06/05/distributor-ed-system-predstavil-nove-firemni-internetove-stranky/'},
        {'name': 'Tomáš Jungmann', 'role': 'Obchodní ředitel(商务总监）', 'contact': '同上', 'status': 'edsystem.cz 2020-03 自曝', 'source': 'https://www.edsystem.cz/2020/03/05/canon-zvolil-nejlepsim-distributorem-za-rok-2019-ed-system-3/'}],
    facts=[{'dim': 'R65 实体核正', 'text': "B-208「eD's system Czech」即 eD system a.s. Ostrava 大 IT 分销；Petr Slouka 长＋ Tomáš Jungmann 商务总监；Canon 2019 年度采购商",
             'quote': 'Petr Slouka, výkonný ředitel eD system … Tomáš Jungmann je obchodním ředitelem eD system … Ostrava, 5. 6. 2018 - eD system dnes spustil novou webovou prezentaci společnosti www.edsystem.cz',
             'url': 'https://www.edsystem.cz/2018/06/05/distributor-ed-system-predstavil-nove-firemni-internetove-stranky/'}],
    fihadd='真正的 eD system=捷克大 IT 分销；Slouka 执行长血统')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 13 批（爱尔兰/葡萄牙/罗马尼亚/波兰/捷克）',
       'scope': 'B-279 / B-456 / B-313 / B-274 / B-263 / B-192 / B-208',
       'records': [by[c] for c in ('B-279', 'B-456', 'B-313', 'B-274', 'B-263', 'B-192', 'B-208')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第13批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 13 批 7 户落盘')
