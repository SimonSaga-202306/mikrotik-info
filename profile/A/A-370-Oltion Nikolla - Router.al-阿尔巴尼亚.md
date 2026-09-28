# Oltion Nikolla / Router.al

> **评级 A**　|　阿尔巴尼亚 · Tirana　|　档案编号 `A-370`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Router.al |
| 国家 | 阿尔巴尼亚 |
| 城市 | Tirana |
| 网站 | router.al |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424DGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 域名 **router.al**（阿尔巴尼亚国别域名做 MikroTik 生意）；资深网络工程师与 IT 顾问，**业务覆盖整个巴尔干地区与国际**；核心专长明确含「**复杂路由与交换：BGP、OSPF、MPLS/VPLS、VLAN Filtering、RSTP/MSTP、多 WAN 负载均衡**」；高密度 Wi-Fi、CAPsMAN、Asterisk/VoIP 集成；服务含 ISP/WISP 建网与企业 IT 外包 【2026-09-27 A360–A378联络核验】来源等级：official-company。官方顾问名录（阿尔巴尼亚筛选）列Oltion Nikolla（Tirana, Albania）：电话+355695250949、邮箱oltionnikolla@gmail.com、站点router.al；条目列MTCNA、MTCRE，自述资深网络工程师与IT顾问、服务覆盖巴尔干地区与国际，核心专长含复杂路由与交换（BGP、OSPF、MPLS/VPLS、VLAN Filtering、RSTP/MSTP、多WAN负载均衡）、高密度Wi-Fi与CAPsMAN、Asterisk/VoIP集成、ISP/WISP建网——与本行原备注一致。公司站另见admin@router.al（次级入口）。CSV城市Tirana与名录一致，未改字段。 证据：[1](https://mikrotik.com/consultants?region=Albania&category=consultants) [2](https://router.al/) 仅覆盖所述联络/关联事实，不证明投递、在职、采购权、芯片或需求；批次：batch/contact_research_2026-09-27_A360-A378.json#A-370 |

## 三、人员与联系方式

- **对接人**：Oltion Nikolla
- **邮箱**：oltionnikolla@gmail.com、admin@router.al
- **电话**：+355 695 250 949
- **原始联系字段**：+355 695 250 949 / oltionnikolla@gmail.com（官方顾问名录条目一致）；admin@router.al（公司站）

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由

**涉及品牌 / 技术**：Asterisk、CAPsMAN、MikroTik

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**STC-424XGGPM-440W（Saga）（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`STC-424DGGPM-440W（Saga）`（供参考，以实际沟通为准）

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
Hi Oltion,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on WISP, MSTP, RSTP, VLAN, VoIP, Asterisk and CAPsMAN.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424DGGPM-440W evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
