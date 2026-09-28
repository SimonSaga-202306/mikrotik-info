# Zorn Elektrik GmbH

> **评级 A**　|　德国 · Korntal-Münchingen　|　档案编号 `A-186`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-186
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 主场景匹配+首触只推一个型号的纪律；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Zorn Elektrik GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Korntal-Münchingen | 事实 |
| 网站 | https://www.zorn-elektrik.de | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@zorn-elektrik.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@zorn-elektrik.de [Publicly listed; delivery not tested]; https://www.zorn-elektrik.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（楼宇数据配套接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：一句话敲门：楼宇数据/监控配套的 24 口 PoE++ 一页报价。
- **要问的问题**：楼宇项目的数据/监控供电交换怎么配？报价发您。
- **随附证明**：一页报价 + 规格要点（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（竖井/车库点位）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：竖井/车库小点位：4 口宽温小机试单价。
- **要问的问题**：竖井/车库点位的小交换用什么？
- **随附证明**：宽温报告 + 试单价（德文）。

### 第 3 次跟进 · 管理型 PoE（大点项目的分段简件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：大点楼宇项目的分段简件：VLAN 速查一张。
- **要问的问题**：大点项目的网分段模板要不要？
- **随附证明**：VLAN 速查卡（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第10批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：路德维希堡旁 Korntal-Münchingen 本地电气承包商：楼宇电气+配电柜施工，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：电气安装/配电柜/楼宇电气（官网图注口径）。
- **目标行业与场景**：区域楼宇电气项目；数据/弱电配套段。
- **团队与规模**：小型本地店。
- **决策链与对接人**：info@zorn-elektrik.de（CSV 9-27：联系页明文）。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：小电气店：项目里数据技术配套的接入层件偶发——给一页报价+挂靠价快。
- **近期动态与线索**：站点 2017-2020 版式（静态运营，电话文化）。
- **与我方契合点**：楼宇数据配套的 24 口与小机位。
- **风险与注意**：站薄说明轻线上——邮件简短一句+附件报价，或先电话；别塞长文档。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网首页极简：轮播图即主业自述——脚手架施工/配电柜/楼宇外景——典型本地电气承包商站。
  > （首页轮播图题注文件）slider_steiger_zorn_elektrik（施工）· Slider_schaltschrank_zorn_elektrik（配电柜）· slider_gebaeude_zorn_elektrik（楼宇）‖ 仅声明"本网站仅使用功能必需 Cookie"（页面正文极薄）
  > 来源：https://www.zorn-elektrik.de/
- **【决策链与对接人】**CSV 9-27：联系页公开 info@zorn-elektrik.de 且 Korntal-Münchingen 地址匹配——本地店作风。
  > 官网联系页明文邮箱，Korntal-Münchingen 地址匹配（CSV 2026-09-27 记录，源 zorn-elektrik.de/kontakt/）
  > 来源：https://www.zorn-elektrik.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第19批.json`；价格均为 EXW 快照。

- **①背景再核**：1971 电工承包（控制柜自制+IKT 双证）
- **②芯片/型号**：未明
- **③KP 深挖**：info@+Othmar Zorn 具名
- **④Saga 对标**：楼宇弱电随单 value 件
- **⑤在乎与偏好**：Augenhöhe 文化

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Als kompetentes Dienstleistungsunternehmen im Elektrohandwerk…seit 1971…50 Jahre Zorn Elektrik GmbH…[Schaltschrankbau]+[Gebäude- und Elektrotechnik]”（滑片+官网新闻存档）
  > “Als kompetentes Dienstleistungsunternehmen im Elektrohandwerk…seit 1971…50 Jahre Zorn Elektrik GmbH…[Schaltschrankbau]+[Gebäude- und Elektrotechnik]”（滑片+官网新闻存档）
  > 来源：https://www.zorn-elektrik.de/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：老牌
- **W**：薄证
- **O**：随单
- **T**：在位

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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Mr. Zorn,

Fifty years of electrical craftsmanship, control cabinets built in-house, and an IKT ticket on the trade register - a company that has seen technology cycles come and go and still works at eye level.

We manufacture a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with honest documentation. Reference: $165 USD EXW - a value unit for the network layer inside your building and cabinet projects.

One question: in your building and cabinet projects, which switch brand currently supplies the network side - and would a documented value alternative be worth a bench test for your team?

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

*建档日期：2026-09-22　|　结构 v2：2026-09-28（R56 规则）　|　数据来源：客户名单_反向信号_2026-09.csv + R54/R55 调研 JSON*
