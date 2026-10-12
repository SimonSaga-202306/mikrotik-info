#!/usr/bin/env python3
"""Apply the R71 A/B follow-up and exact-address receipt overlay to dossiers.

The CSV and structured-profile source remain unchanged.  This overlay is
re-applied by make_profiles.py after rendering so the reported outreach state,
reply, and exact bounce exceptions survive dossier regeneration.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FOLLOWUP_PATH = ROOT / "batch/邮件跟进_2026-10-12_R71.json"
BOUNCE_PATH = ROOT / "batch/邮件退信_2026-10-12_R71.json"
ALL_BOUNCE_DIR = ROOT / "batch"
START = "<!-- R71-FOLLOWUP-START -->"
END = "<!-- R71-FOLLOWUP-END -->"
GENERIC_VERIFY = (
    "- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——"
    "「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。"
)
FOLLOWUP_VERIFY = (
    "- **R71 跟进核对**：本户一轮跟进已完成（用户报告）；逐户发送日期与实际收件地址未提供，"
    "不补造。已核实的地址级异常见本档 R71/退信记录；未将用户报告扩大成逐地址送达结论。"
)
B457_VERIFY = (
    "- **R71 跟进核对**：Gmail 核实本户于 2026-10-10 向 services@adrnet.site 发件并收到客户回信；"
    "确切时间、主题与原话见本档 R71 记录，不外推到其他客户。"
)
DEFAULT_NEXT = (
    "R71（2026-10-12）：一轮跟进已完成（用户报告；本户具体发送日期/收件地址未逐户提供）。"
    "可继续按本档既有策略低频跟进；不对首轮无实质回应者无差别催促；不编排未提供的下次动作日期。"
)
DEFAULT_STATUS = "01-已跟进一轮（用户报告；具体日期/收件人未逐户记录）"


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _code_from_profile(text: str) -> str | None:
    match = re.search(r"(?m)^code: ([AB]-\d+)\s*$", text)
    if match:
        return match.group(1)
    match = re.search(r"(?m)^> \*\*评级 [AB].*?档案编号 `([AB]-\d+)`", text)
    return match.group(1) if match else None


def _bounce_records(path: Path) -> list[dict[str, Any]]:
    """Read address-level records while ignoring unmatched/non-customer groups."""
    if not path.exists():
        return []
    return [r for r in _read_json(path).get("records", []) if r.get("code")]


def load_bounces_by_code(batch_dir: Path = ALL_BOUNCE_DIR) -> dict[str, dict[str, dict[str, Any]]]:
    """Collect all bounce exceptions by customer and exact recipient.

    Later records supersede an earlier event for the *same exact address*;
    distinct addresses under one customer remain separate. This prevents a new
    bounce from silently replacing another address's history for that code.
    """
    by_code: dict[str, dict[str, dict[str, Any]]] = {}
    for path in sorted(batch_dir.glob("邮件退信_*.json")):
        try:
            records = _read_json(path).get("records", [])
        except (OSError, json.JSONDecodeError):
            continue
        for record in records:
            code = record.get("code")
            if not code:
                continue
            recipient = (record.get("email") or
                         (record.get("bounced") if "@" in str(record.get("bounced", "")) else None) or
                         record.get("bounced") or record.get("type") or path.name)
            by_code.setdefault(code, {})[str(recipient).casefold()] = record
    return by_code


def _display_bounce(record: dict[str, Any]) -> list[str]:
    recipient = record.get("email") or record.get("bounced") or "（未提供收件地址）"
    status = record.get("delivery_status") or record.get("type") or "性质待核"
    date = record.get("date_time") or record.get("date") or "日期未提供"
    source = record.get("source") or "台账记录"
    lines = [f"  - `{recipient}` — {status}（{date}；来源：{source}）。"]
    detail = record.get("detail")
    if detail:
        lines.append(f"    - 证据：{detail}")
    action = record.get("action")
    if action:
        lines.append(f"    - 处置：{action}")
    return lines


def _r71_section(code: str, record: dict[str, Any], current_bounces: list[dict[str, Any]],
                 has_older_bounce: bool) -> str:
    lines = [
        START,
        "## R71 本轮跟进与邮件回执（2026-10-12）",
        "",
    ]
    gmail = record.get("gmail", {})
    if code == "B-457" and gmail:
        lines.append(
            f"- **跟进范围**：用户报告 A/B 已完成一轮；本户另有 Gmail 外发记录：{gmail.get('outbound_date', '日期未提供')}，"
            f"收件人 `{gmail.get('recipient', '—')}`。"
        )
    else:
        lines.append(
            "- **跟进范围**：A/B 本轮一轮跟进已完成（用户报告）；逐户发送日期与实际收件地址未提供，本节不补造发送日志。"
        )
    reply_status = record.get("reply_status")
    if reply_status:
        lines.append(f"- **回复状态**：{reply_status}")
    elif code == "B-457":
        # The special record is guarded below as well; this branch keeps a clear
        # status if a future data edit accidentally omits reply_status.
        lines.append("- **回复状态**：客户已回复，待我方回复；本轮不自动发送。")
    else:
        lines.append("- **本户结论**：一轮跟进已完成；可继续按本档既有策略低频跟进，不把“已跟进”误写成“逐地址送达成功”。")

    if code == "B-457":
        gmail = record.get("gmail", {})
        if gmail:
            lines.extend([
                f"- **Gmail 核实**：主题 `{gmail.get('subject_outbound', '—')}`；外发收件人 `{gmail.get('recipient', '—')}`，时间 {gmail.get('outbound_date', '—')}；",
                f"  客户回信来自 `{gmail.get('inbound_sender', '—')}`，时间 {gmail.get('inbound_date', '—')}。",
                f"  客户原话：“{gmail.get('inbound_text', '—')}”",
                "- **待办**：等待用户决定是否回复；不自动发送、不追加销售推介或附件。",
            ])

    if current_bounces:
        lines.append("- **本轮地址级退信/延迟例外**：")
        for bounce in current_bounces:
            lines.extend(_display_bounce(bounce))
        lines.append("- **客户级跟进结论**：只对上述精确收件地址按回执处置；不把单地址异常扩大到整家公司或其他邮箱。")
    elif has_older_bounce:
        lines.append("- **历史地址级例外**：本档已有较早的精确退信记录；继续跟进时遵守原记录的替代渠道/停止重投标记。R71 不清除或改写旧例外。")
    elif not record.get("reply_status") and code != "B-457":
        lines.append("- **地址级范围**：R71 退信台账未为本户列出新的精确地址异常；可继续跟进不等于对每个邮箱作了 SMTP 或逐地址送达验证。")

    cadence = record.get("cadence")
    if not cadence:
        cadence = "首轮之后不作无差别催促；按既有节奏等待或低频跟进，不填造日期。"
    lines.extend([f"- **后续节奏**：{cadence}", END])
    return "\n".join(lines)


def _replace_next_step(text: str, code: str, record: dict[str, Any],
                       current_bounces: list[dict[str, Any]], older_bounces: bool,
                       followup_defaults: dict[str, Any]) -> str:
    pattern = re.compile(r"(?m)^- \*\*下一步\*\*：.*$")
    match = pattern.search(text)
    if not match:
        # Legacy profiles may have no SALES BRIEF field. Do not invent a new
        # SALES BRIEF section; the dedicated R71 block still carries the state.
        return text
    old_line = match.group(0)

    override_next = record.get("next_step")
    if override_next:
        replacement = f"- **下一步**：{override_next}"
    elif current_bounces:
        actions = []
        for bounce in current_bounces:
            action = bounce.get("action")
            if action and action not in actions:
                actions.append(action)
        replacement = "- **下一步**：R71（2026-10-12）：" + "；".join(actions)
    elif "R71：" in old_line or "R71（2026-10-12）" in old_line:
        replacement = old_line
    elif "发出首触邮件（见文末样板）→ 等待信号" in old_line:
        if older_bounces:
            replacement = (
                "- **下一步**：R71（2026-10-12）：一轮跟进已完成（用户报告）；继续时按本档既有退信记录走替代路径，"
                "不重投已标记的失败地址；不对首轮无实质回应者无差别催促，也不编排未提供的日期。"
            )
        else:
            replacement = f"- **下一步**：{followup_defaults.get('next_step', DEFAULT_NEXT)}"
    else:
        suffix = (
            "；R71：一轮跟进已完成（用户报告）；保留本档既有下一步与低频节奏，不对首轮无实质回应者无差别催促，"
            "也不补造未提供的下次动作日期。"
        )
        if older_bounces:
            suffix = (
                "；R71：一轮跟进已完成（用户报告）；保留本档既有计划，并遵守历史退信的替代渠道/停止重投标记；"
                "不作无差别催促或补造日期。"
            )
        replacement = old_line + suffix

    return pattern.sub(lambda _m: replacement, text, count=1)


def _update_stage_and_status(text: str, code: str, record: dict[str, Any],
                             defaults: dict[str, Any]) -> str:
    stage = record.get("stage", defaults.get("stage", "01-contacted"))
    header_status = record.get("header_status", defaults.get("header_status", DEFAULT_STATUS))
    text = re.sub(
        r"(?m)^(> \*\*评级 [AB].*?状态：).*$",
        lambda m: m.group(1) + header_status,
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^(> \*\*触达状态（Stage）\*\*：)[^　]+",
        lambda m: m.group(1) + stage,
        text,
        count=1,
    )
    text = re.sub(r"(?m)^stage: .*?$", f"stage: {stage}", text, count=1)
    text = re.sub(r"(?m)^updated: .*?$", "updated: 2026-10-12", text, count=1)
    return text


def _patch_exact_contact_notes(text: str, code: str) -> str:
    """Keep dossier contact notes aligned with the exact R71 evidence."""
    if code == "B-457":
        text = text.replace(
            "- **邮箱**：services@adrnet.site\n  - 状态：既有/公开",
            "- **邮箱**：services@adrnet.site\n  - 状态：客户于 2026-10-10 回信，证明该地址当时可接收邮件；当前待我方回复",
            1,
        )
    elif code == "B-487":
        text = text.replace(
            "- **邮箱**：sales@accreda.eu\n  - 状态：既有/公开",
            "- **邮箱**：sales@accreda.eu\n  - 状态：Gmail 临时延迟、46 小时重试中；不是地址不存在",
            1,
        )
    elif code == "B-491":
        text = text.replace(
            "- **邮箱**：info@setehnica.com\n  - 状态：既有/公开",
            "- **邮箱**：info@setehnica.com\n  - 状态：域名 MX 查询返回 NXDOMAIN；保留为失败地址，不再投递",
            1,
        )
    elif code == "B-352":
        # The current CSV explicitly stores the .com address. The structured
        # profile's email field was truncated; repair only this generated MD
        # display, leaving the source CSV and rating untouched.
        text = text.replace(
            "- **邮箱**：sales@usa.ieiworld\n  - 状态：既有/公开",
            "- **邮箱**：sales@usa.ieiworld.com\n  - 状态：既有/公开（主表原文；本次退信不是此地址）",
            1,
        )

    replacements = {
        "B-340": (
            "Mark O'Day",
            "mark@controllerservice.com",
            "用户报告收件人不存在（Gmail 原件未检出、日期未提供）；不向此精确地址重投",
            "用户报告收件人不存在（未检出 Gmail 原件；日期未提供）；不向此精确地址重投",
        ),
        "B-352": (
            "Richard Kao",
            "richard@ieiworld.com",
            "Gmail 退信：550 5.4.1 Access denied；不证明地址不存在；不向此精确地址重投",
            "Gmail 退信：550 5.4.1 Access denied；非地址不存在；不向此精确地址重投",
        ),
    }
    if code in replacements:
        person, email, inline_status, table_status = replacements[code]
        updated_lines: list[str] = []
        for line in text.splitlines():
            if line.startswith("  - **" + person + "**") and email in line and "〔猜测(" in line:
                line = re.sub(r"〔猜测\(.*?;源:", f"〔{inline_status};源:", line, count=1)
            if line.startswith("| " + person + " |") and email in line:
                parts = line.split("|")
                if len(parts) >= 6:
                    parts[4] = " " + table_status + " "
                    line = "|".join(parts)
            updated_lines.append(line)
        text = "\n".join(updated_lines) + ("\n" if text.endswith("\n") else "")
    return text


def apply_r71_followup(profile_dir: str | Path | None = None,
                       followup_path: str | Path = FOLLOWUP_PATH,
                       bounce_path: str | Path = BOUNCE_PATH) -> int:
    """Apply R71 to existing A/B dossiers and return the number updated.

    ``profile_dir`` is relative to the current working directory by default so
    the production generator's isolated tests can render into a temporary
    directory while reusing the committed R71 source data.
    """
    profile_root = Path(profile_dir) if profile_dir is not None else (Path.cwd() / "profile")
    followup = _read_json(Path(followup_path))
    defaults = followup.get("default", {})
    records = {r["code"]: r for r in followup.get("records", []) if r.get("code")}
    overrides = followup.get("overrides", {})
    if not records:
        raise ValueError("R71 follow-up data has no A/B dossier codes")
    if any(not c.startswith(("A-", "B-")) for c in records):
        raise ValueError("R71 follow-up data must not include C dossiers")

    all_bounces = load_bounces_by_code()
    current_bounce_data = _read_json(Path(bounce_path))
    current_by_code: dict[str, list[dict[str, Any]]] = {}
    for bounce in current_bounce_data.get("records", []):
        if bounce.get("code"):
            current_by_code.setdefault(bounce["code"], []).append(bounce)

    applied = 0
    for tier in ("A", "B"):
        tier_dir = profile_root / tier
        if not tier_dir.exists():
            continue
        for path in sorted(tier_dir.glob("*.md")):
            original = path.read_text(encoding="utf-8")
            code = _code_from_profile(original)
            if code not in records:
                continue
            record = dict(overrides.get(code, {}))
            previous = records[code]
            # File-level records may carry per-profile additions in later runs.
            record.setdefault("cadence", previous.get("cadence"))
            bounces = current_by_code.get(code, [])
            existing_bounces = all_bounces.get(code, {})
            has_older_bounce = any(
                str(r.get("date", "")) < "2026-10-12"
                for r in existing_bounces.values()
            )

            text = re.sub(
                re.escape(START) + r".*?" + re.escape(END) + r"\n?",
                "",
                original,
                flags=re.S,
            )
            text = _update_stage_and_status(text, code, record, defaults)
            text = _replace_next_step(text, code, record, bounces, has_older_bounce, defaults)
            if GENERIC_VERIFY in text:
                text = text.replace(GENERIC_VERIFY, FOLLOWUP_VERIFY, 1)
            if code == "B-457" and FOLLOWUP_VERIFY in text:
                text = text.replace(FOLLOWUP_VERIFY, B457_VERIFY, 1)
            text = _patch_exact_contact_notes(text, code)

            section = _r71_section(code, record, bounces, has_older_bounce)
            text = text.rstrip() + "\n\n" + section + "\n"
            if text != original:
                path.write_text(text, encoding="utf-8")
                applied += 1
    return applied


def main() -> None:
    count = apply_r71_followup(Path.cwd() / "profile")
    print(f"applied R71 follow-up overlay to {count} A/B dossiers")


if __name__ == "__main__":
    main()
