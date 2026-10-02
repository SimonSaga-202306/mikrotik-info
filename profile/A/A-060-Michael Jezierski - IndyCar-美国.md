# Michael Jezierski / IndyCar

> **评级 A**　|　美国 · Indianapolis　|　档案编号 `A-060`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-060
rating: A
country: 美国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE、PoE/监控/门禁、组播/IPTV），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Jezierski INDYCAR 赛道技术：临时赛事网 PoE+现货直击大厂交期痛点（$165 锚点一致）；顾问身份接触；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Michael Jezierski / IndyCar（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Indianapolis | 事实 |
| 网站 | indycar.com | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Michael Jezierski | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCIPv6E+MTCSWE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Michael Jezierski（美国印第安纳波利斯）：NTT INDYCAR 系列赛 Technology Manager/System Engineer——赛道侧技术（计时计分网络、视频流/电信、车队网络服务）；自曝“给各赛车队配发 CCR1009”；吐槽大厂交期“Catalyst 带 PoE 近一年报价”；MikroTik 论坛常驻（2019 加入）；MTCNA+MTCRE+MTCIPv6E+MTCSWE
- 【推断】赛事网=每场临时搭建的移动机房：计时计分+车队视频/数据回传都吞 PoE（摄像/传感尾头）；大厂交期痛点=我们现货交期直击
- 【假设】US 赛事赛道网=高价值 showcase；从单场协商切入

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE+MTCIPv6E+MTCSWE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：mjezierski@indycar.com
  - 状态：既有/公开
- **电话**：+1 317 492 5005
- **原始联系字段**：+1 317 492 5005 / mjezierski@indycar.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Michael Jezierski**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 PoE++（Fan WiFi/监控的推荐档次）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：分站 Fan WiFi+监控接入层：24 口 PoE++ 一次到位，场地清单备件/到货可直接整箱——赛季收口时盘点他最敏感。
- **要问的问题**：分站现场 24 口 PoE 一般用哪个档位、现在留多少台备用？
- **随附证明**：功率实测表 + 与 CRS328-24P/UniFi 对照页（英文）。

### 第 2 次跟进 · 工业非管理 PoE（临时设施/移动机柜）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：临时设施的赛道旁+内场机柜：宽温宽压、DIN、免配置，随包随拆——拆装运输都轻。
- **要问的问题**：现场临时点位和机柜现在怎么供货、搭建期交期压到几天？
- **随附证明**：宽温报告 + DIN 安装图 + 备件包价格。

### 第 3 次跟进 · 管理型（IGMP 组播/ERPS 环）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：IP 视频/组播业务是他熟项：管理型 VLAN 分段+IGMP+ERPS 快速环——给方案文档面板到底，节省工时。
- **要问的问题**：席位/监控/计时网段是分开的吗？环网用什么协议做？
- **随附证明**：VLAN/ERPS/IGMP 配置模板 + ERPS 收敛实测（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：美国 IndyCar 赛事组织内（机构属性 Indianapolis Headquarters）：Michael Jezierski 是赛事方的 MikroTik 顾问，L2/L3、无线 LAN、PtP、IP 视频与组播 IP 是熟项。
- **产品线与在售品牌**：赛事内部采购＋车队外部顾问业务（私下购买路径双通道）。
- **目标行业与场景**：分站现场搭建：Fan WiFi/赛事内部 IPTV/监控/计时与数据传输/Timing equipment。
- **团队与规模**：IndyCar 是一家机构（赛事主办方）——技术、IOT、后勤多层级，他本人即可决定配置。
- **决策链与对接人**：Michael Jezierski（mjezierski@indycar.com / +1 317 492 5005）。
- **技术与认证**：MTCNA+MTCRE+MTCIPv6E+MTCSWE（CSV 既有 MikroTik 名录记录）；地气极熟。
- **采购与供应链信号**：分站现场临时设施在赛季前的搭建期集中采购——9 月 6 日收官战后进入盘点/封存阶段，休赛期正是补新件的窗口。
- **近期动态与线索**：赛季刚刚收官，设施/物料清单在盘点——现在进他的采购周期最好。
- **与我方契合点**：高密度 PoE++（Fan WiFi/监控）、工业宽温（室外临时机柜）、管理型（IGMP 组播视频、ERPS 快速环）——三点都好讲。
- **风险与注意**：他的主品牌体系固定（MikroTik 也同时给站台）——方案要从“现场临时设施里换算成本”维度切，别主诉品牌替代。

