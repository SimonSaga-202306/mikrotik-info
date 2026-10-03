# Selos Informationssysteme GmbH

> **评级 A**　|　德国 · Wilhelmshaven　|　档案编号 `A-178`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-178
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
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Selos 威廉港深 SMB：Auerswald/1&1 同盟随单（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Selos Informationssysteme GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Wilhelmshaven | 事实 |
| 网站 | https://www.selos.de | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Selos Informationssysteme GmbH（德国 Wilhelmshaven 威廉港）：区域 SMB IT——伙伴墙 **1&1/Auerswald（Advanced Partner）/Dell/Kaspersky/IONOS（官方伙伴）**；页面后台图片主题 explicit 含 ethernet/switch 元素
- 【推断】Auerswald 高级伙伴=德国深 SMB 通信同盟（PBX 厂）+1&1/IONOS 双通道=托管 ISP 生态；深 SMB 随单 value 件自然
- 【假设】威廉港港口/海事经济区域=本地企业特色客群

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：kontakt@selos.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：kontakt@selos.de [Publicly listed; delivery not tested]; https://www.selos.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 工业级非管理小件（电话/办公小网供电层）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：Auerswald 电话与办公小网：4 口宽温小机当供电件试单。
- **要问的问题**：电话/办公小网的供电交换配什么？试单价发你。
- **随附证明**：一页报价 + 宽温报告（德文）。

### 第 2 次跟进 · 24 口 CCTV/PoE（稍大项目接入层）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：稍大办公/店面项目：24 口 PoE++ 成本对照。
- **要问的问题**：店面/办公大点的项目接入层现在配什么？
- **随附证明**：规格对照 + 报价（德文）。

### 第 3 次跟进 · 管理型 PoE（办公网分段简件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：办公网分段简件：VLAN 模板速查。
- **要问的问题**：办公网分段模板要不要留一份？
- **随附证明**：VLAN 模板 + 速查卡（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第9批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：威廉港本地硬件老牌：1&1/IONOS 线路业+Auerswald 电话设施+硬件店，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：硬件零售与装机+1&1/IONOS 托管线路+Auerswald TC+Dell+Kaspersky。
- **目标行业与场景**：弗里斯兰海岸区中小企业与私客。
- **团队与规模**：小型本地店。
- **决策链与对接人**：kontakt@selos.de（CSV 9-27：官网明牌与目录互证）。
- **技术与认证**：Auerswald Advanced/IONOS 官方/Kaspersky Silver（官网）；Allied Resell（CSV 记录）。
- **采购与供应链信号**：小店走量小：VoIP/安防/办公小网络升级替他配 4–8 口小 PoE 件最合适。
- **近期动态与线索**：站点 Joomla 老版式但伙伴牌新（IONOS 徽章体系新）。
- **与我方契合点**：电话/办公小网的 PoE 小件——Auerswald 电话安装旁的供电层。
- **风险与注意**：量少别提大单一页；德文报价给试单价。

### R54 原文证据摘录（全部保留）

- **【产品线与在售品牌】**官网伙伴墙：1&1（一级代理绑定）/Auerswald Advanced Partner/Dell/Kaspersky Silver/IONOS 官方伙伴——通信与主机托管是他的两条筋。
  > （伙伴墙）1und1 Partner · Auerswald Advanced Partner · Dell · Kaspersky United Silver Partner · IONOS - Offizieller Partner（PartnerBadge 带链接）
  > 来源：https://www.selos.de/
- **【决策链与对接人】**官网明牌：地址/电话/邮箱/作息一次给全——本地化小店作风（CSV 9-27 同，与目录互证）。
  > Selos Informationssysteme GmbH, Bismarckstraße 185, 26382 Wilhelmshaven · Tel.: +49 4421 9787-0 · Email: kontakt@selos.de · Montag-Donnerstag 8:30-13:00 und 14:00-17:00, Freitag… 16:00
  > 来源：https://www.selos.de/
- **【业务定位】**首页横幅就是自己产品线关键词：CPU/EPROM/Ethernet/硬盘/主板/**Switch**——硬件店起家的信息系统商。
  > （首页横幅图序列文件名）cpu_1920x1280 · eprom_1920x1280 · ethernet_1920x1280 · hd_1920x1280 · kwbruecke_1920x1280 · motherboard_1920x1280 · switch_1920x1280
  > 来源：https://www.selos.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第18批.json`；价格均为 EXW 快照。

- **①背景再核**：威廉港深 SMB（Auerswald 高级伙伴+1&1/IONOS）
- **②芯片/型号**：Auerswald/Dell
- **③KP 深挖**：kontakt@
- **④Saga 对标**：深 SMB 随单 value 件
- **⑤在乎与偏好**：伙伴级文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“[partner wall:] 1und1, Auerswald Advanced Partner, Dell, Kaspersky, IONOS Offizieller Partner”
  > “[partner wall:] 1und1, Auerswald Advanced Partner, Dell, Kaspersky, IONOS Offizieller Partner”
  > 来源：https://www.selos.de/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：威廉港深 SMB IT（Auerswald/1&1 同盟）
- **产品线与在售品牌**：Auerswald/Dell/Kaspersky
- **目标行业与场景**：深 SMB
- **团队与规模**：小型
- **决策链与对接人**：kontakt@ 口
- **技术与认证**：伙伴级
- **采购与供应链信号**：随单
- **近期动态与线索**：—
- **与我方契合点**：深 SMB 随单 value 件
- **风险与注意**：

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Selos 威廉港深 SMB：Auerswald/1&1 同盟随单（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：同盟
- **W**：体量
- **O**：随单
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
  - [ ] 1&1 通道关系
  - [ ] 量

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Selos team,

An Auerswald Advanced Partner serving Wilhelmshaven's local businesses - deep-SMB communication systems, configured and cared for.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, Voice VLAN - the feature your Auerswald telephony customers actually use) with full documentation. Reference: $180 USD EXW.

One question: in your deep-SMB installations, which switch brand carries the PoE voice and network layer today - and would a documented value alternative earn a bench test beside your Auerswald line?

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

- **KP 领英直达**:[Selos Informationssysteme GmbH · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Selos%20Informationssysteme%20GmbH)(无具名 KP 信号,先搜公司再加人;待查)
- **中国进口与管制**:国别档位 中(IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
