# Modelec Data-Industrie

> **评级 A**　|　荷兰　|　档案编号 `A-277`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-277
rating: A
country: 荷兰
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: true, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Modelec 荷工业数据通信分销（Westermo 官方 where-to-buy 名录实锤）：替补窄位（$180 锚点一致）；官网 JS 重证据薄注；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Modelec Data-Industrie（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 荷兰 | 事实 |
| 网站 | https://www.modelec.nl | 事实 |
| 类型 | 分销（Westermo Reseller） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Westermo | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Modelec Data-Industrie:MODELEC Data-Industrie B.V.(荷兰 Ede(Gelderland),Galvanistraat;**1977 创 49 年;21-50 人;「Your OT Network. Our Expertise」=OT 网络+网安专营(电网/水务/监狱/智能交通=KRITIS 守界加厚)**;**品牌谱 Moxa/Westermo/TXOne/Robustel;SPIE 站台自动化长期伙伴件**;**Contactinfo: Stefan Barten stefan@modelec.nl(SecurityDelta 伙伴页=O)+Bart Jan Witteveen bartjan@modelec.nl(Energy Storage NL+SPIE 案例件)+Sergio Alonso Owner(prospeo 谱)**
- 【推断】R66 第 20 波具名 KP 金谱
- 【假设】24 口 value PoE($180 USD EXW (2026-10-07, 15天有效))具名谱位引路

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Westermo）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：contact@modelec.nl
  - 状态：既有/公开
- **电话**：+31 318 636 262
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：contact@modelec.nl（官网联系页正文）；支持：support@modelec.nl；订单：order@modelec.nl；原入口：+31 318 636 262
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Stefan Barten**(Contactinfo(伙伴页具名 stefan@modelec.nl +31 318-626262))— securitydelta.nl 伙伴页(O) 〔已有(公司官方公开件/登记册自曝);源:https://securitydelta.nl/partners/overview-partners/modelec〕
  - **Bart Jan Witteveen**(联络/案例件具名(bartjan@modelec.nl;SPIE 案例照件))— energystoragenl.nl+modelec.nl 双源 〔已有(公司官方公开件/登记册自曝);源:https://www.energystoragenl.nl/en/lid/modelec-data-industrie-bv/〕
  - **Sergio Alonso**(Owner(业主谱))— prospeo.io 谱面条 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://prospeo.io/c/modelec〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Stefan Barten | Contactinfo(伙伴页具名 stefan@modelec.nl +31 318-626262) | securitydelta.nl 伙伴页(O) | official-self-published·谱/leads-only(直发需 opt-in) | https://securitydelta.nl/partners/overview-partners/modelec |
| Bart Jan Witteveen | 联络/案例件具名(bartjan@modelec.nl;SPIE 案例照件) | energystoragenl.nl+modelec.nl 双源 | official-self-published·谱/leads-only(直发需 opt-in) | https://www.energystoragenl.nl/en/lid/modelec-data-industrie-bv/ |
| Sergio Alonso | Owner(业主谱) | prospeo.io 谱面条 | leads-only·待 opt-in(LinkedIn/谱面带核) | https://prospeo.io/c/modelec |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 工业非管理低价档一页（报价空档位）

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：荷/英一封：Westermo 报价之外的非管理宽温价位档第二来源（CE/宽温参数一体）；提一句可直接书面报价到 order@。
- **要问的问题**：现场非管理件的报价空档目前怎么填？
- **随附证明**：工业件一页 + 参数包。

### 第 2 次跟进 · 收发器/配线邻位件

- **推什么**：收发器 + SFP 窄线
- **切入点**：工业光纤场景的收发器/SFP 邻位窄线低价档。
- **要问的问题**：收发器/SFP 邻位件有补价位档需求吗？
- **随附证明**：窄线一页价卡。

### 第 3 次跟进 · 条款收口

- **推什么**：—（条款）
- **切入点**：梯价/中性发货条款收口；不回即冻结。
- **要问的问题**：（无需回）条款留档。
- **随附证明**：条款一页（英）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：荷兰工业数据通信分销（Westermo+Moxa 双锚，Ede）——同规格 1/3 价工业第二来源标准打法。
- **产品线与在售品牌**：工业联网件/布线（Westermo/Moxa 口径）；全套技术支持与本地办会能力（CSV）。
- **目标行业与场景**：荷兰工业/轨道/公用事业客群。
- **团队与规模**：中型专业分销（部门制分箱）。
- **决策链与对接人**：contact@modelec.nl（销售）/order@modelec.nl（订单采购箱，官网联系页正文）。
- **技术与认证**：Westermo Reseller（名录+CSV）。
- **采购与供应链信号**：Westermo 锚位深：**报价空档的非管理价位档与配线/收发器邻位件**；order@ 存在=其采购流程习惯书面报价单，合拍我们的报价节奏。
- **近期动态与线索**：站正常运行、部门体系完整=采购流程规范户。
- **与我方契合点**：工业非管理宽温 8 口低价档+收发器邻位件。
- **风险与注意**：Westermo/Moxa 锚牌不碰排位；首封到 contact@、报价单抄送习惯提一句可 order@ 直接下单。

### R54 原文证据摘录（全部保留）

- **【业务定位】**埃德（Ede）的工业数据通信分销：站题自述「以可靠安全的网络方案做连接」；支持页自述 Moxa 与 Westermo（CSV 9-27 复核；Westermo 官方 where-to-buy 名录在册）。
  > MODELEC weet te verbinden met betrouwbare en veilige netwerkoplossingen ‖ （CSV 2026-09-23/27 记录）Westermo 官方 where-to-buy 名录确认；支持页复核其自称 Moxa 与 Westermo
  > 来源：https://www.modelec.nl/contact/
- **【决策链与对接人】**联系页按部门分箱：Sales contact@modelec.nl / Support support@ / 行政 administratie@ / **订单与采购委托 order@modelec.nl**；Ede Galvanistraat 38，KvK 09079853。
  > 📧 Afdeling Sales — contact@modelec.nl ‖ 📧 Afdeling Support — support@modelec.nl ‖ 📧 Bestellingen / Inkoopopdrachten — order@modelec.nl ‖ Galvanistraat 38, 6716 AE Ede · KvK 09079853
  > 来源：https://www.modelec.nl/contact/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-10-08_R66_R56_KP第20波50户.json`；价格均为 EXW 快照。

- **①背景再核**：MODELEC Data-Industrie B.V.(荷兰 Ede(Gelderland),Galvanistraat;**1977 创 49 年;21-50 人;「Your OT Network. Our Expertise」=OT 网络+网安专营(电网/水务/监狱/智能交通=KRITIS 守界加厚)**;**品牌谱 Moxa/Westermo/TXOne/Robustel;SPIE 站台自动化长期伙伴件**;**Contactinfo: Stefan Barten stefan@modelec.nl(SecurityDelta 伙伴页=O)+Bart Jan Witteveen bartjan@modelec.nl(Energy Storage NL+SPIE 案例件)+Sergio Alonso Owner(prospeo 谱)**
- **②芯片/型号**：(待谱面二补)
- **③KP 深挖**：**Stefan Barten(Contactinfo(伙伴页具名 stefan@modelec.nl +31 318-626262),official-self-published·谱/leads-only(直发需 opt-in));Bart Jan Witteveen(联络/案例件具名(bartjan@modelec.nl;SPIE 案例照件),official-self-published·谱/leads-only(直发需 opt-in));Sergio Alonso(Owner(业主谱),leads-only·待 opt-in(LinkedIn/谱面带核))**
- **④Saga 对标**：24 口 value PoE($180 USD EXW (2026-10-07, 15天有效))
- **⑤在乎与偏好**：OT/电网专营=最高守界

### R55 证据摘录（全部保留 · 含数量）

- **【决策链与对接人】**Contactinfo: Stefan Barten stefan@modelec.nl 0318-626262(SecurityDelta 伙伴页);Contact: Bart Jan Witteveen bartjan@modelec.nl(Energy Storage NL 会员页);案例件照: Bart Jan Witteveen(MODELEC)+SPIE 项目位;Owner: Sergio Alonso(prospeo 谱)
  > Contactinfo: Stefan Barten stefan@modelec.nl 0318-626262(SecurityDelta 伙伴页);Contact: Bart Jan Witteveen bartjan@modelec.nl(Energy Storage NL 会员页);案例件照: Bart Jan Witteveen(MODELEC)+SPIE 项目位;Owner: Sergio Alonso(prospeo 谱)
  > 来源：https://securitydelta.nl/partners/overview-partners/modelec
- **【联系方式与基础画像】**Ede, Gelderland;founded 1977;21-50 employees;+31 318 636262;**OT network & cybersecurity specialist for energy/utilities/water/penitentiary/traffic**;Partners: Moxa, Westermo, TXOne, Robustel(securitydelta/prospeo/psychiatrie 件)
  > Ede, Gelderland;founded 1977;21-50 employees;+31 318 636262;**OT network & cybersecurity specialist for energy/utilities/water/penitentiary/traffic**;Partners: Moxa, Westermo, TXOne, Robustel(securitydelta/prospeo/psychiatrie 件)
  > 来源：https://securitydelta.nl/partners/overview-partners/modelec
- **【近期动态与线索】**2025: SPIE×MODELEC 「Samen Sterk」站台自动化长期件(案例页);Energy Storage NL 网络安全 workshop Ede 主办谱(modelec.nl/energystoragenl 件)
  > 2025: SPIE×MODELEC 「Samen Sterk」站台自动化长期件(案例页);Energy Storage NL 网络安全 workshop Ede 主办谱(modelec.nl/energystoragenl 件)
  > 来源：https://www.modelec.nl/case/samen-sterk-modelec-en-spie-bundelen-hun-krachten-voor-de-lange-termijn/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：MODELEC Data-Industrie B.V.(荷兰 Ede(Gelderland),Galvanistraat;**1977 创 49 年;21-50 人;「Your OT Network. Our Expertise」=OT 网络+网安专营(电网/水务/监狱/智能交通=KRITIS 守界加厚)**;**品牌谱 Moxa/Westermo/TXOne/Robustel;SPIE 站台自动化长期伙伴件**;**Contactinfo: Stefan Barten stefan@modelec.nl(SecurityDelta 伙伴页=O)+Bart Jan Witteveen bartjan@modelec.nl(Energy Storage NL+SPIE 案例件)+Sergio Alonso Owner(prospeo 谱)**
- **产品线与在售品牌**：(波次二补谱面)
- **目标行业与场景**：荷兰 Ede 49 年 OT 网络网安屋(KRITIS)
- **团队与规模**：21-50 人;1977 创
- **决策链与对接人**：**Stefan Barten(Contactinfo(伙伴页具名 stefan@modelec.nl +31 318-626262),official-self-published·谱/leads-only(直发需 opt-in));Bart Jan Witteveen(联络/案例件具名(bartjan@modelec.nl;SPIE 案例照件),official-self-published·谱/leads-only(直发需 opt-in));Sergio Alonso(Owner(业主谱),leads-only·待 opt-in(LinkedIn/谱面带核))**
- **技术与认证**：(波次二补)
- **采购与供应链信号**：(波次二补)
- **近期动态与线索**：2026-10-08 R66 20 波谱名牌
- **与我方契合点**：24 口 value PoE 谱链窗口
- **风险与注意**：Stefan Barten 直达(opt-in 律;KRITIS 守界)

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Modelec 荷工业数据通信分销（Westermo 官方 where-to-buy 名录实锤）：替补窄位（$180 锚点一致）；官网 JS 重证据薄注 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：OT/电网专营=最高守界
- **W**：KRITIS 守界段
- **O**：Barten/Witteveen 联络直达位
- **T**：Moxa/Westermo 链谱

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
  - [ ] 硬件采购线在职者(波次二)
  - [ ] MikroTik 谱面份额

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Geachte heer Barten,

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-07, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?

Best regards,
Saga Networks Export Desk
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
