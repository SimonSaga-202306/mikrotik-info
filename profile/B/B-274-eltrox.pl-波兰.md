# eltrox.pl

> **评级 B**　|　波兰　|　档案编号 `B-274`　|　优先级 ★★　|　状态：01-已跟进一轮（用户报告；具体日期/收件人未逐户记录）
>
> **触达状态（Stage）**：01-contacted　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-274
rating: B
country: 波兰
biz_org: 分销/批发商（有官网）
business_model: 分销 stocking
decision_speed: moderate
price_sensitivity: high
volume_potential: 5  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 01-contacted
struct_version: v2  # v2 骨架
updated: 2026-10-12
```

## SALES BRIEF（压缩模型）

- **是谁**：2003 创 23 年;Częstochowa;资本 560k zł;KRS全谱(股东+CEO+prokura)…
- **商业模式**：分销 stocking
- **为什么值得跟**：通用分销商信号，无差异化切入点，慢慢跟
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — 波兰安防巨头的监控/报警安装商随单 24 口 280W PoE 走量位(40 门店架)；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：你们的监控/报警安装商客户,24 口管理型 PoE+ 现随哪家?门店架上 value 档有位吗?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：R71（2026-10-12）：一轮跟进已完成（用户报告；本户具体发送日期/收件地址未逐户提供）。可继续按本档既有策略低频跟进；不对首轮无实质回应者无差别催促；不编排未提供的下次动作日期。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | eltrox.pl（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 波兰 | 事实 |
| 网站 | eltrox.pl | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Master） | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | 2003 创 23 年;Częstochowa;资本 560k zł;KRS全谱(股东+CEO+prokura) | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 监控/报警电商+电子电信批发;PoE 24 口=监控供电正行对口 | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】波 R67/TUB·批9·B-274:波谱: **ELTROX SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ 深挖(krs-pobierz/aleo/D&B/eltrox.pl 四源互证)**:**KRS 0000175807;NIP 6462490527;REGON 276916481;Kapitał zakładowy 560,000 zł;2003-12-01 注册(23 年);ul. Warszawska 74,42-202 Częstochowa;Forma prawna=Spółka z O.O.;Status aktywna;Główna działalność=**sprzedaż hurtowa sprzętu elektronicznego i telekomunikacyjnego oraz części do niego=电子与电信设备批发(登档法言)**;D&B 别类=Courier/Trading 谱注**;**官网电商谱(eltrox.pl):**监控+报警系统+家居自动化+门驱动+能源电源+电脑配件+消费电子**=安防电商谱;ceneo s2306 店;sklep@eltrox.pl/finanse@eltrox.pl;+48 34 387 29 92**;**KP 金锚(krs 档全谱):**Zbigniew Dąbrowski(zarząd=董事会/Dyrektor naczelny=CEO 谱,D&B 记「President of the Board of Directors」full=Zbigniew Feliks Dąbrowski P0)+Wiktor Dąbrowski(wspólnik=股东参与人+Barbara Otolińska(wspólnik 股东)+Przemysław Piotrowski(prokura=授权代理人)**=Dąbrowski 家族全谱+代理谱**;**谱位=琴斯托霍瓦 23 年安防电商+电子电信批发(登档)=24 口 PoE 对监控/报警供电正行=批 9 波谱对口金矿**;排噪:krs-online 同厅档「Eltrox.pl Dąbrowski Z.」Białystok BHP/PPOŻ 劳保消防谱(同 NIP/KRS 号但描述 2000 创+劳保业)=同 NIP 错挂数,以 krs-pobierz/D&B 琴斯托霍瓦电子批发谱为准**。
- 【推断】R67/TUB 推土机深挖 批9 B 类既定十户
- 【假设】STC-424XGGPM-280W($165 USD EXW (2026-10-08, 15天有效))具名谱引路

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

监控/报警电商+电子电信批发;PoE 24 口=监控供电正行对口

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sklep@eltrox.pl
  - 状态：既有/公开
- **电话**：34 333 57 04
- 来源等级：official-channel（R41–R48 联系方式台账口径）
- **原始联系字段**：34 333 57 04 / sklep@eltrox.pl
- **R71 跟进核对**：本户一轮跟进已完成（用户报告）；逐户发送日期与实际收件地址未提供，不补造。已核实的地址级异常见本档 R71/退信记录；未将用户报告扩大成逐地址送达结论。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Zbigniew Dąbrowski**(Prezes Zarządu（主席）)— 经 eltrox.pl/finanse@eltrox.pl 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://aleo.com/int/company/eltrox-pl〕
  - **Barbara Otolińska**(大股东（90%))— 同上 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:同上〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Zbigniew Dąbrowski | Prezes Zarządu（主席） | 经 eltrox.pl/finanse@eltrox.pl | aleo/KRS 双源实名 | https://aleo.com/int/company/eltrox-pl |
| Barbara Otolińska | 大股东（90%) | 同上 | 同源 | 同上 |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · Dąbrowski CEO+Piotrowski prokura

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：CEO+代理双轨 → 24 口 PoE(监控供电正行)
- **要问的问题**：贵司监控品线的 24 口 PoE 交换机供货由哪位同事主责?
- **随附/动作**：krs/D&B 4 源

### 第 2 次跟进 · sklep 电商采购线

- **推什么**：STI-288GPM/424（统一口径=P1 系列，不外溢）
- **切入点**：sklep@+ceneo 谱类
- **要问的问题**：贵司电商上架线的 PoE 谱口?
- **随附/动作**：eltrox.pl 谱

### 第 3 次跟进 · Wiktor Dąbrowski+Otolińska 股东层

- **推什么**：STC-28DGGPM（统一口径=P1 系列，不外溢）
- **切入点**：股东层=资本谱
- **要问的问题**：贵司供应商审核周期的 Docs 谱?
- **随附/动作**：


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-08**；原始记录：`batch/B类深挖_2026-10-08_R67_R56_推土机批9.json`；价格均为 EXW 快照。

- **背景深描**：2003 创 23 年;Częstochowa;资本 560k zł;KRS全谱(股东+CEO+prokura)
- **芯片与在用型号**：监控/报警电商+电子电信批发;PoE 24 口=监控供电正行对口
- **关键人KP**：Zbigniew Feliks Dąbrowski(CEO=President of the Board)+Wiktor Dąbrowski(股东)+Barbara Otolińska(股东)+Przemysław Piotrowski(prokura)=4 人登档谱
- **关注点与资质**：波兰安防电商 → 24 口 PoE 监控供电(正行直对口)
- **优缺点SWOT**：S=23 年+KRS 登档全谱+监控正行对口+电商谱·W=微商谱量级小;krs-online 同名错挂排噪注·O=波兰安防电商潮=PoE 监控供电上新轴·T=BAT/pol 电商竞争;价敏谱
- **Saga产品适配**：STC-424XGGPM-280W 24 口 PoE($165 USD EXW,15 天有效):波语谱;电商节奏;ceneo 平台价敏;登档名=批发业

### R55 证据摘录（全部保留 · 含数量）

- **【KRS 登档】**NIP 6462490527 | KRS 0000175807 | REGON 276916481 | ul. WARSZAWSKA 74, CZĘSTOCHOWA;Kapitał zakładowy 560 000,00 ZŁ;Status aktywna;Główna działalność: Sprzedaż hurtowa sprzętu elektronicznego i telekomunikacyjnego oraz części do niego;Osoby powiązane: BARBARA OTOLIŃSKA(wspolnik)+WIKTOR DĄBROWSKI(wspolnik)+ZBIGNIEW DĄBROWSKI(zarzad)+PRZEMYSŁAW PIOTROWSKI(prokura)
  > NIP 6462490527 | KRS 0000175807 | REGON 276916481 | ul. WARSZAWSKA 74, CZĘSTOCHOWA;Kapitał zakładowy 560 000,00 ZŁ;Status aktywna;Główna działalność: Sprzedaż hurtowa sprzętu elektronicznego i telekomunikacyjnego oraz części do niego;Osoby powiązane: BARBARA OTOLIŃSKA(wspolnik)+WIKTOR DĄBROWSKI(wspolnik)+ZBIGNIEW DĄBROWSKI(zarzad)+PRZEMYSŁAW PIOTROWSKI(prokura)
  > 来源：https://krs-pobierz.pl/eltrox-spolka-z-ograniczona-odpowiedzialnoscia-i0000175807
- **【登档谱】**ELTROX SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ;WARSZAWSKA 74, 42-202 CZĘSTOCHOWA;TAX ID 6462490527;KRS 0000175807;REGON 276916481;Legal form: limited liability company
  > ELTROX SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ;WARSZAWSKA 74, 42-202 CZĘSTOCHOWA;TAX ID 6462490527;KRS 0000175807;REGON 276916481;Legal form: limited liability company
  > 来源：https://aleo.com/int/company/eltrox-pl
- **【KP/CEO 档】**ELTROX SP Z O O;Dyrektor naczelny: Dąbrowski Zbigniew Feliks(President of the Board of Directors);NIP 6462490527;KRS 0000175807;Częstochowa, śląskie;Other Electronic Parts and Equipment Merchant Wholesalers;www.eltrox.pl
  > ELTROX SP Z O O;Dyrektor naczelny: Dąbrowski Zbigniew Feliks(President of the Board of Directors);NIP 6462490527;KRS 0000175807;Częstochowa, śląskie;Other Electronic Parts and Equipment Merchant Wholesalers;www.eltrox.pl
  > 来源：https://www.dnb.com/pl-pl/baza-firm/profile-firm.eltrox_sp_z_o_o.73dff5fc245430eb355305496fe12e72.html
- **【电商品类谱】**eltrox.pl:监控+报警系统+家居自动化+门驱动+能源电源+电脑配件+消费电子;sklep@eltrox.pl;finanse@eltrox.pl;+48 34 387 29 92;ceneo 店谱
  > eltrox.pl:监控+报警系统+家居自动化+门驱动+能源电源+电脑配件+消费电子;sklep@eltrox.pl;finanse@eltrox.pl;+48 34 387 29 92;ceneo 店谱
  > 来源：https://eltrox.pl/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 波兰安防巨头的监控/报警安装商随单 24 口 280W PoE 走量位(40 门店架) |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S=23 年+KRS 登档全谱+监控正行对口+电商谱·W=微商谱量级小;krs-online 同名错挂排噪注·O=波兰安防电商潮=PoE 监控供电上新轴·T=BAT/pol 电商竞争;价敏谱

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
  - [ ] MikroTik 谱位 eltrox.pl 在售线核
  - [ ] Zbigniew 直邮推 eltrox.pl 域(sklep@/finanse@)
  - [ ] ceneo 店评价谱节奏

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your line

```text
Dear Zbigniew,\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) — a natural fit for powering CCTV cameras and alarm systems in your portfolio. Reference: $165 USD EXW (2026-10-08, 15 days valid). Datasheet + CE pack on request.\n\nBest regards\nSaga / SmartByte ODM
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
