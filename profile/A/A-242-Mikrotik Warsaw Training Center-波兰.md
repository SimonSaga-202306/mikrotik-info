# Mikrotik Warsaw Training Center

> **评级 A**　|　波兰 · Warsaw　|　档案编号 `A-242`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-242
rating: A
country: 波兰
biz_org: 公司/工作室（有官网）
business_model: 培训交付
decision_speed: moderate
price_sensitivity: medium
volume_potential: 2  # 1-5
needs: {poe: true, industrial: false, tenG: true, l2plus: true, voice: true, oem: false, hotel: false, training: true}
p1: CONSULT-OEM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE），且有具体人直联
- **P1（首触唯一主推）**：OEM/白牌合作探询（无量产型号首推） — MWTC 华沙多厂商认证培训（MikroTik/Zabbix/UniFi+轻实施）：对照单元+wdrożenia 窄位双角（$180 锚点一致）；—（合作探询，无量产报价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Mikrotik Warsaw Training Center（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 波兰 / Warsaw | 事实 |
| 网站 | https://mwtc.pl | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证培训伙伴，持 MTCNA MTCRE MTCWE MTCTCE MTCUME MTCINE MTCIPv6E MTCSE MTCSWE MTCEWE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Mikrotik Warsaw Training Center:MikroTik Warsaw Training Center(MWTC)(波兰 Warszawa,ul. Ogrodowa 58(4 楼),00-876;**NIP 1132330628;2016 创;2-10 人;波兰最大 MikroTik 培训中心(官方全证谱 MTCNA..MTCUME+Zabbix ZCS/ZCP/ZCE 双证;UE/PARP/KFS 资助课;Proxmox/Windows 副谱)**;**官网 Trainers 页全谱:Michał Filipek(MikroTik+Zabbix+Ubiquiti 三证师)+Piotr Wasyk(**Właściciel 业主**,华沙理工 2004 入行;PARP BUR 件)+Ihor Hreskiv(塔尔诺波尔工大;MBUM/MUM 2019 演讲谱)+Iwona Wasyk(Frontend 族谱)**
- 【推断】R66 第 20 波具名 KP 金谱
- 【假设】24 口 value PoE($180 USD EXW (2026-10-07, 15天有效))具名谱位引路

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证培训伙伴，持 MTCNA MTCRE MTCWE MTCTCE MTCUME MTCINE MTCIPv6E MTCSE MTCSWE MTCEWE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@mwtc.pl
  - 状态：既有/公开
