# Alessandro Campanella / 1off

> **评级 A**　|　意大利 · Mogliano Veneto　|　档案编号 `A-034`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　重点，且好跟进（有具体对接人、决策链短）
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | 1off |
| 国家 | 意大利 |
| 城市 | Mogliano Veneto |
| 网站 | 1off.it |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCIPv6E+MTCSE+MTCSWE+MTCEWE |
| 原备注 | ★★ 持 MTCSWE；2003 年起做 MikroTik、2007 年起当讲师；**Routing + Switching + Wireless + QoS + VPN + 安全**；网络设计/迁移/排障；为全球运营商与系统集成商服务 → 给 SI 供货的机会 |

## 三、人员与联系方式

- **对接人**：Alessandro Campanella
- **邮箱**：a.campanella@1off.it
- **电话**：+39 320 299 7787
- **原始联系字段**：+39 320 299 7787 / a.campanella@1off.it

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCIPv6E、MTCSE、MTCSWE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik

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
Hi Alessandro,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on switching.

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
