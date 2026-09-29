# Heartland Business Systems

> **评级 A**　|　美国 · Little Chute, WI　|　档案编号 `A-118`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-118
rating: A
country: 美国
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
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — HBS 威州全栈（Cisco/HPE 同盟）：第二架价值线窄判别（$165 锚点一致）；第三方名录邮箱存疑标注；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Heartland Business Systems（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Little Chute, WI | 事实 |
| 网站 | https://www.hbs.net | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】HBS Heartland Business Systems（威斯康星 Little Chute）：中大企业技术全栈商——基础设施转型（数据中心）/协作（Webex）/网络安全（SOC/IR/渗透/GRC）/托管 IT（Managed One）/应用开发；伙伴墙：Cisco/HPE/Microsoft/Verkada/Lenovo/Everpure；Copilot 生态营销活跃
- 【推断】伙伴墙=一线大牌（Cisco/HPE/Verkada）——其接入层被在位大牌主力占据；CSV 具名邮箱 jgasperich@hbs.net 为第三方名录来源，质量存疑
- 【假设】大牌同盟结构下 value 位切入空间窄：最现实角度=报价受限项目/中小客户的价值线补位——承认大牌主场并定位“第二架”

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：jgasperich@hbs.net
  - 状态：既有/公开
- **电话**：—
- 来源等级：directory（R41–R48 联系方式台账口径）
- **原始联系字段**：jgasperich@hbs.net [Third-party listing; not independently confirmed]; https://www.hbs.net
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 工业级非管理 PoE（厂区/仓库边缘窄缝）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：窄缝提案：Cisco/HPE 主体不动的边缘场景（厂区/仓库/室外）宽温 DIN PoE，成本敏感段的候选。
- **要问的问题**：（先验证联系人）厂区/仓库边缘点位的交换用什么？
- **随附证明**：宽温报告 + 单点测算 + 交付说明（英文）。

### 第 2 次跟进 · 24 口 CCTV/PoE（托管/Managed One 客户成本段）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：Managed One 客户里的成本敏感 SMB：24 口 PoE++ 接入候选，附规格对照。
- **要问的问题**：托管客户有没有成本敏感段需要备选接入件？
- **随附证明**：规格对照 + 单端口测算（英文）。

### 第 3 次跟进 · 管理型 PoE（评估样机+引荐）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：实验室评估机+ERPS 实测：目标进入其 SMB 段备选清单或获转介绍。
- **要问的问题**：实验室要不要留一台对照评估？
- **随附证明**：评估样机 + VLAN/ERPS 模板 + 实测（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第6批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：威斯康星起家的中西部中型综合 SI：基础设施/协作/安全/应用四线+托管服务，区域医疗教育政府客群（Allied 关系按 CSV 记录，官网伙伴墙未见露出）。
- **产品线与在售品牌**：数据中心/协作（Webex）/安全（SOC/渗透/风险评估）/应用开发/Managed One 托管；大厂栈为主。
- **目标行业与场景**：中西部企业/医疗/教育/地方政府的基础设施换代项目。
- **团队与规模**：中型区域 SI（多办事处网络）。
- **决策链与对接人**：联系人为 jgasperich@hbs.net（商会第三方列源，CSV 标注待核）；发件前电话确认该联系人在岗。
- **技术与认证**：Cisco/HPE 高阶资质（官网伙伴页）；Allied 代理（CSV 记录）。
- **采购与供应链信号**：大厂栈主导：标准接入层是强品牌场——切入靠「边缘/工业窄缝」而非正面对标。
- **近期动态与线索**：Microsoft Copilot/AI 叙事主推（2026 版式）；活动与 webinar 获客常态。
- **与我方契合点**：边缘窄缝：工业 PoE（厂区/仓库项目）与 NaaS/托管客户的成本敏感接入段，求评估位不求替位。
- **风险与注意**：联系人邮箱为第三方列源：先发短信+LinkedIn 验证身份再展开；别把他家安全品牌（Halo 客服等）写进报价抬头。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网抬头：技术·网络安全·综合 IT 服务——中西部区域综合方案商。
  > Technology. Cybersecurity. Comprehensive IT services. · Driving business outcomes across your technology journey.
  > 来源：https://www.hbs.net/
- **【产品线与在售品牌】**四大转型线+伙伴墙（Cisco/HPE/Microsoft/Verkada/Lenovo 打头）——⚠️ 首页伙伴行未见 Allied 露出，Allied 关系以 CSV 记录为准。
  > Transforming Infrastructure（Data Center）· Revolutionizing Work（Collaboration）· Securing What Matters（Risk Assessment）· Modernizing Applications（App Development）‖ HBS has built strong partnerships with the world’s top technology providers.（伙伴墙打头：Cisco · HPE · Microsoft · Verkada · Lenovo）
  > 来源：https://www.hbs.net/
- **【团队与规模】**Managed One 托管服务自成产品线——公司化中型 SI 的标准建制。
  > With Managed One—comprehensive managed IT services by HBS—you’ll have proactive IT support and services to keep you running at your best.
  > 来源：https://www.hbs.net/
- **【决策链与对接人】**商会名录（第三方页）列出的业务联系人为 Joe Gasperich（CSV 9-27 记录：第三方来源、未独立确认，admin 地址不作为优先入口）。
  > 业务联系人邮箱 jgasperich@hbs.net（商会列出，第三方待核；不把 legal 法务邮箱当销售入口——CSV 2026-09-27 说明）
  > 来源：https://deltami.org/places/heartland-business-systems/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第12批.json`；价格均为 EXW 快照。

- **①背景再核**：中大企业全栈商；一线伙伴同盟（Cisco/HPE/Verkada）；value 位窄
- **②芯片/型号**：Allied 信号（CSV 载）
- **③KP 深挖**：jgasperich 第三方名录存疑
- **④Saga 对标**：第二架价值线（窄）
- **⑤在乎与偏好**：伙伴目录

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Market-leading technologies…Cisco, HPE, Microsoft, Verkada, Lenovo…Managed One comprehensive managed IT services”
  > “Market-leading technologies…Cisco, HPE, Microsoft, Verkada, Lenovo…Managed One comprehensive managed IT services”
  > 来源：https://www.hbs.net/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：威州中大企业技术全栈商
- **产品线与在售品牌**：Cisco/HPE/MS/Verkada 一线同盟
- **目标行业与场景**：中大企业/数据中心
- **团队与规模**：中大型
- **决策链与对接人**：官网联系口主路+jgasperich 辅助
- **技术与认证**：SOC/渗透级
- **采购与供应链信号**：伙伴目录内采购
- **近期动态与线索**：Copilot 生态营销
- **与我方契合点**：第二架价值线（窄判别）
- **风险与注意**：大牌同盟强

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | HBS 威州全栈（Cisco/HPE 同盟）：第二架价值线窄判别（$165 锚点一致）；第三方名录邮箱存疑标注 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：全栈
- **W**：同盟
- **O**：预算线
- **T**：在位

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
  - [ ] value 缺口
  - [ ] jgasperich 在职性
  - [ ] 评测窗

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi HBS team,

A partner wall anchored by Cisco, HPE and Verkada speaks for where your first shelf stands. We are not writing to displace it.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) at $165 USD EXW - built for projects where the first-shelf brands price themselves out: budget-constrained schools, municipal buildings, or SMB rollouts inside your managed plans.

One question: when a project cannot carry the first-shelf price, is there a second approved value line at HBS today?

If useful, I can send one unit with full documentation for the lab. If not relevant, one line and I close the loop.

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
