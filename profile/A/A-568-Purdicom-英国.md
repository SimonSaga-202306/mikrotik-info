# Purdicom Limited

> **评级 A**　|　英国　|　档案编号 `A-568`　|　优先级 ★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-568
rating: A
country: 英国
biz_org: 公司/工作室（有官网）
business_model: 分销（增值分销 VAD）
decision_speed: moderate
price_sensitivity: medium
volume_potential: 5  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-29
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；分销（增值分销 VAD）
- **商业模式**：分销（增值分销 VAD）
- **为什么值得跟**：【人工定级】A —— R58 竞品谱挖第1波：UK 大 VAD（£38-45M 营业、58-66 人，Oxfordshire Wantage 独立 Ltd），15 品牌谱密且交换机线薄弱，Marvell Prestera 锚=MikroTik CRS 谱在架；Cambium WiFi & Networking Champion 2020 亮相，UK WISP/MSP 通道深
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — ICX/Cambium/TP-Link 交换谱间的 Marvell 级价值对照行（大牌墙旁诚实角+工业件二轨）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：With Cambium/RUCKUS ICX/TP-Link in your stack, who currently fills the 24-port 370W PoE + 4×10G uplink requirement for your WISP/MSP builds?
- **最大未知（影响成交的）**：Crown Group 收购后 buying/product 决策链结构；MikroTik CRS 谱在其 15 品牌里的实际排位与库存量
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Purdicom Limited（原 SELCOMS LIMITED，2013-07-29 更名；CIN 05361794） | 事实 |
| 国家/城市 | 英国 · Wantage, Oxfordshire | 事实 |
| 注册地址 | Mitchell House, Unit 4 Woolley Barns, Wantage, Oxfordshire OX12 8TA | 事实（Companies House 口径） |
| 网站 | purdicom.com | 事实 |
| 成立 | 2005-02-11 | 事实（Companies House 口径） |
| 规模 | 营业额 £38.4M–£45.37M（2024 财年，Endole £45.37M +18.2%）；员工 58（2024 accounts，曾 63） | 事实（公开报表口径） |
| 类型 | 分销（增值分销 VAD） | 事实（CSV 名录口径+官网自述） |
| 反向信号（资质/品牌） | Ubiquiti/MikroTik/Cambium Networks/CommScope RUCKUS/WatchGuard/Teltonika/Siklu/TP-Link/Legrand CertaUPS/IO by HFCL/Nomadix/PatchBox/CertaUPS | 事实（官网/LinkedIn 自认） |
| 获奖 | Cambium Networks WiFi & Networking Champion（Partner Summit 2020）；CRN Sales & Marketing Award 2021 入围；Sunday Times International Track 200 上榜 | 事实（公开报道口径） |
| 组织性质 | 私有 Ltd（非上市） | 【推断】 |
| 商业模式 | 分销（增值分销 VAD） | 【推断】 |
| 团队规模 | 58-66 员工 | 【事实+推断】（Companies House 58；Tracxn 2026-04=66） |
| 决策链 | 中（buying/product manager 两层以内） | 【推断】 |
| Marvell Prestera 锚 | MikroTik CRS 谱在架（RouterBOARD/CRS 系） | 【推断】（官网产品目录含 MikroTik 谱） |

**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Purdicum Limited（英国 Oxfordshire Wantage）：2005 起独立 VAD，营业 £38-45M、员工 58-66；15 品牌谱含 MikroTik/Ubiquiti（非 MikroTik 官方渠道名分）；Cambium WiFi & Networking Champion 2020
- 【推断】谱系以无线/安全为主（Cambium/RUCKUS/WatchGuard/Siklu/Teltonika），交换线弱（ICX=Broadcom 谱、TP-Link 商用散件），Marvell Prestera 谱 PoE++ 价值档正好堵缝
- 【假设】双角：商业 PoE 替补对照行（STC-424）+工业 PoE 二轨（STI-288GP 随 Siklu/Teltonika 户外缘场景缝合）

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有品牌谱口径：Ubiquiti/MikroTik/Cambium/RUCKUS/WatchGuard/Teltonika/Siklu/TP-Link/Legrand CertaUPS/IO by HFCL/Nomadix/PatchBox）

