#!/usr/bin/env python3
"""Generate a per-account follow-up strategy for the A-grade accounts."""
import csv, re

CSV = "客户名单_反向信号_2026-09.csv"
OUT = "A级客户跟进策略_2026-09.md"

# 场景 -> (型号, 卖点, 怎么开发, 风险点)
PLAY = {
    "INDUSTRIAL": (
        "STI-488XGGPM（Saga）（导轨式，4×10G 上行 + 8×千兆 PoE++）",
        "DIN 导轨安装、-40~75℃ 宽温、宽压输入、双电源冗余、ERPS 环网收敛 <20ms、PoE++ 90W 直接带工业相机和 AP",
        "第一句就问「你工业现场现在用谁的交换机？环网收敛多少毫秒？」——用 ERPS 实测数据对比切入，然后要求送一台上机柜实测 30 天",
        "工业客户认硬认证（CE / UL / EN50155 / 海事 DNV），缺一项直接出局；温度范围、MTBF、EMC 等级必须给书面数据，不能口头说；现场一旦上线几乎不换，所以第一次必须测通，否则永远没第二次"),
    "POE": (
        "STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）",
        "802.3bt 单口 90W、**PoE 看门狗（摄像头死机自动断电重启，省一趟上门）**、250m 延长供电、端口隔离、整机功率预算足",
        "替他算一笔账：24 个 4K 头全开要多少瓦、满配后还剩多少余量——这是每个做监控的人都踩过的坑，算清楚就赢一半",
        "**PoE 功率预算和供电稳定性是验收红线**，虚标功率会当场翻车；必须送测、必须给整机功率实测数；部分非标 PoE 相机存在兼容性问题，要先拿他的机型测"),
    "HOTEL": (
        "STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）",
        "客房 VLAN 隔离、端口隔离（防客人私接路由器）、PoE 同时供 AP / IPTV 机顶盒 / IP 话机、组播 IPTV 不卡",
        "问「一间客房下几根线？AP 怎么供电？IPTV 走不走组播？」——酒店是多期项目，一期做进去后面几期跟着走",
        "酒店项目周期长且受装修进度牵制，别押季度指标；采购决定权常在弱电总包而非业主，要找到总包；客房网络出问题客人直接投诉，稳定性零容忍"),
    "MULTICAST": (
        "STC-424XGGPM-440W（Saga）（组播能力完整 + PoE 供电）",
        "IGMP Snooping v2/v3、IGMP Querier、组播 VLAN、快速离开（Fast Leave）、**QoS/DSCP 优先级队列**（Dante 音频 over IP 与 IPTV 都靠它不丢包不抖动）",
        "开口就问「IPTV 卡不卡？是不是组播没配好，全楼在泛洪？」；若是 Dante / 音频 over IP 场景，改问「音频有没有出现过断续或丢包？」——Dante 对组播和 QoS 极敏感，说中就是内行",
        "组播出问题是满屏花屏，客户零容忍；必须先小规模（一个楼层）验证再铺开；要确认他的组播源和播放器兼容性"),
    "SWITCH": (
        "STC-424XGGPM-440W（Saga）（24×千兆 + 4×万兆 SFP+，三层）",
        "**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写",
        "这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」",
        "他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任"),
    "FIBRE": (
        "STC-424XGGM（Saga）（24×千兆 + 4×万兆 SFP+）",
        "4×10G SFP+ 上行、QinQ 做用户隔离、端口隔离、组播、广播风暴抑制",
        "问「OLT 下面挂多少用户？每用户怎么隔离？上行带宽怎么收敛？」——他们是按端口数买设备的，算单端口成本最有效",
        "户外机柜场景要确认温度和防雷等级；运营商类客户可能要求入网许可或本地认证，先问清楚再报价"),
    "CAMPUS": (
        "STC-424XGGPM-440W（Saga）（PoE 供 AP 与摄像头）",
        "PoE 供 AP / 摄像头 / 门禁、按楼栋或按班级 VLAN 隔离、组播、端口隔离、整机功率足",
        "校园是分期扩建的，问「今年新增几栋楼 / 几个班？」；寒暑假是施工窗口，提前一个季度谈",
        "校园网常走政府招标或教育局集采，要提前摸清是不是框架协议内；开学季绝对不能出问题，验收极严"),
    "ISP": (
        "STC-424XGGM（Saga）（4×10G 上行，收敛比高）",
        "4×10G 上行、QinQ 用户隔离、组播、端口隔离、广播抑制、SNMP 对接现有网管",
        "问「接入层一台带多少用户？上行怎么收敛？」；他们按端口成本算账，把单端口价格摊到每个用户给他看",
        "ISP 对设备故障率极度敏感，一台炸掉就是一批投诉；要先小批量试用跑半年；备件和 RMA 响应速度要提前承诺"),
    "MTCSWE": (
        "STC-424XGGPM-440W（Saga）（24×千兆 + 4×万兆 SFP+，三层）",
        "**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写",
        "他持有 MTCSWE（MikroTik 交换认证），交换是正式专长——**不用给他做科普**。开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」直接给 CLI 命令对比和转发实测数据",
        "他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全；含糊其辞会立刻失去这类技术型客户的信任"),
    "INFLUENCE": (
        "先给样机，不做型号推销",
        "他靠讲课和方案吃饭，多一个能讲、能演示、能推荐的品牌就是多一门课",
        "给他样机 + 完整技术资料 + 可公开讲的案例，让他讲课时用；**不要一上来谈价格和返点**，谈「你能多讲什么内容」",
        "这类人最在意「会不会砸我招牌」——绝不能让他推荐没实测过的东西；给他的一定要先自己测通；后续他带来的单子要让他有面子也有实际收益"),
}

