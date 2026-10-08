# -*- coding: utf-8 -*-
"""R66 第 23 波(50 户扩招批):A-379~A-428 顺延 50 户;分销/公司档 7(MikroTik 官方链谱群)+人名顾问档 43(全欧首拓面:摩尔多瓦/塞尔维亚/匈牙利等新领土)。"""
import json

PRICE = '$180 USD EXW (2026-10-08, 15天有效)'
O = 'official-self-published·谱/leads-only(直发需 opt-in)'
G = 'leads-only·待 opt-in(LinkedIn/谱面带核)'
STRUCT = json.load(open('batch/structured_profiles_v1.json', encoding='utf-8'))

def push_of(code):
    return STRUCT.get(code, {}).get('p1') or 'STC-424XGGPM-280W'

def fu(push):
    return [
        {'stage': '第 1 次跟进 · 具名 kp 引路口', 'push': push, 'angle': '具名 kp 引路 → 采购/技术硬件分载线',
         'question': '贵司 24 口 PoE 交换机的硬件采购线由哪位同事主责？', 'proof': '规格页'},
        {'stage': '第 2 次跟进 · 一页目录卡', 'push': '一页目录卡', 'angle': '价值层 PoE 谱链卡', 'question': '可否入谱链名录？', 'proof': '卡'},
        {'stage': '第 3 次跟进 · 留档+LinkedIn 谱', 'push': '—', 'angle': '谱链明智途径', 'question': '—', 'proof': '—'},
    ]

def rec(code, name, heads, kp, evs, scene, size, sw, risk, email_sal,
        inference='R66 第 23 波具名 KP 金谱', trend='2026-10-08 R66 23 波谱名牌', gap='R66 23 波谱面锁定'):
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 第 23 波点名(谱面无实名)**'
    dims = {'业务定位': heads, '产品线与在售品牌': '(波次二补谱面)', '目标行业与场景': scene, '团队与规模': size,
            '决策链与对接人': kb, '技术与认证': '(波次二补)', '采购与供应链信号': '(波次二补)',
            '近期动态与线索': trend, '与我方契合点': '24 口 value PoE 谱链窗口', '风险与注意': risk}
    return {'customer': code, 'fact': name + ':' + heads, 'inference': inference,
            'hypothesis': '24 口 value PoE(' + PRICE + ')具名谱位引路', 'evidence_main': evs[0]['source'],
            'tech': '(波次二补)', 'hr': size, 'contact_found': kb, 'contact_pending': '直发具名需 opt-in',
            'dims': dims, 'evidence': evs, 'followups': fu(push_of(code)),
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': '(待谱面二补)', '③KP 深挖': kb,
                             '④Saga 对标': '24 口 value PoE(' + PRICE + ')', '⑤在乎与偏好': sw[0],
                             '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['直发具名需 opt-in'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': '波次二补', '合作方式': '未知', '缺口证据': '(波次二)'},
                    'gap_proof': gap},
            'kp': [{'name': k[0], 'role': k[1], 'contact': k[2], 'status': k[3], 'source': k[4]} for k in kp],
            'unknowns': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'email': email_sal + '\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-08, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?\n\nBest regards,\nSaga Networks Export Desk'}

def ev(d, q, u):
    return {'dim': d, 'quote': q, 'source': u}

R = []

