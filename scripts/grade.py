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
    "POE":         (r'PoE|POE|CCTV|视频监控|摄像头|门禁|报警|对讲|Dante', "PoE/监控/门禁"),
    "HOTEL":       (r'酒店|Hospitality|hospitality|多住户|MDU|公寓|强制门户|Captive', "酒店/多住户"),
    "INDUSTRIAL":  (r'工业|IT/OT|IT-OT|BMS|楼宇自控|电网|制造|仓库|农业|能源', "工业/楼宇"),
    "MULTICAST":   (r'组播|Multicast|multicast|IPTV|PIM-SM',   "组播/IPTV"),
    "FIBRE":       (r'FTTH|GPON|光纤|Glasfaser|FTTC|xDSL|DOCSIS', "光纤接入"),
    "ISP":         (r'WISP|ISP|运营商|骨干|backbone|BGP',        "ISP/骨干"),
    "CAMPUS":      (r'校园|学区|教育|学校|学院|Campus',            "校园/教育"),
    "INFLUENCE":   (r'讲师|培训|学院|Academy|academy|培训中心|大会|MUM|产品经理|售前', "影响力/渠道"),
}
# weak on its own: routing or user-management specialists
WEAK = r'^MTCNA(\+MTCRE)?(\+MTCWE)?(\+MTCUME)?(\+MTCIPv6E)?$'

HARD_TYPE = r'大分销|Master\+VAD|自有品牌|品牌（竞品）|竞品|台厂|工控二手'
HARD_NOTE = (r'Fortune|财富 ?500|上市|全国性|市政|IBEX35|集团|'
             r'全球最大|北美领先|全国性 ISP|NS ?万|100 ?万|8000|1M|'
             # 规模信号：多分部、跨州/跨国覆盖、自称大型/最大/领先
             r'大型|最大|领先|\d+ ?\+ ?州|\d+ ?个分部|覆盖 \d+|跨国|'
             r'官方分销之一|one of the largest|leading|nationwide|'
             # 规模别称常写在备注里而非类型列
             r'大分销|老牌|巨头|electrical distribution')


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

        hits = [(key, label) for key, (pat, label) in NEED.items() if re.search(pat, blob)]
        needs = [label for _, label in hits]
        strong = [label for key, label in hits
                  if key in ("MTCSWE", "SWITCH", "POE", "HOTEL",
                             "INDUSTRIAL", "MULTICAST", "FIBRE")]
        hard = (re.search(HARD_TYPE, typ) or re.search(HARD_NOTE, blob)
                or "范围外" in note or re.search(r'台湾|台厂', blob))

        # grade -------------------------------------------------------
        if hard:
            grade, why = "C", "集团/大公司/自有品牌/竞品/范围外，决策链长或存在品牌冲突"
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
