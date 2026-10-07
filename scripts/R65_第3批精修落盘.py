# -*- coding: utf-8 -*-
"""R65 B 类深挖第 3 批:R64 KP 猎捕战果 7 户并入精修层(零新搜,素材=KP猎捕_B_R64_第1批.json)。"""
import json

kpb = {r['code']: r for r in json.load(open('batch/KP猎捕_B_R64_第1批.json', encoding='utf-8'))['records']}
src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

C = {}

C['B-005'] = dict(
    head=('Nextron AS/ApS(丹麦分部:Fuglevangsvej 13, 1962 Frederiksberg C;CVR 38306979,2016-12-29 注册;'
          '7 员工 DKK 10.7M 毛利/25.21% 利润比;挪威母 Nextron AS(2000 创,~65 人,$5.5M+,Oslo 总+4 北欧办);'
          'Supermicro 组件组装商,Nvidia PNY EDU 北欧独家,液冷 AI DC 方向;挪威 MikroTik Master 挂(非主业=机柜配套)'),
    kpnote=('丹麦分部:Håkon Aleksander Børstad Gutierrez = Direktør;Carl Henrik Sibbern = Bestyrelsesformand;'
            'Geir Elstad/Kim Nicolai Strømsborg 董事;mail 函数=info@nextron.dk'),
    facts=[
 {'dim': 'R64 商业登记', 'text': 'CVR 38306979 · 2016 注册 · 7 员工 · DKK 10.7M 毛利 · 董事 Gutierrez/Sibbern/Elstad/Strømsborg 全实名',
  'quote': 'Nextron ApS … CVR 38306979 … Direktør Håkon Aleksander Børstad Gutierrez … Bruttofortjeneste 10 687 tkr … Antal ansatte 7',
  'url': 'https://www.proff.dk/firma/nextron-aps/frederiksberg-c/elektronik-og-telekommunikationsudstyr/0MT1URI10MY'},
 {'dim': 'R64 集团谱', 'text': '挪威母 Nextron AS(2000,65 人,4 北欧办)=真正体量;丹麦分部是分销窗口',
  'quote': 'Nextron builds and sells custom servers … offices in Oslo, Stockholm, Copenhagen and Helsinki',
  'url': 'https://gh.linkedin.com/company/nextron'},
    ])

C['B-106'] = dict(
    head=('MS Electronics Ltd(7 Spyrou Kyprianou, Linopetra, Limassol 4103;1992 塞浦路斯消费 AV+电子大分销;'
          '50+ 品牌官方,800+ dealer 网络;11 员工;IT&Networking 为子类目,Security/Mobile/Solar 并列;'
          'R64 KV 对上:名录 pieris@mstronics.com = Pieris Michael Product Manager Networking&IT(2016 至今))'),
    kpnote=('Panicos Michael = Managing Director;Pieris Michael = Product Manager Networking&IT(2016-);'
            'Michalis Pavlou = Sales Director;Theodoros Theodorou = Product Manager(Nicosia)'),
    facts=[
 {'dim': 'R64 实名层', 'text': 'Panicos Michael MD(网络层母公司 Miche);Pieris Michael 产品线 KP(网络对口);Michalis Pavlou 销市总监',
  'quote': 'Panicos Michael is the Managing Director of MS Electronics Ltd … Pieris Michael Product Manager Networking and IT 2016 - now',
  'url': 'https://rocketreach.co/ms-electronics-ltd-profile_b4479492facba323'},
 {'dim': 'R64 PRODUKT 对口', 'text': 'Pieris Michael 公司域失联……已证为库内 pieris@mstronics.com 名录联系人(历史既有,无需再猜)',
  'quote': 'Pieris Michael … has 3 emails: @hotmail.com @icloud.com @mstronics.com', 'url': 'https://rocketreach.co/pieris-michael-email_102832452'},
    ])