- **Marvell Prestera 旁锚**：MikroTik（RouterBOARD + Cloud Router + CRS 系，含 CRS1xx/3xx 谱）——事实（官网品牌目录）
- **Broadcom 谱**：RUCKUS ICX 交换线（非 Saga 对标目标）——事实（谱系归属）
- **mmWave 回传**：Siklu（EH/100G 级 PtP）——事实
- **工业联接**：Teltonika 4G/5G 工业网关/路由 ——事实

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」；在用品牌未获客户本人确认前一律视为【假设】。MikroTik 具体 SKU 级排货（CRS3xx 库存与排位）无公开可考，记【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 15 品牌无线谱（WISP/MSP 项目供电依赖）+勾ch
  - 工业/户外/宽温：【推断】依据 Siklu mmWave + Teltonika 工业网关配套的户外边缘场景
  - 万兆上行/骨干：【推断】依据 CRS518/100G 谱与 Siklu PtP 的回传链路形态
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 WISP/MSP 核心交换业务目录

## HR 与规模信号（招聘/团队/绿旗）

- Companies House 2024 accounts：员工 58（前一年 63）；GlobalDatabase 同日口径 63。Tracxn 2026-04=66（员工趋势著引）
- Endole 营业额口径 £45.37M（+18.2%）；Tracxn £38.4M（2024-12-31）
- 总部固定：Mitchell House, Woolley Barns（皇家 Oxfordshire 园电网）
- 绿旗：Sunday Times International Track 200 上榜 + Cambium 冠军获奖 = 增势与组织魅力实信号

## 联系方式（已有/猜测分标）

- **网站**：purdicom.com（官网；联系页 public）
- **公司注册**：Companies House CIN 05361794（官档开口）
- **邮箱**：未获得具名 KP 邮箱；首触以官网 info@purdicom.com 通用口（域已核，MX 存在——以 fallback 口径使用）
  - 状态：公司域已核，邮箱为【假设】
- **电话**：官网未显著列示（自查）；Companies House 未含电话
- 来源等级：official-company（Companies House + 官网开口域；外延资料=GlobalDatabase/Endole/Tracxn 口径）
- **验证口径**：MX/DNS 级核（域存活=可投递到域）；沙箱 SMTP RCPT 不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行

## 关键人（KP）与触达通道
- 关键人未定位：首封信件以 info/官网联系表开投并索要 buying manager（switching/networking category）的正联系。
- 56 persona=buying manager / product manager for switching；72 persona=同链路。LinkedIn 员工枚举登录墙外不可见（2026-09-28 纪律），未采。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 商业线

- **推什么**：STC-424DGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：Cambium/RUCKUS ICX/TP-Link 交换谱间的 Marvell 价值对照行（谱缝填充）
- **要问的问题**：目前给 WISP/MSP 客户配的 24 口 PoE+10G 上行交换机是 ICX/CRS 还是 TP-Link？价格带卡在哪个位置？
- **随附/动作**：STC 规格页+$165 USD EXW 快照（15 天有效）

### 第 2 次跟进 · 工业线

- **推什么**：STI-288GP（统一口径=P1 系列，不外溢）
- **切入点**：Siklu mmWave/Teltonika 工业边缘配套的宽温 PoE 二轨
- **要问的问题**：户外 WISP/PtP 节点在冬天掉电或 PoE 冻住时怎么救？客户换过多少台？
- **随附/动作**：STI-288GP 低温实测+MTBF 表

### 第 3 次跟进 · 商业线

- **推什么**：STC-424DGGPM-280W 现货询价（统一口径=P1 系列，不外溢）
- **切入点**：EXW 现货窗口（对照行窗口）
- **要问的问题**：对照行收不收？最后一次窗口期
- **随附/动作**：现货库存+排产日历


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-09-29**；原始记录：`batch/A类深挖_2026-09-29_R56_第57批.json`；价格均为 EXW 快照。

