# -*- coding: utf-8 -*-
"""R65 B 类深挖第 2 批(无邮箱户精修)落盘 —— 独立 .py 避免 heredoc 换行坑。"""
import json

src = json.load(open('batch/B类深挖_2026-10-07_R65_R57转写.json', encoding='utf-8'))
by = {r['code']: r for r in src['records']}

# --- B-200 捷克子 ---
r = by['B-200']
r['researched_on'] = '2026-10-07(R65 第 2 批精修 = R57 转写 + R64 KP + 捷克团队页/登记补)'
r['dimensions']['背景深描'] = (
    'OEM Automatic spol. s r.o.(Pražská 239, 250 66 Zdiby;1991 创立=28 年/官网自称 30 年;'
    '瑞典 OEM Automatic AB(Tranås)全资捷克分部;8+ 员工团队页自曝,Red Lion/PULS/HMS Networks/Leadshine/Mersen/Molex/Panasonic 等 30+ 供应商捷克区授权;'
    '捷克 Red Lion 工业交换/HMI 线在位=谱内接口真实;OEM Automatic 集团四国(CZ/SE/UK/NA)协同')
r['fih56']['fact'] += ' | R64/R65 补:Jan Drlík 董事自曝(团队页+info-cechy),Jakub Hanousek 产品口对口'
r['facts'] += [
 {'dim': 'R64 团队页自曝',
  'text': 'Jan Drlík = Ředitel společnosti(董事)+420 241 484 940;Jakub Hanousek = Product Area Manager Machine/Safety/Electronics/Railway(产品口对口);Ilona Kulhánková 供应商订单/物流;Adam Stoklasa 商技代表',
  'quote': 'Jan Drlík Ředitel společnosti +420 241 484 940 … Jakub Hanousek Product Area Manager - Machine, Safety, Electronics, Railway … Ilona Kulhánková Správa dodavatelských objednávek',
  'url': 'https://www.oemautomatic.cz/kontakty/nas-tym'},
 {'dim': 'R64 商业登记',
  'text': 'IČO 438 75 416,1991 创立,Zdiby;Jan Drlík 董事实名名录',
  'quote': 'OEM Automatic, spol. s r.o., Pražská 239, 250 66 Zdiby … IČO: 438 75 416 … Založeno: 1991 … Jan Drlík ředitel společnosti',
  'url': 'https://www.info-cechy.cz/eig-oem-automatic/index.html'},
 {'dim': 'R64 域名核验',
  'text': 'oemautomatic.cz 无 MX(NoAnswer)=无自曝函数邮箱;oemautomatic.se MX outlook 存活,母集团函数邮箱 info@oemautomatic.se 唯一可用直通道',
  'quote': '(dnspython 实测 2026-10-07)oemautomatic.cz → FAIL:NoAnswer;oemautomatic.se → outlook MX',
  'url': '(本地 dnspython 实测记录)'},
]

# --- B-295 瑞典母 ---
r = by['B-295']
r['researched_on'] = '2026-10-07(R65 第 2 批精修 = R57 转写 + R64 KP + 瑞典官网个人页/MyNews 自曝补)'
r['dimensions']['背景深描'] = (
    'OEM Automatic AB(Org.nr 556187-1012,Dalagatan 4 / Box 1011, 573 28 Tranås;075-242 41 00;'
    '瑞典母集团:Jens Kjellsson VD 自曝(MyNews+官网个人页),4 市分部(Malmö/Stockholm/Göteborg/Umeå);'
    '产品线对口=电柜组件(Elskåpskomponenter,Red Lion/工业交换线在同集团旗下 Czech 分);'
    'info@oemautomatic.se 函数邮箱公开+MX outlook 存活;技术/产品/市场/采购/仓层分职能目录')
r['dimensions']['关键人KP'] = ('Jens Kjellsson(VD,jens.kjellsson@oemautomatic.se,076-527 82 80,自曝);'
                             'Nils Svensson(电柜组件产品线经理,nils.svensson@oemautomatic.se);'
                             '集团 Czech 分部 Jan Drlík 借 B-200')
