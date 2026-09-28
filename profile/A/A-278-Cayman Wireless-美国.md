# Cayman Wireless

> **评级 A**　|　美国　|　档案编号 `A-278`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Cayman Wireless |
| 国家 | 美国 |
| 城市 | — |
| 网站 | https://www.caymanwireless.com |
| 类型 | WISP 集成商/代理（Netonix） |
| 反向信号 | Netonix 授权渠道（WISP 接入层交换机） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | WISP 接入层替换 |
| 数据来源 | Netonix 官方分销/代理名录 |
| 原备注 | 【2026-09-23 用户裁决·保留】Netonix 交换机采用 **Vitesse** 芯片，并非 Marvell，严格按「Marvell 接入层生态」标准属于圈外；用户 2026-09-23 明确「先这样吧，没必要删」，故本条保留。注意：对其**不能使用「同芯片」话术**（详见 Netonix_WISP替换矩阵_2026-09.md），切入点应放在交期、宽温、上行与价格上。 Netonix 代理商。 【2026-09-27 A260–A279联络核验】来源等级：public-register。官网正文确认其Authorized Partner Brands含MikroTik与Netonix，但联系入口邮箱在本轮抓取中被遮罩、正文未显示；sales@caymanwireless.com仅有第三方目录结构化数据支持，故按public-register处理，未验证投递、未测试。 证据：[1](https://www.caymanwireless.com/) [2](https://www.yellowpages.com/harlingen-tx/mip/cayman-wireless-inc-461428339) [3](https://www.manta.com/c/mryrnqs/cayman-wireless-inc) 仅覆盖所述联络/关联事实，不证明投递、在职、采购权、芯片或需求；批次：batch/contact_research_2026-09-27_A260-A279.json#A-278 |

## 三、人员与联系方式

- **邮箱**：sales@caymanwireless.com
- **电话**：1-956-825-0710
- **原始联系字段**：sales@caymanwireless.com（第三方目录结构化数据，官网联系入口为遮罩；待核；未测试投递）；原入口：1-956-825-0710

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

- **业务定位**：美国 WISP 老牌 VAR（2004 起，Ubiquiti/MikroTik/Cambium/Netonix/Tycon 墙）——监控+站点供电件对口。
- **产品线与在售品牌**：无线天线/电台/配件分销+编程配置服务（MikroTik RouterOS/Grandstream 逻辑）+监控+NAS。
- **目标行业与场景**：WISP 与任务关键网络客群（国内外）。
- **团队与规模**：小型 VAR（motto：The Best Antennas This Side of Paradise）。
- **决策链与对接人**：sales@caymanwireless.com（**第三方目录级待核**，CSV 9-27）；1-956-825-0710（先表单/电话核）。
- **技术与认证**：UBWA/UEWA 认证（官网徽标）；Netonix 渠道（CSV，Vitesse 圈外标签在档）。
- **采购与供应链信号**：Tycon（PoE/供电牌）在售=供电 PoE 类目熟——我们的 24 口 PoE/工业件是邻位价档；Netonix 位不碰芯片话术。
- **近期动态与线索**：预配置服务=替客户定 BOM 的影响力位。
- **与我方契合点**：24 口 PoE（站点/监控）+宽温小件窄线。
- **风险与注意**：邮箱待核不直发；Netonix 裁决话规：只谈交期/宽温/上行/价格。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**2004 年起的 WISP 社区 VAR/增值转售：自述服务国内外 WISP 客群，「Expert programming and pre-configured wireless solutions for mission-critical networks」。
  > Specialized Value-Added Reseller — Expert programming and pre-configured wireless solutions for mission-critical networks. ‖ Founded in 2004, Cayman Wireless has served the WISP community as a VAR distributor both domestic and abroad.
  > 来源：https://www.caymanwireless.com/
- **【产品线与在售品牌】**授权品牌墙十家：**Ubiquiti/MikroTik/Cambium/Grandstream/Mimosa/Netonix/IC Realtime/TP-Link/Tycon/Laird**；服务=MikroTik 编程配置、UBWA/UEWA 无线设计、NAS、监控摄像头。
  > Authorized Partner Brands — Ubiquiti · MikroTik · Cambium · Grandstream · Mimosa · Netonix · IC Realtime · TP-Link · Tycon · Laird ‖ MikroTik Programming — UBWA/UEWA Certified
  > 来源：https://www.caymanwireless.com/
- **【决策链与对接人】**sales@caymanwireless.com 系第三方目录结构化数据（官网联系入口遮罩），CSV 9-27 定级**待核——第一步先表单/电话核再发件**。
  > （CSV 2026-09-27 记录）sales@caymanwireless.com（第三方目录结构化数据，官网联系入口为遮罩；待核）；public-register
  > 来源：https://www.caymanwireless.com/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 表单/电话核联络+类目一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）
- **切入点**：先表单一句核对接人；随后一页：站点/监控 24 口 PoE 接入层的供货提案（交期+宽温+价格档——不提芯片）。
- **要问的问题**：站点/监控项目的 24 口 PoE 目前指向哪款？
- **随附证明**：一页报价（英）+ 供货期表。

### 第 2 次跟进 · 宽温小件窄线

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：站点/杆侧宽温小件与收发器窄线。
- **要问的问题**：杆侧/机柜外宽温件有货架位吗？
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
Hi Cayman,

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
