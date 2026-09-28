# Neobits

> **评级 A**　|　美国 · California　|　档案编号 `A-276`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Neobits |
| 国家 | 美国 |
| 城市 | California |
| 网站 | https://www.neobits.com |
| 类型 | WISP 集成商/代理（Netonix） |
| 反向信号 | Netonix 授权渠道（WISP 接入层交换机） |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | WISP 接入层替换 |
| 数据来源 | Netonix 官方分销/代理名录 |
| 原备注 | 【2026-09-23 用户裁决·保留】Netonix 交换机采用 **Vitesse** 芯片，并非 Marvell，严格按「Marvell 接入层生态」标准属于圈外；用户 2026-09-23 明确「先这样吧，没必要删」，故本条保留。注意：对其**不能使用「同芯片」话术**（详见 Netonix_WISP替换矩阵_2026-09.md），切入点应放在交期、宽温、上行与价格上。 Netonix 代理商。 【2026-09-27 A260–A279联络核验】来源等级：official-company。官网联系页正文给sales@neobits.com、1-866-636-2487与Santa Clara总部地址，并列出供应商入口vendors@与客服customercare@；电话与名录一致。第三方政府采购资料重复同一组邮箱，仅旁证。 证据：[1](https://www.neobits.com/contactUs) [2](https://www.neobits.com/) 仅覆盖所述联络/关联事实，不证明投递、在职、采购权、芯片或需求；批次：batch/contact_research_2026-09-27_A260-A279.json#A-276 |

## 三、人员与联系方式

- **邮箱**：sales@neobits.com、vendors@neobits.com
- **电话**：1-866-636-2487
- **原始联系字段**：sales@neobits.com（官网联系页正文；未测试投递）；供应商入口：vendors@neobits.com；原入口：1-866-636-2487

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

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。

- **业务定位**：加州 B2B 大卖场（基站基础设施是头部类目）——按**供应商入驻**逻辑走 vendors@，别的户都是对客推销、这户是上架。
- **产品线与在售品牌**：万货电商+基站件/监控件类目；Netonix 渠道（CSV）。
- **目标行业与场景**：全美 SMB/机构买家（长尾动销）。
- **团队与规模**：大型电商后台（Item#/MPN/UPC 体系完整）。
- **决策链与对接人**：vendors@neobits.com（供应商入口，CSV 9-27）；sales@ 客服线。
- **技术与认证**：Netonix 授权渠道（CSV；Vitesse 圈外标签在档）。
- **采购与供应链信号**：**SKU 化供货商逻辑**：24 口 PoE/工业件按 UPC/MPN 上架资料包直达 vendors@（比测量/梯价/代发一体）。
- **近期动态与线索**：海量 SKU 持续在册=长尾类目常年扩。
- **与我方契合点**：24 口 PoE 上架 SKU 包+工业件窄线。
- **风险与注意**：Netonix 用户裁决保留户：绝不提芯片；不与客服线谈合作（只走 vendors@）。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**加州 B2B 百货级电商「where business goes shopping」：类目录从标签打印机到色谱膜——其中**基站基础设施/基站天线/视频监控系统**为头部类目（Netonix 渠道身份 CSV 9-23 用户裁决保留户）。
  > Neobits.com is where business goes shopping. ‖ Top Categories — Base Station Infrastructure · Base Station Antennas · Video Surveillance Systems
  > 来源：https://www.neobits.com/
- **【采购与供应链信号】**货架含 NewMar DIN 轨 DC UPS 等工业件（在库标价直出）=工业/基站供电件已在动销；**vendors@neobits.com 为供应商入口**（CSV 9-27）——我们按「供应商入驻」而非「客户推销」逻辑走。
  > NewMar - DIN-UPS 24-20 - DIN rail mount DC UPS Power System ‖ （CSV 2026-09-27 记录）官网联系页正文 sales@；供应商入口 vendors@neobits.com
  > 来源：https://www.neobits.com/
- **【风险与注意】**【2026-09-23 用户裁决·保留】Netonix 采用 Vitesse 芯片、非 Marvell，严格标准属圈外；用户明确保留——**禁用「同芯片」话术**，切入只放交期/宽温/上行/价格。
  > （CSV 2026-09-23 用户裁决）Netonix=非 Marvell 圈外，「先这样吧，没必要删」；切入应放在交期、宽温、上行与价格上
  > 来源：https://www.neobits.com/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · vendors@ 供应商入驻一页（SKU 包）

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行 L2+）
- **切入点**：对 vendors@：供应商入驻提案——24 口 PoE++ 接入层（SKU 资料包：UPC/规格图/比价表/梯价/代发条款一体）。
- **要问的问题**：网络交换类目接受新供应商入驻吗？需要什么资料？
- **随附证明**：SKU 上架资料包（英）。

### 第 2 次跟进 · 工业窄线 SKU

- **推什么**：LT-IS6310G-2GX8GT 等窄线
- **切入点**：基站基础设施类目的工业宽温件窄线 SKU 包。
- **要问的问题**：工业类目的宽温件窄线要上架吗？
- **随附证明**：窄线 SKU 包。

### 第 3 次跟进 · 条款收口

- **推什么**：—（条款）
- **切入点**：代发/批发条款收口；不回即冻结。
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
Hi Neobits,

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
