# -*- coding: utf-8 -*-
"""R66 第 21 波(50 户扩招批):A-279~A-328 顺延 50 户;公司档 30(Netonix WISP 谱 3+Allied 代理谱 25+分销 2)+人名司名同体培训谱档 20。"""
import json

PRICE = '$180 USD EXW (2026-10-08, 15天有效)'
O = 'official-self-published·谱/leads-only(直发需 opt-in)'
G = 'leads-only·待 opt-in(LinkedIn/谱面带核)'
STRUCT = json.load(open('batch/structured_profiles_v1.json', encoding='utf-8'))

def push_of(code):
    # 供位口径:一阶 push≡STRUCT p1(含 STC-424/CONSULT-OEM/STC-28DGGPM 各档,波 21 全型号版)
    return STRUCT.get(code, {}).get('p1') or 'STC-424XGGPM-280W'

def fu(push):
    return [
        {'stage': '第 1 次跟进 · 具名 kp 引路口', 'push': push, 'angle': '具名 kp 引路 → 采购/技术硬件分载线',
         'question': '贵司 24 口 PoE 交换机的硬件采购线由哪位同事主责？', 'proof': '规格页'},
        {'stage': '第 2 次跟进 · 一页目录卡', 'push': '一页目录卡', 'angle': '价值层 PoE 谱链卡', 'question': '可否入谱链名录？', 'proof': '卡'},
        {'stage': '第 3 次跟进 · 留档+LinkedIn 谱', 'push': '—', 'angle': '谱链明智途径', 'question': '—', 'proof': '—'},
    ]

def rec(code, name, heads, kp, evs, scene, size, sw, risk, email_sal,
        inference='R66 第 21 波具名 KP 金谱', trend='2026-10-08 R66 21 波谱名牌', gap='R66 21 波谱面锁定'):
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 第 21 波点名(谱面无实名)**'
    dims = {'业务定位': heads, '产品线与在售品牌': '(波次二补谱面)', '目标行业与场景': scene, '团队与规模': size,
            '决策链与对接人': kb, '技术与认证': '(波次二补)', '采购与供应链信号': '(波次二补)',
            '近期动态与线索': trend, '与我方契合点': '24 口 value PoE 谱链窗口', '风险与注意': risk}
    return {'customer': code, 'fact': name + ':' + heads, 'inference': inference,
            'hypothesis': '24 口 value PoE(' + PRICE + ')具名谱位引路', 'evidence_main': evs[0]['source'],
            'tech': '(波次二补)', 'hr': size, 'contact_found': kb, 'contact_pending': '直发具名需 opt-in',
            'dims': dims, 'evidence': evs, 'followups': fu(push_of(code)),
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': '(待谱面二补)', '③KP 深挖': kb,
                             '④Saga 对标': '24 口 value PoE(' + PRICE + ')', '⑤在乎与偏好': sw[0],
                             '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['直发具名需 opt-in'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': '波次二补', '合作方式': '未知', '缺口证据': '(波次二)'},
                    'gap_proof': gap},
            'kp': [{'name': k[0], 'role': k[1], 'contact': k[2], 'status': k[3], 'source': k[4]} for k in kp],
            'unknowns': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'email': email_sal + '\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-08, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?\n\nBest regards,\nSaga Networks Export Desk'}

def ev(d, q, u):
    return {'dim': d, 'quote': q, 'source': u}

R = []

# ============ 公司档×30 ============
R.append(rec('A-279', 'wlanparts',
    'WLanParts(美国 Pasadena, CA;**Crunchbase 谱:「large selection and distributor of wireless products」,状态 Closed=关铺谱**;档锚无公开站点;同名 Wireless Parts Inc(Santa Ana,Tammy Doan)=异体已分层)→**守档准由:铺已关+谱面无实名,记噪留档**)',
    [],
    [ev('决策链与对接人', 'Crunchbase: WLanParts (closed), Pasadena, CA — wireless products distributor;谱面无具名决策人=守档准由(2026-10-08 R66 21 波留痕)', 'https://www.crunchbase.com/organization/wlanparts'),
     ev('联系方式与基础画像', '档录: 美国;类型 WISP 集成商/代理(Netonix 谱);无公开站点(档案基础画像行)', '仓内 profile/A/A-279-*(档谱基础画像行)')],
    '美国 WISP 件分销(关铺谱)', '关铺档',
    ('—', '关铺谱', '无守档', '—'),
    '守档:铺关名缺(crunchbase closed 档)', 'Dear Sir or Madam,'))

R.append(rec('A-280', 'Invictus',
    'Invictus Wireless(美国 Tigard, OR;**B2B 无线网络硬件+设计/安装/排障(WiFi 至微波链路)**;**President & Founder: Rick Lindahl(Nextdoor 商家页自署帖=O 级自署)**;邻评 Rick/Steven 双人名谱',
    [('Rick Lindahl', 'President & Founder(Nextdoor 商家页自署)', 'nextdoor.com 商家自署帖(O)', O, 'https://nextdoor.com/pages/invictus-wireless/'),
     ('Steven(名谱)', '技术/服务人名(客户评价双人名谱)', 'nextdoor 评价件', G, 'https://nextdoor.com/pages/invictus-wireless/')],
    [ev('决策链与对接人', '「business-class wireless networking hardware… consulting & design to installation and troubleshooting… Wifi to Microwave Radio links. Thank you, **Rick Lindahl President and Founder**」(Nextdoor 商家页自署)', 'https://nextdoor.com/pages/invictus-wireless/'),
     ev('联系方式与基础画像', 'Tigard, OR;B2B wireless hardware+无线网设计安装;客户评「Rick and Steven… very knowledgeable」(nextdoor 件)', 'https://nextdoor.com/pages/invictus-wireless/')],
    '美俄勒冈 WISP 硬件+工程铺', '小铺谱',
    ('创始人自署帖=O 直达位', '小实体谱', 'Lindahl 直达位', '区域链竞谱'),
    'Rick Lindahl 直达(opt-in 律)', 'Dear Mr. Lindahl,'))

R.append(rec('A-281', 'UNIFYING SOLUTION',
    'Unifying Solution LLC(美国 Guthrie, OK 73044,1407 W Washington Ave;**2015 创;1 人铺;$156,818 营收估计;SIC 7373 计算机集成/VAR**;**Member: Jason Smedley**(manta/buzzfile 双目录件)',
    [('Jason Smedley', 'Member(LLC 成员;1 人铺主)', 'manta/buzzfile 目录双源', G, 'https://www.manta.com/c/mhwy7j9/unifying-solution-llc')],
    [ev('决策链与对接人', 'Contact Jason Smedley, Title: Member;established 2015;annual revenue est. $156,818;approximately 1 employee(manta/buzzfile 目录件)', 'https://www.buzzfile.com/business/Unifying-Solution-LLC-405-293-3282'),
     ev('联系方式与基础画像', '1407 West Washington Avenue, Guthrie, OK 73044;(405) 293-3282;SIC 7373 Computer Integrated Systems Design;NAICS 541512(manta 件)', 'https://www.manta.com/c/mhwy7j9/unifying-solution-llc')],
    '美俄克拉何马 1 人 VAR 微铺', '1 人铺;2015 创',
    ('1 人铺=直达', '营收微谱', 'Smedley 唯一直达位', '区域链竞谱'),
    'Jason Smedley 直达(opt-in 律)', 'Dear Mr. Smedley,'))

R.append(rec('A-282', 'Berdin Grupo',
    'Grupo Berdin, S.A.(西班牙 Donostia-San Sebastián;**CIF A20817391;1980 创(9 合伙人,Balleneros 16 起始);200 人;电气/电子件+照明+自动化分销集团**;**换代金谱:Gerente/Director General Xabier Ostolaza(2017-01-01 接替创始合伙人 F. Javier Fierro;前电信商务总监;proinstalaciones 专访 O)**:Alfonso del Río dir comercial+三区域总(Oscar Vilella 北/Enrique Viana 东/Javier Parro 中南)+Daniel Vilar dir informática+Harkaitz Arrizabalaga dir técnico+Laura Marino CFO+Estíbaliz Sesma RRHH+Javier Mentxaka 国家账户(**官网新闻件全谱 O 级**)',
    [('Xabier Ostolaza', 'Gerente/Director General(2017 换代接棒;专访 O)', 'proinstalaciones.com 专访件', O, 'https://www.proinstalaciones.com/entrevistas/2234-xabier-ostolaza-gerente-de-berdin-grupo'),
     ('Alfonso del Río', 'Director Comercial(官网销售梯队文 O)', 'berdin.com 新闻件', O, 'https://www.berdin.com/noticias/hablan-los-jefes-de-venta'),
     ('Oscar Vilella / Enrique Viana / Javier Parro', 'Jefes de venta 三区域总(北/东/中南)', 'berdin.com 新闻件', O, 'https://www.berdin.com/noticias/hablan-los-jefes-de-venta'),
     ('Daniel Vilar', 'Director de informática y digitalización(数字化=件链口)', 'berdin.com/alimarket 任命件', O, 'https://www.alimarket.es/construccion/noticia/342590/berdin-remodela-su-equipo-directivo'),
     ('Harkaitz Arrizabalaga', 'Director Técnico(技术总监)', 'alimarket 任命件', O, 'https://www.alimarket.es/construccion/noticia/342590/berdin-remodela-su-equipo-directivo')],
    [ev('决策链与对接人', '「sustituido por Xabier Ostolaza desde el 1 de enero de 2017… dirección general de Berdin Grupo… 200 personas」;梯队: Ostolaza(director)+Laura Marino(financiera)+Alfonso del Río(comercial)+Estíbaliz Sesma(RRHH)+Daniel Vilar(informática)+Harkaitz Arrizabalaga(técnico)(proinstalaciones/alimarket 件)', 'https://www.proinstalaciones.com/entrevistas/2234-xabier-ostolaza-gerente-de-berdin-grupo'),
     ev('联系方式与基础画像', 'GRUPO BERDIN SA;CIF A20817391;Donostia;fundada 1980(9 socios);200 personas;distribución material eléctrico y electrónico;技术部 20+ 工程师 5 业务区(einforma/proinstalaciones 件)', 'https://www.einforma.com/informacion-empresa/grupo-berdin')],
    '西班牙巴斯克 45 年电气分销集团', '200 人;1980 创',
    ('官网新闻件=O 级全梯队', '分销巨头谱', 'Ostolaza+Vilar 数字化口直达位', '一线链竞谱'),
    'Ostolaza 总座+del Río 商务位(opt-in 律)', 'Estimado Sr. Ostolaza,'))

