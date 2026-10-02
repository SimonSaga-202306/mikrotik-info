# Eckmann Spezialkabel GmbH

> **评级 A**　|　德国 · Quickborn　|　档案编号 `A-150`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-150
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Eckmann 电缆分销：aktive 类目 PoE 交换补位（$165 锚点一致）；Kai 具名；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Eckmann Spezialkabel GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Quickborn | 事实 |
| 网站 | https://www.eckmann-spezialkabel.co | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Eckmann Spezialkabel GmbH（德国 Quickborn，2000 年创家族企业，Eckmann 集团含 datacom）：**电缆分销专家**——网络技术（铜/光纤线缆/插座/**机柜机架**/配线架/**aktive Komponenten（实版类目：有源组件）**）/演播技术（视频/摄像/麦克线缆）/**船舶海工特种电缆（民用船用）**/定制接头与按米裁剪；Quickborn 大仓+法兰克福/萨尔布吕肯点；11-50 人；GF Kai Eckmann 具名
- 【推断】“aktive Komponenten”类目实版=架上已有有源位——value PoE 交换补位与 RWL 型被动旁 active 同型；海工电缆是民用商用常规段
- 【假设】“按客户规格定制+快速物流”分销文化=上架看交付与文档；Kai Eckmann 具名可直触

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：spezialkabel@eckmann.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：spezialkabel@eckmann.de [Publicly listed; delivery not tested]; https://www.eckmann-spezialkabel.co
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 品类延伸提案（缆旁有源件试点）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：布线盘的自然延伸：4 口宽温小机做「配缆顺带供电」的试点 SKU——小批量起订+动销 KPI 谈法。
- **要问的问题**：布线单里客户常要顺带供电件？试点 SKU 怎么挂？
- **随附证明**：品类建议书 + 分销价目 + 宽温报告（德文）。

### 第 2 次跟进 · 24 口 CCTV/PoE（机房/演播接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：DC 配线与演播布线的机房接入层：24 口 PoE++ 随项目带出。
- **要问的问题**：机房/演播项目的接入层有没有顺带的需求？
- **随附证明**：规格对照 + 到岸价目 + 交付说明（德文）。

### 第 3 次跟进 · 管理型 PoE（工业/演播分段参考件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：工业与演播网的分段参考件：VLAN/ERPS 模板给技术销售当增配话术。
- **要问的问题**：分段模板给你们销售当增配包？
- **随附证明**：VLAN/ERPS 模板 + 销售速查（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第8批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：汉堡 Quickborn 特种电缆分销：数据网缆+演播缆+工业耐化学缆+船/海工缆，自选拼接加工（Konfektion）是差异化，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：网络缆与光纤、演播音视频缆、工业/炼油缆、船舶海工缆、拼接盒/定制加工、项目物流。
- **目标行业与场景**：DC 与机房配线、工厂改造、演播/活动布线、商用船与海工电气配套。
- **团队与规模**：小型成长分销（招聘中；具名 Kai Eckmann）。
- **决策链与对接人**：spezialkabel@eckmann.de（CSV 9-27：官网联系页与 Xing 一致）。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：⚠️ CSV 提醒：电缆分销为主别当强交换买家——有源件按「品类延伸试点」谈：他天天给客户配缆，换机柜里差个供电件时顺手卖。
- **近期动态与线索**：招聘+新品线页更新=在扩品类。
- **与我方契合点**：缆旁的供电件：布线盘加配工业 PoE/商用 24 口的自然延伸——给品类建议书+试点 KPI，不按项目集成商谈。
- **风险与注意**：船用/海工是商用段（只谈民船海工，不碰军）；炼油化工场景问防爆等级的话我们没有 ATEX——别硬套，给非爆区的机房/办公段。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网页标题即定位：数据/网络技术电缆批发（Großhandel）——汉堡圈特种电缆分销商，Allied Resell（CSV 记录）。
  > （页标题）Großhandel für Datentechnik Netzwerktechnik Kabel ‖ Wir beraten, planen und bieten individuelle Lösungen
  > 来源：https://www.eckmann-spezialkabel.co/
