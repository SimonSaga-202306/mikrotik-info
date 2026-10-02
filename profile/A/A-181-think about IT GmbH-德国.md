# think about IT GmbH

> **评级 A**　|　德国 · Bochum　|　档案编号 `A-181`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-181
rating: A
country: 德国
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
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — thinkGROUP Top30 系统屋：企业段 SMB 端窄位（$165 锚点一致）；公共/医疗守界；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | think about IT GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Bochum | 事实 |
| 网站 | https://think-about.it | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】think about IT GmbH（thinkGROUP，德国）：**德国 Top 30 系统屋**——ITIL 认证一站式服务；**Managed NVIDIA DGX/Spark 托管+High Performance Computing 集群落地**+Managed Network/Workplace/Datacenter/Security；自有房展 InfinIT Future（Hattingen Henrichshütte）；Branchen 三块=**Geschäftskunden/Öffentliche Auftraggeber/Healthcare（公共+医疗守界段）**
- 【推断】Top30 规模+Managed Network 模块=其交付接入层随单结构清晰；公共/医疗段守界，企业客户段主打窄位
- 【假设】HPC/数据中心业务重=其 Managed Network 里 SMB 端的 value 件缝隙

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：frontoffice@think-about.it
  - 状态：既有/公开
- **电话**：—
- 来源等级：company-store（R41–R48 联系方式台账口径）
- **原始联系字段**：frontoffice@think-about.it [Publicly listed; delivery not tested]; https://think-about.it
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（商业项目接入层；公共/医疗段划线）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：供应商名录敲门：公司一页+CE/声明文件包+24 口 PoE++ 规格对照，声明公共与医疗项目段不涉。
- **要问的问题**：Managed Network 里的接入层标准件现在什么型号？
- **随附证明**：公司一页 + CE/声明文件包 + 规格对照（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（商业客户厂房/车库点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：商业客户厂房与车库点位：宽温 DIN PoE+备件包。
- **要问的问题**：厂房/车库点位的交换坏机率？
- **随附证明**：宽温报告 + 备件包价（德文）。

### 第 3 次跟进 · 管理型 PoE（Managed Network 分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：分段标准件（VLAN/ERPS/SNMP）进他 Managed Network 模块评估——过评估即模块 BOM。
- **要问的问题**：分段模板要不要进 Managed Network 评估？
- **随附证明**：VLAN/ERPS 模板 + MIB 库 + 样机（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第10批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：波鸿 Top30 系统屋（thinkGROUP，并购成长）：ITIL 认证一站式服务+HPC/AI 栈，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：咨询/采购/Staging/集成/运维/物流全链+四款 Managed 模块+NVIDIA DGX/HPC；Secure Boot 专题（2026-06 证书到期预警内容营销）。
- **目标行业与场景**：企业商业项目（正路）；⚠️公共甲方与 Healthcare（首节划线）。
- **团队与规模**：大型集团（Top30 口径+M&A 页持续并购）。
- **决策链与对接人**：frontoffice@think-about.it（CSV 9-27：前台转接入口；官网公开 Janina Elsenheimer 为前台团队负责人）；eBay 店法律资料匹配 Bochum（CSV）。
- **技术与认证**：Allied Resell（CSV 记录）；ITIL 流程体系（官网）。
- **采购与供应链信号**：大屋走供应商名录与流程：首封给公司一页+合规文件包进名录；商业项目组件化切入；Secure Boot 内容营销显示其资料文化，材料齐全者胜。
- **近期动态与线索**：InfinIT Future 2026 房展+Secure Boot 预警专题（2026-06 起）。
- **与我方契合点**：Managed Network 模块的标准接入层件与商用项目组件——他按 BOM 买件，我们按栈供货。
- **风险与注意**：公共甲方/医疗段不供；大屋节奏慢，别以价格新闻开路——走名录+文件包正规流程。

### R54 原文证据摘录（全部保留）

- **【团队与规模】**官网自述：德国 Top 30 系统屋之一；thinkGROUP 自有房展 InfinIT Future 2026 落地 Hattingen 工业遗址 Henrichshütte。
  > Die think about IT GmbH zählt zu den Top 30 Systemhäusern Deutschlands. ‖ InfinIT Future — Die Hausmesse 2026 der thinkGROUP（Henrichshütte Hattingen）
  > 来源：https://think-about.it/
- **【产品线与在售品牌】**One-Stop 组合：咨询/采购/Staging/集成/运维/物流 + Managed Workplace/Security/Network/Datacenter，另有 NVIDIA DGX 托管与 HPC 集群.
  > Our Portfolio: Beratung, Beschaffung, Staging und Integration, Betrieb, Logistik ‖ Managed Workplace · Managed Security · Managed Network · Managed Datacenter · Managed NVIDIA DGX · High Performance Computing
  > 来源：https://think-about.it/
- **【目标行业与场景】**官网行业导航三大块：企业客户、⚠️公共甲方（Öffentliche Auftraggeber）、Healthcare——公立与医疗段划线。
  > Branchen: Geschäftskunden · Öffentliche Auftraggeber · Healthcare（导航栏）
  > 来源：https://think-about.it/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第19批.json`；价格均为 EXW 快照。

- **①背景再核**：Top30 系统屋（HPC 能力强）+thinkGROUP 结构
- **②芯片/型号**：NVIDIA/M365 深处
- **③KP 深挖**：frontoffice@
- **④Saga 对标**：企业段 SMB 端 value 件（边界句）
- **⑤在乎与偏好**：ITIL 流程文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“zählt zu den Top 30 Systemhäusern Deutschlands…Managed Services bis hin zur Realisation komplexer HPC-Cluster…Geschäftskunden/Öffentliche Auftraggeber/Healthcare”
  > “zählt zu den Top 30 Systemhäusern Deutschlands…Managed Services bis hin zur Realisation komplexer HPC-Cluster…Geschäftskunden/Öffentliche Auftraggeber/Healthcare”
  > 来源：https://think-about.it/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：德国 Top30 一站式系统屋（thinkGROUP）
- **产品线与在售品牌**：NVIDIA DGX/M365 生态
- **目标行业与场景**：企业（主）+公共/医疗（守界）
- **团队与规模**：Top30 规模
- **决策链与对接人**：frontoffice@ 口
- **技术与认证**：ITIL 级
- **采购与供应链信号**：框架+随单
- **近期动态与线索**：InfinIT Future 自家展会
- **与我方契合点**：Managed Network 线 SMB 端 value 件
- **风险与注意**：集团框架

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | thinkGROUP Top30 系统屋：企业段 SMB 端窄位（$165 锚点一致）；公共/医疗守界 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：规模
- **W**：框架
- **O**：缝
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
  - [ ] 准入路径
  - [ ] SMB 端结构

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi thinkGROUP team,

A Top-30 German system house doing everything from NVIDIA DGX clusters to residential-site managed networks - the kind of breadth where the SMB end of the access layer is easy to starve of attention. (This note concerns your Geschäftskunden engagements only; public and healthcare segments stay fully out of scope.)

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW - a value unit for the SMB ends of your managed networks.

One question: across your commercial managed-network projects, which switch brand holds the access layer today - and is there room for a documented value alternative at the smaller end of the spectrum?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

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

- **KP 领英直达**:[Janina Elsenheimer · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Janina%20Elsenheimer%20think%20about%20IT%20GmbH)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 中(IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
