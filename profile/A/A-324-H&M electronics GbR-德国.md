# H&M electronics GbR

> **评级 A**　|　德国 · Dillingen an der Donau　|　档案编号 `A-324`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-324
rating: A
country: 德国
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
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — H&M electronics 德 Dillingen 30 年通信店（Terra Partner+Securepoint+Unify/Agfeo）：SMB 电话/网络 Voice VLAN 随件（$180 锚点一致）；实体名 OHG/GbR 双形注；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | H&M electronics GbR（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Dillingen an der Donau | 事实 |
| 网站 | https://hm-electronics.de | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】H&M electronics（德国 Dillingen a.d. Donau；30 年通信技术店）：电话系统至 ~600 分机+固网/移动资费+IT 线（**Terra Partner+Securepoint Authorized Reseller**）；墙牌 Unify/Agfeo/Wortmann/Securepoint；门店零售在营；CSV=Allied Telesis Resell（官网实体名 OHG vs CSV 'GbR' 名注）
- 【推断】区域通信店多牌共存：SMB 电话/网络项目交换件随身——Voice VLAN 叙事可讲；低中密度
- 【假设】SMB 通信项目随身 value 件（Voice VLAN 角）

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@hm-electronics.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：info@hm-electronics.de（官网AGB页Anbieterkennzeichnung）；09071/7925-0；H&M electronics GbR
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · VoIP 装机配搭 24 口 PoE 一页

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：德语一封直入：600 分机电话系统的 PoE 接入层配搭（话机 VLAN 预设即用+RMA 先行，装机省时）。
- **要问的问题**：PBX 项目的 PoE 接入层目前配哪个牌？
- **随附证明**：一页报价（德）+ 话机 VLAN 预设。

### 第 2 次跟进 · 门店备件小批

- **推什么**：STI-280GE（Saga） 等小批
- **切入点**：多店备件小批常备价。
- **要问的问题**：备件有没有门店常备量？
- **随附证明**：小批价卡一页。

### 第 3 次跟进 · 价卡留档收口

- **推什么**：—（价卡留档）
- **切入点**：全品类价卡留档；无回复即冻结。
- **要问的问题**：（无需回）价卡留档。
- **随附证明**：全品类一页价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第17批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：迪林根 30 年电话系统老店（600 分机装机=VoIP PoE 直通消耗位）；Allied 名录在册。
- **产品线与在售品牌**：PBX/资费/IT 硬件四件（Unify/Agfeo/Wortmann/Securepoint）。
- **目标行业与场景**：施瓦本领地企业（门店型）。
- **团队与规模**：小型多店连锁。
- **决策链与对接人**：info@hm-electronics.de（AGB 页，CSV 9-27）；团队页分工清楚（网络件问 Johann）。
- **技术与认证**：Securepoint Authorized（官网）+Allied Resell（CSV）。
- **采购与供应链信号**：**电话系统的 PoE 接入层即插即用**：600 分机级装机配 24 口 PoE++；Securepoint 防火墙旁位的交换板位。
- **近期动态与线索**：门店型现金流稳，小批备货习性。
- **与我方契合点**：24 口 PoE（VoIP 装机配搭）+备件小批。
- **风险与注意**：老式站与反垃圾态度：一封德文直给、附件少。

### R54 原文证据摘录（全部保留）

- **【业务定位】**多瑙河畔迪林根 30 年**通信技术老店：最大 600 分机的电话系统**设计安装维护+移动商务资费+IT 硬件（Terra/Wortmann 伙伴、Securepoint 授权转售）——**VoIP 装机量即 PoE 装机量**。
  > Seit nunmehr 30 Jahren… Ansprechpartner für die komplette Kommunikationstechnik und IT ‖ konzeptionieren, installieren und warten Telefonanlagen bis ca. 600 Nebenstellen
  > 来源：https://hm-electronics.de/
- **【产品线与在售品牌】**伙伴：Unify/Agfeo/Wortmann（Terra）/Securepoint；门店形态（Filialen）陈列有线/无线话机与PBX现货。
  > Unsere Partner — unify · agfeo · wortmann · securepoint
  > 来源：https://hm-electronics.de/
- **【决策链与对接人】**info@hm-electronics.de（AGB 页 Anbieterkennzeichnung，CSV 9-27 official-company）；09071/7925-0；团队页按项目分工列出 Thomas（电话系统）/Johann（网络与 IT）/Sarah（资费）等直联入口。
  > （CSV 2026-09-27 记录）AGB 页 Anbieterkennzeichnung 给 info@hm-electronics.de、Tel 09071/7925-0、H&M electronics GbR（USt-ID…）‖ （官网团队页）Netzwerk-Einrichtung & Service → Johann
  > 来源：https://hm-electronics.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第33批.json`；价格均为 EXW 快照。

- **①背景再核**：DE 区域通信店（官网一手核）
- **②芯片/型号**：Terra/Securepoint
- **③KP 深挖**：info@
- **④Saga 对标**：随身窄位（$180 锚点一致，低密）
- **⑤在乎与偏好**：门店信誉/本地

### R55 证据摘录（全部保留 · 含数量）

- **【技术与认证】**Als Terra Partner und Securepoint Authorized Reseller haben wir die komplette Hardware im Programm（官网）
  > Als Terra Partner und Securepoint Authorized Reseller haben wir die komplette Hardware im Programm（官网）
  > 来源：https://hm-electronics.de

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：德国区域通信技术店（30 年）
- **产品线与在售品牌**：Terra/Securepoint/Unify/Agfeo（AT CSV）
- **目标行业与场景**：区域 SMB 电话/IT
- **团队与规模**：门店微团
- **决策链与对接人**：info@ 口
- **技术与认证**：—
- **采购与供应链信号**：门店断码随件
- **近期动态与线索**：—
- **与我方契合点**：SMB 通信项目随身件（Voice VLAN 角）
- **风险与注意**：实体名 OHG/GbR 名注已落

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | H&M electronics 德 Dillingen 30 年通信店（Terra Partner+Securepoint+Unify/Agfeo）：SMB 电话/网络 Voice VLAN 随件（$180 锚点一致）；实体名 OHG/GbR 双形注 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：小
- **O**：随身
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
  - [ ] 现供
  - [ ] IT 负责人

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hallo H&M electronics team,

Thirty years of communication technology in Dillingen - phone systems up to 600 extensions, and an IT side carrying Terra and Securepoint hardware. Where IP telephony enters a site, Voice VLANs and PoE follow.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, Voice-VLAN ready, watchdog) with full documentation. Reference: $180 USD EXW (2026-09-29) - a value unit for the SMB phone-plus-network jobs you install.

One question: when a phone-and-network project needs switching, what do you supply today?

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

- **KP 领英直达**:[H&M electronics GbR · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=H%26M%20electronics%20GbR)(搜索链接,点入后核职位再加;来源:联络核验)
- **中国进口与管制**:国别档位 中(IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
