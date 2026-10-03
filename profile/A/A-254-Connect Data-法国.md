# Connect Data

> **评级 A**　|　法国 · Bievres　|　档案编号 `A-254`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-254
rating: A
country: 法国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Connect Data-Sintel 法 30+年电信网络 VAD（明列 LAN Switching+RUCKUS/RAD/Teltonika）：板块内二轨正位（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Connect Data（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 / Bievres | 事实 |
| 网站 | https://www.connectdata.fr | 事实 |
| 类型 | 分销/集成商（Perle 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Connect Data - Sintel（法国 30+年电信网络 VAD）：明写 LAN Switching 板块+Carrier Ethernet/WiFi/安全/IoT/VoIP；品牌含 RUCKUS/RAD/RADWIN/Teltonika/Sangoma/AudioCodes；国家认可培训中心+售前咨询+物流
- 【推断】法国 VAD 明列 LAN Switching——RUCKUS 旁边存在 value 第二轨条例（批 26 最强分销）
- 【假设】其转售网络的 value PoE 接入二轨：RUCKUS 之下不撞车定位

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

- **邮箱**：sales@connectdata.fr
  - 状态：既有/公开
- **电话**：+33 1 60 13 70 10
- 来源等级：official-obfuscated（R41–R48 联系方式台账口径）
- **原始联系字段**：sales@connectdata.fr（官网明确[at]/mailto还原）；原入口：+33 1 60 13 70 10
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · Lan Switching 类目提案（24 口监控 PoE）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：走 sales@ 总销口：Lan Switching 类目录下新增 24 口监控 PoE 接入层供应商提案（分销条件+法语资料包一体）。
- **要问的问题**：Lan Switching 类目录有开新供应商位吗？
- **随附证明**：上架一页提案（法）+ 证书包。

### 第 2 次跟进 · 工业宽温件线

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：RAD/Radwin/Teltonika 客群落的现场宽温件线提案（站点/机房外柜）。
- **要问的问题**：现场宽温件类目录谁在供？
- **随附证明**：工业件一页（法/英）。

### 第 3 次跟进 · 配套光铜配件目录

- **推什么**：SFP/SFP+/DAC 目录
- **切入点**：交换类目录的配套配件位。
- **要问的问题**：SFP/DAC 配件线有补价位位吗？
- **随附证明**：配件价卡一页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第13批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：巴黎南区 30 年电信&网络分销（Lan Switching 类目录正式）；Perle 授权 CSV 存录（不在现墙）。
- **产品线与在售品牌**：RUCKUS/RAD/Radwin/Teltonika/Sangoma/AudioCodes 等+四件服务。
- **目标行业与场景**：法国运营商/行业集成商渠道（Carrier Ethernet/RAD 线缆=运营商带）。
- **团队与规模**：Medium 分销（自有培训资质+物流）。
- **决策链与对接人**：sales@connectdata.fr（官网 (at) 还原，CSV 9-27）。
- **技术与认证**：Perle 授权分销（CSV 9-27）；RUCKUS 等现墙。
- **采购与供应链信号**：Lan Switching 类目录现成：**24 口 CCTV/接入 PoE 与工业宽温件**可进其类扩展提案；Teltonika/RAD 客群的现场件旁位。
- **近期动态与线索**：RUCKUS/培训资质常新=目录滚动期。
- **与我方契合点**：24 口监控 PoE 接入层+工业宽温件两条线提案。
- **风险与注意**：Perle 关系 CSV 存录——话术补位不替位；3 封节奏禁催单（大型分销评估周期长）。

### R54 原文证据摘录（全部保留）

- **【业务定位】**巴黎西南 Bievres 的电信&网络解决方案分销 30+ 年：方案线上明写 **Lan Switching**——有正式交换类目。
  > Distributeur de solutions télécoms & réseaux ‖ Wifi, Sécurité et Monétisation, Radio, Lan Switching, Accès Carrier Ethernet, IOT, VoIP Opérateurs, IPBX, Téléphones...
  > 来源：https://www.connectdata.fr/
- **【产品线与在售品牌】**伙伴墙：Altaro/AudioCodes/Dialogic/Nuance/Sangoma/**RUCKUS Networks**/Weblib/RAD/Radwin/**Teltonika**；服务四件：国家认证培训中心/售前咨询/物流/技术支持。
  > （伙伴墙）ruckus networks · rad · radwin · teltonika ‖ CENTRE DE FORMATION — Centre de formation agréé par l’Etat français; CONSEIL AVANT-VENTE; SERVICE LOGISTIQUE; SUPPORT TECHNIQUE
  > 来源：https://www.connectdata.fr/
- **【决策链与对接人】**sales@connectdata.fr 官网 contact 页（at）还原（CSV 9-27：official-obfuscated）——总销口直发。
  > （CSV 2026-09-27 记录）sales@connectdata.fr（官网明确[at]/mailto还原）；Demander un devis 页正文
  > 来源：https://www.connectdata.fr/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第26批.json`；价格均为 EXW 快照。

- **①背景再核**：FR 电信网络 VAD（官网一手核）
- **②芯片/型号**：RUCKUS/RAD 等墙
- **③KP 深挖**：sales@
- **④Saga 对标**：二轨价值槽（$180 锚点一致）
- **⑤在乎与偏好**：培训+售前深度/物流

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**Distributeur de solutions télécoms & réseaux——Wifi, Sécurité, Radio, LAN Switching, Accès Carrier Ethernet, IOT, VoIP；centre de formation agréé
  > Distributeur de solutions télécoms & réseaux——Wifi, Sécurité, Radio, LAN Switching, Accès Carrier Ethernet, IOT, VoIP；centre de formation agréé
  > 来源：https://www.connectdata.fr

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：法国电信网络 VAD（30+年）
- **产品线与在售品牌**：RUCKUS/RAD/Teltonika 等
- **目标行业与场景**：转售商/企业/运营商
- **团队与规模**：分销+培训中心组织
- **决策链与对接人**：sales@ 口
- **技术与认证**：国认可培训中心
- **采购与供应链信号**：分销泳道
- **近期动态与线索**：Sintel 组合叙事
- **与我方契合点**：LAN Switching 板块内二轨（守界前句）
- **风险与注意**：RUCKUS 生态引力——前句框定

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Connect Data-Sintel 法 30+年电信网络 VAD（明列 LAN Switching+RUCKUS/RAD/Teltonika）：板块内二轨正位（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：引力
- **O**：二轨
- **T**：引力

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
  - [ ] 二轨机制
  - [ ] 品牌权责人

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Connect Data - Sintel team,

Thirty-plus years in telecom and network distribution, LAN Switching printed on your own banner, an approved training centre and real logistics. One sentence up front: we are not asking to displace RUCKUS or any line you represent.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW (2026-09-29) - the natural value tier under your headline switching brands, for resellers whose deals close on ROI.

One question: does a value second-track fit inside your LAN Switching board - and can we place one unit in your lab and training room?

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

- **KP 领英直达**:[Connect Data · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Connect%20Data)(搜索链接,点入后核职位再加;来源:联络核验)
- **中国进口与管制**:国别档位 中(ANSSI 3A 授权制;企业交换机不限);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对;工业锚(Moxa/Westermo 类)提及 → Marvell 工业谱同源,STI-288GP 强对口
- **大概率用到的 Saga 型号**:大概率会用: STI-288GP(工业导轨 24G+4×10G→机柜/自动化)、STC-28DGGPM(24G PoE+/4×25G→分销走量)(批量潜力高,可上 280W 旗舰对照行)(本行为调查分析结论,与开发信首推型号是两回事)
