# -*- coding: utf-8 -*-
"""Persistent dossier numbering (档案编号).

Rules, fixed by the user on 2026-09-23:

  * A number, once assigned, never changes. The user works through the A
    list in order, so any reordering silently repoints their bookmarks.
  * A new account is appended after the current maximum of its grade. It
    never fills a gap.
  * When a grade changes, the row moves to the END of its new grade's
    sequence and the old number is left VACANT. Vacant numbers are never
    backfilled, because backfilling is precisely what reorders the list.
  * Consequence: B and C carry gaps and A should not. A gap in A means
    something got demoted out of A, which is worth looking at.

WHY THIS IS A SEPARATE MODULE
-----------------------------
grade.py changes grades; make_profiles.py builds filenames from numbers.
When the renumbering lived only in make_profiles.py, running grade.py on
its own left the CSV in a state where the number segment disagreed with
the grade -- a row graded C still carrying "B-493", so the dossier was
written as B-493-... while the CSV said C. Any tool reading the CSV at
that moment saw a contradiction, and the profile directory ended up with
a different grade mix than the CSV.

Both callers now go through renumber(), so that state cannot survive.
Call renumber() after anything that changes a grade, and audit() before
writing anything that depends on numbers.
"""

import csv
import re

NUM = re.compile(r'([ABC])-(\d+)$')
GRADE_COL = 17          # 评级; do not move without updating every caller


def num_col(hdr):
    """Index of 档案编号, or None if the column is absent."""
    return hdr.index("档案编号") if "档案编号" in hdr else None


def renumber(data, hdr, csv_path=None, verbose=True):
    """Assign or migrate 档案编号 in place. Returns rows touched.

    data is the list of CSV row lists, hdr the header list. When
    csv_path is given and anything changed, the result is written back so
    the persisted file is never left inconsistent.
    """
    ncol = num_col(hdr)
    if ncol is None:
        return 0

    # Only a number whose prefix matches the CURRENT grade counts as
    # occupied for that grade -- a stale B-xxx on a C row must not block
    # or inflate the B sequence.
    used = {g: set() for g in "ABC"}
    for r in data:
        m = NUM.match((r[ncol] or "").strip())
        if m and m.group(1) == r[GRADE_COL]:
            used[r[GRADE_COL]].add(int(m.group(2)))

    nxt = {g: (max(used[g]) if used[g] else 0) for g in "ABC"}
    touched = 0
    for r in data:
        m = NUM.match((r[ncol] or "").strip())
        if m and m.group(1) == r[GRADE_COL]:
            continue
        nxt[r[GRADE_COL]] += 1
        r[ncol] = "%s-%03d" % (r[GRADE_COL], nxt[r[GRADE_COL]])
        touched += 1

    if touched:
        if csv_path:
            with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
                w = csv.writer(f)
                w.writerow(hdr)
                w.writerows(data)
        if verbose:
            print("re-numbered %d rows into their new grade "
                  "(appended at the end)" % touched)
    return touched


def audit(data, hdr):
    """Return a list of numbering problems. Empty list means clean.

    Check this before anything that writes filenames or exports sheets.
    """
    ncol = num_col(hdr)
    if ncol is None:
        return ["no 档案编号 column"]
    probs, seen = [], {}
    for r in data:
        num = (r[ncol] or "").strip()
        g = r[GRADE_COL]
        if not num:
            probs.append("empty number: %s" % r[0])
            continue
        if num in seen:
            probs.append("duplicate %s: %s / %s" % (num, seen[num], r[0]))
        seen[num] = r[0]
        if not num.startswith(g):
            probs.append("segment mismatch %s on a %s row: %s" % (num, g, r[0]))
    return probs


def summary(data, hdr):
    """Per-grade counts and gap count, for regression reporting."""
    ncol = num_col(hdr)
    out = {}
    for g in "ABC":
        nums = sorted(int(r[ncol].split("-")[1])
                      for r in data if r[GRADE_COL] == g and (r[ncol] or "").strip())
        if not nums:
            out[g] = (0, None, None, 0)
            continue
        s = set(nums)
        gaps = [x for x in range(1, nums[-1] + 1) if x not in s]
        out[g] = (len(nums), nums[0], nums[-1], len(gaps))
    return out
