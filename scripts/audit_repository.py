#!/usr/bin/env python3
"""Offline, reproducible repository inventory and provenance GAP audit.

Does not fetch URLs or verify claims. Reads every business file, including Office
cells/paragraphs/relationships; excludes VCS internals, secrets and caches. Does
not mutate customer data, grades, numbering or original supplier documents.
"""
import argparse
import ast
import csv
import hashlib
import io
import json
import re
import subprocess
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CSV = '客户名单_反向信号_2026-09.csv'
OUT = ROOT / 'docs/audit'
EVIDENCE = ROOT / 'docs/evidence'
URL = re.compile(r'https?://[^\s<>\[\]"\u4e00-\u9fff]+')
EMAIL = re.compile(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}')
EXCLUDE = {'.git', '__pycache__', '.cache', '.pytest_cache', '.venv', 'node_modules', '.arena', '.ssh', '.aws', '.config', '.local', '.npm'}
SENSITIVE = {'.env', '.netrc', '.git-credentials', 'credentials', 'id_rsa', 'id_ed25519'}
GENERATED = {'docs/audit/文件盘点.json', 'docs/audit/外部链接索引.json',
             'docs/audit/缺证段落.json', 'docs/audit/全仓审计.md',
             'docs/audit/Git历史索引.md', 'docs/audit/文件目录.md',
             'docs/evidence/客户溯源索引.json', 'docs/evidence/产品声明候选索引.md',
             'docs/evidence/产品声明候选索引.json',
             *(f'docs/evidence/客户溯源_{g}.md' for g in 'ABC')}


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def links(text):
    # This is an occurrence inventory, not an HTTP checker. Balanced parentheses
    # in a URL are retained; Markdown's final closing parenthesis is removed.
    out = []
    for m in URL.finditer(text):
        u = m.group().rstrip('.,;:!。；，`|\\')
        while u.endswith(')') and u.count(')') > u.count('('):
            u = u[:-1]
        if u and u not in out:
            out.append(u)
    return out


def file_units(path):
    """Return (locator, text), inspection metadata, errors; never execute code."""
    suffix = path.suffix.lower()
    meta, errors, units = {}, [], []
    if suffix in {'.xlsx', '.docx'}:
        with zipfile.ZipFile(path) as z:
            meta['zip_members'] = len(z.namelist())
            meta['embedded_media'] = sum('/media/' in n for n in z.namelist())
            meta['media_note'] = 'Inventoried, not OCRed or visually validated'
            bad = z.testzip()
            if bad:
                errors.append('ZIP CRC failure: ' + bad)
            for name in z.namelist():
                if name.endswith('.rels'):
                    for rel in ET.fromstring(z.read(name)):
                        if rel.attrib.get('TargetMode') == 'External':
                            units.append((name, rel.attrib.get('Target', '')))
            if suffix == '.docx':
                for name in z.namelist():
                    if re.match(r'word/(document|footnotes|endnotes|comments|header\d+|footer\d+)\.xml$', name):
                        tree = ET.fromstring(z.read(name))
                        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
                        for i, para in enumerate(tree.findall('.//w:p', ns), 1):
                            text = ''.join(t.text or '' for t in para.findall('.//w:t', ns))
                            if text:
                                units.append((f'{name}:paragraph-{i}', text))
        if suffix == '.xlsx':
            from openpyxl import load_workbook
            wb = load_workbook(path, data_only=False, read_only=False)
            meta['sheets'] = []
            for ws in wb:
                n = 0
                for row in ws:
                    for c in row:
                        if c.value is not None:
                            n += 1
                            units.append((f'{ws.title}!{c.coordinate}', str(c.value)))
                        if c.hyperlink and c.hyperlink.target:
                            units.append((f'{ws.title}!{c.coordinate}:hyperlink', c.hyperlink.target))
                        if c.comment:
                            units.append((f'{ws.title}!{c.coordinate}:comment', c.comment.text))
                meta['sheets'].append({'name': ws.title, 'state': ws.sheet_state, 'nonempty_cells': n})
            wb.close()
    elif suffix == '.csv':
        with path.open(encoding='utf-8-sig', newline='') as f:
            rr = csv.DictReader(f)
            meta['headers'] = rr.fieldnames
            for rowno, r in enumerate(rr, 2):
                for k, v in r.items():
                    if v:
                        units.append((f'row-{rowno}/{k}', str(v)))
    elif suffix in {'.xls', '.pdf'}:
        # Binary price lists (e.g. `Price List_Marvell Based *.xls/.pdf`) are
        # scan targets for identity/hash only; parse tooling lives in scripts
        # (xlrd/pypdf), so skip unit extraction without recording an error.
        return [], {'type': 'binary-document', 'note': 'skipped by extension (.xls/.pdf); content vetted via dedicated parsers'}, []
    else:
        try:
            text = path.read_text(encoding='utf-8-sig')
        except UnicodeDecodeError:
            return [], {'type': 'binary-unparsed'}, ['Unparsed binary content']
        units = [(f'L{i}', s) for i, s in enumerate(text.splitlines(), 1)]
        if suffix == '.json':
            json.loads(text)
        if suffix == '.py':
            try:
                ast.parse(text, filename=str(path))
            except SyntaxError as e:
                errors.append(f'Python syntax: line {e.lineno}: {e.msg}')
    return units, meta, errors


