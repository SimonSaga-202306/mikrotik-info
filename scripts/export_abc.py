#!/usr/bin/env python3
"""Export the graded list as a working workbook, one sheet per grade.

The A sheet is meant to be worked from day to day, so it carries the
per-account play plus blank columns for the user to fill in as they go.
"""
import csv, re, sys, os
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from strategy import PLAY, NEED_PAT, ORDER, scenarios  # noqa: E402

CSV = "客户名单_反向信号_2026-09.csv"
OUT = "客户分级跟进表_2026-09.xlsx"

BLANK = ["", "", ""]          # 首次触达日 / 客户反馈 / 下一步动作
BLANK_HDR = ["首次触达日", "客户反馈", "下一步动作"]
EMPTY_HDR = ["首次触达日", "客户反馈", "下一步动作"]

SCEN_LABEL = {
    "POE": "PoE/监控/门禁", "HOTEL": "酒店/多住户", "MULTICAST": "组播/IPTV",
    "INDUSTRIAL": "工业/楼宇", "CAMPUS": "校园/教育", "FIBRE": "光纤接入",
    "SWITCH": "交换专长", "MTCSWE": "MTCSWE 交换认证", "ISP": "ISP/骨干",
    "INFLUENCE": "影响力/渠道",
}


def main():
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter

    rows = list(csv.reader(open(CSV, encoding="utf-8-sig")))
    hdr, data = rows[0], rows[1:]

    wb = Workbook()
    wb.remove(wb.active)
    hdr_fill = PatternFill("solid", fgColor="1F4E78")
    a_fill = PatternFill("solid", fgColor="FCE4D6")
    b_fill = PatternFill("solid", fgColor="FFF2CC")
    c_fill = PatternFill("solid", fgColor="E2EFDA")
    inp_fill = PatternFill("solid", fgColor="FFFDE7")
    thin = Side(style="thin", color="BFBFBF")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    def sheet(title, head, body, fill, widths):
        ws = wb.create_sheet(title)
        ws.append(head)
        for r in body:
            ws.append(r)
        for c in ws[1]:
            c.font = Font(bold=True, color="FFFFFF", size=10)
            c.fill = hdr_fill
            c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        # mark the blank input columns
        for col_name in BLANK_HDR:
            if col_name in head:
                i = head.index(col_name) + 1
                ws.cell(row=1, column=i).fill = PatternFill("solid", fgColor="C00000")
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
            for c in row:
                c.alignment = Alignment(wrap_text=True, vertical="top")
                c.border = border
        for i, wd in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = wd
        ws.freeze_panes = "B2"
        ws.auto_filter.ref = "A1:%s%d" % (get_column_letter(len(head)), ws.max_row)
        return ws

    # ---------------- A ----------------
    head_a = (hdr + ["场景", "推荐型号", "核心卖点", "怎么开发", "风险点"]
              + EMPTY_HDR)
    body_a = []
    for r in data:
        if r[17] != "A":
            continue
        blob = " ".join([r[0], r[4], r[5], r[16]])
        sc = scenarios(blob)
        key = sc[0] if sc else None
        if key:
            sku, sell, dev, risk = PLAY[key]
            scen = SCEN_LABEL[key]
        else:
            sku, sell, dev, risk = ("LT-S8328G-4XS24GT-S", "通用接入",
                                    "先问清接入层现用设备与痛点再定型号",
                                    "需求信号不明确，别急着报价")
            scen = "待摸底"
        body_a.append(list(r) + [scen, sku, sell, dev, risk] + BLANK)
    ws_a = sheet("A级-重点好跟进", head_a, body_a, a_fill,
                 [30, 12, 14, 22, 16, 30, 10, 26, 22, 26, 8, 10, 12, 12, 12, 12, 34, 6, 34,
                  14, 26, 40, 46, 46, 12, 26, 26])

    # ---------------- B ----------------
    B_PLAY = {
        "MTCSWE": "交换是正式专长，先用技术资料建立信任，等他有项目再报价",
        "SWITCH": "有交换能力，发 CLI/MIB 文档和实测数据，不谈价格",
        "POE": "先问他在做什么监控项目、多大功率，用小批量试单切入",
        "INDUSTRIAL": "发工业线资料（宽温/导轨/ERPS），问现场工况和认证要求",
        "HOTEL": "问有没有在建酒店项目，酒店是多期的，先做一期",
        "MULTICAST": "问 IPTV 或监控组播有没有踩过坑，用小范围验证切入",
        "FIBRE": "问 FTTH 项目规模和上行收敛，算单端口成本",
        "CAMPUS": "摸清是否属教育局/政府集采，寒暑假是施工窗口",
        "ISP": "先小批量试用跑稳定性，备件与 RMA 承诺是关键",
        "INFLUENCE": "寄样机+可讲的案例，让他讲课时用；不谈返点",
    }
    head_b = hdr + ["场景", "建议打法"] + EMPTY_HDR
    body_b = []
    for r in data:
        if r[17] != "B":
            continue
        blob = " ".join([r[0], r[4], r[5], r[16]])
        sc = scenarios(blob)
        key = sc[0] if sc else None
        body_b.append(list(r) + [SCEN_LABEL.get(key, "待摸底"),
                                 B_PLAY.get(key, "保持低频联系，等他出现交换机需求信号再跟进")]
                      + BLANK)
    ws_b = sheet("B级-慢慢跟", head_b, body_b, b_fill,
                 [30, 12, 14, 22, 16, 30, 10, 26, 22, 26, 8, 10, 12, 12, 12, 12, 34, 6, 34,
                  14, 24, 14, 40, 12, 26, 26])

    # ---------------- C ----------------
    head_c = hdr + ["C级细分", "难在哪", "可能的切口"] + EMPTY_HDR
    body_c = []
    for r in data:
        if r[17] != "C":
            continue
        sub = r[hdr.index("C级细分")] if "C级细分" in hdr else ""
        blob = " ".join([r[0], r[4], r[16]])
        if sub.startswith("B下放"):
            why = "B 级下放：无邮箱，群发触达不到"
            cut = ("补到邮箱 / 对方主动询价 / 出现 EOL 替换需求 / 冒出内部联系人 —— "
                   "任一成立即捞回 B 重评")
        elif sub.startswith("范围外"):
            why = "不在目标区域（欧洲+美加）内"
            cut = "留档，等有当地伙伴或客户指定时再动"
        elif re.search(r'竞品|品牌（竞品）|台厂|台湾', blob):
            why = "竞品或台厂，存在品牌冲突"
            cut = "不开发，只作为价格与功能情报来源"
        elif re.search(r'自有品牌', blob):
            why = "自有品牌制造商/分销，会护自己的产品线"
            cut = "只在其自有线缺规格（如 PoE++/宽温）时，以补位身份谈"
        else:
            why = "集团/大公司，决策链长，采购集中"
            cut = "先问清是国别决策还是集团统一采购；找准品类经理而非 CPO"
        body_c.append(list(r) + [sub, why, cut] + BLANK)
    ws_c = sheet("C级-难啃", head_c, body_c, c_fill,
                 [30, 12, 14, 22, 16, 30, 10, 26, 22, 26, 8, 10, 12, 12, 12, 12, 34, 6, 34,
                  34, 40, 12, 26, 26])

    # ---------------- 说明 ----------------
    ws_n = wb.create_sheet("说明-评级口径与打法")
    notes = [
        ["客户分级跟进表　2026-09", ""],
        ["", ""],
        ["评级口径", ""],
        ["A 级", "有明确需求信号（交换专长 / PoE / 工业 / 酒店 / 组播）且好跟进：有具体对接人、决策链短、不用过总部采购。优先开发。"],
        ["B 级", "有信号但需验证，或只做路由/Hotspot（交换需求弱），或联系人不具体。低频维护，等需求信号出现再转 A。"],
        ["C 级", "大公司 / 大集团 / 自有品牌 / 竞品 / 区域外。先摸清决策层级再动，或只作情报来源。"],
        ["", ""],
        ["评级时特意排除了两处自欺", ""],
        ["1", "「切入角度」列是我们自己的模板话术（如『卖 MikroTik 但缺工业/ERPS/PoE++』），不是客户需求信号，不参与评级——否则 246 家分销商会全部误判为 A。"],
        ["2", "三星但备注为「【待补】」的行，需求未经核实，一律降为 B，不装成研究过。"],
        ["", ""],
        ["场景打法速查", ""],
    ]
    for k in ORDER:
        sku, sell, dev, risk = PLAY[k]
        notes.append([SCEN_LABEL[k], "推 %s｜开口：%s｜风险：%s" % (sku, dev, risk)])
    notes += [
        ["", ""],
        ["通用红线", ""],
        ["1", "包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号——硬要求。"],
        ["2", "台湾厂商不是客户，只是信号源，不开发。"],
        ["3", "PoE 功率与工业温宽是最容易当场翻车的两项，任何口头承诺都要落到实测数据。"],
        ["4", "大集团先问清采购层级：国别决策还是集团统一采购（Senetic 七国、Rexel 三国、OEM Automatic 三国）。"],
        ["5", "样机先送测再谈价格；价格战是最后一张牌。"],
        ["", ""],
        ["怎么用它跟进", ""],
        ["跟进记录", "用户线下维护；只有用户提供实际回复并要求时才入库。历史空白列保留，不要求填写。"],
        ["证据索引", "docs/evidence/客户溯源_A.md、客户溯源_B.md、客户溯源_C.md；按档案编号定位字段来源和缺证。"],
        ["证据边界", "公开邮箱不等于可投递或采购权限；模板卖点/评级是内部分析，不能替代逐SKU参数实证。"],
        ["筛选", "每张表首行已开自动筛选，可按国家、场景、评级依据快速过滤。"],
    ]
    for row in notes:
        ws_n.append(row)
    ws_n.column_dimensions["A"].width = 24
    ws_n.column_dimensions["B"].width = 118
    for row in ws_n.iter_rows(min_row=1, max_row=ws_n.max_row):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
        if row[0].value and row[1].value == "":
            row[0].font = Font(bold=True, size=11, color="1F4E78")
    ws_n["A1"].font = Font(bold=True, size=14, color="1F4E78")

    wb.save(OUT)
    print("written", OUT)
    print("A", ws_a.max_row - 1, "| B", ws_b.max_row - 1, "| C", ws_c.max_row - 1)
    print("A 级场景分布:", dict(Counter(r[-8] for r in body_a)))


if __name__ == "__main__":
    main()
