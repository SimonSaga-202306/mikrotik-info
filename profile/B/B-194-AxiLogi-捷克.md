# AxiLogi

> **评级 B**　|　捷克　|　档案编号 `B-194`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-194
rating: B
country: 捷克
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

- **是谁**：AxiLogi s.r.o.(IČO 10964703, Daimlerova 1161/6, 301 00 Plzeň-Skvrňany, Czech Republic;2021-06-23 创；**法人体制谱：Kol…
- **商业模式**：分销 stocking
- **为什么值得跟**：通用分销商信号，无差异化切入点，慢慢跟
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — 光伏+弱电双驱分销的安装商随单 24 口 280W 管理型 PoE 位(配电柜类目 STI 二线注记)；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：你们光伏/弱电安装商客户在 24 口管理型 PoE 现随哪款?Cudy/Alta 之上有空档吗?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | AxiLogi（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 捷克 | 事实 |
| 网站 | axilogi.com | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Master+VAD） | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | AxiLogi s.r.o.(IČO 10964703, Daimlerova 1161/6, 301 00 Plzeň-Skvrňany, Czech Republic;2021-06-23 创；**法人体制谱：Kolibřík klub invest a.s. + DC Europe system a.s. 双 Jednatel 法人在位（2021-06 | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 【推断】「光伏+弱电网络」双驱分销:安装商客层横跨能源与网络两大弱电场景;Cudy/Alta Labs/Conexpro 等中价网络牌已在架=价值档竞争者在谱;配电柜类目=DIN 轨环境暗示 | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】AxiLogi s.r.o.(Pilsen(+Brno Holzova 点);altostrat Master 名录在册,**谱系独特:DEYE(光伏逆变器)+Olife Energy+Felicity(能源存储)+Stromberg(配电)+MikroTik+Ubiquiti+TP-Link+Cudy+Alta Labs+Conexpro+Teltonika+Vami**;类目=Fotovoltaika(光伏)/Bezdráty/LAN/Optické/Napájení(电源)/Bezpečnostní/Rozvaděče(配电柜)/IoT/安装材料 | R65 深挖:法人家长轴型实体（DC Europe 集团属）;plzen 谱位
- 【推断】「光伏+弱电网络」双驱分销:安装商客层横跨能源与网络两大弱电场景;Cudy/Alta Labs/Conexpro 等中价网络牌已在架=价值档竞争者在谱;配电柜类目=DIN 轨环境暗示
- 【假设】开口角度=「光伏/弱电安装商谱的 PoE 随单位」:STC-424 以其网络安装商 value 档入(Cudy/Alta 之上补 24 口管理型),NOTE 留配电柜类目 STI 二线

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

【推断】「光伏+弱电网络」双驱分销:安装商客层横跨能源与网络两大弱电场景;Cudy/Alta Labs/Conexpro 等中价网络牌已在架=价值档竞争者在谱;配电柜类目=DIN 轨环境暗示

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@axilogi.cz
  - 状态：既有/公开
- **电话**：+420 777 103 488
- **原始联系字段**：+420 777 103 488 / sales@axilogi.cz
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 守档 D+3 · Cudy/Alta 对位页

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「光伏/弱电安装商谱的 PoE 随单位」:STC-424 以其网络安装商 value 档入(Cudy/Alta 之上补 24 口管理型),NOTE 留配电柜类目 STI 二线
- **要问的问题**：你们光伏/弱电安装商客户在 24 口管理型 PoE 现随哪款?Cudy/Alta 之上有空档吗?
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 2 次跟进 · 守档 D+14 · sales@axilogi.cz 开口

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「光伏/弱电安装商谱的 PoE 随单位」:STC-424 以其网络安装商 value 档入(Cudy/Alta 之上补 24 口管理型),NOTE 留配电柜类目 STI 二线
- **要问的问题**：你们光伏/弱电安装商客户在 24 口管理型 PoE 现随哪款?Cudy/Alta 之上有空档吗?
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 3 次跟进 · 守档 D+30 · 果归守档

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「光伏/弱电安装商谱的 PoE 随单位」:STC-424 以其网络安装商 value 档入(Cudy/Alta 之上补 24 口管理型),NOTE 留配电柜类目 STI 二线
- **要问的问题**：你们光伏/弱电安装商客户在 24 口管理型 PoE 现随哪款?Cudy/Alta 之上有空档吗?
- **随附/动作**：随附 1 页特性对照/测试包说明


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-07(R65 第 21 批精修 = R57 转写 + 本轮登记新挖)**；原始记录：`batch/B类深挖_2026-10-07_R65_第21批.json`；价格均为 EXW 快照。

- **背景深描**：AxiLogi s.r.o.(IČO 10964703, Daimlerova 1161/6, 301 00 Plzeň-Skvrňany, Czech Republic;2021-06-23 创；**法人体制谱：Kolibřík klub invest a.s. + DC Europe system a.s. 双 Jednatel 法人在位（2021-06-23 起至今）——谱为法人家长轴**;sales@axilogi.cz + servis@axilogi.cz +420 371 420 573
- **芯片与在用型号**：【推断】「光伏+弱电网络」双驱分销:安装商客层横跨能源与网络两大弱电场景;Cudy/Alta Labs/Conexpro 等中价网络牌已在架=价值档竞争者在谱;配电柜类目=DIN 轨环境暗示
- **关键人KP**：Kolibřík klub invest a.s. + DC Europe system a.s. 双法人 Jednatel(sales/servis 函数口已足）
- **关注点与资质**：MikroTik（Master+VAD） 
- **优缺点SWOT**：S:光伏+弱电双驱+Master 名录 / W:中价牌已在架(Cudy/Alta) / O:安装商随单 24 口管理型位 / T:Cudy 低价惯性
- **Saga产品适配**：光伏+弱电双驱分销的安装商随单 24 口 280W 管理型 PoE 位(配电柜类目 STI 二线注记)

### R55 证据摘录（全部保留 · 含数量）

- **【R57备护深挖证据】**DEYE, MikroTik, Vami, TP-Link, Conexpro, Cudy, Alta Labs, Ubiquiti Networks, Stromberg, Teltonika, Olife Energy, Felicity…Fotovoltaika, Bezd
  > DEYE, MikroTik, Vami, TP-Link, Conexpro, Cudy, Alta Labs, Ubiquiti Networks, Stromberg, Teltonika, Olife Energy, Felicity…Fotovoltaika, Bezdráty, LAN, Optické sítě, Napájení, Rozvaděče
  > 来源：https://www.axilogi.com/
- **【R57备护深挖证据】**AxiLogi Master Distributors Pilsen sales@axilogi.cz
  > AxiLogi Master Distributors Pilsen sales@axilogi.cz
  > 来源：https://altostrat.io/buying/hardware/resellers/europe/czech-republic/
- **【R65 登记/联动】**AxiLogi s.r.o. IČO 10964703 · Plzeň Daimlerova 1161/6 · 双法人 Jednatel（法人家长轴）· sales/servis 函数口
  > Jednatel: Kolibřík klub invest a. s. Den vzniku funkce: 23. 6. 2021 … Jednatel: DC Europe system a.s. Den vzniku funkce: 23. 6. 2021 … AxiLogi s.r.o. IČO: 10964703 DIČ: CZ10964703 Daimlerova 1161/6, 301 00 Plzeň
  > 来源：https://axilogi.com/kontakty_d1502.html

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 光伏+弱电双驱分销的安装商随单 24 口 280W 管理型 PoE 位(配电柜类目 STI 二线注记) |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S:光伏+弱电双驱+Master 名录 / W:中价牌已在架(Cudy/Alta) / O:安装商随单 24 口管理型位 / T:Cudy 低价惯性

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
  - [ ] 光伏安装商谱里网络件随单频度
  - [ ] Cudy/Alta 价位带与我司对位

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE value slot for your line

```text
Hi AxiLogi team,

Photovoltaics and low-voltage networking under one roof - DEYE on one shelf, MikroTik and Cudy on the other. Your installers wire both the roof and the rack.

We build a 24-port PoE+ managed switch (280W, L2-lite) with full English/Czech documentation. Reference: $180 USD EXW (2026-09-29) - the documented step above your Cudy/Alta Labs tier for installer jobs that need managed 24-port PoE, white-label friendly.

One question: for your installers building surveillance and network runs, which 24-port managed PoE switch fills the tier above Cudy today - or is that slot open?

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
