# Carlos Villalobos / Hecnys

> **评级 A**　|　西班牙 · Bormujos (Sevilla)　|　档案编号 `A-070`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Hecnys |
| 国家 | 西班牙 |
| 城市 | Bormujos (Sevilla) |
| 网站 | hecnys.com |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCTCE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-488XGGPM（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 工业工程师出身，专长 **IT/OT 网络融合（工业场景）**；基于 MikroTik 的架构设计、配置与优化 → 推工业导轨交换机 |

## 三、人员与联系方式

- **对接人**：Carlos Villalobos
- **邮箱**：carlosvillalobos@hecnys.com
- **电话**：+34 645 396 100
- **原始联系字段**：+34 645 396 100 / carlosvillalobos@hecnys.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCTCE

- `MTCNA` — 网络助理（入门）
- `MTCTCE` — 流量控制

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：工业 / 楼宇自控

### 推什么型号

**STI-488XGGPM（Saga）（导轨式，4×10G 上行 + 8×千兆 PoE++）**

> 系统初判型号：`STI-488XGGPM（Saga）`（供参考，以实际沟通为准）

### 核心卖点

DIN 导轨安装、-40~75℃ 宽温、宽压输入、双电源冗余、ERPS 环网收敛 <20ms、PoE++ 90W 直接带工业相机和 AP

### 怎么开发

第一句就问「你工业现场现在用谁的交换机？环网收敛多少毫秒？」——用 ERPS 实测数据对比切入，然后要求送一台上机柜实测 30 天

### 风险点

工业客户认硬认证（CE / UL / EN50155 / 海事 DNV），缺一项直接出局；温度范围、MTBF、EMC 等级必须给书面数据，不能口头说；现场一旦上线几乎不换，所以第一次必须测通，否则永远没第二次

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。

- **业务定位**：塞维利亚工业自动化集成商：Ignition 平台 SCADA/IIoT + 工业网络建设，IT/OT 融合方向，工程师直连客户（设计与交付同一人）。
- **产品线与在售品牌**：项目制：Ignition（Inductive Automation）+ MQTT/OPC UA/SQL 技术栈 + 工业网络基础设施；硬件随项目选型。
- **目标行业与场景**：油气/发电/制药/石化/港口/汽车的车间网络：PLC 到现场的分段、边缘采集节点、监控与远程运维通道。
- **团队与规模**：小而精的工程团队（「designs = commissions = supports 同一工程师」）；支持时段周一到周五 8:00–18:00 CET。
- **决策链与对接人**：Carlos Villalobos 本人（+34 645 396 100 / carlosvillalobos@hecnys.com），工业工程师出身。
- **技术与认证**：MTCNA+MTCTCE（CSV 名录记录）+ Inductive Automation 官方集成商（2026 起）；工业协议栈（OPC UA/MQTT Sparkplug）母语级。
- **采购与供应链信号**：车间项目的网络设备由他设计选型：DIN 导轨、宽温、冗余是硬指标；项目复制性强（同平台架构复用）。
- **近期动态与线索**：刚拿到 Inductive Automation 官集资质（2026）=投标资格升级、项目量上行期。
- **与我方契合点**：工业网络这条业务线=我们的 DIN 工业线正对口：机器视觉/PLC 柜/边缘节点都要 PoE 与上行；港口/油气场景的室外点位更多。
- **风险与注意**：工业客户重认证（ATEX/IEC/行业规范）：先问清目标行业的认证要求再谈型号，别硬推不满足项。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**官网抬头：Inductive Automation 官方集成商，车间层的控制与数据工程。
  > Official Inductive Automation integrator · Control and data engineering for the plant floor · We design, integrate and support SCADA, IIoT and industrial network systems on Ignition.
  > 来源：https://hecnys.com/en
- **【产品线与在售品牌】**四条业务线：Ignition SCADA、工业 IIoT（MQTT/Sparkplug+OPC UA）、工业网络（分段/可靠性/远程访问）、定制开发。
  > Ignition SCADA · Industrial IIoT — From plant-floor data to business systems, over MQTT/Sparkplug and OPC UA · Industrial networks — The infrastructure the data rides on: segmentation, reliability and remote access.
  > 来源：https://hecnys.com/en
- **【近期动态与线索】**2026 年新晋 Inductive Automation 认证集成商（15 年行业经验）——资质刚升级，正在扩项目盘。
  > Certified Integrator of Inductive Automation since 2026, with 15 years of experience in industrial control and integration.
  > 来源：https://hecnys.com/en
- **【目标行业与场景】**服务行业清单：油气、发电、制药、石化、集装箱港口物流、汽车——全部是重 PoE/工业交换场景。
  > Oil & Gas · Power generation · Pharmaceutical · Petrochemical · Container port logistics · Automotive
  > 来源：https://hecnys.com/en

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（车间监控/办公接入）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：车间项目的监控与办公接入段：24 口 PoE++ 带摄像头/机器视觉上位/AP，4×10G 上行回主控——从 IT 侧先建立合作。
- **要问的问题**：项目里 CCTV 与办公接入的交换机现在用哪个牌子？
- **随附证明**：规格对照 + 工业场景供电预算表（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（PLC 柜/边缘节点）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：正对工业网络业务线：PLC 柜与边缘采集节点的宽温 DIN PoE，-40 冷启动、SFP 上行——按柜标配。
- **要问的问题**：柜内交换现在用什么型号？有没有 -40 或高温失效的案例？
- **随附证明**：宽温报告 + DIN 图 + 抗扰测试项清单。

### 第 3 次跟进 · 管理型 PoE（IT/OT 分段模板）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他做 segmentation 出身：管理型 VLAN/ACL/ERPS 模板对接他的 IT/OT 分段架构，方案写进他的标准设计。
- **要问的问题**：你的分段参考架构里接入层有没有候选型号空位？
- **随附证明**：分段架构对照 + VLAN/ERPS 模板 + 实测。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：Ring convergence + -40 to 75C switches

```text
Hi Carlos,

I do industrial access switches — DIN rail, wide temperature, ERPS ring — which matches the environments you work in.

What caught my eye is that you work on IT/OT.

Where we may be useful: DIN rail, -40 to 75 C, wide input voltage, dual power input, ERPS ring under 20 ms, PoE++ for cameras and APs on the same unit.

What ring protocol are you on today, and what convergence do you actually see?

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
