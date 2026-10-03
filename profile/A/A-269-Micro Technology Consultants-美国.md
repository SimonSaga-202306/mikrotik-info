# Micro Technology Consultants

> **评级 A**　|　美国 · Warner Robins, GA　|　档案编号 `A-269`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-269
rating: A
country: 美国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: true, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Micro Technology Consultants 佐治亚 K12+SMB（RUCKUS 交换在墙）：SMB/私校段 value 替补（$180 锚点一致）；公立段守界句；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Micro Technology Consultants（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Warner Robins, GA | 事实 |
| 网站 | https://www.microtechnology.net | 事实 |
| 类型 | MikroTik 生态集成商 | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Ruckus（无线与交换）+ Avigilon | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Micro Technology Consultants（美国佐治亚）：K12 与 SMB IT 服务商——网络安全备份/服务器与网络基础设施/站点安防；品牌墙=Avigilon/Verkada/RUCKUS（无线与 Network Switching）/Fortinet/3CX/Clear Touch/Wahsega/HPE 等
- 【推断】K12+SMB：RUCKUS 交换在墙——价值替补窄位；K12=公立教育段守界句（只有私校/商业段可谈）
- 【假设】合规双句后价值替补窄口

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Ruckus（无线与交换）+ Avigilon）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@microtechnology.net
  - 状态：既有/公开
- **电话**：478) 953-1921
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：info@microtechnology.net（官网联系页正文）；另 sales@microtechnology.net；原入口：(478) 953-1921
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 监控/广播项目 24 口 PoE（视频 VLAN 即用）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：英语一封：Avigilon/Wahsega/Verkada 项目的大口数 PoE 接入层（视频/广播 VLAN 预设即插即用+RMA），声明只做商业段、不涉及公立学校采购。
- **要问的问题**：监控/广播项目的大口数 PoE 目前由哪个牌供应？要第二来源吗？
- **随附证明**：一页报价（英）+ 视频 VLAN 预设示例。

### 第 2 次跟进 · 现场宽温小件

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：体育馆/库房/停车场的宽温件与收发器。
- **要问的问题**：户外/库房点位有宽温件需求吗？
- **随附证明**：工业件一页 + 参数。

### 第 3 次跟进 · 话机/3CX 旁位与价卡收口

- **推什么**：PoE 小件 + 价卡留档
- **切入点**：3CX 话机/无线 AP 的 PoE 预算一页+全品类价卡留档；不回即冻结。
- **要问的问题**：（无需回）价卡留档。
- **随附证明**：PoE 预算表 + 价卡各一页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：佐治亚 SMB/K12 集成商（RUCKUS 为交换锚牌+Avigilon/Verkada/Wahsega 监控广播三牌）——监控项目 PoE 接入层真需求。
- **产品线与在售品牌**：网络/服务器/安防三服务；RUCKUS/Avigilon/Verkada/Wahsega/Fortinet/3CX 等 15 牌。
- **目标行业与场景**：K-12 学校与本地 SMB——**K-12/E-Rate 公立资金面划出不涉，只做商业段**。
- **团队与规模**：小型集成商（Wix 站）。
- **决策链与对接人**：info@/sales@microtechnology.net（官网联系页，CSV 9-27）。
- **技术与认证**：（集成商职能型；无 MikroTik 证书面——RUCKUS 体系）。
- **采购与供应链信号**：**RUCKUS 锚位不碰**：Avigilon/Wahsega/Verkada 监控广播项目的 24 口大 PoE 接入层（视频 VLAN 预设旁位）与库房/体育馆现场宽温件。
- **近期动态与线索**：监控+广播双线活跃=PoE 消耗稳定。
- **与我方契合点**：24 口监控 PoE（视频 VLAN 即用模板）→现场宽温件→3CX 话机 PoE 旁位。
- **风险与注意**：K12/E-Rate 公立段不经由我们（首封声明只做商业段）；RUCKUS 锚牌不提替位。

### R54 原文证据摘录（全部保留）