C['B-307'] = dict(
    head=('ACC Distribution UAB(Kaunas Raudondvario pl. 131B;公司码 135150085,VAT LT351500811;1998 注册=28 年;'
          '股本 €691,856.20;ACME Grupė 全资(Stepas Telešius/Tomas Palšis/Stede W. Ingram 各 29.16%);'
          '2025 营收 €394.49M/净利 €5.75M;300+ 供应商/20,000+ SKU/7 公司(LT/LV/EE)/200+ 员工;'
          'CONTEXT ChannelWatch 2022 四奖立陶宛分销/网络安全伙伴/客服/物流;+370 37 333933 / +370 682 11646)'),
    kpnote=('Žymantas Baušys = Direktorius(2017-07-05 至今,前财务总监 2015-);'
            'Regimantas Buožius = 董事会主席(1998 创始人,现主战略);',
           ),
    facts=[
 {'dim': 'R64 商业登记', 'text': 'Žymantas Baušys Direktorius 2017-07-05 起(okredo.lt);公司码 135150085',
  'quote': 'Žymantas Baušys, Direktorius | Įstatinis kapitalas 691 856,20 EUR | Kaunas, Raudondvario pl. 131B',
  'url': 'https://okredo.com/lt-lt/imone/uab-acc-distribution-135150085'},
 {'dim': 'R64 集团与换帅', 'text': 'ACME Grupė 全资;Buožius(创始人)退居董事长,Baušys 升董事 2017',
  'quote': 'Nuo šių metų liepos … direktoriaus pareigas eis Žymantas Baušys … UAB „ACME Grupė" akcijas dengia Stepas Telešius, Tomas Palšis ir Stede W. Ingramas',
  'url': 'https://www.vz.lt/vadyba/is-tarnybos-i/2017/06/02/acc-distribution-turi-nauja-direktoriu'},
    ])

C['B-320'] = dict(
    head=('TELESYSTEM SRL(CUI RO22460883,J2007001650049,2007-09-25 注册,Bacău Spiru Haret nr. 8 showroom;'
          '安防+IT&C 全国批发:总部 Bacău + București/Cluj/Iași 仓点;Hikvision/Honeywell/Uniview/MikroTik/TRENDnet/UniPos 等 40-70 牌官方;'
          '三点股东结构(D.I./D.M./N.M.R.),D.M.=David Marian Administrator 公示,0728 105 124;安装商/集成商专供)'),
    kpnote=('David Marian = Administrator(公安许可台账实名);Marian David(Marketing 同姓口径);'
            'Monica Balcu KAM;Stefan Cosa 产品经理;Răzvan Dobocan BDM Cluj'),
    facts=[
 {'dim': 'R64/Administrator 实名', 'text': 'Societatea TELESYSTEM S.R.L. administrată de David Marian(公安/许可证台账公开);companywall/termene 对应 D.M. 缩写股东',
  'quote': 'Societate: Telesystem S.R.L. administrată de David Marian … Contact David Marian 0234/551055 0728 105 124 office@telesystem.ro',
  'url': 'https://www.protectiesipaza.ro/sisteme-de-alarma/telesystem-s-r-l-sisteme-de-alarma/'},
 {'dim': 'R64 商业登记', 'text': 'CUI RO22460883,2007-09-25,功能正常,三位股东三位董事(缩写台账)',
  'quote': 'TELESYSTEM SRL CUI 22460883 J2007001650049 Funcţiune … 3 shareholders and 3 directors',
  'url': 'https://termene.ro/en/firma/22460883-TELESYSTEM-SRL'},
    ])

C['B-352'] = dict(
    head=('IEI Technology USA Corp.(138 University Parkway, Pomona CA 91768;1997 组,台湾 IEI Integration Corp 美国子;'
          '集团墙注纪律维持:R53 判定 hold=Teddy Kuo 创始人/Meiji Chang 董事长/Jordan Jiang GM 集团侧,Subi Zhang CISO 复层直管;'
          'USA 侧 Richard Kao Operation Director(Pomona)+Wendy Wang Office Manager(2005 至今);'
          '美国侧向 AI/边缘计算/安防/医械/国警/交运/通信基站垂直'),
    kpnote=('USA 层:Richard Kao Operation Director;Wendy Wang Office Manager;'
            '集团层(R53 已 hold 纪律,不直谈):Teddy Kuo/Meiji Chang/Jordan Jiang'),
    facts=[
 {'dim': 'R64 USA 层 KP', 'text': 'Richard Kao Operation Director(LinkedIn, Pomona)+Wendy Wang Office Manager(2005)',
  'quote': 'Richard Kao - Operation Director at IEI Technology USA Corp. Pomona … Wendy Wang OFFICE MANAGER Feb 2005 - Present',
  'url': 'https://www.linkedin.com/in/richard-kao-233a5368/'},
 {'dim': 'R64 集团谱', 'text': '台湾母 IEI Integration:Teddy Kuo Founder/Meiji Chang Chairman/Jordan Jiang GM(Subi Zhang CISO 懂中国产——集团墙口径维持)',
  'quote': 'Founder Teddy Kuo and Chairman Meiji Chang … Jordan Jiang serves as the General Manager and Director … Subi Zhang CISO',
  'url': 'https://www.pressreleasepoint.com/user/iei-technology-usa-corp'},
    ])

