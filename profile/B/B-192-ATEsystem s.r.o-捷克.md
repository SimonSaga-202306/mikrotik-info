# ATEsystem s.r.o.

> **评级 B**　|　捷克　|　档案编号 `B-192`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-192
rating: B
country: 捷克
biz_org: 分销/批发商（有官网）
business_model: 分销 stocking
decision_speed: moderate
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: false, oem: true, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-10-07
```

## SALES BRIEF（压缩模型）

- **是谁**：ATEsystem s.r.o.(Ostrava Technologická 378/9(+Jablonec 分部);2013 创,11-50 人;**判型翻转=机器视觉(machine vision)专精集成商+组件分…
- **商业模式**：分销 stocking
- **为什么值得跟**：通用分销商信号，无差异化切入点，慢慢跟
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — 机器视觉集成商 turnkey BOM 的 GigE 相机 PoE 供电 DIN 轨位(Antaira 旁二源或 OEM 变体)；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：你们的 turnkey 视觉系统 BOM 里,GigE 相机供电的 DIN 轨 PoE 交换现随哪家?Antaira 旁二源有位吗?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | ATEsystem s.r.o.（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 捷克 | 事实 |
| 网站 | atesystem.cz | 事实 |
| 类型 | 分销（Antaira 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Antaira | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | ATEsystem s.r.o.(Ostrava Technologická 378/9(+Jablonec 分部);2013 创,11-50 人;**判型翻转=机器视觉(machine vision)专精集成商+组件分销**:Basler/JAI/Automation Technology/Computar/Kowa/SCHNEIDER/CCS/Effil | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 【推断】**GigE Vision 工业相机几乎全 PoE 供电**——机器视觉产线的 PoE 交换是其方案里真实伴随件(相机直连 PoE 网口);其 turnkey 项目把相机+光源+工控+网络一起投标,PoE 交换是 BOM 常客 | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】ATEsystem s.r.o.(Ostrava Technologická 378/9(+Jablonec 分部);2013 创,11-50 人;**判型翻转=机器视觉(machine vision)专精集成商+组件分销**:Basler/JAI/Automation Technology/Computar/Kowa/SCHNEIDER/CCS/Effilux 相机组件官分(捷克+斯洛伐克);**自有机器视觉 turnkey 系统开发**;NI Silver Alliance Partner;EU 基金研发;具名团队(Filip Volný 销售主管/Petr Bílovský 系统集成/Christian Kremser 工业相机);CSV 标 Antaira 授权为其工业网络件出处
- 【推断】**GigE Vision 工业相机几乎全 PoE 供电**——机器视觉产线的 PoE 交换是其方案里真实伴随件(相机直连 PoE 网口);其 turnkey 项目把相机+光源+工控+网络一起投标,PoE 交换是 BOM 常客
- 【假设】开口角度=「机器视觉产线的相机供电 DIN 轨 PoE 位」:STI-288GP 以其 turnkey 系统 BOM 的 GigE 相机供电伴 随件入(DIN 轨+工业温宽对机器视觉严苛现场)

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

【推断】**GigE Vision 工业相机几乎全 PoE 供电**——机器视觉产线的 PoE 交换是其方案里真实伴随件(相机直连 PoE 网口);其 turnkey 项目把相机+光源+工控+网络一起投标,PoE 交换是 BOM 常客

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、OEM/白牌
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - OEM/白牌：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- ATEsystem s.r.o.(Ostrava Technologická 378/9(+Jablonec 分部);2013 创,11-50 人;**判型翻转=机器视觉(machine vision)专精集成商+组件分销**:Basler/JAI/Automation Technology/Computar/Kowa/SCHNEIDER/CCS/Effilux 相机组件官分(捷克+斯洛伐克);**自有机器视觉 turnkey 系统开发**;NI Silver Alliance Partner;EU 基金研发;具名团队(Filip Volný 销售主管/Petr Bílovský 系统集成/C

## 联系方式（已有/猜测分标）

- **邮箱**：atesystem@atesystem.cz
  - 状态：既有/公开
- **电话**：+420 595 172 720
- **原始联系字段**：+420 595 172 720 / atesystem@atesystem.cz
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 守档 D+3 · 机器视觉 BOM PoE 对位页

- **推什么**：STI-288GP（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「机器视觉产线的相机供电 DIN 轨 PoE 位」:STI-288GP 以其 turnkey 系统 BOM 的 GigE 相机供电伴 随件入(DIN 轨+工业温宽对机器视觉严苛现场)
- **要问的问题**：你们的 turnkey 视觉系统 BOM 里,GigE 相机供电的 DIN 轨 PoE 交换现随哪家?Antaira 旁二源有位吗?
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 2 次跟进 · 守档 D+14 · atesystem@atesystem.cz 开口

- **推什么**：STI-288GP（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「机器视觉产线的相机供电 DIN 轨 PoE 位」:STI-288GP 以其 turnkey 系统 BOM 的 GigE 相机供电伴 随件入(DIN 轨+工业温宽对机器视觉严苛现场)
- **要问的问题**：你们的 turnkey 视觉系统 BOM 里,GigE 相机供电的 DIN 轨 PoE 交换现随哪家?Antaira 旁二源有位吗?
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 3 次跟进 · 守档 D+30 · 果归守档

- **推什么**：STI-288GP（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「机器视觉产线的相机供电 DIN 轨 PoE 位」:STI-288GP 以其 turnkey 系统 BOM 的 GigE 相机供电伴 随件入(DIN 轨+工业温宽对机器视觉严苛现场)
- **要问的问题**：你们的 turnkey 视觉系统 BOM 里,GigE 相机供电的 DIN 轨 PoE 交换现随哪家?Antaira 旁二源有位吗?
- **随附/动作**：随附 1 页特性对照/测试包说明


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-09-29(R57 备护深挖转写 2026-10-07)**；原始记录：`batch/B类深挖_2026-10-07_R65_R57转写.json`；价格均为 EXW 快照。

- **背景深描**：ATEsystem s.r.o.(Ostrava Technologická 378/9(+Jablonec 分部);2013 创,11-50 人;**判型翻转=机器视觉(machine vision)专精集成商+组件分销**:Basler/JAI/Automation Technology/Computar/Kowa/SCHNEIDER/CCS/Effilux 相机组件官分(捷克+斯洛伐克);**自有机器视觉 turnkey 系统开发**;NI Silver Alliance Partner;EU 基金研发;具名团队(Filip Volný 销售主管/Petr Bílovský 系统集成/C
- **芯片与在用型号**：【推断】**GigE Vision 工业相机几乎全 PoE 供电**——机器视觉产线的 PoE 交换是其方案里真实伴随件(相机直连 PoE 网口);其 turnkey 项目把相机+光源+工控+网络一起投标,PoE 交换是 BOM 常客
- **关键人KP**：—
- **关注点与资质**：Antaira 
- **优缺点SWOT**：S:机器视觉专精+自研 turnkey+多国相机牌 / W:Antaira 授权已在位 / O:GigE 相机 PoE 供电 DIN 轨伴随刚需 / T:Antaira 排他
- **Saga产品适配**：机器视觉集成商 turnkey BOM 的 GigE 相机 PoE 供电 DIN 轨位(Antaira 旁二源或 OEM 变体)

### R55 证据摘录（全部保留 · 含数量）

- **【R57备护深挖证据】**comprehensive services in machine vision and visual inspection…official distributor of machine vision components (Basler, JAI, Computar, Kow
  > comprehensive services in machine vision and visual inspection…official distributor of machine vision components (Basler, JAI, Computar, Kowa, CCS, Effilux…) for the Czech Republic and Slovakia…NI Silver Alliance Partner
  > 来源：https://cz.linkedin.com/company/atesystem
- **【R57备护深挖证据】**vlastnímu vývoji strojového vidění na klíč…testy a studie proveditelnosti, zápůjčky kamer
  > vlastnímu vývoji strojového vidění na klíč…testy a studie proveditelnosti, zápůjčky kamer
  > 来源：https://cz.linkedin.com/company/atesystem

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 机器视觉集成商 turnkey BOM 的 GigE 相机 PoE 供电 DIN 轨位(Antaira 旁二源或 OEM 变体) |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S:机器视觉专精+自研 turnkey+多国相机牌 / W:Antaira 授权已在位 / O:GigE 相机 PoE 供电 DIN 轨伴随刚需 / T:Antaira 排他

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**停止开发条件（命中任一即停）**：3 次定向触达无任何实质回复；确认现用平台完全满足需求；只愿比价不愿谈场景；决策者确认接触不到；对方书面拒绝。

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（PoE/接入层池） | ✅ |
| 决策人识别 | ❓ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 其 turnkey BOM 里 PoE 交换现供(Antaira?)与价位
  - [ ] GigE 相机功率谱(PoE vs PoE+ 需求)

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE value slot for your line

```text
Hi ATEsystem team,

