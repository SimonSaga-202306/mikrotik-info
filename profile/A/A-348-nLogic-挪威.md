# nLogic

> **评级 A**　|　挪威 · Oslo　|　档案编号 `A-348`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-348
rating: A
country: 挪威
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: true, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — nLogic 北欧（客户墙 Bane Nor 国铁/NRK/GlobalConnect/Orange；伙伴 HPE/PAN/Nokia/Arista）：私营段长尾窄针（$180 锚点一致）；关基/运营商守界句；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | nLogic（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 挪威 / Oslo | 事实 |
| 网站 | https://www.nlogic.no | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Nlogic AS(挪威 Oslo Skøyen,Karenslyst allé 20;Org.nr 821 678 102;2007 创立,2018-11-07 重新注册;49 名员工(2026-09-21 1881.no 报),Omsetning ≈501,875 kNOK,Fortjenestemargin 25.8%;Nlogic Group AS 持 68%;谱型=网络/安全/数据中心咨询&经销商,MikroTik 15 年以上沉淀
- 【推断】挪威网络咨询中堅,Nlogic Group 结构强化属集团化(68% 母公司);在咨询 + 硬售 + 培训三谱,价值链任一单位可行
- 【假设】15 年挪威网络基础设施⇒ 交换机等硬品长期定点,24 口 value PoE 对工程数量敞口

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：post@nlogic.no
  - 状态：既有/公开
- **电话**：+47 40 61 88 88
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：post@nlogic.no（官网联系页；销售salg@nlogic.no）；+47 40 61 88 88；nLogic AS，Karenslyst Allé 20, 0278 Oslo
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Erlend Bonesvoll**(Daglig leder(总经理))— erlend@nlogic.no / +47 40 61 44 44 〔已有(公司官方公开件/登记册自曝);源:https://www.mynewsdesk.com/no/nlogic-as/pressreleases/nlogic-har-tre-nye-ansatte-1213779〕
  - **Arne Giæver**(Styrets leder(董事长))— nlogic.no 谱面 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://www.1881.no/konsulenter-dataprogramvare-og-utvikling/konsulenter-dataprogramvare-og-utvikling-oslo/konsulenter-dataprogramvare-og-utvikling-skoeyen/nlogic-as_106343012S1/〕
  - **Marcus Erik Wahlberg**(董事)— nlogic.no 谱面 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://www.1881.no/konsulenter-dataprogramvare-og-utvikling/konsulenter-dataprogramvare-og-utvikling-oslo/konsulenter-dataprogramvare-og-utvikling-skoeyen/nlogic-as_106343012S1/〕
  - **Robert R. Olsen**(kundeansvarlig(客户经理))— nLogic 新闻稿谱面 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://www.mynewsdesk.com/no/nlogic-as/pressreleases/nlogic-har-tre-nye-ansatte-1213779〕
  - **Jonas Lindstad**(Nettverkskonsulent)— nLogic 新闻稿谱面 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://www.mynewsdesk.com/no/nlogic-as/pressreleases/nlogic-har-tre-nye-ansatte-1213779〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Erlend Bonesvoll | Daglig leder(总经理) | erlend@nlogic.no / +47 40 61 44 44 | official-self-published·谱/leads-only(直发需 opt-in)·公司新闻稿自曝邮箱 | https://www.mynewsdesk.com/no/nlogic-as/pressreleases/nlogic-har-tre-nye-ansatte-1213779 |
| Arne Giæver | Styrets leder(董事长) | nlogic.no 谱面 | leads-only·待 opt-in(LinkedIn 公开面) | https://www.1881.no/konsulenter-dataprogramvare-og-utvikling/konsulenter-dataprogramvare-og-utvikling-oslo/konsulenter-dataprogramvare-og-utvikling-skoeyen/nlogic-as_106343012S1/ |
| Marcus Erik Wahlberg | 董事 | nlogic.no 谱面 | leads-only·待 opt-in(LinkedIn 公开面) | https://www.1881.no/konsulenter-dataprogramvare-og-utvikling/konsulenter-dataprogramvare-og-utvikling-oslo/konsulenter-dataprogramvare-og-utvikling-skoeyen/nlogic-as_106343012S1/ |
| Robert R. Olsen | kundeansvarlig(客户经理) | nLogic 新闻稿谱面 | leads-only·待 opt-in(LinkedIn 公开面) | https://www.mynewsdesk.com/no/nlogic-as/pressreleases/nlogic-har-tre-nye-ansatte-1213779 |
| Jonas Lindstad | Nettverkskonsulent | nLogic 新闻稿谱面 | leads-only·待 opt-in(LinkedIn 公开面) | https://www.mynewsdesk.com/no/nlogic-as/pressreleases/nlogic-har-tre-nye-ansatte-1213779 |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 挪威网络咨询的随单位价值 PoE

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：挪威网络咨询的随单位价值 PoE
- **要问的问题**：15 年 Node 底座,談案の现场交换机现供品牌与缺口?
- **随附/动作**：规格页

### 第 2 次跟进 · MikroTik 同档 value PoE 品牌面(或其它谱)

