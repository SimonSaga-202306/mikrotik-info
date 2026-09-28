# Alessandro Campanella / 1off

> **评级 A**　|　意大利 · Mogliano Veneto　|　档案编号 `A-034`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | 1off |
| 国家 | 意大利 |
| 城市 | Mogliano Veneto |
| 网站 | 1off.it |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCIPv6E+MTCSE+MTCSWE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 持 MTCSWE；2003 年起做 MikroTik、2007 年起当讲师；**Routing + Switching + Wireless + QoS + VPN + 安全**；网络设计/迁移/排障；为全球运营商与系统集成商服务 → 给 SI 供货的机会 |

## 三、人员与联系方式

- **对接人**：Alessandro Campanella
- **邮箱**：a.campanella@1off.it
- **电话**：+39 320 299 7787
- **原始联系字段**：+39 320 299 7787 / a.campanella@1off.it

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCIPv6E、MTCSE、MTCSWE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**STC-424XGGPM-440W（Saga）（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`STC-424XGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：1off（Mogliano Veneto）：面向运营商/ISP/WISP/系统集成商/企业的「Strategic Network Mentor」（架构指导 + on-the-job 培训），同时是官方 MikroTik 培训中心。
- **产品线与在售品牌**：MikroTik 官方培训 + 架构咨询（2003 年起做 MikroTik、2007 年起当讲师）；无代理绑定，按架构需要选型。
- **目标行业与场景**：ISP/WISP、SI、企业网络的架构重设计、风险降低与演进路线；另办 RouterOS Competition（Arcade/Time Attack 有全球排行榜）与 Insights 技术文章。
- **团队与规模**：个人/小型顾问团队（决策链 = Alessandro Campanella 本人）。
- **决策链与对接人**：Alessandro Campanella（a.campanella@1off.it；+39 320 299 7787），持 MTCSWE+MTCEWE 等。
- **技术与认证**：MikroTik 认证讲师/顾问（MTCNA+MTCIPv6E+MTCSE+MTCSWE+MTCEWE）；咨询内容是「架构、迁移、排障、培训」四件事。
- **采购与供应链信号**：架构顾问能写规格（spec-in）；客户项目设备清单由他建议，但他自己不压货——需要「可被客户采购的清晰 SKU 与文档」。
- **近期动态与线索**：官网 2026 年在推 Competition（互动题库，全球排行）与 Insights 内容库；咨询主打「先评估再演进」。
- **与我方契合点**：他做 ISP/WISP 架构：接入层 PoE、工业现场盒、管理型环网都是他架构里的常规元件；MTCSWE 背景让他能直接评估我们的交换实现。
- **风险与注意**：架构顾问话语权大但不直接下单：要把材料做到「他能交给客户采购」的程度（规格书/合规/交期）。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**Strategic Network Mentor 的定位与服务对象。
  > 1off affianca gli operatori come Strategic Network Mentor … La consulenza 1off è pensata per operatori, integratori e organizzazioni che vogliono rendere la loro rete più affidabile e scalabile: ISP e WISP｜System integrator｜Organizzazioni enterprise
  > 来源：https://www.1off.it/
- **【产品线与在售品牌】**官方 MikroTik 培训中心 + 实操实验室。
  > Siamo il Training Center ufficiale MikroTik e offriamo corsi personalizzati per operatori, ISP e system integrator … Laboratori pratici hands-on con equipaggiamento reale.
  > 来源：https://www.1off.it/
- **【近期动态与线索】**自有互动内容（RouterOS Competition）与知识库，用于拉新与社群运营。
  > MikroTik RouterOS Competition — Quiz interattivi su MikroTik RouterOS … Classifica Globale；Knowledge Hub — Insights Tecnici
  > 来源：https://www.1off.it/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他在给 ISP/SI 做架构评估：把 24 口 PoE++ 作为「接入层标准件」放进他的评估清单，附可交给客户采购的规格与测试方法。
- **要问的问题**：他给 ISP 做接入层标准时，PoE 交换机的筛选条件是什么？
- **随附证明**：规格书 + 实测方法 + 客户可直接用的选型页。

### 第 2 次跟进 · 工业级非管理 PoE（现场/塔站）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：WISP 现场与电箱：宽温 DIN 免配置；他一向强调「减少外部依赖」，免维护设计正好。
- **要问的问题**：他的 ISP 客户里非机房点位占比多大？
- **随附证明**：宽温/宽压报告 + 现场箱方案 + 样品。

### 第 3 次跟进 · 管理型 PoE（架构标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：把管理型交换机写进他的「接入层参考架构」：VLAN/QinQ + ERPS + SNMP，一次评估长期复用。
- **要问的问题**：他愿不愿意把我们的交换机列进参考架构的可选清单？
- **随附证明**：参考架构图 + ERPS/组播实测 + MIB/CLI 文档。

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
Hi Alessandro,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on switching.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

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
