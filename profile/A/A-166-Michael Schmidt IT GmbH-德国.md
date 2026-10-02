# Michael Schmidt IT GmbH

> **评级 A**　|　德国 · Spardorf　|　档案编号 `A-166`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-166
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
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — M. Schmidt Erlangen 安全屋：私营工业段（$165 锚点一致）；公共守界；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Michael Schmidt IT GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Spardorf | 事实 |
| 网站 | https://www.msit-gmbh.de | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Michael Schmidt IT GmbH（德国 Erlangen-Nürnberg 大区）：安全为先系统屋——IT 安全/IT 外包/虚拟化安全/ITK 通信/云安全/微软支持（O365/虚拟化）；客户=企业+**öffentlichen Einrichtungen（公共机构守界段）**；公司名即创始人迈克尔·施密特具名
- 【推断】“Sichere”贯穿全站（安全叙事六次以上）=文档完整度+认证件敏感；公共段守界，私营段主打
- 【假设】Erlangen-Nürnberg=西门子等工业腹地，私营制造业客户为核

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@msit-gmbh.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@msit-gmbh.de [Publicly listed; delivery not tested]; https://www.msit-gmbh.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（外包栈接入标准件）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：外包站点标准件：24 口 PoE++ 单端口成本+质保+材料包（合规声明随附划公共段）。
- **要问的问题**：外包客户的接入层标准件现在什么型号？
- **随附证明**：单站 BOM 测算 + 合规材料包（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（车间/库房点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：制造商业客户的车间/库房：宽温 DIN PoE。
- **要问的问题**：车间点位的坏机率？
- **随附证明**：宽温报告 + 备件包价（德文）。

### 第 3 次跟进 · 管理型 PoE（分段/准入标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：安全语境：管理型（VLAN/ERPS/NAC 配合）分段件+配置基线。
- **要问的问题**：分段基线要不要进你们的方案库？
- **随附证明**：VLAN/ERPS/NAC 兼容说明 + 基线样例（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第9批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：埃尔朗根区系统屋（schmidt IT 品牌）：安全为纲的外包型 IT 服务，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：安全/外包/虚拟化/ITK/云安全/微软栈支持；全天候监控自述。
- **目标行业与场景**：企业与⚠️公共机构（公共段划线只谈商业）。
- **团队与规模**：区域系统屋（Michael Schmidt 品牌）。
- **决策链与对接人**：info@msit-gmbh.de（CSV 9-27：官网明确列出，另有 dokumentation 页）。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：外包全托管逻辑=站点标准件批量；安全话术=分段与准入是舒适话题。
- **近期动态与线索**：2024 新版式上线，站活跃。
- **与我方契合点**：外包栈接入标准件+分段模板（NAC/VLAN 语境他很熟）。
- **风险与注意**：公共机构段划线；别把「数据主权」话题说破嘴——给合规材料包就好。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：埃尔朗根-纽伦堡区系统屋——服务「企业与⚠️公共机构」的安全 IT（公共段划线）。
  > IT-Systemhaus für die Region Erlangen-Nürnberg — bieten wir Unternehmen und öffentlichen Einrichtungen innovative, sichere IT-Lösungen und erstklassigen Service.
  > 来源：https://www.msit-gmbh.de/
- **【产品线与在售品牌】**六大安全主题件：IT 安全/外包/虚拟化/ITK 通信/云安全/微软支持——病毒会讲到合规与数据主权。
  > IT-Sicherheit · IT-Outsourcing · IT-Virtualisierung · ITK-Kommunikation · Sichere IT-Cloud-Lösungen · Umfassender Microsoft Support…（含）Compliance und Datenhoheit（合规与数据主权）
  > 来源：https://www.msit-gmbh.de/
- **【采购与供应链信号】**外包=外部 IT 部模式：客户网由他全管——标准件采购频繁。
  > Als externe IT-Abteilung stellen wir die Sicherheit und Effizienz Ihrer IT-Systeme sicher.（外包页）
  > 来源：https://www.msit-gmbh.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第17批.json`；价格均为 EXW 快照。

- **①背景再核**：Erlangen 安全系统屋（公共守界+工业腹地）
- **②芯片/型号**：微软体系/硬件未明
- **③KP 深挖**：info@
- **④Saga 对标**：私营工业段文档级 value 件
- **⑤在乎与偏好**：安全文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Als zuverlässiger IT-Partner für die Region Erlangen-Nürnberg bieten wir Unternehmen und öffentlichen Einrichtungen innovative, sichere IT-Lösungen”
  > “Als zuverlässiger IT-Partner für die Region Erlangen-Nürnberg bieten wir Unternehmen und öffentlichen Einrichtungen innovative, sichere IT-Lösungen”
  > 来源：https://www.msit-gmbh.de/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：Erlangen 安全系统屋（公段守界+私段主打）
- **产品线与在售品牌**：微软体系/未明示硬件
- **目标行业与场景**：工业私营（主打）+公共（守界）
- **团队与规模**：区域中型
- **决策链与对接人**：info@/M. Schmidt 具名
- **技术与认证**：安全体系
- **采购与供应链信号**：随单
- **近期动态与线索**：安全线完整
- **与我方契合点**：安全意识客户的文档级 value 件
- **风险与注意**：公共段守界

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | M. Schmidt Erlangen 安全屋：私营工业段（$165 锚点一致）；公共守界 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：区位
- **W**：墙
- **O**：工业
- **T**：在位

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
  - [ ] 硬件现供
  - [ ] 工业客户占比
  - [ ] 评窗

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Michael Schmidt IT team,

Erlangen-Nürnberg is Siemens country - engineering companies that hold every IT component to the same standard your own security practice applies. (This note concerns your private-sector engagements only; public institutions stay fully out of scope.)

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with a complete CE and test dossier. Reference: $165 USD EXW - a documented value unit for the access layer behind your private industry clients.

One question: in your private-sector projects, which switch brand holds the access layer today - and would a fully documented value alternative earn a bench test?

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

- **KP 领英直达**:[Michael Schmidt IT GmbH · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Michael%20Schmidt%20IT%20GmbH)(无具名 KP 信号,先搜公司再加人;待查)
- **中国进口与管制**:国别档位 中(IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
