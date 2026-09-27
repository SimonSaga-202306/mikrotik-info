#!/usr/bin/env python3
"""Generate one markdown dossier per customer under profile/.

Each dossier carries the grade, what the company is, the people and
their direct lines, the brands in play, the follow-up play, the risks,
and an empty log that gets filled in as outreach happens.
"""
import csv, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from strategy import PLAY, NEED_PAT, ORDER, scenarios  # noqa: E402

CSV = "客户名单_反向信号_2026-09.csv"
DIR = "profile"

SCEN_LABEL = {
    "POE": "PoE / 监控 / 门禁", "HOTEL": "酒店 / 多住户", "MULTICAST": "组播 / IPTV",
    "INDUSTRIAL": "工业 / 楼宇自控", "CAMPUS": "校园 / 教育", "FIBRE": "光纤接入 / FTTH",
    "SWITCH": "交换专长", "MTCSWE": "MTCSWE 交换认证", "ISP": "ISP / 骨干",
    "INFLUENCE": "影响力 / 渠道",
}
B_PLAY = {
    "MTCSWE": "交换是正式专长。先发技术资料（CLI / MIB / 转发实测）建立信任，等他手上有项目再报价。",
    "SWITCH": "有交换能力。给文档和实测数据，不谈价格；等他出现具体项目信号再提级。",
    "POE": "先问他在做什么监控项目、单口要多大功率，用小批量试单切入。",
    "INDUSTRIAL": "发工业线资料（宽温 / 导轨 / ERPS），问现场工况和认证要求，缺认证就别浪费时间。",
    "HOTEL": "问有没有在建酒店项目。酒店是多期的，先做一期，后面几期跟着走。",
    "MULTICAST": "问 IPTV 或监控组播有没有踩过坑（泛洪、花屏），用小范围验证切入。",
    "FIBRE": "问 FTTH 项目规模和上行收敛比，把单端口成本摊到每个用户给他看。",
    "CAMPUS": "摸清是否属教育局 / 政府集采，寒暑假是施工窗口，提前一个季度谈。",
    "ISP": "先小批量试用跑稳定性。备件与 RMA 响应速度比价格更影响成交。",
    "INFLUENCE": "寄样机 + 可公开讲的案例，让他讲课时用。不谈返点，谈「你能多讲什么内容」。",
}

BRANDS = ["MikroTik", "Cisco", "CCIE", "Ubiquiti", "HP ", "Aruba", "Netgear", "TP-Link",
          "D-Link", "HPE", "Juniper", "Arista", "Ruckus", "Cambium", "Teltonika",
          "Westermo", "ORing", "Antaira", "Moxa", "Korenix", "Red Lion", "N-Tron",
          "ComNet", "Advantech", "Fortinet", "Sophos", "pfSense", "Proxmox",
          "Audinate", "Dante", "KNX", "SimRush", "100MEGA", "i4wifi", "LinITX",
          "RouterBOARD", "SwitchOS", "RouterOS", "The Dude", "CAPsMAN", "RoMON",
          "LibreNMS", "Asterisk", "WireGuard", "IPsec"]

CERTS = ["MTCNA", "MTCRE", "MTCWE", "MTCTCE", "MTCUME", "MTCINE", "MTCIPv6E", "MTCSE",
         "MTCSWE", "MTCEWE"]
CERT_DESC = {
    "MTCNA": "网络助理（入门）", "MTCRE": "路由", "MTCWE": "无线",
    "MTCTCE": "流量控制", "MTCUME": "用户管理（Hotspot / PPPoE）",
    "MTCINE": "ISP 互联", "MTCIPv6E": "IPv6", "MTCSE": "安全",
    "MTCSWE": "**交换**（最能说明他卖交换机）", "MTCEWE": "企业无线",
}


def safe(name):
    s = re.sub(r'[\\/:*?"<>|]+', '-', name).strip().strip('.')
    return (s[:60] or "unnamed")