- **【业务定位】**佐治亚 Warner Robins 的 SMB/K12 全包 IT 商：三大服务=网络安全与备份/服务器与网络架构/站点安防（**Surveillance and access control to secure your business or school**）。
  > SITE SECURITY — Surveillance and access control to secure your business or school ‖ SERVER AND NETWORK INFRASTRUCTURE ‖ MICRO TECHNOLOGY CONSULTANTS — Your Trusted IT Partner
  > 来源：https://www.microtechnology.net/
- **【产品线与在售品牌】**信任品牌墙 15 家：Audio Enhancement（**K-12 广播**）/**Avigilon 监控门禁**/**RUCKUS 无线与网络交换**/Fortinet/3CX/Clear Touch/HPE/Cove/Wahsega IP 广播/**Verkada 云监控**/Lenovo/ESET/SentinelOne/Adlumin。
  > PRODUCTS WE TRUST AND SUPPORT — AVIGILON Surveillance and Access Control ‖ RUCKUS Wireless and Network Switching ‖ WAHSEGA IP Intercoms ‖ VERKADA Cloud Surveillance ‖ AUDIO ENHANCEMENT K-12 Intercom
  > 来源：https://www.microtechnology.net/
- **【决策链与对接人】**info@ 与 sales@microtechnology.net 官网联系页正文双箱（CSV 9-27 official-company）；Facebook 具名 Kyle.smith@ 为第三方平台不作直邮。
  > （CSV 2026-09-27 记录）官网联系页正文 info@ 与 sales@microtechnology.net、478-953-1921、Warner Robins 地址；official-company
  > 来源：https://www.microtechnology.net/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第27批.json`；价格均为 EXW 快照。

- **①背景再核**：US GA K12+SMB 服务商（官网一手核）
- **②芯片/型号**：RUCKUS 线
- **③KP 深挖**：info@
- **④Saga 对标**：价值窄位（$180 锚点一致）
- **⑤在乎与偏好**：预算敏感/品牌信任

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**CYBERSECURITY AND BACKUP/SERVER AND NETWORK INFRASTRUCTURE/SITE SECURITY——RUCKUS Wireless and Network Switching 在墙
  > CYBERSECURITY AND BACKUP/SERVER AND NETWORK INFRASTRUCTURE/SITE SECURITY——RUCKUS Wireless and Network Switching 在墙
  > 来源：https://www.microtechnology.net

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：美国佐治亚 K12+SMB IT 服务商
- **产品线与在售品牌**：RUCKUS（含 Switching）/Avigilon/Verkada…
- **目标行业与场景**：K12（公立守界）+SMB
- **团队与规模**：服务商团队
- **决策链与对接人**：info@ 口
- **技术与认证**：—
- **采购与供应链信号**：项目随单
- **近期动态与线索**：—
- **与我方契合点**：SMB/私校段 RUCKUS 旁 value 窄位（公立守界句）
- **风险与注意**：公立段采购规范敏感

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Micro Technology Consultants 佐治亚 K12+SMB（RUCKUS 交换在墙）：SMB/私校段 value 替补（$180 锚点一致）；公立段守界句 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：公立敏感
- **O**：SMB
- **T**：RUCKUS

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
  - [ ] SMB 占比

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Micro Technology team,

Cybersecurity, network infrastructure, site security for K12 and small businesses across Georgia. Two honest notes before the offer: public school projects follow your established procurement path - untouched - and your RUCKUS switching line keeps its place. This concerns only the commercial side.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW (2026-09-29) - a value tier for SMB and private-school projects where budget decides.

One question: on the commercial side, do you keep a value switching tier?

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

- **KP 领英直达**:[Micro Technology Consultants · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Micro%20Technology%20Consultants)(搜索链接,点入后核职位再加;来源:联络核验)
- **中国进口与管制**:国别档位 高(Covered List+SECURE Act+§301 关税;采购方警惕中国标签,话术锚 Marvell(美企)+FCC);战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:待定(档案无芯片信号,首开先问品牌谱)
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
