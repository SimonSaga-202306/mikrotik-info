# BlueBearsIT

> **评级 A**　|　法国 · Limonest　|　档案编号 `A-307`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-307
rating: A
country: 法国
biz_org: 公司/工作室（有官网）
business_model: 培训交付
decision_speed: moderate
price_sensitivity: medium
volume_potential: 2  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: true}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — BlueBearsIT 法里昂 MSP TPE/PME（infogérance 三地+Qualiopi 培训注）：托管现场随单（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | BlueBearsIT（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 / Limonest | 事实 |
| 网站 | https://bluebearsit.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】BlueBearsIT（法国 Lyon/Grenoble/Annecy）：TPE/PME 外包 IT（infogérance N1-N3）+系统集成+BI;品牌墙 Veeam/VMware/Dell/Sophos/OVHcloud/Barracuda;CSV=Allied Telesis Resell 伙伴+Qualiopi 培训资质注
- 【推断】法国中型 MSP：私营 TPE/PME 托管现场交换件随单真实；AT Resell 粘性低——value 窄位好靶
- 【假设】TPE/PME 托管现场的 value PoE 随单

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：ec@bluebearsit.com
  - 状态：既有/公开
- **电话**：04 28 29 86 50
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：ec@bluebearsit.com（官网培训页“service Commercial”信箱；第三方名录另给contact@/cg@bluebearsit.com）；04 28 29 86 50
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · SMB 项目接入层第二来源一页

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：法语一封到 ec@：TPE/PME 项目的 24 口 PoE 接入层第二来源（VLAN 预设即用+RMA+小批梯价）。
- **要问的问题**：集成项目的接入层目前有第二来源位吗？
- **随附证明**：一页报价（法）+ VLAN 预设。

### 第 2 次跟进 · 迁移案 DC 配件零位

- **推什么**：DAC/SFP 目录
- **切入点**：OVH/机房迁移案的互连配件小批。
- **要问的问题**：迁移案的互连配件走按需还是常备？
- **随附证明**：配件一页价卡。

### 第 3 次跟进 · 价卡留档收口

- **推什么**：—（价卡留档）
- **切入点**：全品类价卡留档；无回复即冻结。
- **要问的问题**：（无需回）价卡留档。
- **随附证明**：全品类一页价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第16批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：里昂三地 SMB 全包商（Allied Resell）——客户网项目接入层第二来源+备件。
- **产品线与在售品牌**：infogérance/集成/项目管理/BI；Veeam/Sophos/OVHcloud 生态。
- **目标行业与场景**：罗讷-阿尔卑斯 TPE/PME（含会计所等案例）。
- **团队与规模**：中小三地群（团队页专家制）。
- **决策链与对接人**：ec@bluebearsit.com（培训页商务箱，CSV 9-27）；04 28 29 86 50。
- **技术与认证**：Allied Resell（CSV）+Qualiopi 培训资质。
- **采购与供应链信号**：SMB 项目的接入/无线/PoE 第二来源；OVH 迁移案的机房侧 DAC/SFP 零位。
- **近期动态与线索**：墨西哥远程交付案例=跨境项目能力自证，接得住英文资料。
- **与我方契合点**：24 口 PoE 接入层第二来源+迁移案 DC 配件零位。
- **风险与注意**：Qualiopi 培训渠道（公共补贴资格面）不经由我们；Allied Resell 锚位轻、不替位。

### R54 原文证据摘录（全部保留）

- **【业务定位】**里昂/格勒诺布尔/安纳西三地的 TPE/PME 全包 IT 商：infogérance N1/N2/N3+系统集成迁移+功能项目管理+BI 四线。
  > BlueBearsIT, l’entreprise informatique à Lyon qui challenge votre Système d'information ‖ Infogérance · Intégration Systèmes & Réseaux · Gestion de projet fonctionnel · Business Intelligence ‖ Présent sur 3 sites : Lyon / Grenoble / Annecy
  > 来源：https://bluebearsit.com/
- **【产品线与在售品牌】**生态墙：Veeam/VMware/Barracuda/OVHcloud/Dell/Power BI/Sophos/PRTG/Azure/M365——云迁移案例走 OVHcloud。
  > （生态墙）Veeam · VMware · Barracuda · OVHcloud · Dell · Sophos · PRTG · Azure · Microsoft 365 ‖ études de cas — Migration Cloud… groupe européen vers OVHcloud
  > 来源：https://bluebearsit.com/
- **【决策链与对接人】**ec@bluebearsit.com 培训页「service Commercial」商务箱+ap@（CSV 9-27 official-company）；SIREN 840859524+Qualiopi 培训机构资质（培训渠道涉公共补贴资格面、轻划出）。
  > （CSV 2026-09-27 记录）官网培训页公布商务信箱 ec@bluebearsit.com（service Commercial）与 ap@；SIREN 840859524、Qualiopi 培训机构；official-company
  > 来源：https://bluebearsit.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第31批.json`；价格均为 EXW 快照。

- **①背景再核**：FR Lyon MSP（官网+CSV 双核）
- **②芯片/型号**：多牌+AT Resell
- **③KP 深挖**：ec@
- **④Saga 对标**：随单（$180 锚点一致）
- **⑤在乎与偏好**：私营 TPE 性价比

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**Infogérance N1/N2/N3+Intégration Systèmes & Réseaux——TPE/PME，3 sites Lyon/Grenoble/Annecy；CSV: AT Resell+Qualiopi
  > Infogérance N1/N2/N3+Intégration Systèmes & Réseaux——TPE/PME，3 sites Lyon/Grenoble/Annecy；CSV: AT Resell+Qualiopi
  > 来源：https://bluebearsit.com

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：法国 Lyon MSP（TPE/PME）
- **产品线与在售品牌**：Veeam/VMware/Dell/Sophos（AT Resell CSV）
- **目标行业与场景**：私营 TPE/PME
- **团队与规模**：中型（3 城）
- **决策链与对接人**：ec@ 商务口
- **技术与认证**：Qualiopi 培训（CSV）
- **采购与供应链信号**：托管随单
- **近期动态与线索**：—
- **与我方契合点**：托管现场 value 随单窄位
- **风险与注意**：品牌散——需问清现供

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | BlueBearsIT 法里昂 MSP TPE/PME（infogérance 三地+Qualiopi 培训注）：托管现场随单（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：散
- **O**：随单
- **T**：—

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 教师红线：不打学员名单、不经培训语境推销

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
  - [ ] 现供
  - [ ] 决策权

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Bonjour BlueBearsIT team,

Infogérance for TPE and PME across Lyon, Grenoble and Annecy - your engineers live inside customer networks every week, and every managed site that adds cameras or APs silently consumes a PoE switch.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW (2026-09-29) - a documented value unit for the managed sites you run.

One question: when a managed TPE/PME site needs a new switch, what do you supply today - and would a value PoE unit earn a test?

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

- **KP 领英直达**:[BlueBearsIT · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=BlueBearsIT)(搜索链接,点入后核职位再加;来源:联络核验)
- **中国进口与管制**:国别档位 中(ANSSI 3A 授权制;企业交换机不限);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
