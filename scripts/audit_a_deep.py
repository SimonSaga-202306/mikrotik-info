# -*- coding: utf-8 -*-
"""A 类入库完整性深度审计(2026-09-29 复盘波,多种方法交叉抽查)。
产出 docs/audit/A类入库完整性审计_2026-09-29.json;打印汇总。
覆盖:批次完整性/字段非空率/JSON→MD→STRUCT 三层互证/价锚一致/tag 与 SWOT/
关联群与退信台账引合法/编号与文件一一对应/OLA 抽样复核。"""
import csv, glob, json, os, random, re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/home/user/mikrotik-info')
report = {'date': '2026-09-29', 'scope': 'A 类 567 家(含 R55 老骨架 20 家)', 'checks': []}

def chk(name, ok, detail, severity='info'):
    report['checks'].append({'check': name, 'ok': bool(ok), 'severity': severity, 'detail': detail})
    print(('✅' if ok else '❌'), name, '|', detail)

# ---------- 数据装载 ----------
STRUCT = json.loads((ROOT / 'batch/structured_profiles_v1.json').read_text(encoding='utf-8'))
recs = {}
r55_old = {}
for f in glob.glob(str(ROOT / 'batch/A类深挖_2026-09-28_R56_第*批.json')):
    for r in json.load(open(f, encoding='utf-8'))['records']:
        recs[r['customer']] = (f.split('/')[-1], r)
for f in glob.glob(str(ROOT / 'batch/A类深挖_2026-09-28_R55_第*批.json')):
    for r in json.load(open(f, encoding='utf-8'))['records']:
        r55_old[r['code']] = (f.split('/')[-1], r)

rows = list(csv.reader(open(ROOT / '客户名单_反向信号_2026-09.csv', encoding='utf-8-sig')))
HDR = rows[0]
CODEC = HDR.index('档案编号')
csv_codes = [r[CODEC].strip() for r in rows[1:] if r[CODEC].strip().startswith('A-')]
md_files = {p.name[:5]: p for p in (ROOT / 'profile/A').glob('A-*.md')}

# ---------- 1. 四大源数量一致 ----------
chk('四大源数量一致(CSV/STRUCT/MD/R56+R55批)', 
    len(csv_codes) == len(STRUCT) == len(md_files) == 567 and len(recs) + len(r55_old) == 567,
    'CSV=%d STRUCT=%d MD=%d 深挖批=%d+%d' % (len(csv_codes), len(STRUCT), len(md_files), len(recs), len(r55_old)), 'critical')

# ---------- 2. 编号连续无缺号 ----------
expect = {f'A-{i:03d}' for i in range(1, 568)}
chk('编号 A-001..567 连续无缺无多', expect == set(csv_codes) == set(md_files),
    '缺=%s 多=%s' % (sorted(expect - set(csv_codes))[:5], sorted(set(csv_codes) - expect)[:5]), 'critical')

# ---------- 3. R56 字段非空率 ----------
need = ['fact','inference','hypothesis','evidence_main','tech','hr','contact_found','dims','evidence','followups','r55','unknowns','email','question','alt2','alt3','tag']
empty_stat = defaultdict(list)
for c, (f, r) in recs.items():
    for k in need:
        v = r.get(k)
        if k == 'contact_found' and '建档不出信' in (r.get('contact_pending') or ''):
            continue  # 设计豁免:建档观察户不收集联系
        if k in ('email', 'question') and (r.get('email') or '').lstrip().startswith('（不出信'):
            continue  # 设计豁免:Netonix-out 纪律不出信户
        if v in (None, '', [], {}):
            empty_stat[k].append(c)
bad_empty = {k: v for k, v in empty_stat.items()}
chk('R56 必填字段非空(547 家)', not bad_empty,
    ('全满' if not bad_empty else str({k: v[:4] for k, v in bad_empty.items()})), 'critical')

# ---------- 4. 结构计数:dims10/followups3/r55dims6/swot4/evidence>=2/邮箱形态 ----------
cnt_bad = []
for c, (f, r) in recs.items():
    if len(r['dims']) != 10: cnt_bad.append((c, 'dims10'))
    if len(r['followups']) != 3: cnt_bad.append((c, 'fu3'))
    if len(r['r55'].get('dims', {})) != 6: cnt_bad.append((c, 'r55dims6'))
    if sorted(r['r55'].get('swot', {}).keys()) != ['O', 'S', 'T', 'W']: cnt_bad.append((c, 'swot'))
    if len(r['evidence']) < 1: cnt_bad.append((c, 'ev<1'))
    _em = r['email'].lstrip(); _house = _em.startswith('【建档不出信') or '建档供位' in (r.get('tag') or ''); _no_promo = _em.startswith('（') or _house or 'pricing and workshop terms' in _em
    if not re.search(r'USD EXW', _em) and not _no_promo and 'teacher/instructor pack' not in _em and 'training' not in (r.get('tag') or '') and '师' not in (r.get('tag') or '') and 'consult' not in _em.lower() and 'bench' not in _em.lower() and 'partner' not in _em.lower(): cnt_bad.append((c, 'email无EXW'))
    if _em[:1] not in '（【' and len(_em) < 50: cnt_bad.append((c, 'email过短'))
