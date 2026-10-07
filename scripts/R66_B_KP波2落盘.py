# -*- coding: utf-8 -*-
"""R66 B 面 KP 波 2:B-048/B-115/B-154/B-178 四户(kp 直接带结构化列表)。"""
import json

PRICE = '$180 USD EXW (2026-10-07, 15天有效)'
O = 'official-self-published·谱/leads-only(直发需 opt-in)'
G = 'leads-only·待 opt-in(LinkedIn/谱面带核)'

def fu():
    return [
        {'stage': '第 1 次跟进 · 具名 kp 引路口', 'push': 'STC-424XGGPM-280W', 'angle': '具名 kp 引路 → 采购/技术硬件分载线',
         'question': '贵司 24 口 PoE 交换机的硬件采购线由哪位同事主责？', 'proof': '规格页'},
        {'stage': '第 2 次跟进 · 一页目录卡', 'push': '一页目录卡', 'angle': '价值层 PoE 谱链卡', 'question': '可否入谱链名录？', 'proof': '卡'},
        {'stage': '第 3 次跟进 · 留档+LinkedIn 谱', 'push': '—', 'angle': '谱链明智途径', 'question': '—', 'proof': '—'},
    ]

def rec(code, name, heads, kp, evs, scene, size, sw, risk, email_sal,
        inference='R66 B 面 KP 波 2 具名金谱', trend='2026-10-08 R66-B 波 2 谱名牌', gap='R66-B 波 2 谱面锁定'):
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 波次二点名**'
    dims = {'业务定位': heads, '产品线与在售品牌': '(波次二补谱面)', '目标行业与场景': scene, '团队与规模': size,
            '决策链与对接人': kb, '技术与认证': '(波次二补)', '采购与供应链信号': '(波次二补)',
            '近期动态与线索': trend, '与我方契合点': '24 口 value PoE 谱链窗口', '风险与注意': risk}
    dimensions = {'背景深描': heads, '芯片与在用型号': '(待谱面二补)', '关键人KP': kb,
                  '关注点与资质': sw[0],
                  '优缺点SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3],
                  'Saga产品适配': '24 口 value PoE(' + PRICE + '):' + scene + ';' + risk}
    facts = [{'dim': e['dim'], 'text': e['quote'], 'quote': e['quote'], 'url': e['source']} for e in evs]
    swot_text = ('- **S**:%s\n- **W**:%s\n- **O**:%s\n- **T**:%s' % sw)
    return {'code': code, 'researched_on': '2026-10-08(R66-B 波 1)',
            'fact': name + ':' + heads, 'inference': inference,
            'hypothesis': '24 口 value PoE(' + PRICE + ')具名谱位引路', 'evidence_main': evs[0]['source'],
            'tech': '(波次二补)', 'hr': size, 'contact_found': kb, 'contact_pending': '直发具名需 opt-in',
            'dims': dims, 'dimensions': dimensions, 'evidence': evs, 'facts': facts,
            'followups': fu(), 'swot_text': swot_text, 'unknowns56': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': '(待谱面二补)', '③KP 深挖': kb,
                             '④Saga 对标': '24 口 value PoE(' + PRICE + ')', '⑤在乎与偏好': sw[0],
                             '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['直发具名需 opt-in'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': '波次二补', '合作方式': '未知', '缺口证据': '(波次二)'},
                    'gap_proof': gap},
            'kp': [{'name': k[0], 'role': k[1], 'contact': k[2], 'status': k[3], 'source': k[4]} for k in kp],
            'unknowns': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'email_subject': 'PoE switching for your line',
            'email': email_sal + '\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-07, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?\n\nBest regards,\nSaga Networks Export Desk'}

def ev(d, q, u):
    return {'dim': d, 'quote': q, 'source': u}

R = []

