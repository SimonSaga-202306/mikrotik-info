"""Offline regression checks; never modify live customer data or send traffic."""
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import audit_repository as audit
from make_profiles import emails, without_contact_evidence
from numbering import renumber

CSV = '客户名单_反向信号_2026-09.csv'
BASELINE = '5ac5c56'  # Governance baseline; cumulative A200–A299 contact-only allowance.
CONTACT_BASELINE = 'f974d9c'  # Before R48; R48 promotions and R49 email backfills carry explicit allowances below.


def git_file(path):
    return subprocess.check_output(['git', 'show', f'{BASELINE}:{path}'], cwd=ROOT)


def read_csv():
    with (ROOT / CSV).open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.header, cls.rows = read_csv()
        cls.by_code = {r['档案编号']: r for r in cls.rows}

    PROMOTED_OLD = {'B-070', 'B-272', 'B-465', 'B-416', 'B-361', 'B-175'}   # R48 B/C rescreen
    PROMOTED_NEW = {'A-379', 'A-380', 'A-381', 'A-382', 'A-383', 'A-384'}
    PROMOTED_FIELDS = {'评级', '档案编号', '评级依据', '人工定级', '备注'}
    # R49: 23 C rows regained an official mailbox -> back to B (renumbered, row stays in place).
    R49_OLD_TO_NEW = {'C-168': 'B-513', 'C-173': 'B-514', 'C-176': 'B-515', 'C-178': 'B-516',
                      'C-191': 'B-517', 'C-194': 'B-518', 'C-197': 'B-519', 'C-199': 'B-520',
                      'C-204': 'B-521', 'C-205': 'B-522', 'C-209': 'B-523', 'C-210': 'B-524',
                      'C-215': 'B-525', 'C-216': 'B-526', 'C-226': 'B-527', 'C-227': 'B-528',
                      'C-228': 'B-529', 'C-272': 'B-530', 'C-282': 'B-531', 'C-284': 'B-532',
                      'C-285': 'B-533', 'C-291': 'B-534', 'C-298': 'B-535'}
    R49_C_TO_B_FIELDS = {'评级', '档案编号', '评级依据', '备注', '入口/联系方式', 'C级细分'}
    R49_NOTE_ONLY = {'C-152', 'C-183', 'C-195', 'C-208', 'C-212', 'C-214', 'C-218', 'C-223',
                     'C-279', 'C-296', 'B-344', 'B-340', 'B-356', 'B-510', 'B-442', 'B-401',
                     'B-463', 'B-258', 'B-378', 'B-226'}
    R49_A_CONTENT = {'A-044', 'A-046'}
    R49_A_FIELDS = {'入口/联系方式', '备注'}

    # R50: 存量全表复核提炼 A 类 -> 37 条 B 升 A-385..A-421；31 条去重提示（本轮写入 29 条备注）。
    R50_PROMOTED = {
        'B-006': 'A-385', 'B-020': 'A-386', 'B-025': 'A-387', 'B-029': 'A-388', 'B-045': 'A-389',
        'B-050': 'A-390', 'B-074': 'A-391', 'B-102': 'A-392', 'B-109': 'A-393', 'B-122': 'A-394',
        'B-145': 'A-395', 'B-161': 'A-396', 'B-172': 'A-397', 'B-181': 'A-398', 'B-198': 'A-399',
        'B-199': 'A-400', 'B-212': 'A-401', 'B-226': 'A-402', 'B-243': 'A-403', 'B-257': 'A-404',
        'B-267': 'A-405', 'B-293': 'A-406', 'B-302': 'A-407', 'B-309': 'A-408', 'B-317': 'A-409',
        'B-356': 'A-410', 'B-357': 'A-411', 'B-378': 'A-412', 'B-441': 'A-413', 'B-447': 'A-414',
        'B-463': 'A-415', 'B-472': 'A-416', 'B-473': 'A-417', 'B-475': 'A-418', 'B-478': 'A-419',
        'B-483': 'A-420', 'B-511': 'A-421',
    }
    R50_PROMOTED_NEW = set(R50_PROMOTED.values())
    R50_PROMOTED_FIELDS = {'评级', '档案编号', '评级依据', '人工定级', '备注'}
    R50_NOTE_ONLY = {'B-011', 'B-044', 'C-159', 'C-167', 'B-083', 'B-113', 'B-135', 'B-141',
                     'B-149', 'B-158', 'B-182', 'B-207', 'B-288', 'B-290', 'B-297', 'B-299',
                     'B-430', 'B-432', 'B-437', 'B-440', 'B-442', 'B-443', 'C-011', 'C-014',
                     'C-065', 'C-067', 'C-098', 'C-131', 'C-145'}
    # R51: 用户规则「达到 A 级标准就可以升级」-> R50 去重提示里够标准的 9 条 B 行升 A-422..A-430。
    R51_PROMOTED = {'B-083': 'A-422', 'B-149': 'A-423', 'B-207': 'A-424', 'B-288': 'A-425',
                    'B-430': 'A-426', 'B-432': 'A-427', 'B-437': 'A-428', 'B-442': 'A-429',
                    'B-443': 'A-430'}
    R51_PROMOTED_NEW = set(R51_PROMOTED.values())
    R51_PROMOTED_FIELDS = {'评级', '档案编号', '评级依据', '人工定级', '备注'}
    # R52: 31 条重复提示行收尾 -> C-011 Kerberos 补升 A-431（原 C 判定「大型」为模板词误伤）。
    R52_PROMOTED = {'C-011': 'A-431'}
    R52_PROMOTED_NEW = set(R52_PROMOTED.values())
    R52_PROMOTED_FIELDS = {'评级', '档案编号', '评级依据', '人工定级', '备注', 'C级细分'}
    # R53: B 段逐站复筛（283 条带网站 B 行，按 CSV 顺序）达标升级 -> 136 条 B 升 A-432..A-567。
    R53_PROMOTED = {
        'B-010': 'A-432',
        'B-014': 'A-433',
        'B-015': 'A-434',
        'B-016': 'A-435',
        'B-017': 'A-436',
        'B-019': 'A-437',
        'B-027': 'A-438',
        'B-028': 'A-439',
        'B-030': 'A-440',
        'B-033': 'A-441',
        'B-044': 'A-442',
        'B-049': 'A-443',
        'B-063': 'A-444',
        'B-067': 'A-445',
        'B-068': 'A-446',
        'B-069': 'A-447',
        'B-073': 'A-448',
        'B-075': 'A-449',
        'B-077': 'A-450',
        'B-078': 'A-451',
        'B-079': 'A-452',
        'B-513': 'A-453',
        'B-086': 'A-454',
        'B-087': 'A-455',
        'B-089': 'A-456',
        'B-091': 'A-457',
        'B-092': 'A-458',
        'B-093': 'A-459',
        'B-095': 'A-460',
        'B-096': 'A-461',
        'B-097': 'A-462',
        'B-098': 'A-463',
        'B-099': 'A-464',
        'B-100': 'A-465',
        'B-101': 'A-466',
        'B-104': 'A-467',
        'B-112': 'A-468',
        'B-113': 'A-469',
        'B-114': 'A-470',
        'B-117': 'A-471',
        'B-118': 'A-472',
        'B-120': 'A-473',
        'B-125': 'A-474',
        'B-135': 'A-475',
        'B-136': 'A-476',
        'B-137': 'A-477',
        'B-515': 'A-478',
        'B-141': 'A-479',
        'B-516': 'A-480',
        'B-143': 'A-481',
        'B-144': 'A-482',
        'B-146': 'A-483',
        'B-147': 'A-484',
        'B-156': 'A-485',
        'B-158': 'A-486',
        'B-167': 'A-487',
        'B-170': 'A-488',
        'B-171': 'A-489',
        'B-174': 'A-490',
        'B-179': 'A-491',
        'B-182': 'A-492',
        'B-518': 'A-493',
        'B-190': 'A-494',
        'B-195': 'A-495',
        'B-196': 'A-496',
        'B-519': 'A-497',
        'B-206': 'A-498',
        'B-209': 'A-499',
        'B-216': 'A-500',
        'B-227': 'A-501',
        'B-521': 'A-502',
        'B-229': 'A-503',
        'B-236': 'A-504',
        'B-241': 'A-505',
        'B-245': 'A-506',
        'B-247': 'A-507',
        'B-255': 'A-508',
        'B-525': 'A-509',
        'B-258': 'A-510',
        'B-259': 'A-511',
        'B-526': 'A-512',
        'B-262': 'A-513',
        'B-266': 'A-514',
        'B-273': 'A-515',
        'B-275': 'A-516',
        'B-282': 'A-517',
        'B-287': 'A-518',
        'B-289': 'A-519',
        'B-290': 'A-520',
        'B-297': 'A-521',
        'B-299': 'A-522',
        'B-300': 'A-523',
        'B-529': 'A-524',
        'B-303': 'A-525',
        'B-306': 'A-526',
        'B-318': 'A-527',
        'B-321': 'A-528',
        'B-322': 'A-529',
        'B-326': 'A-530',
        'B-330': 'A-531',
        'B-334': 'A-532',
        'B-337': 'A-533',
        'B-342': 'A-534',
        'B-344': 'A-535',
        'B-350': 'A-536',
        'B-351': 'A-537',
        'B-353': 'A-538',
        'B-355': 'A-539',
        'B-362': 'A-540',
        'B-363': 'A-541',
        'B-364': 'A-542',
        'B-365': 'A-543',
        'B-373': 'A-544',
        'B-383': 'A-545',
        'B-391': 'A-546',
        'B-395': 'A-547',
        'B-530': 'A-548',
        'B-399': 'A-549',
        'B-404': 'A-550',
        'B-414': 'A-551',
        'B-419': 'A-552',
        'B-424': 'A-553',
        'B-427': 'A-554',
        'B-429': 'A-555',
        'B-534': 'A-556',
        'B-445': 'A-557',
        'B-446': 'A-558',
        'B-448': 'A-559',
        'B-451': 'A-560',
        'B-454': 'A-561',
        'B-460': 'A-562',
        'B-461': 'A-563',
        'B-470': 'A-564',
        'B-476': 'A-565',
        'B-535': 'A-566',
        'B-492': 'A-567',
    }
    R53_PROMOTED_NEW = set(R53_PROMOTED.values())
    R53_PROMOTED_FIELDS = {'评级', '档案编号', '评级依据', '人工定级', '备注', 'C级细分'}
    PROMOTED_MAP = {'B-070': 'A-379', 'B-272': 'A-380', 'B-465': 'A-381', 'B-416': 'A-382',
                    'B-361': 'A-383', 'B-175': 'A-384', **R50_PROMOTED, **R51_PROMOTED, **R52_PROMOTED,
                    **R53_PROMOTED}

    @classmethod
    def r49_allowed(cls, code):
        if code in cls.R49_OLD_TO_NEW:
            return cls.R49_C_TO_B_FIELDS
        if code in cls.R49_NOTE_ONLY:
            return {'备注'}
        if code in cls.R49_A_CONTENT:
            return cls.R49_A_FIELDS
        return None

    @classmethod
    def r50_allowed(cls, code):
        if code in cls.R50_PROMOTED:
            return cls.R50_PROMOTED_FIELDS
        if code in cls.R50_NOTE_ONLY:
            return {'备注'}
        return None

    @classmethod
    def r51_allowed(cls, code):
        if code in cls.R51_PROMOTED:
            return cls.R51_PROMOTED_FIELDS
        return None

    @classmethod
    def r52_allowed(cls, code):
        if code in cls.R52_PROMOTED:
            return cls.R52_PROMOTED_FIELDS
        return None

    @classmethod
    def r53_allowed(cls, code):
        if code in cls.R53_PROMOTED:
            return cls.R53_PROMOTED_FIELDS
        return None

    def grade_now(self, code):
        # R50/R51 升级行已改号：按升级映射取当前行，其余取原号。
        return self.by_code[self.PROMOTED_MAP.get(code, code)]['评级']

    def test_frozen_identity_and_physical_order(self):
        baseline = list(csv.DictReader(io.StringIO(git_file(CSV).decode('utf-8-sig'))))
        # Physical order stays frozen by 公司名/国家; R48 promotions keep the row in place and only
        # change 评级/档案编号 (+ the R48 reason/note fields), so those positions are compared with
        # the promotion map applied instead of raw equality.
        pos = lambda r: (r['公司名'], r['国家'])
        self.assertEqual([pos(r) for r in baseline], [pos(r) for r in self.rows])
        targets = {f'A-{n:03}' for n in range(200, 379)}
        for before, after in zip(baseline, self.rows):
            allowed = (self.r53_allowed(before['档案编号']) or self.r52_allowed(before['档案编号'])
                       or self.r51_allowed(before['档案编号']) or self.r50_allowed(before['档案编号'])
                       or self.r49_allowed(before['档案编号']))
            if before['档案编号'] in self.PROMOTED_MAP:
                self.assertEqual(after['档案编号'], self.PROMOTED_MAP[before['档案编号']])
                self.assertEqual(after['评级'], 'A')
                extra = (self.R52_PROMOTED_FIELDS if (before['档案编号'] in self.R52_PROMOTED
                                                                              or before['档案编号'] in self.R53_PROMOTED) else set())
                for k in self.header:
                    if k not in self.PROMOTED_FIELDS and k not in extra:
                        self.assertEqual(before[k], after[k], (before['档案编号'], k))
            elif allowed is not None:
                # R49: only the email-backfill fields may differ; the row keeps its position.
                if before['档案编号'] in self.R49_OLD_TO_NEW:
                    mapped = self.R49_OLD_TO_NEW[before['档案编号']]
                    if mapped in self.R53_PROMOTED:
                        # R53 B 段复筛达标升级：R49 回升行再次改号为 A-5xx
                        self.assertEqual(after['档案编号'], self.R53_PROMOTED[mapped])
                        self.assertEqual(after['评级'], 'A')
                        for k in self.header:
                            if k not in (allowed | self.R53_PROMOTED_FIELDS):
                                self.assertEqual(before[k], after[k], (before['档案编号'], k))
                        continue
                    self.assertEqual(after['档案编号'], mapped)
                    self.assertEqual(after['评级'], 'B')
                for k in self.header:
                    if k not in allowed:
                        self.assertEqual(before[k], after[k], (before['档案编号'], k))
            elif before['档案编号'] not in targets:
                self.assertEqual(before, after)
            else:
                self.assertTrue(all(before[k] == after[k] for k in self.header
                                    if k not in {'网站', '入口/联系方式', '备注', '评级依据'}))

    def test_first_49_dossiers_frozen_except_r49_content(self):
        # 2026-09-28 用户授权：前 49 位内容可编辑，位置/编号仍冻结。
        # R54 起 A-001 起逐批（第 1–4 批已到 A-080）允许追加「深度加厚 / 原文证据摘录 / 3 步跟进计划」三段
        # （后续小节号顺延；本测试仍只覆盖前 49 位）。
        first = sorted(p for p in (ROOT / 'profile/A').glob('A-*.md') if int(p.name[2:5]) <= 49)
        self.assertEqual(len(first), 49)
        self.assertEqual([p.name[:5] for p in first], [f'A-{n:03}' for n in range(1, 50)])
        editable = {'A-044', 'A-046'}
        r54 = {f'A-{n:03}' for n in range(1, 221)}
        mutable_lines = ('- **邮箱**', '- **电话**', '- **原始联系字段**', '- **原备注**', '| 原备注 |')
        renumber = {'## 九、注意点': '## 六、注意点',
                    '## 十、首触邮件（可直接发送）': '## 七、首触邮件（可直接发送）',
                    '## 十一、跟进记录': '## 八、跟进记录'}

        def strip_r54(text):
            """去掉 R54 新增的三段并把后续小节号退回 R49 前的编号。"""
            out, skip = [], False
            for line in text.splitlines():
                if line.startswith('## '):
                    skip = 'R54' in line
                    if skip:
                        continue
                if not skip:
                    out.append(renumber.get(line, line))
            return '\n'.join(out) + '\n'

        for p in first:
            base = git_file(p.relative_to(ROOT).as_posix()).decode('utf-8')
            cur = p.read_text(encoding='utf-8')
            if p.name[:5] in r54:
                self.assertIn('R54', cur)
                self.assertEqual(cur.count('### 第 '), 3, p.name)
                self.assertNotIn('深度加厚', strip_r54(cur), p.name)
                comparable = strip_r54(cur)
            elif p.name[:5] in editable:
                self.assertIn('R49', cur)
                comparable = cur
            else:
                self.assertEqual(cur, base, p.name)
                continue

            def blocks(text):
                out, key = {}, '(head)'
                for line in text.splitlines(keepends=True):
                    if line.startswith('## '):
                        key = line.strip()
                    out[key] = out.get(key, '') + line
                return out

            b, c = blocks(base), blocks(comparable)
            self.assertEqual(list(b), list(c), p.name)
            for key in b:
                if key in ('## 二、公司概览', '## 三、人员与联系方式'):
                    missing = [ln for ln in b[key].splitlines() if ln.strip()
                               and ln not in comparable and not ln.startswith(mutable_lines)]
                    self.assertEqual(missing, [], (p.name, key, missing[:2]))
                elif key == '## 四、品牌与技术栈':
                    # R49 证据摘录可能引入新品牌名 → 只允许“品牌集合是原集合的超集”。
                    bb = re.search(r'：(.+)', b[key]).group(1).split('、')
                    cb = re.search(r'：(.+)', c[key]).group(1).split('、')
                    self.assertTrue(set(bb) <= set(cb), (p.name, set(bb) - set(cb)))
                else:
                    self.assertEqual(c[key], b[key], (p.name, key))

    def test_r54_enrichment_matches_dossiers(self):
        # 2026-09-28 R54：A 类逐户加厚 = 10 个维度 + 原文证据摘录 + 恰好 3 步跟进计划。
        # 数据源 batch/A类加厚_*.json 是唯一事实源；profile/ 由 make_profiles.py 渲染，不许手改。
        batches = {1: range(1, 21), 2: range(21, 41), 3: range(41, 61), 4: range(61, 81), 5: range(81, 101), 6: range(101, 121), 7: range(121, 141), 8: range(141, 161), 9: range(161, 181), 10: range(181, 201), 11: range(201, 221)}
        for batch, codes in batches.items():
            data = json.loads((ROOT / f'batch/A类加厚_2026-09-28_R54_第{batch}批.json').read_text(encoding='utf-8'))
            self.assertEqual(data['batch'], batch)
            self.assertEqual([r['code'] for r in data['records']], [f'A-{n:03}' for n in codes])
            for rec in data['records']:
                self._assert_r54_record(rec)

    def _assert_r54_record(self, rec):
        self.assertEqual([s['step'] for s in rec['followup_plan']], [1, 2, 3], rec['code'])
        self.assertTrue(len(rec['dimensions']) >= 8, rec['code'])
        self.assertTrue(rec['facts'] and rec['sources'], rec['code'])
        for f in rec['facts']:
            self.assertIn(f['url'], [s[1] for s in rec['sources']], (rec['code'], f['url']))
        p = next((ROOT / 'profile/A').glob(rec['code'] + '-*.md'))
        text = p.read_text(encoding='utf-8')
        for head in ('## 六、深度加厚（R54 逐户调研）', '## 七、原文证据摘录（R54）',
                     '## 八、3 步跟进计划（R54，**最多 3 次**）'):
            self.assertIn(head, text, rec['code'])
        self.assertEqual(text.count('### 第 '), 3, rec['code'])
        self.assertEqual([ln for ln in text.splitlines() if ln.startswith('### 第 ')],
                         [f'### 第 {n} 次跟进 · ' + next(
                             s for s in rec['followup_plan'] if s['step'] == n)['stage'].split('·', 1)[-1].strip()
                          for n in (1, 2, 3)], rec['code'])
        for f in rec['facts']:
            self.assertIn(f['quote'].splitlines()[0][:40], text, rec['code'])
            self.assertIn(f['url'], text, rec['code'])
        for st in rec['followup_plan']:
            for field in ('product', 'angle', 'question', 'proof'):
                self.assertIn(st[field], text, (rec['code'], field))

    def test_dossier_identity_and_c_subdivision(self):
        files = list((ROOT / 'profile').glob('[ABC]/*.md'))
        self.assertEqual(len(files), len(self.rows))
        self.assertEqual({p.name[:5] for p in files}, set(self.by_code))
        for p in files:
            r = self.by_code[p.name[:5]]
            text = p.read_text()
            self.assertIn(f'档案编号 `{r["档案编号"]}`', text)
            self.assertTrue(text.startswith('# ' + r['公司名'] + '\n'))
            if r['评级'] == 'C':
                self.assertIn(f'C 级细分：`{r["C级细分"]}`', text)
                self.assertNotIn('C 级细分：`profile/', text)
                self.assertIn('总表 22 列', text)

    def test_every_profile_index_link_resolves(self):
        p = ROOT / 'profile/00-索引.md'
        targets = re.findall(r'\]\(<([^>]+)>\)', p.read_text())
        self.assertEqual(len(targets), len(self.rows))
        for t in targets:
            self.assertTrue((p.parent / t).is_file(), t)

    def test_guesses_are_not_extracted_as_found(self):
        s = self.by_code['A-077']['入口/联系方式']
        self.assertIn('sales@jashomer.com', emails(s))
        self.assertNotIn('czaugg@jashomer.com', emails(s))
        self.assertEqual(emails('public@example.org；guess@example.org（推测）'), ['public@example.org'])
        self.assertEqual(emails('a@example.org; b@example.org'), ['a@example.org', 'b@example.org'])

    def test_append_does_not_fill_gaps(self):
        hdr = [''] * 17 + ['评级', '评级依据', '档案编号']
        data = [[''] * 17 + [g, '', code] for g, code in [('A', 'A-001'), ('A', 'A-003'), ('A', ''), ('A', 'B-005')]]
        renumber(data, hdr, verbose=False)
        self.assertEqual([r[-1] for r in data], ['A-001', 'A-003', 'A-004', 'A-005'])

    def test_evidence_coverage_and_new_batch(self):
        entries = json.loads((ROOT / 'docs/evidence/客户溯源索引.json').read_text())
        self.assertEqual({e['code'] for e in entries}, set(self.by_code))
        self.assertEqual(len(entries), len(self.rows))
        for e in entries:
            row = self.by_code[e['code']]
            self.assertEqual((e['name'], e['country']), (row['公司名'], row['国家']))
            doc = (ROOT / f'docs/evidence/客户溯源_{e["grade"]}.md').read_text()
            self.assertIn(f'id="{e["code"]}"', doc)
        for low, high in [(200, 210), (210, 240), (240, 260), (260, 280), (280, 300), (300, 320), (320, 340), (340, 360), (360, 379)]:
            path = ROOT / f'batch/contact_research_2026-09-27_A{low}-A{high-1}.json'
            batch = json.loads(path.read_text())['records']
            self.assertEqual([r['code'] for r in batch], [f'A-{n:03}' for n in range(low, high)])
            for r in batch:
                row = self.by_code[r['code']]
                self.assertEqual(row['公司名'], r['name'])
                self.assertTrue(r['quote'] and r['fields_supported'] and r['retrieved_on'])
                if r['email']:
                    self.assertIn(r['email'], row['入口/联系方式'])
                for _, u in r['sources']:
                    self.assertIn(u, row['备注'])

    def test_current_round_promotion_fields_and_frozen_exports(self):
        def old(path):
            return subprocess.check_output(['git', 'show', f'{CONTACT_BASELINE}:{path}'], cwd=ROOT)
        baseline = list(csv.DictReader(io.StringIO(old(CSV).decode('utf-8-sig'))))
        self.assertEqual(len(baseline), len(self.rows))
        for before, after in zip(baseline, self.rows):
            allowed = (self.r53_allowed(before['档案编号']) or self.r52_allowed(before['档案编号'])
                       or self.r51_allowed(before['档案编号']) or self.r50_allowed(before['档案编号'])
                       or self.r49_allowed(before['档案编号']))
            if before['档案编号'] in self.PROMOTED_MAP:
                self.assertEqual(after['档案编号'], self.PROMOTED_MAP[before['档案编号']])
                extra = (self.R52_PROMOTED_FIELDS if (before['档案编号'] in self.R52_PROMOTED
                                                                              or before['档案编号'] in self.R53_PROMOTED) else set())
                for k in self.header:
                    if k not in self.PROMOTED_FIELDS and k not in extra:
                        self.assertEqual(before[k], after[k], (before['档案编号'], k))
            elif allowed is not None:
                if before['档案编号'] in self.R49_OLD_TO_NEW:
                    mapped = self.R49_OLD_TO_NEW[before['档案编号']]
                    if mapped in self.R53_PROMOTED:
                        self.assertEqual(after['档案编号'], self.R53_PROMOTED[mapped])
                        self.assertEqual(after['评级'], 'A')
                        for k in self.header:
                            if k not in (allowed | self.R53_PROMOTED_FIELDS):
                                self.assertEqual(before[k], after[k], (before['档案编号'], k))
                        continue
                    self.assertEqual(after['档案编号'], mapped)
                    self.assertEqual(after['评级'], 'B')
                for k in self.header:
                    if k not in allowed:
                        self.assertEqual(before[k], after[k], (before['档案编号'], k))
            else:
                self.assertEqual(before, after)
        from openpyxl import load_workbook
        skip = (self.PROMOTED_OLD | self.PROMOTED_NEW | set(self.R49_OLD_TO_NEW)
                | set(self.R49_OLD_TO_NEW.values()) | self.R49_NOTE_ONLY | self.R49_A_CONTENT
                | set(self.R50_PROMOTED) | self.R50_PROMOTED_NEW | self.R50_NOTE_ONLY
                | set(self.R51_PROMOTED) | self.R51_PROMOTED_NEW
                | set(self.R52_PROMOTED) | self.R52_PROMOTED_NEW
                | set(self.R53_PROMOTED) | self.R53_PROMOTED_NEW)
        workbook = '客户分级跟进表_2026-09.xlsx'
        a = load_workbook(io.BytesIO(old(workbook)), read_only=True)
        b = load_workbook(ROOT / workbook, read_only=True)
        self.assertEqual(a.sheetnames, b.sheetnames)
        for name in a.sheetnames:
            av, bv = list(a[name].values), list(b[name].values)
            if name in a.sheetnames[:3]:
                # promoted rows move between grade sheets; every other row must be byte-identical
                self.assertEqual(list(av[0]), list(bv[0]))
                self.assertEqual([r for r in av[1:] if str(r[19]) not in skip],
                                 [r for r in bv[1:] if str(r[19]) not in skip], name)
            else:
                self.assertEqual(av, bv, name)
        self.assertEqual(len(list(b['A级-重点好跟进'].values)) - 1, 567)
        self.assertEqual(len(list(b['B级-慢慢跟'].values)) - 1, 179)
        self.assertEqual(len(list(b['C级-难啃'].values)) - 1, 287)
        a.close()
        b.close()
        workbook2 = 'MikroTik_vs_SmartByte_替代对照表.xlsx'
        c = load_workbook(io.BytesIO(old(workbook2)), read_only=True)
        d = load_workbook(ROOT / workbook2, read_only=True)
        self.assertEqual(c.sheetnames, d.sheetnames)
        for name in c.sheetnames:
            cv, dv = list(c[name].values), list(d[name].values)
            if name == '反向信号名单':
                self.assertEqual(list(cv[0]), list(dv[0]))
                self.assertEqual([r for r in cv[1:] if str(r[19]) not in skip],
                                 [r for r in dv[1:] if str(r[19]) not in skip], name)
            else:
                self.assertEqual(cv, dv, name)
        c.close()
        d.close()

    def test_r40_source_limits_not_silently_promoted(self):
        records = json.loads((ROOT / 'batch/contact_research_2026-09-27_A210-A239.json').read_text())['records']
        by_code = {r['code']: r for r in records}
        expected = {'A-212': 'leads-only', 'A-213': 'association', 'A-215': 'official-search-only',
                    'A-218': 'official-pdf-historical', 'A-227': 'official-identity-pending',
                    'A-230': 'public-register', 'A-233': 'official-search-only',
                    'A-236': 'official-pdf-historical'}
        for code, level in expected.items():
            self.assertEqual(by_code[code]['level'], level)
            self.assertIn(level, self.by_code[code]['备注'])
        self.assertFalse(by_code['A-212']['email'])
        for code in ['A-222', 'A-225']:
            self.assertIn('(at)', by_code[code]['quote'])
            self.assertEqual(by_code[code]['level'], 'official-obfuscated')
        self.assertEqual(self.by_code['A-227']['城市'], 'Olsztyn')
        self.assertEqual(self.by_code['A-227']['网站'], '')
        self.assertEqual(self.by_code['A-236']['网站'], 'satelithuset.se')

    def test_contact_evidence_cannot_change_strategy_or_mail(self):
        note = '伙伴等级：Resell。 【2026-09-27 A210–A239联络核验】Campus Q；旧产品经理新闻；bad@example.org'
        self.assertEqual(without_contact_evidence(note), '伙伴等级：Resell。')
        self.assertEqual(without_contact_evidence('legacy campus customer'), 'legacy campus customer')
        r49 = '核心事实。【2026-09-28 R49 邮箱补录】…official-company…【2026-09-28 R49 复核】more'
        self.assertEqual(without_contact_evidence(r49), '核心事实。')
        def strip_r54_injection(tail):
            """去掉 R54 注入的 §六/§七/§八，并把被顺延的旧段序号还原（九→六、十→七、十一→八）。"""
            parts = tail.split('\n## 六、深度加厚', 1)
            if len(parts) == 1:
                return tail
            head, rest = parts
            _, rest = rest.split('\n## 九、注意点', 1)
            tail = head + '\n## 六、注意点' + rest
            return (tail
                    .replace('\n## 十、首触邮件', '\n## 七、首触邮件')
                    .replace('\n## 十一、跟进记录', '\n## 八、跟进记录'))
        for p in (ROOT / 'profile/A').glob('A-*.md'):
            if not 210 <= int(p.name[2:5]) < 379:
                continue
            old = subprocess.check_output(['git', 'show', f'{CONTACT_BASELINE}:{p.relative_to(ROOT)}'], cwd=ROOT).decode()
            marker = '## 四、品牌与技术栈'
            self.assertEqual(strip_r54_injection(p.read_text().split(marker, 1)[1]),
                             strip_r54_injection(old.split(marker, 1)[1]), p.name)
        young = next((ROOT / 'profile/A').glob('A-233-*.md')).read_text()
        self.assertIn('- **邮箱**：info@young.hu\n', young)
        self.assertNotIn('work on A210', young)

    def test_r41_legacy_mailboxes_not_promoted_and_source_tiers(self):
        records = json.loads((ROOT / 'batch/contact_research_2026-09-27_A240-A259.json').read_text())['records']
        by_code = {r['code']: r for r in records}
        self.assertEqual(sum(bool(r['email']) for r in records), 17)
        self.assertEqual(sum(r['level'].startswith('official') and r['level'] != 'official-search-only'
                             for r in records), 14)
        for code in ['A-249', 'A-251']:
            r = by_code[code]
            self.assertEqual(r['level'], 'local-legacy-unverified')
            self.assertFalse(r['email'])
            self.assertTrue(r['local_sources'])
            self.assertEqual(self.by_code[code]['网站'], '')
            self.assertEqual(emails(self.by_code[code]['入口/联系方式']), [])
            profile = next((ROOT / 'profile/A').glob(code + '-*.md')).read_text()
            self.assertIn('- **邮箱**：—\n', profile)
            self.assertIn('来源等级：local-legacy-unverified', profile)
        self.assertFalse(by_code['A-258']['email'])
        self.assertEqual(by_code['A-258']['level'], 'leads-only')
        self.assertEqual(by_code['A-253']['level'], 'official-search-only')
        self.assertEqual(by_code['A-243']['level'], 'public-register')
        self.assertEqual(by_code['A-252']['level'], 'public-register-company')
        self.assertEqual(by_code['A-241']['email'], 'm.polainer@triotronik.com')
        self.assertIn('(at)', by_code['A-247']['quote'])
        self.assertIn('[at]', by_code['A-254']['quote'])
        self.assertEqual(self.by_code['A-248']['城市'], 'Las Palmas de Gran Canaria')

    def test_r42_official_sources_and_unresolved_mailboxes(self):
        records = json.loads((ROOT / 'batch/contact_research_2026-09-27_A260-A279.json').read_text())['records']
        by_code = {r['code']: r for r in records}
        self.assertEqual(len(records), 20)
        self.assertEqual(sum(bool(r['email']) for r in records), 18)
        self.assertEqual(sum(r['level'].startswith('official') and r['level'] != 'official-search-only'
                             for r in records), 16)
        for code in ['A-272', 'A-279']:
            r = by_code[code]
            self.assertEqual(r['level'], 'leads-only')
            self.assertFalse(r['email'])
            self.assertEqual(self.by_code[code]['网站'], '')
            profile = next((ROOT / 'profile/A').glob(code + '-*.md')).read_text()
            self.assertIn('- **邮箱**：—\n', profile)
            self.assertIn('来源等级：leads-only', profile)
        self.assertIn('待人工补信息', self.by_code['A-272']['备注'])
        self.assertEqual(by_code['A-262']['level'], 'official-search-only')
        self.assertIn('待核', self.by_code['A-262']['入口/联系方式'])
        self.assertEqual(by_code['A-278']['level'], 'public-register')
        self.assertEqual(by_code['A-273']['level'], 'official-company-historical-named')
        self.assertIn('kevin.myers@iparchitechs.com', self.by_code['A-273']['备注'])
        self.assertIn('2016', self.by_code['A-273']['备注'])
        self.assertIn('[at]', by_code['A-263']['quote'])
        self.assertEqual(self.by_code['A-260']['网站'], 'https://gpe-networks.com')
        self.assertIn('info@gpe-networks.com', self.by_code['A-260']['入口/联系方式'])
        self.assertTrue(by_code['A-260']['local_sources'])
        for code, site in [('A-261', 'https://iptechniek.nl'), ('A-271', 'https://interstellar.nl'),
                           ('A-266', 'https://www.andisa.net'), ('A-277', 'https://www.modelec.nl')]:
            self.assertEqual(self.by_code[code]['网站'], site)
        for r in records:
            self.assertIn('来源等级：', self.by_code[r['code']]['备注'])
            self.assertIn(f'batch/contact_research_2026-09-27_A260-A279.json#{r["code"]}',
                          self.by_code[r['code']]['备注'])

    def test_r43_official_sources_and_unresolved_mailboxes(self):
        records = json.loads((ROOT / 'batch/contact_research_2026-09-27_A280-A299.json').read_text())['records']
        by_code = {r['code']: r for r in records}
        self.assertEqual([r['code'] for r in records], [f'A-{n:03}' for n in range(280, 300)])
        self.assertEqual(sum(bool(r['email']) for r in records), 11)
        self.assertEqual(sum(r['level'] == 'official-company' for r in records), 11)
        for code in ['A-281', 'A-284', 'A-289', 'A-290', 'A-293', 'A-295', 'A-296', 'A-297', 'A-298']:
            self.assertEqual(by_code[code]['level'], 'leads-only')
            self.assertFalse(by_code[code]['email'])
            self.assertEqual(self.by_code[code]['网站'], '')
            profile = next((ROOT / 'profile/A').glob(code + '-*.md')).read_text()
            self.assertIn('- **邮箱**：—\n', profile)
            self.assertIn('来源等级：leads-only', profile)
        for code in ['A-289', 'A-290', 'A-293', 'A-295', 'A-296', 'A-297', 'A-298']:
            self.assertIn('待人工补信息', self.by_code[code]['备注'])
        self.assertEqual(by_code['A-292']['level'], 'official-company')
        self.assertIn('billing@panorafiber.com', self.by_code['A-292']['入口/联系方式'])
        self.assertIn('非24/7', self.by_code['A-292']['入口/联系方式'])
        self.assertIn('待人工补信息', self.by_code['A-292']['备注'])
        self.assertIn('Netonix', self.by_code['A-280']['备注'])
        self.assertIn('同芯片', self.by_code['A-280']['备注'])
        for code, site in [('A-280', 'https://www.invictuswireless.com'),
                           ('A-283', 'https://www.jellyfishbroadband.com'),
                           ('A-285', 'https://www.dael.com'),
                           ('A-288', 'https://www.wifiprofi.cz'),
                           ('A-291', 'https://adeodc.com'),
                           ('A-299', 'http://sn-solution.hu')]:
            self.assertEqual(self.by_code[code]['网站'], site)
        self.assertIn('hello@jellyfishbroadband.com', self.by_code['A-283']['入口/联系方式'])
        self.assertIn('klima@wifiprofi.cz', self.by_code['A-288']['入口/联系方式'])
        self.assertIn('info@sn-solution.hu', self.by_code['A-299']['入口/联系方式'])
        self.assertIn('ms@adeodc.dk', self.by_code['A-291']['入口/联系方式'])
        for code in ['A-290', 'A-292', 'A-295']:
            self.assertIn('遮罩', self.by_code[code]['备注'])
        self.assertIn('第三方', self.by_code['A-294']['备注'])
        self.assertIn('RIPE', by_code['A-291']['note'])
        self.assertTrue(by_code['A-281']['local_sources'])
        for r in records:
            self.assertIn('来源等级：', self.by_code[r['code']]['备注'])
            self.assertIn(f'batch/contact_research_2026-09-27_A280-A299.json#{r["code"]}',
                          self.by_code[r['code']]['备注'])

    def test_r44_official_sources_and_unresolved_mailboxes(self):
        records = json.loads((ROOT / 'batch/contact_research_2026-09-27_A300-A319.json').read_text())['records']
        by_code = {r['code']: r for r in records}
        self.assertEqual([r['code'] for r in records], [f'A-{n:03}' for n in range(300, 320)])
        self.assertEqual(sum(bool(r['email']) for r in records), 18)
        self.assertEqual(sum(r['level'] == 'official-company' for r in records), 18)
        self.assertEqual([r['code'] for r in records if not r['email']], ['A-301', 'A-316'])
        for code in ['A-301', 'A-316']:
            self.assertEqual(by_code[code]['level'], 'leads-only')
            profile = next((ROOT / 'profile/A').glob(code + '-*.md')).read_text()
            self.assertIn('来源等级：leads-only', profile)
            self.assertIn('待人工补信息', self.by_code[code]['备注'])
        profile_316 = next((ROOT / 'profile/A').glob('A-316-*.md')).read_text()
        self.assertIn('- **邮箱**：—\n', profile_316)
        mail_301 = [l for l in next((ROOT / 'profile/A').glob('A-301-*.md')).read_text().splitlines()
                    if l.startswith('- **邮箱**：')][0]
        self.assertIn('social@3tec.co.uk', mail_301)
        self.assertIn('social@3tec.co.uk', self.by_code['A-301']['入口/联系方式'])
        self.assertIn('social@3tec.co.uk', by_code['A-301']['note'])
        self.assertIn('+1 315-451-0971', self.by_code['A-316']['入口/联系方式'])
        self.assertIn('第三方', by_code['A-316']['note'])
        for code in ['A-300', 'A-302', 'A-303', 'A-304', 'A-305', 'A-306', 'A-307', 'A-308',
                     'A-309', 'A-310', 'A-314', 'A-315', 'A-317', 'A-318', 'A-319']:
            self.assertNotIn('待人工补信息', self.by_code[code]['备注'])
        for code, site in [('A-300', 'https://gbeconverge.com'),
                           ('A-303', 'https://www.trusol.com'),
                           ('A-305', 'https://quadratek.net'),
                           ('A-307', 'https://bluebearsit.com'),
                           ('A-310', 'http://www.ittrust.at'),
                           ('A-312', 'https://www.atlantikelektronik.com'),
                           ('A-313', 'https://www.powertechcontrols.com'),
                           ('A-314', 'https://ningaloo.cloud'),
                           ('A-319', 'https://www.nexus.com.pe')]:
            self.assertEqual(self.by_code[code]['网站'], site)
        self.assertEqual(self.by_code['A-315']['网站'], '')
        self.assertIn('roelof.daleboudt@ip-central.nl', self.by_code['A-315']['入口/联系方式'])
        self.assertIn('gbeconvergebv.com', by_code['A-300']['note'])
        self.assertIn('不合并', self.by_code['A-303']['备注'])
        self.assertIn('FirmenABC', by_code['A-310']['note'])
        self.assertIn('反诈', self.by_code['A-308']['备注'])
        self.assertIn('7777500', by_code['A-314']['note'])
        self.assertIn('deinta@deinta.com', self.by_code['A-318']['入口/联系方式'])
        self.assertIn('enquiries@holkerit.co.uk', self.by_code['A-306']['入口/联系方式'])
        self.assertIn('sales@fikesmedia.com', self.by_code['A-311']['入口/联系方式'])
        self.assertIn('RIPE', by_code['A-315']['note'])
        self.assertEqual(self.by_code['A-319']['国家'], '西班牙')
        self.assertEqual(self.by_code['A-319']['城市'], '')
        self.assertIn('Peru', by_code['A-319']['note'])
        self.assertIn('国别待人工确认', self.by_code['A-319']['备注'])
        for r in records:
            self.assertIn('来源等级：', self.by_code[r['code']]['备注'])
            self.assertIn(f'batch/contact_research_2026-09-27_A300-A319.json#{r["code"]}',
                          self.by_code[r['code']]['备注'])
            self.assertTrue(r['quote'] and r['fields_supported'] and r['retrieved_on'])

    def test_r45_official_sources_and_unresolved_mailboxes(self):
        records = json.loads((ROOT / 'batch/contact_research_2026-09-27_A320-A339.json').read_text())['records']
        by_code = {r['code']: r for r in records}
        self.assertEqual([r['code'] for r in records], [f'A-{n:03}' for n in range(320, 340)])
        self.assertEqual(sum(bool(r['email']) for r in records), 19)
        self.assertEqual(sum(r['level'] == 'official-company' for r in records), 18)
        self.assertEqual([r['code'] for r in records if not r['email']], ['A-334'])
        self.assertEqual(by_code['A-334']['level'], 'leads-only')
        self.assertEqual(by_code['A-335']['level'], 'official-obfuscated')
        self.assertIn('(at)', by_code['A-335']['quote'])
        self.assertTrue(by_code['A-334']['local_sources'])
        for code in ['A-334']:
            profile = next((ROOT / 'profile/A').glob(code + '-*.md')).read_text()
            self.assertIn('- **邮箱**：—\n', profile)
            self.assertIn('来源等级：leads-only', profile)
            self.assertIn('待人工补信息', self.by_code[code]['备注'])
            self.assertEqual(self.by_code[code]['网站'], '')
            self.assertIn('frutti del poggio', by_code[code]['note'])
            self.assertIn('0565', self.by_code[code]['入口/联系方式'])
        for code in ['A-320', 'A-321', 'A-322', 'A-323', 'A-324', 'A-325', 'A-326', 'A-327',
                     'A-328', 'A-329', 'A-330', 'A-331', 'A-332', 'A-333', 'A-335', 'A-336',
                     'A-337', 'A-338', 'A-339']:
            self.assertNotIn('待人工补信息', self.by_code[code]['备注'])
        for code, site in [('A-320', 'https://www.evelem.fr'),
                           ('A-321', 'https://edvpartner.de'),
                           ('A-326', 'https://www.merlinedv.de'),
                           ('A-327', 'https://cfigroupe.com'),
                           ('A-330', 'https://www.nxo.eu'),
                           ('A-335', 'https://www.dpsinformatica.it'),
                           ('A-337', 'https://www.ingesw.com'),
                           ('A-339', 'https://www.mlsoftware.it')]:
            self.assertEqual(self.by_code[code]['网站'], site)
        self.assertIn('contact@evelem.fr', self.by_code['A-320']['入口/联系方式'])
        self.assertIn('vertrieb@edvpartner.de', self.by_code['A-321']['入口/联系方式'])
        self.assertIn('info@dpsinformatica.it', self.by_code['A-335']['入口/联系方式'])
        self.assertIn('info@ingesw.com', self.by_code['A-337']['入口/联系方式'])
        self.assertIn('info@mlsoftware.it', self.by_code['A-339']['入口/联系方式'])
        self.assertIn('不合并', self.by_code['A-321']['备注'])
        self.assertIn('Bayern', by_code['A-326']['note'])
        self.assertIn('Saint-Denis', by_code['A-327']['note'])
        self.assertIn('Puteaux', by_code['A-330']['note'])
        self.assertIn('Toulon', by_code['A-331']['note'])
        self.assertIn('European Job Days', by_code['A-337']['note'])
        self.assertIn('Savona', by_code['A-338']['note'])
        for r in records:
            self.assertIn('来源等级：', self.by_code[r['code']]['备注'])
            self.assertIn(f'batch/contact_research_2026-09-27_A320-A339.json#{r["code"]}',
                          self.by_code[r['code']]['备注'])
            self.assertTrue(r['quote'] and r['fields_supported'] and r['retrieved_on'])

    def test_r46_official_sources_and_unresolved_mailboxes(self):
        records = json.loads((ROOT / 'batch/contact_research_2026-09-27_A340-A359.json').read_text())['records']
        by_code = {r['code']: r for r in records}
        self.assertEqual([r['code'] for r in records], [f'A-{n:03}' for n in range(340, 360)])
        self.assertEqual(sum(bool(r['email']) for r in records), 20)
        self.assertEqual(sum(r['level'] == 'official-company' for r in records), 15)
        self.assertEqual([r['code'] for r in records if r['level'] == 'official-named'], ['A-355', 'A-359'])
        self.assertEqual(by_code['A-343']['level'], 'official-search-only')
        self.assertEqual(by_code['A-344']['level'], 'public-register')
        self.assertEqual(by_code['A-357']['level'], 'partner-directory')
        for code in [f'A-{n:03}' for n in range(340, 360)]:
            self.assertNotIn('待人工补信息', self.by_code[code]['备注'])
            self.assertIn('来源等级：', self.by_code[code]['备注'])
            self.assertIn(f'batch/contact_research_2026-09-27_A340-A359.json#{code}', self.by_code[code]['备注'])
            self.assertTrue(by_code[code]['quote'] and by_code[code]['fields_supported'] and by_code[code]['retrieved_on'])
        for code, site in [('A-340', 'https://netengineering.it'), ('A-344', ''),
                           ('A-345', 'https://avelution.nl'), ('A-349', 'https://www.c2f.pt'),
                           ('A-355', 'https://www.mikrotikls.com.ua'), ('A-357', 'https://www.digitalsima.gr'),
                           ('A-359', 'https://mikrotik.coach')]:
            self.assertEqual(self.by_code[code]['网站'], site)
        self.assertIn('mail@netengineering.it', self.by_code['A-340']['入口/联系方式'])
        self.assertIn('info@technocenter.it', self.by_code['A-343']['入口/联系方式'])
        self.assertIn('worldtechnology@tiscali.it', self.by_code['A-344']['入口/联系方式'])
        self.assertIn('sales@digitalsima.gr', self.by_code['A-357']['入口/联系方式'])
        self.assertIn('vadsco@gmail.com', self.by_code['A-359']['入口/联系方式'])
        self.assertIn('liquidation', by_code['A-350']['note'].lower())
        self.assertIn('Schijndel', by_code['A-345']['note'])
        self.assertIn('Rafina', by_code['A-356']['note'])
        self.assertIn('netspa.com', by_code['A-340']['note'])
        self.assertIn('公开招标', by_code['A-344']['note'])
        self.assertIn('Zyxel', by_code['A-357']['note'])
        for code, level in [('A-343', 'official-search-only'), ('A-344', 'public-register'), ('A-357', 'partner-directory')]:
            profile = next((ROOT / 'profile/A').glob(code + '-*.md')).read_text()
            self.assertIn(f'来源等级：{level}', profile)
        self.assertEqual(self.by_code['A-355']['城市'], 'Kyiv')
        self.assertEqual(self.by_code['A-359']['城市'], 'Kyiv')

    def test_r47_official_sources_and_unresolved_mailboxes(self):
        records = json.loads((ROOT / 'batch/contact_research_2026-09-27_A360-A378.json').read_text())['records']
        by_code = {r['code']: r for r in records}
        self.assertEqual([r['code'] for r in records], [f'A-{n:03}' for n in range(360, 379)])
        self.assertEqual(sum(bool(r['email']) for r in records), 18)
        self.assertEqual(sum(r['level'] == 'official-company' for r in records), 17)
        self.assertEqual([r['code'] for r in records if r['level'] == 'public-register'], ['A-372'])
        self.assertEqual([r['code'] for r in records if r['level'] == 'leads-only'], ['A-378'])
        self.assertFalse(by_code['A-378']['email'])
        for code in [f'A-{n:03}' for n in range(360, 379)]:
            self.assertIn('来源等级：', self.by_code[code]['备注'])
            self.assertIn(f'batch/contact_research_2026-09-27_A360-A378.json#{code}', self.by_code[code]['备注'])
            self.assertTrue(by_code[code]['quote'] and by_code[code]['fields_supported'] and by_code[code]['retrieved_on'])
        self.assertIn('待人工补信息', self.by_code['A-378']['备注'])
        for code in ['A-372', 'A-376', 'A-377']:
            self.assertNotIn('待人工补信息', self.by_code[code]['备注'])
        self.assertEqual(self.by_code['A-360']['网站'], 'http://www.mikrotik.net.ua/')
        self.assertEqual(self.by_code['A-361']['网站'], 'https://www.itlearning.sk')
        self.assertEqual(self.by_code['A-362']['网站'], 'http://www.connet-group.sk/')
        self.assertEqual(self.by_code['A-376']['网站'], 'https://www.virtua-it.si')
        self.assertEqual(self.by_code['A-372']['网站'], 'https://www.pondi.hr')
        self.assertEqual(self.by_code['A-377']['网站'], 'https://infiniti.hr')
        self.assertIn('trainer@mikrotik.net.ua', self.by_code['A-360']['入口/联系方式'])
        self.assertIn('ekomunikacija@pondi.hr', self.by_code['A-372']['入口/联系方式'])
        self.assertIn('jernej.suhadolc@virtua.si', self.by_code['A-376']['入口/联系方式'])
        self.assertIn('ivan.jezerinac@infiniti.hr', self.by_code['A-377']['入口/联系方式'])
        self.assertIn('缺 MTCSWE', by_code['A-373']['note'])
        self.assertIn('MB Tikslingi mokslai', by_code['A-368']['note'])
        self.assertIn('Poltsamaa', by_code['A-374']['note'])
        self.assertIn('持全部十证', by_code['A-360']['note'])
        self.assertIn('leads-only', by_code['A-378']['note'])
        for code in ['A-372', 'A-378']:
            profile = next((ROOT / 'profile/A').glob(code + '-*.md')).read_text()
            self.assertIn(f'来源等级：{by_code[code]["level"]}', profile)
        self.assertEqual(self.by_code['A-365']['城市'], '')
        self.assertEqual(self.by_code['A-373']['城市'], 'Brasov')

    def test_r48_bc_rescreen_promotions(self):
        obj = json.loads((ROOT / 'batch/contact_research_2026-09-28_BCrescreen_A379-A384.json').read_text())
        self.assertEqual(obj['date'], '2026-09-28')
        records = obj['records']
        promoted = [r for r in records if r['decision'] == 'promote']
        holds = [r for r in records if r['decision'] == 'hold-B']
        self.assertEqual([r['code'] for r in promoted], [f'A-{n:03}' for n in range(379, 385)])
        self.assertEqual([r['before_code'] for r in promoted],
                         ['B-070', 'B-272', 'B-465', 'B-416', 'B-361', 'B-175'])
        self.assertEqual(len(holds), 13)
        for r in records:
            self.assertTrue(r['quote'] and r['fields_supported'] and r['sources'])
            self.assertEqual(r['retrieved_on'], '2026-09-28')
        for r in promoted:
            row = self.by_code[r['code']]
            self.assertEqual((row['评级'], row['人工定级'], row['公司名']), ('A', 'A', r['name']))
            self.assertIn('【人工定级】A', row['评级依据'])
            self.assertIn('原' + r['before_code'], row['评级依据'])
            self.assertIn('来源等级：', row['备注'])
            self.assertIn('原' + r['before_code'], row['备注'])
            self.assertIn('batch/contact_research_2026-09-28_BCrescreen_A379-A384.json#' + r['code'],
                          row['备注'])
            profile = next((ROOT / 'profile/A').glob(r['code'] + '-*.md')).read_text()
            self.assertIn(f'来源等级：{r["level"]}', profile)
        for old_code in sorted(self.PROMOTED_OLD):
            self.assertNotIn(old_code, self.by_code)
            self.assertEqual(list((ROOT / 'profile/B').glob(old_code + '-*.md')), [])
        for r in holds:
            if r['code'] in self.PROMOTED_MAP:
                self.assertEqual(self.grade_now(r['code']), 'A')   # R50/R51 达标升级
            else:
                self.assertEqual(self.grade_now(r['code']), 'B')
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'A'), 567)
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'B'), 179)
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'C'), 287)
        a_nums = sorted(int(r['档案编号'][2:]) for r in self.rows if r['评级'] == 'A')
        self.assertEqual(a_nums, list(range(1, 568)))
        self.assertEqual(len(list((ROOT / 'profile/A').glob('A-*.md'))), 567)
        for code in ['A-379', 'A-381']:
            self.assertNotIn('【待补】', self.by_code[code]['备注'])
            self.assertIn('待补标记解除', self.by_code[code]['备注'])
        leftover = [r for r in self.rows if '【待补】' in r['备注']]
        self.assertEqual(len(leftover), 10)   # R49: 23 rows regained a mailbox via official pages
        self.assertTrue(all(r['评级'] == 'C' for r in leftover))
        hold_codes = {r['code'] for r in holds}
        self.assertIn('B-245', hold_codes)
        self.assertIn('mhzshop.com', json.dumps(holds, ensure_ascii=False))
        self.assertIn('B-344', hold_codes)
        self.assertIn('B-226', hold_codes)

    def test_r49_email_backfill_and_rescreen(self):
        obj = json.loads((ROOT / 'batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json').read_text())
        self.assertEqual(obj['date'], '2026-09-28')
        records = obj['records']
        self.assertEqual(len(records), 45)
        by_dec = {}
        for r in records:
            by_dec.setdefault(r['decision'], []).append(r)
            self.assertTrue(r['quote'] and r['fields_supported'] and r['sources'])
            self.assertEqual(r['retrieved_on'], '2026-09-28')
        self.assertEqual(len(by_dec['email-backfill-C-to-B']), 23)
        self.assertEqual(len(by_dec['hold-C']), 10)
        self.assertEqual(len(by_dec['hold-B']), 9)
        self.assertEqual(len(by_dec['email-enrich-B']), 1)
        self.assertEqual(len(by_dec['email-backfill-A']), 2)
        for r in by_dec['email-backfill-C-to-B']:
            self.assertEqual(r['code'], self.R49_OLD_TO_NEW[r['before_code']])
            if r['code'] in self.R53_PROMOTED:
                # R53 B 段逐站复筛后该行达标升 A：编号变为 A-5xx，R49 的邮箱回升事实留在备注里
                row = self.by_code[self.R53_PROMOTED[r['code']]]
                self.assertEqual(row['评级'], 'A')
                self.assertEqual(row['C级细分'], '')
                self.assertIn(r['email'], row['入口/联系方式'])
                self.assertNotIn('【待补】', row['备注'])
                self.assertIn('待补标记解除', row['备注'])
                self.assertIn('#' + r['code'], row['备注'])
                self.assertIn('R53 B段复筛达标升级', row['评级依据'])
                self.assertTrue(list((ROOT / 'profile/A').glob(self.R53_PROMOTED[r['code']] + '-*.md')))
                self.assertEqual(list((ROOT / 'profile/C').glob(r['before_code'] + '-*.md')), [])
                self.assertNotIn(r['before_code'], self.by_code)
                self.assertNotIn(r['code'], self.by_code)
                continue
            row = self.by_code[r['code']]
            self.assertEqual(row['评级'], 'B')
            self.assertEqual(row['C级细分'], '')
            self.assertIn(r['email'], row['入口/联系方式'])
            self.assertNotIn('【待补】', row['备注'])
            self.assertIn('待补标记解除', row['备注'])
            self.assertIn('复核回升', row['评级依据'])
            self.assertIn(r['before_code'] + '→' + r['code'], row['评级依据'])
            self.assertIn('#' + r['code'], row['备注'])
            self.assertTrue(list((ROOT / 'profile/B').glob(r['code'] + '-*.md')))
            self.assertEqual(list((ROOT / 'profile/C').glob(r['before_code'] + '-*.md')), [])
            self.assertNotIn(r['before_code'], self.by_code)
            profile = next((ROOT / 'profile/B').glob(r['code'] + '-*.md')).read_text()
            self.assertIn(f'来源等级：{r["level"]}', profile)
        for r in by_dec['hold-C']:
            row = self.by_code[r['code']]
            self.assertEqual(row['评级'], 'C')
            self.assertIn('【待补】', row['备注'])
            self.assertIn('R49 复核', row['备注'])
        for r in by_dec['hold-B'] + by_dec['email-enrich-B']:
            row = self.by_code[self.PROMOTED_MAP.get(r['code'], r['code'])]
            expect = 'A' if r['code'] in self.PROMOTED_MAP else 'B'   # R50/R51 达标升级
            self.assertEqual(row['评级'], expect)
            self.assertIn('R49 复筛补录', row['备注'])
        for r in by_dec['email-backfill-A']:
            row = self.by_code[r['code']]
            self.assertEqual(row['评级'], 'A')
            self.assertIn(r['email'], row['入口/联系方式'])
            self.assertIn('前 49 位内容可编辑', r['note'])
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'C'), 287)
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'B'), 179)

    def test_r50_full_list_audit_and_promotions(self):
        obj = json.loads((ROOT / 'batch/contact_research_2026-09-28_R50_A提炼.json').read_text())
        self.assertEqual(obj['date'], '2026-09-28')
        records = obj['records']
        self.assertEqual(len(records), 37)
        self.assertEqual([r['code'] for r in records], [f'A-{n:03}' for n in range(385, 422)])
        self.assertEqual({r['before_code'] for r in records}, set(self.R50_PROMOTED))
        for r in records:
            self.assertEqual(self.R50_PROMOTED[r['before_code']], r['code'])
            self.assertTrue(r['quote'] and r['fields_supported'] and r['sources'])
            self.assertEqual(r['retrieved_on'], '2026-09-28')
            row = self.by_code[r['code']]
            self.assertEqual((row['评级'], row['人工定级']), ('A', 'A'))
            self.assertIn('【人工定级】A', row['评级依据'])
            self.assertIn('原 ' + r['before_code'], row['评级依据'])
            self.assertIn('R50 A级提炼', row['备注'])
            self.assertIn('batch/contact_research_2026-09-28_R50_A提炼.json#' + r['code'], row['备注'])
            self.assertTrue(list((ROOT / 'profile/A').glob(r['code'] + '-*.md')))
            self.assertEqual(list((ROOT / 'profile/B').glob(r['before_code'] + '-*.md')), [])
            self.assertNotIn(r['before_code'], self.by_code)
        dups = json.loads((ROOT / 'batch/dedup_hints_2026-09-28_R50.json').read_text())['records']
        self.assertEqual(len(dups), 29)
        for d in dups:
            row = self.by_code[self.PROMOTED_MAP.get(d['code'], d['code'])]
            self.assertIn('【2026-09-28 R50 去重提示】', row['备注'])
            self.assertIn('batch/dedup_hints_2026-09-28_R50.json#' + d['code'], row['备注'])
            self.assertNotIn(d['code'], self.R50_PROMOTED)
        self.assertEqual({d['code'] for d in dups}, self.R50_NOTE_ONLY)
        for code in sorted(self.R50_NOTE_ONLY):
            if code in self.R51_PROMOTED or code in self.R52_PROMOTED or code in self.R53_PROMOTED:
                self.assertEqual(self.grade_now(code), 'A')   # R51/R52/R53 达标升级
            else:
                self.assertEqual(self.by_code[code]['评级'], code[0])
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'A'), 567)
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'B'), 179)
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'C'), 287)
        a_nums = sorted(int(r['档案编号'][2:]) for r in self.rows if r['评级'] == 'A')
        self.assertEqual(a_nums, list(range(1, 568)))
        self.assertEqual(len(list((ROOT / 'profile/A').glob('A-*.md'))), 567)
        self.assertEqual(len(list((ROOT / 'profile/B').glob('B-*.md'))), 179)
        self.assertEqual(len(list((ROOT / 'profile/C').glob('C-*.md'))), 287)
        leftover = [r for r in self.rows if '【待补】' in r['备注']]
        self.assertEqual(len(leftover), 10)
        self.assertTrue(all(r['评级'] == 'C' for r in leftover))

    def test_r51_upgrade_to_a_when_standard_met(self):
        obj = json.loads((ROOT / 'batch/contact_research_2026-09-28_R51_达标即升级.json').read_text())
        self.assertEqual(obj['date'], '2026-09-28')
        records = obj['records']
        self.assertEqual(len(records), 9)
        self.assertEqual([r['code'] for r in records], [f'A-{n:03}' for n in range(422, 431)])
        self.assertEqual({r['before_code'] for r in records}, set(self.R51_PROMOTED))
        for r in records:
            self.assertEqual(self.R51_PROMOTED[r['before_code']], r['code'])
            self.assertTrue(r['quote'] and r['fields_supported'] and r['sources'])
            self.assertEqual(r['retrieved_on'], '2026-09-28')
            row = self.by_code[r['code']]
            self.assertEqual((row['评级'], row['人工定级']), ('A', 'A'))
            self.assertIn('R51 达标即升级', row['评级依据'])
            self.assertIn('原 ' + r['before_code'], row['评级依据'])
            self.assertIn('R51 达标即升级', row['备注'])
            self.assertIn('batch/contact_research_2026-09-28_R51_达标即升级.json#' + r['code'], row['备注'])
            self.assertIn('R50 去重提示', row['备注'])
            self.assertIn('不合并', row['备注'])
            self.assertTrue(list((ROOT / 'profile/A').glob(r['code'] + '-*.md')))
            self.assertEqual(list((ROOT / 'profile/B').glob(r['before_code'] + '-*.md')), [])
            self.assertNotIn(r['before_code'], self.by_code)
        held = [c for c in self.R50_NOTE_ONLY if c not in self.R51_PROMOTED and c not in self.R52_PROMOTED]
        self.assertEqual(len(held), 19)          # 29 条 R50 去重行 - 9 条(R51) - 1 条(R52)
        for code in held:
            if code in self.R53_PROMOTED:
                self.assertEqual(self.grade_now(code), 'A')   # R53 B 段复筛达标升级
                continue
            self.assertEqual(self.by_code[code]['评级'], code[0])
        for code in ['B-245', 'C-214']:           # 早前轮次已记录的 2 条重复提示，仍不合并
            expect = 'A' if code in self.R53_PROMOTED else code[0]
            self.assertEqual(self.grade_now(code), expect)
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'A'), 567)
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'B'), 179)
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'C'), 287)
        leftover = [r for r in self.rows if '【待补】' in r['备注']]
        self.assertEqual(len(leftover), 10)
        self.assertTrue(all(r['评级'] == 'C' for r in leftover))

    def test_r52_duplicate_hint_review_finished(self):
        obj = json.loads((ROOT / 'batch/contact_research_2026-09-28_R52_达标复核补升.json').read_text())
        self.assertEqual(obj['date'], '2026-09-28')
        records = obj['records']
        promoted = [r for r in records if r['decision'] == 'promote']
        holds = json.loads((ROOT / 'batch/达标复核_2026-09-28_R52_维持原级清单.json').read_text())['records']
        self.assertEqual(len(promoted) + len(holds), 22)
        self.assertEqual([r['code'] for r in promoted], ['A-431'])
        self.assertEqual(promoted[0]['before_code'], 'C-011')
        self.assertEqual(len(holds), 21)
        for r in records + holds:
            self.assertTrue(r['note'] and r['sources'])
            self.assertEqual(r['retrieved_on'], '2026-09-28')
        row = self.by_code['A-431']
        self.assertEqual((row['评级'], row['人工定级'], row['C级细分']), ('A', 'A', ''))
        self.assertIn('R52 达标复核补升', row['评级依据'])
        self.assertIn('R52 达标复核补升', row['备注'])
        self.assertIn('batch/contact_research_2026-09-28_R52_达标复核补升.json#A-431', row['备注'])
        self.assertIn('不合并', row['备注'])
        self.assertNotIn('C-011', self.by_code)
        self.assertEqual(list((ROOT / 'profile/C').glob('C-011-*.md')), [])
        self.assertTrue(list((ROOT / 'profile/A').glob('A-431-*.md')))
        for r in holds:
            if r['code'] in self.R53_PROMOTED:
                # R53 B 段逐站复筛后达标升级（原 R52 维持B 的复核结论被后续轮次覆盖）
                self.assertEqual(self.grade_now(r['code']), 'A')
                continue
            self.assertIn(r['code'], self.by_code)
            self.assertEqual(self.by_code[r['code']]['评级'], r['code'][0])
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'A'), 567)
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'B'), 179)
        self.assertEqual(sum(1 for r in self.rows if r['评级'] == 'C'), 287)
        self.assertEqual(len(list((ROOT / 'profile/A').glob('A-*.md'))), 567)

    def test_r53_b_rescreen_promotions(self):
        obj = json.loads((ROOT / 'batch/contact_research_2026-09-28_R53_B复筛升级.json').read_text())
        self.assertEqual(obj['date'], '2026-09-28')
        records = obj['records']
        self.assertEqual(len(records), 136)
        self.assertEqual([r['code'] for r in records], [f'A-{n:03}' for n in range(432, 568)])
        self.assertEqual({r['before_code'] for r in records}, set(self.R53_PROMOTED))
        for r in records:
            self.assertEqual(self.R53_PROMOTED[r['before_code']], r['code'])
            self.assertTrue(r['note'] and r['quote'] and r['sources'])
            self.assertEqual(r['retrieved_on'], '2026-09-28')
            self.assertEqual(r['decision'], 'promote')
        for old, new in self.R53_PROMOTED.items():
            self.assertNotIn(old, self.by_code)
            self.assertEqual(list((ROOT / 'profile/B').glob(old + '-*.md')), [])
            row = self.by_code[new]
            self.assertEqual((row['评级'], row['人工定级'], row['C级细分']), ('A', 'A', ''))
            self.assertIn('R53 B段复筛达标升级', row['评级依据'])
            self.assertIn('R53 B段复筛达标升级', row['备注'])
            self.assertIn('batch/contact_research_2026-09-28_R53_B复筛升级.json#' + new, row['备注'])
            self.assertNotIn('【待补】', row['备注'])
            self.assertTrue(list((ROOT / 'profile/A').glob(new + '-*.md')))
        # 逐站复筛原始批次（hold/pending 与 promote 同存）放在非 contact_research_ 前缀文件里，
        # 避免把「维持原级」的记录算成结构化联系方式证据。
        batch_files = sorted((ROOT / 'batch').glob('B段复筛_2026-09-28_R53_第*批.json'),
                             key=lambda p: int(re.search(r'第(\d+)批', p.name).group(1)))
        self.assertEqual(len(batch_files), 27)
        seen = {}
        for p in batch_files:
            for r in json.loads(p.read_text())['records']:
                seen[r['code']] = r['decision']
        decisions = {}
        for code, dec in seen.items():
            decisions[dec] = decisions.get(dec, 0) + 1
        self.assertEqual(len(seen), 283)                     # 全部带网站 B 行逐站复核
        self.assertEqual(decisions, {'promote': 136, 'hold-B': 136, 'pending': 11})
        self.assertEqual(set(seen) & set(self.R53_PROMOTED), set(self.R53_PROMOTED))

    def test_office_exports_preserve_base_fields(self):
        from openpyxl import load_workbook
        paths = ['客户分级跟进表_2026-09.xlsx', 'MikroTik_vs_SmartByte_替代对照表.xlsx']
        for path in paths:
            wb = load_workbook(ROOT / path, read_only=True)
            names = wb.sheetnames[:3] if path == paths[0] else ['反向信号名单']
            seen = set()
            for name in names:
                ws = wb[name]
                rr = ws.iter_rows(values_only=True)
                self.assertEqual(list(next(rr))[:len(self.header)], self.header)
                expected = [r for r in self.rows if r['评级'] == name[0]] if path == paths[0] else self.rows
                got = [list(r)[:len(self.header)] for r in rr]
                self.assertEqual(len(got), len(expected))
                for a, b in zip(got, expected):
                    self.assertEqual([str(v) if v is not None else '' for v in a], [b[k] for k in self.header])
                    seen.add(b['档案编号'])
            self.assertEqual(seen, set(self.by_code))
            wb.close()
        before = load_workbook(io.BytesIO(git_file(paths[1])), read_only=True)
        after = load_workbook(ROOT / paths[1], read_only=True)
        self.assertEqual(before.sheetnames, after.sheetnames)
        for name in before.sheetnames:
            if name != '反向信号名单':
                self.assertEqual(list(before[name].values), list(after[name].values), name)
        before.close()
        after.close()

    def test_history_is_preserved_and_rounds_explicit(self):
        self.assertEqual((ROOT / 'docs/history/AGENT-README_截至5ac5c56.md').read_bytes(), git_file('AGENT-README.md'))
        text = (ROOT / 'docs/requirements/用户要求总账.md').read_text()
        for n in range(1, 55):
            self.assertIn(f'### R{n:02d} ·', text)
        self.assertEqual(len(re.findall(r'(?m)^- 用户消息时间：', text)), 55)  # 54 rounds + template
        self.assertIn('未知', text)
        self.assertIn('旧Agent摘要', text)

    def test_inventory_hashes_and_parse_success(self):
        manifest = json.loads((ROOT / 'docs/audit/文件盘点.json').read_text())
        self.assertEqual(manifest['errors'], [])
        for f in manifest['files']:
            p = ROOT / f['path']
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(), f['sha256'], f['path'])
        self.assertEqual(audit.links('[1](https://example.org/test_(one))'), ['https://example.org/test_(one)'])

    def test_generator_isolated_and_followup_guard(self):
        # Runtime test against real production generator, in an isolated directory.
        sample = [self.by_code['A-001'], self.by_code['B-001'], self.by_code['C-001'],
                  self.by_code['A-222'], self.by_code['A-233'], self.by_code['A-249'],
                  self.by_code['A-251'], self.by_code['A-258'], self.by_code['A-272'],
                  self.by_code['A-279'], self.by_code['A-281'], self.by_code['A-292'],
                  self.by_code['A-299'], self.by_code['A-303'], self.by_code['A-315'],
                  self.by_code['A-319'], self.by_code['A-320'], self.by_code['A-334'],
                  self.by_code['A-335'], self.by_code['A-337'], self.by_code['A-339'],
                  self.by_code['A-343'], self.by_code['A-344'], self.by_code['A-350'],
                  self.by_code['A-355'], self.by_code['A-357'], self.by_code['A-359'],
                  self.by_code['A-360'], self.by_code['A-364'], self.by_code['A-368'],
                  self.by_code['A-372'], self.by_code['A-378']]
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            with (root / CSV).open('w', encoding='utf-8-sig', newline='') as f:
                w = csv.DictWriter(f, fieldnames=self.header)
                w.writeheader()
                w.writerows(sample)
            cmd = [sys.executable, str(ROOT / 'scripts/make_profiles.py')]
            subprocess.run(cmd, cwd=root, check=True, capture_output=True)
            p = next((root / 'profile/C').glob('*.md'))
            self.assertIn(f'C 级细分：`{sample[2]["C级细分"]}`', p.read_text())
            for code in ['A-222', 'A-233', 'A-249', 'A-251', 'A-258', 'A-272', 'A-279',
                         'A-281', 'A-292', 'A-299', 'A-303', 'A-315', 'A-319',
                         'A-320', 'A-334', 'A-335', 'A-337', 'A-339',
                         'A-343', 'A-344', 'A-350', 'A-355', 'A-357', 'A-359',
                         'A-360', 'A-364', 'A-368', 'A-372', 'A-378']:
                generated = next((root / 'profile/A').glob(code + '-*.md'))
                checked = next((ROOT / 'profile/A').glob(code + '-*.md'))
                self.assertEqual(generated.read_bytes(), checked.read_bytes())
            frozen = {str(p): p.read_bytes() for p in (root / 'profile').rglob('*.md')}
            subprocess.run(cmd, cwd=root, check=True, capture_output=True)
            self.assertEqual(frozen, {str(p): p.read_bytes() for p in (root / 'profile').rglob('*.md')})
            p = next((root / 'profile/A').glob('*.md'))
            p.write_text(p.read_text() + '\n| 2026-09-27 | email | existing | reply | keep |\n')
            protected = p.read_bytes()
            result = subprocess.run(cmd, cwd=root, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(p.read_bytes(), protected)


if __name__ == '__main__':
    unittest.main()