R.append(rec('A-300', 'GBE Converge',
    'GBE Converge(英国 Gloucester(Barnwood);**1992 谱史/2016 GBE 消防安防+Converge IT 合并=双牌谱;158-196 人;$24M**;**Joint MD 双:Jason Buttle(GBE 方 MD,并购主导者引语 O)+Martyn Smith(Converge 创始人 2008,joint MD)**;梯队 Group FD Derek Gibby+Head BD EMEA Alex May+Contracts Dir Darren Fell/Dave Collins+Tech BU Dir Mark Hallett;教育(Gloucester Academy/Cheltenham College)+体育场(Ricoh Arena)=教育公段守界注',
    [('Jason Buttle', 'Managing Director(GBE 方;合并主导引语)', 'gfirstlep.com 合并件(引语)', O, 'https://www.gfirstlep.com/news/gbe-and-converge-unite-to-create-industry-powerhouse/'),
     ('Martyn Smith', 'Joint Managing Director(Converge 创始人;官网博文 O)', 'gbeconverge.com 博文件', O, 'https://gbeconverge.com/2018/03/22/martyn-smith-on-gbe-converges-it-solutions-for-smes/'),
     ('Derek Gibby', 'Group Finance Director', 'rocketreach 谱面条', G, 'https://rocketreach.co/gbe-converge-management_b54bd808f9f06a5b'),
     ('Alex May', 'Head of Business Development EMEA', 'rocketreach 谱面条', G, 'https://rocketreach.co/gbe-converge-management_b54bd808f9f06a5b')],
    [ev('决策链与对接人', '「Managing Director of GBE, Jason Buttle…make the acquisition」;「Martyn Smith is joint Managing Director…formed Converge in 2008 before merging with GBE in 2016」(gfirstlep/官网博文件)', 'https://www.gfirstlep.com/news/gbe-and-converge-unite-to-create-industry-powerhouse/'),
     ev('联系方式与基础画像', 'Gloucester(Barnwood+Staverton 双址);158-196 employees;$24M;Fire&Security+IT 合并谱;education/stadium 客户谱(rocketreach/gbeconverge 件)', 'https://rocketreach.co/gbe-converge-profile_b54bd808f9f06a5b')],
    '英格洛斯特消防安防+IT 合并谱大户', '158-196 人;£11M+',
    ('双 MD 联合谱+教育/体育场案', '合并集团谱', 'Buttle/Smith 双直达位', '一线链竞谱'),
    '双 MD 位(opt-in 律;教育段守界)', 'Dear Jason,'))

R.append(rec('A-301', '3TEC',
    '3TEC LTD(英国 Waltham Abbey,110 Brooker Road, EN9 1JH;**2012 创;2-10 人;统一通信+LAN 谱(Mitel/Gamma/Fortinet/Allied Telesis)**;谱面检索未锁具名决策人(RR 员工条串味弃用;CH 03816109 为 Coalville 异体)→**守档准由:牌链在档,具名待专批 CH 直查**)',
    [],
    [ev('决策链与对接人', '公开谱面未锁具名决策人=守档准由;LinkedIn 公司页(19 followers)/Facebook 页在档;specialties: Mitel, Gamma, Fortinet, Allied Telesis(2026-10-08 R66 21 波留痕)', 'https://www.linkedin.com/company/3tec-ltd'),
     ev('联系方式与基础画像', '110 Brooker Road, Waltham Abbey EN9 1JH;+44 20 8275 1120;social@3tec.co.uk;founded 2012;2-10 employees(rocketreach/FB 件)', 'https://rocketreach.co/3tec-ltd-profile_b468a32bfc5c9bbd')],
    '英 Waltham Abbey 小铺 UC+LAN 谱', '2-10 人;2012 创',
    ('Allied/Mitel 谱=件链', '微实体谱', '无守档', '—'),
    '守档:牌在名缺(待 CH 专批)', 'Dear Sir or Madam,'))

R.append(rec('A-302', 'ACC Yotta',
    'ACC Yotta(英国 Woking;**Jeff Rhys-Jones: Director @ ACCYotta(rocketreach 谱面条;兼 Owner @ YottaServe;现 Territory Director @ Admin By Request=离任/兼任差旗注)**;accyotta.com 谱面弱',
    [('Jeff Rhys-Jones', 'Director @ ACCYotta(谱面条;差旗:现职他司+自有 YottaServe)', 'rocketreach 谱面条', G, 'https://rocketreach.co/jeff-rhys-jones-email_33550928')],
    [ev('决策链与对接人', 'Work: Director @ ACCYotta;Owner @ YottaServe;Technical Director @ Emojo Ltd(rocketreach 谱面条;Woking GB)', 'https://rocketreach.co/jeff-rhys-jones-email_33550928'),
     ev('联系方式与基础画像', 'Woking, GB;档录类型: 集成商/代理(Allied Telesis 谱);accyotta.com(档案基础画像行+谱面核验)', 'https://www.accyotta.com')],
    '英 Woking 小 IT 谱铺', '小铺谱',
    ('Director 谱面孔在', '谱面弱+差旗', 'Rhys-Jones 位(差旗注)', '区域链竞谱'),
    'Jeff Rhys-Jones 位(opt-in 律;差旗待核)', 'Dear Jeff,'))

R.append(rec('A-303', 'Electracom-Trusol',
    'Trusol Limited(英国 Feltham(Middlesex),Unit 11 Mount Road Industrial Estate, TW13 6AR;**CH 04487827;2003 创 23 年;21-20 人;$5M;教育+企业+休闲三牌(trusol-education/trusol-it)**;**2024-02 换代窗:Neil Goodhead(2003 创主 MD)退位→Michelle Louise Sen 任 Director(2024-02-02)+PSC 唯一实控+Joanne Margaret Gammage 任 Director(2024-03);官网团队页仍示 Neil MD+Liz Goodhead FD+Mark O\'Farrell Procurement Officer(采购 KPI!)**',
    [('Michelle Louise Sen', 'Director+PSC 唯一实控(2024-02 接任;新班主)', 'CH/Endole 登记件', O, 'https://open.endole.co.uk/insight/company/04487827-trusol-limited'),
     ('Joanne Margaret Gammage', 'Director(2024-03 任;HR Director 谱)', 'CH 件+官网团队页', O, 'https://find-and-update.company-information.service.gov.uk/company/04487827/officers'),
     ("Mark O'Farrell", 'Procurement Officer(采购官=件链 KPI)', 'trusol-education.com 团队页(O)', O, 'https://trusol-education.com/our-team/'),
     ('Neil Goodhead', '前 MD/创主(2024-02 退休;官网/RR 仍署 MD=换代差旗注)', '官网团队页+CH 退位件', G, 'https://trusol-education.com/our-team/')],
    [ev('决策链与对接人', 'CH 2024-02: Notification of **Michelle Louise Sen as a person with significant control**;Termination of Neil Derek Goodhead as a director(02/02/2024);Appointment of Joanne Margaret Gammage(03/2024);官网团队: Neil MD+Liz FD+Michelle Services Director+**Mark O\'Farrell Procurement Officer**(CH/endole/trusol-education 件)', 'https://open.endole.co.uk/insight/company/04487827-trusol-limited'),
     ev('联系方式与基础画像', 'TRUSOL LIMITED 04487827;11 Mount Road, Feltham TW13 6AR;2003 创;21 employees;$5M;education/corporate/leisure 三牌(rocketreach/官网件)', 'https://rocketreach.co/the-trusol-group-profile_b5ee6c39f42e7628')],
    '英 Feltham 教育 IT+安防牌(2024 换代窗)', '21-20 人;2003 创',
    ('换代窗+采购官具名=KPI', '教育段守界注', 'Sen 新班+O\'Farrell 采购直达位', '一线链竞谱'),
    "Michelle Sen+O'Farrell 采购位(opt-in 律;教育段守界)", 'Dear Michelle,'))

