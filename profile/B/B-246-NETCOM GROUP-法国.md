# NETCOM GROUP

> **评级 B**　|　法国　|　档案编号 `B-246`　|　优先级 ★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-246
rating: B
country: 法国
biz_org: 分销/批发商（有官网）
business_model: 分销 stocking
decision_speed: moderate
price_sensitivity: high
volume_potential: 5  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-10-07
```

## SALES BRIEF（压缩模型）

- **是谁**：2004 创 22 年;Pantin;NETCOM GROUP=MVNO;12 分支;€27M(2017)…
- **商业模式**：分销 stocking
- **为什么值得跟**：通用分销商信号，无差异化切入点，慢慢跟
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — FRANCE NUMERIQUE 集团自牌之外的 value PoE 第 4 线入端；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Phenix Partner/linknet 之外,你们 PoE 接层现供哪家？客资加入第 4 线可谈？
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | NETCOM GROUP（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 | 事实 |
| 网站 | netcom-group.fr | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Reseller） | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | 2004 创 22 年;Pantin;NETCOM GROUP=MVNO;12 分支;€27M(2017) | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | MVNO+phone systems install+wholesale+VoIP/Internet | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】波 R67/TUB·批12·B-246:法谱: **NEXERA SAS / NETCOM GROUP 深挖(rubypayeur/manageo/societe/wikipedia 四源互证)**:**法人正谱=**NEXERA**(SIREN **453 006 314**;INSEE 2004-04-30=22 年;RCS Bobigny 2005-04-13);**nom commercial=**NETCOM GROUP**(3 marques déposées)**;SIRET siège 453 006 314 00109;SAS;capital social **€106,300**(2018-05 增自 €105,000);**41 Rue Delizy,93500 Pantin**(siège 2017-05-31);NAF 46.52Z;20-49 员；TVA FR66453006314;**谱口铺=**Courtier en télécommunication+commerce de gros de communication et/ou de minutes téléphoniques+commerce de gros d'équipements téléphoniques**;**wikipedia 谱档=**Netcom Group=**opérateur de télécommunications+MVNO**;créée le 30 avril 2004 par **Jamal Assraoui+Saïd Benamrouche+Mohamed Benamrouche**(创者 3 人谱);produit=**opérateur de télécommunications, téléphonie fixe, mobile, Internet, VoIP, installation de standards téléphoniques pour les TPE, PME et grandes entreprises**;**2015 SFR MVNO;2016 Bouygues Telecom 批发约;2018 Orange MVNO;2018=12 agences 全法;2018 SG Capital Partenaires 入股少数;**CA 2017=**€27,000,000****;netcom-group.fr**;**KP 谱:**Président=**NEXERA CONNECT**(法人口,SIREN 945230381)+**LMBH & ASSOCIES**(审计 SIREN 492915780)+manageo 谱=**Président PERSONNE MORALE=FRANCE NUMERIQUE**(谱口谱注)**+创者 3 人谱**;**谱位=法国 22 年 MVNO 电信运营铺+12 分支谱+€27M+3 创者谱=批 12 法谱金矿(谱口谱注)**;排噪=**NETCOM GROUP(SIREN 507726115 Paris,2012 已注销 liquidateur Abdallah Ayachi)**=完全别司勿混。
- 【推断】R67/TUB 推土机深挖 批12 B 类档序续批三十户
- 【假设】STC-424XGGPM-280W($165 USD EXW (2026-10-08, 15天有效))具名谱引路

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

MVNO+phone systems install+wholesale+VoIP/Internet

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：h.matri@netcom-group.fr
  - 状态：既有/公开
- **电话**：+33 826 10 56 05
- **原始联系字段**：+33 826 10 56 05 / h.matri@netcom-group.fr
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Jamal Assraoui**(Président(Pantin NETCOM GROUP, 候选）)— 经 58 Rue Denis Papin 93500 Pantin 总线 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://edecideur.info/edecideur.php?q=198020130215benmoh-benamrouche-mohamed-directeur-general-4652z-45300631400042-netcom-group-58-rue-denis-papin-93500-pantin〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Jamal Assraoui | Président(Pantin NETCOM GROUP, 候选） | 经 58 Rue Denis Papin 93500 Pantin 总线 | edecideur 候选，未最终证 | https://edecideur.info/edecideur.php?q=198020130215benmoh-benamrouche-mohamed-directeur-general-4652z-45300631400042-netcom-group-58-rue-denis-papin-93500-pantin |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · NETCOM MVNO 谱口+12 分支谱网

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：MVNO 铺 → 24 口 PoE(电信谱铺)
- **要问的问题**：NETCOM 12 分支谱网络的 PoE 谱件由哪位谱?
- **随附/动作**：wikipedia/manageo 4 源

### 第 2 次跟进 · FRANCE NUMERIQUE 谱口

- **推什么**：STI-288GPM/424（统一口径=P1 系列，不外溢）
- **切入点**：法人口谱口
- **要问的问题**：您法人口谱口铺谱?
- **随附/动作**：manageo 谱

### 第 3 次跟进 · 创者 3 人谱口

- **推什么**：STC-28DGGPM（统一口径=P1 系列，不外溢）
- **切入点**：创者谱口
- **要问的问题**：创者谱谱谱铺 PoE?
- **随附/动作**：


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-08**；原始记录：`batch/B类深挖_2026-10-08_R67_R56_推土机批12.json`；价格均为 EXW 快照。

- **背景深描**：2004 创 22 年;Pantin;NETCOM GROUP=MVNO;12 分支;€27M(2017)
- **芯片与在用型号**：MVNO+phone systems install+wholesale+VoIP/Internet
- **关键人KP**：Assraoui+Benamrouche×2 创者谱+NEXERA CONNECT+FRANCE NUMERIQUE
- **关注点与资质**：MVNO/电信铺 → 24 口 PoE(铺谱)
- **优缺点SWOT**：S=22 年 MVNO+12 分支+€27M+3 创者谱·W=MVNO 电信运营谱铺注(谱铺谱堂注)·O=电信铺谱口铺注=PoE 铺谱口谱注·T=谱堂谱铺注+SG 入股少数注
- **Saga产品适配**：STC-424XGGPM-280W 24 口 PoE($165 USD EXW,15 天有效):法语谱;3 创者谱;12 分支谱;netcom-group.fr

### R55 证据摘录（全部保留 · 含数量）

- **【谱档】**NEXERA(NETCOM GROUP);SIREN 453006314;RCS Bobigny;41 RUE DELIZY 93500 PANTIN;Capital social 106 300,00 €;Courtier en télécommunication;Commerce de gros de communication et/ou de minutes téléphoniques;Commerce de gros d'équipements téléphoniques;NAF 46.52Z;Président NEXERA CONNECT(SIREN 945230381);Commissaire aux comptes LMBH & ASSOCIES(SIREN 492915780)
  > NEXERA(NETCOM GROUP);SIREN 453006314;RCS Bobigny;41 RUE DELIZY 93500 PANTIN;Capital social 106 300,00 €;Courtier en télécommunication;Commerce de gros de communication et/ou de minutes téléphoniques;Commerce de gros d'équipements téléphoniques;NAF 46.52Z;Président NEXERA CONNECT(SIREN 945230381);Commissaire aux comptes LMBH & ASSOCIES(SIREN 492915780)
  > 来源：https://rubypayeur.com/societe/netcom-group-453006314
- **【谱档】**NETCOM GROUP vend en gros des composants et équipements électroniques et de télécommunication;capital actuel 106,300 €(2018-05 增自 105,000);création avril 2004;Président est une PERSONNE MORALE(FRANCE NUMERIQUE);20 à 49 salariés;3 marques déposées NETCOM GROUP
  > NETCOM GROUP vend en gros des composants et équipements électroniques et de télécommunication;capital actuel 106,300 €(2018-05 增自 105,000);création avril 2004;Président est une PERSONNE MORALE(FRANCE NUMERIQUE);20 à 49 salariés;3 marques déposées NETCOM GROUP
  > 来源：https://www.manageo.fr/entreprises/453006314.html
- **【谱档】**Netcom Group;Création: 30 avril 2004;SAS;Siège social: Pantin;Direction: France Numérique;Actionnaires: France Numérique;Produits: Opérateur de télécommunications, Téléphonie fixe, mobile, Internet, VoIP, installation de standards téléphoniques;SIREN: 453006314;Site: https://www.netcom-group.fr;MVNO de SFR en 2015;grossiste en minutes avec Bouygues Telecom en 2016;MVNO d'Orange en 2018;doté de douze agences;CA 2017 = 27 millions d'euros
  > Netcom Group;Création: 30 avril 2004;SAS;Siège social: Pantin;Direction: France Numérique;Actionnaires: France Numérique;Produits: Opérateur de télécommunications, Téléphonie fixe, mobile, Internet, VoIP, installation de standards téléphoniques;SIREN: 453006314;Site: https://www.netcom-group.fr;MVNO de SFR en 2015;grossiste en minutes avec Bouygues Telecom en 2016;MVNO d'Orange en 2018;doté de douze agences;CA 2017 = 27 millions d'euros
  > 来源：https://fr.wikipedia.org/wiki/Netcom_Group
- **【谱档】**Netcom Group;créée en 2004 par Jamal Assraoui, Saïd Benamrouche et Mohamed Benamrouche;spécialisée dans l'installation de standards téléphoniques;2018 Société Générale Capital Partenaires part minoritaire
  > Netcom Group;créée en 2004 par Jamal Assraoui, Saïd Benamrouche et Mohamed Benamrouche;spécialisée dans l'installation de standards téléphoniques;2018 Société Générale Capital Partenaires part minoritaire
  > 来源：https://fr.wikipedia.org/wiki/Netcom_Group

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | FRANCE NUMERIQUE 集团自牌之外的 value PoE 第 4 线入端 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S=22 年 MVNO+12 分支+€27M+3 创者谱·W=MVNO 电信运营谱铺注(谱铺谱堂注)·O=电信铺谱口铺注=PoE 铺谱口谱注·T=谱堂谱铺注+SG 入股少数注

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
  - [ ] NETCOM GROUP(SIREN 507726115 Paris)2012 已注销=完全别司勿混!
  - [ ] Président 法人口(NEXERA CONNECT/FRANCE NUMERIQUE 双窗谱注)
  - [ ] netcom-group.fr 谱口注

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your line

```text
Dear Jamal,\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) — built for telecom group branches and standard-telephony deployments. Reference $165 USD EXW (2026-10-08, 15 days valid). Datasheet + CE pack on request.\n\nBest regards\nSaga / SmartByte ODM
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
