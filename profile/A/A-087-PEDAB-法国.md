# PEDAB

> **评级 A**　|　法国 · Paris　|　档案编号 `A-087`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-087
rating: A
country: 法国
biz_org: 个体顾问（无官网）
business_model: 顾问项目制
decision_speed: fast
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；顾问项目制
- **商业模式**：顾问项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — PEDAB 法国大集团分销：工业 PoE value 档并架（$74.8 锚点一致）；准入文件严谨；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | PEDAB（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 / Paris | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 分销/集成商（Perle 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网） | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：commercial@pedab.fr
  - 状态：既有/公开
- **电话**：—
- **原始联系字段**：commercial@pedab.fr（具名：Christine Berthon（法国区总经理）christine.berthon@pedab.fr；Thibaut Perié（网络销售）thibaut.perie@pedab.fr）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 品类空缺（接入层+工业 PoE 类目提案）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行） / STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：以「新类目上架」提案开场：Nokia 大型机旁的接入层与 Perle 旁的工业 PoE 价位空档，附完整供应商材料包。
- **要问的问题**：贵司新品牌/类目上架的评估流程怎么走？
- **随附证明**：公司一页介绍+合规包+类目建议书（英/法）。

### 第 2 次跟进 · 工业非管理 PoE（法国区试点 SKU）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：大 VAD 先试点：法国区 2–3 个 SKU 试销 90 天，动销数据说话再谈北欧大区。
- **要问的问题**：法国区愿意先试哪两个 SKU？试点 KPI 怎么定？
- **随附证明**：试点方案+起订价+营销物料包。

### 第 3 次跟进 · 管理型 10G（企业接入层类目扩展+渠道政策）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：类目扩展第二步：管理型接入层+渠道培训（他 partner enablement 模式），配项目注册与价格保护。
- **要问的问题**：项目注册与价格保护的条款按贵司模板来拟？
- **随附证明**：渠道政策包+培训计划+ERPS/L3 实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第5批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：欧洲八国（北欧+波罗的海+法国）基础设施与安全 VAD：IBM/Inspur/ASUS 服务器、Nokia IP/光网络、Perle 工业联网（CSV 记录）——体量远大于同类户。
- **产品线与在售品牌**：企业级基础设施（服务器/存储/云市场）+ Nokia 运营商网络 + 安全软件栈 + Perle 边缘联网。
- **目标行业与场景**：政府、大学、制造、医疗的数字化与网络改造项目；渠道二次分销（他不下场做项目）。
- **团队与规模**：Pedab Group 集团化运作（CEO Jesper Bartholdson），法国区总经理 Christine Berthon、网络销售 Thibaut Perié（CSV 记录）。
- **决策链与对接人**：commercial@pedab.fr；具名：christine.berthon@pedab.fr / thibaut.perie@pedab.fr（CSV 记录）。
- **技术与认证**：IBM/Nokia 官方分销资质；Perle 授权（CSV 记录）。
- **采购与供应链信号**：VAD 上架逻辑：完整产品线+认证培训+物流金融配套后才谈；周期长但一单覆盖多国。
- **近期动态与线索**：密集新签（ASUS 服务器、Nokia IP、AWS 市场首发）——产品线扩张期，货架在加类目。
- **与我方契合点**：Nokia/Perle 旁的「企业接入层+工业 PoE」价位空档：以新类目上架评估流程进他的供应商漏斗，先拿法国区试点。
- **风险与注意**：大 VAD 流程重（供应商审核/合规/业绩承诺）：材料一次备齐（合规、质保、渠道政策），别催单；以 Christine 线为准。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网口号：「生态 orchestrator + 可信赖分销商」——北欧起家的欧洲 VAD。
  > Pedab orchestrateur d’écosystème et distributeur de confiance.
  > 来源：https://www.pedab.fr/
- **【团队与规模】**IBM 伙伴名录：瑞典起家 30+ 年的 IBM 增值分销/Techbroker，法国公司在巴黎圣日耳曼大道 280 号。
  > Pedab is a dedicated IBM Value Add Distributor and Techbroker… From the local start in Sweden over 30 years ago, to their European presence today… 280 Boulevard Saint-Germain, Paris 75007
  > 来源：https://www.ibm.com/partnerplus/directory/company/4191
- **【近期动态与线索】**官方新闻室：Nokia 选定 Pedab 为其 IP 与光网解决方案的增值分销，面向政府/大学/制造/医疗——运营商级产品线在手。
  > Nokia has selected Pedab, as a value-added distributor for its IP… Nokia IP and Optical solutions… government, universities, manufacturing and healthcare industries.
  > 来源：https://www.pedab.com/about-pedab/newsroom/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第9批.json`；价格均为 EXW 快照。

- **①背景再核**：Pedab 集团法国区大 VAD；Perle 线在册
- **②芯片/型号**：Perle
- **③KP 深挖**：Berthon GM 具名
- **④Saga 对标**：value 档工业 PoE 并架
- **⑤在乎与偏好**：准入文档+集团流程

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Pedab orchestrateur d’écosystème et distributeur de confiance”
  > “Pedab orchestrateur d’écosystème et distributeur de confiance”
  > 来源：https://www.pedab.fr/
- **【联系方式】**commercial@pedab.fr；Christine Berthon 法国区总经理（CSV）；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > commercial@pedab.fr；Christine Berthon 法国区总经理（CSV）；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://www.pedab.fr/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | PEDAB 法国大集团分销：工业 PoE value 档并架（$74.8 锚点一致）；准入文件严谨 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：覆盖
- **W**：长准入
- **O**：并架
- **T**：正面

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
  - [ ] 法国区独立采力度
  - [ ] 准入清单
  - [ ] 阶梯

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Christine,

Pedab’s ecosystem-orchestrator role in France makes you the natural stop for a new industrial PoE line at a value price point.

We build industrial managed PoE switches rated -40 to 75C with watchdog and full documentation packs - next to, not against, the industrial lines you carry. Reference: $74.8 USD EXW.

One question: within your French catalog, is there an open slot for a value industrial PoE switch line?

If useful, I can send the full onboarding documentation pack and a unit. If not a fit, one line and I close the loop.

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
