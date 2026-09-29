# Alexej Sokolow / DECOIT

> **评级 A**　|　德国 · Bremen　|　档案编号 `A-026`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-026
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — DECOIT vendor-neutral 科研型：datasheet/SNMP 透明先行，Voice VLAN 对齐其 Asterisk 线；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Alexej Sokolow / DECOIT（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Bremen | 事实 |
| 网站 | decoit.de | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Alexej Sokolow | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCSWE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE+MTCSWE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sokolow@decoit.de
  - 状态：既有/公开
- **电话**：+49 421 5960640
- **原始联系字段**：+49 421 5960640 / sokolow@decoit.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Alexej Sokolow**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：以「可验证指标」开场：给他整机功率曲线、逐口数据、SNMP/MIB 清单与 CLI 文档，让他用自己的方式验（他持 MTCSWE）。
- **要问的问题**：他评估接入层交换机时，哪些指标是硬门槛（时延/功率/管理面）？
- **随附证明**：完整规格 + MIB/CLI 文档 + 一台可自测的样机。

### 第 2 次跟进 · 工业级非管理 PoE（机房外/研究现场）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：研究机构与工业客户的现场点位：宽温、DIN、免配置，减少他的运维面。
- **要问的问题**：他的客户里有没有非机房安装的网络点位？
- **随附证明**：宽温报告 + 免维护设计说明（无风扇/宽压）+ 样品价。

### 第 3 次跟进 · 管理型 PoE（自动化/监控集成）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他有 Icinga/Cacti/Munin 监控栈：把我们的交换机接进他的监控模板 + 批量配置脚本，做「可脚本化的标准化接入层」。
- **要问的问题**：愿不愿意把他的监控模板接到我们设备上做一次联调？
- **随附证明**：MIB 文件 + Icinga/Cacti 模板示例 + 批量配置脚本。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：不来梅的 IT 咨询/系统集成与软件公司（2001 年起），专做客户 IT 基础设施的优化与开源方案，并参与国家级/国际研究项目。
- **产品线与在售品牌**：**明确「厂商中立」**：不与软件授权销量绑定，但以产品组合形式合作（网络/服务器/备份/虚拟化/身份管理：oVirt、KVM、UCS、Red Hat、OpenLDAP、Active Directory；安全：pfSense、OpenVPN、IPsec NCP；监控：Icinga/Nagios/Cacti/Munin；VoIP：Asterisk、Kamailio）。
- **目标行业与场景**：科研/公共机构（Fraunhofer SIT/FOKUS、Uni Siegen、HSH、Infineon、devolo、isBremen 等研究合作伙伴）+ 企业 IT 基础设施。
- **团队与规模**：中小型技术公司（研究项目 + 服务团队），决策链短，技术负责人即决策人。
- **决策链与对接人**：Alexej Sokolow（sokolow@decoit.de；+49 421 5960640），持 **MTCSWE**（交换认证）。
- **技术与认证**：MTCNA+MTCRE+MTCSWE；官网简历强调 2001 年起优化客户 IT 基础设施。
- **采购与供应链信号**：厂商中立 = 只按技术标准与 TCO 选型，没有品牌忠诚包袱；开源栈出身 → 看重 CLI/SNMP/可脚本化与文档。
- **近期动态与线索**：官网（德语/英语双语）持续更新研究项目与产品组合；研究合作方列表 15+ 家机构。
- **与我方契合点**：MTCSWE + 开源栈：可以直接谈 VLAN/ERPS/MIB/自动化；监控栈（Icinga/Cacti）说明他们吃 SNMP 数据，我们的 MIB 支持是卖点。
- **风险与注意**：厂商中立意味着必须用「可验证指标 + 完整文档」过他的评审；别谈品牌溢价，谈可替换性与备件。

### R54 原文证据摘录（全部保留）

- **【产品线与在售品牌】**官网明确厂商中立原则（不为销量绑定品牌）。
  > In order to stay vendor-neutral we do not engage in contracts that oblige us to sell a certain amount of software licences. But we do cooperate with vendors by offering their products as part of our product portfolio.
  > 来源：https://www.decoit.de/en/home_en.html