R.append(rec('A-304', 'European Electronique',
    'EUROPEAN ELECTRONIQUE LIMITED(英国 Eynsham(Oxon),Forward House, Oakfields Industrial Estate, OX29 4TT;**CH 01704440;1988 创 38 年;110 人;£75M;私营 ICT 基建方案商(有线/无线网+网安+混合云)**;**Owner & CEO: Yolanta Anastazja Gill(波兰裔,华沙大学法律硕士+牛津 MBA,1996 入司;官网 CEO 页 O+CH 双 O)**;+Katarzyna Scout Gill Director(族谱)+Guy Daniel Parker FD;**公共段/教育框架谱(HP for Education Top Partner;Schools&Academies Show 2024)=公共守界注**',
    [('Yolanta Anastazja Gill', 'Owner & CEO(官网 CEO 页自署+CH Director 双源)', 'euroele.com CEO 页(O)', O, 'https://www.euroele.com/company-it-infrastructure-solutions/ceo-profile/'),
     ('Guy Daniel Parker', 'Director/Financial Director(CH+RR 双源)', 'CH 件', O, 'https://find-and-update.company-information.service.gov.uk/company/01704440/officers'),
     ('Katarzyna Scout Gill', 'Director(Gill 族谱)', 'CH 件', O, 'https://find-and-update.company-information.service.gov.uk/company/01704440/officers'),
     ('Pete Anderson', 'Head of Service Sales(服务销售口)', 'rocketreach 谱面条', G, 'https://rocketreach.co/european-electronique-management_b5c68ea8f42e0ce3')],
    [ev('决策链与对接人', '「Yolanta Gill is the owner and CEO…£75m ICT market leader…30 years trading history…privately owned」(euroele.com CEO 页);CH: GILL Yolanta Anastazja+GILL Katarzyna Scout+PARKER Guy Daniel(Active)', 'https://www.euroele.com/company-it-infrastructure-solutions/ceo-profile/'),
     ev('联系方式与基础画像', 'CH 01704440;Forward House, Eynsham OX29 4TT;founded 1988;110 employees;£75M;Wired/Wireless Networks+Cyber Security+Hybrid Cloud;**Public Sector frameworks+Education 谱=公共守界注**(官网/CH/RR 件)', 'https://find-and-update.company-information.service.gov.uk/company/01704440/officers')],
    '英牛津郡 £75M ICT 基建私营大户', '110 人;1988 创',
    ('38 年 Owner 亲政+£75M', '公共/教育段守界注', 'Gill+FD/服务销售直达位', '一线盟链竞谱'),
    'Yolanta Gill+Parker FD 位(opt-in 律;公共段守界)', 'Dear Ms Gill,'))

R.append(rec('A-305', 'Quadratek',
    'Quadratek(=PH15 Ventures Ltd)(英国 Hartley Wintney(Hampshire),Taplins Court Unit 6, Church Lane, RG27 8XU;**1997 创 29 年;51-200 人;IT 基建(结构化布线/网安/托管)**;**「A Defence supplier of 20+ years」官网 legal 页自署=军防守界加厚!**;**p1=STC-28DGGPM 供位谱(28 口)**;Jason Underhill President(zoominfo 目录谱 G)',
    [('Jason Underhill', 'President(zoominfo 目录谱)', 'zoominfo 目录件', G, 'https://www.zoominfo.com/pic/quadratek/31769135')],
    [ev('联系方式与基础画像', 'Site owned by **PH15 Ventures Ltd**;Taplins Court Unit 6, Hartley Wintney RG27 8XU;**A Defence supplier of 20+ years…employed Veterans and Reservists**(官网 legal 页自署)', 'https://quadratek.net/legal/'),
     ev('近期动态与线索', 'zoominfo: 51-200 employees;structured cabling/cybersecurity/managed services since 1997;defence/government/enterprise 客户谱;Jason Underhill President', 'https://www.zoominfo.com/pic/quadratek/31769135')],
    '英汉普郡军防系 IT 基建屋(守界加厚)', '51-200 人;1997 创',
    ('军防 20+ 年=壁垒谱', '**军防/KRITIS 最高守界**', '供位 28D 谱,24 口二轨切入', '军防链竞谱'),
    'Underhill 位(opt-in 律;**军防守界:24 口二轨窄针,不触军段**)', 'Dear Mr Underhill,'))

R.append(rec('A-306', 'Holker IT',
    'Holker IT Limited(英国 Burnley(Lancashire),Jubilee House, Phoenix Way;**2009 创(Colne)→2017 迁 Burnley;44-46 人;$13M;网安成长谱**;**Founder & Managing Director: Matthew Metcalfe(Crunchbase+burnley.co.uk 引语双源)**;梯队:Paul Taylor Technical Director+Steve McGrath Director of Sales Ops+**Przemyslaw Demski Product and Vendor Manager(产品/原厂经理=件链 KPI!)**+Gavin Roper Head of New Business',
    [('Matthew Metcalfe', 'Founder & Managing Director(CB+地方报引语双源)', 'crunchbase/burnley.co.uk 件', O, 'https://www.crunchbase.com/organization/holker-it'),
     ('Paul Taylor', 'Technical Director', 'rocketreach 谱面条', G, 'https://rocketreach.co/holker-it-management_b5e0010ef42e6fa7'),
     ('Przemyslaw Demski', 'Product and Vendor Manager(原厂件链 KPI)', 'rocketreach 谱面条', G, 'https://rocketreach.co/holker-it-management_b5e0010ef42e6fa7'),
     ('Steve McGrath', 'Director of Sales Operations', 'rocketreach 谱面条', G, 'https://rocketreach.co/holker-it-management_b5e0010ef42e6fa7')],
    [ev('决策链与对接人', 'Founder and Managing Director: Matthew Metcalfe(crunchbase;burnley.co.uk 2017 件引语「Our new premises are a perfect fit」);management: Steve McGrath(Sales Ops)+Przemyslaw Demski(Product&Vendor)+Paul Taylor(Technical)', 'https://www.crunchbase.com/organization/holker-it'),
     ev('联系方式与基础画像', 'Jubilee House, Phoenix Way, Burnley;+44 1282 859806;founded 2009;44 employees;$13M;cyber security/IT support;UK+EU+America 支持谱(rocketreach/burnley.co.uk 件)', 'https://burnley.co.uk/growing-cyber-security-firm-holker-relocate-burnley/')],
    '英兰开夏网安成长屋', '44-46 人;2009 创',
    ('创主 MD+原厂件链经理具名', '中小实体谱', 'Metcalfe+Demski 件链直达位', '区域链竞谱'),
    'Metcalfe+Demski 件链位(opt-in 律)', 'Dear Matthew,'))

R.append(rec('A-307', 'BlueBearsIT',
    'BLUEBEARSIT SAS(法国 Limonest(里昂北),13 Rue des Aulnes, 69760;**SIREN 840859524;2018-07-06 创;20-49 人;IT 咨询(6202A)**;**2024-03 换代窗:Président Mikaël Baduel 退→Eric Stève Charpentier(1982 生,前 DG)接任 Président(BODACC+verif/kompass 三源);实控受益人: Charpentier+Baduel+Sylvain Di Paola+1**',
    [('Eric Stève Charpentier', 'Président(2024-03-18 接任;BODACC O)', 'pappers.fr/BODACC 件', O, 'https://www.pappers.fr/entreprise/bluebearsit-840859524'),
     ('Mikaël Baduel', '前 Président/实控受益人(换代谱注)', 'pappers.fr 实控件', O, 'https://www.pappers.fr/entreprise/bluebearsit-840859524'),
     ('Nadjib Charef', 'Partner/Service Delivery Manager', 'rocketreach 谱面条', G, 'https://rocketreach.co/bluebearsit-management_b41a1a34ff6018bd')],
    [ev('决策链与对接人', 'BODACC 2024-03-18: Baduel démissionné de Président;Eric CHARPENTIER nommé Président;bénéficiaires effectifs: Eric CHARPENTIER, Mikaël BADUEL, Sylvain DI PAOLA et 1 autre(pappers/BODACC 件)', 'https://www.pappers.fr/entreprise/bluebearsit-840859524'),
     ev('联系方式与基础画像', 'SIREN 840 859 524;13 Rue des Aulnes, 69760 Limonest;création 06/07/2018;SAS capital €11-20k;20-49 salariés(2023);conseil en systèmes et logiciels informatiques(pappers/manageo 件)', 'https://www.manageo.fr/entreprises/840859524.html')],
    '法国里昂 2018 创 IT 咨询谱(2024 换代窗)', '20-49 人;2018 创',
    ('换代窗+BODACC O 级谱', '咨询铺谱', 'Charpentier 直达位', '区域链竞谱'),
    'Eric Charpentier 直达(opt-in 律)', 'Monsieur Charpentier,'))

