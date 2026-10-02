#!/usr/bin/env python3
# R60(2026-09-29)A 类 568 户一次性运营判定注入:
# ① 摘除 53 处「;未测试投递」标注(用户首轮开发信已发完)
# ② 5 户退信补「发不过去」标签 + 找新邮箱方法行
# ③ 每户注入 R60 区块:KP 领英直达 / 中国进口与管制 / 芯片谱 / 大概率 Saga 型号(调查结论)
# ④ 落 batch/A类_三项判定与KP领英_R60_2026-09-29.json
# 用法: python3 scripts/R60_A类运营判定注入.py
import glob, os, re, json, csv, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = '2026-09-29'

# ---------- 数据底座 ----------
base = json.load(open('/tmp/r60_base.json', encoding='utf-8'))
kp_verify = json.load(open('/tmp/r60_kp_verify.json', encoding='utf-8'))
chip = json.load(open(os.path.join(ROOT, 'batch/A类_芯片谱_2026-09-29.json'), encoding='utf-8'))
sp = json.load(open(os.path.join(ROOT, 'batch/structured_profiles_v1.json'), encoding='utf-8'))
brand_hits = json.load(open(os.path.join(ROOT, 'batch/A类_中国品牌命中_2026-09-29.json'), encoding='utf-8'))
brand_map = {h['code']: h for h in brand_hits}

CN_COUNTRY = {
    '美国': ('高', 'Covered List+SECURE Act+§301 关税;采购方警惕中国标签,话术锚 Marvell(美企)+FCC'),
    '加拿大': ('高', '2022 禁华为 5G;企业层警惕,话术同上'),
    '瑞典': ('高', 'PTS 2020 全面禁华为 5G;政治偏冷'),
    '德国': ('中', 'IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM'),
    '英国': ('中', 'NCSC 2027 华为 HNT 移除(电信网);企业网开放;PSTI 合规'),
    '意大利': ('中', 'Golden Power 5G/能源延伸;企业交换机不受限'),
    '波兰': ('中', 'NCSA 2024 高风险供应商禁(5G/军队);亲美倾向'),
    '荷兰': ('中', 'NCSC 政府供应商排除;企业网自由'),
    '法国': ('中', 'ANSSI 3A 授权制;企业交换机不限'),
    '乌克兰': ('中', '战争期;华为/中兴仍在售,部分转向北约标准;货款周期与物流保险另计'),
    '捷克': ('中', 'NUKIB 2018.12 警示;政府网规避,企业网自由'),
    '罗马尼亚': ('中', '2021 禁华为 5G 法案;企业层自由'),
    '保加利亚': ('中', 'EU 5G Toolbox 跟随;常规'),
    '立陶宛': ('中', '跟随 EU Toolbox;对华偏冷'),
    '拉脱维亚': ('中', '同上'),
    '爱沙尼亚': ('中', '同上'),
    '匈牙利': ('低', '政府亲华;2024 华为匈 5G 强进;可正面谈中国产能'),
    '希腊': ('低', '政治摇摆、Cosco 比港;华为存量大'),
    '塞尔维亚': ('低', '亲华倾向强;华为巴尔干枢纽'),
    '西班牙': ('低', '务实采购;电信层只登记不排斥'),
    '葡萄牙': ('低', '务实;NOS/MEO 有华为量'),
    '瑞士': ('低', '中立;企业网完全开放'),
    '奥地利': ('低', '跟随 EU 但干预少'),
    '丹麦': ('中', 'EU 跟随;政府层谨慎'),
    '挪威': ('中', 'EU 跟随;政府层谨慎'),
    '芬兰': ('中', 'EU 跟随;政府层谨慎'),
    '克罗地亚': ('中', '常规 EU'),
    '斯洛伐克': ('中', '常规 EU'),
    '斯洛文尼亚': ('中', '常规 EU'),
    '摩尔多瓦': ('中', '亲欧转向;常规'),
    '土耳其': ('中', '摇摆;BTK 注册+政府偏好'),
    '马其顿': ('低', '小国务实'),
    '阿尔巴尼亚': ('低', '小国务实'),
    '马耳他': ('低', '小国务实'),
    '塞浦路斯': ('低', '小国务实'),
    '爱尔兰': ('中', 'EU 跟随'),
    '比利时': ('中', 'EU 跟随(NATO/EU 总部谨慎度略高)'),
    '卢森堡': ('中', 'EU 跟随'),
    '冰岛': ('低', '小国'),
    '以色列': ('中', '亲美技术栈;无禁但偏好美系'),
}
DEFAULT_COUNTRY = ('中', 'EU 5G Toolbox 跟随档;企业网开放')

