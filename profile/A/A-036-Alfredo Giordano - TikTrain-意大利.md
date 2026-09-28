# Alfredo Giordano / TikTrain

> **评级 A**　|　意大利 · Montoro　|　档案编号 `A-036`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（PoE/监控/门禁），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | TikTrain |
| 国家 | 意大利 |
| 城市 | Montoro |
| 网站 | tiktrain.com |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ISP/**运营商网络**设计实施与排障；动态路由、隧道、QoS、PPPoE、RouterOS 与现有网集成、PtP/PtMP、负载均衡与故障切换、带宽管理；可服务欧洲与墨西哥 |

## 三、人员与联系方式

- **对接人**：Alfredo Giordano
- **邮箱**：alfredo@tiktrain.com
- **电话**：+39 347 312 5813
- **原始联系字段**：+39 347 312 5813 / alfredo@tiktrain.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCTCE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCTCE` — 流量控制

**涉及品牌 / 技术**：MikroTik、RouterOS

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

- **业务定位**：TikTrain：2000 年起做电信/网络的专业团队，现在做认证培训 + 咨询（MikroTik 与 Ubiquiti 双线课程）。
- **产品线与在售品牌**：MikroTik 10 项认证课程（MTCNA…MTCINE，含 **MTCSWE**）+ Ubiquiti 5 项认证（UBWA/UEWA/UBRSS/UBWS/UBRSA）；所有课程由认证讲师授课并提供相应语言教材。
- **目标行业与场景**：ISP/运营商网络的设计、实施与排障咨询（动态路由、隧道、QoS、PPPoE、与既有网集成、PtP/PtMP、负载均衡与故障切换、带宽管理）；培训覆盖欧洲与墨西哥。
- **团队与规模**：小型专业团队（决策链 = Alfredo Giordano 本人）。
- **决策链与对接人**：Alfredo Giordano（alfredo@tiktrain.com；+39 347 312 5813），持 MTCNA+MTCRE+MTCTCE。
- **技术与认证**：MikroTik 认证（MTCNA/MTCRE/MTCTCE）+ 培训资质；同时教 Ubiquiti 课程 → 双生态。
- **采购与供应链信号**：培训实验设备 + ISP 项目设备；跨欧洲/墨西哥服务意味着他可能在多地采购，价格与交期都要能算清。
- **近期动态与线索**：官网在线：课程体系与联系方式（Contacts 页）保持更新，training events 分类持续发布。
- **与我方契合点**：他做 ISP 网络与培训：24 口 PoE（接入）、工业款（站址）、管理型（VLAN/QoS/环网）都能同时用于课与项目。
- **风险与注意**：同时教 Ubiquiti：谈到 UniFi 时避免贬低对手，用「同档规格+价格」对比即可。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**团队沿革与「咨询+培训」定位。
  > We are a group of professionals working with in telecommunications from 2000. After deploying high value solutions over hundreds of networks of different type and size and we are committed to consulting and training.
  > 来源：https://tiktrain.com/
- **【产品线与在售品牌】**MikroTik 10 项 + Ubiquiti 5 项认证课程体系。
  > Mikrotik offers the following certifications: MTCNA, MTCRE, MTCWE, MTCEWE, MTCTCE, MTCIPv6E, MTCUME, MTCSWE, MTCSE, and MTCINE.；Ubiquiti offers the following certifications: UBWA, UEWA, UBRSS, UBWS, UBRSA.
  > 来源：https://tiktrain.com/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：课程实验 + ISP 项目双用：MTCSWE 内容里加一节「24 口 PoE 供电预算与端口隔离」，项目上直接复用。
- **要问的问题**：他 MTCSWE 课程的实验台用什么设备？
- **随附证明**：实验手册 + 成本价实验机 + 实测数据。

### 第 2 次跟进 · 工业级非管理 PoE（ISP 站址）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他服务 ISP/运营商：站址与室外箱要宽温 DIN 免配置设备，作为现场标准件。
- **要问的问题**：他的 ISP 项目里站址设备现在怎么选？
- **随附证明**：宽温报告 + SFP 兼容清单 + 样品。

### 第 3 次跟进 · 管理型 PoE（QoS/环网）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他讲动态路由与 QoS：接入层给 VLAN/QoS/ERPS 模板与实测，与他课程里的 QoS 章节呼应。
- **要问的问题**：他愿不愿意在课上用我们的设备做 QoS/环网演示？
- **随附证明**：QoS 模板 + ERPS 实测 + 课程可用的演示脚本。

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
Hi Alfredo,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on ISP, QoS and PPPoE.

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
