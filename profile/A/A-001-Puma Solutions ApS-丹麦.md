# Puma Solutions ApS

> **评级 A**　|　丹麦　|　档案编号 `A-001`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-001
rating: A
country: 丹麦
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：**Puma Solutions ApS**（对外品牌 **Puma IT**），丹麦 Valby（Bjerregårdsvej 16, 2500），CVR **DK44763729**（丹麦 44 开头 CVR ≈ 2021–2022 年注册，年轻公司）。
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（PoE/监控/门禁、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — 主场景匹配+首触只推一个型号的纪律；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Puma Solutions ApS（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 丹麦 | 事实 |
| 网站 | pumait.dk | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Reseller） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | **Puma Solutions ApS**（对外品牌 **Puma IT**），丹麦 Valby（Bjerregårdsvej 16, 2500），CVR **DK44763729**（丹麦 44 开头 CVR ≈ 2021–2022 年注册，年轻公司）。形态=**集成商+网店混合体**：MikroTik 171 个在售产品 + **UniFi 680 个 | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 全线 MikroTik（RouterOS 生态）+ Ubiquiti UniFi（含 UniFi Switching 类目）。芯片层：MikroTik CRS3xx/5xx 交换线多为 Marvell 98DX 系（与我方同源叙事可直接对话）；UniFi 交换线为博通系封闭生态、价格显著高于同级 Marvell 方案——**这就是价差切入位**。出货量/订单 | 事实+【推断】混合，见证据摘录 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

全线 MikroTik（RouterOS 生态）+ Ubiquiti UniFi（含 UniFi Switching 类目）。芯片层：MikroTik CRS3xx/5xx 交换线多为 Marvell 98DX 系（与我方同源叙事可直接对话）；UniFi 交换线为博通系封闭生态、价格显著高于同级 Marvell 方案——**这就是价差切入位**。出货量/订单信息：未公开（私营 ApS 无披露义务），在售 SKU 计数（171/680）作活跃库存代理指标。客户反馈：未见公开评价页，官网自述「Vi siger hvilket brand der passer til opgaven, også når svaret er det, vi tjener mindst på」（品牌中立自评，我方可用）。

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：rfi@pumait.dk
  - 状态：既有/公开
- **电话**：+45 60 70 90 09
- **原始联系字段**：+45 60 70 90 09 / rfi@pumait.dk
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **（法定董事待查）**(业主/采购决策人（推定）)— rfi@pumait.dk；+45 32 33 13 12 / +45 60 70 90 09 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://pumait.dk/ ・ https://www.pumait.dk/contactus〕
  - **—（模式猜测）**(—)— firstname@pumait.dk（待 CVR 查到董事名后套） 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:dns://pumait.dk/MX 2026-09-28 本机核验〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| （法定董事待查） | 业主/采购决策人（推定） | rfi@pumait.dk；+45 32 33 13 12 / +45 60 70 90 09 | 角色邮箱官网公开；姓名未公开→CVR 登记处可拉 | https://pumait.dk/ ・ https://www.pumait.dk/contactus |
| —（模式猜测） | — | firstname@pumait.dk（待 CVR 查到董事名后套） | 模式猜测 · 未验证（MX 已验 Google） | dns://pumait.dk/MX 2026-09-28 本机核验 |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++，4×万兆上行，440W 级）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：接着他自己的话术走：把他手头一个监控项目的「摄像头数 × 单口瓦数」做成一张 PoE 预算表，用我们的整机功率预算实测数 + PoE 看门狗（摄像头死机自动断电重启）对比 CRS328-24P / UniFi Switch 的余量。
- **要问的问题**：现在 24 口 PoE 项目里，他按每口多少瓦设计？满配后留多少余量？
- **随附证明**：整机功率实测表（逐口负载曲线）+ 看门狗演示视频 + 30 天测试机。

### 第 2 次跟进 · 工业级非管理 PoE（DIN 导轨/宽温，零配置）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C，PoE 版 / PoE++ 版）
- **切入点**：他做仓储与门禁，现场经常没有机柜。工业壳 + 宽温 + 宽压 + 免配置，直接装在配电箱或门口弱电箱里；把「非管理」当卖点：插上就用，坏了整机换。
- **要问的问题**：有没有需要装在现场电箱（无空调、无 UPS）的网络点？
- **随附证明**：宽温/宽压测试报告 + DIN 配件实物照 + 现场接线图（一页）。

