# RWL Advanced Solutions

> **评级 A**　|　英国 · London　|　档案编号 `A-109`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **下次复核**：收到反馈后重新评级


> 🟡 **信息不够，需要人工处理**
>
> 本条为集成商/顾问型（A 级主产地），但目前**抓不到邮箱**，群发触达不到。
> 已按人工定级提为 A，**请先补齐以下任一信息再进入群发名单**：
> 1. 找邮箱（官网 / 名录页 / LinkedIn）；
> 2. 若确实只有电话，确认其为唯一触达方式，改为单独跟进、不进群发。
>
> 补到邮箱后，可删掉本条备注开头的 `【待人工补信息】` 标记。

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | RWL Advanced Solutions |
| 国家 | 英国 |
| 城市 | London |
| 网站 | — |
| 类型 | 集成商/代理（Allied Telesis） |
| 反向信号 | Allied Telesis（Marvell Prestera 接入层） |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | Marvell Prestera 接入层切入 |
| 数据来源 | Allied Telesis 英国代理名录 |
| 原备注 | 【待人工补信息】本条为**集成商/顾问型**，属 A 级主产地，但当前**抓不到邮箱**（群发触达不到），故由人工定级提为 A。**需要人工处理**：请补邮箱（或确认电话为唯一触达方式）后再进入群发名单。补到邮箱后本标注可删。 【2026-09-27 挖邮箱·真邮箱】都柏林。自述「欧洲领先的数据布线与网络产品独立分销商」，代理 Panduit 等；覆盖电信/商用/数据中心。⚠️ 属**分销商**（转化率低），且主业是布线不是交换机 |

## 三、人员与联系方式

- **邮箱**：sales@rwlas.com
- **电话**：—
- **原始联系字段**：sales@rwlas.com（都柏林。自述「欧洲领先的数据布线与网络产品独立分销商」，代理 Panduit 等；覆盖电信/商用/数据中心。⚠️ 属**分销商**（转化率低），且主业是布线不是交换机）

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
Hi RWL,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on Panduit.

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
