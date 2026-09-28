# Charalampos Marinakis / SystemCon

> **评级 A**　|　希腊 · Heraklion（克里特）　|　档案编号 `A-021`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | SystemCon |
| 国家 | 希腊 |
| 城市 | Heraklion（克里特） |
| 网站 | systemcon.gr |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCINE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328GP-4GX24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 公司**同时交付硬件与软件网络系统**（从小型企业到企业级），并提供安装/配置/支持/管理的认证专业服务；核心服务：网络设计、**Routing、Switching**、防火墙安全、HotSpot 与用户管理、VPN、负载均衡与故障切换、高可用、流量整形与 QoS、无线、**SLA 支持服务** |

## 三、人员与联系方式

- **对接人**：Charalampos Marinakis
- **邮箱**：info@systemcon.gr
- **电话**：+30 281 121 7219
- **原始联系字段**：+30 281 121 7219 / info@systemcon.gr

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCINE

- `MTCNA` — 网络助理（入门）
- `MTCINE` — ISP 互联

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328GP-4GX24GT-S`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：克里特岛的综合 IT 服务商（SystemCon）：企业智能 BI、ERP、系统基础设施与云，官网自述「Complete IT Business Solutions」。
- **产品线与在售品牌**：品牌墙含 MikroTik、Ubiquiti、Fortinet、Huawei Enterprise、Alcatel、Dell、Lenovo、Synology、Yeastar——网络设备以 MikroTik + Ubiquiti 为主，安全用 Fortinet。
- **目标行业与场景**：中小企业到企业级客户的基础设施建设：服务器/虚拟化、备份与容灾、网络优化、高可用、云迁移。
- **团队与规模**：克里特本地团队（站点为 Elementor 模板、部分文案仍是占位文本 → 正在改版），决策链短。
- **决策链与对接人**：Charalampos Marinakis（持 MTCNA+MTCINE）；info@systemcon.gr；+30 281 121 7219。
- **技术与认证**：MikroTik 认证顾问（MTCNA+MTCINE）；官网把「Routing/Switching、防火墙、Hotspot、VPN、负载均衡与故障切换、QoS」列为核心能力。
- **采购与供应链信号**：项目型采购（服务器+网络+云打包）；同时卖 MikroTik 与 Ubiquiti，说明他对「第三条补充线」不排斥，只要规格与价格说得清。
- **近期动态与线索**：官网 2025–2026 年持续更新（含 Fortinet/Huawei Enterprise 伙伴徽标），站点部分区块仍是模板占位文本——正在扩张服务目录。
- **与我方契合点**：他做基础设施整体交付：24 口 PoE（监控/AP/门禁）、工业款（机房外点位）与管理型（VLAN/冗余）都是他每单都会遇到的接入层；对 MikroTik 生态熟，参数对话成本低。
- **风险与注意**：站点改版未完成，别把占位文案当业务事实；Fortinet/Huawei 是既有关系方，谈接入层硬件不与其冲突。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**官网首页定位：综合 IT 业务方案（BI/ERP/基础设施）。
  > Complete IT Business Solutions — Tailored IT services to meet your organization's unique needs.；Our expertise spans Business Intelligence, Enterprise Resource Planning, Systems Infrastructure, and more
  > 来源：https://systemcon.gr/
- **【产品线与在售品牌】**品牌墙含 MikroTik、Ubiquiti、Fortinet、Huawei Enterprise、Alcatel、Dell、Lenovo、Synology、Yeastar。
  > （首页品牌徽标：microsoft-partner｜aws｜epsilonnet｜fortinet_partner｜huawei_enterprise_partner｜ubiquiti｜alcatel｜mikrotik｜dell｜lenovo｜yeastar｜synology）
  > 来源：https://systemcon.gr/
- **【技术与认证】**系统基础设施能力项明确列出网络优化、高可用、备份与容灾。
  > Systems Infrastructure — Robust Security｜High Availability｜Cloud Solutions｜Backup and Disaster Recovery｜Network Optimization
  > 来源：https://systemcon.gr/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：按他「基础设施整体交付」的语境切入：监控/AP/门禁一次上 24 口 PoE++，把整机功率预算与看门狗写进他的交付清单，替代同档 MikroTik CRS328 / UniFi 的备选位。
- **要问的问题**：他现在的接入层订单里，24 口 PoE 一般谁供货、卡在价格还是交期？
- **随附证明**：整机功率实测表 + 看门狗演示 + 与 CRS328-24P/UniFi 的同规格对照页。

### 第 2 次跟进 · 工业级非管理 PoE（机房外点位）

- **推什么**：LT-IS6310G-2GX8GT PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他做酒店、工厂、园区类客户时总有非机房点位：宽温宽压、DIN、免配置，坏了整机换。
- **要问的问题**：有没有现场弱电箱/室外点位需要工业设备？
- **随附证明**：宽温报告 + DIN 安装图 + 一台测试机。

### 第 3 次跟进 · 管理型 PoE（VLAN/冗余进方案）

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他讲高可用与网络优化：VLAN 分段 + ERPS 环网 + 10G 上行的标准模板，让他的方案书多一点可写的东西。
- **要问的问题**：他的项目里监控/办公/门禁网段是分开的吗？
- **随附证明**：VLAN 模板 + ERPS 实测 + 招标可用参数条目。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：L3 hardware offload + QinQ on access switching

```text
Hi Charalampos,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on switching.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

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
