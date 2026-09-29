# Axbyte

> **评级 A**　|　瑞典 · Järfälla / Älvsjö　|　档案编号 `A-064`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-064
rating: A
country: 瑞典
biz_org: 公司/工作室（有官网）
business_model: 培训交付
decision_speed: moderate
price_sensitivity: medium
volume_potential: 2  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: true}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Axbyte 瑞典托管 datacom（自有 co-lo+外包 NOC）：NOC 监控集成 24 口 PoE（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Axbyte（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 瑞典 / Järfälla / Älvsjö | 事实 |
| 网站 | axbyte.se | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证顾问 公司内 2 人：Leo（瑞典 MikroTik 讲师）+ Fredrik Hellgren（MTCSWE） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 公司内 2 人：Leo（瑞典 MikroTik 讲师）+ Fredrik Hellgren（MTCSWE））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：leo@axbyte.se
  - 状态：既有/公开
- **电话**：+46 70 591 5987、+46 8 586 195 00
- **原始联系字段**：Leo +46 70 591 5987 / leo@axbyte.se；Fredrik Hellgren +46 8 586 195 00 / support@axbyte.se
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（机房接入层/客户站点）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：他的托管机房与客户站点互连都需要可靠接入层：24 口 PoE++ + 4×10G 上行，给他的「整体方案」做标准件候选。
- **要问的问题**：机房接入层现在标准化在什么型号上？
- **随附证明**：规格书 + MTBF/功耗数据 + 万兆上行实测（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（机房走道/远程点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：机柜走廊监控/AP、客户现场无空调弱电间：宽温 DIN 免配置，NOC 代维场景里最省心的一段。
- **要问的问题**：代维客户现场的零散 PoE 点位现在怎么处理？
- **随附证明**：宽温报告 + DIN 图 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（NOC 标准件 + 讲师实验台）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：双线：NOC 托管网统一 VLAN/ERPS 模板（固件标准化=省运维工时）；Leo 的讲师身份让设备进瑞典 MikroTik 课堂。
- **要问的问题**：Leo 的课用什么交换机型做演示？标准件名单要不要加一个实测候选？
- **随附证明**：VLAN/ERPS 模板 + CLI 速查 + 实验机成本价。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：斯德哥尔摩西南（Järfälla/Älvsjö）数据中心与网络服务商：办公室互连 + 自有服务器机房托管 + 外包 NOC，走「全包伙伴」路线。
- **产品线与在售品牌**：服务合同制（含硬件配套）：Datakom 方案、机柜托管、网络代维；CSV 名录显示 Leo 为瑞典 MikroTik 官方讲师、Fredrik Hellgren 持 MTCSWE。
- **目标行业与场景**：瑞典中小企业全包 IT/网络；机房托管客户的接入层与带外管理网。
- **团队与规模**：小型精干团队，愿景「瑞典本细分市场最好的数据通信服务」、承诺「blixtsnabb support」（极速支持）。
- **决策链与对接人**：Leo（21 年 MikroTik、SE 官方讲师，+46 70 591 5987 / leo@axbyte.se）与 Fredrik Hellgren（MTCSWE）；两人即全部技术决策。
- **技术与认证**：公司双人持证（讲师+MTCSWE，CSV 名录记录）——技术对话可以直接上 L2/L3 深层。
- **采购与供应链信号**：机房+NOC 模式=标准化 hardware stack 复购；官网明说要扩产品组合——正是递资料的好时候。
- **近期动态与线索**：「持续扩充产品组合」自述=供应商库在重整；抢在他确定新标准件前上门。
- **与我方契合点**：机房接入层/带外管理=24 口与 10G 机型；客户站点互连的室外/弱电点=工业件；讲师牌照=可以把我们设备带进课堂。
- **风险与注意**：他卖「品质与服务」不打价格战：首轮别报价，先给规格与实测建立技术信任。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网定位「整体数据通信方案商」：把客户的完整数据通信服务包下来做。
  > Helhetslösningar inom Datakom · Datakom-lösningar – förenklat. · Vi superladdar din Datakom-tjänst så du kan fokusera på det ditt företag gör bäst.
  > 来源：https://axbyte.se/
- **【产品线与在售品牌】**三条业务线：办公室/系统/站点互连、自建服务器机房托管、外包 NOC 运维监控——有机房就有持续网络设备需求。
  > Sammankoppling av kontor, system, platser, gamla som nya · Co-location — Ställ din egna server eller nätverksenhet i våra serverhallar… · NOC-tjänst — Vi hjälper ert företag med er Nätverksdrift och övervakning.
  > 来源：https://axbyte.se/
- **【近期动态与线索】**官网自述「一直在看如何扩充产品组合来满足客户」——产品线扩张窗口敞开。
  > Vi tittar hela tiden på hur vi kan utöka vår produktportfölj för att kunna erbjuda just det våra kunder eftersöker.
  > 来源：https://axbyte.se/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第7批.json`；价格均为 EXW 快照。

- **①背景再核**：瑞典托管 datacom（自有 co-lo+NOC）；内部讲师在册
- **②芯片/型号**：未公开（讲师 MikroTik 向）
- **③KP 深挖**：Leo 直达
- **④Saga 对标**：NOC 集成 24 口 PoE
- **⑤在乎与偏好**：监控友好/合同友好

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Co-location：Ställ din egna server eller nätverksenhet i våra serverhallar…NOC-tjänst：vi hjälper ert företag med er Nätverksdrift och övervakning”
  > “Co-location：Ställ din egna server eller nätverksenhet i våra serverhallar…NOC-tjänst：vi hjälper ert företag med er Nätverksdrift och övervakning”
  > 来源：https://axbyte.se/
- **【联系方式】**leo@axbyte.se +46 70 591 5987（CSV）；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > leo@axbyte.se +46 70 591 5987（CSV）；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://axbyte.se/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Axbyte 瑞典托管 datacom（自有 co-lo+外包 NOC）：NOC 监控集成 24 口 PoE（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：托管
- **W**：小
- **O**：代维接入
- **T**：大厂

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
| 决策人识别 | ❓ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] NOC 客户规模
  - [ ] 机柜规格
  - [ ] 教具现况

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Leo,

Co-location halls plus an outsourced NOC means Axbyte lives inside other people’s racks every single day.

We build a 24-port Gigabit PoE switch with full SNMPv3 and clean monitoring integration, sized for exactly the access layer in managed datacom setups. Reference: $165 USD EXW.

One question: in your NOC-managed racks, who supplies the access switches today?

If useful, I can send one unit with the SNMP documentation pack. If not a fit, one line and I close the loop.

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
