# VARtek Services Inc

> **评级 A**　|　美国　|　档案编号 `A-129`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-129
rating: A
country: 美国
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
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — VARtek K-12 教育专属驻场托管：学区接入柜免回访（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | VARtek Services Inc（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 | 事实 |
| 网站 | https://vartek.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】VARtek Services（俄亥俄西南，vartek.com）：**教育专属 IT 伙伴**——K-12 学区 IT 托管（驻场技术团队）+整合支持+网络安全教育资源（10 步网络犯罪防御计划等）；“strategic partner to schools…save school leaders time”
- 【推断】教育专属=学区预算审批常规商用段；驻场托管结构=硬件随单+refresh 滚动；服务商为主但硬件线存在（integration support）
- 【假设】“save leaders time”使命=可靠免回访件话术（看门狗）适配

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@vartek.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：company-social（R41–R48 联系方式台账口径）
- **原始联系字段**：info@vartek.com [Publicly listed; delivery not tested]; https://vartek.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（私立/特许学校接入层，E-rate 划线）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：开局讲边界：仅供私立/特许与商业条款段；24 口 PoE++ 按教育预算给，规格对照+合规声明。
- **要问的问题**：私立/特许客户的接入层用什么？（附 E-rate 边界说明）
- **随附证明**：边界声明 + 教育预算价 + 规格对照（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（校园室外/体育馆）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：操场/体育馆/校车场点位：宽温 DIN PoE 暑假安装窗口批量装。
- **要问的问题**：暑期改造清单里室外点位做了吗？
- **随附证明**：宽温报告 + 暑期安装计划模板 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（校园网分段模板）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：学区网分段样板（教学/访客/IoT/安防四段）：VLAN/ERPS 模板给他的驻校工程师团队。
- **要问的问题**：驻校工程师要不要一套四段 VLAN 模板？
- **随附证明**：VLAN/ERPS 模板 + 工程师速查 + 评估样机（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第7批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：代顿 K-12 专属 MSP：「驻校 IT 人员+愿景规划」模式，西南俄亥俄学区客户盘，Allied 代理（CSV 记录）。
- **产品线与在售品牌**：IT 托管（驻校人员）/技术规划集成/网络安全教育与响应方案。
- **目标行业与场景**：K-12 学区（公立为主）——校园网/教室设备/1:1 终端配套。
- **团队与规模**：教育技术专职团队（ Dayton 总部）。
- **决策链与对接人**：info@vartek.com（CSV 9-27 核验：Facebook 与 Crunchbase 一致）。
- **技术与认证**：Allied 代理（CSV 记录）。
- **采购与供应链信号**：⚠️ 公立学区资金走 E-rate/州共购——合规约束段（E-rate 合格的供应商名录与产地要求）划线；私立/特许学校与学区行政网商业条款内可谈。
- **近期动态与线索**：网安教育内容密集投放=在签学区网安服务单。
- **与我方契合点**：私立/特许学校与学区非 E-rate 商业段的接入层与课堂 PoE 设备；驻校模式=他要稳定易维护的标准件。
- **风险与注意**：公立段（E-rate）不硬闯：先讲清可做商业段范围，别让一单不合规毁关系；报价按教育行业预算节奏（暑假改造季）。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网页标题：「Education’s IT Partner」——专门做学校的战略技术伙伴。
  > Vartek | Education’s IT Partner · IT Built on Your Vision — Vartek is a strategic partner to schools, delivering tailored, innovative technology and integration support so that educators are empowered to create the learning environment they envision.
  > 来源：https://vartek.com/
- **【产品线与在售品牌】**IT 托管服务=派驻校的技术专业团队（on-site staffing）+课堂技术支持——「驻校 IT 部」模式。
  > IT Managed Services — Comprehensive, innovative technology plans, staffing your school with a team of on-site technology professionals and helping teachers create engaging classrooms.
  > 来源：https://vartek.com/
- **【目标行业与场景】**证言点名西南俄亥俄学区（助理督学）——K-12 学区客户盘。
  > “When working with Vartek, I always sense and feel this deep level of commitment to our success…” — Assistant Superintendent, Southwest Ohio
  > 来源：https://vartek.com/
- **【近期动态与线索】**博客主线=校园网络安全教育（勒索软件防御 10 步、教职员工安全意识培训）——网安服务在加码。
  > Educate on Cybersecurity and Protect Your Students · Vartek’s 10 Step Cybercrime Defense Plan · School Sectors Targets for Ransomware · Threat Detection and Response（博客标题串）
  > 来源：https://vartek.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第13批.json`；价格均为 EXW 快照。

- **①背景再核**：K-12 教育专属托管（驻场）；服务为主硬件为辅
- **②芯片/型号**：CSV 载 Allied 信号
- **③KP 深挖**：info@
- **④Saga 对标**：学区接入柜 value 件
- **⑤在乎与偏好**：免回访+预算

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“strategic partner to schools, delivering tailored, innovative technology and integration support so that educators are empowered…staffing your school with a team of on-site technology professionals”
  > “strategic partner to schools, delivering tailored, innovative technology and integration support so that educators are empowered…staffing your school with a team of on-site technology professionals”
  > 来源：https://vartek.com/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：K-12 教育专属 IT 托管（驻场模式）
- **产品线与在售品牌**：托管+整合（CSV 载 Allied 信号）
- **目标行业与场景**：K-12 学区
- **团队与规模**：区域中型
- **决策链与对接人**：info@ 口
- **技术与认证**：教育资源内容
- **采购与供应链信号**：随单+refresh
- **近期动态与线索**：网络安全教育资源化
- **与我方契合点**：学区接入柜 value 件
- **风险与注意**：服务主硬件辅

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | VARtek K-12 教育专属驻场托管：学区接入柜免回访（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：专精
- **W**：服务主
- **O**：接入
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
  - [ ] 预算周期
  - [ ] refresh 节奏

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Vartek team,

Staffing schools with on-site technology professionals is a promise built on reliability - and nothing tests reliability like an access switch that freezes during class.

We build a 24-port Gigabit PoE switch (280W, 802.3af/at, Voice VLAN, hardware watchdog that restarts frozen endpoints automatically). Reference: $180 USD EXW - a district-friendly price with the full documentation pack.

One question: in your K-12 deployments, which switch brand fills the PoE access layer for classroom Wi-Fi and cameras today?

If useful, I can send one unit with full documentation for evaluation. If not a fit, one line and I close the loop.

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

---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:[VARtek Services Inc · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=VARtek%20Services%20Inc)(无具名 KP 信号,先搜公司再加人;待查)
- **中国进口与管制**:国别档位 高(Covered List+SECURE Act+§301 关税;采购方警惕中国标签,话术锚 Marvell(美企)+FCC);战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
