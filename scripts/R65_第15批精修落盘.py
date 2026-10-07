# -*- coding: utf-8 -*-
"""R65 B 类深挖第 15 批:美国 10 户收尾。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 15 批精修 = R57 转写 + 本轮调研新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-366',
    head='Pace International(1972 年创立,Rochester, Minnesota;'
         '**Richard Siegel = Founder & CEO**;Brent Afseth = VP of Channel Partners;Sam Schell = SVP Business Development;Jeremy Nelson = E-Commerce Director;'
         '2025-26 Tim + Eric Deutsch 三代接棒列股东；谱型=video/data 解决方案 50+ 年批发名堂；官网「Brands we stock and stand behind:MikroTik」自曝',
    kpn='Richard Siegel = Founder & CEO(1972 创）;Brent Afseth VP Channel Partners;Tim/Eric Deutsch 三代股东',
    kp=[{'name': 'Richard Siegel', 'role': 'Founder & CEO', 'contact': '经 paceintl.com', 'status': 'LinkedIn pace-electronics 官方页自曝', 'source': 'https://www.linkedin.com/company/pace-electronics'},
        {'name': 'Brent Afseth', 'role': 'VP of Channel Partners', 'contact': '同上', 'status': '同上', 'source': '同上'}],
    facts=[{'dim': 'R65 谱/实名', 'text': 'Pace International 1972 创立 Rochester MN 50+ 年批发名称；Richard Siegel 创始 CEO；MikroTik stocked 自曝',
            'quote': 'Pace International is a distribution company of video and data solutions … Founded in 1972 … Richard Siegel Founder & CEO … Brands we stock and stand behind: MikroTik',
            'url': 'https://paceintl.com/'}],
    fihadd='美 1972 三代谱；Deutsch 三代 2025 接棒')

put('B-375',
    head='RUGGED SCIENCE(60 Loveton Circle, Sparks Glencoe, MD 21152;2014 国防工业武功人创立；'
         '**Jack Vogt = CEO;Drew Vogt = COO;Rob Schubel = Marketing Director**(PR.com 2025-02 新闻稿三源） ',
    kpn='Jack Vogt = CEO;Drew Vogt = COO;Rob Schubel = Marketing Director',
    kp=[{'name': 'Jack Vogt', 'role': 'CEO', 'contact': '经 ruggedscience.com / Rob Schubel 443-595-8384', 'status': 'theorg + PR.com 双源', 'source': 'https://www.pr.com/press-release/930487'},
        {'name': 'Drew Vogt', 'role': 'COO', 'contact': '同上', 'status': '同上', 'source': '同上'}],
    facts=[{'dim': 'R65 谱位/实名', 'text': 'Rugged Science 2014 创 Sparks MD；以军用/工业/Edge AI 高耐用计算》名；33,234 SF 新 HQ;Vogt 家谱系',
            'quote': 'Rugged Science, founded by Defense industry veterans, designs, engineers, and manufactures high-performance computing solutions in Sparks, MD, USA … Jack Vogt, CEO … Drew Vogt, COO … Rob Schubel, Marketing Director … 33,234 SF headquarters',
            'url': 'https://www.pr.com/press-release/930487'}],
    fihadd='军工/Edge AI 美北谱；Vogt 两号位家族谱')

put('B-233',
    head='Tech Atlantix(Sugar Land, Greater Houston, Texas;谱型=Texas 在线 marketplace主营 CPU/显卡/主板/networking 硬件电商；'
         '**Mike Ross = CEO;Ethan Klein = EVP(2025-12 新加，R65 新增动态）；Jake West Director Operations(2025-11);Jorge Hernandez Ops&Procurement(2025-09);Kevin Foster(2025-08)**——2025 下半年小乱动态大量招雇佣，企业扩张连通性走开通口',
    kpn='Mike Ross = CEO;Ethan Klein = EVP(2025-12 新任，谱口）',
    kp=[{'name': 'Mike Ross', 'role': 'Chief Executive Officer', 'contact': '经 techatlantix.com', 'status': 'zoominfo 自曝', 'source': 'https://www.zoominfo.com/c/tech-atlantix/1340571212'},
        {'name': 'Ethan Klein', 'role': 'Executive Vice President(2025-12 新聘）', 'contact': '同上', 'status': '同上', 'source': '同上'}],
    facts=[{'dim': 'R65 实名+扩影响', 'text': 'Tech Atlantix Sugar Land TX CPU/网络电商；Mike Ross CEO;Ethan Klein EVP 2025-12；三聘营运动态=抢入档口',
            'quote': 'Tech Atlantix\'s CEO is Mike Ross … Ethan Klein Executive Vice President Joined Dec 1, 2025 … Jake West Director, Operations Joined Nov 25, 2025',
            'url': 'https://www.zoominfo.com/c/tech-atlantix/1340571212'}],
    fihadd='Sugar Land 电商新谱；2025 年扩大专长位谱口利')

put('B-329',
    head='BIBAOnline / BIBA LLC(Centerville, Virginia;2009-07 创；'
         '谱型=美国 VAR/VoIP/IT 三合一——IP phone/PBX/SSD/HDD/KVM/VoIP 等营销+电缆/布线/病毒清/网络工程服务连售；家庭/中小企业 audience',
    kpn='—(BIBA LLC 业主方未自曝；R65 谱位足档）',
    facts=[{'dim': 'R65 谱位', 'text': 'BIBAOnline=BIBA LLC 旗下 VAR/VoIP/IT 在 Centerville VA 2009-07 创；SKU 范吻合',
            'quote': '@bibaonline your one stop shop for VAR, VoIP products, tech gadgets and software. A division of BIBA LLC … Centerville, VA bibaonline.com … BIBA Online provides … SSDs, HDDs, USB Flash Drives, KVM switches, VoIP Products … networking',
            'url': 'https://x.com/bibaonline'}],
    fihadd='BIBA VAR/VoIP 一条龙谱 2009')

put('B-327',
    head='Andrei Zhernosek（美国个体谱；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由')

put('B-338',
    head='Christopher Schiessl（美国个体谱；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote': '(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由')

put('B-343',
    head='Distrigo Inc（美国车配/谱者主体；R65 搜索缺谱走=守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由')

put('B-359',
    head='Leverify LLC（美国个体谱；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由')

put('B-377',
    head='Ray Evelyn（美国个体谱；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由')

put('B-508',
    head='NCTIK（美国个体谱；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote': '(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 15 批（美国 10 户收尾）',
       'scope': 'B-366 Pace / B-375 Rugged Science / B-233 Tech Atlantix / B-329 BIBAOnline / B-327 / B-338 / B-343 / B-359 / B-377 / B-508',
       'records': [by[c] for c in ('B-366', 'B-375', 'B-233', 'B-329', 'B-327', 'B-338', 'B-343', 'B-359', 'B-377', 'B-508')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第15批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 15 批 10 户落盘')
