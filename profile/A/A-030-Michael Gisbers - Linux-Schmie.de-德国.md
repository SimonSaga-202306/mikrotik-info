# Michael Gisbers / Linux-Schmie.de

> **评级 A**　|　德国 · Oberhausen　|　档案编号 `A-030`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Linux-Schmie.de |
| 国家 | 德国 |
| 城市 | Oberhausen |
| 网站 | linux-schmie.de |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCUME+MTCINE+MTCIPv6E+MTCSE+MTCSWE+MTCEWE（10 证，全证） |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维，会自己采购设备 → 用 ERPS/IGMP/VLAN/CLI 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | 10 项认证全拿 → 技术能力最强档；做 RouterOS 咨询/运维/培训，含 Linux 与云集成 |

## 三、人员与联系方式

- **对接人**：Michael Gisbers
- **邮箱**：m.gisbers@linux-schmie.de
- **电话**：+49 173 5106822
- **原始联系字段**：+49 173 5106822 / m.gisbers@linux-schmie.de

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCTCE、MTCUME、MTCINE、MTCIPv6E、MTCSE、MTCSWE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCTCE` — 流量控制
- `MTCUME` — 用户管理（Hotspot / PPPoE）
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik、RouterOS

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

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：Oberhausen 的 MikroTik 培训与咨询个人品牌（Linux-Schmie.de）：官方认证课程、RouterOS 咨询/运维、Linux 与云集成；同时运营 MikroTik 用户组与安全博客。
- **产品线与在售品牌**：纯 MikroTik/RouterOS + Linux 生态；课程覆盖 MTCNA 到 MTCINE，2027 年起新增 **MTCSWE** 课程。
- **目标行业与场景**：德语区网络工程师培训（含考试）、企业 RouterOS 咨询；MikroTik 用户组（MUG Oberhausen）每月线上聚会，覆盖本地技术社群。
- **团队与规模**：个人品牌（本人即讲师/顾问/作者），决策链 = 本人。
- **决策链与对接人**：Michael Gisbers（m.gisbers@linux-schmie.de；+49 173 5106822）。
- **技术与认证**：MikroTik 认证顾问 **10 证全拿**（含 MTCSWE+MTCEWE）；博客做安全事件深度分析（MikroTrick CVE-2026-67276/86060）说明跟踪漏洞与补丁节奏。
- **采购与供应链信号**：培训实验设备 + 学员项目；个人采购但影响力大（用户组 + 博客 + 课程）。
- **近期动态与线索**：2026-09-16 发布「MikroTik Kurse für 2027 online – Jetzt auch mit MTCSWE」；2026-10-13 下一场 MUG Oberhausen；近期课程 MTCRE 2026-09-28、MTCEWE 2026-11-03、MTCNA 2026-12-07。
- **与我方契合点**：MTCSWE 课程刚开（2027 年批次）——需要能讲 VLAN/PoE/环网的交换机做实验台与案例；他的用户组也是本地曝光渠道。
- **风险与注意**：他写安全分析、对细节极敏感：任何夸大都会被写进博客，只给可验证数据。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【近期动态与线索】**2027 年课程计划新增 MTCSWE（交换）课程。
  > MikroTik Kurse für 2027 online – Jetzt auch mit MTCSWE … Neben MTCNA und weiteren Vertiefungskursen ist ab sofort auch der MikroTik Certified Switching Engineer (MTCSWE) verfügbar.
  > 来源：https://www.linux-schmie.de/posts/mikrotik-kurse-2027/
- **【目标行业与场景】**运营本地 MikroTik 用户组（每月线上聚会）。
  > Monatliches Treffen der MikroTik User Group Oberhausen am 2026-10-13 um 19:30 Uhr. Online-Treffen für alle Interessierten an MikroTik und RouterOS.
  > 来源：https://www.linux-schmie.de/posts/mug/mikrotik_user_group_oberhausen_2026-10-13/
- **【技术与认证】**安全博客做 CVE 深度分析（说明其技术深度与话语权）。
  > Detaillierte Analyse der 'MikroTrick'-Sicherheitslücken in MikroTik RouterOS (CVE-2026-67276, CVE-2026-86060), Informationen zu aktiven Angriffen, Patches von MikroTik und Handlungsempfehlungen für Administratoren.
  > 来源：https://www.linux-schmie.de/posts/mikrotik-routeros-mikrotrick/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：MTCSWE 课程实验台 + 学员项目两用：一台设备可演示 VLAN、PoE 预算、端口隔离、看门狗；先给成本价实验机与实验手册草稿。
- **要问的问题**：他 2027 年 MTCSWE 课程的实验台还缺什么演示能力？
- **随附证明**：实验手册草稿 + 成本价实验机 + 可公开实测数据。

### 第 2 次跟进 · 工业级非管理 PoE（现场/用户组演示）

- **推什么**：LT-IS6306G-2GX4GT PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：用户组演示与现场课需要便携耐用的设备：宽温、DIN、免配置，可做「现场盒」主题分享。
- **要问的问题**：用户组活动里愿不愿意做一次工业交换机的现场演示？
- **随附证明**：宽温报告 + 便携方案 + 样品价。

### 第 3 次跟进 · 管理型 PoE（课程与安全视角）

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他写安全分析：给他一份我们的管理面安全说明（默认关闭外部管理、VLAN 隔离、端口安全、固件更新流程），可写进课程的安全章节。
- **要问的问题**：他课程里的交换安全章节愿意用我们的设备做案例吗？
- **随附证明**：管理面安全配置清单 + 固件更新流程 + ERPS/VLAN 实测。

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
Hi Michael,

You hold MTCSWE, so switching is a declared specialism rather than a side task — that is who I want to talk to.

What caught my eye is that you work on RouterOS and Linux.

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
