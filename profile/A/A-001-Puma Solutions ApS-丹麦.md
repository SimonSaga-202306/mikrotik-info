# Puma Solutions ApS

> **评级 A**　|　丹麦　|　档案编号 `A-001`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（PoE/监控/门禁、工业/楼宇），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Puma Solutions ApS |
| 国家 | 丹麦 |
| 城市 | — |
| 网站 | pumait.dk |
| 类型 | 分销（MikroTik 官方） |
| 反向信号 | MikroTik（Reseller） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-480XGGM（Saga） |
| 切入点 | 卖 MikroTik 但缺工业/ERPS/PoE++ → 用同价位工业线补他的产品缺口 |
| 数据来源 | 2026-09-22 |
| 原备注 | 同时是 MikroTik 认证顾问（MTCNA+MTCRE，Stefan Andersen，stefan@pumait.dk / +45 60 709 009）：1998 年起做 ISP 网络，实战派；还设计更大的运营技术栈——**仓库自动化 warehouse automation、门禁 access control、CCTV 视频监控** → 这三项全是 PoE 供电场景，交换机需求最硬。分销商身份 + 集成项目能力 + 工业/PoE 场景，三线合一 |

## 三、人员与联系方式

- **邮箱**：rfi@pumait.dk、stefan@pumait.dk
- **电话**：+45 60 70 90 09
- **原始联系字段**：+45 60 70 90 09 / rfi@pumait.dk

## 四、品牌与技术栈

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：PoE / 监控 / 门禁

### 推什么型号

**STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`STI-480XGGM（Saga）`（供参考，以实际沟通为准）

### 核心卖点

802.3bt 单口 90W、**PoE 看门狗（摄像头死机自动断电重启，省一趟上门）**、250m 延长供电、端口隔离、整机功率预算足

### 怎么开发

替他算一笔账：24 个 4K 头全开要多少瓦、满配后还剩多少余量——这是每个做监控的人都踩过的坑，算清楚就赢一半

### 风险点

**PoE 功率预算和供电稳定性是验收红线**，虚标功率会当场翻车；必须送测、必须给整机功率实测数；部分非标 PoE 相机存在兼容性问题，要先拿他的机型测

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。

- **业务定位**：丹麦 MikroTik 认证顾问 + 自营网店（Puma IT，口号「Teknik der virker. Forretning der virker.」），从方案设计、设备预配置到全国上门安装一条龙。
- **产品线与在售品牌**：自营网店两条主线：MikroTik 171 个 SKU（Routers / **Switches** / WiFi / Wireless PtP-PtMP / LTE-5G / 60 GHz）与 UniFi 680 个 SKU（WiFi / **Switching** / Gateways / Protect 视频 / Door Access 门禁）。
- **目标行业与场景**：四条打包方案：视频监控（按「像素/米」而不是按摄像头数量设计）、多站点网络（同一套配置、从第一天就分段）、办公+仓储 WiFi（先做站点勘测与信道规划，并**把 PoE 预算算清楚**）、门禁（门、卡、日志与摄像头同一系统）。
- **团队与规模**：小团队 + 全国服务/安装伙伴网络；自有库存 3–5 个工作日发货；项目只有「一个对接人」。
- **决策链与对接人**：rfi@pumait.dk（对外邮箱）、stefan@pumait.dk（Stefan Andersen，MTCNA+MTCRE，1998 年起做 ISP 网络）、电话 +45 32 33 13 12 / +45 60 70 90 09。
- **技术与认证**：丹麦持证 MikroTik 顾问（MTCNA、MTCRE）；强调「永久许可、无强制云、配置是可进 git 的文本文件」。
- **采购与供应链信号**：已经同时经营 MikroTik 与 UniFi 两条完整产品线，采购逻辑是「按任务选品牌，即使回报最低」——说明他对第三条补充线（成本/规格补位）是开放的。
- **近期动态与线索**：新上「监控存储合规检查（Retention-tjek）」与「30 分钟免费现状评估」两项服务 → 监控与合规项目在增加，摄像头盘位与 PoE 预算都要重算。
- **与我方契合点**：他自己的销售话术就是「把 PoE 预算算清楚」「按像素/米设计」——正是 24 口 PoE++（单口 90W、整机预算实测、看门狗）最能说服的对象；同时他做门禁/监控/多站点，全是我们的目标场景。
- **风险与注意**：已代理 UniFi + MikroTik 两条线，必须以「补规格/压成本/备第二供应商」身份进入；丹麦对 GDPR/CE/能效文件敏感，材料要备齐。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【产品线与在售品牌】**官网首页明列 MikroTik 171 个产品、UniFi 680 个产品，并且两条线都有独立的 Switches/Switching 分类页。
  > MikroTik171 produkter … Routers｜Switches｜WiFi｜Wireless PtP/PtMP｜LTE/5G｜60 GHz；UniFi680 produkter … WiFi｜Switches｜Gateways｜Videoovervågning｜Adgangskontrol
  > 来源：https://pumait.dk/
