# N&C TELECOMUNICAZIONI S.p.a.

> **评级 A**　|　意大利 · Veglie (LE)　|　档案编号 `A-206`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-206
rating: A
country: 意大利
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定；联系方式仍待核实
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 主场景匹配+首触只推一个型号的纪律；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | N&C TELECOMUNICAZIONI S.p.a.（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Veglie (LE) | 事实 |
| 网站 | https://www.nectlc.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@nectlc.com
  - 状态：待核·未验证投递（不进群发）
- **电话**：—
- 来源等级：official-search-only（R41–R48 联系方式台账口径）
- **原始联系字段**：info@nectlc.com [旧官网搜索索引邮箱；页面404，待核]; https://www.nectlc.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（商业段 Cabling/Networking 项目接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：供应商名录敲门：公司资质+CE 文件包+24 口 PoE++ 对照——走 Networking/Cabling BU 商业段（汽车/制造/运输），声明公立/医疗/金融段不涉。
- **要问的问题**：商业段布线/网络项目的接入层现在配什么？（请转 Networking BU）
- **随附证明**：资质包 + CE 文件 + 边界声明（意/英）。

### 第 2 次跟进 · 工业级非管理 PoE（海事/厂房/户外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：Luxury 游艇建造与厂房/运输户外点位：宽温 DIN PoE——海事环境的真实场景。
- **要问的问题**：船坞/厂房户外的供电交换坏机率？
- **随附证明**：宽温报告 + 海事/厂房场景 + DIN 图。

### 第 3 次跟进 · 管理型 PoE（项目分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：项目分段标准件：VLAN/ERPS 模板+样机评估进工程库。
- **要问的问题**：分段模板要不要评估进工程库？
- **随附证明**：VLAN/ERPS 模板 + 样机。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第11批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：萨伦托 Veglie 起家的 700 人科技集团：八 BU 垂直交付大型民营与公立项目，Allied Resell（CSV 记录）。⚠️ 规模/总部采购风险保留（CSV 原话）。
- **产品线与在售品牌**：八 BU 全谱：DC/布线/网络/安全/软件 AI/云/工作空间/托管。
- **目标行业与场景**：商业段（汽车/制造/GDO/运输/豪华游艇 Stellantis·Azimut-Benetti 级）正路；⚠️PA/医疗/教育/金融公立相关段划线。
- **团队与规模**：700 人全球（大型集团）。
- **决策链与对接人**：info@nectlc.com（CSV 9-27：旧官网搜索索引邮箱，页面 404 待核；新站表单/get-in-touch 备用——先表单+电话确认）。
- **技术与认证**：Allied Resell（CSV 记录）；930+ 厂资质（官网）。
- **采购与供应链信号**：大体系=供应商名录/采购流程：按要求 BU 对口（Networking 或 Cabling BU）+全套资质文件进名录；游艇（Luxury）段=海事级环境，宽温工业件有真实场景。
- **近期动态与线索**：2026-03 新站改版+营收 +23% 公告=扩张猛。
- **与我方契合点**：Networking/Cabling BU 的项目接入层与海事/厂房工业件——商业段项目流大。
- **风险与注意**：勿跨 BU 多头；公立/医疗/金融段不供；先表单登记后电话跟进档案。

### R54 原文证据摘录（全部保留）

- **【团队与规模】**官网硬数：700 全球人员、40+ 年、2025 营收 +23%、930+ 认证、每年 820+ 项目、UNI/PDR 125 配额认证——大型集成商。
  > 40+ Anni di innovazione al servizio di imprese e PA · 700 Risorse nel mondo · +23% Crescita del fatturato (2025) · 930+ Certificazioni ottenute · 820+ Progetti ogni anno
  > 来源：https://www.nectlc.com/
- **【业务定位】**八个垂直 BU 自负运营：**Data Center/Cabling & Infrastructure/Networking/Cybersecurity/Software & AI/IT System & Cloud/Digital Workspace/Managed Services（Operation Center）**。
  > Business Unit — Competenze verticali, visione integrata: Data Center · Cabling & Infrastructure · Networking · Cybersecurity & Security · Software & AI · IT System & Cloud · Digital Workspace & Collaboration · Managed Services（Operation Center）
  > 来源：https://www.nectlc.com/
- **【目标行业与场景】**十一行业页含 Automotive/制造/GDO/运输/Luxury（**Azimut-Benetti 豪华游艇**）等商业段；⚠️同时列 Pubblica Amministrazione/Healthcare/Finance/Istruzione——公立相关段划线。
  > Settori: Automotive · Energy & Utilities · GDO · Manufacturing · Telco · Trasporti · Luxury · Finance · Healthcare · Istruzione · Pubblica Amministrazione ‖ Clienti privati（logo）：Stellantis · Azimut-Benetti · Leasys · CNH · TIM
  > 来源：https://www.nectlc.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第21批.json`；价格均为 EXW 快照。

- **①背景再核**：700 人大型 ICT 集成 8 BU（车企/游艇/GDO 私客；公共段守界）
- **②芯片/型号**：未明
- **③KP 深挖**：info@（待核）
- **④Saga 对标**：Networking BU value 测试窄位（低优先）
- **⑤在乎与偏好**：—

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“700 Risorse nel mondo…40+ Anni di innovazione…820+ Progetti ogni anno…8 Business Unit…Automotive…Luxury…Stellantis, Azimut-Benetti…”
  > “700 Risorse nel mondo…40+ Anni di innovazione…820+ Progetti ogni anno…8 Business Unit…Automotive…Luxury…Stellantis, Azimut-Benetti…”
  > 来源：https://www.nectlc.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：体量
- **W**：体距
- **O**：Luxury
- **T**：协议价

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
Hi N&C team,

Eight Business Units, 820 projects a year, from Stellantis's factories to Azimut-Benetti's yacht yards - and a Networking BU where the access layer has to earn its place against the usual suspects. (For clarity: your public-administration engagements stay fully out of scope here.)

We manufacture a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW - a documented value unit for the access-layer edge when a project needs a second source. (Mooted realistically: our scale suits selective feeds, not framework-mandated volumes.)

One question: does the Networking BU keep a bench slot for a documented value PoE access line - and would our unit earn a place in that test?

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
