# Invictus

> **评级 A**　|　美国 · Tigard, OR　|　档案编号 `A-280`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Invictus |
| 国家 | 美国 |
| 城市 | Tigard, OR |
| 网站 | https://www.invictuswireless.com |
| 类型 | WISP 集成商/代理（Netonix） |
| 反向信号 | Netonix 授权渠道（WISP 接入层交换机） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | WISP 接入层替换 |
| 数据来源 | Netonix 官方分销/代理名录 |
| 原备注 | 【2026-09-23 用户裁决·保留】Netonix 交换机采用 **Vitesse** 芯片，并非 Marvell，严格按「Marvell 接入层生态」标准属于圈外；用户 2026-09-23 明确「先这样吧，没必要删」，故本条保留。注意：对其**不能使用「同芯片」话术**（详见 Netonix_WISP替换矩阵_2026-09.md），切入点应放在交期、宽温、上行与价格上。 Netonix 代理商。 【2026-09-27 A280–A299联络核验】来源等级：official-company。官网联系页正文给sales@/info@/accounting@/orders@invictuswireless.com、1.503.635.2562 x1与17435 Wren Ct地址；Deliberant北美经销页把Invictus Networks列为美加authorized reseller并给sales@invictusnetworks.com。该行为2026-09-23保留的Netonix豁免行，本轮不改等级与话术。 证据：[1](https://www.invictuswireless.com/Contact-Us-s/89.htm) [2](https://deliberant.com/north-america) [3](https://www.facebook.com/InvictusWireless/) 仅覆盖所述联络/关联事实，不证明投递、在职、采购权、芯片或需求；批次：batch/contact_research_2026-09-27_A280-A299.json#A-280 |

## 三、人员与联系方式

- **邮箱**：sales@invictuswireless.com、sales@invictusnetworks.com
- **电话**：1-503-635-2562
- **原始联系字段**：sales@invictuswireless.com（官网联系页正文；同页另有info@/accounting@/orders@分工邮箱；未测试投递）；候选：sales@invictusnetworks.com（Deliberant北美经销页，同一实体待核）；原入口：1-503-635-2562

## 四、品牌与技术栈

**涉及品牌 / 技术**：（未记录）

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

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。

- **业务定位**：俄勒冈无线/安防电商（室外 WISP 件+监控门禁类目）——**UniFi 监控线的 24 口大 PoE 空档与 Inter Project 同型**。
- **产品线与在售品牌**：Ubiquiti 精选（UISP/UVC）+Netonix（CSV）+安防/自动化类目。
- **目标行业与场景**：楼宇-园区-城市级室外无线与监控客群。
- **团队与规模**：中型电商（Volusion 店）。
- **决策链与对接人**：sales@invictuswireless.com（官网联系页，CSV 9-27）；1-503-635-2562。
- **技术与认证**：Netonix 授权渠道（CSV；Vitesse 圈外标签在档）。
- **采购与供应链信号**：UVC/UISP 监控项目的大口数 PoE 接入层（UniFi 交换薄位）+站点宽温件；Netonix 位只谈交期/宽温/上行/价格。
- **近期动态与线索**：UISP-CONSOLE 特价置顶=流量入口在 UniFi 生态，话音接得上。
- **与我方契合点**：24 口监控 PoE（UniFi 项目旁位）+工业窄线。
- **风险与注意**：Netonix 裁决话规；候选 invictusnetworks.com 域未核不引用。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**俄勒冈 Tigard 的无线/网络/安防电商：三大卖场类目=室内网络/**室外无线网络**（楼宇-园区-城市级，licensed+unlicensed）/**监控与门禁**；Netonix 授权渠道（CSV）。
  > Networking, Security & Wireless ‖ Outdoor Wireless Networking Technologies — licensed and unlicensed products to connect and enhance spaces across buildings to campuses to cities ‖ Surveillance & Access Control
  > 来源：https://www.invictuswireless.com/
- **【产品线与在售品牌】**在售精选 Ubiquiti 系（UISP-CONSOLE、UVC-G4-IRExtender、UVC-AI-THETA 360° 相机等）——**UniFi 监控线活跃**；Netonix 渠道（CSV）；候选同实体域 invictusnetworks.com（Deliberant 北美经销页，待核）。
  > UISP-CONSOLE — UISP Host Console with Integrated Switch and Multi-Gig Ethernet Gateway by Ubiquiti Networks ‖ UVC-AI-THETA UniFi Protect 8/9MP IP Camera ‖ （CSV 2026-09-27 记录）同页另有 info@/accounting@/orders@ 分工邮箱；候选 sales@invictusnetworks.com 同一实体待核
  > 来源：https://www.invictuswireless.com/
- **【决策链与对接人】**sales@invictuswireless.com 官网联系页正文（CSV 9-27 official-company；info@/accounting@/orders@ 分工同页）。
  > （CSV 2026-09-27 记录）sales@invictuswireless.com（官网联系页正文）；official-company
  > 来源：https://www.invictuswireless.com/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · UniFi 监控项目 24 口 PoE 一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）
- **切入点**：对 sales@：UVC/UISP 监控项目 15 路以上的大口数 PoE 接入层上架提案（梯价+代发）。
- **要问的问题**：UVC 项目的大口数 PoE 目前导购指向哪款？
- **随附证明**：一页提案（英）+ PoE 预算表。

### 第 2 次跟进 · 室外站点宽温件

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：室外无线站点的机柜宽温小件与收发器窄线（交期/宽温/价格档位——不提芯片）。
- **要问的问题**：室外站点机柜里的接入小件有宽温位吗？
- **随附证明**：工业件一页。

### 第 3 次跟进 · 条款收口

- **推什么**：—（条款）
- **切入点**：梯价/代发条款收口；不回即冻结。
- **要问的问题**：（无需回）条款留档。
- **随附证明**：条款一页（英）。

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
Hi Invictus,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on WISP.

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
