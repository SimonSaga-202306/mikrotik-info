#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R65:把 profile/B 全部 167 户的 R57「备护深挖」节机械转写为 R56 结构深挖 JSON,
并生成 batch/structured_profiles_v1.json 中缺失的 B 类 STRUCT 条目。

纪律:
- 只读旧档、只写 batch JSON(不直改 profile;profile 升级经 B类_v2渲染.py)
- 事实/推断/假设/SWOT/证据/备养信 一律忠实原 R57 原文转写,不加工不脑补
- 数据源 = 2026-09-29 R57-BC 备护深挖;补入 R64 KP 猎捕战果(KP 表)
"""
import csv, io, json, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

CSV = os.path.join(ROOT, '客户名单_反向信号_2026-09.csv')
STRUCT_P = os.path.join(ROOT, 'batch/structured_profiles_v1.json')
KP_B_P = os.path.join(ROOT, 'batch/KP猎捕_B_R64_第1批.json')
OUT_P = os.path.join(ROOT, 'batch/B类深挖_2026-10-07_R65_R57转写.json')

TODAY = '2026-10-07'
VALID_P1 = {'STC-424XGGPM-280W', 'STC-28DGGPM', 'STI-288GP', 'STI-480XGGM', 'STI-280GE', 'CONSULT-OEM'}


def load_csv():
    with io.open(CSV, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    return {r['档案编号']: r for r in rows if r['评级'] == 'B'}


def sec(text, start_pat, end_pats):
    m = re.search(start_pat, text)
    if not m:
        return ''
    s = m.start()
    e = len(text)
    for pat in end_pats:
        m2 = re.search(pat, text[m.end():])
        if m2:
            e = min(e, m.end() + m2.start())
    return text[s:e]


def bullets(block, pat):
    return re.findall(pat, block)


def parse_r57(code, txt):
    blk = sec(txt, r'## 备护深挖', [r'\n<!-- BDEEP:', r'\n## 七、', r'\n## 2026-'])
    if not blk or '深挖三层' not in blk:
        return None
    def one(label):
        m = re.search(r'【%s】(.+?)(?=\n- 【|\n\n|\n\*\*)' % label, blk, re.S)
        return ' '.join(m.group(1).split()) if m else ''
    fact, inf, hyp = one('事实'), one('推断'), one('假设')
    swot = {}
    for k in 'SWOT':
        m = re.search(r'\*\*%s\*\*:\s*(.+)' % k, blk)
        swot[k] = m.group(1).strip() if m else '—'
    facts = []
    ev_sec = sec(blk, r'\*\*证据（quote → 来源）\*\*', [r'\n\*\*判位备档'])
    for q, u in re.findall(r'[「"](.+?)[」"]\s*—\s*(\S+)', ev_sec):
        facts.append({'dim': 'R57备护深挖证据', 'text': q[:140], 'quote': q, 'url': u})
    p1_m = re.search(r'参考 P1:\s*`([A-Z0-9-]+)`\s*—\s*(.+)', blk)
    p1 = p1_m.group(1) if p1_m else 'CONSULT-OEM'
    p1 = p1 if p1 in VALID_P1 else 'STC-424XGGPM-280W'
    p1_reason = p1_m.group(2).strip() if p1_m else '判位备档默认'
    q_m = re.search(r'第一问:\s*(.+)', blk)
    first_q = ' '.join(q_m.group(1).split()) if q_m else ''
    tag_m = re.search(r'标签:\s*(.+)', blk)
    tags = tag_m.group(1).strip() if tag_m else ''
    mail_m = re.search(r'\*\*备养出信稿（未触发，供后续用户启用参考）\*\*\s*```text\n(.*?)\n```', blk, re.S)
    email = mail_m.group(1) if mail_m else None
    unks = re.findall(r'^\d+\.\s*(.+?)\s*$', sec(blk, r'\*\*待补证清单\*\*', [r'\n\*\*判位', r'\n\*\*备养', r'\n\*\*跟进']), re.M)
    fu = re.findall(r'^-\s*(D\+\d+)\s*(.+?)\s*$', sec(blk, r'\*\*跟进建议（守档节奏）\*\*', [r'\n<!--', r'\n## ', r'\Z']), re.M)
    return dict(fact=fact, inference=inf, hypothesis=hyp, swot=swot, facts=facts,
                p1=p1, p1_reason=p1_reason, first_q=first_q, tags=tags,
                email=email, unknowns=unks, pace=fu)


KWS = {
    'industrial': ('工业', 'DIN', '宽温', '机柜', '户外', '-40'),
    'tenG': ('10G', '万兆', '骨干', '机房', '数据中心', 'SFP+'),
    'l2plus': ('管理型', 'L2', 'VLAN', '网管', 'ERPS'),
    'voice': ('VoIP', '语音', 'IP 电话'),
    'oem': ('OEM', '白牌', '贴牌'),
    'hotel': ('酒店', '多住户'),
    'training': ('培训', '教具', '教学', '认证顾问', 'MTC'),
}


def needs_of(blob):
    n = {k: False for k in ('poe', 'industrial', 'tenG', 'l2plus', 'voice', 'oem', 'hotel', 'training', 'subscription')}
    n['poe'] = True
    for k, vs in KWS.items():
        if any(v in blob for v in vs):
            n[k] = True
    return n


def main():
    rows = load_csv()
    struct = json.load(open(STRUCT_P, encoding='utf-8'))
    kpb = {}
    if os.path.exists(KP_B_P):
        for r in json.load(open(KP_B_P, encoding='utf-8'))['records']:
            kpb[r['code']] = r

    records, added, skipped = [], 0, []
    for code, row in sorted(rows.items(), key=lambda kv: int(kv[0].split('-')[1])):
        fns = glob.glob(os.path.join(ROOT, 'profile/B', code + '-*.md'))
        if not fns:
            skipped.append((code, '无 profile 档')); continue
        txt = open(fns[0], encoding='utf-8').read()
        p = parse_r57(code, txt)
        if p is None:
            skipped.append((code, 'R57 节缺失/结构不符')); continue

        # 人名户(person / company 形)
        person_disp = row['公司名'].split(' / ', 1)[0] if ' / ' in row['公司名'] else None

        # KP:R64 猎捕战果 persons 优先,本人户兜底
        kp = []
        br = kpb.get(code)
        if br:
            for person in br.get('persons', []):
                contact = '—'
                if person.get('email_candidates'):
                    contact = list(person['email_candidates'].values())[0]
                kp.append({'name': person['name'], 'role': person['role'][:60],
                           'contact': contact,
                           'status': person.get('email_state', '—')[:40],
                           'source': person.get('source', 'R64 第 2 波')[:80]})
        elif person_disp:
            kp.append({'name': person_disp, 'role': '本人=业主/顾问(名录口径)', 'contact': '—',
                       'status': '名录具名', 'source': '客户名单_反向信号_2026-09.csv'})

        blob = ' '.join([row['类型'], row['信号（在卖什么品牌）'], p['fact'], p['inference'], p['hypothesis'],
                         ' '.join(p['swot'].values()), p['p1_reason']])
        is_person = bool(person_disp)
        biz_org = ('个体顾问（有公司域）' if is_person else
                   ('分销/批发商（有官网）' if '分销' in row['类型'] else '公司/工作室（有官网）'))
        biz_model = ('咨询/项目交付' if ('顾问' in row['类型'] or is_person) else
                     ('分销 stocking' if '分销' in row['类型'] else '工程/项目集成'))
        if '培训' in blob and 'certified trainer' in row['信号（在卖什么品牌）'].lower():
            biz_model = '培训交付'
        n = needs_of(blob)
        vp = 5 if ('集团' in blob or '巨头' in blob) else (4 if '分销' in row['类型'] else (2 if is_person else 3))

        dims = {
            '背景深描': p['fact'][:300] or (row['类型'] + '；' + row['切入点'] if row.get('切入点') else row['类型']),
            '芯片与在用型号': ('【推断】' + p['inference'][:200]) if p['inference'] else '（R57 未涉谱，待人工深挖批）',
            '关键人KP': (p['tags'] and ('具名线索：' + p['tags'][:120]) or (person_disp or '—')) if False else ('（见 R64 KP 猎捕节/本档 KP 表）' if kp else '—'),
            '关注点与资质': ' '.join(x for x in [row['信号（在卖什么品牌）'][:120], '| 传承人名开口：见 KP 表' if kp else '']),
            '优缺点SWOT': ('S:%s / W:%s / O:%s / T:%s' % (p['swot']['S'], p['swot']['W'], p['swot']['O'], p['swot']['T'])),
            'Saga产品适配': p['p1_reason'][:200],
        }
        swot_text = ('- **S**:%s\n- **W**:%s\n- **O**:%s\n- **T**:%s'
                     % (p['swot']['S'], p['swot']['W'], p['swot']['O'], p['swot']['T']))

        follow = []
        if p.get('first_q'):
            for i, (d, txt2) in enumerate((p['pace'] or [])[:3]):
                follow.append({'stage': '守档 %s · %s' % (d, txt2[:60]),
                               'push': p['p1'], 'angle': p['hypothesis'][:120] or p['p1_reason'][:120],
                               'question': p['first_q'], 'proof': '随附 1 页特性对照/测试包说明'})
            if not follow:
                follow.append({'stage': '守档 D+14 · 低频开口', 'push': p['p1'],
                               'angle': p['p1_reason'][:120], 'question': p['first_q'],
                               'proof': '随附 1 页特性对照'})
        subj = 'PoE value slot for your line'
        if p['email']:
            m = re.search(r'Subject:\s*(.+)', p['email'])
            subj = m.group(1).strip() if m else subj

        rec = {
            'code': code, 'researched_on': p and '2026-09-29(R57 备护深挖转写 2026-10-07)',
            '_parser': 'R65_B类升v2转写.py',
            'fih56': {'fact': p['fact'][:400], 'inference': p['inference'][:300], 'hypothesis': p['hypothesis'][:300]},
            'dimensions': dims, 'swot_text': swot_text,
            'facts': p['facts'], 'kp': kp, 'unknowns56': p['unknowns'][:4],
            'followups': follow,
            'email': p['email'], 'email_subject': subj,
        }
        records.append(rec)

        # STRUCT 条目(A/B 平级;B 条目带 wave 注)
        if code not in struct:
            mails = re.findall(r'[\w.+-]+@[\w-]+\.[A-Za-z]{2,}', (row.get('入口/联系方式') or '') + ' ' + re.sub(r'（.*?）', '', row.get('备注') or ''))
            email = mails[0] if mails else None
            struct[code] = {
                'code': code, 'name': '', 'country': row['国家'], 'city': row['城市'],
                'rating': 'B', 'website': row['网站'] or None,
                'phone': None, 'email': email,
                'email_state': ('既有/公开' if email else '缺失'),
                'certs': [], 'biz_org': biz_org, 'business_model': biz_model,
                'needs': n,
                'price_sensitivity': 'high' if '分销' in row['类型'] or '集团' in blob else 'medium',
                'decision_speed': 'fast' if is_person else 'moderate',
                'volume_potential': vp, 'risk_flags': [], 'lang': 'en',
                'p1': p['p1'], 'p1_reason': p['p1_reason'],
                'first_question': p['first_q'] or '(待定)',
                'alternates': [], 'stage': '00-researched',
                'struct_version': 'v2', 'updated': TODAY,
                'note': ('R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档)'
                         ),
            }
            added += 1
        else:
            skipped.append((code, 'STRUCT 已存在'))
            records.pop()

    json.dump({'date': TODAY, 'wave': 'R65 B 类升 v2 · R57 备护深挖机械转写',
               'discipline': '忠实转写不脑补;P1=判位参考位;评级不动;不出信(乌克兰守界沿用)',
               'records': records}, open(OUT_P, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    json.dump(struct, open(STRUCT_P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'转写成功 {len(records)} 户;STRUCT 新增 B 条目 {added} 个;跳过 {len(skipped)} 户')
    for c, why in skipped:
        print('  SKIP', c, why)


if __name__ == '__main__':
    main()
