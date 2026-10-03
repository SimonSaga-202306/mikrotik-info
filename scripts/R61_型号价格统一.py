#!/usr/bin/env python3
"""
R61 型号价格统一批量替换:
  STC-424XGGPM-280W/-440W → STC-424XGGPM-280W/-440W  (PoE 主推款 DG=2.5G 错改 XG=10G)
  STC-424XGGM → STC-424XGGM  (24口 非PoE 同款 DG→XG;负向随后不接 PM 以免双重替换)
  $180 → $180  (所有 STC-424XG 相关价格;其他 $143/$99/$220 等不动)

规则(长→短,避免串位):
  先型号(DGGPM/DGGM)→XG 后价格;价格切换仅在 $180 非历史 xlsx 原文保留场景
"""
import glob, re, sys

STATS = {'files_changed': 0, 'total_replacements': 0}

MODEL_RULES = [
    ('STC-424XGGPM-280W',   'STC-424XGGPM-280W'),
    ('STC-424XGGPM-440W',   'STC-424XGGPM-440W'),
    (r'STC-424XGGM(?!PM)',  'STC-424XGGM'),       # 正则,带 negative lookahead
]
PRICE_RULES = [
    ('$180 USD EXW', '$180 USD EXW'),
    ('EXW $180',     'EXW $180'),
    ('$180 USD',     '$180 USD'),
    ('$180 EXW',     '$180 EXW'),
    ('($180)',       '($180)'),
    ('($180',        '($180'),
    ('$180)',        '$180)'),
    ('$180 ',        '$180 '),
    ('$180,',        '$180,'),
    ('$180,',        '$180,'),
    ('$180;',        '$180;'),
    ('$180;',        '$180;'),
    ('$165\n',       '$180\n'),
    ('$180 锚',      '$180 锚'),
    ('$180 vs',      '$180 vs'),
    ('$180 段',      '$180 段'),
    ('$180 到',      '$180 到'),
    ('$180~',        '$180~'),
]

# 处理文件类型
PATTERNS = ['**/*.md', '**/*.csv', '**/*.json', '**/*.py']

def replace_in_text(text: str) -> tuple:
    n = 0
    # 型号
    for old, new in MODEL_RULES:
        if old.startswith('STC-424XGGM(?!PM)'):
            text, c = re.subn(r'STC-424XGGM(?!PM)', 'STC-424XGGM', text)
        else:
            c = text.count(old)
            text = text.replace(old, new)
        n += c
    # 价格
    for old, new in PRICE_RULES:
        c = text.count(old)
        text = text.replace(old, new)
        n += c
    return text, n

changed_files = set()
for pattern in PATTERNS:
    for path in glob.glob(pattern, recursive=True):
        if '.git' in path: continue
        try:
            raw = open(path, encoding='utf-8').read()
        except Exception:
            continue
        new_raw, n = replace_in_text(raw)
        if new_raw != raw:
            open(path, 'w', encoding='utf-8').write(new_raw)
            changed_files.add(path)
            STATS['total_replacements'] += n

STATS['files_changed'] = len(changed_files)
print(f'变更文件 {STATS["files_changed"]} 个;替换 {STATS["total_replacements"]} 处')

# Fix Saga产品目录 specific(R61 已知 4 行需特殊修)
sp = 'Saga产品目录与SmartByte替换对照_2026-09-28.md'
try:
    raw = open(sp, encoding='utf-8').read()
    orig = raw
    fixes = [
        ('4×2.5G SFP+24×GE PoE af/at,PoE 管理+watchdog | **$165.0 / $220.0**',
         '4×10G SFP+24×GE PoE af/at,PoE 管理+watchdog | **$180.0 / $220.0**'),
        ('STC-424XGGPM-440W**($220);预算紧用 **-280W**($180)',
         'STC-424XGGPM-440W**($220);预算紧用 **-280W**($180)'),
        ('STC-424XGGPM-280W($180)。', 'STC-424XGGPM-280W($180)。'),
        ('24口 PoE 商用 $165–264 EXW', '24口 PoE 商用 $180–264 EXW'),
    ]
    for old, new in fixes:
        if old in raw:
            raw = raw.replace(old, new)
    if raw != orig:
        open(sp, 'w', encoding='utf-8').write(raw)
        print(f'Saga 产品目录 special fix 完成')
except FileNotFoundError:
    pass
