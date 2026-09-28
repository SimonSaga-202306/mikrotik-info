# Aikom Technology

> **评级 A**　|　意大利 · Riccione (RN)　|　档案编号 `A-032`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-032
rating: A
country: 意大利
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
- **为什么值得跟**：有明确交换/供电需求（交换专长、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — 主场景匹配+首触只推一个型号的纪律；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Aikom Technology（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Riccione (RN) | 事实 |
| 网站 | aikomtech.com | 事实 |
| 类型 | 分销（Teltonika Gold + ComNet 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Teltonika, ComNet | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Teltonika, ComNet）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@aikomtech.com（既有/公开）
- **电话**：+39 0541 648894
- **原始联系字段**：info@aikomtech.com；电话 +39 0541 648894
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：进 AikomGo 目录：对标他 Wi-Fi & Networking 板块的 24 口 PoE 档，给渠道价与文档包（datasheet/认证/图片），让他先上架再看动销。
- **要问的问题**：他们的目录里 24 口 PoE 目前有几个价位段、缺哪一档？
- **随附证明**：上架资料包 + 渠道价目 + 与他现售型号的对照表。

### 第 2 次跟进 · 工业级非管理 PoE（Broadband/工业安防项目）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他的 Broadband 板块服务 WISP/ISP/MSP：塔站/室外箱用宽温 DIN 款；安防项目里的危险/室外点位同样适用。
- **要问的问题**：WISP/ISP 渠道客户最缺哪一档工业交换设备？
- **随附证明**：宽温报告 + SFP 兼容清单 + 样机。

### 第 3 次跟进 · 管理型 PoE（活动演示 + 项目型）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：把管理型交换机放进 Connectivity Camp 之类的活动做「VLAN/环网/组播」现场演示；渠道活动带单，项目同款跟进。
- **要问的问题**：下一场渠道活动能不能安排我们的交换演示位？
- **随附证明**：演示脚本 + 现场拓扑图 + 实测数据（组播不泛洪/ERPS 收敛）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：意大利/国际 B2B 增值分销商（VAD，2026 年满 20 年）：电信、安全、连接类产品的渠道分销 + 自有 B2B 电商门户 AikomGo（实时库存/价目/促销/文档，24/7 下单）。
- **产品线与在售品牌**：六大板块：Wi-Fi & Networking（AP/路由/布线）、Broadband Connectivity（WISP/ISP/MSP 用的固定无线与微波）、Sicurezza e Videosorveglianza（视频监控/门禁）、Radio Professionali（DMR/TETRA/LTE/PTX）、Smart Communications（IoT）、Unified Communication；品牌含 Hikvision、Peplink、Ruijie、Commend、Townet、Zyxel、Motorola Solutions、Avigilon(Alta)、Cambium、Selea 等。
- **目标行业与场景**：系统集成商、安装商、ISP/WISP/MSP 渠道；自办行业活动（Connectivity Camp 2026-10-13 Franciacorta，主题含 Wi-Fi、**switching**、routing、IoT）与 Aikom Partner Conference（Rimini，20 周年）。
- **团队与规模**：中型 VAD（20 年、国际销售），渠道销售 + 技术支持团队，决策链在品类经理层。
- **决策链与对接人**：info@aikomtech.com；+39 0541 648894；地址 Viale Lambrusco 1, 47838 Riccione (RN)；B2B 门户 go.aikomtech.com。
- **技术与认证**：厂商授权分销（Teltonika Gold 等）+ 自建培训/活动体系（Connectivity Camp 含设计工作台、厂商专家现场）。
- **采购与供应链信号**：VAD 逻辑：要「能补齐目录缺档 + 有渠道政策 + 有文档与活动支持」的第三条线；对中性品牌只要规格与价格能打。
- **近期动态与线索**：2026 年 9 月官网新增 Zyxel 品牌页；AikomGo 电商与 Connectivity Camp（10/13）是近期动作——上新品与渠道活动的节奏很快。
- **与我方契合点**：他的 Wi-Fi & Networking 目录与工业安防项目正是 24 口 PoE（AP/摄像头/门禁）与工业款场景；Switching 是他活动主题词，谈交换层正好接话。
- **风险与注意**：VAD 关心的是「供货稳定性 + 渠道保护 + 是否能进他们的活动/目录」；别只谈单价，谈打包进 AikomGo 与活动演示。

### R54 原文证据摘录（全部保留）

- **【业务定位】**B2B 增值分销定位与自建电商门户。
  > B2B value added distributor — Prodotti, soluzioni, tecnologie e competenze avanzate per i professionisti del canale e delle telecomunicazioni.；AikomGo, il portale e-commerce B2B di Aikom Technology — giacenze, listini, promozioni e documentazione, ordini 24/7 per system integrator, installatori e service provider
  > 来源：https://www.aikomtech.com/
- **【近期动态与线索】**Connectivity Camp（10/13）与 20 周年伙伴大会。
  > Connectivity Camp: l'evento networking dell'autunno — Il 13 ottobre … sessioni pratiche, dimostrazioni e tavoli di progettazione dedicati a Wi-Fi, switching, routing e IoT；Aikom Partner Conference 2026 – Speciale 20° Anniversario … 20 anni
  > 来源：https://www.aikomtech.com/
- **【产品线与在售品牌】**六大业务板块（含 Broadband 面向 WISP/ISP/MSP）。
  > Wi-Fi & Networking｜Broadband Connectivity — Apparati Fixed Wireless e Microwave ad alta capacità per WISP, ISP e MSP｜Sicurezza e Videosorveglianza｜Radio Professionali (DMR, TETRA, LTE, PTX)｜Smart Communications (IoT)｜Comunicazione Unificata
  > 来源：https://www.aikomtech.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（交换专长、工业/楼宇），且有具体人直联
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
Hi Aikom,

I came across Aikom Technology - 分销（Teltonika Gold + ComNet 授权）.

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
