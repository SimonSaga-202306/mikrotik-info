# -*- coding: utf-8 -*-
"""R66 第 15 波:A-133/A-134/A-178/A-187 四户。"""
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
        inference='R66 第 14 波具名 KP 金谱', trend='2026-10-08 R66 14 波谱名牌', gap='R66 14 波谱面锁定'):
    kb = '**' + ';'.join('%s(%s,%s)' % (k[0], k[1], k[3]) for k in kp) + '**' if kp else '**守档准由;R66 波次二点名**'
    dims = {'业务定位': heads, '产品线与在售品牌': '(波次二补谱面)', '目标行业与场景': scene, '团队与规模': size,
            '决策链与对接人': kb, '技术与认证': '(波次二补)', '采购与供应链信号': '(波次二补)',
            '近期动态与线索': trend, '与我方契合点': '24 口 value PoE 谱链窗口', '风险与注意': risk}
    return {'customer': code, 'fact': name + ':' + heads, 'inference': inference,
            'hypothesis': '24 口 value PoE(' + PRICE + ')具名谱位引路', 'evidence_main': evs[0]['source'],
            'tech': '(波次二补)', 'hr': size, 'contact_found': kb, 'contact_pending': '直发具名需 opt-in',
            'dims': dims, 'evidence': evs, 'followups': fu(),
            'r55': {'dims': {'①背景再核': heads, '②芯片/型号': '(待谱面二补)', '③KP 深挖': kb,
                             '④Saga 对标': '24 口 value PoE(' + PRICE + ')', '⑤在乎与偏好': sw[0],
                             '⑥SWOT': 'S ' + sw[0] + ' / W ' + sw[1] + ' / O ' + sw[2] + ' / T ' + sw[3]},
                    'care': ['直发具名需 opt-in'], 'swot': {'S': sw[0], 'W': sw[1], 'O': sw[2], 'T': sw[3]},
                    'uncertain': {'产品线核实': '波次二补', '合作方式': '未知', '缺口证据': '(波次二)'},
                    'gap_proof': gap},
            'kp': [{'name': k[0], 'role': k[1], 'contact': k[2], 'status': k[3], 'source': k[4]} for k in kp],
            'unknowns': ['硬件采购线在职者(波次二)', 'MikroTik 谱面份额'],
            'email': email_sal + '\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-07, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?\n\nBest regards,\nSaga Networks Export Desk'}

def ev(d, q, u):
    return {'dim': d, 'quote': q, 'source': u}

R = []

R.append(rec('A-133', '5G IT Service GmbH',
    '5G IT Service GmbH(德国 Westmünsterland,2020-01-01 创(六岁;**"5G"=Fünf Gründer 五位创始人从他 IT 系统屋集体跳出**);**HRB 18608 Amtsgericht Coesfeld,资本 €25,000;原址 Reken Carl-Benz-Str. 21 → 2026-02-12 迁址登记 Velen Industriestraße 13**;19 员工;$info@5G-IT.de;谱型=全栈 MSP(denken in Lösungen,咨询/概念/落地/托管+安全 NIS2-化+营销义观察;Kappenhagen 引语「IT 后台可靠运转,老板腾手」=SMB 管服谱)',
    [('Falk Kappenhagen', 'Geschäftsführer(执行董事;2022-11-02 起 einzelvertretungsberechtigt;一九九〇年生;regiomanager 公司事引语)', 'webvalid/registercheck 登记册谱+regiomanager 专文引语', O, 'https://www.webvalid.de/company/5G+IT+Service+GmbH,+Velen/HRB+18608'),
     ('Bernward Schepermann', 'Prokurist(授权代理;2020-01-09 与公司同日登记入职位)', 'webvalid 登记册谱', O, 'https://www.webvalid.de/company/5G+IT+Service+GmbH,+Velen/HRB+18608'),
     ('Michael Paschen', '原 Geschäftsführer(2020 联合登记,2021-01-25 Austritt 谱)', 'webvalid 登记册谱(留痕)', O, 'https://www.webvalid.de/company/5G+IT+Service+GmbH,+Velen/HRB+18608'),
     ('Alexander Hilgenberg', 'Marketing-Verantwortlicher(营销负责人;安全议题公司事引语)', 'regiomanager.de 专文引语', G, 'https://www.regiomanager.de/artikel/5g-it-service-it-pauschal-skalierbar/')],
    [ev('决策链与对接人', 'Geschäftsführer: Kappenhagen, Falk (seit 02.11.2022, einzelvertretungsberechtigt, geb. 1990);Prokurist: Schepermann, Bernward (Eintritt 09.01.2020);Nicht mehr GF: Paschen, Michael (Austritt 25.01.2021)', 'https://www.webvalid.de/company/5G+IT+Service+GmbH,+Velen/HRB+18608'),
     ev('团队与规模', '„Unser Ziel ist, dass der Unternehmer seinen Kopf frei hat…" — GF Falk Kappenhagen;5G=fünf Gründer(1.1.2020, vor Corona);heute 19 Mitarbeitende;Alexander Hilgenberg verantwortet das Marketing(安全议题引语)', 'https://www.regiomanager.de/artikel/5g-it-service-it-pauschal-skalierbar/'),
     ev('联系方式与基础画像', 'Sitzverlegung 12.02.2026: Velen, Industriestraße 13, 46342;原 Carl-Benz-Str. 21, 48734 Reken;AG Coesfeld HRB 18608;€25,000;g gegründet 3.12.2019;info@5G-IT.de;+49 2864 3303110', 'https://www.registercheck.de/companies/5g-it-service-gmbh')],
    '德国 Münsterland 五位创始 SMB 全栈 MSP', '19 人;2020 创;€2-5M 谱',
    ('五创始联合跳槽谱=技术硬核', '小实体(19 人)年轻谱', 'Kappenhagen 法代直达位', 'KRITIS/安全谱竞位'),
    'Kappenhagen GF+Schepermann Prokurist(opt-in 律)', 'Guten Tag Herr Kappenhagen,'))

