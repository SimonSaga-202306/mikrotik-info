# TQ-Systems GmbH

> **评级 A**　|　德国 · Seefeld　|　档案编号 `A-183`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-183
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
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
| 名称 | TQ-Systems GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Seefeld | 事实 |
| 网站 | https://www.tq-group.com | 事实 |
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

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@tq-group.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@tq-group.com [Publicly listed; delivery not tested]; https://www.tq-group.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 工业级非管理 PoE（自用产线/实验室网络段）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：工程师对工程师：产线测试区/实验室的宽温 DIN PoE——宽温报告/MTBF/浪涌数据摆上桌。
- **要问的问题**：产线与实验室的供电交换用什么规格？
- **随附证明**：宽温报告 + MTBF/浪涌数据 + DIN 图（德文）。

### 第 2 次跟进 · 24 口 CCTV/PoE（园区/办公接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：Seefeld 园区与办公接入层 24 口 PoE++ 成本对照。
- **要问的问题**：园区/办公接入层现在配什么？
- **随附证明**：规格对照 + 报价（德文）。

### 第 3 次跟进 · 管理型 PoE（研发网分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：研发/测试网分段：VLAN/ERPS 模板+收敛实测——给实验室同仁看得懂的文档。
- **要问的问题**：实验网分段模板要不要留一套？
- **随附证明**：VLAN/ERPS 模板 + 收敛实测（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第10批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：慕尼黑西侧 Seefeld 电子技术集团：E²MS 制造+自有嵌入式/电驱/航电产品线，Allied Resell（CSV 记录）。⚠️ 本体为制造方案商，非普通交换买家（CSV 口径）。
- **产品线与在售品牌**：E²MS 定制电子+TQ-Embedded/RoboDrive/eBike/Aviation/Automation/Medical 自有线；arkona 直播系统成功案例。
- **目标行业与场景**：高科技制造客户（他们卖电子产品给别人）；自用产线/实验室/园区网络是现实空间。
- **团队与规模**：大型技术集团（多产品线+多厂区）。
- **决策链与对接人**：info@tq-group.com（CSV 9-27：Seefeld 总部公开联系邮箱；集团层级，非具名采购）。
- **技术与认证**：Allied Resell（CSV 记录）；全系产品认证体系+PCC 自有合规中心（官网）。
- **采购与供应链信号**：制造集团=自用网络采购走设施/IT 部门：宽温工业 PoE（产线/实验环境）与 24 口（园区/办公）是现实类目；产品级嵌入不现实（他们自研电子）。
- **近期动态与线索**：新闻流活跃：arkona 大赛直播系统（2026-06）/Formula Student 车队合作/TQ.Compliant 工作坊系列。
- **与我方契合点**：自用产线与实验室的宽温工业 PoE——他自己懂电子，宽温/MTBF 数据最能对话。
- **风险与注意**：别当他们普通客户谈「卖你交换机装项目」；按自用件+数据的工程师对话走，一步一印。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：TQ-Group=电子技术集团——E²MS 电子制造服务起家，「与客户共立异标准」，自有七大产品线。
  > As a leading technology company we provide solutions to all your electronics needs. ‖ TQ-Systems has strong roots as an E²MS service provider and offers solutions for electronics needs.
  > 来源：https://www.tq-group.com/en/
- **【产品线与在售品牌】**自有产品军：TQ-Embedded 模块/E-Mobility 电助力系统/RoboDrive 无框伺服电机（上卫星）/Aviation/Automation 能源管理/Medical/PCC 合规测试中心。
  > Products & Services: TQ-Embedded · TQ-E-Mobility · TQ-RoboDrive · TQ-Aviation · TQ-Automation · TQ-Medical · TQ-PCC（Certifications and product testing）· Other Products
  > 来源：https://www.tq-group.com/en/
- **【目标行业与场景】**行业列表含工业通信/楼宇自动化/IoT 4.0/航空航天/医疗/船海/交通——高科技制造客户为主。
  > TQ industries: Agriculture · Drive technology · E-Mobility · Energy & Smart Grid · Building automation · Industrial automation · Industrial electronics · Industrial communication · IoT / Industry 4.0 · Aerospace/ Aviation · Medical technology · Robotics · Shipping & Offshore · Transportation
  > 来源：https://www.tq-group.com/en/

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
Hi TQ-Systems,

I came across TQ-Systems GmbH - 集成商/代理（Allied Telesis）.

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
