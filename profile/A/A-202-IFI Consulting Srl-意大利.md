# IFI Consulting Srl

> **评级 A**　|　意大利 · Modena　|　档案编号 `A-202`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-202
rating: A
country: 意大利
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
| 名称 | IFI Consulting Srl（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Modena | 事实 |
| 网站 | https://www.ificonsulting.eu | 事实 |
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

- **邮箱**：assistenza@ificonsulting.eu
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：assistenza@ificonsulting.eu [官网正文公开邮箱；未测试投递]; https://www.ificonsulting.eu
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 工业级非管理 PoE（OT 边缘接入件；请转对口）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：顺 OT Security Suite 新线：车间 OT 边缘的宽温 DIN PoE——邮件开头注明请转 Infrastructure 对口。
- **要问的问题**：OT 项目里车间点位的供电交换用什么规格？
- **随附证明**：宽温报告 + OT 场景方案 + DIN 图（意/英）。

### 第 2 次跟进 · 24 口 CCTV/PoE（商用基建接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：基建线商用项目：24 口 PoE++ 补位件对照。
- **要问的问题**：客户机房接入层有没有补位选项？
- **随附证明**：规格对照 + 一页报价。

### 第 3 次跟进 · 管理型 PoE（IT/OT 分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：OT 安全语境：分段标准件（VLAN/ERPS/NAC 兼容）进方案库评估。
- **要问的问题**：IT/OT 分段模板要不要纳入 OT 方案库？
- **随附证明**：VLAN/ERPS 模板 + 兼容说明 + 样机。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第11批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：摩德纳多区布局数字化转型商：安全/支持/基建三瓣+OT 安全专线，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：OT Security Suite/网络安全/基础设施/云/协作+25+ 大厂伙伴墙+My-IFI 客户门户。
- **目标行业与场景**：跨区中型与制造企业； OT（工业控制安全）项目是新战线。
- **团队与规模**：中型多区服务商。
- **决策链与对接人**：assistenza@ificonsulting.eu（CSV 9-27：首页支持邮箱=转接入口，非采购专员；Modena 电话 059 47 32 399）。
- **技术与认证**：Allied Resell（CSV 记录）；多厂资质挂墙（官网）。
- **采购与供应链信号**：OT Security Suite=IT/OT 边界项目窗口：车间/厂线的 OT 边缘要工业级接入件——工业宽温 PoE 抢头位；基建线商用 24 口正路。
- **近期动态与线索**：2026-01 Splunk/2024-12 Cisco Partner/Libraesva 等新牌上墙=伙伴关系扩张期。
- **与我方契合点**：OT 边缘的工业宽温 PoE+商用接入层——顺他 OT 安全新线。
- **风险与注意**：assistenza@ 是支持台：首封标题请注明「请转 Infrastructure/Networking 对口」；大厂伙伴墙厚，按补位不替位。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：数字化转型整合商——Security/Service & Support/Infrastructure 三瓣+**OT Security Suite 独立服务线**。
  > I nostri servizi: Cybersecurity · OT Security Suite · Service & Support · Digital Transformation & Applications · Cloud · Collaboration · Infrastructure
  > 来源：https://www.ificonsulting.eu/
- **【产品线与在售品牌】**伙伴墙 25+ 牌：AWS/Cisco Partner/Check Point/Fortinet/Palo Alto/CyberArk/Splunk/Schneider/HPE/DellEMC/Lenovo/Veeam/VMware/Yealink——大厂级多厂商。
  > （伙伴墙）AWS · Check Point · Cisco Partner · Commvault · CyberArk · DellEMC · Fortinet · HPE · Lenovo · Palo Alto · Schneider · Sophos · Splunk · Veeam · VMware · Yealink
  > 来源：https://www.ificonsulting.eu/
- **【目标行业与场景】**官网自述多地实体存在（意大利多地 sedi 地图）——跨区客户布局；成功故事页运营中。
  > Grazie alla presenza fisica in differenti zone d'Italia, il team IFI progetta soluzioni… · Storie di successo（case-history 页）· My-IFI 客户门户
  > 来源：https://www.ificonsulting.eu/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：【人工定级】A —— 自动规则已跳过；人工指定
- **W**：公开信息有限
- **O**：P1 场景切入（主场景匹配+首触只推一个型号的纪律）
- **T**：现有供应商惯性；价格竞争。

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

**主题**：8-port PoE with auto-recovery for your field deployments

```text
Hi IFI,

I came across IFI Consulting Srl - 集成商/代理（Allied Telesis）.

We build a compact 8-port Gigabit PoE switch (240W budget, af/at) with a hardware PoE watchdog that power-cycles a frozen AP or camera automatically, plus clean 802.1Q VLAN / ERPS / sFlow on the management side. Reference: $99 USD EXW.

One question: How many PoE ports does a typical site of yours need today?

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
