# 5Gstore

> **评级 A**　|　美国　|　档案编号 `A-268`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-268
rating: A
country: 美国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），三星重点
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — 5Gstore 美蜂窝电商大户（Teltonika 授权含 TSW212）：分支/IoT 部署 PoE 新窄口（$165 锚点一致）；TSW 旁前句；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | 5Gstore（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 | 事实 |
| 网站 | https://5gstore.com | 事实 |
| 类型 | 分销（Teltonika 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Teltonika Networks（含 TSW212 工业 PoE+ 交换机） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Teltonika Networks（含 TSW212 工业 PoE+ 交换机））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@5gstore.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：sales@5gstore.com（官网隐私页正文；未测试投递）；原入口：见 5gstore.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 交换类目价位档扩品一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：对 sales@：TSW212 之外的大口数商业 PoE 接入层电商上架提案（当日发可配合其节奏+梯价）。
- **要问的问题**：交换类目在 Teltonika 之外有没有大口数价位档上架位？
- **随附证明**：一页提案（英）+ 梯价表。

### 第 2 次跟进 · 车载/野外工业件窄线

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：车联/野外项目的宽温小件与收发器窄线（其蜂窝路由的 LAN 侧周边）。
- **要问的问题**：蜂窝项目的 LAN 侧宽温小件有货架位吗？
- **随附证明**：工业件一页（英）。

### 第 3 次跟进 · 供应商条款包

- **推什么**：—（条款）
- **切入点**：中性发货/梯价/RMA 条款包收口；不回即冻结。
- **要问的问题**：（无需回）条款留档。
- **随附证明**：供应商条款一页（英）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：芝加哥区蜂窝电商（Teltonika 授权+七大路由落地页）：其客群=车辆/野外/企业容灾——PoE 小件与工业件是邻位货架。
- **产品线与在售品牌**：蜂窝路由/天线/数据套餐；TSW212 工业 PoE+ 在架=已吃交换类目。
- **目标行业与场景**：车联/野外作业/企业容灾备份链路客群（评价点名报价快）。
- **团队与规模**：中型电商（工程师认证客服团）。
- **决策链与对接人**：sales@5gstore.com（隐私页正文，CSV 9-27）。
- **技术与认证**：Teltonika 授权分销（站+CSV 双证）。
- **采购与供应链信号**：蜂窝盒子配套的 LAN 侧接入件：TSW 之外的**大口数商业 PoE 与更低价工业件**两个价位档空档。
- **近期动态与线索**：评价滚动（2026 仍在更新）+当日发承诺=动销型渠道。
- **与我方契合点**：车载/现场套装旁的 24 口 PoE（营地监控/AP）与工业非管理件窄线。
- **风险与注意**：电商比价敏感：报价给到岸全款+阶梯；别碰其 Teltonika/Peplink 锚牌排位。

### R54 原文证据摘录（全部保留）

- **【业务定位】**伊利诺伊 Crystal Lake 的蜂窝联网电商：路由/天线/数据套餐/连接方案四线，自述美国本土获奖客服+大库存当日发+全员工程师认证。
  > Cellular Routers • Antennas • Data Plans • Connectivity Solutions ‖ Award Winning customer service (US based sales & support teams) ‖ Large inventory for Same Day error free shipping
  > 来源：https://5gstore.com/
- **【产品线与在售品牌】**路由落地页七家：Digi/Ericsson Cradlepoint/Inseego/Katalyst/Peplink/Semtech/**Teltonika**；天线八家 MobileMark/Panorama/PCTEL/Poynting/SureCall/Taoglas/weBoost/Wilson；**Teltonika TSW212 工业 PoE+ 交换机在架**（CSV 复核）。
  > Router Landing Pages — Digi · Ericsson Cradlepoint · Inseego · Katalyst · Peplink · Semtech · Teltonika ‖ （CSV 记录）亦供 TSW212 等工业 PoE+ 交换机
  > 来源：https://5gstore.com/
- **【决策链与对接人】**sales@5gstore.com 官网隐私页正文（CSV 9-27 official-company）；联系表单为第三方 Cognito 表单不显邮箱；Teltonika 分销栏目复核 authorized。
  > （CSV 2026-09-27 记录）官网隐私页正文 sales@5gstore.com 与 1-833-5GSTORE、Crystal Lake IL 地址；Teltonika 分销栏目页复核 authorized Teltonika Distributor；official-company
  > 来源：https://5gstore.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第27批.json`；价格均为 EXW 快照。

- **①背景再核**：US 蜂窝电商（官网+CSV 双核）
- **②芯片/型号**：Teltonika 线在墙
- **③KP 深挖**：sales@
- **④Saga 对标**：新窄口（$165 锚点一致）
- **⑤在乎与偏好**：现货/工程师支持

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**Cellular Routers•Antennas•Data Plans——Large inventory Same Day shipping;Teltonika 授权含 TSW212（CSV 9-23）
  > Cellular Routers•Antennas•Data Plans——Large inventory Same Day shipping;Teltonika 授权含 TSW212（CSV 9-23）
  > 来源：https://5gstore.com

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 5Gstore 美蜂窝电商大户（Teltonika 授权含 TSW212）：分支/IoT 部署 PoE 新窄口（$165 锚点一致）；TSW 旁前句 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：窄
- **O**：新口
- **T**：一线

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
  - [ ] 类目策略
  - [ ] 试单权

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi 5Gstore team,

Cellular routers, antennas, data plans - same-day shipping from US warehouses, engineer-certified support. Your switch shelf today is mostly Teltonika-class; the question is what happens when a branch deployment needs more PoE ports than that class gives.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29). It pairs naturally with the cellular edge devices you already sell - the LAN side of a branch or IoT rollout.

One question: would a documented value PoE switch earn a listing test beside your Teltonika line?

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
