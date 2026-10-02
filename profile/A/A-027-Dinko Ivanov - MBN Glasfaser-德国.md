# Dinko Ivanov / MBN Glasfaser

> **评级 A**　|　德国 · Westhofen　|　档案编号 `A-027`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-027
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（光纤接入），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — MBN 塔站密封柜夏天高温：工业温宽 PoE 钉住缺口（$74.8 邮件锚点一致）；EU 补贴市政段走合规；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Dinko Ivanov / MBN Glasfaser（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Westhofen | 事实 |
| 网站 | mbn-glasfaser.de | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Dinko Ivanov | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCSE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Mobile Breitbandnetze GmbH（MBN，Westhofen/Rheinhessen）：18 年市场；FTTT（光纤到塔）+Richtfunk 定向无线混合的农村宽带运营商，单链路 10Gbit@50m-10km；自营公共热点业务（24h 服务、德国热点法规合规）；市政宽带 EU 补贴项目线；RIPE ORG-MBG9-RIPE 自有 AS
- 【推断】WISP 运营商：塔站/杆站机柜接入层=工业温宽 PoE 刚需（CPE 供电、AP、回传），热点业务线再多一层 PoE AP 采购
- 【假设】农村学校/市政热点是其增长段（EU 补贴节奏）

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCSE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：dinko.ivanov@mbn-glasfaser.de
  - 状态：既有/公开
- **电话**：+49 6344 9442084
- **原始联系字段**：+49 6344 9442084 / dinko.ivanov@mbn-glasfaser.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Dinko Ivanov**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：PoP/节点机柜：一台 24 口 PoE++ 同时喂热点 AP、监控与客户接入；重点给整机功率预算与长期稳定性（MTBF/温升）。
- **要问的问题**：他的 PoP/节点现在用什么交换机、单点多少用户？
- **随附证明**：功率实测 + 长稳测试建议 + 备件/RMA 政策。

### 第 2 次跟进 · 工业级非管理 PoE（塔站/室外箱）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：塔站与室外箱：宽温宽压、DIN、免配置；配合他们的 FTTT 架构做「现场盒」。
- **要问的问题**：塔站/室外箱的供电与温度条件如何？
- **随附证明**：宽温报告 + 双电源接线图 + SFP 兼容清单。

### 第 3 次跟进 · 管理型 PoE（回传环与 QoS）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：多节点回传要环网与 QoS：ERPS + VLAN/QinQ + 端口限速，按运营商话术谈。
- **要问的问题**：回传网要不要做环网冗余与用户隔离？
- **随附证明**：ERPS 实测 + QinQ 模板 + SNMP 监控清单。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Mobile Breitbandnetze GmbH（MBN）：自建「光纤-微波混合」网络并以 ISP/网络运营商身份卖宽带，重点是农村地区覆盖；同时是公共热点运营商。
- **产品线与在售品牌**：自建基础设施（FTTT 光纤到塔 + 微波到户），未公开设备品牌；RIPE 组织 ORG-MBG9-RIPE。
- **目标行业与场景**：农村宽带（居民/村镇）、市政补贴宽带项目、公共热点（政府/城市 WiFi）、企业专线。
- **团队与规模**：中小型运营商（「seit 18 Jahren auf dem Markt」），决策链短，技术负责人 Dinko Ivanov 持多证。
- **决策链与对接人**：Dinko Ivanov（dinko.ivanov@mbn-glasfaser.de）；+49 6344 9442084。
- **技术与认证**：MikroTik 认证顾问（MTCNA+MTCSE）——路由与安全为主，交换设备外购。
- **采购与供应链信号**：运营商自建 = 设备进他们的网（长期资产）：看重 MTBF、宽温、远程管理、备件速度；一次选型长期复购。
- **近期动态与线索**：官网 2026 年在线：主打「光纤-微波混合」把 10 Gbit/s 送到 50 m–10 km 的任意距离、市政补贴项目无需大规模土木工程。
- **与我方契合点**：FTTT 到户的接入层 + PoP/机箱 + 塔站设备全是我们的场景；24 口 PoE 用于 PoP/节点，工业款用于塔站与室外箱，管理型用于回传环。
- **风险与注意**：运营商采购看长期稳定性与备件（他不是一次性买卖）；先小批量试点跑稳定性和 RMA 响应速度。

### R54 原文证据摘录（全部保留）

- **【业务定位】**公司自述：光纤网络与无线网络基础设施的承建者、网络运营商与 ISP，聚焦农村宽带。
  > Mobile Breitbandnetze GmbH (kurz MBN) ist Ersteller von Funknetz-Infrastruktur und Glasfasernetzen, sowie Netzbetreiber und Internet Provider. Unser Schwerpunkt liegt in der Breitbandversorgung im ländlichen Raum.
  > 来源：https://mbn-glasfaser.de/
- **【目标行业与场景】**FTTT + 微波混合架构的技术参数（距离与带宽）。
  > Die Anbindung erfolgt über eine Glasfaser-/Richtfunk-Hybridinfrastruktur: Zunächst wird der Standort per Fiber-to-the-Tower (FTTT) bis zur Richtfunkantenne angebunden. Von dort führt die Richtfunkstrecke direkt zum Zielstandort … Breitband bis zu 10 Gigabit pro Sekunde über Entfernungen zwischen 50 Metern und 10 Kilometern
  > 来源：https://mbn-glasfaser.de/