- **①背景再核**：PURDICOM LIMITED 05361794（前身 SELCOMS LIMITED 2013-07-29 更名），2005-02-11 起营业；Mitchell House, Woolley Barns, Wantage OX12 8TA；独立 Ltd；Crown Group/Phoenix Amin 收购（2026 报道）——集团加持下购并链信号
- **②芯片/型号**：MikroTik RouterBOARD + CRS（含 CRS 谱在售）；Teltonika 工业 4G/5G；Siklu mmWave EH；RUCKUS ICX（Broadcom 谱）；Marvell 锚=CRS 谱
- **③KP 深挖**：buying/product manager 未公开定位；56 persona=buying manager、72 persona=同链路；LinkedIn 墙外不览
- **④Saga 对标**：谱系缝隙=交换机谱空（ICX 内墙非 Marvell；Cambium 被动 PoE；TP-Link 商用散件）——P1 STC-424DGGPM-280W+二轨 STI-288GP，价值对照行定位（不一味下价）
- **⑤在乎与偏好**：vendor 墙密=决策单一价值承诺开场；声名渠道（award 领跑者）；现货+可验证数据比砍价更快

### R55 证据摘录（全部保留 · 含数量）

- **【公司主体】**PURDICOM LIMITED is an active company incorporated on 11 February 2005 with the registered office located in Wantage...Turnover £45.37M (+18.2%)...
  > 来源：https://open.endole.co.uk/insight/company/05361794-purdicom-limited
- **【公司主体】**Incorporated 2005-02-11, Registered office: Mitchell House...The principal activity of the company is that of the wholesale distribution of electronic parts and equipment...Employees: 58 (2024 accounts · was 63 in 2023)
  > 来源：https://www.companiesintheuk.co.uk/ltd/purdicom
- **【公司主体】**Unfunded Annual Revenue £38.4M as on Dec 31, 2024...Employee Count 66 as on Apr 30, 2026
  > 来源：https://tracxn.com/d/companies/purdicom/
- **【业务定位】**Purdicom is a growth focused UK value-added IT distributor, focused on wireless, cloud & security
  > 来源：https://purdicom.com/
- **【厂商谱】**From TP-Link through to Ruckus Networks, Purdicom works alongside trusted vendors (TP-Link, Cambium Networks, CertaUPS, IO by HFCL, Nomadix, Ruckus Networks, Siklu, Teltonika, WatchGuard)
  > 来源：https://www.linkedin.com/company/purdicom/
- **【厂商谱合并】**partners for Purdicom include Ubiquiti, Mikrotik, CertaUPS, PatchBox, Purdicom Cloud...
  > 来源：https://www.channelfutures.com/market-trends/crown-group-completes-acquisition-of-purdicom
- **【获奖】**Purdicom awarded Cambium Networks WiFi & Networking Champion at Partner Summit 2020
  > 来源：https://www.google.com/search?q=Purdicom+Cambium+WiFi+Networking+Champion+2020

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：英 Oxfordshire Wantage 无线/云/安全增值分销（VAD），2005 起独立私有 Ltd
- **产品线与在售品牌**：Cambium、RUCKUS、WatchGuard、Teltonika、Siklu、TP-Link、MikroTik、Ubiquiti、Legrand CertaUPS、IO by HFCL、Nomadix、PatchBox、Purdicom Cloud
- **目标行业与场景**：WISP/MSP/校园/酒店多户/户外广覆盖无线与回传、云与安全配套
- **团队与规模**：58-66 员工（Companies House 2024=58；Tracxn 2026=66）
- **决策链与对接人**：私有 Ltd，buying/product manager 未公开定位，info/官网表道首触
- **技术与认证**：Marvell 旁锚=在谱 MikroTik CRS 谱；Teltonika 工业网关；mmWave Siklu；Award=Cambium WiFi & Networking Champion 2020
- **采购与供应链信号**：VAD 分销货模利；谱宽=15 品牌可上样机路线图
- **近期动态与线索**：Cambium Networks Partner Summit 2020 冠军；Crown Group/Phoenix Amin 收购 2026 报道
- **与我方契合点**：交换线弱=STC/STI 互补缝；PoE++/10G 商业+工业 PoE 二轨对照行；Teltonika/Siklu 户外缘联动
- **风险与注意**：谱系拥挤（15 品牌）需一张差异表；RUCKUS ICX 内墙（Broadcom 谱）不是 Saga 对位；Award 型诚信渠道不以谈返点开场；Crown Group 收购后 buying 决策链未绘

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 谱缝填补行：Cambium 被动 PoE/RUCKUS ICX Broadcom 墙/TP-Link 商用散件之间无 Marvell 级 24 口 370W PoE++ + 4×10G；英 VAD 谱开口直接对照行 |
| 备选2 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶；Siklu/Teltonika 户外缘场景补电源，不进首触邮件 |
| 备选3 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶；酒店/多户小区（Nomadix 谱联动）下场，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：£38-45M 营业额 VAD，15 品牌谱网+英国 WISP/MSP 通路深；Cambium 冠军声名；Crown Group 收购加持
- **W**：谱系拥挤（15 品牌）需一张差异表先胜出；ICX 内墙难进；KP（buying manager）未公开定位
- **O**：交换机谱空=STC-424 价值对照行+STI-288GP 工业件二轨；Teltonika/Siklu 户外缘联动
- **T**：大 VAD 供应商侧竞争激烈；收购后 buying 决策链重架；首触需以「现货+可验证数据」抢形似风

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一——Crown Group 收购后尤必问）。
5. 样机先送测，再谈价格。

