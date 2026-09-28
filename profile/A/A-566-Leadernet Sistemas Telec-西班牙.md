# Leadernet Sistemas Telec

> **评级 A**　|　西班牙 · Oricáin (Navarra)　|　档案编号 `A-566`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— R53 B段复筛达标升级：B 段逐站复筛达标（站点在线 + 交换机品类/产品在售 + 网络/交换专营 + 小公司决策链短）；官网核对：Grupo Leadernet（西班牙，1992 年起；info@leadernet.es）自述 **«grupo multinacional español especializado en el suministro, instalación, puesta en marcha y mantenimiento de redes de comunicación industrial y…；原 B-535 升级，编号顺延 A-566
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Leadernet Sistemas Telec |
| 国家 | 西班牙 |
| 城市 | Oricáin (Navarra) |
| 网站 | leadernet.es |
| 类型 | 分销（HMS/N-Tron·Red Lion 渠道） |
| 反向信号 | N-Tron + Red Lion |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-IS6312XG-4XS8GT |
| 切入点 | 卖 N-Tron/Red Lion 工业交换机（8口非网管约 $500+）→ 中性货同规格 LT-IS6310G 约 $91，做第二供应商，价差 5 倍 |
| 数据来源 | 2026-09-22 |
| 原备注 | 本行由分销商名录批量导入，三星依据仅为渠道等级（分销（HMS/N-Tron·Red Lion 渠道））与「N-Tron + Red Lion」，尚无人工核实。建议先查证其是否已有工业交换机 / PoE++ 产品线，再定切入型号 【2026-09-28 R49 邮箱补录】来源等级：official-company。官网首页正文可见：info@leadernet.es。待补标记解除；C→B 回升（原下放原因=无邮箱）。 证据：[1](https://www.leadernet.es/)；批次：batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json#B-535 【2026-09-28 R53 B段复筛达标升级】官网核对：Grupo Leadernet（西班牙，1992 年起；info@leadernet.es）自述 **«grupo multinacional español especializado en el suministro, instalación, puesta en marcha y mantenimiento de redes de comunicación industrial y seguridad electrónica»**（工业通信网络与电子安防的供应/安装/调试/维护），主业为风电/光伏/光热电站；明确 **«Suministro de electrónica de red: switches, routers, conversores de medio»**、«Suministro e instalación de la red de comunicaciones: switches; routers; fibra óptica MM, SM, HCS; bus serie 485; Profibus y Profinet»，并提供 Cisco 咨询支持；8 国设点、100+ 人员、1000+ 项目。原 B-535 → 现 A-566，物理位置不动、原 B 号空置不回填；证据与原文摘录见批次文件。 证据：[1](https://www.leadernet.es/)；批次：batch/contact_research_2026-09-28_R53_B复筛升级.json#A-566 |

## 三、人员与联系方式

- **邮箱**：info@leadernet.es
- **电话**：—
- **原始联系字段**：info@leadernet.es（官网正文/隐私条款）

## 四、品牌与技术栈

**涉及品牌 / 技术**：N-Tron、Red Lion

## 五、跟进策略

**场景判断**：PoE / 监控 / 门禁

### 推什么型号

**LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`LT-IS6312XG-4XS8GT`（供参考，以实际沟通为准）

### 核心卖点

802.3bt 单口 90W、**PoE 看门狗（摄像头死机自动断电重启，省一趟上门）**、250m 延长供电、端口隔离、整机功率预算足

### 怎么开发

替他算一笔账：24 个 4K 头全开要多少瓦、满配后还剩多少余量——这是每个做监控的人都踩过的坑，算清楚就赢一半

### 风险点

**PoE 功率预算和供电稳定性是验收红线**，虚标功率会当场翻车；必须送测、必须给整机功率实测数；部分非标 PoE 相机存在兼容性问题，要先拿他的机型测

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 七、首触邮件（可直接发送）

**主题**：PoE budget question on your camera jobs

```text
Hi Leadernet,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on HMS, N-Tron and Red.

Where we may be useful: 24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.

How many cameras per job, and what wattage per port are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a LT-IS6312XG-4XS8GT evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