# 芯片谱分桶
chip_bucket = {}
for k in ('Marvell已确认', 'Broadcom谱', 'Qualcomm谱', 'MediaTek谱', 'Realtek谱', '无芯片信号'):
    for rec in chip[k]:
        chip_bucket[rec['code']] = k.replace('已确认', '')
ind_set = set(chip['工业锚'])

# 品牌主营(CSV 信号) → 中国进口概率
def china_judge(code, country, sig):
    lvl, note = CN_COUNTRY.get(country, DEFAULT_COUNTRY)
    parts = [f'国别档位 {lvl}({note})']
    bh = brand_map.get(code)
    if bh:
        parts.append('档案信号: 在卖中国品牌 ' + '/'.join(bh['brands']) + ' → 对中国产线接受度已被事实验证')
    s = (sig or '')
    if any(x in s for x in ('TP-Link', 'TPLink', 'Huawei', '华为', 'Hikvision', 'Dahua', 'ZTE', 'Ruijie')):
        parts.append('CSV 品牌谱含中国厂商 → 大概率已有中国采购线(集采或分销)')
    if lvl == '高':
        parts.append('战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询')
    elif lvl == '低':
        parts.append('战术: 可正面谈中国产能/成本优势')
    else:
        parts.append('战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片')
    if not bh and not any(x in s for x in ('TP-Link', 'Huawei', 'Hikvision', 'Dahua', 'ZTE', 'Ruijie')):
        parts.append('户级进口史: 档案无信号(是否从中国进口过 → 待定)')
    return ';'.join(parts)

def chip_judge(code):
    b = chip_bucket.get(code, '无芯片信号')
    ind = code in ind_set
    if b == 'Marvell':
        t = 'Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对'
    elif b == 'Broadcom':
        t = 'Broadcom 谱信号(如 RUCKUS ICX);Marvell 以性价比对照切入,BCM 备选方案可备'
    elif b == 'Qualcomm':
        t = '高通谱信号(纯无线 AP/CPE 线);交换机位空 → Marvell 后背交换直接补位,无冲突'
    elif b in ('MediaTek', 'Realtek'):
        t = 'MTK/Realtek 散件谱;Marvell 以稳定性升级位切入'
    else:
        t = '待定(档案无芯片信号,首开先问品牌谱)'
    if ind:
        t += ';工业锚(Moxa/Westermo 类)提及 → Marvell 工业谱同源,STI-288GP 强对口'
    return t

def saga_judge(code):
    d = sp.get(code)
    if not d:
        return '待定(无结构化谱,R60 后补)'
    needs = d.get('needs') or {}
    pri = []
    if needs.get('industrial'):
        pri.append('STI-288GP(工业导轨 24G+4×10G→机柜/自动化)')
    if needs.get('poe') and needs.get('tenG'):
        pri.append('STC-424DGGPM-280W(48G PoE++/4×25G→智算安防酒店全谱)')
    elif needs.get('poe'):
        pri.append('STC-28DGGPM(24G PoE+/4×25G→分销走量)')
    if needs.get('tenG') and not needs.get('poe'):
        pri.append('STI-480XGGM(48×10G/6×100G→万兆汇聚)')
    bm = d.get('business_model') or ''
    if not pri:
        if '分销' in bm or 'VAD' in bm:
            pri.append('STC-28DGGPM(分销走量款)')
        elif '顾问' in bm or '培训' in bm or '咨询' in bm:
            pri.append('CONSULT-OEM(顾问谱非硬件首倡,讲合作框架)')
    vol = d.get('volume_potential') or 0
    if pri:
        extra = ''
        if vol >= 4: extra = '(批量潜力高,可上 280W 旗舰对照行)'
        return '大概率会用: ' + '、'.join(pri[:2]) + extra
    return '待定(业务模型信号太薄,首开问谱后判定)'

