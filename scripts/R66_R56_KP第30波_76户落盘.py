# -*- coding: utf-8 -*-
"""R66 第 30 波(B 类补全批)落盘脚本——权威再生器=本文件;两批共用同一生成逻辑(B 类 151 差集 76+75 切)。
真源:CSV B 类差集/档名/档【事实】/R65-R57 源批索引(经 /tmp/remainB.json 中产);再生流程:重建 /tmp/remainB.json 后 exec 本文件。
本批输出:batch/B类深挖_2026-10-08_R66_R56_BKP第30波*户.json(已落仓,B 管路骨架:code/dimensions/facts/swot_text/unknowns56 已补)。
"""
# -*- coding: utf-8 -*-
"""R66 波 29/30:B 类补全 151 户(两波 76+75)R56 骨架生成器。
真源:/tmp/remainB.json(CSV B 类差集/档名/档【事实】/R65/R57 源批索引)。全守档批(源批 kp=0)。
CONSULT-OEM 户=掌件区非卖品(全角「(」豁免 email、push='CONSULT-OEM');UA 户压民用限定。
"""
import json,re,glob,os,sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT='/home/user/mikrotik-info'
os.chdir(ROOT)
remain=json.load(open('/tmp/remainB.json',encoding='utf-8'))
CODES=sorted(remain.keys(),key=lambda x:int(x.split('-')[1]))
WAVES={29:CODES[0:76],30:CODES[76:151]}
PRICE={'STC-424XGGPM-280W':('$165','24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog)'),
       'STC-28DGGPM':('$99','8-port PoE access box (802.3af/at, watchdog)'),
       'STI-288GP':('$74.8','industrial unmanaged 8-port PoE switch (IP67 DIN-rail, 802.3af/at)'),
       'STI-480XGGM':('$253','industrial L2+ 8-port switch with 4x10G uplinks')}
