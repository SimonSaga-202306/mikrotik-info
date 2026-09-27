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
from make_profiles import emails
from numbering import renumber

CSV = '客户名单_反向信号_2026-09.csv'
BASELINE = '5ac5c56'  # Before this governance/contact-research change.


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

    def test_frozen_identity_and_physical_order(self):
        baseline = list(csv.DictReader(io.StringIO(git_file(CSV).decode('utf-8-sig'))))
        identity = lambda r: (r['档案编号'], r['公司名'], r['国家'], r['评级'])
        self.assertEqual(list(map(identity, baseline)), list(map(identity, self.rows)))
        targets = {f'A-{n:03}' for n in range(200, 210)}
        for before, after in zip(baseline, self.rows):
            if before['档案编号'] not in targets:
                self.assertEqual(before, after)
            else:
                self.assertTrue(all(before[k] == after[k] for k in self.header
                                    if k not in {'网站', '入口/联系方式', '备注', '评级依据'}))

    def test_first_49_dossiers_byte_identical(self):
        first = [p for p in (ROOT / 'profile/A').glob('A-*.md') if int(p.name[2:5]) <= 49]
        self.assertEqual(len(first), 49)
        for p in first:
            self.assertEqual(p.read_bytes(), git_file(p.relative_to(ROOT).as_posix()), p.name)

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
        batch = json.loads((ROOT / 'batch/contact_research_2026-09-27_A200-A209.json').read_text())['records']
        self.assertEqual([r['code'] for r in batch], [f'A-{n:03}' for n in range(200, 210)])
        for r in batch:
            row = self.by_code[r['code']]
            self.assertEqual(row['公司名'], r['name'])
            self.assertTrue(r['quote'] and r['fields_supported'] and r['retrieved_on'])
            if r['email']:
                self.assertIn(r['email'], row['入口/联系方式'])
            for _, u in r['sources']:
                self.assertIn(u, row['备注'])

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
        for n in range(1, 40):
            self.assertIn(f'### R{n:02d} ·', text)
        self.assertEqual(len(re.findall(r'(?m)^- 用户消息时间：', text)), 40)  # 39 + template
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
        sample = [self.by_code['A-001'], self.by_code['B-001'], self.by_code['C-001']]
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
