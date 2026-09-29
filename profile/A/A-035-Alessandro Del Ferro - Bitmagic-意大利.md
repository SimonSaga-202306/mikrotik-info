# Alessandro Del Ferro / Bitmagic

> **评级 A**　|　意大利 · Pesaro　|　档案编号 `A-035`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-035
rating: A
country: 意大利
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
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Bitmagic 8 证休眠顾问：L2+ 特性表对话；先电话解冻再发信；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Alessandro Del Ferro / Bitmagic（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Pesaro | 事实 |
| 网站 | bitmagic.it | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Alessandro Del Ferro | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 8 证（含 MTCSWE+MTCEWE） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Bitmagic（Alessandro Del Ferro）：bitmagic.it 官网「Sito in costruzione」（休眠重建中）；CSV 载 MikroTik 顾问 8 证（含 MTCSWE+MTCEWE 双高阶）；Seeweb 托管邮箱存活
- 【推断】个人高级顾问休眠期或纯口碑接单：LinkedIn 外公开足迹弱
- 【假设】8 证集合=工程深度型，教具/实验室概念仍适用

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 8 证（含 MTCSWE+MTCEWE））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：mikrotik_consultant@bitmagic.it
  - 状态：既有/公开
- **电话**：+39 339 651 8864
- **原始联系字段**：+39 339 651 8864 / mikrotik_consultant@bitmagic.it
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Alessandro Del Ferro**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：他持 MTCSWE：直接给硬货（整机功率曲线、VLAN 上限、看门狗、端口隔离），请他自测后给结论。
- **要问的问题**：他近期项目的接入层规格（口数/功率/上行）通常怎么定？
- **随附证明**：完整规格 + 实测数据 + 30 天测试机。

### 第 2 次跟进 · 工业级非管理 PoE（现场点位）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：现场电箱/室外点位：宽温宽压、DIN、免配置；他的项目里非机房点位用得上。
- **要问的问题**：有没有需要装进电箱/室外的接入点？
- **随附证明**：宽温报告 + DIN 图 + 样品价。

### 第 3 次跟进 · 管理型 PoE（QoS/环网）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他持 MTCTCE（流量控制）：给 QoS/队列与 ERPS 的实测与模板，对上他的专长。
- **要问的问题**：他项目里 QoS 与环网冗余的需求多不多？
- **随附证明**：QoS 模板 + ERPS 实测 + MIB 清单。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：佩萨罗的网络顾问/集成个体（Bitmagic，Alessandro Del Ferro）：MikroTik 生态的项目实施与顾问。
- **产品线与在售品牌**：未取得（官网本轮为「Sito in costruzione」占位页）；按 CSV 记录其认证结构属 MikroTik 生态。
- **目标行业与场景**：按既有记录为中小型网络项目与顾问服务（站点重建中）。
- **团队与规模**：个人/极小型，决策链 = 本人。
- **决策链与对接人**：mikrotik_consultant@bitmagic.it；+39 339 651 8864。
- **技术与认证**：MikroTik 认证顾问 8 证，含 **MTCSWE（交换）+ MTCEWE（企业无线）+ MTCTCE（流量控制）**——交换是正式专长。
- **采购与供应链信号**：按项目采购；以技术参数为主要判据（MTCSWE 背景）。
- **近期动态与线索**：bitmagic.it 本轮实测为「Sito in costruzione」（建设中）占位页 → 站点改版中，业务内容暂不可见；首次联系时顺带确认。
- **与我方契合点**：MTCSWE 专长：可直接谈 VLAN/QoS/环网与转发实测；24 口 PoE 与工业款都有明确落点。
- **风险与注意**：公开信息少（仅名录 + 建设中的站点）→ 首封邮件以技术内容破冰，先建立信任不催单。

### R54 原文证据摘录（全部保留）

- **【近期动态与线索】**bitmagic.it 为建设中占位页（无业务内容）。
  > Sito in costruzione（bitmagic.it 首页）
  > 来源：https://www.bitmagic.it/
- **【技术与认证】**既有记录：8 证含交换与企业无线、流量控制专项。
  > 持 MTCSWE（交换）+ MTCEWE（企业无线）+ MTCTCE（流量控制）（CSV 备注）
  > 来源：https://www.bitmagic.it/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第4批.json`；价格均为 EXW 快照。

- **①背景再核**：8 证个人顾问；官网休眠重建中
- **②芯片/型号**：未公开
- **③KP 深挖**：Del Ferro 本人；Seeweb 邮箱存活
- **④Saga 对标**：L2+ 特性表对话 MTCSWE 人士
- **⑤在乎与偏好**：深度技术对话

### R55 证据摘录（全部保留 · 含数量）

- **【近期动态与线索】**bitmagic.it 首页仅“Sito in costruzione”
  > bitmagic.it 首页仅“Sito in costruzione”
  > 来源：https://www.bitmagic.it/index.html
- **【技术与认证】**CSV 名录：Alessandro Del Ferro 8 证（含 MTCSWE+MTCEWE）
  > CSV 名录：Alessandro Del Ferro 8 证（含 MTCSWE+MTCEWE）
  > 来源：https://mikrotik.com/consultants

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：个人 8 证 MikroTik 顾问（交换+企业无线双高阶）；站休眠
- **产品线与在售品牌**：咨询服务
- **目标行业与场景**：网络咨询（无线+交换双线）
- **团队与规模**：个人
- **决策链与对接人**：Del Ferro 本人
- **技术与认证**：MTCNA+…+MTCSWE+MTCEWE 8 证
- **采购与供应链信号**：未知（休眠）
- **近期动态与线索**：官网“Sito in costruzione”
- **与我方契合点**：交换专长人士对 L2+ 特性表敏感
- **风险与注意**：先电话/短信解冻再发信

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Bitmagic 8 证休眠顾问：L2+ 特性表对话；先电话解冻再发信 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：8证双高阶
- **W**：休眠
- **O**：MTCSWE 对口
- **T**：竞争顾问

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
  - [ ] 当前执业状态
  - [ ] 现用接入层
  - [ ] 评测意愿

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Alessandro,

I found you on the MikroTik consultant list - eight certifications including MTCSWE and MTCEWE is rare air.

Quick context: we build managed PoE switches with a full L2+ feature table (Voice VLAN, ERPS, watchdog). I would not pitch blind - your site says under construction, so I keep this short.

One question: are you currently taking on projects where the switching layer is open for alternatives?

If yes, I can send the full feature table and an evaluation unit. If not, one line and I close the loop.

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
