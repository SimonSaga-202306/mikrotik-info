# Jonathan De Graeve / Smarteye

> **评级 A**　|　比利时 · Wilrijk (Antwerpen)　|　档案编号 `A-402`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— R50 A级提炼：官方顾问名录收录的认证顾问/讲师，持工程师级认证 MTCEWE、MTCINE、MTCRE、MTCSE，且有直达邮箱；A 段既有同类先例（A-360–A-384）；原 B-226 升级，编号顺延 A-402
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Smarteye |
| 国家 | 比利时 |
| 城市 | Wilrijk (Antwerpen) |
| 网站 | smarteye.eu |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCINE+MTCSE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 比利时**唯一**认证顾问（稀缺）；专做**骨干网设计**与 RouterOS 全栈运维诊断：BGP、MPLS、VPLS、OSPF、流量管理、带宽整形、防火墙、Hotspots、VPN、无线 【2026-09-28 R49 复筛补录】来源等级：official-company。官网正文可见销售/支持邮箱与公司实体：smarteye.eu：Sales +32 9 395 7000 / sales@smarteye.eu；Support BE +32 9 395 6000 / support@smarteye.eu；SmartEye BV, Terbekehofdreef 24, B-2610 Wilrijk, B.T.W. BE0542740338；自述 30,000+ Wi-Fi 接入点、700+ 场址、165,000+ 年用户；客户含 Artevelde、UGent、Howest、XIOR、Home Invest、Hasselt 等 结论：B 级群发可触达（原 jonathan@smarteye.eu 保留）。 证据：[1](https://www.smarteye.eu/)；批次：batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json#B-226 【2026-09-28 R50 A级提炼】来源等级：official-directory（沿用既有轮次官方名录记录）。持 MTCEWE、MTCINE、MTCNA、MTCRE、MTCSE；★ 比利时**唯一**认证顾问（稀缺）；专做**骨干网设计**与 RouterOS 全栈运维诊断：BGP、MPLS、VPLS、OSPF、流量管理、带宽整形、防火墙、Hotspots、VPN、无线。R50 全表去重扫描：未发现与现有 A 行同邮箱/同域名/同名（对照同轮 31 条重复提示）。人工定级 A：认证顾问/讲师 + 直达邮箱 + 个体/小公司决策链短。原 B-226 → 现 A-402。 证据：[1](https://mikrotik.com/consultants?region=Belgium)；批次：batch/contact_research_2026-09-28_R50_A提炼.json#A-402 |

## 三、人员与联系方式

- **对接人**：Jonathan De Graeve
- **邮箱**：jonathan@smarteye.eu
- **电话**：+32 9 395 6202
- **原始联系字段**：+32 9 395 6202 / jonathan@smarteye.eu

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCINE、MTCSE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCINE` — ISP 互联
- `MTCSE` — 安全
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik、RouterOS

## 五、跟进策略

**场景判断**：ISP / 骨干

### 推什么型号

**STC-424XGGM（Saga）（4×10G 上行，收敛比高）**

> 系统初判型号：`STC-424XGGPM-440W（Saga）`（供参考，以实际沟通为准）

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
Hi Jonathan,

I do access switches for WISPs and small ISPs, where the number that matters is cost per subscriber port.

What caught my eye is that you work on RouterOS, BGP and MPLS.

Where we may be useful: 4×10G uplink, QinQ subscriber isolation, port isolation, broadcast suppression, SNMP that drops into whatever NMS you already run.

How many subscribers per access switch, and what uplink ratio are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424XGGPM-440W evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