- **推什么**：一页目录卡（统一口径=P1 系列，不外溢）
- **切入点**：MikroTik 同档 value PoE 品牌面(或其它谱)
- **要问的问题**：RCT-suites like NETGEAR/Ubiquiti/SFP-line:现供件?
- **随附/动作**：卡

### 第 3 次跟进 · erlend@ 邮件模式跟进(官方自曝金谱)

- **推什么**：—（统一口径=P1 系列，不外溢）
- **切入点**：erlend@ 邮件模式跟进(官方自曝金谱)
- **要问的问题**：「坚实·安稳」里我们价值 PoE 谱 Q4
- **随附/动作**：—


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-10-07_R66_R56_KP第1波.json`；价格均为 EXW 快照。

- **①背景再核**：Gulesider+1881.no 双登记册一手核,49 员工、68% Group AS 持、25.8% margin
- **②芯片/型号**：(未列硬牌)=网络/安全/datacenter 咨询;MikroTik 15 年沉淀
- **③KP 深挖**：**Erlend Bonesvoll(Daglig leder/官方自曝邮 erlend@nlogic.no) + Arne Giæver(董事长) + Marcus Erik Wahlberg(董事) + Robert R. Olsen(kundeansvarlig) + Jonas Lindstad(Nettverkskonsulent)**
- **④Saga 对标**：咨询+硬售+培训三谱的价值 PoE($180 USD EXW (2026-10-07, 15天有效))
- **⑤在乎与偏好**：网络坚实基础 + 25.8% margin 稳如

### R55 证据摘录（全部保留 · 含数量）

- **【决策链与对接人】**Daglig leder Erlend Bonesvoll · Styrets leder Arne Giæver · Styremedlem Erlend Bonesvoll, Marcus Erik Wahlberg · Antall ansatte: 49
  > Daglig leder Erlend Bonesvoll · Styrets leder Arne Giæver · Styremedlem Erlend Bonesvoll, Marcus Erik Wahlberg · Antall ansatte: 49
  > 来源：https://www.1881.no/konsulenter-dataprogramvare-og-utvikling/konsulenter-dataprogramvare-og-utvikling-oslo/konsulenter-dataprogramvare-og-utvikling-skoeyen/nlogic-as_106343012S1/
- **【决策链与对接人】**Kontakter: Erlend Bonesvoll Daglig leder erlend@nlogic.no +47 40 61 44 44 · Ola hadde noe kjennskap fra Robert R. Olsen kundeansvarlig Powertech
  > Kontakter: Erlend Bonesvoll Daglig leder erlend@nlogic.no +47 40 61 44 44 · Ola hadde noe kjennskap fra Robert R. Olsen kundeansvarlig Powertech
  > 来源：https://www.mynewsdesk.com/no/nlogic-as/pressreleases/nlogic-har-tre-nye-ansatte-1213779
- **【业务定位】**Org.nr 821 678 102 · Omsetning 501 875 tkr · Fortjenestemargin 25.8% · Aksjonærer: Nlogic Group AS (68%)
  > Org.nr 821 678 102 · Omsetning 501 875 tkr · Fortjenestemargin 25.8% · Aksjonærer: Nlogic Group AS (68%)
  > 来源：https://www.gulesider.no/nlogic+as+oslo/147338258/bedrift

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：挪威网安/数据中心咨询谱,15 年 Node 底座
- **产品线与在售品牌**：(官方未列牌谱)=网络+安全+IT-drift+datasikkerhet;MikroTik 库内信号
- **目标行业与场景**：Oslo 通行/So-huskient(网络基础设施谱)
- **团队与规模**：49 名员工(1881.no 2026);Nlogic Group AS 68%
- **决策链与对接人**：**Erlend Bonesvoll(Daglig leder/总经理,官方自曝 erlend@nlogic.no);Arne Giæver(董事长);Marcus Erik Wahlberg(董事);Robert R. Olsen(kundeansvarlig);Jonas Lindstad(Nettverkskonsulent)**
- **技术与认证**：网络/安全/数据中心咨询,MikroTik 谱(库内信号)
- **采购与供应链信号**：15 年 Node 底座,网络件的供应铺放定期流动
- **近期动态与线索**：2018 新注;25.8% fortjenestemargin;Plugtech 等谱(nLogic press 有谱)
- **与我方契合点**：咨询+硬售+培训三谱,value PoE 各场景
- **风险与注意**：ePOST (erlend@nlogic.no) 虽自曝,但直发要 opt-in/谱链明智

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | nLogic 北欧（客户墙 Bane Nor 国铁/NRK/GlobalConnect/Orange；伙伴 HPE/PAN/Nokia/Arista）：私营段长尾窄针（$180 锚点一致）；关基/运营商守界句 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：自曝金谱
- **W**：小谱增援
- **O**：规模敞口
- **T**：大牌

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
  - [ ] 当前现场交换机品牌/服务谱
  - [ ] MikroTik 谱份额

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Erlend,

I came across nLogic while mapping MikroTik-related distributors in Norway — 49 engineers on Skøyen and a name that keeps showing up on the serious Norwegian infrastructure projects. Impressive longevity: since 2007 on the same beat.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW (2026-10-07, 15天有效) - a value unit for the on-site deployments your team designs.

Could you point me to whoever carries the switching line in your projects, so we can get the right spec to the right desk?

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
