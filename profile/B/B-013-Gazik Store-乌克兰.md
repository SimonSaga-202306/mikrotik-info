# Gazik Store

> **评级 B**　|　乌克兰　|　档案编号 `B-013`　|　优先级 ★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：B　**Maybe** —— 不太明显，慢跟待验证
- **评级依据**：通用分销商信号，无差异化切入点，慢慢跟
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Gazik Store |
| 国家 | 乌克兰 |
| 城市 | — |
| 网站 | gazik.ua |
| 类型 | 分销（MikroTik 官方） |
| 反向信号 | MikroTik（Reseller） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-480XGGM（Saga） |
| 切入点 | 卖 MikroTik 但缺工业/ERPS/PoE++ → 用同价位工业线补他的产品缺口 |
| 数据来源 | 2026-09-22 |
| 原备注 | Lviv |

## 三、人员与联系方式

- **邮箱**：orest@gazik.in
- **电话**：+380 67 323 17 30
- **原始联系字段**：+380 67 323 17 30 / orest@gazik.in

## 四、品牌与技术栈

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景**：待摸底

保持低频联系，等他出现交换机需求信号再提级为 A。

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
- 【事实】Gazik Store（利沃夫 Stryjska 202）:2006 创网销连锁+Lviv 实体店;**自联 ISP 自营（「продаємо тільки перевірений товар нашими фахівцями на власній мережі」=自验过才卖）**;PON/radio 谱+ZTE/MikroTik/Ubiquiti/Extralink/Netis/TPLINK/D-Link PON ONU 分销;欧洲/美国/中国自主进出口分销血统
- 【推断】GAZIK 是「店+ISP 自营」双形态血统——自营 ISP 意味着真实企业户 PoE 部署场景;PON/radio 优先,接入层 PoE 是 ISP 运营的副产业（AP/监控陈设）
- 【假设】开口角度=「你自家 ISP 网络里部署 AP/监控时的 PoE 稳健需求」以及店内 value PoE 档——STC-424 对客段位正口

**SWOT 速描**
- **S**: 自营 ISP 实操+店网双开
- **W**: 焦点全在 PON/radio
- **O**: STC-424 ISP 副段位
- **T**: 店铺行情风,价动能高

**证据（quote → 来源）**
- 「продаємо тільки перевірений товар нашими фахівцями на власній мережі…Ми працюємо, як з роздрібними так і оптовими клієнтами」 — https://hotline.ua/ua/yp/32481/reviews/
- 「Продаж мережевого обладнання ZTE, Mikrotik, Totolink, Extralight, Netis, TPLINK, D-link (PON, ONU)…інтернет-магазин для інтернет провайдерів」 — https://gazik.ua/

**判位备档**(参考位，评级仍 B · 不出信）
- 参考 P1: `STC-424DGGPM-280W` — 店+ISP 双血统:自营网络部署副位+店铺 value PoE 档
- 第一问: 你们自营 ISP 上对客部署(AP/监控）里,PoE 接入现供哪家？
- 标签: 乌克兰|利沃夫|店网血统|ISP自营

**备养出信稿（未触发，供后续用户启用参考）**
```text
Hi Gazik team,

A store chain on one side, a running ISP on the other, and the rule "we only sell what our own specialists run on our own network" - that is a rare level of honesty for a reseller.

We build a 24-port PoE+ managed switch (280W, L2-lite) with full English/Ukrainian-friendly documentation. Reference: $165 USD EXW (2026-09-29) - the kind of value PoE line you could bench-test on your own ISP before listing it in store.

One question: for the AP/surveillance deployments on your ISP side, which PoE access switch do you run today - and would a documented bench-trial unit earn a look?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

**待补证清单**
1. 自营 ISP 层的规模与 PoE 部署面
2. 店内 value PoE 档 SKU 现状

**跟进建议（守档节奏）**
- D+3 ISP 副段位方案页
- D+14 样机提议
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
