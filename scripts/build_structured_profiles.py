# -*- coding: utf-8 -*-
"""结构化档案 v1 生成器（R56）：CSV 推断 + 批1/2 人工覆盖。
推断字段在 MD 渲染时打【推断】标签；人工覆盖源：batch/A类深挖_2026-09-28_R55_第*.json。
生成 batch/structured_profiles_v1.json 后删除本文件。"""
import csv, json, re
from pathlib import Path

ROOT = Path('/home/user/mikrotik-info')
TODAY = '2026-09-28'
rows = list(csv.reader(open(ROOT / '客户名单_反向信号_2026-09.csv', encoding='utf-8-sig')))
header, data = rows[0], rows[1:]
COL = {h: i for i, h in enumerate(header)}

def col(r, name):
    i = COL.get(name)
    return r[i].strip() if i is not None and i < len(r) else ''

# ---------- 证书解析 ----------
CERT_RE = re.compile(r'MTC[A-Z0-9]+|CCIE|MTCNA|MTCRE|MTCWE|MTCTCE|MTCINE|MTCSE|MTCSWE|MTCUME|MTCEWE|MTCIPv6E')
def parse_certs(brand):
    m = re.search(r'证书[：:]([^）\)]+)', brand or '')
    if not m: return []
    return sorted(set(CERT_RE.findall(m.group(1))))

# ---------- 类型/需求推断（全部打推断标签在渲染层） ----------
def infer(row):
    brand = col(row, '信号（在卖什么品牌）'); site = col(row, '网站'); name = col(row, '客户名称')
    b = ' '.join([brand, col(row, '备注'), col(row, '类型'), col(row, '切入点')]).lower()
    certs = parse_certs(brand)
    is_trainer = any(k in b for k in ['train', '讲师', '培训']) or 'MikroTik 认证培训' in (brand or '')
    is_college = any(k in (site or '').lower() for k in ['cegep', 'college', 'edu'])
    has_site = bool(site) and 'linkedin' not in site
    # 组织性质
    if is_college: org = '公立院校（教授个人顾问线）'
    elif has_site: org = '公司/工作室（有官网）'
    elif 'linkedin' in (site or ''): org = '个体（LinkedIn 仅存）'
    else: org = '个体顾问（无官网）'
    model = ('订阅制服务/租赁' if any(k in b for k in ['租', 'naa', 'subscription', 'month'])
             else '培训交付' if is_trainer
             else ('工程/集成项目制' if has_site else '顾问项目制'))
    needs = {
        'poe': True,  # A 类=接入层池，默认 PoE 诉求
        'industrial': any(k in b for k in ['工业', 'industrial', 'wisp', 'isp', '能源', '农业', 'grid', 'festival', '户外']),
        'tenG': any(k in b for k in ['mtcine', 'ccie', '骨干', 'isp', '10g']),
        'l2plus': any(k in b for k in ['mtcswe', '交换']) or 'MTCSWE' in certs,
        'voice': any(k in b for k in ['voip', '语音', '电话']),
        'oem': any(k in b for k in ['oem', '白牌', '贴牌', 'master distributor']),
        'hotel': any(k in b for k in ['酒店', 'hotel', 'hospitality', '餐饮', 'hospitality']),
        'training': bool(is_trainer),
        'subscription': model.startswith('订阅'),
    }
    price = ('high' if org.startswith('个体') and not has_site else
             'medium' if has_site else 'medium')
    decision = ('fast' if org.startswith('个体') or '一人' in (brand or '') else
                'moderate' if has_site else 'moderate')
    big = any(k in b for k in ['vad', '分销', 'distributor', '批发', 'master', 'isp'])
    vol = (4 if needs['oem'] or big else
           3 if has_site and not is_trainer else
           2 if is_trainer or has_site else 1)
    lang = {'德国': 'de', '奥地利': 'de', '法国': 'fr', '加拿大': 'en', '希腊': 'el',
            '匈牙利': 'hu', '塞尔维亚': 'sr', '捷克': 'cs', '波兰': 'pl', '西班牙': 'es',
            '意大利': 'it', '荷兰': 'nl', '丹麦': 'da', '瑞典': 'sv', '挪威': 'no',
            '芬兰': 'fi', '葡萄牙': 'pt', '罗马尼亚': 'ro', '克罗地亚': 'hr',
            '乌克兰': 'uk', '立陶宛': 'lt', '拉脱维亚': 'lv', '爱沙尼亚': 'et',
            '斯洛伐克': 'sk', '斯洛文尼亚': 'sl', '瑞士': 'de', '比利时': 'nl',
            '英国': 'en', '美国': 'en', '爱尔兰': 'en'}.get(col(row, '国家'), 'en')
    risks = []
    if org.startswith('个体'): risks.append('一人/个体=单点与节奏风险')
    if is_college: risks.append('公立身份合规：只谈私人/自费语境')
    if is_trainer: risks.append('教师红线：不打学员名单、不经培训语境推销')
    if col(row, '国家') in ('塞尔维亚', '罗马尼亚', '克罗地亚', '保加利亚', '爱沙尼亚',
                    '拉脱维亚', '立陶宛', '卢森堡', '冰岛', '斯洛文尼亚'):
        risks.append('R32 低投入小国：档案照建、外联降级')
    return org, model, needs, price, decision, vol, sorted(set(risks)), lang, certs

