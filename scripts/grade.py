#!/usr/bin/env python3
"""Grade the reverse-signal list A / B / C and record the reason.

A = worth chasing AND reachable: a specific switching need, plus a named
    person with a direct line and a short decision chain.
B = worth keeping warm: a signal exists but the need is unproven or the
    contact is generic.
C = hard: big groups, own-brand distributors, competitors, out of scope.
"""
import csv, re
from collections import Counter

CSV = "客户名单_反向信号_2026-09.csv"

# --- need signals, strongest first ---------------------------------------
NEED = {
    "MTCSWE":      (r'MTCSWE',                              "交换认证 MTCSWE"),
    "SWITCH":      (r'交换|Switching|switch|交换机|CRSDL2|L2 ', "交换专长"),
    # 「监控」歧义：只认明确写「视频监控 / CCTV / 摄像头」，避免把网络监控(NMS)误判成 PoE 需求
    "POE":         (r'PoE|POE|CCTV|视频监控|摄像头|门禁|报警|对讲', "PoE/监控/门禁"),
    "HOTEL":       (r'酒店|Hospitality|hospitality|多住户|MDU|公寓|强制门户|Captive', "酒店/多住户"),
    "INDUSTRIAL":  (r'工业|IT/OT|IT-OT|BMS|楼宇自控|电网|制造|仓库|农业|能源', "工业/楼宇"),
    "MULTICAST":   (r'组播|Multicast|multicast|IPTV|PIM-SM|Dante|Audinate', "组播/IPTV"),
    "FIBRE":       (r'FTTH|GPON|光纤|Glasfaser|FTTC|xDSL|DOCSIS', "光纤接入"),
    "ISP":         (r'WISP|ISP|运营商|骨干|backbone|BGP',        "ISP/骨干"),
    "CAMPUS":      (r'校园|学区|教育|学校|学院|Campus',            "校园/教育"),
    "INFLUENCE":   (r'讲师|培训|学院|Academy|academy|培训中心|大会|MUM|产品经理|售前', "影响力/渠道"),
}
# weak on its own: routing or user-management specialists
WEAK = r'^MTCNA(\+MTCRE)?(\+MTCWE)?(\+MTCUME)?(\+MTCIPv6E)?$'

HARD_TYPE = r'大分销|Master\+VAD|自有品牌|品牌（竞品）|竞品|台厂|工控二手'
HARD_NOTE = (r'Fortune|财富 ?500|上市|全国性|市政|IBEX35|集团|'
             # 规模数字：必须排除前接数字，否则会命中型号片段（IGS-801M、EX-9911M）
             # 或电话号码片段（+44 1449 888000）—— 后者曾把 LinITX 压在 C 级
             r'全球最大|北美领先|全国性 ISP|NS ?万|100 ?万|(?<![\d.])8000|(?<![\d.])1M\b|'
             # 规模信号：多分部、跨州/跨国覆盖、自称大型/最大/领先
             r'大型|最大|领先|\d+ ?\+ ?州|\d+ ?个分部|覆盖 \d+|跨国|'
             r'官方分销之一|one of the largest|leading|nationwide|'
             # 规模别称常写在备注里而非类型列
             r'大分销|老牌|巨头|electrical distribution')


# Countries confirmed outside the target region (Europe + US/Canada).
#
# Deliberately an EXCLUSION list rather than an inclusion list: the 国家
# column holds multi-country labels ("瑞典/丹麦", "荷兰/比利时/法国") that
# an exact-match inclusion test can never match, which is how those ten
# rows - several of them the highest-value pan-European groups - came to be
# stamped 范围外 and nailed to grade C. Listing only the labels we know are
# out keeps every correct judgement intact and fixes only the slash rows.
OUT_OF_SCOPE = {
    "中国（在欧销售）", "巴西", "澳大利亚", "智利", "日本", "泰国", "越南",
    "阿根廷", "厄瓜多尔", "秘鲁", "伊拉克", "多米尼加", "墨西哥", "埃及",
    "南非", "香港", "印尼", "马来西亚", "新加坡", "巴基斯坦",
}


