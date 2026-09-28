# Urbino Lobo / MiniMeLabs

> **评级 A**　|　葡萄牙 · Funchal（马德拉）　|　档案编号 `A-053`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（酒店/多住户），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | MiniMeLabs |
| 国家 | 葡萄牙 |
| 城市 | Funchal（马德拉） |
| 网站 | minimelabs.com |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCUME |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424DGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 自述「**酒店 Hospitality、多住户公寓 Multi-Dwelling Properties、公共接入 Public Access 的网络与强制门户 Captive Portal 环境专家**」，且「**手上有大量现场工程师与生态方案的数据库**」→ 酒店+MDU 是 PoE 接入交换机批量出货场景；他还有外场工程师网络，能铺量。同事 João Martins（+351 968 850 581 / joao@minimelabs.com，MTCNA+MTCUME） |

## 三、人员与联系方式

- **对接人**：Urbino Lobo
- **邮箱**：urbino@minimelabs.com、joao@minimelabs.com
- **电话**：+351 919 379 550
- **原始联系字段**：+351 919 379 550 / urbino@minimelabs.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCUME

- `MTCNA` — 网络助理（入门）
- `MTCUME` — 用户管理（Hotspot / PPPoE）

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：酒店 / 多住户

### 推什么型号

**STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`STC-424DGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

客房 VLAN 隔离、端口隔离（防客人私接路由器）、PoE 同时供 AP / IPTV 机顶盒 / IP 话机、组播 IPTV 不卡

### 怎么开发

问「一间客房下几根线？AP 怎么供电？IPTV 走不走组播？」——酒店是多期项目，一期做进去后面几期跟着走

### 风险点

酒店项目周期长且受装修进度牵制，别押季度指标；采购决定权常在弱电总包而非业主，要找到总包；客房网络出问题客人直接投诉，稳定性零容忍

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。

- **业务定位**：马德拉（/伦敦）的场景体验公司：公共空间/酒店/零售的“位置感知+PWA+获客”平台，硬件依赖现场网络基础。
- **产品线与在售品牌**：Morfus（PWA）/MidasMoon（广告）/EzeHome（IoT）/Sentry——软件驱动，但任何案例都要配合现场 WiFi/NAC/供电与分网设备。
- **目标行业与场景**：广场/机场/商场/酒店/餐饮——高价位场景、对 WiFi 与 VLAN 分段/Guest-PSK 等有实质要求。
- **团队与规模**：小型软件+现场交付工程队。
- **决策链与对接人**：Urbino Lobo（+351 919 379 550 / urbino@minimelabs.com），工程师+BD 兼位。
- **技术与认证**：MTCNA+MTCUME（来源：CSV 既有 MikroTik 名录记录）——他们看得懂我方的管理面参数。
- **采购与供应链信号**：随场景项目订齐现场网络设备（每酒店/商圈单子都是一次设备采购窗口）。
- **近期动态与线索**：伦敦大型商圈项目知名度高，葡萄牙/马德拉本地酒店也在升级周期里——主要切入点。
- **与我方契合点**：WiFi 服务=我们的 PoE++：他们要的就是“24 口设备一次到位 + 分网监管”；管理型在给 GDPR/客人网隔离时也有说头。
- **风险与注意**：他卖的是方案与数据价值——我们要给能进技术标书的参数细节，不与纯低价竞争。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**MiniMeLabs：做“物理与数字桥接”的智能酒店/公共空间场景方案（7 年品牌历程）。
  > Bridging the Physical & Digital — Innovating the way people connect with the world around them for 7 years
  > 来源：https://minimelabs.com/
- **【目标行业与场景】**方案覆盖 Hospitality、Public Spaces、Retail、Food & Beverage——WiFi 接入与获客平台是他主力。
  > Seamless customer Wifi onboarding… Public spaces · Hospitality · Retail mall · Food & Beverage
  > 来源：https://minimelabs.com/
- **【近期动态与线索】**在伦敦高端商圈落地（Trafalgar Square/Oxford Street/Westminster 与机场/商场/场馆）。
  > Proudly operating digital engagement solutions throughout London, in the exquisite areas of Trafalgar square, Oxford street & other areas of Westminster.
  > 来源：https://minimelabs.com/
- **【技术与认证】**其核心是 WiFi 定位分析与客户洞察（GDPR 合规），意味着对接入层设备的管理性（DHCP/SNMP/VLAN）有专业要求。
  > Customer Insights That Overcome MAC Randomization — Our Wi-Fi analytics and communications platform… maintains GDPR compliance.
  > 来源：https://minimelabs.com/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 PoE++（酒店/商圈 WiFi 接入主设备）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他每个场景 24 口一次到位：PoE++ 带齐 AP+监控+话机；他的 captive portal 架构完全不动——架构上零冲突。
- **要问的问题**：一场景的 AP 平均多少个、楼层交换机现在是什么速位？
- **随附证明**：功率实测表 + AP/监控混合供电对照。

### 第 2 次跟进 · 工业非管理 PoE（室外广场点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：广场/外部场馆的室外 AP 点位：宽温宽压、DIN、免配置、坏了整机现场热换——给他减少外场上门次数。
- **要问的问题**：室外/广场点位冬天会出现什么供电问题？
- **随附证明**：宽温报告 + DIN 安装图 + 一台测试机。

### 第 3 次跟进 · 管理型 + GDPR/客人网分段

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：管理型 VLAN 多网段+访客隔离+SNMP 资产管理——与他 GDPR 话术对齐，把「客人/员工/监控」的分层写成分段模板。
- **要问的问题**：他的 captive portal 与 VLAN 分层怎么做的、每个场景分几个 VLAN？
- **随附证明**：VLAN/ERPS/ACL 模板 + ERPS 收敛实测（英文）+ SNMP 参数页。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：PoE + VLAN per room — question on your hotel jobs

```text
Hi Urbino,

I build PoE access switches for hotel and multi-dwelling networks, which is where you seem to spend most of your time.

What caught my eye is that you work on hospitality, multi-dwelling, MDU and captive portal.

Where we may be useful: 24 gigabit PoE++ ports (APs, IP phones and IPTV boxes on one cable), per-room VLAN isolation, port isolation to stop guests plugging in their own router, IGMP snooping for the TV.

How many drops per room, and is your IPTV running on multicast?

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