def emails(text):
    return re.findall(r'[\w.+-]+@[\w.-]+\.\w+', text)


def phones(text):
    out = []
    for m in re.findall(r'(?:\+\d[\d\s().-]{6,}|\d[\d\s().-]{7,})', text):
        m = m.strip().strip('.,;')
        if sum(c.isdigit() for c in m) >= 7:
            out.append(re.sub(r'\s+', ' ', m))
    return out


FILLED_RE = re.compile(r'^\|\s*\d{4}-\d{2}-\d{2}\s*\|', re.M)


def _clear_stale_dossiers():
    """Remove old dossiers before regenerating.

    Dossier filenames embed a sequence number that shifts whenever rows are
    added or regraded, so without this a single new account leaves behind
    dozens of orphaned copies of the same company (e.g. B-468 and B-470 both
    being RIDMONT D.O.O).

    SAFETY: refuse to delete anything if a dossier's 跟进记录 table already
    holds hand-entered rows (a dated row written by the user after outreach).
    Those notes are not reproducible from the CSV and must be preserved.
    """
    if not os.path.isdir(DIR):
        return
    stale = [f for f in os.listdir(DIR) if f.endswith(".md") and f != "00-索引.md"]
    if not stale:
        return
    guarded = []
    for f in stale:
        try:
            txt = open(os.path.join(DIR, f), encoding="utf-8").read()
        except OSError:
            continue
        if FILLED_RE.search(txt):
            guarded.append(f)
    if guarded:
        raise SystemExit(
            "❌ 拒绝重建 profile/：以下档案的「跟进记录」已填入手工内容，\n"
            "   删除会丢失不可再生的信息。请先手工备份或确认后处理：\n   "
            + "\n   ".join(guarded[:20])
            + ("\n   ..." if len(guarded) > 20 else "")
        )
    for f in stale:
        os.remove(os.path.join(DIR, f))
    print("cleared %d stale dossiers from %s/" % (len(stale), DIR))


