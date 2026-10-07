# Balazs Meretei

> **评级 A**　|　匈牙利 · Kecskemét　|　档案编号 `A-012`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-012
rating: A
country: 匈牙利
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：**Balázs Meretei**（圈内名 **NoXy**），匈牙利 Kecskemét 独立网络顾问。
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE、PoE/监控/门禁、组播/IPTV），且有具体人直联
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — Cisco↔MikroTik 迁移实验室置换机；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Balazs Meretei（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 匈牙利 / Kecskemét | 事实 |
| 网站 | meretei.hu | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCSE+MTCSWE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | **Balázs Meretei**（圈内名 **NoXy**），匈牙利 Kecskemét 独立网络顾问。个人技术博客 meretei.hu（2015–2024 持续发帖：IANA 协议号备忘、IPsec DH-group、PKCS12/openssl、Cisco NTP 夏令时配置备忘——**Cisco 与 MikroTik 双栈实操者**）。另在匈牙利 | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | Cisco ASA/Catalyst CLI（PKCS12、NTP 配置笔记）+ MikroTik RouterOS 脚本（写过 import 即用的 facebook.rsc 生成 bash 脚本）——**自动化与 CLI 深度用户**，对芯片层话题（Marvell 同源）听得懂。其交换笔记覆盖 STP/NTP 等 L2 运维痛点=与我方 L2+ 特性表语 | 事实+【推断】混合，见证据摘录 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

Cisco ASA/Catalyst CLI（PKCS12、NTP 配置笔记）+ MikroTik RouterOS 脚本（写过 import 即用的 facebook.rsc 生成 bash 脚本）——**自动化与 CLI 深度用户**，对芯片层话题（Marvell 同源）听得懂。其交换笔记覆盖 STP/NTP 等 L2 运维痛点=与我方 L2+ 特性表语境重合。出货量：无（顾问）。客户反馈：博客形态即其作品集。

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

- **邮箱**：balazs@meretei.hu
  - 状态：既有/公开
- **电话**：+36 30 999 9900
- **原始联系字段**：+36 30 999 9900 / balazs@meretei.hu
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Balázs Meretei（NoXy）**(独立顾问/wireless-bolt.hu 客座 MTCNA 讲师)— balazs@meretei.hu；+36 30 999 9900 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://meretei.hu/ ・ https://www.wireless-bolt.hu/46618-oktatas/673516-mikrotik-mtcna-kepzes〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Balázs Meretei（NoXy） | 独立顾问/wireless-bolt.hu 客座 MTCNA 讲师 | balazs@meretei.hu；+36 30 999 9900 | 自有域邮箱既有；MX（flash-net.hu）已验 | https://meretei.hu/ ・ https://www.wireless-bolt.hu/46618-oktatas/673516-mikrotik-mtcna-kepzes |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：他在做视频监控与 IPTV：24 口 PoE++ 喂摄像头/AP，重点讲组播表现（IGMP snooping 行为、组播 VLAN）与功率预算。
- **要问的问题**：他现在监控/IPVT 项目里组播怎么做（snooping 开关、组播 VLAN、上行带宽）？
- **随附证明**：组播测试（不泛洪验证）+ 功率实测 + 30 天样机。

### 第 2 次跟进 · 工业级非管理 PoE（WISP/室外）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：WISP 塔站与室外箱体：宽温宽压、DIN、免配置；配 SFP 做长距离回传。
- **要问的问题**：他手上的 WISP 站点的供电与箱体条件如何？
- **随附证明**：宽温/宽压报告 + SFP 兼容清单 + 现场接线一页图。

