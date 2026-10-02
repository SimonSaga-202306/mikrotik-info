# Michiel Visser

> **评级 A**　|　荷兰 · Deventer　|　档案编号 `A-271`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-271
rating: A
country: 荷兰
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Interstellar 荷微软栈大 MSP（TD SYNNEX PoY 2026）：私营段随单窄针（$165 锚点一致）；Gemeente Katwijk 公共守界；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Michiel Visser（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 荷兰 / Deventer | 事实 |
| 网站 | https://interstellar.nl | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证顾问，持 MTCRE MTCWE MTCIPv6E MTCINE MTCSE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Interstellar（荷兰 Microsoft 主栈大 MSP）：四域=Cloud&Infra/Workspace/Security/Data&AI；TD SYNNEX Partner of the Year 2026；ISO 27001/B Corp；客户墙含 KLM/Gemeente Katwijk（市政=公共守界）；CSV=Michiel Visser MikroTik 认证顾问在册
- 【推断】大 MSP 微软栈：网络件边缘位——窄针；公共段（市政）守界句先置
- 【假设】私营段客户现场的偶发随单窄针

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问，持 MTCRE MTCWE MTCIPv6E MTCINE MTCSE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@interstellar.nl
  - 状态：既有/公开
- **电话**：+31 6 29047127
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：info@interstellar.nl（关联公司官网联系页；个人归属/现任职限制见备注）；原入口：+31 6 29047127
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 商业客户段接入层第二来源一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：荷/英一封到集团箱（注明可转网基建团队）：商业客户办公室/园区项目的 24 口 PoE 第二来源（RMA/供货连续性随行）；声明不涉及市政/医疗客户段。
- **要问的问题**：商业客户项目的接入层目前有第二来源位吗？
- **随附证明**：一页报价（英）+ 保修/RMA。

### 第 2 次跟进 · 万兆上行/汇聚件

- **推什么**：STC-424XGGPM-440W（Saga）（24×万兆 PoE++ + 4×万兆 SFP+ 上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：spine-leaf/汇聚话题的万兆上行件（与 MikroTik 演讲者的技术语境对齐）。
- **要问的问题**：汇聚/spine-leaf 预商用场景需要高性价比万兆件吗？
- **随附证明**：万兆件一页规格。

### 第 3 次跟进 · 价卡留档收口

- **推什么**：—（价卡留档）
- **切入点**：全品类价卡留档、评估流程走完前不打扰；无回复即冻结。
- **要问的问题**：（无需回）价卡留档。
- **随附证明**：全品类一页价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：荷兰全国微软系 MSP 集团（TD SYNNEX 2026 年度伙伴）：其顾问 Michiel 是 MikroTik spine-leaf 演讲者=集团内有交换技术火种。
- **产品线与在售品牌**：Cloud/Workspace/Security/Data-AI 四域+全国多地办公室。
- **目标行业与场景**：中大型组织（市政/医疗案例划出、商业客户如 Quooker/KLM 体系可做）。
- **团队与规模**：大型 MSP（多地点+认证群）。
- **决策链与对接人**：info@interstellar.nl（集团总箱，CSV 9-27；个人归属限制按备注）。
- **技术与认证**：（集团 ISO/NEN/B Corp；Michiel 个人 MikroTik 顾问持 MTCRE/MTCWE/MTCIPv6E/MTCINE/MTCSE，CSV）。
- **采购与供应链信号**：商业客户园区/办公室项目的接入层第二来源；**spine-leaf/数据中心话题与万兆上行件对得上 Michiel 的技术口味**。
- **近期动态与线索**：TD SYNNEX 年度伙伴=采购走渠道架构，报价须走他们的供应商引入流程。
- **与我方契合点**：商业段办公室/园区 24 口 PoE + 万兆上行件第二来源。
- **风险与注意**：公立市政/医疗案例客户段不经由我们；大集团评估周期长、3 封后留档不催。

### R54 原文证据摘录（全部保留）

