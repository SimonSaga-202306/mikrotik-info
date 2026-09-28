# Charalampos Marinakis / SystemCon

> **评级 A**　|　希腊 · Heraklion（克里特）　|　档案编号 `A-021`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-021
rating: A
country: 希腊
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: true, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 主场景匹配+首触只推一个型号的纪律；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Charalampos Marinakis / SystemCon（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 希腊 / Heraklion（克里特） | 事实 |
| 网站 | systemcon.gr | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Charalampos Marinakis | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCINE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCINE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、万兆上行/骨干
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@systemcon.gr（既有/公开）
- **电话**：+30 281 121 7219
- **原始联系字段**：+30 281 121 7219 / info@systemcon.gr
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Charalampos Marinakis**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：按他「基础设施整体交付」的语境切入：监控/AP/门禁一次上 24 口 PoE++，把整机功率预算与看门狗写进他的交付清单，替代同档 MikroTik CRS328 / UniFi 的备选位。
- **要问的问题**：他现在的接入层订单里，24 口 PoE 一般谁供货、卡在价格还是交期？
- **随附证明**：整机功率实测表 + 看门狗演示 + 与 CRS328-24P/UniFi 的同规格对照页。

### 第 2 次跟进 · 工业级非管理 PoE（机房外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他做酒店、工厂、园区类客户时总有非机房点位：宽温宽压、DIN、免配置，坏了整机换。
- **要问的问题**：有没有现场弱电箱/室外点位需要工业设备？
- **随附证明**：宽温报告 + DIN 安装图 + 一台测试机。

### 第 3 次跟进 · 管理型 PoE（VLAN/冗余进方案）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他讲高可用与网络优化：VLAN 分段 + ERPS 环网 + 10G 上行的标准模板，让他的方案书多一点可写的东西。
- **要问的问题**：他的项目里监控/办公/门禁网段是分开的吗？
- **随附证明**：VLAN 模板 + ERPS 实测 + 招标可用参数条目。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：克里特岛的综合 IT 服务商（SystemCon）：企业智能 BI、ERP、系统基础设施与云，官网自述「Complete IT Business Solutions」。
- **产品线与在售品牌**：品牌墙含 MikroTik、Ubiquiti、Fortinet、Huawei Enterprise、Alcatel、Dell、Lenovo、Synology、Yeastar——网络设备以 MikroTik + Ubiquiti 为主，安全用 Fortinet。
- **目标行业与场景**：中小企业到企业级客户的基础设施建设：服务器/虚拟化、备份与容灾、网络优化、高可用、云迁移。
- **团队与规模**：克里特本地团队（站点为 Elementor 模板、部分文案仍是占位文本 → 正在改版），决策链短。
- **决策链与对接人**：Charalampos Marinakis（持 MTCNA+MTCINE）；info@systemcon.gr；+30 281 121 7219。
- **技术与认证**：MikroTik 认证顾问（MTCNA+MTCINE）；官网把「Routing/Switching、防火墙、Hotspot、VPN、负载均衡与故障切换、QoS」列为核心能力。
- **采购与供应链信号**：项目型采购（服务器+网络+云打包）；同时卖 MikroTik 与 Ubiquiti，说明他对「第三条补充线」不排斥，只要规格与价格说得清。
- **近期动态与线索**：官网 2025–2026 年持续更新（含 Fortinet/Huawei Enterprise 伙伴徽标），站点部分区块仍是模板占位文本——正在扩张服务目录。
- **与我方契合点**：他做基础设施整体交付：24 口 PoE（监控/AP/门禁）、工业款（机房外点位）与管理型（VLAN/冗余）都是他每单都会遇到的接入层；对 MikroTik 生态熟，参数对话成本低。
- **风险与注意**：站点改版未完成，别把占位文案当业务事实；Fortinet/Huawei 是既有关系方，谈接入层硬件不与其冲突。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网首页定位：综合 IT 业务方案（BI/ERP/基础设施）。
  > Complete IT Business Solutions — Tailored IT services to meet your organization's unique needs.；Our expertise spans Business Intelligence, Enterprise Resource Planning, Systems Infrastructure, and more
  > 来源：https://systemcon.gr/
- **【产品线与在售品牌】**品牌墙含 MikroTik、Ubiquiti、Fortinet、Huawei Enterprise、Alcatel、Dell、Lenovo、Synology、Yeastar。
  > （首页品牌徽标：microsoft-partner｜aws｜epsilonnet｜fortinet_partner｜huawei_enterprise_partner｜ubiquiti｜alcatel｜mikrotik｜dell｜lenovo｜yeastar｜synology）
  > 来源：https://systemcon.gr/
- **【技术与认证】**系统基础设施能力项明确列出网络优化、高可用、备份与容灾。
  > Systems Infrastructure — Robust Security｜High Availability｜Cloud Solutions｜Backup and Disaster Recovery｜Network Optimization
  > 来源：https://systemcon.gr/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（交换专长），且有具体人直联
- **W**：公开信息有限
- **O**：P1 场景切入（主场景匹配+首触只推一个型号的纪律）
- **T**：现有供应商惯性；价格竞争。

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：8-port PoE with auto-recovery for your field deployments

```text
Hi Charalampos,

I came across SystemCon - 集成商/顾问（MikroTik 认证）.

We build a compact 8-port Gigabit PoE switch (240W budget, af/at) with a hardware PoE watchdog that power-cycles a frozen AP or camera automatically, plus clean 802.1Q VLAN / ERPS / sFlow on the management side. Reference: $99 USD EXW.

One question: How many PoE ports does a typical site of yours need today?

If it is useful, I can send one unit for a 30-day evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

Best regards,
Saga Communications - PoE switch OEM/ODM (neutral packing available)
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