R.append(rec('A-308', 'ITNI',
    'ITNI SAS(法国 Saint-Denis,103-105 Rue Charles Michels, 93200;**SIREN 505346312;2008-07-18 创 18 年;SAS cap €700k;100-199 人;CA €113.3M(2020)=法电信电子件批发大户(4652Z)**;**Président: Jean Marie Tawil(1962 生,2015-11-06 起;verif/corporama/lejournaldesentreprises 三源 O)**;5 支局(Ambares-et-Lagrave/Les Ulis 等);LEI 谱;entreprise familiale 注;Importateur+Exportateur important 谱',
    [('Jean Marie Tawil', 'Président(2015-11 起;三源一致)', 'verif.com/corporama 双件', O, 'https://corporama.com/fr/societe/itni/505346312')],
    [ev('决策链与对接人', 'Dirigeant: Jean Marie TAWIL(Président;né 1962;depuis 06/11/2015)(corporama/e-pro/verif 件)', 'https://corporama.com/fr/societe/itni/505346312'),
     ev('联系方式与基础画像', 'SIREN 505 346 312;103 Rue Charles Michels, 93200 Saint-Denis;SAS 2008;capital €700.000;100-199 salariés;CA €113.278.828(2020);4652Z 电信电子批发;5 établissements;Importateur/Exportateur important(corporama/lejournaldesentreprises 件)', 'https://www.lejournaldesentreprises.com/entreprise/itni')],
    '法国圣但尼 €113M 电信件批发大户', '100-199 人;2008 创',
    ('€113M 进出口大户=件链窗', '批发大户谱', 'Tawil 直达位', '一线链竞谱'),
    'Jean-Marie Tawil 直达(opt-in 律)', 'Monsieur Tawil,'))

R.append(rec('A-309', 'General Computer Italia S.p.A',
    'GENERAL COMPUTER ITALIA S.p.A (GCI)(意大利 Pavia(总部)+Roma 分社;**1993 创 33 年;€36M+(2018);Unix 硬件 Post-Warranty 维护起家→全硬件/DC 维护+增值分销+翻新件谱**;**Barbieri 兄弟:Roberto=Presidente, Maurizio=Amministratore Delegato(2019 impresacity 专访 O)**;**GCI System Integrator(2017 BU, Cisco/HPE/Fortinet;AD Patrizio Labella)→TXT e-solutions 收购谱(集团变动注)**;Irene Dimanuele 行政+Davide Bozzelli IT Manager 具名谱(gci.it 新闻页)',
    [('Roberto Barbieri', 'Presidente(创始兄弟长)', 'impresacity.it 专访件(O)', O, 'https://www.impresacity.it/news/22226/gci-rinnovarsi-nella-continuita.html'),
     ('Maurizio Barbieri', 'Amministratore Delegato(创始兄弟次;gaia 新闻件引语 O)', 'impresacity/gaia3.gci.it 件', O, 'https://gaia3.gci.it/gaia/eng/newsbox.html?id_p=221'),
     ('Patrizio Labella', 'AD,GCI System Integrator(TXT 收购谱注)', 'forbes.it/impresacity 件', O, 'https://forbes.it/eccellenza/gci-system-integrator/')],
    [ev('决策链与对接人', '「società nasce nel 1994 a Pavia, per opera dei due fratelli Roberto e Maurizio Barbieri…rispettivamente Presidente l\'uno e Amministratore Delegato l\'altro」;GCI System Integrator: Patrizio Labella AD(GCG cede GCI SI a TXT e-solutions 谱)(impresacity/forbes/gci.it 件)', 'https://www.impresacity.it/news/22226/gci-rinnovarsi-nella-continuita.html'),
     ev('联系方式与基础画像', 'GCI General Computer Italia SpA;Pavia+Roma;founded 1993;€36M(2018);maintenance post-warranty Unix→system integration;SIA 成员;refurbished HW 谱(gci.it 历史页/impresacity 件)', 'https://www.gci.it/la-nostra-storia/')],
    '意帕维亚 33 年维护+分销谱大户', '中型谱;1993 创',
    ('兄弟双驾 33 年+TXT 变动窗', '集团变动谱', 'Barbieri 双直达位', '一线链竞谱'),
    'Maurizio Barbieri AD 位(opt-in 律)', 'Gentile Sig. Barbieri,'))

R.append(rec('A-310', 'IT-TRUST Network Solution',
    'IT-TRUST Network Solution(奥地利 Großrußbach(Weinsteig);档锚 ittrust.at;谱面检索全打同名异体(南非 Midrand IT Trust/瑞士 iTrust AG/TÜV TRUST IT)→**守档准由:同名群噪,谱面无实名,档锚留档待专批 ittrust.at Whois/站点页**)',
    [],
    [ev('决策链与对接人', '公开谱面检索未锁具名决策人=守档准由;命中均为异体(Midrand/Zürich/TÜV Austria)已分层(2026-10-08 R66 21 波留痕)', 'http://www.ittrust.at'),
     ev('联系方式与基础画像', '档录: 奥地利 Weinsteig/Großrußbach;类型: 集成商/代理(Allied Telesis 谱);ittrust.at(档案基础画像行)', '仓内 profile/A/A-310-*(档谱基础画像行)')],
    '奥下奥州 Allied 谱小铺(同名群噪)', '守档案',
    ('—', '同名噪谱', '无守档', '—'),
    '守档:锚在名缺(待专批 ittrust.at 深查)', 'Sehr geehrte Damen und Herren,'))

R.append(rec('A-312', 'Atlantik Elektronik',
    'ATLANTIK ELEKTRONIK GmbH(德国 Planegg(慕尼黑),Fraunhoferstr. 11a, 82152;**HRB49191 AG München;DE129290761;1977 创 49 年;40 人;€10-50M;ATXX-Gruppe**;**CEOs(印谱):Ottmar Flach+Christian Flach(CFO)(atestore.de Impressum O 金谱!)**;**Lantronix EMEA Distributor Partner of the Year 2021+2022 蝉联(官网新闻件引语 O)=20 年 Lantronix 专谱**;Robert Bahler(印谱联络)',
    [('Ottmar Flach', 'Geschäftsführer(印谱自署+Lantronix 奖件引语)', 'atestore.de Impressum(O)', O, 'https://www.atestore.de/en/info/imprint.html'),
     ('Christian Flach', 'Geschäftsführer/CFO(印谱自署;Flach 族双驾)', 'atestore.de Impressum(O)', O, 'https://www.atestore.de/en/info/imprint.html')],
    [ev('决策链与对接人', 'Impressum: CEOs **Ottmar Flach, Christian Flach (CFO)**(atestore.de);「Über diese Auszeichnung freute sich Ottmar Flach, Geschäftsführer der Atlantik Elektronik GmbH」(Lantronix EMEA Partner of the Year 2021 官网件)', 'https://www.atestore.de/en/info/imprint.html'),
     ev('联系方式与基础画像', 'HRB49191 Amtsgericht München;Fraunhoferstr. 11a, 82152 Planegg;+49 89 89505-0;gegründet 1977;40 Mitarbeiter;€10-50 Mio;Eigentümer ATXX-Gruppe(wer-zu-wem/官网件)', 'https://www.wer-zu-wem.de/firma/atlantik-elektronik.html'),
     ev('近期动态与线索', 'Lantronix SmartEdge EMEA Distributor Partner of the Year 2021+2022 卫冕;20 年 Lantronix 谱(atlantikelektronik.com 新闻件)', 'https://www.atlantikelektronik.com/de/news/lantronix-smartedge-partner-program-award')],
    '德慕尼黑 49 年 Lantronix 专谱分销屋', '40 人;1977 创',
    ('印谱双 GF+连任原厂奖=金谱', '分销谱', 'Flach 双直达位', 'Lantronix 自家链谱'),
    'Flach 双 GF 位(opt-in 律)', 'Guten Tag Herr Flach,'))

R.append(rec('A-313', 'Powertech Controls',
    'Powertech Controls Co. Inc(美国 Ronkonkoma, NY 11779,101 Christopher St;**1991 创 35 年;58-51 人;$24.6M(2020);**Supply Chain Connect 2021 电子分销 Top 50 第 45 位**;工业自动化控制元件全球分销**;**President & CEO: Annemarie Leigh-Austin(榜单件+zoominfo 双源)**;**Hirschmann(Belden 工业以太)授权+Idec 授权=工业谱**;Norman Davieau VP Sales;Jordan Leventhal Sales Mgr Distributor',
    [('Annemarie Leigh-Austin', 'President & CEO(Top 50 榜单件+zoominfo)', 'supplychainconnect.com 榜单件', O, 'https://www.supplychainconnect.com/home/article/21162803/top-50-electronics-distributors-2021-45-powertech-controls-co-inc'),
     ('Norman Davieau', 'VP, Sales(销售口)', 'zoominfo 谱面条', G, 'https://www.zoominfo.com/c/powertech-controls-co-inc/85361181')],
    [ev('决策链与对接人', 'Top 50 Electronics Distributors 2021 #45: President/CEO **Annemarie Leigh-Austin**;zoominfo org: Annemarie Austin President & CEO + Norman Davieau VP Sales + Jordan Leventhal Sales Manager Distributor', 'https://www.supplychainconnect.com/home/article/21162803/top-50-electronics-distributors-2021-45-powertech-controls-co-inc'),
     ev('联系方式与基础画像', '101 Christopher St., Ronkonkoma, NY 11779;800-938-6678;info@powertechcontrols.com;Founded 1991;58 employees;$24.6M(2020);**Authorized Hirschmann Distributor(Belden 工业以太谱)+Authorized Idec**(榜单/官网件)', 'https://www.powertechcontrols.com/hirschmann')],
    '美长岛 35 年工业控制元件分销(Top 50)', '51-58 人;1991 创',
    ('Top 50 榜单+Hirschmann 谱', '分销谱', 'Austin CEO+VP Sales 直达位', '一线链竞谱'),
    'Austin+VP Sales 位(opt-in 律)', 'Dear Ms Leigh-Austin,'))

