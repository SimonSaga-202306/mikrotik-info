# Axbyte

> **评级 A**　|　瑞典 · Järfälla / Älvsjö　|　档案编号 `A-064`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Axbyte |
| 国家 | 瑞典 |
| 城市 | Järfälla / Älvsjö |
| 网站 | axbyte.se |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 公司内 2 人：Leo（瑞典 MikroTik 讲师）+ Fredrik Hellgren（MTCSWE） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ Leo 自述 **做了 21 年 MikroTik，是瑞典（SE）MikroTik RouterOS 官方讲师**，全领域覆盖：防火墙、流量管理、**switching、VLAN**、CAPsMAN、IPv6、OSPF/OSPFv3/iBGP/eBGP、脚本、有线无线设计、认证培训 → 瑞典最强的个人影响力节点 |

## 三、人员与联系方式

- **邮箱**：leo@axbyte.se、support@axbyte.se
- **电话**：+46 70 591 5987、+46 8 586 195 00
- **原始联系字段**：Leo +46 70 591 5987 / leo@axbyte.se；Fredrik Hellgren +46 8 586 195 00 / support@axbyte.se

## 四、品牌与技术栈

**持有认证**：MTCSWE

- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：CAPsMAN、MikroTik、RouterOS

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

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。

- **业务定位**：斯德哥尔摩西南（Järfälla/Älvsjö）数据中心与网络服务商：办公室互连 + 自有服务器机房托管 + 外包 NOC，走「全包伙伴」路线。
- **产品线与在售品牌**：服务合同制（含硬件配套）：Datakom 方案、机柜托管、网络代维；CSV 名录显示 Leo 为瑞典 MikroTik 官方讲师、Fredrik Hellgren 持 MTCSWE。
- **目标行业与场景**：瑞典中小企业全包 IT/网络；机房托管客户的接入层与带外管理网。
- **团队与规模**：小型精干团队，愿景「瑞典本细分市场最好的数据通信服务」、承诺「blixtsnabb support」（极速支持）。
- **决策链与对接人**：Leo（21 年 MikroTik、SE 官方讲师，+46 70 591 5987 / leo@axbyte.se）与 Fredrik Hellgren（MTCSWE）；两人即全部技术决策。
- **技术与认证**：公司双人持证（讲师+MTCSWE，CSV 名录记录）——技术对话可以直接上 L2/L3 深层。
- **采购与供应链信号**：机房+NOC 模式=标准化 hardware stack 复购；官网明说要扩产品组合——正是递资料的好时候。
- **近期动态与线索**：「持续扩充产品组合」自述=供应商库在重整；抢在他确定新标准件前上门。
- **与我方契合点**：机房接入层/带外管理=24 口与 10G 机型；客户站点互连的室外/弱电点=工业件；讲师牌照=可以把我们设备带进课堂。
- **风险与注意**：他卖「品质与服务」不打价格战：首轮别报价，先给规格与实测建立技术信任。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**官网定位「整体数据通信方案商」：把客户的完整数据通信服务包下来做。
  > Helhetslösningar inom Datakom · Datakom-lösningar – förenklat. · Vi superladdar din Datakom-tjänst så du kan fokusera på det ditt företag gör bäst.
  > 来源：https://axbyte.se/
- **【产品线与在售品牌】**三条业务线：办公室/系统/站点互连、自建服务器机房托管、外包 NOC 运维监控——有机房就有持续网络设备需求。
  > Sammankoppling av kontor, system, platser, gamla som nya · Co-location — Ställ din egna server eller nätverksenhet i våra serverhallar… · NOC-tjänst — Vi hjälper ert företag med er Nätverksdrift och övervakning.
  > 来源：https://axbyte.se/
- **【近期动态与线索】**官网自述「一直在看如何扩充产品组合来满足客户」——产品线扩张窗口敞开。
  > Vi tittar hela tiden på hur vi kan utöka vår produktportfölj för att kunna erbjuda just det våra kunder eftersöker.
  > 来源：https://axbyte.se/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（机房接入层/客户站点）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他的托管机房与客户站点互连都需要可靠接入层：24 口 PoE++ + 4×10G 上行，给他的「整体方案」做标准件候选。
- **要问的问题**：机房接入层现在标准化在什么型号上？
- **随附证明**：规格书 + MTBF/功耗数据 + 万兆上行实测（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（机房走道/远程点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：机柜走廊监控/AP、客户现场无空调弱电间：宽温 DIN 免配置，NOC 代维场景里最省心的一段。
- **要问的问题**：代维客户现场的零散 PoE 点位现在怎么处理？
- **随附证明**：宽温报告 + DIN 图 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（NOC 标准件 + 讲师实验台）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：双线：NOC 托管网统一 VLAN/ERPS 模板（固件标准化=省运维工时）；Leo 的讲师身份让设备进瑞典 MikroTik 课堂。
- **要问的问题**：Leo 的课用什么交换机型做演示？标准件名单要不要加一个实测候选？
- **随附证明**：VLAN/ERPS 模板 + CLI 速查 + 实验机成本价。

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
Hi Axbyte,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on switching, VLAN and CAPsMAN.

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