r['kp'] = [
 {'name': 'Jens Kjellsson', 'role': 'VD OEM Automatic AB(董事总经理)',
  'contact': 'jens.kjellsson@oemautomatic.se / 076-527 82 80',
  'status': 'official-self-published(Mynewsdesk+官网个人页双自曝)',
  'source': 'https://www.mynewsdesk.com/se/oemautomatic/contact_people + oemautomatic.se/kontakt/personal'},
 {'name': 'Nils Svensson', 'role': 'Produktansvarig Elskåpskomponenter(电柜组件产品线经理=Red Lion/工业交换对口)',
  'contact': 'nils.svensson@oemautomatic.se', 'status': 'official-self-published',
  'source': 'https://www.mynewsdesk.com/se/oemautomatic/contact_people'},
 {'name': 'Andreas Friberg', 'role': 'Produktansvarig Maskin(机械设备产品线经理)',
  'contact': 'andreas.friberg@oemautomatic.se / 076-527 84 27', 'status': 'official-self-published',
  'source': '同 Mynewsdesk'},
]
r['facts'] += [
 {'dim': 'R65 瑞典 VD 自曝',
  'text': 'Jens Kjellsson VD,jens.kjellsson@oemautomatic.se,076-527 82 80——MyNews+官网个人页双源自曝',
  'quote': 'Jens Kjellsson VD OEM Automatic AB jens.kjellsson@oemautomatic.se 076-527 82 80',
  'url': 'https://www.mynewsdesk.com/se/oemautomatic/contact_people'},
 {'dim': 'R65 瑞典母函数',
  'text': 'info@oemautomatic.se + 075-242 41 00 + Org.nr 556187-1012 + Dalagatan 4 573 42 Tranås 自曝',
  'quote': 'OEM Automatic Sverige AB Box 1011 573 28 Tranås 075-242 41 00 info@oemautomatic.se Org.nr: 556187-1012',
  'url': 'https://www.oemautomatic.se/kontakt/personal'},
 {'dim': 'R65 产品口对口',
  'text': '电柜组件(Elskåpskomponenter)线=Red Lion/工业交换同集团对口,Nils Svensson 为产品线经理',
  'quote': 'Nils Svensson Produktansvarig Elskåpskomponenter nils.svensson@oemautomatic.se 076-527 81 95',
  'url': 'https://www.mynewsdesk.com/se/oemautomatic/contact_people'},
]
r['unknowns56'].insert(0, '捷克子(B-200)vs 瑞典母(本户)谱权边界——Drlík 与 Kjellsson 区域/产品线分层')

# --- B-340 Controller Service ---
r = by['B-340']
r['researched_on'] = '2026-10-07(R65 第 2 批精修 = R57 转写 + R64 KP + DnB/tED/RocketReach 源)'
r['dimensions']['背景深描'] = (
    "Controller Service and Sales Co., Inc.(13 Robbie Rd, Avon MA 02322;"
    "1926 年创立三代家族:Mark M O'Day President(2005 至今,Brown AB+Chicago MBA),"
    "父辈 Bob O'Day 1951-2005;兄弟 Scott O'Day VP Sales&Marketing 共管;38 员工;"
    "Moxa 官方授权+ABB/Eaton Cutler-Hammer/IDEC/Hammond/Puls/Datalogic/Honeywell/Ferraz 在架;"
    "价锚透明:Moxa EDS-G512E-4GSFP $1,399 / EDS-G516E $1,749 页面印刷价")
