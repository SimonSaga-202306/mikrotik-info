#!/usr/bin/env python3
"""Generate one markdown dossier per customer under profile/.

Each dossier carries the grade, what the company is, the people and
their direct lines, the brands in play, the follow-up play, the risks,
and an empty log that gets filled in as outreach happens.
"""
import csv, json, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from strategy import PLAY, NEED_PAT, ORDER, scenarios  # noqa: E402
from numbering import renumber, audit  # noqa: E402

CSV = "客户名单_反向信号_2026-09.csv"
DIR = "profile"
# 档案按评级分目录存放（用户 2026-09-23 要求）；索引仍留在 profile/ 根
SUBDIRS = {"A": "profile/A", "B": "profile/B", "C": "profile/C"}


def _subdir(code):
    """档案所在子目录，按编号前缀（A/B/C）决定。"""
    return SUBDIRS.get(code[0], DIR)


def _all_dossier_files():
    """返回 [(子目录, 文件名)]，覆盖所有评级子目录。"""
    out = []
    for d in list(SUBDIRS.values()) + [DIR]:
        if os.path.isdir(d):
            out += [(d, f) for f in os.listdir(d)
                    if f.endswith(".md") and f != "00-索引.md"]
    return out

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
    # Keep uncertainty in the raw field, but do not promote guessed addresses
    # into the extracted mailbox list (e.g. the historical J A Shomer guess).
    segments = re.split(r"[；;。\n]", text)
    non_guessed = " ".join(x for x in segments if not re.search(r"推测|猜测", x))
    return re.findall(r'[\w.+-]+@[\w.-]+\.\w+', non_guessed)


def without_contact_evidence(note):
    """Contact-audit prose/URLs are not customer demand or personalization facts.

    Keep the full note in the dossier, but exclude the explicitly marked
    append-only research section from scenario, brand and mail extraction.
    Legacy notes without this marker retain their existing behavior.

    Two marker families are cut: the A###–A### 联络核验 rounds (R40+) and the
    R-numbered rounds (R49 邮箱补录/复核), so audit prose such as
    "official-company" or "R49" can never leak into a customer-facing mail.
    """
    return re.split(r"【\d{4}-\d{2}-\d{2} (?:A\d+[–-]A\d+联络核验|R\d+[^】]*?)】",
                    note, maxsplit=1)[0].rstrip()


def phones(text):
    out = []
    for m in re.findall(r'(?:\+\d[\d\s().-]{6,}|\d[\d\s().-]{7,})', text):
        m = m.strip().strip('.,;')
        if sum(c.isdigit() for c in m) >= 7:
            out.append(re.sub(r'\s+', ' ', m))
    return out


FILLED_RE = re.compile(r'^\|\s*\d{4}-\d{2}-\d{2}\s*\|', re.M)

# ── R54：A 类档案加厚（逐户深度调研 + 原文证据 + 3 步跟进计划）────────────
# 数据只放在 batch/*.json 里，本脚本负责渲染 → dossier 永远可由
# 「CSV + 加厚 JSON」重新生成，手工改 profile/ 的下场是下次重建被覆盖。
ENRICH_FILES = [
    "batch/A类加厚_2026-09-28_R54_第1批.json",
    "batch/A类加厚_2026-09-28_R54_第2批.json",
    "batch/A类加厚_2026-09-28_R54_第3批.json",
    "batch/A类加厚_2026-09-28_R54_第4批.json",
    "batch/A类加厚_2026-09-28_R54_第5批.json",
    "batch/A类加厚_2026-09-28_R54_第6批.json",
    "batch/A类加厚_2026-09-28_R54_第7批.json",
    "batch/A类加厚_2026-09-28_R54_第8批.json",
    "batch/A类加厚_2026-09-28_R54_第9批.json",
    "batch/A类加厚_2026-09-28_R54_第10批.json",
    "batch/A类加厚_2026-09-28_R54_第11批.json",
    "batch/A类加厚_2026-09-28_R54_第12批.json",
    "batch/A类加厚_2026-09-28_R54_第13批.json",
    "batch/A类加厚_2026-09-28_R54_第14批.json",
    "batch/A类加厚_2026-09-28_R54_第15批.json",
    "batch/A类加厚_2026-09-28_R54_第16批.json",
    "batch/A类加厚_2026-09-28_R54_第17批.json",
]
CN = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)


