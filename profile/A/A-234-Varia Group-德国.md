# Varia Group

> **评级 A**　|　德国 · Chemnitz　|　档案编号 `A-234`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Varia Group |
| 国家 | 德国 |
| 城市 | Chemnitz |
| 网站 | https://www.varia.org |
| 类型 | 分销（Netonix 授权） |
| 反向信号 | Netonix 授权渠道（WISP 接入层交换机） |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | WISP 接入层替换 |
| 数据来源 | Netonix 官方分销/代理名录 |
| 原备注 | 【2026-09-23 用户裁决·保留】Netonix 交换机采用 **Vitesse** 芯片，并非 Marvell，严格按「Marvell 接入层生态」标准属于圈外；用户 2026-09-23 明确「先这样吧，没必要删」，故本条保留。注意：对其**不能使用「同芯片」话术**（详见 Netonix_WISP替换矩阵_2026-09.md），切入点应放在交期、宽温、上行与价格上。 Netonix 德国分销。 【2026-09-27 A210–A239联络核验】来源等级：official。旧/en/kontakt/实际404，改查有效/en/imprint/正文：VARIA System GmbH、Chemnitz、HRB26881、DE279278184、Sven Grimpe/Sven Huth。与A031公司名/官网属于强关联候选，不因品牌别名擅自合并或变号，前49不改。既有Netonix/Vitesse特批保留仍有效，不能说同Marvell芯片。 证据：[1](https://www.varia.org/en/imprint/) [2](https://www.varia.org/en/kontakt/) 仅证实对应联络字段/所述身份线索，不证明投递、当前任职、采购权、芯片或需求。批次：batch/contact_research_2026-09-27_A210-A239.json#A-234 |

## 三、人员与联系方式

- **邮箱**：info@varia.org
- **电话**：+49-371-400-7682
- **原始联系字段**：info@varia.org（官网正文公开；未验证投递）；原入口：+49-371-400-7682

## 四、品牌与技术栈

**涉及品牌 / 技术**：（未记录）

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第12批.json`。

- **业务定位**：Chemnitz 25 年分销运营体：用户裁决保留户（Vitesse 圈外标签在档）；分销/白标代发/多市场电商一体。
- **产品线与在售品牌**：分销服务（厂商品牌分销）+自有商城+市场代发+白标中性发货+定制系统集成。
- **目标行业与场景**：德/欧多市场电商渠道+B2B 分销网络。
- **团队与规模**：中型运营体（自有物流与流程系统）。
- **决策链与对接人**：info@varia.org（官网正文，CSV 9-27）；+49 371 400…。
- **技术与认证**：（分销职能型；CSV 9-23 用户裁决保留）。
- **采购与供应链信号**：**双向互补**：其分销/白标能力=SmartByte 类目的德国履约与上架渠道；其 WISP 商户客群缺工业 PoE 宽温线。
- **近期动态与线索**：官网 2026 版改版强调白标/履约=正在向品牌方卖履约能力——正合我们「你出货品我出品类」结构。
- **与我方契合点**：分销上架提案（接入层/CCTV 小件）+按其白标条款中性代发。
- **风险与注意**：Netonix/Vitesse 条目不谈替代（用户裁决保留在档）；只做其目录空档与履约互补。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**Chemnitz 25+ 年分销/电商/代发（Fulfillment & Dropshipping）：「我们搬运你的产品」。
  > Wir bewegen Ihre Produkte. Wir machen Ihre Produkte sichtbar, verfügbar und erfolgreich. Seit über 25 Jahren.
  > 来源：https://www.varia.org/
- **【产品线与在售品牌】****White Label Service：以你的名义中性发货**——中性货/白标是其能力项，与我方中性货打法结构同构。
  > White Label Service — Alle Sendungen erfolgen neutral in Ihrem Namen – ohne VARIA-Branding, mit Lieferscheinen und Verpackungen in Ihrer Markenidentität.
  > 来源：https://www.varia.org/
- **【目标行业与场景】**自有店铺+多市场直销（Amazon/eBay/Galaxus/Conrad/MediaMarkt/Kaufland），B2B&B2C 通吃。
  > Über eigene Shops und etablierte Marktplätze wie Amazon, eBay, Galaxus, Conrad, MediaMarkt oder Kaufland übernimmt VARIA die Direktvermarktung im B2B- und B2C-Bereich
  > 来源：https://www.varia.org/
- **【风险与注意】**CSV 裁决记录：其 Netonix 条目交换机为 Vitesse 芯片、严格按 Marvell 生态标准属圈外；用户 2026-09-23 明确「先这样」保留——本户只做互补、不谈生态归属。
  > （CSV 2026-09-23 用户裁决·保留）Netonix 交换机采用 Vitesse 芯片，并非 Marvell……用户明确保留
  > 来源：https://www.varia.org/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 分销上架提案（接入层/CCTV 小件）

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行 L2+）
- **切入点**：向其分销口递交品牌上架提案：24 口 PoE 接入层+监控小件类目，分销条款+白标代发可选。
- **要问的问题**：你们现在接受新网络硬件品牌上架吗？走什么评估流程？
- **随附证明**：品牌一页提案（德/英）+ 分销条款模板。

### 第 2 次跟进 · 白标代发互补

- **推什么**：—（履约方案）
- **切入点**：按其白标服务条款：我们供货他们代发或反之，跑通跨境中性履约结构。
- **要问的问题**：白标代发的入仓/系统对接条件是什么？
- **随附证明**：履约流程一页 + 系统对接要点。

### 第 3 次跟进 · WISP 客群目录空档（工业宽温 PoE）

- **推什么**：LT-IS6310G-2GX8GT + 宽温收发器
- **切入点**：其 WISP 商户客户群目录里尚无工业宽温 PoE/收发器线——类目空档提案。
- **要问的问题**：户外/宽温件类目有上架空档吗？
- **随附证明**：类目对比一页 + CE 包。

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
Hi Varia,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on WISP.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

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
