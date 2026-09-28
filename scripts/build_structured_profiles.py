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
 # ── R56 批 3（A-021..A-030 深挖 2026-09-28）：邮件价格锚点 = P1 型号单价 ──
 'A-021': {'p1': 'STC-424DGGPM-280W', 'p1_reason': '克里特酒店/企业 WiFi 项目型：楼层 24 口 PoE+10G 上联一台到位（$165 邮件锚点一致）'},
 'A-022': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': '希腊 MikroTik 培训中心（HellasCom 集团）：教具实验架红线内；同集团采购合并触达，主商务窗在 A-024'},
 'A-023': {'p1': 'STC-28DGGPM', 'p1_reason': 'GTA 站点休眠、现职 e-dreams 智能楼宇分销：酒店 KNX/IP 混接 8 口盒（按现职开场，不炒 GTA 旧故事）'},
 'A-024': {'needs': {'hotel': True, 'voice': True}, 'p1': 'STC-424DGGPM-280W',
           'p1_reason': 'HellasCom 酒店 6Play 楼层标准件（WiFi/IPTV/CCTV/VoIP 混载）；隧道/机场公共段不跟，仅私营酒店线'},
 'A-025': {'p1': 'STC-28DGGPM', 'p1_reason': 'IME 软件商交叉销售（imeFoodService 门店）：餐饮一盒网络 8 口 PoE；ΔΕΥΑ 水务市政段规避'},
 'A-026': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'DECOIT vendor-neutral 科研型：datasheet/SNMP 透明先行，Voice VLAN 对齐其 Asterisk 线'},
 'A-027': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'MBN 塔站密封柜夏天高温：工业温宽 PoE 钉住缺口（$74.8 邮件锚点一致）；EU 补贴市政段走合规'},
 'A-028': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'SKYTRON 活动/市政 WLAN+监控：24 口 PoE 一台到位+10G 回传（Event 峰值问题开场）'},
 'A-029': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Kehrlein 全十证 NDA 级顾问：实验室评测机+技术档案，不打探其客户名单'},
 'A-030': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': 'Linux-Schmie 2027 新增 MTCSWE 课=教具采购窗（STP/VLAN 实验架），师者红线内'},
 # ── R56 批 4（A-031..A-040 深挖 2026-09-28）──
 'A-031': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'VARIA 大型 B2B 分销：$100-170 空白价位段是给它的牌；发票结算信用体系可镜像试探'},
 'A-032': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Aikom 2026 交换机线密集纳新（Zyxel 入职为证）：PoE 专精错位卡位，Connectivity Camp 为节点'},
 'A-033': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': '意大利官方 Trainer 双线：教具实验架红线内；WISP 咨询客户项目推荐位第 2 步'},
 'A-034': {'p1': 'STC-424DGGPM-280W', 'p1_reason': '1off OptiWize 管理面叙事：硬件级自愈（PoE 看门狗）+SNMP 遥测是同频语言'},
 'A-035': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Bitmagic 8 证休眠顾问：L2+ 特性表对话；先电话解冻再发信'},
 'A-036': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': 'TikTrain MikroTik+Ubiquiti 双栈培训：双栈通用 8 口 PoE 实验架，师者红线内'},
 'A-037': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Netify 安防集成：监控/门禁 PoE 供电接入层每单基础件（内编 Trainer 对话成本低）'},
 'A-038': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Toffoletto 9 证老炮、公开足迹弱：特性表+电话破冰，信息缺口如实标注'},
 'A-039': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'EFA/Relatech 工业 DT：温宽 PoE+看门狗错位 Red Lion/N-Tron（$74.8 邮件锚点一致）；水务公用段规避'},
 'A-040': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': 'Ciacci 前公立大学 IT 主管：公立红线户，仅私人顾问/鉴定线；实验室工具机 $99'},
 # ── R56 批 5（A-041..A-050 深挖 2026-09-28）──
 'A-041': {'p1': 'STC-28DGGPM', 'p1_reason': 'Busatti WISP 教父（Grifonline ISP+Linkwave 双创始人）：POP 柜自愈看门狗语言开路（$99 锚点一致），教具/生态二轨'},
 'A-042': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'PF Tech 分销+ROC 运营+监控工程三线：监控柜 24 口 PoE 牵头；公共监控段走规范'},
 'A-043': {'p1': 'STC-28DGGPM', 'p1_reason': 'Pína 个人 ISP：POP/CPE 8 口盒常换购（$99 锚点一致）；邮件极简三行字'},
 'A-044': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'Westercom 工业分销（Advantech EKI/Westermo）：EOL 替代场景低位温宽 PoE 补位不当对标（$74.8 锚点一致）'},
 'A-045': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Erhan 摩尔多瓦双证、公开足迹缺失：先短信破冰，信息缺口如实标注'},
 'A-046': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'AIRICOM IoT/M2M 分销：工业路由项目现场随单温宽 PoE；Red Lion/N-Tron 盘错位（$74.8 锚点一致）'},
 'A-047': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'CSI 30 年工业分销（Antaira 核心盘）：能源自动化民营段低价位错位；MSPO 军防+电车公共段一律不触（$74.8 锚点一致）'},
 'A-048': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': 'mtik.pl 全真硬件教室：MTCSWE 工位交换教具期期消耗（$99 锚点一致）；师者红线'},
 'A-049': {'p1': 'STC-28DGGPM', 'p1_reason': 'C3NET 双高阶工作室站休眠：支持邮箱域存活走 mt-support@；企业无线随单'},
 'A-050': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'SINUX 华沙个体双高阶（MTCSWE+MTCEWE）：特性表+电话核实（NIP 在册真实存续）'},
 # ── R56 批 6（A-051..A-060 深挖 2026-09-28）──
 'A-051': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'SAFES 波高端物业/酒店 IT 全托管（PMS+SOC）：单店客房 Wi-Fi+安防 24 口 PoE 随单（$165 锚点一致）'},
 'A-052': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'narrowin 瑞士 OT 可见性软件商：多站点试点被推荐温宽小盒（$74.8 锚点一致）；基建客户招牌段守边界'},
 'A-053': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'MiniMeLabs 葡团伦敦场所 Wi-Fi/分析：高密 AP 项目 PoE 接入层随单（$165 锚点一致）'},
 'A-054': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Direktronik PCR 40 年分销（N-net 在卖 ERPS/SNMPv3）：value-tier 24 口 PoE 白牌补位（$165 锚点一致）'},
 'A-055': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'Sarlin 芬兰 90 年工业伙伴（LNG/生物气站）：能源站温宽 PoE 补充+生命周期语言（$74.8 锚点一致）'},
 'A-056': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'AA Jones 赫尔批发大仓（N-Tron+Red Lion/HMS）：温宽 PoE 批发补件（$74.8 锚点一致）'},
 'A-057': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'System Devices 独代分销（Opto22/Epson 等）：Antaira 旁柜内温宽 PoE 独代候选（$74.8 锚点一致）'},
 'A-058': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'AGL 葡 Edge AI 分销（视觉机 4×PoE+、PoE 入类目）：PoE 上游温宽交换上架位（$74.8 锚点一致）'},
 'A-059': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'LinITX 双 Master 分销+培训中心：货架纯值 PoE 错价位补位+教具箱二轨（$165 锚点一致）'},
 'A-060': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Jezierski INDYCAR 赛道技术：临时赛事网 PoE+现货直击大厂交期痛点（$165 锚点一致）；顾问身份接触'},
 # ── R56 批 7（A-061..A-070 深挖 2026-09-28）──
 'A-061': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Mikrotikon 个人专家（CAPsMAN 集中 Wi-Fi 专长）：多 AP 项目 24 口 PoE 随单（$165 锚点一致）'},
 'A-062': {'p1': 'STC-28DGGPM', 'p1_reason': 'Tayyebi 奥斯汀 7 证个人、站 FreeHostia 占位：短信破冰薄档如实（$99 锚点一致）'},
 'A-063': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': 'Netrotik 芬兰培训中心+工程咨询双轨：诚实教具对比样本（$99 锚点一致）；师者红线'},
 'A-064': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Axbyte 瑞典托管 datacom（自有 co-lo+外包 NOC）：NOC 监控集成 24 口 PoE（$165 锚点一致）'},
 'A-065': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'FreeClix 英全栈 ISP（Guest WiFi+VoIP 双线）：Voice VLAN 接入层随单；NHS/郡议会公共段守边界（$165 锚点一致）'},
 'A-066': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Celenet 西班牙区域运营商+企业线：企业 WiFi/安防接入层随单，节点小盒二轨（$165 锚点一致）'},
 'A-067': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Hotelinking 千店酒店科技：争取进其 WiFiBot NOC 合格硬件推荐位=千店杠杆（看门狗自愈=少巡店；$165 锚点一致）；vendor-agnostic 中立尊重'},
 'A-068': {'p1': 'STC-28DGGPM', 'p1_reason': 'Díaz Gómez 十证个人、足迹薄：WhatsApp 破冰薄档如实（$99 锚点一致）'},
 'A-069': {'p1': 'STC-28DGGPM', 'p1_reason': 'Millie Evolution 英五证个人站裸目录：WhatsApp 破冰薄档如实（$99 锚点一致）'},
 'A-070': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'Hecnys Ignition 官认 SCADA 集成：边缘/现场段温宽 PoE（$74.8 锚点一致）；发电/油气/港口边界守'},
 # ── R56 批 8（A-071..A-080 深挖 2026-09-28）──
 'A-071': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Straznet 瑞南部 SMB 托管+SaaS 转轨：SMB 机柜 24 口 PoE 随单（$165 锚点一致）'},
 'A-072': {'p1': 'STC-28DGGPM', 'p1_reason': 'Ocampo 美 7 证 Hotmail 个人：破冰薄档如实（$99 锚点一致）'},
 'A-073': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': 'McCharles 多厂牌学院（UniFi+MikroTik 课）：课程教具诚实比较样本；师者红线（$99 锚点一致）'},
 'A-074': {'p1': 'STC-28DGGPM', 'p1_reason': 'Shore 英双证个人 CV 页：WhatsApp 破冰薄档如实（$99 锚点一致）'},
 'A-075': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': 'MyNetworkTraining 在线平台 7 万学员：视频课诚实第二厂牌样本；师者红线+平台中立不付背书（$99 锚点一致）'},
 'A-076': {'p1': 'STC-28DGGPM', 'p1_reason': 'Ziółkowski 波双证个站 500 休眠：邮件直连薄档如实（$99 锚点一致）'},
 'A-077': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'JA Shomer 克利夫兰老分销（Red Lion/HMS/Fieldbus）：温宽 PoE 补件（$74.8 锚点一致）'},
 'A-078': {'p1': 'STC-28DGGPM', 'p1_reason': 'Bejarano 西 MTCINE 个人：WhatsApp 破冰薄档如实（$99 锚点一致）'},
 'A-079': {'p1': 'STC-28DGGPM', 'p1_reason': 'Fuentes 西三证个人：WhatsApp 破冰薄档如实（$99 锚点一致）'},
 'A-080': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Cárdenas 与 A-066 同人互注：商务统一走 A-066，不重复触达（档案互注留档）'},
 # ── R56 批 9（A-081..A-090 深挖 2026-09-28）──
 'A-081': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'Profcon 瑞典 60 年工业集团：Nova 网络线温宽 PoE 生命周期补位（$74.8 锚点一致）；国防载荷线红线不触'},
 'A-082': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'Microstar 华沙 Perle 分销（站维护页）：Perle 旁并架（$74.8 锚点一致）维护期电话并行'},
 'A-083': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': 'FMS 德国 ISP 向 VAD+培训伙伴：ISP 白牌随单+训练教具比较样本（$99 锚点一致）；市政段边界+师者红线'},
 'A-084': {'p1': 'STC-28DGGPM', 'p1_reason': 'Dashti 美 7 证站长（站暂不可达）：邮件深持破冰（$99 锚点一致）'},
 'A-085': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'ATEC 英 30 年安防整合（全厂牌）：私营段监控柜 value PoE 补位（$165 锚点一致）；公共段边界'},
 'A-086': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'EQUIPAGES 法全 SI 集成：办公网无线/VoIP 接入柜随单+infogérance 滚动（$165 锚点一致）'},
 'A-087': {'needs': {'industrial': True}, 'p1': 'STI-288GP',
           'p1_reason': 'PEDAB 法国大集团分销：工业 PoE value 档并架（$74.8 锚点一致）；准入文件严谨'},
 'A-088': {'p1': 'STC-28DGGPM', 'p1_reason': 'Electromaster 爱尔兰：域名流落+NO-MX 触达降级（站被占如实标注；先电话名录核验）'},
 'A-089': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Switchshop 英框架大户：公共框架红线明示不碰；只谈私营段 24 口 PoE 补位（$165 锚点一致）'},
 'A-090': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'D-Side 荷中小电信一体交付：Voice VLAN 接入柜随单（$165 锚点一致）'},
 # ── R56 批 10（A-091..A-100 深挖 2026-09-28）──
 'A-091': {'needs': {'training': True}, 'p1': 'STC-28DGGPM',
           'p1_reason': 'mikrotikgyor 匈官方 Training Center：交换课诚实比较样本（$99 锚点一致）；师者红线；无公开邮箱先电话'},
 'A-092': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Marksman Titan 安保合并电子线：全国楼宇监控柜 value PoE（$165 锚点一致）'},
 'A-093': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Watkins 60 年安防：场馆高密摄像柜 PoE（$165 锚点一致）；DHS 联邦红线不触'},
 'A-094': {'p1': 'STC-28DGGPM', 'p1_reason': 'VELOCIgroup 丹 Netonix 渠道：Round-28 Netonix-out 纪律建档不推，无官网电话核验'},
 'A-095': {'p1': 'STC-28DGGPM', 'p1_reason': 'Rowe Networks 美 Netonix 渠道：Netonix-out 纪律建档不推（表单站+电话）'},
 'A-096': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Last Mile Gear→已并入 WAV 集团（301+同 MX 设施双信号）：Netonix-out 纪律建档；WAV 入口价值留档'},
 'A-097': {'p1': 'STC-28DGGPM', 'p1_reason': 'InternetTY 英 AltNet（100+ 五星）：POP/街柜接入小盒（$99 锚点一致）；网责 MTCSE/MTCINE 在册'},
 'A-098': {'p1': 'STC-28DGGPM', 'p1_reason': 'Vargyas 美 MTCNA 单证 LinkedIn 渠道：破冰薄档如实（$99 锚点一致）'},
 'A-099': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'MSI Works 英小体 Allied 信号（Wix 表单无邮箱）：手机破冰（$165 锚点一致）'},
 'A-100': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Networkology 英高监管 IT（G-Cloud/DoS 红线）：私营段 value PoE+边界明示（$165 锚点一致）；tenders@ 不动用'},
 # ── R56 批 11（A-101..A-110 深挖 2026-09-28）──
 'A-101': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Lloret 英智慧楼宇 MSI：Converged Network Systems 楼网总包指定权切入（$165 锚点一致）；Budd 具名'},
 'A-102': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'EAC 白金汉郡 MSP：私立教育段+制造随单接入柜（$165 锚点一致）；公立教育守边界已注'},
 'A-103': {'p1': 'STC-28DGGPM', 'p1_reason': 'Bechtle 英超大 VAR：CSV 自注规模排除名单——纪律建档不出信'},
 'A-104': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Centerprise 40 年公共生命周期（G-Cloud/TePAS/MoD·DE&S 红线）：只谈私营 Regulated 窄段+边界句（$165 锚点一致）'},
 'A-105': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Cisilion 大型集成：CSV 警告字条截断待核——排期冻结，待用户核原表全文后定'},
 'A-106': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'DACC 伦敦布线/DC 厂商中立：RISQS 铁路红线不触；私营银行/制药段+电话先行（$165 锚点一致）'},
 'A-107': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Esotec 安审安防（CCS 红线主干）：只谈非安审私营窄段+承认边界（$165 锚点一致）'},
 'A-108': {'p1': 'STC-28DGGPM', 'p1_reason': 'Roadtech 运输 SaaS：Allied 信号来源待核的弱对口破冰（$99 锚点一致）；如实薄档'},
 'A-109': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'RWL 爱/英/荷布线独立分销：Panduit 旁 active PoE 补位铺货（$165 锚点一致）'},
 'A-110': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Senseco 消防安防全国办：楼内消防/安防 IP 化接入柜（$165 锚点一致）；工程师文化实测文档'},
 # ── R56 批 12（A-111..A-120 深挖 2026-09-28）──
 'A-111': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Universal Networks 英 30 年光纤布线（multipartner）：架上 active 补位（$165 锚点一致）；无公开邮箱电话先行'},
 'A-112': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'BRS Networks 瑞典 NaaS+OT 监控（80 专家）：NaaS 接入位 TCO 话术（$165 锚点一致）'},
 'A-113': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'A3/CBX 美全国楼宇集团：安防/网络一体接入柜（$165 锚点一致）；集团采购中心化注意'},
 'A-114': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Amplitel 威州 MSP：公营事业楼宇接入+透明定价文化（$165 锚点一致）；CEO Lahm 具名'},
 'A-115': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'BCL 俄亥俄女性持有 ICT 设计（WBE/WOSB/DBE）：指定单接入层 value 位（$165 锚点一致）；Christy Miller 具名'},
 'A-116': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'GSI 密歇根 30 年安防/网络（厂商中立）：客户墙能源/汽车段接入层（$165 锚点一致）；USACE 联邦红线明示不触'},
 'A-117': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Griffon 缅因本地安防：摄像头柜 value PoE（$165 锚点一致）；安装质量文化'},
 'A-118': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'HBS 威州全栈（Cisco/HPE 同盟）：第二架价值线窄判别（$165 锚点一致）；第三方名录邮箱存疑标注'},
 'A-119': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'ITC 纽约 SMB 托管（监控+VoIP 双主线）：随单柜 value 位（$165 锚点一致）；无公开邮箱'},
 'A-120': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Kidwell 内布拉斯加 75 年弱电+电气：交钥匙 BOM 接入层 value 位（$165 锚点一致）'},
 # ── R56 批 13（A-121..A-130 深挖 2026-09-28）──
 'A-121': {'p1': 'STC-28DGGPM', 'p1_reason': 'Nexware 美：站点 500 异常如实薄档；MX 存活 support@ 信号核实破冰（$99 锚点一致）'},
 'A-122': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Paramount 三州安防：SHIELD SECaaS 月付模式的硬件现金结构切入（$165 锚点一致）'},
 'A-123': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'PCS 辛辛那提 2003 布线 F1000 史：NO-MX 触达降级，电话/表单先行（$165 锚点一致）'},
 'A-124': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'RTI 全国教育部署+仓储入库：K-12 接入柜（$165 锚点一致）；danl@ 具名'},
 'A-125': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Security 101 CT 加盟：一线同盟下分支第二架 value 线窄判别（$165 锚点一致）'},
 'A-126': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Security 101 Rochester：同集团判别具名 Victor 首邮（$165 锚点一致）'},
 'A-127': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Silco 多州消防安防 45,000 客户：随单柜+看门狗免回访（$165 锚点一致）'},
 'A-128': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'UberData NaaS 订阅+refresh 采购池：入门档套餐 value 位（$165 锚点一致）'},
 'A-129': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'VARtek K-12 教育专属驻场托管：学区接入柜免回访（$165 锚点一致）'},
 'A-130': {'p1': 'STC-424DGGPM-280W', 'p1_reason': 'Wire Technologies 30 年布线/DC/交换直通：直接对口接入层 value 位（$165 锚点一致）'},
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
