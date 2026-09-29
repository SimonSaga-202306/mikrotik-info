# Evelem

> **评级 A**　|　法国　|　档案编号 `A-320`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-320
rating: A
country: 法国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: true, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Evelem 法 Meudon 集成商（Meraki 旗舰+Cambium EX3000 展示+Small Business 板块）：SMB 段二轨窄位（$165 锚点一致）；Meraki/Cambium 旁前句；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Evelem（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 | 事实 |
| 网站 | https://www.evelem.fr | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Evelem（法国 Meudon-la-Forêt）：设计-部署-运维网络架构的集成商——Infrastructure/Sécurité/UC/Hybrid Work/**Small Business** 五板块+**Cisco Meraki 旗舰（摄像头 MV63 推荐位）与 Cambium EX3000 交换展示位**;Evelem Academy+Refresh 计划+Ni Fi 专家服务；CSV=Allied Telesis 伙伴
- 【推断】Meraki 主打的集成商：Cambium EX3000 与 AT 在其 LAN 供应走廊——value 二轨窄位，Small Business 板块是最软口
- 【假设】Small Business 板块的 value PoE 二轨窄位

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

- **邮箱**：contact@evelem.fr
  - 状态：既有/公开
- **电话**：+33 1 76 43 22 22、+33 1 76 43 22 00
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：contact@evelem.fr（官网首页/服务页；客户空间页支持support@evelem.fr、+33 1 76 43 22 22）；+33 1 76 43 22 00；原入口：见 elioplus 渠道库
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · EX3000 旁价位档：24 口 PoE 一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：法语一封：Cambium EX 谱系外的 24 口 PoE++ 价位档第二来源（WIFI/监控项目的接入预算对照+RMA）。
- **要问的问题**：EX3000 之外的价位档谁来填？要第二来源吗？
- **随附证明**：一页报价（法）+ 预算对照。

### 第 2 次跟进 · 监控项目 PoE 旁位

- **推什么**：同左（PoE 预算对照 Meraki MV）
- **切入点**：Meraki MV 摄像项目的 PoE 接入预算对照位。
- **要问的问题**：MV 摄像项目的 PoE 预算有空档吗？
- **随附证明**：PoE 预算表一页。

### 第 3 次跟进 · 配件窄线收口

- **推什么**：SFP/收发器 目录
- **切入点**：全光 EX 型号邻位的 SFP 配件窄线；不回即冻结。
- **要问的问题**：SFP 配件窄线有位吗？
- **随附证明**：配件一页价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第16批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：巴黎 MSP（Cambium 交换线正热+Meraki/Allied 伙伴）——**EX3000 之外价位档=类目空档现成**。
- **产品线与在售品牌**：网络架构托管全系+WIFI 专家服务+Academy+大使计划。
- **目标行业与场景**：巴黎商圈企业（SMB 到中型）。
- **团队与规模**：中型 MSP（360/Academy/大使多臂）。
- **决策链与对接人**：contact@evelem.fr（首页/服务页，CSV 9-27）。
- **技术与认证**：Allied 伙伴（CSV）+Cambium/Meraki 在架。
- **采购与供应链信号**：**Cambium EX 谱系之外的 24 口 PoE 价位档**与 Meraki 监控项目的第三方 PoE 位（MV63 摄像项目）；WIFI 专案服务常有交换机需求随行。
- **近期动态与线索**：EX3000 发布新闻置顶=客户问交换机的流量正进门——价位档提案正当时。
- **与我方契合点**：24 口 PoE 价位档+配件窄线。
- **风险与注意**：Cambium/Meraki 位不替替位；大使/培训生态不做营销。

### R54 原文证据摘录（全部保留）

- **【业务定位】**巴黎南郊 Meudon 的 MSP：「Nous concevons, déployons et maintenons vos architectures réseaux」——设计/部署/营运托管一体；Evelem 360 项目/支持/常驻/WIFI 专家四件服务。
  > INTEGRITE - TECHNICITE - VISION ‖ Nous concevons, déployons et maintenons vos architectures réseaux. Notre offre de service vous assure la continuité de votre activité
  > 来源：https://www.evelem.fr/
- **【近期动态与线索】**首页新品滚动：**Cambium EX3000 交换系列发布（24/48 口含全光型号，cnMaestro One Network）**+Cambium X7-35X WiFi7 AP+Meraki MV63 摄像——Cambium 交换线在其目录里正热。
  > Nouveaux Switchs EX3000 Cambium Networks — Plusieurs modèles 24 et 48 ports, dont des modèles full Fibre ‖ Nouvelle Borne WIFI Cambium Networks X7-35X ‖ Caméra Meraki MV63
  > 来源：https://www.evelem.fr/
- **【决策链与对接人】**contact@evelem.fr 官网首页/服务页正文+支持 support@evelem.fr（CSV 9-27 official-company）；+33 1 76 43 22 00。
  > （CSV 2026-09-27 记录）官网（首页/服务/客户空间）给 contact@evelem.fr、+33 1 76 43 22 00 与 92360 Meudon-la-Forêt；official-company
  > 来源：https://www.evelem.fr/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第32批.json`；价格均为 EXW 快照。

- **①背景再核**：FR Meudon 集成商（官网+CSV 双核）
- **②芯片/型号**：Meraki/Cambium 线
- **③KP 深挖**：contact@
- **④Saga 对标**：二轨窄位（$165 锚点一致）
- **⑤在乎与偏好**：方案完整

### R55 证据摘录（全部保留 · 含数量）

- **【近期动态】**首页展示 Cambium Switchs EX3000（24/48 口系列）与 Meraki MV63；CSV: Allied Telesis 伙伴
  > 首页展示 Cambium Switchs EX3000（24/48 口系列）与 Meraki MV63；CSV: Allied Telesis 伙伴
  > 来源：https://www.evelem.fr

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：法国 Meudon 集成商
- **产品线与在售品牌**：Meraki/Cambium/AT（CSV）
- **目标行业与场景**：企业 SMB/中型 LAN/WiFi
- **团队与规模**：中型
- **决策链与对接人**：contact@ 口
- **技术与认证**：—
- **采购与供应链信号**：项目随单
- **近期动态与线索**：Refresh 计划
- **与我方契合点**：Small Business 段二轨窄位（Meraki/Cambium 旁前句）
- **风险与注意**：Meraki 主权——前句框定

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Evelem 法 Meudon 集成商（Meraki 旗舰+Cambium EX3000 展示+Small Business 板块）：SMB 段二轨窄位（$165 锚点一致）；Meraki/Cambium 旁前句 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：主权
- **O**：窄位
- **T**：Meraki

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
  - [ ] SMB 占比

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Bonjour Evelem team,

Meraki leads the shelf, Cambium EX3000 is on display, and your Small Business offer needs exactly one thing more than the other segments: a budget that closes. One sentence up front: your Meraki and Cambium lines keep their place.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29) - a value tier for the Small Business projects where price decides.

One question: does the Small Business shelf keep a value PoE slot - and would one unit earn a lab test?

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
