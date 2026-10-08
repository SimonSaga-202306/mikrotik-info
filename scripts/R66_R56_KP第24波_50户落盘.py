# -*- coding: utf-8 -*-
"""R66 第 24 波(50 户扩招批):A-429~A-478 顺延 50 户;分销/公司档 45(乌克兰官方分销 9 连+土耳其 9+希腊 6+匈牙利 5+北马 2+塞尔维亚 2+奥地利 3+德国 2+加拿大 4+以色列/保加利亚 3)+集成/顾问人名档 5(荷兰 2/克罗地亚 1/加拿大魁北克 1/温尼伯 1)。"""
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
        inference='R66 第 24 波具名 KP 金谱', trend='2026-10-08 R66 24 波谱名牌', gap='R66 24 波谱面锁定'):
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 第 24 波点名(谱面无实名)**'
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

def person(code, name, city, web, p1, why, extra, sal):
    kb = '**%s(MikroTik 认证培训师/顾问 本人谱位,档谱官网自署,%s)' % (name, O) + '**'
    if not web.startswith('http') and __import__('re').match(r'^[\w.-]+\.[a-zA-Z]{2,}$', web):
        web = 'https://' + web
    src = web if web.startswith('http') else '仓内 profile/A/%s-*(R54/R66 档谱基础画像行)' % code
    return rec(code, name,
        '%s(%s;**【人名司名同体=CSV 公司名即本人谱位,official-self-published 级金谱】**;类型: 集成商/顾问(MikroTik 认证);培训交付谱;档站 %s;%s)' % (name, city, web, extra),
        [(name, 'MikroTik 认证培训师/顾问(档谱:CSV 公司名字段即本人)', '档谱+档站自署', O, src)],
        [ev('联系方式与基础画像', '国家/城市: %s;网站: %s;类型: 集成商/顾问(MikroTik 认证)(档案基础画像行=事实)' % (city, web), src),
         ev('近期动态与线索', '档定首触角: %s' % p1, src),
         ev('目标行业与场景', '档定值得跟: %s' % why, src)],
        '培训交付谱(MTCSWE 谱链)', '单铺/工作室谱',
        ('MTCSWE/交换认证谱=对口窗', '单铺谱', '%s 本人直达位' % name, 'MikroTik 官方课链'),
        sal + '(opt-in 律)',
        sal)

WHY1 = '有明确交换/供电需求(交换认证 MTCSWE),且有具体人直联'
WHY2 = '【人工定级】A——自动规则已跳过(档注)'
UA = '**战区民用商业限定句必压(民用商业限定前句)**'
R = []

# ============ 段一:乌克兰官方分销 9 连(A-432~440,民用限定句全压) ============
R.append(rec('A-432', 'DEPS',
    'DEPS(乌克兰 Kyiv;**MikroTik Master+VAD(名录信号)+Ubiquiti 官方分销;Telecom Ukraine 2026 冠名赞助商(行业晚报谱);УкрСЕПРО 认证谱**;分销大户 VAD 档;具名决策人谱面未锁→守档准由(波次二走 youcontrol EDRPOU 登记件挖名);' + UA + ')',
    [],
    [ev('联系方式与基础画像', 'MikroTik Master+VAD(名录信号);deps.ua 官网;Ubiquiti 官方分销谱', 'https://deps.ua/'),
     ev('近期动态与线索', 'Telecom Ukraine 2026 冠名赞助=行业活动曝光窗', 'https://deps.ua/')],
    '乌克兰 ISP/企业 VAD 分销;' + UA, '分销大户谱',
    ('Master+VAD 双档=链窗', '具名缺', '展会冠名赞助曝光', 'MikroTik 官方链'),
    UA + '；具名缺(守档准由)', 'Dear DEPS Team,',
    trend='2026-10-08 R66 24 波谱名牌(Master+VAD 名录信号)'))

R.append(rec('A-433', 'Lanbox',
    'Lanbox(乌克兰 Kyiv;**MikroTik Reseller(名录信号);FB 自宣 MikroTik+Ubiquiti 官方分销谱**;零售+小批发谱;具名决策人谱面未锁→守档准由(波次二登记件/FB 管理页挖名);' + UA + ')',
    [],
    [ev('联系方式与基础画像', 'MikroTik Reseller(名录信号);lanbox.com.ua;MT+UBNT 官方分销 FB 自宣', 'https://lanbox.com.ua/'),
     ev('业务定位', '基辅零售+小批发网络件谱', 'https://lanbox.com.ua/')],
    '乌克兰零售/小批发;' + UA, '小中铺谱',
    ('MT+UBNT 双牌自宣', '铺面小谱', 'FB 自营活跃谱', 'MikroTik 官方链'),
    UA + '；具名缺(守档准由)', 'Dear Lanbox Team,'))

R.append(rec('A-434', 'Lanmarket',
    'Lanmarket(乌克兰 Chernivtsi,2008 创 18 年;**MikroTik Reseller(名录信号);官网联络版面直接自署 4 名销售含手机号=official-self-published 金谱**;Crunchbase 档在册;' + UA + ')',
    [('Беркаев Максим Сергеевич', '销售(官网联络版自署+手机号)', 'lanmarket.ua 联络版', O, 'https://lanmarket.ua/kontakty/'),
     ('Шарапов Дмитрий', '销售(官网联络版自署+手机号)', 'lanmarket.ua 联络版', O, 'https://lanmarket.ua/kontakty/'),
     ('Дячук Семен Вікторович', '销售(官网联络版自署+手机号)', 'lanmarket.ua 联络版', O, 'https://lanmarket.ua/kontakty/'),
     ('Бойко Анатолий Іванович', '销售(官网联络版自署+手机号)', 'lanmarket.ua 联络版', O, 'https://lanmarket.ua/kontakty/')],
    [ev('决策链与对接人', '官网联络版面自署 4 销售(Беркаев/Шарапов/Дячук/Бойко)含手机号=O 级自署谱', 'https://lanmarket.ua/kontakty/'),
     ev('联系方式与基础画像', 'Chernivtsi;2008 创;lanmarket.ua;Crunchbase 档', 'https://lanmarket.ua/')],
    '乌克兰西部 ISP/企业谱;' + UA, '10-50 铺谱',
    ('官网 4 销售具名手机号=金谱', '零售身段', '18 年老铺', 'MikroTik 官方链'),
    UA + '；具名为销售线非采购线(波次二挖采购)', 'Доброго дня, шановні,'))

R.append(rec('A-435', 'Lantorg',
    'Lantorg(乌克兰 Kharkiv,**2012 创 14 年;MikroTik Reseller(名录信号);自设服务中心谱**;哈尔科夫东部谱;具名决策人谱面未锁→守档准由;' + UA + ')',
    [],
    [ev('联系方式与基础画像', '2012 创;Kharkiv;lantorg.com;服务中心谱', 'https://lantorg.com/'),
     ev('业务定位', 'MT 官方渠道零售+售后服务中心谱', 'https://lantorg.com/')],
    '乌克兰东部 ISP/企业;' + UA, '小中铺谱',
    ('服务中心=售后绑定谱', '东部战区委顿', '14 年谱', 'MikroTik 官方链'),
    UA + '；具名缺(守档准由)', 'Dear Lantorg Team,'))

R.append(rec('A-436', 'Lux-Mobil',
    'Lux-Mobil(乌克兰 Kyiv;**MikroTik Reseller(名录信号);维修中心谱**;移动件+网络件店谱;具名决策人谱面未锁→守档准由;' + UA + ')',
    [],
    [ev('联系方式与基础画像', 'lux-mobil.com.ua;Kyiv;维修中心谱', 'https://lux-mobil.com.ua/'),
     ev('业务定位', '移动+网络件零售维修铺', 'https://lux-mobil.com.ua/')],
    '乌克兰零售维修;' + UA, '小铺谱',
    ('维修中心=技术绑谱', '铺面小', '维修口碑谱', 'MikroTik 官方链'),
    UA + '；具名缺(守档准由)', 'Dear Lux-Mobil Team,'))

R.append(rec('A-437', 'Network Discount',
    'Network Discount(乌克兰 Kyiv;**MikroTik Reseller(名录信号);多牌批发谱(0(800) 33-32-83 全国免费电话)**;批发身段;具名决策人谱面未锁→守档准由;' + UA + ')',
    [],
    [ev('联系方式与基础画像', 'networkdiscount.com.ua;Kyiv;0(800) 33-32-83', 'https://networkdiscount.com.ua/'),
     ev('业务定位', '多牌网络件批发谱=过货身段', 'https://networkdiscount.com.ua/')],
    '乌克兰批发;' + UA, '批发铺谱',
    ('批发=过货窗', '多牌杂谱', '全国免费电话=规模谱', 'MikroTik 官方链'),
    UA + '；具名缺(守档准由)', 'Dear Network Discount Team,'))

