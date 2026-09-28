# AA Jones Electric Ltd

> **评级 A**　|　英国 · Hull / East Yorkshire　|　档案编号 `A-056`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-056
rating: A
country: 英国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — 主场景匹配+首触只推一个型号的纪律；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | AA Jones Electric Ltd（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Hull / East Yorkshire | 事实 |
| 网站 | aajones.co.uk | 事实 |
| 类型 | 分销（HMS/N-Tron·Red Lion 渠道） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | N-Tron + Red Lion + Anybus + Ixxat | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：N-Tron + Red Lion + Anybus + Ixxat）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@aajones.co.uk（既有/公开）
- **电话**：01482 589015
- **原始联系字段**：sales@aajones.co.uk；电话 01482 589015
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 PoE++（上架试销）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：电气批发商逻辑：24 口 PoE++ 是给安防/监控/WiFi 装好材料的同一单配套——低价格头部上架试用。
- **要问的问题**：你们店是否常做交换机类配套、低价位头上架愿意接哪种？
- **随附证明**：英文规格页 + 首入件价格表 + 备货单页。

### 第 2 次跟进 · 工业非管理 PoE（工厂/船舶柜外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：工厂自动化/船舶/危险区域柜外点位：宽温宽压、DIN、免配置，给他柜里加一个能讲得清的技术档。
- **要问的问题**：柜外设备里 PoE 供电用得怎样？
- **随附证明**：宽温报告 + DIN 安装图 + 台测试机。

### 第 3 次跟进 · 管理型 + 大库备货档

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：进库房常备档：管理型 PoE 作为上架可动销、退换/质保都明写的档位，接着谈店内常备库存规模。
- **要问的问题**：库房常备档的规格与质保条款怎么接？
- **随附证明**：管理型 ERPS/10G 实测（英文）+ 质保/退换承诺函 + 常备库存条款。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Hull 独立电气批发商（trade counter）+ 工业控制线：备货量大、现场交付快。
- **产品线与在售品牌**：电气/照明/安全信号/面板/工业控制全线 13,000+ 行，兼营 N-Tron/Red Lion 等 HMS 渠道工业网络线（CSV 既有名录验证记录）。
- **目标行业与场景**：工厂自动化/船舶/危险区域——面板柜以外的现场布线与监控供电点位。
- **团队与规模**：中型独立批商；销售+售后支持字为明牌。
- **决策链与对接人**：sales@aajones.co.uk / 01482 589015。
- **技术与认证**：工业电气批发代理体系。
- **采购与供应链信号**：批发商逻辑：低门槛开头单、看得到备货价值、续订单直进他库房。
- **近期动态与线索**：工业控制线正在扩大——他自己在备货面会带着上柜式交换机。
- **与我方契合点**：配电柜外的 PoE 连接段是他店里空白：低价位开头+店里全价格带，宽温工业款能在他综合柜里占座。
- **风险与注意**：批发者博价，但每次报价都拼“库存+促销位”——首信直接进价格档及对价。

### R54 原文证据摘录（全部保留）

- **【业务定位】**Hull 主营/独立电气批发商（trade counter），现场库房常年备货 30,000+ 项货。
  > As one of Hull's leading independent electrical wholesalers… we have over 30,000 items in stock at all times.
  > 来源：https://www.aajones.co.uk/
- **【产品线与在售品牌】**电气分销门类 13,000+ 行——工业自动化、船舶与防爆现场器材都在服务范围。
  > We stock over 13,000 lines of market leading electrical distribution solutions to complete your projects from start to finish.
  > 来源：https://www.aajones.co.uk/
- **【目标行业与场景】**自述专长现在转工业控制：工厂自动化面板、船业组件、危险区域设备——工业客层最密。
  > The company now specialises in controls for industry; supplying panel equipment for factory automation, components for the marine industry, hazardous area equipment.
  > 来源：https://www.aajones.co.uk/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（工业/楼宇），且有具体人直联
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
| 决策人识别 | ❓ |
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

**主题**：Rugged 8-port PoE for outdoor/unheated cabinets

```text
Hi AA,

I came across AA Jones Electric Ltd - 分销（HMS/N-Tron·Red Lion 渠道）.

We build an unmanaged industrial 8-port PoE switch (af/at) with 250m extended reach, redundant 44–57V DC input with reverse-polarity protection, DIN-rail mount and a 3-year warranty. Reference: $74.8 USD EXW.

One question: Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?

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