def load_enrichment():
    """{档案编号: 加厚记录}；缺文件就当没有（保持历史输出）。
    先在当前工作目录找 batch/ 相对路径；找不到就回退到仓库根（脚本上一级）。
    这样从隔离目录调用本脚本时（如测试）与正常根目录调用产出一致。"""
    out = {}
    for rel in ENRICH_FILES:
        path = rel if os.path.exists(rel) else os.path.join(_REPO_ROOT, rel)
        if not os.path.exists(path):
            continue
        for rec in json.load(open(path, encoding="utf-8"))["records"]:
            if len(rec.get("followup_plan", [])) != 3:
                raise SystemExit("❌ %s：%s 的跟进计划不是 3 步（用户要求最多 3 次）"
                                 % (rel, rec.get("code")))
            rec["_file"] = rel
            out[rec["code"]] = rec
    return out


ENRICH = load_enrichment()

ENRICH55_FILES = [
    "batch/A类深挖_2026-09-28_R55_第1批.json",
    "batch/A类深挖_2026-09-28_R55_第2批.json",
    "batch/A类深挖_2026-09-28_R56_第3批.json",
    "batch/A类深挖_2026-09-28_R56_第4批.json",
    "batch/A类深挖_2026-09-28_R56_第5批.json",
    "batch/A类深挖_2026-09-28_R56_第6批.json",
    "batch/A类深挖_2026-09-28_R56_第7批.json",
    "batch/A类深挖_2026-09-28_R56_第8批.json",
    "batch/A类深挖_2026-09-28_R56_第9批.json",
    "batch/A类深挖_2026-09-28_R56_第10批.json",
    "batch/A类深挖_2026-09-28_R56_第11批.json",
    "batch/A类深挖_2026-09-28_R56_第12批.json",
    "batch/A类深挖_2026-09-28_R56_第13批.json",
    "batch/A类深挖_2026-09-28_R56_第14批.json",
    "batch/A类深挖_2026-09-28_R56_第15批.json",
    "batch/A类深挖_2026-09-28_R56_第16批.json",
    "batch/A类深挖_2026-09-28_R56_第17批.json",
    "batch/A类深挖_2026-09-28_R56_第18批.json",
    "batch/A类深挖_2026-09-28_R56_第19批.json",
    "batch/A类深挖_2026-09-28_R56_第20批.json",
    "batch/A类深挖_2026-09-28_R56_第21批.json",
    "batch/A类深挖_2026-09-28_R56_第22批.json",
    "batch/A类深挖_2026-09-28_R56_第23批.json",
    "batch/A类深挖_2026-09-28_R56_第24批.json",
    "batch/A类深挖_2026-09-28_R56_第25批.json",
    "batch/A类深挖_2026-09-28_R56_第26批.json",
    "batch/A类深挖_2026-09-28_R56_第27批.json",
    "batch/A类深挖_2026-09-28_R56_第28批.json",
    "batch/A类深挖_2026-09-28_R56_第29批.json",
    "batch/A类深挖_2026-09-29_R56_第57批.json",  # R58 竞品谱新挖入库第 1 波（A-568/569 深挖 + B-534/C-371/372/373 评估）
    "batch/A类深挖_2026-09-28_R56_第30批.json",
    "batch/A类深挖_2026-09-28_R56_第31批.json",
    "batch/A类深挖_2026-09-28_R56_第32批.json",
    "batch/A类深挖_2026-09-28_R56_第33批.json",
    "batch/A类深挖_2026-09-28_R56_第34批.json",
    "batch/A类深挖_2026-09-28_R56_第35批.json",
    "batch/A类深挖_2026-09-28_R56_第36批.json",
    "batch/A类深挖_2026-09-28_R56_第37批.json",
    "batch/A类深挖_2026-09-28_R56_第38批.json",
    "batch/A类深挖_2026-09-28_R56_第39批.json",
    "batch/A类深挖_2026-09-28_R56_第40批.json",
    "batch/A类深挖_2026-09-28_R56_第41批.json",
    "batch/A类深挖_2026-09-28_R56_第42批.json",
    "batch/A类深挖_2026-09-28_R56_第43批.json",
    "batch/A类深挖_2026-09-28_R56_第44批.json",
    "batch/A类深挖_2026-09-28_R56_第45批.json",
    "batch/A类深挖_2026-09-28_R56_第46批.json",
    "batch/A类深挖_2026-09-28_R56_第47批.json",
    "batch/A类深挖_2026-09-28_R56_第48批.json",
    "batch/A类深挖_2026-09-28_R56_第49批.json",
    "batch/A类深挖_2026-09-28_R56_第50批.json",
    "batch/A类深挖_2026-09-28_R56_第51批.json",
    "batch/A类深挖_2026-09-28_R56_第52批.json",
    "batch/A类深挖_2026-09-28_R56_第53批.json",
    "batch/A类深挖_2026-09-28_R56_第54批.json",
    "batch/A类深挖_2026-09-28_R56_第55批.json",
    "batch/A类深挖_2026-09-28_R56_第56批.json",
    "batch/A类深挖_2026-10-07_R66_R56_341_376基线.json",
    "batch/A类深挖_2026-10-07_R66_R56_KP第1波.json",
    "batch/A类深挖_2026-10-07_R66_R56_KP第2波.json",
    "batch/A类深挖_2026-10-07_R66_R56_KP第4波.json",
    "batch/A类深挖_2026-10-07_R66_R56_KP第5_6波.json",
    "batch/A类深挖_2026-10-07_R66_R56_KP第7_8波.json",
    "batch/A类深挖_2026-10-07_R66_R56_KP第9波.json",
    "batch/A类深挖_2026-10-07_R66_R56_KP第10波.json",
]