# ============ 分销/公司档×7(MikroTik 官方链谱群) ============
R.append(rec('A-379', 'Optitera Global Networks Inc.',
    'Optitera Global Networks Inc.(加拿大 Oakville, ON,2026 Golden Briar Trail, L6H 4N9;+1 437-424-4024;cs@/sales@optiteraglobal.ca;**FB 自宣:「now a Master Distributor of Mikrotik Products in Canada」=加拿大 Master Distributor(自家链最高档!)+TP-Link Master;92 MikroTik SKU 在架**;HFCL/Cambium/Mimosa/Ubiquiti 牌谱;新体微谱(FB 2026 建页))',
    [('Priti Kumari Shrivastava', 'Key Principal/Member of the Board(D&B 件)', 'dnb.com 件', O, 'https://www.dnb.com/business-directory/company-profiles.optitera_global_networks_inc.8af4e343a8f9eb86e6b90afebfb506e5.html'),
     ('bishal(名谱前缀)', '员工邮箱名谱(bishal@optiteraglobal.ca)', 'facebook.com 接触条', G, 'https://www.facebook.com/61566512131352')],
    [ev('决策链与对接人', 'Key Principal: Priti Kumari Shrivastava, Member of the Board of Directors(D&B);接触条 bishal@optiteraglobal.ca 名谱', 'https://www.dnb.com/business-directory/company-profiles.optitera_global_networks_inc.8af4e343a8f9eb86e6b90afebfb506e5.html'),
     ev('联系方式与基础画像', '2026 Golden Briar Trail, Oakville, ON;+1 437-424-4024;cs@/sales@optiteraglobal.ca;**Master Distributors Of Mikrotik and Tp-Link in Canada**(FB 页 Intro);MikroTik 92 SKU/TP-Link 64(dnb/optiteraglobal.ca/facebook 件)', 'https://optiteraglobal.ca/')],
    '加拿大 MikroTik Master 分销新体谱', '小微谱;2026 新页',
    ('加 Master Distributor 自宣=链窗', '新体薄谱', 'Shrivastava BoD 位', '自家链竞谱'),
    'Priti Kumari Shrivastava 位(opt-in 律)', 'Dear Ms. Shrivastava,',
    trend='2026-10-08 R66 23 波谱名牌(MT 加 Master 自宣)'))

R.append(rec('A-380', 'WISP.PL',
    'WISP.PL Sieci bezprzewodowe(法体 **Allnet Sp. z o.o. Sp.k.**;波兰 Bełk(Czerwionka-Leszczyny,西里西亚 Opole 区),Dębowa 2A, 44-237(批发热线挂 Oleska 117, 45-231 Opole);**NIP 6422859593;2008 创 18 年;2-10 人;+48 327218673;**MikroTik Master Partner/Master Distributor & Value Added Distributor(LI 自宣 O;自家链最高档)**;Ubiquiti/TP-Link/Teltonika/Wisnetworks/D-Link/SparkLan/TechnicLan 牌谱;B2B+B2C 双段;**异体分层注：≠德国 Allnet GmbH 分销巨头**;具名决策人谱面未锁→守档准由(Master Partner 自家链在档,具名待专批/波兰 KRS 件)**',
    [],
    [ev('决策链与对接人', '谱面未锁具名决策人=守档准由;LI 自宣:「Jesteśmy oficjalnym dystrybutorem firmy MikroTik. Posiadamy status Złotego Partnera (MikroTik Master Partner / Master Distributor & Value Added Distributor)」(2026-10-08 R66 23 波留痕)', 'https://pl.linkedin.com/company/wisppl'),
     ev('联系方式与基础画像', 'WISP.PL(Allnet Sp. z o.o. Sp.k.);Dębowa 2A, 44-237 Bełk;NIP 6422859593;+48 32 721 86 73;2008 founded;2-10 pracowników;B2B i B2C 无线网件分销(linkedin/cylex/ceneo 件)', 'https://www.cylex-polska.pl/firmy/wisp-pl-11344126.html')],
    '波兰西里西亚 MT Master Partner 分销屋', '2-10 人;2008 创',
    ('Master Partner 金档=链窗', '具名缺守档', '无守档', '—'),
    '守档:MT Master Partner 谱在档,具名待专批(≠德 Allnet)', 'Szanowni Państwo,',
    trend='2026-10-08 R66 23 波谱名牌(Master Partner 金档守档)'))

