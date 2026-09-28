# Davide Toffoletto

> **评级 A**　|　意大利 · Udine　|　档案编号 `A-038`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-038
rating: A
country: 意大利
biz_org: 个体顾问（无官网）
business_model: 培训交付
decision_speed: fast
price_sensitivity: high
volume_potential: 2  # 1-5
needs: {poe: true, industrial: false, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: true}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：有明确交换/供电需求（交换专长、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Toffoletto 9 证老炮、公开足迹弱：特性表+电话破冰，信息缺口如实标注；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Davide Toffoletto（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Udine | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE+MTCEWE | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE+MTCEWE）

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

- **邮箱**：davide.toffoletto@gmail.com
  - 状态：既有/公开
- **电话**：+39 347 918 8529
- **原始联系字段**：+39 347 918 8529 / davide.toffoletto@gmail.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他做仓库/办公 CAPsMAN 覆盖：24 口 PoE++ 喂 AP + 摄像头，讲 PoE 预算与端口隔离；讲师身份 → 顺带提「课程实验机」合作。
- **要问的问题**：他现在的仓库/办公项目里，一台交换机要喂多少 AP？
- **随附证明**：功率预算表 + 看门狗演示 + 可公开的实测数据。

### 第 2 次跟进 · 工业级非管理 PoE（仓库/车间）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：仓库与车间不是机房环境：宽温、DIN、免配置，装进现场箱就用。
- **要问的问题**：仓库/车间现场的温湿度与安装条件如何？
- **随附证明**：宽温报告 + 现场安装图 + 样品价。

### 第 3 次跟进 · 管理型 PoE（防火墙集群旁的接入层）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他做防火墙集群与安全的接入层：VLAN 分段 + ERPS 双上行，把接入层做成「安全边界的一部分」。
- **要问的问题**：他的防火墙集群方案里，接入层冗余与分段怎么设计？
- **随附证明**：VLAN/双上行模板 + ERPS 实测 + MIB 清单。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：乌迪内的 MikroTik 认证顾问/讲师型个体工程师（无公司官网）。
- **产品线与在售品牌**：未公开品牌清单；生态以 MikroTik 为主（含企业无线 CAPsMAN）。
- **目标行业与场景**：企业级网络：交换、路由、防火墙与防火墙集群；站点间 PtP 无线；仓库与办公的室内无线覆盖（CAPsMAN）；QoS。
- **团队与规模**：个人/极小型，决策链 = 本人。
- **决策链与对接人**：davide.toffoletto@gmail.com；+39 347 918 8529（个人邮箱/手机接单）。
- **技术与认证**：**全科目 MikroTik 认证讲师**：MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE+MTCEWE——覆盖路由、无线、流量、互联、IPv6、安全与企业无线，讲师级表达能力强。
- **采购与供应链信号**：按项目/课程采购；讲师身份意味着他能把设备写进课程，小批量但影响面广。
- **近期动态与线索**：无官网；本轮公开检索仅得同名社交账号（X @dtoffoletto），未发现可用的职业主页 → 公开信息以 MikroTik 名录与 CSV 记录为准。
- **与我方契合点**：他做仓库/办公无线与防火墙集群：24 口 PoE（AP 供电）、工业款（仓库环境）、管理型（防火墙集群旁的接入层分段与环网）。
- **风险与注意**：公开信息少 → 首封邮件要靠「技术内容 + 讲师合作」建立关系；不要一上来谈价格。

### R54 原文证据摘录（全部保留）

- **【技术与认证】**既有记录：全科目 MikroTik 认证讲师，专长含交换/路由/防火墙集群。
  > ★★ 全科目 MikroTik 认证讲师；企业级网络 = 交换 switching、路由、防火墙、防火墙集群；站点间 PtP 无线；仓库与办公的室内无线覆盖（CAPsMAN）；QoS（CSV 备注）
  > 来源：https://mikrotik.com/consultants
- **【近期动态与线索】**本轮公开检索未找到可用职业主页（仅同名社交账号）。
  > Davide Toffoletto (@dtoffoletto) / X — Montebelluna, Joined July 2010（同名账号，未确认身份）
  > 来源：https://x.com/dtoffoletto

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第4批.json`；价格均为 EXW 快照。

- **①背景再核**：9 证个人顾问；公开足迹弱（如实标注）
- **②芯片/型号**：未公开
- **③KP 深挖**：本人 gmail+手机
- **④Saga 对标**：特性表对话
- **⑤在乎与偏好**：未知

### R55 证据摘录（全部保留 · 含数量）

- **【技术与认证】**CSV：Davide Toffoletto MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE 等 9 证
  > CSV：Davide Toffoletto MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE 等 9 证
  > 来源：https://mikrotik.com/consultants
- **【业务定位】**LinkedIn 搜索无命中；仅 Facebook 同名页（弱证据，不作为事实层）
  > LinkedIn 搜索无命中；仅 Facebook 同名页（弱证据，不作为事实层）
  > 来源：https://www.facebook.com/davide.toffoletto/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Toffoletto 9 证老炮、公开足迹弱：特性表+电话破冰，信息缺口如实标注 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：9证
- **W**：足迹弱
- **O**：接入层
- **T**：不可见

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 一人/个体=单点与节奏风险
- 教师红线：不打学员名单、不经培训语境推销

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
Hi Davide,

I found you on the MikroTik consultant list - nine certifications says you have been in the trenches a long time.

We build managed PoE switches (Voice VLAN, ERPS, watchdog, 4×10G uplinks on the 24-port). I keep this short because I could not find much public material - which usually means word-of-mouth business, fair enough.

One question: do your client projects ever leave room for an alternative on the switching layer?

If yes, I can send the full feature table and an evaluation unit. If not, one line and I close the loop.

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