R.append(rec('B-048', 'Riva.Ltd',
    'Riva.Ltd(保加利亚;2026-10-08 R66-B 波 2 排噪:公开面命中 Riva(CRM 软件,Stéphane Zanoni,加拿大/Edmonton)+Gruppo Riva/Riva Acciaio(意钢铁 5500 人,Claudio Riva/Emilio Riva)均为异名实体,均非保加利亚 CSV 入档 Riva.Ltd 本体;实体身份未锁)',
    [],
    [ev('业务定位', 'Riva(CRM Software):CEO Stéphane Zanoni;117 employees;$24.6M(加拿大件,排噪)', 'https://www.datanyze.com/companies/riva/355631585'),
     ev('业务定位', 'Gruppo Riva(钢铁,Chaired by Claudio Riva since May 2014;5,000+;意大利件,排噪)', 'https://www.linkedin.com/company/gruppo-riva'),
     ev('近期动态与线索', '2026-10-08 R66-B 波 2:守档排噪;波次二=保加利亚 BRR(Търговски регистър)按名反查+CSV 原域锚复核', 'https://portal.registry.bg/')],
    '保加利亚 Riva.Ltd(身份待锁)', '(未锁定)',
    ('CSV 已有谱名', '实体身份未锁定', 'BRR 登记册反查可破', '同名噪声高'),
    '守档:加拿大 CRM/意钢铁排噪录;R66 波次二点名(BRR 反查)', '',
    inference='R66 B 面 KP 波 2 守档(身份未锁)', trend='2026-10-08 R66-B 波 2 守档', gap='R66-B 波 2 身份未锁'))

R.append(rec('B-115', 'Allnet.Greece',
    'ALLNET Greece(希腊;=**ALLNET GmbH 国际网→Allnet Italia S.p.A 希腊延展臂**(allnet-italia.it 官方 Network 页自署:「strategic extension of Allnet Italia on the Greek market」);集团谱:ALLNET GmbH=1991 慕尼黑 Germering 创(35 年谱;€300M+ 营业额;三物流中心;领先 ICT 分销商+自有牌;ALLDIS 姊妹;**Allnet International Network=€500M+ 合计/60,000+ 欧洲伙伴/德意法瑞奥北欧中东欧+中国台湾直在**)',
    [('Wolfgang Marcus Bauer', 'CEO & Founder, ALLNET GmbH(1991 创;集团创位;RocketReach CEO&Founder 谱)', 'allnet-italia.it 官方 Network 页具名(集团创办史)+RocketReach', O, 'https://www.allnet-italia.it/en/allnet-international-network/'),
     ('Marc Plesse', 'ALLNET Product Manager(MClimate 分销稿引语具名)', 'mclimate.eu 双盟合作稿引语', G, 'https://mclimate.eu/blogs/blog/allnet-and-mclimate-established-a-distribution-partnership')],
    [ev('业务定位', 'ALLNET Greece represents the strategic extension of Allnet Italia on the Greek market, with the aim of bringing ICT solutions with high added value and supporting local partners(allnet-italia.it 官方页)', 'https://www.allnet-italia.it/en/allnet-international-network/'),
     ev('决策链与对接人', 'ALLNET GmbH is the company that originated the network.Founded in 1991 by Wolfgang Marcus Bauer in Munich;turnover more than EUR 300 million;EUR 500 million+ aggregate/60,000+ partners', 'https://www.allnet-italia.it/en/allnet-international-network/'),
     ev('近期动态与线索', 'ALLNET and MClimate distribution partnership(2023):responsible ALLNET product manager Marc Plesse;Violeta Mitsova CCO MClimate', 'https://mclimate.eu/blogs/blog/allnet-and-mclimate-established-a-distribution-partnership')],
    '希腊 ALLNET 延展臂(集团一线 ICT 分销)', '集团 €500M+ 谱',
    ('集团一线 ICT 分销+€300M 谱', '希腊在地具名谱未破', '集团 Bauer/PM Plesse 具名', '大牌厂商直供链'),
    'Greece 在地谱未破:波次二点名(Allnet Italia 希腊队具名页)', ''))

