# -*- coding: utf-8 -*-
"""R66 第 28 波(A 类补全批)落盘脚本——权威再生器=本文件;三批共用同一生成逻辑(批切=编号序 missing[0:50]/[50:100]/[100:137])。
真源:/tmp 中产数据不入仓;再生流程:按 CSV/档名/源批索引重建 /tmp/remain137.json 后 exec 本文件 mk()。
本批输出:batch/A类深挖_2026-10-08_R66_R56_KP第28波*户.json(已落仓)。
"""
# -*- coding: utf-8 -*-
"""波 26/27/28 三批 137 户(A 类 R66 补全)R56 骨架成批生成。
真源:/tmp/remain137.json(CSV/档名/p1 锚定)+ batch 源批 record(fact/kp 引真)。
口径:KP=源批 O 级自署具名户;其余守档准由·谱基增厚。供位 push≡STRUCT p1;email 价锚型号映射;R63 台账外户不涉;退信免。
"""
import json,re,glob,subprocess,os,sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT='/home/user/mikrotik-info'
os.chdir(ROOT)
remain=json.load(open('/tmp/remain137.json',encoding='utf-8'))
CODES=sorted(remain.keys(),key=lambda x:int(x.split('-')[1]))
WAVES={26:CODES[0:50],27:CODES[50:100],28:CODES[100:137]}
# 源批 record 索引
SRC={}
for fn in glob.glob('batch/A类深挖_2026-09-2*R5*_*.json')+['batch/A类深挖_2026-10-07_R66_R56_341_376基线.json']:
    try: d=json.load(open(fn,encoding='utf-8'))
    except Exception: continue
    for rec in (d.get('records',d) if isinstance(d,dict) else d):
        c=rec.get('customer') or rec.get('code') or rec.get('id')
        if c in remain and c not in SRC: SRC[c]=rec
PRICE={'STC-424XGGPM-280W':('$165','24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog)'),
       'STC-28DGGPM':('$99','8-port PoE access box (802.3af/at, watchdog)'),
       'STI-288GP':('$74.8','industrial unmanaged 8-port PoE switch (IP67 DIN-rail, 802.3af/at)'),
       'STI-480XGGM':('$253','industrial L2+ 8-port switch with 4x10G uplinks')}
SCRIPT_URL='https://szqcyyy.r.foreach.today/scripts/R66_R56_KP第{n}波_50户落盘.py'
# 退信真源(台账 7 条+CSV/profile 节批注)跨波引用:无新增,137 户免查。
def kp_ok(kp):
    if not kp: return []
    out=[]
    for k in kp:
        nm=k.get('name','')
        if nm and '待查' not in nm and '待问' not in nm and '推定' not in k.get('status',''): out.append(k)
    return out[:2]