### R54 原文证据摘录（全部保留）

- **【近期动态与线索】**NTT INDYCAR SERIES 2026 赛季赛历完整收官：9 月 6 日 Laguna Seca 收官战（冠军 Scott McLaughlin）——赛季后基建改造窗口明开。
  > Sep 6 Laguna Seca — Scott McLaughlin
  > 来源：https://www.indycar.com/
- **【目标行业与场景】**2026 赛历从 3 月 1 日 St. Pete 至 9 月 6 日 17 站巡回——Street/Circuit/Superspeedway 三类现场都需要移动搭建网络与监控。
  > Mar 1 St. Petersburg · May 24 Indy 500 · Sep 6 Laguna Seca
  > 来源：https://www.indycar.com/
- **【技术与认证】**他（CSV 记录为 MikroTik 官方顾问）所在机构即 NTT INDYCAR SERIES 官方——权威主办的赛事组织（来源性质：机构官网）。
  > The Official Site of the NTT INDYCAR SERIES
  > 来源：https://www.indycar.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第6批.json`；价格均为 EXW 快照。

- **①背景再核**：INDYCAR 赛道技术总管；CCR1009 已车队配发；自诉大厂交期痛点
- **②芯片/型号**：CCR1009 在役
- **③KP 深挖**：本人直达+论坛 ID 互证
- **④Saga 对标**：临时赛事网 24 口 PoE+现货速度
- **⑤在乎与偏好**：可靠+速度+震动耐受

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Technology Manager - NTT INDYCAR Series…we issue the teams CCR1009s for network access”
  > “Technology Manager - NTT INDYCAR Series…we issue the teams CCR1009s for network access”
  > 来源：https://forum.mikrotik.com/viewtopic.php?t=187155
- **【近期动态】**“Our corporate IT was quoted almost a year from Big C on some Catalyst equipment with PoE”
  > “Our corporate IT was quoted almost a year from Big C on some Catalyst equipment with PoE”
  > 来源：https://forum.mikrotik.com/viewtopic.php?t=187155
- **【联系方式】**mjezierski@indycar.com +1 317 492 5005；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > mjezierski@indycar.com +1 317 492 5005；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://mikrotik.com/consultants

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：美国顶级赛车系列赛赛道技术总管（计时/视频/车队网）
- **产品线与在售品牌**：CCR1009 车队配发（论坛自证）
- **目标行业与场景**：赛事临时网/计时计分/视频回传
- **团队与规模**：赛事技术组
- **决策链与对接人**：Jezierski 本人
- **技术与认证**：MTCNA+MTCRE+MTCIPv6E+MTCSWE
- **采购与供应链信号**：赛务更迭高频采购；大厂交期痛点（自诉）
- **近期动态与线索**：2026 赛季在即；论坛吐槽交期待解
- **与我方契合点**：临时网 PoE 解锁+现货速度
- **风险与注意**：以顾问身份接触；品牌名头不外借

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Jezierski INDYCAR 赛道技术：临时赛事网 PoE+现货直击大厂交期痛点（$165 锚点一致）；顾问身份接触 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：痛点吻合
- **W**：制度未知
- **O**：赛季现窗
- **T**：大厂关系

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
  - [ ] 赛道 POE 现供
  - [ ] 采购通道
  - [ ] 评测时间窗

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Michael,

Your forum post about waiting a year for PoE switches while running CCR1009s on race weekends really landed - timing and scoring does not wait for vendor backlogs.

We build a 24-port Gigabit PoE switch (280W, 802.3af/at, hardware watchdog, ships from stock) sized for exactly the trackside timing, scoring and video-access pockets. Reference: $165 USD EXW.

One question: who supplies the PoE switching layer trackside today?

If useful, I can have an evaluation unit ready in days, not months. If not a fit, one line and I close the loop.

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

---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:[Michael Jezierski · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Michael%20Jezierski)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 高(Covered List+SECURE Act+§301 关税;采购方警惕中国标签,话术锚 Marvell(美企)+FCC);战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
