# Michael Gisbers / Linux-Schmie.de

> **评级 A**　|　德国 · Oberhausen　|　档案编号 `A-030`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-030
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 培训交付
decision_speed: moderate
price_sensitivity: medium
volume_potential: 2  # 1-5
needs: {poe: true, industrial: false, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: true}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE），且有具体人直联
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 主场景匹配+首触只推一个型号的纪律；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Michael Gisbers / Linux-Schmie.de（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Oberhausen | 事实 |
| 网站 | linux-schmie.de | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Michael Gisbers | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCUME+MTCINE+MTCIPv6E+MTCSE+MTCSWE+MTCEWE（10 证，全证） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCUME+MTCINE+MTCIPv6E+MTCSE+MTCSWE+MTCEWE（10 证，全证））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：m.gisbers@linux-schmie.de
  - 状态：既有/公开
- **电话**：+49 173 5106822
- **原始联系字段**：+49 173 5106822 / m.gisbers@linux-schmie.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Michael Gisbers**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：MTCSWE 课程实验台 + 学员项目两用：一台设备可演示 VLAN、PoE 预算、端口隔离、看门狗；先给成本价实验机与实验手册草稿。
- **要问的问题**：他 2027 年 MTCSWE 课程的实验台还缺什么演示能力？
- **随附证明**：实验手册草稿 + 成本价实验机 + 可公开实测数据。

### 第 2 次跟进 · 工业级非管理 PoE（现场/用户组演示）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：用户组演示与现场课需要便携耐用的设备：宽温、DIN、免配置，可做「现场盒」主题分享。
- **要问的问题**：用户组活动里愿不愿意做一次工业交换机的现场演示？
- **随附证明**：宽温报告 + 便携方案 + 样品价。

### 第 3 次跟进 · 管理型 PoE（课程与安全视角）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他写安全分析：给他一份我们的管理面安全说明（默认关闭外部管理、VLAN 隔离、端口安全、固件更新流程），可写进课程的安全章节。
- **要问的问题**：他课程里的交换安全章节愿意用我们的设备做案例吗？
- **随附证明**：管理面安全配置清单 + 固件更新流程 + ERPS/VLAN 实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Oberhausen 的 MikroTik 培训与咨询个人品牌（Linux-Schmie.de）：官方认证课程、RouterOS 咨询/运维、Linux 与云集成；同时运营 MikroTik 用户组与安全博客。
- **产品线与在售品牌**：纯 MikroTik/RouterOS + Linux 生态；课程覆盖 MTCNA 到 MTCINE，2027 年起新增 **MTCSWE** 课程。
- **目标行业与场景**：德语区网络工程师培训（含考试）、企业 RouterOS 咨询；MikroTik 用户组（MUG Oberhausen）每月线上聚会，覆盖本地技术社群。
- **团队与规模**：个人品牌（本人即讲师/顾问/作者），决策链 = 本人。
- **决策链与对接人**：Michael Gisbers（m.gisbers@linux-schmie.de；+49 173 5106822）。
- **技术与认证**：MikroTik 认证顾问 **10 证全拿**（含 MTCSWE+MTCEWE）；博客做安全事件深度分析（MikroTrick CVE-2026-67276/86060）说明跟踪漏洞与补丁节奏。
- **采购与供应链信号**：培训实验设备 + 学员项目；个人采购但影响力大（用户组 + 博客 + 课程）。
- **近期动态与线索**：2026-09-16 发布「MikroTik Kurse für 2027 online – Jetzt auch mit MTCSWE」；2026-10-13 下一场 MUG Oberhausen；近期课程 MTCRE 2026-09-28、MTCEWE 2026-11-03、MTCNA 2026-12-07。
- **与我方契合点**：MTCSWE 课程刚开（2027 年批次）——需要能讲 VLAN/PoE/环网的交换机做实验台与案例；他的用户组也是本地曝光渠道。
- **风险与注意**：他写安全分析、对细节极敏感：任何夸大都会被写进博客，只给可验证数据。

### R54 原文证据摘录（全部保留）

- **【近期动态与线索】**2027 年课程计划新增 MTCSWE（交换）课程。
  > MikroTik Kurse für 2027 online – Jetzt auch mit MTCSWE … Neben MTCNA und weiteren Vertiefungskursen ist ab sofort auch der MikroTik Certified Switching Engineer (MTCSWE) verfügbar.
  > 来源：https://www.linux-schmie.de/posts/mikrotik-kurse-2027/
- **【目标行业与场景】**运营本地 MikroTik 用户组（每月线上聚会）。
  > Monatliches Treffen der MikroTik User Group Oberhausen am 2026-10-13 um 19:30 Uhr. Online-Treffen für alle Interessierten an MikroTik und RouterOS.
  > 来源：https://www.linux-schmie.de/posts/mug/mikrotik_user_group_oberhausen_2026-10-13/
- **【技术与认证】**安全博客做 CVE 深度分析（说明其技术深度与话语权）。
  > Detaillierte Analyse der 'MikroTrick'-Sicherheitslücken in MikroTik RouterOS (CVE-2026-67276, CVE-2026-86060), Informationen zu aktiven Angriffen, Patches von MikroTik und Handlungsempfehlungen für Administratoren.
  > 来源：https://www.linux-schmie.de/posts/mikrotik-routeros-mikrotrick/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（交换认证 MTCSWE），且有具体人直联
- **W**：教师红线：不打学员名单、不经培训语境推销
- **O**：P1 场景切入（主场景匹配+首触只推一个型号的纪律）
- **T**：现有供应商惯性；价格竞争。

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 教师红线：不打学员名单、不经培训语境推销

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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：8-port PoE with auto-recovery for your field deployments

```text
Hi Michael,

I came across Linux-Schmie.de - 集成商/顾问（MikroTik 认证）.

We build a compact 8-port Gigabit PoE switch (240W budget, af/at) with a hardware PoE watchdog that power-cycles a frozen AP or camera automatically, plus clean 802.1Q VLAN / ERPS / sFlow on the management side. Reference: $99 USD EXW.

One question: Which switch do you currently put on the bench for the VLAN/PoE lab demos?

If it is useful, I can send one unit for a 30-day evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)
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
