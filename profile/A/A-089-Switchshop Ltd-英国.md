# Switchshop Ltd

> **评级 A**　|　英国 · Hitchin　|　档案编号 `A-089`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-089
rating: A
country: 英国
biz_org: 个体顾问（无官网）
business_model: 顾问项目制
decision_speed: fast
price_sensitivity: high
volume_potential: 1  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；顾问项目制
- **商业模式**：顾问项目制
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Switchshop 英框架大户：公共框架红线明示不碰；只谈私营段 24 口 PoE 补位（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Switchshop Ltd（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Hitchin | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Switchshop Ltd（英国）：25+ 年企业网络/网安/基建 VAR——Fortinet 英国最高位（**2025 公共部门年度伙伴**）、HPE Aruba/Juniper/**Allied Telesis（Marvell Prestera 接入层）**/Splicecom 在册；500+ 机构、137 张技术认证、全英自有工程团；ISO 9001/14001/27001+Cyber Essentials；**公共采购框架大户：NHS SBS、Crown Commercial Service LAN Lot 2a、Jisc、enFrame、DfE Everything ICT**
- 【推断】其业务主干是公共部门框架采购（学校/NHS/政府）= 我方公共段红线区；合规触达仅限其私营企业项目，定位为 Allied 旁的 value PoE 补位
- 【假设】私营段为其边角业务但真实存在（Allied+Splicecom 线）；一口价明确“不碰框架”反而加分

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@switchshop.co.uk
  - 状态：既有/公开
- **电话**：+44 1438 831870
- **原始联系字段**：+44 1438 831870 / sales@switchshop.co.uk（官网 contact 页；Allied Telesis Premier Partner，另有格拉斯哥与利兹分部）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（商业侧 LAN 项目）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：先走商业/私营侧（学校假期改造外的项目）：24 口 PoE++ 同档对比 Aruba 接入层的成本差+合规材料包。
- **要问的问题**：商业客户的接入层现在有没有兴趣加一个成本更优的选项？
- **随附证明**：规格对照 + 合规文件包 + 英国交付说明（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（工业线配套）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：正对他的工业以太网线（制造/交通/油气）：宽温 DIN PoE 与 Allied 工业件同柜报价，价差做进项目毛利。
- **要问的问题**：工业线项目的 DIN PoE 现在单价到什么位？
- **随附证明**：宽温报告 + 同规格价差对照 + DIN 图。

### 第 3 次跟进 · 管理型 PoE（私营段标准件+项目注册）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：私营/商业客户的标准件：VLAN/ERPS 模板+项目注册制，绕开框架产地敏感段，用商业项目数据说话。
- **要问的问题**：商业侧的标准件清单评审周期？我们能走一次技术评估。
- **随附证明**：VLAN/ERPS 模板 + 项目注册政策 + 实测（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第5批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：英国头部独立企业网/网安集成商：公共部门（教育/NHS/政府）为基本盘、Fortinet 年度伙伴光环加身，Allied Telesis 顶级伙伴。
- **产品线与在售品牌**：Fortinet/HPE Aruba/HPE Juniper/Allied Telesis/Acronis/Splicecom/Lenovo；CSV 记录另设独立工业以太网线（制造/交通/安防/油气/国防）。
- **目标行业与场景**：学校 LAN 改造、NHS 院区网、政府网络；工业线覆盖制造/交通/油气/国防项目的严苛环境网络。
- **团队与规模**：全英 100% 自有工程师体系，500+ 客户；中型精品集成商里的标杆。
- **决策链与对接人**：+44 1438 831870 / sales@switchshop.co.uk（官网 contact 页；Allied Telesis Premier Partner，CSV 记录）。
- **技术与认证**：137 张认证+三 ISO+CE；AMF/SDN 熟练（Allied 生态，CSV 记录）。
- **采购与供应链信号**：框架内项目对供应链合规与资质文件要求极高；工业线项目=标准件复购逻辑。
- **近期动态与线索**：2025 Fortinet 公共部门年度伙伴+框架续约季——势头正盛、供应商池子相对封闭。
- **与我方契合点**：他的工业以太网线：宽温 DIN PoE 是 Allied 工业系列的价位补充；私营/商业侧（非框架单）有议价弹性可先谈。
- **风险与注意**：⚠️ 公共部门单（NHS/教育/政府框架）对产地与声明敏感——先给合规文件包并主动说明适用边界：先谈商业与工业线，框架单后谈。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网抬头：企业级网络/网安/基础设施设计部署支持，全英客户，100% 英国本土工程师团队。
  > Switchshop designs, deploys and supports enterprise networking, cyber security and infrastructure for organisations across the UK, backed by the highest Fortinet and HPE Aruba Networking accreditations in the country, and a 100% in-house UK engineering team.
  > 来源：https://www.switchshop.co.uk/
