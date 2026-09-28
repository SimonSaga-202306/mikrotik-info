# AGL Industrial Solutions

> **评级 A**　|　葡萄牙　|　档案编号 `A-058`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-058
rating: A
country: 葡萄牙
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
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — AGL 葡 Edge AI 分销（视觉机 4×PoE+、PoE 入类目）：PoE 上游温宽交换上架位（$74.8 锚点一致）；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | AGL Industrial Solutions（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 葡萄牙 | 事实 |
| 网站 | guedeslopes.pt | 事实 |
| 类型 | 分销（Antaira 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Antaira | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Antaira）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：geral@guedeslopes.pt
  - 状态：既有/公开
- **电话**：+351 218 278 341
- **原始联系字段**：+351 218 278 341 / geral@guedeslopes.pt
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 PoE++（监视保护线配套）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他讲 Vídeo·PoE·Processamento：监视保护线 24 口 PoE++ 一次到位——首封邮件直接给规格/价格对账表。
- **要问的问题**：监视保护线现在 24 口 PoE 用什么型号？
- **随附证明**：英文规格对照页 + 功率实测。

### 第 2 次跟进 · 工业非管理 PoE（Jetson/机器视觉配套）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：Jetson/机器视觉项目配套：宽温宽压、DIN，PoE++ 为 4 路 PoE+（vision/aec-4201级接入）的下游供电补齐。
- **要问的问题**：AEC-4201 旁边带什么交换机最常见？
- **随附证明**：宽温报告 + DIN 安装图 + PoE 功率预算计算表。

### 第 3 次跟进 · 管理型

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：管理型进他工业通信类目：参数页+测试报告+供货承诺三件套，对 Antaira 牌做「第二来源+项目注册=价格保护」。
- **要问的问题**：你们的 Antaira 档位里哪些段位有空缺或价格竞争力不足？
- **随附证明**：ERPS 收敛实测 + 项目注册条款 + 单价表。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：里斯本 AGL（Guedes Lopes）：1980s 起工业 PC/Edge AI 平台分销+配置服务，Portuguese 市场中央。
- **产品线与在售品牌**：工业 PC/Edge AI/Touch/工业通信（Ethernet/PoE/Wireless/Serial）+NVIDIA Jetson 全线——属技术口径强分销。
- **目标行业与场景**：工厂自动化、运输、医疗、POS、监视保护、看板——多场景做工控穿透。
- **团队与规模**：正式分销，售前选型+装机、BTO 配置。
- **决策链与对接人**：geral@guedeslopes.pt / +351 218 278 341。
- **技术与认证**：工业嵌入式硬件专家，Antaira 授权（CSV 验证）。
- **采购与供应链信号**：《Requisitos/Seleção/Configuração/Operação》流程——按配置+阶段报价，常按对价+最终文件包。
- **近期动态与线索**：官网刚改版、新品持续上线——目录扩充期，正是新品牌评估窗口。
- **与我方契合点**：「PoE·Ethernet·Wireless」是他自己挂出的品类标签：24 口 PoE++ 与管理型属于他工业通信类目的自然延伸；Antaira 关系之外我们能做第二来源。
- **风险与注意**：他代理品牌层厚——首信直接走「Antaira 之外第二供应位」，规格对价表一次给全。

### R54 原文证据摘录（全部保留）

- **【业务定位】**AGL：从需求到运营的工业嵌入式硬件平台商——工业 PC/Edge AI/Touch/通信四产品线。
  > Do requisito à operação: hardware industrial preparado para integrar.
  > 来源：https://guedeslopes.pt/
- **【产品线与在售品牌】**「Comunicação Industrial」整段对的就是以太网+PoE——他品类里就有对口的入口。
  > Comunicação Industrial — Ethernet · PoE · Wireless · Serial. Redes e gateways para ligar máquinas, sensores e sistemas.
  > 来源：https://guedeslopes.pt/
- **【目标行业与场景】**主营业务领域挂牌监视与保护（Vídeo · PoE · Processamento）——PoE 视频监控核心场景。
  > Vigiar e proteger — Vídeo · PoE · Processamento
  > 来源：https://guedeslopes.pt/
- **【技术与认证】**Arbor Jetson Orin Edge AI 产品带 4 个 PoE+ 口——他本人也会算供电预算。
  > Arbor AEC-4201 (NVIDIA® Jetson Orin™ NX, 117/157 TOPS, 4x PoE+)
  > 来源：https://guedeslopes.pt/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第6批.json`；价格均为 EXW 快照。

- **①背景再核**：葡工业计算/Edge AI 电商分销；PoE 入类目+监控解法在册
- **②芯片/型号**：Antaira（CSV）+视觉机 4×PoE+
- **③KP 深挖**：geral@ 口+电话
- **④Saga 对标**：PoE 上游温宽交换（避其视觉机正面）
- **⑤在乎与偏好**：目录文档齐/RFQ

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Comunicação Industrial: Ethernet·PoE·Wireless·Serial…07 Vigiar e proteger: Vídeo·PoE·Processamento”
  > “Comunicação Industrial: Ethernet·PoE·Wireless·Serial…07 Vigiar e proteger: Vídeo·PoE·Processamento”
  > 来源：https://guedeslopes.pt/
- **【产品线】**新品：Arbor AEC-4201 (Jetson Orin NX, 4x PoE+)、NVIDIA DGX Spark
  > 新品：Arbor AEC-4201 (Jetson Orin NX, 4x PoE+)、NVIDIA DGX Spark
  > 来源：https://guedeslopes.pt/en/collections/novos-produtos
- **【联系方式】**geral@guedeslopes.pt +351 218 278 341；MX=Google（MX/DNS 级核验：域存活=邮件可投递到域）
  > geral@guedeslopes.pt +351 218 278 341；MX=Google（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://guedeslopes.pt/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | AGL 葡 Edge AI 分销（视觉机 4×PoE+、PoE 入类目）：PoE 上游温宽交换上架位（$74.8 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：目录吞吐
- **W**：非主轴
- **O**：双吞 PoE
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
Hi AGL team,

A catalog that sells Jetson vision platforms with 4x PoE+ on board knows the PoE device world well - it is right there in your Industrial Communication category.

We build industrial managed PoE switches rated -40 to 75C that sit just upstream of those devices. Reference: $74.8 USD EXW.

One question: who supplies the PoE switch layer upstream of your vision and security device rows today?

If useful, I can send one unit plus catalog-ready documentation. If not a fit, one line and I close the loop.

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