TAIWAN_LABELS = {"台湾", "台灣", "Taiwan", "TW", "中国台湾"}


def is_taiwan_vendor(country, typ, name):
    """True only for the Taiwan vendor itself, never for its distributors.

    Decided from the row's own 国家/类型 fields. The 备注 column is
    deliberately not consulted: it records what an account *sells*, so a
    British or Greek PLANET distributor carries the word 台厂 while being
    exactly the kind of company we want to develop.
    """
    if country.strip() in TAIWAN_LABELS:
        return True
    if re.search(r'台厂|台湾', typ):
        return True
    return False


def in_scope(country):
    """True if the row is in the target region.

    Splits multi-country labels on "/" so "瑞典/丹麦" counts as in-scope.
    A row is out of scope only when EVERY part is out of scope.
    """
    parts = [p.strip() for p in re.split(r"[/、,，]", country) if p.strip()]
    if not parts:
        return True          # unknown country: don't silently bury the row
    return any(p not in OUT_OF_SCOPE for p in parts)


def direct_contact(s):
    """A named person's own address or a mobile number beats a generic inbox."""
    if not s:
        return False
    generic = re.search(r'\b(info|sales|support|office|contact|admin|service|shop'
                        r'|hello|technical|mikrotik|training|billing|facturacion)@', s, re.I)
    has_mail = '@' in s
    has_tel = bool(re.search(r'\d[\d\s().+-]{6,}', s))
    return (has_mail and not generic) or has_tel


