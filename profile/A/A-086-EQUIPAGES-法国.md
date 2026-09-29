# EQUIPAGES

> **评级 A**　|　法国 · Voisins Le Bretonneux　|　档案编号 `A-086`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-086
rating: A
country: 法国
biz_org: 个体顾问（无官网）
business_model: 顾问项目制
decision_speed: fast
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；顾问项目制
- **商业模式**：顾问项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），三星重点
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — EQUIPAGES 法全 SI 集成：办公网无线/VoIP 接入柜随单+infogérance 滚动（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | EQUIPAGES（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 / Voisins Le Bretonneux | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 分销/集成商（Perle 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网） | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】EQUIPAGES（法国）：2007 年起的 IT 集成商——全 SI 生命周期（架构→部署→迁移→能力转移→支持→外包 infogérance）；业务面：协作/O365、**VoIP 电话**、无线网、路由/防火墙/代理、光纤布线、安全（EDR/XDR/ZTNA）、云私有/备份、24×7 支持；CSV：Perle 工业 PoE 线
- 【推断】办公网+无线+VoIP 三线都吞接入层 PoE；infogérance 客群=滚动翻修口
- 【假设】其“exigence 方法论”文风=做深度学习后的高质提案适配

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：contact@equipages.fr
  - 状态：既有/公开
- **电话**：—
- **原始联系字段**：contact@equipages.fr（大区邮箱：contact-idf@ / contact-paca@ / contact-rha@ / contact-na@equipages.fr）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（网络改造项目接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：顺着他 WS2016/机房整改潮：接入层 24 口 PoE++ 随整改项打包，规格+英法资料+RMA 承诺一次给全。
- **要问的问题**：机房整改项目里的接入交换现在主要配什么？
- **随附证明**：规格对照 + RMA 承诺函 + 英法资料。

### 第 2 次跟进 · 工业级非管理 PoE（工业/楼宇客户点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：工业与楼宇客户的无空调区点位：宽温 DIN PoE 补充他的 Perle 线价位段。
- **要问的问题**：工业客户的边缘点位用什么交换？Perle 价有没有压力？
- **随附证明**：宽温报告 + 同规格价差对照 + DIN 图。

### 第 3 次跟进 · 管理型 PoE（托管客户标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：托管网 VLAN 分段与 ERPS 冗余的统一模板+监控接口（SNMP/MIB 全），匹配他 24×7 运维体系。
- **要问的问题**：托管客户的接入层有没有标准化型号？
- **随附证明**：VLAN/ERPS 模板 + MIB 库 + 项目注册政策。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第5批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：巴黎西郊 19 年的系统集成+托管服务商：企业 IT 全生命周期，网络/安全/机房三轴，Perle 授权渠道（CSV 记录）。
- **产品线与在售品牌**：集成项目（无线网络/路由防火墙/光纤/EDR/私有云/备份）+ 24×7 外包运维；Perle 工业联网件（CSV 记录）。
- **目标行业与场景**：法兰西岛及多区企业客户：办公网改造、机房建设、网络安全升级；WS2016 停服换机潮（博客在推）。
- **团队与规模**：2007 年至今的中型 MSP：项目经理+集成工程师班底，多区域邮箱（idf/paca/rha/na）。
- **决策链与对接人**：contact@equipages.fr（总部）+大区邮箱（CSV 记录）。
- **技术与认证**：系统集成/网络/网安三栈；Perle 渠道（CSV 记录）；认证合集页（nos-certifications）。
- **采购与供应链信号**：项目制批量+托管客户持续小量；安全类博客密集说明在推升级项目，交换与 PoE 随网络改造走量。
- **近期动态与线索**：WS2016 EOL（2027-01）引发的机房整改潮已经在他们内容排期里——项目窗口明确。
- **与我方契合点**：网络改造项目的接入层与工业园区客户的工业 PoE；托管客户 SLA 场景需要备件响应——我们能给。
- **风险与注意**：法国 MSP 重关系与本地服务：首轮英法双语资料+明确本地备件/RMA 承诺；别只发价目表。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：覆盖客户全部 IT 诉求的集成/托管商，全生命周期陪伴（架构/部署/迁移/培训/支持/外包）。
  > Equipages accompagne ses clients sur l’ensemble de leurs enjeux informatiques… architecture, déploiement, migration, transfert de compétence, support et infogérance.
  > 来源：https://www.equipages.fr/
