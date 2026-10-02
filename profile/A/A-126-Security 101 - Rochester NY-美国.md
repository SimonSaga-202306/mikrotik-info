# Security 101 - Rochester NY

> **评级 A**　|　美国 · Rochester, NY　|　档案编号 `A-126`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-126
rating: A
country: 美国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Security 101 Rochester：同集团判别具名 Victor 首邮（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

- **关联档警示**：A-125（同品牌不同分部（独立实体，可并行））→ 非重复，可并行开发；标注防误判

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Security 101 - Rochester NY（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Rochester, NY | 事实 |
| 网站 | https://www.security101.com/rochester | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Security 101 Rochester NY 分支：同 Security 101 集团体系（一线伙伴墙+Team101+101ware 门户）；**具名 victor.wainwright@security101.com**（CSV 公开列）
- 【推断】具名分支负责人=直接商务对话口；同集团判别与 A-125 一致（一线同盟→第二架窄位）
- 【假设】具名首邮定制（祝贺 SiteGuard/监控托管线）+分支弹性问题

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：victor.wainwright@security101.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：victor.wainwright@security101.com [Publicly listed; delivery not tested]; https://www.security101.com/rochester
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 工业级非管理 PoE（活动安保/拖车点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：顺 PGA 移动监控履历开场：活动/临时部署的宽温 DIN PoE 独立供电段——Owner 一点就懂的场景。
- **要问的问题**：PGA 那种移动部署，供电交换怎么做的？
- **随附证明**：宽温报告 + 拖车配套方案 + 报价（英文）。

### 第 2 次跟进 · 24 口 CCTV/PoE（学校/企业接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：Safe Learning 与企业项目：24 口 PoE++ 接入层成本对照。
- **要问的问题**：学校/企业项目的接入层现在用什么？
- **随附证明**：单端口测算 + 规格对照（英文）。

### 第 3 次跟进 · 管理型 PoE（校园/园区分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：校园安防网分段模板：VLAN/ERPS 标准化，他卖方案时随带。
- **要问的问题**：校园网分段有标准做法吗？模板发你。
- **随附证明**：VLAN/ERPS 模板 + 评估样机（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第7批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Security 101 罗切斯特网点：纽约上州商用安防+活动安保（PGA 履历），Owner 具名可直达，Allied 代理（CSV 记录）。⚠️ 与 A-125 同体系——Rochester 先行、CT 错峰。
- **产品线与在售品牌**：与体系同：门禁/监控/入侵/云安防/移动监控拖车/SiteGuard。
- **目标行业与场景**：罗切斯特企业园区、学校（Safe Learning 101）、医疗、活动赛事安保（PGA）。
- **团队与规模**：Owner 经营的加盟网点（Victor Wainwright，CSV 记录）。
- **决策链与对接人**：victor.wainwright@security101.com + rochester-service@security101.com（CSV 9-27 核验，具名职务未验证延续）。
- **技术与认证**：体系厂商矩阵；Allied 代理（CSV 记录）。
- **采购与供应链信号**：Owner 直决=响应快：小企业采购像老板买自己的东西——报价一步到位。
- **近期动态与线索**：PGA 移动监控案例可继续深挖聊天素材（2023 年）。
- **与我方契合点**：活动安保/临时点位的工业 PoE+学校/企业接入层。
- **风险与注意**：同体系别与 CT 互串信息；学校单（公立）注意条款，商业校优先；拖车线配套给联合方案思路。

### R54 原文证据摘录（全部保留）

- **【决策链与对接人】**CSV 9-27 记录：官网 2023 年 PGA 锦标赛移动监控安保新闻公开了 Owner/CEO Victor Wainwright 邮箱（职务延续未验证，另有当前网点服务邮箱）。
  > 官网 2023 年 PGA 项目新闻公开 Owner/CEO Victor Wainwright 邮箱；另有当前地方服务邮箱 rochester-service@security101.com。具名职位属历史披露，未验证任职延续（CSV 2026-09-27 记录）
  > 来源：https://www.security101.com/blog/security-101-helps-secure-the-pga-championship-with-mobile-surveillance
- **【业务定位】**品牌体系页（Rochester 站）：商用安防系统设计-安装-维护一网打尽，与康州网点同体系。
  > ROCHESTER NY Commercial Security Systems Company（页标题）· Design & Engineering · Installation, Inspection, & Maintenance · Advanced Security Integration（服务导航）
  > 来源：https://www.security101.com/rochester
- **【近期动态与线索】**PGA 锦标赛级移动监控履历（2023 新闻标题证据）+集团主推的移动监控拖车/SiteGuard 在他的工具箱里。
  > （页标题）Security 101 Helps Secure the PGA Championship with Mobile Surveillance · Mobile Surveillance Trailers · SiteGuard 101™ Proactive Video Monitoring
  > 来源：https://www.security101.com/rochester

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第13批.json`；价格均为 EXW 快照。

- **①背景再核**：Rochester 分支（集团体系）；具名 Victor
- **②芯片/型号**：Allied 信号（CSV）
- **③KP 深挖**：Victor Wainwright 具名
- **④Saga 对标**：分支第二架 value 线
- **⑤在乎与偏好**：集团目录

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Security 101 maintains long-standing strategic partnerships with the security industry’s leading manufacturers”
  > “Security 101 maintains long-standing strategic partnerships with the security industry’s leading manufacturers”
  > 来源：https://www.security101.com/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：Security 101 加盟分支（Rochester NY）
- **产品线与在售品牌**：一线伙伴墙（同集团；CSV 载 Allied 信号）
- **目标行业与场景**：十行业
- **团队与规模**：集团级分支
- **决策链与对接人**：Victor Wainwright 具名
- **技术与认证**：Team101
- **采购与供应链信号**：集团伙伴目录
- **近期动态与线索**：同集团
- **与我方契合点**：分支第二架价值线（窄判别）
- **风险与注意**：同盟强

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Security 101 Rochester：同集团判别具名 Victor 首邮（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：具名
- **W**：同盟
- **O**：弹性
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
  - [ ] 分支弹性
  - [ ] value 缺口
  - [ ] Victor 职责

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Victor,

Security 101's Rochester operation carries one of the strongest partner walls in the industry - Axis, Genetec, Avigilon, Verkada. We are not writing to displace any of it.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) at $165 USD EXW - for the projects where the first shelf prices itself out: budget-constrained schools, municipal buildings, value-engineered retrofits.

One question: at your branch, is there room for a second approved value line when a project cannot carry the standard brands?

If useful, I can send one unit with full documentation. If not relevant, one line and I close the loop.

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

- **KP 领英直达**:[Victor Wainwright · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Victor%20Wainwright%20Security%20101%20-%20Rochester%20NY)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 高(Covered List+SECURE Act+§301 关税;采购方警惕中国标签,话术锚 Marvell(美企)+FCC);战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
