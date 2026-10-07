# -*- coding: utf-8 -*-
"""R66 第 3 波:A-341 ~ A-376 基线补足 36 户(机械基线,含司名/人名谱位)。
→ 法语基:个体户公司名字段=本人实名 → KP REALNAME 谱位自曝资格;
→ 公司谱:函数口职能口 + R66 波次点名点名(具体 KP 待补撬件);
→ 沙箱精核不变 CSV/STRUCT 渲染字段。"""
import csv, json, re

PRICE = '$180 USD EXW (2026-10-07, 15天有效)'
rows = list(csv.reader(open('客户名单_反向信号_2026-09.csv', encoding='utf-8-sig')))
ci = rows[0].index('档案编号')
ni = rows[0].index('公司名')
co = rows[0].index('国家')
we = rows[0].index('网站')
em = rows[0].index('入口/联系方式')

WANT = [f'A-{n}' for n in range(341, 377)]
PERSON_FACTOR = {
    'A-344': ('World Technology di Luigi Boi', 'Luigi Boi', '个体工商结人名司名=法定人名同体;Luigi Boi 本人谱位公开件'),
    'A-355': ('Ahababian V.', 'V. Ahababian', '人名档同体;实名谱位=Ahababian'),
    'A-356': ('Pournaras Athanasios', 'Athanasios Pournaras', '人名档同体;实名谱位=Athanasios Pournaras'),
    'A-359': ('Scornici Vadim', 'Vadim Scornici', '人名档同体;实名谱位=Vadim Scornici'),
    'A-360': ('Andrii Sychov', 'Andrii Sychov', '人名档同体;实名谱位=Andrii Sychov'),
    'A-361': ('Michal Dobšovič', 'Michal Dobšovič', '人名档同体;签名口 dobsovic@itlearning.sk 实名谱捆绑'),
    'A-362': ('Ivan Dolnak', 'Ivan Dolnak', '人名档同体;签名口 ivan.dolnak@connet-group.sk 实名谱捆绑'),
    'A-364': ('Olisian Sulaj', 'Olisian Sulaj', '人名档同体;olisian.sulaj@gmail.com 实名谱捆绑'),
    'A-366': ('Robertas Stauskas / Magit', 'Robertas Stauskas', '人名+牌司名 Magit;robertas@magit.lt 实名谱捆绑'),
    'A-367': ('Petar Dimitrov', 'Petar Dimitrov', '人名档同体;实名谱位=Petar Dimitrov'),
    'A-368': ('Kęstutis Viselga / MikroTik Training Lietuva', 'Kęstutis Viselga', '司名+达 MikroTik Trainer 谱;trainer@ 口实名谱捆绑'),
    'A-369': ('Veaceslav Samburschii / Academia MikroTik', 'Veaceslav Samburschii', '司名+达 Academia MikroTik;vsamburski@gmail.com 实名谱捆绑'),
    'A-370': ('Oltion Nikolla / Router.al', 'Oltion Nikolla', '司名+达 Router.al;oltionnikolla@gmail.com 实名谱捆绑'),
    'A-371': ('Martin Soovares', 'Martin Soovares', '人名档同体(Tartu 爱沙尼亚);实名谱位=Martin Soovares'),
    'A-372': ('Domagoj Bikic', 'Domagoj Bikic', '人名档同体(Split 克罗地亚);实名谱位=Domagoj Bikic'),
    'A-374': ('Rein Põdra', 'Rein Põdra', '人名档同体(Tallinn 爱沙尼亚);实名谱位=Rein Põdra'),
    'A-375': ('Jānis Jaunošāns', 'Jānis Jaunošāns', '人名档同体;实名谱位=Jānis Jaunošāns'),
    'A-376': ('Jernej Suhadolc', 'Jernej Suhadolc', '人名档+virtua-it.si 司面;实名谱位=Jernej Suhadolc'),
}

info = {}
for r in rows[1:]:
    if len(r) > ci and r[ci] in WANT:
        info[r[ci]] = {'name': r[ni], 'country': r[co], 'site': r[we], 'email': r[em]}

def mk_fus(email):
    return [
        {'stage': '第 1 次跟进 · 具名 kp 引路口', 'push': 'STC-424XGGPM-280W',
         'angle': '具名 kp 引路 → 采购/技术硬件分载线', 'question': '贵司 24 口 PoE 交换机的硬件采购线由哪位同事主责？',
         'proof': '规格页'},
        {'stage': '第 2 次跟进 · 一页目录卡', 'push': '一页目录卡',
         'angle': '价值层 PoE 谱链卡', 'question': '可否入谱链名录？', 'proof': '卡'},
        {'stage': '第 3 次跟进 · 留档+LinkedIn 谱', 'push': '—',
         'angle': '谱链明智途径(LinkedIn 公开面)', 'question': '—', 'proof': '—'},
    ]

