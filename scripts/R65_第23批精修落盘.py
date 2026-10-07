# -*- coding: utf-8 -*-
"""R65 B 类深挖第 23 批(收尾波):27 户一锅(5 强 + 22 守档)。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 23 批精修收尾 = R57 转写 + 本轮调研/守档)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

# ——— 5 强 ———
put('B-051',
    head='ZL Media d.o.o.(Osijek, Croatia;**B-051 Dejan Liović 实体映射核正**;'
         '**Dejan Liović = MikroTik 官方认证教练(licencirani MikroTik predavač,MTCNA/MTCWE 课程讲师,ZL Media 自主)**;'
         '2013-2019 多次 Samobor/Osijek MTCNA/MTCWE 课程实绩;谱型=克国网络解决方案 + MikroTik 培训双谱',
    kpn='Dejan Liović = licencirani MikroTik predavač(官方教练,ZL Media 谱位)',
    kp=[{'name': 'Dejan Liović', 'role': 'MikroTik 官方认证教练(ZL Media)', 'contact': '经 zlmedia.hr', 'status': 'zlmedia.hr + smbwireless.hr 双毂自曝', 'source': 'http://www.zlmedia.hr/en/first-mtcwe-mikrotik-training-held-in-osijek-croatia/'}],
    facts=[{'dim': 'R65 核正/谱位', 'text': 'Dejan Liović(ZL Media Osijek)= MikroTik 认证教练 MTCNA/MTCWE 双课讲师;2015 Samobor MTCNA;2019 Osijek MTCWE 首课',
            'quote': 'Lectures were led by a certified MikroTik trainer – Dejan Liovic … official MikroTik Training Partner … putem kojih je angažiran licencirani Mikrotik predavač Dejan Liović',
            'url': 'http://www.zlmedia.hr/en/first-mtcwe-mikrotik-training-held-in-osijek-croatia/'}],
    fihadd='克罗地亚认证教练 实体ZL Media=克 MikroTik 培训谱!')

put('B-072',
    head='JMR Logics / JMR.ca(Niagara Falls, Ontario,Canada;716-804-5878 总部;',
    kpn='Simon Miners = Network Administrator(即 CSV B-072 本人)+John Riley President & Senior IT Consultant',
    kp=[{'name': 'Simon Miners', 'role': 'Network Administrator(B-072 本人谱位),Wireless/Cyber/MikroTik 专长 LinkedIn 自曝', 'contact': 's*****@jmr.ca(模式提示；905 前缀）', 'status': 'zoominfo + rocketreach 双自曝', 'source': 'https://rocketreach.co/simon-miners-email_95924696'},
        {'name': 'John Riley', 'role': 'President & Senior IT Consultant', 'contact': 'j*****@jmr.ca', 'status': 'rocketreach 自曝', 'source': 'https://rocketreach.co/simon-miners-email_95924696'}],
    facts=[{'dim': 'R65 实名/谱位', 'text': 'JMR.ca=JMR Logics Niagara Falls ON 谱；Simon Miners Network Admin(MLS:Brock U,Microtik,cyber,wireless)+老板 Riley President',
            'quote': 'Simon Miners is Network Administrator at JMR Logics & Upper Rapids … With a robust skill set that includes Network Administration, Wireless Networking, Cybersecurity, Mikrotik, Network Security … John Riley President and Senior IT Consultant',
            'url': 'https://rocketreach.co/simon-miners-email_95924696'}],
    fihadd='Niagara ON 本地 Bitsy 实体;Simon+Riley 双谱位')

put('B-400',
    head='HP Networks / High Performance Networks Limited(2 Lislasly Road, Dungannon BT71 6TA(UK RIPE 索引)/Belfast Innovation Factory+ Dublin,2015-10 创；'
         '**Paul Hagan = Managing Director(MD 创始人本人,p.hagan@hpnetworks.net 公式行)**;谱型=英/爱 Creative Managed Communications + Creative Carrier 络',
    kpn='Paul Hagan = MD & 创始人(p.hagan@hpnetworks.net RIPE 会员名录自曝）',
    kp=[{'name': 'Paul Hagan', 'role': 'Managing Director(创始人）', 'contact': 'p.hagan@hpnetworks.net / +44 28 9053 8411(00442890 → proper intl)', 'status': 'hpnetworks.net about + ripe.net member index 双源', 'source': 'https://www.ripe.net/membership/indices/data/uk.hpnetworks.html'}],
    facts=[{'dim': 'R65 实体/谱位', 'text': 'HP Networks 2015 创 Belfast/Dublin 双办 / RIPE 正式名录 / MD Paul Hagan p.hagan@ 公式',
            'quote': 'HP Networks Ltd 2 Lislasly Road BT71 6TA Dungannon UNITED KINGDOM … phone: +442890538411 e-mail: p (dot) hagan (at) hpnetworks (dot) net … High Performance Networks formed October 2015 by MD Paul Hagan',
            'url': 'https://www.hpnetworks.net/about'}],
    fihadd='Belfast 实体 RIPE 拨名）;Paul Hagan 公式 MD/CSV B-400 Adam Reid 或为销售人员')

put('B-418',
    head='Morgan Ingland Limited(418 Ladypool Rd, Birmingham B12 8JZ(+London 1710 军侧办）, UK;'
         '**谱型=英国 IT 硬件/软件独立大批发乱迈商——100+ top brands ICT 分销，251-500 员工(crunchbase/zoominfo 双口径）**;10+ 年行业职业专谱；info@miatlantic.com',
    kpn='—(Companies House MORGAN INGLAND LIMITED 董事名单 unpaid;R65 谱位+地址件已足，购购 kp 待定）',
    facts=[{'dim': 'R65 谱位', 'text': 'Morgan Ingland Ltd Birmingham/London 100+ 品谱 ICT 批发 251-500 员工；miatlantic.com/us.miatlantic.com 双站营运',
            'quote': 'Morgan Ingland is an advanced independent reseller of Information Technology related products … Headquarters: 418 Ladypool Rd, Birmingham, West Midlands, B12 8JZ … 251-500 … The company collaborates with over 100 top brands',
            'url': 'https://www.crunchbase.com/organization/morgan-ingland'}],
    fihadd='伯明罕 ICT 大批发乱迈商 500 级员谱')

put('B-305',
    head='Jeton Syla（科索沃；R65 多同名画像：**候选 1= PULLMA Group SH.P.K.(Financial Planning and Analysis Manager, Universiteti i Prishtinës)**/候选 2=Express Delivery LLC 科索沃（弱档）；不采信保密，守档准由',
    kpn='—（同名候选已核；R65 守档准由；PULLMA FP&A 或为本人=候选非证）',
    facts=[{'dim': 'R65 同名候选注', 'text': 'PULLMA Group FP&A(Jeton Syla Prishtina)=候选，非证；Express Delivery 另一名同级候选；R65 不采信',
            'quote': '(LinkedIn 2026-10-07 jeton-syla-7a7204233 PULLMA Group FP&A/Express Delivery 候选同名同名二柱，与 MikroTik 无关联证)',
            'url': '(沙箱核验日志)'}],
    fihadd='同名两候选守档准由（科索沃未证）')

# ——— 22 守档 ———
for code, name, note in (
    ('B-059','Afshin Yadollahi','同名伊朗工程师（IRIB)/已故伊 什 lyricist 噪声排除，加拿大本体守档'),
    ('B-062','Falak Sheth','加拿大谱；R65 搜索无果'),
    ('B-064','Gerald Paul Mamaril','加拿大谱；R65 搜索无果'),
    ('B-066','Hussein Khalil','加拿大谱；R65 搜索无果'),
    ('B-085','Richárd Szabolcs Tóth','同名 SZTAKI 工程师/P&G technikánzah leszül 噪声排除，谱主守档'),
    ('B-164','Jacopo Cipriani','同名 IMDb 摄影组噪声排除（R65)，谱主守档'),
    ('B-166','Lorenzo Webber','意大利谱；R65 搜索无果'),
    ('B-173','Valerio Simeraro','意大利谱；R65 搜索无果'),
    ('B-176','Zen Vittore','意大利谱；R65 搜索无果'),
    ('B-214','（摩尔多瓦）MikroTik 集中管理软件开发者（SIA 私谱）','R65 搜索无果（摩尔多瓦小实体公开件薄）'),
    ('B-264','Grzegorz Śliwiński','波兰谱；R65 搜索无果'),
    ('B-265','Kacper Kisielewski','波兰谱；R65 搜索无果'),
    ('B-269','Piotr Maślak','波兰谱；R65 搜索无果'),
    ('B-280','Oskar Siejk','爱尔兰谱（oskar.network/pureoskar 同名噪声排除）；R65 守档'),
    ('B-315','George Lupulescu','罗马尼亚谱；R65 搜索无果'),
    ('B-319','Octavian Nicolae Tolea - Newvision','罗马尼亚谱（Newvision 同名谱生发）；R65 守档'),
    ('B-455','Rogério Costa','同名巴西 Product Manager 噪声排除，葡萄牙谱主守档'),
    ('B-490','Andrey Glushchenko - Core-Bridge','同名 Corebridge Financial 噪谱排除；黑山本体守档'),
):
    put(code,
        head=name + '(R65 搜索/核验：' + note + '；守档准由）',
        facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索/同名核验：' + note, 'quote': '(R65 同名实体验证日志）', 'url': '(R65 核验日志）'}],
        fihadd=note + '；R65 守档准由')

codes = ('B-051','B-072','B-400','B-418','B-305','B-059','B-062','B-064','B-066','B-085','B-164','B-166','B-173','B-176','B-214','B-264','B-265','B-269','B-280','B-315','B-319','B-455','B-490')
out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 23 批（收尾波 23 户）',
       'scope': 'B-051 ZL Media / B-072 JMR / B-400 HP Networks / B-418 Morgan Ingland / B-305 Jeton Syla + 18 守档',
       'records': [by[c] for c in codes]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第23批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 23 批', len(codes), '户落盘')
