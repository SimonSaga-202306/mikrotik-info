# Controller Service and Sales

> **评级 B**　|　美国　|　档案编号 `B-340`　|　优先级 ★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-340
rating: B
country: 美国
biz_org: 分销/批发商（有官网）
business_model: 分销 stocking
decision_speed: moderate
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-10-07
```

## SALES BRIEF（压缩模型）

- **是谁**：1926 创 100 年;Boston/Avon MA;O'Dea→O'Day 家族三代;service 起家→分销…
- **商业模式**：分销 stocking
- **为什么值得跟**：有信号（交换专长、工业/楼宇）但需先验证需求或联系人不具体
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — Moxa 授权老分销+在架千美元档：value DIN 轨 8 口（$74.8）入子位置最对口；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：你们的电柜项目里，那些非主环路的 PoE 点（视频/传感支线）现用什么 value 解决？
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Controller Service and Sales（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 | 事实 |
| 网站 | controllerservice.com | 事实 |
| 类型 | 分销（Moxa 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Moxa 授权分销商，Moxa SDS-3008 系列工业智能交换机用户手册扉页标注其为 Authorized Distributor | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | 1926 创 100 年;Boston/Avon MA;O'Dea→O'Day 家族三代;service 起家→分销 | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 电控/自动化/安全分销 90+ 线+turnkey 系统;PoE 24 口=控制柜/项目基建件 | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】波 R67/TUB·批9·B-340:美谱: **Controller Service & Sales Company, Inc. 深挖(controllerservice.com/aboutus+tedmag 百年通稿+leadiq 三源互证)**:**1926 创=整整 100 年(2026 百年庆,tedmag 通稿);创始 Matthew O'Dea(1899 生于 Stoughton MA,孤儿起奋;Wentworth Institute of Technology 1916 毕业→Cutler-Hammer 任职→1926 Boston Oliver Street 创);O'Day 家族 mid-1980s 接力=**第三代家族企业**;「Service Before Sales Since 1926」**;**业务=**新英格兰电气控制+工业自动化+安全产品首要分销商**:**电机控制/电路线保护/安全产品 90+ 产品线;授权分销=Cutler-Hammer/ABB/Idec 首批;最小组件→完整 turnkey 控制系统(设计/制造/工程/调试);根源=service 起家转分销;NAICS 3339;**11-50 员(37 员档记);+1-800-584-**** 谱口;Boston/Avon MA 谱**;**KP 金谱:Michael Murphy(President,zoominfo 档 P0)+Vance Smith(VP)+Joseph Lavallee(Senior Engineer)+Louis Guerra/John Trubiano(Account Mgr)+Gregg Jackman(Sales)+Cristina Cataldo(Service&Sales Controller)+Adrian Crooker(AP)+**Robert O'Day(tedmag 家族二代代表谱)**=8-9 人谱;$8.9M 营收估(zoominfo 单窗注)**;**谱位=百年三代家族电控/安全产品分销(90+ 线+turnkey 系统)=24 口 PoE 对控制盘柜/turnkey 系统基建谱口=批 9 美系金矿**。
- 【推断】R67/TUB 推土机深挖 批9 B 类既定十户
- 【假设】STC-424XGGPM-280W($165 USD EXW (2026-10-08, 15天有效))具名谱引路

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

电控/自动化/安全分销 90+ 线+turnkey 系统;PoE 24 口=控制柜/项目基建件

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@controllerservice.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：官网联系页
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Mark O'Day**(President(2005 至今,三代家族;祖父 1926 创立;Brown AB+Chicago MBA))— mark@controllerservice.com 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://www.dnb.com/business-directory/company-profiles.controller_service__sale〕
  - **Scott O'Day**(VP Sales and Marketing(兄弟共管))— scott@controllerservice.com 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://rocketreach.co/controller-service-sales-inc-management_b5fee96bf60669ae〕
  - **Jim Long**(Corporate Controller)— jim@controllerservice.com 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:同 RocketReach 源〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Mark O'Day | President(2005 至今,三代家族;祖父 1926 创立;Brown AB+Chicago MBA) | mark@controllerservice.com | guessed-leads-only(域 MX 存活;SMTP 未验;不进群发) | https://www.dnb.com/business-directory/company-profiles.controller_service__sale |
| Scott O'Day | VP Sales and Marketing(兄弟共管) | scott@controllerservice.com | guessed-leads-only(域 MX 存活;SMTP 未验;不进群发) | https://rocketreach.co/controller-service-sales-inc-management_b5fee96bf60669ae |
| Jim Long | Corporate Controller | jim@controllerservice.com | guessed-leads-only(域 MX 存活;SMTP 未验;不进群发) | 同 RocketReach 源 |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · Murphy President+Smith VP 双轨

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：President+VP → 24 口 PoE(turnkey 系统/控制柜基建)
- **要问的问题**：贵司 turnkey 系统线的 24 口 PoE 交换机集购由哪位同事主责?
- **随附/动作**：aboutus/tedmag 3 源

### 第 2 次跟进 · Lavallee Sr Engineer

- **推什么**：STI-288GPM/424（统一口径=P1 系列，不外溢）
- **切入点**：Senior Engineer=技术评估口
- **要问的问题**：贵司控制盘柜线的网络件谱口?
- **随附/动作**：leadiq 谱

### 第 3 次跟进 · O'Day 家族+Guerra/Trubiano

- **推什么**：STC-28DGGPM（统一口径=P1 系列，不外溢）
- **切入点**：家族三代+客户线谱
- **要问的问题**：贵司 90+ 产品线的供应商审核周期?
- **随附/动作**：


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-08**；原始记录：`batch/B类深挖_2026-10-08_R67_R56_推土机批9.json`；价格均为 EXW 快照。

- **背景深描**：1926 创 100 年;Boston/Avon MA;O'Dea→O'Day 家族三代;service 起家→分销
- **芯片与在用型号**：电控/自动化/安全分销 90+ 线+turnkey 系统;PoE 24 口=控制柜/项目基建件
- **关键人KP**：Michael Murphy(President)+Vance Smith(VP)+Joseph Lavallee(Sr Eng)+Guerra/Trubiano/Jackman/Cataldo/Crooker+Robert O'Day=9 人谱
- **关注点与资质**：美系百年分销 → 24 口 PoE(turnkey 系统基建+白牌辅位)
- **优缺点SWOT**：S=100 年三代+90+ 授权线+turnkey 系统能力·W=$8.9M 单窗估;家族决策人际谱·O=turnkey/控制柜 PoE 基建+新英制造业潮·T=ABB/Cutler-Hammer 授权轨道谱;关系型销售周期长
- **Saga产品适配**：STC-424XGGPM-280W 24 口 PoE($165 USD EXW,15 天有效):英谱;百年关系型信用;授权分销轨道;turnkey 项目节奏

### R55 证据摘录（全部保留 · 含数量）

- **【创史/产品官方档】**A 100 year old family-owned company and leading distributor of electrical control, industrial automation, and safety products;Since its founding in 1926;New England's premiere resource;Matthew O'Dea born 1899 Stoughton, orphan, Wentworth 1916→Cutler-Hammer→founded Controller Service & Sales in Boston in 1926;third generation business soon approaching our hundredth year;Service Before Sales Since 1926
  > A 100 year old family-owned company and leading distributor of electrical control, industrial automation, and safety products;Since its founding in 1926;New England's premiere resource;Matthew O'Dea born 1899 Stoughton, orphan, Wentworth 1916→Cutler-Hammer→founded Controller Service & Sales in Boston in 1926;third generation business soon approaching our hundredth year;Service Before Sales Since 1926
  > 来源：https://www.controllerservice.com/aboutus
- **【百年庆/二代档】**Controller Service & Sales Company, Inc., a third-generation distributor, is celebrating its 100th anniversary in 2026;Matthew O'Dea founded the company in 1926 in Boston on Oliver Street;founded as a service company→Cutler-Hammer first supplier→sales/distribution;in the mid-1980s, the O'Day family formally carried that legacy forward into its next generation;Robert O'Day
  > Controller Service & Sales Company, Inc., a third-generation distributor, is celebrating its 100th anniversary in 2026;Matthew O'Dea founded the company in 1926 in Boston on Oliver Street;founded as a service company→Cutler-Hammer first supplier→sales/distribution;in the mid-1980s, the O'Day family formally carried that legacy forward into its next generation;Robert O'Day
  > 来源：https://tedmag.com/controller-service-sales-celebrates-100-years/
- **【产品/规模档】**authorized distributor for Cutler-Hammer, ABB, and Idec;more than 90 product lines;component level to fully integrated turn-key control systems;Founded 1926;employees 11-50(37);NAICS 3339;Avon, Massachusetts;engineering and start-up service;can design and fabricate complete control systems;+1-800-584
  > authorized distributor for Cutler-Hammer, ABB, and Idec;more than 90 product lines;component level to fully integrated turn-key control systems;Founded 1926;employees 11-50(37);NAICS 3339;Avon, Massachusetts;engineering and start-up service;can design and fabricate complete control systems;+1-800-584
  > 来源：https://leadiq.com/c/controller-service--sales-inc/5a1d9d692300005c008d41c1

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Moxa 授权老分销+在架千美元档：value DIN 轨 8 口（$74.8）入子位置最对口 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S=100 年三代+90+ 授权线+turnkey 系统能力·W=$8.9M 单窗估;家族决策人际谱·O=turnkey/控制柜 PoE 基建+新英制造业潮·T=ABB/Cutler-Hammer 授权轨道谱;关系型销售周期长

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
  - [ ] MikroTik 谱位 controllerservice.com 在售线核
  - [ ] Murphy/Smith 直邮推档
  - [ ] $8.9M 营收 vs 37 员=人效注核验

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your line

```text
Dear Michael,\n\nWe build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) — a sturdy supply for control panels and turnkey control-system deployments across New England industry. Reference: $165 USD EXW (2026-10-08, 15 days valid). Datasheet + CE pack on request.\n\nBest regards\nSaga / SmartByte ODM
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
