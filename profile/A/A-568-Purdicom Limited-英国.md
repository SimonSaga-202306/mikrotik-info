# Purdicom Limited

> **评级 A**　|　英国 · Wantage, Oxfordshire　|　档案编号 `A-568`　|　优先级 ★★　|　状态：未触达
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
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-10-07
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；分销（增值分销 VAD）
- **商业模式**：分销（增值分销 VAD）
- **为什么值得跟**：【人工定级】A —— R58 竞品谱挖第1波：UK 大 VAD（£38-45M 营业、58-66 人），15 品牌谱密且交换线空，Marvell Prestera 锚=CRS 在谱，可接 PoE++/10G 商业件补位；A 挖档已加厚
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Purdicom 英 Oxfordshire £38–45M VAD（CIN 05361794，2005 起；Cambium 冠军 2020）：15 品牌谱交换线空（ICX=Broadcom/Cambium 被动PoE/TP-Link 散件）→ PoE++/10G 对照行+工业二轨（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Purdicom Limited（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Wantage, Oxfordshire | 事实 |
| 网站 | purdicom.com | 事实 |
| 类型 | 分销（增值分销 VAD） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Ubiquiti/MikroTik/Cambium Networks/CommScope RUCKUS/WatchGuard/Teltonika/Siklu/TP-Link/Legrand CertaUPS/IO by HFCL/Nomadix/PatchBox（官网 15 品牌谱） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 分销（增值分销 VAD） | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】PURDICOM LIMITED（英国公司序 05361794，前身为 SELCOMS LIMITED 2013-07-29 更名），2005-02-11 成立，注册址 Mitchell House, Unit 4 Woolley Barns, Wantage, Oxfordshire OX12 8TA；英国增值 IT 分销商（VAD），自述「growth focused UK value-added IT distributor focused on wireless, cloud & security」，营业 £38.4M-£45.37M（2024 财年，Endole £45.37M +18.2% GlobalDatabase £44M），员工 58-66 人（Companies House 2024 报表 58；Tracxn 2026-04 为 66）；vendor 谱 15+：Cambium Networks（2020 WiFi & Networking Champion）、CommScope RUCKUS、WatchGuard、Teltonika Networks、Siklu、TP-Link、Legrand CertaUPS、IO by HFCL、MikroTik、Ubiquiti（UI Distributors UK）、Nomadix、PatchBox、Purdicom Cloud
- 【推断】谱系以无线回传/校园无线/安全为主，交换线弱（RUCKUS ICX 是 Broadcom 谱、Cambium PoE 被动供电为主），MikroTik 在谱但没有官方 Master 名分（mikrotik.com 官方分销目录查无此户）——Marvell Prestera 锚=CRS 在售 + Teltonika 工业网关联动的边缘场景；Saga PoE++/10G 商业与工业交换机正是其谱系缝隙
- 【假设】可作为英国多品牌补位渠道切入：以 STC-424XGGPM-280W 对位 ICX 空白价格带 + STI-288GP 补工业/户外拼接 Siklu Teltonika 项目画完；Badge 强（Continence/自治身 posture 强），首触需以「香港可验证现货+POE++/IP 工程数据」开场

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Ubiquiti/MikroTik/Cambium Networks/CommScope RUCKUS/WatchGuard/Teltonika/Siklu/TP-Link/Legrand CertaUPS/IO by HFCL/Nomad）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：—
  - 状态：缺失（leads-only 口径：人工补录前**不进群发**，与旧批次纪律一致）
- **电话**：05361794
- **原始联系字段**：purdicom.com 官网；Companies House CIN 05361794（Mitchell House, Unit 4 Woolley Barns, Wantage OX12 8TA）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 商业线

- **推什么**：STC-424XGGPM-280W（24口 PoE+4×10G）（统一口径=P1 系列，不外溢）
- **切入点**：ICX/Cambium 交换谱旁的高性价比商业 PoE 替补对照行
- **要问的问题**：目前给你的 WISP/MSP 客户提供 24 口 PoE+10G 上行交换的方案是 ICX/CRS 还是 TP-Link？价格带卡在哪个位置？
- **随附/动作**：STC 规格页+$180 USD EXW 快照（15 天有效）

### 第 2 次跟进 · 工业线

