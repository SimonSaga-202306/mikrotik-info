# Wojciech Mańka / Mikrotikon

> **评级 A**　|　波兰 · Czerwionka-Leszczyny　|　档案编号 `A-061`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Mikrotikon |
| 国家 | 波兰 |
| 城市 | Czerwionka-Leszczyny |
| 网站 | mikrotikon.pl |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE+MTCSWE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-488XGGPM（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | VPN/无线/防火墙/网络安全；小企业到运营商级方案 |

## 三、人员与联系方式

- **对接人**：Wojciech Mańka
- **邮箱**：kontakt@mikrotechnology.pl
- **电话**：+48 791 560 569
- **原始联系字段**：+48 791 560 569 / kontakt@mikrotechnology.pl

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCTCE、MTCINE、MTCIPv6E、MTCSE、MTCSWE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCTCE` — 流量控制
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：ISP / 骨干

### 推什么型号

**STC-424XGGM（Saga）（4×10G 上行，收敛比高）**

> 系统初判型号：`STI-488XGGPM（Saga）`（供参考，以实际沟通为准）

### 核心卖点

4×10G 上行、QinQ 用户隔离、组播、端口隔离、广播抑制、SNMP 对接现有网管

### 怎么开发

问「接入层一台带多少用户？上行怎么收敛？」；他们按端口成本算账，把单端口价格摊到每个用户给他看

### 风险点

ISP 对设备故障率极度敏感，一台炸掉就是一批投诉；要先小批量试用跑半年；备件和 RMA 响应速度要提前承诺

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。

- **业务定位**：西里西亚个体 MikroTik 顾问：企业网络配置/优化/安全/审计/托管维护，远程或上门交付，覆盖小企业到「rozbudowana infrastruktura korporacyjna」。
- **产品线与在售品牌**：配置服务（无分销目录）：MikroTik 全系 + Ubiquiti UniFi（含交换机与控制器）；自购硬件随项目走。
- **目标行业与场景**：中小企业办公网、Wi-Fi（CAPsMAN/UniFi 漫游）、站点 VPN、网络审计；评价显示服务过酒店类客户。
- **团队与规模**：1 人个体户（MikroTechnology），Google 57 评「卓越」，复购客户多——信誉是他最重要资产。
- **决策链与对接人**：Wojtek Mańka 本人（+48 791 560 569 / kontakt@mikrotechnology.pl），决策者=交付者，链路最短。
- **技术与认证**：全部 10 证（官网自述；CSV 名录同记 MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE+MTCSWE 等）。
- **采购与供应链信号**：项目制采购：每个客户现场的路由/交换/AP 由他选配——他指定什么，客户买什么。
- **近期动态与线索**：2025 年 3 月起网站改版为新模板并持续积累新评价，业务处于活跃上升期。
- **与我方契合点**：他给 UniFi 客户配交换机=价格敏感替换点；酒店/中小企业项目=24 口 PoE 一次到位；10 证人懂技术、不用教育市场。
- **风险与注意**：他兼做 UniFi——首轮别攻击 Ubiquiti，用「同规格更低成本+万兆上行实测」摆参数说话。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**官网首页自我定位：从 NAT/防火墙基础配置一直到 VPN、动态路由与 QoS 的 MikroTik 全栈配置服务，远程与上门均可。
  > Pomagam w pełnym zakresie – od podstawowych ustawień takich jak NAT i firewall, aż po zaawansowane funkcje związane z VPN, routingiem dynamicznym czy QoS.
  > 来源：https://mikrotikon.pl/
- **【产品线与在售品牌】**服务页同时配置路由器、交换机与 AP，且另设 Ubiquiti UniFi 专线——他也给客户配 UniFi 交换机，存在替换窗口。
  > Niezależnie od tego, czy chodzi o routery, switche, czy punkty dostępowe… Specjalizuję się także w konfiguracji systemów Wi-Fi Ubiquiti Unifi… pełną konfigurację punktów dostępowych, przełączników i kontrolerów Unifi.
  > 来源：https://mikrotikon.pl/
- **【技术与认证】**自述 10+ 年网络行业经验，并已拿齐全部 10 张 MikroTik 证书——含交换方向。
  > od ponad 10 lat zajmuję się branżą sieci komputerowych… zdobywając wszystkie 10 certyfikatów MikroTik.
  > 来源：https://mikrotikon.pl/
- **【团队与规模】**个体经营实体 MikroTechnology Wojciech Mańka（工商信息齐全），Google 57 条评价、评级「卓越」，客户含酒店（Hotel Żubrówka）。
  > Dane firmy — MikroTechnology Wojciech Mańka, ul. Rybnicka 61G, 44-238 Czerwionka-Leszczyny, NIP: 6423234731, REGON: 520870419 … DOSKONAŁA Na podstawie 57 opinii.
  > 来源：https://mikrotikon.pl/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（办公/酒店项目交付款）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：顺着他的项目制交付切入：酒店/办公现场 AP+监控+话机一张网，24 口 PoE++ 配 4×10G 上行，比他常配的 UniFi 交换方案规格更高、到岸价更低。
- **要问的问题**：你最近一个用了 20+ 口 PoE 的现场，交换机用的是哪家的？
- **随附证明**：规格对照表（英文：PoE 预算/万兆口/价格）+ 整机功率实测。

### 第 2 次跟进 · 工业级非管理 PoE（现场室外/弱电间点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他常跑现场与上门：零散室外点位/车库/阁楼里，宽温 DIN 免配置款即插即用，坏了整机换——作为他工具箱常备。
- **要问的问题**：室外点位现在怎么解决？用消费级机型还是工业件？
- **随附证明**：宽温报告 + DIN 安装图 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（进他的交付模板）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：10 证的技术人：给 CLI/MIB/VLAN/ERPS 全套文档，让管理型成为他「企业客户交付模板」里的默认接入层。
- **要问的问题**：你给客户做企业网时，接入层有没有标准化型号候选？
- **随附证明**：CLI 速查 + VLAN/ERPS 模板 + MIB 库（英文）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：Access layer cost per port

```text
Hi Wojciech,

I do access switches for WISPs and small ISPs, where the number that matters is cost per subscriber port.

What caught my eye is that you work on VPN.

Where we may be useful: 4×10G uplink, QinQ subscriber isolation, port isolation, broadcast suppression, SNMP that drops into whatever NMS you already run.

How many subscribers per access switch, and what uplink ratio are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a STI-488XGGPM evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
