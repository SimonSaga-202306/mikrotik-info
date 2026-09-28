# NetHighTech

> **评级 A**　|　葡萄牙 · Lisboa　|　档案编号 `A-262`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-262
rating: A
country: 葡萄牙
biz_org: 公司/工作室（有官网）
business_model: 培训交付
decision_speed: moderate
price_sensitivity: medium
volume_potential: 2  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: true, oem: false, hotel: false, training: true}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE），三星重点
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 主场景匹配+首触只推一个型号的纪律；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | NetHighTech（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 葡萄牙 / Lisboa | 事实 |
| 网站 | https://www.nethightech.com | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 培训伙伴，持 MikroTik 培训伙伴（开 MTCSWE 等课程） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 培训伙伴，持 MikroTik 培训伙伴（开 MTCSWE 等课程））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：nethightech@gmail.com（既有/公开）
- **电话**：—
- 来源等级：official-search-only（R41–R48 联系方式台账口径）
- **原始联系字段**：nethightech@gmail.com（待核：仅搜索索引，对应课程页本轮已404；未测试投递）；原入口：见 mikrotik.com/training
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 表单/电话核联络+演示机位

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ 演示机可选）
- **切入点**：先经官网表单一句核实对接人；随后一封（葡/英）只邀其 ISP/WISP PoC 环境与 MikroTik 课程实验自用演示机。
- **要问的问题**：OmniEdge 的 PoC 演示环境用得上高性价比 24 口 PoE 接入层吗？
- **随附证明**：一页规格（葡/英）。

### 第 2 次跟进 · 有回复才续：实验备件小批

- **推什么**：—（按回复定）
- **切入点**：仅当其回复感兴趣，补备件小批价卡。
- **要问的问题**：—
- **随附证明**：小批价卡一页。

### 第 3 次跟进 · 无回复即冻结

- **推什么**：—
- **切入点**：无回复不再自动化跟进（转型期公司，不追）。
- **要问的问题**：—
- **随附证明**：—。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：里斯本 MikroTik 培训伙伴（MTCSWE 课在列，CSV）——现主业企业 AI 软件平台（其 OmniEdge BRAS 明写服务 ISP/WISP 客户）。
- **产品线与在售品牌**：OmniCore/OmniEdge/SolarOps/OmniBrain 四件自有软件+IT 学院（MikroTik/Cisco/AI/Linux）。
- **目标行业与场景**：ISP/WISP 软件客群（BNG/计费）+企业 AI 改造客群；培训学员群。
- **团队与规模**：软件团队（预约 demo 制）。
- **决策链与对接人**：nethightech@gmail.com（**搜索索引级待核**，CSV 9-27）；先表单/电话核。
- **技术与认证**：MikroTik 培训伙伴（官方课程表，CSV）。
- **采购与供应链信号**：其 ISP/WISP 软件 PoC 与培训实验=潜在的硬件演示/实验位；但其已非硬件渠道——**只谈自用实验与 PoC 演示机，不谈渠道**。
- **近期动态与线索**：向 AI 软件整体转型中（2026 站全面重做）=培训线收缩风险，硬件口很窄。
- **与我方契合点**：尊重型一封：OmniEdge 的 ISP/WISP PoC 环境要不要高性价比接入层演示机。
- **风险与注意**：Gmail 不直发；不向其学员推销；若核得其已完全不做硬件，归档冻结。

### R54 原文证据摘录（全部保留）

- **【业务定位】**里斯本 MikroTik 培训伙伴（官方课程表在列，CSV）——**现官网已整体转型企业级 AI 软件**：OmniCore AI（厂商无关网络/IoT/ERP 控制）、OmniEdge BRAS（运营商级 BNG/TR-069 ACS/ISP 计费，明写面向 ISP 与 WISP）、SolarOps AI、OmniBrain AI。
  > Carrier-Grade BNG, TR-069 ACS & ISP Billing — OmniEdge BRAS … designed for modern ISPs and WISPs ‖ Universal Network, IoT & ERP Controller — OmniCore AI — completely vendor-agnostic platform
  > 来源：https://www.nethightech.com/
- **【近期动态与线索】**首页仍保留 Enterprise IT Academy 栏目并列出 MikroTik 课程（Routing & Bandwidth Mgmt），另有 Cisco/AI/Linux 课线。
  > Enterprise IT Academy ‖ MikroTik — Routing & Bandwidth Mgmt ‖ Cisco — Advanced Enterprise Networks
  > 来源：https://www.nethightech.com/
- **【决策链与对接人】**nethightech@gmail.com 仅见搜索索引（对应课程页本轮 404），CSV 定级 official-search-only 待核——**第一步先经表单/电话核联络，不直发 Gmail**。
  > （CSV 2026-09-27 记录）official-search-only：邮箱与电话仅见于搜索索引（对应课程页本轮返回 404，首页仍含 MikroTik 培训栏目）
  > 来源：https://www.nethightech.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（交换认证 MTCSWE），三星重点
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

**主题**：8-port PoE with auto-recovery for your field deployments

```text
Hi NetHighTech,

I came across NetHighTech - 集成商/顾问（MikroTik 认证）.

We build a compact 8-port Gigabit PoE switch (240W budget, af/at) with a hardware PoE watchdog that power-cycles a frozen AP or camera automatically, plus clean 802.1Q VLAN / ERPS / sFlow on the management side. Reference: $99 USD EXW.

One question: Which switch do you currently put on the bench for the VLAN/PoE lab demos?

If it is useful, I can send one unit for a 30-day evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

Best regards,
Saga Communications - PoE switch OEM/ODM (neutral packing available)
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
