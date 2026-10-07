# Pymatek Automation

> **评级 B**　|　英国　|　档案编号 `B-421`　|　优先级 ★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-421
rating: B
country: 英国
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

- **是谁**：Pymatek Automation Ltd(CH 09293772,2014-11-04 注册,Venture Point Wheelhouse Rd, Rugeley WS15 1UZ, Staffordshire;…
- **商业模式**：分销 stocking
- **为什么值得跟**：有信号（工业/楼宇）但需先验证需求或联系人不具体
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — EtherWAN/Hirschmann 双高价谱旁的 DIN 轨 value 第三源(英国+拉美 11 国复用)；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：你们 EtherWAN/Hirschmann 客户在预算紧的项目里,value DIN 轨 PoE 现无供?第三源 OEM 变体可谈吗?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Pymatek Automation（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 | 事实 |
| 网站 | pymatek.co.uk | 事实 |
| 类型 | 分销（EtherWAN 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | EtherWAN 英国分销商（同时在西班牙及拉美多国分销）；站点按品牌建档，主营工业自动化供货 | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | Pymatek Automation Ltd(CH 09293772,2014-11-04 注册,Venture Point Wheelhouse Rd, Rugeley WS15 1UZ, Staffordshire;SIC 71129 Other engineering activities;3 员工规模;主域=pymatek.com(非 .co.uk) | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 【推断】工业交换在其谱里已有 EtherWAN+Hirschmann 两高价牌——value 档缺位;其独特资产=英公司做西语拉美 11 国渠道(Se habla español),DIN 轨工业件跨区流动 | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Pymatek Automation(Staffordshire 01543 区;VAT GB 2060 155 3431;pymatek.us 美国站):**工业自动化零组件大目录分销商**(PLC/驱动/HMI/电机/编码器;ABB/Siemens/Schneider/Mitsubishi/Omron/Bosch Rexroth 全谱);**同时分销两大工业交换牌:EtherWAN(凤凰触点旗下台厂)+Hirschmann(Belden)**,另带 eWON;**分销区域=英国+美国+西语拉美 11 国**(墨西哥/秘鲁/西班牙/玻利维亚/智利/哥伦比亚/厄瓜多尔/阿根廷/乌拉圭/巴拉圭) | R64/R65 补:Ybet 唯一董事 CH 实名 + pymatek.com 主域(非 .co.uk)
- 【推断】工业交换在其谱里已有 EtherWAN+Hirschmann 两高价牌——value 档缺位;其独特资产=英公司做西语拉美 11 国渠道(Se habla español),DIN 轨工业件跨区流动
- 【假设】开口角度=「EtherWAN/Hirschmann 双高价旁的 DIN 轨 value 第三源」:STI-288GP 以差价位进,兼提其拉美站的 value 需求带(价格敏)+OEM 变体

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

【推断】工业交换在其谱里已有 EtherWAN+Hirschmann 两高价牌——value 档缺位;其独特资产=英公司做西语拉美 11 国渠道(Se habla español),DIN 轨工业件跨区流动

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、OEM/白牌
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - OEM/白牌：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- Pymatek Automation Ltd(CH 09293772,2014-11-04 注册,Venture Point Wheelhouse Rd, Rugeley WS15 1UZ, Staffordshire;SIC 71129 Other engineering activities;3 员工规模;主域=pymatek.com(非 .co.uk)MX outlook 存活;Ybet Haydeé Sánchez Vargas de Pattison 唯一登记董事(2014 至今,1975-06 生);Martin Pattison 销市经理/Franco Sanchez 销售主管/Kimberly Pinillos GM,GlobalDatabase 全自曝

## 联系方式（已有/猜测分标）

- **邮箱**：sales@pymatek.co
  - 状态：既有/公开
- **电话**：—
- **原始联系字段**：官网联系页
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Ybet Sánchez Vargas de Pattison**(Director(2014 至今,唯一登记董事))— ybet@pymatek.com 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://www.companiesintheuk.co.uk/ltd/pymatek-automation〕
  - **Martin Pattison**(Sales Manager)— martin@pymatek.com 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://uk.globaldatabase.com/company/pymatek-automation-ltd〕
  - **Franco Sanchez**(Jefe De Ventas)— franco@pymatek.com 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:同 GlobalDatabase 源〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Ybet Sánchez Vargas de Pattison | Director(2014 至今,唯一登记董事) | ybet@pymatek.com | guessed-leads-only(域 MX 存活;SMTP 未验;不进群发) | https://www.companiesintheuk.co.uk/ltd/pymatek-automation |
| Martin Pattison | Sales Manager | martin@pymatek.com | guessed-leads-only(域 MX 存活;SMTP 未验;不进群发) | https://uk.globaldatabase.com/company/pymatek-automation-ltd |
| Franco Sanchez | Jefe De Ventas | franco@pymatek.com | guessed-leads-only(域 MX 存活;SMTP 未验;不进群发) | 同 GlobalDatabase 源 |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 守档 D+3 · 双牌对位表+拉美 value 带提案

- **推什么**：STI-288GP（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「EtherWAN/Hirschmann 双高价旁的 DIN 轨 value 第三源」:STI-288GP 以差价位进,兼提其拉美站的 value 需求带(价格敏)+OEM 变体
- **要问的问题**：你们 EtherWAN/Hirschmann 客户在预算紧的项目里,value DIN 轨 PoE 现无供?第三源 OEM 变体可谈吗?
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 2 次跟进 · 守档 D+14 · sales@pymatek.co.uk 开口(西英双版)

- **推什么**：STI-288GP（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「EtherWAN/Hirschmann 双高价旁的 DIN 轨 value 第三源」:STI-288GP 以差价位进,兼提其拉美站的 value 需求带(价格敏)+OEM 变体
- **要问的问题**：你们 EtherWAN/Hirschmann 客户在预算紧的项目里,value DIN 轨 PoE 现无供?第三源 OEM 变体可谈吗?
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 3 次跟进 · 守档 D+30 · 果归守档

- **推什么**：STI-288GP（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「EtherWAN/Hirschmann 双高价旁的 DIN 轨 value 第三源」:STI-288GP 以差价位进,兼提其拉美站的 value 需求带(价格敏)+OEM 变体
- **要问的问题**：你们 EtherWAN/Hirschmann 客户在预算紧的项目里,value DIN 轨 PoE 现无供?第三源 OEM 变体可谈吗?
- **随附/动作**：随附 1 页特性对照/测试包说明


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-07(R65 第 2 批精修 = R57 转写 + R64 KP + CH/GlobalDatabase 补)**；原始记录：`batch/B类深挖_2026-10-07_R65_第2批.json`；价格均为 EXW 快照。

- **背景深描**：Pymatek Automation Ltd(CH 09293772,2014-11-04 注册,Venture Point Wheelhouse Rd, Rugeley WS15 1UZ, Staffordshire;SIC 71129 Other engineering activities;3 员工规模;主域=pymatek.com(非 .co.uk)MX outlook 存活;Ybet Haydeé Sánchez Vargas de Pattison 唯一登记董事(2014 至今,1975-06 生);Martin Pattison 销市经理/Franco Sanchez 销售主管/Kimberly Pinillos GM,GlobalDatabase 全自曝
- **芯片与在用型号**：【推断】工业交换在其谱里已有 EtherWAN+Hirschmann 两高价牌——value 档缺位;其独特资产=英公司做西语拉美 11 国渠道(Se habla español),DIN 轨工业件跨区流动
- **关键人KP**：（见 R64 KP 猎捕节/本档 KP 表）
- **关注点与资质**：EtherWAN 英国分销商（同时在西班牙及拉美多国分销）；站点按品牌建档，主营工业自动化供货 | 传承人名开口：见 KP 表
- **优缺点SWOT**：S:双工业牌已带+11 国跨区域+大目录 / W:第三家工业交换品牌教育成本 / O:value DIN 轨第三源+拉美价差带 / T:EtherWAN 排他条款
- **Saga产品适配**：EtherWAN/Hirschmann 双高价谱旁的 DIN 轨 value 第三源(英国+拉美 11 国复用)

### R55 证据摘录（全部保留 · 含数量）

- **【R57备护深挖证据】**Distributor of Etherwan in UK…Hirschmann industrial connectivity solutions: industrial Ethernet switches, M12 connectors, industrial network
  > Distributor of Etherwan in UK…Hirschmann industrial connectivity solutions: industrial Ethernet switches, M12 connectors, industrial networking systems
  > 来源：https://www.pymatek.co.uk/manufacturers/542-etherwan/
- **【R57备护深挖证据】**Distributor of Etherwan in UK, Perú, Bolivia, España, Colombia, México, Ecuador, Chile, Argentina, Uruguay, Paraguay
  > Distributor of Etherwan in UK, Perú, Bolivia, España, Colombia, México, Ecuador, Chile, Argentina, Uruguay, Paraguay
  > 来源：https://www.pymatek.co.uk/manufacturers/542-etherwan/
- **【R57备护深挖证据】**PLCs, servo motors, variable frequency drives, HMIs, encoders…ABB, Siemens, Schneider Electric, Mitsubishi Electric, Omron
  > PLCs, servo motors, variable frequency drives, HMIs, encoders…ABB, Siemens, Schneider Electric, Mitsubishi Electric, Omron
  > 来源：https://www.pymatek.us/
- **【R64 CH 实名】**PYMATEK AUTOMATION LTD CH 09293772,2014-11-04 注册,Rugeley WS15 1UZ;Ybet SÁNCHEZ VARGAS DE PATTISON 唯一现任董事
  > PYMATEK AUTOMATION LTD. Company number: 09293772 … Incorporated on 4 November 2014 … Directors: 1 … Mrs. Ybet Haydee Sanchez Vargas De Pattison 04 Nov 2014
  > 来源：https://www.companiesintheuk.co.uk/ltd/pymatek-automation
- **【R64 团队层自曝】**pymatek.com 域内:Ybet(Director)/Franco Sanchez(Jefe De Ventas)/Martin Pattison(Sales Manager)/Lucero Vaenzuela(Admin Asst)/Kimberly Pinillos(Gerente General)
  > Ybet Sanchez Vargas De Pattison Director … Franco Sanchez Jefe De Ventas … Martin Pattison Sales Manager … Kimberly Pinillos Gerente General … @pymatek.com
  > 来源：https://uk.globaldatabase.com/company/pymatek-automation-ltd
- **【R64 域名核正】**CSV 网站=pymatek.co.uk(名录口径),实际职能域=pymatek.com(全员邮箱挂 pymatek.com),MX outlook 存活——候选挂 pymatek.com 系
  > (GlobalDatabase 员工邮箱全挂 ****@pymatek.com)
  > 来源：https://uk.globaldatabase.com/company/pymatek-automation-ltd

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | EtherWAN/Hirschmann 双高价谱旁的 DIN 轨 value 第三源(英国+拉美 11 国复用) |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S:双工业牌已带+11 国跨区域+大目录 / W:第三家工业交换品牌教育成本 / O:value DIN 轨第三源+拉美价差带 / T:EtherWAN 排他条款

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
  - [ ] EtherWAN/Hirschmann 在谱价位带(其客户价值缺口在哪)
  - [ ] 拉美 11 国站的 value 件需求真实量级

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE value slot for your line

```text
Hi Pymatek team,

EtherWAN and Hirschmann on the same industrial shelf, plus plain-Spanish channels into eleven Latin American markets - you already run two premium industrial Ethernet names, and you know exactly where the budget-constrained projects walk away.

We build an 8-port Gigabit industrial PoE switch (DIN-rail, fanless, -40..75C class) with full English/Spanish documentation. Reference: $74.8 USD EXW (2026-09-29) - strictly the value-side third source beside your premium pair, fully open to an OEM variant under your terms.

One question: for your EtherWAN/Hirschmann buyers with tight project budgets - especially in Latin America - is there a documented value-side DIN-rail source in your line-up today, or is that slot still open?

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
