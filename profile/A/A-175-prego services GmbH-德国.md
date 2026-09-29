# prego services GmbH

> **评级 A**　|　德国 · Ludwigshafen am Rhein　|　档案编号 `A-175`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-175
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — prego 能源 BPO 专家：自身 IT 窄位低优先（$165 锚点一致）；Stadtwerke 交付线守界；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | prego services GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Ludwigshafen am Rhein | 事实 |
| 网站 | https://www.prego-services.de | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】prego services GmbH（德国，**能源市场服务商 25+ 年**）：流程咨询/IT 解决方案/**SAP（咨询到运营）/Data&Analytics/BPO（薪资外包/材料物流）**；客户墙几乎全是 **Stadtwerke 群**（Saarbrücken/Heidelberg/Bad Nauheim/Kreuznach/St. Wendel/Am See）+区县/医疗商会；13+ 员工精益专深
- 【推断】**结构性公共客群（EVU/Stadtwerke=集体市立资本）**：其交付进来的方案件在公共采购规范光照内——纪律只谈 prego 自身企业 IT 与私营侧面，明示不碰其 Stadtwerke 交付线
- 【假设】13 人精益+SAP 级专业=其自身内部 infra 小量无需大谈，窄位低优先客观

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@prego-services.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@prego-services.de [Publicly listed; delivery not tested]; https://www.prego-services.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（自用/商业咨询客户段，市公终端项目划线）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：边界面先摆清：终端市公/KRITIS 项目不供；谈他自用与非 KRITIS 商业咨询客户的 24 口接入层。
- **要问的问题**：自用与商业咨询客户的接入层用什么？（边界声明随附）
- **随附证明**：边界声明 + 规格对照（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（商业客户厂房段）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：非 KRITIS 商业客户的厂房：宽温 DIN PoE。
- **要问的问题**：商业客户厂房段有需求吗？
- **随附证明**：宽温报告 + DIN 图（德文）。

### 第 3 次跟进 · 管理型 PoE（自用分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：自用机房/办公分段标准件：VLAN/ERPS 模板；无商业回响则归档。
- **要问的问题**：自用段的分段模板要不要留一套？
- **随附证明**：VLAN/ERPS 模板（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第9批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：路德维希港分支（品牌源自萨尔圈）的能源行业 IT/BPO 服务商：市公（KRITIS 能源）客户为主场，Allied Resell（CSV 记录）。⚠️ 不对终端市政公用项目供货。
- **产品线与在售品牌**：流程咨询/托管服务/SAP/采办数字化/薪酬外包/能源行业 IT 方案。
- **目标行业与场景**：市公（Stadtwerke）与能源体的流程/托管；内部自用与 BPO 运营 IT 可谈。
- **团队与规模**：中型行业服务商（多分支）。
- **决策链与对接人**：info@prego-services.de（CSV 9-27：自有域 Impressum 列 Ludwigshafen 分支与通用邮箱）。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：⚠️ 边界：不通过他进市公终端项目（采购约束与 KRITIS 能源语境）；现实空间=他自有办公室/运营 IT 与非 KRITIS 商业咨询客户的商用件。
- **近期动态与线索**：能源转型内容营销密集（行业趋势栏目）。
- **与我方契合点**：自用运营 IT 的接入层与工业件——边界透明反而容易建立信任。
- **风险与注意**：首封即划市公项目不供；别让他当你进市公的通道去设计。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网抬头：能源市场服务商——25+ 年给能源行业做流程/系统/数字化方案与托管。
  > prego services ist der Energiemarktdienstleister für Prozess-, System und Digitalisierungslösungen mit ganzheitlichem Beratungsansatz. ‖ Seit über 25 Jahren Partner der Energiewirtschaft.
  > 来源：https://www.prego-services.de/
- **【目标行业与场景】**⚠️ 客户墙几乎全是市政公用与能源体：海德堡/萨尔布吕肯/St.Wendel/Bad Nauheim/Kreuznach 市政公用+Saarpfalz 县+Ahrtal/VSE/Voltaris/1-2-3 energie——公共/KRITIS 客户段为主场。
  > Referenzkunden: Stadtwerke Heidelberg · Stadtwerke Saarbrücken · Stadtwerke St. Wendel · Stadtwerke Bad Nauheim · Kreuznacher Stadtwerke · Stadtwerk am See · Saarpfalz-Kreis · Ahrtal-Werke · VSE · Voltaris · 1-2-3 energie · profine · Ärztekammer des Saarlandes · die Rheinpfalz
  > 来源：https://www.prego-services.de/
- **【产品线与在售品牌】**四块：流程咨询/IT 方案/数据分析 AI/运营优化——托管（CIO 指导+DC 与网络）+SAP+采办数字化+薪会计外包。
  > Prozessberatung · IT-Lösungen · Data, Analytics, KI · Betrieb und Optimierung ‖ Managed Service（Von CIO Guidance bis Umsetzung… Cyber Security Themen auf das Datacenter und das Network）· SAP® Lösungen · Beschaffungsprozesse digitalisieren（数字化采购服务）
  > 来源：https://www.prego-services.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第18批.json`；价格均为 EXW 快照。

- **①背景再核**：能源 BPO 专家（Stadtwerke 客墙全谱）；自身 IT 窄位
- **②芯片/型号**：SAP 生态
- **③KP 深挖**：info@；自建双 MX（技术自托）
- **④Saga 对标**：prego 自身 IT value 件（窄位低优先，公共交付线守界）
- **⑤在乎与偏好**：SAP 级文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“der Energiemarktdienstleister für Prozess-, System und Digitalisierungslösungen…[referenz logos:] Stadtwerke Saarbrücken, Stadtwerke Heidelberg…Seit über 25 Jahren Partner der Energiewirtschaft”
  > “der Energiemarktdienstleister für Prozess-, System und Digitalisierungslösungen…[referenz logos:] Stadtwerke Saarbrücken, Stadtwerke Heidelberg…Seit über 25 Jahren Partner der Energiewirtschaft”
  > 来源：https://prego-services.de/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：能源 BPO 专家（Stadtwerke 客墙——公共本性）
- **产品线与在售品牌**：SAP 体系
- **目标行业与场景**：EVU/Stadtwerke（守界）
- **团队与规模**：13+ 精益
- **决策链与对接人**：info@ 口
- **技术与认证**：SAP 级
- **采购与供应链信号**：其自身 IT 小量
- **近期动态与线索**：能源转型内容线
- **与我方契合点**：prego 自身 IT 窄位（低优先）
- **风险与注意**：公共客群结构

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | prego 能源 BPO 专家：自身 IT 窄位低优先（$165 锚点一致）；Stadtwerke 交付线守界 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：专
- **W**：小+公共
- **O**：自身
- **T**：占据

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
  - [ ] 自身 IT 现状
  - [ ] 私营侧面

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi prego team,

Twenty-five years deep in the energy market - Microsoft to SAP, process consulting to payroll BPO, for a customer list of Stadtwerke that speaks for itself. (To be explicit: this note concerns prego's own corporate IT only - your Stadtwerke delivery lines are fully out of scope here.)

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW - a value unit for your own office and lab infrastructure, nothing more ambitious.

One question: what currently powers the access layer of prego's own internal IT - and would a documented value alternative be worth a look for your own rack?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

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
