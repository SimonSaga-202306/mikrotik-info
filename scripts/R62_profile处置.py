#!/usr/bin/env python3
"""R62 profile 批量处置:退信标 + 补录邮箱"""
import glob, re

# (档案号, 文件路径, 邮箱, 退信原因, 替代建议)
BOUNCE = [
    ('A-170', 'einkauf@nitoit.de', 'not-found',
     '官网 https://nitoit.de 表单/Impressum 电话;电话先验证'),
    ('A-123', 'hbowerman@professionalcablingsolutions.com', 'not-found(46h|21h retry 后 Message not delivered)',
     '官网 professionalcablingsolutions.com 表单 +1 513 总机'),
    ('A-355', 'vartan@mikrotikls.com.ua', 'domain-not-found',
     '乌克兰守界:只标注;电话 +38 066 907 44 88 保留'),
    ('A-424', 'lima@wifiprofi.cz', 'not-found',
     '正确人名 klima@wifiprofi.cz(A-288 Krystof Klima 个人档);774 331 774'),
    ('A-434', 'sale@lanmarket.net', 'domain-not-found(.net 失效,正域 lanmarket.ua)',
     '乌克兰守界:只标注;电话 +380 50 666 78 58 保留'),
    ('A-439', 'molya@technotrade.com.ua', 'not-found',
     '乌克兰守界:只标注;电话 +380 57 764 02 54 保留'),
    ('A-458', 'info@cooltechtrading.com', 'not-found',
     '官网 cooltechtrading.com 表单;+90 542 883 1111'),
    ('A-476', 'info@wirelesslan.gr', 'not-found',
     '官网 wirelesslan.gr 表单;+30 2310 510030'),
    ('A-088', 'info@electromaster.ie', 'not-found(46h|20h retry 后 Message not delivered)',
     'Golden Pages 总机/官网表单'),
]

SUPP = [
    ('A-251', 'beszerzes@macsoft.hu', '用户 2026-10-04 官网查到(机构采购邮箱;与 A-250 Péter Major 同入口)'),
    ('A-258', 'biuro@csidet.edu.pl', '用户 2026-10-04 官网查到(机构邮箱非个人直邮;与 A-252 Kajetan Tadra 同入口)'),
    ('A-487', None, 'typo 修:nfo@marcomweb.it → info@marcomweb.it(用户 2026-10-04 官网核对)'),
    ('A-520', 'support@axbyte.se', '用户 2026-10-04 官网查询(同 A-064 Axbyte 入口,08-586 195 00 同总机,替代通道)'),
]

def find_profile(code):
    hits = glob.glob(f'profile/A/{code}-*.md')
    return hits[0] if hits else None

results = []
for code, email, reason, alt in BOUNCE:
    p = find_profile(code)
    if not p: results.append(f'{code}: profile not found'); continue
    raw = open(p, encoding='utf-8').read()
    tag = f'【已停用:2026-10-04 退信 {reason} 发不过去】'
    if tag not in raw:
        if email in raw:
            raw = raw.replace(email, email + tag, 1)
        else:
            raw += f'\n\n### R62 退信补档(2026-10-04)\n\n- **退信实测(2026-10-04)**:`{email}` {reason} Gmail 发不过去;不删邮箱只标;替代:{alt}\n'
    # 追加 R62 节
    if '### R62 退信' not in raw:
        raw += f'\n\n### R62 退信补档(2026-10-04)\n\n- **退信实测(2026-10-04)**:`{email}` Gmail 退回(**{reason}**);永久不可投递。规则:不删邮箱、只标「发不过去」+找替代路径;不主动群发重投该地址\n- **替代路径建议**:{alt}\n'
    open(p, 'w', encoding='utf-8').write(raw)
    results.append(f'{code}: ✓ tag + 补档节')

# A-337/A-342 备注型
for code, note in [
    ('A-337', '**退信实测(2026-10-04)**:`fabio.mundadori7114@ingesw.onmicrosoft.com` M365 tenant 域直邮被退(user not found);库内无此邮箱;**以后勿向 onmicrosoft.com 租户域猜测投递**(M365 自动生成域不等于企业域)。主邮箱 info@ingesw.com 未发不受影响'),
    ('A-342', '**退信观察(2026-10-04)**:`info@tnet.it` Gmail 临时退信(45h retry 中),非永久失败;等 48h 结果再定;若永久失败转正式退信处置'),
]:
    p = find_profile(code)
    if p:
        raw = open(p, encoding='utf-8').read()
        if '### R62 退信' not in raw:
            raw += f'\n\n### R62 退信补档(2026-10-04)\n\n- {note}\n'
            open(p, 'w', encoding='utf-8').write(raw)
        results.append(f'{code}: ✓ 备注节')

for code, email, note in SUPP:
    p = find_profile(code)
    if not p: results.append(f'{code}: profile not found'); continue
    raw = open(p, encoding='utf-8').read()
    if code == 'A-487':
        # typo 修复
        if 'nfo@marcomweb.it' in raw and 'info@marcomweb.it' not in raw:
            raw = raw.replace('nfo@marcomweb.it', 'info@marcomweb.it')
        raw += '\n\n### R62 邮箱修正(2026-10-04)\n\n- **typo 修**:nfo@marcomweb.it → **info@marcomweb.it**(用户官网核对缺首字母 i;原数据库录入源头已修)\n'
    elif email and email not in raw:
        raw += f'\n\n### R62 邮箱补录(2026-10-04)\n\n- **新增邮箱**:`{email}` — {note}\n'
    else:
        if email in raw:
            results.append(f'{code}: 已存在,跳过')
            continue
    open(p, 'w', encoding='utf-8').write(raw)
    results.append(f'{code}: ✓ 补录')

print('\n'.join(results))
