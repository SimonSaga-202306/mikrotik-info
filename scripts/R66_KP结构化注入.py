# -*- coding: utf-8 -*-
"""R66 具名 KP 结构化注入:把第 1-6 波捕获的具名 KP 写回各批次 JSON 的 kp 列表,
渲染器「关键人(KP)与触达通道」表 + 联系方式段附加行直接出表。
纪律:contact 只写公开件邮箱/电话/LinkedIn 通道;status 一律标 leads-only/直发需 opt-in。"""
import glob, json

O = 'official-self-published·谱/leads-only(直发需 opt-in)'
G = 'leads-only·待 opt-in(LinkedIn 公开面)'

KP = {
    'A-342': [
        ('Francesco Mazzola', 'President & CEO/创始人/大股东', 'tnet.it shareholders 页自曝', O, 'https://www.tnet.it/en/shareholders/'),
        ('Elisa Giacone', '联合创始人/HR 负责人', 'tnet.it shareholders 页自曝', O, 'https://www.tnet.it/en/shareholders/'),
    ],
    'A-343': [],
    'A-346': [
        ('Patrick Casteels', 'Kappa Data Group 唯一 CEO/创始人(35% 股)', 'LinkedIn 公司号/Channel News 自曝', G, 'https://channelnews.be/nl/kappa-data-wil-tegen-2030-verdubbelen-nieuwe-ceo-versterkte-aandeelhouders-en-expansie-in-europa/'),
        ('Chris Willems', '前 Co-CEO/M&A 主责', 'Channel News 自曝', G, 'https://channelnews.be/nl/kappa-data-wil-tegen-2030-verdubbelen-nieuwe-ceo-versterkte-aandeelhouders-en-expansie-in-europa/'),
        ('Koert Martens', '技术总监(集团)', 'kappadata.be 25 年史自曝', G, 'https://www.kappadata.be/25-jaar-kappa-data-laten-we-het-samen-vieren/'),
        ('Rubin Zwanenburg', 'Kappa Data Nederland 员工(IoT/Security)', 'LinkedIn 自曝', G, 'https://www.linkedin.com/in/rubin-zwanenburg-b05a952/'),
    ],
    'A-347': [
        ('Patrick Casteels', 'Kappa Data Group 唯一 CEO/创始人(35% 股)', 'LinkedIn 公司号/Channel News 自曝', G, 'https://channelnews.be/nl/kappa-data-wil-tegen-2030-verdubbelen-nieuwe-ceo-versterkte-aandeelhouders-en-expansie-in-europa/'),
        ('Chris Willems', 'M&A 主责', 'Channel News 自曝', G, 'https://channelnews.be/nl/kappa-data-wil-tegen-2030-verdubbelen-nieuwe-ceo-versterkte-aandeelhouders-en-expansie-in-europa/'),
        ('Koert Martens', '技术总监(集团)', 'kappadata.be 自曝', G, 'https://www.kappadata.be/25-jaar-kappa-data-laten-we-het-samen-vieren/'),
        ('Michel Grunspan', '法国 Exer CEO(集团管理)', 'kappadata.be 自曝', G, 'https://www.kappadata.be/25-jaar-kappa-data-laten-we-het-samen-vieren/'),
        ('Erwan Le Guen', '法国国别总监', 'dutchitleaders 自曝', G, 'https://www.dutchitleaders.nl/news/660744/kappa-data-wil-groeien-in-nederland'),
    ],
    'A-348': [
        ('Erlend Bonesvoll', 'Daglig leder(总经理)', 'erlend@nlogic.no / +47 40 61 44 44', O + '·公司新闻稿自曝邮箱', 'https://www.mynewsdesk.com/no/nlogic-as/pressreleases/nlogic-har-tre-nye-ansatte-1213779'),
        ('Arne Giæver', 'Styrets leder(董事长)', 'nlogic.no 谱面', G, 'https://www.1881.no/konsulenter-dataprogramvare-og-utvikling/konsulenter-dataprogramvare-og-utvikling-oslo/konsulenter-dataprogramvare-og-utvikling-skoeyen/nlogic-as_106343012S1/'),
        ('Marcus Erik Wahlberg', '董事', 'nlogic.no 谱面', G, 'https://www.1881.no/konsulenter-dataprogramvare-og-utvikling/konsulenter-dataprogramvare-og-utvikling-oslo/konsulenter-dataprogramvare-og-utvikling-skoeyen/nlogic-as_106343012S1/'),
        ('Robert R. Olsen', 'kundeansvarlig(客户经理)', 'nLogic 新闻稿谱面', G, 'https://www.mynewsdesk.com/no/nlogic-as/pressreleases/nlogic-har-tre-nye-ansatte-1213779'),
        ('Jonas Lindstad', 'Nettverkskonsulent', 'nLogic 新闻稿谱面', G, 'https://www.mynewsdesk.com/no/nlogic-as/pressreleases/nlogic-har-tre-nye-ansatte-1213779'),
    ],
    'A-350': [
        ('Marcos Díaz Nicolás', '物流与采购总监(硬件采购线)', 'LinkedIn 公司页员工自曝', G, 'https://mx.linkedin.com/company/landatel-comunicaciones'),
        ('Roberto Avila', '技术支持经理', 'LinkedIn 公司页员工自曝', G, 'https://mx.linkedin.com/company/landatel-comunicaciones'),
        ('Juana Suarez Lois', '财务/会计', 'LinkedIn 公司页员工自曝', G, 'https://mx.linkedin.com/company/landatel-comunicaciones'),
    ],
    'A-354': [
        ('Ammar Rezek', 'President', 'NTS Direct 官方新闻稿署名下三星扩谱', O, 'https://ntsdirect.com/nts-direct-expands-continued-partnership-samsung/'),
        ('Michael Prefontaine', 'CEO', 'CBInsights/ZoomInfo 双源', G, 'https://www.cbinsights.com/company/nts-direct/people'),
        ('Christopher Turcotte', 'Vice President', 'ZoomInfo', G, 'https://www.datanyze.com/companies/nts-direct/347616523'),
        ('Timothy Dinwoodie', 'Director, Channel Sales', 'ZoomInfo', G, 'https://www.datanyze.com/companies/nts-direct/347616523'),
        ('Erica Ferretti', 'Manager, Marketing & Communications', 'ZoomInfo', G, 'https://www.datanyze.com/companies/nts-direct/347616523'),
    ],
    'A-358': [
        ('Lilly Filopoulou', 'Business Development Manager', 'ContactOut 谱', G, 'https://contactout.com/company/LEXIS-SA-95442'),
        ('Miltos Drikos', 'technical manager', 'ContactOut 谱', G, 'https://contactout.com/company/LEXIS-SA-95442'),
        ('Pavlos Filopoulos', 'Sales Engineer & Technical Support', 'ContactOut 谱', G, 'https://contactout.com/company/LEXIS-SA-95442'),
        ('Grigoris Chatzikakis', 'Store Manager', 'ContactOut 谱', G, 'https://contactout.com/company/LEXIS-SA-95442'),
    ],
    'A-363': [
        ('Ján Seszták', 'Konateľ/CEO(三源一致)', 'Kompass/DnB/clodura 公开件', G, 'https://gb.kompass.com/c/sos-electronic-s-r-o/sk007749/'),
        ('Renáta Tančaková', '财务董事', 'DnB 谱', G, 'https://www.dnb.com/business-directory/company-profiles.sos_electronic_sro.2bbfecf5afc6341343f4aac3b94d9fcd.html'),
        ('Ján Michalko', '商务董事', 'DnB 谱', G, 'https://www.dnb.com/business-directory/company-profiles.sos_electronic_sro.2bbfecf5afc6341343f4aac3b94d9fcd.html'),
        ('Rastislav Taliarovič', '市场董事', 'DnB 谱', G, 'https://www.dnb.com/business-directory/company-profiles.sos_electronic_sro.2bbfecf5afc6341343f4aac3b94d9fcd.html'),
        ('Jozef Jarábek', '采购', 'LinkedIn 自曝 500+', G, 'https://www.linkedin.com/in/jozefjarabek/'),
    ],
    'A-570': [],
    'A-571': [],
    'A-572': [],
    'A-573': [
        ('Grazian Dominik Twonski', 'Gründer & CEO', 'etree.de Über-uns 自署', O, 'https://etree.de/Services/Informationen/UEber-uns/'),
        ('Sebastian Rinne', 'Geschäftsführer/Head of Sales/CFO', '+49 221 292 417 09', O + '·登记册+官网公开电话', 'https://www.online-handelsregister.de/handelsregisterauszug/nw/Koeln/HRB/75598/ETREE-GmbH'),
        ('Peter Valentin Voigt', 'Geschäftsführer', 'Handelsregister 任命件', G, 'https://www.online-handelsregister.de/handelsregisterauszug/nw/Koeln/HRB/75598/ETREE-GmbH'),
        ('Bartholomäus Paul Scislak', 'Geschäftsführer', 'Handelsregister 任命件', G, 'https://www.online-handelsregister.de/handelsregisterauszug/nw/Koeln/HRB/75598/ETREE-GmbH'),
        ('Herr Wysoczanski', 'Sales/Purchase Manager(采购线)', '+49 221 292 417 62', O + '·官网/lieferanten 公开', 'https://www.lieferanten.de/lieferant-21930-ETREE%20GmbH.html'),
    ],
    'A-574': [],
    'A-577': [
        ('Peter Jezernik', 'Direktor', '+386 2 250 22 35', O + '·sloexport 官方名录自曝', 'https://www.sloexport.si/en/company-card?ms=2259826'),
    ],
    'A-578': [],
    'A-579': [
        ('Philippe GINOT', 'Associate Founder(联合创办人)', 'EDOX 公司号 LinkedIn 自署', G, 'https://fr.linkedin.com/company/edox-sas'),
        ('David Hugueny', '技术/销售(MikroTik 培训谱 LinkedIn 自曝)', 'LinkedIn 自曝', G, 'https://www.linkedin.com/in/david-hugueny/'),
        ('Olivier Beluche', '销售(Burnhaupt)', 'LinkedIn 自曝', G, 'https://www.linkedin.com/in/olivier-beluche/'),
        ('Véronique GOERGER', 'Business Development', 'LinkedIn 自曝', G, 'https://fr.linkedin.com/in/v%C3%A9ronique-goerger'),
        ('Olivier GIRARD', 'Graphic Team Leader(15 年)', 'LinkedIn 自曝', G, 'https://www.linkedin.com/in/olivier-girard-edox/'),
    ],
    'A-580': [
        ('Piotr Poniatowski', '个体谱主(本人)', 'CSV 公司名字段即本人谱位', G + '·人名司名同体档', 'https://www.linkedin.com/in/piotrponiatowski'),
    ],
    'A-582': [
        ('Albert Krakus', 'Founder(创始人)', '官网 About 自署+DnB Key Principal', O, 'https://www.vodanetsystems.com/about-us'),
        ('Alper Karakus', 'President', 'ZoomInfo/datanyze 三源', G, 'https://www.datanyze.com/people/Alper-Karakus/-1994171768'),
        ('Andy Kayalica', 'CTO', 'ZoomInfo', G, 'https://www.zoominfo.com/c/vodanet-systems-llc/370619677'),
        ('Cihan Algöz', 'COO', 'ZoomInfo', G, 'https://www.zoominfo.com/c/vodanet-systems-llc/370619677'),
        ('James Cakmak', 'Division Director Industrial Automation', 'datanyze', G, 'https://www.datanyze.com/people/Alper-Karakus/-1994171768'),
        ('Henry Dyson', 'Director IT', 'datanyze', G, 'https://www.datanyze.com/people/Alper-Karakus/-1994171768'),
    ],
    'A-056': [
        ('Jill Samantha Lomax', 'Director(2025-01-08 新任命·谱面交替期首击位)', 'Companies House 军官名单', O, 'https://find-and-update.company-information.service.gov.uk/company/03212967/officers'),
        ('Anthony Owen Moore', 'Director(2008-01-29 任命·原 PSC)', 'Companies House 军官名单', O, 'https://find-and-update.company-information.service.gov.uk/company/03212967/officers'),
        ('Andrew Moulds', 'Director(2009-01-29 任命)', 'Companies House 军官名单', O, 'https://find-and-update.company-information.service.gov.uk/company/03212967/officers'),
    ],
    'A-057': [
        ('Martin Stewart', 'Owner(2005 MBO 班底)', 'LinkedIn 自署 Owner', G, 'https://www.linkedin.com/in/martin-stewart-b3a9616/'),
        ('Ian Rennell', 'Director(2012 至今,原财务总监)', 'RocketReach 谱', G, 'https://rocketreach.co/ian-rennell-email_37924345'),
    ],
    'A-099': [
        ('David James Salisbury', 'Managing Director(2024-12-30 任命)', 'Companies House 军官名单', O, 'https://find-and-update.company-information.service.gov.uk/company/15643579/officers'),
        ('John Robert Dente', 'Director(2024-04-13)', 'Companies House 军官名单', O, 'https://find-and-update.company-information.service.gov.uk/company/15643579/officers'),
        ('John Paul Hubbard', 'Director(2024-12-30)', 'Companies House 军官名单', O, 'https://find-and-update.company-information.service.gov.uk/company/15643579/officers'),
    ],
    'A-100': [
        ('James Douglas Morgan', 'Director(ADS Group 官网联系人)', 'ADS Group 会员页自曝', O, 'https://www.adsgroup.org.uk/members/networkology-ltd-1/'),
        ('David John Owen', 'Director', 'Companies House 军官名单', O, 'https://find-and-update.company-information.service.gov.uk/company/08680414/officers'),
        ('Stefan Nicholas Wallington', 'Director', 'Companies House 军官名单', O, 'https://find-and-update.company-information.service.gov.uk/company/08680414/officers'),
        ('Stuart Andrew Monteith', 'Director(2024-10)', 'Companies House 军官名单', O, 'https://find-and-update.company-information.service.gov.uk/company/08680414/officers'),
        ('Robert Kevin Jelley', 'Director(2024-10)', 'Companies House 军官名单', O, 'https://find-and-update.company-information.service.gov.uk/company/08680414/officers'),
    ],
    'A-103': [
        ('James Napp', 'Managing Director Bechtle direct UK', 'bechtle.com 官网自曝', O, 'https://www.bechtle.com/pt/a-bechtle/a-empresa/filiais/bechtle-direct-UK'),
        ('Konstantin Ebert', 'Executive VP France/Benelux/UK(Bechtle AG 集团层)', 'Tangible Benefit 收购稿自曝', G, 'https://www.tangiblebenefit.com/bechtle-acquisition-bechtle-on-track-to-become-one-of-the-top-10-it-solutions-providers-in-the-uk/'),
    ],
    'A-104': [
        ('Rafi Arif Abdul Razzak', 'Founder & Chairman(1991 在位 35 年)', 'Companies House+Crunchbase 双源', O, 'https://www.crunchbase.com/organization/centerprise-international'),
        ("Jeremy Shane 'Jez' Nash", 'CEO/Director of Sales', 'Crunchbase', G, 'https://www.crunchbase.com/organization/centerprise-international'),
        ('Samantha Louise Lailey', 'HR & Support Director', 'Companies House 军官名单', O, 'https://www.companycheck.co.uk/company/01738519/CENTERPRISE-INTERNATIONAL-LIMITED/companies-house-data'),
        ('Sharon Ann Allen', 'Finance Director', 'Companies House 军官名单', O, 'https://www.companycheck.co.uk/company/01738519/CENTERPRISE-INTERNATIONAL-LIMITED/companies-house-data'),
        ('Jon Atherton', 'CI Group Director', 'Crunchbase', G, 'https://www.crunchbase.com/organization/centerprise-international'),
    ],
    'A-105': [
        ('Roger Paul', 'Founder/Owner & Chairman', 'Crunchbase+Tracxn 双源', G, 'https://www.crunchbase.com/organization/cisilion'),
        ('Nick Paul (Nicholas Paul)', 'CEO', 'RocketReach/Tracxn/Owler 三源', G, 'https://rocketreach.co/cisilion-profile_b5c6770bf42e0c8b7b'),
        ('Rob Quickenden', 'Chief Technology Officer', 'Crunchbase', G, 'https://www.crunchbase.com/organization/cisilion'),
        ('Paul Johnson', 'Account Director', 'Crunchbase', G, 'https://www.crunchbase.com/organization/cisilion'),
    ],
}

