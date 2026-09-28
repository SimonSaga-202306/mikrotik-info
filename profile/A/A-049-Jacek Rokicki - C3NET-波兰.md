# Jacek Rokicki / C3NET

> **评级 A**　|　波兰 · Falenty Nowe　|　档案编号 `A-049`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | C3NET |
| 国家 | 波兰 |
| 城市 | Falenty Nowe |
| 网站 | c3net.pl |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCTCE+MTCINE+MTCSE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XG-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 自述技能直接写「CRS switches and many L2 topics」+ BGP/OSPF/CAPsMAN/队列与策略路由 → 交换机话题现成 |

## 三、人员与联系方式

- **对接人**：Jacek Rokicki
- **邮箱**：mt-support@c3net.pl
- **电话**：+48 506 457 447
- **原始联系字段**：+48 506 457 447 / mt-support@c3net.pl

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCTCE、MTCINE、MTCSE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCTCE` — 流量控制
- `MTCINE` — ISP 互联
- `MTCSE` — 安全
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：CAPsMAN、MikroTik

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328XG-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。

- **业务定位**：华沙近郊一人系统集成商：计算机网络与集成服务；自述技能含「CRS switches and many L2 topics」——交换是熟项。
- **产品线与在售品牌**：项目制选型（MikroTik CRS 系为主打话题），无开放目录。
- **目标行业与场景**：本地企业组网、集成项目、远程运维。
- **团队与规模**：一人个体户——决策快、量小、频次中等。
- **决策链与对接人**：Jacek Rokicki 本人（+48 506 457 447 / mt-support@c3net.pl / j.rokicki@c3net.pl）。
- **技术与认证**：MTCNA+MTCTCE+MTCINE+MTCSE+MTCEWE（来源：CSV 既有 MikroTik 名录记录）。
- **采购与供应链信号**：一人工程商：采购随项目流动，小批量、价格敏感、看中技术对话效率。
- **近期动态与线索**：官网 HTTP 500 故障期——说明业务全凭口碑，方案细节不是他们对外叙述重点，第一封信直接丢规格。
- **与我方契合点**：他的项目里 CRS 话题很熟，我们的 PoE++ 与管理型属于参数直接对账型。
- **风险与注意**：一人工程商小批量，不要谈经销框架——按「测试机+项目价格」模式谈单。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**C3 NET Jacek Rokicki（个体经营，2012-06-15 起）：IT 服务与咨询，主业是计算机网络与系统集成。
  > Usługi i doradztwo IT… Data rozpoczęcia wykonywania działalności gospodarczej: 15.06.2012
  > 来源：https://www.gowork.pl/c3-net-jacek-rokicki,23332517/dane-kontaktowe-firmy
- **【决策链与对接人】**公开目录列示联系方式：马佐夫舍省 Falenty Nowe（ul. Rozbrat 3），邮箱 j.rokicki@c3net.pl。
  > Głównym profilem działalności firmy C3 Net Jacek Rokicki jest Sieci komputerowe i integracja systemów… j.rokicki@c3net.pl
  > 来源：https://panoramafirm.pl/mazowieckie,pruszkowski,falenty_nowe,rozbrat,3/c3_net_jacek_rokicki-axpjfb_fsc.html
- **【团队与规模】**第三方登记为一人个体经营（Jednoosobowa działalność）——决策链最短；主 PKD 6220B 电信类活动。
  > Jednoosobowa działalność · Głowne PKD: 6220B
  > 来源：https://cabb.pl/firma/c-net-jacek-rokicki-8251386484
- **【近期动态与线索】**官网 c3net.pl 本轮抓取 HTTP 500（2026-09-28），门面站故障中，联系走邮箱。
  > Failed to fetch page (HTTP 500) — c3net.pl
  > 来源：https://c3net.pl/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 PoE++（华沙周边项目备货）

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：对标 CRS328：24 口 PoE++ 按项目用，便宜一些、规格可验，给他下一次集成单子一个备选 SKU。
- **要问的问题**：你常规接入层 24 口 PoE 用什么型号、卡在价格还是交期？
- **随附证明**：英文规格对照页（对 CRS328-24P）+ 样品机政策。

### 第 2 次跟进 · 工业非管理 PoE（弱电间/室外小批）

- **推什么**：LT-IS6306G-2GX4GT PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：弱电间/室外点位的小批量采购：宽温宽压、DIN、免配置，替他省去为商用设备加空调/环境改造的成本。
- **要问的问题**：室外/无空调机柜点位用什么供电稳定？
- **随附证明**：宽温报告 + 宽压输入说明 + 单台测试价。

### 第 3 次跟进 · 管理型（BGP/OSPF 项目带起的 VLAN 方案）

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他熟 CRS 与 L2：管理型给他做「路由+交换边界」场景下的高性价比答案，VLAN 分段 + ERPS 环网是对路料。
- **要问的问题**：他的 CRS 项目里 VLAN/冗余怎么做的，成本降到哪档？
- **随附证明**：VLAN/ERPS 收敛实测（英文）+ 配置示例手册打包。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：L3 hardware offload + QinQ on access switching

```text
Hi Jacek,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on CAPsMAN.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328XG-4XS24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
