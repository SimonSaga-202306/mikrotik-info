# Millbeck

> **评级 B**　|　英国　|　档案编号 `B-533`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-533
rating: B
country: 英国
biz_org: 分销/批发商（有官网）
business_model: 分销 stocking
decision_speed: moderate
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-10-07
```

## SALES BRIEF（压缩模型）

- **是谁**：MILLBECK COMMUNICATIONS LIMITED(Companies House 04501248;Wetherby 西约克郡;2002 年 **Paul Graham Finder = 创始董事总经理(1…
- **商业模式**：分销 stocking
- **为什么值得跟**：【2026-09-28 复核回升 C-285→B-533】官网联系页正文可见；邮箱补到后原「无邮箱（群发触达不到）」下放原因消除 → 恢复 B（群发可触达）。原判：三星依据仅渠道等级（分销）与「Teltonika（Diamond 最高级）」，需求未核。
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Diamond 排他谱外的招标双源/竞价对照位(PS:原『只有8口』切入点已被 SWM 谱推翻,修正)；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：公用事业招标要双源、或 Teltonika 交期紧时,你们对照件现用哪家?非 Teltonika 的文档全对照位可谈吗?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Millbeck（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 | 事实 |
| 网站 | millbeck.co.uk | 事实 |
| 类型 | 分销 | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Teltonika（Diamond 最高级） | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | MILLBECK COMMUNICATIONS LIMITED(Companies House 04501248;Wetherby 西约克郡;2002 年 **Paul Graham Finder = 创始董事总经理(1960 生,2002-08 在任至今)**;谱型=英国商业通信服务/VoIP/宽带/OLT(Fibre/ADSL/EFM/移动 4G);Da | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 【推断】Diamond 最高级=与 Teltonika 深绑,原档案『只有 8 口』切入点已被 SWM 管理型 PoE 新品推翻;但其宣传语自家写『不锁 vendor、兼容 Cisco/Juniper/HPE』——开放叙事留了第二源缝;公用事业项目招标常有双源要求 | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Millbeck(Millbeck Communications Ltd;Leeds LS17 9BF 6 Arena Park;**Teltonika Diamond Partner(官方最高级)16+ 年**):全谱 Teltonika——RUT 4G/5G 路由 + **TSW/SWM 交换谱(含 TSW202 管理工业 PoE+、SWM280/281/282 管理型 PoE)** + IoT SIM + 天线 + RMS rms.credit;**公用事业垂直深绑(水/气/电/热网络运营商 SCADA/智能计量 LTE-M/NB-IoT)**;自述开放式站位『without vendor lock-in, fully compatible with Cisco, Juniper, HPE』 | R65 深挖:Wetherby 电信 VoIP 老谱 2002;Finder 家族富二代 2024 接棒
- 【推断】Diamond 最高级=与 Teltonika 深绑,原档案『只有 8 口』切入点已被 SWM 管理型 PoE 新品推翻;但其宣传语自家写『不锁 vendor、兼容 Cisco/Juniper/HPE』——开放叙事留了第二源缝;公用事业项目招标常有双源要求
- 【假设】开口角度=「Diamond 排他谱之外的竞价对照/双源位」:STC-424 不做替换做双源——其 SWM 谱缺『非 Teltonika 品牌对照件』,招标双源场景与 Teltonika 交期紧时的备胎

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

【推断】Diamond 最高级=与 Teltonika 深绑,原档案『只有 8 口』切入点已被 SWM 管理型 PoE 新品推翻;但其宣传语自家写『不锁 vendor、兼容 Cisco/Juniper/HPE』——开放叙事留了第二源缝;公用事业项目招标常有双源要求

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：hello@millbeck.co
  - 状态：既有/公开
- **电话**：—
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：hello@millbeck.co.uk（官网联系页）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Paul Graham Finder | Founder & Managing Director | 经 millbeck.co.uk | Companies House + Tracxn 双源 | https://find-and-update.company-information.service.gov.uk/company/04501248/officers |
| Daniel Finder | Director(2024-11 新任) | 同上 | 同上 | 同上 |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 守档 D+3 · [双源对照] 招标场景页

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「Diamond 排他谱之外的竞价对照/双源位」:STC-424 不做替换做双源——其 SWM 谱缺『非 Teltonika 品牌对照件』,招标双源场景与 Teltonika 交期紧时的备胎
- **要问的问题**：公用事业招标要双源、或 Teltonika 交期紧时,你们对照件现用哪家?非 Teltonika 的文档全对照位可谈吗?
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 2 次跟进 · 守档 D+14 · hello@millbeck.co.uk 开口

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「Diamond 排他谱之外的竞价对照/双源位」:STC-424 不做替换做双源——其 SWM 谱缺『非 Teltonika 品牌对照件』,招标双源场景与 Teltonika 交期紧时的备胎
- **要问的问题**：公用事业招标要双源、或 Teltonika 交期紧时,你们对照件现用哪家?非 Teltonika 的文档全对照位可谈吗?
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 3 次跟进 · 守档 D+30 · 果归守档

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「Diamond 排他谱之外的竞价对照/双源位」:STC-424 不做替换做双源——其 SWM 谱缺『非 Teltonika 品牌对照件』,招标双源场景与 Teltonika 交期紧时的备胎
- **要问的问题**：公用事业招标要双源、或 Teltonika 交期紧时,你们对照件现用哪家?非 Teltonika 的文档全对照位可谈吗?
- **随附/动作**：随附 1 页特性对照/测试包说明


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-07(R65 第 12 批精修 = R57 转写 + 本轮 Companies House/KvK 新挖)**；原始记录：`batch/B类深挖_2026-10-07_R65_第12批.json`；价格均为 EXW 快照。

- **背景深描**：MILLBECK COMMUNICATIONS LIMITED(Companies House 04501248;Wetherby 西约克郡;2002 年 **Paul Graham Finder = 创始董事总经理(1960 生,2002-08 在任至今)**;谱型=英国商业通信服务/VoIP/宽带/OLT(Fibre/ADSL/EFM/移动 4G);Daniel Finder(1991 生)+Benjamin Finder(1994 生)2024-11 新任董事——富二代接棒家族谱
- **芯片与在用型号**：【推断】Diamond 最高级=与 Teltonika 深绑,原档案『只有 8 口』切入点已被 SWM 管理型 PoE 新品推翻;但其宣传语自家写『不锁 vendor、兼容 Cisco/Juniper/HPE』——开放叙事留了第二源缝;公用事业项目招标常有双源要求
- **关键人KP**：Paul Graham Finder = Founder & Managing Director(核查处 1960 生);Daniel/Benjamin Finder = 2024-11 新任双董事
- **关注点与资质**：Teltonika（Diamond 最高级） 
- **优缺点SWOT**：S:Diamond 最高级+公用事业深垂直+16 年 / W:Teltonika 排他深绑 / O:招标双源/交期备胎对照位(其自写不锁 vendor) / T:Diamond 忠诚冲突
- **Saga产品适配**：Diamond 排他谱外的招标双源/竞价对照位(PS:原『只有8口』切入点已被 SWM 谱推翻,修正)

### R55 证据摘录（全部保留 · 含数量）

- **【R57备护深挖证据】**Millbeck is a Teltonika Diamond Partner…TSW/SWM switch range: unmanaged industrial TSW switches and SWM managed PoE switches for enterprise 
  > Millbeck is a Teltonika Diamond Partner…TSW/SWM switch range: unmanaged industrial TSW switches and SWM managed PoE switches for enterprise LAN, CCTV, smart building and industrial automation…without vendor lock-in
  > 来源：https://millbeck.co.uk/teltonika-switches/
- **【R57备护深挖证据】**Millbeck supplies multi-network IoT SIMs, industrial routers…water, gas, electricity and heat network operators…private APN services, fixed 
  > Millbeck supplies multi-network IoT SIMs, industrial routers…water, gas, electricity and heat network operators…private APN services, fixed private IP addressing for SCADA
  > 来源：https://millbeck.co.uk/solutions/utilities
- **【R65 商业登记】**Millbeck Communications Ltd 04501248 · Wetherby 2002 · Paul Finder 创始 MD+2024 年 Daniel/Benjamin Finder 新董事
  > FINDER, Paul Graham Role Active: Director Date of birth: August 1960 … Founded in 2002 by Paul Finder … The founders of Millbeck Communications is Paul Finder
  > 来源：https://tracxn.com/d/companies/millbeck-communications/__txNX05Uaoy5lfW7NMbICWfCeiasg7vXQEi5eN4DW-C0

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Diamond 排他谱外的招标双源/竞价对照位(PS:原『只有8口』切入点已被 SWM 谱推翻,修正) |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S:Diamond 最高级+公用事业深垂直+16 年 / W:Teltonika 排他深绑 / O:招标双源/交期备胎对照位(其自写不锁 vendor) / T:Diamond 忠诚冲突

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

- **深挖专属待问（R56）**：
  - [ ] SWM 交换谱上市后的客户接受度与价带
  - [ ] 公用事业招标里双源要求出现频度

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE value slot for your line

```text
Hi Millbeck team,

Sixteen years as a Teltonika Diamond Partner with utility networks on your customer list - and your own switching page still says without vendor lock-in. That sentence is exactly where a second source lives.

We build a 24-port PoE+ managed switch (280W, L2-lite) with full English documentation. Reference: $180 USD EXW (2026-09-29) - not a Teltonika replacement; the documented comparison unit for tender dual-source requirements and tight-lead-time weeks, white-label friendly.

One question: when a utility tender asks for a second source, or Teltonika lead time stretches, which switch do you quote as the alternative today - and would a documented unit earn a bench test for that slot?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

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
