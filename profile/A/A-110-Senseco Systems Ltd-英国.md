# Senseco Systems Ltd

> **评级 A**　|　英国 · Gillingham　|　档案编号 `A-110`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-110
rating: A
country: 英国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: true, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — 主场景匹配+首触只推一个型号的纪律；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Senseco Systems Ltd（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Gillingham | 事实 |
| 网站 | https://www.sensecosystems.com | 事实 |
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

- **推断需求面**：PoE 接入供电、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@sensecosystems.com
  - 状态：既有/公开
- **电话**：+44 (0) 845 644 2888
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：sales@sensecosystems.com [Publicly listed; delivery not tested]; https://www.sensecosystems.com; +44 (0) 845 644 2888
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（安防监控项目接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：借品牌更新窗口期递资料：监控/门禁项目接入层 24 口 PoE++ 成本对照+低功耗数据（呼应他 CarbonNeutral 叙事）。
- **要问的问题**：（双品牌落款）安防项目的接入层现在用哪个型号？功耗指标在测算里吗？
- **随附证明**：单端口测算 + 功耗对照 + 规格对照（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（屋面/机房外监控点）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：屋面摄像头、泵房/车库烟感联网点：宽温小机随项目配套。
- **要问的问题**：屋面和机房外点位用什么供电交换？
- **随附证明**：宽温报告 + DIN 图 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（INTEGRATION 线标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他的 INTEGRATION 线：安防/消防监控/楼控三网分段的 VLAN/ERPS 模板标准件。
- **要问的问题**：集成项目的网络分段模板有没有标准化？
- **随附证明**：VLAN/ERPS 模板 + 收敛实测 + 评估样机（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第6批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Kent Gillingham 起家的全英消防+安防集成商：消防（报警/喷淋/气体灭火）+安防+监控+集成系统九线一体，Allied 代理（CSV 记录）。
- **产品线与在售品牌**：FIRE/PASSIVE/SPRINKLERS/SUPPRESSION/VOICE/SECURITY/MONITORING/INTEGRATION 八条线；集成线=安防网与 IoT 的泊接点。
- **目标行业与场景**：商业楼宇/高校/数据中心（Comms Room 气体灭火产品线侧面印证 DC 客群）/酒店医疗。
- **团队与规模**：工程师创立、工程师领导（官网自述），全英多办公室。
- **决策链与对接人**：sales@sensecosystems.com；+44 (0) 845 644 2888；北区另有销售入口（CSV 9-27 核验记录）。
- **技术与认证**：Allied 代理（CSV 记录）；CarbonNeutral 认证。
- **采购与供应链信号**：消防+安防一体项目：监控摄像头/门禁/火灾盘联网的 PoE 需求随项目批量——其 INTEGRATION 线是网络件落点。
- **近期动态与线索**：2026-04 新品牌资源（andwis）→ 若更名/集团化进行中，供应商目录会重排——正是递资料窗口。
- **与我方契合点**：安防网接入 24 口 PoE+机房外/屋面消防监控点位的工业件；ESG 叙事下低功耗卖点可呼应。
- **风险与注意**：更名期组织归属不明：报价与沟通都写双品牌落款；消防联动属生命安全系统，交换件只做非联动的监控/门禁段。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网自述：行业领先的独立消防与安防专家，设计-供货-安装-调试-维护全链覆盖。
  > Senseco Systems is an industry-leading, independent fire and security specialist. We’re experts in the design, supply, installation, commissioning and maintenance of fire, passive, sprinklers, suppression, voice, security, monitoring and integrated systems.
  > 来源：https://www.sensecosystems.com/
- **【团队与规模】**从伦敦与东南起步，现已全英多办公室；英国首家 CarbonNeutral 认证消防安防公司。
  > Whilst we started working in London and the South East, we now have offices across the UK, offering an unrivalled level of expertise… Plus, we’re proud to be the UK’s first CarbonNeutral-certified fire and security company.
  > 来源：https://www.sensecosystems.com/
- **【近期动态与线索】**官网工程师文化自述+2026-04 上传的新 Logo 资源文件名「andwis」——疑似品牌更新进行中（如实标注，待核实）。
  > Senseco, Founded by Engineers, Led by Engineers（官网宣传片标题）·（2026-04 Logo 资源文件名：FINAL-andwis-Logo-Assets）
  > 来源：https://www.sensecosystems.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
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

**主题**：24-port PoE + 10G uplinks for your larger sites

```text
Hi Senseco,

I came across Senseco Systems Ltd - 集成商/代理（Allied Telesis）.

We build a 24-port Gigabit PoE switch (280W, af/at) with 4×10G SFP+ uplinks, Voice VLAN and a hardware PoE watchdog that reboots hung APs/cameras without a site visit. Reference: $165 USD EXW.

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
