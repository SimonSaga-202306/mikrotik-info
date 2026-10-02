# Groupe Networks

> **评级 A**　|　法国 · Aubagne　|　档案编号 `A-187`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-187
rating: A
country: 法国
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
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Groupe Networks 马赛圈：数字转型方案随单件窄位（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Groupe Networks（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 / Aubagne | 事实 |
| 网站 | https://groupenetworks.fr | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Groupe Networks（法国 Aubagne/马赛圈，20+ 年）：**企业数字化转型集成商**——数字打印逻辑+**ZEENDOC 集成伙伴（法国 DMS）**+网络安全全线服务；“acteur incontournable de la cybersécurité en France”自评；客户=大企业+PME 双谱
- 【推断】打印/DMS/网络安全三线的项目随单中，网络层是其交付物的载体——接入件随单窄位
- 【假设】其“réponse globale à la gestion digitale”定位=硬件在方案里随单

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：contact@groupenetworks.fr
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：contact@groupenetworks.fr [Publicly listed; delivery not tested]; https://groupenetworks.fr
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（视监/报警 IP 项目接入层+铜换光窗口）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：法国铜网关停窗口：换光客户叠加视监/报警 IP 化的 24 口 PoE++ 接入层——租售全周期账给他客户讲。
- **要问的问题**：视监/报警 IP 项目的接入层现在配什么？（法语材料包随附）
- **随附证明**：规格对照（法）+ 租售全周期测算。

### 第 2 次跟进 · 工业级非管理 PoE（车库/户外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：车库/户外监控点位：宽温 DIN PoE。
- **要问的问题**：户外点位的坏机率？
- **随附证明**：宽温报告（法）+ DIN 图。

### 第 3 次跟进 · 管理型 PoE（MSP 托管分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他 MSP/SOC 托管语境：分段标准件（VLAN/ERPS/SNMP）纳入托管栈评估。
- **要问的问题**：托管网分段模板要不要纳入你们的栈？
- **随附证明**：VLAN/ERPS 模板 + MIB 库（法/英）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第10批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：马赛（Aubagne）360° 数字服务商：打印+电信+视监+MSP 安全一体，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：Xerox/Lexmark 打印经销、Zeendoc GED、Factorial SIRH、Beemo 备份、Sophos 安全、托管 SOC（Cyna）+视监报警。
- **目标行业与场景**：普罗旺斯地区 SMB；电信/视监/安全集成项目。
- **团队与规模**：区域服务商（TrustIndex 4.6）。
- **决策链与对接人**：contact@groupenetworks.fr（CSV 9-27：支持页公开商业/行政邮箱；主联系页为表单）。
- **技术与认证**：ExpertCyber 标签（HEO 实体）；Allied Resell（CSV 记录）。
- **采购与供应链信号**：订购制（abonnement mensuel/location déductible）模式=设备按月租算：接入层件租售比账最能谈；铜网关停=全法企业换光纤接入的窗口，SFP/光纤接入件需求抬头。
- **近期动态与线索**：铜网关停内容营销正热（2026-09 博客）。
- **与我方契合点**：视监/报警 IP 项目的 PoE 接入层+铜换光窗口的光纤接入件——租售模式按全周期账谈。
- **风险与注意**：法国 SMB 重关系：先给法语材料包+租售测算；别催单节奏。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：马赛企业数字化 360°——打印（Xerox/Lexmark 官方经销）/GED/SIRH/大屏/电信/视监报警/IT 安全 MSP/备份八瓣花。
  > Notre métier : tout le numérique d'entreprise — IMPRESSION · GED · SIRH · AFFICHAGE · TÉLÉCOMS · VIDÉO · SÉCURITÉ IT · SAUVEGARDE ‖ Votre Concessionnaire et Distributeur officiel: XEROX, LEXMARK, Zeendoc, Factorial, Beemo et Sophos à MARSEILLE
  > 来源：https://groupenetworks.fr/
- **【技术与认证】**姐妹实体 HEO NETWORKS 获 ExpertCyber 认证标签+托管 SOC（Cyna）——网络安全产品线自有资质。
  > HEO NETWORKS est labelisé Expert Cyber（ExpertCyber 标签图）‖ SOC managé（Cyna）· sécurité informatique
  > 来源：https://groupenetworks.fr/
- **【近期动态与线索】**博客紧贴政策脉冲：**法国铜网关停**（fin du cuivre）为中小企业写应对指南+ANSSI 2025 威胁全景+IA Act 合规工具。
  > La Fin du Cuivre en France : Ce que les PME doivent impérativement anticiper ‖ Décryptage du Panorama ANSSI 2025 · Conformité IA Act : Le Tableau de Bord Pratique
  > 来源：https://groupenetworks.fr/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第19批.json`；价格均为 EXW 快照。

- **①背景再核**：马赛圈数字化转型集成（ZEENDOC/安全，20+ 年）
- **②芯片/型号**：未明
- **③KP 深挖**：contact@
- **④Saga 对标**：方案随单接入件（窄位）
- **⑤在乎与偏好**：法语文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Nous apportons aux grandes entreprises et PME une réponse globale à la gestion digitale…Fort de plus de 20 ans d’expérience[Groupe Networks 官网/官档]”
  > “Nous apportons aux grandes entreprises et PME une réponse globale à la gestion digitale…Fort de plus de 20 ans d’expérience[Groupe Networks 官网/官档]”
  > 来源：https://groupenetworks.fr/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：马赛圈数字转型集成商（ZEENDOC/安全）
- **产品线与在售品牌**：ZEENDOC 伙伴
- **目标行业与场景**：大企业+PME
- **团队与规模**：区域中型
- **决策链与对接人**：contact@ 口
- **技术与认证**：—
- **采购与供应链信号**：项目随单
- **近期动态与线索**：网络安全线
- **与我方契合点**：方案随单的接入件窄位
- **风险与注意**：

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Groupe Networks 马赛圈：数字转型方案随单件窄位（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：区域
- **W**：边埴
- **O**：随单
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
  - [ ] 网络件现供
  - [ ] 随单率
  - [ ] 量

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Groupe Networks team,

Twenty years answering digital transformation for enterprises and SMBs from Aubagne - print, document management, cybersecurity. Every one of those solutions eventually lands on an access switch.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW - a value unit for the network layer behind your digital-transformation projects.

One question: in your integration projects, which switch brand holds the PoE access layer today - and would a documented value alternative earn a bench test?

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

- **KP 领英直达**:[Groupe Networks · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Groupe%20Networks)(搜索链接,点入后核职位再加;来源:档案名(个人档))
- **中国进口与管制**:国别档位 中(ANSSI 3A 授权制;企业交换机不限);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
