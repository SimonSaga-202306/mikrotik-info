# Carlos Otin / Hotelinking

> **评级 A**　|　西班牙 · Palma（马略卡）　|　档案编号 `A-067`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长、酒店/多住户、光纤接入），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Hotelinking |
| 国家 | 西班牙 |
| 城市 | Palma（马略卡） |
| 网站 | hotelinking.com |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCSE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328GP-4GX24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 高级网络工程师，专注**酒店 hospitality 与多站点 multi-site** 可扩展网络；专长 MikroTik 路由 + **交换 switching** + 无线 + **GPON 集成**；做网络审计、复杂故障排查、配置标准化、对接监控与自动化平台 → 酒店多站点 = PoE 接入交换机批量需求 |

## 三、人员与联系方式

- **对接人**：Carlos Otin
- **邮箱**：c.otin@hotelinking.com
- **电话**：+34 691 837 651
- **原始联系字段**：+34 691 837 651 / c.otin@hotelinking.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCSE` — 安全

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：酒店 / 多住户

### 推什么型号

**LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`LT-S8328GP-4GX24GT-S`（供参考，以实际沟通为准）

### 核心卖点

客房 VLAN 隔离、端口隔离（防客人私接路由器）、PoE 同时供 AP / IPTV 机顶盒 / IP 话机、组播 IPTV 不卡

### 怎么开发

问「一间客房下几根线？AP 怎么供电？IPTV 走不走组播？」——酒店是多期项目，一期做进去后面几期跟着走

### 风险点

酒店项目周期长且受装修进度牵制，别押季度指标；采购决定权常在弱电总包而非业主，要找到总包；客房网络出问题客人直接投诉，稳定性零容忍

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。

- **业务定位**：马略卡酒店科技平台（非传统集成商）：CRM（GuestMaker）+ 酒店网络运营（WiFiBot）+ 前台数字化（DeskForce）三件套，按平台费模式收费。
- **产品线与在售品牌**：软件平台+托管网络服务；网络硬件「厂商无关」=他们替酒店全国选型，交换机是 WiFiBot 交付的底层耗材。
- **目标行业与场景**：西班牙连锁酒店集团（60% 渗透率）：客房/公区 Wi-Fi、前台数字化、酒店网络安全合规——AP/IPTV/话机密集的 PoE 场景。
- **团队与规模**：平台公司编制（Palma 总部），NOC 团队 24/7 运营 1000+ 酒店网络；Carlos Otin 为高级网络工程师（MikroTik 路由+交换+无线+GPON）。
- **决策链与对接人**：技术侧 Carlos Otin（+34 691 837 651 / c.otin@hotelinking.com）；平台公司采购走技术背书包。
- **技术与认证**：MTCNA+MTCSE（CSV 名录记录）；团队管着千家酒店的异构网络，交换分段/客人网隔离是日常。
- **采购与供应链信号**：千家酒店网络的扩容与翻新=持续性硬件需求；「厂商无关」意味着能以规格/价格进标准件清单。
- **近期动态与线索**：平台在高速扩张（集成数 120+、渗透率 60%），每条新签约酒店都要铺网络——硬件需求跟着平台增长。
- **与我方契合点**：酒店楼层接入=24 口 PoE++；公区/户外点位=工业件；客人网/员工网/IoT 三层分段=管理型标准模板；量级=平台级。
- **风险与注意**：平台公司对供应商稳定性/质保/备件要求高：首轮给全质保与备件政策；别用「便宜」开场，用「TCR 总成本」。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**酒店科技平台：1000+ 酒店与连锁在用，西班牙连锁酒店渗透率 60%。
  > +1.000 hoteles y cadenas ya confían en Hotelinking · 60% de penetración en cadenas hoteleras en España
  > 来源：https://www.hotelinking.com/
- **【产品线与在售品牌】**WiFiBot 产品线=酒店网络 24/7 监控+NOC 托管+集中控制，并强调「与厂商无关」——网络硬件采购话语权在他们手里。
  > WiFiBot: plataforma de operación y seguridad de redes para hoteles · Monitorización de Redes 24/7 … servicios expertos de NOC · Unifica infraestructuras diversas con soluciones independientes de proveedores y sistemas de control escalables.
  > 来源：https://www.hotelinking.com/
- **【团队与规模】**平台数据：1000 万+注册住客、为酒店省下 3000 万+ OTA 佣金、120+ 个 PMS/预订引擎/CRM 集成——平台体量可观。
  > +10M de huéspedes registrados y activados para marketing directo · +30 M en comisiones ahorradas · +120 integraciones activas con PMS, motores de reserva y CRM
  > 来源：https://www.hotelinking.com/
- **【目标行业与场景】**客户墙全是西班牙大型连锁酒店集团：RIU、Zafiro、Best Hotels、Bluesea、Coral、Grupotel。
  > RIU · Zafiro Hotels · Best Hotels · Bluesea · Coral Hotels · Grupotel（客户墙 Logo）
  > 来源：https://www.hotelinking.com/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（酒店楼层接入层）

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：酒店一层楼的 AP+IPTV+话机+监控一张网：24 口 PoE++ + 4×10G 上行，按「每层一台」给他算总拥有成本。
- **要问的问题**：WiFiBot 交付的酒店楼层接入换型时，哪段成本最头疼？
- **随附证明**：每层一台的 BBOM 测算 + 规格对照（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（公区/户外/机电间点位）

- **推什么**：LT-IS6306G-2GX4GT PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：酒店泳池/露台/停车场/机电间的零散点位：宽温 DIN 免配置 4 口小机，NOC 远程看不出差别、现场免调试。
- **要问的问题**：公区零散点位现在用什么型号？坏机率高不高？
- **随附证明**：宽温报告 + 备件包价 + 免配置说明。

### 第 3 次跟进 · 管理型 PoE（客人网/员工网分段标准件）

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：WiFiBot「厂商无关」标准件清单加一个候选：VLAN 三层分段+ERPS 冗余的接入层模板，整套交付文档英文齐套。
- **要问的问题**：标准件清单评审周期是多久？我们可以走一次技术评估。
- **随附证明**：VLAN/ERPS 模板 + 实测 + 质保/备件政策（英文）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：PoE + VLAN per room — question on your hotel jobs

```text
Hi Carlos,

I build PoE access switches for hotel and multi-dwelling networks, which is where you seem to spend most of your time.

What caught my eye is that you work on hospitality, GPON and switching.

Where we may be useful: 24 gigabit PoE++ ports (APs, IP phones and IPTV boxes on one cable), per-room VLAN isolation, port isolation to stop guests plugging in their own router, IGMP snooping for the TV.

How many drops per room, and is your IPTV running on multicast?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328GP-4GX24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