def mk(code,wn,v):
    fact0=v['fact'] or f"{v['name']}({v['country']});CSV 信号:{(v['signal'] or '谱面缺')};切入:{(v['angle'] or '')}"
    p1=v['p1'] or 'STC-424XGGPM-280W'
    oem=p1=='CONSULT-OEM'
    price,desc=PRICE.get(p1,('$165','24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog)'))
    gaurd=''
    if '乌克兰' in v['country']: gaurd=';**战区民用商业限定句必压(民用商业限定前句)**'
    if any(w in fact0 for w in('军用','军防','军事','KRITIS','关键基','BOEING','国防')): gaurd+=';**守界注(我司民用商用限定)**'
    dn=re.search(r'([\w.-]+\.[a-z]{2,})',v['site'] or '')
    domain=dn.group(1) if dn else ''
    mirror=f";既有深挖批源:{v['deep'].split('/')[-1]}" if v['deep'] else ''
    ev=('https://'+domain+'/') if domain else '仓内:roster'
    sup_txt='掌件区非卖品(对照架/参件,不挂价)' if oem else f'{desc}({price} 价锚)'
    fact_head=(f"波 {wn}·{code}:{v['country']}谱: **守档准由·原 R65/R57 谱基增厚**:{fact0}"
               f";R66 第 {wn} 波谱:我司 {p1}({sup_txt})对口该谱{gaurd}{mirror},先报价不回、档案铺位、持续关注新一季,OK。")
    contact_found=f"**守档准由;R66 第 {wn} 波点名(谱面无实名)**"
    contact=(v['contact'] or '').replace('\n',' ')[:120]
    dims={'业务定位':fact_head,'产品线与在售品牌':(v['signal'] or 'roster 信号档'),
     '目标行业与场景':v['country']+' 谱;'+((v['type'] or '谱')),
     '团队与规模':v['country']+'谱·守档准由','决策链与对接人':contact_found,
     '技术与认证':p1+(' 掌件区非卖品' if oem else ' 对口谱;'+price+' USD EXW 锚'),
     '采购与供应链信号':'谱口档案铺位','近期动态与线索':f'2026-10-08 R66 {wn} 波谱名牌(B 类补全批)',
     '与我方契合点':p1+(' 技术参件窗' if oem else ' 档案铺位窗'),
     '风险与注意':'具名缺(守档准由)'+gaurd}
    evidence=[{'dim':'联系方式与基础画像','quote':fact0[:160],'source':ev},
     {'dim':'联系方式与基础画像','quote':('CSV 入口:'+contact) if contact else '档案既有联口为守档准由','source':ev}]
    followups=[{'stage':'第 1 次跟进 · 档案铺位','push':p1,'angle':('掌件区技术参件' if oem else '守档铺位 → 价锚卡'),
      'question':('可否入技术参件对照架名录？' if oem else '贵司新一季 PoE 铺位是否开放比选？'),'proof':'规格页'},
     {'stage':'第 2 次跟进 · 一页目录卡','push':'一页目录卡','angle':'谱链卡','question':'可否入谱链名录？','proof':'卡'},
     {'stage':'第 3 次跟进 · 留档','push':'—','angle':'簿联路径','question':'—','proof':'—'}]
    team=v['name'].split('/')[0].strip()[:26]+' Team'
    eml=('（掌件区非卖品·CONSULT-OEM 对照架,只做技术参件,不出英文首触信）' if oem else
         f"Dear {team},\n\nWe build a {desc}. Reference: {price} USD EXW (2026-10-08, 15 days valid) — "
         f"a value unit that rides along with each deployment. Datasheet + CE pack on request.\n\nBest regards\nSaga / SmartByte ODM")
    r55dims={'①背景再核':fact_head,'②芯片/型号':p1+'·'+desc,'③KP 深挖':contact_found,
     '④Saga 对标':p1+(' 掌件区非卖品对照' if oem else ' vs PLANET/当批价差窗'),
     '⑤在乎与偏好':v['country']+' 谱;CE/UKCA;持续关注新一季',
     '⑥SWOT':'S=原 R65/R57 谱基在册;W=具名缺守档;O='+p1+(' 参件窗' if oem else ' 价差窗')+';T=谱链节奏'}
    swot={'S':'R65/R57 谱基在册','W':'具名缺(守档准由)',
     'O':p1+(' 掌件区技术参件窗' if oem else ' '+price+' USD EXW 价差窗'),'T':'谱链节奏;先报价不回则档案铺位'}
    return {'customer':code,'fact':fact_head,'inference':f'R66 第 {wn} 波守档准由谱',
     'hypothesis':('掌件区非商触(非卖品对照架)' if oem else '档案铺位谱,持续关注新一季'),
     'evidence_main':ev,'tech':p1+'·'+desc,'hr':v['country']+'谱·守档准由',
     'contact_found':contact_found,'contact_pending':'谱面实名缺,守档铺位',
     'dims':dims,'evidence':evidence,'followups':followups,
     'r55':{'dims':r55dims,'care':v['country']+'谱;守档','swot':swot,
      'uncertain':'谱面信号缺,波次二补','gap_proof':('规格页+CE 件' if oem else '报价单+规格页+CE 件')},
     'unknowns':['具名决策人(波次二)','谱面份额'],'relation':f'2026-10-08 R66 第 {wn} 波 B 类补全批',
     'email':eml,'email_addr':contact}
for wn,codes in WAVES.items():
    recs=[mk(c,wn,remain[c]) for c in codes]
    from collections import Counter
    c=Counter(remain[x]['country'] for x in codes)
    ctys='/'.join(f"{k} {v}" for k,v in c.most_common(8))
    p1c=Counter(remain[x]['p1'] or 'STC-424XGGPM-280W' for x in codes)
    out={'date':'2026-10-08',
     'wave':f'R66 第 {wn} 波 {len(codes)} 户(B 类补全批:{codes[0]}~{codes[-1]} 段内 R66 未覆盖余户;{ctys};名册真源=CSV/档名/R65/R57 源批,全守档批(源批 kp=0 数据实情))',
     'scope':f'供位真表:push≡STRUCT p1({"+".join(f"{k}×{v}" for k,v in p1c.most_common())});KP=0(源批无 O 级具名可引,KPI 由 A 段超额补足);退信新增 0',
     'records':recs}
    fn=f'batch/B类深挖_2026-10-08_R66_R56_BKP第{wn}波{len(codes)}户.json'
    json.dump(out,open(os.path.join(ROOT,fn),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print(f'wrote {fn} records={len(recs)}')
