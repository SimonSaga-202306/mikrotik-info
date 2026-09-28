# Kehrlein（MikroTik 认证顾问）

> **评级 A**　|　德国 · München　|　档案编号 `A-029`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（PoE/监控/门禁），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Kehrlein（MikroTik 认证顾问） |
| 国家 | 德国 |
| 城市 | München |
| 网站 | kehrlein.de |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCRE 等 |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XG-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维，会自己采购设备 → 用 ERPS/IGMP/VLAN/CLI 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 |  München；技能含 VPN/IPsec/L2TP/OpenVPN/PPPoE/IPv6/无线/CAPsMAN/QoS/HA/负载均衡/数据中心 |

## 三、人员与联系方式

- **邮箱**：info@kehrlein.de
- **电话**：+49 89 69387111
- **原始联系字段**：+49 89 69387111 / info@kehrlein.de

## 四、品牌与技术栈

**持有认证**：MTCRE

- `MTCRE` — 路由

**涉及品牌 / 技术**：CAPsMAN、IPsec、MikroTik

## 五、跟进策略

**场景判断**：PoE / 监控 / 门禁

### 推什么型号

**LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`LT-S8328XG-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

802.3bt 单口 90W、**PoE 看门狗（摄像头死机自动断电重启，省一趟上门）**、250m 延长供电、端口隔离、整机功率预算足

### 怎么开发

替他算一笔账：24 个 4K 头全开要多少瓦、满配后还剩多少余量——这是每个做监控的人都踩过的坑，算清楚就赢一半

### 风险点

**PoE 功率预算和供电稳定性是验收红线**，虚标功率会当场翻车；必须送测、必须给整机功率实测数；部分非标 PoE 相机存在兼容性问题，要先拿他的机型测

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：慕尼黑（另设 Haßfurt 点位）的 IT 咨询顾问：网络与基础设施（高可用方向、全球远程+现场、24×7）、IT 管理与敏捷转型（SAFe 认证讲师）。
- **产品线与在售品牌**：MikroTik/RouterOS 专家（官网自述 Official MikroTik Consultant · Since 2007）；其余为方法论与开源/自选厂商，无代理绑定。
- **目标行业与场景**：企业网络设计/审计/高可用改造、IT 组织转型；客户遍及德语区与海外（全球远程）。
- **团队与规模**：个人顾问（+15 年管理经验，可做 interim manager），决策链 = 本人。
- **决策链与对接人**：Sandro Kehrlein（info@kehrlein.de；+49 89 69387111；另有 +49 9521 9580741）。
- **技术与认证**：MikroTik 官方顾问（2007 起），官网列 10 证：MTCNA/MTCRE/MTCWE/MTCTCE/MTCUME/MTCINE/MTCIPv6E/MTCSE/**MTCSWE**/MTCEWE；技术栈含 MPLS/VRF、VXLAN、**MLAG/VRRP**、WireGuard、CAPsMAN、自动化与监控、安全审计。
- **采购与供应链信号**：设计/审计角色 → 他能写入规格（spec-in）；本人不囤货，但项目设备清单由他出。
- **近期动态与线索**：官网 2026 年在线（英德双语），列 SAFe ASPC 等 8 项敏捷认证；提供 TeamViewer QuickSupport 远程支持入口。
- **与我方契合点**：他谈 MLAG/VRRP/ERPS 级的高可用：我们的管理型 PoE（ERPS、双上行、VLAN）正好是他设计里的接入层元件；工业款补现场点位。
- **风险与注意**：技术天花板高、只认数据：任何「支持/不支持」都要有文档或实测；不打价格战，打可验证性。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【技术与认证】**官网明列 MikroTik 官方顾问身份、10 项认证与技术栈清单。
  > Official MikroTik Consultant · Since 2007；MTCNA · MTCRE · MTCWE · MTCTCE · MTCUME · MTCINE · MTCIPv6E · MTCSE · MTCSWE · MTCEWE；Technologies: Routing (BGP, OSPF, VRF, MPLS), Firewalling, Switching, VLAN, DNS, Tunneling (GRE, EoIP, VXLAN), VPN (IPsec, L2TP, OpenVPN, WireGuard), PPPoE, Wireless & CAPsMAN, Hotspot & Captive Portals, QoS, IPv6, Load Balancing, High Availability (VRRP, MLAG), Security Audits, Monitoring, Backup, Network Automation
  > 来源：https://www.kehrlein.de/en/
- **【业务定位】**网络/基础设施咨询的定位与交付方式（24×7、远程+现场）。
  > IT consulting, IT services and support with a focus on high-availability network solutions — worldwide, remote and on-site, individually tailored and 24×7. Specialised in MikroTik and RouterOS.
  > 来源：https://www.kehrlein.de/en/
- **【目标行业与场景】**双重身份（网络顾问 + IT 管理/敏捷），可做 interim manager 与监事席位。
  > Strategic IT consulting, IT organisational development and transformation … Available as an interim manager and for advisory board and supervisory board mandates — backed by more than 15 years of leadership and management experience.
  > 来源：https://www.kehrlein.de/en/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：按他的设计口径给料：整机功率预算、逐口实测、PoE 看门狗、端口隔离；请他用自己的方法复测（他是评审型客户）。
- **要问的问题**：他设计高可用接入层时，PoE 交换机的硬门槛是什么？
- **随附证明**：测试方法说明 + 实测原始数据 + 可上他测试台的样机。

### 第 2 次跟进 · 工业级非管理 PoE（现场点位）

- **推什么**：LT-IS6310G-2GX8GT PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：给客户设计时总有非机房点位；宽温 DIN 免配置，减少设计复杂度与维护面。
- **要问的问题**：他的方案里现场点位一般怎么做冗余与供电？
- **随附证明**：宽温/宽压报告 + 双电源设计图 + 样品。

### 第 3 次跟进 · 管理型 PoE（高可用实测）

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他讲 MLAG/VRRP/ERPS：用我们的管理型做接入层环网与双上行，给他可复现的收敛时间与丢包数据。
- **要问的问题**：他的高可用设计里，接入层环网收敛目标是多少？
- **随附证明**：ERPS 收敛实测 + 双上行拓扑验证 + CLI/MIB 文档。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：PoE budget question on your camera jobs

```text
Hi Kehrlein（MikroTik,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on IPsec and CAPsMAN.

Where we may be useful: 24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.

How many cameras per job, and what wattage per port are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328XG-4XS24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
