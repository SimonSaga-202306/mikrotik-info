# -*- coding: utf-8 -*-
"""R65 B 类深挖第 20 批:西班牙 8 户收尾。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

def put(code, head=None, kpn=None, kp=None, facts=(), fihadd=''):
    r = by[code]
    r['researched_on'] = '2026-10-07(R65 第 20 批精修 = R57 转写 + 本轮调研新挖)'
    if head: r['dimensions']['背景深描'] = head
    if kpn: r['dimensions']['关键人KP'] = kpn
    if kp is not None: r['kp'] = kp
    r['facts'] += facts
    if fihadd: r['fih56']['fact'] += ' | R65 深挖:' + fihadd
    return r

put('B-480',
    head='Strato Networks(C/ Pollensa 2 planta 1, 28290 Las Rozas de Madrid;2008-01 创；Ricardo Bernao Gonzalez 实体谱主位（CSV 谱口径）;',
    kpn='Ricardo Bernao Gonzalez = 实体谱主位（CSV 口径）',
    kp=[{'name': 'Ricardo Bernao Gonzalez', 'role': '谱主位实体', 'contact': 'info@stratonetworks.com / +34 657 478 596', 'status': 'CSV 口径+stratonetworks.com 官网自曝', 'source': 'https://www.stratonetworks.com/portada/acerca.php'}],
    facts=[{'dim': 'R65 谱/自曝', 'text': 'Strato Networks 2008 创 Las Rozas · 50+ 客户 85% tech staff · 公行(public sector 专放） · Blue team防御 Sophos Silver/SonicWall/MikroTik · MikroTik RouterOS 训练课与 InstantByte 欧洲分销联名(5 届)',
            'quote': 'En Enero de 2008 fundamos Strato Networks … Strato Networks trabaja con más 50 clientes … 85% de personal técnico … Somos partner Silver de Sophos … Certificaciones Mikrotik … formacion(arroba)stratonetworks(punto)(com)',
            'url': 'https://www.stratonetworks.com/portada/acerca.php'}],
    fihadd='Las Rozas 公行防御实体 + MikroTik 培训课联名实体')

put('B-467',
    head='Enric Perpinyà Pitarch(Perpignan 法国侧,R65 判定谱型：西班牙马略卡青年创业——PERPITECH 法国PERPIGNAN SIREN 818099160,2016-01-23 创（原名 BD ELEC 2019-01-28 转名）= **Enric Perpinyà 实体映射核正**;'
         '**2025 Connect\'Up 青年类（Youth 2025）首获奖**：Perpi.Tech 企业网络监测/安全防护方案;14 Rue Pierre Lescot 66000 Perpignan;Damien Boudot 首任 prá 总裁 2016',
    kpn='Enric Perpinyà = Perpi.Tech 创始人（2025 Connect\'Up Youth 获奖）;Damien Boudot 实体 2016 首总裁',
    kp=[{'name': 'Enric Perpinyà Pitarch', 'role': 'PerpiTech 创始人/CEO(Youth 2025 获奖）', 'contact': '经 perpi.tech / +33 侧', 'status': 'ultimahora.es 2026-07-15 专访自曝', 'source': 'https://www.ultimahora.es/noticias/local/2026/07/15/2666711/connect-ayudo-convertir-idea-algo-util-para-mercado.html'}],
    facts=[{'dim': 'R65 实体核正', 'text': 'PERPITECH Perpignan SIREN 818099160 · 2016 创（BD ELEC 转名）· Enric Perpinyà Connect\'Up Youth 2025 首获企业网络监测方案',
            'quote': 'Société PERPITECH à PERPIGNAN - SIREN : 818099160 … «Connect\'Up me ayudó a convertir la idea en algo útil para el mercado» … Enric Perpinyà, fundador de Perpi.Tech … ganó la categoría Youth 2025',
            'url': 'https://rubypayeur.com/societe/perpitech-818099160'}],
    fihadd='Perpignan 西班牙跨界实体；Youth 2025 青年谱位最新入场口')

put('B-471',
    head='IT Consultores（西班牙 MikroTik 官方认证咨询者实体：「Consultores Certificados MikroTik」自曝 itconsultores.es;20+ 年 TI 网络经验；Jorge Agulló 实体谱主位（CSV))',
    kpn='Jorge Agulló（CSV 谱主位）+ Consultores Certificados MikroTik 官方自曝',
    kp=[{'name': 'Jorge Agulló', 'role': 'Consultor Certificado MikroTik', 'contact': '经 itconsultores.es', 'status': 'CSV + itconsultores.es 官网自曝', 'source': 'https://www.itconsultores.es/'}],
    facts=[{'dim': 'R65 自曝', 'text': 'IT Consultores 官方自曝「Consultores Certificados MikroTik;20+ 年」',
            'quote': 'Consultores Certificados MikroTik Más de 20 años de experiencia en el el área de TI y redes … diseño de infraestructura de red … VPN … ancho de banda',
            'url': 'https://www.itconsultores.es/'}],
    fihadd='西班牙 MikroTik 认证咨询 20 年谱位')

put('B-474',
    head='Jose Maria Catala Ortega(DUALCOM 个体顾问本体;R65 判定:法国 Villebrumier SIREN 403131188(holding) / Marseille SIREN 499768315(已解散) / UK CSL DualCom(M2M 1996) 三同名实体均已排除,不采信;B-474=西班牙个体顾问本体(CSV 谱主位))',
    kpn='José María Catalá Ortega = 个体谱主位（CSV 口径；R65 同名排除）',
    kp=[{'name': 'José María Catalá Ortega', 'role': 'Consultor(Dualcom 个人谱）', 'contact': '经 CSV 入口', 'status': 'CSV 口径（R65 同名实体排除）', 'source': '(CSV 本体 + R65 同名排核日志）'}],
    facts=[{'dim': 'R65 同名排除', 'text': '法国/马赛/英国三同名 DUALCOM 实体排除后，B-474 为西班牙个体顾问本体',
            'quote': '(R65 同名实体验证日志：403131188/499768315/CSL Dualcom UK 均已排除）',
            'url': '(R65 核验日志）'}],
    fihadd='同名三暗排除；西班牙个体本体守档')

put('B-457',
    head='Adrián González Notario（西班牙个体谱；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由')

put('B-458',
    head='Arber Reca Sina（西班牙/阿尔巴尼亚谱；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote': '(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由')

put('B-464',
    head='David Forteza Rey Casasnovas(son Andreu/Illes Balears 个体谱；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由')

put('B-481',
    head='Santiago Balaguer Garcia（西班牙个体谱；R65 搜索无果守档准由）',
    facts=[{'dim': 'R65 查询注', 'text': '2026-10-07 搜索无果；守档准由', 'quote':'(web_search 无果）', 'url': '（沙箱日志）'}],
    fihadd='守档准由')

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 20 批（西班牙 8 户收尾）',
       'scope': 'B-480 Strato Networks / B-467 Perpi.tech / B-471 IT Consultores / B-474 Dualcom / B-457 / B-458 / B-464 / B-481',
       'records': [by[c] for c in ('B-480', 'B-467', 'B-471', 'B-474', 'B-457', 'B-458', 'B-464', 'B-481')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第20批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 20 批 8 户落盘')