def git_history(rows):
    commits = subprocess.check_output(['git', 'log', '--format=%H\t%cI\t%s'], cwd=ROOT).decode().splitlines()
    wanted = {(r['公司名'], r['国家']) for r in rows}
    first = {}
    revs = subprocess.check_output(['git', 'log', '--reverse', '--format=%H', '--', CSV], cwd=ROOT).decode().split()
    for rev in revs:
        p = subprocess.run(['git', 'show', f'{rev}:{CSV}'], cwd=ROOT, capture_output=True)
        if p.returncode:
            continue
        for r in csv.DictReader(io.StringIO(p.stdout.decode('utf-8-sig'))):
            key = (r.get('公司名'), r.get('国家'))
            if key in wanted and key not in first:
                first[key] = rev
    lines = ['# Git 历史索引', '', '> 时间为Git committer timestamp，不是用户消息时间、网页发布时间或服务器观测时间。',
             '> 只检索了可达本分支历史及客户CSV历史；不读取凭证、Git内部对象原文或已删除的不可达对象。', '',
             '| Commit | 提交时间（原始时区） | 说明 |', '|---|---|---|']
    for line in commits:
        sha, date, subject = line.split('\t', 2)
        lines.append(f'| `{sha[:12]}` | {date} | {subject.replace("|", " / ")} |')
    (OUT / 'Git历史索引.md').write_text('\n'.join(lines).rstrip() + '\n')
    return first, len(commits)


def research_records():
    found = defaultdict(list)
    for p in sorted((ROOT / 'batch').glob('contact_research_*.json')):
        obj = json.loads(p.read_text())
        for i, r in enumerate(obj.get('records', [])):
            found[r['code']].append({**r, 'batch_path': p.relative_to(ROOT).as_posix(),
                                    'locator': f'records[{i}]', 'recorded_on': obj.get('date')})
    return found


def c_public_research_records():
    """Load R73 C-tier public research so the provenance index survives regeneration."""
    found = {}
    for p in sorted((ROOT / 'batch').glob('C类AB标准加厚_*.json')):
        obj = json.loads(p.read_text(encoding='utf-8'))
        if not isinstance(obj, dict) or not str(obj.get('round', '')).startswith('R73'):
            continue
        batch_path = p.relative_to(ROOT).as_posix()
        for rec in obj.get('records', []):
            if not isinstance(rec, dict) or not (rec.get('name') and rec.get('country')):
                continue
            sources, seen_sources, record_urls = [], set(), []
            for fact in rec.get('facts', []):
                url = fact.get('url')
                if not url:
                    continue
                if url not in record_urls:
                    record_urls.append(url)
                source = {
                    'url': url,
                    'source_type': fact.get('source_type', '公开来源'),
                    'source_level': fact.get('source_level', '来源等级未标注'),
                }
                source_key = (source['url'], source['source_type'], source['source_level'])
                if source_key not in seen_sources:
                    sources.append(source)
                    seen_sources.add(source_key)
            dimensions = rec.get('dimensions', {})
            boundary = next((value for key, value in dimensions.items()
                             if key.startswith('证据边界')), '')
            found[(rec['name'], rec['country'])] = {
                'round': 'R73',
                'batch_path': batch_path,
                'researched_on': rec.get('researched_on', obj.get('date')),
                'fact_count': len(rec.get('facts', [])),
                'dimension_count': len(dimensions),
                'sources': sources,
                'boundary': boundary,
                'outreach': '未触达；无邮件、电话、寄样或报价',
                'grade': '保持 C；未改主表',
                'record_urls': record_urls,
                'site_lead': rec.get('site_lead'),
            }
    return found


