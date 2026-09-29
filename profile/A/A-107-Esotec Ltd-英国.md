# Esotec Ltd

> **评级 A**　|　英国 · Didcot　|　档案编号 `A-107`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-107
rating: A
country: 英国
biz_org: 个体顾问（无官网）
business_model: 顾问项目制
decision_speed: fast
price_sensitivity: high
volume_potential: 1  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: true, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；顾问项目制
- **商业模式**：顾问项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Esotec 安审安防（CCS 红线主干）：只谈非安审私营窄段+承认边界（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Esotec Ltd（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Didcot | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |
| ⚠️ 信息缺口 | 本条**抓不到邮箱**，需人工补齐邮箱或改为电话单独跟进后再进群发名单 | 事实 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Esotec Ltd（英国）：高监管安防集成商——**secure government/national heritage/public spaces** 全生命周期安防（测试/设计/安装/支持）；**30+ 安审级别员工（Security Cleared）**；NSI Gold+ISO 14001/27001/45001+**Crown Commercial Service 供应商**；客户墙：London Transport Authority（公共）/大型赛事组织/历史建筑信托/World-leading 安全印务/高净值人士/工程企业
- 【推断】公共+安审主干=红线区；私营窄段（安全印务/高净值/工程企业/部分赛事）为高规格但合规可触的位
- 【假设】安审级操作=文档与来源核验异常敏感——外资设备在 secure government 场景不现实，承认并只谈非安审私营段

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

- **邮箱**：sales@esotec.co.uk
  - 状态：既有/公开
- **电话**：—
- **原始联系字段**：sales@esotec.co.uk（另有 info@ / support@ / finance@esotec.co.uk。**高端监控/安防集成**，政府、国家遗产、公共空间项目 → PoE 供电场景强对口）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（私营商业项目接入层，合规划线）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：明确「仅供私营商业/高净值段」开局+合规声明，再递 24 口接入层成本测算——他的商业小项目池常年有货。
- **要问的问题**：私营商业项目的接入层用什么？（附适用边界声明与合规包）
- **随附证明**：适用边界声明 + 合规文件包 + 单端口测算（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（周界/室外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：周界与庭院摄像头（庄园/厂房）：宽温 DIN PoE 减少冬季上门——高净值项目的维护成本他最敏感。
- **要问的问题**：室外周界点位的坏机率与上门成本现在多少？
- **随附证明**：宽温报告 + 坏机测算 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（商业段安防网段模板）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：商业段标准件：VLAN 隔离+ERPS 冗余模板，配全套 MIB/文档给他的设计团队。
- **要问的问题**：商业段的安防网段设计有模板吗？
- **随附证明**：VLAN/ERPS 模板 + 设计文档包 + 收敛实测（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第6批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Didcot 高端安防集成商：涉密政府/国家遗产/公共交通局/高净值的交钥匙监控与周界， Allied 代理（CSV 记录）。
- **产品线与在售品牌**：设计咨询→安装→维护的视频监控/周界/入侵一体化；自有技术+「best-of-breed」品牌组合。
- **目标行业与场景**：伦敦交通局（客户墙）、大型赛事主办方、历史建筑信托、安全印务、高净值个人——敏感场景为主。
- **团队与规模**：50 人级精专公司，30+ 员工持安全审查（SC 级别）资质——人员含金量=投标票价。
- **决策链与对接人**：sales@esotec.co.uk（另有 info@ / support@ / finance@，CSV 9-27 记录）。
- **技术与认证**：NSI Gold+CE Plus+三 ISO+CCS 供应商；Allied 代理（CSV 记录）。
- **采购与供应链信号**：⚠️ 涉密政府与 CCS 框架项目对供应链产地审查敏感——公共段划线；商业/高净值/私营遗产基金会段可谈。
- **近期动态与线索**：网站为 Wix 静态站（在线客服组件失效可见）——业务靠存量口碑运转。
- **与我方契合点**：商业/私营段的视频监控接入层与室外周界工业件；高合规文件包前置。
- **风险与注意**：其客户类型（政府/遗产/交通）决定大多数项目不能装中国产设备：首封即划边界（仅供私营商业段），反而赢得专业信任。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网抬头：全生命周期安防方案的可信系统集成商。
  > Trusted Systems Integrator for full-lifecycle Security Solutions
  > 来源：https://www.esotec.co.uk/
- **【目标行业与场景】**⚠️ 交付场景：安全涉密政府、国家遗产、公共空间等高曝光场所——公共/敏感段为主。
  > …we are able to deliver turn-key solutions into secure government, national heritage, public spaces and other high-profile locations.
  > 来源：https://www.esotec.co.uk/
- **【团队与规模】**数字：每天 3.5 万+ 名员工由其系统守护、团队组合经验 500+ 年、30+ 名持安全审查资质员工、5000+ 项目。
  > 35,000+ Employees made safe, daily · 500+ Years of team experience · 30+ Security Cleared staff · 5000+ Completed Projects
  > 来源：https://www.esotec.co.uk/
- **【技术与认证】**认证墙：FORS/SSIP/NSI Gold/Cyber Essentials Plus/ISO14001/27001/45001，且是 Crown Commercial Service 供应商名册企业。
  > FORS · Safety Schemes in Procurement (SSIP) · NSI Gold Accreditation · Cyber Essentials Certified Plus · ISO14001 · ISO27001 · ISO45001 · Crown Commercial Service Supplier（认证墙 Logo）
  > 来源：https://www.esotec.co.uk/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第11批.json`；价格均为 EXW 快照。

- **①背景再核**：高监管安防（安审主干红线）；CCS 供应商
- **②芯片/型号**：未公开
- **③KP 深挖**：sales@
- **④Saga 对标**：非安审窄段 value PoE（承认安审不进）
- **⑤在乎与偏好**：规格+来源核验

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“secure government, national heritage, public spaces…30+ security cleared staff…Crown Commercial Service Supplier”
  > “secure government, national heritage, public spaces…30+ security cleared staff…Crown Commercial Service Supplier”
  > 来源：https://www.esotec.co.uk/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：英国高监管安防集成（安审主干 红线）+私营窄段
- **产品线与在售品牌**：安防全生命周期
- **目标行业与场景**：安审政府（红线）+安全印务/高净值/工程（窄段）
- **团队与规模**：大型安防集成
- **决策链与对接人**：sales@ 口
- **技术与认证**：NSI Gold+三 ISO+安审员工
- **采购与供应链信号**：高规格项目
- **近期动态与线索**：CCS 供应商在册
- **与我方契合点**：非安审私营窄段 value PoE
- **风险与注意**：安审/公共红线

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Esotec 安审安防（CCS 红线主干）：只谈非安审私营窄段+承认边界（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：规格
- **W**：红线
- **O**：窄段
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
  - [ ] 非安审占比
  - [ ] 接入现供
  - [ ] 评测窗

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Esotec team,

Your security-cleared projects demand equipment provenance we respect completely - this note explicitly does not touch those engagements in any way.

For your private commercial customers (secure printers, engineering firms, private estates), we build a 24-port Gigabit PoE switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW.

One question: in your non-cleared private projects, who supplies the PoE camera closet layer today?

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
