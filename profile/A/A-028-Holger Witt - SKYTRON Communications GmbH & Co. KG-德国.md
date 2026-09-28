# Holger Witt / SKYTRON Communications GmbH & Co. KG

> **评级 A**　|　德国 · Karlsbad　|　档案编号 `A-028`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（光纤接入），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | SKYTRON Communications GmbH & Co. KG |
| 国家 | 德国 |
| 城市 | Karlsbad |
| 网站 | skytron.business |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCUME+MTCINE+MTCIPv6E+MTCSE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维，会自己采购设备 → 用 ERPS/IGMP/VLAN/CLI 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | WISP/运营商：自建骨干网、BGP/OSPF/MPLS-VPLS、光纤与微波回传、公共 WiFi、IPv6/IoT/LoRaWAN → 最对口 |

## 三、人员与联系方式

- **对接人**：Holger Witt
- **邮箱**：h.witt@skytron.de
- **电话**：+49 7248 4528-130
- **原始联系字段**：+49 7248 4528-130 / h.witt@skytron.de

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCTCE、MTCUME、MTCINE、MTCIPv6E、MTCSE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCTCE` — 流量控制
- `MTCUME` — 用户管理（Hotspot / PPPoE）
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：光纤接入 / FTTH

### 推什么型号

**LT-S8328XG-4XS24GT-S（24×千兆 + 4×万兆 SFP+）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

4×10G SFP+ 上行、QinQ 做用户隔离、端口隔离、组播、广播风暴抑制

### 怎么开发

问「OLT 下面挂多少用户？每用户怎么隔离？上行带宽怎么收敛？」——他们是按端口数买设备的，算单端口成本最有效

### 风险点

户外机柜场景要确认温度和防雷等级；运营商类客户可能要求入网许可或本地认证，先问清楚再报价

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：SKYTRON Communications GmbH & Co. KG（2000 年成立的微波/无线电先驱，现为全栈电信服务商）：自建基础设施，做企业互联网、WLAN、电话、IT 安全、云/数据中心与 IoT/LoRaWAN。
- **产品线与在售品牌**：自建 Richtfunk/Glasfaser/VDSL 接入与自有网络；方案页明列 **managed Switchen** 与 Enterprise WLAN、视频监控；未公开具体品牌。
- **目标行业与场景**：企业多点组网（Standortvernetzung）、园区/停车场监控（Campus-Vernetzung）、城市公共 WiFi 与活动 WiFi、高可用（微波做冗余链路、SD-WAN 多线捆绑）、工业 IoT。
- **团队与规模**：中型区域服务商（团队含多领域专家，Karlsbad 基地，服务德国西南部），决策链为技术负责人。
- **决策链与对接人**：Holger Witt（h.witt@skytron.de；+49 7248 4528-130），持 10 证含 MTCEWE。
- **技术与认证**：MTCNA+MTCRE+MTCWE+MTCTCE+MTCUME+MTCINE+MTCIPv6E+MTCSE+MTCEWE（10 证）——从路由到企业无线全覆盖。
- **采购与供应链信号**：自建网络 + 客户项目双线采购：网内设备按运营商标准选（稳定性/备件），客户项目按方案选（要能写进标书）。
- **近期动态与线索**：官网 2026 年在线：把微波定位为「介质冗余」（与光纤并行）并推 SD-WAN 捆绑；新增 LoRaWAN/IoT 板块与可视化 Dashboard。
- **与我方契合点**：客户侧「managed Switchen + Enterprise WLAN + 视频监控」就是 24 口 PoE 与工业款的场景；网内侧塔站/机箱需要宽温工业设备；高可用话术直接对上 ERPS。
- **风险与注意**：他对链路冗余要求高：任何冗余参数都要有实测数据（切换时间、丢包），不能只给规格表。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【产品线与在售品牌】**能力页明确写 WLAN & Netzwerk 含托管交换机、企业无线、公共/活动 WiFi 与视频监控。
  > WLAN & Netzwerk — Von managed Switchen bis hin zu zuverlässigem Enterprise WLAN bieten wir maßgeschneiderte Lösungen. Unser Angebot umfasst auch öffentliches WLAN für Städte, Event-WLAN für Veranstaltungen und Videoüberwachungssysteme.
  > 来源：https://skytron.business/
- **【业务定位】**公司沿革与自有基础设施（2000 年起的微波先驱）。
  > Wir sind ein Unternehmen, das im Jahr 2000 als Richtfunk-Pioniere gestartet ist … Unsere Kunden profitieren davon, dass wir unsere eigene Infrastruktur zur Privat- und Firmenkundenanbindung betreiben
  > 来源：https://skytron.business/
- **【目标行业与场景】**高可用叙事：微波做介质冗余 / SD-WAN 多线捆绑。
  > In der Kundenpraxis dient Richtfunk als hochwertige Medienredundanz, die parallel zu anderen Leitungen wie Glasfaser eingesetzt wird … Alternativ bieten wir Backup-Lösungen über SD-WAN an, die mehrere Internetanschlüsse bündeln
  > 来源：https://skytron.business/
- **【目标行业与场景】**园区/多点组网与监控场景。
  > Wir bieten die ideale Lösung für die Vernetzung Ihrer Unternehmensstandorte. Darüber hinaus ermöglichen wir auch Campus-Vernetzungen, beispielsweise für die Überwachung des Firmenparkplatzes.
  > 来源：https://skytron.business/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：客户侧「托管交换机 + 企业 WLAN + 视频监控」打包：24 口 PoE++ 一台覆盖一层/一栋，讲整机功率预算与看门狗（减少上门）。
- **要问的问题**：他们的企业客户项目里，接入层交换机现在谁供货？
- **随附证明**：功率实测 + 与 CRS328-24P/UniFi 同规格对照 + 测试机。

### 第 2 次跟进 · 工业级非管理 PoE（塔站/室外箱）

- **推什么**：LT-IS6310G-2GX8GT PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：自建网塔站与室外箱：宽温宽压、DIN、免配置；他们自己就是运营商，最懂现场故障成本。
- **要问的问题**：塔站/室外箱设备现在用什么、坏得最多的是哪一类？
- **随附证明**：宽温/宽压报告 + 双电源 + 备件政策。

### 第 3 次跟进 · 管理型 PoE（冗余与高可用）

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他卖「介质冗余」：给他 ERPS/环网切换实测数据与 VLAN/QoS 模板，把我们的交换机写进他高可用方案的设备清单。
- **要问的问题**：他们的冗余方案里，接入层交换机要不要支持 ERPS？切换指标多少？
- **随附证明**：ERPS 切换实测（丢包/恢复时间）+ VLAN/QoS 模板 + 招标参数条目。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：Per-subscriber isolation on your FTTH build

```text
Hi Holger,

I build access switches for FTTH and fixed wireless — per-subscriber isolation and uplink aggregation are the whole job.

What caught my eye is that you work on WISP.

Where we may be useful: 4×10G SFP+ uplink, QinQ per subscriber, port isolation, broadcast storm control, IGMP for IPTV.

How are you isolating subscribers now — QinQ per user, or something simpler?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328XGP-4XS24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