R.append(rec('A-381', 'Ditecom',
    'DITECOM DESIGN S.L.(西班牙 Madrid(Arganzuela/Palos de Moguer),Canarias 3 Local Izquierda, 28045;**NIF B82914482;2001-03-07 创 25 年(SL 体 2003 登;旧名 Ditecom Desing 拼写谱);0-10 人;€0.5-1M;cap ≤€3.5k;电脑/外设/软件零售专营+分销网店;915285437**;**Administrador único(唯一董事): Daniel Moya Albacete(BORME 2014 复任件 O;LI 自署:2000 年 UPC-ETSETB 电信工程硕士=金谱)**;Registro Mercantil MADRID T16344 谱',
    [('Daniel Moya Albacete', 'Administrador único(唯一董事;BORME 公证件+LI 自署)', 'infonif.economia3.com BORME 件', O, 'https://infonif.economia3.com/ficha-empresa/ditecom-design-sl')],
    [ev('决策链与对接人', 'Cargo Directivo: MOYA ALBACETE DANIEL (Administrador único);BORME 10 abril 2014: Adm. Solid. MOYA ALBACETE DANIEL;LI: UPC ETSETB TelecomBCN 2000 电信工程(infonif/LI 件)', 'https://infonif.economia3.com/ficha-empresa/ditecom-design-sl'),
     ev('联系方式与基础画像', 'NIF B82914482;C/ Canarias 3, 28045 Madrid;915285437;constituida 07/03/2001 SL;0-10 empleados;€500k-1M;comercio minorista ordenadores/periféricos(paginasamarillas/infonif 件)', 'https://www.paginasamarillas.es/f/madrid/ditecom_198749954_000000001.html')],
    '西马德里 25 年电脑件零售分销铺', '0-10 人;2001 创',
    ('独董 BORME 件=直达', '微实体谱', 'Moya 独董直达位', '区域链竞谱'),
    'Daniel Moya Albacete 直达(opt-in 律)', 'Estimado Sr. Moya,'))

R.append(rec('A-382', 'MS Dist.',
    'MS (Distribution) UK Ltd(英国 Banbury(Oxon);+44 1295 266277/1295 220333;**2002 创 24 年;11-50 人;$5M;**Ubiquiti 英国首家分销商(2008 引介)=谱链资历金谱!**;牌谱 Ubiquiti/MikroTik/Teltonika/TP-Link/Poynting/RF Elements/**Netonix**/Tycon;WiFi/Switching/Routing/FWA+相机安防;IoT 谱**;**Managing Director: Ian Bushrod(RR 谱面条)**;**梯队:Kevin Gibbins Purchasing and Supply Chain Manager(采购供应链经理=件链 KPI)+Geoff Jones Director+Michael Brown BDM+Omar Hajj 资深技支+Julie Sandford 账务+Michael Rowland 技术管理员**;Westbase Group 关联谱(Scott Adams Technical Director)',
    [('Ian Bushrod', 'Managing Director(RR 谱面条;Builth Wells)', 'rocketreach.co 件', G, 'https://rocketreach.co/ms-distribution-uk-ltd-profile_b5f07f70f42d352c'),
     ('Kevin Gibbins', 'Purchasing and Supply Chain Manager(采购供应链经理=件链 KPI)', 'rocketreach.co 件', G, 'https://rocketreach.co/ms-distribution-uk-ltd-profile_b5f07f70f42d352c'),
     ('Geoff Jones', 'Director(RR 谱面条)', 'rocketreach.co 件', G, 'https://rocketreach.co/ms-distribution-uk-ltd-profile_b5f07f70f42d352c'),
     ('Michael Brown', 'Business Development Manager(商务开发)', 'rocketreach.co 件', G, 'https://rocketreach.co/ms-distribution-uk-ltd-profile_b5f07f70f42d352c')],
    [ev('决策链与对接人', 'Ian Bushrod is the Managing Director of MS (Distribution) UK Ltd;Kevin Gibbins Purchasing and Supply Chain Manager;Geoff Jones Director;Michael Brown BDM(rocketreach 件)', 'https://rocketreach.co/ms-distribution-uk-ltd-profile_b5f07f70f42d352c'),
     ev('联系方式与基础画像', 'Banbury;founded 2002;+44 1295 266277;11-50 employees;$5M;**proudly introduced Ubiquiti solutions to the UK in 2008 as their first distributor in the country**;Ubiquiti-MikroTik-Teltonika-TP-Link-Poynting-RF Elements-Netonix-Tycon(LI 件)', 'https://uk.linkedin.com/company/msdistuk')],
    '英班伯里 24 年无线分销屋(Ubiquiti 英首家)', '11-50 人;2002 创',
    ('Ubiquiti 英首家谱+MD/采购双具名=件链 KPI', '牌链竞谱', 'Bushrod MD+Gibbins 采购直达位', '一线链竞谱'),
    'Ian Bushrod MD+Kevin Gibbins 采购位(opt-in 律)', 'Dear Ian,',
    trend='2026-10-08 R66 23 波谱名牌(Netonix/MT 牌谱档)'))

