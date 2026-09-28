# Alexej Sokolow / DECOIT

> **评级 A**　|　德国 · Bremen　|　档案编号 `A-026`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | DECOIT |
| 国家 | 德国 |
| 城市 | Bremen |
| 网站 | decoit.de |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCSWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 持 MTCSWE（交换认证）→ 交换机是正式专长，不是顺带；DECOIT 是不来梅 IT 安全/网络公司 |

## 三、人员与联系方式

- **对接人**：Alexej Sokolow
- **邮箱**：sokolow@decoit.de
- **电话**：+49 421 5960640
- **原始联系字段**：+49 421 5960640 / sokolow@decoit.de

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCSWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：MTCSWE 交换认证

### 推什么型号

**STC-424XGGPM-440W（Saga）（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`STC-424XGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

他持有 MTCSWE（MikroTik 交换认证），交换是正式专长——**不用给他做科普**。开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」直接给 CLI 命令对比和转发实测数据

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全；含糊其辞会立刻失去这类技术型客户的信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：不来梅的 IT 咨询/系统集成与软件公司（2001 年起），专做客户 IT 基础设施的优化与开源方案，并参与国家级/国际研究项目。
- **产品线与在售品牌**：**明确「厂商中立」**：不与软件授权销量绑定，但以产品组合形式合作（网络/服务器/备份/虚拟化/身份管理：oVirt、KVM、UCS、Red Hat、OpenLDAP、Active Directory；安全：pfSense、OpenVPN、IPsec NCP；监控：Icinga/Nagios/Cacti/Munin；VoIP：Asterisk、Kamailio）。
- **目标行业与场景**：科研/公共机构（Fraunhofer SIT/FOKUS、Uni Siegen、HSH、Infineon、devolo、isBremen 等研究合作伙伴）+ 企业 IT 基础设施。
- **团队与规模**：中小型技术公司（研究项目 + 服务团队），决策链短，技术负责人即决策人。
- **决策链与对接人**：Alexej Sokolow（sokolow@decoit.de；+49 421 5960640），持 **MTCSWE**（交换认证）。
- **技术与认证**：MTCNA+MTCRE+MTCSWE；官网简历强调 2001 年起优化客户 IT 基础设施。
- **采购与供应链信号**：厂商中立 = 只按技术标准与 TCO 选型，没有品牌忠诚包袱；开源栈出身 → 看重 CLI/SNMP/可脚本化与文档。
- **近期动态与线索**：官网（德语/英语双语）持续更新研究项目与产品组合；研究合作方列表 15+ 家机构。
- **与我方契合点**：MTCSWE + 开源栈：可以直接谈 VLAN/ERPS/MIB/自动化；监控栈（Icinga/Cacti）说明他们吃 SNMP 数据，我们的 MIB 支持是卖点。
- **风险与注意**：厂商中立意味着必须用「可验证指标 + 完整文档」过他的评审；别谈品牌溢价，谈可替换性与备件。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【产品线与在售品牌】**官网明确厂商中立原则（不为销量绑定品牌）。
  > In order to stay vendor-neutral we do not engage in contracts that oblige us to sell a certain amount of software licences. But we do cooperate with vendors by offering their products as part of our product portfolio.
  > 来源：https://www.decoit.de/en/home_en.html
- **【业务定位】**自 2001 年起做客户 IT 基础设施，并参与研究项目。
  > Since 2001 we attend and optimize customer IT infrastructures. Our solutions always adjust to our customers' IT infrastructure and individual processes. Additionally, we have been active in several different IT research projects, both national and international ones.
  > 来源：https://www.decoit.de/en/home_en.html
- **【技术与认证】**产品组合覆盖监控/身份/虚拟化/安全/VoIP 全套开源栈（利于 SNMP/脚本化对话）。
  > Network/server, back-up, virtualization, identity & infrastructure mgmt.（Sansymphony/Symantec/oVirt/KVM/UCS/RedHat/OpenLDAP/AD）；IT security（pfSense/OpenVPN/IPsec NCP）；Monitoring: Icinga｜Nagios｜Cacti｜Munin｜InterMapper；VoIP: Asterisk｜Kamailio｜Cisco｜Snom
  > 来源：https://www.decoit.de/en/home_en.html

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：以「可验证指标」开场：给他整机功率曲线、逐口数据、SNMP/MIB 清单与 CLI 文档，让他用自己的方式验（他持 MTCSWE）。
- **要问的问题**：他评估接入层交换机时，哪些指标是硬门槛（时延/功率/管理面）？
- **随附证明**：完整规格 + MIB/CLI 文档 + 一台可自测的样机。

### 第 2 次跟进 · 工业级非管理 PoE（机房外/研究现场）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：研究机构与工业客户的现场点位：宽温、DIN、免配置，减少他的运维面。
- **要问的问题**：他的客户里有没有非机房安装的网络点位？
- **随附证明**：宽温报告 + 免维护设计说明（无风扇/宽压）+ 样品价。

### 第 3 次跟进 · 管理型 PoE（自动化/监控集成）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他有 Icinga/Cacti/Munin 监控栈：把我们的交换机接进他的监控模板 + 批量配置脚本，做「可脚本化的标准化接入层」。
- **要问的问题**：愿不愿意把他的监控模板接到我们设备上做一次联调？
- **随附证明**：MIB 文件 + Icinga/Cacti 模板示例 + 批量配置脚本。

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
Hi Alexej,

You hold MTCSWE, so switching is a declared specialism rather than a side task — that is who I want to talk to.

What caught my eye is that you work on MTCSWE and DECOIT.

Where we may be useful: L3 hardware offload (line-rate forwarding off the CPU), QinQ and VLAN translation, ERPS and MSTP, ACLs and static routing, full CLI plus SSH plus SNMP with a private MIB.

What are you using for L2 redundancy today, and does it need ERPS-class convergence?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424XGGPM-440W evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