- **【近期动态与线索】**市政补贴项目是他们的增长点（快速落地、无需大规模土建）。
  > Kommunenausbau mit förderfähigem EU-Internet-Breitbandzugang über Glasfaser-Richtfunk-Hybrid-Technologie … Schnelle Realisierbarkeit der Breitbanderschließung (wenige Monate statt Jahre)
  > 来源：https://mbn-glasfaser.de/
- **【团队与规模】**运营商身份（RIPE 组织对象）与市场年限。
  > seit 18 Jahren auf dem Markt；RIPE lookup: ORG-MBG9-RIPE（官网页脚链接）
  > 来源：https://mbn-glasfaser.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第3批.json`；价格均为 EXW 快照。

- **①背景再核**：Westhofen 18 年 WISP；FTTT+Richtfunk 10Gbit；自有 AS；EU 补贴市政段在售
- **②芯片/型号**：回传定向无线为主；接入层未公开（塔站柜件）
- **③KP 深挖**：Dinko Ivanov（MTCNA+MTCSE）技术直达
- **④Saga 对标**：塔站机柜工业 PoE：STI-288GP ——钉住工业温宽缺口
- **⑤在乎与偏好**：24h 服务 SLA 对等条件；合规文件齐

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Ersteller von Funknetz-Infrastruktur und Glasfasernetzen, sowie Netzbetreiber…Breitbandversorgung im ländlichen Raum…FTTT…bis zu 10 Gigabit…50 Meter bis 10 Kilometer”
  > “Ersteller von Funknetz-Infrastruktur und Glasfasernetzen, sowie Netzbetreiber…Breitbandversorgung im ländlichen Raum…FTTT…bis zu 10 Gigabit…50 Meter bis 10 Kilometer”
  > 来源：https://mbn-glasfaser.de/
- **【产品线与在售品牌】**“Öffentliche Hotspots von MBN…erstklassige Technologie, rechtssicheren Betrieb und professionellen 24-h-Service”
  > “Öffentliche Hotspots von MBN…erstklassige Technologie, rechtssicheren Betrieb und professionellen 24-h-Service”
  > 来源：https://mbn-glasfaser.de/
- **【近期动态与线索】**“Kommunenausbau mit förderfähigem EU-Internet-Breitbandzugang…wenige Monate statt Jahre…ORG-MBG9-RIPE”
  > “Kommunenausbau mit förderfähigem EU-Internet-Breitbandzugang…wenige Monate statt Jahre…ORG-MBG9-RIPE”
  > 来源：https://mbn-glasfaser.de/
- **【联系方式】**MX=mx00.ionos.de/mx01.ionos.de（1&1 IONOS）（MX/DNS 级核验：域存活=邮件可投递到域）
  > MX=mx00.ionos.de/mx01.ionos.de（1&1 IONOS）（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://mbn-glasfaser.de/kontakt

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：Rheinhessen 农村宽带运营商：FTTT+Richtfunk 混合；公共热点业务线；EU 补贴市政段
- **产品线与在售品牌**：自建塔站+热点系统；品牌未公开
- **目标行业与场景**：农村住户、学校热点、市政（EU 补贴段=公共采购，走规范流程）
- **团队与规模**：18 年区域运营商
- **决策链与对接人**：Dinko Ivanov（MTCNA+MTCSE，技术口直达）
- **技术与认证**：MTCNA+MTCSE；自有 AS（RIPE ORG-MBG9-RIPE）
- **采购与供应链信号**：塔站机柜工业温宽件；热点 AP 批量
- **近期动态与线索**：“Kommunenausbau mit förderfähigem EU-Internet-Breitband”持续主推
- **与我方契合点**：工业温宽 PoE 接入（STI-288GP 系）进塔站柜；热点 AP 供电
- **风险与注意**：EU 补贴采购=公共流程守规则；私营住户/热点段可正常商务

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | MBN 塔站密封柜夏天高温：工业温宽 PoE 钉住缺口（$74.8 邮件锚点一致）；EU 补贴市政段走合规 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：区域基础设施垄断
- **W**：区域体量
- **O**：EU 补贴+热点线增长
- **T**：巨头下沉

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
| 决策人识别 | ✅ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 塔站柜现用交换机
  - [ ] 热点线年度点位计划
  - [ ] 市政段合规清单

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Dinko,

I found you via the MikroTik consultant list (MTCNA/MTCSE) - and MBN's FTTT+Richtfunk hybrid for rural broadband is a clever architecture.

We build industrial-grade managed PoE switches rated -40 to 75C, designed for exactly the sealed tower cabinets your tower sites use. 802.3af/at, PoE watchdog included. Reference: $74.8 USD EXW.

One question: how hot do your tower cabinets get in summer - and do the switches in them survive?

If useful, I can send one unit for evaluation with the full temperature test report. If not a fit, one line and I close the loop.

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

- **KP 领英直达**:[Dinko Ivanov · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Dinko%20Ivanov)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 中(IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STI-288GP(工业导轨 24G+4×10G→机柜/自动化)、STC-424DGGPM-280W(48G PoE++/4×25G→智算安防酒店全谱)(批量潜力高,可上 280W 旗舰对照行)(本行为调查分析结论,与开发信首推型号是两回事)