### 第 3 次跟进 · 管理型 PoE（组播+冗余）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：管理型：IGMP snooping/querier、组播 VLAN、ERPS 环网 —— 直接对应他的 IPTV/监控规模。
- **要问的问题**：规模上去后他打算怎么解决组播泛洪与链路冗余？
- **随附证明**：组播配置模板 + ERPS 实测 + MIB 清单。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：匈牙利（Kecskemét）独立网络工程师，MikroTik 认证顾问；个人站点是技术备忘博客（RouterOS/IPsec/Cisco 现场笔记），说明是长期在项目上的实战派。
- **产品线与在售品牌**：以 MikroTik/RouterOS 生态为主，另有 Cisco/ASA 现场经验（博客内容）。
- **目标行业与场景**：ISP 网络（ADSL/DOCSIS/ETTH/FTTH/WISP）+ 大规模组播（IPTV、视频监控系统）+ RADIUS 认证计费系统（既有记录）。
- **团队与规模**：个人/小团队，决策链=本人。
- **决策链与对接人**：balazs@meretei.hu；+36 30 999 9900。
- **技术与认证**：MTCNA+MTCRE+MTCWE+MTCSE+**MTCSWE**（交换）；博客显示其关注 IPsec、证书、NTP/时区、Cisco 配置等细节。
- **采购与供应链信号**：按项目采购，个人决策；组播/IPTV 项目对 IGMP snooping、组播 VLAN、上行带宽要求高 —— 换设备试错成本高，需要样品测试。
- **近期动态与线索**：博客长期更新（最近含协议号速查、IPsec 证书生成、Cisco NTP 时区备忘等），无公司官网。
- **与我方契合点**：监控与 IPTV 组播是他明写的场景：24 口 PoE（摄像头/AP）+ 组播优化（IGMP snooping、组播 VLAN）+ 环网冗余，正好对上我们的管理型 PoE 与工业线。
- **风险与注意**：他是技术型个人客户：先聊组播/交换细节建立信任，价格话题放后面。

### R54 原文证据摘录（全部保留）

- **【业务定位】**个人站点为技术备忘博客（RouterOS/IPsec/Cisco 实战笔记）。
  > Gyakran kell, ha IPsec routereket bántunk …；Nagyon unom, hogy a switchek/routerek órája … Switch(config)#ntp server 148.6.0.1 / clock timezone CET 1
  > 来源：https://meretei.hu/
- **【目标行业与场景】**既有记录：ISP 网络 + 大规模组播（IPTV、视频监控）+ RADIUS/计费。
  > 专长 ISP 网络（ADSL/DOCSIS/ETTH/FTTH/WISP）+ 大规模组播网络（IPTV、视频监控系统）+ RADIUS 认证计费系统的设计实施
  > 来源：https://mikrotik.com/consultants
