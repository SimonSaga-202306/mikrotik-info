# Profcon AB

> **评级 A**　|　瑞典 · Vansbro　|　档案编号 `A-081`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-081
rating: A
country: 瑞典
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
- **为什么值得跟**：有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — Profcon 瑞典 60 年工业集团：Nova 网络线温宽 PoE 生命周期补位（$74.8 锚点一致）；国防载荷线红线不触；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Profcon AB（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 瑞典 / Vansbro | 事实 |
| 网站 | profcon.se | 事实 |
| 类型 | 分销/集成商（Perle 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@profcon.se
  - 状态：既有/公开
- **电话**：+46 281 30600
- **原始联系字段**：+46 281 30600 / info@profcon.se（Profcon 官网联系页；总部/销售同一邮箱。Perle 授权分销商）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 品类空缺补位（Nova 网络线的工业 PoE 价位段）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：顺着 Nova 苛刻环境网络线：8 口宽温 DIN PoE 与现售工业件同规格、价优一档，做并列货架 SKU 不冲突。
- **要问的问题**：Nova 网络线的工业 PoE 现在只有 Perle 一家吗？
- **随附证明**：宽温/-40 冷启动报告 + 同规格对照 + 瑞典交付说明（英文）。

### 第 2 次跟进 · 工业非管理 PoE 第二来源（项目配套）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：站台屏/医院/国防项目的零散点位：4 口小机配套盒，本地备货+逐年质保，给他当项目报价里的「性价比选项」。
- **要问的问题**：项目里 4–8 口工业 PoE 的年度用量大概多少？
- **随附证明**：长期供货承诺 + 备件包价 + DIN 安装图。

### 第 3 次跟进 · 管理型 10G（机房/骨干段升级+项目注册）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他的数据中心方案线：管理型 8G+4×10G SFP+ 带 ERPS/VLAN 模板，谈项目注册与价格保护，不伤日常分销价。
- **要问的问题**：机房段的接入/汇聚有没有 10G 升级单在评估？
- **随附证明**：ERPS 实测 + 项目注册政策 + 价格保护条款（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第5批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：瑞典达拉纳老牌工业技术公司：防火阀控制（OnControl/Siox）+ 苛刻环境工业 IT（Nova，含 Perle 工业网络产品授权分销），「必须可靠」是品牌灵魂。
- **产品线与在售品牌**：Nova：工业 PC/Panel-PC/力传感器/称重+苛刻环境网络与数据中心（Perle 线）；OnControl：排烟阀控制；Siox：防火阀监控系统。
- **目标行业与场景**：医院、能源（大坝）、轨道交通站台、国防——全部要求宽温、长寿命、可维护性的工业网络场景。
- **团队与规模**：源起 1960 年代末的近 60 年工业公司，现为 Nova / OnControl / Siox 三专业品牌；2026 年仍在招人。
- **决策链与对接人**：总部销售一体：+46 281 30600 / info@profcon.se；Perle 授权分销商在册（CSV 记录）。
- **技术与认证**：工业自动化与消防安全体系；Perle 工业 PoE/媒体转换/串口联网授权渠道（CSV 记录）。
- **采购与供应链信号**：本地备货分销+自有项目配套双通道；苛刻环境件重可靠性证明与长期供货承诺。
- **近期动态与线索**：扩编+新模块+新品牌上架（2026 年夏），产品组合在扩——正是递资料窗口。
- **与我方契合点**：Nova 的「苛刻环境网络」货架与我们的工业宽温线同构：Perle 同规格价差是天然对话；Siox 项目的联网段也有配套机会。
- **风险与注意**：品质叙事型客户：别用低价开场，先给宽温/MTBF/质保全套资料；瑞典沟通用英文技术资料即可。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网口号「必须正常运转的时候」：防火阀控制、医院、中国大坝项目、火车站台信息屏、国防载荷传感器——全是极限工况。
  > När det måste fungera. · Oavsett om det handlar om brandspjäll i ett sjukhus, ett dammprojekt i Kina, informationstavlor på en tågperrong, eller lastceller till försvaret…
  > 来源：https://www.profcon.se/
- **【产品线与在售品牌】**Nova 品牌线含「苛刻环境下的网络与数据中心解决方案」——正是其 Perle 工业交换/串口联网产品的落点。
  > Profcon Nova — Utforska Novas lösningar inom panel-PC, industridatorer, kraftgivare, lastceller samt nätverks- och datacenterlösningar för krävande miljöer.
  > 来源：https://www.profcon.se/
- **【团队与规模】**公司源起 1960 年代末，现为三品牌工业集团（Nova / OnControl / Siox），产品寿命长到「我们中间改过几次名」。
  > Företaget har sina rötter i slutet av 1960-talet och har sedan dess vuxit till ett modernt industriföretag med tre specialiserade varumärken: Nova, OnControl, Siox.
  > 来源：https://www.profcon.se/
- **【近期动态与线索】**2026 年 7 月在招人扩编、6 月发 RELIO 新 I/O 模块并上架 Calectro 烟感——业务在增长期。
  > Bli en del av vårt team!（2026-07-08）· RELIO – ny flexibel I/O-modul för Siox（2026-07-06）· Nu säljer vi Calectros rökdetektor UG8-O（2026-06-15）
  > 来源：https://www.profcon.se/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第9批.json`；价格均为 EXW 快照。

- **①背景再核**：60 年工业集团三牌；消防阀控为骨干，Nova 网络线是对口入口
- **②芯片/型号**：Perle 在册（CSV）
- **③KP 深挖**：info@；电话并行
- **④Saga 对标**：温宽 PoE 生命周期补位（避国防/公共）
- **⑤在乎与偏好**：必须可用+超长期支持

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“När det måste fungera…Nova: industridatorer, Panel-PC, lastceller samt lösningar för nätverk och datacenter”
  > “När det måste fungera…Nova: industridatorer, Panel-PC, lastceller samt lösningar för nätverk och datacenter”
  > 来源：https://www.profcon.se/
- **【近期动态】**“RELIO – ny flexibel I/O-modul för Siox（2026-07）+Nu säljer vi Calectros rökdetektor UG8-O（2026-06）”
  > “RELIO – ny flexibel I/O-modul för Siox（2026-07）+Nu säljer vi Calectros rökdetektor UG8-O（2026-06）”
  > 来源：https://www.profcon.se/nyheter
- **【风险与注意】**“lastceller till försvaret”（国防载荷传感——红线不涉）
  > “lastceller till försvaret”（国防载荷传感——红线不涉）
  > 来源：https://www.profcon.se/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Profcon 瑞典 60 年工业集团：Nova 网络线温宽 PoE 生命周期补位（$74.8 锚点一致）；国防载荷线红线不触 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：信誉
- **W**：红线段
- **O**：Nova 线
- **T**：在位盘

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

**主题**：PoE switching for your projects

```text
Hi Profcon team,

"När det måste fungera" - products that outlive a couple of renames - that is exactly the lifecycle culture our switches are built for.

We build industrial managed PoE switches rated -40 to 75C with a hardware watchdog and multi-year supply commitments - a natural fit beside the Nova networking line. Reference: $74.8 USD EXW. (We stay strictly within civilian industrial projects.)

One question: within the Nova networking portfolio, who supplies the industrial PoE layer today?

If useful, I can send one unit with the full temperature test documentation. If not a fit, one line and I close the loop.

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
