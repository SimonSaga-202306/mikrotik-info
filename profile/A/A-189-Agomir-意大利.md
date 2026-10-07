# Agomir

> **评级 A**　|　意大利 · Lecco　|　档案编号 `A-189`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-189
rating: A
country: 意大利
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Agomir Lecco 三柱商：Sistemi 支线随单（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Agomir（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Lecco | 事实 |
| 网站 | https://agomir.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Agomir S.r.l.（意大利 Lecco，伦巴第，45 年）：**软件（自研 ERP IntegraERP/BI)+系统（infrastrutture sistemistiche e di rete 设计与运维）+服务**三柱；Zebra AutoID 伙伴（智能物流 webinar）；案例 Logicat/Stepper Italia/Protecta Group；Copilot+ PC 工作坊常态
- 【推断】“软件+系统+服务三柱”中的系统柱=网络基础设计运维——随单接入件；ERP 客户的 rollout 必配网络
- 【假设】45 年自我品牌+“persone, tecnologie, competenze”人文调=关系驱动销售，窄线耐心评估愿意

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：marketing@agomir.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：marketing@agomir.com [Publicly listed; delivery not tested]; https://agomir.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（仓库 AutoID 无线网供电层）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：顺他 Zebra AutoID 话题：仓库 AP/扫描终端的 24 口 PoE++ 供电接入层——请他转系统线对口。
- **要问的问题**：仓库无线项目的供电接入层现在配什么？
- **随附证明**：仓库场景方案 + 规格对照（意/英）。

### 第 2 次跟进 · 工业级非管理 PoE（车间/冷库点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：制造客户车间与冷库点位：宽温 DIN PoE。
- **要问的问题**：车间/冷库点位的坏机率？
- **随附证明**：宽温报告（冷库低温语境）+ DIN 图。

### 第 3 次跟进 · 管理型 PoE（厂区 IT/OT 分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：厂区业务连续性语境：分段标准件（VLAN/ERPS）+冗余收斂值——业务连续性他的产品线正好接。
- **要问的问题**：厂区 IT/OT 分段模板要不要进业务连续性方案？
- **随附证明**：VLAN/ERPS 模板 + 收敛实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第10批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Lecco 45 年 ERP+基建整合商：软件带硬件的 SMB 制造/分销客群，Allied Integrate/Resell（CSV 记录）。
- **产品线与在售品牌**：IntegraERP/BI/业务连续性+系统线（网络基建）+Zebra AutoID 物流栈对话中。
- **目标行业与场景**：伦巴第制造与分销 SMB；仓库/物流数据化项目。
- **团队与规模**：中型老牌（团队合影街拍文化）。
- **决策链与对接人**：marketing@agomir.com（CSV 9-27：页脚公开营销邮箱，可要求转采购不能当采购人直邮；另有系统支持邮箱）。
- **技术与认证**：Allied Integrate/Resell（CSV 记录）。
- **采购与供应链信号**：仓库 AutoID 热题=无线覆盖+扫描终端的 PoE 接入层项目窗口；ERP 客户多制造=车间工业件自然延伸。
- **近期动态与线索**：2026-09 Zebra AutoID 网络研讨会+意媒报道（咨讯人设）。
- **与我方契合点**：仓库 WiFi/扫描网的 PoE 供电层+车间工业件——接他 AutoID 内容热。
- **风险与注意**：marketing@ 是入口不是买家：首封请转系统/采购对口；别轰炸营销线。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：45 年 Lecco 数字化伙伴——Software（自有 gestionale 线）/Sistemi（基础设施）/Servizi 三柱。
  > Da 45 anni, collaboriamo con i nostri clienti per guidarli nell'evoluzione digitale ‖ SOFTWARE · SISTEMI · SERVIZI（三柱）
  > 来源：https://agomir.com/
- **【产品线与在售品牌】**自有方案牌：IntegraERP/AgomirBI/Business Continuity；案例流：Logicat 工时管理/Stepper Italia 订单库存/Protecta 安防 ERP——制造与分销 SMB 客群。
  > Alcune delle nostre soluzioni: IntegraERP · AgomirBI · Business continuity ‖ Case history: Logicat · Stepper Italia · Protecta Group
  > 来源：https://agomir.com/
- **【近期动态与线索】**内容流紧贴物流 AutoID：Zebra 智能物流（AI/移动/AutoID）网络研讨会+Copilot+ PC 工作坊——仓库数据化是他的热题。
  > Logistica Intelligente: la visione di Zebra Technologies su AI, mobile app e autoID（网络研讨会）· Workshop Copilot+PC e Windows 11 Pro（2026-10-15 Lecco）
  > 来源：https://agomir.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第19批.json`；价格均为 EXW 快照。

- **①背景再核**：45 年 ERP+系统三柱（网络支线+Zebra 生态）
- **②芯片/型号**：Zebra/自有 ERP
- **③KP 深挖**：marketing@
- **④Saga 对标**：系统柱随单 value 件
- **⑤在乎与偏好**：人文关系文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Da 45 anni…Software. Sistemi. Servizi…Infrastrutture sistemistiche e di rete progettate e manutenute nel tempo”
  > “Da 45 anni…Software. Sistemi. Servizi…Infrastrutture sistemistiche e di rete progettate e manutenute nel tempo”
  > 来源：https://agomir.com/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：Lecco ERP+系统三柱商（网络支线）
- **产品线与在售品牌**：Zebra/IntegraERP 自有
- **目标行业与场景**：伦巴第制造 Mittelstand
- **团队与规模**：中型
- **决策链与对接人**：marketing@ 口
- **技术与认证**：Zebra 生态
- **采购与供应链信号**：随单
- **近期动态与线索**：AutoID/物流 webinar
- **与我方契合点**：系统柱的接入随单 value 件
- **风险与注意**：

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Agomir Lecco 三柱商：Sistemi 支线随单（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：三柱
- **W**：支线
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
  - [ ] 网络牌
  - [ ] ERP rollout 模式
  - [ ] 量

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Agomir team,

Forty-five years of Software, Sistemi and Servizi from Lecco - ERP projects that always land on the network layer your Sistemi pillar designs and maintains.

We manufacture a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW - a value unit for the network closets beside your ERP and Zebra logistics deployments.

One question: in your Sistemi projects, which switch brand holds the access layer today - and would a documented value alternative earn a bench test?

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
