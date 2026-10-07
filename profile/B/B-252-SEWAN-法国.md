# SEWAN

> **评级 B**　|　法国　|　档案编号 `B-252`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-252
rating: B
country: 法国
biz_org: 分销/批发商（有官网）
business_model: 分销 stocking
decision_speed: moderate
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: true, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-10-07
```

## SALES BRIEF（压缩模型）

- **是谁**：SEWAN(法国电信 ETI 大户;2007 年 Alexis de Goriaïnoff + 3 名联合创始人联合创立——从同一运营商 4 人「全员辞职」创办起家;谱型=Cloud+Télécoms 生态/自创 Saa…
- **商业模式**：分销 stocking
- **为什么值得跟**：有信号（ISP/骨干）但需先验证需求或联系人不具体
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — 欧 B2B 运营型:OEM 白标(SEWAN 牌）供给其渠道伙伴部署 SME 接入用；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：你们渠道伙伴在 SME 部署里 PoE 接入现供哪家？白标 OEM 新鲜件可谈？
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | SEWAN（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 | 事实 |
| 网站 | sewan.fr | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Master） | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | SEWAN(法国电信 ETI 大户;2007 年 Alexis de Goriaïnoff + 3 名联合创始人联合创立——从同一运营商 4 人「全员辞职」创办起家;谱型=Cloud+Télécoms 生态/自创 SaaS「Sophia」;300-1000 员工/75M€ 收；总部巴黎+贝尔福/蒙彼利埃；西班牙/德/意/荷国际化);**Alexis de G | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 【推断】SEWAN 实为运营型：接入是 dead simple 的构线（间接销售模型），它不卖硬件但它提供客户网点（SME）的接入设备组件列表——价值=渠道伙伴部署时使用的 OEM 白标设备供给链 | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】SEWAN(法国 Paris 2 Cité Paradis 75010):**B2B 运营商（非分销！)**——2007 创 450 人，2019-11 Kartesia €75M 投资加持；55k 企业客户/4 国网络（法/西 Vozelia/比 3StarsNet/德 42one);间接销售模式（渠道销合作伙伴）;通讯+连接+托管全家（真 RE fixe/mobile/UC/xDSL/云）具直技术面 | R65 深挖:SEWAN 法国 ETI 巨号;同代电信云族 75M€/自建 Sophia
- 【推断】SEWAN 实为运营型：接入是 dead simple 的构线（间接销售模型），它不卖硬件但它提供客户网点（SME）的接入设备组件列表——价值=渠道伙伴部署时使用的 OEM 白标设备供给链
- 【假设】开口角度=「你渠道伙伴部署市级 SME 接入时的 OEM 白标 PoE 随单」——STC-424 以 OEM 白标供货 SEWAN 牌，假装 SEWAN 形象部署

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

【推断】SEWAN 实为运营型：接入是 dead simple 的构线（间接销售模型），它不卖硬件但它提供客户网点（SME）的接入设备组件列表——价值=渠道伙伴部署时使用的 OEM 白标设备供给链

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、OEM/白牌
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - OEM/白牌：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- SEWAN(法国电信 ETI 大户;2007 年 Alexis de Goriaïnoff + 3 名联合创始人联合创立——从同一运营商 4 人「全员辞职」创办起家;谱型=Cloud+Télécoms 生态/自创 SaaS「Sophia」;300-1000 员工/75M€ 收；总部巴黎+贝尔福/蒙彼利埃；西班牙/德/意/荷国际化);**Alexis de Goriaïnoff = PDG & 联合创始人**;Philippe Moutinho 同站 PDG 口径(疑子站/分公司)

## 联系方式（已有/猜测分标）

- **邮箱**：contact@sewan.fr
  - 状态：既有/公开
- **电话**：+33 1 76 21 00 00
- **原始联系字段**：+33 1 76 21 00 00 / contact@sewan.fr
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Alexis de Goriaïnoff**(PDG et Cofondateur(集团 CEO/联合创始人))— 经 sewan.fr 联系页 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://business.lesechos.fr/entrepreneurs/success-stories/sewan-pixopolitan-et-opendatasoft-sur-l-entreprise-bfm-les-chos-316692.php〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Alexis de Goriaïnoff | PDG et Cofondateur(集团 CEO/联合创始人) | 经 sewan.fr 联系页 | sewan.fr + business.lesechos.fr 双源 | https://business.lesechos.fr/entrepreneurs/success-stories/sewan-pixopolitan-et-opendatasoft-sur-l-entreprise-bfm-les-chos-316692.php |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 守档 D+3 · SEWAN 牌 OEM 白标套件页

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「你渠道伙伴部署市级 SME 接入时的 OEM 白标 PoE 随单」——STC-424 以 OEM 白标供货 SEWAN 牌，假装 SEWAN 形象部署
- **要问的问题**：你们渠道伙伴在 SME 部署里 PoE 接入现供哪家？白标 OEM 新鲜件可谈？
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 2 次跟进 · 守档 D+14 · contact@sewan.com 具名开口

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「你渠道伙伴部署市级 SME 接入时的 OEM 白标 PoE 随单」——STC-424 以 OEM 白标供货 SEWAN 牌，假装 SEWAN 形象部署
- **要问的问题**：你们渠道伙伴在 SME 部署里 PoE 接入现供哪家？白标 OEM 新鲜件可谈？
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 3 次跟进 · 守档 D+30 · 果归守档

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「你渠道伙伴部署市级 SME 接入时的 OEM 白标 PoE 随单」——STC-424 以 OEM 白标供货 SEWAN 牌，假装 SEWAN 形象部署
- **要问的问题**：你们渠道伙伴在 SME 部署里 PoE 接入现供哪家？白标 OEM 新鲜件可谈？
- **随附/动作**：随附 1 页特性对照/测试包说明


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-07(R65 第 11 批精修 = R57 转写 + 本轮登记/媒体新挖)**；原始记录：`batch/B类深挖_2026-10-07_R65_第11批.json`；价格均为 EXW 快照。

- **背景深描**：SEWAN(法国电信 ETI 大户;2007 年 Alexis de Goriaïnoff + 3 名联合创始人联合创立——从同一运营商 4 人「全员辞职」创办起家;谱型=Cloud+Télécoms 生态/自创 SaaS「Sophia」;300-1000 员工/75M€ 收；总部巴黎+贝尔福/蒙彼利埃；西班牙/德/意/荷国际化);**Alexis de Goriaïnoff = PDG & 联合创始人**;Philippe Moutinho 同站 PDG 口径(疑子站/分公司)
- **芯片与在用型号**：【推断】SEWAN 实为运营型：接入是 dead simple 的构线（间接销售模型），它不卖硬件但它提供客户网点（SME）的接入设备组件列表——价值=渠道伙伴部署时使用的 OEM 白标设备供给链
- **关键人KP**：Alexis de Goriaïnoff = PDG & Cofondateur(官网 + LesEchos/BFM 双源);Philippe Moutinho 同城站 PDG 位
- **关注点与资质**：MikroTik（Master） 
- **优缺点SWOT**：S:€75M 投资+450 人+55k 客户+4国 / W:不直购硬件 / O:OEM 白标(SEWAN 牌）渠道伙伴部署随单位 / T:运营型血易拐谱对我不熟
- **Saga产品适配**：欧 B2B 运营型:OEM 白标(SEWAN 牌）供给其渠道伙伴部署 SME 接入用

### R55 证据摘录（全部保留 · 含数量）

- **【R57备护深挖证据】**75 millions d'euros auprès de Kartesia en novembre 2019…450 collaborateurs…55 000 entreprises clientes dans 4 pays européens
  > 75 millions d'euros auprès de Kartesia en novembre 2019…450 collaborateurs…55 000 entreprises clientes dans 4 pays européens
  > 来源：https://www.frenchweb.fr/telecoms-75-millions-deuros-pour-loperateur-b2b-sewan/384659
- **【R57备护深挖证据】**cap sur l'Allemagne…rachat de l'opérateur allemand 42one…vente indirecte
  > cap sur l'Allemagne…rachat de l'opérateur allemand 42one…vente indirecte
  > 来源：https://www.frenchweb.fr/telecoms-sewan-continue-de-tisser-sa-toile-en-europe-avec-le-rachat-de-loperateur-allemand-42one/400067
- **【R65 体量+位】**Sewan 2007 创 · 4 创始人同人离职创办 · 300-1000 员工 · 75M€ 收 · Sophia 生态 · 西班牙已并入 · 德/意/荷在望
  > Alexis de Goriaïnoff a créé Sewan en 2007 … 75 millions d’euros de chiffre d’affaires et emploie 300 personnes … Sophia … Nourrissant des ambitions européennes
  > 来源：https://business.lesechos.fr/entrepreneurs/success-stories/sewan-pixopolitan-et-opendatasoft-sur-l-entreprise-bfm-les-chos-316692.php

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 欧 B2B 运营型:OEM 白标(SEWAN 牌）供给其渠道伙伴部署 SME 接入用 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S:€75M 投资+450 人+55k 客户+4国 / W:不直购硬件 / O:OEM 白标(SEWAN 牌）渠道伙伴部署随单位 / T:运营型血易拐谱对我不熟

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
  - [ ] SEWAN 渠道伙伴部署级 SME 接入设备（含 PoE 交换）现供目录
  - [ ] 白标 OEM 供应链现有没有

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE value slot for your line

```text
Hi SEWAN team,

450 people, a €75M war chest from Kartesia, 55k B2B customers and a four-country footprint (France / Spain / Belgium / Germany) - Sewan is the heavyweight operator of the European indirect-sale channel.

We build a 24-port PoE+ managed switch (280W, L2-lite) with full English/French documentation, fully open to Sewan white-label. Reference: $180 USD EXW (2026-09-29) - designed to become the default PoE access SKU your channel partners deploy under the Sewan brand.

One question: for your channel partners' SME deployments, which PoE access source supplies the installations today - and would a documented white-label unit earn a pilot in your catalog?

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
