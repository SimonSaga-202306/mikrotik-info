# Data Connect

> **评级 A**　|　美国　|　档案编号 `A-270`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-270
rating: A
country: 美国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇），三星重点
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Data Connect 美 master stocking 大盘+DCE Made 制造（数百牌墙）：商业/批发段二轨窄口+OEM 辅角（$165 锚点一致）；联邦/州/地方守界句；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Data Connect（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 | 事实 |
| 网站 | https://www.data-connect.com | 事实 |
| 类型 | 集成商/主备货分销（Belden 工业） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Hirschmann + GarrettCom（Belden 工业接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Data Connect（美国 Maryland 等三仓）：**MASTER STOCKING DISTRIBUTOR**——母体握 DSL Warehouse/ClickITDirect/VOIP-Networking/Arc Electronics/IDP/Synxcom/Wireless Network Supply 多实体；既是制造商（DCE Made/旧 Ctek/Relcomm/Telenetics 资产）又是专业大盘：品牌墙数百（Belden/Hirschmann/GarrettCom/Moxa/Perle/EtherWAN/Allied/MIKROTIK 在列）；行业含 Federal Government/State & Local（守界句关键）
- 【推断】巨型分销+自有制造线：双钩——分销侧 value 二轨窄口+制造侧可能合作；联邦/州/地方段守界句必压
- 【假设】商业/批发段的窝口

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Hirschmann + GarrettCom（Belden 工业接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@data-connect.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：sales@data-connect.com（官网联系页正文；未测试投递）；分销商/顾问入口：bpatton@data-connect.com；原入口：见 data-connect.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 分销口：24 口商业 PoE 价位档上架一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：对 bpatton@（分销/顾问口）：其品牌墙价位谱系里补 24 口监控/商业 PoE 价位档上架提案（分销条件+TAC 级规格包）。
- **要问的问题**：商业 PoE 接入层的价位档目前由哪几个牌覆盖？有上架位吗？
- **随附证明**：一页提案（英）+ 规格包。

### 第 2 次跟进 · DCE Made 白牌/OEM 提案

- **推什么**：工业非管理/管理交换机 OEM 线（中性或可贴 DCE 牌）
- **切入点**：单独一封对其制造侧：DCE Made 产品族的交换机白牌/代工供货（CNY 成本位、可做品牌定制），不接政府/国防终向。
- **要问的问题**：DCE Made 线考虑过引入交换机的代工/白牌供应吗？
- **随附证明**：OEM 能力一页 + 定制范围说明。

### 第 3 次跟进 · 工业窄线收口

- **推什么**：STI-280GE（Saga） 等窄线+条款
- **切入点**：工业非管理件窄线价卡+分销条款收口；不回即冻结。
- **要问的问题**：（无需回）条款留档。
- **随附证明**：窄线+条款一页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：美国 30 年总代大厂（七实体三仓）：Belden/Hirschmann+GarrettCom 主备货+TAC 中心——**其 DCE Made 自有线=白牌/OEM 供货位是本库独有切法**。
- **产品线与在售品牌**：自有制造（DCE Made 吸纳 Ctek/Relcomm/Synxcom/Telenetics 产线）+200 牌分销+翻新机+延保。
- **目标行业与场景**：VAR/集成商/批发/WISP/CLEC/ISP 渠道（政府段划出）。
- **团队与规模**：大型总代（三仓多实体）。
- **决策链与对接人**：bpatton@data-connect.com（分销/顾问口，CSV 9-27）；sales@ 总箱；1-888-492-6526。
- **技术与认证**：数百厂牌授权与 TAC（官网 authorizations 页）。
- **采购与供应链信号**：**双轨**：①对其分销渠道=24 口商业 PoE 与工业非管理件的价位档上架；②对其 DCE Made 自有线=OEM/白牌代工供货（本库独有）。
- **近期动态与线索**：Positron 新任 MSD=扩张窗口、品类评审活跃。
- **与我方契合点**：24 口 PoE 上架+工业件窄线+DCE Made 白牌提案三选二节奏走。
- **风险与注意**：政府/国防市场段不经由我们；首封走 bpatton@ 分销口、OEM 话题单独一封不混。