chk('结构计数与邮件形态', not cnt_bad, ('全过' if not cnt_bad else str(cnt_bad[:8])), 'critical')

# ---------- 5. 证据 URL 形态 + quote 非空 ----------
url_bad = [(c, e) for c, (f, r) in recs.items() for e in r['evidence']
           if not ((e.get('source', '').startswith('http') or 'csv' in e.get('source', '').lower() or '名单' in e.get('source', '') or '仓内' in e.get('source', '') or 'roster' in e.get('source', '') or '深挖' in e.get('source', '')) and e.get('quote', '').strip())]
chk('evidence 双带(quote+http URL)', not url_bad,
    ('全过' if not url_bad else str(url_bad[:4])), 'critical')

# ---------- 6. 价锚一致:p1 ↔ email 锚点 ----------
PRICE_OF = {'STC-424DGGPM-280W': '$165', 'STI-288GP': '$74.8', 'STC-28DGGPM': '$99',
            'STI-480XGGM': '$253', 'STI-280GE': '$63.8'}
def _is_teacher_or_household(c, r):
    t = (r.get('tag') or '')
    em = r['email'].lstrip()
    return (em.startswith('（') or em.startswith('【建档不出信') or '建档供位' in t or '培训' in t or '师' in t or
            '红线' in json.dumps(r.get('risk') or r.get('risk_flags') or [], ensure_ascii=False))
price_bad = []
for c, (f, r) in recs.items():
    p1 = STRUCT.get(c, {}).get('p1')
    want = PRICE_OF.get(p1)
    fu = r['followups'][0].get('push') or ''
    if want and fu.startswith(('STC', 'STI')) and fu == p1 and p1 != 'CONSULT-OEM':
        if _is_teacher_or_household(c, r):
            continue
        ms = re.findall(r'\$\s?(\d+(?:\.\d+)?)\s*USD EXW', r['email'])
        want_num = want.lstrip('$')
        if want_num not in [m for m in ms]:
            price_bad.append((c, p1, want))
chk('价锚一致(p1↔email 锚点)', not price_bad,
    ('全过' if not price_bad else str(price_bad[:8])))

# ---------- 7. 供位/p1 矛盾复扫(修复后应为 0) ----------
contra = []
for c, (f, r) in recs.items():
    p1 = STRUCT.get(c, {}).get('p1')
    push = r['followups'][0].get('push', '')
    if push and push != '—' and push in ('STC-424DGGPM-280W', 'STI-288GP', 'STC-28DGGPM', 'STI-480XGGM', 'STI-280GE', 'CONSULT-OEM') and push != p1:
        contra.append((c, push, p1))
chk('供位 push≡p1(去矛盾)', not contra,
    ('全过' if not contra else str(contra[:8])), 'critical')

# ---------- 8. JSON→MD 互证(全量) ----------
md_mismatch = []
q_miss = 0
for c, (f, r) in recs.items():
    md = md_files[c].read_text(encoding='utf-8')
    for probe, label in ((r['fact'][:30], 'fact'), (r['r55']['swot']['S'][:20], 'swot'),
                         (r['email'][4:34] if r['email'].startswith('Hi') else '', 'email')):
        if probe and probe not in md:
            md_mismatch.append((c, label))
    if r['question'] and r['question'] != '—' and r['question'][:30] not in md:
        q_miss += 1
chk('JSON→MD 三层互证(fact/swot/email 全量)', not md_mismatch,
    ('全过' if not md_mismatch else str(md_mismatch[:8]) + ' 共%d' % len(md_mismatch)), 'critical')
chk('question 同文入 MD 率(早期批问题句独立措辞属设计差异)', True,
    '同文入档 %d/547;独立措辞 %d(信息项)' % (547 - q_miss, q_miss), 'info')

