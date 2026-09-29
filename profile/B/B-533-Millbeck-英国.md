# Millbeck

> **评级 B**　|　英国　|　档案编号 `B-533`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：B　**Maybe** —— 不太明显，慢跟待验证
- **评级依据**：【2026-09-28 复核回升 C-285→B-533】官网联系页正文可见；邮箱补到后原「无邮箱（群发触达不到）」下放原因消除 → 恢复 B（群发可触达）。原判：三星依据仅渠道等级（分销）与「Teltonika（Diamond 最高级）」，需求未核。
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Millbeck |
| 国家 | 英国 |
| 城市 | — |
| 网站 | millbeck.co.uk |
| 类型 | 分销 |
| 反向信号 | Teltonika（Diamond 最高级） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-21616XGGPM（Saga） |
| 切入点 | 他们只有8口→补16/24口与10G |
| 数据来源 | 反向信号/2026-09 |
| 原备注 | 本行由分销商名录批量导入，三星依据仅为渠道等级（分销）与「Teltonika（Diamond 最高级）」，尚无人工核实。建议先查证其是否已有工业交换机 / PoE++ 产品线，再定切入型号 【2026-09-28 R49 邮箱补录】来源等级：official-company。官网联系页正文可见：hello@millbeck.co.uk。待补标记解除；C→B 回升（原下放原因=无邮箱）。 证据：[1](https://www.millbeck.co.uk/contact)；批次：batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json#B-533 |

## 三、人员与联系方式

- **邮箱**：hello@millbeck.co.uk
- **电话**：—
- **原始联系字段**：hello@millbeck.co.uk（官网联系页）

## 四、品牌与技术栈

**涉及品牌 / 技术**：Teltonika

## 五、跟进策略

**场景**：PoE / 监控 / 门禁

先问他在做什么监控项目、单口要多大功率，用小批量试单切入。

参考型号：`STI-21616XGGPM（Saga）`

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 备护深挖(2026-09-29 · R57-BC 轻量对齐 A · 评级不动、不出信）

**深挖三层**
- 【事实】Millbeck(Millbeck Communications Ltd;Leeds LS17 9BF 6 Arena Park;**Teltonika Diamond Partner(官方最高级)16+ 年**):全谱 Teltonika——RUT 4G/5G 路由 + **TSW/SWM 交换谱(含 TSW202 管理工业 PoE+、SWM280/281/282 管理型 PoE)** + IoT SIM + 天线 + RMS rms.credit;**公用事业垂直深绑(水/气/电/热网络运营商 SCADA/智能计量 LTE-M/NB-IoT)**;自述开放式站位『without vendor lock-in, fully compatible with Cisco, Juniper, HPE』
- 【推断】Diamond 最高级=与 Teltonika 深绑,原档案『只有 8 口』切入点已被 SWM 管理型 PoE 新品推翻;但其宣传语自家写『不锁 vendor、兼容 Cisco/Juniper/HPE』——开放叙事留了第二源缝;公用事业项目招标常有双源要求
- 【假设】开口角度=「Diamond 排他谱之外的竞价对照/双源位」:STC-424 不做替换做双源——其 SWM 谱缺『非 Teltonika 品牌对照件』,招标双源场景与 Teltonika 交期紧时的备胎

**SWOT 速描**
- **S**: Diamond 最高级+公用事业深垂直+16 年
- **W**: Teltonika 排他深绑
- **O**: 招标双源/交期备胎对照位(其自写不锁 vendor)
- **T**: Diamond 忠诚冲突

**证据（quote → 来源）**
- 「Millbeck is a Teltonika Diamond Partner…TSW/SWM switch range: unmanaged industrial TSW switches and SWM managed PoE switches for enterprise LAN, CCTV, smart building and industrial automation…without vendor lock-in」 — https://millbeck.co.uk/teltonika-switches/
- 「Millbeck supplies multi-network IoT SIMs, industrial routers…water, gas, electricity and heat network operators…private APN services, fixed private IP addressing for SCADA」 — https://millbeck.co.uk/solutions/utilities

**判位备档**(参考位，评级仍 B · 不出信）
- 参考 P1: `STC-424DGGPM-280W` — Diamond 排他谱外的招标双源/竞价对照位(PS:原『只有8口』切入点已被 SWM 谱推翻,修正)
- 第一问: 公用事业招标要双源、或 Teltonika 交期紧时,你们对照件现用哪家?非 Teltonika 的文档全对照位可谈吗?
- 标签: 英国|利兹|Teltonika-Diamond|公用事业|双源对照位

**备养出信稿（未触发，供后续用户启用参考）**
```text
Hi Millbeck team,

Sixteen years as a Teltonika Diamond Partner with utility networks on your customer list - and your own switching page still says without vendor lock-in. That sentence is exactly where a second source lives.

We build a 24-port PoE+ managed switch (280W, L2-lite) with full English documentation. Reference: $165 USD EXW (2026-09-29) - not a Teltonika replacement; the documented comparison unit for tender dual-source requirements and tight-lead-time weeks, white-label friendly.

One question: when a utility tender asks for a second source, or Teltonika lead time stretches, which switch do you quote as the alternative today - and would a documented unit earn a bench test for that slot?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

**待补证清单**
1. SWM 交换谱上市后的客户接受度与价带
2. 公用事业招标里双源要求出现频度

**跟进建议（守档节奏）**
- D+3 [双源对照] 招标场景页
- D+14 hello@millbeck.co.uk 开口
- D+30 果归守档

> 备注: **切入点修正**:R49 原判『只有8口→补16/24口』已失效——Teltonika SWM280/281/282 管理型 PoE 与 TSW202 工业 PoE+ 已全谱在架;角度改为『排他谱外双源对照』,勿再提补口数。

<!-- BDEEP:B类深挖_2026-09-29_R57-BC_第7波 -->
## 七、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