R.append(rec('A-316', 'Davis Ulmer Family of Companies',
    'Davis-Ulmer Sprinkler Co Inc(美国 Buffalo, NY 14228,1 Commerce Dr;**1946 创 80 年;265 人;$96.3M;消防喷淋全服务商(喷洒/报警/检测)+Allied 谱 IT 支线**;**三代家族谱+APi Group 2005 收购=集团谱**;**R Steven Ulmer: President(buzzfile;Equilar 史:1972 入司学徒→1988 President→2020 回 APi 安全服务 SVP=已交班注)**;zoominfo 列 Michael Shibrowski President+Wayne Gray+Domenick Serrano Branch Presidents(代际差旗注)',
    [('R Steven Ulmer', 'President(buzzfile;三代家族;Equilar: 已交班 APi SVP 差旗注)', 'buzzfile/equilar 双源', G, 'https://www.buzzfile.com/business/Davis~Ulmer-Sprinkler-Co-Inc-716-691-3200'),
     ('Michael Shibrowski', 'President(zoominfo 新谱;代际对位)', 'zoominfo 件', G, 'https://www.zoominfo.com/pic/davis-ulmer-sprinkler-co/32738779')],
    [ev('决策链与对接人', 'R Steven Ulmer is the President at Davis-Ulmer Sprinkler Co(buzzfile);Equilar 史: Steve joined 1972, president 1988, third-generation family business, **APi Group company since 2005**, 2020 returned as APi SVP safety services;zoominfo: Michael Shibrowski President(差旗注)', 'https://www.buzzfile.com/business/Davis~Ulmer-Sprinkler-Co-Inc-716-691-3200'),
     ev('联系方式与基础画像', '1 Commerce Dr, Buffalo NY 14228;(716) 691-3200;founded 1946;265 employees;$96.3M revenue est;fire sprinkler/suppression/alarm 全服务;Buffalo HQ+Rochester(East Syracuse 档案锚双址谱)(buzzfile/leadiq 件)', 'https://leadiq.com/c/davis-ulmer-sprinkler-co/5a1d9743230000540085cf01')],
    '美纽约州 80 年消防全服集团(APi 系)', '265 人;$96M',
    ('80 年三代谱+APi 集团靠', '消防主业谱(IT 支线窄)', 'President 位+Alarm&Detection VP 口(待核差旗)', '集团审批链'),
    'President 位(opt-in 律;集团集采谱;差旗待核)', 'Dear Sir or Madam,'))

R.append(rec('A-317', 'Shea Electric',
    'Shea Electric & Communications, LLC(美国 Oshkosh, WI 54904,1922 S Washburn St;**2006 创 20 年;11-16 人;工商业电气承包+低压布线/安防/生命安防**;**Patty(Patricia P)Shea Owner(insightonbusiness 专访+D&B Key Principal 双源)+Dan Shea COO(专访引语)**;社区 $1.25M 捐赠/20 周年谱;Allied 谱低电压件链',
    [('Patty (Patricia P) Shea', 'Owner(专访+D&B Key Principal 双源)', 'insightonbusiness/D&B 件', O, 'https://insightonbusiness.com/shea-electric-communications-llc/'),
     ('Dan Shea', 'COO(专访具名;Shea 族谱)', 'insightonbusiness 专访件(O)', O, 'https://insightonbusiness.com/shea-electric-communications-llc/')],
    [ev('决策链与对接人', '「Founded in 2006…**Patty Shea, Owner**…**Dan Shea, COO**, understood that philanthropy…」;D&B Key Principal: Patricia P Shea(insightonbusiness 专访/D&B 件)', 'https://insightonbusiness.com/shea-electric-communications-llc/'),
     ev('联系方式与基础画像', '1922 S Washburn St, Oshkosh WI 54904;founded 2006;11-16 employees;industrial/commercial electrical+low voltage wiring+security+life safety;20 周年/$1.25M+ 社区捐赠谱(datanyze/insightonbusiness 件)', 'https://www.datanyze.com/companies/shea-electric-communications/348635113')],
    '美威斯康星 20 年电气承包家族铺', '11-16 人;2006 创',
    ('Owner+COO 双具名=直达', '小微铺谱', 'Patty/Dan 直达位', '区域链竞谱'),
    'Patty Shea+Dan Shea 位(opt-in 律)', 'Dear Ms Shea,'))

R.append(rec('A-318', 'DeInta',
    'DeInta(Grupo;Deinta Seguridad S.L.,西班牙 Zaragoza;**CIF B99060089;2001 创(集团)/2005 Seguridad 体;11 人(2024);安防+视听+电气安装;自研 ALMAND 安防集成平台(停车/独栋/企业园区/水文谱)**;**换代+重整双金谱:创始人 Jesús Pola Villarroya(2021 退居股东;concurso 债权人协议 74%/70% 通过出清公告 O)→子 Jorge Pola 任 Director General(2024 萨拉戈萨商会专访父子同席 O)**;2024-04 单一管理人体制(einforma)',
    [('Jorge Pola', 'Director General(子;2024 商会专访 O)', 'redaccion.camarazaragoza.com 专访件', O, 'https://redaccion.camarazaragoza.com/deinta-nuevo-socio-de-club-de-camara/'),
     ('Jesús Pola Villarroya', '创始人/前 Gerente(2021 退居股东;重整公告自署)', 'LI 自署+专访件', O, 'https://www.linkedin.com/in/jes%C3%BAs-pola-villarroya-9b241a32/')],
    [ev('决策链与对接人', '「**Jorge Pola, director general**, junto a su padre y fundador, **Jesús Pola**…matriz data de 2001」(Cámara Zaragoza 2024 件);Jesús 自署: convenios aprobados 74%/70%;jubilación como máximo directivo, sigue como accionista', 'https://redaccion.camarazaragoza.com/deinta-nuevo-socio-de-club-de-camara/'),
     ev('联系方式与基础画像', 'Deinta Seguridad SL;CIF B99060089;Zaragoza;fundada 2001(grupo);11 empleados(2024);ALMAND 自研平台;clientes: Banco de España/Parques Reunidos/AEAT 等公共谱=守界注(einforma/LI 件)', 'https://www.einforma.com/informacion-empresa/deinta-seguridad')],
    '西班牙萨拉戈萨 25 年安防视听屋(重整出清+换代)', '11 人;2001 创',
    ('重整出清+父子换代=双窗', '公客户谱守界注', 'Jorge Pola 直达位', '区域链竞谱'),
    'Jorge Pola 直达(opt-in 律;公段客户守界)', 'Estimado Sr. Pola,'))

R.append(rec('A-319', 'Nexus Technology',
    'NEXUS TECHNOLOGY S.A.C(**秘鲁 Lima(Miraflores),Ricardo Palma 693;RUC 20267178331;1995-05-11 创 31 年;增值分销大户(VAD)**;**roster 档标西班牙=国别差旗更正:官网/登记全为秘鲁利马**;**GERENTE GENERAL: Guillermo Alberto Nuñez Danjoy(1996-05-18 起 30 年;PAD Univ. Piura;gnunez@nexus.com.pe)**;**Carlos Miguel González Uria 创始 Socio(1995)/Administration Director**;NetScout/Ruijie 分约引语件;Ernesto Noriega gerente de línea networking(件链口,enoriega@nexus.com.pe)',
    [('Guillermo Alberto Nuñez Danjoy', 'Gerente General(1996 起 30 年;登记+LI+引语件三源)', 'datosperu 登记件+LI 自署', O, 'https://www.datosperu.org/empresa-nexus-technology-sac-20267178331.php'),
     ('Carlos Miguel González Uria', '创始 Socio/Administration Director(1995 起)', 'datosperu/D&B 件', O, 'https://www.dnb.com/business-directory/company-profiles.nexus_technology_sac.a29a290595a35170b1827ad07d96ca84.html'),
     ('Ernesto Noriega', 'Gerente de línea networking(网络品线总=件链 KPI)', 'playmarketing 专访件', O, 'https://playmarketing.net/nexus-enriquece-su-portafolio-con-ruijie/')],
    [ev('决策链与对接人', 'GERENTE GENERAL: NUÑEZ DANJOY GUILLERMO ALBERTO(desde 18/05/1996);SOCIO: GONZALEZ URIA CARLOS MIGUEL(02/06/1995)(datosperu 登记件);「Guillermo Nuñez gerente general de Nexus Technology」(NetScout 2016/Ruijie 2022 件引语)', 'https://www.datosperu.org/empresa-nexus-technology-sac-20267178331.php'),
     ev('联系方式与基础画像', 'RUC 20267178331;Av. Ricardo Palma 693, Lima(Miraflores);inicio 11/05/1995;Sociedad Anónima Cerrada;estado ACTIVO;**roster 档标西班牙=国别差旗,更正为秘鲁利马主谱(datosperu/dnb 件)**', 'https://www.dnb.com/business-directory/company-profiles.nexus_technology_sac.a29a290595a35170b1827ad07d96ca84.html'),
     ev('近期动态与线索', 'NetScout 全国代理(2016)+Ruijie Networks 组合强化(2022);enoriega@nexus.com.pe networking 品线直邮(americasistemas/playmarketing 件)', 'https://playmarketing.net/nexus-enriquece-su-portafolio-con-ruijie/')],
    '秘鲁利马 31 年 VAD 分销大户', '中型谱;1995 创',
    ('31 年 GM 稳谱+品线总直邮', '国别差旗已更正', 'Nuñez+Noriega 品线直达位', '一线链竞谱'),
    'Nuñez+Noriega 网络品线位(opt-in 律)', 'Estimado Sr. Núñez,',
    trend='2026-10-08 R66 21 波谱名牌(国别差旗更正:秘鲁)'))