### 第 3 次跟进 · 管理型 PoE（跨站点标准化）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版 / -2BT 版）
- **切入点**：他卖「多站点同一套配置」，那就给他统一的 VLAN/环网（ERPS）模板：同一份配置下发到不同站点，链路故障 20ms 级切换；把配置模板做成他的交付资产。
- **要问的问题**：跨站点项目要不要环网冗余和统一 VLAN 模板？
- **随附证明**：ERPS 切换实测（打流断链计时）+ 可直接套用的配置模板文件。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：丹麦 MikroTik 认证顾问 + 自营网店（Puma IT，口号「Teknik der virker. Forretning der virker.」），从方案设计、设备预配置到全国上门安装一条龙。
- **产品线与在售品牌**：自营网店两条主线：MikroTik 171 个 SKU（Routers / **Switches** / WiFi / Wireless PtP-PtMP / LTE-5G / 60 GHz）与 UniFi 680 个 SKU（WiFi / **Switching** / Gateways / Protect 视频 / Door Access 门禁）。
- **目标行业与场景**：四条打包方案：视频监控（按「像素/米」而不是按摄像头数量设计）、多站点网络（同一套配置、从第一天就分段）、办公+仓储 WiFi（先做站点勘测与信道规划，并**把 PoE 预算算清楚**）、门禁（门、卡、日志与摄像头同一系统）。
- **团队与规模**：小团队 + 全国服务/安装伙伴网络；自有库存 3–5 个工作日发货；项目只有「一个对接人」。
- **决策链与对接人**：rfi@pumait.dk（对外邮箱）、stefan@pumait.dk（Stefan Andersen，MTCNA+MTCRE，1998 年起做 ISP 网络）、电话 +45 32 33 13 12 / +45 60 70 90 09。
- **技术与认证**：丹麦持证 MikroTik 顾问（MTCNA、MTCRE）；强调「永久许可、无强制云、配置是可进 git 的文本文件」。
- **采购与供应链信号**：已经同时经营 MikroTik 与 UniFi 两条完整产品线，采购逻辑是「按任务选品牌，即使回报最低」——说明他对第三条补充线（成本/规格补位）是开放的。
- **近期动态与线索**：新上「监控存储合规检查（Retention-tjek）」与「30 分钟免费现状评估」两项服务 → 监控与合规项目在增加，摄像头盘位与 PoE 预算都要重算。
- **与我方契合点**：他自己的销售话术就是「把 PoE 预算算清楚」「按像素/米设计」——正是 24 口 PoE++（单口 90W、整机预算实测、看门狗）最能说服的对象；同时他做门禁/监控/多站点，全是我们的目标场景。
- **风险与注意**：已代理 UniFi + MikroTik 两条线，必须以「补规格/压成本/备第二供应商」身份进入；丹麦对 GDPR/CE/能效文件敏感，材料要备齐。

### R54 原文证据摘录（全部保留）

- **【产品线与在售品牌】**官网首页明列 MikroTik 171 个产品、UniFi 680 个产品，并且两条线都有独立的 Switches/Switching 分类页。
  > MikroTik171 produkter … Routers｜Switches｜WiFi｜Wireless PtP/PtMP｜LTE/5G｜60 GHz；UniFi680 produkter … WiFi｜Switches｜Gateways｜Videoovervågning｜Adgangskontrol
  > 来源：https://pumait.dk/
- **【目标行业与场景】**监控方案以「像素/米」为设计口径，并把 GDPR 标识与后续运维写进交付内容。
  > Videoovervågning — Dimensioneret på pixels per meter, ikke på antal kameraer. Lokal storage, GDPR-skiltning som del af leverancen, og drift bagefter.
  > 来源：https://pumait.dk/
- **【与我方契合点】**WiFi 方案承诺在下单前把 PoE 预算算清楚——这是我们最能接话的技术点。
  > WiFi til kontor og lager — Site plan før indkøb: dækning, kanalplan og PoE-budget regnet igennem, så der ikke skal hænges flere access points op bagefter.
  > 来源：https://pumait.dk/
- **【技术与认证】**官网自述为丹麦认证 MikroTik 顾问，且每天自己配置设备。
  > En af Danmarks certificerede MikroTik-konsulenter. Vi konfigurerer udstyret selv til daglig … MTCNA / MTCRE
  > 来源：https://pumait.dk/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类深挖_2026-09-28_R55_第1批.json`；价格均为 EXW 快照。

