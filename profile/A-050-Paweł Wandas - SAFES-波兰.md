# Paweł Wandas / SAFES

> **评级 A**　|　波兰 · Kraków　|　档案编号 `A-050`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　重点，且好跟进（有具体对接人、决策链短）
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | SAFES |
| 国家 | 波兰 |
| 城市 | Kraków |
| 网站 | safes.pl |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE+MTCSWE+MTCEWE |
| 原备注 | 防火墙/VPN/隧道/负载均衡/故障切换/QoS/高级路由/无线；熟 The Dude 网管 → 对 SNMP/MIB/NMS 集成有感觉 |

## 三、人员与联系方式

- **对接人**：Paweł Wandas
- **邮箱**：biuro@safes.pl
- **电话**：+48 412 412 324
- **原始联系字段**：+48 412 412 324 / biuro@safes.pl

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCTCE、MTCINE、MTCIPv6E、MTCSE、MTCSWE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCTCE` — 流量控制
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik、The Dude

## 五、跟进策略

**场景判断**：MTCSWE 交换认证

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

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
Hi Paweł,

You hold MTCSWE, so switching is a declared specialism rather than a side task — that is who I want to talk to.

What caught my eye is that you work on The Dude.

Where we may be useful: L3 hardware offload (line-rate forwarding off the CPU), QinQ and VLAN translation, ERPS and MSTP, ACLs and static routing, full CLI plus SSH plus SNMP with a private MIB.

What are you using for L2 redundancy today, and does it need ERPS-class convergence?

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