R.append(rec('A-320', 'Evelem',
    'EVELEM SAS(法国 Meudon(上塞纳),8 Rue de la Pépinière, 92360;**SIREN 900722067;2021-06-22 创;1-2 人;网络/电信集成咨询**;**Président: Amir Hachefi(1980 生)+Directeur Général: Jean-Pierre Batrikian(1980 生)(pappers/BODACC 双创双驾 O)**;**排噪:EVOLEM family office(Bruno Rousset/APRIL)=一字母异体已分层**',
    [('Amir Hachefi', 'Président(2021 创始;BODACC O)', 'pappers.fr/infonet 件', O, 'https://www.pappers.fr/entreprise/evelem-900722067'),
     ('Jean-Pierre Batrikian', 'Directeur Général(创始双驾)', 'pappers.fr 件', O, 'https://www.pappers.fr/entreprise/evelem-900722067')],
    [ev('决策链与对接人', 'Président: HACHEFI Amir;Directeur général: BATRIKIAN Jean-Pierre(depuis 23/06/2021)(pappers/BODACC 创立公告)', 'https://www.pappers.fr/entreprise/evelem-900722067'),
     ev('联系方式与基础画像', 'SIREN 900 722 067;8 Rue de la Pépinière, 92360 Meudon;SAS capital €1.000;1-2 salariés;conseil/intégration réseaux informatiques et télécoms;contact@evelem.fr;**EVOLEM(family office)异体已分层**(pappers/infonet/evolem 件)', 'https://infonet.fr/entreprises/90072206700015-evelem/')],
    '法国上塞纳 2021 创网络集成微铺', '1-2 人;2021 创',
    ('双创双驾=直达', '微实体谱', 'Hachefi/Batrikian 直达位', '区域链竞谱'),
    'Hachefi+Batrikian 直达(opt-in 律)', 'Messieurs,'))

R.append(rec('A-321', 'EDV-Partner',
    'EDV-Partner GmbH(档锚 edvpartner.de→**Hamburg 主体:1995 创;11-50 人;自有 Rechenzentrum;「IT-Lösungen mit System」**;**GF Nikolai Hommola(LI 公司页员工谱)+Sven Meyer(LI 谱)**;**多异体分层注:EDV-Partner GmbH Leonberg(1983 Bernd Peter 创→2021 子 Tobias Peter 70% 接棒=换代谱;HRB251349;域名 edv-partner.de 带横杠)/theorg 示 Oberhausen(Sven Meyer GF)=按档锚域名 edvpartner.de 对位 Hamburg**',
    [('Nikolai Hommola', 'Geschäftsführer(LI 公司页员工谱;Hamburg 主体)', 'linkedin.com/company/edv-partner-hamburg', G, 'https://de.linkedin.com/company/edv-partner-hamburg'),
     ('Tobias Peter', 'GF(Leonberg 异体;2021 接棒 70%=分层副注)', 'viaductus 登记件(异体副注)', O, 'https://www.viaductus.de/firma/DE-B2609-HRB-251349-edv-partner-gmbh-systemhaus-fuer-it-infrastruktur-und-it-sec-leonberg')],
    [ev('决策链与对接人', 'LI 公司页(edv-partner-hamburg): Nikolai Hommola Geschäftsführer bei EDV-Partner GmbH+Sven Meyer+Florian Gebauer+Bernhard Graßhoff;**分层: Leonberg 体 GF Bernd Michael Peter+Tobias Peter(2021 换代;Anteile 70/30)+Sven Geipel Prokurist**', 'https://de.linkedin.com/company/edv-partner-hamburg'),
     ev('联系方式与基础画像', '档锚 www.edvpartner.de;Hamburg;gegründet 1995;11-50 Beschäftigte;eigenes Rechenzentrum;Systemhaus+Ingenieurgesellschaft(LI 件);Leonberg 异体: Dieselstraße 1, 71229 Leonberg, HRB251349(viaductus 件)', 'https://de.linkedin.com/company/edv-partner-hamburg')],
    '德汉堡 1995 创系统屋(自有 DC)', '11-50 人;1995 创',
    ('自有 DC=件链谱', '多异体噪已分层', 'Hommola GF 位(G 谱)', '区域链竞谱'),
    'GF 位(opt-in 律;异体已分层)', 'Sehr geehrte Damen und Herren,'))

R.append(rec('A-322', 'AlphaCron Datensysteme',
    'AlphaCron Datensysteme(德国 Apfelstädt(图林根),Wandersleber Straße 1a, 99192;**IT-Systemhaus+自建 Rechenzentrum,全国服务;AlphaFax.net 产品谱**;**Inhaber: Marc Pauls(官网 Impressum O!);Uwe Pauls(RIPE 谱)**;**自营 AS28748 ALPHACRON-AS+滥用箱 abuse@alphacron.de=ISP 级自营网谱!Funknetz 无线网价单 PDF 谱=乡区无线工程**',
    [('Marc Pauls', 'Inhaber(业主;官网 Impressum+RIPE 双源)', 'alphacron.de Impressum(O)', O, 'https://www.alphacron.de/'),
     ('Uwe Pauls', '联络具名(RIPE 谱;Pauls 族谱)', 'ipshu AS28748 件', G, 'https://de.ipshu.com/asn/28748')],
    [ev('决策链与对接人', 'Impressum/Kontakt: AlphaCron Datensysteme **Inh. Marc Pauls**, Wandersleber Straße 1a, 99192 Apfelstädt(官网自署);RIPE AS28748: Marc Pauls(AlphaCron Datensysteme)+Uwe Pauls', 'https://www.alphacron.de/'),
     ev('联系方式与基础画像', 'Tel. 036202/759994;contact@alphacron.de;**AS28748 ALPHACRON-AS 自营自治域**;Funknetz-Dokumente(preisliste-funknetz.pdf)=无线网工程谱;IT-Systemhaus mit angeschlossenem Rechenzentrum(官网/ipshu 件)', 'https://de.ipshu.com/asn/28748')],
    '德图林根系统屋+自营 AS 乡区无线谱', '小铺谱;自营 ISP 级网',
    ('自营 AS+Funknetz=工程强契', '小实体谱', 'M. Pauls 直达位', '区域链竞谱'),
    'Marc Pauls 直达(opt-in 律)', 'Guten Tag Herr Pauls,'))

R.append(rec('A-323', 'EDV-Beratung u Dienstleistungen Berg-Duda',
    'EDV Beratung & Dienstleistungen Berg-Duda(德国 Bergneustadt(北威),Am Leiweg 11, 51702;**2000-01-01 创 26 年;KMU 全包(硬软件销售/安装/组网/安全/培训)**;**Gründer & Geschäftsführer: Sebastian Berg-Duda(官网+Impressum O;20+ 年经验自署;DE205474676)**',
    [('Sebastian Berg-Duda', 'Gründer & Geschäftsführer(官网引语+Impressum 双源)', 'berg-duda.de 官网(O)', O, 'https://berg-duda.de/')],
    [ev('决策链与对接人', '「Wir finden einen Weg, Ihre individuellen Anforderungen professionell umzusetzen.» **Sebastian Berg-Duda (Gründer & Geschäftsführer)**」;Impressum: Geschäftsführer Sebastian Berg-Duda(berg-duda.de)', 'https://berg-duda.de/'),
     ev('联系方式与基础画像', 'Am Leiweg 11, 51702 Bergneustadt;+49 2261/478849;info@berg-duda.de;gegründet 01.01.2000;USt-Id DE205474676;硬软件+组网+安全+培训(官网/über uns 页)', 'https://berg-duda.de/ueber-uns')],
    '德北威 26 年 KMU 全包单铺', '单铺谱;2000 创',
    ('创主 GF 单铺=直达', '小微谱', 'Berg-Duda 唯一直达位', '区域链竞谱'),
    'Sebastian Berg-Duda 直达(opt-in 律)', 'Guten Tag Herr Berg-Duda,'))

R.append(rec('A-324', 'H&M electronics GbR',
    'H&M electronics GbR(德国 Dillingen an der Donau(巴伐利亚),Am Stadtberg 19 / Vorstadtstr. 6, 89407;**30+ 年;通信/安防/IT(程控至 600 门/警报/火警)**;**双个人责任合伙人:Herbert Kuchenbaur(Dipl. Ing (FH))+Marcus Dick(AGB 页 O+Creditreform 双源;USt 127780918)**;联络 thomas.hoffmann@hm-electronics.de 具名',
    [('Herbert Kuchenbaur', 'Gesellschafter(个人责任合伙人;AGB 自署)', 'hm-electronics.de AGB 页(O)', O, 'https://www.hm-electronics.de/agb/index.html'),
     ('Marcus Dick', 'Gesellschafter(双合伙人)', 'hm-electronics.de AGB 页(O)', O, 'https://www.hm-electronics.de/agb/index.html')],
    [ev('决策链与对接人', 'Anbieterkennzeichnung: H&M electronics GbR **Herbert Kuchenbaur Dipl. Ing (FH) & Marcus Dick**(AGB 页自署);Creditreform: 2 x persönlich haftender Gesellschafter', 'https://www.hm-electronics.de/agb/index.html'),
     ev('联系方式与基础画像', 'Am Stadtberg 19, 89407 Dillingen;09071/7925-0;info@hm-electronics.de;seit mehr als 30 Jahren;Kommunikationstechnik/Sicherheitstechnik/IT;Telefonanlagen bis 600 Nebenstellen(elektriker.org/Creditreform 件)', 'https://firmeneintrag.creditreform.de/89407/8030038997/HERBERT_KUCHENBAUR_MARCUS_DICK_H_M_ELECTRONICS_GBR')],
    '德巴伐利亚 30+ 年通信安防双合伙铺', '小铺谱',
    ('双合伙人 AGB 自署=O 直达', '小实体谱', 'Kuchenbaur/Dick 直达位', '区域链竞谱'),
    'Herbert Kuchenbaur 直达(opt-in 律)', 'Guten Tag Herr Kuchenbaur,'))

