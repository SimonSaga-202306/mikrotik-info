#!/usr/bin/env python3
"""Build a short first-contact email for an account.

Cold mail to a technical buyer should be under about 120 words, should
open with something that proves you looked at them, and should ask for
one small thing. No marketing voice, no origin story, no attachment.
"""
import re

SCEN = {
    "POE": dict(
        subject="PoE budget question on your camera jobs",
        hook="I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.",
        ask="How many cameras per job, and what wattage per port are you designing to?"),
    "HOTEL": dict(
        subject="PoE + VLAN per room — question on your hotel jobs",
        hook="I build PoE access switches for hotel and multi-dwelling networks, which is where you seem to spend most of your time.",
        ask="How many drops per room, and is your IPTV running on multicast?"),
    "MULTICAST": dict(
        subject="IGMP / multicast behaviour on your IPTV builds",
        hook="Multicast is where most IPTV and camera builds quietly fall over, and it is the part I specialise in on the access switch.",
        ask="Are you running IGMP snooping plus a querier, or still flooding the VLAN?"),
    "INDUSTRIAL": dict(
        subject="Ring convergence + -40 to 75C switches",
        hook="I do industrial access switches — DIN rail, wide temperature, ERPS ring — which matches the environments you work in.",
        ask="What ring protocol are you on today, and what convergence do you actually see?"),
    "SWITCH": dict(
        subject="L3 hardware offload + QinQ on access switching",
        hook="You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.",
        ask="What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?"),
    "MTCSWE": dict(
        subject="Switching question for an MTCSWE holder",
        hook="You hold MTCSWE, so switching is a declared specialism rather than a side task — that is who I want to talk to.",
        ask="What are you using for L2 redundancy today, and does it need ERPS-class convergence?"),
    "FIBRE": dict(
        subject="Per-subscriber isolation on your FTTH build",
        hook="I build access switches for FTTH and fixed wireless — per-subscriber isolation and uplink aggregation are the whole job.",
        ask="How are you isolating subscribers now — QinQ per user, or something simpler?"),
    "CAMPUS": dict(
        subject="PoE access switching for campus / school builds",
        hook="Campus and school networks are mostly a PoE and VLAN isolation problem, which is the part I build for.",
        ask="Are APs and cameras on the same switching layer, and how are you segmenting them?"),
    "ISP": dict(
        subject="Access layer cost per port",
        hook="I do access switches for WISPs and small ISPs, where the number that matters is cost per subscriber port.",
        ask="How many subscribers per access switch, and what uplink ratio are you designing to?"),
    "INFLUENCE": dict(
        subject="Sample unit for your training lab",
        hook="You teach and design on MikroTik, so you are the person whose opinion actually reaches buyers. I would rather you test the hardware than hear a pitch.",
        ask="Would a sample unit and the full CLI / MIB documentation be useful in your lab?"),
}
DEFAULT = dict(
    subject="Access switching — quick question",
    hook="I build managed access switches (PoE and industrial) and your profile came up while I was looking at who is actually doing this work in your market.",
    ask="What are you using for access layer today, and where does it hurt?")

SPECS = {
    "POE": "24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.",
    "HOTEL": "24 gigabit PoE++ ports (APs, IP phones and IPTV boxes on one cable), per-room VLAN isolation, port isolation to stop guests plugging in their own router, IGMP snooping for the TV.",
    "MULTICAST": "IGMP snooping v2/v3, a querier so the VLAN stops flooding, multicast VLAN, fast leave, and DSCP/QoS queues — the things that decide whether IPTV is watchable and whether Dante audio drops out.",
    "INDUSTRIAL": "DIN rail, -40 to 75 C, wide input voltage, dual power input, ERPS ring under 20 ms, PoE++ for cameras and APs on the same unit.",
    "SWITCH": "L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.",
    "MTCSWE": "L3 hardware offload (line-rate forwarding off the CPU), QinQ and VLAN translation, ERPS and MSTP, ACLs and static routing, full CLI plus SSH plus SNMP with a private MIB.",
    "FIBRE": "4×10G SFP+ uplink, QinQ per subscriber, port isolation, broadcast storm control, IGMP for IPTV.",
    "CAMPUS": "PoE++ for APs, cameras and door controllers, per-building or per-classroom VLAN isolation, port isolation, IGMP snooping, enough total power budget to run a full floor.",
    "ISP": "4×10G uplink, QinQ subscriber isolation, port isolation, broadcast suppression, SNMP that drops into whatever NMS you already run.",
    "INFLUENCE": "Managed access switching in both commercial and DIN-rail industrial forms, full CLI/SSH/SNMP, and documentation you can teach from.",
}