**停止开发条件（命中任一即停）**：3 次定向触达无任何实质回复；确认现用平台完全满足需求；只愿比价不愿谈场景；决策者确认接触不到；对方书面拒绝。

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（PoE/接入层池） | ✅ |
| 决策人识别 | ❓ KP（buying/product manager for switching）未公开 |
| 触达通道 | ✅ 官网域信息+Companies House；info 通用口待用 |
| 现用交换品牌 | ❓ 谱已知（ICX/TP-Link/Cambium），CRS 排位未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] Crown Group/Phoenix Amin 收购后 buying 决策链变化
  - [ ] MikroTik CRS 谱在 15 品牌中的排位与库存量
  - [ ] 首触 KP（product/buying manager for switching）具名候选

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] WISP/MSP 典型项目端口数与供电预算
- [ ] 仓库与交付时效（EXW 现货敏感度）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for Purdicom's wireless-led catalogue

```text
Hi Purdicom team,

2020 Cambium WiFi & Networking Champion - that is a statement for how Purdicom treats its vendor wall. Your 15-brand catalogue (Cambium, RUCKUS, MikroTik, Ubiquiti, Teltonika, Siklu, TP-Link, WatchGuard...) has depth across wireless and security. But between Cambium's passive PoE, the RUCKUS ICX Broadcom line, and TP-Link commercial SKUs, we noticed a missing Marvell-tier row for 24-port 370W PoE + 4x10G uplink switching - the workhorse box your WISP/MSP deals actually land on.

We are Saga Networks (Saga Telecom), an OEM/ODM of Marvell-Prestera L2/L3 PoE switches, supplying reseller channels in the US, Canada and Europe. Our STC-424DGGPM-280W is exactly that row: 24x Gigabit PoE af/at, 280W budget, 4x10G SFP+ uplinks, Layer 2+ managed with Voice VLAN and PoE watchdog. Reference: $165 USD EXW (snapshot 2026-09-29, 15-day valid) - full English documentation, neutral packaging, customer label by default.

One question: when your WISP/MSP deals spec a 24-port 370W PoE + 4x10G uplink box today, which SKU do you reach for between the ICX line, CRS3xx, and TP-Link - and is that slot stable, or open for a documented value comparison?

If useful, I can send one unit with the complete test pack (PoE-WDG spec sheet + MTBF + raw CLI) for your engineers. If not a fit, one line and I close the loop.

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
- 报价纪律：全部价格为 USD EXW 快照（2026-09-29，15 天有效）；过窗先核价再报价。

---

*建档日期：2026-09-29　|　结构 v2：2026-09-29（R56 规则）　|　数据来源：客户名单_反向信号_2026-09.csv + R58 竞品谱挖第1波调研 JSON（`batch/A类深挖_2026-09-29_R56_第57批.json`）*

---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:[Purdicom · 领英公司页](https://www.linkedin.com/company/purdicom)(既有证据链接,来源:档案;公司页进群后可挑 KP 添加)
- **中国进口与管制**:国别档位 中(NCSC 2027 华为 HNT 移除(电信网);企业网开放;PSTI 合规);档案信号: 在卖中国品牌 TP-Link → 对中国产线接受度已被事实验证;CSV 品牌谱含中国厂商 → 大概率已有中国采购线(集采或分销);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STI-288GP(工业导轨 24G+4×10G→机柜/自动化)、STC-424DGGPM-280W(48G PoE++/4×25G→智算安防酒店全谱)(批量潜力高,可上 280W 旗舰对照行)(本行为调查分析结论,与开发信首推型号是两回事)
