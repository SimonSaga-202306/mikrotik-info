# 5G IT Service GmbH

> **评级 A**　|　德国 · Reken　|　档案编号 `A-133`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-133
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — 5G IT NRW：Allied 伙伴实版印证→第二供位 value 线（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | 5G IT Service GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Reken | 事实 |
| 网站 | https://www.5g-it.de | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@5g-it.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@5g-it.de [Publicly listed; delivery not tested]; https://www.5g-it.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（园区项目接入层成本对照）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：同生态对照：24 口 PoE++ 与 Allied 同档的规格/成本对比，定位项目毛利优化选项而非替位。
- **要问的问题**：园区项目接入层的成本有没有优化空间？（德文对照表）
- **随附证明**：规格对照 + 单端口测算 + 交付说明（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（车间/室外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：制造与农企客户的车间/仓棚：宽温 DIN PoE 免维护。
- **要问的问题**：车间/仓棚点位用什么交换？
- **随附证明**：宽温报告 + DIN 图 + 备件包价（德文）。

### 第 3 次跟进 · 管理型 PoE（客户网分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：SMB 客户网分段模板：VLAN/ERPS+监控模版，给他工程师速成。
- **要问的问题**：客户网分段模板要不要来一套？
- **随附证明**：VLAN/ERPS 模板 + 工程师速查（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第7批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：北威州 Borken 县区域 IT 服务商：中小企业全托管/云/网安，Allied Telesis Integrate+Resell 级伙伴（官网伙伴墙+CSV 记录）。
- **产品线与在售品牌**：咨询/规划/实施/运维全包；伙伴：Ruckus（无线）+Allied（有线）+Sophos+Acronis+Microsoft/enreach 通信。
- **目标行业与场景**：Borken 县与 NRW 中小企业/诊所/事务所：办公网与云迁移项目。
- **团队与规模**：14 人实名团队年轻公司（团队页公开到狗）。
- **决策链与对接人**：info@5g-it.de（CSV 9-27 核验：官网公开，Velen/Reken）。
- **技术与认证**：Allied Integrate+Resell（CSV 记录）；Ruckus/Sophos/Acronis 认证。
- **采购与供应链信号**：区域 SMB 项目制：办公网改造单带接入层；Ruckus 无线+Allied 有线组合=他卖整套园区的习惯。
- **近期动态与线索**：团队照片 2026-05 更新——公司形象在运营，状态健康。
- **与我方契合点**：园区项目的接入层 24 口与室外/车间工业件——同 Allied 生态的成本对照选项。
- **风险与注意**：小团队人情型：给技术负责人（非泛泛 info）发简短资料+待机交流；德文优先。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网抬头：优化你在 Borken 县乃至整个北威州的 IT——区域全包 IT 服务商。
  > Wir optimieren Deine IT im Kreis Borken und in ganz NRW!
  > 来源：https://www.5g-it.de/
- **【产品线与在售品牌】**官网自述全链路方法：咨询-规划-实施-运维；强调资源互联、减负与流程优化。
  > Unser ganzheitlicher Ansatz bei Beratung, Konzeptionierung, Realisierung und Betreuung ergibt passgenaue IT-Lösungen… eigene Ressourcen effektiver zu vernetzen, Mitarbeiter zu entlasten und Geschäftsprozesse zu optimieren.
  > 来源：https://www.5g-it.de/
- **【技术与认证】**伙伴墙（官网 Logo）：Ruckus · Acronis · Sophos · Allied Telesis · Microsoft · enreach · VMware——Allied 在墙（同步 CSV：Integrate+Resell）。
  > Starke Partner — Wir setzen auf eine starke Partnerschaften mit ausgewählten Herstellern.（伙伴墙 Logo：Ruckus · Acronis · Sophos · Allied Telesis · Microsoft · enreach · VMware）
  > 来源：https://www.5g-it.de/
- **【团队与规模】**官网团队页 14 位实名成员+1 只狗（Milow），位于 Münsterland 创新与服务园（IDPM）。
  > Das Team（实名：Falk Kappenhagen · Jens Tarraschewski · Benjamin Yildiz · Bernward Schepermann · Jonas Franik · Benjamin Eweleit · Christopher Heidemann · Lars Wolter · Michael Paschen · Amirkhan Dzhabrailov · Markus Gerwing · Christian Schlemmer · Nick Brinkmann · Florian Elsing · Milow 🐾）· Innovations- und Dienstleistungspark Münsterland (IDPM)
  > 来源：https://www.5g-it.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第14批.json`；价格均为 EXW 快照。

- **①背景再核**：NRW 区域商；伙伴墙 Allied 实版印证
- **②芯片/型号**：Allied Telesis（官网实版）
- **③KP 深挖**：具名团队+info@
- **④Saga 对标**：第二供位 value 线（不贬在位）
- **⑤在乎与偏好**：认证级文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Starke Partner…zertifizierte Mitarbeiter aus Vertrieb und Technik…[Allied Telesis][Ruckus][Sophos]…”
  > “Starke Partner…zertifizierte Mitarbeiter aus Vertrieb und Technik…[Allied Telesis][Ruckus][Sophos]…”
  > 来源：https://www.5g-it.de/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 5G IT NRW：Allied 伙伴实版印证→第二供位 value 线（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：印证
- **W**：绑定
- **O**：二线
- **T**：同盟

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
  - [ ] 二线空间
  - [ ] 文档门槛
  - [ ] 评测窗

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi 5G IT team,

A partner wall with certified staff behind each brand - Ruckus, Sophos, Allied Telesis - shows how seriously Kreis Borken businesses are served. We write with respect for that structure, not against it.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, Voice VLAN, watchdog) with full CE documentation and test reports. Reference: $165 USD EXW - a value second line for projects where the standard partner brands overshoot the budget.

One question: when a customer project cannot carry the usual brands, is there room for a documented value alternative on your bench?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

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
