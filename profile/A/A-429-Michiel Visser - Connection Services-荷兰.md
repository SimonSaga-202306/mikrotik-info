# Michiel Visser / Connection Services

> **评级 A**　|　荷兰 · Deventer　|　档案编号 `A-429`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— R51 达标即升级：用户指示「达到 A 级标准即可升级」；本条与 A-271 疑似同一实体，但自身独立满足 A 标准（优先级★★★、工程师级认证 MTCINE、MTCRE、MTCSE、MTCWE、直达邮箱、非硬排除）；原 B-442 升级，编号顺延 A-429
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Connection Services |
| 国家 | 荷兰 |
| 城市 | Deventer |
| 网站 | connectionservices.nl |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCINE+MTCIPv6E+MTCSE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | 含 MTCINE（ISP 互联）+ MTCWE（无线） 【2026-09-28 R49 复筛补录】来源等级：official-company。站点仅占位页；与 A-271 同名同人，保留不合并：connectionservices.nl 现仅单页 IPv6 连通性测试占位（含 he.net 徽章），无公司介绍/产品/服务正文；原入口 +31 6 29047127 / michiel@connectionservices.nl 保留 结论：维持 B（无采购/替换新证据）。 证据：[1](https://connectionservices.nl/)；批次：batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json#B-442 【2026-09-28 R50 去重提示】与 A-271 （同名 michiel visser） → 疑似同一实体；按既有规则只记录、不合并，A 级行保留，本行维持 B 待用户裁决。批次：batch/dedup_hints_2026-09-28_R50.json#B-442 【2026-09-28 R51 达标即升级】按用户指示：达到 A 级标准即升级。本条独立满足 A 标准（★★★、工程师级认证 MTCINE、MTCRE、MTCSE、MTCWE、直达邮箱）。原 B-442 → 现 A-429，物理位置不动、原 B 号空置不回填；与 A-271 的疑似同一实体重复提示继续保留，不合并、不删除。 证据：[1](https://mikrotik.com/consultants?region=Netherlands)；批次：batch/contact_research_2026-09-28_R51_达标即升级.json#A-429 |

## 三、人员与联系方式

- **对接人**：Michiel Visser
- **邮箱**：michiel@connectionservices.nl
- **电话**：+31 6 29047127
- **原始联系字段**：+31 6 29047127 / michiel@connectionservices.nl

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCINE、MTCIPv6E、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：ISP / 骨干

### 推什么型号

**LT-S8328XG-4XS24GT-S（4×10G 上行，收敛比高）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

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
Hi Michiel,

I do access switches for WISPs and small ISPs, where the number that matters is cost per subscriber port.

What caught my eye is that you work on MTCINE, ISP and MTCWE.

Where we may be useful: 4×10G uplink, QinQ subscriber isolation, port isolation, broadcast suppression, SNMP that drops into whatever NMS you already run.

How many subscribers per access switch, and what uplink ratio are you designing to?

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
