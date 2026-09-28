# dainox GmbH

> **评级 A**　|　德国 · Bad Wörishofen　|　档案编号 `A-145`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-145
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 主场景匹配+首触只推一个型号的纪律；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | dainox GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Bad Wörishofen | 事实 |
| 网站 | https://www.dainox.net | 事实 |
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

- **邮箱**：info@dainox.net（既有/公开）
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@dainox.net [Publicly listed; delivery not tested]; https://www.dainox.net
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（仅自用/民用咨询段，军段划线）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：开门见山划边界：仅供民用商业项目与自用设施；24 口接入层规格+适用范围一页。
- **要问的问题**：自用设施和民用咨询客户的接入层用什么？（军段不供声明随附）
- **随附证明**：适用边界声明 + 规格表（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（自用厂房/办公配套）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：新厂房建设期：厂房/办公的商用配套交换，按一般企业规格谈。
- **要问的问题**：新厂房的通用网络配套做了吗？
- **随附证明**：宽温报告 + DIN 图 + 报价（德文）。

### 第 3 次跟进 · 管理型 PoE（民用 GRC 咨询客户商用段）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：GRC 咨询客户的商用网分段参考件：VLAN/ERPS 模板+评估样机；若前两步无民用回响就此归档。
- **要问的问题**：民用咨询项目要不要一套商用分段参考件？
- **随附证明**：VLAN/ERPS 模板 + 样机（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第8批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：巴伐利亚防务通信商：北约 FMN/AFCEA/DWT 海军圈的物资与方案+自有 dainBox 产品，Allied Resell（CSV 记录）。⚠️ 防务主业是禁区；民用只留 IT-GRC 咨询与自用段。
- **产品线与在售品牌**：防务通信方案/dainBox 加固箱产品线/IT 咨询与 GRC 合规。
- **目标行业与场景**：军政：北约/德军任务网（禁区）。民用：企业 GRC 合规咨询、自用办公/车间网络。
- **团队与规模**：成长型（新厂房在建）；咨询与产品双编组。
- **决策链与对接人**：info@dainox.net（CSV 9-27：用于一般询问与报价；军事通信项目有资质门槛——CSV 原话，补邮箱不等于可成交）。
- **技术与认证**：AFCEA/CWIX/FMN 体系（官网）；Allied Resell（CSV 记录）。
- **采购与供应链信号**：⚠️ 军段采购链绝不可进（资质/审查/北约互操作门槛）；仅自用与民用咨询周边可按普通商业谈。
- **近期动态与线索**：新厂房 2026 动工——自用部署在增。
- **与我方契合点**：很窄：自用办公/车间网络（非军品产线专网）与民用咨询客户的商用品——首封划线后试探。
- **风险与注意**：军段一句话都别碰产品；若回应全在防务口径=归档不强求（同 ARCHE 处置）。

### R54 原文证据摘录（全部保留）

- **【业务定位】**⚠️ 官网双主业：IT 全生命周期咨询 + 「Defence 环境通信方案专家」——防务通信是主战场。
  > Wenn es darauf ankommt - dainox ist der Experte für Kommunikationslösungen im Defence-Umfeld. ‖ dainox unterstützt Sie in allen Lifecycle-Phasen Ihrer IT Infrastruktur.
  > 来源：https://www.dainox.net/
- **【近期动态与线索】**⚠️ 新闻流清一色军政：2026 年 AFCEA 波恩展台+CWIX 2026（北约 FMN/PCN 联合任务网）+DWT 海军研讨会+LBO 部署联网专文。
  > Ein Auftrag. Viele Nationen. Ein Netz: dainox auf der AFCEA Fachausstellung 2026 ‖ dainox stärkt die Zukunft der FMN- und PCN-Architektur auf der CWIX 2026 ‖ Vernetzungsfähigkeit in LBO-Einsätzen（Fachartikel）
  > 来源：https://www.dainox.net/
- **【团队与规模】**扩张信号：2026-07 新生产厂房奠基（自有 dainBox 产品线扩产）。
  > Meilenstein für die dainox GmbH: Offizieller Spatenstich für die neue Produktionshalle（2026-07-24）‖ FAQ… über dainBox
  > 来源：https://www.dainox.net/
- **【技术与认证】**民用线存在但窄：IT-GRC/云合规咨询（2026 IT-GRC 大会演讲，Bernd Kohler 高级安全顾问）。
  > IT-GRC Kongress 2026: Cloud Compliance im regulatorischen Stresstest — Bernd Kohler（Senior Security Consultant）
  > 来源：https://www.dainox.net/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：【人工定级】A —— 自动规则已跳过；人工指定
- **W**：公开信息有限
- **O**：P1 场景切入（主场景匹配+首触只推一个型号的纪律）
- **T**：现有供应商惯性；价格竞争。

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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：8-port PoE with auto-recovery for your field deployments

```text
Hi dainox,

I came across dainox GmbH - 集成商/代理（Allied Telesis）.

We build a compact 8-port Gigabit PoE switch (240W budget, af/at) with a hardware PoE watchdog that power-cycles a frozen AP or camera automatically, plus clean 802.1Q VLAN / ERPS / sFlow on the management side. Reference: $99 USD EXW.

One question: How many PoE ports does a typical site of yours need today?

If it is useful, I can send one unit for a 30-day evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

Best regards,
Saga Communications - PoE switch OEM/ODM (neutral packing available)
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
