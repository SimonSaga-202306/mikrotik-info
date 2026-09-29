# MHz Shop

> **评级 A**　|　法国　|　档案编号 `A-352`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-352
rating: A
country: 法国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: true, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — MHz Shop 法 WISP 装备电商（MikroTik/Ubiquiti/Teltonika/Poynting 牌墙）：店目录替补收录窄位（$165 锚点一致）；低密；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

- **关联档警示**：A-506（人-司关联档）→ 互注；首触走 A-506

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | MHz Shop（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 | 事实 |
| 网站 | https://www.mhzshop.com | 事实 |
| 类型 | 分销（Netonix 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Netonix 授权渠道（WISP 接入层交换机） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】MHz Shop（法国）：法国天线/WISP 装备活跃电商：**品牌墙=MikroTik/Ubiquiti/Teltonika/Poynting/RF-Elements/QuWireless/Telegärtner**;PoE 配件区存在；CloudSpot hotspot
- 【推断】店里 PoE 交换仅两大牌=替补收录缝正口（value 对照行）
- 【假设】店目录替补收录窄位

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Netonix 授权渠道（WISP 接入层交换机））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@mhzshop.com
  - 状态：既有/公开
- **电话**：+33 4 86 68 83 30
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：info@mhzshop.com（官网CGV/客服务句；自社FB同）；+33 4 86 68 83 30；Megahertz Wireless Eurl，66320 Marquixanes
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 收录位

- **推什么**：STC-424DGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：店目录替补对照行（两大牌旁）
- **要问的问题**：试收录吗？
- **随附/动作**：规格页

### 第 2 次跟进 · 留档

- **推什么**：—（统一口径=P1 系列，不外溢）
- **切入点**：无响——留档
- **要问的问题**：—
- **随附/动作**：—

### 第 3 次跟进 · 留档

- **推什么**：—（统一口径=P1 系列，不外溢）
- **切入点**：留档
- **要问的问题**：—
- **随附/动作**：—


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第36批.json`；价格均为 EXW 快照。

- **①背景再核**：https://www.mhzshop.com|品牌墙+PoE 配件区双核
- **②芯片/型号**：——
- **③KP 深挖**：WISP 店生态
- **④Saga 对标**：STC-424 替补收录（$165 锚点一致）
- **⑤在乎与偏好**：价格透明文化（€ 明示）

### R55 证据摘录（全部保留 · 含数量）

- **【在售品牌】**By manufacturer: MikroTik/Ubiquiti/Teltonika/MARS/Telegärtner/Poynting + Accessories/PoE 区
  > By manufacturer: MikroTik/Ubiquiti/Teltonika/MARS/Telegärtner/Poynting + Accessories/PoE 区
  > 来源：https://www.mhzshop.com

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：法 WISP 装备电商
- **产品线与在售品牌**：MikroTik/Ubiquiti/Teltonika/Poynting 等
- **目标行业与场景**：WISP/营地/安装商
- **团队与规模**：小微
- **决策链与对接人**：info@ 口
- **技术与认证**：QuWireless 官方分销
- **采购与供应链信号**：库存电商
- **近期动态与线索**：WiFi6/7 新品活跃
- **与我方契合点**：店目录替补收录（两大牌旁对照行）
- **风险与注意**：体量小——低密

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | MHz Shop 法 WISP 装备电商（MikroTik/Ubiquiti/Teltonika/Poynting 牌墙）：店目录替补收录窄位（$165 锚点一致）；低密 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口店
- **W**：体量小
- **O**：收录缝
- **T**：两大牌

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
  - [ ] 替补收录意愿
  - [ ] 首发量

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi MHz Shop team,

Your shop covers the WISP kit end to end - antennas, radios, CPE - but the PoE switch shelf today is essentially MikroTik and Ubiquiti. A documented value option at $165 USD EXW (2026-09-29) could be the honest third row for budget-driven builds.

We build a 24-port Gigabit PoE access switch (280W total budget, 802.3af/at, per-port watchdog, desktop or rack) with full English documentation. Reference: $165 USD EXW (2026-09-29) - a documented value tier beside the lines you already carry, not a replacement.

One question: would your shop test-shelf a documented value PoE switch beside the two incumbents?

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
