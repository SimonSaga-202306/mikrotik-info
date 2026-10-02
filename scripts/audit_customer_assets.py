"""
客户资产池质量审核(A/B/C 资产长期跟进口径)
======================================================

2026-09-29 起新增。audit_repository.py 扫"仓库文件结构级"完整性; 本脚本扫
"客户资产池业务级"完整性: CSV↔profile 对称、编号退役线、联系字段格式、
评级↔档案结构联动、疑似重复客户、触达手段可用性。

用法:
    python3 scripts/audit_customer_assets.py        # 输出 JSON 汇总(stdout) + 机读 JSON(docs/audit/客户资产池审核_日期.json)

输出分级:
    P0 数据断裂(同客户重复/退信号复活/高优先级无触达)
    P1 可信度受损(邮箱格式/占位域名/人工定级与评级矛盾/快照日期漂移)
    P2 一致性偏差(B 档缺深挖块/非 C 却有 C级细分 等)
    P3 观察项(状态值/档案命名等国家尾标)
"""
import csv, json, re, sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / '客户名单_反向信号_2026-09.csv'
MAIL_RE = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}')
BAD_MAIL_RE = re.compile(r'@(@|\.\.)|\.\.@|@\.|\s@|@\s|mailto:mailto:|\(at\)\S*@')
PHONE_RE = re.compile(r'(?:\+\d[\d\s\-()]{6,}|\d{3}[\-\s]\d{3}[\-\s]\d{4}|\d{2,4}\s\d{3,4}\s\d{3,4})')