R.append(rec('A-325', 'Ingo Seidenberg Inseid – EDV-Beratung',
    'Ingo Seidenberg「INSEID-EDV-Beratung」(德国 Burgwedel(下萨克森),Schulze-Delitzsch-Straße 11, 30938;**业主自名单铺(IT 咨询/电脑贸易)**;+49 5139 985230;inseid.de;Creditreform/目录件对位',
    [('Ingo Seidenberg', 'Inhaber(业主自名;目录件)', 'lieber-lokal.de/11880 目录件', G, 'https://www.lieber-lokal.de/merchant/8KSMFU')],
    [ev('决策链与对接人', 'Ingo Seidenberg Inseid - EDV-Beratung;Schulze-Delitzsch-Straße 11, 30938 Burgwedel;+49 5139 985230;inseid.de(lieber-lokal/11880/firmenwissen 目录件)', 'https://www.lieber-lokal.de/merchant/8KSMFU'),
     ev('联系方式与基础画像', 'Burgwedel(Großburgwedel);Computerhändler/EDV-Beratung 单铺;Creditreform「Ingo Seidenberg INSEID-EDV-Beratung」对位(firmenwissen 件)', 'https://www.firmenwissen.de/az/firmeneintrag/30938/2190332903/DIPL_ING_FH_THOMAS_BERTRAM_IT_SERVICE_UND_BERATUNG.html')],
    '德下萨克森业主单铺', '单铺谱',
    ('业主自名=直达', '微实体谱', 'Seidenberg 唯一直达位', '区域链竞谱'),
    'Ingo Seidenberg 直达(opt-in 律)', 'Guten Tag Herr Seidenberg,',
    trend='2026-10-08 R66 21 波谱名牌(目录件级)'))

R.append(rec('A-326', 'Merlin EDV',
    'Merlin(=**Merlin Kommunikationstechnik e.K.**,德国 Erlangen(巴伐利亚);**IT 咨询/硬件工作坊/存储谱**;**Founder & Managing Director: Matthias Behle(Crunchbase 谱同址同名同域)**;**多异体分层注:Merlin EDV-Großhandel Geschäftsführungsges.mbH(Dillingen/Saar,HRB25876,GF Petra Junker 2018-10 起)/Merlin Solutions(Jochen Kobusch)/Merlin Beteiligungs(Kramarsch+Sebald)=各已分层**',
    [('Matthias Behle', 'Founder & Managing Director(Erlangen 主谱)', 'crunchbase 件', G, 'https://www.crunchbase.com/organization/merlin-0c8f')],
    [ev('决策链与对接人', 'Merlin Kommunikationstechnik e.K.: Matthias Behle Founder and Managing Director;Erlangen, Bayern;11-50(crunchbase 件,sameAs: merlinedv.de)', 'https://www.crunchbase.com/organization/merlin-0c8f'),
     ev('联系方式与基础画像', '档锚 www.merlinedv.de(Erlangen);IT consulting/hardware workshops/data storage;**异体分层: Merlin EDV-Großhandel Dillingen/Saar(HRB25876;GF Petra Junker seit 11.10.2018)**(webvalid/registercheck 件)', 'https://www.registercheck.de/companies/merlin-edv-grosshandel-geschaeftsfuehrungsgesellschaft-mbh')],
    '德埃朗根 IT 咨询谱铺', '11-50 人',
    ('Founder MD 谱面孔在', '多异体噪已分层', 'Behle 直达位(G 谱)', '区域链竞谱'),
    'Matthias Behle 直达(opt-in 律)', 'Guten Tag Herr Behle,'))

R.append(rec('A-327', 'CFI France',
    'CFI - Compagnie Française d\'Informatique(法国 Saint-Denis/Saint-Ouen-sur-Seine/Villeneuve-la-Garenne 多址;**SIREN 323540534;1981 创 45 年!;Société commerciale cap €1,098,000;4651 电脑设备批发**;**Président et directeur de la publication: Thierry Clabault(官网 mentions légales 自署=O 印谱)**;**多异体分层:CFI(France Médias Monde 公共机构)/CFI funds SAS=已分层**',
    [('Thierry Clabault', 'Président(官网法律声明页自署)', 'cfigroupe.com mentions légales(O)', O, 'https://cfigroupe.com/mentions-legales.html')],
    [ev('决策链与对接人', 'Mentions légales: Editeur et responsable de la publication — **Président et directeur de la publication : Thierry CLABAULT**, CFI - Compagnie Française Informatique(官网自署)', 'https://cfigroupe.com/mentions-legales.html'),
     ev('联系方式与基础画像', 'COMPAGNIE FRANCAISE D\'INFORMATIQUE;SIREN 323540534;créée 1981;capital €1.098.000;4651 commerce de gros ordinateurs;Saint-Denis/Villeneuve-la-Garenne 址;www.cfigroupe.com(verif 件);异体 CFI(MEAE/fonds)=已分层', 'https://www.verif.com/societe/COMPAGNIE-FRANCAISE-D-INFORMATIQUE-323540534/')],
    '法国圣但尼 45 年电脑批发谱', '中型谱;1981 创',
    ('45 年老牌+印谱直达', '批发谱', 'Clabault 直达位', '区域链竞谱'),
    'Thierry Clabault 直达(opt-in 律)', 'Monsieur Clabault,'))

R.append(rec('A-328', 'Delta Sertec',
    'DELTA SERTEC(法国 Marseille 13e(15 Rue Georges Charpak;Le Thor 分社 84250);**SIREN 950012989;1979-01-01 创 47 年!;20-49 人;CA €4.27M(2017);电气安装(所有楼宇)+Smart Building(布线/数显/IPTV/安防)+DELTA TELECOM 电信运营双牌**;**实控链:Président=DELTA SMART TECHNOLOGIES←DELTA SERTEC DEVELOPPEMENT(SARL)←Gérant Arnaud Brouquier(1982 生,2017-04 接任母 Geneviève Brouquier=二代换代谱;pappers/BODACC O)**;**Brouquier 兼 Directeur Commercial+Directeur des Achats(采购直兼=KPI!)+直邮 arnaud.brouquier@deltasertec.com(O)**;Carine Plassais Directeur Financier',
    [('Arnaud Brouquier', '实控 Gérant(终端)+Dir. Commercial+**Dir. des Achats(采购)**;直邮 O', 'pappers/luberonetsorguesentreprendre 双件', O, 'https://www.pappers.fr/entreprise/DELTA+SERTEC-950012989'),
     ('Carine Plassais', 'Directeur Financier(财务总监)', 'manageo 件', G, 'https://www.manageo.fr/entreprises/950012989.html')],
    [ev('决策链与对接人', 'Président: DELTA SMART TECHNOLOGIES(←DELTA SERTEC DEVELOPPEMENT appropriée par son gérant **Arnaud BROUQUIER**, remplacement Geneviève BROUQUIER 2017);fonctionnels: PLASSAIS Carine(Finance)+**BROUQUIER Arnaud(Achats/Commercial/RH)**(pappers/manageo/BODACC 件)', 'https://www.pappers.fr/entreprise/DELTA+SERTEC-950012989'),
     ev('联系方式与基础画像', 'DELTA SERTEC 950 012 989;Marseille 13e;créée 01/01/1979;20-49 salariés;CA €4.265.778(2017);travaux d\'installation électrique;**DELTA SERTEC/DELTA TELECOM 双牌;arnaud.brouquier@deltasertec.com 04 90 33 80 70**(manageo/luberonetsorguesentreprendre 件)', 'https://luberonetsorguesentreprendre.fr/Annuaires%20des%20entreprises/delta-sertec-delta-telecom/')],
    '法马赛 47 年电气安装+电信运营屋(二代谱)', '20-49 人;1979 创',
    ('实控兼采购直兼=件链直达 KPI', '中小谱', 'Brouquier 直邮直达位', '区域链竞谱'),
    'Arnaud Brouquier 直邮直达(opt-in 律)', 'Monsieur Brouquier,',
    trend='2026-10-08 R66 21 波谱名牌(二代换代+采购直兼)'))

