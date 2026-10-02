#!/usr/bin/env python3
"""Apply the fixes surfaced by the audit.

1.  Normalise the 澳洲 / 澳大利亚 country label.
2.  Merge the two Clayton Engineering rows (same US company, two domains).
3.  Merge the overlapping Rexel row into its country entities.
4.  Cross-reference the nine genuine multi-country groups.
5.  Give the 40 unexplained three-star rows an honest note.
6.  Flag rows that fall outside the Europe + North America scope.
"""
import csv, re

CSV = "客户名单_反向信号_2026-09.csv"
SCOPE = {"英国", "爱尔兰", "法国", "德国", "意大利", "西班牙", "葡萄牙", "荷兰", "比利时",
         "卢森堡", "瑞士", "奥地利", "波兰", "捷克", "斯洛伐克", "匈牙利", "罗马尼亚",
         "保加利亚", "希腊", "克罗地亚", "斯洛文尼亚", "塞尔维亚", "波黑", "黑山",
         "北马其顿", "阿尔巴尼亚", "科索沃", "爱沙尼亚", "拉脱维亚", "立陶宛", "芬兰",
         "瑞典", "挪威", "丹麦", "冰岛", "马耳他", "塞浦路斯", "乌克兰", "摩尔多瓦",
         "美国", "加拿大", "土耳其", "格鲁吉亚", "以色列", "阿联酋"}

GROUPS = {
    "labotest.se": ("labotest.fi", "LaboTest AB（瑞典/丹麦）"),
    "labotest.fi": ("labotest.se", "LaboTest Oy（芬兰）"),
    "alidex.it": ("alidex.es", "ALIDEX IBERIA（西班牙/葡萄牙）"),
    "alidex.es": ("alidex.it", "ALIDEX ITALIA（意大利）"),
    "ispsupplies.com": ("ispsupplies.ca", "ISP Supplies Canada（MBSI WAV）"),
    "ispsupplies.ca": ("ispsupplies.com", "ISP Supplies（美国，powered by WAV）"),
    "oemautomatic.pl": ("oemautomatic.se", "OEM Automatic AB（瑞典）"),
    "oemautomatic.se": ("oemautomatic.pl", "OEM AUTOMATIC Sp. z o.o.（波兰）"),
    "oemautomatic.cz": ("oemautomatic.pl", "OEM AUTOMATIC Sp. z o.o.（波兰）"),
    "rbt-technologies.si": ("rbt-technologies.rs", "RBT Technologies Srbija（塞尔维亚）"),
    "rbt-technologies.rs": ("rbt-technologies.hr", "RBT Technologies Hrvatska（克罗地亚）"),
    "rbt-technologies.hr": ("rbt-technologies.si", "RBT Technologies d.o.o.（斯洛文尼亚）"),
    "wifi-stock.co.uk": ("wifi-stock.com", "WiFi-Stock.com（JSC Katalita，立陶宛）"),
    "wifi-stock.com": ("wifi-stock.co.uk", "Wifi Stock (UK) Ltd"),
    "tempelgroup.pt": ("tempelgroup.com", "Tempel Group（西班牙）"),
    "tempelgroup.com": ("tempelgroup.pt", "Tempel Group（葡萄牙）"),
}
SENETIC = ("senetic.de", "Senetic（同集团另有 pl / co.uk / fr / it / ch / se 站点，"
           "一国的采购决策可能由集团统一，谈一家等于谈七国）")


def main():
    rows = list(csv.reader(open(CSV, encoding="utf-8-sig")))
    hdr, data = rows[0], rows[1:]
    merged = fixed_geo = noted = flagged = linked = 0

    # 1 + 2: country label, and merge the duplicate Clayton rows
    clayton = [r for r in data if r[0].startswith("Clayton Engineering")]
    if len(clayton) == 2:
        keep, drop = (clayton[0], clayton[1]) if clayton[0][3] else (clayton[1], clayton[0])
        keep[3] = " / ".join(x for x in (keep[3], drop[3]) if x)
        keep[16] = ("两条重复记录已合并（同一家美国公司，两个域名 claytonengineering.com 与 clayeng.net）"
                    + ("；" + keep[16] if keep[16] else ""))
        data.remove(drop)
        merged += 1

    # 3: Rexel — drop the overlapping multi-country row, keep country entities
    rexel_multi = [r for r in data if r[0] == "Rexel"]
    rexel_it = [r for r in data if r[0] == "Rexel Italia"]
    if rexel_multi and rexel_it:
        rexel_it[0][16] = ("Rexel 集团意大利实体；集团为全球电气分销巨头，"
                           "另有 Rexel USA（rexelusa.com）。原「法国/意大利」合并行已并入此行与法国实体"
                           + ("；" + rexel_it[0][16] if rexel_it[0][16] else ""))
        data.remove(rexel_multi[0])
        merged += 1

    for r in data:
        site = r[3].split('/')[0].strip().lower()

        # 1: normalise country label
        if r[1] == "澳洲":
            r[1] = "澳大利亚"
            fixed_geo += 1

        # 4: cross-reference groups
        if site in GROUPS:
            other, label = GROUPS[site]
            r[16] = (r[16] + " " if r[16] else "") + "【关联】同集团另一实体：" + label + "（" + other + "）"
            linked += 1
        elif site.startswith("senetic."):
            r[16] = (r[16] + " " if r[16] else "") + "【关联】" + SENETIC[1]
            linked += 1

        # 5: unexplained three-star rows
        if r[10] == "★★★" and not r[16].strip():
            r[16] = ("【待补】本行由分销商名录批量导入，三星依据仅为渠道等级（%s）与「%s」，"
                     "尚无人工核实。建议先查证其是否已有工业交换机 / PoE++ 产品线，再定切入型号"
                     % (r[4], r[5]))
            noted += 1

        # 6: out of scope
        if r[1] not in SCOPE and "欧洲+美加范围外" not in r[16]:
            r[16] = (r[16] + " " if r[16] else "") + \
                "【范围外】不在本次目标区域（欧洲+美加）内，暂不触达，留档备用"
            flagged += 1

    with open(CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(hdr)
        w.writerows(data)

    print("merged duplicate rows:", merged)
    print("country labels fixed:", fixed_geo)
    print("cross-references added:", linked)
    print("unexplained stars annotated:", noted)
    print("out-of-scope rows flagged:", flagged)
    print("total rows:", len(data))


if __name__ == "__main__":
    main()
