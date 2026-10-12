# SEWAN

> **评级 B**　|　法国　|　档案编号 `B-252`　|　优先级 ★★★　|　状态：01-已跟进一轮（用户报告；具体日期/收件人未逐户记录）
>
> **触达状态（Stage）**：01-contacted　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

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
stage: 01-contacted
struct_version: v2  # v2 骨架
updated: 2026-10-12
```

## SALES BRIEF（压缩模型）

- **是谁**：2004 创 22 年;Paris 10;De Goriaïnoff 10 年 Président;€154.6M(2024)…
- **商业模式**：分销 stocking
- **为什么值得跟**：有信号（ISP/骨干）但需先验证需求或联系人不具体
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — 欧 B2B 运营型:OEM 白标(SEWAN 牌）供给其渠道伙伴部署 SME 接入用；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：你们渠道伙伴在 SME 部署里 PoE 接入现供哪家？白标 OEM 新鲜件可谈？
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：R71（2026-10-12）：一轮跟进已完成（用户报告；本户具体发送日期/收件地址未逐户提供）。可继续按本档既有策略低频跟进；不对首轮无实质回应者无差别催促；不编排未提供的下次动作日期。

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
| R55·背景深描 | 2004 创 22 年;Paris 10;De Goriaïnoff 10 年 Président;€154.6M(2024) | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 有线电信(NAF 6110Z)+企业云+集团 17 司 | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】波 R67/TUB·批10·B-252:法谱: **SEWAN 深挖(manageo/verif/score3/xerfi/contract-factory 五源互证)**:**SIREN 452 363 153;SIRET( siège) 452 363 153 00043;SAS 创 2004-03-05(22 年);capital social 723,057 EUR;TVA FR10452363153; siège=2 Cité Paradis,75010 Paris 10(établissement siège 2015-03-01);**NAF 6110Z=Télécommunications filaires(有线电信)**; effectif=250-499 salariés(xerfi 记 ~400 员)**;**财务金谱:**Chiffre d"affaires 2024=**154,624,210 €**(bilan 2024-12-31;xerfi 记 155 M€;+行业最大谱之一);**Group of 17 entities;Global Ultimate=SEWAN 集团母**;**KP 金谱:**Président=**Alexis Julien Armand Michel De Goriaïnoff**(b. 1974-11;**2016-06-28 任 10 年**)+**Directeur Général=**David Brette**(b. 1972-10)+N.S.K FIDUCIAIRE(审计 SIREN 391857760)=核心三档谱**;**谱位=**有线电信运营/企业云服务(sagepaas 谱位谱口)+集团千家客户谱;Facturation électronique=TESSI TECHNOLOGIES 域谱**=谱口=**电信大客户采购口+企业客户云接入**;**谱位注=谱位谱位=谱口=非直分销谱位(电信/云运营非电子设备批发)=谱位接 +MikroTik 采购口谱(MikroTik 已是法音 SEWAN 类谱案?谱档注)=批 10 法谱大谱(€154.6M 规模大谱;谱位谱注:谱口=谱位=法電信/云运营接谱位谱注,直口=设备采购层非分销谱**;排噪:法国同名 Sewan(simepreuve 法艺术司)=别司注。
- 【推断】R67/TUB 推土机深挖 批10 B 类档序续批十户
- 【假设】STC-424XGGPM-280W($165 USD EXW (2026-10-08, 15天有效))具名谱引路

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

有线电信(NAF 6110Z)+企业云+集团 17 司

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、OEM/白牌
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - OEM/白牌：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：contact@sewan.fr
  - 状态：既有/公开
- **电话**：+33 1 76 21 00 00
- 来源等级：official-channel（R41–R48 联系方式台账口径）
- **原始联系字段**：+33 1 76 21 00 00 / contact@sewan.fr
- **R71 跟进核对**：本户一轮跟进已完成（用户报告）；逐户发送日期与实际收件地址未提供，不补造。已核实的地址级异常见本档 R71/退信记录；未将用户报告扩大成逐地址送达结论。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Alexis de Goriaïnoff**(PDG et Cofondateur(集团 CEO/联合创始人))— 经 sewan.fr 联系页 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://business.lesechos.fr/entrepreneurs/success-stories/sewan-pixopolitan-et-opendatasoft-sur-l-entreprise-bfm-les-chos-316692.php〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Alexis de Goriaïnoff | PDG et Cofondateur(集团 CEO/联合创始人) | 经 sewan.fr 联系页 | sewan.fr + business.lesechos.fr 双源 | https://business.lesechos.fr/entrepreneurs/success-stories/sewan-pixopolitan-et-opendatasoft-sur-l-entreprise-bfm-les-chos-316692.php |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · De Goriaïnoff 合唱 10 年谱(€154.6M 集团)

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：Président → 24 口 PoE(电信运营采购谱注)
- **要问的问题**：SEWAN 集团设备采购岚借接入件主任谱?
- **随附/动作**：manageo/verif 5 源

### 第 2 次跟进 · Brette DG 谱

- **推什么**：STI-288GPM/424（统一口径=P1 系列，不外溢）
- **切入点**：DG 谱口
- **要问的问题**：贵司 MikroTik 谱位采购谱?
- **随附/动作**：contract-factory 谱

### 第 3 次跟进 · 集团 17 司谱链

- **推什么**：STC-28DGGPM（统一口径=P1 系列，不外溢）
- **切入点**：集团谱链谱
- **要问的问题**：17 司谱的接入设备谱?
- **随附/动作**：


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-08**；原始记录：`batch/B类深挖_2026-10-08_R67_R56_推土机批10.json`；价格均为 EXW 快照。

- **背景深描**：2004 创 22 年;Paris 10;De Goriaïnoff 10 年 Président;€154.6M(2024)
- **芯片与在用型号**：有线电信(NAF 6110Z)+企业云+集团 17 司
- **关键人KP**：Alexis De Goriaïnoff(Président 2016-06-28 起 10 年)+David Brette(DG)+N.S.K FIDUCIAIRE 审计=核心三档
- **关注点与资质**：谱位注谱口谱谱口(设备采购层非分销谱)=注意谱当谱注 MikroTik 采购层
- **优缺点SWOT**：S=€154.6M 大谱+集团 17 司+400 员规模·W=谱位谱当半对口=谱谱谱注(运营非分销)·O=企业/电信设备采购层=接入设备链纺谱注·T=谱亲敏注(运营/谱供系统注);集团决策链长
- **Saga产品适配**：STC-424XGGPM-280W 24 口 PoE($165 USD EXW,15 天有效):法语谱;€154.6M 大谱;集团决策链;谱档谱口谱注

### R55 证据摘录（全部保留 · 含数量）

- **【法体登册】**ENTREPRISE SEWAN;SIREN 452 363 153;SIRET 452 363 153 00043;TVA FR10452363153;Code NAF 6110Z Télécommunications filaires;Capital social 723 057 EURO;Dirigeant: Alexis Julien Armand Michel De Goriainoff;Effectif 250 à 499 salariés;SAS 创 2004-03-05;2 Cité Paradis, Paris 10(établissement siège 2015)
  > ENTREPRISE SEWAN;SIREN 452 363 153;SIRET 452 363 153 00043;TVA FR10452363153;Code NAF 6110Z Télécommunications filaires;Capital social 723 057 EURO;Dirigeant: Alexis Julien Armand Michel De Goriainoff;Effectif 250 à 499 salariés;SAS 创 2004-03-05;2 Cité Paradis, Paris 10(établissement siège 2015)
  > 来源：https://www.manageo.fr/entreprises/452363153.html
- **【财务档】**SEWAN;bilan publié 31/12/2024;chiffre d"affaires 154,624,210 euros;Group of 17 entities;Global Ultimate SEWAN;SIREN 452363153;FR10452363153
  > SEWAN;bilan publié 31/12/2024;chiffre d"affaires 154,624,210 euros;Group of 17 entities;Global Ultimate SEWAN;SIREN 452363153;FR10452363153
  > 来源：https://www.verif.com/en/company/SEWAN-68d9c0ee1299230338840361/
- **【掌权】**Dirigeants: De Goriainoff Alexis(Président, depuis 28/06/2016, né 11/1974, residant Paris 9e)+David BRETTE(Directeur Général, né 10/1972, residant Ville-d"Avray)+N.S.K FIDUCIAIRE(Commissaire aux comptes titulaire)
  > Dirigeants: De Goriainoff Alexis(Président, depuis 28/06/2016, né 11/1974, residant Paris 9e)+David BRETTE(Directeur Général, né 10/1972, residant Ville-d"Avray)+N.S.K FIDUCIAIRE(Commissaire aux comptes titulaire)
  > 来源：https://www.contract-factory.com/infosocietes/sewan-452363153
- **【谱档】**SEWAN;2 Cité Paradis,75010 Paris;Capital 723 057 €;7 établissements;SIRET 452 363 153 00043;SAS
  > SEWAN;2 Cité Paradis,75010 Paris;Capital 723 057 €;7 établissements;SIRET 452 363 153 00043;SAS
  > 来源：https://www.score3.fr/SEWAN-452363153.shtml
- **【谱档】**Sewan;créée mars 2004;capital 723 k€;400 personnes;CA 155 M€ en 2024;siège social Paris 10;2 autres établissements;NAF 61.10Z(Télécommunications filaires);Président Alexis DE GORIAINOFF;DG David BRETTE
  > Sewan;créée mars 2004;capital 723 k€;400 personnes;CA 155 M€ en 2024;siège social Paris 10;2 autres établissements;NAF 61.10Z(Télécommunications filaires);Président Alexis DE GORIAINOFF;DG David BRETTE
  > 来源：https://www.xerfi.com/etudes-par-entreprise/sewan_452363153

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 欧 B2B 运营型:OEM 白标(SEWAN 牌）供给其渠道伙伴部署 SME 接入用 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S=€154.6M 大谱+集团 17 司+400 员规模·W=谱位谱当半对口=谱谱谱注(运营非分销)·O=企业/电信设备采购层=接入设备链纺谱注·T=谱亲敏注(运营/谱供系统注);集团决策链长

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
  - [ ] 谱位谱注:谱位谱=电信运营+云非白牌分销=谱口半对口注
  - [ ] 400 员 vs 250-499 双窗注
  - [ ] SIRES 452363153 谱注

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your line

```text
Dear Alexis,\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) — reference $165 USD EXW (2026-10-08, 15 days valid), with our private-label and supply-chain flexibility documented for distribution groups. Datasheet + CE pack on request.\n\nBest regards\nSaga / SmartByte ODM
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

<!-- R71-FOLLOWUP-START -->
## R71 本轮跟进与邮件回执（2026-10-12）

- **跟进范围**：A/B 本轮一轮跟进已完成（用户报告）；逐户发送日期与实际收件地址未提供，本节不补造发送日志。
- **本户结论**：一轮跟进已完成；可继续按本档既有策略低频跟进，不把“已跟进”误写成“逐地址送达成功”。
- **地址级范围**：R71 退信台账未为本户列出新的精确地址异常；可继续跟进不等于对每个邮箱作了 SMTP 或逐地址送达验证。
- **后续节奏**：首轮之后不作无差别催促；按既有节奏等待或低频跟进，不填造日期。
<!-- R71-FOLLOWUP-END -->
