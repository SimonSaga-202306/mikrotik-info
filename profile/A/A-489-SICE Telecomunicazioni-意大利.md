# SICE Telecomunicazioni

> **评级 A**　|　意大利　|　档案编号 `A-489`　|　优先级 ★★★　|　状态：01-已跟进一轮（用户报告；具体日期/收件人未逐户记录）
>
> **触达状态（Stage）**：01-contacted　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-489
rating: A
country: 意大利
biz_org: 公司/工作室（有官网）
business_model: 培训交付
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: true, oem: false, hotel: false, training: true}
p1: STC-424XGGPM-280W
stage: 01-contacted
struct_version: v2  # v2 骨架
updated: 2026-10-12
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：【人工定级】A —— R53 B段复筛达标升级：B 段逐站复筛达标（站点在线 + 交换机品类/产品在售 + 网络/交换专营 + 小公司决策链短）；官网核对：SICE Telecomunicazioni（意大利，1980 年起，自述累计生产超百万台 TLC 设备）**Networking 产品线**页明示 **«La linea Networking di SICE è composta da una famiglia completa di Switch e Router»**（覆盖千兆以太网至光纤网络，支持 BGP/MPLS/OSPF），…；原 B-171 升级，编号顺延 A-489
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — SiCE Telecom 意无线/热点老店（CPE/基站/Hotspot/LoRaWan）：项目随单 PoE 缝低密（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：R71（2026-10-12）：一轮跟进已完成（用户报告；本户具体发送日期/收件地址未逐户提供）。可继续按本档既有策略低频跟进；不对首轮无实质回应者无差别催促；不编排未提供的下次动作日期。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | SICE Telecomunicazioni（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 | 事实 |
| 网站 | sicetelecom.it | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Master+VAD） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】波 R67·A-489:意谱: **SICE 厂级全梯队深挖(意 ICT 老牌第一)**:**法体 Società Italiana Costruzioni Elettroniche S.r.l.(P.IVA 00871160461,1980 创 46 年,Capannori LU)€22.48M 营收(2024 registroaziende)**;**KP 梯队(RocketReach 全谱)**:**Arnaldo Moriconi=Amministratore delegato(CEO)**;**Tommaso Cecchini=EVP+研发分部总监(R&D Division Director)**;**Matteo Tognini=采购经理(Purchasing Manager=P0 KPI 件链直口!)**;Michele Picconi=区销售经理;Francesco Zanni=营销经理;Fabio Moriconi=PM;厂谱:Hiperlink 3.4-28GHz+持牌 IP 桥至 80GHz+OEM 射频模块至 43/80GHz,100 万+设备产量,R&D 40+ 年,军带分支(「ponti radio in banda militare VHF÷80GHz」=守界注);分销阵 MT/Ubiquiti/Cambium/Arc Wireless/Jirous/Mars/Mobotix/Dragon Wave;赞助 ICT Security Forum 2024;Smart Road/Radar/电充站/车牌识读=业务分布五板
- 【推断】R67 推土机深挖 批1 具名 KP 金谱(全系深挖加厚)
- 【假设】Tognini 经理:我司 24 口 280W PoE($165 USD EXW 15 天)对照分销阵,新一季谱链开放比选?

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik（Master+VAD））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@sicetelecom.it
  - 状态：既有/公开
- **电话**：+39 0583 980787
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：+39 0583 980787 / info@sicetelecom.it
- **R71 跟进核对**：本户一轮跟进已完成（用户报告）；逐户发送日期与实际收件地址未提供，不补造。已核实的地址级异常见本档 R71/退信记录；未将用户报告扩大成逐地址送达结论。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Arnaldo Moriconi**(Amministratore delegato(CEO))— sicetelecom.it 域箱 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://rocketreach.co/sice-telecomunicazioni-profile_b452c9befc8c62d8〕
  - **Tommaso Cecchini**(EVP & R&D Division Director(研发分部总监))— sicetelecom.it 域箱 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://contactout.com/company/SICE-Telecomunicazioni-57515〕
  - **Matteo Tognini**(Purchasing Manager(采购经理=P0 KPI 件链直口))— sicetelecom.it 域箱;mob 39328827XXXX(部分掩) 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://rocketreach.co/sice-telecomunicazioni-profile_b452c9befc8c62d8〕
  - **Michele Picconi / Francesco Zanni**(Area Sales Manager / Sales & Marketing Manager)— sicetelecom.it 域箱 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://contactout.com/company/SICE-Telecomunicazioni-57515〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Arnaldo Moriconi | Amministratore delegato(CEO) | sicetelecom.it 域箱 | third-party-RocketReach G+/leads-only | https://rocketreach.co/sice-telecomunicazioni-profile_b452c9befc8c62d8 |
