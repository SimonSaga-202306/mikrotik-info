# PF Tech

> **评级 A**　|　意大利 · Favria / Cuorgnè　|　档案编号 `A-042`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（PoE/监控/门禁），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | PF Tech |
| 国家 | 意大利 |
| 城市 | Favria / Cuorgnè |
| 网站 | pftech.it |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCSE（公司内 3 人） |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | 公司内 3 位 MikroTik 顾问。Paolo：静态路由与 OSPF、防火墙安全、网络设计、全系列 VPN 隧道（IPsec/PPPoE/L2TP/PPTP/SSTP/oVPN/EoIP/IPIP）、CHR over Proxmox/KVM、虚拟化 |

## 三、人员与联系方式

- **邮箱**：info@pftech.it、stefano.c@pftech.it、stefano@pftech.it
- **电话**：+39 0124 576161
- **原始联系字段**：Paolo Vacca +39 0124 576161 / info@pftech.it；Stefano Callegari stefano.c@pftech.it；Stefano Vallosio stefano@pftech.it

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCSE` — 安全

**涉及品牌 / 技术**：IPsec、MikroTik、Proxmox

## 五、跟进策略

**场景判断**：PoE / 监控 / 门禁

### 推什么型号

**LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

802.3bt 单口 90W、**PoE 看门狗（摄像头死机自动断电重启，省一趟上门）**、250m 延长供电、端口隔离、整机功率预算足

### 怎么开发

替他算一笔账：24 个 4K 头全开要多少瓦、满配后还剩多少余量——这是每个做监控的人都踩过的坑，算清楚就赢一半

### 风险点

**PoE 功率预算和供电稳定性是验收红线**，虚标功率会当场翻车；必须送测、必须给整机功率实测数；部分非标 PoE 相机存在兼容性问题，要先拿他的机型测

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。

- **业务定位**：都灵省 Favria 的 IT 综合服务商：硬件/软件分销 + 系统集成 + ROC 牌照的连接运营，覆盖本地到大企业客户。
- **产品线与在售品牌**：IT 软硬件全线分销（未列限牌），以太网/光纤/无线、点对点无线回传、视频监控、云话机、VPS/备份。
- **目标行业与场景**：公私视频监控、局域网改造、酒店与公共设施连接——PoE 交换机是其视频监控线的底座。
- **团队与规模**：公司内 3 位 MikroTik 认证顾问；Paolo Vacca（静态路由/OSPF/VPN/防火墙）与 Stefano Callegari 两条技术线；Favria+Cuorgnè 两址。
- **决策链与对接人**：Paolo Vacca（+39 0124 576161 / info@pftech.it），公司级 Srl 但规模小、决策快。
- **技术与认证**：3 名 MikroTik 顾问，MTCNA+MTCRE+MTCSE（来源：CSV 既有记录）；技术对话零门槛。
- **采购与供应链信号**：自述做分销 → 他既买设备自用也转售；进他的货盘=多一条微型分销腿。
- **近期动态与线索**：网站改版中；ROC 运营商身份意味着他对设备价格/批量条款敏感。
- **与我方契合点**：视频监控线 = 24 口 PoE++ 直接命中；他卖硬件 = 上架机会；顾问身份 = 看得懂完整规格对比。
- **风险与注意**：既是集成商又是（潜在）分销商，首轮别把他当纯中间商压价，以「自用+试点客户」双轨开场。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**PF Technology Srl：面向企业/个人/公共机构的 360° IT 方案商，自述含硬件与软件的分销（既有经销属性）。
  > PF Tech si occupa di distribuire prodotti informatici hardware e software, oltre a tutti i servizi e soluzioni ad essi correlati, con una platea di riferimento che va dall’utenza domestica alla grande azienda.
  > 来源：https://www.pftech.it/
- **【目标行业与场景】**「Impianti Tecnologici」板块明示：以太网/光纤/无线局域网 + 点对点无线 + 广域网 + 公私视频监控——监控供电链路明确。
  > Ci occupiamo di impianti tecnologici e di videosorveglianza privata e pubblica, sfruttando le più recenti tecnologie disponibili sul mercato.
  > 来源：https://www.pftech.it/
- **【采购与供应链信号】**持 ROC（意大利通信运营商登记）资质，可向全国提供连接服务——同时做设备与承载服务，项目型采购。
  > PF Tech è Operatore autorizzato ROC per poter erogare, su tutto il territorio nazionale, servizi di connettività internet, linee telefoniche voce tradizionali e VoIP con centrali Cloud
  > 来源：https://www.pftech.it/
- **【近期动态与线索】**官网首页挂着「SITE UNDER COSTRUCTION」——改版窗口期，供应商重选可能性上升。
  > SITE UNDER COSTRUCTION — PF Tech è il partner ideale per chi vuole cambiare il modo di connettersi.
  > 来源：https://www.pftech.it/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 PoE++（视频监控交付）

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他们家的视频监控业务：监控/门禁/AP 一项目 24 口 PoE++，功率预算与看门狗写进他的交付清单，再给一张和 CRS328/UniFi 的同规格对照页。
- **要问的问题**：监控项目的供电交换机现在用谁、单台供电预算如何核算？
- **随附证明**：功率实测表 + 看门狗演示视频 + 对照页（英文）。

### 第 2 次跟进 · 工业非管理 PoE（户外/弱电间）

- **推什么**：LT-IS6310G-2GX8GT PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：点对点回传与户外监控点位：宽温宽压、DIN、免配置，替他省掉市电改造与风扇故障。
- **要问的问题**：山区/户外监控点位现在怎么供电、换机成本多大？
- **随附证明**：宽温报告 + DIN 安装图 + 一台测试机。

### 第 3 次跟进 · 管理型 + 试销上架

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他自己分销硬件：第三路直接谈上架——管理型 10G 款做他产品线里「有 10G 又不贵」的那格，小批量备货试销。
- **要问的问题**：对应价格档次定多少、试点客户选哪几个项目？
- **随附证明**：VLAN/ERPS 实测 + 试销价格单（英文）+ 供货承诺函。

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
Hi PF,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on IPsec.

Where we may be useful: 24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.

How many cameras per job, and what wattage per port are you designing to?

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
