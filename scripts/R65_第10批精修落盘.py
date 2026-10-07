# -*- coding: utf-8 -*-
"""R65 B 类深挖第 10 批:希腊 7 户收尾。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 10 批精修 = R57 转写 + 本轮调研新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-115',
    head='ALLNET.Greece / Allnet Greece 分支(R57 已述;ALLNET 世界集团 Bauer 家长径在同科——德国母体 B-138 Bauer/意大利 B-154 €88M 距并;',
    kpn='—(谱与 B-138 W.M. Bauer 联动径)',
    facts=[{'dim': 'R65 联动', 'text': 'ALLNET 集团全球分支;谱与 B-138/B-154  Bauer 同联径；希腊站内坑',
            'quote': '(R65 联动口径:ALLNET 集团家长 Wolfgang Marcus Bauer 1991 创立,99 员工国际)',
            'url': 'https://www.wer-zu-wem.de/firma/allment-computer.html'}],
    fihadd='ALLNET 集团联动径宣称')

put('B-119',
    head='Allen.Gre此举谱(B-119;R65 搜索无果,守档准由)',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果;守档准由', 'quote':'(web_search 无果)', 'url': '(沙箱日志)'}])

put('B-123',
    head='OZEOkueng / Glowe Pefki(希腊 Rah 罗地;R65 检索无果守档准由)',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果;守档准由', 'quote': '(web_search 无果)', 'url': '(沙箱日志)'}])

put('B-126',
    head='Alfa-Tech (2 实体同卵：已并 B-127 档写 Analytis 登记；B-126 偏米科诺斯/爱琴海小壮；R65 均不合格守档准由)',
    facts=[{'dim': 'R65 联动', 'text': 'B-126/B-127 两 Alfa-Tech 同名系应视为并集；Analytis KP 挂 B-127，均守档', 'quote':'(R65 同域联动口径)', 'url': '(沙箱谱位核验日志)'}],
    fihadd='B-127 联动 Analytis 谱;两站均守档')

put('B-128',
    head='Planet1.gr / Planet1 SA 或 SA Planet 1 同名档（希腊小谱；R65 检索无果守档准由)',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果)', 'url': '(沙箱日志)'}])

put('B-132',
    head='Cybertek.gr / Cybertek S.A.（希腊雅典 Bouton 轴大谱)——守望准由',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果)', 'url': '(沙箱日志)'}])

put('B-134',
    head='Phoenix Fone S.A.（希腊包；R65 检索无果守档准由)',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果)', 'url': '(沙箱日志)'}])

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 10 批（希腊收尾 7 户）',
       'scope': 'B-115 / B-119 / B-123 / B-126 / B-128 / B-132 / B-134',
       'records': [by[c] for c in ('B-115', 'B-119', 'B-123', 'B-126', 'B-128', 'B-132', 'B-134')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第10批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 10 批 7 户落盘')