# ============ 人名司名同体培训谱档×20 ============
def person(code, name, city, web, p1, why, extra, sal):
    kb = '**%s(MikroTik 认证培训师/顾问 本人谱位,档谱官网自署,%s)' % (name, O) + '**'
    if not web.startswith('http') and __import__('re').match(r'^[\w.-]+\.[a-zA-Z]{2,}$', web):
        web = 'https://' + web
    src = web if web.startswith('http') else '仓内 profile/A/%s-*(R54/R66 档谱基础画像行)' % code
    return rec(code, name,
        '%s(%s;**【人名司名同体=CSV 公司名即本人谱位,official-self-published 级金谱】**;类型: 集成商/顾问(MikroTik 认证);培训交付谱;档站 %s;%s)' % (name, city, web, extra),
        [(name, 'MikroTik 认证培训师/顾问(档谱:CSV 公司名字段即本人)', '档谱+档站自署', O, src)],
        [ev('联系方式与基础画像', '国家/城市: %s;网站: %s;类型: 集成商/顾问(MikroTik 认证)(档案基础画像行=事实)', src),
         ev('近期动态与线索', '档定首触角: %s' % p1, src),
         ev('目标行业与场景', '档定值得跟: %s' % why, src)],
        '培训交付谱(MTCSWE 谱链)', '单铺/工作室谱',
        ('MTCSWE/交换认证谱=对口窗', '单铺谱', '%s 本人直达位' % name, 'MikroTik 官方课链'),
        sal + '(opt-in 律)',
        sal)

R.append(person('A-283', 'Jake Louis Petre Woodhouse', '英国／Driffield', 'https://www.jellyfishbroadband.com',
    '园区 WiFi PoE 随单正口($180 锚点一致);顾问诚实角', '有明确交换/供电需求(交换专长 MTCSWE),且有具体人直联',
    'jellyfishbroadband.com=约克郡乡区无线宽带铺谱', 'Dear Jake,'))
R.append(person('A-284', 'Kevin Riding', '英国／Barton-upon-Humber', '—（无公开站点）',
    '**建档不出信(无站无邮箱);用户补邮箱→CONSULT-OEM 候选供位**', '有明确交换/供电需求(交换专长 MTCSWE),且有具体人直联',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Dear Kevin,'))
R.append(person('A-285', 'Corné Van Halteren', "荷兰／'s-Hertogenbosch", 'https://www.dael.com',
    '私营段随单窄位($180 锚点一致);**DJI 公共守界句**', '【人工定级】A——自动规则已跳过(档注)',
    'dael.com 档站谱;DJI 公共守界注', 'Geachte heer Van Halteren,'))
R.append(person('A-286', 'Aris Vink', '荷兰／Zoetermeer', 'https://www.sdc.nl',
    '二轨窄位($180 锚点一致);前句框定', '【人工定级】A——自动规则已跳过(档注)',
    'sdc.nl 档站谱', 'Geachte heer Vink,'))
R.append(person('A-287', 'Rene Dirks', '荷兰／Tilburg', 'gewoon-it.nl',
    '随身 value 窄位($180 锚点一致);诚实角', '【人工定级】A——自动规则已跳过(档注)',
    'gewoon-it.nl=蒂尔堡 IT 单铺谱', 'Geachte heer Dirks,'))
R.append(person('A-288', 'Krystof Klima', '捷克／Lety', 'https://www.wifiprofi.cz',
    '课程对照单元+作业队装备双角($180 锚点一致);尊敬入场;**p1=CONSULT-OEM 谱(无量产报价)**', '【人工定级】A——自动规则已跳过(档注)',
    'wifiprofi.cz=捷克 WiFi 专业谱', 'Vážený pane Klima,'))
R.append(person('A-289', 'Dan Parrish', '美国／Fenton, MO', '—（无公开站点）',
    '**建档不出信(无站无邮箱);用户补邮箱→CONSULT-OEM 候选供位**', '【人工定级】A——自动规则已跳过(档注)',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Dear Dan,'))
R.append(person('A-290', 'Chris Schiessl', '美国／Minot, ND', '—（无公开站点）',
    '**建档不出信(无站无邮箱);用户补邮箱→CONSULT-OEM 候选供位**', '【人工定级】A——自动规则已跳过(档注)',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Dear Chris,'))
R.append(person('A-291', 'Martin Sundahl', '美国／New Port Richey, FL(档谱);**roster 国家更正注:美→丹麦**', 'https://adeodc.com',
    '机柜/现场件窄位($180 锚点一致);**roster 国家更正注(美→丹麦)**', '【人工定级】A——自动规则已跳过(档注)',
    'adeodc.com 档站谱;国别差旗更正注(美→丹麦)', 'Dear Martin,'))
R.append(person('A-292', 'David Garland', '美国／Panora, IA', 'https://panorafiber.com',
    '局端/商用现场窄位低密针($180 锚点一致);**billing@ 唯一箱宽注**', '【人工定级】A——自动规则已跳过(档注)',
    'panorafiber.com=爱荷华乡区光纤铺谱(Panora Fiber/局端件链)', 'Dear David,'))
R.append(person('A-293', 'Hector Prado', '美国／La Habra, CA', '—（无公开站点）',
    '**建档不出信(无站无邮箱);用户补邮箱→CONSULT-OEM 候选供位**', '【人工定级】A——自动规则已跳过(档注)',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Dear Hector,'))
R.append(person('A-294', 'Steve Discher', '美国／TX(College Station)', 'https://www.ispsupplies.com',
    '非 BABA 品类二轨窄口($180 锚点一致);**BABA 守界句必压**', '【人工定级】A——自动规则已跳过(档注)',
    '**ISP Supplies 谱(College Station,TX;LinkedIn 公司页 Founder- ISP Supplies 具名谱顺带 O 级旁证;Ubiquiti/MikroTik/RF elements 牌谱)**;**BABA 守界句必压**', 'Dear Steve,'))
R.append(person('A-295', 'Matthew Phillip Main', '英国／Portsmouth', '—（无公开站点）',
    '**建档不出信(无站无邮箱);用户补邮箱→CONSULT-OEM 候选供位**', '【人工定级】A——自动规则已跳过(档注)',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Dear Matthew,'))
R.append(person('A-296', 'Frederic Gauthier', '加拿大／Quebec', '—（无公开站点）',
    '**建档不出信(无站无邮箱);用户补邮箱→CONSULT-OEM 候选供位**', '【人工定级】A——自动规则已跳过(档注)',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Bonjour Monsieur Gauthier,'))
R.append(person('A-297', 'Johannes Edgren', '芬兰／Porvoo', '—（无公开站点）',
    '**建档不出信(无站无邮箱);用户补邮箱→CONSULT-OEM 候选供位**', '【人工定级】A——自动规则已跳过(档注)',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Dear Mr. Edgren,'))
R.append(person('A-298', 'Luca Martinelli', '意大利／Modena', '—（无公开站点）',
    '**建档不出信(无站无邮箱);用户补邮箱→CONSULT-OEM 候选供位**', '【人工定级】A——自动规则已跳过(档注)',
    '个体顾问无官网档;建档供位待用户补邮箱', 'Gentile Sig. Martinelli,'))
R.append(person('A-299', 'Antal Bacskai', '匈牙利／Budapest', 'http://sn-solution.hu',
    '运维换代随单窄位($180 锚点一致);存量诚实角', '【人工定级】A——自动规则已跳过(档注)',
    'sn-solution.hu 档站谱', 'Tisztelt Bacskai Úr!'))
R.append(person('A-311', 'Christopher Fikes', '美国／Silsbee, TX', 'https://www.fikesmedia.com',
    '顾问对照单元($180 锚点一致);**地方政府/K12 守界句**', '有明确交换/供电需求(交换专长 MTCSWE),且有具体人直联',
    'fikesmedia.com=德州东部顾问铺谱;**地方政府/K12 守界句**;A-311 供位旧差(STC-424 vs CONSULT-OEM)→本波 push≡p1 归位', 'Dear Chris,'))
R.append(person('A-314', 'Rogier Banis', '荷兰／Maurik', 'https://ningaloo.cloud',
    '顾问+托管双窄针($180 锚点一致);诚实角;**p1=CONSULT-OEM 谱(无量产报价)**', '【人工定级】A——自动规则已跳过(档注)',
    'ningaloo.cloud=荷兰云托管顾问铺谱', 'Geachte heer Banis,'))
R.append(person('A-315', 'Roelof Daleboudt', '荷兰／Coevorden', '—（无公开站点）',
    '个人箱窄针($180 锚点一致);Ruckus/HP-E 栈共存句;**p1=CONSULT-OEM 谱(无量产报价)**', '【人工定级】A——自动规则已跳过(档注)',
    '个体顾问无官网档(个人箱在档);Ruckus/HP-E 栈共存句;建档供位待用户补邮箱', 'Geachte heer Daleboudt,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第21波50户.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 21 波 50 户扩招批:A-279~A-328 顺延 50 户(公司档 30(Netonix WISP 谱 3+Allied 代理谱 25+分销 2)+人名司名同体培训谱档 20)',
               'scope': 'US13(公司6+人名7)/UK10(公司7+人名3)/DE7/FR5/NL5/ES2+PE1(319 国别差旗更正)/AT1/IT2/CZ1/HU1/FI1/CA1;守档 3(A-279 关铺/A-301 CH 待查/A-310 同名噪);无站建档 8(284/289/290/293/295/296/297/298);换代窗 4(Berdin/Trusol/BlueBears/DeInta);军防守界 2(Quadratek 加厚+Shea 区注);BABA/教育/公共各守界注',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 21 波 50 户扩招批落盘:', len(R))