NEED_PAT = [
    ("MTCSWE",     r'MTCSWE'),
    ("SWITCH",     r'交换专长|Switching|switch|交换机|CRSDL2|L2 过滤器|Link Bonding|链路聚合|生成树|RSTP|MSTP'),
    # 「监控」在中文里既指视频监控也指网络监控(NMS)，只认明确的视频监控写法
    ("POE",        r'CCTV|视频监控|摄像头|门禁|access control|报警|对讲|PoE|POE'),
    ("HOTEL",      r'酒店|Hospitality|hospitality|多住户|MDU|Multi-Dwelling|公寓|强制门户|Captive'),
    ("INDUSTRIAL", r'工业|IT/OT|IT-OT|BMS|楼宇自控|电网|制造|仓库|农业|能源|KNX|Marine|船用'),
    ("MULTICAST",  r'组播|Multicast|multicast|IPTV|PIM-SM|Dante|Audinate'),
    ("FIBRE",      r'FTTH|GPON|光纤|Glasfaser|FTTC|xDSL|DOCSIS|ETTH'),
    ("CAMPUS",     r'校园|学区|教育|学校|学院|Campus'),
    ("ISP",        r'WISP|ISP|运营商|骨干|backbone|BGP|POP'),
    ("INFLUENCE",  r'讲师|培训|学院|Academy|academy|培训中心|大会|MUM|产品经理|售前|开源|自研软件'),
]
# 场景优先级：越具体越靠前
# 组播排在 PoE 之前：同时命中两者时，组播才是决定方案成败的那一项（Dante 音频、
# IPTV、监控组播都是如此），PoE 只是常见供电需求，谁都能满足
ORDER = ["MULTICAST", "POE", "HOTEL", "INDUSTRIAL", "CAMPUS", "FIBRE", "SWITCH", "ISP", "MTCSWE", "INFLUENCE"]
LABEL = dict((k, k) for k in ORDER)


