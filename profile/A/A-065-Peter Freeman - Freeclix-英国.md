# Peter Freeman / Freeclix

> **评级 A**　|　英国 · Rackheath (Norwich)　|　档案编号 `A-065`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-065
rating: A
country: 英国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: true, oem: true, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE、光纤接入），且有具体人直联
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — FreeClix 英全栈 ISP（Guest WiFi+VoIP 双线）：Voice VLAN 接入层随单；NHS/郡议会公共段守边界（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do you currently badge any switching hardware under your own name, or is everything resold vendor-branded?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Peter Freeman / Freeclix（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Rackheath (Norwich) | 事实 |
| 网站 | freeclix.com | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Peter Freeman | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCSWE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】FreeClix（英国诺里奇）：英国 ISP+托管服务商——商用互联网（专线/FTTP/SOGEA、4G/卫星 fail-over）、无线桥接、**Guest WiFi**、托管/机柜托管、Hosted VoIP/SIP、全英运营商移动接入（含 IoT/M2M SIM）；ISO9001；客户墙：PwC、NHS、诺福克郡议会、Naked Wines、Cosy Club、Auntie Anne’s 等（公私混）
- 【推断】Guest WiFi+酒店餐饮连锁+Hosted VoIP 三线都需要 Voice VLAN/PoE 接入层——餐饮连锁翻修滚动口
- 【假设】酒店/餐饮私域客户（Cosy Club/Auntie Anne’s/Naked Wines）是合规主巷，NHS/Norfolk CC 公共段守边界

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCSWE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN、OEM/白牌
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖
  - OEM/白牌：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@freeclix.com
  - 状态：既有/公开
- **电话**：+44 1603 703340
- **原始联系字段**：+44 1603 703340 / sales@freeclix.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Peter Freeman**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（Guest WiFi 项目接入层）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：他访客 Wi-Fi 项目密集：24 口 PoE++ 一层楼一次带满 AP，4×10G 上行回机房——用 NHS/会所类客户场景对话。
- **要问的问题**：Guest WiFi 项目的接入交换机现在用哪个牌子、预算卡在哪？
- **随附证明**：规格对照 + 英文资料（合规/质保说明齐全版）。

### 第 2 次跟进 · 工业级非管理 PoE（无线链路/室外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他做 wireless links 与 4G/5G failover：室外点位/桅杆旁的宽温 DIN PoE，配 SimRush CPE 同一套备件逻辑。
- **要问的问题**：室外链路点的供电与交换现在用什么组合？
- **随附证明**：宽温报告 + DIN 图 + CPE 组合清单。

### 第 3 次跟进 · 管理型 PoE（托管网标准件+分销试点）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：双线：他自己托管网络的 VLAN 分段标准件；借他 SimRush 分销管道谈首批 SKU 试销（24 口+工业 8 口）。
- **要问的问题**：有没有兴趣在 SimRush 旁边加一条企业交换机线试销？
- **随附证明**：分销价目 + 样机组合 + 英国交付时效说明。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Norwich 企业 ISP + 通信方案商：互联网接入/托管/无线/电话一体化，客户名单含 NHS 与郡政府——英国公共部门也有案例。
- **产品线与在售品牌**：连接（专线/FTTP/4G-5G failover）+ 托管（Co-Lo/VPS）+ 无线链路 + Guest WiFi + 电话 + 移动/eSIM IoT；SimRush Master Distributor 身份说明他习惯代理硬件品牌。
- **目标行业与场景**：英国中小企业办公连接、商业场所访客 Wi-Fi、分支机构组网；公共部门（NHS/郡议会）项目要求流程合规。
- **团队与规模**：公司化运作（诺里奇 Rackheath 办公点），客服+工程师班底，Google 4.9 分，WhatsApp 直达。
- **决策链与对接人**：Peter Freeman（+44 1603 703340 / sales@freeclix.com）。
- **技术与认证**：MTCNA+MTCSWE（CSV 名录记录）；ISO9001 流程意味着供应商资料要齐全（合规文件先行）。
- **采购与供应链信号**：项目+自有网络双需求：客户现场的 AP/交换与他自己的 POP 点；SimRush 分销管道跑通后，加第二个硬件线顺理成章。
- **近期动态与线索**：持续在签公共部门与连锁商业客户（客户墙更新中），访客 Wi-Fi 项目量大。
- **与我方契合点**：Guest WiFi 项目=PoE AP 接入层；无线链路/室外点位=工业件；他有分销资质与管道，是「客户+渠道」双重价值。
- **风险与注意**：服务 NHS/政府客户对产地与合规文件敏感：提前备齐 CE/UKCA 类声明，首轮别急着推大单。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网抬头：英国 ISP，帮企业客户简化通信与网络。
  > We are a UK internet service provider. · We simplify business telecommunications.
  > 来源：https://freeclix.com/
