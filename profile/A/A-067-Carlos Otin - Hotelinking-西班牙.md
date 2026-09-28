# Carlos Otin / Hotelinking

> **评级 A**　|　西班牙 · Palma（马略卡）　|　档案编号 `A-067`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-067
rating: A
country: 西班牙
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: false, oem: false, hotel: true, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、酒店/多住户、光纤接入），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — 主场景匹配+首触只推一个型号的纪律；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Roughly how many site visits a month come from a hung AP or camera across your hospitality sites?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Carlos Otin / Hotelinking（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 西班牙 / Palma（马略卡） | 事实 |
| 网站 | hotelinking.com | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Carlos Otin | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCSE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCSE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）、酒店/多住户
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - 酒店/多住户：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：c.otin@hotelinking.com
  - 状态：既有/公开
- **电话**：+34 691 837 651
- **原始联系字段**：+34 691 837 651 / c.otin@hotelinking.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Carlos Otin**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（酒店楼层接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：酒店一层楼的 AP+IPTV+话机+监控一张网：24 口 PoE++ + 4×10G 上行，按「每层一台」给他算总拥有成本。
- **要问的问题**：WiFiBot 交付的酒店楼层接入换型时，哪段成本最头疼？
- **随附证明**：每层一台的 BBOM 测算 + 规格对照（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（公区/户外/机电间点位）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：酒店泳池/露台/停车场/机电间的零散点位：宽温 DIN 免配置 4 口小机，NOC 远程看不出差别、现场免调试。
- **要问的问题**：公区零散点位现在用什么型号？坏机率高不高？
- **随附证明**：宽温报告 + 备件包价 + 免配置说明。

### 第 3 次跟进 · 管理型 PoE（客人网/员工网分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：WiFiBot「厂商无关」标准件清单加一个候选：VLAN 三层分段+ERPS 冗余的接入层模板，整套交付文档英文齐套。
- **要问的问题**：标准件清单评审周期是多久？我们可以走一次技术评估。
- **随附证明**：VLAN/ERPS 模板 + 实测 + 质保/备件政策（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：马略卡酒店科技平台（非传统集成商）：CRM（GuestMaker）+ 酒店网络运营（WiFiBot）+ 前台数字化（DeskForce）三件套，按平台费模式收费。
- **产品线与在售品牌**：软件平台+托管网络服务；网络硬件「厂商无关」=他们替酒店全国选型，交换机是 WiFiBot 交付的底层耗材。
- **目标行业与场景**：西班牙连锁酒店集团（60% 渗透率）：客房/公区 Wi-Fi、前台数字化、酒店网络安全合规——AP/IPTV/话机密集的 PoE 场景。
- **团队与规模**：平台公司编制（Palma 总部），NOC 团队 24/7 运营 1000+ 酒店网络；Carlos Otin 为高级网络工程师（MikroTik 路由+交换+无线+GPON）。
- **决策链与对接人**：技术侧 Carlos Otin（+34 691 837 651 / c.otin@hotelinking.com）；平台公司采购走技术背书包。
- **技术与认证**：MTCNA+MTCSE（CSV 名录记录）；团队管着千家酒店的异构网络，交换分段/客人网隔离是日常。
- **采购与供应链信号**：千家酒店网络的扩容与翻新=持续性硬件需求；「厂商无关」意味着能以规格/价格进标准件清单。
- **近期动态与线索**：平台在高速扩张（集成数 120+、渗透率 60%），每条新签约酒店都要铺网络——硬件需求跟着平台增长。
- **与我方契合点**：酒店楼层接入=24 口 PoE++；公区/户外点位=工业件；客人网/员工网/IoT 三层分段=管理型标准模板；量级=平台级。
- **风险与注意**：平台公司对供应商稳定性/质保/备件要求高：首轮给全质保与备件政策；别用「便宜」开场，用「TCR 总成本」。

### R54 原文证据摘录（全部保留）

- **【业务定位】**酒店科技平台：1000+ 酒店与连锁在用，西班牙连锁酒店渗透率 60%。
  > +1.000 hoteles y cadenas ya confían en Hotelinking · 60% de penetración en cadenas hoteleras en España
  > 来源：https://www.hotelinking.com/
- **【产品线与在售品牌】**WiFiBot 产品线=酒店网络 24/7 监控+NOC 托管+集中控制，并强调「与厂商无关」——网络硬件采购话语权在他们手里。
  > WiFiBot: plataforma de operación y seguridad de redes para hoteles · Monitorización de Redes 24/7 … servicios expertos de NOC · Unifica infraestructuras diversas con soluciones independientes de proveedores y sistemas de control escalables.
  > 来源：https://www.hotelinking.com/
- **【团队与规模】**平台数据：1000 万+注册住客、为酒店省下 3000 万+ OTA 佣金、120+ 个 PMS/预订引擎/CRM 集成——平台体量可观。
  > +10M de huéspedes registrados y activados para marketing directo · +30 M en comisiones ahorradas · +120 integraciones activas con PMS, motores de reserva y CRM
  > 来源：https://www.hotelinking.com/
- **【目标行业与场景】**客户墙全是西班牙大型连锁酒店集团：RIU、Zafiro、Best Hotels、Bluesea、Coral、Grupotel。
  > RIU · Zafiro Hotels · Best Hotels · Bluesea · Coral Hotels · Grupotel（客户墙 Logo）
  > 来源：https://www.hotelinking.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（交换专长、酒店/多住户、光纤接入），且有具体人直联
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

**主题**：24-port PoE + 10G uplinks for your larger sites

```text
Hi Carlos,

I came across Hotelinking - 集成商/顾问（MikroTik 认证）.

We build a 24-port Gigabit PoE switch (280W, af/at) with 4×10G SFP+ uplinks, Voice VLAN and a hardware PoE watchdog that reboots hung APs/cameras without a site visit. Reference: $165 USD EXW.

One question: Roughly how many site visits a month come from a hung AP or camera across your hospitality sites?

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