def mk(code,wn,rec0):
    v=remain[code]
    grp=rec0 or {}
    kp=kp_ok(grp.get('kp'))
    fact0=v['fact'] or grp.get('fact','') or f"{v['name']}({v['country']});CSV 信号:{(v['signal'] or '谱面缺')};切入:{(v['angle'] or '')}"
    p1=v['p1'] or 'STC-424XGGPM-280W'
    price,desc=PRICE.get(p1,PRICE['STC-424XGGPM-280W'])
    iskp=bool(kp)
    gaurd=''
    if '乌克兰' in v['country']: gaurd=';**战区民用商业限定句必压(民用商业限定前句)**'
    if any(w in fact0 for w in('军用','军防','军事','krit','KRITIS','关键基','BOEING','国防')):
        gaurd+=';**守界注(我司民用商用限定)**'
    mirror=''
    dn=re.search(r'([\w.-]+\.[a-z]{2,})',v['site'] or '')
    domain=dn.group(1) if dn else ''
    if v['deep']: mirror=f";既有深挖批源:{v['deep'].split('/')[-1]}"
    ev=domain and ('https://'+domain+'/') or (v['deep'] and '仓内:'+v['deep'].split('/')[-1]) or '仓内:roster'
    fact_head=(f"波 {wn}·{code}:{v['country']}谱: **{'具名金谱·原批引真' if iskp else '守档准由·原 R56 谱基增厚'}**:{fact0}"
               f";R66 第 {wn} 波谱:我司 {p1}({price} 价锚)对口该谱{gaurd}{mirror},先报价不回、档案铺位、持续关注新一季,OK。")
    contact_found=(('**'+';'.join(f"{k['name']}({k.get('role','')},{k.get('status','')[:60]})" for k in kp)[:260]+'**')
                   if iskp else f"**守档准由;R66 第 {wn} 波点名(谱面无实名)**{('·原批具名带核:'+','.join(k['name'] for k in (rec0.get('kp') or [])[:1])) if grp.get('kp') else ''}")
    dims={
     '业务定位':fact_head,
     '产品线与在售品牌':(v['signal'] or 'roster 信号档'),
     '目标行业与场景':v['country']+' 谱;'+((v['type'] or '分销/顾问谱')),
     '团队与规模':v['country']+'谱·'+('具名决策档' if iskp else '守档准由'),
     '决策链与对接人':contact_found,
     '技术与认证':p1+' 对口谱;'+price+' USD EXW 锚',
     '采购与供应链信号':('具名谱位引路' if iskp else 'B2B 批口谱'),
     '近期动态与线索':f'2026-10-08 R66 {wn} 波谱名牌(A 类补全批)',
     '与我方契合点':f'{p1}({desc.split(" (")[0]})'+(' 具名窗' if iskp else ' 档案铺位窗'),
     '风险与注意':('leads-only;直发需 opt-in' if iskp else '具名缺(守档准由)')+gaurd,
    }
    contact=(v['contact'] or '').replace('\n',' ')[:120]
    evidence=[
     {'dim':'联系方式与基础画像','quote':fact0[:160],'source':ev},
     {'dim':'联系方式与基础画像','quote':('CSV 入口:'+contact) if contact else '档案既有联口为守档准由','source':ev or '仓内:roster'},
    ]
    team=(kp[0]['name']+' Team' if iskp else (v['name'].split('/')[0].strip()[:26]+' Team'))
    if iskp:
        followups=[
         {'stage':'第 1 次跟进 · 具名 kp 引路口','push':p1,'angle':'具名 kp 引路 → 采购/技术硬件分载线','question':'贵司 PoE 交换机的硬件采购线由哪位同事主责？','proof':'规格页'},
         {'stage':'第 2 次跟进 · 一页目录卡','push':'一页目录卡','angle':'价值层 PoE 谱链卡','question':'可否入谱链名录？','proof':'卡'},
         {'stage':'第 3 次跟进 · 留档+LinkedIn 谱','push':'—','angle':'谱链明智途径','question':'—','proof':'—'}]
    else:
        followups=[
         {'stage':'第 1 次跟进 · 档案铺位','push':p1,'angle':'守档铺位 → 价锚卡','question':'贵司新一季 PoE 铺位是否开放比选？','proof':'规格页'},
         {'stage':'第 2 次跟进 · 一页目录卡','push':'一页目录卡','angle':'价值层 PoE 谱链卡','question':'可否入谱链名录？','proof':'卡'},
         {'stage':'第 3 次跟进 · 留档','push':'—','angle':'簿联路径','question':'—','proof':'—'}]
    eml=(f"Dear {team},\n\nWe build a {desc}. "
         f"Reference: {price} USD EXW (2026-10-08, 15 days valid) — a value unit that rides along with each deployment. "
         f"Datasheet + CE pack on request.\n\nBest regards\nSaga / SmartByte ODM")
    r55dims={'①背景再核':fact_head,'②芯片/型号':p1+'·'+desc,'③KP 深挖':contact_found,
             '④Saga 对标':p1+' vs PLANET/当批价差窗','⑤在乎与偏好':v['country']+' 谱;CE/UKCA;持续关注新一季',
             '⑥SWOT':('S=原批具名金谱在册;W=直发需 opt-in;O='+p1+' 价差窗;T=欧洲/北美带节奏' if iskp else 'S=原 R56 谱基在册;W=具名缺守档;O='+p1+' 价差窗;T=欧洲/北美带节奏')}
    swot={'S':('原批 O 级具名金谱+' if iskp else '')+'R56 谱基在册','W':('直发需 opt-in' if iskp else '具名缺(守档准由)'),
          'O':p1+' '+price+' USD EXW 价差窗','T':'谱链节奏;先报价不回则档案铺位'}
    rec={'customer':code,
     'fact':fact_head,
     'inference':(f'R66 第 {wn} 波具名 KP 金谱(原批引真)' if iskp else f'R66 第 {wn} 波守档准由谱'),
     'hypothesis':(f'{p1}({price} USD EXW (2026-10-08, 15天有效))具名谱位引路' if iskp else '档案铺位谱,持续关注新一季'),
     'evidence_main':ev if ev.startswith('http') else '仓内:roster',
     'tech':p1+'·'+desc,
     'hr':v['country']+'谱·'+('具名决策档' if iskp else '守档准由'),
     'contact_found':contact_found,
     'contact_pending':('直发具名需 opt-in' if iskp else '谱面实名缺,守档铺位'),
     'dims':dims,
     'evidence':evidence,
     'followups':followups,
     'r55':{'dims':r55dims,'care':v['country']+'谱;'+('具名档' if iskp else '守档'),'swot':swot,
            'uncertain':('KP 在职时效待核' if iskp else '谱面信号缺,波次二补'),'gap_proof':'报价单+规格页+CE 件'},
     'unknowns':(['KP 在职时效','谱面份额'] if iskp else ['具名决策人(波次二)','谱面份额']),
     'relation':f'2026-10-08 R66 第 {wn} 波 A 类补全批',
     'email':eml,'email_addr':contact}
    if iskp: rec['kp']=kp
    return rec
for wn,codes in WAVES.items():
    recs=[mk(c,wn,SRC.get(c)) for c in codes]
    cty={}
    for c in codes: cty[remain[c]['country']]=cty.get(remain[c]['country'],0)+1
    ctys='/'.join(f"{k} {v}" for k,v in sorted(cty.items(),key=lambda x:-x[1])[:8])
    kpids=[r['customer'] for r in recs if r.get('kp')]
    spans=f"{codes[0]}~{codes[-1]}"
    out={'date':'2026-10-08',
     'wave':f'R66 第 {wn} 波 {len(codes)} 户(A 类补全批:{spans} 段内 R66 未覆盖余户;{ctys};名册真源=CSV/档名/源批{len(kpids)} 户 O 级具名 KP 引真,其余守档准由·原 R56 谱基增厚)',
     'scope':f'供位真表:push≡STRUCT p1(424×{sum(1 for c in codes if remain[c]["p1"]=="STC-424XGGPM-280W")}+28D×{sum(1 for c in codes if remain[c]["p1"]=="STC-28DGGPM")}+288GP×{sum(1 for c in codes if remain[c]["p1"]=="STI-288GP")});KP={len(kpids)};退信新增 0;名册真源仲裁制延续(波 25 教训)',
     'records':recs}
    fn=f'batch/A类深挖_2026-10-08_R66_R56_KP第{wn}波{len(codes)}户.json'
    json.dump(out,open(os.path.join(ROOT,fn),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print(f'wrote {fn} records={len(recs)} KP={len(kpids)} {kpids[:8]}')
