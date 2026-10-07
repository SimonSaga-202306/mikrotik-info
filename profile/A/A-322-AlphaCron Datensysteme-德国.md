# AlphaCron Datensysteme

> **评级 A**　|　德国 · Apfelstädt　|　档案编号 `A-322`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-322
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — AlphaCron 德图林根系统屋（自有 DC+DSL/Funk 接入+汽车厂支持+LWL/监控）：自用+客户双角窄位（$180 锚点一致）；Marc Pauls 具名；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | AlphaCron Datensysteme（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Apfelstädt | 事实 |
| 网站 | https://www.alphacron.de | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】AlphaCron Datensysteme（德国 Apfelstädt/Erfurt 一带；Inhaber Marc Pauls）：IT 系统屋+**自有数据中心+DSL/Funknetz（自有接入网运营）**+24/7 监控+汽车厂系统支持（Volvo/VW…）+LWL 熔接+视频监控+VoIP；CSV=Allied Telesis Resell
- 【推断】系统屋兼接入网运营+自有 DC：其 Funknetz/DC/监控线自身消耗交换件+其客户现场件双线——中密窄位
- 【假设】自有 DC/接入与客户现场的 value 件双角

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：contact@alphacron.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：contact@alphacron.de（官网Impressum/隐私页）；036202/759994；Inhaber Marc Pauls；网络记录另有abuse@alphacron.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 车行/监控接入层一页

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：德语一封：车行网点与网基监控项目的 24 口 PoE 接入层（维保全包现场的 RMA 先行+分点复制梯价）。
- **要问的问题**：车行/监控项目的接入层目前由哪个牌供应？
- **随附证明**：一页报价（德）+ RMA 条款。

### 第 2 次跟进 · 自营机房互连配件

- **推什么**：DAC/AOC + SFP/SFP+ 目录
- **切入点**：Serverhousing/管理网的互连配件批量。
- **要问的问题**：机房互连配件走常备吗？
- **随附证明**：配件一页价卡+兼容表。

### 第 3 次跟进 · 站点宽温件

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：DSL/站间点位的宽温小件收口；不回即冻结。
- **要问的问题**：站点外置件有需求吗？
- **随附证明**：工业件一页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第17批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：图林根系统商+自营机房+小 ISP 混血（**本批首位**：车行系统线+机房互连+视频监控三线都吃件）。
- **产品线与在售品牌**：全谱系服务（虚拟化/VoIP/光纤熔接/卫星 BK/EPROM 编程等极宽）+自营 DC+DSL 接入。
- **目标行业与场景**：汽车经销集团网点+区域企业+里士多夫居民接入面。
- **团队与规模**：小型全能系统商（主理人 Marc Pauls）。
- **决策链与对接人**：contact@alphacron.de（Impressum，CSV 9-27）。
- **技术与认证**：IBM/HCL Business Partner、LANCOM Adv.（CSV 记录）。
- **采购与供应链信号**：**三位**：车行网点的监控/办公接入层 24 口 PoE+自营机房管理网与互连 DAC/SFP+站点外置宽温件。
- **近期动态与线索**：Erfurt Herrenberg 新 VDSL 区放装=住客接入扩张季。
- **与我方契合点**：24 口 PoE（车行/监控）+DAC/SFP（机房）+工业件（站点）。
- **风险与注意**：个人店口径：德语资料+小批梯价+真实参数。

### R54 原文证据摘录（全部保留）

- **【业务定位】**图林根 Apfelstädt 的 IT 系统商**连自营数据中心**：24/7 监控、Serverhousing、DSL/VDSL 接入（固定 IP/IPv6 双栈）、光纤熔接、站间互联——**系统商+小 ISP 混血**。
  > IT-Systemhaus mit angeschlossenem Rechenzentrum ‖ 24/7 Monitoring von IT-Infrastrukturen mit aktivem Incident-Management ‖ DSL Zugänge mit festen IP-Adressen ‖ Standleitungen · Standortvernetzung (VPN, MPLS)
  > 来源：https://www.alphacron.de/
- **【目标行业与场景】****汽车经销商全线系统运维**（Volvo/VW/Audi/Skoda/Seat/Nissan/Renault/Dacia 网点）+**网基视频监控（netzwerkbasierte Videoüberwachung）**——24 口监控 PoE 与车行接入层的真消耗。
  > gesamte Systembetreuung im Automotive-Umfeld (Volvo, VW, Audi, Skoda, Seat, Nissan, Renault, Dacia) ‖ netzwerkbasierte Videoüberwachung
  > 来源：https://www.alphacron.de/
- **【决策链与对接人】**contact@alphacron.de（Impressum 正文 Inh. Marc Pauls，CSV 9-27 official-company）；036202/759994。
  > AlphaCron Datensysteme · Inh. Marc Pauls · Wandersleber Straße 1a, 99192 Apfelstädt · Tel.: 036202 / 759994 · eMail: contact@alphacron.de
  > 来源：https://www.alphacron.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第33批.json`；价格均为 EXW 快照。

- **①背景再核**：DE 系统屋+运营（官网一手核）
- **②芯片/型号**：AT Resell
- **③KP 深挖**：contact@（Pauls）
- **④Saga 对标**：双角（$180 锚点一致）
- **⑤在乎与偏好**：小而全/光纤工艺

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**IT-Systemhaus mit angeschlossenem Rechenzentrum…DSL Zugänge/Standortvernetzung/netzwerkbasierte Videoüberwachung/LWL Spleißarbeiten；Inh. Marc Pauls
  > IT-Systemhaus mit angeschlossenem Rechenzentrum…DSL Zugänge/Standortvernetzung/netzwerkbasierte Videoüberwachung/LWL Spleißarbeiten；Inh. Marc Pauls
  > 来源：https://www.alphacron.de

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：德国图林根系统屋（自有 DC+接入）
- **产品线与在售品牌**：AT Resell（CSV）+多牌
- **目标行业与场景**：区域企业+汽车配套
- **团队与规模**：小团
- **决策链与对接人**：contact@（Marc Pauls 具名）
- **技术与认证**：—
- **采购与供应链信号**：自用件+随单
- **近期动态与线索**：DSL/Funk 网 IPv6 native
- **与我方契合点**：自用+客户双角窄位
- **风险与注意**：个体运营——低中密度

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | AlphaCron 德图林根系统屋（自有 DC+DSL/Funk 接入+汽车厂支持+LWL/监控）：自用+客户双角窄位（$180 锚点一致）；Marc Pauls 具名 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：双角
- **W**：小
- **O**：双路
- **T**：—

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
| 决策人识别 | ❓ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 现供
  - [ ] 体况

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hallo AlphaCron team,

A system house with its own datacenter, DSL/Funk access lines, LWL splicing and network video on top - you are one of the few small houses that both operates infrastructure and installs it.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW (2026-09-29) - for your own racks and access nodes, and for customer sites alongside.

One question: where does switching for your own infrastructure and customer installs come from today?

Best regards,
Saga Telecom - PoE switch OEM/ODM
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