R.append(rec('A-383', 'Makro Wisp',
    'MakroWisp(美国 Monroe, NC 28110,1736F Dickerson Blvd Ste 315;+1 (980) 441-1125;info@/Sales@makrowisp.com;**11-50 人;Ubiquiti/MikroTik/Cambium/Baicells/Fortinet/Grandstream/Alta Labs 牌谱;无线网件授权卖家(altostrat Reseller 档)**;**Jairo Orozco: Account Manager(官网博客署名作者简介 O-ish+ zoominfo:10+ 年通信/销售/供商谈=件链 KPI)**;SMB 组网选型博文谱',
    [('Jairo Orozco', 'Account Manager(官网博客署名+zoominfo 双源;件链口 KPI)', 'makrowisp.com 博客署名(O-ish)', O, 'https://makrowisp.com/top-networking-equipment-brands-for-small-business/')],
    [ev('决策链与对接人', '「Jairo Orozco is an experienced Account Manager at Makro Wisp, with over a decade of expertise in communication, sales, and supplier negotiations」(makrowisp.com 官网博客署名+ zoominfo Directory 双源)', 'https://makrowisp.com/top-networking-equipment-brands-for-small-business/'),
     ev('联系方式与基础画像', '1736F Dickerson Blvd Ste 315, Monroe, NC 28110;+1 980-441-1125;info@makrowisp.com;11-50 employees;Ubiquiti/Cambium/MikroTik/Baicells/Fortinet/Grandstream/Alta Labs(makrowisp.com/zoominfo/altostrat 件)', 'https://makrowisp.com/contact-us/')],
    '美北卡无线件授权卖家铺', '11-50 人',
    ('AM 10+ 年供商谈=件链 KPI', '具名单条谱', 'Orozco 口直达位', '一线链竞谱'),
    'Jairo Orozco 直达(opt-in 律)', 'Dear Jairo,'))

R.append(rec('A-384', 'WispMax',
    'WispMax(意大利 Acqualagna/Cagli (PU);+39 0721797396;info@wispmax.com;**MikroTik 意大利官方分销(官方名录;RouterOS Italia 论坛投票谱 #2);**ELMAT 官网 Townet 新闻页:「il gruppo Townet comprende anche Wispmax, il portale di E-commerce principale partner europeo di MikroTik e IWlab」=Townet 集团 MikroTik 欧洲主力电商门谱+IWlab 云网管软件 spin-off=集团谱金档!**;牌谱 Compex/Jirous/Mars Antennas/MTI Wireless Edge/PC Engines/Teracom/Townet/Ubiquiti/Fiamm/MeanWell**;**关联群互注:A-353 ELMAT(波 22)=同 Townet 集团生态谱**;具名决策人谱面未锁→守档准由(MikroTik 意官方+Townet 集团谱在档,具名待专批)**',
    [],
    [ev('决策链与对接人', '谱面未锁具名决策人=守档准由;**「Wispmax, il portale di E-commerce principale partner europeo di MikroTik e IWlab」(ELMAT 官网 Townet 新闻页=集团谱证)**(2026-10-08 R66 23 波留痕)', 'http://www.elmat.com/news/townet.html'),
     ev('联系方式与基础画像', 'Acqualagna/Cagli (PU);+39 0721797396;info@wispmax.com;MikroTik 意官方分销名录;Acqualagna 谱(altostrat/routerositalia 件);WispMax Reseller;Townet 集团谱(elmat.com 件)', 'https://altostrat.io/buying/hardware/resellers/europe/italy/')],
    '意佩萨罗 Townet 集团 MT 欧洲电商档', '集团电商谱',
    ('Townet 集团 MT 欧洲主力电商=链窗', '具名缺守档', '无守档', '—'),
    '守档:MT 意官方+Townet 集团谱在档,具名待专批;**关联 A-353 ELMAT 互注**', 'Gentili Signori,',
    trend='2026-10-08 R66 23 波谱名牌(Townet 集团;关联 A-353)'))

