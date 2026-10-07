# NXO France

> **评级 A**　|　法国 · Rueil-Malmaison　|　档案编号 `A-330`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-330
rating: A
country: 法国
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
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — NXO 法超大集成/运营商（SOC aaS+Linkernet 运营+总部迁 Puteaux；CSV: AT Integrate Elite）：商业客户长尾窄针（$180 锚点一致）；公共段守界句；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | NXO France（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 / Rueil-Malmaison | 事实 |
| 网站 | https://www.nxo.eu | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】NXO（法国，总部 2026-03 迁 Puteaux）：大盘'集成商+运营商'——Infrastructures digitales（LAN/WiFi/SD-WAN/DC)+UCaaS/通信+Cybersécurité（含 SOC aaS)+Cloud&Opérateur（Linkernet/Linkerconnect 电信运营）+Academy；客户案例含 Ville de Villefranche（公共）;CSV=**Allied Telesis Integrate Elite+Resell**
- 【推断】法国超大一体集成/运营：value 只在其商业客户长尾的私段窄口；公共案例=守界句；大盘低密窄针
- 【假设】商业客户长尾的 value 二轨窄针

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：contact@nxo.eu
  - 状态：既有/公开
- **电话**：0 821 201 201、2026-03-30
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：contact@nxo.eu（官网联系/法律页）；0 821 201 201；总部2026-03-30迁Puteaux（法律页仍Rueil-Malmaison）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 供应商登记+价位档一页

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：法语一封：申请入供应商名册；随附 24 口 PoE 价位档第二来源资料（声明不涉市政/公共项目）。
- **要问的问题**：（电话并行）供应商登记对接口与流程？
- **随附证明**：一页提案+RMA/供货连续性说明。

### 第 2 次跟进 · 组网伴生配件

- **推什么**：SFP/收发器 目录
- **切入点**：其组网项目伴生的光配件窄线。
- **要问的问题**：项目伴生配件有补位需求吗？
- **随附证明**：配件一页价卡。

### 第 3 次跟进 · 无入口即冻结

- **推什么**：—
- **切入点**：集团册无入口/无回响即冻结。
- **要问的问题**：—
- **随附证明**：—。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第17批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：法国头部集成运营集团（Allied Elite 级；**大集团规矩：供应商登记先行、市政公共面划出、不越级**）。
- **产品线与在售品牌**：基建/协作/安全/运营/服务五大板；Allied Integrate Elite+Resell（CSV）。
- **目标行业与场景**：大型企业/工业客户（商业面）；市政公共面不涉。
- **团队与规模**：大型集团（多子公司 NXO Experts/Telecom/Océan Indien）。
- **决策链与对接人**：contact@nxo.eu（联系页，CSV 9-27）+电话同用。
- **技术与认证**：Allied Integrate Elite/Resell（CSV 9-23）。
- **采购与供应链信号**：**其 LAN 集成业务的接入层第二来源在册供应商**位：价位档 24 口 PoE——量大时靠集团册，点状靠 BU。
- **近期动态与线索**：总部乔迁+品牌持续投放=供应商名册刷新窗口。
- **与我方契合点**：供应商在册+24 口价位档。
- **风险与注意**：不代替 Allied 位；市政/公共工程项目一概不经由我们。

### R54 原文证据摘录（全部保留）

- **【业务定位】**法国头部 IT 集成与运营集团：数字基建（NetDevOps/LAN/WLAN/WAN/SD-WAN/DC）+通讯协作+网络安全（SOC）+**云与运营（Linkernet 互联网接入/Linkerconnect 运营 WAN/Linkersip SIP 中继）**+MCO 维保/培训五大板，总部 2026-03 迁 La Défense/Puteaux。
  > Intégrateur et opérateur IT, réseaux, télécoms, sécurité ‖ Linkernet — accès internet haut débit · Linkerconnect — wan opéré · Linkersip — accès télécom — trunk sip ‖ NXO installe son siège social à La Défense
  > 来源：https://www.nxo.eu/
- **【目标行业与场景】**客户墙含市政机构项目（La Ville de Villefranche 文化场所数字化=**市政公共面划出**）；商业与工业 4.0 内容线（podcast IT-OT 融合）=商业可做面。
  > La Ville de Villefranche digitalise un lieu culturel avec NXO — guichet unique… services publics（市政公共面划出）‖ Industrie 4.0 : convergence IT-OT（podcast）
  > 来源：https://www.nxo.eu/
- **【决策链与对接人】**contact@nxo.eu 官网联系/法律页+0 821 201 201（CSV 9-27 official-company）；**大集团采购走供应商登记流程**——第一步先按指引登记+电话，不越级直闯各 BU。
  > （CSV 2026-09-27 记录）官网联系/法律页给 contact@nxo.eu、0 821 201 201；总部自 2026-03-30 迁至 1-7 Cours de Valmy, 92800 Puteaux；official-company
  > 来源：https://www.nxo.eu/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第33批.json`；价格均为 EXW 快照。

- **①背景再核**：FR 超大集成/运营（官网+CSV 双核）
- **②芯片/型号**：AT Elite
- **③KP 深挖**：contact@
- **④Saga 对标**：窄针低密（$180 锚点一致）
- **⑤在乎与偏好**：大盘框架/合规

### R55 证据摘录（全部保留 · 含数量）

- **【近期动态】**NXO installe son siège social à La Défense（Puteaux 2026-03）;案例: La Ville de Villefranche（公共标注）；CSV: AT Integrate Elite
  > NXO installe son siège social à La Défense（Puteaux 2026-03）;案例: La Ville de Villefranche（公共标注）；CSV: AT Integrate Elite
  > 来源：https://www.nxo.eu

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：法国超大集成/运营商
- **产品线与在售品牌**：AT Integrate Elite（CSV）
- **目标行业与场景**：大型商业/公共（守界注）
- **团队与规模**：千人级组织
- **决策链与对接人**：contact@ 口
- **技术与认证**：—
- **采购与供应链信号**：框架+项目随单
- **近期动态与线索**：总部迁 Puteaux 2026-03
- **与我方契合点**：商业长尾窄针（公共守界句）
- **风险与注意**：大盘集中——低密窄位

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | NXO 法超大集成/运营商（SOC aaS+Linkernet 运营+总部迁 Puteaux；CSV: AT Integrate Elite）：商业客户长尾窄针（$180 锚点一致）；公共段守界句 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：体量
- **W**：集中
- **O**：窄
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
  - [ ] 替补机制
  - [ ] 责权

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Bonjour NXO team,

Integrator and operator at national scale - digital infrastructures, communications, cybersecurity, operator services. One boundary sentence: your public-sector engagements stay on their established paths; this is a commercial-side question.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW (2026-09-29) - a value tier for commercial projects in the long tail where budgets close deals.

One question: on the commercial side, does a documented value PoE tier exist - and who owns the networking catalogue?

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
