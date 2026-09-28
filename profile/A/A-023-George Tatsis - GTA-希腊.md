# George Tatsis / GTA

> **评级 A**　|　希腊 · Galatsi (Athens)　|　档案编号 `A-023`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | GTA |
| 国家 | 希腊 |
| 城市 | Galatsi (Athens) |
| 网站 | gta.gr |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCSE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424DGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 自述场景「**楼宇自控跑在网络上（controls running on the network），你需要为你的建筑提供稳定的承载网**」→ 楼宇自动化/弱电集成方向，帮客户设计、维护甚至翻新网络基础设施 |

## 三、人员与联系方式

- **对接人**：George Tatsis
- **邮箱**：george@gta.gr
- **电话**：+30 210 291 1011
- **原始联系字段**：+30 210 291 1011 / george@gta.gr

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCSE` — 安全

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：工业 / 楼宇自控

### 推什么型号

**STI-488XGGPM（Saga）（导轨式，4×10G 上行 + 8×千兆 PoE++）**

> 系统初判型号：`STC-424DGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

DIN 导轨安装、-40~75℃ 宽温、宽压输入、双电源冗余、ERPS 环网收敛 <20ms、PoE++ 90W 直接带工业相机和 AP

### 怎么开发

第一句就问「你工业现场现在用谁的交换机？环网收敛多少毫秒？」——用 ERPS 实测数据对比切入，然后要求送一台上机柜实测 30 天

### 风险点

工业客户认硬认证（CE / UL / EN50155 / 海事 DNV），缺一项直接出局；温度范围、MTBF、EMC 等级必须给书面数据，不能口头说；现场一旦上线几乎不换，所以第一次必须测通，否则永远没第二次

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：雅典的楼宇技术/弱电集成商（GTA，slogan「Buildings for people」）；自述切入点是「楼宇自控跑在网络上（controls running on the network）」。
- **产品线与在售品牌**：未公开品牌清单；方向是楼宇自动化承载网 + 网络基础设施设计/维护/翻新。
- **目标行业与场景**：楼宇自控（BMS/弱电）、办公与商业楼宇的网络承载网——BMS 控制器、门禁、摄像头、AP 都要挂在同一张接入网上。
- **团队与规模**：小型本地公司（站点极简，仅联系表单），决策链 = George Tatsis 本人。
- **决策链与对接人**：George Tatsis（MTCNA+MTCRE+MTCSE）；george@gta.gr；+30 210 291 1011。
- **技术与认证**：MikroTik 认证顾问（MTCNA+MTCRE+MTCSE）——路由与安全为主，交换靠外购设备补齐。
- **采购与供应链信号**：按楼宇项目采购；楼宇自控项目对 PoE 功率、宽温、看门狗（现场无人值守）要求高。
- **近期动态与线索**：gta.gr 本轮实测只有首页标题与联系表单（无业务内容页），公开信息仅限 MikroTik 名录与 CSV 记录。
- **与我方契合点**：楼宇自控是 PoE 接入最典型的场景：控制器+门禁+摄像头+AP 混挂，VLAN 分段是刚需；工业款可进弱电间/机房外。
- **风险与注意**：官网几乎无内容 → 首次联系时顺带确认业务现状；别按大客户谈，按本地集成商节奏走。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【近期动态与线索】**gta.gr 首页仅有标题与菜单，联系页只有表单字段，无业务内容。
  > GTA – Buildings for people；contact 页仅 First name / Last name / email / Where do you live / Telephone / Your Message 表单
  > 来源：https://gta.gr/contact/
- **【业务定位】**既有记录：自述「楼宇自控跑在网络上」，需要为建筑提供稳定的承载网，帮客户设计/维护/翻新网络基础设施。
  > ★ 自述场景「controls running on the network，你需要为你的建筑提供稳定的承载网」→ 楼宇自动化/弱电集成方向（CSV 备注）
  > 来源：https://gta.gr/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：楼宇承载网：BMS 控制器/门禁/摄像头/AP 全走 PoE，一台 24 口 PoE++ 喂一层楼；看门狗对无人值守楼宇尤其重要（死机自动断电重启）。
- **要问的问题**：他做的一栋楼里，BMS + 门禁 + 摄像头大概多少路 PoE？
- **随附证明**：整机功率预算表 + 看门狗演示 + VLAN 分段示例。

### 第 2 次跟进 · 工业级非管理 PoE（弱电间/机房外）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：楼宇弱电间、屋面机房、地下车库配电箱：宽温宽压、DIN、免配置。
- **要问的问题**：有没有装在弱电间/车库/屋面的接入点？
- **随附证明**：宽温报告 + DIN 图 + 样机。

### 第 3 次跟进 · 管理型 PoE（楼宇分段与冗余）

- **推什么**：STI-480DGGM（Saga） PoE 版（8G + 4×2.5G SFP）
- **切入点**：楼宇自控的行业规范要求分段（BMS/安防/办公/租户）：VLAN + ERPS 环网，一台设备解决一个竖井。
- **要问的问题**：他的楼宇项目要不要做网段隔离与环网冗余？
- **随附证明**：VLAN 模板 + ERPS 实测 + 端口隔离演示。

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
Hi George,

I do industrial access switches — DIN rail, wide temperature, ERPS ring — which matches the environments you work in.

What caught my eye is that you work on controls, running and network.

Where we may be useful: DIN rail, -40 to 75 C, wide input voltage, dual power input, ERPS ring under 20 ms, PoE++ for cameras and APs on the same unit.

What ring protocol are you on today, and what convergence do you actually see?

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
