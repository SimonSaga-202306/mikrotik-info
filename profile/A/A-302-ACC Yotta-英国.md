# ACC Yotta

> **评级 A**　|　英国 · Woking　|　档案编号 `A-302`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-302
rating: A
country: 英国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — ACC Yotta 英应用方案屋（自有 DC+AT 专区）：私营段（酒店/零售/法律金融）二槽窄位（$180 锚点一致）；航空防务证言守界句；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | ACC Yotta（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Woking | 事实 |
| 网站 | https://www.accyotta.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】ACC Yotta（英国 Woking）：应用专注 IT 方案屋——自有数据中心托管（APP:HOST/APP:LINK）、商业连续性、群集存储、安全；行业=航空航天/教育/企业/酒店活动/法律金融/零售；品牌导航明列 **ALLIED TELESIS 专区**+Brocade/Palo Alto/Scale/Spectra；首页存一桩 'Aerospace and Defence' 客户（Safran Labinal）证言
- 【推断】中大型混合行业方案商：AT 在墙但非独家——私营段（酒店/零售/法律金融）二轨窄位；航空防务证言=守界句必压
- 【假设】其私营段客户现场的 value PoE 二槽窄位

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：contact@accyotta.com
  - 状态：既有/公开
- **电话**：+44 (0)20 7043 6090
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：contact@accyotta.com（官网联系页正文；支持候选help@accyotta.com）；+44 (0)20 7043 6090
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 应考型一页：24 口 PoE++（RMA 背书）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：呼其「考核厂商」名言：提交 24 口 PoE++ 接入层供评估——供货连续性/RMA 流程/规格全参数一体（声明不涉防务与公立教育项目）。
- **要问的问题**：接入层目前在你的 portfolio 里由谁占？愿意评一家新供应商吗？
- **随附证明**：全参数一页+RMA/连续性说明。

### 第 2 次跟进 · 托管机房 DAC/SFP 自用位

- **推什么**：DAC/AOC + SFP/SFP+ 目录
- **切入点**：APP:HOST 机房互连配件批量位。
- **要问的问题**：机房互连配件走常备吗？
- **随附证明**：配件一页价卡+兼容表。

### 第 3 次跟进 · 价卡留档收口

- **推什么**：—（价卡留档）
- **切入点**：全品类价卡留档；无回复即冻结。
- **要问的问题**：（无需回）价卡留档。
- **随附证明**：全品类一页价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第16批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：萨里应用托管/支持商（「考核厂商支持与供应链」名言=愿评新供应商的信号）。
- **产品线与在售品牌**：APP:LINK/APP:HOST/存储/监控/安全；Allied/Brocade/Palo Alto/Scale/Spectra 品牌区。
- **目标行业与场景**：法律金融/零售/酒店活动/企业商业四域（防务+公立教育两域划出）。
- **团队与规模**：中型（自有 APP: 产品线+海外客户）。
- **决策链与对接人**：contact@accyotta.com（官网联系页，CSV 9-27）。
- **技术与认证**：Allied 专区在站（CSV+品牌导航）。
- **采购与供应链信号**：**其名言即开门**：只给他们能「过考核」的东西——24 口 PoE++ 带 RMA/供应链连续性背书+数据中心 DAC/SFP 互连件。
- **近期动态与线索**：APP:HOST 托管线=机房互连件自用位。
- **与我方契合点**：接入层（RMA 体系话术）+DAC/SFP 自用位。
- **风险与注意**：防务（Safran 证言面）与公立教育域不经由我们；考核型买手资料必须全参数别水。

### R54 原文证据摘录（全部保留）

- **【业务定位】**萨里 Woking 的应用中心 IT 商：APP:LINK 应用支持/APP:HOST 托管/业务连续性/集群存储/监控/网络安全——**公开自述「连厂商都要考核：支持与供应链过关才进目录」**=供应商评估话术直通。
  > We love testing products, but it's important we test the vendors behind them too. Only when we are completely satisfied with a vendor's support, & supply chain will consider adding a product to our solution portfolio.
  > 来源：https://www.accyotta.com/
- **【目标行业与场景】**六行业：Aerospace（Safran Labinal 证言明写 Aerospace **and Defence**——**防务客户面划出**）/Education（公立教育面划出）/Enterprise/Hospitality & Events/Legal & Finance/Retail——商业四域可做。
  > （证言）As a large organisation involved in Aerospace and Defence, unfortunately we can’t provide detail… ‖ SECTORS — aerospace · education · enterprise · hospitality & events · legal & finance · retail
  > 来源：https://www.accyotta.com/
- **【决策链与对接人】**contact@accyotta.com 官网联系页正文+支持 help@（CSV 9-27 official-company）；官网品牌导航含 ALLIED TELESIS 专区。
  > （CSV 2026-09-27 记录）官网联系页给 contact@accyotta.com、+44 (0)20 7043 6090 与 Woking Acacia House；official-company
  > 来源：https://www.accyotta.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第31批.json`；价格均为 EXW 快照。

- **①背景再核**：UK 方案屋（官网一手核）
- **②芯片/型号**：AT/Brocade 线
- **③KP 深挖**：contact@
- **④Saga 对标**：二槽窄位（$180 锚点一致）
- **⑤在乎与偏好**：bench-tested 实测文化/应用专注

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**bench tested, performance proven solutions…BRANDS: ALLIED TELESIS/BROCADE/PALO ALTO——SECTORS: Aerospace/Education/Hospitality/Legal/Retail
  > bench tested, performance proven solutions…BRANDS: ALLIED TELESIS/BROCADE/PALO ALTO——SECTORS: Aerospace/Education/Hospitality/Legal/Retail
  > 来源：https://www.accyotta.com

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：英国应用专注 IT 方案屋
- **产品线与在售品牌**：ALLIED TELESIS/Brocade/Palo Alto/Scale
- **目标行业与场景**：酒店/零售/法律金融（航空防务=守界注）
- **团队与规模**：中型组织
- **决策链与对接人**：contact@ 口
- **技术与认证**：—
- **采购与供应链信号**：项目随单+托管
- **近期动态与线索**：自有 DC 运营中
- **与我方契合点**：私营段二轨窄位（守界句在）
- **风险与注意**：航防证言——前句框定

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | ACC Yotta 英应用方案屋（自有 DC+AT 专区）：私营段（酒店/零售/法律金融）二槽窄位（$180 锚点一致）；航空防务证言守界句 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：行业宽
- **W**：在墙
- **O**：私营段
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
  - [ ] 替补机制
  - [ ] 托管客户占比

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi ACC team,

Bench-tested, performance-proven solutions with your own datacenters behind them - and Allied Telesis holding a real position on your brand shelf. Two honest sentences up front: your AT line keeps its place, and anything in the aerospace-and-defence orbit stays on your certified paths. This concerns only the commercial side.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW (2026-09-29) - a value second slot for hospitality, retail, legal and finance projects.

One question: on the commercial side, is there room for a documented value PoE tier?

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

- **KP 领英直达**:[ACC Yotta · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=ACC%20Yotta)(搜索链接,点入后核职位再加;来源:联络核验)
- **中国进口与管制**:国别档位 中(NCSC 2027 华为 HNT 移除(电信网);企业网开放;PSTI 合规);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
