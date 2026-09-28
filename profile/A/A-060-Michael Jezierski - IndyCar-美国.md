# Michael Jezierski / IndyCar

> **评级 A**　|　美国 · Indianapolis　|　档案编号 `A-060`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、PoE/监控/门禁、组播/IPTV），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | IndyCar |
| 国家 | 美国 |
| 城市 | Indianapolis |
| 网站 | indycar.com |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCIPv6E+MTCSWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424DGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 持 MTCSWE；**专做美国赛车运动产业与车队（邮箱是 @indycar.com，人在 IndyCar 赛事方）**；业务：Layer 2/3、无线 LAN、PtP、**IP 视频与组播 IP Video & Multicast**、IP 对讲、**Audinate Dante 认证 1/2/3 级（专业音频 over IP）** → 赛事转播+ Dante 音频对交换机的 IGMP Snooping/组播/低时延要求极高，是极高门槛高单价的细分市场 |

## 三、人员与联系方式

- **对接人**：Michael Jezierski
- **邮箱**：mjezierski@indycar.com
- **电话**：+1 317 492 5005
- **原始联系字段**：+1 317 492 5005 / mjezierski@indycar.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCIPv6E、MTCSWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCIPv6E` — IPv6
- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：Audinate、Dante、MikroTik

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

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。

- **业务定位**：美国 IndyCar 赛事组织内（机构属性 Indianapolis Headquarters）：Michael Jezierski 是赛事方的 MikroTik 顾问，L2/L3、无线 LAN、PtP、IP 视频与组播 IP 是熟项。
- **产品线与在售品牌**：赛事内部采购＋车队外部顾问业务（私下购买路径双通道）。
- **目标行业与场景**：分站现场搭建：Fan WiFi/赛事内部 IPTV/监控/计时与数据传输/Timing equipment。
- **团队与规模**：IndyCar 是一家机构（赛事主办方）——技术、IOT、后勤多层级，他本人即可决定配置。
- **决策链与对接人**：Michael Jezierski（mjezierski@indycar.com / +1 317 492 5005）。
- **技术与认证**：MTCNA+MTCRE+MTCIPv6E+MTCSWE（CSV 既有 MikroTik 名录记录）；地气极熟。
- **采购与供应链信号**：分站现场临时设施在赛季前的搭建期集中采购——9 月 6 日收官战后进入盘点/封存阶段，休赛期正是补新件的窗口。
- **近期动态与线索**：赛季刚刚收官，设施/物料清单在盘点——现在进他的采购周期最好。
- **与我方契合点**：高密度 PoE++（Fan WiFi/监控）、工业宽温（室外临时机柜）、管理型（IGMP 组播视频、ERPS 快速环）——三点都好讲。
- **风险与注意**：他的主品牌体系固定（MikroTik 也同时给站台）——方案要从“现场临时设施里换算成本”维度切，别主诉品牌替代。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【近期动态与线索】**NTT INDYCAR SERIES 2026 赛季赛历完整收官：9 月 6 日 Laguna Seca 收官战（冠军 Scott McLaughlin）——赛季后基建改造窗口明开。
  > Sep 6 Laguna Seca — Scott McLaughlin
  > 来源：https://www.indycar.com/
- **【目标行业与场景】**2026 赛历从 3 月 1 日 St. Pete 至 9 月 6 日 17 站巡回——Street/Circuit/Superspeedway 三类现场都需要移动搭建网络与监控。
  > Mar 1 St. Petersburg · May 24 Indy 500 · Sep 6 Laguna Seca
  > 来源：https://www.indycar.com/
- **【技术与认证】**他（CSV 记录为 MikroTik 官方顾问）所在机构即 NTT INDYCAR SERIES 官方——权威主办的赛事组织（来源性质：机构官网）。
  > The Official Site of the NTT INDYCAR SERIES
  > 来源：https://www.indycar.com/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 PoE++（Fan WiFi/监控的推荐档次）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：分站 Fan WiFi+监控接入层：24 口 PoE++ 一次到位，场地清单备件/到货可直接整箱——赛季收口时盘点他最敏感。
- **要问的问题**：分站现场 24 口 PoE 一般用哪个档位、现在留多少台备用？
- **随附证明**：功率实测表 + 与 CRS328-24P/UniFi 对照页（英文）。

### 第 2 次跟进 · 工业非管理 PoE（临时设施/移动机柜）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：临时设施的赛道旁+内场机柜：宽温宽压、DIN、免配置，随包随拆——拆装运输都轻。
- **要问的问题**：现场临时点位和机柜现在怎么供货、搭建期交期压到几天？
- **随附证明**：宽温报告 + DIN 安装图 + 备件包价格。

### 第 3 次跟进 · 管理型（IGMP 组播/ERPS 环）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：IP 视频/组播业务是他熟项：管理型 VLAN 分段+IGMP+ERPS 快速环——给方案文档面板到底，节省工时。
- **要问的问题**：席位/监控/计时网段是分开的吗？环网用什么协议做？
- **随附证明**：VLAN/ERPS/IGMP 配置模板 + ERPS 收敛实测（英文）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：IGMP / multicast behaviour on your IPTV builds

```text
Hi Michael,

Multicast is where most IPTV and camera builds quietly fall over, and it is the part I specialise in on the access switch.

What caught my eye is that you work on Dante, Audinate, multicast and IGMP.

Where we may be useful: IGMP snooping v2/v3, a querier so the VLAN stops flooding, multicast VLAN, fast leave, and DSCP/QoS queues — the things that decide whether IPTV is watchable and whether Dante audio drops out.

Are you running IGMP snooping plus a querier, or still flooding the VLAN?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424DGGPM-440W evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

Either way, no follow-up sequence from me.

Best,
[your name]
```

> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；③ 落款换成你自己的名字与公司；④ 一次只问一个问题。

## 十一、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
