# CFI France

> **评级 A**　|　法国 · Saint-Ouen Cedex　|　档案编号 `A-327`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-327
rating: A
country: 法国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — CFI Groupe 法 Saint-Denis 知名多行业集成商（Éducation/Retail/Santé/Smart office/Smart city）：私营板块窄位（$180 锚点一致）；教育/智慧城市守界句；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | CFI France（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 法国 / Saint-Ouen Cedex | 事实 |
| 网站 | https://cfigroupe.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】CFI——Compagnie Française d'Informatique（法国 Saint-Denis Carré Pleyel）：多行业集成商——**Éducation**/Retail/**Santé**/Smart office/**Smart city**/Cybersécurité/IA;CSV=Allied Telesis Resell
- 【推断】法国知名多板块集成商：教育/智慧城市=公共段守界句；零售/智能办公/私营医疗段为私营主打
- 【假设】私营板块（零售/智慧办公/私营医疗）的 value 窄位

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：contact@cfigroupe.com
  - 状态：既有/公开
- **电话**：+33 1 70 94 90 91
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：contact@cfigroupe.com（官网联系页）；+33 1 70 94 90 91；AT名录地址为旧址Saint-Ouen，现址Saint-Denis Carré Pleyel
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 商业垂直（零售/办公）接入层一页

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：法语一封：零售连锁/商务办公项目的 24 口 PoE 接入层第二来源（门店复制梯价+RMA）；声明不涉公立教育/医疗/智慧城市垂直。
- **要问的问题**：商业垂直的接入层有第二来源位吗？
- **随附证明**：一页报价（法）。

### 第 2 次跟进 · 门店高密备件小批

- **推什么**：STI-280GE（Saga） 等小批
- **切入点**：连锁门店高部署密度场景的备件小批价。
- **要问的问题**：门店项目的备件有常备量吗？
- **随附证明**：小批价卡一页。

### 第 3 次跟进 · 价卡留档收口

- **推什么**：—（价卡留档）
- **切入点**：全品类价卡留档；无商业面回响即冻结。
- **要问的问题**：（无需回）价卡留档。
- **随附证明**：全品类一页价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第17批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：巴黎 CFI 集成商（教育/医疗/智慧城市公立三面划出；**零售+智能办公商业面可做**）。
- **产品线与在售品牌**：全谱集成+ORIA 产品+网络安全线。
- **目标行业与场景**：零售连锁/商务办公商业垂直（公立三面不涉）。
- **团队与规模**：中大型集成商（集团化各垂直页）。
- **决策链与对接人**：contact@cfigroupe.com（联系页，CSV 9-27）。
- **技术与认证**：Allied Resell（CSV 9-23 名录）。
- **采购与供应链信号**：零售门店群/商务楼宇项目的 24 口 PoE 接入层第二来源+门店高密备件。
- **近期动态与线索**：教育 2025 新版面=其公立面在发力，商业面窗口有限——语气简洁。
- **与我方契合点**：零售/办公 24 口 PoE+备件小批。
- **风险与注意**：公立教育/医疗/智慧城市标案一律不经由我们（首封明写）。

### R54 原文证据摘录（全部保留）

- **【业务定位】**巴黎城北 Carré Pleyel 的 CFI Groupe：解决方案集成商，主列垂直 **Éducation - Retail - Santé - Smart office - Smart city - Cybersécurité - IA**。
  > Intégrateur de solutions · Éducation - Retail - Santé - Smart office - Smart city - Cybersécurité - IA
  > 来源：https://cfigroupe.com/
- **【风险与注意】**垂直矩阵里 **Éducation/Santé/Smart city 三面以公立标案为主——该采购面完全划出**；只做 Retail 零售与 Smart office 商务办公等纯商业垂直面的设备生意。
  > （主导航）Education · Retail · Santé · Smart city · Smart office（其教育/医疗/智慧城市三块划出不涉）
  > 来源：https://cfigroupe.com/
- **【决策链与对接人】**contact@cfigroupe.com 官网联系页正文+01 70 94 90 91（CSV 9-27 official-company）；AT 名录现址已迁 Saint-Denis Carré Pleyel。
  > （CSV 2026-09-27 记录）cfigroupe 官网联系页给 contact@cfigroupe.com、+33 1 70 94 90 91；AT 名录地址为旧址 Saint-Ouen，现址 Saint-Denis Carré Pleyel
  > 来源：https://cfigroupe.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第33批.json`；价格均为 EXW 快照。

- **①背景再核**：FR 知名集成商（官网一手核）
- **②芯片/型号**：AT Resell
- **③KP 深挖**：contact@
- **④Saga 对标**：窄位（$180 锚点一致，低密）
- **⑤在乎与偏好**：品牌/合规

### R55 证据摘录（全部保留 · 含数量）

- **【目标行业】**Intégrateur de solutions——Éducation / Retail / Santé / Smart office / Smart city / Cybersécurité
  > Intégrateur de solutions——Éducation / Retail / Santé / Smart office / Smart city / Cybersécurité
  > 来源：https://cfigroupe.com

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：法国多行业集成商
- **产品线与在售品牌**：AT Resell（CSV）
- **目标行业与场景**：零售/智能办公/私营医疗（教育/智慧城市=守界注）
- **团队与规模**：中型+
- **决策链与对接人**：contact@ 口
- **技术与认证**：—
- **采购与供应链信号**：项目随单
- **近期动态与线索**：—
- **与我方契合点**：私营板块窄位（公共段守界句）
- **风险与注意**：公共段浓——守界句必压

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | CFI Groupe 法 Saint-Denis 知名多行业集成商（Éducation/Retail/Santé/Smart office/Smart city）：私营板块窄位（$180 锚点一致）；教育/智慧城市守界句 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：公共
- **O**：私营段
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
  - [ ] 替补机制
  - [ ] 占比

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Bonjour CFI team,

Compagnie Française d'Informatique - integrator across education, retail, healthcare, smart office and smart city. One boundary sentence: your education and smart-city engagements stay on their established public paths; this concerns the private boards only - retail, smart office, private healthcare.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW (2026-09-29) - a value tier for private projects where budget decides.

One question: on the private boards, does a documented value PoE tier exist?

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