- **【团队与规模】**数字：500+ 组织客户、25+ 年、137 张技术认证；2025 年获 Fortinet 英国公共部门年度伙伴（每年仅一家）。
  > 500+ Organisations · 25+ Years · 137 Technical Certifications · Switchshop named Fortinet Public Sector Partner of the Year — Awarded to only one partner per year from Fortinet’s UK partner network.
  > 来源：https://www.switchshop.co.uk/
- **【产品线与在售品牌】**伙伴墙：Fortinet、HPE Aruba、HPE Juniper、Lenovo、Allied Telesis、Acronis、Splicecom；资质 ISO 9001/14001/27001+Cyber Essentials。
  > Vendor Support Partners & Top-Tier Partnerships — Fortinet · HPE Aruba Networking · HPE Juniper Networking · Lenovo · Allied Telesis · Acronis · Splicecom（伙伴墙）
  > 来源：https://www.switchshop.co.uk/
- **【目标行业与场景】**英国公共采购框架全配：NHS SBS、Crown Commercial Network Services 3（LAN 段）、Jisc（教育）、enFrame、Everything ICT——教育/NHS/政府是基本盘。
  > Trusted Supplier on Major Public & Commercial Frameworks — NHS SBS Digital Workplace Solutions 2 · Crown Commercial Service Network Services 3 - Lot 2a: Intra-site Connectivity (LAN) · Jisc Network Equipment Framework（Lots 3 HPE Aruba / 6 Fortinet）· enFrame · Everything ICT
  > 来源：https://www.switchshop.co.uk/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第9批.json`；价格均为 EXW 快照。

- **①背景再核**：25 年 VAR；公共框架大户（红线区）+私营段并存
- **②芯片/型号**：Allied Telesis 在册
- **③KP 深挖**：sales@；电话并行
- **④Saga 对标**：私营段 value PoE（框架不涉）
- **⑤在乎与偏好**：三重 ISO 文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Enterprise networks…backed by the highest Fortinet and HPE Aruba accreditations in the country…Fortinet Public Sector Partner of the Year 2025”
  > “Enterprise networks…backed by the highest Fortinet and HPE Aruba accreditations in the country…Fortinet Public Sector Partner of the Year 2025”
  > 来源：https://www.switchshop.co.uk/
- **【风险与注意】**框架墙：NHS SBS Digital Workplace 2 / CCS Network Services 3 Lot 2a / Jisc / enFrame / Everything ICT（DfE）
  > 框架墙：NHS SBS Digital Workplace 2 / CCS Network Services 3 Lot 2a / Jisc / enFrame / Everything ICT（DfE）
  > 来源：https://www.switchshop.co.uk/frameworks/nhs-shared-business-services-framework

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：英国 25 年企业网络 VAR（Fortinet 公部年度伙伴）
- **产品线与在售品牌**：Fortinet/Aruba/Juniper/Allied Telesis/Splicecom
- **目标行业与场景**：公共部门为主（学校/NHS/地方政府）+私营企业段
- **团队与规模**：500+ 客户大型 VAR
- **决策链与对接人**：sales@ 口
- **技术与认证**：Fortinet 最高位+三重 ISO
- **采购与供应链信号**：框架采购为主
- **近期动态与线索**：2025 Fortinet 公部年度伙伴；2026 全网换新
- **与我方契合点**：私营段 value PoE 补位（Allied 旁）
- **风险与注意**：公共框架红线——明确不投标、不涉框架

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Switchshop 英框架大户：公共框架红线明示不碰；只谈私营段 24 口 PoE 补位（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：大客群
- **W**：红线主干
- **O**：私营
- **T**：大牌

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
  - [ ] 私营段规模
  - [ ] value 档现状
  - [ ] 试点窗

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Switchshop team,

Twenty-five years, Fortinet UK Public Sector Partner of the Year 2025, and the strongest framework coverage in the market - congratulations, earned.

To be perfectly clear upfront: this email does NOT touch your public frameworks in any way. For your private-sector projects, we build a 24-port Gigabit PoE switch (280W, 802.3af/at, watchdog) as a value complement next to your existing switching lines. Reference: $165 USD EXW.

One question: in your private-sector builds, who supplies the PoE access layer today?

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