| Tommaso Cecchini | EVP & R&D Division Director(研发分部总监) | sicetelecom.it 域箱 | third-party-contactout G/leads-only | https://contactout.com/company/SICE-Telecomunicazioni-57515 |
| Matteo Tognini | Purchasing Manager(采购经理=P0 KPI 件链直口) | sicetelecom.it 域箱;mob 39328827XXXX(部分掩) | third-party-RocketReach G/leads-only | https://rocketreach.co/sice-telecomunicazioni-profile_b452c9befc8c62d8 |
| Michele Picconi / Francesco Zanni | Area Sales Manager / Sales & Marketing Manager | sicetelecom.it 域箱 | third-party-contactout G/leads-only | https://contactout.com/company/SICE-Telecomunicazioni-57515 |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 具名 kp 引路口

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：具名 kp 引路 → 采购/技术硬件分载线
- **要问的问题**：贵司 PoE 交换机的硬件采购线由哪位同事主责？
- **随附/动作**：规格页

### 第 2 次跟进 · 一页目录卡

- **推什么**：一页目录卡（统一口径=P1 系列，不外溢）
- **切入点**：价值层 PoE 谱链卡
- **要问的问题**：可否入谱链名录？
- **随附/动作**：卡

### 第 3 次跟进 · 留档+LinkedIn 谱