# Distinctive English terms worth naming in a cold mail. Everything here is
# something a reseller would recognise as their own specialism.
DISTINCTIVE = [
    "hospitality", "multi-dwelling", "MDU", "captive portal", "hotel",
    "Dante", "Audinate", "IPTV", "multicast", "PIM-SM", "IGMP",
    "WISP", "FTTH", "GPON", "FTTC", "DOCSIS", "ETTH",
    "switching", "QinQ", "EVPN", "VXLAN", "ERPS", "MSTP", "RSTP",
    "hardware offload", "L3", "VLAN", "802.1x", "RADIUS",
    "industrial", "IT/OT", "BMS", "KNX", "warehouse", "automation",
    "access control", "CCTV", "surveillance", "intercom", "motorsports",
    "campus", "education", "healthcare", "government", "utilities",
    "agriculture", "grid control", "marine", "stadium", "venue", "festival",
    "VoIP", "Asterisk", "WireGuard", "IPsec", "redundancy", "high availability",
    "monitoring", "The Dude", "CAPsMAN", "SwitchOS", "RoMON", "Netinstall",
]
STOP = {"the", "and", "you", "with", "for", "from", "that", "this", "are", "not",
        "all", "any", "has", "have", "our", "his", "its", "was", "been", "more",
        "also", "both", "such", "into", "over", "than", "then", "when", "where"}


def concrete_detail(note):
    """Pick the two or three most telling English terms from a Chinese note."""
    if not note:
        return ""
    found = []
    for term in DISTINCTIVE:
        if re.search(re.escape(term), note, re.I) and term.lower() not in STOP:
            found.append(term)
    if not found:
        # fall back to any capitalised technical token
        toks = re.findall(r'\b([A-Za-z][A-Za-z0-9+#\-]{2,})\b', note)
        found = [t for t in dict.fromkeys(toks) if t.lower() not in STOP][:3]
    if not found:
        return ""
    if len(found) == 1:
        return found[0]
    return ", ".join(found[:-1]) + " and " + found[-1]


def build(name, person, country, city, key, sku, note):
    """Return (subject, body) for one account."""
    t = SCEN.get(key, DEFAULT)
    spec = SPECS.get(key, SPECS["SWITCH"])
    who = (person or "").strip() or name.split(" / ")[0].strip()
    first = who.split()[0] if who else "there"

    # The notes are written in Chinese, so quoting a raw sentence would drop a
    # Chinese clause into an English mail. Instead lift the English technical
    # terms, which is where the real specificity lives anyway.
    detail = concrete_detail(note)

    lines = []
    lines.append("Hi %s," % first)
    lines.append("")
    lines.append(t["hook"])
    if detail:
        lines.append("")
        lines.append("What caught my eye is that you work on %s." % detail)
    lines.append("")
    lines.append("Where we may be useful: %s" % spec)
    lines.append("")
    lines.append(t["ask"])
    lines.append("")
    lines.append("If it is easier to judge from hardware than from a datasheet, I can send a %s evaluation unit and you can put it in a rack for 30 days. "
                 "Otherwise a two-page spec sheet is one email away." % sku.split("（")[0].strip())
    lines.append("")
    lines.append("Either way, no follow-up sequence from me.")
    lines.append("")
    lines.append("Best,")
    lines.append("[your name]")
    return t["subject"], "\n".join(lines)
