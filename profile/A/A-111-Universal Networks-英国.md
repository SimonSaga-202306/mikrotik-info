# Universal Networks

> **评级 A**　|　英国 · Hungerford　|　档案编号 `A-111`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-111
rating: A
country: 英国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: true, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Universal Networks 英 30 年光纤布线（multipartner）：架上 active 补位（$180 锚点一致）；无公开邮箱电话先行；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Universal Networks（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Hungerford | 事实 |
| 网站 | https://www.universalnetworks.co.uk | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| ⚠️ 信息缺口 | 本条**抓不到邮箱**，需人工补齐邮箱或改为电话单独跟进后再进群发名单 | 事实 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Universal Networks（英国 Hungerford）：30 年光纤/布线器材供应商——“30 years’ technical expertise…tailored solutions through a broad range of products from carefully selected industry partners”；咨询电话 01488 685800
- 【推断】无源主干供应商，CSV 载 Allied Telesis 信号=其架上曾有 active 位——Multipartner 模式下 active 补位是天然进函角度
- 【假设】“carefully selected industry partners”=挑件看文档与稳定性，OEM 候选评有门

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：—
  - 状态：缺失（leads-only 口径：人工补录前**不进群发**，与旧批次纪律一致）
- **电话**：+44 1488 685800
- 来源等级：lead（R41–R48 联系方式台账口径）
- **原始联系字段**：No published email found; universalnetworks.co.uk; +44 1488 685800; contact form: https://www.universalnetworks.co.uk/contact-us/; Eddie Hing (Managing Director); LinkedIn: https://uk.linkedin.com/company/universal-networks-ltd
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 工业级非管理 PoE（harsh 环境货架互补）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：同频叙事开场：他卖「扛最狠环境的光纤」，我们卖「扛最狠环境的供电交换」——媒体转换器旁的货架空档提案。
- **要问的问题**：（表单+电话）过滤掉军工线，转播/工业现场的有源交换现在配什么？
- **随附证明**：宽温报告 + 场景对照（光纤↔交换）+ 规格单（英文）。

### 第 2 次跟进 · 24 口 CCTV/PoE（活动现场/场馆网络）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：大型活动现场（Crystal Palace Bowl 场景）的临时网络：24 口 PoE++ 带 AP/摄像头/门禁，与他的部署光纤成套。
- **要问的问题**：活动网络的接入层现在怎么租/怎么采购？
- **随附证明**：场景方案 + 单端口测算 + DIN/机架图。

### 第 3 次跟进 · 管理型 10G（定制方案线的有源端）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他做 bespoke 定制系统：管理型（ERPS/VLAN）作其定制包的有源端选项，按项目注册供货。
- **要问的问题**：定制方案里的有源端要不要加一款可 OEM 贴牌的管理型？
- **随附证明**：项目注册政策 + OEM 说明 + VLAN/ERPS 模板（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第6批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Hungerford 30 年光纤/铜缆专家：加固型可部署光纤（转播/活动/军用野外）+常规布线+媒体转换器，Allied 代理（CSV 记录）。
- **产品线与在售品牌**：ArmourLux 等加固光纤/预端接/走线/媒体转换器/定制方案+在线商店（WooCommerce）。
- **目标行业与场景**：演出与赛事临时光纤、军工野外部署（G7 安保案例）、能源与重工业 harsh 环境。
- **团队与规模**：30 年家族气质公司，具名 Eddie Hing（Managing Director）（CSV 9-27 记录）。
- **决策链与对接人**：⚠️ 无公开邮箱（官网仅表单）：+44 1488 685800；LinkedIn 公司页可作入口（CSV 9-27 核验记录）。
- **技术与认证**：ISO 质量体系 10+ 年（官网）；Allied 代理（CSV 记录）。
- **采购与供应链信号**：harsh 环境场景与我们的宽温工业品同构；媒体转换器旁补工业 PoE 是零冲突类目扩展；军工段（Allen-Vanguard 线）主动划线。
- **近期动态与线索**：持续接演出/活动光纤单（Crystal Palace Bowl 案例 2026-05）。
- **与我方契合点**：加固/野外/宽温叙事完全同频：工业 DIN PoE+2.5G SFP 上他媒体转换器的货架——「线缆之上的一步」。
- **风险与注意**：无邮箱=先 Form+电话双路；军工线（G7/Allen-Vanguard）不碰，只谈转播/活动/工业民用。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网抬头：可依赖的光纤方案 + 30 年技术积累 + 精选厂商伙伴布线供货。
  > A Universal Approach to dependable fibre optics — With 30 years’ of technical expertise, we offer tailored solutions through a broad range of products from carefully selected industry partners.
  > 来源：https://www.universalnetworks.co.uk/
- **【目标行业与场景】**⚠️ 行业页两大方向：Broadcast & Events 与 Military & Defence——军工段划线，转播/活动段与民用 harsh 场景可谈。
  > Industries we serve: Broadcast & Events · Military & Defence（rugged, deployable fibre for harsh environments）
  > 来源：https://www.universalnetworks.co.uk/