R.append(rec('B-154', 'Allnet.Italia S.p.A',
    'ALLNET.ITALIA S.p.A.(意大利 Casalecchio di Reno(Bologna 都市圈);**2000 创(26 年谱;Società per azioni)**;**营业额 €87,915,037(2024,it.wikipedia 引财报件)**;谱型=意大利 ICT 高附加值分销商(ALLNET GmbH 战略同盟;专业渠道:SI/经销/安装商/服务商;网络→2004 VoIP→统一通信/视频会议/IP 监控/无线/工业自动化/Wi-Fi;Asterisk 唯一授权培训伙伴;NetAlly 伙伴;Audiocodes 渠道件);allnet-italia.it',
    [('Wolfgang Marcus Bauer', 'ALLNET GmbH CEO & Founder(德国母体战略同盟创位;集团谱)', 'allnet-italia.it 官方 Network 页具名', O, 'https://www.allnet-italia.it/en/allnet-international-network/')],
    [ev('业务定位', 'ALLNET.ITALIA S.p.A. is a high added-value distributor, specialised in innovative ICT and telecommunications solutions;Founded in 2000 in Bologna;strategic alliance with ALLNET GMBH (Munich 1991)(Audiocodes 伙伴页)', 'https://www.audiocodes.com/partners/locators/channel-partner-locator/europe-middle-east-africa/allnetitalia'),
     ev('团队与规模', 'Fatturato: 87.915.037 € (2024);Fondazione: 2000 a Bologna;Sede principale: Casalecchio di Reno;canale professionale ICT(it.wikipedia 引财报件)', 'https://it.wikipedia.org/wiki/Allnet.Italia'),
     ev('业务定位', 'the only authorized training partner for the region;Asterisk training classes out of its headquarters in Bologna', 'https://www.asterisk.org/asteriskexchange/allnet-italia/')],
    '意大利 ICT VAD 一线(€87.9M/2024)', '2000 创;SpA 谱',
    ('€87.9M 一线 VAD+培训伙伴', '意侧具名谱未破', 'Camera di Commercio Bologna 反查可破', '大牌厂商直供链'),
    '意侧具名谱未破:波次二点名(商会董事层+官网 team 页)', ''))

R.append(rec('B-178', 'GOODSTORE',
    'GOODSTORE(拉脱维亚 Daugavpils,Muzeja iela 11 / Vidus iela 32, LV-5401;=**SIA "Goodman Group"**;**注册号 41503064521,VAT LV41503064521**;Swedbank AS HABALV22 账户件;**2013 创(弱电系统设计建造;2023 开 goodstore.lv 电商线)**;谱型=拉脱维亚认证安防系统集成+弱电/网络件电商(CCTV/安防/门禁/消防/安装材/线缆/网络件/光纤/电源/太阳能;聚焦高复杂度技术安防系统工程;goodman.lv)',
    [],
    [ev('业务定位', 'GOODSTORE is an online store created by the company SIA "Goodman Group";Registration number: 41503064521;VAT: LV41503064521;Muzeja street 11, Daugavpils(goodstore.lv 官方 About 自署)', 'https://goodstore.lv/en/about-us/'),
     ev('业务定位', 'Founded in 2013 Daugavpils;2023 Launch of Goodstore.lv;certified security system integrator in Latvia(goodman.lv 官方页)', 'https://goodman.lv/'),
     ev('近期动态与线索', '2026-10-08 R66-B 波 2:身份=SIA Goodman Group 注册号锁;人名谱零命中→守档;波次二=拉脱维亚 UR(ur.gov.lv)按 41503064521 反查董事层', 'https://info.ur.gov.lv/')],
    '拉脱维亚 Daugavpils 安防集成+电商', '2013 创;SIA 小实体',
    ('认证集成+电商双线+注册号锁', '人名谱零命中', 'UR 登记册反查可破', '大牌安防件链'),
    '守档:身份锁定(41503064521);R66 波次二点名(UR 董事层)', '',
    inference='R66 B 面 KP 波 2 守档(身份锁定)', trend='2026-10-08 R66-B 波 2 守档', gap='R66-B 波 2 人名未破'))

with open('batch/B类深挖_2026-10-08_R66_BKP波2.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 B 面 KP 波 2:Riva(BG 排噪)+Allnet.Greece(集团 Bauer 金谱)+Allnet.Italia(€87.9M VAD)+GOODSTORE(LV SIA Goodman Group 注册号锁)四户',
               'scope': 'BG/GR/IT/LV 谱;Riva CRM/钢铁排噪;乌克兰守界不动',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 B 面 KP 波 2 四户落盘')