def load_enrichment55():
    """R55 深度再发掘（背景/芯片/KP/在意点/SWOT/Saga 适配）。结构：
    code, researched_on, dimensions{6+}, kp[{name,role,contact,status,source}]（可空）,
    facts[{dim,text,quote,url}]（>=3）。只加内容、不影响既有小节顺序逻辑之外的部分。"""
    out = {}
    for rel in ENRICH55_FILES:
        if not os.path.exists(os.path.join(_REPO_ROOT, rel)):
            continue
        data = json.load(open(os.path.join(_REPO_ROOT, rel), encoding="utf-8"))
        for rec in data["records"]:
            if "_R56_" in rel:
                # R56 批（合并加厚+深挖单批产出）：字段适配进 R55 骨架，证据不降级
                rec["code"] = rec.get("code") or rec.get("customer")
                _d5 = rec.get("r55", {}).get("dims", {})
                _sw = rec.get("r55", {}).get("swot", {})
                # dims 仅保留 ①-⑤（⑥SWOT 移入 swot_text，避免要点区重复打印）
                _dim = {k: v for k, v in _d5.items() if k != "⑥SWOT"}
                if _sw:
                    rec["swot_text"] = ("- **S**：%s\n- **W**：%s\n- **O**：%s\n- **T**：%s"
                                        % (_sw.get("S", "—"), _sw.get("W", "—"), _sw.get("O", "—"), _sw.get("T", "—")))
                rec["dimensions"] = rec.get("dimensions") or _dim
                rec["facts"] = rec.get("facts") or [
                    {"dim": e.get("dim", "证据"), "text": e.get("quote", ""),
                     "quote": e.get("quote", ""), "url": e.get("source", "")}
                    for e in rec.get("evidence", [])]
                rec["unknowns56"] = rec.get("unknowns") or []
                rec["fih56"] = {"fact": rec.get("fact", ""), "inference": rec.get("inference", ""),
                                 "hypothesis": rec.get("hypothesis", "")}
                rec["dims10"] = rec.get("dims") or {}
                rec["followup_plan"] = rec.get("followup_plan") or [
                    {"stage": f.get("stage", ""), "push": f.get("push", ""), "angle": f.get("angle", ""),
                     "question": f.get("question", ""), "proof": f.get("proof", "")}
                    for f in rec.get("followups", [])]
            elif len(rec.get("facts", [])) < 3:
                raise SystemExit("❌ %s：%s 的 R55 facts 少于 3 条（深挖必带证据）" % (rel, rec.get("code")))
            if "_R56_" not in rel:
                missing = [k for k in ("背景深描", "芯片与在用型号", "关键人KP", "关注点与资质", "优缺点SWOT", "Saga产品适配")
                           if k not in rec.get("dimensions", {})]
                if missing:
                    raise SystemExit("❌ %s：%s 的 R55 dimensions 缺 %s" % (rel, rec.get("code"), missing))
            for f in rec["facts"]:
                if not (f.get("quote") and f.get("url")):
                    raise SystemExit("❌ %s：%s facts 必须同时带原文摘录与来源URL" % (rel, rec.get("code")))
            rec["_file"] = rel
            out[rec["code"]] = rec
    return out


