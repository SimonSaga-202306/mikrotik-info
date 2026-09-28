#!/usr/bin/env python3
"""R55 一次性迁移：客户内容中的 SmartByte 推荐型号 -> Saga（2026-09-28）。

规则（用户 R55-4）：
- 推荐产品一律换成 Saga（Price List_Marvell Based * 三份价格表里的 STC-/STI- 型号）；
- Saga 没有的规格（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）保留 SmartByte 并显式标注；
- 只改内容、不动任何顺序；B/C 级档案不动；
- 客户网站原文引号（facts[].quote）与来源 URL 一字不动。

改写范围：
1. 客户名单_反向信号_2026-09.csv  —— 列8 `首推SmartByte型号`（值 + 表头名）
2. scripts/strategy.py           —— PLAY 话术里的型号字符串
3. scripts/make_profiles.py      —— 公司概览表行标签
4. batch/A类加厚_*_第1..17批.json  —— 我方撰写的文本字段（dimensions / followup_plan /
   researched_on 等），跳过 facts[].quote 与 facts[].url（客户原文，逐字保留）
幂等：全部替换可重复执行（目标文本里不再含旧 token）。
"""
import csv, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

MAP = json.load(open("batch/saga_smartbyte_model_map_2026-09-28.json", encoding="utf-8"))["map"]
# 长码优先，避免 LT-IS6310G 吃掉 LT-IS6310G-2GX8GT
TOKENS = sorted(MAP, key=len, reverse=True)
BRAND = re.compile(r"[Ss]mart[Bb]yte")


def sagify(text):
    for t in TOKENS:
        if t in text:
            text = text.replace(t, MAP[t])
    # 剩余裸品牌词（我们自己的话术）统一归 Saga，再把 "Saga/Saga" 收敛
    text = BRAND.sub("Saga", text)
    text = text.replace("Saga/Saga", "Saga").replace("Saga（Saga）", "Saga")
    return text


def walk(obj, key=None):
    """递归改写；quote/url 字段跳过（客户原文与来源不可动）。"""
    if isinstance(obj, dict):
        return {k: (v if k in ("quote", "url") else walk(v, k)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [walk(v, key) for v in obj]
    if isinstance(obj, str):
        return sagify(obj)
    return obj


def migrate_csv():
    path = "客户名单_反向信号_2026-09.csv"
    raw = open(path, encoding="utf-8-sig", newline="").read()
    rows = list(csv.reader(io.StringIO(raw)))
    hdr, n = rows[0], 0
    assert hdr[8] == "首推SmartByte型号", hdr[8]
    hdr[8] = "首推Saga型号"
    for r in rows[1:]:
        if len(r) > 8 and r[8].strip() and r[8] != "—":
            new = sagify(r[8])
            if new != r[8]:
                r[8] = new
                n += 1
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerows(rows)
    open(path, "w", encoding="utf-8-sig", newline="").write(buf.getvalue())
    print("csv: %d cells sagified" % n)


def migrate_py(path, pairs):
    s = open(path, encoding="utf-8").read()
    for old, new in pairs:
        assert old in s, (path, old)
        s = s.replace(old, new)
    s = sagify(s)
    open(path, "w", encoding="utf-8").write(s)
    print("py patched:", path)


def migrate_batches():
    import glob
    total = 0
    for fp in sorted(glob.glob("batch/A类加厚_2026-09-28_R54_第*批.json")):
        d = json.load(open(fp, encoding="utf-8"))
        d2 = walk(d)
        if d2 != d:
            json.dump(d2, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            total += 1
    print("batch json rewritten: %d files" % total)


if __name__ == "__main__":
    migrate_csv()
    migrate_py("scripts/make_profiles.py", [
        ("| 首推 SmartByte 型号 | %s |", "| 首推 Saga 型号 | %s |"),
    ])
    migrate_py("scripts/strategy.py", [])
    migrate_batches()
    print("DONE")