- **【业务定位】**荷兰全国多地的微软系 MSP 集团：四大域 Cloud & Infrastructure/Workspace/Security/Data & AI，**2026-08 被提名 TD SYNNEX Partner of the Year 2026**；认证 NEN 7510/ISO 9001/ISO 27001/B Corp。
  > Eén partner. Vier domeinen. ‖ Interstellar uitgeroepen tot TD SYNNEX Partner of the Year 2026（26.08.2026）‖ Gecertificeerd. Volgens de eisen van NEN 7510, ISO 9001, ISO 27001 en B Corp.
  > 来源：https://interstellar.nl/
- **【目标行业与场景】**客户案例墙：Gemeente Katwijk（**市政——公立面划出**）、Emergis（**医疗——划出**）、Quooker（商业）、KLM 等墙标——只做商业客户段。
  > Gemeente Katwijk ‖ Emergis ‖ Quooker ‖ （墙标）KLM · VHZ …
  > 来源：https://interstellar.nl/
- **【决策链与对接人】**info@interstellar.nl 集团总箱（官网联系页，CSV 9-27 official-company）；Michiel Visser 个人归属限制按 CSV 备注走集团箱——LinkedIn 显示其 2026 在 MikroTik Professionals Conference 讲 spine-leaf 交换架构（个人技术信用留档）。
  > （CSV 2026-09-27 记录）info@interstellar.nl（官网联系页集团总邮箱）；LinkedIn 显示 Michiel Visser 任职 Interstellar（Amersfoort/Utrecht），并在 2026 MikroTik Professionals Conference 演讲 MikroTik spine-leaf 交换架构
  > 来源：https://interstellar.nl/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第28批.json`；价格均为 EXW 快照。

- **①背景再核**：NL 微软栈大 MSP（官网一手核）
- **②芯片/型号**：Microsoft
- **③KP 深挖**：info@
- **④Saga 对标**：窄针（$165 锚点一致，低密）
- **⑤在乎与偏好**：合规/品牌

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**Eén partner. Vier domeinen——TD SYNNEX Partner of the Year 2026；case: Gemeente Katwijk（公共标注）
  > Eén partner. Vier domeinen——TD SYNNEX Partner of the Year 2026；case: Gemeente Katwijk（公共标注）
  > 来源：https://interstellar.nl

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：荷兰微软栈大 MSP
- **产品线与在售品牌**：Microsoft/TD SYNNEX
- **目标行业与场景**：企业/公共（守界注）
- **团队与规模**：大规模组织
- **决策链与对接人**：info@ 口
- **技术与认证**：ISO 27001/B Corp
- **采购与供应链信号**：集团采购
- **近期动态与线索**：TD SYNNEX 年度伙伴 2026
- **与我方契合点**：窄针（私营段，公共守界句在）
- **风险与注意**：微软栈离轴+公共敏感

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Interstellar 荷微软栈大 MSP（TD SYNNEX PoY 2026）：私营段随单窄针（$165 锚点一致）；Gemeente Katwijk 公共守界 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：规模
- **W**：离轴
- **O**：随单
- **T**：大牌

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
  - [ ] 硬件权重
  - [ ] 采购集权

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Interstellar team,

Four domains, one partner - and TD SYNNEX Partner of the Year 2026. One boundary sentence: your public-sector engagements, Gemeente included, stay on your established paths; this is a narrow question about private-segment sites.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29) - for private customer sites where your infrastructure teams need a documented switching unit.

One question: when a private-segment site needs switching, who sources it - and would a value PoE line be worth keeping on file?

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

---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:[Michiel Visser](https://www.linkedin.com/in/michiel-visser-a0720b81)(既有证据链接,来源:档案/联络核验)
- **中国进口与管制**:国别档位 中(NCSC 政府供应商排除;企业网自由);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-424DGGPM-280W(48G PoE++/4×25G→智算安防酒店全谱)(本行为调查分析结论,与开发信首推型号是两回事)
