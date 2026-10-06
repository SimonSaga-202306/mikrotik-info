#!/usr/bin/env python3
"""
R62(2026-10-04)批量处置:
  ① 退信 9 户永久 dead + A-337 备注标注 + A-342 临时 retry 观察备注
  ② 4 户人工新邮箱补录: A-251 beszerzes@macsoft.hu、A-258 biuro@csidet.edu.pl、
     A-487 nfo@→info@marcomweb.it 修正、A-520 support@axbyte.se(与 A-064 同源)
  ③ A-311 状态升 02-已双向对话(2 轮) + 跟进日期
原则: 退信不删邮箱,只标「发不过去」+替代路径(乌克兰户不主动找替代,只标注)
"""
import csv, sys

CSV = '客户名单_反向信号_2026-09.csv'
with open(CSV, encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    rows = list(reader)

BOUNCE = {   # 编号: (退信邮箱, 类型, 替代路径建议)
    'A-170': ('einkauf@nitoit.de', 'not-found',
              '官网 https://nitoit.de 表单/Impressum 电话;今未再发送,先电话验证'),
    'A-123': ('hbowerman@professionalcablingsolutions.com', 'not-found(46h|21h retry 后 Message not delivered)',
              '官网 professionalcablingsolutions.com 表单 +1 513 总机;今未再发送'),
    'A-355': ('vartan@mikrotikls.com.ua', 'domain-not-found',
              '乌克兰守界:仅标注不主动挖替代;电话 +38 066 907 44 88 保留'),
    'A-424': ('lima@wifiprofi.cz', 'not-found',
              '正确人名 klima@wifiprofi.cz(已库有 A-288 Krystof Klima 个人档);774 331 774'),
    'A-434': ('sale@lanmarket.net', 'domain-not-found(.net 失效,正域 lanmarket.ua)',
              '乌克兰守界:仅标注;电话 +380 50 666 78 58 保留;若续发应改 lanmarket.ua 域'),
    'A-439': ('molya@technotrade.com.ua', 'not-found',
              '乌克兰守界:仅标注;电话 +380 57 764 02 54 保留'),
    'A-458': ('info@cooltechtrading.com', 'not-found',
              '官网 cooltechtrading.com 表单;+90 542 883 1111'),
    'A-476': ('info@wirelesslan.gr', 'not-found',
              '官网 wirelesslan.gr 表单;+30 2310 510030'),
    'A-088': ('info@electromaster.ie', 'not-found(46h|20h retry 后 Message not delivered)',
              '爱尔兰都柏林 Tallaght 总机(Golden Pages 名录);官网表单;今未再发送'),
}

cnt = 0
for r in rows:
    code = r['档案编号']
    if code in BOUNCE:
        email, reason, alt = BOUNCE[code]
        ent = r.get('入口/联系方式', '')
        # 退信标:在该邮箱后插入【已停用】标记(若未标)
        if '发不过去' not in ent and email not in ent.split('【已停用')[0][-0:] :
            tag = f'【已停用:2026-10-04 退信 {reason} 发不过去】'
            if email in ent:
                ent = ent.replace(email, email + tag, 1)
            else:
                ent = tag + ' ' + ent
        r['入口/联系方式'] = ent
        note = f'【2026-10-04 R62 退信批】{email} Gmail 退回({reason});不删邮箱只标发不过去;替代:{alt}'
        if note not in r.get('备注',''):
            r['备注'] = (r.get('备注','').rstrip() + ' ' + note) if r.get('备注') else note
        cnt += 1

    # A-337 ingesw:guess tenant not in library → 备注标注
    if code == 'A-337':
        note = ('【2026-10-04 R62 退信批】fabio.mundadori7114@ingesw.onmicrosoft.com M365 tenant 猜测直邮'
                '被退(user not found);库内无此邮箱,仅标注说明以后勿向 onmicrosoft.com 租户域猜测投递;'
                '主邮箱 info@ingesw.com 未发不受影响')
        if 'onmicrosoft.com' not in r.get('备注',''):
            r['备注'] = r.get('备注','').rstrip() + ' ' + note
        cnt += 1

    # A-342 tnet temporary retry
    if code == 'A-342':
        note = ('【2026-10-04 R62 退信批·观察】info@tnet.it Gmail 临时退信(45h retry 中),'
                '非永久失败;暂不标发不过去,等 48h 结果再定;若永久失败转正式退信处置')
        if '观察' not in r.get('备注',''):
            r['备注'] = r.get('备注','').rstrip() + ' ' + note
        cnt += 1

    # ② 补录邮箱
    if code == 'A-251':
        ent = r.get('入口/联系方式','')
        if 'beszerzes@macsoft.hu' not in ent:
            r['入口/联系方式'] = ent + ';beszerzes@macsoft.hu(用户 2026-10-04 官网查到,macsoft.hu 机构采购邮箱;与 A-250 Péter Major 同入口)'
            r['备注'] = r.get('备注','').rstrip() + ' 【2026-10-04 R62 用户补录】beszerzes@macsoft.hu 官网录入'
        cnt += 1
    if code == 'A-258':
        ent = r.get('入口/联系方式','')
        if 'biuro@csidet.edu.pl' not in ent:
            r['入口/联系方式'] = ent + ';biuro@csidet.edu.pl(用户 2026-10-04 官网查到,csidet.edu.pl 机构邮箱非个人直邮;与 A-252 Kajetan Tadra 同入口)'
            r['备注'] = r.get('备注','').rstrip() + ' 【2026-10-04 R62 用户补录】biuro@csidet.edu.pl 官网录入'
        cnt += 1
    if code == 'A-487':
        ent = r.get('入口/联系方式','')
        if 'nfo@marcomweb.it' in ent:
            r['入口/联系方式'] = ent.replace('nfo@marcomweb.it',
                'info@marcomweb.it【2026-10-04 修正:原录 nfo@ 缺首字母 i,用户官网核对为 info@】')
            r['备注'] = r.get('备注','').rstrip() + ' 【2026-10-04 R62 用户修正】nfo@→info@marcomweb.it(缺 i typo)'
            cnt += 1
    if code == 'A-520':
        ent = r.get('入口/联系方式','')
        if 'support@axbyte.se' not in ent:
            r['入口/联系方式'] = ent + ';support@axbyte.se(用户 2026-10-04 官网查询;同属瑞典 AxByte 系 A-064 入口,08-586 195 00 同总机,作替代通道)'
            r['备注'] = r.get('备注','').rstrip() + ' 【2026-10-04 R62 用户查重】support@axbyte.se 已见于 A-064(Fredrik Hellgren),本 A-520 补作替代通道'
            cnt += 1

    # ③ A-311 升级
    if code == 'A-311':
        r['状态'] = '02-已双向对话(2 轮)'
        r['最后互动日'] = '2026-10-04'
        r['下次跟进日'] = '2026-10-08'
        note = ('【2026-10-04 R62】Fikes Media 开发信 12 分钟后 Owner Christopher Fikes 亲回:'
                '「This actually does have my interest」三问=定制程度/controller integration API/规格书+型号表;'
                '当晚回信(5 附件:datasheet/Feature List L2+/MIB/CLI/Web manual),'
                '定制项清单(logo/包装/PVC mask/label/型号名/SN/manual/默认 IP/SNMP OID/Web 语言)'
                '+CT integration 反问(REST/SNMP/SSH/CLI/NETCONF/其他)+用途追问(lab/deployment/OEM);'
                '等客户回 controller 架构后再问 SmartByte 技术(假期中勿乱答 API)')
        if 'Fikes Media 开发信' not in r.get('备注',''):
            r['备注'] = r.get('备注','').rstrip() + ' ' + note
        cnt += 1

with open(CSV, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=header)
    w.writeheader(); w.writerows(rows)
print(f'CSV 处置完成: {cnt} 行')
