# Merlin EDV

> **评级 A**　|　德国 · Bayern　|　档案编号 `A-326`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-326
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
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Merlin EDV 德 Erlangen 30 年 MSP+Industrielösungen（LTB/EOL/真伪鉴别/Kits/JIT/报关）：供应链服务通道角度强对口（$165 锚点一致+EOL 逻辑）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Merlin EDV（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Bayern | 事实 |
| 网站 | https://www.merlinedv.de | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】MERLIN Kommunikationstechnik e.K.（德国 Erlangen，30 年）：双柱——**Mittelstand MSP** ＋ **Industrielösungen（采购/供应链服务）：LTB/EOL 支持、真伪鉴别、Kits 集配、JIT、报关物流**（面向研究/医疗/工业客户）;CSV=Allied Telesis Resell（站点实体 MERLIN e.K.,Erlangen 实注）
- 【推断】供应链服务商本身就是'找得到、配得齐'的通道——我们文档化的 value 件可其 EOL 承载/Kits 组件/二供线进入其服务流程——高度同频道
- 【假设】以 EOL 满载与 kit 供货通道角度切入：value 件入其供应链货架

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@merlinedv.de
  - 状态：既有/公开
- **电话**：+49 9131 90715-0
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：info@merlinedv.de（官网Contact/Imprint）；+49 9131 90715-0；MERLIN Kommunikationstechnik e.K.，坐落Erlangen（CSV城市字段为Bayern）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 供应源登记一页

- **推什么**：STC-424DGGPM-440W（Saga） + STI-280GE（Saga） 系列目录（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：德语一封：申请入其采购名册——接入/工业件的第二供应源（批次一致性证明+供应年限 LTS 承诺+原厂文档）。
- **要问的问题**：贵司采购名册接入/工业件的第二供应源缺位吗？
- **随附证明**：供应商资料包（参数+原产地/批次+LTS）。

### 第 2 次跟进 · EOL 替代对照

- **推什么**：EOL 替代型号对照页
- **切入点**：停厂接入件的规格替代对照（同 PoE 预算/端口/管理级）；配套真伪证明流程由他们主导。
- **要问的问题**：近期有停厂交换件的替代需求吗？
- **随附证明**：对照一页（德）。

### 第 3 次跟进 · 托管臂 24 口常规件

- **推什么**：STC-424DGGPM-440W（Saga）（一页报价）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：Mittelstand 托管客户的 24 口 PoE 常规第二来源+小批梯；不回即冻结。
- **要问的问题**：托管客户的接入层也要第二来源吗？
- **随附证明**：一页报价（德）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第17批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：埃尔朗根 30 年托管+采购服务双臂（**采购供应链专长=在其采购册里登记为我们的供应源**；医疗客群面注意只做商业）。
- **产品线与在售品牌**：Mittelstand 托管+工业采购服务（LTB/EOL/寄售/套件/检测）。
- **目标行业与场景**：科研/医疗/工业企业（医疗运营面声明只做商业网络件段）。
- **团队与规模**：中型（国际物流通关能力）。
- **决策链与对接人**：info@merlinedv.de（Imprint，CSV 9-27）。
- **技术与认证**：Allied Resell（CSV 9-23；AT 伙伴页同址）。
- **采购与供应链信号**：**反向切法**：把我们的产品入其采购名册——常规接入层的第二供应源+EOL 交换件的替代型号对照（真伪检测他们自己做，我们给原厂证明）。
- **近期动态与线索**：2026-08 新图文版 Industrielösungen=该臂在营销扩张。
- **与我方契合点**：在册供应源（接入/工业件）+EOL 替代对照+寄售仓议案。
- **风险与注意**：医疗机构客群=只做其商业网络件采购段（医疗专用系统不涉）；替代对照不得冒称原厂件。

### R54 原文证据摘录（全部保留）

- **【业务定位】**埃尔朗根 30 年双臂：Mittelstand IT 托管 + **Industrielösungen 采购供应链服务**（LTB/EOL 尾货采购/寄售仓/套件组配/国际物流通关/真伪检测）——服务科研机构/医疗运营/工业企业。
  > Industrielösungen — Beschaffung · LTB/EOL-Support · Supply Chain Services ‖ Last-Time-Buy (LTB) & End-of-Life-Produkte… spezialisierte Lieferquellen ‖ Authentizitäts- und Plagiatsprüfungen
  > 来源：https://www.merlinedv.de/
- **【采购与供应链信号】****他们本职就是替客户找难买件**——我们的位置=其采购案的**在册供应源**：接入交换/工业件的常规供 + 停厂件的替代品（EOL 替代位）。
  > Wir unterstützen Forschungseinrichtungen, Healthcare-Betriebe und Industrieunternehmen mit umfassenden Supply-Chain-Services bei anspruchsvollen Beschaffungsaufgaben und Sonderprojekten.
  > 来源：https://www.merlinedv.de/
- **【决策链与对接人】**info@merlinedv.de（Contact/Imprint，CSV 9-27 official-company）；+49 9131 90715-0；主体 MERLIN Kommunikationstechnik e.K.（HRA 7006 Fürth）。
  > （CSV 2026-09-27 记录）官网联系页与 Imprint 给 info@merlinedv.de、+49 9131 90715-0 与 Gerberei 19, 91054 Erlangen；official-company
  > 来源：https://www.merlinedv.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第33批.json`；价格均为 EXW 快照。

- **①背景再核**：DE Erlangen 双柱（官网一手核）
- **②芯片/型号**：供应链服务
- **③KP 深挖**：info@
- **④Saga 对标**：通道角度（$165 锚点一致+EOL logic）
- **⑤在乎与偏好**：供货安全/透明度

### R55 证据摘录（全部保留 · 含数量）

- **【采购与供应链信号】**LTB & End-of-Life-Produkte…Konsignationslager…Just-in-Time…Kundenspezifische Konfektionierung (Lieferung als Kit)——30 Jahre Procurement-Lösungen
  > LTB & End-of-Life-Produkte…Konsignationslager…Just-in-Time…Kundenspezifische Konfektionierung (Lieferung als Kit)——30 Jahre Procurement-Lösungen
  > 来源：https://www.merlinedv.de

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：德国 Erlangen MSP+供应链服务商（30 年）
- **产品线与在售品牌**：多牌（AT CSV）
- **目标行业与场景**：研究/医疗/工业+本地 SMB
- **团队与规模**：中型
- **决策链与对接人**：info@ 口
- **技术与认证**：—
- **采购与供应链信号**：供应链服务泳道（受方可溯源）
- **近期动态与线索**：—
- **与我方契合点**：EOL 满载+Kits 通道到位（强对口）
- **风险与注意**：其采购半步法规客户多——诚实角

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Merlin EDV 德 Erlangen 30 年 MSP+Industrielösungen（LTB/EOL/真伪鉴别/Kits/JIT/报关）：供应链服务通道角度强对口（$165 锚点一致+EOL 逻辑） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：同频
- **W**：内控
- **O**：入架
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
  - [ ] 入架机制
  - [ ] 责权

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hallo MERLIN team,

Your industrial-solutions pillar reads like our business from the buyer's side: LTB and EOL support, authenticity testing, kitting, JIT, customs logistics. You keep components available when normal supply chains fail - that is exactly where a documented supplier earns its place.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation, traceable to the unit. Reference: $165 USD EXW (2026-09-29). As an EOL-filler, a kit component, or a second-source line in your supply-chain services.

One question: what does a component need to show to enter your supply-chain catalogue - and would one evaluation unit start that process?

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
