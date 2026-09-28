# Rick Frey / Rick Frey Consulting

> **评级 A**　|　美国 · Rexburg, ID　|　档案编号 `A-412`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— R50 A级提炼：官方顾问名录收录的认证顾问/讲师，持工程师级认证 MTCEWE、MTCINE、MTCRE、MTCSE、MTCTCE、MTCWE，且有直达邮箱；A 段既有同类先例（A-360–A-384）；原 B-378 升级，编号顺延 A-412
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Rick Frey Consulting |
| 国家 | 美国 |
| 城市 | Rexburg, ID |
| 网站 | rickfreyconsulting.com |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCSE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGM（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | **30+ 年网络、19 年 MikroTik**，提供 MikroTik 全科目咨询与培训（含 ROS7 迁移）；路由/无线/QoS/VPN/防火墙/监控/OSPF/BGP/MPLS/VPLS/TE/负载均衡/VLAN/安全/CAPsMAN 【2026-09-28 R49 复筛补录】来源等级：official-company。站点持续被拦截，无法直连（失败站重试）：rickfreyconsulting.com 仍被客户端/扩展拦截（ERR_BLOCKED_BY_CLIENT，跳转纯搜寻域），无法直连核验内容 结论：维持 B（无采购/替换新证据）。 证据：[1](https://rickfreyconsulting.com/)；批次：batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json#B-378 【2026-09-28 R50 A级提炼】来源等级：official-directory（沿用既有轮次官方名录记录）。持 MTCEWE、MTCINE、MTCNA、MTCRE、MTCSE、MTCTCE、MTCWE；**30+ 年网络、19 年 MikroTik**，提供 MikroTik 全科目咨询与培训（含 ROS7 迁移）；路由/无线/QoS/VPN/防火墙/监控/OSPF/BGP/MPLS/VPLS/TE/负载均衡/VLAN。R50 全表去重扫描：未发现与现有 A 行同邮箱/同域名/同名（对照同轮 31 条重复提示）。人工定级 A：认证顾问/讲师 + 直达邮箱 + 个体/小公司决策链短。原 B-378 → 现 A-412。 证据：[1](https://mikrotik.com/consultants?region=USA)；批次：batch/contact_research_2026-09-28_R50_A提炼.json#A-412 |

## 三、人员与联系方式

- **对接人**：Rick Frey
- **邮箱**：rickfrey1000@gmail.com
- **电话**：+1 430 236 5829
- **原始联系字段**：+1 430 236 5829 / rickfrey1000@gmail.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCTCE、MTCINE、MTCSE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCTCE` — 流量控制
- `MTCINE` — ISP 互联
- `MTCSE` — 安全
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：CAPsMAN、MikroTik

## 五、跟进策略

**场景判断**：ISP / 骨干

### 推什么型号

**STC-424XGGM（Saga）（4×10G 上行，收敛比高）**

> 系统初判型号：`STC-424XGGM（Saga）`（供参考，以实际沟通为准）

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
Hi Rick,

I do access switches for WISPs and small ISPs, where the number that matters is cost per subscriber port.

What caught my eye is that you work on VLAN and CAPsMAN.

Where we may be useful: 4×10G uplink, QinQ subscriber isolation, port isolation, broadcast suppression, SNMP that drops into whatever NMS you already run.

How many subscribers per access switch, and what uplink ratio are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424XGGM evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