def main():
    rows = list(csv.reader(open(CSV, encoding="utf-8-sig")))
    hdr, data = rows[0], rows[1:]
    if len(hdr) == 17:
        hdr.append("评级")
        hdr.append("评级依据")
        for r in data:
            r.extend(["", ""])

    cnt = Counter()
    for r in data:
        name, country, city, site = r[0], r[1], r[2], r[3]
        typ, signal, sku, contact, prio, note = r[4], r[5], r[8], r[9], r[10], r[16]
        # 切入角度(r[7])是我们要说的话，不是客户的信号，不能用来判断客户需求
        blob = " ".join([name, typ, signal, note])
        blob = re.sub(r'【[^】]*】', ' ', blob)
        blob = re.sub(r'→[^；。]*', ' ', blob)
        blob = re.sub(r'[★☆]+', ' ', blob)

        hits = [(key, label) for key, (pat, label) in NEED.items() if re.search(pat, blob)]
        needs = [label for _, label in hits]
        strong = [label for key, label in hits
                  if key in ("MTCSWE", "SWITCH", "POE", "HOTEL",
                             "INDUSTRIAL", "MULTICAST", "FIBRE")]
        hard_reasons = []
        if re.search(HARD_TYPE, typ):
            hard_reasons.append("类型属大盘/自有品牌（%s）" % typ)
        m = re.search(HARD_NOTE, blob)
        if m:
            hard_reasons.append("备注含「%s」" % m.group(0))
        if not in_scope(country):
            hard_reasons.append("区域外（%s），不在欧洲+美加范围内" % country)
        # A row is a Taiwan vendor only by its OWN identity. Never read this
        # out of the notes: notes describe what the account sells, so a UK
        # PLANET distributor legitimately carries "台厂 PLANET" in its 备注 -
        # matching that here marks the distributor as the Taiwan vendor and
        # buries it in C. Same self-read-back class as the 切入点/【待补】/→ bugs.
        if is_taiwan_vendor(country, typ, name):
            hard_reasons.append("台厂本体，非客户，仅作信号源")
        hard = bool(hard_reasons)

        # grade -------------------------------------------------------
        if hard:
            # report only the reasons that actually fired; a generic label
            # listing every possible cause is how "范围外" ended up attached
            # to Dutch and Swedish rows
            grade, why = "C", "；".join(hard_reasons) + "，决策链长或存在品牌冲突"
        elif prio in ("✕", "观察"):
            grade, why = "C", "竞品或观察对象，不作为客户开发"
        elif "【待补】" in note:
            # 需求未核实，不能算"重点且好跟进"，先验证再提级
            grade, why = "B", "三星依据仅为渠道等级，需求未核实，需先查证其是否已有工业/PoE 产品线"
        elif strong and direct_contact(contact) and prio.startswith("★★★"):
            grade = "A"
            why = "有明确交换/供电需求（%s），且有具体人直联" % "、".join(strong[:3])
        elif strong and prio.startswith("★★★"):
            grade = "A"
            why = "有明确交换/供电需求（%s），三星重点" % "、".join(strong[:3])
        elif strong or (needs and prio.startswith("★★★")):
            grade = "B"
            why = "有信号（%s）但需先验证需求或联系人不具体" % ("、".join(needs[:3]) or "渠道等级")
        elif re.search(WEAK, signal.strip()):
            grade, why = "B", "以路由/用户管理为主，交换需求弱，需先教育"
        else:
            grade, why = "B", "通用分销商信号，无差异化切入点，慢慢跟"

        r[17], r[18] = grade, why
        cnt[grade] += 1

    # ── 下放规则（2026-09-23 用户指定，非评级标准改动）───────────────────
    # 用户口径：A 重点跟进；B **只做群发**；没价值群发的直接沉 C。
    # 因此 B 若「连邮箱都没有」→ 群发触达不到 → 沉 C 待命（全量信息仍然保留）。
    # 用户 2026-09-23 定稿口径：B **只做群发**，因此「有邮箱 → 留 B；没邮箱 → 沉 C」，
    # 集成商型也不例外（有电话但没邮箱的，群发同样触达不到）。
    MAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]{2,}")
    INT = re.compile(r"集成商|顾问|Consultant|Integrator|工程|服务", re.I)
    demoted = 0
    for r in data:
        if r[17] != "B":
            continue
        if MAIL.search(" ".join([r[9], r[16], r[3], r[0]])):
            continue          # 有邮箱 → 群发得到，留 B
        r[17] = "C"
        r[18] = ("【2026-09-23 复核下放】无邮箱（群发触达不到），按「B 只做群发」原则沉 C 待命；"
                 "全量信息保留，出现以下任一情形可重评：①补到邮箱 ②对方主动询价 "
                 "③出现 EOL 替换需求 ④冒出内部联系人。原判：" + r[18])
        demoted += 1
    if demoted:
        cnt["B"] -= demoted
        cnt["C"] += demoted
        print("下放 B→C（无邮箱且非集成商型，群发触达不到）: %d 家" % demoted)

    # ── C 级细分归类（2026-09-23 用户要求：C 里要能区分是 too hard 还是 B 下放还是别的原因）
    SUBCOL = hdr.index("C级细分")
    SCALE = re.compile(r"大分销|跨国|覆盖\s*\d|大型|最大|全国性|\d+\s*个分部|"
                       r"(?<![\d.])8000|(?<![\d.])1M\b|100\s*万|集团|上市")
    def sub(r):
        why = r[18]
        if "复核下放" in why or "群发触达不到" in why:
            return "B下放·无邮箱（群发触达不到）"
        if "范围外" in why or "区域外" in why:
            return "范围外（非欧洲/北美）"
        if "竞品" in why:
            return "竞品"
        if "自有品牌" in why:
            return "太难·自有品牌"
        if SCALE.search(why + " " + r[16]):
            return "太难·规模过大/决策链长"
        return "其他"
    subc = Counter()
    for r in data:
        if r[17] == "C":
            r[SUBCOL] = sub(r); subc[r[SUBCOL]] += 1
        else:
            r[SUBCOL] = ""
    if subc:
        print("C 级细分:", dict(subc))

    with open(CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(hdr)
        w.writerows(data)

    print("评级分布:", dict(cnt), "总计", len(data))
    a = [r for r in data if r[17] == "A"]
    print("\nA 级按国家:", dict(Counter(r[1] for r in a).most_common(12)))
    print("\nA 级样例(前12):")
    for r in a[:12]:
        print("  %s | %s | %s" % (r[0][:34], r[1], r[18][:40]))


if __name__ == "__main__":
    main()
