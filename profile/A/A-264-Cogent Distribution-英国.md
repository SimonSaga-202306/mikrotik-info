# Cogent Distribution

> **评级 A**　|　英国 · Newbury, Berkshire　|　档案编号 `A-264`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-264
rating: A
country: 英国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: true, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），三星重点
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Cogent Distribution 英无线连接 VAD（Switches 类目 Teltonika/Perle 在墙）：二轨价值窄口（$165 锚点一致）；分销守界前句；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Cogent Distribution（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Newbury, Berkshire | 事实 |
| 网站 | https://www.cogentdistribution.com | 事实 |
| 类型 | 分销/集成商（Perle 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Cogent Distribution（英国）：无线+连接件 VAD——固定无线（RADWIN 图）/路由网关（Teltonika）/**Switches 类目（Teltonika TSW 图）**/天线/光谱仪/5G-LTE/设备服务器/媒体转换等；VAR-集成商+行业+消费者三通道；CSV=Perle 授权
- 【推断】VAD 有明设 Switches 类目——Teltonika TSW 级之上存在 value 替补窄口（分销守界前句）
- 【假设】其转售管线的 value PoE 接入二轨

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：enquiries@cogentdistribution.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：enquiries@cogentdistribution.com（官网联系页正文；未测试投递）；原入口：见 Perle 名录（distributor=656）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · Switches 类目扩品：24 口监控 PoE 上架一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：对 enquiries@：Switches 类目目前只有小型工业款——补 24 口 CCTV/商业 PoE 接入层的供应商上架提案（分销条件+英语资料包+梯价）。
- **要问的问题**：Switches 类目有扩 24 口商业 PoE 货架位的计划吗？
- **随附证明**：上架一页提案（英）+ 证书包。

### 第 2 次跟进 · 工业宽温件线

- **推什么**：STI-280GE（Saga） / STI-480DGGM（Saga）（ERPS）
- **切入点**：交通/港口垂直行业客户的现场宽温件与环网件线。
- **要问的问题**：交通/港口类项目的现场宽温件谁在供？
- **随附证明**：工业件一页 + 宽温参数。

### 第 3 次跟进 · 光铜配件窄线

- **推什么**：SFP/收发器 目录
- **切入点**：Device Servers/Media Converters 邻位的光配件窄线低价档。
- **要问的问题**：SFP/收发器窄线有补价位档需求吗？
- **随附证明**：配件价卡一页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：英国无线/连接 VAD（RADWIN/Teltonika/RF elements/Peplink/SAF 微波系）——**交换类目存在但只有 Teltonika 小工业款=空档精准**。
- **产品线与在售品牌**：13 类目含 Switches/Device Servers/Media Converters 等（Perle 授权为旧记录标签，本轮未重读名录不重复背书）。
- **目标行业与场景**：VAR/集成商渠道+垂直行业（港口/交通等轮播图）。
- **团队与规模**：中型 VAD（在线商城+方案设计服务）。
- **决策链与对接人**：enquiries@cogentdistribution.com（官网联系页，CSV 9-27）。
- **技术与认证**：多牌厂商认证依据官方手册；Teltonika/RF elements 等在架。
- **采购与供应链信号**：**交换类目扩品逻辑**：TSW 小工业之外缺 24 口商业监控 PoE 与更宽温工业管理件——两段提案。
- **近期动态与线索**：「fast-growing」自述+快速上新记录=供应商评估窗口常在。
- **与我方契合点**：24 口 CCTV PoE 上架提案+工业宽温件线扩品。
- **风险与注意**：其无线为主业：别把交换说成其核心，提案以「补齐连接解决方案最后一公里」为框。

### R54 原文证据摘录（全部保留）

- **【业务定位】**纽伯里的无线与连接增值分销（VAD）快速成长者：自述 stocking and selling best-of-breed connectivity equipment，服务对象 VAR/集成商/垂直行业/消费端四类。
  > We’re a fast-growing value-added distributor (VAD) focused on stocking and selling best-of-breed connectivity equipment ‖ For resellers (VARs) and system integrators, we don’t just supply premium connectivity products but solutions design…
  > 来源：https://www.cogentdistribution.com/
- **【产品线与在售品牌】**13 个产品类目：Fixed Wireless（RADWIN）/Routers&Gateways（Teltonika RUT 图）/**Switches（页面配图为 Teltonika TSW200）**/Antennas（RF elements）/频谱仪（SAF）/5G&LTE（Peplink）/信号增强/Device Servers/Ethernet Extenders/Serial Extenders/Media Converters/配件——**交换类目现仅小型工业款**。
  > Switches —（类目配图为 Teltonika Networks TSW200）‖ Device servers · Ethernet extenders · Serial extenders · Media converters
  > 来源：https://www.cogentdistribution.com/
- **【决策链与对接人】**enquiries@cogentdistribution.com 官网联系页正文（CSV 9-27 official-company）；2023 官方手册另有 sales@/solutions@ 部门入口。
  > （CSV 2026-09-27 记录）官网联系页正文给 enquiries@cogentdistribution.com 与 +44 (0)1635 917 722、Newbury 地址；official-company
  > 来源：https://www.cogentdistribution.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第27批.json`；价格均为 EXW 快照。

- **①背景再核**：UK 无线连接 VAD（官网一手核）
- **②芯片/型号**：Teltonika/Perle 等墙
- **③KP 深挖**：enquiries
- **④Saga 对标**：二轨窄口（$165 锚点一致）
- **⑤在乎与偏好**：best-of-breed 组合/又快又好供货

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**value-added distributor stocking wireless and connectivity…products: Fixed wireless/Routers/Switches/Antennas——VARs & Integrators 通道
  > value-added distributor stocking wireless and connectivity…products: Fixed wireless/Routers/Switches/Antennas——VARs & Integrators 通道
  > 来源：https://www.cogentdistribution.com

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：英国无线连接 VAD
- **产品线与在售品牌**：RADWIN/Teltonika/Peplink/Perle…
- **目标行业与场景**：VAR/集成商+行业垂直
- **团队与规模**：分销团队
- **决策链与对接人**：enquiries 口
- **技术与认证**：—
- **采购与供应链信号**：分销泳道
- **近期动态与线索**：行业垂直页在扩
- **与我方契合点**：Switches 类目内二轨窄口（守界前句）
- **风险与注意**：SKU 主权强——前句框定

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Cogent Distribution 英无线连接 VAD（Switches 类目 Teltonika/Perle 在墙）：二轨价值窄口（$165 锚点一致）；分销守界前句 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：主权
- **O**：二轨
- **T**：墙

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
  - [ ] 类目负责人

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Cogent Distribution team,

A growing VAD for wireless broadband and connectivity - RADWIN links, Teltonika gateways and switches, Peplink, device servers, media converters - with a real Switches category on the shelf. One sentence up front: we are not asking to displace any line you stock.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29) - a value tier your resellers can carry beside the current switching offers.

One question: is there room for a value PoE tier in your Switches category - and would you evaluate one unit?

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