- **推什么**：STI-288GP（8 口工业 PoE 导轨）（统一口径=P1 系列，不外溢）
- **切入点**：Sikulu/Teltonika 户外广覆盖配套的宽温边缘供电二轨
- **要问的问题**：户外 WISP/PtP 节点冬天掉电或 PoE 冻住时怎么救？换过多少台？
- **随附/动作**：STI-288GP 低温实测+MTBF

### 第 3 次跟进 · 商业线

- **推什么**：STC-424XGGPM-280W 现货询价（统一口径=P1 系列，不外溢）
- **切入点**：最后一次窗口：EXW 现货产能
- **要问的问题**：对照行收不收？封顶一时问
- **随附/动作**：现货库存+排产日历


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-29_R56_第57批.json`；价格均为 EXW 快照。

- **①背景再核**：PURDICOM LIMITED 05361794，2005-02-11 起营业；前身 SELCOMS LIMITED（2013-07-29 更名）；独立 Ltd，2026-10 Crown Group/Phoenix Amin 收购其（UK 上市集团体系）——自 报道可见「Crown Group completes acquisition of Purdicom」，年头成立；Mitchell House, Woolley Barns OX12 8TA
- **②芯片/型号**：MikroTik 在谱（含 RouterBOARD+CRS 谱）；Teltonika 工业 4G/5G 网关；Siklu mmWave；ICX=RUCKUS（Broadcom 谱非 Saga 目标）；Marvell Prestera 旁锚=CRS
- **③KP 深挖**：56 persona 未公开；72 persona=buying manager/product manager（LinkedIn 枚举登录墙外不可见，未定位，首触 info 索人）
- **④Saga 对标**：谱系缝隙=商业 PoE++/10G + 工业 PoE 二轨；P1 STC-424XGGPM-280W；二轨 STI-288GP；速决性=大 VAD 广谱为模，对位成本型补位谱
- **⑤在乎与偏好**：vendor 墙密，决策僧需清楚「New vendor onboarding」表单+单一价值承诺；不以打折做角；Cambium 冠军 2020 诉时尚

### R55 证据摘录（全部保留 · 含数量）

- **【公司主体】**PURDICOM LIMITED is an active company incorporated on 11 February 2005 with the registered office located in Wantage...Turnover £45.37M (+18.2%)...
  > PURDICOM LIMITED is an active company incorporated on 11 February 2005 with the registered office located in Wantage...Turnover £45.37M (+18.2%)...
  > 来源：https://open.endole.co.uk/insight/company/05361794-purdicom-limited
- **【公司主体】**PURDICOM LIMITED, Incorporated 2005-02-11, Registered office: Mitchell House, Unit 4 Woolley Barns, Wantage, Oxfordshire, OX12 8TA...The principal activity of the company is that of the wholesale distribution of electronic parts and equipment...Employees: 58 (2024 accounts · was 63 in 2023)
  > PURDICOM LIMITED, Incorporated 2005-02-11, Registered office: Mitchell House, Unit 4 Woolley Barns, Wantage, Oxfordshire, OX12 8TA...The principal activity of the company is that of the wholesale distribution of electronic parts and equipment...Employees: 58 (2024 accounts · was 63 in 2023)
  > 来源：https://www.companiesintheuk.co.uk/ltd/purdicom
- **【公司主体】**Unfunded Annual Revenue £38.4M as on Dec 31, 2024...Employee Count 66 as on Apr 30, 2026...PURDICOM LIMITED CIN: 5361794
  > Unfunded Annual Revenue £38.4M as on Dec 31, 2024...Employee Count 66 as on Apr 30, 2026...PURDICOM LIMITED CIN: 5361794
  > 来源：https://tracxn.com/d/companies/purdicom/__xWiPZ6y_AdH8M4sNAUUipBZ3Oy3nHPcdGCjLEwSGV0c
- **【业务定位】**Purdicom is a growth focused UK value-added IT distributor, focused on wireless, cloud & security
  > Purdicom is a growth focused UK value-added IT distributor, focused on wireless, cloud & security
  > 来源：https://purdicom.com/
- **【厂商谱】**From TP-Link through to Ruckus Networks, Purdicom works alongside trusted vendors who guarantee quality(Tp-Link, Cambium Networks, CertaUPS, IO by HFCL, Nomadix, Ruckus Networks, Siklu, Teltonika, WatchGuard)
  > From TP-Link through to Ruckus Networks, Purdicom works alongside trusted vendors who guarantee quality(Tp-Link, Cambium Networks, CertaUPS, IO by HFCL, Nomadix, Ruckus Networks, Siklu, Teltonika, WatchGuard)
  > 来源：https://www.linkedin.com/company/purdicom/
- **【厂商谱】**...partners for Purdicom include Ubiquiti, Mikrotik, CertaUPS, PatchBox, Purdicom Cloud...The group prides itself...
  > ...partners for Purdicom include Ubiquiti, Mikrotik, CertaUPS, PatchBox, Purdicom Cloud...The group prides itself...
  > 来源：https://www.channelfutures.com/market-trends/crown-group-completes-acquisition-of-purdicom
- **【获奖】**Purdicom awarded Cambium Networks WiFi & Networking Champion at Partner Summit 2020
  > Purdicom awarded Cambium Networks WiFi & Networking Champion at Partner Summit 2020
  > 来源：https://www.google.com/search?q=Purdicom+Cambium+WiFi+Networking+Champion+2020

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：英国 Oxfordshire Wantage 无线/云/安全增值分销（VAD），2005 起营业，独立私有
- **产品线与在售品牌**：Cambium、RUCKUS、WatchGuard、Teltonika、Siklu、TP-Link、MikroTik、Ubiquiti、Legrand CertaUPS、IO by HFCL、Nomadix、PatchBox、Purdicom Cloud
- **目标行业与场景**：WISP/MSP/校园/酒店多户/户外广覆盖无线与回传、云与安全配套
- **团队与规模**：58-66 员工（Companies House 2024=58；Tracxn 2026=66）
- **决策链与对接人**：私有 Ltd，buying/product manager 未公开定位，info 通道首触
- **技术与认证**：Marvell 旁锚=在谱 MikroTik CRS 谱；Teltonika 工业网关；mmWave Siklu
- **采购与供应链信号**：VAD 分销货模利；VAD 量厂可上样机路线图（15 brand 谱系）
- **近期动态与线索**：Cambium Networks WiFi & Networking Champion（2020 Partner Summit）；扩大 5/无放弃线不断增长
- **与我方契合点**：交换线弱=STC/STI 互补空显；交换机为先的 PoE++/10G 商业与工业件正好堵其谱缝
- **风险与注意**：谱系拥挤（15+ 品牌）需一张差异表做决定；RUCKUS ICX 内墙（Broadcom 谱）不是 Saga 的目标对位；Price 议以可验证现货+对照行开场

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Purdicom 英 Oxfordshire £38–45M VAD（CIN 05361794，2005 起；Cambium 冠军 2020）：15 品牌谱交换线空（ICX=Broadcom/Cambium 被动PoE/TP-Link 散件）→ PoE++/10G 对照行+工业二轨（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：£38-45M 营业额 VAD,15 品牌无线/云/安全谱深，收购加持
- **W**：谱系拥挤+ICX 内墙+KP 未定位
- **O**：交换机互补空显 PoE++/工业二轨；Teltonika 联动
- **T**：大 VAD 供应商侧拥挤，首触需以差异化数据开场

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
| 触达通道 | ❓ 缺邮箱 |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] Crown Group/Phoenix Amin 收购后 buying 决策链变化
  - [ ] 具体 MikroTik CRS 套件与在价（grating)JD
  - [ ] 首触 KP（product/buying manager for switching）未定位

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi team

I'm with Saga Networks (Saga 网络配套厂商）。我们在你家谱系里发现一个真空区：Cambium 的被动 PoE 租象、RUCKUS ICX 的 Broadcom 等级墙、TP-Link 的商用线之间，没有任何 Marvell Prestera 等级的高性价比 PoE++ 24 口交换。

这当布局还对你腾空：STC-424XGGPM-280W（24 口 370W PoE++ + 4×10G SFP+ L2+ 交换机，EXW $180 快照 15 天有效），发规格页对照行；工业缘 STI-288GP（导轨 DIN 导轨宽温 -40–75°C 8 口 PoE）Siklu/Teltonika 边缘荒场景可缝合。

可问一句：在五Tag你MSP给客户哪些 24 口 PoE+10G 交换？若 ICX/CRS 档位有缝，对照行给你发过去。

Regards,
[Saga Networks]David
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