PERSON = {
    'A-344': 'Luigi Boi', 'A-355': 'V. Ahababian', 'A-356': 'Athanasios Pournaras',
    'A-359': 'Vadim Scornici', 'A-360': 'Andrii Sychov', 'A-361': 'Michal Dobšovič',
    'A-362': 'Ivan Dolnak', 'A-364': 'Olisian Sulaj', 'A-366': 'Robertas Stauskas',
    'A-367': 'Petar Dimitrov', 'A-368': 'Kęstutis Viselga', 'A-369': 'Veaceslav Samburschii',
    'A-370': 'Oltion Nikolla', 'A-371': 'Martin Soovares', 'A-372': 'Domagoj Bikic',
    'A-374': 'Rein Põdra', 'A-375': 'Jānis Jaunošāns', 'A-376': 'Jernej Suhadolc',
    'A-583': 'Barry Higgins', 'A-584': 'Ron Touw',
}
PERSON_EXTRA = {'A-368': 'MikroTik 认证 Trainer 谱(守界:训练类不新挖=本体存档)',
                'A-369': 'Academia MikroTik 主理(守界)', 'A-583': 'Allness(守界:训练/顾问类不新挖)',
                'A-584': 'MikroTik Trainer 谱(守界:训练/顾问类不新挖)'}