R.append(rec('A-438', 'Setevuha',
    'Setevuha(乌克兰 Kyiv;**MikroTik Reseller(名录信号);自宣 MikroTik 乌克兰官方分销谱;双域 setevuha.ua/setevuha.com.ua(域差旗注)**;具名决策人谱面未锁→守档准由;' + UA + ')',
    [],
    [ev('联系方式与基础画像', 'setevuha.com.ua 主站;setevuha.ua 双域谱(域差旗注);Kyiv', 'https://setevuha.com.ua/'),
     ev('业务定位', 'MT 乌克兰官方分销自宣谱', 'https://setevuha.com.ua/')],
    '乌克兰 ISP/企业;' + UA, '小中铺谱',
    ('官方分销自宣+双域谱', '域差旗', '双域同牌谱', 'MikroTik 官方链'),
    UA + '；双域差旗注；具名缺(守档准由)', 'Dear Setevuha Team,'))

R.append(rec('A-439', 'Technotrade LLC',
    'Technotrade LLC(乌克兰 Kyiv,**EDRPOU 32251835,2002 创 24 年;MikroTik Reseller(名录信号)+Ubiquiti 官方分销官网自宣;youcontrol 登记件:Authorised person+真实受益人(UBO)=Доберчак Сергій Валерійович=登记具名 O 级金谱**;' + UA + ')',
    [('Доберчак Сергій Валерійович', '授权代表人+真实受益人(youcontrol EDRPOU 32251835 登记件)', 'youcontrol 登记件', O, 'https://youcontrol.com.ua/')],
    [ev('决策链与对接人', 'youcontrol EDRPOU 32251835:Authorised person+UBO=Доберчак Сергій Валерійович(登记件具名)', 'https://youcontrol.com.ua/'),
     ev('联系方式与基础画像', '2002 创;Kyiv;technotrade.com.ua;MT+Ubiquiti 官方分销官网自宣', 'https://technotrade.com.ua/')],
    '乌克兰 ISP/企业 24 年老分销;' + UA, '分销中户谱',
    ('UBO 登记具名=直达业主谱', '登记件需 opt-in 照转', '24 年分销老户', 'MikroTik 官方链'),
    UA + '；登记名直发需 opt-in', 'Доброго дня, пане Доберчак,',
    trend='2026-10-08 R66 24 波谱名牌(youcontrol UBO 具名谱)'))

R.append(rec('A-440', 'Viatec',
    'Viatec(乌克兰 Kyiv;**EDRPOU 36413740;MikroTik Master+VAD(名录信号);官网自宣 2018 起 MikroTik Master-дистрибьютор(大师分销 8 年);Hikvision/Dahua/Ruijie 官方分销=安防大户谱**;ua-region 登记件:Head=Bilous Oleksandr Anatolijovych(登记表级);smart-city/机场/加油站客户场景谱=关键基建邻谱→民用商业限定前句加厚(只谈民用园区/商用场景,不涉军防/执法用途);' + UA + ')',
    [('Bilous Oleksandr Anatolijovych', 'Head(ua-region EDRPOU 36413740 登记表)', 'ua-region 登记件', G, 'https://www.ua-region.com.ua/')],
    [ev('决策链与对接人', 'ua-region EDRPOU 36413740:Head: Bilous Oleksandr Anatolijovych(登记表级,弱于官网件)', 'https://www.ua-region.com.ua/'),
     ev('联系方式与基础画像', '官网自宣 2018 起 MT Master-дистрибьютор;Hikvision/Dahua/Ruijie 官方分销;smart-city/机场/加油站场景', 'https://viatec.ua/')],
    '乌克兰安防+智能城市分销;' + UA + '；关键基建场景只谈民用商用侧', '分销大户谱',
    ('Master 8 年+安防三巨头牌谱=大户', '安防大户=军警邻谱风险', 'smart-city 扩大谱', 'MikroTik 官方链+安防链'),
    UA + '；**安防/关键基建商用限定注(民用商用侧,不涉军防执法)**；登记名直发需 opt-in', 'Доброго дня, пане Bilous,',
    trend='2026-10-08 R66 24 波谱名牌(Master 8 年+安防大户)'))

# ============ 段二:以色列+保加利亚(A-441~443) ============
R.append(rec('A-441', 'Dipole Wireless Communication',
    'Dipole Wireless Communication(以色列;**MikroTik Reseller(名录信号);dipole.co.il+dipole-ltd.com 双域自宣「authorized distributor of MikroTik in ISRAEL」;Ubiquiti/Compex/Wouxun/L-com 官方进口牌谱**;+972 3-5732221;info@dipole.co.il;**R63 退信注:dipole-ltd.com 生平条 46h 观察期 2026-10-08 届满→转永久退信处置(不删档内邮箱、标「发不过去」,主触替代口=dipole.co.il 域在册)**;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'dipole.co.il+dipole-ltd.com 双域;自宣 authorized distributor of MikroTik in ISRAEL;+972 3-5732221', 'https://www.dipole.co.il/'),
     ev('近期动态与线索', 'R63 退信注:dipole-ltd.com 生平条 46h 观察 2026-10-08 届满→转永久(替代口 dipole.co.il)', 'https://www.dipole.co.il/')],
    '以色列 WISP/企业谱', '分销中户谱',
    ('以色列官方授权自宣=唯一链窗', '退信域降档', '双域牌谱多牌进口', 'MikroTik 官方链'),
    '**R63 退信期满转永久注(dipole-ltd.com;替代口 dipole.co.il)**；具名缺(守档准由)', 'Dear Dipole Team,',
    trend='2026-10-08 R66 24 波谱名牌(R63 退信期满注)'))

R.append(rec('A-442', 'MTBG OOD（mikrotikbg.shop）',
    'MTBG OOD(保加利亚 Burgas,131 Tsar Simeon I;**MikroTik Master+VAD(名录信号);mikrotikbg.shop 官网 schema 自宣「Official MikroTik distributor since 2018(MTCSA)」+培训/证书页;500 SKU 全谱**;+359 2 451 2525;info@mikrotikbg.shop;**与 A-367(Petar Dimitrov,波 22 人名档,同域 mikrotikbg.shop)同人同域镜像注:A-367 已发档谱位,A-442 公司体档,首触错峰 7+ 天,仍走 A-367 位主发**;具名决策人谱面未锁(除 Petar 本体外)→守档准由)',
    [],
    [ev('联系方式与基础画像', 'mikrotikbg.shop schema:Official MikroTik distributor since 2018;Burgas;+359 2 451 2525;500 SKU', 'https://mikrotikbg.shop/'),
     ev('近期动态与线索', '镜像错峰注:A-367 Petar Dimitrov 同域同人(波 22 已发谱位)', 'https://mikrotikbg.shop/')],
    '保加利亚 WISP/企业+培训谱', '分销中户谱',
    ('官方分销 2018 起+培训页=链窗', '镜像错峰', '500 SKU 全谱', 'MikroTik 官方链'),
    '**A-367 同人同域镜像错峰注**；具名缺(守档准由)', 'Dear MTBG Team,'))

R.append(rec('A-443', 'Rootelsat, Ltd.（vesuviustreamline.com）',
    'Rootelsat, Ltd.(保加利亚 Shumen,Industrialna zona ZIENO #2;**MikroTik Reseller(名录信号);vesuviustreamline.com 官网自宣「official distributor of Mikrotik for Bulgaria」=官网授权自宣金句;Ubiquiti 同分销;GPEN 光纤概念+60GHz+视频监控/NVR 谱**;+359 54 862 991;office@vstl.eu;**希腊 Rhodes 点具名联系 Ivo Valev +30 693 243 5176(官网联系件自署)=跨境点谱**;zoominfo 法人拼作 RutelSat OOD(名差旗注);11-50 人)',
    [('Ivo Valev', '希腊 Rhodes 点联系(官网联系件自署手机号)', 'vesuviustreamline.com 联系版', O, 'https://vesuviustreamline.com/en/form/1/rootelsat-ltd.html')],
    [ev('联系方式与基础画像', '官网自宣 official distributor of Mikrotik for Bulgaria;Shumen;+359 54 862 991;GPEN/60GHz/监控谱', 'https://vesuviustreamline.com/en/'),
     ev('决策链与对接人', '官网联系件:希腊 Rhodes 点 Ivo Valev +30 693 243 5176(自署)=跨境具名谱', 'https://vesuviustreamline.com/en/form/1/rootelsat-ltd.html')],
    '保加利亚+希腊罗德岛 WISP/监控谱', '11-50 人;分销中户',
    ('官网授权自宣金句+GPEN 光纤谱=对口窗', '法人名差旗(RutelSat)', 'Rhodes 跨境点=希腊面延伸', 'MikroTik 官方链'),
    '名差旗注(Rootelsat↔RutelSat OOD)；具名为 Rhodes 点非采购线(波次二)', 'Dear Mr. Valev,'))

