# General Computer Italia S.p.A.

> **评级 A**　|　意大利 · Roma　|　档案编号 `A-309`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-309
rating: A
country: 意大利
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
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — GCI 意 Milano 维修服务厂（post-warranty 现场+100×100 白标通道）：备件池窄位窄针（$165 锚点一致，低密）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | General Computer Italia S.p.A.（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Roma | 事实 |
| 网站 | https://www.gci.it | 事实 |
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

- **邮箱**：info@gci.it
  - 状态：既有/公开
- **电话**：02 90092830
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：info@gci.it（官网页脚；联系地含罗马办公室Via del Poggio Laurentino 66）；02 90092830
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 维保备件库一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：意语一封：过保交换机更换的备件库供应——批次一致性+RMA 先行+意大利到货期，适配其 SLA 承诺。
- **要问的问题**：维保备件库的接入交换目前有第二来源位吗？
- **随附证明**：备件供应方案一页+RMA 条款。

### 第 2 次跟进 · 工业备件窄线

- **推什么**：STI-280GE（Saga） 等窄线
- **切入点**：工业现场维保的宽温备件窄线。
- **要问的问题**：工业点位备件有常备目录吗？
- **随附证明**：窄线一页价卡。

### 第 3 次跟进 · 备件框架协议收口

- **推什么**：—（协议）
- **切入点**：年度备件框架（常备清单+价格锁定+）协议留档；不回即冻结。
- **要问的问题**：（无需回）协议留档。
- **随附证明**：框架一页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第16批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：意大利保外维保大厂（**维保备件库补货位**是独门切法：过保交换机替换=我们的市场）；Allied Resell。
- **产品线与在售品牌**：保外维保/渠道伙伴计划/GREEN 循环。
- **目标行业与场景**：意大利 ICT mission critical 客户（维保合约群）。
- **团队与规模**：中大型（三地+Cap 2M€+治理文件体系）。
- **决策链与对接人**：info@gci.it（官网页脚，CSV 9-27）；02 90092830。
- **技术与认证**：Allied Resell（CSV 名录）。
- **采购与供应链信号**：**维保备件逻辑直通**：24 口 PoE++ 与工业件作维保替换备件报价（质量三证+批次一致性，维保最怕断档）。
- **近期动态与线索**：渠道伙伴计划招募中=合作心态开放。
- **与我方契合点**：维保备件 24 口/工业件+RMA 与备件池协议。
- **风险与注意**：别当普通集成商推销项目位——主诉永远「备件库补货」；意大利语资料佳。

### R54 原文证据摘录（全部保留）

- **【业务定位】**米兰法定总部+罗马办公室的**保外硬件维保**大厂（GCI SERVICE FACTORY）：ICT mission critical 的 post-warranty 现场维保；另有 GCI GREEN 可持续线与「100×100 Canale」渠道伙伴计划。
  > Servizi di manutenzione post warranty per l’ICT mission critical ‖ 100×100 Canale — Amplia la tua offerta con i servizi GCI — DIVENTA PARTNER
  > 来源：https://www.gci.it/
- **【团队与规模】**三地：Foro Buonaparte 68 Milano（法定）/Via Milano 11 Lacchiarella（运营）/Via del Poggio Laurentino 66 Roma；公司化治理齐备（Codice Etico/231 模型/举报通道）+注册资本 200 万欧。
  > SEDE LEGALE — Foro Buonaparte, 68, 20121 Milano ‖ UFFICI DI ROMA — Via del Poggio Laurentino, 66, 00144 Roma ‖ Cap. Soc. 2.000.000 € i.v. · P.I. 01546870187
  > 来源：https://www.gci.it/
- **【采购与供应链信号】**保外维保生意本质=**替换件持续采购**：过保交换机的替换位需要高性价比现货——我们正是其维保备件库的补货位。
  > Manutenzione Post Warranty Hardware On-site（维保主业定义）‖ （CSV 记录）Allied 名录 Resell
  > 来源：https://www.gci.it/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第31批.json`；价格均为 EXW 快照。

- **①背景再核**：IT 服务厂（官网一手核）
- **②芯片/型号**：—
- **③KP 深挖**：info@
- **④Saga 对标**：备件窄位（$165 锚点一致，低密）
- **⑤在乎与偏好**：mission-critical 时效

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**GCI SERVICE FACTORY: Manutenzione Post Warranty Hardware On-site per ICT mission critical；100×100 Canale: Amplia la tua offerta con i servizi GCI
  > GCI SERVICE FACTORY: Manutenzione Post Warranty Hardware On-site per ICT mission critical；100×100 Canale: Amplia la tua offerta con i servizi GCI
  > 来源：https://www.gci.it

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | GCI 意 Milano 维修服务厂（post-warranty 现场+100×100 白标通道）：备件池窄位窄针（$165 锚点一致，低密） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：通道
- **W**：非采购向
- **O**：备件
- **T**：—

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
  - [ ] 备件机制
  - [ ] 伙伴网

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Ciao GCI team,

Post-warranty on-site maintenance for mission-critical ICT, plus a 100-percent-channel model that lets partners broaden their offer. Both machines eat spare parts - and somewhere in that spare-parts logic there is room for a documented value unit.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29) - a value replacement unit for spare pools and partner bundles.

One question: does your spare pool accept documented value units - or do frame contracts decide every part?

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