C['B-436'] = dict(
    head=('Qtopia(Kolstee 5, 7021 NZ Zelhem, Achterhoek 乡村区;2013 创立,'
          '双创始董事 Dennis van Elk + Jan Geert Hek;40 粉丝 LinkedIn;Microsoft Gold Partner;'
          'CEH/CNDA/TOGAF 证书;安全+软件开发+架构+顾问,服务教育与 SME;088-7110500,info@qtopia.nl;'
          'R57 具名 j.g.hek@qtopia.nl 公司域)'),
    kpnote=('Dennis van Elk + Jan Geert Hek = 双创始董事(2013);Hek 15 年大规模防火墙系经验/SEI 认证架构师/Ethical Hacker'),
    facts=[
 {'dim': 'R64 双创始', 'text': 'Dennis van Elk + Jan Geert Hek 2013 创立,directeuren van Qtopia 官网口径',
  'quote': 'Qtopia is gestart in 2013 door Dennis van Elk en Jan Geert Hek … Dennis van Elk en Jan Geert Hek, directeuren van Qtopia … T: 088-7110500 E: info@qtopia.nl',
  'url': 'https://www.oostgelderlandbusiness.nl/magazine/artikel/328/9632/qtopia:-kennis-is-een-krachtig-wapen'},
 {'dim': 'R64 证书谱', 'text': 'Microsoft Gold Partner + Certified Ethical Hacker + CNDA + TOGAF 全谱认证(安全主攻)',
  'quote': 'beschikt Qtopia over certificeringen waaronder Certified Ethical Hacker, Certified Network Defence Architect en TOGAF. Tevens is Qtopia Microsoft Gold Partner',
  'url': 'https://nl.linkedin.com/company/qtopia'},
    ])

C['B-512'] = dict(
    head=('MTK Technologies, Inc.(Champaign, Illinois;1996 创立本地 IT 咨询公司,51-200 人,$19M+ 年收口径;'
          'Microsoft Server/SQL/Exchange/Untangle/Sonicwall/VMware 支持+270+ LOB 应用;'
          'Kailash Chakravarti = President(zoominfo 确认),@mtktechnologies.com 模式(库内 CSV mtk-tech.com 域名需核正)'),
    kpnote=('Kailash Chakravarti = President;Sayyed Fazal = Business Development Manager(Dover DE)'),
    facts=[
 {'dim': 'R64 董事实名', 'text': "Kailash Chakravarti President @ MTK Technologies(zoominfo 未锁版; k***@mtktechnologies.com 模式提示=president 域)",
  'quote': "Kailash Chakravarti's role at MTK Technologies is President … k***@mtktechnologies.com",
  'url': 'https://www.zoominfo.com/p/Kailash-Chakravarti/1721726706'},
 {'dim': 'R64 域核正', 'text': 'CSV 网站=mtk-tech.com(简缩);实际职能域疑为 mtktechnologies.com(全员邮箱长域),需核 XML', 
  'quote': 'MTK Technologies, Inc. is a small, locally owned IT consulting firm based in Champaign, Illinois … since 1996 … Microsoft network support',
  'url': 'https://www.zoominfo.com/c/mtk-technologies-inc/346288944'},
    ])


def apply(code, add):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 3 批精修 = R57 转写 + R64 KP 猎捕战果并入)'
    r['dimensions']['背景深描'] = add['head']
    if kpb.get(code, {}).get('persons'):
        r['kp'] = [{'name': p['name'],
                    'role': p['role'][:60],
                    'contact': (list(p['email_candidates'].values())[0] if p.get('email_candidates') else '—'),
                    'status': p.get('email_state', '—')[:40],
                    'source': p.get('source', 'R64')[:80]} for p in kpb[code]['persons']]
    r['dimensions']['关键人KP'] = add['kpnote'] if isinstance(add['kpnote'], str) else add['kpnote'][0]
    r['facts'] += add['facts']
    r['fih56']['fact'] += ' | R64 并入:' + (add['kpnote'] if isinstance(add['kpnote'], str) else add['kpnote'][0])[:60]
    return r


out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 3 批(R64 KP 战果并入层)',
       'scope': 'B-005 Nextron / B-106 MS Electronics / B-307 ACC Distribution / B-320 TELESYSTEM / B-352 IEI USA / B-436 Qtopia / B-512 MTK',
       'discipline': '与 R64 guessed-leads-only 纪律一致;R53 集团墙对 B-352 维持;不改评级不出信',
       'records': [apply(c, C[c]) for c in ('B-005', 'B-106', 'B-307', 'B-320', 'B-352', 'B-436', 'B-512')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第3批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 3 批 7 户落盘')
