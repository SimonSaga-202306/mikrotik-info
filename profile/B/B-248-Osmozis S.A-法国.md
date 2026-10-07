# Osmozis S.A.

> **评级 B**　|　法国　|　档案编号 `B-248`　|　优先级 ★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-248
rating: B
country: 法国
biz_org: 分销/批发商（有官网）
business_model: 分销 stocking
decision_speed: moderate
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: false, oem: true, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-10-07
```

## SALES BRIEF（压缩模型）

- **是谁**：Osmozis S.A.(Montpellier;2005 年 Gérard Tremblay + Yves Boulot 联合创;谱型=露营地/度假村 WiFi & IoT 数字化欧洲头号专家——2600+ sites…
- **商业模式**：分销 stocking
- **为什么值得跟**：通用分销商信号，无差异化切入点，慢慢跟
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — 露营 WiFi 自用网络的 PoE 组网接线(bornes backhaul 位+中心接入双样）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：你们的 bornes 组网(backhaul + camp LAN)里,PoE 接层现供哪个 OEM？OEM 贴牌？
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Osmozis S.A.（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 | 事实 |
| 网站 | osmozis.com | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Master） | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | Osmozis S.A.(Montpellier;2005 年 Gérard Tremblay + Yves Boulot 联合创;谱型=露营地/度假村 WiFi & IoT 数字化欧洲头号专家——2600+ sites/108 员工/2023 €12.8M;2017 Euronext 上市(FR0013231180),2024-05 被 Passman 集 | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 【推断】「自研 outdoor bornes+软件全家」血脉有力:上游自产 AP/IoT 不与我们 PoE 交换正对面;整个 bornes 组网刚需 PoE 接入交换(我们补后特正位) | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Osmozis S.A.(法国中南部 Clapiers/Montpellier 34830 7 avenue de l'Europe):**法国第一的露营地 WiFi/IoT 运营商+自研**——自制 bornes WiFi hotspots(户外 bornes)+软件全家(OsmoGestion/OsmoVentes/OsmoPay/OsmoKey/OsmoPower/OsmoWater);CA €1M+;曾启动 Alternext 上市计划;FB 页主「opérateur majeur de réseaux Wifi et de l'Internet des Objets」 | R65 深挖:露营 WiFi 全欧大户;Passman 收购在架
- 【推断】「自研 outdoor bornes+软件全家」血脉有力:上游自产 AP/IoT 不与我们 PoE 交换正对面;整个 bornes 组网刚需 PoE 接入交换(我们补后特正位)
- 【假设】开口角度=「露营地 bornes 组网的回程部署 PoE 位随单/OEM 后特」:STC-424 在 bornes backhaul 里（中心 narc 室）+STI-288GP DIN 轨（每个 bornes 节子服务）。P1 双联呈

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

【推断】「自研 outdoor bornes+软件全家」血脉有力:上游自产 AP/IoT 不与我们 PoE 交换正对面;整个 bornes 组网刚需 PoE 接入交换(我们补后特正位)

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、OEM/白牌
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - OEM/白牌：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- Osmozis S.A.(Montpellier;2005 年 Gérard Tremblay + Yves Boulot 联合创;谱型=露营地/度假村 WiFi & IoT 数字化欧洲头号专家——2600+ sites/108 员工/2023 €12.8M;2017 Euronext 上市(FR0013231180),2024-05 被 Passman 集团收购 €15/股 OPA;**KP:Gérard Tremblay+Yves Boulot 联合创始人;Pierre-Benoit Labbé 总经理(现任)**

## 联系方式（已有/猜测分标）

- **邮箱**：support@osmozis.com
  - 状态：既有/公开
- **电话**：+33 4 11 93 27 51
- **原始联系字段**：+33 4 11 93 27 51 / support@osmozis.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Gérard Tremblay**(Co-fondateur)— 经 osmozis.com 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://gazette-du-midi.fr/au-sommaire/entreprises/osmozis-specialiste-de-la-digitalisation-des-campings-accelere-son〕
  - **Yves Boulot**(Co-fondateur)— 同上 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:同上〕
  - **Pierre-Benoit Labbé**(Directeur Général(总经理))— 同上 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:同上〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Gérard Tremblay | Co-fondateur | 经 osmozis.com | gazette-du-midi 图照双源 | https://gazette-du-midi.fr/au-sommaire/entreprises/osmozis-specialiste-de-la-digitalisation-des-campings-accelere-son |
| Yves Boulot | Co-fondateur | 同上 | 同源 | 同上 |
| Pierre-Benoit Labbé | Directeur Général(总经理) | 同上 | 同源 | 同上 |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 守档 D+3 · bornes PoE 接线部署页(核心+节子双联）

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「露营地 bornes 组网的回程部署 PoE 位随单/OEM 后特」:STC-424 在 bornes backhaul 里（中心 narc 室）+STI-288GP DIN 轨（每个 bornes 节子服务）。P1 双联呈
- **要问的问题**：你们的 bornes 组网(backhaul + camp LAN)里,PoE 接层现供哪个 OEM？OEM 贴牌？
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 2 次跟进 · 守档 D+14 · 样机 OEM 贴牌提案

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「露营地 bornes 组网的回程部署 PoE 位随单/OEM 后特」:STC-424 在 bornes backhaul 里（中心 narc 室）+STI-288GP DIN 轨（每个 bornes 节子服务）。P1 双联呈
- **要问的问题**：你们的 bornes 组网(backhaul + camp LAN)里,PoE 接层现供哪个 OEM？OEM 贴牌？
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 3 次跟进 · 守档 D+30 · 果归守档

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「露营地 bornes 组网的回程部署 PoE 位随单/OEM 后特」:STC-424 在 bornes backhaul 里（中心 narc 室）+STI-288GP DIN 轨（每个 bornes 节子服务）。P1 双联呈
- **要问的问题**：你们的 bornes 组网(backhaul + camp LAN)里,PoE 接层现供哪个 OEM？OEM 贴牌？
- **随附/动作**：随附 1 页特性对照/测试包说明


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-07(R65 第 11 批精修 = R57 转写 + 本轮登记/媒体新挖)**；原始记录：`batch/B类深挖_2026-10-07_R65_第11批.json`；价格均为 EXW 快照。

- **背景深描**：Osmozis S.A.(Montpellier;2005 年 Gérard Tremblay + Yves Boulot 联合创;谱型=露营地/度假村 WiFi & IoT 数字化欧洲头号专家——2600+ sites/108 员工/2023 €12.8M;2017 Euronext 上市(FR0013231180),2024-05 被 Passman 集团收购 €15/股 OPA;**KP:Gérard Tremblay+Yves Boulot 联合创始人;Pierre-Benoit Labbé 总经理(现任)**
- **芯片与在用型号**：【推断】「自研 outdoor bornes+软件全家」血脉有力:上游自产 AP/IoT 不与我们 PoE 交换正对面;整个 bornes 组网刚需 PoE 接入交换(我们补后特正位)
- **关键人KP**：Gérard Tremblay + Yves Boulot = 联合创始人;Pierre-Benoit Labbé = Directeur Général(现任, Passman 收购在架仍原位)
- **关注点与资质**：MikroTik（Master） 
- **优缺点SWOT**：S:法国第一露营 WiFi 运营+自牌血统 / W:主路径 WiFi harvest 不是 PoE / O:bornes 组网 backhaul/备触 PoE 刚需随单 / T:其自研 AP 和我 outdoor 在我司面同向
- **Saga产品适配**：露营 WiFi 自用网络的 PoE 组网接线(bornes backhaul 位+中心接入双样）

### R55 证据摘录（全部保留 · 含数量）

- **【R57备护深挖证据】**OSMOZIS S.A. est opérateur majeur de réseaux Wifi et de l'Internet des Objets (IoT) dédiés aux campings
  > OSMOZIS S.A. est opérateur majeur de réseaux Wifi et de l'Internet des Objets (IoT) dédiés aux campings
  > 来源：https://www.facebook.com/osmozis.wifi/
- **【R57备护深挖证据】**Osmozis fabrique et installe des bornes WiFi hotspots adaptées aux terrains de campings…OsmoGestion/OsmoVentes/Wi-Fi Camping/OsmoKey/OsmoPay
  > Osmozis fabrique et installe des bornes WiFi hotspots adaptées aux terrains de campings…OsmoGestion/OsmoVentes/Wi-Fi Camping/OsmoKey/OsmoPay/OsmoPower
  > 来源：https://www.gestion-camping.com/fournisseurs-camping/646/osmozis.html
- **【R65 谱位+收购】**Osmozis 露营度假 WiFi 欧洲一号 2600+ 站 · 108人/12.8M€(2023) · 2017 Euronext 上市 FR0013231180 · 2024-05 Passman 15€/股 收购
  > Osmozis, spécialiste de la transition digitale des campings … équipe plus de 2 600 sites en Europe … 108 personnes … 12,8 M€ … annonce rejoindre le groupe Passman … Gérard Tremblay et Yves Boulot, cofondateurs d’Osmozis
  > 来源：https://gazette-du-midi.fr/au-sommaire/entreprises/osmozis-specialiste-de-la-digitalisation-des-campings-accelere-son

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 露营 WiFi 自用网络的 PoE 组网接线(bornes backhaul 位+中心接入双样） |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S:法国第一露营 WiFi 运营+自牌血统 / W:主路径 WiFi harvest 不是 PoE / O:bornes 组网 backhaul/备触 PoE 刚需随单 / T:其自研 AP 和我 outdoor 在我司面同向

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
  - [ ] 自产 bornes 组网中 PoE 接层/回程现供(每个 bornes/共 camp LAN 中心）
  - [ ] Alternext 上市计划构成谱压力(公众化后采购单层面）

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE value slot for your line

```text
Hi Osmozis team,

France's leading WiFi-and-IoT operator for campgrounds with your own bornes, your own software stack (OsmoGestion / OsmoPay / OsmoPower…), and a network story so good it once had you looking at Alternext - bornes everywhere, and every single one of them is a PoE load.

We build PoE switches for exactly that job: a 24-port PoE+ managed switch (280W, L2-lite, $180 USD EXW ref. 2026-09-29) for the camp LAN core, and an 8-port Gigabit industrial PoE switch (DIN-rail, fanless, -40..75C class, $74.8 EXW) for the individual borne cabinets. Full English/French documentation, fully open to Osmozis own branding.

One question: across your bornes and camp LAN installations, which PoE source are your borne boxes and the camp core running on today - and would a documented OEM unit earn a bench test?

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