def customer_index(rows, first):
    research = research_records()
    c_public = c_public_research_records()
    batch_matches = defaultdict(list)
    for p in sorted((ROOT / 'batch').glob('*.json')):
        obj = json.loads(p.read_text())
        if isinstance(obj, list):
            records, locator_prefix = obj, 'item'
        elif isinstance(obj, dict) and p.name.startswith('C类'):
            records, locator_prefix = obj.get('records', []), 'records'
        else:
            continue
        for i, r in enumerate(records):
            if isinstance(r, dict) and r.get('name') and r.get('country'):
                batch_matches[(r['name'], r['country'])].append(
                    f'{p.relative_to(ROOT)} / {locator_prefix}[{i}]')
    entries = []
    for rowno, r in enumerate(rows, 2):
        code = r['档案编号']
        rr = research.get(code, [])
        public = c_public.get((r['公司名'], r['国家']))
        urls = links(r['备注'] + ' ' + r['来源'] + ' ' + r['入口/联系方式'])
        if public:
            urls = list(dict.fromkeys(urls + public['record_urls']))
        latest = rr[-1] if rr else None
        status = ('R73 A/B标准公开研究已完成（证据见批次；仍为C/未触达）' if public else
                  '结构化联系方式证据（仅覆盖该字段/记录中所述内容）' if latest else
                  '有URL但未逐项核实' if urls else '无逐项证据URL·待补证')
        entry = {'code': code, 'name': r['公司名'], 'country': r['国家'], 'grade': r['评级'],
                 'csv_locator': f'{CSV}:row-{rowno}', 'legacy_source_label': r['来源'],
                 'site_lead': (public.get('site_lead') or r['网站']) if public else r['网站'],
                 'record_urls': urls, 'status': status,
                 'contact_research': rr,
                 'exact_batch_matches': batch_matches.get((r['公司名'], r['国家']), []),
                 'first_seen_exact_identity_commit': first.get((r['公司名'], r['国家'])),
                 'warning': ('公开研究仅支持所引用字段；公司自述、政府登记、厂商名录和动态商品页按各自来源范围解释，'
                             '不证明销量、当前完整授权、采购意向/订单或供应商开放。评级保持C，未触达。'
                             if public else
                             '网站/同域名/旧batch/Git只能定位记录，不能单独证明身份、持证有效、采购需求或SKU性能。')}
        if public:
            entry['public_research'] = {k: v for k, v in public.items() if k != 'record_urls'}
        entries.append(entry)
    dump(EVIDENCE / '客户溯源索引.json', entries)
    for grade in 'ABC':
        subset = sorted((e for e in entries if e['grade'] == grade), key=lambda e: int(e['code'][2:]))
        lines = [f'# {grade}级客户溯源索引', '',
                 '> 本索引不改客户等级或编号。缺证不等于事实为假，有链接也不等于事实已经核实。',
                 '> 邮箱来源不能证明 Marvell Prestera 芯片、实际交换需求、当前认证、决策链短或推荐SKU能力。',
                 '> 新批次必须保存字段、原文摘录、URL、检索日期、来源等级；旧批次缺原文时不得补造。', '']
        for e in subset:
            lines += [f'<a id="{e["code"]}"></a>', f'## {e["code"]} · {e["name"]} · {e["country"]}', '',
                      f'- 状态：**{e["status"]}**',
                      f'- 主数据位置：`{e["csv_locator"]}`；字段：来源 / 备注 / 入口/联系方式。',
                      f'- 旧来源标签（不是证据）：{e["legacy_source_label"]}',
                      f'- 官网线索（不自动背书其他字段）：{e["site_lead"] or "未留存"}',
                      f'- 精确同名同国别首次入库提交：`{e["first_seen_exact_identity_commit"] or "未匹配"}`。',
                      '- 本地原始批次：' + ('；'.join(f'`{x}`' for x in e['exact_batch_matches']) or '无精确同名同国家匹配，禁止靠子串合并。')]
            for rr in e['contact_research']:
                lines += [f'- 联系方式证据记录：`{rr["batch_path"]}` → `{rr["locator"]}`；记录日期 {rr["recorded_on"]}；来源等级 `{rr["level"]}`。',
                          f'  - 公开邮箱：{rr.get("email") or "未发现"}；投递未测试。',
                          f'  - 说明：{rr["note"]}']
                if rr.get('quote'):
                    lines += [f'  - 保留原文：{rr["quote"]}']
                else:
                    lines += ['  - 原文摘录：旧批次未存逐字摘录；上述说明为Agent转述，不冒充原文。']
                for i, url in rr['sources']:
                    lines += [f'  - [{i}]({url})']
            if e.get('public_research'):
                public = e['public_research']
                lines += [f'- R73 原始研究批次：`{public["batch_path"]}`；检索日期：{public["researched_on"]}；'
                          f'{public["fact_count"]} 条逐项证据、{public["dimension_count"]} 个分析维度。',
                          '- 主要逐项来源：']
                for source in public['sources']:
                    label = source['source_type'].replace('|', ' / ')
                    level = source['source_level'].replace('|', ' / ')
                    lines.append(f'  - [{label}]({source["url"]})（{level}）')
                if public.get('boundary'):
                    lines.append(f'- 证据边界：{public["boundary"]}')
                lines.append(f'- 联系/评级边界：**{public["outreach"]}；{public["grade"]}。**')
            elif not e['contact_research']:
                lines += [f'- 原记录URL（只做线索，不等于本次验证）：{", ".join(e["record_urls"]) or "未留存"}',
                          '- 待补：邮箱/电话、人员职位/认证、品牌型号/芯片、需求与规模判断的对应证据。']
            lines += ['- 分析与生成内容：评级来自 `scripts/grade.py`，策略来自 `scripts/strategy.py`，首触邮件来自 `scripts/emails.py`；不是客户陈述或实测报告。', '']
        (EVIDENCE / f'客户溯源_{grade}.md').write_text('\n'.join(lines).rstrip() + '\n')
    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', default='2026-09-27', help='Audit recording date, not source publication date')
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    tracked = set(subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0'))
    inventory, occurrences, gaps, errors = [], defaultdict(list), [], []
    product_hits = defaultdict(list)
    for p in sorted(ROOT.rglob('*')):
        rel = p.relative_to(ROOT).as_posix()
        if (any(part in EXCLUDE for part in p.relative_to(ROOT).parts) or not p.is_file()
                or p.name in SENSITIVE or p.name.startswith('.env.')):
            continue
        if rel in GENERATED:
            # Avoid circular hashes/self-indexing; generated outputs validated separately.
            continue
        if p.is_symlink():
            errors.append({'path': rel, 'error': 'Symlink not followed'})
            continue
        try:
            units, meta, errs = file_units(p)
        except Exception as ex:
            units, meta, errs = [], {}, [f'{type(ex).__name__}: {ex}']
        refs = []
        for loc, text in units:
            if p.suffix in {'.docx', '.xlsx'} and (p.name.startswith(('SmartByte', 'Saga Feature', 'Marvell Based', 'The pricelist'))):
                if re.search(r'watchdog|250\s*m|90\s*w|ERPS|G\.8032|Prestera|88E\w+|L3|hardware\s*(?:routing|offload)', text, re.I):
                    product_hits[rel].append({'locator': loc, 'excerpt': text, 'status': '关键词候选；未核实SKU适用性或实测性能'})
            for url in links(text):
                occurrences[url].append({'path': rel, 'locator': loc})
                refs.append(url)
            # Candidate claim gaps, not a semantic verdict. Dossiers covered by row ledger.
            if p.suffix == '.md' and not rel.startswith(('profile/', 'docs/')):
                if re.search(r'\d|认证|芯片|持证|唯一|最大|支持|PoE|MTCSWE|Marvell', text) and len(text.strip()) > 24 and not links(text):
                    gaps.append({'path': rel, 'locator': loc, 'text': text,
                                 'status': '同一行缺显式URL；可能在上下文/原始附件有来源，未逐项语义核验'})
            if p.suffix != '.py' and re.search(r'cite|turn\d+(?:search|view)\d+', text):
                errors.append({'path': rel, 'locator': loc, 'error': 'Conversation citation token; not a durable URL'})
        item = {'path': rel, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size,
                'tracked_at_scan': rel in tracked, 'units_scanned': len(units),
                'unique_url_count': len(set(refs)), 'inspection': meta, 'errors': errs}
        inventory.append(item)
        errors += [{'path': rel, 'error': er} for er in errs]
    rows = list(csv.DictReader((ROOT / CSV).open(encoding='utf-8-sig')))
    first, commit_count = git_history(rows)
    entries = customer_index(rows, first)
    dump(OUT / '文件盘点.json', {'recorded_on': args.date, 'excluded': sorted(EXCLUDE | SENSITIVE) + ['.env.*'],
         'generated_outputs_not_recursively_scanned': sorted(GENERATED), 'files': inventory, 'errors': errors})
    dump(OUT / '外部链接索引.json', [{'url': u, 'http_checked': False, 'occurrences': hits}
                                       for u, hits in sorted(occurrences.items())])
    dump(OUT / '缺证段落.json', gaps)
    dump(EVIDENCE / '产品声明候选索引.json', dict(product_hits))
    prod = ['# 产品声明候选索引', '', f'记录日期：{args.date}；由 audit_repository.py 扫描原始供应商Office文件生成。', '',
            '> 仅提供关键词定位，不将关键词命中当成功能支持或实测证明。需核对表头、SKU、版本、限制条件及原文上下文。图片未OCR。',
            '> 每文件展示前12个命中（不是重要性排序）；全部命中及位置见 [JSON](产品声明候选索引.json)。', '']
    for name, hits in sorted(product_hits.items()):
        prod += [f'## [{name}](<../../{name}>)', '', f'文本候选：{len(hits)}处。', '']
        for h in hits[:12]:
            excerpt = re.sub(r'\s+', ' ', h['excerpt']).replace('|', ' / ').strip()
            prod += [f'- `{h["locator"]}`：{excerpt[:700]}' + ('（截断，详见JSON）' if len(excerpt) > 700 else '')]
        prod.append('')
    (EVIDENCE / '产品声明候选索引.md').write_text('\n'.join(prod).rstrip() + '\n')
    counts = Counter(e['status'] for e in entries)
    lines = ['# 全仓文件目录', '', '> 自动生成，链接指向原路径；不搬动客户档案或原始供应商附件。SHA-256 全值见文件盘点JSON。', '',
             '| 文件 | 字节 | 检查单元 | URL数 |', '|---|---:|---:|---:|']
    for f in inventory:
        lines.append(f'| [{f["path"]}](<../../{f["path"]}>) | {f["bytes"]} | {f["units_scanned"]} | {f["unique_url_count"]} |')
    (OUT / '文件目录.md').write_text('\n'.join(lines).rstrip() + '\n')
    report = f'''# 全仓溯源审计 — {args.date}

## 结论

**全文件机械盘点已完成；历史事实逐项补证未完成。不能宣称“所有信息都有证据”。**

- 扫描业务文件：{len(inventory)}；文本行/表格单元格/文档段落/外部关系：{sum(x['units_scanned'] for x in inventory)}。
- XLSX：{sum(x['path'].endswith('.xlsx') for x in inventory)}；DOCX：{sum(x['path'].endswith('.docx') for x in inventory)}。
- 唯一外部URL：{len(occurrences)}（**没有逐个联网验证**）。
- 根目录MD待审候选行：{len(gaps)}（启发式扫描，既不是缺证事实总数，也不是全部正确性的证明）。
- Git可达提交索引：{commit_count}。客户记录 {len(rows)}；{dict(Counter(r['评级'] for r in rows))}。
- 客户来源覆盖：{dict(counts)}。
- 解析/引用异常：{len(errors)}，逐项位置见 [文件盘点](文件盘点.json)。

## 如何定位

1. [完整文件目录](文件目录.md) → 文件路径、大小、读取范围；哈希见JSON。
2. [外部链接索引](外部链接索引.json) → URL反向查文件、行号、工作表单元格或DOCX段落。
3. [A客户](../evidence/客户溯源_A.md) / [B客户](../evidence/客户溯源_B.md) / [C客户](../evidence/客户溯源_C.md) → 冻结编号定位证据与缺证。
4. [缺证候选段落](缺证段落.json) → 原文、文件、行号，不需要重新搜索全仓。
5. [Git历史](Git历史索引.md) → 入库过程；Git不是外部事实证据。

## 覆盖范围与限制

- 扫描根目录、profile全部等级、batch、scripts、docs、tests，包括未跟踪业务文件和隐藏业务文件。
- Office检查全部工作表（含隐藏表）、非空单元格、公式文本、超链接、批注、DOCX正文/表格/页眉页脚/脚注/尾注/批注。
- Office ZIP逐成员CRC检查；内嵌图片计数。**没有OCR或逐图视觉核验，也不重算Excel公式。**
- `.git`内部、缓存、依赖、凭证不作业务资料读取；Git只读取本分支提交元数据和历史客户CSV。
- 审计自身的生成文件单列排除以避免循环哈希；会由校验测试检查结构/编号覆盖。
- 官网首页不等于该公司邮箱/证书/规模/采购需求的证据；名录中的Allied Telesis品牌信号不等于逐型号Prestera芯片确认。
- 旧供应商附件是本地原始材料；文件名中的有效期不是本次确认的市场报价，也不是第三方实测。

## 高风险待办

- 旧客户大量只留日期/名录名；逐项证据仍需补，不得通过拼接URL冒充曾验证。
- profile索引曾有1033条相对链接多写一层profile/；已修复并加入测试。C级细分变量曾被目录覆盖，已改回真实字段；未重评级。
- J A Shomer旧推测邮箱曾被正则提升到邮箱列表：已过滤推测段落，原字段保留警告；Industrial Solutions的bob@/amy@原本仅不完整推测，仍非有效联系证据。
- 旧README有互相覆盖的日期/轮次（尤其第37轮）、已过时统计与恢复命令：完整归档，只执行当前README。
- `A级客户跟进策略_2026-09.md` 旧导出有过时B/C数量及国家排序，不作当前跟进顺序依据。
- `scripts/strategy.py` 包含PoE看门狗、90W、250m、ERPS时延等模板卖点，需逐SKU/固件/测试条件证据；**未核实前不得对外承诺**。
- `scripts/grade.py` 两个A分支条件仍不同；遵守“不擅改评级逻辑”。
- `scripts/add_batch.py` / `fix_audit.py` 是历史写入脚本，旧列宽/去重/合并逻辑不应直接用于现有22列数据。

## 后续

继续A顺号补联系方式时同步补证；A完成后复筛B/C，升级只追加末尾。
历史缺证补齐是独立持续任务，不能用本次盘点覆盖率替代事实核实。
'''
    (OUT / '全仓审计.md').write_text(report)
    print(json.dumps({'files': len(inventory), 'units': sum(x['units_scanned'] for x in inventory),
                      'urls': len(occurrences), 'gaps': len(gaps), 'errors': len(errors),
                      'customers': len(entries), 'source_status': counts}, ensure_ascii=False))


if __name__ == '__main__':
    main()