Machine vision turnkey systems with Basler and JAI cameras on the line card - every GigE camera you deploy is a PoE load on a DIN rail in a harsh cabinet. You know exactly what those camera power budgets look like.

We build an 8-port Gigabit industrial PoE switch (DIN-rail, fanless, -40..75C class) with full English/Czech documentation. Reference: $74.8 USD EXW (2026-09-29) - the value-side second source for your vision-system BOMs, fully open to an OEM variant under your terms.

One question: inside your turnkey vision BOMs, which DIN-rail PoE switch feeds the GigE cameras today - and would a documented second source earn a bench test in your feasibility lab?

If useful, I can send one unit with the complete test pack (surge 6 kV, EFT/ESD data sheet, cold-start log). If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；③ 落款换成你自己的名字与公司；④ **一次只问一个问题**；⑤ 货币单位一律 USD 并带快照日期；⑥ 该客户为教师/公立身份时先读「本户特别红线」。

## 跟进记录

| 日期 | 渠道（邮件/电话/LinkedIn/展会） | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 首次触达前留空；发出邮件后填入日期与渠道。有新进展时告诉我，我来更新本档案并重评 stage。

## 下次复核

- 固定节点：首触发出后 **14 天**无回复 → 复核是否降频/降级；有任何回复 → 当即重评 stage 与评级。
- 报价纪律：全部价格为 USD EXW 快照（2026-09-28，15 天有效）；过窗先核价再报价。

---

*建档日期：2026-09-22　|　结构 v2：2026-10-07（R56 规则 · R65 B 类对齐 A 标准）　|　数据来源：客户名单_反向信号_2026-09.csv + B 类深挖调研 JSON*
