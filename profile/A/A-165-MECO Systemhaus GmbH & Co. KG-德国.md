# MECO Systemhaus GmbH & Co. KG

> **评级 A**　|　德国 · Boppard　|　档案编号 `A-165`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-165
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
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — MECO ISO27001 屋：合规随单 value 件（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | MECO Systemhaus GmbH & Co. KG（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Boppard | 事实 |
| 网站 | https://www.meco.de | 事实 |
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

- **邮箱**：info@meco.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：directory（R41–R48 联系方式台账口径）
- **原始联系字段**：info@meco.de [Third-party listing; not independently confirmed]; https://www.meco.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（托管栈接入层旁位选项）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：Elite 深绑定的旁位对话：24 口 PoE++ 成本对照+完整安全/固件文件包（顺 ISO 语境）。
- **要问的问题**：托管栈的接入层有没有成本旁位选项？（德文，安全文件包随附）
- **随附证明**：规格对照 + 安全/固件文件包 + 报价（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（分支点/CPE 配套）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：他卖分支 VPN 互联：分支点机柜的供电配套 4 口宽温小机。
- **要问的问题**：分支点的配套供电交换用什么？
- **随附证明**：宽温报告 + DIN 图 + 备件包价（德文）。

### 第 3 次跟进 · 管理型 PoE（托管管理件评估）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：托管管理件（VLAN/ERPS/SNMP）进他监控栈评估——过标准即套件。
- **要问的问题**：管理件要不要进你们的托管技术评估？
- **随附证明**：VLAN/ERPS 模板 + MIB 库 + 样机（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第9批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：莱茵中游 Boppard 系统屋：ISO 27001+Trust Center 的安全托管线（桌面/备份/防火墙/邮件归档），Allied **Integrate Elite** 级（CSV 记录）。
- **产品线与在售品牌**：托管服务四件套+hyper-available 备份管理+德本土云。
- **目标行业与场景**：中型企业客户的合规托管与分支互联。
- **团队与规模**：区域系统屋（法人形态变更中，CSV 留注）。
- **决策链与对接人**：info@meco.de（第三方待核——CSV 口径；首触建议先电话确认法人名称与邮箱可达）。
- **技术与认证**：ISO 27001（官网）；Allied Integrate Elite（CSV 记录）。
- **采购与供应链信号**：Elite 级 Allied 深绑定：同生态成本对照逻辑（不替位求旁位）；托管四套件=标准件采购稳。
- **近期动态与线索**：ISO 27001 获证+Trust Center 上线（近期头条）。
- **与我方契合点**：托管栈接入层旁位选项+防火墙管理线分支点的 PoE 配套（CPE 接入）。
- **风险与注意**：法人变更期先电话核对公司形态；ISO 语境下他会要安全/固件管理文件包——一次给全。

### R54 原文证据摘录（全部保留）

- **【技术与认证】**官网头条：成功通过 ISO 27001 认证并开 Trust Center——安全管理体系是招牌卖点（Allied Integrate Elite 级见 CSV）。
  > ISO 27001 zertifiziert — …dieser international anerkannte Standard gilt als Maßstab für professionelles Informationssicherheits-Management und bestätigt offiziell, dass wir Daten, Systeme und Prozesse auf einem sehr hohen Sicherheitsniveau schützen. · Trust Center（直达）
  > 来源：https://www.meco.de/
- **【产品线与在售品牌】**托管产品架：桌面管理/云备份（德国本土服务器）/防火墙管理（VPN 分支互联）/邮件归档（100% revisionssicher）。
  > Desktop Management（Tägliche Prüfung auf Fehler und Schwachstellen）· Datensicherung in der Cloud（Der Datenschutz wird durch Server auf deutschem Boden gewährleistet）· Firewall Management（Nutzung der VPN-Technologie zur Anbindung von Filialen & Co.）· E-Mail-Archivierung（Zu 100 % revisionssichere Ablage）
  > 来源：https://www.meco.de/
- **【决策链与对接人】**CSV 9-27 记录：info@meco.de 来自第三方企业库/杂志（第三方公开待核）；官网只抓得反爬文本；法人 GmbH 与旧库 GmbH & Co. KG 名称差待核（不合并不改号）。
  > 邮箱为反向文本夹杂时间戳；第三方企业库及企业杂志明确列出完整邮箱，按第三方公开待核记录。官网当前法人为 GmbH，旧库为 GmbH & Co. KG，名称变化留待核实，不合并或改编号（CSV 2026-09-27 记录）
  > 来源：https://www.unternehmen24.info/Firmeninformationen/Deutschland/Firma/1203534

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第17批.json`；价格均为 EXW 快照。

- **①背景再核**：Boppard ISO27001 系统屋（合规/备份主权）
- **②芯片/型号**：未明示
- **③KP 深挖**：info@
- **④Saga 对标**：合规随单 value 件
- **⑤在乎与偏好**：审查级文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“ISO 27001 zertifiziert…Der Datenschutz wird durch Server auf deutschem Boden gewährleistet”
  > “ISO 27001 zertifiziert…Der Datenschutz wird durch Server auf deutschem Boden gewährleistet”
  > 来源：https://www.meco.de/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | MECO ISO27001 屋：合规随单 value 件（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：合规
- **W**：审查
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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi MECO team,

ISO 27001 certification and backups on German soil - your house runs on documented, auditable trust. Any component you add to a client project has to survive the same scrutiny.

We manufacture a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with a complete CE and test dossier, ready for supplier review. Reference: $165 USD EXW - a documented value line for the access layer inside your managed projects.

One question: in your managed projects, which switch brand occupies the access layer today - and would a fully documented value alternative pass your supplier review?

If useful, I can send one unit plus the complete documentation pack for assessment. If not a fit, one line and I close the loop.

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