def clean(text):
    """Strip our own annotations so it is never read back as a customer signal.

    Everything after an arrow is our inference. Bracketed tags and star
    markers are ours too. Leaving them in caused real mis-grading: a note
    reading "酒店多站点 = PoE 接入交换机批量需求" was scored as though
    the customer had asked for PoE.
    """
    text = re.sub(r'【[^】]*】', ' ', text)
    text = re.sub(r'→[^；。\n]*', ' ', text)
    text = re.sub(r'[★☆]+', ' ', text)
    return text


def scenarios(blob):
    """Single source of truth for scenario detection.

    Cleans our own annotations out first, then returns matches in ORDER
    priority. Every script must import this rather than rolling its own,
    because duplicates silently drifted apart and graded the same account
    three different ways.
    """
    blob = clean(blob)
    hits = [k for k, pat in NEED_PAT if re.search(pat, blob)]
    return [k for k in ORDER if k in hits]


def main():
    rows = list(csv.reader(open(CSV, encoding="utf-8-sig")))
    hdr, data = rows[0], rows[1:]
    a = [r for r in data if r[17] == "A"]

    lines = []
    w = lines.append
    w("# A 级客户跟进策略（2026-09）")
    w("")
    w("评级口径：**A = 有明确需求信号 且 好跟进**（有具体对接人、决策链短、不需要过总部采购）。")
    w("B 级 490 家慢慢养，C 级 102 家是大公司/集团/自有品牌/竞品，单独走另一套路子。")
    w("")
    w("本文件共 **%d 家** A 级客户，按国家排列。每家四行：客户特点 → 推什么型号 → 怎么开发 → 风险点。" % len(a))
    w("")
    w("---")
    w("")

    from collections import defaultdict
    byc = defaultdict(list)
    for r in a:
        byc[r[1]].append(r)

    for country in sorted(byc, key=lambda c: -len(byc[c])):
        w("## %s（%d 家）" % (country, len(byc[country])))
        w("")
        for r in byc[country]:
            name, city, site, typ, contact, note = r[0], r[2], r[3], r[4], r[9], r[16]
            blob = " ".join([name, typ, r[5], note])
            sc = [k for k in ORDER if k in scenarios(blob)]
            feat = note.strip() or "（%s）" % typ
            w("### %s%s" % (name, "　—　%s" % city if city else ""))
            w("")
            w("**客户特点**：%s" % feat)
            w("")
            for key in sc[:2]:
                sku, sell, dev, risk = PLAY[key]
                w("**推什么**（%s）：%s" % (key, sku))
                w("")
                w("　卖点：%s" % sell)
                w("")
                w("**怎么开发**：%s" % dev)
                w("")
                w("**风险点**：%s" % risk)
                w("")
            if not sc:
                w("**推什么**：STC-424XGGM（Saga）（通用接入，先验证需求）")
                w("")
                w("**怎么开发**：先问清他现在接入层用谁的设备、痛点在哪，再定型号")
                w("")
                w("**风险点**：需求信号不明确，别急着报价，先摸底")
                w("")
            w("- 联系：%s%s" % (contact, "　网站：%s" % site if site else ""))
            w("")
        w("---")
        w("")

    w("## 通用红线（所有客户适用）")
    w("")
    w("1. **包装、外观、说明书全部中性**，不出现「Made in China」，贴客户自己的型号——这是硬要求，不能为了省事破坏。")
    w("2. **台湾厂商不是客户**，只是信号源，不要开发。")
    w("3. **PoE 功率和工业温宽是两类最容易当场翻车的指标**，任何口头承诺都要落到实测数据。")
    w("4. **大集团先问清采购层级**：是国别决策还是集团统一采购（Senetic 七国、Rexel 三国、OEM Automatic 三国都是这类），问错了白谈。")
    w("5. 样机先送测再谈价格；价格战是最后一张牌，不是第一张。")
    w("")

    open(OUT, "w", encoding="utf-8").write("\n".join(lines))
    print("written", OUT, len(lines), "lines,", len(a), "accounts")


if __name__ == "__main__":
    main()
