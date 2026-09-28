# Neobits

> **评级 A**　|　美国 · California　|　档案编号 `A-276`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-276
rating: A
country: 美国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: true, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — 主场景匹配+首触只推一个型号的纪律；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Neobits（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / California | 事实 |
| 网站 | https://www.neobits.com | 事实 |
| 类型 | WISP 集成商/代理（Netonix） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Netonix 授权渠道（WISP 接入层交换机） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Netonix 授权渠道（WISP 接入层交换机））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@neobits.com
  - 状态：既有/公开
- **电话**：1-866-636-2487
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：sales@neobits.com（官网联系页正文；未测试投递）；供应商入口：vendors@neobits.com；原入口：1-866-636-2487
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · vendors@ 供应商入驻一页（SKU 包）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）
- **切入点**：对 vendors@：供应商入驻提案——24 口 PoE++ 接入层（SKU 资料包：UPC/规格图/比价表/梯价/代发条款一体）。
- **要问的问题**：网络交换类目接受新供应商入驻吗？需要什么资料？
- **随附证明**：SKU 上架资料包（英）。

### 第 2 次跟进 · 工业窄线 SKU

- **推什么**：STI-280GE（Saga） 等窄线
- **切入点**：基站基础设施类目的工业宽温件窄线 SKU 包。
- **要问的问题**：工业类目的宽温件窄线要上架吗？
- **随附证明**：窄线 SKU 包。

### 第 3 次跟进 · 条款收口

- **推什么**：—（条款）
- **切入点**：代发/批发条款收口；不回即冻结。
- **要问的问题**：（无需回）条款留档。
- **随附证明**：条款一页（英）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：加州 B2B 大卖场（基站基础设施是头部类目）——按**供应商入驻**逻辑走 vendors@，别的户都是对客推销、这户是上架。
- **产品线与在售品牌**：万货电商+基站件/监控件类目；Netonix 渠道（CSV）。
- **目标行业与场景**：全美 SMB/机构买家（长尾动销）。
- **团队与规模**：大型电商后台（Item#/MPN/UPC 体系完整）。
- **决策链与对接人**：vendors@neobits.com（供应商入口，CSV 9-27）；sales@ 客服线。
- **技术与认证**：Netonix 授权渠道（CSV；Vitesse 圈外标签在档）。
- **采购与供应链信号**：**SKU 化供货商逻辑**：24 口 PoE/工业件按 UPC/MPN 上架资料包直达 vendors@（比测量/梯价/代发一体）。
- **近期动态与线索**：海量 SKU 持续在册=长尾类目常年扩。
- **与我方契合点**：24 口 PoE 上架 SKU 包+工业件窄线。
- **风险与注意**：Netonix 用户裁决保留户：绝不提芯片；不与客服线谈合作（只走 vendors@）。

### R54 原文证据摘录（全部保留）

- **【业务定位】**加州 B2B 百货级电商「where business goes shopping」：类目录从标签打印机到色谱膜——其中**基站基础设施/基站天线/视频监控系统**为头部类目（Netonix 渠道身份 CSV 9-23 用户裁决保留户）。
  > Neobits.com is where business goes shopping. ‖ Top Categories — Base Station Infrastructure · Base Station Antennas · Video Surveillance Systems
  > 来源：https://www.neobits.com/
- **【采购与供应链信号】**货架含 NewMar DIN 轨 DC UPS 等工业件（在库标价直出）=工业/基站供电件已在动销；**vendors@neobits.com 为供应商入口**（CSV 9-27）——我们按「供应商入驻」而非「客户推销」逻辑走。
  > NewMar - DIN-UPS 24-20 - DIN rail mount DC UPS Power System ‖ （CSV 2026-09-27 记录）官网联系页正文 sales@；供应商入口 vendors@neobits.com
  > 来源：https://www.neobits.com/
- **【风险与注意】**【2026-09-23 用户裁决·保留】Netonix 采用 Vitesse 芯片、非 Marvell，严格标准属圈外；用户明确保留——**禁用「同芯片」话术**，切入只放交期/宽温/上行/价格。
  > （CSV 2026-09-23 用户裁决）Netonix=非 Marvell 圈外，「先这样吧，没必要删」；切入应放在交期、宽温、上行与价格上
  > 来源：https://www.neobits.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
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

**主题**：24-port PoE + 10G uplinks for your larger sites

```text
Hi Neobits,

I came across Neobits - WISP 集成商/代理（Netonix）.

We build a 24-port Gigabit PoE switch (280W, af/at) with 4×10G SFP+ uplinks, Voice VLAN and a hardware PoE watchdog that reboots hung APs/cameras without a site visit. Reference: $165 USD EXW.

One question: Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?

If it is useful, I can send one unit for a 30-day evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)
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
