# EG Electronics AB

> **评级 B**　|　瑞典 · Spånga (Stockholm)　|　档案编号 `B-527`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：B　**Maybe** —— 不太明显，慢跟待验证
- **评级依据**：【2026-09-28 复核回升 C-226→B-527】官网 /contact-us/ 正文可见；邮箱补到后原「无邮箱（群发触达不到）」下放原因消除 → 恢复 B（群发可触达）。原判：三星依据仅渠道等级（分销（HMS/N-Tron·Red Lion 渠道））与「N-Tron + Red Lion + Anybus」，需求未核。
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | EG Electronics AB |
| 国家 | 瑞典 |
| 城市 | Spånga (Stockholm) |
| 网站 | egelectronics.com |
| 类型 | 分销（HMS/N-Tron·Red Lion 渠道） |
| 反向信号 | N-Tron + Red Lion + Anybus |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-480XGGM（Saga） |
| 切入点 | 卖 N-Tron/Red Lion 工业交换机（8口非网管约 $500+）→ 中性货同规格 STI-280GE（Saga）约 $64（EXW 快照，15 天有效），做第二供应商/替换，价差 5 倍 |
| 数据来源 | 2026-09-22 |
| 原备注 | 本行由分销商名录批量导入，三星依据仅为渠道等级（分销（HMS/N-Tron·Red Lion 渠道））与「N-Tron + Red Lion + Anybus」，尚无人工核实。建议先查证其是否已有工业交换机 / PoE++ 产品线，再定切入型号 【2026-09-28 R49 邮箱补录】来源等级：official-company。官网 /contact-us/ 正文可见：hello@egelectronics.com。待补标记解除；C→B 回升（原下放原因=无邮箱）。 证据：[1](https://www.egelectronics.com/contact-us/)；批次：batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json#B-527 |

## 三、人员与联系方式

- **邮箱**：hello@egelectronics.com
- **电话**：—
- **原始联系字段**：hello@egelectronics.com（官网联系页）

## 四、品牌与技术栈

**涉及品牌 / 技术**：N-Tron、Red Lion

## 五、跟进策略

**场景**：PoE / 监控 / 门禁

先问他在做什么监控项目、单口要多大功率，用小批量试单切入。

参考型号：`STI-480XGGM（Saga）`

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 备护深挖(2026-09-29 · R57-BC 轻量对齐 A · 评级不动、不出信）

**深挖三层**
- 【事实】EG Electronics AB(Spånga Fagerstagatan 3,Stockholm;**KAMIC Group 电子事业部主公司**;51-100 人):**显示/HMI/嵌入计算 VAD**——Noritake Itron 显示授权、嵌入 PC/存储/RF 微波谱;北欧 8 国+美/亚,斯京中央仓+美国/香港物流点;收购 Acte Solutions 显示系统业务;工业自动化市场(HMI+connectivity);CSV 标 N-Tron/Red Lion/Anybus 谱出自其 connectivity 板块
- 【推断】嵌入显示/HMI 为主血统的 KAMIC 集团 VAD,connectivity(N-Tron/Anybus)是其一角;客户=机械制造商/OEM,正是工业 PoE 的装机客层
- 【假设】开口角度=「KAMIC 集团 connectivity 板块 N-Tron 旁的 DIN 轨 value 位」:STI-288GP 以其 OEM/机械制造客户谱的二源入

**SWOT 速描**
- **S**: KAMIC 集团+8 国物流+OEM/机械制造客层
- **W**: connectivity 非主业
- **O**: N-Tron 旁 DIN 轨 value 位
- **T**: 主业绑定显示谱

**证据（quote → 来源）**
- 「The largest company in the business area is EG Electronics…represented in eight countries…central warehouse in Stockholm…integrated logistics centres in the USA and Hong Kong」 — https://kamicgroup.com/index.php/en/electronics-2/
- 「We help machine builders, OEMs, and manufacturers power the next generation of automation…embedded computing, industrial displays, connectivity」 — https://egelectronics.com/markets/industrial-automation/

**判位备档**(参考位，评级仍 B · 不出信）
- 参考 P1: `STI-288GP` — KAMIC 集团 VAD 的 connectivity 板块 N-Tron 谱旁 DIN 轨 value 二源(OEM/机械制造客层对口)
- 第一问: 你们 connectivity 板块 N-Tron 旁,value DIN 轨 PoE 二源有位吗?OEM 客户要 value 件的频次多高?
- 标签: 瑞典|斯德哥尔摩|KAMIC集团|显示嵌入式VAD

**备养出信稿（未触发，供后续用户启用参考）**
```text
Hi EG Electronics team,

KAMIC Group's electronics flagship with HMI displays, embedded computing and industrial connectivity for machine builders across eight countries - your OEM customers already ask you for the connectivity layer, and the value side of that layer is thin.

We build an 8-port Gigabit industrial PoE switch (DIN-rail, fanless, -40..75C class) with full English documentation. Reference: $74.8 USD EXW (2026-09-29) - strictly the value-side second source next to your N-Tron shelf, fully open to an OEM variant under your terms.

One question: inside your connectivity offering for machine builders, is there a documented value DIN-rail PoE source today, or is that slot still open?

If useful, I can send one unit with the complete test pack (surge 6 kV, EFT/ESD data sheet, cold-start log). If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

**待补证清单**
1. connectivity 板块在架(PoE 件谱深)
2. 其 OEM 客户 value 档接受度

**跟进建议（守档节奏）**
- D+3 N-Tron 对位页
- D+14 hello@egelectronics.com 开口
- D+30 果归守档

<!-- BDEEP:B类深挖_2026-09-29_R57-BC_第9波 -->
## 七、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
