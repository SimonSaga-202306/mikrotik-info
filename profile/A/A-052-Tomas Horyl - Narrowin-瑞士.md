# Tomas Horyl / Narrowin

> **评级 A**　|　瑞士 · Lugano　|　档案编号 `A-052`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Narrowin |
| 国家 | 瑞士 |
| 城市 | Lugano |
| 网站 | narrowin.ch |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCSWE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328GP-4GX24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 持 MTCSWE；公司为 MikroTik 提供**网络设计、可视化 visibility 与自动化**，并自研 **network explorer 工具 + MikroTik 开源自动化平台**（narrowin.ch/en/mikrotik_lightweight_sdn.html）→ 做工具的，会看重设备的 API/可管理性；英捷意德四语 |

## 三、人员与联系方式

- **对接人**：Tomas Horyl
- **邮箱**：info@narrowin.ch
- **电话**：+41 61 511 23 30
- **原始联系字段**：info@narrowin.ch（另 +41 61 511 23 30）

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCSWE

- `MTCNA` — 网络助理（入门）
- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：MTCSWE 交换认证

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328GP-4GX24GT-S`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

他持有 MTCSWE（MikroTik 交换认证），交换是正式专长——**不用给他做科普**。开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」直接给 CLI 命令对比和转发实测数据

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全；含糊其辞会立刻失去这类技术型客户的信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。

- **业务定位**：瑞士（Basel 生态/德语区）的 OT 可见性+网络自动化公司 Narrowin：Explorer 可视工具跑在 MikroTik 设备上，顾问 Tomas Horyl 持 MTCSWE。
- **产品线与在售品牌**：软件+服务模式（Explorer/IPAM/Log Analytics/OT Connect/Diode/AI Stack），硬件依赖客户现有 MikroTik——「架构师」角色。
- **目标行业与场景**：能源/供暖/大学医院/水务/核电等关键基础设施客户（瑞士与德语区）。
- **团队与规模**：小而精工程团队 + Innosuisse 科研背书。
- **决策链与对接人**：info@narrowin.ch / +41 61 511 23 30。
- **技术与认证**：Tomas：MTCNA+MTCSWE；团队懂 IT 又懂 OT（专家自述 on narrowin.com）。
- **采购与供应链信号**：不是转售商但其设计=硬件推荐权：Explorer/Lab/客户架构里点名设备品牌的机会=出口。
- **近期动态与线索**：Innosuisse OT-IDS 试点伙伴招募中——与他共同参与试点是最好的切入机会。
- **与我方契合点**：让他把管理型纳入其「参考架构」（设计文档里推荐高性价比、参数完整的替代）；同时可随 OT 试点现场供 LT-IS6312XG 节点设备。
- **风险与注意**：他本身很有原则性（“world as it actually is”）——首信就发学术/工程语气，不要 B2C 营销腔；硬件推荐仍要过他的技术评审。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**Narrowin：做轻量级 OT 网络可见性/分段/安全工具——“能跑在现有设备上”，官网自我介绍即为其定位。
  > narrowin builds the lightweight network and security tools that work in the world as it actually is. They are lightweight, plug-and-play, and manageable by the team you already have.
  > 来源：https://narrowin.com/en/
- **【技术与认证】**Explorer 产品页面示意直接以 MikroTik CRS326-24G 作为节点示例（其核心环境=客户的 MikroTik 架）。
  > CORE-SW-01 · vendor MikroTik model CRS326-24G interfaces 24 vlans 4 neighbours 3
  > 来源：https://narrowin.com/en/
- **【目标行业与场景】**已在关键基础设施运行：Swissgas、Breitband Lörrach、Basel 大学附属医院等 reference；正在承担 Innosuisse 资助的分布式 OT 网络研究项目。
  > Running in critical infrastructure today… Looking for pilot partners · distributed OT networks (heating, energy, transportation, multi-site)
  > 来源：https://narrowin.com/en/
- **【近期动态与线索】**正在招募 Innosuisse 资助的 OT-IDS 试点伙伴——试点意向即最新动向。
  > An OT-IDS that runs on the equipment you already have… funded by Innosuisse · with FHNW
  > 来源：https://narrowin.com/en/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 PoE++（Lab/试点环境的“次选硬件”）

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他的客户环境基本是 MikroTik CRS：把 24 口 PoE++ 作为「可接受的替代型号」介绍进他的 Lab 与交付文档，由他自己拿实测评估。
- **要问的问题**：Lab 里除了 CRS 怎么评估替代型号、评审标准是什么？
- **随附证明**：英文规格书 + 功率实测 + 由我方提交的测试申请。

### 第 2 次跟进 · 工业非管理 PoE（OT 试点的现场节点）

- **推什么**：LT-IS6310G-2GX8GT PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：Innosuisse OT-IDS 试点的现场箱体节点：DIN、宽温宽压——类瑞士热力/能源分布式站点环境。
- **要问的问题**：试点站点箱体的安装空间/温度条件怎样、现场现在用什么牌子？
- **随附证明**：宽温报告 + DIN 安装图 + 试产样机数量安排建议。

### 第 3 次跟进 · 管理型进「参考架构」与联合案例

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：如果实测过关：管理型进 Narrowin 参考架构清单，附带 VLAN 分段/ERPS 模板作为其 OT Connect 自动化的配套推荐；可以联合出案例。
- **要问的问题**：你们的参考架构由谁维护、模板要做到什么程度才能进客户的交付清单？
- **随附证明**：VLAN/ERPS 收敛实测（英文）+ 模板仓库合并提案。

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
Hi Tomas,

You hold MTCSWE, so switching is a declared specialism rather than a side task — that is who I want to talk to.

What caught my eye is that you work on MTCSWE, MikroTik and visibility.

Where we may be useful: L3 hardware offload (line-rate forwarding off the CPU), QinQ and VLAN translation, ERPS and MSTP, ACLs and static routing, full CLI plus SSH plus SNMP with a private MIB.

What are you using for L2 redundancy today, and does it need ERPS-class convergence?

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
