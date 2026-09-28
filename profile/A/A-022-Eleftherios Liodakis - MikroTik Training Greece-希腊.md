# Eleftherios Liodakis / MikroTik Training Greece

> **评级 A**　|　希腊 · Chania　|　档案编号 `A-022`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、PoE/监控/门禁），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | MikroTik Training Greece |
| 国家 | 希腊 |
| 城市 | Chania |
| 网站 | mikrotiktraining.gr |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCUME+MTCINE+MTCIPv6E+MTCSE+MTCSWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424DGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 9 证含 **MTCSWE**；经营 **mikrotiktraining.gr（希腊 MikroTik 培训机构）**；防火墙安全、PPPoE、各类隧道 VPN、负载均衡与多路径故障切换、队列与 QoS、User Manager + RADIUS |

## 三、人员与联系方式

- **对接人**：Eleftherios Liodakis
- **邮箱**：el@dce.gr
- **电话**：+30 28210 98579
- **原始联系字段**：+30 28210 98579 / el@dce.gr

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCTCE、MTCUME、MTCINE、MTCIPv6E、MTCSE、MTCSWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCTCE` — 流量控制
- `MTCUME` — 用户管理（Hotspot / PPPoE）
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：PoE / 监控 / 门禁

### 推什么型号

**STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`STC-424DGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

802.3bt 单口 90W、**PoE 看门狗（摄像头死机自动断电重启，省一趟上门）**、250m 延长供电、端口隔离、整机功率预算足

### 怎么开发

替他算一笔账：24 个 4K 头全开要多少瓦、满配后还剩多少余量——这是每个做监控的人都踩过的坑，算清楚就赢一半

### 风险点

**PoE 功率预算和供电稳定性是验收红线**，虚标功率会当场翻车；必须送测、必须给整机功率实测数；部分非标 PoE 相机存在兼容性问题，要先拿他的机型测

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：希腊第一家 MikroTik 培训中心（HellasCom 旗下品牌）：官方认证课程 + 考场，同时通过 linkshop.gr 做 MikroTik 分销（2001 年起）。
- **产品线与在售品牌**：MikroTik 全线（培训与分销）；课程覆盖 MTCNA…MTCINE 十项认证，含 **MTCSWE（交换）** 与 MTCEWE。
- **目标行业与场景**：希腊全国的 ISP/WISP、系统集成商与企业网工程师培训（已培养 9,313+ 名持证工程师、完成 1,944+ 场研讨）；同时做 WISP/ISP 与 hospitality 网络集成。
- **团队与规模**：两位持证讲师（Stavros Maragkoudakis、Eleftherios Liodakis，均持 10 证）+ HellasCom 平台支撑。
- **决策链与对接人**：Eleftherios Liodakis（el@dce.gr）；+30 28210 98579；课程与考试报名走 mikrotiktraining.gr 站点。
- **技术与认证**：讲师本人持 MTCNA/MTCRE/MTCWE/MTCTCE/MTCUME/MTCSE/MTCSWE/MTCIPv6E/MTCEWE/MTCINE（全证）；培训中心同时是希腊官方考点。
- **采购与供应链信号**：培训中心需要大量实验设备（可反复刷配置的交换机）；同时作为分销商按项目采购——培训与分销两条线都能带量。
- **近期动态与线索**：2026 年 10–11 月排期密集：MTCNA 比雷埃夫斯 10/2–3（€490）、MTCSE 10/16–17（€500，已满）、MTCNA 哈尼亚 11/5–7（€490，酒店场地）——MTCSWE 课程也在体系内。
- **与我方契合点**：MTCSWE 课程需要能演示 VLAN/PoE/端口隔离的交换机；实验台一次要 2–4 台，且学员项目会外溢；工业款可用于现场实验。
- **风险与注意**：**与 A-024 HellasCom 是同一体系**（本培训中心即 HellasCom 品牌，讲师 Liodakis 也在 HellasCom 授课）——不要两边各自报价，建议把 A-024 当商务口、这里当技术口。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**培训中心自述与 HellasCom 的关系：2001 年起的 MikroTik 分销商、2011 年起的首个培训中心。
  > MikroTik Distributor από το 2001 — Training Center από το 2011 … Η HellasCom και το ηλεκτρονικό κατάστημα LinkShop.GR, MikroTik Distributor στην Ελλάδα από το 2001
  > 来源：https://mikrotiktraining.gr/
- **【团队与规模】**两位讲师均持 10 项认证；培训规模数据。
  > Stavros Maragkoudakis / Eleftherios Liodakis — Εκπαιδευτής MikroTik：MTCNA MTCRE MTCWE MTCTCE MTCUME MTCSE MTCSWE MTCIPv6E MTCEWE MTCINE；9.313+ πιστοποιημένοι μηχανικοί｜1944+ σεμινάρια ολοκληρωμένα
  > 来源：https://mikrotiktraining.gr/
- **【近期动态与线索】**2026 年秋季课程排期（公开价格与场地）。
  > MTCNA – Πειραιάς | 2-3-4 Οκτωβρίου 2026 €490；MTCSE – Πειραιάς | 17-18 Οκτωβρίου 2026 €500 (Εξαντλημένο)；MTCNA – Χανιά | 6-7-8 Νοεμβρίου 2026 €490
  > 来源：https://mikrotiktraining.gr/
- **【产品线与在售品牌】**课程体系覆盖 10 项官方认证（含交换专项）。
  > Δέκα επίσημες πιστοποιήσεις — MTCNA｜MTCRE｜MTCWE｜MTCTCE｜MTCUME｜MTCSWE（Switching，3 ημ.）｜MTCIPv6E｜MTCEWE｜MTCSE｜MTCINE
  > 来源：https://mikrotiktraining.gr/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：课程实验台角度：一台设备可同时演示 VLAN、PoE 功率预算、看门狗、端口隔离（MTCSWE/MTCNA 都能用），先给成本价实验机。
- **要问的问题**：MTCSWE 实验台现在用哪台交换机、缺哪些演示点？
- **随附证明**：实验手册草案 + 成本价实验机 + 可公开的实测数据。

### 第 2 次跟进 · 工业级非管理 PoE（现场课/客户现场）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：旅游区/岛屿现场课常遇到电箱、无空调环境：宽温 DIN、免配置，拿来当「现场盒」演示。
- **要问的问题**：他们的学员项目里有没有室外/电箱场景？
- **随附证明**：宽温报告 + 便携箱方案 + 样品价。

### 第 3 次跟进 · 管理型 PoE（课程 + 客户项目）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：把管理型交换机写进 MTCSWE/企业网络课程案例与学员项目清单；与 A-024（HellasCom 商务口）协同，避免重复报价。
- **要问的问题**：课程案例能不能用我们的 ERPS/VLAN 实测做一节？
- **随附证明**：ERPS 实测 + 配置模板 + 招标参数条目。

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
Hi Eleftherios,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on RADIUS.

Where we may be useful: 24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.

How many cameras per job, and what wattage per port are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424DGGPM-440W evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
