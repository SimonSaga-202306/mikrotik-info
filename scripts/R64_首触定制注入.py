# -*- coding: utf-8 -*-
"""R64 首触定制稿(R63 新升 12 户 KP 点名)落盘+注入。"""
import json, glob

DRAFTS = {
 'A-579': dict(kp='Lionel Weckerle', role='采购部负责人', to='l.weckerle@edox.com(候选系;或 commercial@edox.com 转交)',
   subject='24-port PoE+ with 10G uplinks for the EDOX shelves',
   body="""Hi Lionel,

As purchasing lead for EDOX's networking lines, you'll know where the margins hide on 24-port managed PoE.

We manufacture a 24-port Gigabit PoE+ switch (280W budget, 4x10G SFP+ uplinks, ERPS<20ms, PoE watchdog) under full neutral/white-label terms. Reference: $180 USD EXW (2026-10-07, valid 15 days) - built to sit between your MikroTik CRS and the premium brands.

One question: which model currently carries that value tier at EDOX - and would a documented evaluation unit earn a place on your bench?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-582': dict(kp='Ihsan Aslan', role='Purchase Manager', to='ihsan.aslan@vodanetsystems.com(候选系)',
   subject="A value-tier 24-port PoE switch for Vodanet NJ warehouse",
   body="""Hi Ihsan,

Vodanet's 25-brand line-up - Juniper, HPE Aruba, Fortinet, MikroTik, Teltonika - has one obvious value gap: 24-port managed PoE with real 10G uplinks at import-friendly cost.

We build exactly that: 24 Gigabit PoE+ ports, 280W budget, 4x10G SFP+, ERPS ring <20ms, hardware PoE watchdog. Neutral packing, your label if wanted. Reference: $180 USD EXW (2026-10-07, valid 15 days).

One question: what currently fills that slot in your New Jersey warehouse stock - and can I send one unit for a 30-day evaluation?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-577': dict(kp='Peter Jezernik', role='董事/50%业主', to='peter.jezernik@pec-sistemi.si / peter@tehnox.si(候选系)',
   subject='PoE switch line beside your DIGITUS range',
   body="""Hi Peter,

Twenty-five years of importing DIGITUS and distributing MikroTik/Ubiquiti from Maribor - you know the reseller shelf better than most.

We make a 24-port Gigabit PoE+ managed switch (280W, 4x10G SFP+ uplinks, ERPS<20ms, PoE watchdog) with clean English documentation, white-label friendly. Reference: $180 USD EXW (2026-10-07, valid 15 days).

One question: between DIGITUS and MikroTik on your tehnox.si shelves, who holds the 24-port managed PoE value tier today - and would one documented sample earn a listing test?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-572': dict(kp='Thomas Thoma', role='Managing Director', to='thomas.thoma@art2soft.com(名录源)/ info@cy-wireless.com(官网)',
   subject='PoE switching for your WISP/ISP channel in Cyprus',
   body="""Hi Thomas,

Six vendor lines through Nicosia - MikroTik, Ubiquiti, Cambium, RF elements, Fanvil, Yeastar - suggests your installers live on PoE budgets.

We manufacture a 24-port Gigabit PoE+ switch (280W, 4x10G uplinks, ERPS<20ms, watchdog that cold-reboots frozen APs) under neutral packing. Reference: $180 USD EXW (2026-10-07, valid 15 days).

One question: which PoE switch do your Cyprus/WISP installers default to at 24 ports - and would a documented evaluation unit get a fair test at ART2SOFT?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-573': dict(kp='Grazian Twonski', role='Founder & CEO', to='grazian.twonski@etree.de / twonski@etree.de(候选系;总线 sales@etree.de)',
   subject='A vendor line that actually moves: 24-port PoE+',
   body="""Hi Grazian,

From a Cologne garage to 40,000 SKUs in fourteen years - you clearly only add lines that move.

Ours is one product, not a catalogue: a 24-port Gigabit PoE+ managed switch, 280W budget, 4x10G SFP+ uplinks, ERPS<20ms, PoE watchdog, neutral packing. Reference: $180 USD EXW (2026-10-07, valid 15 days) - priced to sit under your MikroTik CRS and Ubiquiti alternatives.

One question: who owns the 24-port PoE value tier on etree.de today - and is one documented sample worth a bench test to your team?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-574': dict(kp='Eugenia Zito / Alessandro Monti', role='Presidente / 产品专员', to='eugenia.zito@nimwave.com / alessandro.monti@nimwave.com(候选系;info@dnet-distribution.com)',
   subject='PoE 24 ports + 10G uplinks for your installer channel',
   body="""Dear Eugenia, dear Alessandro,

Dnet-Distribution's shelves already run CRS305/CRS317 - the WISP installers you serve keep asking for the 24-port PoE workhorse under them.

We build it: 24x Gigabit PoE+ (280W), 4x10G SFP+, ERPS<20ms, watchdog auto-reboot, neutral packing. Reference: $180 USD EXW (2026-10-07, valid 15 days).

One question: who holds that 24-port managed PoE tier for your installer channel today - and may I send one documented unit to Lainate for a 30-day test?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-570': dict(kp='Tomer Shitrit', role='Ronitek Distribution 负责人', to='tomer@ronitek.co.il(候选系;Info@ronitek.co.il 现有)',
   subject='24-port PoE value tier between your UniFi and CRS shelves',
   body="""Hi Tomer,

A full-spectrum Tel Aviv importer stocking RDS2216 down to hAP - your catalogue knows exactly where the PoE gaps are.

We build one product well: 24-port Gigabit PoE+ managed switch, 280W, 4x10G SFP+ uplinks, ERPS<20ms, PoE watchdog, neutral packing. Reference: $180 USD EXW (2026-10-07, valid 15 days) - the documented value tier between UniFi and CRS.

One question: on ronitek.co.il today, which 24-port managed PoE holds the value slot - and would one unit earn a listing test with your integrator clients?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-571': dict(kp='—(人名待定,走职能口)', role='—', to='Support@triple-core.com(官网公开)+ WhatsApp +970 59 498 1993',
   subject='PoE+ switching tier beside your six vendor lines',
   body="""Hello Triple Core team,

Six authorized lines - MikroTik, Ubiquiti, RF elements, MaxLink, MasterLAN, Cudy - and 4,000+ wholesale ISP clients across Ramallah and Jerusalem means your PoE volumes are real.

We manufacture one thing seriously: 24-port Gigabit PoE+ managed switch, 280W, 4x10G SFP+ uplinks, ERPS<20ms, watchdog. Neutral packing. Reference: $180 USD EXW (2026-10-07, valid 15 days) - notably under your CRS318 shelf.

One question: which 24-port PoE model leads your wholesale numbers today - and would a documented evaluation unit be useful to your purchasing team?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-578': dict(kp='Sergey Shapovalov', role='Regional Manager', to='sergey.shapovalov@takopi.ge(候选系;info@smart-network.ge)',
   subject='A PoE+ value tier for your 25-brand portfolio',
   body="""Hi Sergey,

Someone who led networking product teams at Treolan knows exactly where a 24-port PoE+ value tier sits in a 25-brand portfolio.

We build it: 24 Gigabit PoE+ ports (280W), 4x10G SFP+ uplinks, ERPS<20ms, hardware watchdog, neutral packing. Reference: $180 USD EXW (2026-10-07, valid 15 days).

One question: in Takopi's Tbilisi stock today, which model holds that tier - and would a documented evaluation unit earn bench time beside your MikroTik and Netgear lines?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-580': dict(kp='Piotr Poniatowski', role='本人=业主/顾问', to='piotr@poniatowski.pl(已有,official)',
   subject="Hardware worth showing to Poland's biggest MikroTik group",
   body="""Hi Piotr,

Founder of the largest Polish MikroTik group, MBUM speaker, MTCSWE holder - you see every switch that enters the Polish MikroTik world.

We manufacture documented PoE switches (24-port PoE+ 280W, 4x10G, ERPS<20ms; also 8-port models) for OEM/white-label programs - neutral packing, your model numbers.

One question: which PoE switches do you currently point group members and clients to for enterprise builds - and would an engineering evaluation unit interest you personally?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-583': dict(kp='Barry Higgins', role='本人=业主/Trainer', to='barry@allness.net(候选系;官网表单备份)',
   subject='A documented PoE switch for your training benches',
   body="""Hi Barry,

Ten years running a WISP, training MTCNA through MTCEWE at Kidderminster - your students see whatever sits on your bench.

We build engineering-grade PoE switches (24-port PoE+ 280W with 4x10G; 8-port 240W), fully documented, neutral packing. A comparison unit in switching labs shows trainees how different CLIs solve the same L2+ job. Reference: $180 USD EXW (2026-10-07, valid 15 days).

One question: what switch do your students learn PoE budgets on today - and would one documented unit be worth bench space at Allness?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
 'A-584': dict(kp='Ron Touw', role='本人=业主/UK 首位 Trainer', to='ron@mikrotiktraining.co.uk(候选系;官网在线 shop 备份)',
   subject="For the lab at Britain first MikroTik trainer",
   body="""Hi Ron,

UK's first certified trainer, ten certifications, author of the course that became MTCEWE - more MikroTik engineers carry your habits than anyone in the country.

We make documented PoE switches (24-port PoE+ 280W, 4x10G uplinks, ERPS; 8-port compact), neutral packing, white-label friendly. For training labs, a second-vendor switch is the cleanest way to show CLI differences on identical L2+ tasks. Reference: $180 USD EXW (2026-10-07, valid 15 days).

One question: which PoE hardware do your London lab sessions run today - and would one evaluation unit be welcome on the bench?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)"""),
}

def main():
    json.dump({'date':'2026-10-07','round':'R64','scope':'R63 新升 12 户 KP 点名首触定制稿(英语;发送前用户改名+核价)',
               'discipline':'一次一问;P1 唯一;$180 USD EXW 15 天有效;guessed 邮箱先小批量试探,退信即换',
               'drafts':DRAFTS}, open('batch/首触定制_R64_KP点名_2026-10-07.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
    for code, d in DRAFTS.items():
        fn = glob.glob(f'profile/A/{code}-*.md')[0]
        t = open(fn, encoding='utf-8').read()
        L = ['', '## 2026-10-07 R64 首触定制稿(KP 点名)', '',
             f"**对象**:{d['kp']}({d['role']})",
             f"**通道**:{d['to']}", '',
             f"**主题**:{d['subject']}", '', '```text', d['body'], '```', '',
             '> 发送前检查:①不出现「Made in China」;②落款换用户本人;③guessed 邮箱先单发试探,退信即换通道;④问 API 话题先反问架构(纪律)。']
        t = t.rstrip() + '\n' + '\n'.join(L) + '\n'
        open(fn, 'w', encoding='utf-8').write(t)
        print('首触稿注入:', code)

if __name__ == '__main__':
    main()
