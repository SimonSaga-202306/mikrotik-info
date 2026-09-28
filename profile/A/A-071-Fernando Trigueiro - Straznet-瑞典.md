# Fernando Trigueiro / Straznet

> **评级 A**　|　瑞典 · Kungsbacka　|　档案编号 `A-071`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Straznet |
| 国家 | 瑞典 |
| 城市 | Kungsbacka |
| 网站 | straznet.se |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCSE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328GP-4GX24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 20+ 年 IT，近十年专做 MikroTik，自述聚焦 **advanced routing、switching、network design**；为各种规模企业做规划/实施/监控，强调可靠性、可扩展性与安全；巴西+瑞典两国背景，英葡波瑞四语 |

## 三、人员与联系方式

- **对接人**：Fernando Trigueiro
- **邮箱**：info@straznet.se
- **电话**：+46 300 307 80
- **原始联系字段**：+46 300 307 80 / info@straznet.se

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCSE` — 安全

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328GP-4GX24GT-S`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。

- **业务定位**：哥德堡南的全包 IT 服务商：外包 IT 部门+云+网络+安全，正在从服务型升级为自有 SaaS 平台（NextCloud 系）。
- **产品线与在售品牌**：服务合同制；伙伴栈 Microsoft/Bitdefender/Synology/MikroTik——MikroTik 在其交付体系里有正式位置。
- **目标行业与场景**：Kungsbacka/哥德堡地区中小企业的整体 IT 外包；他自建 SaaS 的机房与交付客户现场都是交换场景。
- **团队与规模**：本地化公司团队（博客署名 Peter Straznyk 等），承诺全天候响应——服务密度高。
- **决策链与对接人**：Fernando Trigueiro（+46 300 307 80 / info@straznet.se，CSV 名录：MTCNA+MTCSE，近十年专做 MikroTik）。
- **技术与认证**：MTCNA+MTCSE + 20 年 IT 经验（CSV 记录）；自述专注 advanced routing、switching、network design。
- **采购与供应链信号**：外包模式=客户现场设备大包采购+自有 SaaS 机房设备——复购稳定；扩张期在评估新供应源。
- **近期动态与线索**：SaaS 转型（2026-06 官宣）+ AI 服务线（2026-08 博客）双线扩张——机房与交付量都在涨。
- **与我方契合点**：客户现场接入层=24 口 PoE；SaaS 机房接入/带外=10G 机型；交付工具箱=工业件备件。
- **风险与注意**：他重「服务品质」叙事：首轮给规格与质保承诺，别用低价冲锋抢占注意力。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**官网抬头：Kungsbacka 与哥德堡的 IT 伙伴，全天候（全年无休）专家支持。
  > IT-PARTNER I KUNGSBACKA OCH GÖTEBORG — Straznet är din IT-leverantör för snabb support, personlig service och bekymmersfri IT. Dygnet runt, alla dagar om året.
  > 来源：https://straznet.se/
- **【产品线与在售品牌】**四大板块：外包 IT 部门、云、网络（安装/优化/排障/安全）、IT 安全；合作伙伴栏挂 Microsoft/Bitdefender/Synology/MikroTik。
  > Extern IT-avdelning · Moln · Nätverk — Vi hjälper er med allt från installation och optimering till felsökning och säkerhet · IT-säkerhet（合作伙伴 Logo：Microsoft、Bitdefender、Synology、MikroTik）
  > 来源：https://straznet.se/
- **【近期动态与线索】**2026-06 官宣上线 NextCloud+EuroOffice 自有 SaaS（自述 25 年云与运维经验），转型正式 SaaS 公司——业务扩张期。
  > Nu tar vi på Straznet, med 25 års erfarenhet av molntjänster och driftsäkerhet, ett stort steg framåt: vi lanserar vår nya SaaS-lösning och blir ett fullfjädrat SaaS-företag.（2026-06-18 博客）
  > 来源：https://straznet.se/
- **【团队与规模】**办公点 Kabelgatan 5, 434 37 Kungsbacka；总机 0300-30 780 / info@straznet.se；AI 博客显示团队在跟新技术线。
  > Kabelgatan 5, 434 37, Kungsbacka · 0300-30 780 · info@straznet.se · 2026-08-07 — AI för företag – tre nivåer i praktiken（博客）
  > 来源：https://straznet.se/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（外包客户现场接入）

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他给中小企业全包 IT：客户现场 AP/话机/监控一张网——24 口 PoE++ 做交付标配，帮他把「无忧 IT」的成本打下来。
- **要问的问题**：客户现场接入层现在标准化在什么型号？
- **随附证明**：规格对照 + 质保政策 + 到岸价目（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（仓储/车间客户）

- **推什么**：LT-IS6310G-2GX8GT PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：制造/仓储类客户的无空调区点位：宽温 DIN 免配置——他工具箱里的省心备件。
- **要问的问题**：工业类客户现场的交换故障多吗？用什么替换策略？
- **随附证明**：宽温报告 + DIN 图 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（SaaS 机房+客户标准件）

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：双线：他 SaaS 机房接入/带外管理段 + 外包客户网统一 VLAN/ERPS 模板——标准件思维对得上他的规模化打法。
- **要问的问题**：客户网的标准配置模板里接入层定型了吗？
- **随附证明**：VLAN/ERPS 模板 + CLI 速查 + 实测。

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
Hi Fernando,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on switching.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328GP-4GX24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