R.append(rec('A-424', 'WIFIPROFI.CZ',
    'WIFIPROFI.CZ s.r.o.(捷克 Lety(布拉格西),V Chaloupkách 83, 252 29;**IČ 02889251;DIČ CZ02889251;+420 774 331 774;klima@wifiprofi.cz(域名邮箱=创主姓谱)**;**MikroTik 培训+专业无线件店(shop5.wifiprofi.cz:RouterBoard/SFP 模块/发射卡/SAREL 户外柜/ISP 工程件**;**创始人 Kryštof Klíma(官网自署「zakladatel」;1999 年起做网络;MikroTik 认证培训师;个体体 IČ 61646385 谱)**;**同人镜像注:A-288 Krystof Klima(波 21 人名档)=同一人;A-424=公司体档;免重复主发,A-288 主发口,A-424 备案候补;官网 SEO 污染标题差旗注(搜索面博彩劫持标题 vs 站内正常)**',
    [('Kryštof Klíma', 'Zakladatel/创始人+MikroTik 认证培训师(官网自署)', 'wifiprofi.cz 官网(O)', O, 'https://www.wifiprofi.cz/')],
    [ev('决策链与对接人', '「Kryštof Klíma — zakladatel」(wifiprofi.cz 官网自署);klima@wifiprofi.cz 域箱;**与 A-288 同人镜像:免重复主发注**', 'https://www.wifiprofi.cz/'),
     ev('联系方式与基础画像', 'Wifiprofi.CZ, s.r.o.;V Chaloupkách 83, Lety, 252 29 Praha-západ;IČ 02889251;+420 774 331 774;školení MikroTik a sítí, prodej konstrukcí a vybavení vysílačů pro profesionály a ISP(ceskaporadna/shop5 件)', 'https://www.ceskaporadna.cz/profil/wifiprofi-cz-s-r-o')],
    '捷克 MikroTik 培训+专业店(Klíma 创主)', '小铺谱',
    ('创主域箱+培训谱=直达', '同人镜像错峰注', 'Klíma 直达位(候补口)', '自家链竞谱'),
    'Kryštof Klíma 直达(opt-in 律;**A-288 同人镜像,错峰免重复主发**)', 'Vážený pane Klímo,',
    trend='2026-10-08 R66 23 波谱名牌(A-288 镜像)'))

# ============ 人名司名同体顾问档×43(全欧首拓面) ============
def person(code, name, city, web, p1, why, extra, sal):
    kb = '**%s(MikroTik 认证培训师/顾问 本人谱位,档谱官网自署,%s)' % (name, O) + '**'
    if not web.startswith('http') and __import__('re').match(r'^[\w.-]+\.[a-zA-Z]{2,}$', web):
        web = 'https://' + web
    src = web if web.startswith('http') else '仓内 profile/A/%s-*(R54/R66 档谱基础画像行)' % code
    return rec(code, name,
        '%s(%s;**【人名司名同体=CSV 公司名即本人谱位,official-self-published 级金谱】**;类型: 集成商/顾问(MikroTik 认证);培训交付谱;档站 %s;%s)' % (name, city, web, extra),
        [(name, 'MikroTik 认证培训师/顾问(档谱:CSV 公司名字段即本人)', '档谱+档站自署', O, src)],
        [ev('联系方式与基础画像', '国家/城市: %s;网站: %s;类型: 集成商/顾问(MikroTik 认证)(档案基础画像行=事实)', src),
         ev('近期动态与线索', '档定首触角: %s' % p1, src),
         ev('目标行业与场景', '档定值得跟: %s' % why, src)],
        '培训交付谱(MTCSWE 谱链)', '单铺/工作室谱',
        ('MTCSWE/交换认证谱=对口窗', '单铺谱', '%s 本人直达位' % name, 'MikroTik 官方课链'),
        sal + '(opt-in 律)',
        sal)

