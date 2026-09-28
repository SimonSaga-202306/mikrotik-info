# Balazs Meretei

> **评级 A**　|　匈牙利 · Kecskemét　|　档案编号 `A-012`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、PoE/监控/门禁、组播/IPTV），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Balazs Meretei |
| 国家 | 匈牙利 |
| 城市 | Kecskemét |
| 网站 | meretei.hu |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCSE+MTCSWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424DGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 持 MTCSWE；专长 **ISP 网络（ADSL/DOCSIS/ETTH/FTTH/WISP）+ 大规模组播网络（IPTV、视频监控系统）+ RADIUS 认证计费系统**的设计实施 → 监控与 IPTV 是最吃交换机的场景，IGMP Snooping/组播 VLAN 是硬需求 |

## 三、人员与联系方式

- **邮箱**：balazs@meretei.hu
- **电话**：+36 30 999 9900
- **原始联系字段**：+36 30 999 9900 / balazs@meretei.hu

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCSE、MTCSWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：组播 / IPTV

### 推什么型号

**STC-424DGGPM-440W（Saga）（组播能力完整 + PoE 供电）**

> 系统初判型号：`STC-424DGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

IGMP Snooping v2/v3、IGMP Querier、组播 VLAN、快速离开（Fast Leave）、**QoS/DSCP 优先级队列**（Dante 音频 over IP 与 IPTV 都靠它不丢包不抖动）

### 怎么开发

开口就问「IPTV 卡不卡？是不是组播没配好，全楼在泛洪？」；若是 Dante / 音频 over IP 场景，改问「音频有没有出现过断续或丢包？」——Dante 对组播和 QoS 极敏感，说中就是内行

### 风险点

组播出问题是满屏花屏，客户零容忍；必须先小规模（一个楼层）验证再铺开；要确认他的组播源和播放器兼容性

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。

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

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**个人站点为技术备忘博客（RouterOS/IPsec/Cisco 实战笔记）。
  > Gyakran kell, ha IPsec routereket bántunk …；Nagyon unom, hogy a switchek/routerek órája … Switch(config)#ntp server 148.6.0.1 / clock timezone CET 1
  > 来源：https://meretei.hu/
- **【目标行业与场景】**既有记录：ISP 网络 + 大规模组播（IPTV、视频监控）+ RADIUS/计费。
  > 专长 ISP 网络（ADSL/DOCSIS/ETTH/FTTH/WISP）+ 大规模组播网络（IPTV、视频监控系统）+ RADIUS 认证计费系统的设计实施
  > 来源：https://mikrotik.com/consultants
- **【技术与认证】**持 MTCSWE（交换）与多证，博客体现 Cisco 现场经验。
  > MTCNA+MTCRE+MTCWE+MTCSE+MTCSWE
  > 来源：https://mikrotik.com/consultants

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
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

## 九、深度再发掘（R55：背景 · 芯片/型号 · 关键人 · 在意点 · SWOT · Saga 适配）

> 调研日期 **2026-09-28**；来源含官网/公开工商与社媒页面，原文摘录见本节后部；原始记录：`batch/A类深挖_2026-09-28_R55_第2批.json`。涉及我方价格均为 EXW 快照（15 天有效，报价前核价）。

- **背景深描**：**Balázs Meretei**（圈内名 **NoXy**），匈牙利 Kecskemét 独立网络顾问。个人技术博客 meretei.hu（2015–2024 持续发帖：IANA 协议号备忘、IPsec DH-group、PKCS12/openssl、Cisco NTP 夏令时配置备忘——**Cisco 与 MikroTik 双栈实操者**）。另在匈牙利 MikroTik 装备店 **wireless-bolt.hu 讲授 MTCNA 课程**（第三方授课记录）。持 5 证含 MTCSWE+MTCSE（交换+安全双专向）。
- **芯片与在用型号**：Cisco ASA/Catalyst CLI（PKCS12、NTP 配置笔记）+ MikroTik RouterOS 脚本（写过 import 即用的 facebook.rsc 生成 bash 脚本）——**自动化与 CLI 深度用户**，对芯片层话题（Marvell 同源）听得懂。其交换笔记覆盖 STP/NTP 等 L2 运维痛点=与我方 L2+ 特性表语境重合。出货量：无（顾问）。客户反馈：博客形态即其作品集。
- **关键人KP**：**Balázs Meretei 本人（NoXy）**。邮箱 **balazs@meretei.hu**（CSV 既有；自有域 MX flash-net.hu 今日核验有效）；电话 +36 30 999 9900。LinkedIn 未见确认档案（技术博客型人格）。无需猜测邮箱——实名自有域。
- **关注点与资质**：①证书运维痛点自述（每年 cert 更新流程吐槽=时间敏感型实操者）；②实用主义脚本复用（我写我用）；③swap Cisco↔MikroTik 双语境迁移类项目（企业把思科换 MikroTik 时找他=**交换机替换项目入口人**！）；④匈牙利语沟通。社媒：无，纯博客。
- **优缺点SWOT**：**S**：双栈迁移经验=替换案场的天然买手；自有域实名深技术；教学出镜（wireless-bolt 课）带流量。**W**：一人低频运营、无公司外壳；采购自己动手量小。**O**：Cisco→MikroTik/白牌迁移项目潮里，给他一台可放实验室的 Saga 交换=进入其方案推荐清单的门票；MTCSWE 持证=ERPS/QinQ 特性可深聊。**T**：玩家型顾问忠诚度靠技术信服度；他对虚标零容忍（同 A-008 类型）。
- **Saga产品适配**：实验室置换机：**STC-28DGGPM**（8口 PoE af/at 240W，**EXW $99**，DC 随附电源）+ 进阶 **STI-480XGGM**（工业 L2+ 8口 4×10G ERPS<20ms，**EXW $253**）。话术：工程师对工程师，附 L2+ 特性表原文（<20ms ERPS、Private VLAN、QinQ、MQTT/sFlow）与「出厂可刷预配置」；注明 af/at 上限，不夸大 bt。

### 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Balázs Meretei（NoXy） | 独立顾问/wireless-bolt.hu 客座 MTCNA 讲师 | balazs@meretei.hu；+36 30 999 9900 | 自有域邮箱既有；MX（flash-net.hu）已验 | https://meretei.hu/ ・ https://www.wireless-bolt.hu/46618-oktatas/673516-mikrotik-mtcna-kepzes |

### R55 证据摘录

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

## 十、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十一、首触邮件（可直接发送）

**主题**：IGMP / multicast behaviour on your IPTV builds

```text
Hi Balazs,

Multicast is where most IPTV and camera builds quietly fall over, and it is the part I specialise in on the access switch.

What caught my eye is that you work on IPTV, IGMP, WISP, FTTH, DOCSIS, ETTH, VLAN and RADIUS.

Where we may be useful: IGMP snooping v2/v3, a querier so the VLAN stops flooding, multicast VLAN, fast leave, and DSCP/QoS queues — the things that decide whether IPTV is watchable and whether Dante audio drops out.

Are you running IGMP snooping plus a querier, or still flooding the VLAN?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424DGGPM-440W evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

Either way, no follow-up sequence from me.

Best,
[your name]
```

> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；③ 落款换成你自己的名字与公司；④ 一次只问一个问题。

## 十二、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
