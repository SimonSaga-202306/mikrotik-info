# ELKO Ukraine

> **评级 B**　|　乌克兰　|　档案编号 `B-011`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：B　**Maybe** —— 不太明显，慢跟待验证
- **评级依据**：通用分销商信号，无差异化切入点，慢慢跟
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | ELKO Ukraine |
| 国家 | 乌克兰 |
| 城市 | — |
| 网站 | elko.ua |
| 类型 | 分销（MikroTik 官方） |
| 反向信号 | MikroTik（Master+VAD） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-48DGGM-U（Saga） |
| 切入点 | ELKO 集团乌克兰站 |
| 数据来源 | 2026-09-22 |
| 原备注 | Kyiv 【2026-09-28 R50 去重提示】与 A-360 （同域名 elko.ua） → 疑似同一实体；按既有规则只记录、不合并，A 级行保留，本行维持 B 待用户裁决。批次：batch/dedup_hints_2026-09-28_R50.json#B-011 |

## 三、人员与联系方式

- **邮箱**：elko@elko.ua
- **电话**：+380 44 461 9670
- **原始联系字段**：+380 44 461 9670 / elko@elko.ua

## 四、品牌与技术栈

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景**：待摸底

保持低频联系，等他出现交换机需求信号再提级为 A。

参考型号：`STC-48DGGM-U（Saga）`

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 备护深挖(2026-09-29 · R57-BC 轻量对齐 A · 评级不动、不出信）

**深挖三层**
- 【事实】ELKO Ukraine（基辅,1998 创,51-200 人）=ELKO Group 旗下（400 IT 厂牌/10 国 10000+ 伙伴;拉脱维亚血统）;双主线=项目分销（系统集成支持服务）+批发出货;在架网牌 20+:AAeon/Advantech/Aruba/Axiomtek/GIGA-IPC/IEI/Intel/Keenetic/Lanner/LR-Link/Mellanox/MikroTik/Netis/Nexcom/QLogic/QNAP/Supermicro/Synology/TP-Link/Ubiquiti;LinkedIn 每周更新 MikroTik 新品/停产公告（活跃度高）
- 【推断】ELKO Group 是波罗的海 VAD 集团（ELKO Latvia 母体）;UA 站是活跃运营体,MikroTik 每周锚定其目录——MikroTik 新系列上架（RB5009/knot 等）投放密度说明:ELKO UA 的 IT infra 谱里,MikroTik 是核心牢位
- 【假设】从「ELKO 谱系里缺 PoE 楼价档」入手:ELKO 在架 TP-Link/Keenetic/Netis 属 value 网谱,但 PoE 接入层（8~24 口）没有专架;STC-424 以「集团谱 value 楼价档补位」+具名 MikroTik 项目经理切入

**SWOT 速描**
- **S**: 波罗的海集团主权+50-200 人+多谱
- **W**: 谱太宽、SKU 单一进入难,决策多层
- **O**: STC-424 入 value PoE 档集团谱补位
- **T**: 乌克兰运营+集团远程同位层次

**证据（quote → 来源）**
- 「ELKO Group – один із найбільших дистрибюторів…400 ІТ-виробників…10 000 партнерів у 10 країнах Європи」 — https://www.linkedin.com/company/elko-ukraine
- 「AAeon, Advantech, Aruba, Axiomtek, GIGA-IPC, IEI, Intel, Keenetic, Lanner, LR-Link, Mellanox, Mikrotik, Netis, Nexcom…Ubiquiti」 — https://www.elko.ua/ru/produkty/setevoe-oborudovanie-u-oficialnogo-distribyutora-elko-ukraine

**判位备档**(参考位，评级仍 B · 不出信）
- 参考 P1: `STC-424XGGPM-280W` — 波罗的海 VAD 集团乌克兰站——value PoE 档集团谱补位最对口
- 第一问: ELKO Group 在 value PoE 接入层（非 Aruba 谱）现用的主力 SKU 是哪家？
- 标签: 乌克兰|基辅|ELKO集团|波罗的海VAD集团

**备养出信稿（未触发，供后续用户启用参考）**
```text
Hi ELKO Ukraine team,

ELKO Group with 400 vendors and 10k partners across 10 European countries, and a Kyiv operation that still pushes MikroTik news out weekly - your IT-infrastructure catalog is one of the most attentive in the region.

We build a 24-port PoE+ managed switch (280W, L2-lite) with full English documentation. Reference: $180 USD EXW (2026-09-29) - built for the value PoE access tier that sits below the Aruba/TP-Link heavy lines in your catalog.

One question: below the Aruba-class shelf, which PoE access switch is carrying the value tier in your network-equipment lines today - and is there room for a documented second source?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

**待补证清单**
1. ELKO 谱里 PoE 接入交换现供 SKU 进深（TP-Link/Keenetic 之外的专属）
2. 战争下 ELKO Group 对 UA 库存位/采购口决策级（UA 站还是拉脱维亚集团）

**跟进建议（守档节奏）**
- D+3 ELKO 谱空位对照单页（TP-Link/Keenetic vs STC-424)
- D+14 具名 MikroTik 项目经理引见请求
- D+30 果归守档

> 备注: （乌克兰经营状态敏感:不触战事议题,只谈商业;如回插具名先问经营与物流现状是否仍正常）

<!-- BDEEP:B类深挖_2026-09-29_R57-BC_第2波 -->
## 七、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
