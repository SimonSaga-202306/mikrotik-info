# Efa Automazione S.p.A.

> **评级 A**　|　意大利 · Cernusco Sul Naviglio (MI)　|　档案编号 `A-039`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-039
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
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — EFA/Relatech 工业 DT：温宽 PoE+看门狗错位 Red Lion/N-Tron（$74.8 邮件锚点一致）；水务公用段规避；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Efa Automazione S.p.A.（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Cernusco Sul Naviglio (MI) | 事实 |
| 网站 | efa.it | 事实 |
| 类型 | 分销（HMS/N-Tron·Red Lion 渠道） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | N-Tron + Red Lion | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：N-Tron + Red Lion）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：vendite@efa.it
  - 状态：既有/公开
- **电话**：02 92 11 31 80
- **原始联系字段**：vendite@efa.it（销售部）；info@efa.it；电话 02 92 11 31 80
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：从他们的工厂安防/无线场景切：24 口 PoE++ 汇聚摄像头与 AP；先给一份「同规格价差表」让他做内部降本论证。
- **要问的问题**：他们的项目里商用级 PoE 汇聚现在谁供货、价格锚在哪？
- **随附证明**：同规格对照表（含他现售品牌）+ 价差表 + 测试机。

### 第 2 次跟进 · 工业级非管理 PoE（第二供应商）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C，PoE++ 版）
- **切入点**：他卖 N-Tron/Red Lion 8 口非网管约 $500+：同规格（DIN/宽温/双电源）中性货价差明显；以「备件/第二供应商」起步，不进主 BOM。
- **要问的问题**：愿不愿意先拿 2 台做现场对比（不动他现有品牌）？
- **随附证明**：规格对照（MTBF/宽温/双电源）+ 认证文件包 + 2 台测试机。

### 第 3 次跟进 · 管理型 PoE（冗余环/10G）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：工厂与市政项目要冗余环与 10G 上行：管理型 + 光纤组合补他方案里的接入环；若集团框架允许，可谈区域代理。
- **要问的问题**：水务/能源项目的接入环网与 10G 上行需求有多少？
- **随附证明**：ERPS 切换实测 + 光模块兼容清单 + 参考案例（可公开）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：米兰工业区的工业数字化转型方案商（EFA Automazione S.p.A.，Relatech 集团成员）：IIoT 方案、软件与硬件分销 + 系统集成，30 年行业 know-how。
- **产品线与在售品牌**：方案板块含 **Switch & Networking**、通信网关、工业 I/O 与数据采集、HMI 操作面板、版本管理、信息安全、DataOps、工业软件、远程维护与遥测；渠道背景为 **N-Tron / Red Lion / HMS** 等工业品牌（CSV 记录），同类还有 Moxa/Advantech 等生态。
- **目标行业与场景**：制造、流程工业、能源、建筑、交通、基础设施（水务、乳业、水电、酿酒、层压板等大量公开案例）；客户以系统集成商与最终工厂为主。
- **团队与规模**：成规模的技术分销/集成公司（米兰 Cernusco sul Naviglio 总部 + Villafranca di Verona 分部），隶属 Relatech 集团（注意集团采购层级）。
- **决策链与对接人**：销售部 vendite@efa.it、info@efa.it；+39 02 92 11 31 80。
- **技术与认证**：工业品牌授权渠道 + 自有系统集成团队；官网强调「数以千计的可用参考与案例文档」。
- **采购与供应链信号**：**价格锚点优势**：他卖 N-Tron/Red Lion 8 口非网管工业交换机（约 $500+ 级），同规格中性货在其体系里有量级价差空间 → 天然的「第二供应商/降本项目」故事。
- **近期动态与线索**：2026 年官网持续更新（Ignition + AI 水务案例、案例库与培训课程 OPC Router），工业 IIoT 主线在扩张——交换机作为承载件需求同步增长。
- **与我方契合点**：Switch & Networking 是他们明列方案板块；海量工厂/水务/能源现场就是宽温、DIN、冗余环、PoE 的场景；我们的工业线正好补他渠道里的价位段。
- **风险与注意**：**集团层级**：Relatech 下属公司的采购可能受集团框架约束，先问清「品类决策在 EFA 还是集团」；另外工业客户看重认证文件（UL/CSA/Class 1 Div 2），资料要备齐。

