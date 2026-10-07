# System Devices UK Ltd

> **评级 A**　|　英国　|　档案编号 `A-057`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-057
rating: A
country: 英国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — System Devices 独代分销（Opto22/Epson 等）：Antaira 旁柜内温宽 PoE 独代候选（$74.8 锚点一致）；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | System Devices UK Ltd（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 | 事实 |
| 网站 | systemdevices.co.uk | 事实 |
| 类型 | 分销（Antaira 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Antaira | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】System Devices UK Ltd（1983 创立）：UK/爱尔兰工控自动化分销——独家英国总代 Opto 22、Epson Robots、Asyril 柔性上料、Mecademic 精密机器人+Weintek HMI；ISO 9001:2015；行业覆盖含废水/农业/运输/制药/汽车/油气/制造；客户口碑（Harwin/油气/制药代表）突出
- 【推断】CSV 信号 Antaira=其工业以太网线；自动化机柜生态（Opto22 groov/Epson 机械臂）的网络接入层=PoE 供视觉/传感尾头的配位
- 【假设】其“独家总代”喜好=喜欢做差异化代理；温宽 PoE 作为其独家位候选有戏

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Antaira）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@systemdevices.co.uk
  - 状态：既有/公开
- **电话**：+44 1928 571 977
- **原始联系字段**：+44 1928 571 977 / info@systemdevices.co.uk
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 PoE++（安防/视觉项目配套）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：机器人+视觉项目里的摄像/传感供电：24 口 PoE++ 先送少量测试机，让他在真实项目里验证。
- **要问的问题**：机器类项目的 PoE 供电现在接什么设备？
- **随附证明**：英文规格对照页 + 功率实测。

### 第 2 次跟进 · 工业非管理 PoE（车场/轨交/污水柜外）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他的轨道/污水/油气场景里柜外点位：宽温宽压、DIN、免配置——在他自动化总包里留座。
- **要问的问题**：柜外点位现在什么来源、冬夏重更换吗？
- **随附证明**：宽温报告 + DIN 安装图 + 台测试机寄 Runcorn。

### 第 3 次跟进 · 管理型

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：管理型进他的总包方案：VLAN 分段+ERPS 环网——随 ISO 流程交付完整文档包。
- **要问的问题**：他们的 ISO 流程对供应商资质/范围（scope）有什么要求？
- **随附证明**：ERPS 收敛实测 + spec 文件包 + 两年供货承诺。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：英国 Runcorn 43 年工业自动化与技术专家：核心是做机器人/工控屏/活喂料系统等总包技术分销。
- **产品线与在售品牌**：Opto 22/Epson/Asyril/Mecademic/Weintek——网络设备侧以 Opto 22 control network 为核心。
- **目标行业与场景**：工厂机器车场、轨道交通、污水、油气——DIN 类与宽温点位多。
- **团队与规模**：40 年经验工程师型队，售前支持正规（ISO 9001:2015）。
- **决策链与对接人**：info@systemdevices.co.uk / +44 1928 571 977。
- **技术与认证**：ISO 9001:2015 认证，工程法语境系统。
- **采购与供应链信号**：规范分销：要 ISO 的物料/厂商范围——他会问我们常供材料与质量控制证书。
- **近期动态与线索**：机器视觉+机器人赛道火——配套的网络硬件（Poe 摄像头供电、现场点对点）他会在案外找。
- **与我方契合点**：车用/工控/机器视觉点位=我们的工业 PoE+管理型是“配套补充”；Opto 22 核心工控柜外，我们能做网络段。
- **风险与注意**：不是主流网络店——首轮拿准“柜外二层”位置，不猛推主流供应商完全替代。

### R54 原文证据摘录（全部保留）

- **【业务定位】**1983 年起的工业自动化与控制系统专家——英国 Automation Industrial 段的专业分销/集成。
  > Ahead of the Technology Curve since 1983 — System Devices UK is a trusted authority in the field.
  > 来源：https://systemdevices.co.uk/
- **【产品线与在售品牌】**代理 Opto 22、Epson Robots、Asyril、Mecademic 与 Weintek——多家为英国独家分销商段位。
  > exclusive UK distributors of Opto 22, Epson Robotics, Asyril Flexible Feeding Systems and Mecademic Industrial Robotics, and leading distributor of Weintek HMIs.
  > 来源：https://systemdevices.co.uk/
- **【技术与认证】**ISO 9001:2015 认证的质量管理体系——售前/售后均有体系化流程。
  > Back by comprehensive technical support and training, everything we deliver is rooted in quality — evidenced by our ISO 9001:2015-accredited Quality Management System.
  > 来源：https://systemdevices.co.uk/
- **【目标行业与场景】**客户行业表包括污水处理/研发/农业/交通/制药/汽车/制造/油气——全是工控现场点位。
  > Waste Water Management · Research & Development · Agriculture · Transportation · Pharmaceutical · Automotive · Oil and Gas
  > 来源：https://systemdevices.co.uk/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第6批.json`；价格均为 EXW 快照。

- **①背景再核**：1983 独代分销四件（Opto22/Epson/Asyril/Mecademic）；Antaira 线在册
- **②芯片/型号**：Antaira 工业以太网
- **③KP 深挖**：info@ 口；电话并行
- **④Saga 对标**：温宽 PoE 独代候选（避对标）
- **⑤在乎与偏好**：独代差异化+ISO 文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“exclusive UK distributors of Opto 22, Epson Robotics, Asyril, Mecademic…ISO 9001:2015…Ahead of the Technology Curve since 1983”
  > “exclusive UK distributors of Opto 22, Epson Robotics, Asyril, Mecademic…ISO 9001:2015…Ahead of the Technology Curve since 1983”
  > 来源：https://systemdevices.co.uk/
- **【联系方式】**info@systemdevices.co.uk +44 1928 571 977；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > info@systemdevices.co.uk +44 1928 571 977；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://systemdevices.co.uk/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：UK 工控自动化独代分销（1983）：Opto22/Epson/Asyril/Mecademic
- **产品线与在售品牌**：独代四件+Weintek+Antaira（CSV）
- **目标行业与场景**：制造/制药/农业/汽车（废水占比公共）
- **团队与规模**：中型独代分销
- **决策链与对接人**：info@ 口
- **技术与认证**：ISO 9001:2015
- **采购与供应链信号**：独代制采购入库
- **近期动态与线索**：2024-25 换 Logo 墙+新增 Opto22/Mecademic 独代
- **与我方契合点**：Antaira 旁温宽 PoE 独代候选
- **风险与注意**：公共段（废水/交通）守边界

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | System Devices 独代分销（Opto22/Epson 等）：Antaira 旁柜内温宽 PoE 独代候选（$74.8 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424XGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：独代偏好
- **W**：非主流
- **O**：柜配位
- **T**：在位盘

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
  - [ ] Antaira 盘规模
  - [ ] 独代可行性
  - [ ] 柜内现供

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi System Devices team,

Exclusive distribution done right since 1983 - Opto 22, Epson, Asyril, Mecademic, and ISO 9001 behind it.

We build industrial managed PoE switches rated -40 to 75C, aimed as an exclusive-candidate industrial Ethernet line next to your current connectivity portfolio. Reference: $74.8 USD EXW.

One question: within your automation cabinets, who supplies the Ethernet switching layer today?

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