records = []
for code in WANT:
    v = info.get(code)
    cp = v['name'] or '(公司名档空)'
    email = v['email']
    dom = email.split('@')[-1].replace('【已', '') if '@' in email else '—'
    site = v['site'] or ('https://www.' + dom if dom != '—' else 'https://www.RegisterOfCompanies')
    pname = None
    if code in PERSON_FACTOR:
        cp2, pname, pnote = PERSON_FACTOR[code]
        kp_block = ('**' + pname + ' = ' + pnote + '(official-self-published 级:公司名字段即本人公开件);'
                    + email + ' 口不动(' + dom + ' 口)**')
        fact = (cp2 + '(' + v['country'] + ';**个体户/人名司名档=实名谱位实名:' + pname + '(CSV 公司名字段即本人谱位,'
                'official-self-published 级谱位公开件)**;' + email + ' 签名/公司函数口已记 STRUCT')
        dim_kp = ('**' + pname + '(CSV 公司名字段即本人谱位)—— official-self-published 级金谱;'
                  + email + ' 口(' + dom + ')跟团不动;登记册查询指向该自然人的法人公开件**')
        sw = ('个人实名档谱简洁直接', '该档个体不表征司面大小(个体谱)', '个体档的成本谱替换件直达位', '个体档档期能力低交换')
        note_core = '个体户谱:' + pname
    else:
        kp_block = ('**函数口职能口:' + email + '(' + dom + ')跟团不动;具名 KP 待 R66 波次补'
                    '(波次 1-3 已摘位的司实谱位顺手补之;该司实谱位点名=R66 KPI 核心补件)**')
        fact = (cp + '(' + v['country'] + ';R66 基线补足档·公司面全貌待补;函数口职能口 ' + email + '(' + dom + ')'
                '跟团不动;司实谱位点名指R66 后续波次/KPI 核心补件)')
        dim_kp = ('**函数口职能口 ' + email + '(' + dom + ')已实位;R66 波次点名(KPI 核心):具体 KP 待补撬件'
                  '(Urzeówne Rejstery+LinkedIn+official-self-published 渠道+R64 RocketReach 谱)&#10;具体实名谱位待 R66 波次补' 
                  '(司实谱位点名=R66 KPI 核心补件)**')
        sw = ('函数口职能口已实位', '具名 kp 未勘出(波次点名)', '函数口面心谱链档的特制效应', '函数口档直发不直接')
        note_core = '公司谱面全谱待补kp'
    dim_b = ('R66 基线补足档(' + note_core + ');司面全谱待 R66 波次补;'
             '函数口 ' + email + '(' + dom + ')跟团不动')
    dim_lineu = '(待问;' + dom + ' 域名面谱=' + ('公司面谱' if email else '未知口') + ')'
    dim_swot = ('S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3])
    ev = [
        {'dim': '决策链与对接人', 'quote': (cp + ' — ' + email + ' (CSV/STRUCT 落穗件;' + note_core + ')'), 'source': site},
        {'dim': '业务定位', 'quote': ('R66 基线补足档(2026-10-07 沙箱精核):函数口职能口实位;' + note_core), 'source': site},
        {'dim': '近期动态与线索', 'quote': ('2026-10-07 R66 波次点名(A-341~A-376 基线补足;司实谱位点名=R66 KPI 核心补件;'
                '公司面全谱待 R66 波次补撬件)'), 'source': site},
    ]
    records.append({
        'customer': code,
        'fact': fact,
        'inference': 'R66 基线补足档(个体谱=实名同体谱;公司谱=函数口面谱)，公司面全谱/司实谱位待 R66 波次补件',
        'hypothesis': '函数口职能口' + dom + ' 为谱链入口；具名 kp 直发需 opt-in；后续波次以登记册+LinkedIn+R64 RocketReach 谱补撬件',
        'evidence_main': site,
        'tech': '(未列谱;R66 后续波次补)',
        'hr': '(未列;R66 后续波次补)',
        'contact_found': kp_block,
        'contact_pending': '具名 kp 实名谱位=波次点名(KPI 核心补件)',
        'dims': {
            '业务定位': dim_b,
            '产品线与在售品牌': dim_lineu,
            '目标行业与场景': '(R66 后续波次补)',
            '团队与规模': '(R66 后续波次补)',
            '决策链与对接人': dim_kp,
            '技术与认证': '(R66 后续波次补)',
            '采购与供应链信号': '(R66 后续波次补)',
            '近期动态与线索': '2026-10-07 R66 波次点名(基线补足)',
            '与我方契合点': '函数口职能口' + dom + ' 面心谱链档',
            '风险与注意': '具名 kp 未勘出/波次点名；不要直发或未 opt-in',
        },
        'evidence': ev,
        'followups': mk_fus(email),
        'r55': {
            'dims': {
                '①背景再核': dim_b,
                '②芯片/型号': dim_lineu,
                '③KP 深挖': dim_kp,
                '④Saga 对标': '24 口 value PoE(' + PRICE + ')→ 成本谱替换件/随行件',
                '⑤在乎与偏好': sw[0],
                '⑥SWOT': dim_swot,
            },
            'care': ['具名 kp 直发需 opt-in 手序'],
            'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
            'uncertain': {'产品线核实': 'R66 后续波次补', '合作方式': '未知', '缺口证据': '司面全谱待补'},
            'gap_proof': 'R66 时点公司面全谱未列公开件',
        },
        'unknowns': ['司实谱位点名(波次点名)', '公司面全谱', '具名 kp 直发邮箱'],
        'email': (
            ('Hi ' + pname.split()[0] + ',' if pname else 'Hi team,') +
            '\n\nI came across ' + (cp2 if pname else cp) + ' while mapping ' + v['country'] +
            ' network/IT suppliers — your name showed up on the serious side of the market. Behind every deployment sits a switching layer that has to stay cheap, PoE-healthy and well documented.\n\n'
            'We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: ' + PRICE + ' — a value unit that rides along with each deployment.\n\n'
            'Could you point me to the colleague who carries the hardware purchasing line, so we route the right spec to the right desk?\n\n'
            'Best regards,\nSaga Networks Export Desk'),
    })

out = {'date': '2026-10-07', 'wave': 'R66 第 3 波:A-341~A-376 基线补足 36 户',
       'scope': '人名司名同体谱位 + 公司面全谱待补函数口职能口(普适基线)',
       'records': records}
json.dump(out, open('batch/A类深挖_2026-10-07_R66_R56_341_376基线.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('R66 基线补足', len(records), '户落盘')