changed = 0
for path in glob.glob('batch/A类深挖_2026-10-07_R66_R56_*.json'):
    data = json.load(open(path, encoding='utf-8'))
    dirty = False
    for rec in data['records']:
        code = rec.get('customer') or rec.get('code')
        if not code:
            continue
        kp_list = []
        if code in KP:
            for name, role, contact, status, src in KP[code]:
                kp_list.append({'name': name, 'role': role, 'contact': contact, 'status': status, 'source': src})
        elif code in PERSON:
            nm = PERSON[code]
            em = ''
            blob = json.dumps(rec, ensure_ascii=False)
            if '@' in blob:
                import re as _re
                m = _re.search(r'([\w.+-]+@[\w-]+\.[\w.]+)', blob)
                em = m.group(1) if m else ''
            kp_list.append({'name': nm, 'role': PERSON_EXTRA.get(code, '个体谱主/本人(公司名字段即本人谱位)'),
                            'contact': em or '—', 'status': 'official-self-published·谱/人名司名同体(leads-only,直发需 opt-in)',
                            'source': 'CSV 公司名字段+R66 基线(2026-10-07)'})
        if kp_list and rec.get('kp') != kp_list:
            rec['kp'] = kp_list
            dirty = True
    if dirty:
        json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        changed += 1
        print('注入:', path.split('/')[-1])
print('kp 结构化注入完成,改动文件数:', changed)
