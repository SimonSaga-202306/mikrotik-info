# ATEsystem s.r.o.

> **评级 B**　|　捷克　|　档案编号 `B-192`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：B　**Maybe** —— 不太明显，慢跟待验证
- **评级依据**：通用分销商信号，无差异化切入点，慢慢跟
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | ATEsystem s.r.o. |
| 国家 | 捷克 |
| 城市 | — |
| 网站 | atesystem.cz |
| 类型 | 分销（Antaira 授权） |
| 反向信号 | Antaira |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-488XGGPM（Saga） |
| 切入点 | 工业/轨道同规格 1/3 价第二供应源 |
| 数据来源 | 2026-09-22 |
| 原备注 | 俄斯特拉发，捷克 T1 |

## 三、人员与联系方式

- **邮箱**：atesystem@atesystem.cz
- **电话**：+420 595 172 720
- **原始联系字段**：+420 595 172 720 / atesystem@atesystem.cz

## 四、品牌与技术栈

**涉及品牌 / 技术**：Antaira

## 五、跟进策略

**场景**：待摸底

保持低频联系，等他出现交换机需求信号再提级为 A。

参考型号：`STI-488XGGPM（Saga）`

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 备护深挖(2026-09-29 · R57-BC 轻量对齐 A · 评级不动、不出信）

**深挖三层**
- 【事实】ATEsystem s.r.o.(Ostrava Technologická 378/9(+Jablonec 分部);2013 创,11-50 人;**判型翻转=机器视觉(machine vision)专精集成商+组件分销**:Basler/JAI/Automation Technology/Computar/Kowa/SCHNEIDER/CCS/Effilux 相机组件官分(捷克+斯洛伐克);**自有机器视觉 turnkey 系统开发**;NI Silver Alliance Partner;EU 基金研发;具名团队(Filip Volný 销售主管/Petr Bílovský 系统集成/Christian Kremser 工业相机);CSV 标 Antaira 授权为其工业网络件出处
- 【推断】**GigE Vision 工业相机几乎全 PoE 供电**——机器视觉产线的 PoE 交换是其方案里真实伴随件(相机直连 PoE 网口);其 turnkey 项目把相机+光源+工控+网络一起投标,PoE 交换是 BOM 常客
- 【假设】开口角度=「机器视觉产线的相机供电 DIN 轨 PoE 位」:STI-288GP 以其 turnkey 系统 BOM 的 GigE 相机供电伴 随件入(DIN 轨+工业温宽对机器视觉严苛现场)

**SWOT 速描**
- **S**: 机器视觉专精+自研 turnkey+多国相机牌
- **W**: Antaira 授权已在位
- **O**: GigE 相机 PoE 供电 DIN 轨伴随刚需
- **T**: Antaira 排他

**证据（quote → 来源）**
- 「comprehensive services in machine vision and visual inspection…official distributor of machine vision components (Basler, JAI, Computar, Kowa, CCS, Effilux…) for the Czech Republic and Slovakia…NI Silver Alliance Partner」 — https://cz.linkedin.com/company/atesystem
- 「vlastnímu vývoji strojového vidění na klíč…testy a studie proveditelnosti, zápůjčky kamer」 — https://cz.linkedin.com/company/atesystem

**判位备档**(参考位，评级仍 B · 不出信）
- 参考 P1: `STI-288GP` — 机器视觉集成商 turnkey BOM 的 GigE 相机 PoE 供电 DIN 轨位(Antaira 旁二源或 OEM 变体)
- 第一问: 你们的 turnkey 视觉系统 BOM 里,GigE 相机供电的 DIN 轨 PoE 交换现随哪家?Antaira 旁二源有位吗?
- 标签: 捷克|俄斯特拉发|机器视觉|GigE相机PoE刚需|NI伙伴

**备养出信稿（未触发，供后续用户启用参考）**
```text
Hi ATEsystem team,

Machine vision turnkey systems with Basler and JAI cameras on the line card - every GigE camera you deploy is a PoE load on a DIN rail in a harsh cabinet. You know exactly what those camera power budgets look like.

We build an 8-port Gigabit industrial PoE switch (DIN-rail, fanless, -40..75C class) with full English/Czech documentation. Reference: $74.8 USD EXW (2026-09-29) - the value-side second source for your vision-system BOMs, fully open to an OEM variant under your terms.

One question: inside your turnkey vision BOMs, which DIN-rail PoE switch feeds the GigE cameras today - and would a documented second source earn a bench test in your feasibility lab?

If useful, I can send one unit with the complete test pack (surge 6 kV, EFT/ESD data sheet, cold-start log). If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

**待补证清单**
1. 其 turnkey BOM 里 PoE 交换现供(Antaira?)与价位
2. GigE 相机功率谱(PoE vs PoE+ 需求)

**跟进建议（守档节奏）**
- D+3 机器视觉 BOM PoE 对位页
- D+14 atesystem@atesystem.cz 开口
- D+30 果归守档

<!-- BDEEP:B类深挖_2026-09-29_R57-BC_第10波 -->
## 七、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