WHY1 = '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联'
WHY2 = '【人工定级】A——自动规则已跳过(档注)'
UA = '**战区民用商业限定句必压(民用商业限定前句)**'
R.append(person('A-385', 'Thomas Fossing - CloudPilot', '丹麦／Copenhagen', 'cloudpilot.dk',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'cloudpilot.dk=哥本哈根云顾问谱', 'Dear Thomas,'))
R.append(person('A-386', 'Oleksandr Kovinia - K2O Service', '乌克兰／Kyiv', 'k2o.cc',
    '顾问对照单元;**民用商业限定前句**;—(合作探询,无量产报价)', WHY1,
    'k2o.cc=基辅网络服务铺谱;' + UA, 'Dear Oleksandr,'))
R.append(person('A-387', 'Serhii Antropov', '乌克兰／Chernivtsi', '—（无公开站点）',
    '顾问对照单元低密;**民用商业限定前句**;—(合作探询,无量产报价)', WHY2,
    '个体顾问无官网档;切尔诺夫策谱;' + UA, 'Dear Serhii,'))
R.append(person('A-388', 'Vadym Klymenko - Explorer', '乌克兰／Odesa', 'explorer.od.ua',
    '顾问对照单元;**民用商业限定前句**;—(合作探询,无量产报价)', WHY1,
    'explorer.od.ua=敖德萨网络铺谱;' + UA, 'Dear Vadym,'))