- **【产品线与在售品牌】**完整企业通信栈：专线/FTTP/SOGEA 宽带、托管机房与 VPS、无线链路与访客 Wi-Fi、VoIP 电话、云 SaaS 与移动数据。
  > Internet Connectivity — Uninterrupted Hosting, Secure Co-Location, Internet Access · Wireless Services — Network Consultancy, wireless Links, Managed Infrastructure, Guest WIFI · Business grade internet access. Leased Lines, FTTP, SOGEA. Mobile and Satellite Failover.
  > 来源：https://freeclix.com/
- **【团队与规模】**官网「we are trusted by」客户墙：NHS（国民医疗）、PWC、Norfolk 郡政府、Naked Wines 等；流程过 ISO9001 质量认证。
  > We are trusted by — NHS · PWC · NORFOLK CC · WILCO MOTORS · NAKED WINES · COSY CLUB … Our processes are certified for quality (ISO9001).
  > 来源：https://freeclix.com/
- **【技术与认证】**持 MTCSWE 且为 SimRush（英国户外 4G/5G CPE 品牌）Master Distributor——既懂交换又有分销管道（来源性质：CSV 既有记录）。
  > 持 MTCSWE；4G/5G 方案、ISP 服务、光纤专线/xDSL/FTTC、机柜托管、语音；SimRush Master Distributor（CSV 备注）
  > 来源：https://mikrotik.com/consultants

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第7批.json`；价格均为 EXW 快照。

- **①背景再核**：英国 ISP 全栈：Guest WiFi/VoIP/无线桥/移动 IoT；ISO9001；公私混客墙
- **②芯片/型号**：未公开硬件架
- **③KP 深挖**：Freeman sales@ 直达
- **④Saga 对标**：Voice VLAN 24 口 PoE 配 VoIP/Wi-Fi 双线
- **⑤在乎与偏好**：质量档（ISO）+托管节奏

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“We are a UK internet service provider…Guest WIFI…Hosted VoIP, Phone Systems…trusted by PwC, NHS, Norfolk CC, Cosy Club, Auntie Anne’s”
  > “We are a UK internet service provider…Guest WIFI…Hosted VoIP, Phone Systems…trusted by PwC, NHS, Norfolk CC, Cosy Club, Auntie Anne’s”
  > 来源：https://freeclix.com/
- **【联系方式】**sales@freeclix.com +44 1603 703340；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > sales@freeclix.com +44 1603 703340；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://freeclix.com/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：英国 ISP 全栈托管商（互联网/无线/VoIP/移动/Guest WiFi）
- **产品线与在售品牌**：自有服务+运营商代理
- **目标行业与场景**：酒店餐饮连锁/商企/（公共部分存在）
- **团队与规模**：中型 ISP
- **决策链与对接人**：Peter Freeman（MTCNA+MTCSWE）sales@
- **技术与认证**：ISO9001
- **采购与供应链信号**：连锁项目滚动+VoIP 线 VoWiFi 配位
- **近期动态与线索**：客户墙持续扩（2024-25 新增）
- **与我方契合点**：Guest WiFi/VoIP 的 Voice VLAN 接入层随行
- **风险与注意**：公共账户段边界明确

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | FreeClix 英全栈 ISP（Guest WiFi+VoIP 双线）：Voice VLAN 接入层随单；NHS/郡议会公共段守边界（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：全栈
- **W**：边界
- **O**：滚动
- **T**：大厂

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
| 决策人识别 | ✅ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 连锁项目量
  - [ ] 接入层现供
  - [ ] 监控体系

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Peter,

FreeClix bundles exactly the three things that meet in one access cabinet - guest WiFi, hosted VoIP and wireless backhaul. That is a clean design decision if the switching layer cooperates.

Our 24-port PoE switch (280W, 802.3af/at, Voice VLAN, watchdog self-healing) is built for exactly that closet. Reference: $180 USD EXW.

One question: in a typical Cosy Club-style venue you wire, how are voice and guest WiFi separated today?

If useful, I can send one unit with a VLAN sample config. If not a fit, one line and I close the loop.

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
