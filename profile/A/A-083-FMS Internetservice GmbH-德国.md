# FMS Internetservice GmbH

> **评级 A**　|　德国 · Umkirch　|　档案编号 `A-083`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-083
rating: A
country: 德国
biz_org: 个体顾问（无官网）
business_model: 培训交付
decision_speed: fast
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: true}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE），三星重点
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 主场景匹配+首触只推一个型号的纪律；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | FMS Internetservice GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Umkirch | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 培训伙伴，开课/持证 MTCRE MTCSWE | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 培训伙伴，开课/持证 MTCRE MTCSWE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@fmsweb.de
  - 状态：既有/公开
- **电话**：—
- **原始联系字段**：info@fmsweb.de（Impressum 页；总经理 Patrick Schaub。⚠️**同时运营 mikrotik-shop.de**（MikroTik 网店）→ 直接竞品替代位）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 品类空缺补位（分销货架 Switche 价位段）

- **推什么**：STI-280GE（Saga） 系列 + STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他的 Switche 类目以 MikroTik 为主：高性价比工业 PoE+24 口万兆上行接入层是明显的价位空缺，先寄贸易样册（德语）。
- **要问的问题**：你们的 Switche 货架有没有考虑过 MikroTik 之外的第二品牌？
- **随附证明**：分销价目（德语）+ 同档对照 + 欧盟交付/RMA 说明。

### 第 2 次跟进 · 工业非管理 PoE（ISP 塔站/室外配套）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他服务 ISP 与无线链路客户：塔站/室外箱配套宽温 DIN PoE 与他 SAF/LigoWave 链路同柜台，组合销售。
- **要问的问题**：Richtfunk 客户塔站上的供电与交换现在配什么？
- **随附证明**：宽温报告 + 链路配套组合清单 + 备件包价。

### 第 3 次跟进 · 管理型 + MTCSWE 课实训机

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他开 MTCSWE 德语课：管理型（ERPS/VLAN/L3 卸载）进实训台做对照演示；分销+培训双通道合谈。
- **要问的问题**：MTCSWE 课的实训交换机够不够？要不要加一组对照机型？
- **随附证明**：实训机成本价 + 课程案例素材 + L3 卸载实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第5批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：德国弗莱堡旁的增值分销商（VAD）：ISP 设备+宽带建设+无线链路的德语区头部渠道之一，另有官方培训牌照（MTCSWE 德语课稀缺）。
- **产品线与在售品牌**：分销货架：MikroTik/LigoWave/SAF Tehnika/Nokia/AVM/eonyx + 机柜金工/电源/防雷配件；店内 Switche 为独立品类；自有培训业务。
- **目标行业与场景**：德语区 ISP、市政运营商、系统商客户群的接入/回传/热点建设；培训课程学员=渠道末端工程师。
- **团队与规模**：20+ 年公司化 VAD，自有物流仓储与技术支持团队（总经理 Patrick Schaub，CSV 记录）。
- **决策链与对接人**：info@fmsweb.de（Impressum 页）；采购/分销对口同一团队。
- **技术与认证**：MTCRE+MTCSWE 授课资质（官方培训伙伴，CSV 名录记录）；ISP 级宽带/无线链路工程背景。
- **采购与供应链信号**：VAD 自有物流+渠道网络：上架即覆盖德语区系统商；对「互补不内斗」的品牌持开放态度（货架已多品牌）。
- **近期动态与线索**：店内主推 CRS320-8P/CRS520 等交换新品——交换品类在加码；MTCSWE 课持续开（德语区稀缺供给）。
- **与我方契合点**：分销货架 Switche 类目高性价比补位+他 MTCSWE 课实训机双钩子；COM 类品牌与其现有货架互补（他卖荔枝波段无线、我们卖有线接入）。
- **风险与注意**：他是 MikroTik 深度渠道：首轮别替换思维，先问「货架缺什么价位段」；德语资料比英文更吃香。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：20+ 年 ITK（信息通信）老牌增值分销商，自有物流与技术企划能力。
  > FMS Internetservice GmbH – ITK Kompetenz seit über 20 Jahren. · Als „Value Added Distributor“ bieten wir unseren Kunden ein ausgesuchtes Herstellerportfolio, eigene Logistik und fundiertes Know-how in Planung, Betrieb und Support.
  > 来源：https://www.fmsweb.de/
- **【目标行业与场景】**客户群明确：ISP、市政公用事业（Stadtwerke）、系统商/IT 服务商等转售商，及公共部门客户。
  > Zu unseren Kunden zählen überwiegend Firmenkunden und öffentliche Auftraggeber, insbesondere Internet-Service-Provider, Stadtwerke und Wiederverkäufer wie Systemhäuser und IT-Dienstleister.
  > 来源：https://www.fmsweb.de/
- **【产品线与在售品牌】**自有网店 mikrotik-shop.de：除 MikroTik 外备授牌微波/毫米波链路、热点系统、测量仪、机柜金工——品类目录含 Switche 与 Training。
  > Neben den RouterBOARD und RouterOS Produkten von MikroTik führen wir ein ausgesuchtes Sortiment im Bereich Richtfunk, Access-Lösungen, Network-Appliances sowie dem entsprechenden Zubehör. · Produkte 目录含 DSLAMs und FTTx · Hotspotlösungen · Switche · Training；Hersteller：MikroTik · eonyx · SAF Tehnika · LigoWave · Nokia · AVM
  > 来源：https://www.mikrotik-shop.de/
- **【技术与认证】**MikroTik 官方培训伙伴：在 Umkirch 开 MTCRE 与 MTCSWE 德语班（来源性质：CSV 既有 MikroTik 官方名录记录）。
  > MikroTik 官方培训伙伴，开课/持证 MTCRE MTCSWE（CSV 信号列；名录页 JS 渲染，以既有记录为准）
  > 来源：https://mikrotik.com/consultants

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（交换认证 MTCSWE），三星重点
- **W**：一人/个体=单点与节奏风险；教师红线：不打学员名单、不经培训语境推销
- **O**：P1 场景切入（主场景匹配+首触只推一个型号的纪律）
- **T**：现有供应商惯性；价格竞争。

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 一人/个体=单点与节奏风险
- 教师红线：不打学员名单、不经培训语境推销

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

**主题**：8-port PoE with auto-recovery for your field deployments

```text
Hi FMS,

I came across FMS Internetservice GmbH - 集成商/顾问（MikroTik 认证）.

We build a compact 8-port Gigabit PoE switch (240W budget, af/at) with a hardware PoE watchdog that power-cycles a frozen AP or camera automatically, plus clean 802.1Q VLAN / ERPS / sFlow on the management side. Reference: $99 USD EXW.

One question: Which switch do you currently put on the bench for the VLAN/PoE lab demos?

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
