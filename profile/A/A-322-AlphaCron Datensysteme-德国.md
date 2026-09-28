# AlphaCron Datensysteme

> **评级 A**　|　德国 · Apfelstädt　|　档案编号 `A-322`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | AlphaCron Datensysteme |
| 国家 | 德国 |
| 城市 | Apfelstädt |
| 网站 | https://www.alphacron.de |
| 类型 | 集成商/代理（Allied Telesis） |
| 反向信号 | Allied Telesis（Marvell Prestera 接入层） |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | Marvell Prestera 接入层切入 |
| 数据来源 | Allied Telesis 官方伙伴定位器（?country=germany） |
| 原备注 | 伙伴等级：Resell。 【2026-09-27 A320–A339联络核验】来源等级：official-company。官网（首页/Impressum/隐私页）给contact@alphacron.de、036202/759994（Fax 759997）与Wandersleber Straße 1a, 99192 Apfelstädt，注明Inhaber Marc Pauls；自述为IT系统商并附自营数据中心，列IBM Business Partner、LANCOM Advanced Partner、Ubiquiti、AVM等多品牌；IP记录（RIPE/ipgeolocation）显示AS28748（Marc Pauls AlphaCron Datensysteme）与abuse@alphacron.de，地址与主站一致。 证据：[1](https://www.alphacron.de/) [2](https://www.alphacron.de/datenschutz/) [3](https://www.11880.com/branchenbuch/nesse-apfelstaedt/050331035B43413838/alphacron-datensysteme.html) [4](https://ipgeolocation.io/browse/ip/134.97.52.0) 仅覆盖所述联络/关联事实，不证明投递、在职、采购权、芯片或需求；批次：batch/contact_research_2026-09-27_A320-A339.json#A-322 |

## 三、人员与联系方式

- **邮箱**：contact@alphacron.de、网络记录另有abuse@alphacron.de
- **电话**：—
- **原始联系字段**：contact@alphacron.de（官网Impressum/隐私页）；036202/759994；Inhaber Marc Pauls；网络记录另有abuse@alphacron.de

## 四、品牌与技术栈

**涉及品牌 / 技术**：（未记录）

## 五、跟进策略

场景信号不明确，先摸底：问清他接入层现在用谁的设备、痛点是供电、VLAN 还是环网，再定型号。

初判可参考型号：`LT-S8328XGP-4XS24GT-S`

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第17批.json`。

- **业务定位**：图林根系统商+自营机房+小 ISP 混血（**本批首位**：车行系统线+机房互连+视频监控三线都吃件）。
- **产品线与在售品牌**：全谱系服务（虚拟化/VoIP/光纤熔接/卫星 BK/EPROM 编程等极宽）+自营 DC+DSL 接入。
- **目标行业与场景**：汽车经销集团网点+区域企业+里士多夫居民接入面。
- **团队与规模**：小型全能系统商（主理人 Marc Pauls）。
- **决策链与对接人**：contact@alphacron.de（Impressum，CSV 9-27）。
- **技术与认证**：IBM/HCL Business Partner、LANCOM Adv.（CSV 记录）。
- **采购与供应链信号**：**三位**：车行网点的监控/办公接入层 24 口 PoE+自营机房管理网与互连 DAC/SFP+站点外置宽温件。
- **近期动态与线索**：Erfurt Herrenberg 新 VDSL 区放装=住客接入扩张季。
- **与我方契合点**：24 口 PoE（车行/监控）+DAC/SFP（机房）+工业件（站点）。
- **风险与注意**：个人店口径：德语资料+小批梯价+真实参数。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**图林根 Apfelstädt 的 IT 系统商**连自营数据中心**：24/7 监控、Serverhousing、DSL/VDSL 接入（固定 IP/IPv6 双栈）、光纤熔接、站间互联——**系统商+小 ISP 混血**。
  > IT-Systemhaus mit angeschlossenem Rechenzentrum ‖ 24/7 Monitoring von IT-Infrastrukturen mit aktivem Incident-Management ‖ DSL Zugänge mit festen IP-Adressen ‖ Standleitungen · Standortvernetzung (VPN, MPLS)
  > 来源：https://www.alphacron.de/
- **【目标行业与场景】****汽车经销商全线系统运维**（Volvo/VW/Audi/Skoda/Seat/Nissan/Renault/Dacia 网点）+**网基视频监控（netzwerkbasierte Videoüberwachung）**——24 口监控 PoE 与车行接入层的真消耗。
  > gesamte Systembetreuung im Automotive-Umfeld (Volvo, VW, Audi, Skoda, Seat, Nissan, Renault, Dacia) ‖ netzwerkbasierte Videoüberwachung
  > 来源：https://www.alphacron.de/
- **【决策链与对接人】**contact@alphacron.de（Impressum 正文 Inh. Marc Pauls，CSV 9-27 official-company）；036202/759994。
  > AlphaCron Datensysteme · Inh. Marc Pauls · Wandersleber Straße 1a, 99192 Apfelstädt · Tel.: 036202 / 759994 · eMail: contact@alphacron.de
  > 来源：https://www.alphacron.de/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 车行/监控接入层一页

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行 L2+）
- **切入点**：德语一封：车行网点与网基监控项目的 24 口 PoE 接入层（维保全包现场的 RMA 先行+分点复制梯价）。
- **要问的问题**：车行/监控项目的接入层目前由哪个牌供应？
- **随附证明**：一页报价（德）+ RMA 条款。

### 第 2 次跟进 · 自营机房互连配件

- **推什么**：DAC/AOC + SFP/SFP+ 目录
- **切入点**：Serverhousing/管理网的互连配件批量。
- **要问的问题**：机房互连配件走常备吗？
- **随附证明**：配件一页价卡+兼容表。

### 第 3 次跟进 · 站点宽温件

- **推什么**：LT-IS6310G-2GX8GT（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：DSL/站间点位的宽温小件收口；不回即冻结。
- **要问的问题**：站点外置件有需求吗？
- **随附证明**：工业件一页。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：Access switching — quick question

```text
Hi AlphaCron,

I build managed access switches (PoE and industrial) and your profile came up while I was looking at who is actually doing this work in your market.

What caught my eye is that you work on Resell.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you using for access layer today, and where does it hurt?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328XGP-4XS24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