r['fih56']['fact'] += " | R64/R65 补:Mark O'Day President + Scott O'Day VP S&M + Jim Long Corporate Controller"
r['facts'] += [
 {'dim': 'R64 DnB 实名',
  'text': "Key Principal MARK M O'DAY(President),Avon MA,(800)584-5565",
  'quote': "Key Principal: MARK M O'DAY … Controller Service & Sales Co., Inc. is located at 13 Robbie Rd Avon, MA",
  'url': 'https://www.dnb.com/business-directory/company-profiles.controller_service__sales_co_inc.65ac94bbcbb878dab554ba6fd7598a67.html'},
 {'dim': 'R64 三代家族',
  'text': "Mark 2005 至今;父 Bob O'Day 1951-2005;兄弟 Scott O'Day VP S&M;Michael Sandonato 销市总监;Jim Long Corporate Controller;38 员工",
  'quote': "Mark O'Day (President) | Scott O'Day (VP Sales and Marketing) | Jim Long (Corporate Controller) … 38 employees … company president since 2005 … late father Bob O'Day 1951 to 2005",
  'url': 'https://rocketreach.co/controller-service-sales-inc-management_b5fee96bf60669ae'},
 {'dim': 'R64 管理层访谈',
  'text': "Mark O'Day tED 2014 访谈:收购战略/家族血脉公开口径",
  'quote': 'Mark and his brother Scott share management responsibilities … family owned … founded by his grandfather in 1926',
  'url': 'https://tedmag.com/instant-message-qa-with-controller-services-mark-oday/'},
]

# --- B-421 Pymatek ---
r = by['B-421']
r['researched_on'] = '2026-10-07(R65 第 2 批精修 = R57 转写 + R64 KP + CH/GlobalDatabase 补)'
r['dimensions']['背景深描'] = (
    'Pymatek Automation Ltd(CH 09293772,2014-11-04 注册,Venture Point Wheelhouse Rd, Rugeley WS15 1UZ, Staffordshire;'
    'SIC 71129 Other engineering activities;3 员工规模;主域=pymatek.com(非 .co.uk)MX outlook 存活;'
    'Ybet Haydeé Sánchez Vargas de Pattison 唯一登记董事(2014 至今,1975-06 生);'
    'Martin Pattison 销市经理/Franco Sanchez 销售主管/Kimberly Pinillos GM,GlobalDatabase 全自曝')
r['fih56']['fact'] += ' | R64/R65 补:Ybet 唯一董事 CH 实名 + pymatek.com 主域(非 .co.uk)'
r['facts'] += [
 {'dim': 'R64 CH 实名',
  'text': 'PYMATEK AUTOMATION LTD CH 09293772,2014-11-04 注册,Rugeley WS15 1UZ;Ybet SÁNCHEZ VARGAS DE PATTISON 唯一现任董事',
  'quote': 'PYMATEK AUTOMATION LTD. Company number: 09293772 … Incorporated on 4 November 2014 … Directors: 1 … Mrs. Ybet Haydee Sanchez Vargas De Pattison 04 Nov 2014',
  'url': 'https://www.companiesintheuk.co.uk/ltd/pymatek-automation'},
 {'dim': 'R64 团队层自曝',
  'text': 'pymatek.com 域内:Ybet(Director)/Franco Sanchez(Jefe De Ventas)/Martin Pattison(Sales Manager)/Lucero Vaenzuela(Admin Asst)/Kimberly Pinillos(Gerente General)',
  'quote': 'Ybet Sanchez Vargas De Pattison Director … Franco Sanchez Jefe De Ventas … Martin Pattison Sales Manager … Kimberly Pinillos Gerente General … @pymatek.com',
  'url': 'https://uk.globaldatabase.com/company/pymatek-automation-ltd'},
 {'dim': 'R64 域名核正',
  'text': 'CSV 网站=pymatek.co.uk(名录口径),实际职能域=pymatek.com(全员邮箱挂 pymatek.com),MX outlook 存活——候选挂 pymatek.com 系',
  'quote': '(GlobalDatabase 员工邮箱全挂 ****@pymatek.com)',
  'url': 'https://uk.globaldatabase.com/company/pymatek-automation-ltd'},
]

out = {'date': '2026-10-07', 'wave': 'R65 B 类深挖第 2 批(无邮箱户精修层)',
       'scope': 'B-200/B-295/B-340/B-421 —— 无邮箱 4 户:R64 KP + 公开登记/官网/集团页补',
       'discipline': 'guessed 邮箱 leads-only 不进群发;CSV 入口字段不动;STRUCT email 保持 null(生成器锁步);第一候选仅驻 profile KP 表',
       'records': [by[c] for c in ('B-200', 'B-295', 'B-340', 'B-421')]}
json.dump(out, open('batch/B类深挖_2026-10-07_R65_第2批.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('第 2 批精修 4 户落盘')
