# Joost Van De Weijer

> **评级 A**　|　荷兰 · Bladel　|　档案编号 `A-261`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-261
rating: A
country: 荷兰
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: true, l2plus: true, voice: true, oem: false, hotel: false, training: false}
p1: CONSULT-OEM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），三星重点
- **P1（首触唯一主推）**：OEM/白牌合作探询（无量产型号首推） — IP Techniek 荷 Bladel 个体顾问（薄站）：顾问项目随件窄口（$180 锚点一致）；训练通道判；—（合作探询，无量产报价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Joost Van De Weijer（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 荷兰 / Bladel | 事实 |
| 网站 | https://iptechniek.nl | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证顾问，持 MTCRE MTCWE MTCTCE MTCINE MTCSWE MTCEWE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】IP Techniek（荷兰 Bladel，Joost Van De Weijer）：极简页=电话+数据通信顾问；CSV=MikroTik 官方认证顾问（MTCRE/MTCWE 等）
- 【推断】个体顾问=训练通道判（CONSULT-OEM）；站极薄，顾问身份为主证
- 【假设】顾问项目里的装备对照/随件窄口——低密针

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问，持 MTCRE MTCWE MTCTCE MTCINE MTCSWE MTCEWE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@iptechniek.nl
  - 状态：既有/公开
- **电话**：—
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：sales@iptechniek.nl（关联公司官网正文；个人归属/现任职限制见备注）；原入口：MikroTik 顾问名录
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（OEM/白牌合作探询（无量产型号首推）），备选型不进邮件。

### 第 1 次跟进 · VoIP/小项目 24 口 PoE 接入层一页

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：荷语/英语一封到 sales@：电话+网络项目的 24 口 PoE++ 接入层第二来源（供货连续性+RMA 随行）。
- **要问的问题**：您交付的电话/网络项目，接入层目前固定配哪个牌？有第二来源位吗？
- **随附证明**：一页报价（荷/英）+ 保修条款。

### 第 2 次跟进 · 商铺/库房宽温小件

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：客户现场（车库/库房/楼层间）的宽温小件与收发器。
- **要问的问题**：现场环境有宽温/机柜受限的点位吗？
- **随附证明**：工业件一页 + -40~75°C 参数。

### 第 3 次跟进 · 价卡留档收口

- **推什么**：—（价卡留档）
- **切入点**：全品类价卡留档、不催单；无回复即冻结。
- **要问的问题**：（无需回）价卡留档。
- **随附证明**：全品类一页价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Bladel 电话+数据通信小店（单页站+TeamViewer 支持链接）；Joost 六证含 MTCSWE=技术型买手。
- **产品线与在售品牌**：（站极简无目录；按 CSV：MikroTik 顾问型集成/运维服务）。
- **目标行业与场景**：当地 SMB 的电话系统（VoIP）+数据网络项目——**VoIP 话机/AP 的 PoE 接入层是天然对口**。
- **团队与规模**：主理人单店。
- **决策链与对接人**：sales@iptechniek.nl（官网首页正文，CSV 9-27 official-company；个人归属按备注限制走公司箱）。
- **技术与认证**：六证 MikroTik 顾问（CSV）。
- **采购与供应链信号**：顾问自己设计+采购：PoE 接入层第二来源话术直通（ERPS/VLAN/CLI 语言有效）。
- **近期动态与线索**：站常年单页=轻营销重交付；无负面信号。
- **与我方契合点**：VoIP/监控小项目的 24 口 PoE 接入层+商铺/办公室小件。
- **风险与注意**：单页站目录零信息——外联只凭顾问身份与邮箱，一步一问问清他是否在接项目。

### R54 原文证据摘录（全部保留）

- **【业务定位】**布拉班特 Bladel 的电话与数据通信店（站题 Telefonie en Data Communicatie）：官网为单页名片型，直接给地址/电话/销售邮箱与 TeamViewer 远程支持入口。
  > Ip Techniek Telefonie en Data Communicatie ‖ IP Techniek, Raamloop 3, 5531PC, Bladel ‖ T. 0497-741013, E. sales@iptechniek.nl
  > 来源：https://iptechniek.nl/
- **【技术与认证】**Joost 持 MikroTik 六证含 MTCSWE，官方顾问名录收录（CSV 9-23/27 记录）；LinkedIn 显示其任职 IPtechniek.nl、教育与 MikroTik 网络方向一致。
  > （CSV 2026-09-23/27 记录）MikroTik 官方认证顾问名录收录；持 MTCRE/MTCWE/MTCTCE/MTCINE/MTCSWE/MTCEWE；official-company
  > 来源：https://iptechniek.nl/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第27批.json`；价格均为 EXW 快照。

- **①背景再核**：NL 个体 MikroTik 顾问（官网+CSV 双核）
- **②芯片/型号**：MikroTik 生态
- **③KP 深挖**：sales@
- **④Saga 对标**：顾问对照（$180 锚点一致，低密）
- **⑤在乎与偏好**：小而灵活

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**IP Techniek…Telefonie en Data Communicatie——MikroTik 官方认证顾问名录收录（CSV 9-23）
  > IP Techniek…Telefonie en Data Communicatie——MikroTik 官方认证顾问名录收录（CSV 9-23）
  > 来源：https://iptechniek.nl

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：荷兰个体 ICT 顾问
- **产品线与在售品牌**：—
- **目标行业与场景**：SMB 电话/数据顾问
- **团队与规模**：个体
- **决策链与对接人**：sales@ 具名（Joost）
- **技术与认证**：MikroTik 认证顾问
- **采购与供应链信号**：顾问随件
- **近期动态与线索**：—
- **与我方契合点**：顾问窄口（CONSULT-OEM）
- **风险与注意**：薄站低信号

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | OEM/白牌合作探询（无量产型号首推） | 主场景 | —（合作探询，无量产报价） | IP Techniek 荷 Bladel 个体顾问（薄站）：顾问项目随件窄口（$180 锚点一致）；训练通道判 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424XGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：OEM/白牌合作：中性包装、贴客户型号、ODM 规格，MOQ 与认证另谈
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：专业
- **W**：极小
- **O**：随件
- **T**：边界

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
  - [ ] 存量项目
  - [ ] 随件意愿

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Joost,

Telephony and data communications advice, and I found your name in the MikroTik certified consultants directory - you carry the certs that make networks behave. Full honesty: we build PoE switches, not RouterOS boxes.

Where we might serve: a documented engineering-grade 24-port Gigabit PoE switch (280W, 802.3af/at; reference $180 USD EXW, 2026-09-29) for consulting projects where a customer site needs switching beside whatever routing stack you choose.

One question: when your projects need switches, who supplies them today - or is hardware sourcing left to the client?

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

- **KP 领英直达**:[Joost Van De Weijer](https://www.linkedin.com/in/joost-van-de-weijer-86482a179)(既有证据链接,来源:档案/联络核验)
- **中国进口与管制**:国别档位 中(NCSC 政府供应商排除;企业网自由);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-424XGGPM-280W(48G PoE++/4×25G→智算安防酒店全谱)(本行为调查分析结论,与开发信首推型号是两回事)
