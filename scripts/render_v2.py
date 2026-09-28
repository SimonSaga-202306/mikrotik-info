# -*- coding: utf-8 -*-
"""A 类档案 v2 渲染器（R56：2026-09-28 用户审定规则）。

用户原始指令：「从头跑，后续所有的都按照加厚+这个优化后的规则来挖」。
规则来源：用户汇总的外部评审意见（R56 外审反馈）——可吸取项已并入本节与
docs/rules/客户档案结构与内容规则.md。

v2 结构（A 类专用；B/C 走旧模板不动）：
  SALES BRIEF（压缩模型）→ 基本事实（事实/推断/假设分层）→ 技术与在用 →
  需求与场景 → HR 与规模信号 → 联系方式 → 关键人 KP → 跟进步骤（最多3）→
  R54 调研要点 → R55 再发掘要点 → 产品决策（P1/备选，单一决策口径）→ SWOT →
  触达与风险红线 → Qualification 清单 → Unknowns → 首触邮件（英文样板）→
  跟进记录（含渠道/下次动作日期）→ 下次复核
价格纪律：一律 `$xx USD EXW (YYYY-MM-DD, 15天有效)`；SMTP 不可验如实标注；
推断字段一律【推断】标签；首触只推一个型号（P1）。"""
import json
import re
from pathlib import Path

ROOT = Path('/home/user/mikrotik-info')
STRUCT = json.loads((ROOT / 'batch/structured_profiles_v1.json').read_text(encoding='utf-8'))

# R41–R48 联系方式台账：code → 来源等级（official-company / leads-only / …），
# 晚文件（09-28 复筛）覆盖早文件（09-27）。profile 内需保留「来源等级：X」字样（冻结断言）。
TIER = {}
for _tp in sorted(ROOT.glob('batch/contact_research_*.json')):
    try:
        _obj = json.loads(_tp.read_text(encoding='utf-8'))
    except Exception:
        continue
    for _r in _obj.get('records', []):
        if _r.get('code') and _r.get('level'):
            TIER[_r['code']] = _r['level']

PRICE = {'STC-28DGGPM': {'price': '$99 USD EXW (2026-09-28, 15天有效）'.replace('（', '(').replace('）', ')'),
                         'price_cn': '$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）',
                         'desc': '8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启'},
         'STC-424DGGPM-280W': {'price_cn': '$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）',
                               'desc': '24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗'},
         'STI-288GP': {'price_cn': '$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）',
                       'desc': '工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保'},
         'STI-480XGGM': {'price_cn': '$253 USD EXW（2026-09-28 快照，15 天有效，报价前核价）',
                         'desc': '工业 L2+ 8口 GE + 4×10G SFP+，ERPS<20ms 环网，宽温，DIN 轨，3 年保'},
         'STI-280GE': {'price_cn': '$63.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）',
                       'desc': '工业非管理 8口 GE，宽温 DIN 轨，3 年保'},
         'CONSULT-OEM': {'price_cn': '—（合作探询，无量产报价）',
                         'desc': 'OEM/白牌合作：中性包装、贴客户型号、ODM 规格，MOQ 与认证另谈'}}
P_LABEL = {'STC-28DGGPM': 'STC-28DGGPM（8口 PoE 接入盒）',
           'STC-424DGGPM-280W': 'STC-424DGGPM-280W（24口 PoE + 4×10G）',
           'STI-288GP': 'STI-288GP（工业非管理 8口 PoE）',
           'STI-480XGGM': 'STI-480XGGM（工业 L2+ 8口+4×10G）',
           'STI-280GE': 'STI-280GE（工业非管理 8口 GE）',
           'CONSULT-OEM': 'OEM/白牌合作探询（无量产型号首推）'}

NEED_LABEL = [('poe', 'PoE 接入供电'), ('industrial', '工业/户外/宽温'), ('tenG', '万兆上行/骨干'),
              ('l2plus', 'L2+ 交换管理（VLAN/ERPS/QinQ）'), ('voice', 'VoIP/Voice VLAN'),
              ('oem', 'OEM/白牌'), ('hotel', '酒店/多住户'), ('training', '教学教具'),
              ('subscription', '订阅制设备资产')]

