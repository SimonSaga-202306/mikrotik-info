# Landatel

> **评级 A**　|　西班牙 · Madrid　|　档案编号 `A-350`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Landatel |
| 国家 | 西班牙 |
| 城市 | Madrid |
| 网站 | https://www.landatel.com |
| 类型 | 分销（Netonix 授权） |
| 反向信号 | Netonix 授权渠道（WISP 接入层交换机） |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | WISP 接入层替换 |
| 数据来源 | Netonix 官方分销/代理名录 |
| 原备注 | 【2026-09-23 用户裁决·保留】Netonix 交换机采用 **Vitesse** 芯片，并非 Marvell，严格按「Marvell 接入层生态」标准属于圈外；用户 2026-09-23 明确「先这样吧，没必要删」，故本条保留。注意：对其**不能使用「同芯片」话术**（详见 Netonix_WISP替换矩阵_2026-09.md），切入点应放在交期、宽温、上行与价格上。 Netonix 西班牙分销。 【2026-09-27 A340–A359联络核验】来源等级：official-company。官网条款/客服页给info@landatel.com、+34 911 461 700、注册地Carretera de La Coruña km 17,800 28231 Las Rozas (Madrid)、CIF B-83170944；分销商政策页给B2B渠道专用comercial@landatel.com，仓库C/ Río Odiel 14, 28906 Getafe。重要：第三方工商档案标题与官网退货/保证页均出现“en liquidación / Liquidation”字样（公司处于清算状态），触达与信用风险须先人工核实。本条为Netonix授权行（Vitesse芯片），2026-09-23用户裁决保留且禁用“同芯片”话术。 证据：[1](https://www.landatel.com/en_US/terminos-y-condiciones) [2](https://www.landashop.com/resellers?___store=default) [3](https://empresite.eleconomista.es/LANDATEL-COMUNICACIONES.html) 仅覆盖所述联络/关联事实，不证明投递、在职、采购权、芯片或需求；批次：batch/contact_research_2026-09-27_A340-A359.json#A-350 |

## 三、人员与联系方式

- **邮箱**：info@landatel.com、B2B商业comercial@landatel.com
- **电话**：+34 911 461 700、83170944
- **原始联系字段**：info@landatel.com（官网条款/客服页；B2B商业comercial@landatel.com）；+34 911 461 700；Landatel Comunicaciones S.L.，Las Rozas (Madrid)，CIF B-83170944；公司状态显示清算（见备注）

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

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 七、首触邮件（可直接发送）

**主题**：L3 hardware offload + QinQ on access switching

```text
Hi Landatel,

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

## 八、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
