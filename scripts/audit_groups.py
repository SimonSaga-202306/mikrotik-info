#!/usr/bin/env python3
"""Find suspected duplicate or cross-border groups in the reverse-signal list."""
import csv, re
from collections import defaultdict

CSV = "客户名单_反向信号_2026-09.csv"
SUFFIX = (r'\b(gmbh|ag|bv|b\.v\.|ltd|limited|s\.?r\.?l\.?|sas|sarl|spa|sp\.?j\.?|oy|ab'
          r'|as|a\.?s\.?|inc|llc|plc|kk|pte|s\.?a\.?|group|holding|international'
          r'|europe|europa|iberia|italia|nordic|uk|us|usa|france|deutschland)\b')


def root(s):
    s = re.sub(SUFFIX, ' ', s.lower())
    s = re.sub(r'[^a-z]+', '', s)
    return s[:9]


def main():
    rows = list(csv.reader(open(CSV, encoding="utf-8-sig")))
    data = rows[1:]
    g = defaultdict(list)
    for r in data:
        k = root(r[0])
        if len(k) >= 5:
            g[k].append((r[0], r[1], r[3], r[10]))
    dups = {k: v for k, v in g.items() if len(v) > 1}
    print("疑似同一集团/同名的组(%d):" % len(dups))
    for k, v in sorted(dups.items()):
        print("  [%s]" % k)
        for name, country, site, prio in v:
            print("     - %s | %s | %s | %s" % (name, country, site or "-", prio))


if __name__ == "__main__":
    main()