- **【产品线与在售品牌】**四大品线：数据技术/演播音视频/工业与炼油耐化学缆/船舶海工特种缆——“拼接盒与特殊加工是我们的招牌”。
  > Datentechnik — Netzwerkkabel und IT-Infrastrukturlösungen · Studiotechnik — Professionelle Audio- und Videokabel · Industrie & Raffinerie — Chemikalienbeständige Kabel · Spezialkabel Marine & Offshore ‖ Kundenspezifische Spleißboxen & Sonderkonfektionen – unsere Spezialitäten
  > 来源：https://www.eckmann-spezialkabel.co/
- **【目标行业与场景】**客户盘：数据中心与 IT 基建、工业与生产、造船与海工、媒体与活动技术——电线电缆配盘型生意。
  > Für wen wir arbeiten: Rechenzentren & IT-Infrastruktur · Industrie & Produktion · Schiffbau & Offshore · Medien- & Veranstaltungstechnik
  > 来源：https://www.eckmann-spezialkabel.co/
- **【近期动态与线索】**在招销售助理/仓库/生产帮工——成长型小分销（具名 Kai Eckmann，LinkedIn/Xing 公开）。
  > neue Stellenangebote: Vertriebsassistent/in (m/w/d) · Lagerhelfer (m/w/d) · Helfer in der Fertigung (m/w/d)
  > 来源：https://www.eckmann-spezialkabel.co/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第15批.json`；价格均为 EXW 快照。

- **①背景再核**：电缆分销专家（aktive 件类目+船用民用线）
- **②芯片/型号**：aktive 类目（厂牌未核）
- **③KP 深挖**：Kai Eckmann 具名
- **④Saga 对标**：aktive 类目 PoE 补位
- **⑤在乎与偏好**：交付+文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Netzwerktechnik (z.B. Kupfer- und Glasfaserleitungen…Schränke/Racks, Patchpanels…aktive Komponenten)”
  > “Netzwerktechnik (z.B. Kupfer- und Glasfaserleitungen…Schränke/Racks, Patchpanels…aktive Komponenten)”
  > 来源：https://de.itsbetter.com/search/show/432092-eckmann-spezialkabel-gmbh.html

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：德国电缆分销专家（aktive 件类目实版）
- **产品线与在售品牌**：电缆/机柜/aktive Komponenten
- **目标行业与场景**：网络工程/演播/船用（民用）
- **团队与规模**：11-50 家族集团
- **决策链与对接人**：Kai Eckmann GF/spezialkabel@
- **技术与认证**：品牌质控
- **采购与供应链信号**：分销上架
- **近期动态与线索**：海事线缆扩线
- **与我方契合点**：aktive 类目 PoE 交换补位
- **风险与注意**：

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Eckmann 电缆分销：aktive 类目 PoE 交换补位（$165 锚点一致）；Kai 具名 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：契合
- **W**：体量
- **O**：补位
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
  - [ ] aktive 类目结构
  - [ ] 上架门槛
  - [ ] 多点结构

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Kai / Eckmann team,

A cable specialist whose range already runs from copper and fibre to racks, patch panels and active components - the natural shelf for a PoE access switch is yours.

We build one thing: a 24-port Gigabit PoE access switch (280W, 802.3af/at, Voice VLAN, watchdog) with full CE documentation. Reference: $165 USD EXW - a value line for the active-components shelf that gives your project customers a healthier margin.

One question: in your active-components range today, is there an open slot for a documented value PoE switch?

If useful, I can send one unit with the full documentation pack. If not a fit, one line and I close the loop.

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

- **KP 领英直达**:[Kai Eckmann · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Kai%20Eckmann%20Eckmann%20Spezialkabel%20GmbH)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 中(IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(批量潜力高,可上 280W 旗舰对照行)(本行为调查分析结论,与开发信首推型号是两回事)