# ============ 段三:人名/机构顾问档 5(A-429/430/431/444/449) ============
R.append(person('A-429', 'Michiel Visser - Connection Services', '荷兰／Deventer', 'connectionservices.nl',
    '顾问 OEM 对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'connectionservices.nl=德文特顾问谱;**CSV 信号:MTCNA+MTCRE+MTCWE+MTCINE+MTCIPv6E 五证谱**;档定 p1=CONSULT-OEM 供位', 'Beste heer Visser,'))
R.append(person('A-430', 'MikroTrain（荷兰 MikroTik 培训）', '荷兰', 'mikrotrain.nl',
    '顾问 OEM 对照单元($180 锚点一致);—(合作探询,无量产报价);**机构名档(认证讲师,教 MTCNA→MTCINE 全部课程)**', WHY1,
    'mikrotrain.nl=荷兰 MikroTik 全科培训机构档(机构名号档,类 A-421);档定 p1=CONSULT-OEM 供位', 'Beste MikroTrain,'))
R.append(person('A-431', 'Tomislav Vrebac - Kerberos', '克罗地亚／Kraljevica', 'kerberos.hr',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'kerberos.hr=克尔克湾顾问谱;**CSV 信号:MTCNA+MTCEWE 双证谱**', 'Poštovani gospodine Vrebac,'))
R.append(person('A-444', 'Frédéric Gauthier - ProRéseau', '加拿大／Québec', 'proreseau.net',
    '顾问对照单元($180 锚点一致);—(合作探询,无量产报价)', WHY1,
    'proreseau.net=魁北克法区顾问谱;**CSV 信号:MTCNA+MTCSE+MTCEWE 三证谱**;**同名片噪排除注:检索命中法国米卢斯 PRORÉSEAU→PROÉVOLUTION 人力谱=无关同名,已排**', 'Bonjour M. Gauthier,'))
R.append(person('A-449', 'Wilmer Almazan - Arawi IT Consulting', '加拿大／Winnipeg', 'arawi.ca',
    '顾问 OEM 对照单元($180 锚点一致);—(合作探询,无量产报价', WHY1.replace(')', ')；十全证官方培训师金谱'),
    'arawi.ca+mikrotiktraining.ca+thenetworktrip.com 三域谱;**Certified MikroTik Trainer #TR0516(官方培训名录件 O);十全证;TechManitoba 会员档:16+ 年、2018 起 1000+ 学员过证、北美+中美 MUM 公认讲者、英西双语**;MikroTik 官方 Training Schedule Winnipeg 2026-10 起连期在列;档定 p1=CONSULT-OEM 供位', 'Dear Mr. Almazan,'))

# ============ 段四:加拿大公司档 4(A-445~448) ============
R.append(rec('A-445', 'JRS Global Technologies Ltd',
    'JRS Global Technologies Ltd(加拿大 Oakville, ON;**MikroTik Master+VAD(名录信号);官网/PRLog 自宣「master distributor of MikroTik」+altostrat 档列 Master Distributor & VAD;自有牌 Optitera=与波 23 A-379 Optitera Global Networks 同谱关联互注(同集团双档,错峰主发走 A-379 Optitera 位)**;RocketReach 载 Shivani Mane Inside Sales(加拿大具名 G)/Kumar Jha/Rahul Singh(印度遥);约 5 人小团谱)',
    [('Shivani Mane', 'Inside Sales(RocketReach 谱,加拿大岗)', 'rocketreach.co 件', G, 'https://rocketreach.co/')],
    [ev('决策链与对接人', 'RocketReach:Shivani Mane Inside Sales(加岗);Kumar Jha/Rahul Singh(印遥)', 'https://rocketreach.co/'),
     ev('联系方式与基础画像', 'Oakville ON;jrsglcanada.com;「master distributor of MikroTik」自宣;Optitera 关联互注', 'https://www.jrsglcanada.com/')],
    '加拿大 VAD 分销+自有牌谱', '小团谱(约 5 人)',
    ('Master+VAD 自宣=链窗', '小团谱', 'Optitera 双档互注谱', 'MikroTik 官方链'),
    '**A-379 Optitera 同谱关联互注(错峰主发走 A-379 位)**；具名为销售线(波次二挖采购)', 'Dear Ms. Mane,',
    trend='2026-10-08 R66 24 波谱名牌(A-379 关联互注)'))

R.append(rec('A-446', 'MBSI WAV',
    'MBSI WAV(加拿大 Medicine Hat, AB;**MikroTik Master+VAD(名录信号);官网自宣 MT 授权分销+altostrat 档列 Master Distributor(加)**;Cambium/TP-Link/ALTALabs/Adtran/Tarana 牌谱;(866) 597-6274;sales@mbsiwav.com;11-50 人;**政府/教育/医疗/公用事业行业列谱→守界注:只谈民用商用网建场景,不涉执法/军防用途**;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'Medicine Hat AB;mbsiwav.com;(866) 597-6274;MT 授权分销官网自宣', 'https://www.mbsiwav.com/'),
     ev('目标行业与场景', 'WISP/ISP 谱+政府/教育/医疗/公用事业行业列=守界注谱', 'https://www.mbsiwav.com/')],
    '加拿大 WISP/ISP+公部门行业谱', '11-50 人',
    ('加 Master 档=链窗', '公部门行业列', 'Cambium/Tarana 邻牌谱', 'MikroTik 官方链'),
    '**政府/医疗行业守界注(只谈民用商用,不涉执法军防)**；具名缺(守档准由)', 'Dear MBSI WAV Team,'))

R.append(rec('A-447', 'Mahkesis Group Inc.',
    'Mahkesis Group Inc.(加拿大 Winnipeg, MB;**MikroTik Reseller(名录信号);shop.mahkesis.com 电商谱 73 MikroTik SKU 在架**;admin@mahkesis.com;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'shop.mahkesis.com 电商;73 MT SKU;Winnipeg;admin@mahkesis.com', 'https://shop.mahkesis.com/'),
     ev('业务定位', '温尼伯 IT 电商谱', 'https://shop.mahkesis.com/')],
    '加拿大中西部电商/企业谱', '小中铺谱',
    ('73 SKU 深度谱=对口窗', '电商身段', '原住民经济圈谱(名谱)', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Dear Mahkesis Team,'))

R.append(rec('A-448', 'Solimedia Technology Inc',
    'Solimedia Technology Inc(加拿大 Vancouver, BC;**MikroTik Master+VAD(名录信号);官网 FAQ 页自宣授权分销谱**;BC 谱;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'solimedia.net;Vancouver BC;FAQ 页授权分销自宣', 'https://www.solimedia.net/'),
     ev('业务定位', 'BC MT+VAD 分销谱', 'https://www.solimedia.net/')],
    '加拿大西部 ISP/企业谱', '小中分销铺',
    ('FAQ 授权自宣=链窗', '薄谱', 'Master+VAD 名录信号', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Dear Solimedia Team,'))

# ============ 段五:匈牙利 5+北马其顿 2(A-450~456) ============
R.append(rec('A-450', 'AXTEK line Kft.',
    'AXTEK line Kft.(匈牙利 Pécel;**分销(Antaira 授权,工业以太网);hunspace 航天产业页载 Space industry contact person: Levente Orosi(具名航天联络谱 G);ceginformacio 同税号登记法体名作 IETEK LINE Kft.(名差旗注)**;只接 B2B;**p1=STI-288GP 供位谱**)',
    [('Levente Orosi', 'Space industry contact person(hunspace 产业页载)', 'hunspace.hu 件', G, 'https://hunspace.hu/')],
    [ev('决策链与对接人', 'hunspace 页:Space industry contact person Levente Orosi(产业页载具名)', 'https://hunspace.hu/'),
     ev('联系方式与基础画像', 'axtek.hu;Antaira 授权工业分销;ceginformacio 同税号法体名差旗:IETEK LINE Kft.;B2B only', 'https://axtek.hu/')],
    '匈牙利工业自动化/航天产业网建谱;**航天联络=民用航天商用限定句(只做民用商用网建,不涉军防航天)**', '小中分销谱',
    ('Antaira 授权=工业链窗', '法体名差旗', 'hunspace 页具名谱', '工业以太网链'),
    '**名差旗注(AXTEK↔IETEK LINE Kft.)**；航天场景民用商用限定注；具名为航天联络非采购线', 'Kedves Orosi úr,',
    trend='2026-10-08 R66 24 波谱名牌(p1=STI-288GP 供位)'))

R.append(rec('A-451', 'AbsolCom Kft.',
    'AbsolCom Kft.(匈牙利;**MikroTik Reseller(名录信号);B2B 注册会员制批发谱**;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'absolcom.hu;B2B 注册会员制批发谱', 'https://absolcom.hu/'),
     ev('业务定位', 'MT 官方渠道 B2B 批发铺', 'https://absolcom.hu/')],
    '匈牙利 B2B 批发谱', '小中铺谱',
    ('B2B 批发=过货窗', '薄谱', '会员制谱', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Kedves AbsolCom Csapat,'))

R.append(rec('A-452', 'AccessPoint Kft.',
    'AccessPoint Kft.(匈牙利 Budapest;**MikroTik Master(名录信号);MTCNA/MTCRE/MTCWE/MTCINE 官方认证培训院+批发分销+OT Networking 工业线(Teltonika/RAD;官网公示 official distributors 谱)=培训+工业双谱金档**;具名决策人谱面未锁→守档准由(波次二走培训讲师具名挖)',
    [],
    [ev('联系方式与基础画像', 'accesspoint.hu;MTCNA/MTCRE/MTCWE/MTCINE 官方认证培训院谱;Master 名录信号', 'https://accesspoint.hu/'),
     ev('业务定位', 'OT Networking 工业线(Teltonika/RAD official distributors 公示)', 'https://accesspoint.hu/')],
    '匈牙利培训+工业 OT 分销谱', '分销中户谱',
    ('官方培训院+工业 OT 双谱=高密链窗', '具名缺', 'Master 名录信号', 'MikroTik 官方链+工业链'),
    '具名缺(守档准由,波次二走讲师具名挖)', 'Kedves AccessPoint Csapat,',
    trend='2026-10-08 R66 24 波谱名牌(培训院金档守档)'))

R.append(rec('A-453', 'Controsys Control Engineering Ltd.',
    'Controsys Control Engineering Ltd.(匈牙利 Budapest,Felső Határ út 20,H-1112;**分销(AVEVA/Red Lion/N-Tron/Sixnet/Softing 工业渠道);HMS 官方经销商名录档(Anybus/Ewon/N-Tron 谱);Red Lion 页面载「甚至军用级实时以太网交换机」字样=军防邻谱守界注**;+36 1 248-1416;具名决策人谱面未锁→守档准由;**p1=STI-288GP 供位谱;与波 24 A-478 ATEG(德国,HMS/Red Lion 同谱链)关联互注**)',
    [],
    [ev('联系方式与基础画像', 'controsys.hu;Budapest;AVEVA/Red Lion/N-Tron/Sixnet/Softing 工业分销;+36 1 248-1416', 'https://controsys.hu/'),
     ev('业务定位', 'HMS 官方经销商名录档载 Anybus/Ewon/N-Tron 谱;Red Lion 军用级字样=守界注', 'https://controsys.hu/')],
    '匈牙利 SCADA/工业控制分销谱;**军用级器件谱民用商用限定注(只做民用商用工业网建)**', '分销中户谱',
    ('HMS/AVEVA 双授权金档=工业链窗', '军用级字样邻谱', '工业以太网对口', '工业链'),
    '**军用级字眼守界注(民用商用工业限定)**；A-478 同谱链互注；具名缺(守档准由)', 'Kedves Controsys Csapat,',
    trend='2026-10-08 R66 24 波谱名牌(p1=STI-288GP 供位)'))

R.append(rec('A-454', 'Wireless-Bolt',
    'Wireless-Bolt(匈牙利 Albertirsa;**MikroTik Reseller(名录信号);零售铺谱**;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'wireless-bolt.hu;Albertirsa;零售铺谱', 'https://wireless-bolt.hu/'),
     ev('业务定位', '匈牙利 MT 零售铺', 'https://wireless-bolt.hu/')],
    '匈牙利零售/小批发谱', '小铺谱',
    ('官方渠道在册', '铺面小', '零售稳定谱', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Kedves Wireless-Bolt Csapat,'))

R.append(rec('A-455', 'ALL4NET DOOEL',
    'ALL4NET DOOEL(北马其顿 Skopje(Aerodrom 区,Ulica Mite Bogoevski 83a;contactout 另载 Blagoja Stefkovski 30=双址差旗注);**MikroTik Master+VAD(名录信号);LI 自宣「Official distributor of Mikrotik and Ubiquiti for Macedonia」=官方金句;contact@overnet.com.mk/info@all4net.mk;**toten.com.mk(roster 挂域)+all4net.mk+overnet.com.mk=三域谱差旗注**;contactout 具名梯队:Manager Marjan Davcevski+Head of Marketing Jovan Gjorgjiev+Sales Naum Stojchevski+Telecom Technician Jan Korosec;Grandstream/Synology/APC/Draka 牌谱**;1-50 人(规模差旗注);+389 2 321 7799;**与 A-466 3NET(塞尔维亚)培训合作互注:Saša Blagojević 与 3Net+All4Net 合办 MTCNA 课程谱**)',
    [('Marjan Davcevski', 'Manager(contactout/LI 具名谱)', 'contactout.com 件', G, 'https://contactout.com/company/All4Net-68616'),
     ('Jovan Gjorgjiev', 'Head of Marketing(contactout/LI 具名谱)', 'contactout.com 件', G, 'https://contactout.com/company/All4Net-68616'),
     ('Naum Stojchevski', 'Sales Department(contactout/LI 具名谱)', 'contactout.com 件', G, 'https://contactout.com/company/All4Net-68616')],
    [ev('决策链与对接人', 'contactout 具名梯队:Davcevski Manager/Gjorgjiev Head of Marketing/Stojchevski Sales/Korosec Technician', 'https://contactout.com/company/All4Net-68616'),
     ev('联系方式与基础画像', 'LI 自宣 Official distributor of Mikrotik and Ubiquiti for Macedonia;Master+VAD 名录信号;+389 2 321 7799;三域谱(toten/all4net/overnet)', 'https://mk.linkedin.com/company/all4net')],
    '北马其顿 ISP/企业全国分销谱', '10-50 人(差旗注)',
    ('Master+VAD+LI 官方金句=金档链窗', '三域+双址差旗', '营销经理具名谱', 'MikroTik 官方链'),
    '**三域差旗注(toten.com.mk↔all4net.mk↔overnet.com.mk)+双址注**；A-466 培训合作互注；具名为营销/销售线(波次二挖采购)', 'Почитуван г-дин Davcevski,',
    trend='2026-10-08 R66 24 波谱名牌(Master+VAD 金档+三域谱)'))

R.append(rec('A-456', 'Treco',
    'Treco(北马其顿 Skopje,Hasan Pristina(Jadranska Magistrala) nr 58;**MikroTik Master(名录信号)+altostrat Master Distributor 档双证**;info@treco.mk;+389 70 411 415;treco.mk 全品类电商谱(交换/路由/无线/SFP 全谱+MKD/€双价谱);具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'treco.mk;Skopje;+389 70 411 415;Master 名录信号+altostrat Master 档', 'https://treco.mk/product-category/mikrotik'),
     ev('业务定位', '全品类 MT 电商谱(CRS310/CCR/CRS328-24P-4S+RM 在架)', 'https://treco.mk/')],
    '北马其顿电商批发谱', '小中分销铺',
    ('Master 名录双证=链窗', '具名缺', 'CRS328-24P 在架=同型对照谱', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Dear Treco Team,'))

# ============ 段六:土耳其 9 连(A-457~465) ============
R.append(rec('A-457', 'C TECH BILISIM（enucuzmikrotik.com）',
    'C TECH Bilişim Teknolojileri(土耳其 Fatih, Istanbul;**MikroTik Reseller(名录信号);bilisimyol.com+enucuzmikrotik.com 双域同屏自宣「Türkiye mikrotik Master Distribitörü Ctech Bilişim」=Master 自宣谱;0850 480 44 47/44 74(双号差旗注);Garanti/Albaraka 双银行 IBAN 谱**;**R63 退信注:enucuzmikrotik.com 生平条 46h 观察期 2026-10-08 届满→转永久退信处置(标「发不过去」,主触替代口=bilisimyol.com 域在册;roster 网站字段即挂 bilisimyol.com,双域注)**;altostrat Reseller 档;Kryptos 加密器牌谱;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'bilisimyol.com+enucuzmikrotik.com 双域;「Türkiye mikrotik Master Distribitörü」自宣;Fatih Istanbul;0850 480 44 47', 'https://www.bilisimyol.com/'),
     ev('近期动态与线索', 'R63 退信注:enucuzmikrotik.com 46h 观察 2026-10-08 届满→转永久(替代口 bilisimyol.com)', 'https://www.bilisimyol.com/iletisim.aspx')],
    '土耳其 ISP/零售电商谱', '分销中户谱',
    ('Master 自宣双域谱=链窗', '退信域降档', '双银行 IBAN=合规谱', 'MikroTik 官方链'),
    '**R63 退信期满转永久注(enucuzmikrotik.com;替代口 bilisimyol.com)**；双号差旗注；具名缺(守档准由)', 'Dear C TECH Team,',
    trend='2026-10-08 R66 24 波谱名牌(R63 退信期满注)'))

R.append(rec('A-458', 'COOLTECH TRADING',
    'COOLTECH TRADING(Cooltech Trading Ltd.;土耳其 Ataşehir, Istanbul(Atatürk Mah. Mimoza 2 Sit. No:11 R/24);**MikroTik Master(名录信号);2009 创进口分销;约 70 零售点网络谱;altostrat Master Distributor 档**;0542 883 1111;info@cooltechtrading.com;Cambium 邻牌谱;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'cooltechtrading.com;Ataşehir Istanbul;0542 883 1111;2009 创;约 70 零售点', 'https://www.cooltechtrading.com/hakkimizda.aspx'),
     ev('业务定位', 'Master 名录信号+altostrat Master 档;Cambium 邻牌', 'https://www.cooltechtrading.com/mikrotik.aspx')],
    '土耳其 B2B 分销+零售网谱', '分销中户谱',
    ('Master 名录+70 点零售网=链窗', '具名缺', '17 年进口分销谱', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Dear COOLTECH Team,'))

R.append(rec('A-459', 'Internetten Ltd.（wi.com.tr）',
    'İnternetten Teknoloji Ltd. Şti.(土耳其 Gebze, Kocaeli(Sultan Orhan Mah. İlyasbey Cad. 1117 Sk. No:6);**MikroTik Master(名录信号);wi.com.tr/FB 自宣「MikroTik Türkiye Master Distributor」;internetten.com.tr 另站:1999 起 MT 分销 vs LI 2011 vs 创立 2009=三纪年差旗注;Ubiquiti+RF Elements 土分销牌谱**;0262 644 66 63/0850 532 23 61;11-50 人;ISP/DC/酒店热点+Radius 软件谱;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'wi.com.tr;Gebze;0262 644 66 63;Master Distributor 自宣;Ubiquiti/RF Elements 牌谱', 'https://www.wi.com.tr/Mikrotik-RB'),
     ev('业务定位', 'internetten.com.tr/LI/FB 三纪年差旗(1999/2011/2009)=谱面差旗注', 'https://internetten.com.tr/')],
    '土耳其 ISP/DC/酒店热点谱', '11-50 人',
    ('Master 自宣+Radius 软件谱=深谱窗', '三纪年差旗', 'ISP 项目化服务谱', 'MikroTik 官方链'),
    '**三纪年差旗注**；具名缺(守档准由)', 'Dear İnternetten Team,'))

R.append(rec('A-460', 'NODENET GLOBAL',
    'NODENET GLOBAL(土耳其 Istanbul;**MikroTik Master+VAD(名录信号);mikrotik.com/buy 官方名录 Master Distributor 金证;官网新闻自宣「MikroTik Türkiye Distribütörü Oldu!」=2026 新任分销窗(新签蜜月期!)**;+90 533 391 22 32;shop.nodenetglobal.com 电商;ISP/DC/企业项目+云/数字转型谱;具名决策人谱面未锁→守档准由)',
    [],
    [ev('近期动态与线索', '官网新闻:MikroTik Türkiye Distribütörü Oldu!(2026 新任=新签窗)', 'https://nodenetglobal.com/'),
     ev('联系方式与基础画像', 'mikrotik.com/buy 官方名录 Master Distributor;Istanbul;+90 533 391 22 32;ISP/DC 项目谱', 'https://mikrotik.com/buy/')],
    '土耳其 ISP/DC/企业项目谱', '分销中户谱',
    ('米官方名录金证+2026 新任=当季蜜月窗', '新体谱薄', 'shop 电商即时谱', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Dear NODENET Team,',
    trend='2026-10-08 R66 24 波谱名牌(官方名录金证+2026 新任窗)'))

R.append(rec('A-461', 'Net Vizyon（4mimo.com）',
    'Net Vizyon Bilgi İşlem(土耳其;**MikroTik Reseller(名录信号);Ubiquiti/Infinet/Mimosa/Siklu 土耳其授权分销四牌+Jirous/Ruijie/Cnet 销售谱(netvizyon.biz 自宣);4mimo.com 电商**;2015 土耳其 IT 500 强第 183 位谱;yenitelekom.com/Novabis 关联谱;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', '4mimo.com 电商+netvizyon.biz/net 三域谱;Ubiquiti/Infinet/Mimosa/Siklu 授权分销', 'http://www.netvizyon.biz/'),
     ev('业务定位', '2015 土耳其 IT500 第 183 位;无线专牌大户谱', 'https://4mimo.com/')],
    '土耳其无线专牌 ISP 谱', '分销中户谱',
    ('四牌授权+IT500=实力谱', 'MT 仅零售线', 'SIKLU/Infinet 高频段专谱', 'MikroTik 官方链(零售线)'),
    '具名缺(守档准由)；MT 线为零售位(主推力度中等)', 'Dear Net Vizyon Team,'))

R.append(rec('A-462', 'Nokta Elektronik',
    'Nokta Elektronik ve Bilişim Sistemleri A.Ş.(土耳其 Istanbul(Şişli Perpa Ticaret Merkezi A Blok K:2/B Blok K:8 No:907);**MERSİS 0631-0730-5210-0020;Tic. Sicil 555138-0;分销(ORing 授权=工业网件);2005-05-26 创 21 年;$7.5M;91-500 人(zoominfo 51-200/signalhire 200-500 规模差旗注);安防 CCTV/火警/护士呼叫/中央时钟/道闸停车+医疗电子(医院病房系统=医疗守界注:只谈民用商用,不涉执法军防)**;+90 212 222 87 80;nokta@noktaelektronik.net;zoominfo 梯队:Ersan Çağlar COO/Chief Digital Officer(具名 G)+Casey Chen;建材/布线/音视频/RF 谱)',
    [('Ersan Çağlar', 'Chief Operating Officer/Chief Digital Officer(zoominfo 谱)', 'zoominfo.com 件', G, 'https://www.zoominfo.com/c/nokta-elektronik/539250914')],
    [ev('决策链与对接人', 'zoominfo:Ersan Çağlar COO/CDO(具名谱);Casey Chen', 'https://www.zoominfo.com/c/nokta-elektronik/539250914'),
     ev('联系方式与基础画像', 'noktaelektronik.net;Şişli Istanbul;+90 212 222 87 80;ORing 授权;MERSİS 0631-0730-5210-0020;医疗电子/安防谱', 'https://www.noktaelektronik.net/en')],
    '土耳其安防+医疗电子大户谱;**医疗/安防行业守界注(只谈民用商用网建)**', '200-500 人大户',
    ('ORing 授权+大户身=高量窗', '医疗/安防行业守界', 'COO 具名谱', '工业网件链+安防链'),
    '**医疗行业守界注(民用商用限定)**；规模差旗注；具名为 COO 层(直发需 opt-in)', 'Dear Mr. Çağlar,',
    trend='2026-10-08 R66 24 波谱名牌(ORing 授权大户)'))

R.append(rec('A-463', 'Poyraz Network',
    'Poyraz Network(Poyraz Ağ Ekipmanları Ltd. Şti.;土耳其 Gölcük, Kocaeli(Dumlupınar Mah. Atatürk Bulvarı No:203/A-B);**MikroTik Master+VAD(名录信号);官网自宣「MikroTik Türkiye Master Distribütörü(2015 起)」;MTCNA/MTCRE/MTCIPV6E/MTCUME/MTCINE 教育课程 SKU=官方培训谱;309 SKU 深度谱**;0850 346 93 63/0850 303 7969/0544 722 5969;Ubiquiti/Mimosa/Cudy/RF Elements/Deltalink/Wow Grup GPON 牌谱;具名决策人谱面未锁→守档准由(培训讲师具名波次二挖)',
    [],
    [ev('联系方式与基础画像', 'poyraznetwork.com;Gölcük;0850 346 93 63;「Türkiye Master Distribütör 2015 起」自宣', 'https://www.poyraznetwork.com/tr/partners/mikrotik'),
     ev('业务定位', 'MT 教育课程 SKU(MTCIPV6E/MTCUME/MTCINE)在售=培训谱;309 SKU 深度', 'https://www.poyraznetwork.com/en/mikrotik-products')],
    '土耳其 ISP 分销+培训谱', '分销中户谱',
    ('Master+教育课 SKU 双谱=深链窗', '具名缺', '309 SKU 全谱', 'MikroTik 官方链+培训链'),
    '具名缺(守档准由,波次二讲师具名挖)', 'Dear Poyraz Network Team,',
    trend='2026-10-08 R66 24 波谱名牌(Master+教育双谱)'))

R.append(rec('A-464', 'Sekuritim Bilisim',
    'Sekuritim Bilişim(土耳其 Istanbul(Kadıköy);**MikroTik Reseller(名录信号);LI 自宣「土耳其首家 MikroTik 土耳其语认证培训公司」+business.site 自署 MikroTik Master Value Added Distributor & Training Center;Sekuritim OÜ(爱沙尼亚体,eu.sekuritim.com)=双国籍双体谱差旗注**;+90 216 302 22 21;info@/training@sekuritim.com;2008 创 18 年;2-10 人;渗透测试/漏扫/取证/安全架构网安谱+自有热点软件;**etkinlik.io 活动件:培训联络 Osman Kazdal(training@sekuritim.com 自署)=具名谱**)',
    [('Osman Kazdal', '培训联络(etkinlik.io 活动件自署 training@ 邮箱)', 'etkinlik.io 件', O, 'https://etkinlik.io/etkinlik/16386/mtcre-mikrotik-certified-routing-engineer-egitimi')],
    [ev('决策链与对接人', 'etkinlik.io 活动件:İletişim Osman Kazdal, training@sekuritim.com, 0216 302 22 21(自署)=O 级谱', 'https://etkinlik.io/etkinlik/16386/mtcre-mikrotik-certified-routing-engineer-egitimi'),
     ev('联系方式与基础画像', 'sekuritim.com;LI:土耳其首家 MT 土语认证培训公司(2008);Master VAD&Training Center 自署;Sekuritim OÜ 双体谱(爱沙尼亚)', 'https://www.linkedin.com/company/sekuritim')],
    '土耳其网安+MT 培训谱', '2-10 人小户',
    ('土首家培训院+Master VAD 自署=深链窗', '小户谱', 'Osman Kazdal 具名 O 级谱', 'MikroTik 官方培训链'),
    '**Sekuritim OÜ 双国籍双体差旗注**；具名为培训联络非采购线(波次二)', 'Dear Mr. Kazdal,',
    trend='2026-10-08 R66 24 波谱名牌(土首家培训院+具名谱)'))

R.append(rec('A-465', 'Sis Bil tek（wifianten.com）',
    'Sis Bil Tek İç ve Dış Ticaret Ltd. Şti.(土耳其 Tekirdağ Çorlu(Muhittin Mah. Adnan Kahveci Cad. No:25/a);**MikroTik Master+VAD(名录信号);ekşi sözlük 件:MikroTik 土官方分销 2011 起;KNOT/LoRa/IoT 专谱**;0850 277 59 59/0282 654 30 30;info@wifianten.com;四银行 IBAN 谱;Interline/LigoWave/RF Elements/Grandstream 牌谱;blog.wifianten.com 技博谱;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'wifianten.com;Çorlu;0850 277 59 59;2011 年 MT 官方分销谱(ekşi 件+官网)', 'https://www.wifianten.com/wifianten-mikrotik'),
     ev('业务定位', 'KNOT/LoRa/IoT 专谱;四银行 IBAN;技博谱', 'https://www.wifianten.com/')],
    '土耳其 IoT/无线专铺谱', '小中分销铺',
    ('Master+VAD+IoT 专谱=对口窗', '具名缺', 'LoRa/IoT 前段谱', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Dear Sis Bil Tek Team,'))

# ============ 段七:塞尔维亚 2+奥地利 3(A-466~470) ============
R.append(rec('A-466', '3NET',
    '3Net d.o.o.(塞尔维亚 Vranje,Proleterskih Brigada b.b.,17500;**MikroTik Reseller(名录信号);官网自宣「Uvoznik za Mikrotik u Srbiji」=MikroTik 塞进口商;官方扩容新闻「MikroTik je proširio svoju distributivnu mrežu u Srbiji preko kompanije 3Net」金句谱**;+381 17 400-234/+381 65 678 22 01;contact@3net.rs;**认证教练 Saša Blagojević 与 3Net+All4Net 合办 MTCNA 课程=与 A-455 ALL4NET 培训合作互注谱**)',
    [('Saša Blagojević', 'MikroTik 认证教练(与 3Net/All4Net 合办 MTCNA 课程,合作件谱)', '3net.rs 课程条', G, 'https://3net.rs/tag/mikrotik-srbija/')],
    [ev('决策链与对接人', 'Saša Blagojević 认证 MikroTik 教练,与 3Net(塞)+All4Net(马)合办 MTCNA obuka=跨境培训谱', 'https://3net.rs/tag/mikrotik-srbija/'),
     ev('联系方式与基础画像', '3net.rs;Vranje;+381 17 400-234;官方扩容新闻(塞分销网 3Net 扩容)', 'https://3net.rs/contact/')],
    '塞尔维亚南部 ISP/企业谱', '小中分销铺',
    ('塞官方扩容新闻金句=链窗', '南部小城谱', '跨境培训合作谱(All4Net 互注)', 'MikroTik 官方链'),
    '**A-455 ALL4NET 培训合作互注**；具名为合作教练非司内采购线(波次二)', 'Poštovani,',
    trend='2026-10-08 R66 24 波谱名牌(A-455 互注)'))

R.append(rec('A-467', 'Pixel Network LLC',
    'PIXEL NETWORK DOO NOVI SAD(塞尔维亚 Novi Sad,Partizanska 64A(法定)/Šajkaška 10(店谱)=双址差旗注;**MikroTik Reseller(名录信号);Matični 21608297;PIB 112105227;2020-08-21 创;20-50 人;营收 50-100m RSD 谱;注册局件 Zastupnik/Vlasnik(代表/业主)=Ivan B.(缩写名谱)**;pixelnetwork.rs;+381 21 271 85 04/+381 69 554 8052;office@pixelnetwork.rs;MT 85 SKU+视频监控/门禁/对讲安防谱)',
    [('Ivan B.(缩写)', 'Zastupnik/Vlasnik 代表/业主(注册局件缩写名谱)', 'pkspartner.rs 注册件', G, 'https://pretraga.pkspartner.rs/sr/kompanija/dc3b380935bee491/pixel-network-doo-novi-sad')],
    [ev('决策链与对接人', '注册局件:Zastupnici/Vlasnici Ivan B.(缩写);Matični 21608297;PIB 112105227;20-50 人;50-100m RSD', 'https://pretraga.pkspartner.rs/sr/kompanija/dc3b380935bee491/pixel-network-doo-novi-sad'),
     ev('联系方式与基础画像', 'pixelnetwork.rs;Novi Sad;+381 21 271 85 04;MT 85 SKU;监控/门禁安防谱', 'https://pixelnetwork.rs/')],
    '塞尔维亚安防系统+电商谱', '20-50 人',
    ('注册件业主缩写名谱+电商 85 SKU=窗', '缩写名谱(波次二补全名)', '安防系统主业谱', 'MikroTik 官方链'),
    '**双址差旗注(Partizanska 64A↔Šajkaška 10)**；缩写名谱(波次二补全名)', 'Poštovani,',
    trend='2026-10-08 R66 24 波谱名牌(注册件具名缩写谱)'))

R.append(rec('A-468', 'QEDV IT-Lösungen（Raum4 GmbH）',
    'QEDV IT-Lösungen(Raum4 GmbH 谱;奥地利 Tirol;**MikroTik Reseller(名录信号);shop.qedv.at 店谱:MikroTik CRS328-24P-4S+RM 24 口 PoE 交换机首页热卖在架=同型对照金口(我方 24 口 PoE 直接对标谱!);IT 全案店+Terra 工作站牌谱**;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'shop.qedv.at;Tirol;CRS328-24P-4S+RM 24 口 PoE 首页热卖(€499.17)', 'https://shop.qedv.at/'),
     ev('业务定位', 'IT 全案店谱(网络/服务器/数字化);24 口 PoE 在架=同型对照谱', 'https://shop.qedv.at/startseite/22-mikrotik-24-port-poe-switch-mit-4x-sfp.html')],
    '奥地利中小企 IT 全案谱', '小店谱',
    ('CRS328-24P 在架=同型对照金口', '小店薄谱', 'Terra 牌谱绑定', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Sehr geehrtes QEDV Team,'))

R.append(rec('A-469', 'TRIOTRONIK',
    'TRIOTRONIK Computer und Netzwerktechnik GmbH(奥地利 Weiz(Steiermark),Energiestraße 10;**MikroTik Master(名录信号);1995 创 31 年奥 VAD 领先;51-100 人;FN 287460k;UID ATU63017835;+43 3172 422990;office@triotronik.com;Kleine Zeitung 2026-09-23 专载:Geschäftsführer Peter Hofer-Perner+Thomas Thir-Greiter+Vertriebsleiter Bernhard Flicker(Prokurist)三驾金谱+新总部扩厂+德国据点新设=当季扩张窗(2026-09 报!);WKO 商会双 GF GISA 谱;TRIOTRONIK Holding GmbH 100% 母;HIKVISION/Ubiquiti/Extreme Networks 牌谱;自有光纤/铜缆/天线产线**;**p1 名录 424 但对标工业 PoE 全谱对口**)',
    [('Peter Hofer-Perner', 'Geschäftsführer(Kleine Zeitung 专载+WKO 商会+Impressum 三源)', 'kleinezeitung.at 件', O, 'https://www.kleinezeitung.at/artikel/41264825/so-will-die-firma-triotronik-in-weiz-weiter-wachsen'),
     ('Thomas Thir-Greiter', 'Geschäftsführer&Gesellschafter(WKO 商会+Impressum 谱)', 'firmen.wko.at 件', O, 'https://firmen.wko.at/triotronik-computer-und-netzwerktechnik-gmbh/steiermark/'),
     ('Bernhard Flicker', 'Vertriebsleiter&Gesellschafter&Prokurist(Kleine Zeitung 专载;销售总监=直对口)', 'kleinezeitung.at 件', O, 'https://www.kleinezeitung.at/artikel/41264825/so-will-die-firma-triotronik-in-weiz-weiter-wachsen')],
    [ev('决策链与对接人', 'Kleine Zeitung 2026-09-23:GF Peter Hofer-Perner+GF Thomas Thir-Greiter+Vertriebsleiter Bernhard Flicker(Prokurist)三驾金谱;新总部扩厂+德国据点新设=扩张窗', 'https://www.kleinezeitung.at/artikel/41264825/so-will-die-firma-triotronik-in-weiz-weiter-wachsen'),
     ev('联系方式与基础画像', 'triotronik.com;Weiz;+43 3172 422990;office@triotronik.com;1995 创;51-100 人;Master 名录信号;UID ATU63017835', 'https://akademie.triotronik.com/impressum/')],
    '奥地利 VAD 网络基建大户+教育/企业谱', '51-100 人;31 年',
    ('奥 VAD 领先+三驾具名+当季扩张窗=黄金时机', '德奥双区谱面分化', '自家产线=OEM 对照谱', 'MikroTik 官方链+多牌链'),
    '**2026-09 当季扩产/德国扩张窗(跟进节奏提频)**；具名 3 位直发需 opt-in', 'Sehr geehrter Herr Hofer-Perner,',
    trend='2026-10-08 R66 24 波谱名牌(三驾金谱+2026-09 扩张窗)'))

R.append(rec('A-470', 'evoNET',
    'evoNET GmbH(奥地利 Landeck(Tirol),Bruggfeldstraße 5;**MikroTik Reseller(名录信号);官网自宣 offizieller österreichischer Distributor(奥官方分销);WISP 专谱;Hotwave 热点牌+Etron 收银+监控谱**;+43 5442 20400;info@evonet.at;1-10 人;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'evonet.at;Landeck;+43 5442 20400;奥官方分销官网自宣;WISP 专谱', 'https://www.evonet.at/it-loesungen/hard-software/mikrotik/'),
     ev('业务定位', 'Hotwave 热点+Etron 收银+监控谱;1-10 人小户', 'https://www.evonet.at/')],
    '奥地利 WISP/酒店热点谱', '1-10 人',
    ('奥官方分销自宣=链窗', '小户薄谱', 'WISP 专谱对口', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Sehr geehrtes evoNET Team,'))

# ============ 段八:希腊 6 连(A-471~476) ============
R.append(rec('A-471', 'Automation Experts',
    'Automation Experts(希腊 Athens(2 Eftichias, 14451 Metamorfosi)+Thessaloniki(Thermi)双点;**分销(Antaira 授权);官网 News:2026-01 新签 Antaira(Industial EtherNet Switches/PoE 方案/媒体转换器)希腊+塞浦路斯分销=当季新牌窗(我方 288GP 工业 PoE 正中!);HMS/Anybus/IXXAT/Red Lion/N-Tron/MBConnect/Wachendorff(2025-05 新签)/Invertek Drives/IDEC/CMZ/Proface/atvise SCADA/acron/JUNE5 全工业授权谱;Red Lion 官方分销页+antaira.eu where-to-buy+atvise 伙伴页三源金档;Lantech EN50155 车载铁路认证谱=民用交通限定注**;+30 210 28 15 988;info@automationexperts.gr;具名决策人谱面未锁→守档准由(波次二走 Antaira 交接联络挖);**p1=STI-288GP 供位谱;与 A-450 AXTEK(匈牙利 Antaira)/A-453 Controsys/A-478 ATEG 同牌谱链互注**)',
    [],
    [ev('近期动态与线索', '官网 News:January 2026 - New partnership with Antaira(Industrial EtherNet Switches, PoE Solutions, Media Converters)for Greece & Cyprus=当季新牌窗', 'https://www.automationexperts.gr/index-en.htm'),
     ev('联系方式与基础画像', 'automationexperts.gr;Athens+Thessaloniki;+30 210 28 15 988;HMS/Anybus/Red Lion/N-Tron 全工业谱', 'https://antaira.eu/antaira-where-to-buy,81')],
    '希腊工业自动化 SCADA/PLC 分销谱;**铁路车载 EN50155 谱民用交通限定注**', '分销中户谱',
    ('Antaira 2026-01 新牌窗=当季蜜月;全工业授权金档', '具名缺', '希+塞双国谱', '工业链'),
    '**EN50155 民用交通限定注**；具名缺(守档准由,波次二 Antaira 交接联络挖)；同牌链互注(A-450/453/478)', 'Dear Automation Experts Team,',
    trend='2026-10-08 R66 24 波谱名牌(Antaira 2026-01 新牌窗;p1=STI-288GP)'))

R.append(rec('A-472', 'CABLEWORKS',
    'CABLEWORKS(希腊 Athens;**MikroTik Reseller(名录信号);FB 自宣 Ubiquiti-Mikrotik-TP-Link-Interline-Hikvision-Dahua-Sigma Security 牌谱;€价全明零售店谱;Noyafa 工具/MINISFORUM 迷你机谱**;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'cableworks.gr;Athens;MT/Ubiquiti/TP-Link/Interline/Hikvision/Dahua 牌谱', 'https://www.cableworks.gr/diktyaka/mikrotik/rbsxt/'),
     ev('业务定位', '零售店谱(网络+监控+工具)', 'https://www.facebook.com/cableworks.gr/')],
    '希腊零售/监控装维谱', '小铺谱',
    ('牌谱齐=对口窗', '零售身段', 'Interline 天线专业谱', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Dear CABLEWORKS Team,'))

R.append(rec('A-473', 'E-WIRELESS',
    'E-WIRELESS(希腊;**MikroTik Master(名录信号);自宣「Ελληνική Αντιπροσωπίας Ubiquiti」=Ubiquiti 希腊代表谱;MikroTik L4 授权在售;全希 ELTA/ACS 快递谱**;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'e-wireless.gr;Ubiquiti 希腊代表自宣;MT L4 授权在售', 'https://www.e-wireless.gr/mikrotik-l4-licence/'),
     ev('业务定位', 'MT+UBNT 双牌专营店谱', 'https://www.e-wireless.gr/')],
    '希腊 WISP/无线专铺谱', '小中铺谱',
    ('Master 名录信号=链窗', 'UBNT 主场谱(MT 为二牌)', '全希快递谱', 'MikroTik 官方链'),
    '具名缺(守档准由)；UBNT 主场注(MT 主推力度中等)', 'Dear E-WIRELESS Team,'))

R.append(rec('A-474', 'Hellas Digital',
    'Hellas Digital(希腊;**MikroTik Master(名录信号);hellasdigital.gr 在线店:卫星上网/VoIP/光纤/Wi-Fi/KNX 楼控谱;MT 全谱+100G QSFP28/400G 高端光模块谱**;Teltonika/Peplink/Cudy/ZTE/TP-Link 牌谱;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'hellasdigital.gr;MT 全谱+100G QSFP28 高端谱;卫星/VoIP/KNX 谱', 'https://www.hellasdigital.gr/'),
     ev('业务定位', '在线店全谱(高端光模块到入门板)', 'https://www.hellasdigital.gr/mikrotik/?page=25')],
    '希腊在线店+KNX 楼控谱', '小中店谱',
    ('Master 名录+高端光模块谱=深窗', '具名缺', 'KNX 楼控差异化谱', 'MikroTik 官方链'),
    '具名缺(守档准由)', 'Dear Hellas Digital Team,'))

R.append(rec('A-475', 'XPATIT S.A.',
    'XPATIT S.A.(希腊 Nea Makri/Rafina(Attica),26th km Marathonos Av.;**MikroTik Master+VAD(名录信号);官网自宣「επίσημος διανομέας(distributor)software και Hardware της Mikrotik στην Ελλάδα」=MT 希腊官方分销官网金句;2016 起官方认证培训中心(MTCNA/MTCRE/MTCWE/MTCTCE/MTCUME/MTCIPv6E/MTCINE/MTCSE/MTCSWE/MTCEWE 十证全谱);2025-10 MTCNA 15 学员全员过证新闻谱**;+30 211 8000 313;info@xpatit.gr;11-50 人;$<5M;**讲师 Athanasios Pournaras=创始成员+MikroTik/Ubiquiti/TP-Link 三牌认证讲师(2016/2018/2023)=与 A-356(波 21 人名档)同人镜像错峰注:A-356 已发谱位,A-475 公司体档,首触错峰走 A-356 位主发(本人);公司采购口二发**;Ubiquiti/Teltonika/RF-elements/Ignitenet/Ruckus 牌谱)',
    [('Athanasios Pournaras', 'MikroTik 认证讲师(2016)+创始成员(官网培训版自署;与 A-356 同人)', 'xpatit.gr 培训版', O, 'https://www.xpatit.gr/en/trainings-services/official-trainings-mikrotik')],
    [ev('决策链与对接人', '官网培训版:Athanasios Pournaras 创始成员,MT Certified Trainer 2016+UCT 2018+Omada OCI 2023;十证全谱培训', 'https://www.xpatit.gr/en/trainings-services/official-trainings-mikrotik'),
     ev('联系方式与基础画像', 'xpatit.gr;Rafina;+30 211 8000 313;MT 希腊官方分销自宣金句;Master+VAD 名录信号', 'https://www.xpatit.gr/el/sinergates/mikrotik')],
    '希腊 MT 官方分销+培训谱', '11-50 人',
    ('官方分销自宣金句+三牌讲师具名=金档链窗', '同人镜像错峰', '十证培训全谱', 'MikroTik 官方链+培训链'),
    '**A-356 同人镜像错峰注(走 A-356 位主发,公司口错峰二发)**；具名直发需 opt-in', 'Dear Mr. Pournaras,',
    trend='2026-10-08 R66 24 波谱名牌(官方分销金句+A-356 镜像注)'))

R.append(rec('A-476', 'wirelesslan.gr（Teledata e.e.）',
    'wirelesslan.gr(Teledata e.e.;希腊;**MikroTik Reseller(名录信号);店谱 Ubiquiti 62/TP-Link 142/MikroTik 47/Teltonika 12/RF Elements 9/Cambium/Mimosa SKU 谱;无线微波专营(Microwaves wlan)**;具名决策人谱面未锁→守档准由)',
    [],
    [ev('联系方式与基础画像', 'wirelesslan.gr;Teledata e.e.;无线微波专谱;MT 47 SKU', 'https://wirelesslan.gr/'),
     ev('业务定位', 'UBNT/TP-Link/MT 多牌专营店', 'https://wirelesslan.gr/shop/')],
    '希腊无线专营铺谱', '小铺谱',
    ('微波专营=对口窗', 'TP-Link 为主牌谱', 'RF Elements 天线谱', 'MikroTik 官方链'),
    '具名缺(守档准由)；TP-Link 主场注(MT 主推力度中等)', 'Dear wirelesslan Team,'))

# ============ 段九:德国 2(A-477~478) ============
R.append(rec('A-477', '4Networks IT-Distribution（OMG.de）',
    '4Networks IT-Distribution(emsnet GmbH 品牌;德国 Aurich(Ostfriesland),Kornkamp 40;**MikroTik Master+VAD(名录信号);官网自宣 authorized MikroTik distributor(德授权分销);HRB 100364;UID DE194342953;ISP/WISP/酒店/培训/工业客谱;400G/数据心高端谱**;0421 244 019 0;info@4networks.de;**CEO Thilko Cullmann(官网团队版自署 O)+Head of Sales Bernd Eisenhauer+Sales Engineer Jamal Mehdi+Sales Manager Andreas Galke 全梯队具名谱**)',
    [('Thilko Cullmann', 'CEO(官网团队版自署+Impressum 双源)', '4networks.de 官网', O, 'https://www.4networks.de/'),
     ('Bernd Eisenhauer', 'Head of Sales(LI 谱;销售头=直对口)', 'linkedin.com 件', G, 'https://www.linkedin.com/in/bernd-eisenhauer-a446b719b/')],
    [ev('决策链与对接人', '官网团队版:CEO Thilko Cullmann+Head of Sales Bernd Eisenhauer+Jamal Mehdi+Andreas Galke 全梯队具名', 'https://www.4networks.de/'),
     ev('联系方式与基础画像', 'omg.de/4networks.de;Aurich;0421 244 019 0;HRB 100364;德授权分销自宣', 'https://www.4networks.de/en/mikrotik')],
    '德国 ISP/WISP/酒店/教育/工业全国分销谱', '分销中户谱',
    ('德授权分销自宣+CEO 具名=金档链窗', 'Aurich 远北谱(物流时效)', 'MSP/40G-400G 高端谱', 'MikroTik 官方链'),
    '具名直发需 opt-in；emsnet GmbH 法体名注(品牌↔法体)', 'Sehr geehrter Herr Cullmann,',
    trend='2026-10-08 R66 24 波谱名牌(CEO 具名金谱)'))

R.append(rec('A-478', 'ATEG Automation GmbH',
    'ATEG Automation GmbH(德国 Remscheid,Intzestraße 50,D-42859;**分销(HMS/N-Tron·Red Lion 工业渠道);HR B 11800(Wuppertal);1995 创 30 年;2-10 人;Geschäftsführer Stefan Glaubitz(Impressum+LI 双源 O)+Jochen Zimmermann FAE/PM+Carina Sigismund/Frohberg 订单处理+Emel Harman 订单具名梯队;SELA 风电驱鸟自有牌谱;Optris 红外测温合作 2026-03 杜塞 all about automation 联展新闻谱**;+49 2191 591457-0;info@ateg.de;**p1=STI-288GP 供位谱;与 A-453 Controsys(匈牙利)/A-471 Automation Experts(希腊)同牌谱链互注(HMS/Red Lion/N-Tron)**)',
    [('Stefan Glaubitz', 'Geschäftsführer(Impressum 自署+LI/RrocketReach 多源)', 'ateg.de Impressum', O, 'https://www.ateg.de/impressum/'),
     ('Jochen Zimmermann', 'FAE&Projektmanagement(官网联系版自署)', 'ateg.de 联系版', O, 'https://www.ateg.de/kontakt/')],
    [ev('决策链与对接人', 'Impressum:GF Stefan Glaubitz;联系版:Jochen Zimmermann FAE&PM, Carina Sigismund/Emel Harman Auftragsabwicklung(订单处理具名)', 'https://www.ateg.de/impressum/'),
     ev('联系方式与基础画像', 'ateg.de;Remscheid;+49 2191 591457-0;HMS/Red Lion/N-Tron 分销;SELA 风电驱鸟自有牌;Optris 2026-03 联展', 'https://de.linkedin.com/company/ateg-automation')],
    '德国工业自动化/风电能源网建谱', '2-10 人小户',
    ('GF 具名+工业 HMSS 谱链=金窗', '小户谱(量有限)', '风电 SELA 差异化谱', '工业链'),
    '**工业守界常规注(民用商用工业限定)**；具名直发需 opt-in；同牌链互注(A-453/471)', 'Sehr geehrter Herr Glaubitz,',
    trend='2026-10-08 R66 24 波谱名牌(GF 具名;p1=STI-288GP 供位)'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第24波50户.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 24 波 50 户扩招批:A-429~A-478 顺延 50 户(MikroTik 官方链分销档 45+集成/顾问人名档 5;乌克兰官方分销 9 连/土耳其 9/希腊 6/匈牙利 5/北马其顿 2/塞尔维亚 2/奥地利 3/德国 2/加拿大 4/以色列 1/保加利亚 2/荷兰 2/克罗地亚 1 欧洲全域面拓)',
               'scope': 'UA9+TR9+GR6+HU5+MK2+RS2+AT3+DE2+CA5(公司4+人名1+顾问1混3)+IL1+BG2+NL2+HR1;守档 30(具名缺);民用限定守界 10(UA9 民用商业限定前句+A-440 安防加厚);政府/医疗守界 3(A-446 加公部门/A-462 土医疗/A-478 工业常规);R63 退信期满注 2(A-441 dipole-ltd.com/A-457 enucuzmikrotik.com 46h 观察 2026-10-08 届满转永久,替代口在册);同人同域镜像错峰注 3(A-442↔A-367 Petar Dimitrov/A-475↔A-356 Pournaras/A-445↔波23 A-379 Optitera 同谱);金谱:Lanmarket 官网 4 销售具名/Technotrade UBO/Viatec Master 8 年安防大户/ALL4NET 官方自宣+NODENET 2026 新任/Sekuritim 土首家培训院/A-449 #TR0516 十全证讲师/TRIOTRONIK 三驾+2026-09 扩张窗/A-477 CEO Cullmann/A-478 GF Glaubitz/Automation Experts Antaira 2026-01 新牌窗;名差旗 4(A-443 Rootelsat↔RutelSat/A-450 AXTEK↔IETEK LINE/A-464 Sekuritim OÜ 双体/A-455 三域);p1=424×43+OEM×3(429/430/449)+STI-288GP×4(450/453/471/478)',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 24 波 50 户扩招批落盘:', len(R))