- **【产品线与在售品牌】**网络线明确：无线网、路由/防火墙/代理、光纤布线，加安全（EDR/XDR/ZTNA/IAM/私有云）与 24×7 托管。
  > Réseaux sans fil · Routeurs, firewall, proxy · Fibre optique ‖ Antivirus, EDR, XDR, ZTNA · Authentification & IAM · Cloud Privé ‖ Support technique et utilisateur 24×7
  > 来源：https://www.equipages.fr/
- **【团队与规模】**2007 年创立，自述技术基因（「l’expertise technique est… notre ADN」），按大区邮箱分点服务。
  > Depuis 2007, Equipages réunit une équipe d’experts en intégration système, réseau et cybersécurité autour d’une vision partagée…
  > 来源：https://www.equipages.fr/
- **【近期动态与线索】**2026 年 9 月仍在发技术博客（PCA/PRA、SASE/SIEM/XDR 解析、Windows Server 2016 停服提醒）——内容营销活跃。
  > 2026-09 — PCA PRA et fournisseurs… · SASE, SIEM, XDR, SOC, VOC, MDR : qui fait quoi en cybersécurité ? · Windows Server 2016 : comment préparer la fin du support en janvier 2027 ?
  > 来源：https://www.equipages.fr/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第9批.json`；价格均为 EXW 快照。

- **①背景再核**：2007 起全 SI 集成；无线/VoIP/布线三线实
- **②芯片/型号**：Perle（CSV）
- **③KP 深挖**：contact@+大区分箱
- **④Saga 对标**：办公网 24 口 PoE 随单；工业段后顾
- **⑤在乎与偏好**：质方法论（题深应广）

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Couvrir l’ensemble de votre SI…Téléphonie (VoIP), Réseaux sans fil, Fibre optique…Support 24×7”
  > “Couvrir l’ensemble de votre SI…Téléphonie (VoIP), Réseaux sans fil, Fibre optique…Support 24×7”
  > 来源：https://www.equipages.fr/
- **【近期动态】**2026-09 三连博文（PCA-PRA/SASE-SIEM 科理谱/WS2016 EOS 2027-01）
  > 2026-09 三连博文（PCA-PRA/SASE-SIEM 科理谱/WS2016 EOS 2027-01）
  > 来源：https://www.equipages.fr/
- **【联系方式】**contact@equipages.fr；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > contact@equipages.fr；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://www.equipages.fr/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：法国 IT 集成商（全生命周期 infogérance）
- **产品线与在售品牌**：O365/EDR/ZTNA 生态+Perle
- **目标行业与场景**：中小企业办公网/移动办公
- **团队与规模**：中型集成商
- **决策链与对接人**：contact@ 口
- **技术与认证**：方法论化集成（DNA 技术口号）
- **采购与供应链信号**：项目随单+外包滚动
- **近期动态与线索**：2026-09 博客活跃（PCA/PRA、Windows 2016 EOS）
- **与我方契合点**：办公网无线/VoIP 接入层随单
- **风险与注意**：中小客群价敏

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | EQUIPAGES 法全 SI 集成：办公网无线/VoIP 接入柜随单+infogérance 滚动（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：生命周期
- **W**：价敏
- **O**：滚动
- **T**：大厂

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 一人/个体=单点与节奏风险

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
  - [ ] 项目量
  - [ ] 接入层现供
  - [ ] 翻修节奏

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Equipages team,

A full-lifecycle integrator that runs VoIP, wireless and fiber cabling under one roof knows exactly where those three meet - the access cabinet.

We build a 24-port Gigabit PoE switch (280W, 802.3af/at, Voice VLAN, watchdog) sized for exactly that cabinet, with documentation that respects your exigence methodology. Reference: $165 USD EXW.

One question: in your typical SME office build, which switch supplies the PoE access layer today?

If useful, I can send one unit with full documentation. If not a fit, one line and I close the loop.

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