- **【业务定位】**自 2001 年起做客户 IT 基础设施，并参与研究项目。
  > Since 2001 we attend and optimize customer IT infrastructures. Our solutions always adjust to our customers' IT infrastructure and individual processes. Additionally, we have been active in several different IT research projects, both national and international ones.
  > 来源：https://www.decoit.de/en/home_en.html
- **【技术与认证】**产品组合覆盖监控/身份/虚拟化/安全/VoIP 全套开源栈（利于 SNMP/脚本化对话）。
  > Network/server, back-up, virtualization, identity & infrastructure mgmt.（Sansymphony/Symantec/oVirt/KVM/UCS/RedHat/OpenLDAP/AD）；IT security（pfSense/OpenVPN/IPsec NCP）；Monitoring: Icinga｜Nagios｜Cacti｜Munin｜InterMapper；VoIP: Asterisk｜Kamailio｜Cisco｜Snom
  > 来源：https://www.decoit.de/en/home_en.html

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第3批.json`；价格均为 EXW 快照。

- **①背景再核**：Bremen 2001 起 25 年；科研项目墙（Fraunhofer SIT/FOKUS、Infineon、devolo）；vendor-neutral 明文不签保底销量
- **②芯片/型号**：VoIP（snom/gigaset/Cisco）+开源监控栈；交换机现用未公开
- **③KP 深挖**：Alexej Sokolow 三证（含 MTCSWE）直达邮箱
- **④Saga 对标**：开放技术档案+SNMP/Icinga 可见度为敲门砖；Voice VLAN 实测对齐其 VoIP 线
- **⑤在乎与偏好**：技术透明>价格；反对绑定 OEM；德式书面化

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Since 2001 we attend and optimize customer IT infrastructures…active in several IT research projects, both national and international”
  > “Since 2001 we attend and optimize customer IT infrastructures…active in several IT research projects, both national and international”
  > 来源：https://decoit.de/en/home_en.html
- **【技术与认证】**“In order to stay vendor-neutral we do not engage in contracts that oblige us to sell a certain amount…”+伙伴墙 Fraunhofer SIT/FOKUS/Infineon/devolo/Pulse Secure
  > “In order to stay vendor-neutral we do not engage in contracts that oblige us to sell a certain amount…”+伙伴墙 Fraunhofer SIT/FOKUS/Infineon/devolo/Pulse Secure
  > 来源：https://decoit.de/en/home_en.html
- **【决策链与对接人】**CSV 名录：Alexej Sokolow MTCNA+MTCRE+MTCSWE（Bremen）sokolow@decoit.de
  > CSV 名录：Alexej Sokolow MTCNA+MTCRE+MTCSWE（Bremen）sokolow@decoit.de
  > 来源：https://mikrotik.com/consultants

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | DECOIT vendor-neutral 科研型：datasheet/SNMP 透明先行，Voice VLAN 对齐其 Asterisk 线 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：科研背书+25年口碑
- **W**：决策慢
- **O**：科研中性硬件需求
- **T**：对商业硬件挑剔

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
  - [ ] 现用接入层品牌
  - [ ] 科研项目硬件采购窗口
  - [ ] 对 CN 制造的合规口径

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Alexej,

I found you via the MikroTik consultant list (MTCNA/MTCRE/MTCSWE) and DECOIT's vendor-neutral, research-heavy profile around Fraunhofer collaborations.

We build a 24-port Gigabit PoE switch (280W) with 4×10G uplinks, full SNMP exposure (Icinga-friendly OID list available) and a hardware PoE watchdog. Instead of a pitch, I would rather send our full technical dossier - datasheet, firmware changelog, test reports. Reference: $165 USD EXW.

One question: is your lab currently evaluating next-generation access-layer switches?

If useful, I can send one unit for a 30-day, no-obligation evaluation - publish your findings or keep them private, your call. If not a fit, one line and I close the loop.

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