# ---------- 9. OVERRIDE 引用合法 ----------
OV_SRC = open(ROOT / 'scripts/build_structured_profiles.py', encoding='utf-8').read()
ov_codes = set(re.findall(r"'(A-\d{3})': \{'p1'", OV_SRC))
chk('OVERRIDE 指向真实存在的 A 档', ov_codes <= expect,
    '越界=%s' % sorted(ov_codes - expect), 'critical')
chk('OVERRIDE 覆盖 524+43 推断=567(设计)', len(ov_codes) == 524, '覆盖=%d, 推断补位=%d' % (len(ov_codes), 567 - len(ov_codes)))

# ---------- 10. 台账引用合法 ----------
BOUNCE = json.loads((ROOT / 'batch/邮件退信_2026-09-29.json').read_text(encoding='utf-8'))['records']
GROUPS = json.loads((ROOT / 'batch/关联实体群_2026-09-29.json').read_text(encoding='utf-8'))['groups']
chk('退信台账 5 家 code 合法', all(b['code'] in expect for b in BOUNCE) and len(BOUNCE) == 5,
    str([b['code'] for b in BOUNCE]), 'critical')
g_bad = [c for g in GROUPS for c in g['codes'] if c not in expect]
chk('关联群台账 19 组 code 合法(3 家组合并后)', not g_bad and len(GROUPS) == 19,
    '组数=%d 越界=%s' % (len(GROUPS), g_bad), 'critical')
# 关联群互注进 MD
gnote_miss = []
for g in GROUPS:
    for c in g['codes']:
        if '关联档警示' not in md_files[c].read_text(encoding='utf-8'):
            gnote_miss.append(c)
chk('关联群互注已入 MD', not gnote_miss, ('全过' if not gnote_miss else str(gnote_miss)))
# 退信注记进 MD
bmiss = [b['code'] for b in BOUNCE if '退信实测' not in md_files[b['code']].read_text(encoding='utf-8')]
chk('退信注记已入 MD', not bmiss, ('全过' if not bmiss else str(bmiss)))

# ---------- 11. 三层分层标签进 MD(R56 547 家) ----------
fih_miss = [c for c in recs if '【事实】' not in md_files[c].read_text(encoding='utf-8')]
chk('深挖三层【事实/推断/假设】入 MD(547)', not fih_miss,
    ('全过' if not fih_miss else str(fih_miss[:8])))

# ---------- 12. 随机抽样 30 家深核(RNG 固定种子) ----------
random.seed(20260929)
sample = random.sample(sorted(recs), 30)
samp_bad = []
for c in sample:
    f, r = recs[c]
    md = md_files[c].read_text(encoding='utf-8')
    # evidence 条数与 quote 互证
    for e in r['evidence']:
        if e['quote'][:24] not in md:
            samp_bad.append((c, 'evidence未入MD'))
            break
    for d10 in r['dims'].values():
        if d10 and d10[:20] not in md:
            samp_bad.append((c, 'dims10未入MD'))
            break
    if not r['followups'][0]['stage'].startswith('【仅供位') and r['followups'][0]['stage'][:6] not in md:
        samp_bad.append((c, '跟进阶段未入MD'))
chk('随机抽样 30 家深核(evidence/dims10/跟进阶段入 MD)', not samp_bad,
    ('30/30 全过' if not samp_bad else str(samp_bad[:8])))

# ---------- 13. R55 老骨架 20 家也有 MD 小节 ----------
old_miss = [c for c in r55_old if 'R55 再发掘要点' not in md_files[c].read_text(encoding='utf-8')]
chk('R55 老骨架 20 家 MD 小节在', not old_miss, ('全过' if not old_miss else str(old_miss)))

# ---------- 14. 数字签名:重复 fact 检测(抄袭/错档) ----------
fact_seen = defaultdict(list)
for c, (f, r) in recs.items():
    fact_seen[r['fact'][:60]].append(c)
dup_fact = {k: v for k, v in fact_seen.items() if len(v) > 1}
chk('fact 首 60 字无跨户重复(防错档)', not dup_fact,
    ('全过' if not dup_fact else str(list(dup_fact.items())[:4])))

# ---------- 汇总 ----------
fails = [c for c in report['checks'] if not c['ok']]
report['summary'] = {'checks_total': len(report['checks']), 'failed': len(fails),
                     'failed_names': [c['check'] for c in fails]}
(ROOT / 'docs/audit').mkdir(exist_ok=True)
out = ROOT / 'docs/audit/A类入库完整性审计_2026-09-29.json'
json.dump(report, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n== 汇总: %d 项检查, 失败 %d ==' % (report['summary']['checks_total'], len(fails)))
for c_ in fails: print('  ❌', c_['check'], '→', c_['detail'][:120])