def lk_url(name, company):
    q = urllib.parse.quote(f'{name} {company}'.strip())
    return f'https://www.linkedin.com/search/results/people/?keywords={q}'

# CSV 行索引
rows = list(csv.DictReader(open(os.path.join(ROOT, '客户名单_反向信号_2026-09.csv'), encoding='utf-8-sig')))
csv_map = {r['档案编号']: r for r in rows if (r.get('评级') or '').strip() == 'A'}

# 二跑模式:KP 用清噪清单(company_words 过滤) + 公司页显示名归一
kp_clean = json.load(open('/tmp/r60_kp_clean.json', encoding='utf-8'))
base['kp_names'] = {k: v for k, v in kp_clean.items()}

# ---------- ① 未测试投递摘除 ----------
n_untest = 0
for p in glob.glob(os.path.join(ROOT, 'profile/A/A-*.md')):
    t = open(p, encoding='utf-8').read()
    nt = t.replace(';未测试投递]', ']').replace('(未测试投递)', '').replace('未测试投递;', '')
    if nt != t:
        n_untest += t.count('未测试投递')
        open(p, 'w', encoding='utf-8').write(nt)
print(f'① 摘除「未测试投递」标注 {n_untest} 处')

# ---------- ② 5 户退信补标 ----------
BOUNCE = {
    'A-054': ('steffo@direktronik.se', 'blocked 服务器拒收', 'Fredrik Brunzell fredrik.brunzell@direktronik.se(主)+46 8 52 400 700 总机'),
    'A-096': ('info@lastmilegear.com', '地址不存在 not-found', 'sales@lastmilegear.com(主,官网与 X 双印证)+X 私信 @LastMileGear'),
    'A-101': ('sales@lloret.co.uk', 'blocked 服务器拒收', 'graham.budd@lloret.co.uk(具名 Graham Budd 主)+sales@ 抄送'),
    'A-103': ('uk@bechtle.com', '地址不存在 not-found', 'sales.uk@bechtle.com(主);本户在规模排除名单,仅归档不主动开发'),
    'A-105': ('info@cisilion.com', 'blocked 服务器拒收', 'marketing@cisilion.com(主);环球 SI 观察档,仅归档'),
}
FIND_TIP = '> 找新邮箱方法(R60 用户授权留存):① 官网 contact/about 页重扫;② Hunter.io 扫域名公开邮箱;③ 领英私信 KP(本档 R60 区块有直达链);④ 按 firstname.lastname@域名 格式推断并用 verify 工具核;⑤ 总机电话转 KP 直线'
for code, (bad, why, alt) in BOUNCE.items():
    p = glob.glob(os.path.join(ROOT, f'profile/A/{code}-*.md'))
    if not p: continue
    p = p[0]
    t = open(p, encoding='utf-8').read()
    tag = f'{bad}(发不过去·2026-09-29 退信:{why})'
    if tag not in t:
        t = t.replace(bad, tag, 1)
    if FIND_TIP not in t:
        # 追加到退信实测块之后;若无该块就附加到 R60 区块前(统一在 R60 区块里再写)
        t = t.rstrip() + f'\n\n{FIND_TIP}\n'
    open(p, 'w', encoding='utf-8').write(t)
print('② 5 户退信补标完成')

