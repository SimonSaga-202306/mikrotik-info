# quattroSEC Gmbh

> **评级 A**　|　奥地利 · Zipf　|　档案编号 `A-222`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-222
rating: A
country: 奥地利
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
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 主场景匹配+首触只推一个型号的纪律；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | quattroSEC Gmbh（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 奥地利 / Zipf | 事实 |
| 网站 | https://www.quattrosec.com | 事实 |
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

- **邮箱**：office@quattrosec.com
  - 状态：待核·未验证投递（不进群发）
- **电话**：—
- 来源等级：official-obfuscated（R41–R48 联系方式台账口径）
- **原始联系字段**：office@quattrosec.com（官网明确(at)可逆还原；非猜测；未验证投递）；原入口：见 alliedtelesis.com 伙伴页
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 以厂商中立为钩：第二来源短清单

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）
- **切入点**：呼应其 herstellerunabhängig 定位：为贵司的客户方案库提供第二个编译的接入层选项（一页对比，专注供货连续性与交付期）。
- **要问的问题**：你们的方案评估清单里有没有固定接入层备选位？
- **随附证明**：一页对比（德/英）+ 交付期与保修条款。

### 第 2 次跟进 · Smart Office 安防项目 PoE 位

- **推什么**：STC-424XGGPM-440W（Saga）（万兆上联通配）
- **切入点**：Smart Home & Office 安防项目的 PoE 接入层与万兆上行。
- **要问的问题**：Smart Office 安防项目里交换/供电件怎么配？
- **随附证明**：PoE 预算表 + 安装手册（德）。

### 第 3 次跟进 · 培训/实验室小件

- **推什么**：STI-240GE（Saga）（工业非管理 4×电口 + 2×上联光）
- **切入点**：安全培训/实验室用途的小批量工业件（实物实验比虚拟更直观）。
- **要问的问题**：你们的 Trainings 课程需要可摸的硬件教具吗？
- **随附证明**：小批量试单价 + 教具折扣提案。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第12批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：上奥 Zipf 的 IT 安全专营：Allied Resell（CSV 记录）；维也纳区号总机。
- **产品线与在售品牌**：IaaS/监控/蜜罐/DDoS/CDN + 安全分析/设计/鉴定/培训 + Smart Office 安全。
- **目标行业与场景**：企业对安全与合规敏感的中型客户；Smart Home/Office 是接入层可及场景。
- **团队与规模**：安全专家小团队（总机 +43 1 2684441 00）。
- **决策链与对接人**：office@quattrosec.com（官网 imprint (at) 可逆，CSV 9-27）。
- **技术与认证**：Allied Resell（CSV）；WKO Austrian Cloud Siegel（站页徽章）。
- **采购与供应链信号**：安全商的接入层用量不大但要求稳：以「中立第二来源」给对比短清单最合适。
- **近期动态与线索**：厂商中立自述=天然开口：不顶 Allied，加入其可选件清单。
- **与我方契合点**：Smart Office/安防项目的 24 口 PoE 与实验室小批量件。
- **风险与注意**：安全公司卖身份：报价比牌页别用「更便宜」字眼，用「第二来源/供货连续性」。

### R54 原文证据摘录（全部保留）

- **【业务定位】**奥地利 IT 安全专营商，口号 your security is our mission；德/英双语站。
  > We Love What We Do ... your security is our mission!
  > 来源：https://www.quattrosec.com/
- **【产品线与在售品牌】**服务目录：IaaS/基础设施监控/蜜罐蜜网/DDoS 防护/CDN-Anycast + 安全分析/设计/鉴定/培训 + 智能家居&智能办公安全。
  > Infrastructure as a Service · Infrastructure Monitoring · Honeynets & Honeypots · DDos Schutz · CDN - Anycast Network ‖ Sicherheit im Smart Home & Smart Office
  > 来源：https://www.quattrosec.com/
- **【决策链与对接人】**自述厂商中立（herstellerunabhängig）——中立顾问姿态=我们「第二来源」话术可直接用；WKO Austrian Cloud Siegel 在页。
  > herstellerunabhängig, von der IST Aufnahme über die Bedarfsanalyse bis zur Entscheidung!
  > 来源：https://www.quattrosec.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
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
Hi quattroSEC,

I came across quattroSEC Gmbh - 集成商/代理（Allied Telesis）.

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