- **【目标行业与场景】**监控方案以「像素/米」为设计口径，并把 GDPR 标识与后续运维写进交付内容。
  > Videoovervågning — Dimensioneret på pixels per meter, ikke på antal kameraer. Lokal storage, GDPR-skiltning som del af leverancen, og drift bagefter.
  > 来源：https://pumait.dk/
- **【与我方契合点】**WiFi 方案承诺在下单前把 PoE 预算算清楚——这是我们最能接话的技术点。
  > WiFi til kontor og lager — Site plan før indkøb: dækning, kanalplan og PoE-budget regnet igennem, så der ikke skal hænges flere access points op bagefter.
  > 来源：https://pumait.dk/
- **【技术与认证】**官网自述为丹麦认证 MikroTik 顾问，且每天自己配置设备。
  > En af Danmarks certificerede MikroTik-konsulenter. Vi konfigurerer udstyret selv til daglig … MTCNA / MTCRE
  > 来源：https://pumait.dk/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++，4×万兆上行，440W 级）
- **切入点**：接着他自己的话术走：把他手头一个监控项目的「摄像头数 × 单口瓦数」做成一张 PoE 预算表，用我们的整机功率预算实测数 + PoE 看门狗（摄像头死机自动断电重启）对比 CRS328-24P / UniFi Switch 的余量。
- **要问的问题**：现在 24 口 PoE 项目里，他按每口多少瓦设计？满配后留多少余量？
- **随附证明**：整机功率实测表（逐口负载曲线）+ 看门狗演示视频 + 30 天测试机。

### 第 2 次跟进 · 工业级非管理 PoE（DIN 导轨/宽温，零配置）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C，PoE 版 / PoE++ 版）
- **切入点**：他做仓储与门禁，现场经常没有机柜。工业壳 + 宽温 + 宽压 + 免配置，直接装在配电箱或门口弱电箱里；把「非管理」当卖点：插上就用，坏了整机换。
- **要问的问题**：有没有需要装在现场电箱（无空调、无 UPS）的网络点？
- **随附证明**：宽温/宽压测试报告 + DIN 配件实物照 + 现场接线图（一页）。

### 第 3 次跟进 · 管理型 PoE（跨站点标准化）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版 / -2BT 版）
- **切入点**：他卖「多站点同一套配置」，那就给他统一的 VLAN/环网（ERPS）模板：同一份配置下发到不同站点，链路故障 20ms 级切换；把配置模板做成他的交付资产。
- **要问的问题**：跨站点项目要不要环网冗余和统一 VLAN 模板？
- **随附证明**：ERPS 切换实测（打流断链计时）+ 可直接套用的配置模板文件。

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
Hi Puma,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on warehouse, automation, access control and CCTV.

Where we may be useful: 24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.

How many cameras per job, and what wattage per port are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a STI-480XGGM evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