# 首触邮件：P1 场景钩子（英文样板；发送前由用户本地化/改名）
EMAIL_HOOK = {
 'STC-28DGGPM': ("8-port PoE with auto-recovery for your field deployments",
                 "We build a compact 8-port Gigabit PoE switch (240W budget, af/at) "
                 "with a hardware PoE watchdog that power-cycles a frozen AP or camera "
                 "automatically, plus clean 802.1Q VLAN / ERPS / sFlow on the management side. "
                 "Reference: $99 USD EXW."),
 'STC-424DGGPM-280W': ("24-port PoE + 10G uplinks for your larger sites",
                      "We build a 24-port Gigabit PoE switch (280W, af/at) with 4×10G SFP+ uplinks, "
                      "Voice VLAN and a hardware PoE watchdog that reboots hung APs/cameras "
                      "without a site visit. Reference: $165 USD EXW."),
 'STI-288GP': ("Rugged 8-port PoE for outdoor/unheated cabinets",
               "We build an unmanaged industrial 8-port PoE switch (af/at) with 250m extended "
               "reach, redundant 44–57V DC input with reverse-polarity protection, DIN-rail "
               "mount and a 3-year warranty. Reference: $74.8 USD EXW."),
 'STI-480XGGM': ("Industrial managed 8-port with 10G ring (ERPS <20ms)",
                 "We build an industrial L2+ 8-port Gigabit switch with 4×10G SFP+ uplinks, "
                 "ERPS sub-20ms ring failover, wide-temperature design, DIN-rail mount and "
                 "a 3-year warranty. Reference: $253 USD EXW."),
 'CONSULT-OEM': ("Neutral-built PoE switches under your own label",
                 "We manufacture PoE access switches (Marvell-based, L2+) for OEM/white-label "
                 "programs - neutral packing, your model numbers, ODM options on request.")}


def first_name(name):
    p = re.split(r'[\s/]', name.strip())[0]
    return p if p and not p[0].isdigit() else 'there'


def yaml_block(e):
    """机器可读档案（结构化一行一字段；推断字段在正文打标签，YAML 保持原值 + _src）。"""
    n = e['needs']
    lines = ['```yaml structured_profile',
             'code: %s' % e['code'],
             'rating: A',
             'country: %s' % (e['country'] or '?'),
             'biz_org: %s' % e['biz_org'],
             'business_model: %s' % e['business_model'],
             'decision_speed: %s' % e['decision_speed'],
             'price_sensitivity: %s' % e['price_sensitivity'],
             'volume_potential: %d  # 1-5' % e['volume_potential'],
             'needs: {poe: %s, industrial: %s, tenG: %s, l2plus: %s, voice: %s, oem: %s, hotel: %s, training: %s}'
             % tuple(str(n[k]).lower() for k in ('poe', 'industrial', 'tenG', 'l2plus', 'voice', 'oem', 'hotel', 'training')),
             'p1: %s' % e['p1'],
             'stage: %s' % e['stage'],
             'struct_version: %s  # v2 骨架' % e['struct_version'],
             'updated: %s' % e['updated'],
             '```']
    return lines