# ---------- P1 决策（候选可多个，首触只推一个） ----------
P = {
 'STC-28DGGPM':  {'price': '$99 USD EXW (2026-09-28, 15天有效)', 'desc': '8口 GE(7)+SFP PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/sFlow），PoE 看门狗'},
 'STC-424DGGPM-280W': {'price': '$165 USD EXW (2026-09-28, 15天有效)', 'desc': '24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗'},
 'STI-288GP':    {'price': '$74.8 USD EXW (2026-09-28, 15天有效)', 'desc': '工业非管理 8口 PoE af/at，250m 延伸，冗余 DC44–57V，DIN 轨，3 年保'},
 'STI-480XGGM':  {'price': '$253 USD EXW (2026-09-28, 15天有效)', 'desc': '工业 L2+ 8口+4×10G，ERPS<20ms，DIN 轨，宽温，3 年保'},
 'STI-280GE':    {'price': '$63.8 USD EXW (2026-09-28, 15天有效)', 'desc': '工业非管理 8口 GE，宽温 DIN，3 年保'},
 'CONSULT-OEM':  {'price': '—', 'desc': 'OEM/白牌合作探询（中性包装+贴客户型号+ODM 规格）'},
}
def p1_of(needs, org):
    if needs['oem']: return 'CONSULT-OEM'
    if needs['training']: return 'STC-28DGGPM'
    if needs['hotel'] or needs['voice']: return 'STC-424DGGPM-280W'
    if needs['industrial'] and not needs['hotel']: return 'STI-288GP'
    return 'STC-28DGGPM'

QUESTION = {
 'sub': "Roughly how many site visits a month come from a hung AP or camera on your networks?",
 'hotel': "Roughly how many site visits a month come from a hung AP or camera across your hospitality sites?",
 'industrial': "Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?",
 'training': "Which switch do you currently put on the bench for the VLAN/PoE lab demos?",
 'oem': "Do you currently badge any switching hardware under your own name, or is everything resold vendor-branded?",
 'default': "How many PoE ports does a typical site of yours need today?",
}
def question_of(needs, model):
    if model.startswith('订阅'): return QUESTION['sub']
    if needs['hotel']: return QUESTION['hotel']
    if needs['training']: return QUESTION['training']
    if needs['oem']: return QUESTION['oem']
    if needs['industrial']: return QUESTION['industrial']
    return QUESTION['default']

