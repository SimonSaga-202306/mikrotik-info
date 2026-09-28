# Laszlo Kalapos / MindenamiMikrotik

> **评级 A**　|　匈牙利 · Miskolc　|　档案编号 `A-013`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、PoE/监控/门禁），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | MindenamiMikrotik |
| 国家 | 匈牙利 |
| 城市 | Miskolc |
| 网站 | mindenamimikrotik.hu |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCTCE+MTCUME+MTCINE+MTCSE+MTCSWE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 持 MTCSWE + MTCEWE；站点名直译「所有关于 MikroTik 的事」→ 纯 MikroTik 专营；有线无线网络设计安装、VPN、PPPoE（含 RADIUS）、防火墙、带宽管理与队列、Hotspot、User Manager、The Dude；现场+远程 |

## 三、人员与联系方式

- **对接人**：Laszlo Kalapos
- **邮箱**：info@mindenamimikrotik.hu
- **电话**：+36 20 295 6414
- **原始联系字段**：+36 20 295 6414 / info@mindenamimikrotik.hu

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCTCE、MTCUME、MTCINE、MTCSE、MTCSWE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCTCE` — 流量控制
- `MTCUME` — 用户管理（Hotspot / PPPoE）
- `MTCINE` — ISP 互联
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik、The Dude

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

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。

- **业务定位**：匈牙利 Miskolc 的 MikroTik 专营顾问（站点名直译「关于 MikroTik 的一切」）：现场/远程网络设计安装、VPN、PPPoE/RADIUS、防火墙、带宽管理与队列、Hotspot、User Manager、The Dude；同时是 MikroTik 培训站（现场课 + 视频课 + 电子书 + 支持服务）。
- **产品线与在售品牌**：纯 MikroTik 技术栈（RouterOS 全线），培训与实施并重。
- **目标行业与场景**：中小企业、ISP/WISP；培训学员覆盖匈牙利本地工程人员。
- **团队与规模**：个人主导（Kalapos László 为站点作者/讲师），决策链=本人。
- **决策链与对接人**：info@mindenamimikrotik.hu；+36 20 295 6414；站点联系页 kapcsolat。
- **技术与认证**：MikroTik 认证顾问 **MTCSWE + MTCEWE**（交换+企业无线）等 7 证。
- **采购与供应链信号**：他既是实施方也是讲师：设备用于客户项目与课程实验；愿意接非 MikroTik 设备做课程实验的可能性高（但需给他「可讲的内容」）。
- **近期动态与线索**：站点持续更新：2025 年 3 月开现场课程、2026 年 2 月挂出「hamarosan（即将推出）」新项目横幅（milpay），并维护在线俱乐部/电子书/技术支持页。
- **与我方契合点**：培训影响力客户：他在课上讲交换机 → 我们的管理型/工业款可以进他的实验台与案例；同时他的客户项目需要 24 口 PoE 与工业 PoE。
- **风险与注意**：影响力路线：谈「能多讲什么内容」而不是返点；先寄实验机 + 可公开案例。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**站点首页即培训与支持入口（现场课、视频课、电子书、技术支持）。
  > Élő MikroTik tanfolyamok；Videós MikroTik tanfolyamok；Segítség, terméktámogatás；Vezeték nélkül, egyszerűen - ebook；Network Online - hálózati alapozó tananyag
  > 来源：https://mindenamimikrotik.hu/
- **【近期动态与线索】**2026 年 2 月挂出即将推出的新项目横幅（milpay）。
  > banner_hamarosan.webp（hamarosan = 即将推出）；页面更新时间 2026-05-19
  > 来源：https://mindenamimikrotik.hu/
- **【技术与认证】**持 MTCSWE+MTCEWE 等 7 证，站点名为「关于 MikroTik 的一切」。
  > MTCNA+MTCTCE+MTCUME+MTCINE+MTCSE+MTCSWE+MTCEWE；站点名直译「所有关于 MikroTik 的事」
  > 来源：https://mikrotik.com/consultants

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：给课程/项目两用：他可以用我们的 24 口 PoE++ 上课（VLAN、端口隔离、PoE 预算、看门狗都能演示），学员项目又直接转化成销量。
- **要问的问题**：他课程里的交换实验现在用什么设备、缺哪些演示点？
- **随附证明**：实验机（成本价）+ 可直接用的实验手册草稿 + 可公开的实测数据。

### 第 2 次跟进 · 工业级非管理 PoE（客户现场）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他的客户里做监控/门禁的现场点位：宽温 DIN 免配置，作为他标准方案里的「现场盒」。
- **要问的问题**：他有没有客户是乡镇/农场/户外场景需要宽温设备？
- **随附证明**：宽温报告 + 一页方案模板（可直接进他的报价单）。

### 第 3 次跟进 · 管理型 PoE（进他的课与方案）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）或 STC-448XGGM（Saga L3）（L3，PoE 版）
- **切入点**：把管理型交换机写进他的「企业网络」课程与标准方案：VLAN、ERPS、L3、SNMP 监控都可讲。
- **要问的问题**：他愿不愿意把我们的型号列进课程实验清单？
- **随附证明**：配置模板 + MIB/SNMP 清单 + ERPS 实测（可公开引用）。

## 九、深度再发掘（R55：背景 · 芯片/型号 · 关键人 · 在意点 · SWOT · Saga 适配）

> 调研日期 **2026-09-28**；来源含官网/公开工商与社媒页面，原文摘录见本节后部；原始记录：`batch/A类深挖_2026-09-28_R55_第2批.json`。涉及我方价格均为 EXW 快照（15 天有效，报价前核价）。

- **背景深描**：**László Kalapos / MindenamiMikrotik**，匈牙利 Miskolc。**匈牙利第一位 MikroTik Certified Trainer**（2009 授证、2010 起授课）——站点自述战绩：**350+ 场培训、约 3000 人次通过考试、20 年 MikroTik 经验、16 年教龄**。mindenamimikrotik.hu=完整培训电商：直播课（élő tanfolyamok）+视频课（online klub）+产品支持服务+自著电子书《Vezeték nélkül, egyszerűen》（无线，简单化）+Network Online 网络基础课；2026 年新挂 milpay 横幅（新业务线酝酿）。站点 2026-05 仍活跃更新。
- **芯片与在用型号**：RouterOS 全系教学（MTCNA→MTCINE 全谱课程）；教学设备=长期教具消耗+课程推荐位双重价值。其电子书与基础课面向初学者=匈牙利 MikroTik 入口守门人。出货量：教具批次+学员引导去向（不可追踪，尊重红线不打探）。客户反馈：课页学员感言摘录（「Többé nem félek hozzányúlni a beállításokhoz」——再也不怕碰配置）=教学口碑资产。
- **关键人KP**：**Kalapos László 本人**。邮箱 **info@mindenamimikrotik.hu**（官网公开；MX nethely.hu 今日核验有效）+ 电话 +36 20 295 6414。公开身份「Magyarország első MikroTik Certified Trainer minősítéssel rendelkező oktatója」（匈牙利首位持证培训师）。LinkedIn 未见（个人品牌站即门面）。
- **关注点与资质**：①**匈牙利第一培训师**品牌=他最大的资产，任何合作都不能稀释其 MikroTik 官方感；②教学工业化（视频课+基础课漏斗）；③学员成果导向（3000 通过数是硬指标）；④⚠️ **教师红线纪律（R54 既定）**：不经培训语境向学员推销、不打学员名单、只谈他本人的教学硬件与自有工程。参展：培训即其展场。
- **优缺点SWOT**：**S**：一国 MikroTik 教学垄断位+3000 学员长尾影响力+站点内容工业化成熟。**W**：教师身份=商业合作边界窄；个人品牌依赖 MikroTik 官方关系。**O**：**教具更新潮**（课程设备换代：24口 PoE 教具箱）+他本人工程/演示自购机——这是红线内全部可做面；milpay 新业务若落地含线下收银/门店网络（2026-02 横幅起步，观察）。**T**：官方培训体系竞争与政策变化；红线踩错永久失信。
- **Saga产品适配**：教具箱（红线内，自述教学用途）：**STC-424DGGPM-280W**（**EXW $165**，L2+ 全套特性=MTCSWE 级演示素材：ERPS<20ms/Private VLAN/QinQ）+ 入门 **STC-28DGGPM**（**EXW $99**）。随附 L2+/L3 特性表原文说明 Voice VLAN 仅在 L2+ 系（教学避坑点）。绝不主动要学员数据、不给课程联名报价。

### 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Kalapos László | 匈牙利首位 MikroTik Certified Trainer（2009）/ 培训站主 | info@mindenamimikrotik.hu；+36 20 295 6414 | 官网公开；MX（nethely.hu）已验 | https://mindenamimikrotik.hu/ ・ https://mindenamimikrotik.hu/mikrotik-online-regisztracio-2/ |

### R55 证据摘录

- **【头部地位】**匈牙利首位 MikroTik 认证培训师自证。
  > Magyarország első MikroTik Certified Trainer minősítéssel rendelkező oktatója. 2010 óta tartok élő képzéseket
  > 来源：https://mindenamimikrotik.hu/mikrotik-online-regisztracio-2/
- **【战绩】**350+ 场、约 3000 人次通过、20 年 MikroTik 经验。
  > Összes képzés: 350+ … Összes sikeres vizsga: ~3000 … MikroTik-es tapasztalat: 20 év
  > 来源：https://mindenamimikrotik.hu/mikrotik-alapozas/
- **【业务范围】**直播课+视频课+产品支持+电子书+基础课全线。
  > Élő MikroTik tanfolyamok … Videós MikroTik tanfolyamok … Segítség, terméktámogatás … Vezeték nélkül, egyszerűen - ebook … Network Online - hálózati alapozó tananyag
  > 来源：https://mindenamimikrotik.hu/
- **【学员口碑】**课页学员感言。
  > Többé nem félek hozzányúlni a beállításokhoz – most már átlátom a rendszert, és ki fogom hozni belőle a legtöbbet.
  > 来源：https://mindenamimikrotik.hu/mikrotik-alapozas/

## 十、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十一、首触邮件（可直接发送）

**主题**：PoE budget question on your camera jobs

```text
Hi Laszlo,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on RADIUS and The Dude.

Where we may be useful: 24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.

How many cameras per job, and what wattage per port are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424XGGPM-440W evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

Either way, no follow-up sequence from me.

Best,
[your name]
```

> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；③ 落款换成你自己的名字与公司；④ 一次只问一个问题。

## 十二、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
