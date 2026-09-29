# Wire Technologies, Inc.

> **评级 A**　|　美国　|　档案编号 `A-130`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-130
rating: A
country: 美国
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
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Wire Technologies 30 年布线/DC/交换直通：直接对口接入层 value 位（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Wire Technologies, Inc.（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 | 事实 |
| 网站 | https://wiretechnologies.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Wire Technologies, Inc.：30+ 年 IT 基建全栈商——结构化布线/数据中心/**路由交换（30 年设计实施经验）**/无线（20+ 年数百网部署）/语音视频会议/云/网络安全/服务器虚拟化备份/**门禁与监控**；联系域 wiretech-inc.com（Barracuda ESS MX 存活，独立双域同归）
- 【推断】CSV 载 Allied Telesis 信号与其“Routing & Switching 30 年”自述相互印证=接入交换是其核心惯件
- 【假设】最对口对象之一：布线+DC+交换三线合一——接入层 value 位切入直接专业

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

- **邮箱**：info@wiretech-inc.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@wiretech-inc.com [Publicly listed; delivery not tested]; https://wiretechnologies.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（厂房/楼宇接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：给「30 年路由交换」工程师的直球：24 口 PoE++ 规格与成本对照清单，技术细节一次给全。
- **要问的问题**：厂房/楼宇项目的接入层现在配什么？对照清单给到你。
- **随附证明**：规格对照 + 单端口测算 + 全套数据手册（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（产线/库房点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：制造客户的产线旁与库房：宽温 DIN PoE 粉尘高温稳定——demo 机先试。
- **要问的问题**：产线旁的 PoE 点位坏机率如何？
- **随附证明**：宽温报告 + DIN 图 + 评估样机。

### 第 3 次跟进 · 管理型 PoE（整网分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他交付整网：VLAN/ERPS 分段模板+10G 上行真机评估，工程师对工程师。
- **要问的问题**：整网分段模板要不要对比跑一轮？
- **随附证明**：VLAN/ERPS 模板 + 收敛实测 + 样机（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第7批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：威州 Kaukauna 30+ 年网络集成商：布线/DC/路由交换/无线/安防一体的老牌，Allied 代理（CSV 记录）。⚠️ 与 A-114 Amplitel 同城不同实体，别互串。
- **产品线与在售品牌**：数据中心与结构化布线（基础设施/硬件）+云与无线+安全监控+服务器虚拟化备份四大块。
- **目标行业与场景**：威州及周边企业：制造业厂房/办公楼/园区的整网交付。
- **团队与规模**：30+ 年公司（官网自述）。
- **决策链与对接人**：info@wiretech-inc.com（CSV 9-27 核验：页脚真实；正文模板邮箱与假电话已排除）。
- **技术与认证**：Allied 代理（CSV 记录）。
- **采购与供应链信号**：整网项目制：DC/厂房从布线到交换一包，接入层是他的核心件；制造业客户=工业场景多。
- **近期动态与线索**：官网 2023 版式+服务全面；无新闻流=口碑盘。
- **与我方契合点**：厂房 DC/产线周边的工业 PoE 与接入层 24 口：技术对话对象就是「路由交换 30 年」的工程师老板。
- **风险与注意**：与同城 Amplitel（A-114）别交叉报价；投递地址用 CSV 核验的 info@wiretech-inc.com 而非页面模板残留邮箱。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网口号：无缝 IT、随处可达——响应快、懂行、有人情味的个性化支持。
  > Seamless IT, Anywhere. · Responsive Knowledgeable Support on a Personal Level… ensuring your technology challenges are addressed with expertise and care.
  > 来源：https://www.wiretechnologies.com/
- **【技术与认证】**官网自述：路由与交换基础设施的设计/实施/支持经验 30+ 年——交换是其老本行。
  > Wire Technologies Inc. has been providing expert design, implementation, and support of routing and switching infrastructure for over thirty years.
  > 来源：https://www.wiretechnologies.com/
- **【产品线与在售品牌】**全谱系：布线/数据中心/路由交换/无线（20+ 年数百张网）/语音视频/云/网安/门禁摄像头/服务器存储虚拟化。
  > Structured Cabling · Data Center · Routing & Switching · Wireless — deployed hundreds of wireless network solutions across many business sectors over the past 20 plus years · Voice and Video · Cloud Solutions · Network Security · Access Control and Cameras · Server Storage
  > 来源：https://www.wiretechnologies.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第13批.json`；价格均为 EXW 快照。

- **①背景再核**：30 年全栈（布线+DC+交换直通）；无线 20 年
- **②芯片/型号**：CSV Allied 信号+交换自述印证
- **③KP 深挖**：info@wiretech-inc.com（双域验真）
- **④Saga 对标**：接入层 value 位（直接对口）
- **⑤在乎与偏好**：专业文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“expert design, implementation, and support of routing and switching infrastructure for over thirty years…deployed hundreds of wireless network solutions across many business sectors”
  > “expert design, implementation, and support of routing and switching infrastructure for over thirty years…deployed hundreds of wireless network solutions across many business sectors”
  > 来源：https://www.wiretechnologies.com/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：30 年 IT 基建全栈（布线+DC+交换直通）
- **产品线与在售品牌**：布线/DC/交换/无线/安防（CSV Allied 信号）
- **目标行业与场景**：企业/中小营商用
- **团队与规模**：中型
- **决策链与对接人**：info@wiretech-inc.com
- **技术与认证**：30 年交换 20 年无线
- **采购与供应链信号**：项目随单
- **近期动态与线索**：—
- **与我方契合点**：直接对口：接入层 value 位
- **风险与注意**：

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Wire Technologies 30 年布线/DC/交换直通：直接对口接入层 value 位（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：规模
- **O**：三线
- **T**：大牌

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
  - [ ] 接入现供
  - [ ] DC 边位
  - [ ] 滚动量

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Wire Technologies team,

Thirty years of routing and switching, hundreds of wireless deployments, structured cabling and data centers under one roof - you work exactly where we manufacture.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, Voice VLAN, watchdog) with full test documentation. Reference: $165 USD EXW - a value line for the access closets inside your cabling, DC and wireless projects.

One question: across your routing-and-switching projects, which brand holds the PoE access layer today?

If useful, I can send one unit with full documentation for your lab. If not a fit, one line and I close the loop.

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
