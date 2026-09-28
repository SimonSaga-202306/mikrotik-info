# BRS Networks AB

> **评级 A**　|　瑞典　|　档案编号 `A-112`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-112
rating: A
country: 瑞典
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
- **为什么值得跟**：有明确交换/供电需求（光纤接入），三星重点
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — 主场景匹配+首触只推一个型号的纪律；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | BRS Networks AB（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 瑞典 | 事实 |
| 网站 | https://brsnetworks.se | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层）+ Fortinet | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层）+ Fortinet）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@brsnetworks.se
  - 状态：既有/公开
- **电话**：—
- 来源等级：company-social（R41–R48 联系方式台账口径）
- **原始联系字段**：info@brsnetworks.se [Publicly listed; delivery not tested]; https://brsnetworks.se
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（NaaS 标准接入件）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：NaaS 模式的 CPE 标准件：24 口 PoE++ 成本对照+全生命周期质保（RMA 流程图附上），给他算每个客户站点的成本差。
- **要问的问题**：NaaS 客户站点的接入件现在标准化到哪个型号？
- **随附证明**：单站点测算 + RMA 流程 + 瑞典交付说明（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（电网/建筑 OT 段）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：电网分包与建筑工地的 OT 点位：宽温 DIN PoE 恶劣环境免维护，配 24×7 监控服务的备件方案。
- **要问的问题**：OT 站点（elnät 分包）的供电交换坏机率如何？备件策略发你看看。
- **随附证明**：宽温/-40 冷启动报告 + 备件包价 + MTBF 数据。

### 第 3 次跟进 · 管理型 PoE（NaaS 汇聚/分段标准+三国框架）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：NaaS 汇聚层与站点分段标准：VLAN/ERPS 模板+集中监控 MIB；他三地经营——谈一份 SE/DK/DE 统一渠道框架。
- **要问的问题**：丹麦德国的业务用同一套标准件吗？三国供货框架有兴趣聊吗？
- **随附证明**：VLAN/ERPS 模板 + MIB + 三国供货/质保条款（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第6批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：瑞典（哥得兰 Visby 起家）全国 MSP+光纤网络方案商：IT 托管+网络安全+NaaS+数字基础设施，业务覆盖瑞典/丹麦/德国（CSV 记录），Allied+Fortinet 信号。
- **产品线与在售品牌**：现代办公/网络安全/NaaS/数字 infrastructure 四线；Allied Telesis+Fortinet（CSV 信号记录）。
- **目标行业与场景**：医疗/建筑/电网/金融客户的 IT 与 OT 全托管——电网 OT 段=工业交换主战场。
- **团队与规模**：80 名技术专家（官网），15 年公司，全国支持网络。
- **决策链与对接人**：info@brsnetworks.se（CSV 9-27 核验：Facebook 公开邮箱，Visby 地址电话相符）。
- **技术与认证**：Allied+Fortinet 资质（CSV 记录）。
- **采购与供应链信号**：NaaS=CPE 标准件持续采购；OT 监控 24×7 服务对坏机零容忍——备件与 MTBF 资料比低价更管用。
- **近期动态与线索**：网站 2025-2026 版式新、服务线扩张中（NaaS 独立成线）。
- **与我方契合点**：NaaS 标准接入件（24 口 PoE）+电网 OT 段工业宽温件；三地经营给我们一次进三国的机会。
- **风险与注意**：瑞典决策重证据与本地服务：英文资料+明确瑞典/欧盟交付与 RMA 流程；OT/电网段合规边界讲清楚（只做商业配套段）。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网三段口号：就是能用的 IT、有感知的网络安全、强化你业务的伙伴——瑞典 MSP。
  > IT som bara fungerar. Cybersäkerhet som märks. En partner som stärker er verksamhet.
  > 来源：https://brsnetworks.se/
- **【产品线与在售品牌】**四大服务线含「Nätverk som tjänst（网络即服务）」与数字基础设施——NaaS 模式=标准件批量采购逻辑。
  > Modern arbetsplats · Cybersäkerhet · Nätverk · Digital infrastruktur（服务线；Nätverk som tjänst 为其子页）
  > 来源：https://brsnetworks.se/
- **【团队与规模】**数字：全年无休守护 IT 与 OT 环境、15 年技术热情、80 名技术专家、全国覆盖的本地支持。
  > Säkrar och övervakar IT- och OT-miljöer dygnet runt, året om · 15 år av passion för teknik, IT och långsiktiga relationer · 80 tekniska experter levererar tillförlitliga tjänster anpassade efter dina behov
  > 来源：https://brsnetworks.se/
- **【目标行业与场景】**客群列举含医疗、建筑、电网（elnät）、金融——OT/电网段的工业网络需求明确。
  > Oavsett om ni arbetar inom sjukvård, bygg, elnät eller ekonomi får ni en partner som följer er utveckling.
  > 来源：https://brsnetworks.se/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（光纤接入），三星重点
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
Hi BRS,

I came across BRS Networks AB - 集成商/代理（Allied Telesis）.

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