R.append(rec('A-134', 'ACP IT Solutions GmbH',
    'ACP IT Solutions GmbH(**德国 Halle(Saale) 中德区**;**HRB 201508 Amtsgericht Stendal,UID DE140098719;Daniel-Vorländer-Straße 6, 06120 Halle**;支谱 Halle/Dresden/Leipzig/Sangerhausen/Bielefeld ~125 人;1990 源 Wichmann,2018 并入 ACP Gruppe(50+ Geschäftsstellen,2,600 人,德奥瑞);档案已谱型谱:360° IT/MS+Veeam BaaS 德国最大 SP 之一/ISO 27001+9001 双证自有 Tier-3 DC(Dresden+Jena)/SIOS 独占欧洲伙伴/NIS2 咨询/**Allied Telesis 集成链(Marvell Prestera 接入层)**;Public Sector+KRITIS 红线分区守界;客户墙 IHK Potsdam/莱比锡会展/Stadtwerke Halle 等',
    [('Sten Jacobson', 'Geschäftsführung(执行董事;acp-gruppe.com Dresden 页 Ansprechpartner+vertretungsrechtlich 自署)', 'acp-gruppe.com 官网 Standort Dresden/Kontaktliste', O, 'https://www.acp-gruppe.com/standorte/dresden'),
     ('Jörg Fischer', 'Prokurist & GF RZ(授权代理+数据中心层谱)', 'acp-gruppe.com 官网 Standort Dresden', O, 'https://www.acp-gruppe.com/standorte/dresden'),
     ('Eric Meier', 'Prokurist(授权代理;档案 R 层深挖已谱)', '档案已落(深挖三层谱)', G, 'https://www.acp-gruppe.com/de-at/kontaktliste'),
     ('Annemarie Plaschnik', 'Vertriebsleiterin-a.D.-谱线(销售副总监;档案已谱)', '档案已落(深挖三层谱)', G, 'https://www.acp-gruppe.com/de-at/kontaktliste')],
    [ev('决策链与对接人', 'ACP Mitteldeutschland Ansprechpartner: Sten Jacobson, Geschäftsführung;Jörg Fischer, Prokurist & GF RZ;Sitz: Daniel-Vorländer-Str. 6, 06120 Halle (Saale);AG Stendal HRB 201508;Ust-ID DE140098719(官网 standorte/dresden Impressum 级)', 'https://www.acp-gruppe.com/standorte/dresden'),
     ev('联系方式与基础画像', 'Halle: ACP IT Solutions GmbH, Daniel-Vorländer-Straße 6, 06120 Halle (Saale);halle@acp.de;+49 345 233040;HRB: 201508;UID: DE140098719(官网 kontaktliste)', 'https://www.acp-gruppe.com/de-at/kontaktliste')],
    '德国 Mitteldeutschland 360° IT 系统屋(ACP 集团)', '~125 人(集团 2,600);1990 源',
    ('集团牌谱+自有 DC 双证', 'KRITIS/Public 守界段', 'Jacobson GF 直达位', '一线厂商链竞位'),
    'Jacobson GF+Fischer Prokurist+已谱 Meier/Plaschnik(opt-in 律+红线守界)', 'Guten Tag Herr Jacobson,'))

