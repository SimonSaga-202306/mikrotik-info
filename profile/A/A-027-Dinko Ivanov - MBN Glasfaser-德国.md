# Dinko Ivanov / MBN Glasfaser

> **评级 A**　|　德国 · Westhofen　|　档案编号 `A-027`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（光纤接入），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | MBN Glasfaser |
| 国家 | 德国 |
| 城市 | Westhofen |
| 网站 | mbn-glasfaser.de |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCSE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGM（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 光纤接入 ISP（公司名带 Glasfaser）→ FTTH 项目需要接入层交换机 |

## 三、人员与联系方式

- **对接人**：Dinko Ivanov
- **邮箱**：dinko.ivanov@mbn-glasfaser.de
- **电话**：+49 6344 9442084
- **原始联系字段**：+49 6344 9442084 / dinko.ivanov@mbn-glasfaser.de

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCSE` — 安全

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：光纤接入 / FTTH

### 推什么型号

**STC-424XGGM（Saga）（24×千兆 + 4×万兆 SFP+）**

> 系统初判型号：`STC-424XGGM（Saga）`（供参考，以实际沟通为准）

### 核心卖点

4×10G SFP+ 上行、QinQ 做用户隔离、端口隔离、组播、广播风暴抑制

### 怎么开发

问「OLT 下面挂多少用户？每用户怎么隔离？上行带宽怎么收敛？」——他们是按端口数买设备的，算单端口成本最有效

### 风险点

户外机柜场景要确认温度和防雷等级；运营商类客户可能要求入网许可或本地认证，先问清楚再报价

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：Mobile Breitbandnetze GmbH（MBN）：自建「光纤-微波混合」网络并以 ISP/网络运营商身份卖宽带，重点是农村地区覆盖；同时是公共热点运营商。
- **产品线与在售品牌**：自建基础设施（FTTT 光纤到塔 + 微波到户），未公开设备品牌；RIPE 组织 ORG-MBG9-RIPE。
- **目标行业与场景**：农村宽带（居民/村镇）、市政补贴宽带项目、公共热点（政府/城市 WiFi）、企业专线。
- **团队与规模**：中小型运营商（「seit 18 Jahren auf dem Markt」），决策链短，技术负责人 Dinko Ivanov 持多证。
- **决策链与对接人**：Dinko Ivanov（dinko.ivanov@mbn-glasfaser.de）；+49 6344 9442084。
- **技术与认证**：MikroTik 认证顾问（MTCNA+MTCSE）——路由与安全为主，交换设备外购。
- **采购与供应链信号**：运营商自建 = 设备进他们的网（长期资产）：看重 MTBF、宽温、远程管理、备件速度；一次选型长期复购。
- **近期动态与线索**：官网 2026 年在线：主打「光纤-微波混合」把 10 Gbit/s 送到 50 m–10 km 的任意距离、市政补贴项目无需大规模土木工程。
- **与我方契合点**：FTTT 到户的接入层 + PoP/机箱 + 塔站设备全是我们的场景；24 口 PoE 用于 PoP/节点，工业款用于塔站与室外箱，管理型用于回传环。
- **风险与注意**：运营商采购看长期稳定性与备件（他不是一次性买卖）；先小批量试点跑稳定性和 RMA 响应速度。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**公司自述：光纤网络与无线网络基础设施的承建者、网络运营商与 ISP，聚焦农村宽带。
  > Mobile Breitbandnetze GmbH (kurz MBN) ist Ersteller von Funknetz-Infrastruktur und Glasfasernetzen, sowie Netzbetreiber und Internet Provider. Unser Schwerpunkt liegt in der Breitbandversorgung im ländlichen Raum.
  > 来源：https://mbn-glasfaser.de/
- **【目标行业与场景】**FTTT + 微波混合架构的技术参数（距离与带宽）。
  > Die Anbindung erfolgt über eine Glasfaser-/Richtfunk-Hybridinfrastruktur: Zunächst wird der Standort per Fiber-to-the-Tower (FTTT) bis zur Richtfunkantenne angebunden. Von dort führt die Richtfunkstrecke direkt zum Zielstandort … Breitband bis zu 10 Gigabit pro Sekunde über Entfernungen zwischen 50 Metern und 10 Kilometern
  > 来源：https://mbn-glasfaser.de/
- **【近期动态与线索】**市政补贴项目是他们的增长点（快速落地、无需大规模土建）。
  > Kommunenausbau mit förderfähigem EU-Internet-Breitbandzugang über Glasfaser-Richtfunk-Hybrid-Technologie … Schnelle Realisierbarkeit der Breitbanderschließung (wenige Monate statt Jahre)
  > 来源：https://mbn-glasfaser.de/
- **【团队与规模】**运营商身份（RIPE 组织对象）与市场年限。
  > seit 18 Jahren auf dem Markt；RIPE lookup: ORG-MBG9-RIPE（官网页脚链接）
  > 来源：https://mbn-glasfaser.de/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：PoP/节点机柜：一台 24 口 PoE++ 同时喂热点 AP、监控与客户接入；重点给整机功率预算与长期稳定性（MTBF/温升）。
- **要问的问题**：他的 PoP/节点现在用什么交换机、单点多少用户？
- **随附证明**：功率实测 + 长稳测试建议 + 备件/RMA 政策。

### 第 2 次跟进 · 工业级非管理 PoE（塔站/室外箱）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：塔站与室外箱：宽温宽压、DIN、免配置；配合他们的 FTTT 架构做「现场盒」。
- **要问的问题**：塔站/室外箱的供电与温度条件如何？
- **随附证明**：宽温报告 + 双电源接线图 + SFP 兼容清单。

### 第 3 次跟进 · 管理型 PoE（回传环与 QoS）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：多节点回传要环网与 QoS：ERPS + VLAN/QinQ + 端口限速，按运营商话术谈。
- **要问的问题**：回传网要不要做环网冗余与用户隔离？
- **随附证明**：ERPS 实测 + QinQ 模板 + SNMP 监控清单。

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
Hi Dinko,

I build access switches for FTTH and fixed wireless — per-subscriber isolation and uplink aggregation are the whole job.

What caught my eye is that you work on FTTH.

Where we may be useful: 4×10G SFP+ uplink, QinQ per subscriber, port isolation, broadcast storm control, IGMP for IPTV.

How are you isolating subscribers now — QinQ per user, or something simpler?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424XGGM evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