def main():
    rows = list(csv.reader(open(CSV, encoding="utf-8-sig")))
    hdr, data = rows[0], rows[1:]
    os.makedirs(DIR, exist_ok=True)
    _clear_stale_dossiers()

    # pull sibling links out of the notes written by the audit pass
    siblings = {}
    for r in data:
        m = re.search(r'【关联】同集团另一实体：(.+?)（([\w.-]+)）', r[16])
        if m:
            siblings[r[0]] = m.group(1)

    order = {"A": 0, "B": 1, "C": 2}
    data.sort(key=lambda r: (order.get(r[17], 9), r[1], r[0]))
    idx = defaultdict(int)
    made = []

    for r in data:
        name, country, city, site = r[0], r[1], r[2], r[3]
        typ, signal, ownbrand, angle, sku = r[4], r[5], r[6], r[7], r[8]
        contact, prio, status, src = r[9], r[10], r[11], r[12]
        note, grade, why = r[16], r[17], r[18]

        idx[grade] += 1
        code = "%s-%03d" % (grade, idx[grade])
        fname = "%s-%s-%s.md" % (code, safe(name), safe(country))
        path = os.path.join(DIR, fname)

        blob = " ".join([name, typ, signal, note])
        sc = scenarios(blob)
        key = sc[0] if sc else None

        # people -------------------------------------------------
        person = ""
        if " / " in name:
            person, company = name.split(" / ", 1)
        else:
            company = name
        mails = emails(contact + " " + note)
        tels = phones(contact)

        # brands -------------------------------------------------
        brands = sorted({b.strip() for b in BRANDS if b.lower() in (blob + " " + signal).lower()})
        certs = [c for c in CERTS if re.search(c, signal)]

        L = []
        w = L.append
        w("# %s" % name)
        w("")
        w("> **评级 %s**　|　%s%s　|　档案编号 `%s`　|　优先级 %s　|　状态：%s"
          % (grade, country, " · " + city if city else "", code, prio, status))
        w("")
        w("---")
        w("")

        # 1 grade
        w("## 一、评级与结论")
        w("")
        w("- **评级**：%s" % {"A": "A　**Yes** —— 明显该做，直接投入精力",
                            "B": "B　**Maybe** —— 不太明显，慢跟待验证",
                            "C": "C　**Too hard** —— 太难（大公司 / 集团 / 自有品牌 / 竞品 / 区域外），**先放着不动，精力只给 A**"}[grade])
        w("- **评级依据**：%s" % why)
        w("- **下次复核**：收到反馈后重新评级")
        w("")

        # 2 company
        w("## 二、公司概览")
        w("")
        w("| 项 | 内容 |")
        w("|---|---|")
        w("| 公司名 | %s |" % company)
        w("| 国家 | %s |" % country)
        w("| 城市 | %s |" % (city or "—"))
        w("| 网站 | %s |" % (site or "—"))
        w("| 类型 | %s |" % typ)
        w("| 反向信号 | %s |" % signal)
        w("| 是否自有品牌 | %s |" % (ownbrand or "—"))
        w("| 首推 SmartByte 型号 | %s |" % (sku or "—"))
        w("| 切入点 | %s |" % (angle or "—"))
        w("| 数据来源 | %s |" % (src or "—"))
        w("| 原备注 | %s |" % (note or "—"))
        w("")

        # 3 people
        w("## 三、人员与联系方式")
        w("")
        if person:
            w("- **对接人**：%s" % person)
        w("- **邮箱**：%s" % ("、".join(dict.fromkeys(mails)) if mails else "—"))
        w("- **电话**：%s" % ("、".join(dict.fromkeys(tels)) if tels else "—"))
        w("- **原始联系字段**：%s" % (contact or "—"))
        extra = [m for m in emails(note) if m not in mails]
        if extra:
            w("- **备注中出现的其他邮箱**：%s" % "、".join(dict.fromkeys(extra)))
        w("")

        # 4 brands
        w("## 四、品牌与技术栈")
        w("")
        if certs:
            w("**持有认证**：%s" % "、".join(certs))
            w("")
            for c in certs:
                w("- `%s` — %s" % (c, CERT_DESC.get(c, "")))
            w("")
        if brands:
            w("**涉及品牌 / 技术**：%s" % "、".join(brands))
        else:
            w("**涉及品牌 / 技术**：（未记录）")
        w("")

        # 5 strategy
        w("## 五、跟进策略")
        w("")
        if grade == "A" and key:
            psku, sell, dev, risk = PLAY[key]
            w("**场景判断**：%s" % SCEN_LABEL[key])
            w("")
            w("### 推什么型号")
            w("")
            w("**%s**" % psku)
            w("")
            w("> 系统初判型号：`%s`（供参考，以实际沟通为准）" % sku)
            w("")
            w("### 核心卖点")
            w("")
            w(sell)
            w("")
            w("### 怎么开发")
            w("")
            w(dev)
            w("")
            w("### 风险点")
            w("")
            w(risk)
        elif grade == "A":
            w("场景信号不明确，先摸底：问清他接入层现在用谁的设备、痛点是供电、VLAN 还是环网，再定型号。")
            w("")
            w("初判可参考型号：`%s`" % sku)
        elif grade == "B":
            w("**场景**：%s" % SCEN_LABEL.get(key, "待摸底"))
            w("")
            w(B_PLAY.get(key, "保持低频联系，等他出现交换机需求信号再提级为 A。"))
            w("")
            w("参考型号：`%s`" % sku)
        else:
            if "范围外" in note:
                w("不在目标区域（欧洲 + 美加）内，**暂不触达**，留档备用。")
            elif re.search(r'竞品|台厂|台湾', blob):
                w("属竞品或台厂，**不作为客户开发**，只作价格与功能情报来源（台厂是信号源，不是客户）。")
            elif re.search(r'自有品牌', blob):
                w("自有品牌厂商，会护自己的产品线。**只在其自有线缺规格（PoE++ / 宽温 / ERPS）时，以补位身份谈**。")
            else:
                w("集团 / 大公司，决策链长、采购集中。")
                w("")
                w("**切口**：先问清是国别决策还是集团统一采购；**找品类经理，不要找 CPO**。")
        if grade == "C":
            w("")
            w("> ⛔ **Too hard pile**：本条进「太难」堆，**当前不投入跟进精力**，不必为它写开发信或做方案。")
            w("> 信息已**全量留档**（本档案 + 总表 19 列），待出现明确触发条件再捞出来重评：")
            w("> ① 对方主动询价；② 出现停产替换需求；③ 我方补齐对应认证；④ 你从别处拿到其内部人线索。")
        w("")

        # 6 cautions
        w("## 六、注意点")
        w("")
        w("**通用红线（所有客户适用）**")
        w("")
        w("1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。")
        w("2. **台厂不是客户**，只是信号源。")
        w("3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。")
        w("4. 大集团先问清采购层级（国别 vs 集团统一）。")
        w("5. 样机先送测，再谈价格。")
        w("")
        if "范围外" in note:
            w("- ⚠️ 本客户**在目标区域外**，跟进前先确认是否值得破例。")
        if re.search(r'TAA|NDAA', note):
            w("- ⚠️ **中国产地受限**：不能做 TAA / NDAA 政府与电力项目，只能谈商业渠道。")
        if siblings.get(name):
            w("- 🔗 **同集团**：%s — 别两边同时报价，先问清决策层级。" % siblings[name])
        w("")

        # 7 first-contact email (A tier only — these are the ones being worked now)
        if grade == "A":
            from emails import build
            subject, body = build(name, person, country, city, key, sku, note)
            w("## 七、首触邮件（可直接发送）")
            w("")
            w("**主题**：%s" % subject)
            w("")
            w("```text")
            w(body)
            w("```")
            w("")
            w("> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；"
              "③ 落款换成你自己的名字与公司；④ 一次只问一个问题。")
            w("")

        # 8 log
        w("## %s、跟进记录" % ("八" if grade == "A" else "七"))
        w("")
        w("| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |")
        w("|---|---|---|---|---|")
        w("|  |  |  |  |  |")
        w("")
        w("<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->")
        w("")
        w("---")
        w("")
        w("*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*")

        open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")
        made.append((code, name, country, fname))

    # index
    idx_lines = ["# 客户档案索引（profile/）", "",
                 "共 **%d** 份档案，按评级分组。文件名格式：`评级-序号-公司名-国家.md`" % len(made),
                 "", "评级含义：", "",
                 "- **A**　重点且好跟进：有明确需求信号 + 具体对接人 + 决策链短",
                 "- **B**　慢慢跟：信号待验证，或交换需求弱",
                 "- **C**　难啃：大公司 / 集团 / 自有品牌 / 竞品 / 区域外", "",
                 "每份档案含：评级与结论 · 公司概览 · 人员与联系方式 · 品牌与技术栈 · 跟进策略 · 注意点 · 跟进记录（待填）",
                 "", "---", ""]
    cur = None
    for code, name, country, fname in made:
        if code[0] != cur:
            cur = code[0]
            idx_lines.append("## %s 级（%d 家）" % (cur, sum(1 for m in made if m[0][0] == cur)))
            idx_lines.append("")
        # wrap the destination in <...>: company names contain parentheses
        # (e.g. "TME (Transfer Multisort Elektronik)"), and a bare
        # [x](file (a).md) link terminates at the first ")" -> broken link.
        idx_lines.append("- [`%s`](<%s>)　%s · %s" % (code, fname, name, country))
    idx_lines.append("")
    open(os.path.join(DIR, "00-索引.md"), "w", encoding="utf-8").write("\n".join(idx_lines))

    print("generated %d dossiers in %s/" % (len(made), DIR))
    print(dict((g, sum(1 for m in made if m[0][0] == g)) for g in "ABC"))


if __name__ == "__main__":
    main()