### R54 原文证据摘录（全部保留）

- **【业务定位】**美国 30 年网络边缘连接**主备货分销+制造商**：母体下辖 DSL Warehouse/ClickITDirect/VOIP-Networking/Arc Electronics/Information Data Products/Synxcom/Wireless Network Supply 七实体，MD/NJ/CA 三仓，Positron 官宣其为 Access/Telecom/Power 线 Master Stocking Distributor。
  > MASTER STOCKING DISTRIBUTOR ‖ Data Connect is both a manufacturer and a specialty distributer ‖ Positron announces Data Connect as their Master Stocking Distributor for their Access, Telecom, and Power Product Lines.
  > 来源：https://www.data-connect.com/
- **【产品线与在售品牌】**品牌字母墙逾 200 家：Belden/**Hirschmann/GarrettCom**/Moxa/EtherWAN/ATOP/Perle/MikroTik/Ubiquiti/Allied Telesis/Netgear/Planet/Transition Networks… 另有 **DCE Made 自有产线**+翻新/二手机与延保体系。
  > DATA-CONNECT BRANDS — B&B SMARTWORX · BELDEN · HIRSCHMANN · GARRETTCOM · MOXA · ETHERWAN · ATOP · PERLE · MIKROTIK · UBIQUITI ‖ DCE Made Products ‖ New, Like New, Refurbished and Used Equipment Available
  > 来源：https://www.data-connect.com/
- **【决策链与对接人】**联系页按角色分箱：总 sales@/support@，**分销商与顾问口 Barry bpatton@data-connect.com**（CSV 9-27 official-company 记录）；市场清单含 Federal/State-Local 政府段——划出。
  > （CSV 2026-09-27 记录）官网联系页正文按角色列出：总 sales@/support@，分销商/顾问 Barry Patton bpatton@；official-company ‖ （市场页）Federal Government · State & Local Government（划出）· VARS & Integrators · Wholesale Distribution
  > 来源：https://www.data-connect.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第27批.json`；价格均为 EXW 快照。

- **①背景再核**：US master 大盘+制造（官网一手核）
- **②芯片/型号**：数百墙+DCE Made
- **③KP 深挖**：sales@
- **④Saga 对标**：二轨窄口+OEM 辅角（$165 锚点一致）
- **⑤在乎与偏好**：库存深度/授权完备

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**MASTER STOCKING DISTRIBUTOR——Positron Master Stocking Distributor；DCE Made Products；markets: Federal Government/State & Local Government（守界注）
  > MASTER STOCKING DISTRIBUTOR——Positron Master Stocking Distributor；DCE Made Products；markets: Federal Government/State & Local Government（守界注）
  > 来源：https://www.data-connect.com

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：美国 master stocking 大盘+制造商
- **产品线与在售品牌**：数百品牌+自有线
- **目标行业与场景**：批发/VAR/ISP/WISP；（联邦/州地方=守界）
- **团队与规模**：三仓大盘+制造
- **决策链与对接人**：sales@ 口
- **技术与认证**：数百授权名录
- **采购与供应链信号**：批发泳道+制造成线
- **近期动态与线索**：Positron 新 master 授权
- **与我方契合点**：商业/批发段二轨窄口+边角：自牌 OEM 通道
- **风险与注意**：守界句必压（联邦/州/地方段）

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Data Connect 美 master stocking 大盘+DCE Made 制造（数百牌墙）：商业/批发段二轨窄口+OEM 辅角（$165 锚点一致）；联邦/州/地方守界句 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：体量
- **W**：主权
- **O**：商业段
- **T**：公共段

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
  - [ ] 公共段占比

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Data Connect team,

Master stocking distributor and manufacturer in one house - Belden, Hirschmann, GarrettCom, and your own DCE Made lines across Maryland, New Jersey and California. One boundary sentence: Federal, State and Local Government business stays on your established compliance paths; this offer concerns only the commercial and wholesale side.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29) - a value tier for the commercial distribution channel that does not collide with your flagship lines.

One question: is there a value PoE slot on the commercial side - and is your manufacturing side ever open to co-branded discussion?

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