ENRICH55 = load_enrichment55()


# ── B 类深挖（R65：B 升 v2 骨架标准；结构同 R56）────────────────────────────
ENRICH_B_FILES = [
    "batch/B类深挖_2026-10-07_R65_R57转写.json",
    "batch/B类深挖_2026-10-07_R65_第1批.json",
    "batch/B类深挖_2026-10-07_R65_第2批.json",
    "batch/B类深挖_2026-10-07_R65_第3批.json",
    "batch/B类深挖_2026-10-07_R65_第4批.json",
    "batch/B类深挖_2026-10-07_R65_第5批.json",
    "batch/B类深挖_2026-10-07_R65_第6批.json",
    "batch/B类深挖_2026-10-07_R65_第7批.json",
    "batch/B类深挖_2026-10-07_R65_第8批.json",
    "batch/B类深挖_2026-10-07_R65_第9批.json",
    "batch/B类深挖_2026-10-07_R65_第10批.json",
    "batch/B类深挖_2026-10-07_R65_第11批.json",
    "batch/B类深挖_2026-10-07_R65_第12批.json",
    "batch/B类深挖_2026-10-07_R65_第13批.json",
    "batch/B类深挖_2026-10-07_R65_第14批.json",
    "batch/B类深挖_2026-10-07_R65_第15批.json",
    "batch/B类深挖_2026-10-07_R65_第16批.json",
    "batch/B类深挖_2026-10-07_R65_第17批.json",
    "batch/B类深挖_2026-10-07_R65_第17批补18.json",
    "batch/B类深挖_2026-10-07_R65_第19批.json",
    "batch/B类深挖_2026-10-07_R65_第20批.json",
    "batch/B类深挖_2026-10-07_R65_第21批.json",
    "batch/B类深挖_2026-10-07_R65_第22批.json",
    "batch/B类深挖_2026-10-07_R65_第23批.json",
]


def load_enrichment_b():
    """B 类深挖批（结构同 R56 深挖；缺文件跳过，与 A 类加厚同一纪律）。"""
    out = {}
    for rel in ENRICH_B_FILES:
        path = rel if os.path.exists(rel) else os.path.join(_REPO_ROOT, rel)
        if not os.path.exists(path):
            continue
        data = json.load(open(path, encoding="utf-8"))
        for rec in data["records"]:
            rec["_file"] = rel
            out[rec["code"]] = rec
    return out


