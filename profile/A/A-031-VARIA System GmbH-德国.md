# VARIA System GmbH

> **评级 A**　|　德国　|　档案编号 `A-031`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-031
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
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
| 名称 | VARIA System GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 | 事实 |
| 网站 | varia-store.com | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Master+VAD） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik（Master+VAD））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：shop@varia-store.com
  - 状态：既有/公开
- **电话**：+49 371 33716890
- **原始联系字段**：+49 371 33716890 / shop@varia-store.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：上架试销：对比他货架上的 MikroTik CRS328-24P 与 Ubiquiti 24 口 PoE，给一档「功率更大、价格更低」的价位补缺；先谈样品与首批小单。
- **要问的问题**：他愿意先上 1–2 个 SKU 试销，还是先做项目配套？
- **随附证明**：上架用中英文规格/图片包 + 首批档位价 + 退货/售后条款。

### 第 2 次跟进 · 工业级非管理 PoE（工业货架补缺）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他已有 MOXA/Teltonika 工业线 → 工业交换机以「宽温 DIN 价位段补缺」进目录，配 MOXA/Teltonika 客户群卖。
- **要问的问题**：他工业货架的客户最常问的交换机规格是什么？
- **随附证明**：同规格对照表（MOXA/Teltonika/我们）+ 认证文件包 + 样品。

### 第 3 次跟进 · 管理型 PoE（项目配套与光模块组合）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：项目型客户（园区/监控/工业）需要管理型 + 光模块：给组合清单（交换机 + SFP 模块 + 配件），提高客单价。
- **要问的问题**：他的项目客户里，管理型交换机的询盘多不多？
- **随附证明**：组合报价模板 + 光模块兼容清单 + ERPS/组播实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：开姆尼茨的官方分销商网店 VARIA System GmbH（varia-store.com）：面向德国与欧盟客户销售网络与工业 IoT 硬件，含 24/7 报价服务、发票购买、国际 DHL 配送。
- **产品线与在售品牌**：自述为官方分销：**MikroTik、Ubiquiti/UniFi、Teltonika、Delock、TP-Link、Deciso、MOXA**、ICY BOX 等；货架同时有工业件（MOXA AG101、Teltonika FMB 车联网、MikroTik KNOT LR9G LoRaWAN 网关）。
- **目标行业与场景**：德国中小企业、系统集成商、工业/IoT 项目（Chemnitz 工业区）、终端 IT 采购；支持发票采购与 14 天退货。
- **团队与规模**：中小型网店/分销团队（站点为 WooCommerce + 多语言），决策链短（shop@varia-store.com 即采购/上架口）。
- **决策链与对接人**：shop@varia-store.com；+49 371 33716890（Chemnitz）。
- **技术与认证**：官方分销身份（多品牌）；未见公开认证列表。
- **采购与供应链信号**：典型网店分销：新 SKU 看「能不能上架卖 + 供货稳定 + 退货率」；对中性品牌接受度高（货架已有 Deciso、MOXA、Teltonika 等）。
- **近期动态与线索**：2026 年站点在推 Teltonika 5G、Ubiquiti U-AirWire、MikroTik KNOT LR9G、MOXA AIG-101 等新货——持续上新品。
- **与我方契合点**：他要的是货架丰富度与毛利：24 口 PoE（商用热销）、工业 8 口（AO 工业线在架）与光模块/配件组合，可直接进他的目录做差异化价位段。
- **风险与注意**：网店分销 ≠ 大货：先用 1–2 个 SKU 试销看动销；他已有 MOXA/Teltonika 工业线，工业款以「价位段补缺」进入。

### R54 原文证据摘录（全部保留）

- **【产品线与在售品牌】**首页品牌区与在架工业件（官方分销定位）。
  > Marken Highlights：Ubiquiti, UNIFI, MikroTik, Teltonika, Delock, TP-Link, Deciso｜在架示例：Mikrotik KNOT LR9G kit、MOXA AIG 101、Teltonika FMB
  > 来源：https://www.varia-store.com/
- **【采购与供应链信号】**网店服务条款（对供应商意味着低退货要求与稳定供货）。
  > Kauf auf Rechnung｜Bonuspunkte sammeln｜Angebotsservice 24/7｜Internationaler Versand (DHL)｜14 Tage Rückgaberecht｜Sichere Kaufabwicklung
  > 来源：https://www.varia-store.com/

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
Hi VARIA,

I came across VARIA System GmbH - 分销（MikroTik 官方）.

We build an unmanaged industrial 8-port PoE switch (af/at) with 250m extended reach, redundant 44–57V DC input with reverse-polarity protection, DIN-rail mount and a 3-year warranty. Reference: $74.8 USD EXW.

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