# ---------- 批1/2 手工覆盖（源自深挖结论；仅关键字段） ----------
OVERRIDE = {
 'A-002': {'org': '一人公司（TEN INVEST ApS 100% 控股壳）', 'model': '订阅制 NaaS（375 DKK/月起租网+29 更新+49 维保）',
   'decision': 'fast', 'vol': 3, 'p1': 'STC-28DGGPM',
   'p1_reason': '租约盒主打少上门+低至 $99 即 2 个月租金回本；学校/仓储 24 口升档在第 2 步再谈',
   'hotel_or_sub_note': '酒店只是 3 个案例之一且无 IPTV 证据；主推位=租约盒 8 口 PoE，不是 24 口酒店机',
   'needs': {'hotel': False}},
 'A-013': {'p1_reason': '教具箱（学员红线内，仅谈本人教学硬件）'},
 'A-016': {'p1_reason': '教具+工程双轨，均红线内'},
 'A-019': {'p1_reason': '教具红线内；工程咨询侧二源'},
 'A-018': {'p1': 'STI-288GP', 'p1_reason': '高山 webcam/户外 AP 供电点位（镜像站相册为证）；酒店侧第 2 步 STC-28DGGPM'},
 'A-011': {'org': '公立学院教授（私人顾问线）'},
 'A-012': {'p1': 'STC-28DGGPM', 'p1_reason': 'Cisco↔MikroTik 迁移实验室置换机'},
 'A-014': {'p1': 'STI-480XGGM', 'p1_reason': 'datasheet 级玩家：ERPS 环网自测最能建立技术信服'},
 'A-017': {'p1': 'STC-28DGGPM', 'p1_reason': 'MTCSWE 交换专向：L2+ 特性表即开场；样机 STC-28DGGPM 起步'},
}

out = {}
for r in data:
    grade = col(r, '评级'); code = col(r, '编号') if '编号' in COL else None
    if grade != 'A':
        continue
    code = col(r, '档案编号') or code
    if not code or not code.startswith('A-'):
        # 列名守卫：编号列实际名
        code = r[-1].strip() if r[-1].strip().startswith('A-') else code
    if not code.startswith('A-'):
        continue
    brand = col(r, '信号（在卖什么品牌）')
    org, model, needs, price, decision, vol, risks, lang, certs = infer(r)
    ov = OVERRIDE.get(code, {})
    org = ov.get('org', org); model = ov.get('model', model)
    for k, v in ov.get('needs', {}).items(): needs[k] = v
    price = ov.get('price', price); decision = ov.get('decision', decision); vol = ov.get('vol', vol)
    name_disp = col(r, '客户名称')
    contact = col(r, '入口/联系方式')
    _em = re.search(r'[\w.+-]+@[\w-]+\.[\w.]+', contact or '')
    email = _em.group(0) if _em else ''
    site = col(r, '网站')
    pending = bool(re.search(r'待核|待人工|未验证', contact or ''))
    email_state = ('待核·未验证投递（不进群发）' if email and pending else
                   '既有/公开' if email and not any(x in email for x in ['猜测', '未验证']) else
                   '模式猜测·未验证' if email else '缺失')
    p1 = ov.get('p1', p1_of(needs, org))
    entry = {
        'code': code, 'name': name_disp, 'country': col(r, '国家'), 'city': col(r, '城市'),
        'rating': 'A', 'website': site or None, 'phone': col(r, '电话') or None,
        'email': email or None, 'email_state': email_state,
        'certs': certs, 'biz_org': org, 'business_model': model,
        'needs': needs, 'price_sensitivity': price, 'decision_speed': decision,
        'volume_potential': vol, 'risk_flags': risks, 'lang': lang,
        'p1': p1, 'p1_reason': ov.get('p1_reason',
                ('主场景匹配+首触只推一个型号的纪律' if p1 != 'CONSULT-OEM' else '白牌/分销语境')),
        'first_question': ov.get('first_question', question_of(needs, model)),
        'alternates': [p for p in ['STC-28DGGPM', 'STC-424DGGPM-280W', 'STI-288GP', 'STI-480XGGM']
                       if p != p1][:2],
        'stage': '00-researched', 'struct_version': 'v2', 'updated': TODAY,
        'note': ov.get('hotel_or_sub_note'),
    }
    out[code] = entry

json.dump(out, open(ROOT / 'batch/structured_profiles_v1.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
missing_p1 = [c for c, e in out.items() if e['p1'] not in P]
print('A 类结构化档案:', len(out), '| P1 未登记:', missing_p1[:5])
from collections import Counter
print('P1 分布:', Counter(e['p1'] for e in out.values()).most_common())
print('推断需求覆盖: industrial', sum(e['needs']['industrial'] for e in out.values()),
      'training', sum(e['needs']['training'] for e in out.values()),
      'oem', sum(e['needs']['oem'] for e in out.values()),
      'voice', sum(e['needs']['voice'] for e in out.values()))