# ---------- ③ R60 区块注入 + ④ JSON ----------
jout = {}
files = sorted(glob.glob(os.path.join(ROOT, 'profile/A/A-*.md')))
assert len(files) == 568, len(files)
for p in files:
    code = os.path.basename(p)[:5]
    t = open(p, encoding='utf-8').read()
    if 'R60 客户运营判定' in t:
        continue
    # 户名与国家
    nm_co = os.path.basename(p)[6:-3]
    name, country = (nm_co.rsplit('-', 1) + ['?'])[:2] if '-' in nm_co else (nm_co, '?')
    if '-' in nm_co:
        name, country = nm_co.rsplit('-', 1)
    sig = (csv_map.get(code) or {}).get('信号（在卖什么品牌）', '')
    # KP:优先联络核验金标,其次正则提取,最后文件名
    kp_name, kp_src = None, None
    if code in kp_verify and kp_verify[code]['name'] and '未' not in kp_verify[code]['name']:
        kp_name = kp_verify[code]['name'].split('(')[0].strip()
        kp_src = '联络核验'
    if not kp_name and code in base['kp_names']:
        cands = [x for x in base['kp_names'][code] if x not in ('Google Workspace', 'General Inquiries')]
        if cands:
            kp_name, kp_src = cands[0], '档案正文提取'
    if not kp_name and ' ' in name and not any(w in name for w in ('GmbH', 'Srl', 'Inc', 'Ltd', 'BV', 'SpA', 'LLC', 'AB', 'SIA', 'S.A', 'S.A.', 'Kft')):
        kp_name, kp_src = name, '档案名(个人档)'
    # 领英:现成 URL > 搜索直达
    lk_direct = None
    if code in kp_verify and kp_verify[code].get('linkedin'):
        lk_direct = kp_verify[code]['linkedin'][0]
    elif code in base['profile_linkedin']:
        ins = [u for u in base['profile_linkedin'][code] if '/in/' in u]
        comps = [u for u in base['profile_linkedin'][code] if '/company/' in u]
        lk_direct = (ins or comps or [None])[0]
    company = name if kp_name != name else (csv_map.get(code) or {}).get('公司名', name).split('(')[0].strip()
    # 公司名若是个名子串(个人档同名公司),不再重复拼接
    def person_q(person, comp):
        pt = set(person.lower().split())
        ct = set(comp.lower().split()) if comp else set()
        if not comp or pt <= ct:  # 人名词已全部被公司名覆盖(个人档同名)→ 只搜人名
            return urllib.parse.quote(person)
        return urllib.parse.quote(f'{person} {comp}')
    if lk_direct:
        if '/company/' in lk_direct:
            kp_line = f'[{company} · 领英公司页]({lk_direct})(既有证据链接,来源:档案;公司页进群后可挑 KP 添加)'
            lk_kind = 'direct_company'
        else:
            disp = kp_name or company
            kp_line = f'[{disp}]({lk_direct})(既有证据链接,来源:档案/联络核验)'
            lk_kind = 'direct_person'
        lk_val = lk_direct
    elif kp_name:
        url = f'https://www.linkedin.com/search/results/people/?keywords={person_q(kp_name, company)}'
        kp_line = f'[{kp_name} · 领英搜索直达]({url})(搜索链接,点入后核职位再加;来源:{kp_src})'
        lk_kind, lk_val = 'search_person', url
    else:
        url = lk_url(company, '')
        kp_line = f'[{company} · 领英搜索直达]({url})(无具名 KP 信号,先搜公司再加人;待查)'
        lk_kind, lk_val = 'search_company', url
    china = china_judge(code, (csv_map.get(code) or {}).get('国家', country), sig)
    chipj = chip_judge(code)
    saga = saga_judge(code)
    block = f'''
---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:{kp_line}
- **中国进口与管制**:{china}
- **芯片谱(Marvell 专注度)**:{chipj}
- **大概率用到的 Saga 型号**:{saga}(本行为调查分析结论,与开发信首推型号是两回事)
'''
    t = t.rstrip() + '\n' + block
    open(p, 'w', encoding='utf-8').write(t)
    jout[code] = {
        'kp': {'name': kp_name, 'linkedin_kind': lk_kind, 'linkedin': lk_val, 'source': kp_src},
        'china_import_control': china,
        'chip_marvell_focus': chipj,
        'saga_models_judged': saga,
    }
json.dump(jout, open(os.path.join(ROOT, 'batch/A类_三项判定与KP领英_R60_2026-09-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'③④ R60 区块注入 {len(files)} 户 + JSON 落盘({len(jout)} 键)')
PYEOF_DONE = True