- **背景深描**：**Puma Solutions ApS**（对外品牌 **Puma IT**），丹麦 Valby（Bjerregårdsvej 16, 2500），CVR **DK44763729**（丹麦 44 开头 CVR ≈ 2021–2022 年注册，年轻公司）。形态=**集成商+网店混合体**：MikroTik 171 个在售产品 + **UniFi 680 个在售产品**双线，配套「全国安装伙伴网+发货前预配置」交付模式（视频监控/多站点网络/办公仓储 WiFi/门禁四大方案页）。持 MTCNA+MTCRE 的丹麦认证顾问之一，强调「我们自己也天天配置这些设备」。LinkedIn/社媒：未见公开公司 LinkedIn，主要通道是官网+电话+rfi@。
- **芯片与在用型号**：全线 MikroTik（RouterOS 生态）+ Ubiquiti UniFi（含 UniFi Switching 类目）。芯片层：MikroTik CRS3xx/5xx 交换线多为 Marvell 98DX 系（与我方同源叙事可直接对话）；UniFi 交换线为博通系封闭生态、价格显著高于同级 Marvell 方案——**这就是价差切入位**。出货量/订单信息：未公开（私营 ApS 无披露义务），在售 SKU 计数（171/680）作活跃库存代理指标。客户反馈：未见公开评价页，官网自述「Vi siger hvilket brand der passer til opgaven, også når svaret er det, vi tjener mindst på」（品牌中立自评，我方可用）。
- **关键人KP**：公开面只有角色邮箱 **rfi@pumait.dk** 与双电话（首页 +45 32 33 13 12 / contactus 页 +45 60 70 90 09）。**决策人姓名未公开**——丹麦 ApS 通常业主即采购；CVR 页可查法定董事（建议跟进前查 datacvr.virk.dk 44763729 拉董事名，再按 firstname@pumait.dk 模式猜测，**当前未验证不写死**）。mx 已验：pumait.dk → Google Workspace。
- **关注点与资质**：①**所有权哲学**：卖「Buy once. Own forever」「Perpetual licens, ingen cloud」——反感订阅/云绑定，报价话术要对齐「一次买断、无云控」；②**发货前预配置**服务是其溢价点，我方供货页可承诺出厂刷配置/贴标；③**GDPR 标识交付**写进监控方案（合规敏感）；④价格透明需求（Priser ekskl. moms 明示）。参展/社媒痕迹未见。
- **优缺点SWOT**：**S**：双线现货（171+680 SKU）+全国安装伙伴网+「敢说 MikroTik 不合适」的顾问信誉；方案页做得细（pixels per meter 维度计算）。**W**：公司年轻（CVR 2021–22）、体量小、人员规模未公开，无自有品牌护城河，对 MikroTik/UniFi 两家供货高度绑定。**O**：UniFi 交换线毛利薄、价格带高 → Saga 同级 Marvell 24口PoE EXW $220 可给「自有利润池/第二品牌」；其 config-before-delivery 模式与 OEM 定制出厂配置天然咬合。**T**：UniFi/MikroTik 官方丹麦分销价格下探时第二供应商空间被挤；所有权哲学可能排拒「无品牌」货，需要样机实测背书破冰。
- **Saga产品适配**：首梯 **STC-424XGGPM-440W**（24×GE PoE af/at 440W，PoE 管理+watchdog，**EXW $220**）对上视频监控/门禁方案页；多站点骨干 **STC-424XGGM**（4×10G SFP+24×GE，**EXW $143**）；小站点 **STC-48DGGPM-U**（EXW $115.5）。⚠️ 商用线无 802.3bt 90W：若其高功率摄像机（PTZ 加热/射灯）超 30W，回 SmartByte `LT-S8328XGP-4XS24GT-S` 并标注「Saga 暂无对应」。报价按 EXW+15 天有效，强调一次买断无云。

### R55 证据摘录（全部保留 · 含数量）

- **【背景】**法定实体 Puma Solutions ApS，CVR DK44763729，rfi@pumait.dk 为公开联系邮箱。
  > PUMA SOLUTIONS APS · CVR DK44763729 · rfi@pumait.dk
  > 来源：https://pumait.dk/
- **【双产品线】**MikroTik 171 款 + UniFi 680 款在售，交换线为两条品牌线。
  > MikroTik171 produkter … UniFi680 produkter
  > 来源：https://pumait.dk/
- **【所有权哲学】**主打一次买断、无云控——报价与出货话术需对齐。
  > Perpetual licens, ingen cloud der skal spørges om lov, og et lettisk selskab bag softwaren.
  > 来源：https://pumait.dk/
- **【联系通道】**contactus 页给出法定地址与第二部电话。
  > Puma Solutions ApS - CVR: DK44763729 - Bjerregårdsvej 16, 2500 Valby - +45 60 70 90 09
  > 来源：https://www.pumait.dk/contactus
- **【交付模式】**发货前按现场图纸预配置——OEM 出厂贴标/刷配置可对口。
  > Vi konfigurerer efter jeres site plan, før udstyret sendes.
  > 来源：https://pumait.dk/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424XGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

**S**：双线现货（171+680 SKU）+全国安装伙伴网+「敢说 MikroTik 不合适」的顾问信誉；方案页做得细（pixels per meter 维度计算）。**W**：公司年轻（CVR 2021–22）、体量小、人员规模未公开，无自有品牌护城河，对 MikroTik/UniFi 两家供货高度绑定。**O**：UniFi 交换线毛利薄、价格带高 → Saga 同级 Marvell 24口PoE EXW $220 可给「自有利润池/第二品牌」；其 config-before-delivery 模式与 OEM 定制出厂配置天然咬合。**T**：UniFi/MikroTik 官方丹麦分销价格下探时第二供应商空间被挤；所有权哲学可能排拒「无品牌」货，需要样机实测背书破冰。

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
| 决策人识别 | ✅ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：Rugged 8-port PoE for outdoor/unheated cabinets

```text
Hi Puma,

I came across Puma Solutions ApS - 分销（MikroTik 官方）.

We build an unmanaged industrial 8-port PoE switch (af/at) with 250m extended reach, redundant 44–57V DC input with reverse-polarity protection, DIN-rail mount and a 3-year warranty. Reference: $74.8 USD EXW.

One question: Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?

If it is useful, I can send one unit for a 30-day evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)
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
