# Jasper Hagoort

> **评级 A**　|　荷兰 · Geertruidenberg　|　档案编号 `A-090`　|　优先级 ★★★　|　状态：未触达

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
| 公司名 | Jasper Hagoort |
| 国家 | 荷兰 |
| 城市 | Geertruidenberg |
| 网站 | — |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问，持 MTCRE MTCWE MTCTCE MTCIPv6E MTCINE MTCSE MTCEWE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328GP-4GX24GT-S |
| 切入点 | MikroTik 生态切入 |
| 数据来源 | MikroTik 官方认证顾问名录 |
| 原备注 | 【待人工补信息】本条为**集成商/顾问型**，属 A 级主产地，但当前**抓不到邮箱**（群发触达不到），故由人工定级提为 A。**需要人工处理**：请补邮箱（或确认电话为唯一触达方式）后再进入群发名单。补到邮箱后本标注可删。 【2026-09-23】MikroTik 官方认证顾问名录（mikrotik.com/consultants）收录。 【2026-09-27 挖邮箱·真邮箱】官网 contact 页。D-Side Telecom 所有者；持 **MTCSWE**（2023-07 发，2026-07 到期）；**2026 年在布拉格 MTPC 大会讲过 MikroTik spine-leaf 交换** → 技术深度高、活跃 |

## 三、人员与联系方式

- **邮箱**：info@dside.nl
- **电话**：—
- **原始联系字段**：info@dside.nl（官网 contact 页。D-Side Telecom 所有者；持 **MTCSWE**（2023-07 发，2026-07 到期）；**2026 年在布拉格 MTPC 大会讲过 MikroTik spine-leaf 交换** → 技术深度高、活跃）

## 四、品牌与技术栈

**持有认证**：MTCRE、MTCWE、MTCTCE、MTCINE、MTCIPv6E、MTCSE、MTCEWE

- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCTCE` — 流量控制
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：MTCSWE 交换认证

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328GP-4GX24GT-S`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

他持有 MTCSWE（MikroTik 交换认证），交换是正式专长——**不用给他做科普**。开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」直接给 CLI 命令对比和转发实测数据

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全；含糊其辞会立刻失去这类技术型客户的信任

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 七、首触邮件（可直接发送）

**主题**：Switching question for an MTCSWE holder

```text
Hi Jasper,

You hold MTCSWE, so switching is a declared specialism rather than a side task — that is who I want to talk to.

What caught my eye is that you work on MikroTik, mikrotik and com.

Where we may be useful: L3 hardware offload (line-rate forwarding off the CPU), QinQ and VLAN translation, ERPS and MSTP, ACLs and static routing, full CLI plus SSH plus SNMP with a private MIB.

What are you using for L2 redundancy today, and does it need ERPS-class convergence?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328GP-4GX24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
