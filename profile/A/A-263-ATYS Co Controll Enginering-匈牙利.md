# ATYS Co Controll Enginering

> **评级 A**　|　匈牙利 · Budapest　|　档案编号 `A-263`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-263
rating: A
country: 匈牙利
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: true, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — ATYS-CO 匈牙利近30年自动化集团（Westermo Reseller）：项目随单+贸易部上架双通道（$165 锚点一致）；Westermo 旁前句框定；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | ATYS Co Controll Enginering（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 匈牙利 / Budapest | 事实 |
| 网站 | https://www.atysco.hu | 事实 |
| 类型 | 集成商/代理（Westermo） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Westermo（工业接入层交换机） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】ATYS-CO Kft（匈牙利，近三十年工业自动化集团）：过程控制/自动化系统设计+施工+全生命周期运维；贸易部 20 年主打工业电源销售；2009 加可再生能源部；CSV=Westermo Reseller
- 【推断】自动化承包+贸易双主业：项目里的工业网络件随单真实存在（Westermo 在墙），贸易部自带分销能力
- 【假设】自动化项目 PoE 接入随单（Westermo 旁 value 替补）+贸易部上架双角

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Westermo（工业接入层交换机））

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

- **邮箱**：sales@atysco.hu
  - 状态：既有/公开
- **电话**：+36 1 263 2561
- 来源等级：official-obfuscated-company（R41–R48 联系方式台账口径）
- **原始联系字段**：sales@atysco.hu（官网正文公开；官方页另有可逆(at)/(dot)写法；未测试投递）；原入口：+36 1 263 2561
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · Westermo 邻位工业第二来源一页

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：匈语/英语一封到 sales@：过程自动化项目的工业非管理宽幅价位档第二来源（CE/宽温参数一体），只谈价位档不碰其锚牌排位。
- **要问的问题**：自动化盘的网络接入件有没有一个更友善价位的第二来源需求？
- **随附证明**：工业件一页 + CE/EMC/宽温参数。

### 第 2 次跟进 · 光伏场/户外 PoE 与 ERPS 环

- **推什么**：STI-480DGGM（Saga）（工业管理 8×电口 + 4×千兆上联，ERPS）
- **切入点**：新能源分部的户外柜监控 PoE+光纤环网。
- **要问的问题**：光伏场的户外监控/环网件目前怎么配？
- **随附证明**：ERPS 环配置示例 + 光伏场景拓扑图。

### 第 3 次跟进 · 商贸线分销条款

- **推什么**：—（条款）
- **切入点**：其商贸线的窄线分销条款（中性发货/梯价）收口；不回即冻结。
- **要问的问题**：（无需回）条款留档。
- **随附证明**：分销条款一页（英）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：匈牙利工业自动化集团（30 年，设计+实施+运维全周期）——Westermo Reseller+自有商贸线=工业件真买家。
- **产品线与在售品牌**：工业控制自动化工程+工业电源分销+光伏新能源分部（RO 姐妹公司覆盖中东欧）。
- **目标行业与场景**：过程工业/制造厂自动化；光伏电场=户外宽温件场景。
- **团队与规模**：中型集团（三板块+扩编中自述）。
- **决策链与对接人**：sales@atysco.hu（官网正文/可逆写法，CSV 9-27）；+36 1 263 2561。
- **技术与认证**：Westermo Reseller（CSV 伙伴记录）。
- **采购与供应链信号**：Westermo 锚位在——**同规格 1/3 价工业第二来源**话术直通；光伏场户外柜宽温件、过程网 ERPS 环。
- **近期动态与线索**：进军机器人+自动化扩编=网络件增量窗口。
- **与我方契合点**：工业非管理宽温 8 口低价档+ERPS 环管理机+光伏场 PoE（球机/传感）。
- **风险与注意**：Westermo 锚位不碰；匈语对接佳；集团多板块一封别铺太广、先工业网配件类。

### R54 原文证据摘录（全部保留）

- **【业务定位】**布达佩斯约 30 年的**工业控制/自动化集团**：自述设计并实施过程控制-自动化系统且全生命周期运维，三大板块=工业服务+商贸+可再生能源（2009 起），正进军机器人。
  > Nem csupán megtervezzük és kivitelezzük a folyamatirányítási-automatizálási rendszereket, hanem a teljes életciklusukon keresztül üzemeltetjük ‖ kereskedelem — ipari tápegységek forgalmazása ‖ megújuló energia (2009)
  > 来源：https://www.atysco.hu/
- **【产品线与在售品牌】**工业服务（设计/软硬件开发/实施/维护）+商贸线（自述**工业电源分销为主干**）+新能源分部；Westermo Reseller（CSV 伙伴等级记录；罗马尼亚 ATYS-co 同属一家覆盖中东欧两国）。
  > a kereskedelem, amelynek gerincét az ipari tápegységek forgalmazása jelenti ‖ （CSV 记录）Westermo Reseller；与 ATYS-co Romania 同属一家
  > 来源：https://www.atysco.hu/
- **【决策链与对接人】**sales@atysco.hu 官网正文公开（另 EN 页 atysco[at]…、HU 页 kukac/pont 可逆写法、销售箱与总经理 Ottó Jász 具名箱——CSV 9-27 official-obfuscated-company）。
  > （CSV 2026-09-27 记录）官网联系页可逆写法+正文销售邮箱 sales@atysco.hu、总经理具名邮箱；official-obfuscated-company
  > 来源：https://www.atysco.hu/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第27批.json`；价格均为 EXW 快照。

- **①背景再核**：HU 自动化集团（官网一手核）
- **②芯片/型号**：Westermo 线
- **③KP 深挖**：sales@
- **④Saga 对标**：随单+贸易双角（$165 锚点一致）
- **⑤在乎与偏好**：全生命周期/本土承包

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**irányítástechnika——jelentős kivitelezői kapacitás;kereskedelem gerincét az ipari tápegységek forgalmazása（20 年）
  > irányítástechnika——jelentős kivitelezői kapacitás;kereskedelem gerincét az ipari tápegységek forgalmazása（20 年）
  > 来源：https://www.atysco.hu

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：匈牙利自动化集团（近 30 年）
- **产品线与在售品牌**：Westermo+工业电源
- **目标行业与场景**：过程工业/制造厂
- **团队与规模**：承包集团规模
- **决策链与对接人**：sales@ 口
- **技术与认证**：—
- **采购与供应链信号**：承包随单+贸易上架
- **近期动态与线索**：机器人/自动化扩张叙事
- **与我方契合点**：项目随单+贸易双通道（Westermo 旁守界前句）
- **风险与注意**：Westermo 主权——前句框定

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | ATYS-CO 匈牙利近30年自动化集团（Westermo Reseller）：项目随单+贸易部上架双通道（$165 锚点一致）；Westermo 旁前句框定 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：双通道
- **W**：Westermo
- **O**：替补
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
  - [ ] 贸易部负责人

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hello ATYS-CO team,

Nearly three decades in process control and industrial automation - engineering, implementation, lifecycle maintenance - plus a trading arm built on industrial power supplies for twenty years. One sentence up front: where you run Westermo today, we are not asking to displace it.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29) - a value substitute that can serve both your project sites and your trading shelf.

One question: does ATYS-CO keep a value tier for industrial switching - and would you evaluate one unit?

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
