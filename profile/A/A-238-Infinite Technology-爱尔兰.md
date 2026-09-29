# Infinite Technology

> **评级 A**　|　爱尔兰 · Dublin　|　档案编号 `A-238`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-238
rating: A
country: 爱尔兰
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Infinite Technology 都柏林 MSP（1997/100 客户）：托管现场随单正口（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Infinite Technology（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 爱尔兰 / Dublin | 事实 |
| 网站 | https://infinitetechnology.ie | 事实 |
| 类型 | 分销/集成商（Perle 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Infinite Technology（爱尔兰都柏林 HQ，1997）：本地 MSP——24/7 托管+云+网安+战略 IT；自报'100 客户/50% 留存/月结 1000 工单'
- 【推断】增长期 MSP：客户现场网络件随单是常态——标准 value 正口
- 【假设】托管现场扩/换代的 PoE 接入随单

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

- **邮箱**：sales@infinitetechnology.ie
  - 状态：待核·未验证投递（不进群发）
- **电话**：+353 1 2939000
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：sales@infinitetechnology.ie（官网正文公开；未验证投递）；原入口：+353 1 2939000
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · MSP 接入层第二来源一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：给 MSP 客户项目的 24 口 PoE 接入层第二来源（供货连续性+保修），一封到位。
- **要问的问题**：客户项目接入层目前有固定的第二来源位吗？
- **随附证明**：一页报价+规格（英）+ 保修条款。

### 第 2 次跟进 · Perle 类目旁位：高功率 PoE++/万兆上联

- **推什么**：STC-424XGGPM-440W（Saga）（万兆上联通配）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：不碰 Perle 主类：提供 90W/口 PoE++ 与万兆上联通配位（其常见 SKU 之外的空档）。
- **要问的问题**：高功率户外/园区 PoE 需求出现时通常配什么？
- **随附证明**：PoE++ 规格页 + 对比表（英）。

### 第 3 次跟进 · 备件池小批

- **推什么**：STI-280GE（Saga） 等小批
- **切入点**：MSP 项目备件池：8 口/收发器小批常备。
- **要问的问题**：项目备件池走常备价吗？
- **随附证明**：备件小批价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第12批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：都柏林 29 年 MSP：Perle 授权分销（CSV 9-27 记录）；公立/医疗慈善客户面在列——划出经营商业段。
- **产品线与在售品牌**：MSP 托管+云+网安+战略支持；SaaS 伙伴栈（MESH 邮滤/LastPass/Spanning 等首页 logo）。
- **目标行业与场景**：爱尔兰中小企业托管；公立关联与医疗慈善客户段划出。
- **团队与规模**：中型 MSP（24/7 支持口径）。
- **决策链与对接人**：sales@infinitetechnology.ie **唯一启用**（info@ 的 mailto 实跳 help@、CSV 9-27 记录）。
- **技术与认证**：Perle Systems 授权（CSV 9-27 记：工业 PoE 交换/媒体转换/串口联网）。
- **采购与供应链信号**：Perle 类目与我方工业线部分重叠：只谈**高功率 PoE++/万兆上行/L2+ 管理**等类目缺位；MSP 自身客户项目的 24 口接入层是正路。
- **近期动态与线索**：2026 版新站格调=正在强化获客，供应商评估窗口常规化。
- **与我方契合点**：MSP 客户项目 24 口 PoE 接入层第二来源；户外/园区高功率 PoE++ 与 L2+ 管理件（Perle 价带旁位）。
- **风险与注意**：公立客户（Fiscal Advisory Council 等）与医疗慈善段不经由我们；邮件只走 sales@。

### R54 原文证据摘录（全部保留）

- **【业务定位】**都柏林 1997 年 Irish-owned MSP：Managed Services/Cloud/Cybersecurity/Strategic Support，24/7 IT Support。
  > Since 1997, Infinite Technology has proudly served as your local, Irish-owned IT Managed Services provider... delivers 24/7 IT Support, IT Services, Advanced Cloud Solutions, and Cybersecurity Services
  > 来源：https://infinitetechnology.ie/
- **【目标行业与场景】**客户墙含 **National Biodiversity Data Centre、Irish Fiscal Advisory Council（公立关联）与 John of God（医疗慈善）**——公立/医疗慈善客户面占显著位，对应项目段划出不涉。
  > （客户墙）National Biodiversity Data Centre · Irish Fiscal Advisory Council · John of God
  > 来源：https://infinitetechnology.ie/
- **【团队与规模】**计数器：100 客户/月关 1000 工单（另有 50% retention 等动效口径不一致——只取「百家客户/千单」业务感，不引具体数字）。
  > 100 Clients nationwide · 1000 Tickets closed last month
  > 来源：https://infinitetechnology.ie/
- **【决策链与对接人】**销售口 sales@ 优先（官网联系页文字与 mailto 一致）；info@ 文字但 mailto 实为 help@（CSV 9-27 记录）——只走 sales@。
  > （CSV 2026-09-27 记录）官网联系页Sales显示文字与mailto一致；Enquiries显示info@但mailto为help@
  > 来源：https://infinitetechnology.ie/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第24批.json`；价格均为 EXW 快照。

- **①背景再核**：IE MSP（官网一手核）
- **②芯片/型号**：云/安全栈
- **③KP 深挖**：sales@
- **④Saga 对标**：随单正口（$165 锚点一致）
- **⑤在乎与偏好**：响应快/留存信任

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**Since 1997…24/7 IT Support、Advanced Cloud、Cybersecurity——100 clients nationwide
  > Since 1997…24/7 IT Support、Advanced Cloud、Cybersecurity——100 clients nationwide
  > 来源：https://infinitetechnology.ie

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：爱尔兰本地 MSP（1997）
- **产品线与在售品牌**：云/安全/托管（伙伴墙：ME 等未全显）
- **目标行业与场景**：全国 SMB 客户
- **团队与规模**：中型团队
- **决策链与对接人**：sales@ 口
- **技术与认证**：—
- **采购与供应链信号**：随单件
- **近期动态与线索**：—
- **与我方契合点**：MSP 随单正口
- **风险与注意**：伙伴墙未全显（标注）

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Infinite Technology 都柏林 MSP（1997/100 客户）：托管现场随单正口（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：中小
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
  - [ ] 现供品牌
  - [ ] 决策人

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Infinite Technology team,

Since 1997 you have been the managed-services provider Irish businesses call first - 24/7 support, cloud, cybersecurity. Every managed site you win eventually needs a network closet refresh.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29).

One question: when a managed customer site needs switching, where do you source it today - and would a documented value PoE line earn a shelf slot?

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