def main():
    rows = list(csv.DictReader(open(CSV, encoding='utf-8-sig')))
    hdr = list(rows[0].keys())
    by_code = {r['档案编号']: r for r in rows}
    codes = Counter(r['档案编号'] for r in rows)

    P = {'P0': [], 'P1': [], 'P2': [], 'P3': []}
    def rec(lv, code, item, detail):
        P[lv].append({'code': code, 'item': item, 'detail': detail})

    # 1. CSV↔profile 对称
    file_codes = {}
    for lvl in ('A','B','C'):
        for f in (ROOT/f'profile/{lvl}').glob(f'{lvl}-*.md'):
            file_codes.setdefault(f.name[:5], []).append(f.name)
    for c in sorted(set(by_code) - set(file_codes)):
        rec('P0', c, 'CSV有行·profile无档', by_code[c]['公司名'])
    for c in sorted(set(file_codes) - set(by_code)):
        rec('P0', c, 'profile有档·CSV无行', str(file_codes[c]))
    for c, names in file_codes.items():
        if len(names) > 1:
            rec('P0', c, '同号多档', str(names))
    for c, n in codes.items():
        if n > 1:
            rec('P0', c, 'CSV编号重复', f'x{n}')

    # 编号洞 (R48 晋升线改号正常留洞,只统计)
    holes = {}
    for lvl in ('A','B','C'):
        have = {int(c[2:]) for c in by_code if c[0]==lvl}
        mx = max(have) if have else 0
        holes[lvl] = sorted(set(range(1, mx+1)) - have)

    # 2. 邮箱格式
    for r in rows:
        for m in MAIL_RE.findall(r['入口/联系方式'] or ''):
            if BAD_MAIL_RE.search(m) or m.endswith('.') or '..' in m:
                rec('P1', r['档案编号'], '邮箱格式可疑', m)
            if m.split('@')[1].lower() in ('example.com','example.org','test.com','domain.com','email.com'):
                rec('P1', r['档案编号'], '邮箱占位域名', m)

    # 3. 评级↔档案结构
    for code, r in by_code.items():
        if code[0] == 'B':
            fs = list((ROOT/'profile/B').glob(f'{code}-*.md'))
            if fs and 'BDEEP:' not in fs[0].read_text(encoding='utf-8'):
                rec('P2', code, 'B档无深挖块', r['公司名'])
        if code[0] == 'C':
            fs = list((ROOT/'profile/C').glob(f'{code}-*.md'))
            if fs and 'BDEEP:' in fs[0].read_text(encoding='utf-8'):
                rec('P2', code, 'C档有深挖块(规则外)', r['公司名'])
        if r['评级'] == 'A' and not r['评级依据'].strip():
            rec('P2', code, 'A级无评级依据', r['公司名'])
        if r['人工定级'] == 'A' and r['评级'] != 'A':
            rec('P1', code, '人工定级A但评级非A', f"评级={r['评级']}")
        if r['评级'] != 'C' and r['C级细分']:
            rec('P2', code, '非C级但有C级细分', r['C级细分'][:40])
        if r['评级'] == 'C' and not r['C级细分']:
            rec('P3', code, 'C级缺细分标注', r['公司名'])

    # 4. 疑似重复客户
    def norm(s):
        s = (s or '').lower().strip()
        for t in (' ltd',' gmbh',' ab',' as',' aps',' ou',' oü',' oy',' bv',' b.v',' inc',' corp',' llc',' s.l',' srl',' spa',' sp. z o.o',' sa',' sas',' ag',' kg',' kft',' s.r.o',' & co',' co.',' ','.','-','_'):
            s = s.replace(t, '')
        return s
    name_map, dom_map = defaultdict(list), defaultdict(list)
    for r in rows:
        name_map[norm(r['公司名'])].append(r['档案编号'])
        w = (r['网站'] or '').lower().strip().replace('www.','').replace('https://','').replace('http://','').rstrip('/')
        if w and w not in ('—','-',''): dom_map[w].append(r['档案编号'])
    for k, v in name_map.items():
        if k and len(set(v)) > 1:
            rec('P1', '|'.join(sorted(set(v))), '疑似重复客户(同名)', f'{k} -> {sorted(set(v))}')
    for k, v in dom_map.items():
        if k and len(set(v)) > 1:
            rec('P1', '|'.join(sorted(set(v))), '疑似重复客户(同域名)', f'{k} -> {sorted(set(v))}')

    # 5. 高优先级触达手段
    for r in rows:
        if r['评级'] in 'AB' and r['优先级'] == '★★★':
            c = r['入口/联系方式'] or ''
            if not MAIL_RE.search(c) and not PHONE_RE.search(c):
                rec('P0', r['档案编号'], '★★★ 无邮箱无电话', f'{r["公司名"]} contact={c[:60]}')

    # 6. 退役编号
    for dead in ('B-534','B-535'):
        if dead in by_code:
            rec('P0', dead, '退役编号复活', by_code[dead]['公司名'])

    # 7. 联系方式占位/敏感词
    for r in rows:
        c = r['入口/联系方式'] or ''
        if any(t in c for t in ('password','passwd','TODO','待补(独)','xxx@','@xxx')):
            rec('P1', r['档案编号'], '联系方式含占位/敏感词', c[:80])

    # 8. EXW 快照日期统一基线(2026-09-28 锁)
    for f in (ROOT/'profile/A').glob('A-*.md'):
        txt = f.read_text(encoding='utf-8')
        for m in re.finditer(r'USD EXW（(2026-09-\d\d) 快照', txt):
            if m.group(1) != '2026-09-28':
                rec('P1', f.name[:5], 'EXW快照日期非统一基线', f'{m.group(1)}(基准=2026-09-28)')

    summary = {
        'total_rows': len(rows),
        'csv_vs_profile': {'csv_only': len(set(by_code)-set(file_codes)), 'fs_only': len(set(file_codes)-set(by_code))},
        'holes_in_numbering': holes,
        'P0': P['P0'], 'P1': P['P1'],
        'P2_count': len(P['P2']), 'P3_count': len(P['P3']),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=1, default=str))
    out = ROOT / 'docs/audit/客户资产池审核_2026-09-29.json'
    out.write_text(json.dumps({**P, 'holes_in_numbering': holes}, ensure_ascii=False, indent=1, default=str), encoding='utf-8')
    print('FULL REPORT ->', out, file=sys.stderr)

if __name__ == '__main__':
    main()
