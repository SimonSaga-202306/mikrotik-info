# Varia Group

> **评级 A**　|　德国 · Chemnitz　|　档案编号 `A-234`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-234
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — VARIA 德分销履约服务商（为品牌商做市直达+白标）：入册分销合作型对象（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Varia Group（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Chemnitz | 事实 |
| 网站 | https://www.varia.org | 事实 |
| 类型 | 分销（Netonix 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Netonix 授权渠道（WISP 接入层交换机） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】VARIA System GmbH（德国开姆尼茨，25年）：Distribution+E-Commerce+Fulfillment——为制造商/品牌做分销与市场直达（Amazon/eBay/Galaxus/Conrad/MediaMarkt），White Label 中性发货
- 【推断】制造商侧分销服务商=渠道合作型对象：等于问'愿不愿意把 Saga 线带进你仓'
- 【假设】其仓配+多 marketplace 上架机器，缺的是一条高周转网络件价值线

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Netonix 授权渠道（WISP 接入层交换机））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@varia.org
  - 状态：待核·未验证投递（不进群发）
- **电话**：+49-371-400-7682
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@varia.org（官网正文公开；未验证投递）；原入口：+49-371-400-7682
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 分销上架提案（接入层/CCTV 小件）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：向其分销口递交品牌上架提案：24 口 PoE 接入层+监控小件类目，分销条款+白标代发可选。
- **要问的问题**：你们现在接受新网络硬件品牌上架吗？走什么评估流程？
- **随附证明**：品牌一页提案（德/英）+ 分销条款模板。

### 第 2 次跟进 · 白标代发互补

- **推什么**：—（履约方案）
- **切入点**：按其白标服务条款：我们供货他们代发或反之，跑通跨境中性履约结构。
- **要问的问题**：白标代发的入仓/系统对接条件是什么？
- **随附证明**：履约流程一页 + 系统对接要点。

### 第 3 次跟进 · WISP 客群目录空档（工业宽温 PoE）

- **推什么**：STI-280GE（Saga） + 宽温收发器
- **切入点**：其 WISP 商户客户群目录里尚无工业宽温 PoE/收发器线——类目空档提案。
- **要问的问题**：户外/宽温件类目有上架空档吗？
- **随附证明**：类目对比一页 + CE 包。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第12批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Chemnitz 25 年分销运营体：用户裁决保留户（Vitesse 圈外标签在档）；分销/白标代发/多市场电商一体。
- **产品线与在售品牌**：分销服务（厂商品牌分销）+自有商城+市场代发+白标中性发货+定制系统集成。
- **目标行业与场景**：德/欧多市场电商渠道+B2B 分销网络。
- **团队与规模**：中型运营体（自有物流与流程系统）。
- **决策链与对接人**：info@varia.org（官网正文，CSV 9-27）；+49 371 400…。
- **技术与认证**：（分销职能型；CSV 9-23 用户裁决保留）。
- **采购与供应链信号**：**双向互补**：其分销/白标能力=Saga 类目的德国履约与上架渠道；其 WISP 商户客群缺工业 PoE 宽温线。
- **近期动态与线索**：官网 2026 版改版强调白标/履约=正在向品牌方卖履约能力——正合我们「你出货品我出品类」结构。
- **与我方契合点**：分销上架提案（接入层/CCTV 小件）+按其白标条款中性代发。
- **风险与注意**：Netonix/Vitesse 条目不谈替代（用户裁决保留在档）；只做其目录空档与履约互补。

### R54 原文证据摘录（全部保留）

- **【业务定位】**Chemnitz 25+ 年分销/电商/代发（Fulfillment & Dropshipping）：「我们搬运你的产品」。
  > Wir bewegen Ihre Produkte. Wir machen Ihre Produkte sichtbar, verfügbar und erfolgreich. Seit über 25 Jahren.
  > 来源：https://www.varia.org/
- **【产品线与在售品牌】****White Label Service：以你的名义中性发货**——中性货/白标是其能力项，与我方中性货打法结构同构。
  > White Label Service — Alle Sendungen erfolgen neutral in Ihrem Namen – ohne VARIA-Branding, mit Lieferscheinen und Verpackungen in Ihrer Markenidentität.
  > 来源：https://www.varia.org/
- **【目标行业与场景】**自有店铺+多市场直销（Amazon/eBay/Galaxus/Conrad/MediaMarkt/Kaufland），B2B&B2C 通吃。
  > Über eigene Shops und etablierte Marktplätze wie Amazon, eBay, Galaxus, Conrad, MediaMarkt oder Kaufland übernimmt VARIA die Direktvermarktung im B2B- und B2C-Bereich
  > 来源：https://www.varia.org/
- **【风险与注意】**CSV 裁决记录：其 Netonix 条目交换机为 Vitesse 芯片、严格按 Marvell 生态标准属圈外；用户 2026-09-23 明确「先这样」保留——本户只做互补、不谈生态归属。
  > （CSV 2026-09-23 用户裁决·保留）Netonix 交换机采用 Vitesse 芯片，并非 Marvell……用户明确保留
  > 来源：https://www.varia.org/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第24批.json`；价格均为 EXW 快照。

- **①背景再核**：DE 分销履约商（官网一手核）
- **②芯片/型号**：服务商非品牌
- **③KP 深挖**：info@
- **④Saga 对标**：入册分销（$165 锚点一致）
- **⑤在乎与偏好**：周转/接口/白标

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**VARIA übernimmt die Distribution für Hersteller und Marken…Direktvermarktung B2B & B2C über Amazon, eBay, Galaxus, Conrad, MediaMarkt；White Label
  > VARIA übernimmt die Distribution für Hersteller und Marken…Direktvermarktung B2B & B2C über Amazon, eBay, Galaxus, Conrad, MediaMarkt；White Label
  > 来源：https://www.varia.org

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：德国分销履约服务商（2000）
- **产品线与在售品牌**：为品牌商分销（无自有 IT 品牌墙）
- **目标行业与场景**：品牌商/电商/B2B-B2C 直达
- **团队与规模**：中型仓储团队
- **决策链与对接人**：info@ 口
- **技术与认证**：系统接口集成
- **采购与供应链信号**：入册/上架类合作
- **近期动态与线索**：白标中性发货叙事
- **与我方契合点**：入册分销合作（非普通销售）
- **风险与注意**：服务条款型对象——沟通=入册逻辑

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | VARIA 德分销履约服务商（为品牌商做市直达+白标）：入册分销合作型对象（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：上架机器
- **W**：非自营
- **O**：新线
- **T**：平台

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
  - [ ] 品类策略
  - [ ] 最低价条款

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi VARIA team,

You run distribution, fulfillment and marketplace go-to-market for manufacturers - Amazon, eBay, Galaxus, Conrad, MediaMarkt, white-label neutral shipping. That machinery is exactly what a hardware maker looks for.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29). A high-turnover value networking line, ready for listing, with stable replenishment behind it.

One question: do you take on new manufacturers in IT/networking categories - and what would onboarding of a PoE switch line look like on your side?

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
