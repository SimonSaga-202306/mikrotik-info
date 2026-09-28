# Cristian Delogu / Netify

> **评级 A**　|　意大利 · Lodi　|　档案编号 `A-037`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（PoE/监控/门禁），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Netify |
| 国家 | 意大利 |
| 城市 | Lodi |
| 网站 | netify.it |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCSE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | WISP/ISP 咨询：有线无线规划设计与迁移；VLAN、PPPoE、防火墙、OSPF、BGP、MPLS、无线、队列与流量整形、脚本、安全 |

## 三、人员与联系方式

- **对接人**：Cristian Delogu
- **邮箱**：cristian.delogu@netify.it
- **电话**：+39 335 127 4723
- **原始联系字段**：+39 335 127 4723 / cristian.delogu@netify.it

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCSE` — 安全

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：PoE / 监控 / 门禁

### 推什么型号

**STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`STC-424XGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

802.3bt 单口 90W、**PoE 看门狗（摄像头死机自动断电重启，省一趟上门）**、250m 延长供电、端口隔离、整机功率预算足

### 怎么开发

替他算一笔账：24 个 4K 头全开要多少瓦、满配后还剩多少余量——这是每个做监控的人都踩过的坑，算清楚就赢一半

### 风险点

**PoE 功率预算和供电稳定性是验收红线**，虚标功率会当场翻车；必须送测、必须给整机功率实测数；部分非标 PoE 相机存在兼容性问题，要先拿他的机型测

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：洛迪（Lodi）的一体化安全系统公司 Netify：实体安防（报警、视频监控、闸机、门禁）+ 网络安全 + 企业网络基础设施设计，并提供 MikroTik 培训（自有讲师）。
- **产品线与在售品牌**：合作品牌含 MikroTik、Cambium Networks、Sophos、Nedap、Kalliope（VoIP）、Zucchetti Axess；方案线：Sicurezza Integrata、Unified Communication、Networking。
- **目标行业与场景**：企业/办公楼宇的安防与网络一体化项目（闸机、门禁、监控、对讲、VoIP、自服务前台）、需要网络与信息安全统一设计的客户。
- **团队与规模**：本地中小企业（洛迪及周边），决策链短；技术负责人 Cristian Delogu 持多证。
- **决策链与对接人**：cristian.delogu@netify.it；+39 335 127 4723。
- **技术与认证**：MikroTik 认证顾问（MTCNA+MTCRE+MTCSE）；公司有 MikroTik 认证讲师做「Formazione MikroTik」。
- **采购与供应链信号**：安防项目 → 大量 PoE 端口（摄像头/门禁/对讲/AP）；按项目采购，对功率预算与稳定性敏感。
- **近期动态与线索**：官网博客 2025 年更新（Self Reception、预测性视频分析），说明在推「安防+IT」一体化方案并持续获客。
- **与我方契合点**：监控+门禁+对讲+AP 全走 PoE：24 口 PoE++ 是标准件；闸机/停车场等室外点位用工业款；VLAN 分段（安防/办公/访客）用管理型。
- **风险与注意**：他重视合规与安全（MTCSE）→ 谈管理面安全配置与隔离能力，不要只谈价格。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**业务三大块：一体化安防、统一通信、网络。
  > sistemi e impianti di sicurezza integrata: dalla sicurezza fisica con sistemi di allarme, videosorveglianza, tornelli e controllo accessi, alla sicurezza informatica … con la cyber security e la progettazione di infrastrutture di rete ad hoc；SOLUZIONI DI SICUREZZA INTEGRATA｜SOLUZIONI UNIFIED COMMUNICATION｜SOLUZIONI DI NETWORKING
  > 来源：https://www.netify.it/
- **【产品线与在售品牌】**合作品牌含 MikroTik 与 Cambium、Sophos、Nedap（门禁）、Kalliope（VoIP）。
  > I partner certificati con cui lavoriamo ogni giorno：CAMBIUM NETWORKS｜KALLIOPE｜SOPHOS｜NEDAP N.V.｜MIKROTIK｜ZUCCHETTI AXESS
  > 来源：https://www.netify.it/
- **【目标行业与场景】**自有 MikroTik 培训业务（讲师授课）。
  > FORMAZIONE MIKROTIK — Seguire un corso di formazione MikroTik ti permette di ottenere una certificazione riconosciuta a livello internazionale … Apprendi tutto ciò che può servire sulle reti IP e ottieni le certificazioni MikroTik con il nostro Trainer.
  > 来源：https://www.netify.it/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：安防一体化：24 口 PoE++ 同时喂摄像头、门禁、对讲与 AP；算功率预算 + 看门狗（省上门），是他每个项目都用的账。
- **要问的问题**：他一个典型安防项目里，PoE 端口一共多少路、单口最大多少瓦？
- **随附证明**：整机功率实测 + 看门狗演示 + VLAN 分段示例。

### 第 2 次跟进 · 工业级非管理 PoE（闸机/停车场/室外）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：闸机、停车场、室外立柱的供电箱：宽温宽压、DIN、免配置，直接进他的现场箱标准。
- **要问的问题**：他们的室外/停车场的网络点现在怎么做防护？
- **随附证明**：宽温报告 + 户外箱方案 + 样机。

### 第 3 次跟进 · 管理型 PoE（安防网段隔离）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：安防与办公必须隔离（他持 MTCSE）：VLAN + 端口隔离 + ERPS；谈管理面安全配置（默认关闭外部管理、固件更新流程）。
- **要问的问题**：他的安防项目里要不要把监控/门禁与办公网物理或 VLAN 隔离？
- **随附证明**：VLAN/隔离模板 + 管理面安全清单 + ERPS 实测。

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
Hi Cristian,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on WISP and VLAN.

Where we may be useful: 24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.

How many cameras per job, and what wattage per port are you designing to?

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