- **电话**：+48 796 171 971
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@mwtc.pl（官网正文公开）；原入口：+48 796 171 971；Michał：michal@mwtc.pl；Piotr：piotr@mwtc.pl（均官网正文）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Piotr Wasyk**(Network Architect/Trener/**Właściciel**(业主;官网教练页+RR+PARP 件三源))— mwtc.pl/aboutUs.php+RR 双源 〔已有(公司官方公开件/登记册自曝);源:https://mwtc.pl/aboutUs.php〕
  - **Michał Filipek**(Network Architect/MikroTik+Zabbix+Ubiquiti Trainer(三证教练))— mwtc.pl 教练页(O) 〔已有(公司官方公开件/登记册自曝);源:https://mwtc.pl/aboutUs.php〕
  - **Ihor Hreskiv**(Certified MikroTik Trainer(乌克兰谱;MUM 2019 演讲者))— mwtc.pl 教练页(O) 〔已有(公司官方公开件/登记册自曝);源:https://mwtc.pl/aboutUs.php〕
  - **Iwona Wasyk**(Frontend Developer(族谱))— LinkedIn 公司页员工谱 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://pl.linkedin.com/company/mikrotik-warsaw-training-center〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Piotr Wasyk | Network Architect/Trener/**Właściciel**(业主;官网教练页+RR+PARP 件三源) | mwtc.pl/aboutUs.php+RR 双源 | official-self-published·谱/leads-only(直发需 opt-in) | https://mwtc.pl/aboutUs.php |
| Michał Filipek | Network Architect/MikroTik+Zabbix+Ubiquiti Trainer(三证教练) | mwtc.pl 教练页(O) | official-self-published·谱/leads-only(直发需 opt-in) | https://mwtc.pl/aboutUs.php |
| Ihor Hreskiv | Certified MikroTik Trainer(乌克兰谱;MUM 2019 演讲者) | mwtc.pl 教练页(O) | official-self-published·谱/leads-only(直发需 opt-in) | https://mwtc.pl/aboutUs.php |
| Iwona Wasyk | Frontend Developer(族谱) | LinkedIn 公司页员工谱 | leads-only·待 opt-in(LinkedIn/谱面带核) | https://pl.linkedin.com/company/mikrotik-warsaw-training-center |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（OEM/白牌合作探询（无量产型号首推）），备选型不进邮件。

### 第 1 次跟进 · 实施线接入层第二来源+MTCSWE 实验室演示机

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+，演示机可选）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：两路邀：给实施团队的接入层第二来源价卡（波兰语）；为 MTCSWE 交换课留一台演示机跑真机实验。
- **要问的问题**：实施项目的接入层有第二来源位吗？MTCSWE 课需要 24 口 PoE 演示机吗？
- **随附证明**：波兰语一页价卡 + 演示机条款。

### 第 2 次跟进 · 客户现场宽温小件

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光）
- **切入点**：其部署/support 线的现场级宽温小件与 LoRa 项目旁位。
- **要问的问题**：客户现场有厂房/户外宽温环境吗？
- **随附证明**：宽温件一页 + CE。

### 第 3 次跟进 · 价卡留档收口

- **推什么**：—（价卡留档）
- **切入点**：全品类价卡留档、培训业务互不打扰；无回复即冻结。
- **要问的问题**：（无需回）价卡留档，以后按项目报。
- **随附证明**：全品类一页价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第13批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：华沙三地点 MikroTik 官方培训中心（M.Filipek/P.Wasyk/I.Hreskiv，CSV 记 MTCSWE）——**培训+实施双业态**。
- **产品线与在售品牌**：MikroTik 官方全课+Zabbix+Ubiquiti 官方认证课+自研 Linux/Proxmox/VoIP/LoRa/Grafana。
- **目标行业与场景**：波兰 IT 管理员学员群；其实施线承接基础设施项目。
- **团队与规模**：中型培训实施一体（三地点+上门专场）。
- **决策链与对接人**：info@mwtc.pl（官网正文，CSV 9-27）；+48 796…。
- **技术与认证**：MikroTik 官方培训中心资质；MTCSWE 在持（CSV）。
- **采购与供应链信号**：实施线（Wdrożenia）=真实拿件口；实验室真机环境=演示件位（真机上做 MTCSWE 交换课）。
- **近期动态与线索**：课程矩阵蔓延到 Proxmox/Grafana/LoRa=客户群从网管扩到运维全栈。
- **与我方契合点**：实施项目的接入层第二来源+MTCSWE 交换课实验室演示机。
- **风险与注意**：dofinansowanie 公共资金补贴课面不经由我们；尊重教师身份，不向学员名单推销。

### R54 原文证据摘录（全部保留）

- **【业务定位】**华沙官方 MikroTik 培训中心+多品牌认证课（Zabbix/Ubiquiti 官方）与自研课（Linux/Proxmox/VoIP/LoRa/Grafana），**另有基础设施审计/实施/支持/咨询业务线**（不止培训）。
  > Certyfikowane szkolenia MikroTik | Zabbix | Ubiquiti ‖ Audyty infrastruktury · Wdrożenia · Wsparcie · Doradztwo
  > 来源：https://mwtc.pl/
- **【团队与规模】**三地点（华沙中心/波兹南/琴斯托霍瓦），认证教练+工程师团队；可上门专场课。
  > Doświadczona kadra certyfikowanych trenerów i inżynierów · Lokalizacje - centrum Warszawy, Poznań, Częstochowa · Szkolenia dedykowane w siedzibie Klienta
  > 来源：https://mwtc.pl/
- **【风险与注意】**主页明示「Możliwość dofinansowania do 100%」（可获公共资金补贴至 100%）——补贴课渠道对应公共资金面，该面划出不涉、只走商业实施/实验硬件线。
  > Możliwość dofinansowania do 100%
  > 来源：https://mwtc.pl/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-10-08_R66_R56_KP第20波50户.json`；价格均为 EXW 快照。

- **①背景再核**：MikroTik Warsaw Training Center(MWTC)(波兰 Warszawa,ul. Ogrodowa 58(4 楼),00-876;**NIP 1132330628;2016 创;2-10 人;波兰最大 MikroTik 培训中心(官方全证谱 MTCNA..MTCUME+Zabbix ZCS/ZCP/ZCE 双证;UE/PARP/KFS 资助课;Proxmox/Windows 副谱)**;**官网 Trainers 页全谱:Michał Filipek(MikroTik+Zabbix+Ubiquiti 三证师)+Piotr Wasyk(**Właściciel 业主**,华沙理工 2004 入行;PARP BUR 件)+Ihor Hreskiv(塔尔诺波尔工大;MBUM/MUM 2019 演讲谱)+Iwona Wasyk(Frontend 族谱)**
- **②芯片/型号**：(待谱面二补)
- **③KP 深挖**：**Piotr Wasyk(Network Architect/Trener/**Właściciel**(业主;官网教练页+RR+PARP 件三源),official-self-published·谱/leads-only(直发需 opt-in));Michał Filipek(Network Architect/MikroTik+Zabbix+Ubiquiti Trainer(三证教练),official-self-published·谱/leads-only(直发需 opt-in));Ihor Hreskiv(Certified MikroTik Trainer(乌克兰谱;MUM 2019 演讲者),official-self-published·谱/leads-only(直发需 opt-in));Iwona Wasyk(Frontend Developer(族谱),leads-only·待 opt-in(LinkedIn/谱面带核))**
- **④Saga 对标**：24 口 value PoE($180 USD EXW (2026-10-07, 15天有效))
- **⑤在乎与偏好**：培训中心谱=课程对照单元窗

### R55 证据摘录（全部保留 · 含数量）

- **【决策链与对接人】**Trainers: Michał Filipek(Zabbix/MikroTik/Ubiquiti Trainer 全证);Piotr Wasyk(Właściciel;MikroTik+Ubiquiti Trainer;Pw BM 2004 起);Ihor Hreskiv(MikroTik Trainer;MBUM/MUM 演讲谱);Iwona Wasyk Frontend(mwtc.pl 教练页自署+LI/RR/PARP BUR 件)
  > Trainers: Michał Filipek(Zabbix/MikroTik/Ubiquiti Trainer 全证);Piotr Wasyk(Właściciel;MikroTik+Ubiquiti Trainer;Pw BM 2004 起);Ihor Hreskiv(MikroTik Trainer;MBUM/MUM 演讲谱);Iwona Wasyk Frontend(mwtc.pl 教练页自署+LI/RR/PARP BUR 件)
  > 来源：https://mwtc.pl/aboutUs.php
- **【联系方式与基础画像】**Ogrodowa 58, 00-876 Warszawa(Wola);NIP 1132330628;+48 796 171 971;info@mwtc.pl;**największe centrum szkoleniowe MikroTik w Polsce**;MTCNA/MTCRE/MTCSE/MTCWE/MTCTCE/MTCIPv6E/MTCSWE/MTCEWE/MTCUME/MTCINE 全证;UE/PARP/KFS dofinansowanie(schoolandcollege/LI/PARP 件)
  > Ogrodowa 58, 00-876 Warszawa(Wola);NIP 1132330628;+48 796 171 971;info@mwtc.pl;**największe centrum szkoleniowe MikroTik w Polsce**;MTCNA/MTCRE/MTCSE/MTCWE/MTCTCE/MTCIPv6E/MTCSWE/MTCEWE/MTCUME/MTCINE 全证;UE/PARP/KFS dofinansowanie(schoolandcollege/LI/PARP 件)
  > 来源：https://pl.linkedin.com/company/mikrotik-warsaw-training-center

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：MikroTik Warsaw Training Center(MWTC)(波兰 Warszawa,ul. Ogrodowa 58(4 楼),00-876;**NIP 1132330628;2016 创;2-10 人;波兰最大 MikroTik 培训中心(官方全证谱 MTCNA..MTCUME+Zabbix ZCS/ZCP/ZCE 双证;UE/PARP/KFS 资助课;Proxmox/Windows 副谱)**;**官网 Trainers 页全谱:Michał Filipek(MikroTik+Zabbix+Ubiquiti 三证师)+Piotr Wasyk(**Właściciel 业主**,华沙理工 2004 入行;PARP BUR 件)+Ihor Hreskiv(塔尔诺波尔工大;MBUM/MUM 2019 演讲谱)+Iwona Wasyk(Frontend 族谱)**
- **产品线与在售品牌**：(波次二补谱面)
- **目标行业与场景**：波兰华沙最大 MikroTik 培训中心
- **团队与规模**：2-10 人;2016 创
- **决策链与对接人**：**Piotr Wasyk(Network Architect/Trener/**Właściciel**(业主;官网教练页+RR+PARP 件三源),official-self-published·谱/leads-only(直发需 opt-in));Michał Filipek(Network Architect/MikroTik+Zabbix+Ubiquiti Trainer(三证教练),official-self-published·谱/leads-only(直发需 opt-in));Ihor Hreskiv(Certified MikroTik Trainer(乌克兰谱;MUM 2019 演讲者),official-self-published·谱/leads-only(直发需 opt-in));Iwona Wasyk(Frontend Developer(族谱),leads-only·待 opt-in(LinkedIn/谱面带核))**
- **技术与认证**：(波次二补)
- **采购与供应链信号**：(波次二补)
- **近期动态与线索**：2026-10-08 R66 20 波谱名牌
- **与我方契合点**：24 口 value PoE 谱链窗口
- **风险与注意**：Wasyk 业主+Filipek 教练位(opt-in 律;OEM 探询)

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | OEM/白牌合作探询（无量产型号首推） | 主场景 | —（合作探询，无量产报价） | MWTC 华沙多厂商认证培训（MikroTik/Zabbix/UniFi+轻实施）：对照单元+wdrożenia 窄位双角（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424XGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：OEM/白牌合作：中性包装、贴客户型号、ODM 规格，MOQ 与认证另谈
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：培训中心谱=课程对照单元窗
- **W**：培训谱
- **O**：Wasyk 业主直达位
- **T**：MikroTik 官方课链

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 教师红线：不打学员名单、不经培训语境推销

**停止开发条件（命中任一即停）**：3 次定向触达无任何实质回复；确认现用平台完全满足需求；只愿比价不愿谈场景；决策者确认接触不到；对方书面拒绝。

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（PoE/接入层池） | ✅ |
| 决策人识别 | ✅ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 硬件采购线在职者(波次二)
  - [ ] MikroTik 谱面份额

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Szanowny Panie Wasyk,

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-07, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?

Best regards,
Saga Networks Export Desk
```

> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；③ 落款换成你自己的名字与公司；④ **一次只问一个问题**；⑤ 货币单位一律 USD 并带快照日期；⑥ 该客户为教师/公立身份时先读「本户特别红线」。

## 跟进记录

| 日期 | 渠道（邮件/电话/LinkedIn/展会） | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 首次触达前留空；发出邮件后填入日期与渠道。有新进展时告诉我，我来更新本档案并重评 stage。

## 下次复核

- 固定节点：首触发出后 **14 天**无回复 → 复核是否降频/降级；有任何回复 → 当即重评 stage 与评级。
- 报价纪律：全部价格为 USD EXW 快照（2026-09-28，15 天有效）；过窗先核价再报价。

---

*建档日期：2026-09-22　|　结构 v2：2026-09-28（R56 规则）　|　数据来源：客户名单_反向信号_2026-09.csv + R54/R55 调研 JSON*