### R54 原文证据摘录（全部保留）

- **【产品线与在售品牌】**方案板块明列 Switch & Networking 与工业网关/I/O/HMI。
  > Soluzioni：Gateway di comunicazione｜Industrial I/O & Data Collection｜Pannelli Operatore HMI｜Piattaforme di versioning｜Sicurezza informatica｜Software di DataOps｜Software Industriale｜**Switch & Networking**｜Teleassistenza & Telecontrollo
  > 来源：https://www.efa.it/
- **【目标行业与场景】**行业覆盖与案例密度（制造/流程/能源/建筑/交通/基础设施）。
  > realizzare applicazioni specifiche per qualsiasi settore: manufacturing, processo, energia, building, trasporti, infrastrutture e molto altro ancora；Casi di Successo: gestione bacini idraulici｜Nuova Complat｜idroelettrico Zeco｜BDF Industries｜Casearia Belladelli｜CAP Arreghini｜Caviro Extra｜Caltanissetta 水网｜OMET｜EasyBrau｜Abet 层压板
  > 来源：https://www.efa.it/
- **【团队与规模】**集团归属与能力沉淀。
  > EFA Automazione S.p.A. è una società [del gruppo Relatech]；Il trentennale know-how maturato sul campo … l'esperienza dei nostri system integrator e le migliaia di referenze che siamo in grado di documentare
  > 来源：https://www.efa.it/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第4批.json`；价格均为 EXW 快照。

- **①背景再核**：Relatech 集团工业 DT；九线含 Switch & Networking；CSV 载 N-Tron+Red Lion
- **②芯片/型号**：Red Lion/N-Tron（工业以太网美系）
- **③KP 深挖**：vendite@ 销售部口；集团采购层级待问
- **④Saga 对标**：温宽 PoE+看门狗错位于美系工业线
- **⑤在乎与偏好**：工业件认证/文档/交期

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Soluzioni di Digital Transformation per il mondo industriale…Accompagniamo i clienti lungo la strada della digitalizzazione”+九大方案线含 Switch & Networking
  > “Soluzioni di Digital Transformation per il mondo industriale…Accompagniamo i clienti lungo la strada della digitalizzazione”+九大方案线含 Switch & Networking
  > 来源：https://www.efa.it/
- **【目标行业与场景】**“manufacturing, processo, energia, building, trasporti, infrastrutture”+Consorzio di Bonifica 水务案例（2026-07）
  > “manufacturing, processo, energia, building, trasporti, infrastrutture”+Consorzio di Bonifica 水务案例（2026-07）
  > 来源：https://www.efa.it/caso/consorzio-di-bonifica-adige-euganeo-md-automation/
- **【产品线】**CSV：N-Tron + Red Lion（工业以太网代表）
  > CSV：N-Tron + Red Lion（工业以太网代表）
  > 来源：https://www.efa.it/soluzioni/#36
- **【联系方式】**vendite@efa.it（CSV）；MX=efa-it.mail.protection.outlook.com（MX/DNS 级核验：域存活=邮件可投递到域）
  > vendite@efa.it（CSV）；MX=efa-it.mail.protection.outlook.com（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://www.efa.it/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | EFA/Relatech 工业 DT：温宽 PoE+看门狗错位 Red Lion/N-Tron（$74.8 邮件锚点一致）；水务公用段规避 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：集团+项目盘
- **W**：美系线稳
- **O**：错位 PoE
- **T**：公用段壁垒

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
Hi EFA team,

I see EFA covers industrial digitalization end to end - and that Switch & Networking is one of your nine solution lines, with Ewon and Ignition in the mix.

We build industrial-grade managed PoE switches rated -40 to 75C with a hardware PoE watchdog - a complement alongside, not a replacement for, your Red Lion / N-Tron lines, at a much lighter price point. Reference: $74.8 USD EXW.

One question: is there an open slot in your industrial switching line for PoE + self-healing at a sharper price?

If useful, I can send one unit with the full temperature test report for your lab. If not a fit, one line and I close the loop.

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