- **【产品线与在售品牌】**产品类目含 Network Hardware 下的 Fibre Media Converters（媒体转换器）——有源器件已在货架上，交换层是自然延伸。
  > Portable Deployable Fibre · Fibre Patch Cables · Pre-term Fibre · Bulk Fibre · Fibre Containment · Portable Deployable Copper · Copper Patch Cables · Media Converters（产品类目）
  > 来源：https://www.universalnetworks.co.uk/
- **【团队与规模】**客户墙与证言：Allen-Vanguard（G7 峰会有害环境部署光纤）、Doosan Babcock、National Grid、Extreme E、Faceit、ADI——高门槛项目履历；ISO 质量体系十几年。
  > Allen-Vanguard — Deployable Fibre to Protect World Leaders at G7 Summit · Doosan Babcock · Extreme E · National Grid（Logo 墙）· underpinned by the ISO Quality Standard, which has been integral to Universal for over a decade.
  > 来源：https://www.universalnetworks.co.uk/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第12批.json`；价格均为 EXW 快照。

- **①背景再核**：30 年光纤布线供应（multipartner 挑件文化）
- **②芯片/型号**：Allied 信号（架上 active 位）
- **③KP 深挖**：电话口先行
- **④Saga 对标**：架上 active 补位
- **⑤在乎与偏好**：文档与稳定性

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“30 years’ technical expertise…tailored solutions through a broad range of products from carefully selected industry partners”
  > “30 years’ technical expertise…tailored solutions through a broad range of products from carefully selected industry partners”
  > 来源：https://www.universalnetworks.co.uk/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：英 30 年光纤布线器材供应（multipartner）
- **产品线与在售品牌**：光纤/布线（Allied 信号=架上 active 位）
- **目标行业与场景**：工程商/布线项目
- **团队与规模**：中型供应商
- **决策链与对接人**：01488 685800
- **技术与认证**：30 年专门
- **采购与供应链信号**：multipartner 挑件
- **近期动态与线索**：30 年庆页面
- **与我方契合点**：架上 active PoE 补位
- **风险与注意**：无公开邮箱

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Universal Networks 英 30 年光纤布线（multipartner）：架上 active 补位（$180 锚点一致）；无公开邮箱电话先行 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：专业
- **W**：无邮箱
- **O**：补位
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
| 触达通道 | ❓ 缺邮箱 |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] active 层现供
  - [ ] 挑件门槛
  - [ ] 上架结构

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Universal Networks team,

Thirty years of carefully selecting partners for fibre and cabling - a catalog built on discipline, not volume.

We build one thing: a 24-port Gigabit PoE access switch (280W, 802.3af/at, Voice VLAN, watchdog) with full test documentation. Reference: $180 USD EXW. A natural active-layer companion to a passive-layer catalog.

One question: on your shelves next to the fibre and copper, is there an open slot for a value PoE access switch?

Happy to arrange a brief call at 01488 685800 hours, or send one unit with documentation. If not a fit, one line and I close the loop.

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

- **KP 领英直达**:[Universal Networks · 领英公司页](https://uk.linkedin.com/company/universal-networks-ltd)(既有证据链接,来源:档案;公司页进群后可挑 KP 添加)
- **中国进口与管制**:国别档位 中(NCSC 2027 华为 HNT 移除(电信网);企业网开放;PSTI 合规);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)

## 2026-10-07 R64 KP 猎捕（第 2 波）

**域 MX**:{"universalnetworks.co.uk": ["mail.universalnetworks.com", "mail2.universalnetworks.com", "whitemail.nildram.co.uk"]}
**结论**:Hungerford Berkshire;Company No 04609481;另有 Elizabeth Waterhouse 资深客户经理
- **Eddie Hing** — MD and Founder(COVID 公开信署名+contactout)（源:https://www.universalnetworks.co.uk/we-are-here-to-help-you/）
  - `eddie@universalnetworks.co.uk`(first@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
  - `eddie.hing@universalnetworks.co.uk`(first.last@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
  - `e.hing@universalnetworks.co.uk`(f.last@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
  - `eddiehing@universalnetworks.co.uk`(firstlast@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
  - `ehing@universalnetworks.co.uk`(flast@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
  - `hing@universalnetworks.co.uk`(last@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
- **Kev Begbie** — Technical Manager（源:https://contactout.com/company/Universal-Networks-UK-Ltd-25477）
  - `kev@universalnetworks.co.uk`(first@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
  - `kev.begbie@universalnetworks.co.uk`(first.last@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
  - `k.begbie@universalnetworks.co.uk`(f.last@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
  - `kevbegbie@universalnetworks.co.uk`(firstlast@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
  - `kbegbie@universalnetworks.co.uk`(flast@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
  - `begbie@universalnetworks.co.uk`(last@(universalnetworks.co.uk);guessed-leads-only(域 MX 存活;SMTP 未验;不进群发))
