# ACP IT Solutions GmbH

> **评级 A**　|　德国 · Halle　|　档案编号 `A-134`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-134
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
| 名称 | ACP IT Solutions GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Halle | 事实 |
| 网站 | https://www.acp-gruppe.com/standorte/halle | 事实 |
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

- **邮箱**：halle@acp.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：halle@acp.de [Publicly listed; delivery not tested]; https://www.acp-gruppe.com/standorte/halle
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（NIS2 改造项目接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：顺着他的 NIS2 咨询潮：中型企业网段现代化的接入层 24 口 PoE++ 成本对照+合规文件包（KRITIS/公共段不供，先讲清）。
- **要问的问题**：NIS2 项目里的接入层有没有成本敏感段？（德文，附边界说明）
- **随附证明**：边界声明 + 规格对照 + 单端口测算（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（制造业客户车间段）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：机械制造客户（如客户墙里的特钢厂类）的车间段：宽温 DIN PoE 配套。
- **要问的问题**：制造业客户的车间段交换用什么？
- **随附证明**：宽温报告 + DIN 图 + 备件包价（德文）。

### 第 3 次跟进 · 管理型 PoE（NIS2 分段标准模板）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：NIS2 常见动作=分段与隔离：VLAN/ERPS/ACL 模板做进他的咨询交付件，技术评估后可进 BOM。
- **要问的问题**：分段隔离模板要不要进你们的 NIS2 交付包？
- **随附证明**：VLAN/ERPS/ACL 模板 + 收敛实测 + 评估样机（德文）


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第7批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：ACP 集团中德分部（原 Wichmann/WISYS 2018 并入）：125 人区域系统屋，自有双 DC+Veeam 备份头部+SIOS 欧洲独家+ NIS2 咨询，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：托管服务/专业服务/Veeam BaaS/双 DC 云（Mitteldeutschlandcloud）/SIOS HA/NIS2 咨询。
- **目标行业与场景**：中德中型企业与集团客户 + 公共机构（IHK/展会/市政公用/大学医院）；⚠️ 公共与 KRITIS 段（stadtwerke/医院/KRITIS 分部）划线。
- **团队与规模**：分部 ~125 人（官网），具名双人联系人体系。
- **决策链与对接人**：halle@acp.de（CSV 核验同；CSV 提醒不拿 Mannheim/奥地利邮箱代替、集团决策链要区分）。
- **技术与认证**：Allied Resell（CSV 记录）；ISO 9001/27001 双认证 DC；SIOS 欧洲独家伙伴。
- **采购与供应链信号**：中型企业 IT 换代项目（NIS2 驱动）=网络段更新批量；自有 DC 运维对交换件有专业判断力——技术评估会做得细。
- **近期动态与线索**：NIS2 咨询产品线主推（首页占位大）——NIS2 合规改造把他的客户推向网段升级。
- **与我方契合点**：中型企业 NIS2 改造里的接入层与分段件（VLAN/隔离正是 NIS2 话题）；商用 24 口+管理型分段模板正中项目潮。
- **风险与注意**：公共/KRITIS 段划线（他专门有分部做那段=那段的采购审查他最懂）；以 NIS2 商业客户为话术锚点，德文资料。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：中德分部（Halle/Dresden/Leipzig/Sangerhausen/Bielefeld 五点）30+ 年经验的 360° IT 方案伙伴。
  > Ihr regionaler Partner für sichere & belastbare IT-Infrastruktur — Mit über 30 Jahren IT-Erfahrung ist ACP Mitteldeutschland Ihr zuverlässiger Partner für innovative 360°-IT-Lösungen.
  > 来源：https://www.acp-gruppe.com/standorte/halle
- **【技术与认证】**数据主權是卖点：ISO 9001&27001 双认证自有数据中心（Dresden & Jena，Tier-3、地理冗余）；⚠️ 集团另有 Public Sector 与 KRITIS & Renewables 专项分部。
  > Als vertrauenswürdiger Partner führender globaler IT-Hersteller setzen wir Standards in puncto Datensouveränität, unter anderem mit unserem ISO 9001- & 27001-zertifizierten Rechenzentrum in Dresden und Jena.（分部导航：Public Sector · KRITIS & Renewables）
  > 来源：https://www.acp-gruppe.com/standorte/halle
- **【目标行业与场景】**客户墙：IHK Potsdam/Leipziger Messe/Stadtwerke Halle（市政公用）/Universitätsklinikum Halle/BGH 特钢——市政+医疗+工商混合。
  > Unsere Kunden（Logo 墙）：IHK Potsdam · Leipziger Messe · Stadtwerke Halle · Universitätsklinikum Halle · BGH Edelstahlwerke
  > 来源：https://www.acp-gruppe.com/standorte/halle
- **【决策链与对接人】**官网分部页公开：地址/总机/halle@ 邮箱+具名 Eric Meier（Prokurist）与 Annemarie Plaschnik（销售副总监）。
  > Daniel-Vorländer-Straße 6, 06120 Halle (Saale) · Tel: +49 345 233040 · E-Mail: halle@acp.de · Ihre Ansprechpartner: Eric Meier（Prokurist）· Annemarie Plaschnik（stellv. Vertriebsleiterin）
  > 来源：https://www.acp-gruppe.com/standorte/halle

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第14批.json`；价格均为 EXW 快照。

- **①背景再核**：ACP 中德 125 人；公共/KRITIS 红线+私营窄段
- **②芯片/型号**：全栈同盟
- **③KP 深挖**：halle@+Meier/Plaschnik 具名
- **④Saga 对标**：私营窄段 value 补位（边界句）
- **⑤在乎与偏好**：数据主权文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Public Sector…KRITIS & Renewables…ISO 9001- & 27001-zertifizierten Rechenzentrum…Kunden sind mittelständische Unternehmen und Konzerne…sowie öffentliche Einrichtungen”
  > “Public Sector…KRITIS & Renewables…ISO 9001- & 27001-zertifizierten Rechenzentrum…Kunden sind mittelständische Unternehmen und Konzerne…sowie öffentliche Einrichtungen”
  > 来源：https://www.acp-gruppe.com/standorte/halle

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：背书
- **W**：红线
- **O**：窄段
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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi ACP Halle team,

Your public-sector and KRITIS practices set a compliance bar we fully respect - this note concerns only your private mid-market engagements, and we will not touch your public or critical-infrastructure work, to be explicit.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, Voice VLAN, watchdog) with complete CE and supply-chain documentation. Reference: $165 USD EXW - a value line for mid-market access closets where the standard brands overshoot the budget.

One question: in your private-sector projects around Mitteldeutschland, which switch brand currently holds the PoE access slots?

If useful, I can send one unit with full documentation for evaluation. If not a fit, one line and I close the loop.

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
