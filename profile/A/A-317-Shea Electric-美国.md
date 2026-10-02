# Shea Electric

> **评级 A**　|　美国 · Oshkosh, WI　|　档案编号 `A-317`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-317
rating: A
country: 美国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Shea Electric 美 WI 工商电工承包商（CCTV/门禁/网络随单；CSV: N-Tron/Red Lion 渠道价差注）：项目 value PoE 随单正口（$165 锚点一致）；alt STI-288GP；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Shea Electric（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Oshkosh, WI | 事实 |
| 网站 | https://sheaelectricllc.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Shea Electric & Communications（美国威斯康星）：工商电气承包商——低压布线/商用网络/AV/EBCS/DAS（WiLS）/**安防（CCTV/门禁/入侵）**与消防报警；CSV=**N-Tron+Red Lion 工业交换渠道**（Anybus/Ewon 同墙，8 口非管理工业约 $500+ 同价位档快照注）
- 【推断】电工承包商连锁里罕见的工业网络渠道线：监控/门禁项目 PoE 消耗真实，随单正口；其工业价档揭价值杠杆
- 【假设】CCTV/门禁/网络项目 value PoE 随单正口（工业价差角度旁注）

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@sheaelectricllc.com
  - 状态：既有/公开
- **电话**：920-303-9380
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：info@sheaelectricllc.com（官网联系页）；920-303-9380；第三方项目页候选csheskey@sheaelectricllc.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · CCTV/低压项目 24 口 PoE 一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：英语一封：CCTV/门禁/通信网项目的 24 口 PoE 接入层（视频 VLAN 预设+交期承诺+备件），声明不涉消防报警链。
- **要问的问题**：安防/低压项目的接入层目前由谁供应？
- **随附证明**：一页报价（英）+ 交期表。

### 第 2 次跟进 · 弱电间备件小批

- **推什么**：STI-280GE（Saga） 等小批
- **切入点**：弱电间/吊顶点位的小批备件（含宽温位）。
- **要问的问题**：现场备件有没有常备需求？
- **随附证明**：小批价卡一页。

### 第 3 次跟进 · 价卡留档收口

- **推什么**：—（价卡留档）
- **切入点**：全品类价卡留档；无回复即冻结。
- **要问的问题**：（无需回）价卡留档。
- **随附证明**：全品类一页价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第16批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：威斯康星电气+低压全包承包商（CCTV/门禁/商务通信网是其网络件消耗面；消防链划出）。
- **产品线与在售品牌**：电气/低压/安防/消防四板块；Allied 谱系（CSV elioplus）。
- **目标行业与场景**：威斯康星工商楼宇。
- **团队与规模**：中型承包商（多板块事业）。
- **决策链与对接人**：info@sheaelectricllc.com（联系页，CSV 9-27）。
- **技术与认证**：（承包商职能型；Allied 谱系按 CSV）。
- **采购与供应链信号**：**CCTV/门禁/通信网项目的 24 口 PoE 接入层直购位**——电气承包商吃交期与备件。
- **近期动态与线索**：DAS/5G 布线业务扩张=弱电间接入件增量。
- **与我方契合点**：24 口监控 PoE+弱电间备件。
- **风险与注意**：消防报警链不涉；Focus on Energy 能源补贴项目面不经由我们。

### R54 原文证据摘录（全部保留）

- **【业务定位】**威斯康星 Oshkosh 的工商业电气承包商：电气（EV 桩/照明/NFPA 70B）+**低压布线（AV/商务通信网/DAS 5G）**+**商务安防（CCTV/门禁/入侵）**+消防报警（生命面划出）。
  > INDUSTRIAL AND COMMERCIAL ELECTRICAL CONTRACTORS ‖ Low Voltage Wiring — Custom design and build of computer networks and audio visual systems ‖ Business Security Systems — Camera, door control and intrusion systems
  > 来源：https://sheaelectricllc.com/
- **【风险与注意】**其 Business Fire Alarm Systems 板块=生命安全联动链——**首封声明该面不涉**，只做安防/低压通信网侧。
  > Business Fire Alarm Systems — Fire alarm and life safety installation（该板块划出）
  > 来源：https://sheaelectricllc.com/
- **【决策链与对接人】**info@sheaelectricllc.com 官网联系页正文+920-303-9380（CSV 9-27 official-company）；第三方 Focus on Energy 项目页 csheskey@ 为候选不主用。
  > （CSV 2026-09-27 记录）官网联系页给 info@sheaelectricllc.com、920-303-9380 与 Oshkosh Atlas Ave；official-company
  > 来源：https://sheaelectricllc.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第32批.json`；价格均为 EXW 快照。

- **①背景再核**：US WI 电工承包商（官网+CSV 双核）
- **②芯片/型号**：N-Tron/Red Lion
- **③KP 深挖**：info@
- **④Saga 对标**：随单正口（$165 锚点一致；STI 快照 $64 旁注）
- **⑤在乎与偏好**：本地响应/工程质量

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**Industrial And Commercial Electrical Contractors——Low Voltage Wiring/Communication Networks/CCTV/Access Control；CSV: N-Tron+Red Lion 渠道
  > Industrial And Commercial Electrical Contractors——Low Voltage Wiring/Communication Networks/CCTV/Access Control；CSV: N-Tron+Red Lion 渠道
  > 来源：https://sheaelectricllc.com

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：美国 WI 工商电气承包商
- **产品线与在售品牌**：N-Tron/Red Lion（CSV）
- **目标行业与场景**：工商楼宇/工厂
- **团队与规模**：区域承包商
- **决策链与对接人**：info@ 口
- **技术与认证**：—
- **采购与供应链信号**：项目随单
- **近期动态与线索**：—
- **与我方契合点**：CCTV/门禁/网络项目 PoE 随单正口+工业价差杠杆（STI-288GP alt）
- **风险与注意**：电工资质见重（标注）

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Shea Electric 美 WI 工商电工承包商（CCTV/门禁/网络随单；CSV: N-Tron/Red Lion 渠道价差注）：项目 value PoE 随单正口（$165 锚点一致）；alt STI-288GP |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：资质
- **O**：随单
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
| 决策人识别 | ❓ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 现供
  - [ ] 项目节奏

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Shea Electric team,

Electrical contracting with a real low-voltage side - business networks, CCTV, access control, DAS. Every camera run ends in a PoE switch; every door controller, too.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29). For the industrial side, our 8-port industrial PoE line is the natural comparison to the N-Tron and Red Lion class you channel - at a fraction of that price class, openly stated.

One question: where do the PoE switches behind your camera and access jobs come from today?

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

- **KP 领英直达**:[Shea Electric · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Shea%20Electric)(搜索链接,点入后核职位再加;来源:联络核验)
- **中国进口与管制**:国别档位 高(Covered List+SECURE Act+§301 关税;采购方警惕中国标签,话术锚 Marvell(美企)+FCC);战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