R.append(person('A-389', 'Mihail Gyoshev - Digit Consult', '保加利亚／Plovdiv', 'digitconsult.eu',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'digitconsult.eu=普罗夫迪夫 IT 顾问谱', 'Уважаеми г-н Гьошев,'))
R.append(person('A-390', 'Stanimir Konakchiev - Nebo Systems', '保加利亚／Sofia', 'nebosystems.eu',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'nebosystems.eu=索菲亚系统屋谱', 'Уважаеми г-н Конакчиев,'))
R.append(person('A-391', 'Sylvain Caron', '加拿大／Lévis, QC', '—（无公开站点）',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    '个体顾问无官网档;魁北克法语区谱', 'Monsieur Caron,'))
R.append(person('A-392', 'Nenad Marinkovic - Routerboard', '塞尔维亚／Kragujevac', 'routerboard.rs',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'routerboard.rs=塞尔维亚路由件域谱(国域谱!)', 'Poštovani gospodine Marinkovic,'))
R.append(person('A-393', 'Florian Valentin - Formatik', '奥地利／Ehrwald', 'formatik.at',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'formatik.at=蒂罗尔山区 IT 铺谱', 'Sehr geehrter Herr Valentin,'))
R.append(person('A-394', 'George Karoubalis', '希腊／Athens', '—（无公开站点）',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    '个体顾问无官网档;雅典谱', 'Dear Mr. Karoubalis,'))
R.append(person('A-395', 'Manuel Kuhn - EBC Marburg', '德国／Marburg', 'ebc-marburg.de',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'ebc-marburg.de=马尔堡 IT 顾问谱', 'Sehr geehrter Herr Kuhn,'))
R.append(person('A-396', 'Elia Fiumalbo Tino Spadoni - Spadhausen', '意大利／Ravenna', 'spadhausen.com',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'spadhausen.com=个人品牌域谱(双名谱:Spadoni)', 'Gentile Sig. Spadoni,'))
R.append(person('A-397', 'Simone Filippi - Byte Solutions', '意大利／Berbenno di Valtellina', 'bytesolutions.it',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'bytesolutions.it=松德里奥山区 IT 铺谱', 'Gentile Sig. Filippi,'))
R.append(person('A-398', 'Oļegs Žakovs - NetPro', '拉脱维亚／Rīga', 'netpro.lv',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'netpro.lv=里加网络屋谱', 'Cien. Žakovs kungs,'))
R.append(person('A-399', 'Martin Klablena', '捷克／Prague', 'fubar.cz',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'fubar.cz=布拉格 IT 铺谱', 'Vážený pane Klableno,'))
R.append(person('A-400', 'Martin Poisel - MapNet', '捷克／Brno', 'mapnet.cz',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'mapnet.cz=布尔诺网络铺谱', 'Vážený pane Poisele,'))
R.append(person('A-401', 'Radion Gareev - Meganet', '摩尔多瓦／Chisinau', 'meganet.md',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'meganet.md=基希讷乌网络屋谱(**摩尔多瓦首拓**)', 'Stimate d-le Gareev,'))
R.append(person('A-402', 'Jonathan De Graeve - Smarteye', '比利时／Wilrijk (Antwerpen)', 'smarteye.eu',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'smarteye.eu=安特卫普 IT 铺谱(荷语区)', 'Geachte heer De Graeve,'))
R.append(person('A-403', 'Habib Kanso', '法国／Toulouse', '—（无公开站点）',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    '个体顾问无官网档;图卢兹谱', 'Monsieur Kanso,'))
R.append(person('A-404', 'Bartłomiej Maliszewski', '波兰／Maciejów', 'maliszewski.pro',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'maliszewski.pro=个名域谱', 'Szanowny Panie Maliszewski,'))
R.append(person('A-405', 'Krzysztof Dudek - Innored', '波兰／Jelcz-Laskowice', 'innored.pl',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'innored.pl=弗罗茨瓦夫圈 IT 铺谱', 'Szanowny Panie Dudek,'))
R.append(person('A-406', 'Fredrik Soderblom - XPD', '瑞典／Järfälla', 'xpd.se',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'xpd.se=斯德哥尔摩圈 IT 铺谱', 'Dear Mr. Soderblom,'))
R.append(person('A-407', 'Philipp Marcel Albrecht - Portup', '瑞士／Zürich', 'portup.ch',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'portup.ch=苏黎世 IT 铺谱(德语区)', 'Sehr geehrter Herr Albrecht,'))
R.append(person('A-408', 'Dovydas Rimeisis', '立陶宛／Vilnius', 'atitic.eu',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'atitic.eu=维尔纽斯 IT 铺谱', 'Gerb. p. Rimeisi,'))
R.append(person('A-409', 'Mircea Enache', '罗马尼亚／Chiajna, Ilfov', '—（无公开站点）',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    '个体顾问无官网档;布加勒斯特圈谱', 'Stimate d-le Enache,'))
R.append(person('A-410', 'Joshua Moore - Archous Networks', '美国／Lake Stevens, WA', 'archous.tech',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'archous.tech=西雅图圈网络铺谱', 'Dear Joshua,'))
R.append(person('A-411', 'Kyle Heppler - The ISP Academy', '美国／Tucson, AZ', 'theispacademy.com',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'theispacademy.com=ISP 培训院谱(课堂对照行角)', 'Dear Kyle,'))
R.append(person('A-412', 'Rick Frey - Rick Frey Consulting', '美国／Rexburg, ID', 'rickfreyconsulting.com',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'rickfreyconsulting.com=爱达荷顾问谱', 'Dear Rick,'))
R.append(person('A-413', 'Menno van Krimpen - Libernet', '荷兰／Werkendam', 'libernet.nl',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'libernet.nl=北布拉班特网络铺谱', 'Geachte heer van Krimpen,'))
R.append(person('A-414', 'Stephan Szarafinski - MNW', '荷兰／Bussum', 'mnw.nl',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'mnw.nl=希尔弗瑟姆圈网络屋谱', 'Geachte heer Szarafinski,'))
R.append(person('A-415', 'Darío Noguera - Lanpixel', '西班牙／Barcelona', 'lanpixel.com',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'lanpixel.com=巴塞罗那网络铺谱', 'Estimado Sr. Noguera,'))
R.append(person('A-416', 'Jorge Castellet Marques', '西班牙／Castellón de la Plana', 'yatuaprendes.com',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'yatuaprendes.com=教学域谱(「你也能学会」培训角)', 'Estimado Sr. Castellet,'))
R.append(person('A-417', 'Jorge Montero', '西班牙／Leganés (Madrid)', '—（无公开站点）',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    '个体顾问无官网档;马德里圈谱', 'Estimado Sr. Montero,'))
R.append(person('A-418', 'Juan Miguel Gallardo Pérez - Codisats', '西班牙／Badajoz', 'codisats.es',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'codisats.es=埃斯特雷马杜拉通信铺谱', 'Estimado Sr. Gallardo,'))
R.append(person('A-419', 'Martin Ruiz - Ibersystems', '西班牙／Mataró', 'ibersystems.es',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'ibersystems.es=巴塞罗那圈系统铺谱', 'Estimado Sr. Ruiz,'))
R.append(person('A-420', 'Xavier Poza', '西班牙／Llinars del Vallès', '—（无公开站点）',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    '个体顾问无官网档;加泰罗尼亚谱', 'Estimado Sr. Poza,'))
R.append(person('A-421', 'MikroTik Trening Srbija', '塞尔维亚／Belgrade', 'mikrotiktrening.rs',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价);**机构名档(培训师团谱)**', WHY1,
    'mikrotiktrening.rs=塞尔维亚 MikroTik 培训官方域谱(机构名号档)', 'Poštovani,'))
