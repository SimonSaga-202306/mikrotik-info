# -*- coding: utf-8 -*-
"""R65 B 类深挖第 4 批:保加利亚/克罗地亚/捷克 8 户(2026-10-07 本轮 web_search 公开源)。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    mail = r.get('email_subject') or ''
    r['researched_on'] = '2026-10-07(R65 第 4 批精修 = R57 转写 + 本轮登记/官网/LinkedIn 新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-040',
    head='ASAP Ltd(93 Tsar Boris III Blvd, Sofia 1612, Bulgarien;2007 创立**SAP Education 伙伴**——主业务=SAP 培训认证+IT 服务(ASAPIT),非纯硬件分销;11-50 人;大客户谱=HP/Coca Cola;LinkedIn 公司页持有者 Peter Zyumbilev MD)',
    kpn='Peter Zyumbilev = Managing Director;Nikolai Enev = Regional IT Services Manager(IT 服务线口)',
    kp=[{'name': 'Peter Zyumbilev', 'role': 'Managing Director', 'contact': '经官网/LinkedIn 索取', 'status': 'LinkedIn 公司页自曝', 'source': 'https://bg.linkedin.com/company/asap-ltd'},
        {'name': 'Nikolai Enev', 'role': 'Regional IT Services Manager', 'contact': '—', 'status': 'LinkedIn 公司页自曝', 'source': '同 LinkedIn'}],
    facts=[{'dim': 'R65 LinkedIn 实名', 'text': 'ASAP Ltd Founded 2007 · HQ Sofia · 11-50 employees · Peter Zyumbilev Managing Director 自曝',
            'quote': "ASAP Ltd is founded in 2007 … Peter Zyumbilev's profile … Managing Director, ASAP Ltd",
            'url': 'https://bg.linkedin.com/company/asap-ltd'}],
    fihadd='SAP Education 伙伴口径=培训交付正事;MikroTik 谱挂在 ASAPIT 服务线')

put('B-042',
    head='Компютър Маркет ЕООД(Computer Market;Царица Йоанна 11-13, Burgas;零售连锁店,**自由人董事/全资**:Неделчо Николов НИКОЛОВ(Nedelcho Nikolov Nikolov);ЕИК 200823637,2021 营收 3.039M BGN(+37% YoY);首都 Sofia 注册+chain Burgas;office@computermarket.bg,+359 700 20 002)',
    kpn='Неделчо Николов Николов(Nedelcho Nikolov Nikolov)= Управител(董事/独资业主,2 司关联)',
    kp=[{'name': 'Неделчо Николов Николов', 'role': 'Управител(董事/独资业主)', 'contact': 'office@computermarket.bg(FB 上公示)', 'status': 'papagal.bg 商业登记实名+FB 页双源', 'source': 'https://papagal.bg/eik/200823637/76e8'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'ЕИК 200823637 · Nedelcho Nikolov Nikolov 董事/独资 · 2021 营业额 3.039M BGN(+37% YoY)',
            'quote': 'Управител: НЕДЕЛЧО НИКОЛОВ НИКОЛОВ … Оборота на фирмата за 2021 година е 3 039 000 лв',
            'url': 'https://papagal.bg/eik/200823637/76e8'}],
    fihadd='计算机零售连锁;独资业主强个人笔')

put('B-046',
    head='ПС ЛАЙФ ООД(PCLife Ltd;Plovdiv Trakiq bl.49 ent.G fl.5;EIK 200453223,2005/2008 注册口径差异;16 员工;**refurbished/二手计算机设备 bulk 贸易**——买入卖出 refurbished computer hardware in Large Quantity;Svetoslav Slavchev = Founder & CEO(yourstory 载);Plovdiv+Stara Zagora 双点)',
    kpn='Svetoslav Slavchev = Founder & CEO',
    kp=[{'name': 'Svetoslav Slavchev', 'role': 'Founder & CEO', 'contact': '经 pclife.bg 联系页/+359 32 624 895 索取', 'status': 'yourstory 登记画像具名', 'source': 'https://yourstory.com/companies/pclife'}],
    facts=[{'dim': 'R65 谱型核正', 'text': 'PCLife=二手/refurbished 计算机设备大批发,16 员工,2005 创;不是标准 MikroTik 新品分销(谱位需重评)',
            'quote': 'We buy and sell refurbished Computer Hardware in Large Quantity … 16 employees … Registered 2008',
            'url': 'https://www.jobs.bg/en/company/pclife'}],
    fihadd='谱型核正:refurbished 大批发=MikroTik 谱只是随单店架')

put('B-052',
    head='EZY Infotech d.o.o.(OIB 79541484681,MBS 070061024,2002-05-16 创立,Čakovec M. Krleže 28;**家族式**:Maja Novosel + Petra Novosel 母女/姐妹双业主双董事,Fina Info 最新的股东/董事二人名录;€120,000 股本,75% 外资股(fininfo/mojatvrtka 记 Branko Novosel dipl.ing. 早期 key person 言);小业主)+rival Mr. Kopeček)',
    kpn='Maja Novosel + Petra Novosel = 双业主双董事(Fina Info.BIZ 最新);Branko Novosel 早期 key person(或退休)',
    kp=[{'name': 'Maja Novosel', 'role': 'Vlasnik & Direktor(业主/董事)', 'contact': '经 ezy.hr/Lost 总线', 'status': 'companywall.hr + fina Info.BIZ 双源实名', 'source': 'https://www.companywall.hr/tvrtka/ezy-infotech-doo/MM17CHn0'},
        {'name': 'Petra Novosel', 'role': 'Vlasnik & Direktor(业主/董事)', 'contact': '同上', 'status': '同源', 'source': '同 companywall.hr'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'OIB 79541484681 · 2002 创立 · Maja+Petra Novosel 双业主双董事 · 股本 €120K · 小业主',
            'quote': 'Trenutni direktori tvrtke su PETRA NOVOSEL, Maja Novosel … Trenutni vlasnici tvrtke su MAJA NOVOSEL, PETRA NOVOSEL … 16.05.2002.',
            'url': 'https://www.companywall.hr/tvrtka/ezy-infotech-doo/MM17CHn0'}],
    fihadd='克罗地亚小家族分销;母女双董事')

put('B-053',
    head='LOST, d.o.o.(Ulica Kreše Golika 7, 10000 Zagreb;1994-12-30 创立=32 年老營抚制造企业(NKD 2620 Proizvodnja računala);OIB 89984971143;20-49 员工规模;lost@lost.hr,+385 1 369 7640;**Stipe Lozušić + Denis Dizdarević = 双业主双董事**,Fina Info/Kompass 两源实名)',
    kpn='Stipe Lozušić + Denis Dizdarević = 双业主双董事(fininfo.hr/companywall 双源)',
    kp=[{'name': 'Stipe Lozušić', 'role': 'Vlasnik & Direktor(业主/董事)', 'contact': 'lost@lost.hr / 013697640', 'status': 'fininfo.hr + companywall.hr 双源实名', 'source': 'https://www.fininfo.hr/Poduzece/Pregled/lost/Detaljno/20723'},
        {'name': 'Denis Dizdarević', 'role': 'Vlasnik & Direktor(业主/董事)', 'contact': '同上', 'status': '同源', 'source': '同 fininfo.hr'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'OIB 89984971143 · 1994 创立 · Stipe Lozušić+Denis Dizdarević 双业主双董事 · 20-49 员工',
            'quote': 'LOST, d.o.o. registrirano je na adresi Ulica Kreše Golika 7, 10000, Zagreb … posluje od 30.12.1994 … Stipe Lozušić, Denis Dizdarević',
            'url': 'https://www.companywall.hr/tvrtka/lost-doo/MM13qecC'}],
    fihadd='32 年老牌制造/分销;双业主结构')

put('B-048',
    head='Рива ООД(Riva Ltd;гр. Бургас, жк.Славейков бл.72;ЕИК/VAT BG102125854;**MikroTik 保加利亚官方分销商**(官网自曝 "официален дистрибутор на Mikrotik");sales@riva.bg/ service@riva.bg 自曝;056 842323 / 0876 911010;Burgas 两江城市门店)',
    kpn='—(实名董事 trailnil 台账击不着,保留待定;A相关紧台账方向)via papagal.bg ЕИК 102125854 可查', 
    facts=[{'dim': 'R65 官网自曝', 'text': 'Рива ООД е официален дистрибутор на Mikrotik за България;ЕИК BG102125854;Burgas 双热线',
            'quote': 'Рива ООД е официален дистрибутор на Mikrotik за България … ЕИК/VAT: BG102125854 … гр. Бургас, жк.Славейков бл.72',
            'url': 'https://www.riva.bg/mikrotik/show/all.html'}],
    fihadd='MikroTik 保加利亚官方分销商定位坐实;董事实名待 papagal 下次补')

put('B-189',
    head='ABCtech s.r.o.(IČ 27546624/DIČ CZ27546624,Hradec Králové 地区司法登记;2008+ 注册;总部 Piletická 55/36, Hradec Králové 3(制造/分销两翼:库存 Česká Skalice Nerudova 742 发票);品牌谱=MikroTik/Cambium/Ubiquiti/TP-Link/RF elements/Netis/Hikvision——**谱型=无线/ISP 设备总批发商**;Jan Hofman 董事(2011-08 重组后,原 Milan Roztočil 退);Komerční banka CZ0301000001157270380287)**',
    kpn='Jan Hofman = Jednatel(董事,2011 至今,继 Milan Roztočil 退位)',
    kp=[{'name': 'Jan Hofman', 'role': 'Jednatel(董事/总经理)', 'contact': '经 abctech.cz reklamace@ 索取', 'status': 'rejstrik.penize.cz + zivefirmy.cz + 官网 O nás 三源实名', 'source': 'https://rejstrik.penize.cz/27546624-abctech-s-r-o'}],
    facts=[{'dim': 'R65 商业登记', 'text': 'IČ 27546624 · Jan Hofman jednatel 2011-08 至今(前 Milan Roztočil 退) · 发票地 Hradec Králové · KB 账号公开',
            'quote': 'Jednatel: Jan Hofman ABCtech s.r.o. … IČ: 27546624 DIČ: CZ27546624 … Den vzniku funkce: 11. 8. 2011',
            'url': 'https://www.abctech.cz/default.asp?cls=stoitem&stiid=39428'}],
    fihadd='捷克 ISP 设备总批发商,MikroTik/Cambium/RFElements 多谱在位=最准年代')

put('B-191',
    head='AT Computers a.s.(IČO 616 72 599,Těšínská 1970/56, Slezská Ostrava, 710 00 Ostrava;**捷克 ICT 大分销体**:65,000+ SKU/300+ 世界品牌/1,000+ 零售伙伴网络;atcmarket.cz = 其纯 B2B 市场平台(不直售终端,全部 resale 通过 reseller);TOUCHIT 项目学生;下面有些话是平台型分销与谱商接口最能通)',
    kpn='—(零售平台层大分销,jednatel/董事需到 or.justice.cz/商业登记查询本,IČO 61672599 挂牌)',
    facts=[{'dim': 'R65 平台谱型坐实', 'text': 'AT Computers a.s.=捷克 ICT 大分销,atcmarket.cz 纯 B2B 市场,65000+ SKU ≈ 300 大谱/大卖家网络,不直售终 user,全部 resale 过 reseller;IČO 616 72 599 发票地 Slezská Ostrava',
            'quote': 'AT Computers, Slezská Ostrava … Distribuční společnost nabízející ICT zařízení … Databáze produktů obsahuje více jak 65 000 různých položek zboží od 300 největších světových i domácích značek … ATC nikdy neprodává koncovým zákazníkům napřímo',
            'url': 'https://www.hwforum.cz/novinky/projekt-www.atcmarket-cz-od-AT-Computers.html'}],
    fihadd='平台型分销大 65000 SKU;MikroTik 商口由 web 册内挂着,PO 口位置价值')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 4 批(保加利亚/克罗地亚/捷克)',
       'scope': 'B-040 ASAP / B-042 Computer Market / B-046 PCLife / B-048 Riva / B-052 EZY Infotech / B-053 LOST / B-189 ABCtech / B-191 AT Computers',
       'discipline': '实名=商业登记/官网/LinkedIn 公开源自曝;评级不动不出信守档;待补证项标待定不重试',
       'records': [by[c] for c in ('B-040', 'B-042', 'B-046', 'B-048', 'B-052', 'B-053', 'B-189', 'B-191')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第4批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 4 批 8 户落盘')