- **【技术与认证】**持 MTCSWE（交换）与多证，博客体现 Cisco 现场经验。
  > MTCNA+MTCRE+MTCWE+MTCSE+MTCSWE
  > 来源：https://mikrotik.com/consultants

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类深挖_2026-09-28_R55_第2批.json`；价格均为 EXW 快照。

- **背景深描**：**Balázs Meretei**（圈内名 **NoXy**），匈牙利 Kecskemét 独立网络顾问。个人技术博客 meretei.hu（2015–2024 持续发帖：IANA 协议号备忘、IPsec DH-group、PKCS12/openssl、Cisco NTP 夏令时配置备忘——**Cisco 与 MikroTik 双栈实操者**）。另在匈牙利 MikroTik 装备店 **wireless-bolt.hu 讲授 MTCNA 课程**（第三方授课记录）。持 5 证含 MTCSWE+MTCSE（交换+安全双专向）。
- **芯片与在用型号**：Cisco ASA/Catalyst CLI（PKCS12、NTP 配置笔记）+ MikroTik RouterOS 脚本（写过 import 即用的 facebook.rsc 生成 bash 脚本）——**自动化与 CLI 深度用户**，对芯片层话题（Marvell 同源）听得懂。其交换笔记覆盖 STP/NTP 等 L2 运维痛点=与我方 L2+ 特性表语境重合。出货量：无（顾问）。客户反馈：博客形态即其作品集。
- **关键人KP**：**Balázs Meretei 本人（NoXy）**。邮箱 **balazs@meretei.hu**（CSV 既有；自有域 MX flash-net.hu 今日核验有效）；电话 +36 30 999 9900。LinkedIn 未见确认档案（技术博客型人格）。无需猜测邮箱——实名自有域。
- **关注点与资质**：①证书运维痛点自述（每年 cert 更新流程吐槽=时间敏感型实操者）；②实用主义脚本复用（我写我用）；③swap Cisco↔MikroTik 双语境迁移类项目（企业把思科换 MikroTik 时找他=**交换机替换项目入口人**！）；④匈牙利语沟通。社媒：无，纯博客。
- **优缺点SWOT**：**S**：双栈迁移经验=替换案场的天然买手；自有域实名深技术；教学出镜（wireless-bolt 课）带流量。**W**：一人低频运营、无公司外壳；采购自己动手量小。**O**：Cisco→MikroTik/白牌迁移项目潮里，给他一台可放实验室的 Saga 交换=进入其方案推荐清单的门票；MTCSWE 持证=ERPS/QinQ 特性可深聊。**T**：玩家型顾问忠诚度靠技术信服度；他对虚标零容忍（同 A-008 类型）。
- **Saga产品适配**：实验室置换机：**STC-28DGGPM**（8口 PoE af/at 240W，**EXW $99**，DC 随附电源）+ 进阶 **STI-480XGGM**（工业 L2+ 8口 4×10G ERPS<20ms，**EXW $253**）。话术：工程师对工程师，附 L2+ 特性表原文（<20ms ERPS、Private VLAN、QinQ、MQTT/sFlow）与「出厂可刷预配置」；注明 af/at 上限，不夸大 bt。

### R55 证据摘录（全部保留 · 含数量）

- **【双栈实操】**Cisco 交换 NTP/夏令时配置笔记（双栈证据）。
  > Switch(config)#ntp server 148.6.0.1 … Switch(config)#clock summer-time CEST recurring last Sun Mar 02:00 last Sun Oct 03:00
  > 来源：https://meretei.hu/
- **【教学出镜】**wireless-bolt.hu 的 MTCNA 课程由 Meretei Balázs 授课。
  > A képzést Meretei Balázs tartja.
  > 来源：https://www.wireless-bolt.hu/46618-oktatas/673516-mikrotik-mtcna-kepzes
- **【脚本能力】**写过 MikroTik 配置自动生成脚本（facebook.rsc 生成器）。
  > A mellékelt bash script bármilyen Linux/MAC gépen futtatva generál egy facebook.rsc fájlt, amit csak importálni kell a MikroTik routerbe.
  > 来源：https://meretei.hu/facebook-tiltasa-mikrotik-routerrel/
- **【痛点自述】**年度证书更新流程常忘——时间敏感实操者画像。
  > Évente mikor lejárnak a certek mindig elfelejtem hogyan is kellett PKCS12-t generálni
  > 来源：https://meretei.hu/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Cisco↔MikroTik 迁移实验室置换机 |
| 备选2 | STC-424XGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

**S**：双栈迁移经验=替换案场的天然买手；自有域实名深技术；教学出镜（wireless-bolt 课）带流量。**W**：一人低频运营、无公司外壳；采购自己动手量小。**O**：Cisco→MikroTik/白牌迁移项目潮里，给他一台可放实验室的 Saga 交换=进入其方案推荐清单的门票；MTCSWE 持证=ERPS/QinQ 特性可深聊。**T**：玩家型顾问忠诚度靠技术信服度；他对虚标零容忍（同 A-008 类型）。

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

**主题**：8-port PoE with auto-recovery for your field deployments

```text
Hi Balazs,

I came across Balazs Meretei - 集成商/顾问（MikroTik 认证）.

We build a compact 8-port Gigabit PoE switch (240W budget, af/at) with a hardware PoE watchdog that power-cycles a frozen AP or camera automatically, plus clean 802.1Q VLAN / ERPS / sFlow on the management side. Reference: $99 USD EXW.

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