def render(e, ctx):
    """e = structured 条目；ctx = dict(name, country, city, site, typ, signal, ownbrand,
    angle, sku, contact, prio, status, src, note, why, rec, rec55, person, person_disp,
    mails, tels, certs_desc, brands, fname_person)。返回行列表。"""
    L = []
    w = L.append
    name, note = ctx['name'], ctx['note']
    person_disp = ctx['person_disp']
    p1 = e['p1']
    p1info = PRICE[p1]

    # ---- 头 ----
    w('# %s' % name)
    w('')
    w('> **评级 A**　|　%s%s　|　档案编号 `%s`　|　优先级 %s　|　状态：%s'
      % (e['country'], ' · ' + ctx['city'] if ctx['city'] else '', e['code'], ctx['prio'], ctx['status']))
    w('>')
    w('> **触达状态（Stage）**：%s　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）' % e['stage'])
    w('')
    for ln in yaml_block(e):
        w(ln)
    w('')

    # ---- SALES BRIEF ----
    w('## SALES BRIEF（压缩模型）')
    w('')
    _bg = ctx['rec55']['dimensions']['背景深描'] if ctx['rec55'] else None
    biz_one = (_bg.split('。')[0] + '。') if _bg and '。' in _bg[:130] else ((_bg[:110] + '…') if _bg else e['biz_org'] + '；' + e['business_model'])
    w('- **是谁**：%s' % biz_one)
    w('- **商业模式**：%s' % e['business_model'])
    w('- **为什么值得跟**：%s' % ctx['why'])
    w('- **P1（首触唯一主推）**：%s — %s；%s' % (P_LABEL[p1], e['p1_reason'], p1info['price_cn']))
    w('- **第一问（只问一个）**：%s' % e['first_question'])
    unk = ('现有交换机品牌与 PoE 预算未确认；' + ('采购量未确认' if e['volume_potential'] < 4 else '集团/分销内部决策层级未确认'))
    w('- **最大未知（影响成交的）**：%s' % unk)
    w('- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理')
    w('')

    # ---- 基本事实 ----
    w('## 基本事实（事实/推断/假设分层）')
    w('')
    w('| 项 | 内容 | 层级 |')
    w('|---|---|---|')
    w('| 名称 | %s（CSV 原样；登记名以调研为准） | 事实 |' % name)
    w('| 国家/城市 | %s%s | 事实 |' % (e['country'], ' / ' + ctx['city'] if ctx['city'] else ''))
    w('| 网站 | %s | 事实 |' % (ctx['site'] or '—（无公开站点）'))
    w('| 类型 | %s | 事实（CSV 名录口径） |' % ctx['typ'])
    if person_disp:
        w('| 关键人 | %s | 事实 |' % person_disp)
    w('| 反向信号（资质/品牌） | %s | 事实（名录/自报口径） |' % ctx['signal'][:200])
    w('| 组织性质 | %s | 【推断】 |' % e['biz_org'])
    w('| 商业模式 | %s | 【推断】 |' % e['business_model'])
    w('| 团队规模 | %s | 【推断】 |' % ('一人/微型' if '个体' in e['biz_org'] or '一人' in e['biz_org'] else ('有官网组织，规模未量化' if ctx['site'] else '未明')))
    w('| 决策链 | %s | 【推断】 |' % ('短（本人即决策）' if e['decision_speed'] == 'fast' else '中（联系人+业主/采购两层以内）'))
    if ctx['rec55']:
        for dim, text in ctx['rec55']['dimensions'].items():
            if dim in ('背景深描', '芯片与在用型号'):
                w('| R55·%s | %s | 事实+【推断】混合，见证据摘录 |' % (dim, text[:180]))
    if e.get('note'):
        w('| 批注 | %s | 【推断】 |' % e['note'])
    if '待人工补信息' in note:
        w('| ⚠️ 信息缺口 | 本条**抓不到邮箱**，需人工补齐邮箱或改为电话单独跟进后再进群发名单 | 事实 |')
    w('')

    # ---- 技术与在用 ----
    w('## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）')
    w('')
    if ctx['rec55']:
        w(ctx['rec55']['dimensions']['芯片与在用型号'])
    else:
        w('（待深挖批覆盖；当前仅有 CSV 名录口径：%s）' % ctx['signal'][:120])
    w('')
    w('> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；'
      '在用品牌未获客户本人确认前一律视为【假设】。')
    w('')

    # ---- 需求与场景 ----
    w('## 需求与场景（推断标签）')
    w('')
    acted = [lbl for k, lbl in NEED_LABEL if e['needs'].get(k)]
    w('- **推断需求面**：%s' % ('、'.join(acted) if acted else '待摸底'))
    for k, lbl in NEED_LABEL:
        if e['needs'].get(k):
            w('  - %s：【推断】依据 CSV 信号/深挖' % lbl)
    w('')

    # ---- HR 与规模信号 ----
    w('## HR 与规模信号（招聘/团队/绿旗）')
    w('')
    hr_bits = []
    if ctx['rec55']:
        bg = ctx['rec55']['dimensions'].get('背景深描', '')
        if any(k in bg for k in ('招', '员工', '团队', '外包', 'one-person', '雇员')):
            hr_bits.append(bg)
    if hr_bits:
        for b in hr_bits:
            w('- %s' % b)
    else:
        w('- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。')
    w('')

    # ---- 联系方式 ----
    w('## 联系方式（已有/猜测分标）')
    w('')
    # 版式纪律：邮箱地址独占一行（R41–R48 冻结断言逐字匹配「- **邮箱**：{addr}」与「- **邮箱**：—」）
    if e['email']:
        w('- **邮箱**：%s' % e['email'])
        w('  - 状态：%s' % e['email_state'])
    else:
        w('- **邮箱**：—')
        w('  - 状态：缺失（leads-only 口径：人工补录前**不进群发**，与旧批次纪律一致）')
    w('- **电话**：%s' % (('、'.join(ctx['tels'])) if ctx['tels'] else '—'))
    tier = TIER.get(e['code'])
    if tier:
        # 台账字样必须逐字出现「来源等级：{level}」（冻结断言按纯文本匹配），故整行不加粗
        w('- 来源等级：%s（R41–R48 联系方式台账口径）' % tier)
    w('- **原始联系字段**：%s' % (ctx['contact'] or '—'))
    w('- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——'
      '「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。')
    if e['email_state'] == '模式猜测·未验证':
        w('- ⚠️ 邮箱为模式猜测：**未验证**，首封若退信立即停用并换通道。')
    w('')

    # ---- 关键人 KP ----
    w('## 关键人（KP）与触达通道')
    w('')
    if ctx['rec55'] and ctx['rec55'].get('kp'):
        w('| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |')
        w('|---|---|---|---|---|')
        for k in ctx['rec55']['kp']:
            w('| %s | %s | %s | %s | %s |' % (k.get('name', '—'), k.get('role', '—'), k.get('contact', '—'), k.get('status', '—'), k.get('source', '—')))
    elif person_disp:
        w('- **%s**（本人直达；角色=业主/顾问本人，依据名录）' % person_disp)
    else:
        w('- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。')
    w('')

    # ---- 跟进步骤 ----
    w('## 跟进步骤（最多 3 次 · 成功/退出标准）')
    w('')
    w('> 每次只推进一个台阶、只问一个问题；全程只推 P1（%s），备选型不进邮件。' % P_LABEL[p1])
    w('')
    steps = ctx['rec']['followup_plan'] if ctx['rec'] else None
    custom = ctx['custom_followup']
    if custom:
        steps = custom
    if steps:
        for i, st in enumerate(steps, 1):
            if custom:
                w('### 第 %d 次 · %s' % (i, st['stage']))
                w('')
                w('- **推什么**：%s（统一口径=P1 系列，不外溢）' % st['product'])
                w('- **切入点**：%s' % st['angle'])
                w('- **要问的问题**：%s' % st['question'])
                w('- **随附/动作**：%s' % st['proof'])
            else:
                stage = re.sub(r'^第[一二三四五六七八九十]+次跟进\s*·\s*', '', st['stage'])
                w('### 第 %d 次跟进 · %s' % (st['step'], stage))
                w('')
                w('- **推什么**：%s' % st['product'])
                w('- **切入点**：%s' % st['angle'])
                w('- **要问的问题**：%s' % st['question'])
                w('- **随附证明**：%s' % st['proof'])
            w('')
    else:
        w('### 第 1 次 · 首触（P1 单型号 + 一个问题）')
        w('')
        w('- **推什么**：%s' % P_LABEL[p1])
        w('- **要问的问题**：%s' % e['first_question'])
        w('- **成功标准**：对方回复任一实质信息（现用品牌/端口数/上门频次）或同意收样机')
        w('- **失败退出**：14 天无回复 → 进入季度低频；退信 → 标记通道失效换 KP')
        w('')
        w('### 第 2 次 · 价值换信息')
        w('')
        w('- **动作**：补一份 1 页特性摘要（L2+ 特性表），再问一个递进问题')
        w('- **成功标准**：给出场景细节或引荐技术对接人')
        w('- **失败退出**：再无回复 → 降为季度触达')
        w('')
        w('### 第 3 次 · 收束')
        w('')
        w('- **动作**：明确提议 30 天评估样机或确认无需求后归档')
        w('- **成功标准**：样机单/报价请求')
        w('- **退出**：书面无兴趣或三次均无实质回应 → **停止主动开发**（停止条件见红线节）')
        w('')
    w('')

    # ---- R54 调研要点 ----
    if ctx['rec']:
        w('## R54 调研要点（加厚 · 全文见原始 JSON）')
        w('')
        w('> 调研日期 **%s**；原始记录：`%s`。以下为要点压缩，证据原文全部保留。'
          % (ctx['rec'].get('researched_on', '—'), ctx['rec'].get('_file', '—')))
        w('')
        for dim, text in ctx['rec']['dimensions'].items():
            w('- **%s**：%s' % (dim, text))
        w('')
        w('### R54 原文证据摘录（全部保留）')
        w('')
        for f in ctx['rec']['facts']:
            w('- **【%s】**%s' % (f['dim'], f['text']))
            w('  > %s' % f['quote'])
            w('  > 来源：%s' % f['url'])
        w('')

    # ---- R55 再发掘要点 ----
    if ctx['rec55']:
        w('## R55 再发掘要点（深挖 · 全文见原始 JSON）')
        w('')
        w('> 调研日期 **%s**；原始记录：`%s`；价格均为 EXW 快照。'
          % (ctx['rec55'].get('researched_on', '—'), ctx['rec55'].get('_file', '—')))
        w('')
        for dim, text in ctx['rec55']['dimensions'].items():
            w('- **%s**：%s' % (dim, text))
        w('')
        w('### R55 证据摘录（全部保留 · 含数量）')
        w('')
        for f in ctx['rec55']['facts']:
            w('- **【%s】**%s' % (f['dim'], f['text']))
            w('  > %s' % f['quote'])
            w('  > 来源：%s' % f['url'])
        w('')
        if ctx['rec55'].get('reliability'):
            w('> 核对可靠性说明：%s' % ctx['rec55']['reliability'])
            w('')

    # ---- 产品决策 ----
    w('## 产品决策（Saga · 单一决策口径）')
    w('')
    w('| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |')
    w('|---|---|---|---|---|')
    w('| **P1（首触唯一）** | %s | 主场景 | %s | %s |' % (P_LABEL[p1], p1info['price_cn'], e['p1_reason']))
    for i, alt in enumerate(e['alternates'], 2):
        if alt in PRICE:
            w('| 备选%d | %s | 升级/延展场景 | %s | P1 过后的台阶，不进首触邮件 |'
              % (i, P_LABEL[alt], PRICE[alt]['price_cn']))
    w('')
    w('- **P1 规格一句话**：%s' % p1info['desc'])
    w('- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子'
      '（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。')
    w('')

    # ---- SWOT ----
    w('## SWOT')
    w('')
    if ctx['rec55']:
        w(ctx['rec55']['dimensions']['优缺点SWOT'])
    else:
        w('- **S**：%s' % ctx['why'])
        w('- **W**：%s' % ('；'.join(e['risk_flags']) if e['risk_flags'] else '公开信息有限'))
        w('- **O**：P1 场景切入（%s）' % e['p1_reason'])
        w('- **T**：现有供应商惯性；价格竞争。')
    w('')

    # ---- 触达与风险红线 ----
    w('## 触达与风险红线')
    w('')
    w('**通用红线（所有客户适用）**')
    w('')
    w('1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。')
    w('2. **台厂不是客户**，只是信号源。')
    w('3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。')
    w('4. 大集团先问清采购层级（国别 vs 集团统一）。')
    w('5. 样机先送测，再谈价格。')
    w('')
    if e['risk_flags']:
        w('**本户特别红线/停止条件**')
        w('')
        for rf in e['risk_flags']:
            w('- %s' % rf)
        w('')
    w('**停止开发条件（命中任一即停）**：3 次定向触达无任何实质回复；确认现用平台完全满足需求；'
      '只愿比价不愿谈场景；决策者确认接触不到；对方书面拒绝。')
    w('')

    # ---- Qualification 清单 ----
    w('## Qualification 清单')
    w('')
    w('| 门槛 | 状态 |')
    w('|---|---|')
    w('| 需求面成立（PoE/接入层池） | ✅ |')
    w('| 决策人识别 | %s |' % ('✅' if (person_disp or (ctx['rec55'] and ctx['rec55'].get('kp'))) else '❓'))
    w('| 触达通道 | %s |' % ('✅ 邮箱域已验 MX' if e['email'] else '❓ 缺邮箱'))
    w('| 现用交换品牌 | ❓ 未确认 |')
    w('| 采购量/预算 | ❓ 未确认 |')
    w('| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |')
    w('')

    # ---- Unknowns（登记待问清单）
    w('## Unknowns（待问清单 · 首触后逐项消除）')
    w('')
    w('- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）')
    w('- [ ] 典型站点端口数与供电预算')
    w('- [ ] 上门/故障频次（订阅制客户的核心成本）')
    w('- [ ] 采购决策人与付款口径')
    if 'training' in acted:
        w('- [ ] 教具现有设备与换代周期（红线内，只问本人教学硬件）')
    w('')

    # ---- 首触邮件 ----
    w('## 首触邮件（英文样板 · 可直接发送）')
    w('')
    subj, pitch = ctx['custom_email'] if ctx['custom_email'] else EMAIL_HOOK[p1]
    if not ctx['custom_email']:
        first = first_name(ctx['person'] or name)
        obs = ('I came across %s - %s.' % (ctx['company'], ctx['typ'])
               if ctx.get('company') else 'I came across your work.')
        body = ('Hi %s,\n\n%s\n\n%s\n\n%s\n\n'
                'If it is useful, I can send one unit for a 30-day evaluation - '
                'just tell me where to ship it. If not a fit, one line and I close the loop.\n\n'
                'Best regards,\nSaga Telecom - PoE switch OEM/ODM (neutral packing available)'
                % (first, obs, pitch, 'One question: %s' % e['first_question']))
    else:
        body = ctx['custom_email'][1]
    w('**主题**：%s' % subj)
    w('')
    w('```text')
    w(body)
    w('```')
    w('')
    w('> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；'
      '③ 落款换成你自己的名字与公司；④ **一次只问一个问题**；⑤ 货币单位一律 USD 并带快照日期；'
      '⑥ 该客户为教师/公立身份时先读「本户特别红线」。')
    w('')

    # ---- 跟进记录 ----
    w('## 跟进记录')
    w('')
    w('| 日期 | 渠道（邮件/电话/LinkedIn/展会） | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |')
    w('|---|---|---|---|---|---|---|')
    w('|  |  |  |  |  |  |  |')
    w('')
    w('> 首次触达前留空；发出邮件后填入日期与渠道。有新进展时告诉我，我来更新本档案并重评 stage。')
    w('')

    # ---- 下次复核 ----
    w('## 下次复核')
    w('')
    w('- 固定节点：首触发出后 **14 天**无回复 → 复核是否降频/降级；有任何回复 → 当即重评 stage 与评级。')
    w('- 报价纪律：全部价格为 USD EXW 快照（2026-09-28，15 天有效）；过窗先核价再报价。')
    w('')
    w('---')
    w('')
    w('*建档日期：2026-09-22　|　结构 v2：2026-09-28（R56 规则）　|　数据来源：客户名单_反向信号_2026-09.csv + R54/R55 调研 JSON*')
    return L


def yaml_of(code):
    e = STRUCT.get(code)
    return yaml_block(e) if e else []
