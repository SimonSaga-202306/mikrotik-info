# Katsariotis Dimitrios / IME

> **评级 A**　|　希腊 · Patra　|　档案编号 `A-025`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | IME |
| 国家 | 希腊 |
| 城市 | Patra |
| 网站 | ime.com.gr |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCSE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424DGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | 20+ 年网络基础设施设计实施管理支持；专长明确含 **switching**；路由、防火墙、无线、流量与带宽管理、IPSec/L2TP/SSTP/PPP/EoIP；云架构与 IT 管理 |

## 三、人员与联系方式

- **对接人**：Katsariotis Dimitrios
- **邮箱**：dkats@ime.com.gr
- **电话**：+30 697 762 8291
- **原始联系字段**：+30 697 762 8291 / dkats@ime.com.gr

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCTCE、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCTCE` — 流量控制
- `MTCSE` — 安全

**涉及品牌 / 技术**：IPsec、MikroTik

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**STC-424XGGPM-440W（Saga）（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`STC-424DGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：帕特雷的信息化公司 ΙΜΕ（软件开发为主：水务计费 ΔΕΥΑ、餐饮点单、门店零售 imeRetail，另做硬件与软件全支持），在雅典设第二办公室。
- **产品线与在售品牌**：以自研软件 + 配套硬件为主；网络方案按项目采购（顾问本人持 MikroTik 多证）。
- **目标行业与场景**：公共事业（水务/排水）、餐饮连锁、零售门店链——门店/站点分散、需要稳定的门店网络与实时数据回传。
- **团队与规模**：帕特雷 + 雅典两地办公；官网强调「全希腊合作伙伴网络 + 365 天支持」。
- **决策链与对接人**：Katsariotis Dimitrios（dkats@ime.com.gr；+30 697 762 8291）；公司总线 +30 2610 452363 / info@ime.com.gr。
- **技术与认证**：MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCSE，自述 20+ 年网络基础设施设计/实施/管理，专长明确含 **switching**。
- **采购与供应链信号**：软件公司的硬件随项目走：门店改造、水厂站点、客户机房升级；对「一次配齐 + 远程可维护」的设备接受度高。
- **近期动态与线索**：官网 2025 年更新（imeFoodService、ΔΕΥΑ 应用），位于帕特雷 Αγ. Διονυσίου 20–22 与雅典 Θρασυμάχου 8。
- **与我方契合点**：水务/门店场景 = 分散站点接入：24 口 PoE（门店/站点）、工业款（水厂/泵站现场）、管理型（多站点统一配置）。
- **风险与注意**：其公司主业是软件，网络采购量取决于项目；联系时直奔「门店/站点接入层」而不是大而全。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**公司自述：覆盖企业信息化全谱，硬件软件全支持，总部帕特雷、服务全希腊。
  > Καλύπτουμε όλο το φάσμα της Μηχανογράφησης-Μηχανοργάνωσης οποιασδήποτε μορφής επιχείρησης. Έχοντας έδρα την Πάτρα … πλήρεις υπηρεσίες υποστήριξης (Hardware και Software) σε όλη την Ελλάδα
  > 来源：https://ime.com.gr/
- **【目标行业与场景】**产品线即行业线索：水务、餐饮点单、零售连锁。
  > Εφαρμογές – ΔΕΥΑ（Πλήρης διαχείριση διαδικασιών ΔΕΥΑ）｜imeFoodService – Σύστημα παραγγελιοληψίας｜imeSales – Eμπορολογιστική Eφαρμογή｜imeRetail – λύση για αλυσίδες καταστημάτων
  > 来源：https://ime.com.gr/
- **【团队与规模】**两地办公与全国支持承诺。
  > Αγ. Διονυσίου 20 – 22, 262 23, Πάτρα｜Θρασυμάχου 8, 104 42, Αθήνα；365 ημέρες τον χρόνο υποστήριξη｜Πανελλαδικό δίκτυο συνεργατών
  > 来源：https://ime.com.gr/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：门店/站点标准包：24 口 PoE++ 一次配齐 AP、摄像头、POS 终端；远程看门狗让他们少跑门店。
- **要问的问题**：他们给连锁客户做门店网络时，接入层现在怎么配？
- **随附证明**：门店标准包报价单（交换机+AP+线材）+ 看门狗演示。

### 第 2 次跟进 · 工业级非管理 PoE（水厂/泵站）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：水务站点的户外柜：宽温宽压、DIN、免配置，停电恢复自动回到工作状态。
- **要问的问题**：水务/排水项目里有没有户外站点？
- **随附证明**：宽温报告 + 户外柜接线图 + 备件政策。

### 第 3 次跟进 · 管理型 PoE（多站点统一模板）

- **推什么**：STI-480DGGM（Saga） PoE 版（8G + 4×2.5G SFP）
- **切入点**：他们给同一客户维护几十个门店/站点：统一 VLAN 模板 + ERPS 冗余 + SNMP 监控，一套模板复制。
- **要问的问题**：多站点客户愿不愿意用统一交换模板运维？
- **随附证明**：配置模板 + SNMP/MIB 清单 + ERPS 实测。

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
Hi Katsariotis,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on switching and IPsec.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

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
