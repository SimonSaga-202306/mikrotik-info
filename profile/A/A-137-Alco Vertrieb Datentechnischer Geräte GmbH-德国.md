# Alco Vertrieb Datentechnischer Geräte GmbH

> **评级 A**　|　德国 · Idstein　|　档案编号 `A-137`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-137
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
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — ALCO 35 年系统屋：90 年代替代方案基因同频 value 件（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Alco Vertrieb Datentechnischer Geräte GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Idstein | 事实 |
| 网站 | https://www.alcoidstein.de | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】ALCO Systemhaus（德国 Idstein，1988 年创）：35+ 年系统屋——硬件/软件/服务/融资租赁/**自有 ISO 级机房（光伏自给+余热回收）**；自述“**1990 年代初即在标准厂家产品目录之外提供替代方案**”；客户全程陪伴（咨询/实施/维保）
- 【推断】“alternative Lösungen neben den standardisierten Herstellerproduktpaletten”=其商业基因就是替代候选——价值位 OEM 件语言完全同频
- 【假设】自有 DC+光伏=技术玩家型买家：实测级文档说话

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@alcoidstein.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@alcoidstein.de [Publicly listed; delivery not tested]; https://www.alcoidstein.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（「替代方案」货架的接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：顺他 90 年代以来的「替代方案」传统：24 口 PoE++ 同规格成本对照+质保条款，放他的替代货架。
- **要问的问题**：替代方案货架里接入层现在有哪家？（德文对照+样机可借）
- **随附证明**：规格对照 + 质保条款 + 评估样机（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（机房外/厂区分点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：客户厂房与机房外点位：宽温 DIN PoE 长期供货承诺。
- **要问的问题**：厂区分点位的供电交换用什么？
- **随附证明**：宽温报告 + 长期供货承诺 + DIN 图（德文）。

### 第 3 次跟进 · 管理型 PoE（自有 DC/客户机房管理件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他自己机房+客户机房的管理件：VLAN/ERPS/SNMP 全套，低功耗点呼应他的光伏叙事。
- **要问的问题**：DC 接入口的管理件要不要做一轮评估？（功耗数据附）
- **随附证明**：VLAN/ERPS 模板 + 功耗对照 + 实测（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第7批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：陶努斯 Idstein 35+ 年系统屋：硬件/软件/自有 DC/租赁金融/绿色能源自营——德式中型系统屋典型，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：厂商品类+替代方案（其自我定位）+自有 DC 托管+租赁/分期金融+软件订阅。
- **目标行业与场景**：黑森/莱茵-美因地区中型企业客户的机房与终端换代。
- **团队与规模**：35+ 年中型系统屋（ALCO Mediencenter 自有展厅）。
- **决策链与对接人**：info@alcoidstein.de（CSV 9-27 核验：官网 info{at} 规范化）。
- **技术与认证**：Allied Resell（CSV 记录）；自有 DC 运维资质。
- **采购与供应链信号**：「替代方案」是他的卖点之一——我们正是那类替代；租赁金融渠道=客户按金分期采购，整机价格敏感度中等。
- **近期动态与线索**：光伏二期（2,500 组件）2024 施工——资本开支在做，经营健康。
- **与我方契合点**：DC 与机房项目的接入层/管理型：直接摆「同规格成本对照+质保」上桌，与他的选型方法论同频。
- **风险与注意**：老将型公司决策谨慎：对照资料+评估样机先行，别催单；德文。

### R54 原文证据摘录（全部保留）

- **【团队与规模】**官网：1988 年 10 月创立的系统屋，35+ 年持续经营。
  > Seit der Gründung des ALCO-Systemhauses im Oktober 1988 bieten wir unseren Kunden Lösungen in den Bereichen Hardware, Software und Dienstleistungen. … seit über 35 Jahren.
  > 来源：https://www.alcoidstein.de/
- **【采购与供应链信号】**官网自述：90 年代初起就提供「标准化厂商品类之外的替代方案」——对第二来源/高性价比品牌本能开放。
  > Bereits Anfang der 1990er Jahre entsprach es unserem Anspruch, alternative Lösungen neben den standardisierten Herstellerproduktpaletten anzubieten.
  > 来源：https://www.alcoidstein.de/
- **【产品线与在售品牌】**五大支柱：融资租赁/自有数据中心/硬件/软件/可持续性（自有光伏 1MWp 级给总部与 DC 供电、废热供暖、IT 回收闭环）。
  > Finanzierung · Rechenzentrum · Hardware · Software · Nachhaltigkeit ‖ Mit eigener elektrischer Energie aus eigenen Photovoltaik Anlagen zur Stromversorgung des Stammhauses in Idstein und des ALCO eigenen Rechenzentrums
  > 来源：https://www.alcoidstein.de/
- **【业务定位】**三词理念：INDIVIDUALITÄT–INNOVATION–QUALITÄT（个性-创新-品质），随项目全程陪伴（咨询-实施-维保）。
  > INDIVIDUALITÄT – INNOVATION – QUALITÄT · Unser Team begleitet unsere Kunden zu jedem Zeitpunkt des Projekts: Von der Beratung über die Implementierung bis hin zur anschließenden Wartungsdienstleistung.
  > 来源：https://www.alcoidstein.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第14批.json`；价格均为 EXW 快照。

- **①背景再核**：35 年系统屋；替代方案基因（90 年代自述）；自有光伏 DC
- **②芯片/型号**：CSV 载 Allied 信号
- **③KP 深挖**：info@
- **④Saga 对标**：替代基因 value 件
- **⑤在乎与偏好**：实测文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Anfang der 1990er Jahre…alternative Lösungen neben den standardisierten Herstellerproduktpaletten anzubieten…seit über 35 Jahren”
  > “Anfang der 1990er Jahre…alternative Lösungen neben den standardisierten Herstellerproduktpaletten anzubieten…seit über 35 Jahren”
  > 来源：https://www.alcoidstein.de/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：Idstein 35 年系统屋（替代方案基因）
- **产品线与在售品牌**：全谱 HW/SW（厂牌图墙）
- **目标行业与场景**：中小企业/区域
- **团队与规模**：区域系统屋
- **决策链与对接人**：info@ 口
- **技术与认证**：自有光伏 DC
- **采购与供应链信号**：咨询型随单
- **近期动态与线索**：1MWp 光伏扩建
- **与我方契合点**：替代方案基因的 value 件
- **风险与注意**：

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | ALCO 35 年系统屋：90 年代替代方案基因同频 value 件（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：基因
- **W**：体量
- **O**：替代
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
  - [ ] 接入现供
  - [ ] DC 边位
  - [ ] 租赁结构

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi ALCO team,

Since the early 1990s you have offered alternatives beyond the standard manufacturer portfolios - that independence of mind is exactly where we hope to earn a bench test.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, Voice VLAN, watchdog) with full test documentation. Reference: $165 USD EXW - a value line your consultants can put next to the catalogue brands with a clear conscience.

One question: in your current consulting engagements, which switch brand holds the PoE access layer for customers today?

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

---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:[Alco Vertrieb Datentechnischer Geräte GmbH · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Alco%20Vertrieb%20Datentechnischer%20Ger%C3%A4te%20GmbH)(无具名 KP 信号,先搜公司再加人;待查)
- **中国进口与管制**:国别档位 中(IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