R.append(rec('A-178', 'Selos Informationssysteme GmbH',
    'Selos Informationssysteme GmbH(德国 Wilhelmshaven,Bismarckstraße 185, 26382;**HRB 130547 Amtsgericht Oldenburg**;**1993-05-03 创立(33+ 年;MPDT+CBR 合并谱;创始谱系 Udo Hicken/Egon Rocker/Rainer Kuhlmann/Peter Warnken)**;kontakt@selos.de;+49 4421 9787-0;谱型=Jade-Weser 技术系统屋(Beratung/Konzeption/Lieferung/Installation;IT 基础设施/Server-Client/备份合规/虚拟化云/电信/监控/补丁管理/Service;**Jörg Johann Müller 国防军 Bundeswehr 政府线(最大最重要客户)+Jan Lucklum 民营 Jade-Weser SME 线,2001 首批 Fachinformatiker Azubi→2018 接棒 GF,两代学徒-继承谱**)',
    [('Jan Lucklum', 'Geschäftsführer(执行董事;2001 首批学徒→2018 起 GF;**民营 SME 线直管**)', 'selos.de Impressum 法代自署+nwzonline 专文+webvalid 登记册', O, 'https://www.selos.de/index.php/impressum'),
     ('Jörg Johann Müller', 'Geschäftsführer(执行董事;Industriemeister Elektrotechnik,创始首日队;**Bundeswehr 政府线直管**)', 'selos.de Impressum 法代自署+awv-jade 会员谱+nwzonline 专文', O, 'https://www.selos.de/index.php/impressum')],
    [ev('决策链与对接人', 'Vertreten durch die Geschäftsführer: Jan Lucklum;Jörg Johann Müller (Industriemeister Fachrichtung Elektrotechnik);Bismarckstraße 185, 26382 Wilhelmshaven;+49 4421 9787-0(selos.de 官网 Impressum)', 'https://www.selos.de/index.php/impressum'),
     ev('团队与规模', '1993-05-03 由 MPDT+CBR 合并创;创始谱 Udo Hicken/Egon Rocker/Rainer Kuhlmann/Peter Warnken;Rocker 2006 离,Hicken 2016 离,Kuhlmann 25 年后 2018 退休;seit 2018 müller+Lücklum 双 GF:Lücklum (42, 2001 首批 Fachinformatiker-Azubi) 民营线+H. Müller (55) Bundeswehr 政府线(nwzonline Selos 公司介绍件)', 'https://www.nwzonline.de/advertorial/selos-informationssysteme_a_4,0,914149308.html'),
     ev('联系方式与基础画像', 'HRB 130547 Oldenburg;Bestellt als GF: Lucklum, Jan(einzelvertretungsberechtigt);Nicht mehr GF: Kuhlmann 2018/Hicken 2015(webvalid 登记册谱);kontakt@selos.de(implisense)', 'https://www.webvalid.de/company/Selos+Informationssysteme+GmbH,+Wilhelmshaven/HRB+130547')],
    '德国 Wilhelmshaven 33 年技术系统屋(Bundeswehr+SME 双线)', 'Kleinunternehmen;1993 创',
    ('33 年谱+Bundeswehr 长期客户', '政府线守界段', '双 GF 学徒-接棒谱直达', '一线品牌链竞位'),
    'Lucklum SME 线 GF 直达(政府线守界;opt-in 律)', 'Guten Tag Herr Lucklum,'))

