# Joshua Moore / Archous Networks

> **评级 A**　|　美国 · Lake Stevens, WA　|　档案编号 `A-410`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— R50 A级提炼：官方顾问名录收录的认证顾问/讲师，持工程师级认证 MTCINE、MTCSE、MTCTCE、MTCUME，且有直达邮箱；A 段既有同类先例（A-360–A-384）；原 B-356 升级，编号顺延 A-410
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Archous Networks |
| 国家 | 美国 |
| 城市 | Lake Stevens, WA |
| 网站 | archous.tech |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCTCE+MTCUME+MTCINE+MTCIPv6E+MTCSE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XG-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | 多厂商网络与系统集成商，专做 **MikroTik 及他牌的自动化网络方案**（端到端开通自动化：用户开通/停用/限速）；OSPF/BGP/MPLS 规模部署、WireGuard/IPIP/GRE/L2TP/PPP 隧道；为企业与 ISP 定制监控与报表 【2026-09-28 R49 复筛补录】来源等级：official-company。官网在线；ISP/数据中心网络设计（含开放网络厂商）：archous.tech 首页：1-866-535-0358 | support@archous.tech | support.archous.tech；自述 ISP/数据中心/企业网络的托管服务、设计与实施；专长品牌含 MikroTik、Edge-Core、UfiSpace、IP Infusion、Juniper、Cisco、Dell、Paessler、Andrisoft、Debian、Microsoft 结论：维持 B（无采购/替换新证据）。 证据：[1](https://www.archous.tech/)；批次：batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json#B-356 【2026-09-28 R50 A级提炼】来源等级：official-directory（沿用既有轮次官方名录记录）。持 MTCINE、MTCIP、MTCNA、MTCSE、MTCTCE、MTCUME；多厂商网络与系统集成商，专做 **MikroTik 及他牌的自动化网络方案**（端到端开通自动化：用户开通/停用/限速）；OSPF/BGP/MPLS 规模部署、WireGuard/IPIP/GRE/L2TP/PPP 隧道。R50 全表去重扫描：未发现与现有 A 行同邮箱/同域名/同名（对照同轮 31 条重复提示）。人工定级 A：认证顾问/讲师 + 直达邮箱 + 个体/小公司决策链短。原 B-356 → 现 A-410。 证据：[1](https://mikrotik.com/consultants?region=USA)；批次：batch/contact_research_2026-09-28_R50_A提炼.json#A-410 |

## 三、人员与联系方式

- **对接人**：Joshua Moore
- **邮箱**：mikrotik@archous.tech
- **电话**：+1 912 218 3720
- **原始联系字段**：+1 912 218 3720 / mikrotik@archous.tech

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCTCE、MTCUME、MTCINE、MTCIPv6E、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCTCE` — 流量控制
- `MTCUME` — 用户管理（Hotspot / PPPoE）
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全

**涉及品牌 / 技术**：MikroTik、WireGuard

## 五、跟进策略

**场景判断**：ISP / 骨干

### 推什么型号

**LT-S8328XG-4XS24GT-S（4×10G 上行，收敛比高）**

> 系统初判型号：`LT-S8328XG-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

4×10G 上行、QinQ 用户隔离、组播、端口隔离、广播抑制、SNMP 对接现有网管

### 怎么开发

问「接入层一台带多少用户？上行怎么收敛？」；他们按端口成本算账，把单端口价格摊到每个用户给他看

### 风险点

ISP 对设备故障率极度敏感，一台炸掉就是一批投诉；要先小批量试用跑半年；备件和 RMA 响应速度要提前承诺

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 七、首触邮件（可直接发送）

**主题**：Access layer cost per port

```text
Hi Joshua,

I do access switches for WISPs and small ISPs, where the number that matters is cost per subscriber port.

What caught my eye is that you work on WireGuard.

Where we may be useful: 4×10G uplink, QinQ subscriber isolation, port isolation, broadcast suppression, SNMP that drops into whatever NMS you already run.

How many subscribers per access switch, and what uplink ratio are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328XG-4XS24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
