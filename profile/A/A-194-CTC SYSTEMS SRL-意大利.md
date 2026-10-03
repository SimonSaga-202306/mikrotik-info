# CTC SYSTEMS SRL

> **评级 A**　|　意大利 · Lecco　|　档案编号 `A-194`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-194
rating: A
country: 意大利
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
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — CTC Lecco OA/软件主线：硬件支线窄位低优先（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | CTC SYSTEMS SRL（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Lecco | 事实 |
| 网站 | https://www.ctcsystems.it | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】CTC SYSTEMS SRL（意大利 Lecco，10+ 年）：**Office Automation+管理软件主线（Sistemi 产品线 eSOLVER/SPRING/PROFIS/PEOPLELINK）+硬件支线+租赁打印+零售**；“arredo-ufficio chiavi in mano（交钥匙办公配套）”；伙伴 Lenovo/Nethesis；自述硬件线含“infrastrutture di networking”
- 【推断】管理软件主线商：网络基础是其硬件支线的次级类目——窄位低优先但存在
- 【假设】Lecco 伦巴第小圈子（同批18 Agomir 同城文化）：关系密集，慢而粘

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@ctcsystems.it
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@ctcsystems.it [Publicly listed; delivery not tested]; https://www.ctcsystems.it
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 工业级非管理小件（门店/POS 供电层）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：门店 POS/打印/摄像头的供电小件：4 口宽温小机试单价先行。
- **要问的问题**：门店/库房点位的小交换用什么？试用价发您。
- **随附证明**：一页报价 + 宽温要点（意/英）。

### 第 2 次跟进 · 24 口 CCTV/PoE（办公网/多点位接入层）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：稍大办公/门店多点位：24 口 PoE++ 对照现用件。
- **要问的问题**：稍大项目的接入层现在配什么？
- **随附证明**：规格对照 + 报价。

### 第 3 次跟进 · 管理型 PoE（门店网分段简件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：门店/办公分段简件：VLAN 速查。
- **要问的问题**：门店网分段模板要不要留一份？
- **随附证明**：VLAN 速查卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第10批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Lecco 十年办公自动化+ICT 店：软件/硬件/多功能/零售四线，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：Sistemi 系 gestionale+硬件+多功能打印+零售 POS/telematic 收银+网络基建。
- **目标行业与场景**：Lecco 商圈小微企业/门店/事务所。
- **团队与规模**：小型（Calco 总部+Lecco 办公，CSV 9-27 双点记录）。
- **决策链与对接人**：info@ctcsystems.it（CSV 9-27：官网列 Calco 总部与 Lecco 办公，邮箱适用本企业）。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：零售/POS/门店场景=小型 PoE（收银/打印/摄像头/门显）接件；价格敏感先试单价。
- **近期动态与线索**：本地报（Giornale di Lecco）2021 两次报道——区域口碑店。
- **与我方契合点**：门店小 PoE 件+稍大办公网的接入层。
- **风险与注意**：新闻区日期字段有乱码（30/11/-0001 模板 bug）不影响正文采用；报价一页式。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：10+ 年 Office Automation/ICT/管理软件/零售四线——Sistemi 系 gestionale（eSOLVER/SPRING/PROFIS/PEOPLELINK）+数码多功能+网络基建。
  > Da oltre 10 anni al servizio del cambiamento… partner di riferimento per la consulenza, il noleggio, la vendita e l'assistenza tecnica nel campo dell'Office Automation, Information & Communication Technology, Software Gestionali e Retail. ‖ Dispositivi e infrastrutture di networking al caso tuo
  > 来源：https://www.ctcsystems.it/
- **【产品线与在售品牌】**零售语境小件：telematic 收银机（registratori telematici）假期流程帖——店销/零售 POS 场景是他的日常。
  > Registratori telematici: cambio di stato in modalità "Fuori Servizio" per le ferie estive（#NEWS 帖）· CTC System: arredo-ufficio chiavi in mano（Giornale di Lecco 2021）
  > 来源：https://www.ctcsystems.it/
- **【产品线与在售品牌】**伙伴牌含 Lenovo/NethServer（Nethesis 开源）/OpenAI/ItalRetail——开源感 SMB 栈。
  > （伙伴牌）Lenovo · Nethesis（NethServer）· OpenAI · ItalRetail
  > 来源：https://www.ctcsystems.it/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第20批.json`；价格均为 EXW 快照。

- **①背景再核**：OA/软件主线（硬件窄支线，网络在支线菜单）
- **②芯片/型号**：Lenovo/Nethesis
- **③KP 深挖**：info@
- **④Saga 对标**：硬件支线窄位（低优先）
- **⑤在乎与偏好**：关系文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“consulenza, il noleggio, la vendita e l’assistenza tecnica nel campo dell’Office Automation, ICT, Software Gestionali e Retail…Dispositivi e infrastrutture di networking al caso tuo”
  > “consulenza, il noleggio, la vendita e l’assistenza tecnica nel campo dell’Office Automation, ICT, Software Gestionali e Retail…Dispositivi e infrastrutture di networking al caso tuo”
  > 来源：https://www.ctcsystems.it/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：Lecco OA/软件主线商（硬件窄支线）
- **产品线与在售品牌**：Lenovo/Sistemi 族
- **目标行业与场景**：区域企业
- **团队与规模**：小型
- **决策链与对接人**：info@ 口
- **技术与认证**：伙伴级
- **采购与供应链信号**：随单（窄）
- **近期动态与线索**：交钥匙办公文化
- **与我方契合点**：硬件支线网络基础窄位（低优先）
- **风险与注意**：主要语言软件

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | CTC Lecco OA/软件主线：硬件支线窄位低优先（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：软件
- **W**：窄
- **O**：随单
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
  - [ ] 网络件现供
  - [ ] 支线权重

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi CTC Systems team,

Software in the lead, office automation in tow - your hardware line carries networking infrastructure exactly where a project needs it, without the badge discussion. (One line of honesty from our side: networking is a supporting discipline for you, so this is a light-touch note.)

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW - a value unit for the network layer inside your arredo-ufficio turnkey projects.

One question: when a client project needs network hardware, which switch brand do you reach for today - and would a documented value alternative be worth keeping in the drawer?

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

- **KP 领英直达**:[CTC SYSTEMS SRL · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=CTC%20SYSTEMS%20SRL)(搜索链接,点入后核职位再加;来源:档案名(个人档))
- **中国进口与管制**:国别档位 中(Golden Power 5G/能源延伸;企业交换机不受限);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