R.append(rec('A-187', 'Groupe Networks',
    'GROUPE NETWORKS(法国 Aubagne(13),100 Chemin de Saint Lambert Actiburo 3 Entrée C;**SIREN 530634252,RCS Marseille;SAS,资本 €866,400(原 879,600 谱减);01/01/2011 创立(15 年);6-9 salariés;CA 2023 €1,031,938**;groupenetworks.fr;谱型=TPE/PME 电信方案商(Telecom et Réseaux:固定/移动(4G/5G)telephony+VoIP/RTC 关闭换代+Internet(基于 Orange/Bouygues/SFR 网络);**MC2C CONSEILS(SIREN 823997283)=Président 2017 起**;CAC=GROUPE FGC;**bénéficiaire effectif=谱面 Maurice COHEN**;历史谱 Président LTH CONSEILS(受益人 Laurent THOMAS)→2016-12-22 辞任交接 MC2C;创位 DG=ED PARTICIPATION(受益人 Emmanuel DAVID);**Groupe Networks 自任 HEO NETWORKS(SIREN 794526004)Président=集团上位节**',
    [('Maurice COHEN', 'Bénéficiaire effectif(实质受益人;MC2C CONSEILS Président 径)', 'pappers.fr RNE 谱推定', G, 'https://www.pappers.fr/entreprise/groupe-networks-530634252'),
     ('MC2C CONSEILS', 'Président(法人总裁;SIREN 823997283,2017-01-10 起在职)', 'societe.com/RNE 谱+lefigaro 法定公告(AGO 22/12/2016)', G, 'https://www.societe.com/societe/groupe-networks-530634252.html'),
     ('Laurent THOMAS', '创位期 Président(LTH CONSEILS;2011-2016 谱;受益人)', 'pappers.fr BODACC 谱(留痕)', G, 'https://www.pappers.fr/entreprise/groupe-networks-530634252'),
     ('Emmanuel DAVID', '创位 Directeur général(ED PARTICIPATION;2011 谱;受益人)', 'pappers.fr/entreprises.lefigaro BODACC 谱(留痕)', G, 'https://entreprises.lefigaro.fr/groupe-networks-13/entreprise-530634252')],
    [ev('决策链与对接人', 'Dirigeants: MC2C CONSEILS Président (SIREN 823997283, depuis 10/01/2017);GROUPE FGC CAC titulaire (depuis 28/10/2021);Dirigeants et bénéficiaires effectifs: Maurice COHEN (via MC2C);Laurent THOMAS (LTH, historique);Emmanuel DAVID (ED PARTICIPATION, historique);GROUPE NETWORKS est Président de HEO NETWORKS (SIREN 794526004)', 'https://www.pappers.fr/entreprise/groupe-networks-530634252'),
     ev('联系方式与基础画像', 'SAS au capital de 866 400 €;SIREN 530634252;RCS Marseille;100 che de St Lambert Actiburo 3, 13400 Aubagne;création 01/01/2011;6 à 9 salariés;CA 2023 1 031 938 €(manageo/societe 件)', 'https://www.manageo.fr/entreprises/530634252.html'),
     ev('业务定位', 'Groupe Networks est LE FOURNISSEUR DE SOLUTIONS TÉLÉCOMS POUR LES TPE/PME;offres Internet basées sur les réseaux Orange, Bouygues et SFR;téléphonie IP/VoIP(RTC 关闭换代)+mobile 4G/5G(groupenetworks.fr 官网 telecom-et-reseaux 页)', 'https://groupenetworks.fr/telecom-et-reseaux/')],
    '法国 Sud TPE/PME 电信方案商(Reseller 三大运营商)', '6-9 人;2011 创;CA €1.03M',
    ('15 年 TPE/PME 电信深耕谱', '小实体谱(6-9 人)', 'Cohen 实质受益人+MC2C Président 谱位', '大牌线缆件链竞谱'),
    'Cohen 受益人+MC2C Consults Président(opt-in 律)', 'Bonjour Monsieur Cohen,'))

with open('batch/A类深挖_2026-10-08_R66_R56_KP第15波.json', 'w', encoding='utf-8') as f:
    json.dump({'date': '2026-10-08',
               'wave': 'R66 第 15 波:5G IT Service(五创始+GF 登记谱)/ACP Halle(GF+Prokurist 官网谱)/Selos(33 年双 GF 学徒-接棒谱)/Groupe Networks(Cohen 受益人谱)四户',
               'scope': 'DE×3/FR 谱;HRB 18608/201508/130547 + SIREN 530634252 各锚;ACP 奥地利同体已分层',
               'records': R}, f, ensure_ascii=False, indent=1)
print('R66 第 15 波四户落盘')
