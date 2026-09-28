# Cristian Delogu / Netify

> **评级 A**　|　意大利 · Lodi　|　档案编号 `A-037`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-037
rating: A
country: 意大利
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（PoE/监控/门禁），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — 主场景匹配+首触只推一个型号的纪律；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Cristian Delogu / Netify（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Lodi | 事实 |
| 网站 | netify.it | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Cristian Delogu | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCSE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE+MTCSE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：cristian.delogu@netify.it
  - 状态：既有/公开
- **电话**：+39 335 127 4723
- **原始联系字段**：+39 335 127 4723 / cristian.delogu@netify.it
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Cristian Delogu**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：安防一体化：24 口 PoE++ 同时喂摄像头、门禁、对讲与 AP；算功率预算 + 看门狗（省上门），是他每个项目都用的账。
- **要问的问题**：他一个典型安防项目里，PoE 端口一共多少路、单口最大多少瓦？
- **随附证明**：整机功率实测 + 看门狗演示 + VLAN 分段示例。

### 第 2 次跟进 · 工业级非管理 PoE（闸机/停车场/室外）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：闸机、停车场、室外立柱的供电箱：宽温宽压、DIN、免配置，直接进他的现场箱标准。
- **要问的问题**：他们的室外/停车场的网络点现在怎么做防护？
- **随附证明**：宽温报告 + 户外箱方案 + 样机。

### 第 3 次跟进 · 管理型 PoE（安防网段隔离）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：安防与办公必须隔离（他持 MTCSE）：VLAN + 端口隔离 + ERPS；谈管理面安全配置（默认关闭外部管理、固件更新流程）。
- **要问的问题**：他的安防项目里要不要把监控/门禁与办公网物理或 VLAN 隔离？
- **随附证明**：VLAN/隔离模板 + 管理面安全清单 + ERPS 实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：洛迪（Lodi）的一体化安全系统公司 Netify：实体安防（报警、视频监控、闸机、门禁）+ 网络安全 + 企业网络基础设施设计，并提供 MikroTik 培训（自有讲师）。
- **产品线与在售品牌**：合作品牌含 MikroTik、Cambium Networks、Sophos、Nedap、Kalliope（VoIP）、Zucchetti Axess；方案线：Sicurezza Integrata、Unified Communication、Networking。
- **目标行业与场景**：企业/办公楼宇的安防与网络一体化项目（闸机、门禁、监控、对讲、VoIP、自服务前台）、需要网络与信息安全统一设计的客户。
- **团队与规模**：本地中小企业（洛迪及周边），决策链短；技术负责人 Cristian Delogu 持多证。
- **决策链与对接人**：cristian.delogu@netify.it；+39 335 127 4723。
- **技术与认证**：MikroTik 认证顾问（MTCNA+MTCRE+MTCSE）；公司有 MikroTik 认证讲师做「Formazione MikroTik」。
- **采购与供应链信号**：安防项目 → 大量 PoE 端口（摄像头/门禁/对讲/AP）；按项目采购，对功率预算与稳定性敏感。
- **近期动态与线索**：官网博客 2025 年更新（Self Reception、预测性视频分析），说明在推「安防+IT」一体化方案并持续获客。
- **与我方契合点**：监控+门禁+对讲+AP 全走 PoE：24 口 PoE++ 是标准件；闸机/停车场等室外点位用工业款；VLAN 分段（安防/办公/访客）用管理型。
- **风险与注意**：他重视合规与安全（MTCSE）→ 谈管理面安全配置与隔离能力，不要只谈价格。

### R54 原文证据摘录（全部保留）

- **【业务定位】**业务三大块：一体化安防、统一通信、网络。
  > sistemi e impianti di sicurezza integrata: dalla sicurezza fisica con sistemi di allarme, videosorveglianza, tornelli e controllo accessi, alla sicurezza informatica … con la cyber security e la progettazione di infrastrutture di rete ad hoc；SOLUZIONI DI SICUREZZA INTEGRATA｜SOLUZIONI UNIFIED COMMUNICATION｜SOLUZIONI DI NETWORKING
  > 来源：https://www.netify.it/
- **【产品线与在售品牌】**合作品牌含 MikroTik 与 Cambium、Sophos、Nedap（门禁）、Kalliope（VoIP）。
  > I partner certificati con cui lavoriamo ogni giorno：CAMBIUM NETWORKS｜KALLIOPE｜SOPHOS｜NEDAP N.V.｜MIKROTIK｜ZUCCHETTI AXESS
  > 来源：https://www.netify.it/
- **【目标行业与场景】**自有 MikroTik 培训业务（讲师授课）。
  > FORMAZIONE MIKROTIK — Seguire un corso di formazione MikroTik ti permette di ottenere una certificazione riconosciuta a livello internazionale … Apprendi tutto ciò che può servire sulle reti IP e ottieni le certificazioni MikroTik con il nostro Trainer.
  > 来源：https://www.netify.it/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（PoE/监控/门禁），且有具体人直联
- **W**：公开信息有限
- **O**：P1 场景切入（主场景匹配+首触只推一个型号的纪律）
- **T**：现有供应商惯性；价格竞争。

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
| 决策人识别 | ✅ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：Rugged 8-port PoE for outdoor/unheated cabinets

```text
Hi Cristian,

I came across Netify - 集成商/顾问（MikroTik 认证）.

We build an unmanaged industrial 8-port PoE switch (af/at) with 250m extended reach, redundant 44–57V DC input with reverse-polarity protection, DIN-rail mount and a 3-year warranty. Reference: $74.8 USD EXW.

One question: Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?

If it is useful, I can send one unit for a 30-day evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)
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

*建档日期：2026-09-22　|　结构 v2：2026-09-28（R56 规则）　|　数据来源：客户名单_反向信号_2026-09.csv + R54/R55 调研 JSON*