- **推什么**：—（统一口径=P1 系列，不外溢）
- **切入点**：谱链明智途径
- **要问的问题**：—
- **随附/动作**：—


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-10-08_R67_R56_推土机批1.json`；价格均为 EXW 快照。

- **①背景再核**：SICE Telecomunicazioni(法体 Società Italiana Costruzioni Elettroniche S.r.l.,P.IVA 00871160461):1980 创 46 年 ICT 老牌
- **②芯片/型号**：R&D 40+ 年;军带分支(banda militare)=守界注;difesa 谱(ICT magazine)
- **③KP 深挖**：**Arnaldo Moriconi(CEO)+Tommaso Cecchini(EVP R&D)+Matteo Tognini(Purchasing Manager KPI)+Picconi(销)/Zanni(销)/Moriconi F.(PM)** 梯队全
- **④Saga 对标**：我司 424($165)对照分销阵+Hiperlink 供电补链;Tognini 直投窗
- **⑤在乎与偏好**：€22.48M 大户+Tognini 采购直口=P0 窗

### R55 证据摘录（全部保留 · 含数量）

- **【团队与规模】**Fatturato € 22.48 M (2024);P.IVA 00871160461;Ateco 26.30.1 Fabbricazione apparati radiotelevisivi
  > Fatturato € 22.48 M (2024);P.IVA 00871160461;Ateco 26.30.1 Fabbricazione apparati radiotelevisivi
  > 来源：https://registroaziende.it/azienda/societa-italiana-costruzioni-elettroniche-srl-enunciabile-anche-in-sice-srl-o-sice-srl-o-capannori
- **【决策链与对接人】**Arnaldo Moriconi Amministratore delegato;Matteo Tognini Purchasing Manager(39328827XXXX)
  > Arnaldo Moriconi Amministratore delegato;Matteo Tognini Purchasing Manager(39328827XXXX)
  > 来源：https://rocketreach.co/sice-telecomunicazioni-profile_b452c9befc8c62d8
- **【决策链与对接人】**Tommaso Cecchini EVP, R&D Division Director;Michele Picconi Area Sales Manager;Francesco Zanni Sales & Marketing Manager
  > Tommaso Cecchini EVP, R&D Division Director;Michele Picconi Area Sales Manager;Francesco Zanni Sales & Marketing Manager
  > 来源：https://contactout.com/company/SICE-Telecomunicazioni-57515
- **【技术与认证】**ponti radio in banda militare in tutte le bande licenziate e non, in gamma VHF ÷ 80 GHz;OEM radio modules up to 43/80 GHz
  > ponti radio in banda militare in tutte le bande licenziate e non, in gamma VHF ÷ 80 GHz;OEM radio modules up to 43/80 GHz
  > 来源：https://www.ictsecuritymagazine.com/notizie/sice-telecomunicazioni/
- **【近期动态与线索】**Sponsor ICT Security Forum 2024;produzione oltre un milione di dispositivi
  > Sponsor ICT Security Forum 2024;produzione oltre un milione di dispositivi
  > 来源：https://www.ictsecuritymagazine.com/eventi/forumictsecurity2024/sponsor-sice_telecomunicazioni

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：SICE Telecomunicazioni(法体 Società Italiana Costruzioni Elettroniche S.r.l.,P.IVA 00871160461):1980 创 46 年 ICT 老牌
- **产品线与在售品牌**：Hiperlink 3.4-28GHz PtP/PtMP+持牌 IP 桥 80GHz+OEM 射频模块 43/80GHz;Smart Road/Radar/电充站/车牌识读/LoRaWAN/WiMax/LTE/5G
- **目标行业与场景**：意+全球 B2B(只安装商/二级分销);ICT Security Forum 2024 赞助;Smart Road/Radar 高新板
- **团队与规模**：26-200 人谱差旗(RocketReach 26/LI 51-200 band/contactout 28);LI 2316 粉;€22.48M(2024)营收
- **决策链与对接人**：**Arnaldo Moriconi(CEO)+Tommaso Cecchini(EVP R&D)+Matteo Tognini(Purchasing Manager KPI)+Picconi(销)/Zanni(销)/Moriconi F.(PM)** 梯队全
- **技术与认证**：R&D 40+ 年;军带分支(banda militare)=守界注;difesa 谱(ICT magazine)
- **采购与供应链信号**：Tognini 采购经理=我司件链 P0 口;sicetelecom.it 域箱;
- **近期动态与线索**：2024-12 ICT magazine 深报;ICT Security Forum 赞助;SIAE/Intracom 谱带
- **与我方契合点**：我司 424($165)对照分销阵+Hiperlink 供电补链;Tognini 直投窗
- **风险与注意**：军带守界;人谱带差旗;leads-only

## 同谱竞合谱注（R67：MikroTik 官方分销位竞合判定）

> 谱注日期 **2026-10-08**；来源=CSV 类型/信号列+R54/R55 深挖档；原始记录：`batch/A类竞合谱注_2026-10-08_R67_批1.json`。本节为定位判定，不改级、不改档。

- **官方位**：MikroTik（Master+VAD）
- **谱位**：通用分销
- **判定**：该户为 MikroTik 官方分销(Master+VAD)+VAD 认证价值型:其 MikroTik 授权位/服务网=不可替资产,我方不与 MT 官方线硬碰;谱策=通用位:非 MT 空档(工业 PoE/大功率 24/48V)补位+价谱情报互织。报价纪律=补位不硬冲(MT 有 SKU 的型号不报价;MT 空档报 STC/STI 谱)。

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | SiCE Telecom 意无线/热点老店（CPE/基站/Hotspot/LoRaWan）：项目随单 PoE 缝低密（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：具名梯队金谱
- **W**：军带守界;人谱差旗;leads-only
- **O**：€22.48M 大户+Tognini 采购直口=P0 窗
- **T**：谱链节奏;leads-only

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 教师红线：不打学员名单、不经培训语境推销

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
  - [ ] CEO/R&D/采购梯队全、46 年 R&D、100 万+设备、雷达/Smart Road 新板
  - [ ] 军段推辞・民用商业限定

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Dear Arnaldo Moriconi Team,

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $165 USD EXW (2026-10-08, 15 days valid) — a value unit that rides along with each deployment. Datasheet + CE pack on request.

Best regards
Saga / SmartByte ODM
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

<!-- R71-FOLLOWUP-START -->
## R71 本轮跟进与邮件回执（2026-10-12）

- **跟进范围**：A/B 本轮一轮跟进已完成（用户报告）；逐户发送日期与实际收件地址未提供，本节不补造发送日志。
- **本户结论**：一轮跟进已完成；可继续按本档既有策略低频跟进，不把“已跟进”误写成“逐地址送达成功”。
- **地址级范围**：R71 退信台账未为本户列出新的精确地址异常；可继续跟进不等于对每个邮箱作了 SMTP 或逐地址送达验证。
- **后续节奏**：首轮之后不作无差别催促；按既有节奏等待或低频跟进，不填造日期。
<!-- R71-FOLLOWUP-END -->
