# Paweł Wandas / SAFES

> **评级 A**　|　波兰 · Kraków　|　档案编号 `A-051`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | SAFES |
| 国家 | 波兰 |
| 城市 | Kraków |
| 网站 | safes.pl |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE+MTCSWE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | 防火墙/VPN/隧道/负载均衡/故障切换/QoS/高级路由/无线；熟 The Dude 网管 → 对 SNMP/MIB/NMS 集成有感觉 |

## 三、人员与联系方式

- **对接人**：Paweł Wandas
- **邮箱**：biuro@safes.pl
- **电话**：+48 412 412 324
- **原始联系字段**：+48 412 412 324 / biuro@safes.pl

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

**涉及品牌 / 技术**：MikroTik、The Dude

## 五、跟进策略

**场景判断**：MTCSWE 交换认证

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

他持有 MTCSWE（MikroTik 交换认证），交换是正式专长——**不用给他做科普**。开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」直接给 CLI 命令对比和转发实测数据

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全；含糊其辞会立刻失去这类技术型客户的信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。

- **业务定位**：Kraków 的托管 IT/网络安全服务商，面向酒店与高级物业，LAN/Zero Trust 话术清晰；工程侧做 LAN/WAN/Wi-Fi 代维。
- **产品线与在售品牌**：按项目选型（MikroTik 栈为主，顾问 Paweł Wandas 墙上全证）。
- **目标行业与场景**：酒店、商业楼宇、高级物业的全年无休设备托管——PoE 交换机是典型运维包里的硬件。
- **团队与规模**：服务/SOC 支持团队制，但决策集中。
- **决策链与对接人**：Paweł Wandas（+48 412 412 324 / biuro@safes.pl）。
- **技术与认证**：公司顾问墙上顾问持 MTCNA 至 MTCEWE/MTCSWE 全证（来源：CSV 既有 MikroTik 名录记录）；熟 The Dude/SNMP 运维文化，能看懂 SNMP/MIB 与资产发现类参数。
- **采购与供应链信号**：7×24 服务包模式：备件/换机库存是硬指标——「备用库存+快速热换」正是他们的购买逻辑。
- **近期动态与线索**：官网主打 SOC/Zero Trust 话术——客户项目多要求 VLAN 分段/802.1X，管理型 PoE 能写进他的托管方案。
- **与我方契合点**：酒店项目 PoE 运维、SOC 管理面安全、SNMP 细节——直接命中管理型；备件模式适合他的 7×24 运维。
- **风险与注意**：运维商对供货连续与更换件仓库敏感：讲备件比讲便宜更能成单。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**SAFES 自述：20 年为波兰与海外的高级物业/场馆做托管 IT 与网络安全，7×24。
  > Przejmujemy pełną odpowiedzialność za systemy IT… Od 20 lat obsługujemy obiekty premium w Polsce i za granicą – w trybie non-stop.
  > 来源：https://safes.pl/
- **【目标行业与场景】**基础设施服务项明确 LAN/WAN/Wi‑Fi 网络、服务器/虚拟化、高可用——托管型服务即其接口。
  > Infrastruktura IT… Sieci LAN/WAN/Wi-Fi · Serwery i wirtualizacja · Wysoka dostępność
  > 来源：https://safes.pl/
- **【技术与认证】**明确 SOC 与 Zero Trust 架构语言——安全分层是他给客户的答案。
  > Security Operations Center · Architektura Zero Trust · Ochrona PMS
  > 来源：https://safes.pl/
- **【产品线与在售品牌】**另有 enova365 ERP 的授权实施线（商业软件+网络安全+托管 IT 混合的工程有限公司）。
  > Autoryzowany Partner enova365
  > 来源：https://safes.pl/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 PoE++（托管酒店/物业项目替换件）

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：托管 7×24 模式：换件仓库的逻辑——24 口 PoE++ 拿来做他的备用库存 + 项目替换机，性价比立现。
- **要问的问题**：替换件仓库现用哪个系列、备机放几台？
- **随附证明**：功率实测 + SNMP/MIB 明细 + 英文对照页。

### 第 2 次跟进 · 工业非管理 PoE（楼层/天花/室外点位）

- **推什么**：LT-IS6310G-2GX8GT PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：运维商最怕的楼层吊顶/地下机槽点位：宽温宽压、免配置，坏了一台热换。
- **要问的问题**：楼层/室外小型节点一年换几台、上门成本多大？
- **随附证明**：宽温报告 + DIN 安装图 + 单机热换说明。

### 第 3 次跟进 · 管理型 + Zero Trust/VLAN 托管包

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：与 SOC/Zero Trust 话术对齐：管理型 VLAN 分段+SNMP 明细+ACL，写进他的托管方案里能涨服务费。
- **要问的问题**：客户托管包里 802.1X/VLAN 分段你们怎么卖、谁交付？
- **随附证明**：VLAN/ERPS/ACL 配置模板 + SNMP 对接说明 + ERPS 收敛实测。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：Switching question for an MTCSWE holder

```text
Hi Paweł,

You hold MTCSWE, so switching is a declared specialism rather than a side task — that is who I want to talk to.

What caught my eye is that you work on The Dude.

Where we may be useful: L3 hardware offload (line-rate forwarding off the CPU), QinQ and VLAN translation, ERPS and MSTP, ACLs and static routing, full CLI plus SSH plus SNMP with a private MIB.

What are you using for L2 redundancy today, and does it need ERPS-class convergence?

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