ENRICH_B = load_enrichment_b()


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
    stale = _all_dossier_files()
    if not stale:
        return
    guarded = []
    for d, f in stale:
        try:
            txt = open(os.path.join(d, f), encoding="utf-8").read()
        except OSError:
            continue
        if FILLED_RE.search(txt):
            guarded.append("%s/%s" % (d, f))
    if guarded:
        raise SystemExit(
            "❌ 拒绝重建 profile/：以下档案的「跟进记录」已填入手工内容，\n"
            "   删除会丢失不可再生的信息。请先手工备份或确认后处理：\n   "
            + "\n   ".join(guarded[:20])
            + ("\n   ..." if len(guarded) > 20 else "")
        )
    for d, f in stale:
        os.remove(os.path.join(d, f))
    print("cleared %d stale dossiers from %s/{A,B,C}/" % (len(stale), DIR))


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

    # 档案编号持久化。grade.py 已经换过段，这里再跑一次只是安全网：
    # 无论上游怎么改的评级，落到写文件之前编号一定与评级一致。
    renumber(data, hdr, csv_path=CSV)
    probs = audit(data, hdr)
    if probs:
        raise SystemExit("numbering problems, refusing to write dossiers: %s" % probs[:5])
    NUMCOL = hdr.index("档案编号")

    def num_of(r):
        m = re.match(r'[ABC]-(\d+)$', (r[NUMCOL] or "").strip())
        return int(m.group(1)) if m else None

    order = {"A": 0, "B": 1, "C": 2}
    data.sort(key=lambda r: (order.get(r[17], 9), num_of(r) or 99999))
    made = []

    # R56：A 类 v2 渲染（B/C 走旧模板，不动）
    from render_v2 import STRUCT, render, yaml_of
    CUSTOM_FOLLOWUP_M = {}
    CUSTOM_EMAIL = {}
    try:  # A-002 手工定制（外部评审样板）
        _cu = json.loads(open('batch/A-002_custom_v2.json', encoding='utf-8').read())
        CUSTOM_FOLLOWUP_M = _cu.get('followup', {})
        CUSTOM_EMAIL = _cu.get('email', {})
    except FileNotFoundError:
        pass
    TRANSIENT_CU_PLAN = {}
    TRANSIENT_CU_MAIL = {}

    def _r56fu(rec):
        """R56 批定制跟进：followups[{stage,push,angle,question,proof}] → 渲染器 custom 形状。"""
        if not rec:
            return None
        fus = rec.get('followups') or rec.get('followup_plan')
        if not fus:
            return None
        out = []
        for f in fus:
            _st = re.sub(r'^第\s*[一二三四五六七八九十\d]+\s*次跟进\s*·\s*', '', f.get('stage', ''))
            out.append({'stage': _st, 'product': f.get('push') or f.get('product', '—'),
                        'angle': f.get('angle', ''), 'question': f.get('question', ''),
                        'proof': f.get('proof', '—')})
        return out or None

    def _r56em(rec):
        """R56 批定制邮件：email 全文 + 主题（从 P1 场景钩子取主题）。"""
        if not rec or not rec.get('email'):
            return None
        p1q = rec.get('question', '')
        subj = rec.get('email_subject') or 'PoE switching for your projects'
        return (subj, rec['email'])

    for r in data:
        name, country, city, site = r[0], r[1], r[2], r[3]
        typ, signal, ownbrand, angle, sku = r[4], r[5], r[6], r[7], r[8]
        contact, prio, status, src = r[9], r[10], r[11], r[12]
        note, grade, why = r[16], r[17], r[18]
        sub = r[hdr.index("C级细分")] if "C级细分" in hdr else ""

        code = (r[NUMCOL] or "").strip() or grade
        fname = "%s-%s-%s.md" % (code, safe(name), safe(country))
        directory = _subdir(code)
        os.makedirs(directory, exist_ok=True)
        path = os.path.join(directory, fname)

        analysis_note = without_contact_evidence(note)
        blob = " ".join([name, typ, signal, analysis_note])
        sc = scenarios(blob)
        key = sc[0] if sc else None

        # people -------------------------------------------------
        person = ""
        if " / " in name:
            person, company = name.split(" / ", 1)
        else:
            company = name
        mails = emails(contact + " " + analysis_note)
        tels = phones(contact)

        # brands -------------------------------------------------
        brands = sorted({b.strip() for b in BRANDS if b.lower() in (blob + " " + signal).lower()})
        certs = [c for c in CERTS if re.search(c, signal)]

        # v2 骨架（R56）：A 类全量 + B 类已深挖户（R65）；C 走旧模板
        # B 户须同时有 STRUCT 条目与深挖批记录才升级，缺一保持旧模板不降级
        if code in STRUCT and (grade == "A" or (grade == "B" and code in ENRICH_B)):
            e = STRUCT[code]
            rec_a = ENRICH.get(code)
            rec55_a = ENRICH55.get(code) if grade == "A" else ENRICH_B.get(code)
            ctx = dict(name=name, country=country, city=city, site=site, typ=typ,
                       signal=signal, ownbrand=ownbrand, angle=angle, sku=sku,
                       contact=contact, prio=prio, status=status, src=src, note=note,
                       why=why, rec=rec_a, rec55=rec55_a,
                       person=person, person_disp=(person or None), company=company,
                       mails=mails, tels=tels,
                       # R54 已有跟进步骤的户（frozen plan）优先保留；R56 定制只在无 R54 记录时补位
                       custom_followup=(CUSTOM_FOLLOWUP_M.get(code) or TRANSIENT_CU_PLAN.get(code)
                                        or (_r56fu(ENRICH55.get(code)) if (grade == "A" and ENRICH55.get(code) and not rec_a)
                                            else (_r56fu(ENRICH_B.get(code)) if grade == "B" else None))),
                       custom_email=(CUSTOM_EMAIL.get(code) or TRANSIENT_CU_MAIL.get(code)
                                     or (_r56em(ENRICH55.get(code)) if grade == "A"
                                         else (_r56em(ENRICH_B.get(code)) if grade == "B" else None))))
            L = render(e, ctx)
            open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")
            made.append((code, name, country, fname))
            continue

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
        if grade == "A" and "待人工补信息" in note:
            w("")
            w("> 🟡 **信息不够，需要人工处理**")
            w(">")
            w("> 本条为集成商/顾问型（A 级主产地），但目前**抓不到邮箱**，群发触达不到。")
            w("> 已按人工定级提为 A，**请先补齐以下任一信息再进入群发名单**：")
            w("> 1. 找邮箱（官网 / 名录页 / LinkedIn）；")
            w("> 2. 若确实只有电话，确认其为唯一触达方式，改为单独跟进、不进群发。")
            w(">")
            w("> 补到邮箱后，可删掉本条备注开头的 `【待人工补信息】` 标记。")
            w("")
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
        w("| 首推 Saga 型号 | %s |" % (sku or "—"))
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
        extra = [m for m in emails(analysis_note) if m not in mails]
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
            if sub:
                w("> **C 级细分：`%s`**" % sub)
                w("")
            w("> ⛔ **Too hard pile**：本条进「太难」堆，**当前不投入跟进精力**，不必为它写开发信或做方案。")
            w("> 信息已**全量留档**（本档案 + 总表 %d 列），待出现明确触发条件再捞出来重评：" % len(hdr))
            w("> ① 对方主动询价；② 出现停产替换需求；③ 我方补齐对应认证；④ 你从别处拿到其内部人线索。")
        w("")

        # 5.5 R54 enrichment (A tier only): dimensions + evidence + 3-touch plan
        sec = 6
        rec = ENRICH.get(code) if grade == "A" else None
        if rec:
            sec = 9
            w("## 六、深度加厚（R54 逐户调研）")
            w("")
            w("> 调研日期 **%s**；来源为客户官网/公开页面抓取，原文摘录见下一节，"
              "原始记录：`%s`。" % (rec.get("researched_on", "—"), rec.get("_file", ENRICH_FILES[0])))
            w("")
            for dim, text in rec["dimensions"].items():
                w("- **%s**：%s" % (dim, text))
            w("")
            w("## 七、原文证据摘录（R54）")
            w("")
            w("> 下列引用为 %s 抓取的页面原文（非我方转述）；点不开或内容变动时，"
              "以抓取 JSON 中的记录为准。" % rec.get("researched_on", "—"))
            w("")
            for f in rec["facts"]:
                w("- **【%s】**%s" % (f["dim"], f["text"]))
                w("  > %s" % f["quote"])
                w("  > 来源：%s" % f["url"])
            w("")
            w("## 八、3 步跟进计划（R54，**最多 3 次**）")
            w("")
            w("> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；"
              "**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。")
            w("")
            for st in rec["followup_plan"]:
                stage = re.sub(r'^第[一二三四五六七八九十]+次跟进\s*·\s*', '', st["stage"])
                w("### 第 %d 次跟进 · %s" % (st["step"], stage))
                w("")
                w("- **推什么**：%s" % st["product"])
                w("- **切入点**：%s" % st["angle"])
                w("- **要问的问题**：%s" % st["question"])
                w("- **随附证明**：%s" % st["proof"])
                w("")

        # 5.6 R55 deep re-excavation (A tier only)
        rec55 = ENRICH55.get(code) if grade == "A" else None
        if rec55:
            sec = 10
            w("## 九、深度再发掘（R55：背景 · 芯片/型号 · 关键人 · 在意点 · SWOT · Saga 适配）")
            w("")
            w("> 调研日期 **%s**；来源含官网/公开工商与社媒页面，原文摘录见本节后部；"
              "原始记录：`%s`。涉及我方价格均为 EXW 快照（15 天有效，报价前核价）。"
              % (rec55.get("researched_on", "—"), rec55.get("_file", ENRICH55_FILES[0])))
            w("")
            for dim, text in rec55["dimensions"].items():
                w("- **%s**：%s" % (dim, text))
            w("")
            if rec55.get("kp"):
                w("### 关键人（KP）与触达通道")
                w("")
                w("| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |")
                w("|---|---|---|---|---|")
                for k in rec55["kp"]:
                    w("| %s | %s | %s | %s | %s |" % (k.get("name", "—"), k.get("role", "—"),
                                                      k.get("contact", "—"), k.get("status", "—"), k.get("source", "—")))
                w("")
            w("### R55 证据摘录")
            w("")
            for f in rec55["facts"]:
                w("- **【%s】**%s" % (f["dim"], f["text"]))
                w("  > %s" % f["quote"])
                w("  > 来源：%s" % f["url"])
            w("")

        # 6 cautions
        w("## %s、注意点" % CN[sec])
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
            log_sec = CN[sec + 2]
        else:
            log_sec = CN[sec + 1]
        if grade == "A":
            from emails import build
            subject, body = build(name, person, country, city, key, sku, analysis_note)
            w("## %s、首触邮件（可直接发送）" % CN[sec + 1])
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
        w("## %s、跟进记录" % log_sec)
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
                 "",
                 "存放位置：`profile/A/`（A 级）、`profile/B/`（B 级）、`profile/C/`（C 级）",
                 "", "证据与缺证：[A](../docs/evidence/客户溯源_A.md) / [B](../docs/evidence/客户溯源_B.md) / [C](../docs/evidence/客户溯源_C.md)。",
                 "模板卖点/邮件不是已核实事实；跟进线下维护，用户报实际回复时才更新。",
                 "", "评级含义：", "",
                 "- **A**　重点且好跟进：有明确需求信号 + 具体对接人 + 决策链短",
                 "- **B**　慢慢跟：信号待验证，或交换需求弱",
                 "- **C**　难啃：大公司 / 集团 / 自有品牌 / 竞品 / 区域外", "",
                 "每份档案含：评级与结论 · 公司概览 · 人员与联系方式 · 品牌与技术栈 · 跟进策略 · 注意点 · 跟进记录（待填）；"
                 "A 级另有 R54 加厚：深度加厚 · 原文证据摘录 · 3 步跟进计划。",
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
        idx_lines.append("- [`%s`](<%s/%s>)　%s · %s"
                         % (code, os.path.relpath(_subdir(code), DIR), fname, name, country))
    idx_lines.append("")
    open(os.path.join(DIR, "00-索引.md"), "w", encoding="utf-8").write("\n".join(idx_lines))

    print("generated %d dossiers in %s/{A,B,C}/" % (len(made), DIR))
    print(dict((g, sum(1 for m in made if m[0][0] == g)) for g in "ABC"))


if __name__ == "__main__":
    main()