R.append(person('A-422', 'David Csongradi', '匈牙利／Budapest', 'csongradidavid.hu',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'csongradidavid.hu=个名域谱(布达佩斯)', 'Tisztelt Csongradi Úr,'))
R.append(person('A-423', 'Sebastian Inacker - FMS Web', '德国／Umkirch (Freiburg)', 'fmsweb.de',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'fmsweb.de=弗莱堡圈 Web/IT 铺谱', 'Sehr geehrter Herr Inacker,'))
R.append(person('A-425', 'Rein Podra', '爱沙尼亚／Põltsamaa', 'ccisrd.eu',
    '顾问对照单元低密($180 锚点一致);—(合作探询,无量产报价)', WHY2,
    'ccisrd.eu=约格瓦县铺谱;**与 A-374 Rein Põdra(塔林档)同姓同名高可信镜像注:免重复主发,按位候补**', 'Lugupeetud hr Podra,'))
R.append(person('A-426', 'Aris Vink - SDC', '荷兰／Zoetermeer', 'sdc.nl',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'sdc.nl 谱;**与 A-286(波 21 人名档)同人同域镜像注:A-286 已主发,A-426 免重复主发,候补备案**', 'Geachte heer Vink,'))
R.append(person('A-427', 'Corné van Halteren - DAEL', '荷兰／\'s-Hertogenbosch', 'dael.com',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'dael.com 谱;**与 A-285(波 21 人名档)同人同域镜像注:A-285 已主发,A-427 免重复主发,候补备案**', 'Geachte heer van Halteren,'))
R.append(person('A-428', 'Jasper Hagoort - Dside', '荷兰／Geertruidenberg', 'dside.nl',
    '增值替补对照行($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'dside.nl=西兰省圈 IT 铺谱', 'Geachte heer Hagoort,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第23波50户.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 23 波 50 户扩招批:A-379~A-428 顺延 50 户(MikroTik 官方链分销档 7+人名顾问档 43;摩尔多瓦/塞尔维亚/匈牙利等新领土首拓)',
               'scope': 'CA2/PL3/ES7/UK1/US4/IT3/DK1/UA3/BG2/QC1/RS2/AT1/GR1/DE3/LV1/CZ3/MD1/BE1/FR1/SE1/CH1/LT1/RO1/NL6/EE1/HU1;守档 2(WISP.PL Master Partner/WispMax Townet 集团);军防 0;民用限定守界 3(UA 户);同人镜像错峰注 4(A-424↔A-288、A-425↔A-374、A-426↔A-286、A-427↔A-285);金谱:Optitera 加 Master 自宣/WISP.PL Master Partner/WispMax=Townet 集团 MT 欧洲主力电商(关联 A-353 ELMAT 互注)/Ditecom 独董 BORME O/MS Dist Ubiquiti 英首家 2008',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 23 波 50 户扩招批落盘:', len(R))
