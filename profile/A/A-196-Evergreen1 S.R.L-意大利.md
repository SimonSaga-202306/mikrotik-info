# Evergreen1 S.R.L

> **评级 A**　|　意大利 · Ciampino (Roma)　|　档案编号 `A-196`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-196
rating: A
country: 意大利
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
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Evergreen1 目录电商（Esprinet 前端）：cablaggio 类目旁窄位低优先（$165 锚点一致）；MEPA 守界；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Evergreen1 S.R.L（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Ciampino (Roma) | 事实 |
| 网站 | https://www.evergreen1.it | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Evergreen1 S.R.L（意大利）：**目录式电商（智能手机/家电/电视/办公/电工耗材/cablaggio 耗材）+Pubblica Amministrazione 专页+mepa@ 专职邮箱**；其**目录供应链上游迹示 Esprinet**（商品图 imgrapido/fornitori/RCS/esprinet）=Esprinet 前端分销零售模型；ISO 认证
- 【推断】**上游 Esprinet 直连**——其议价链长、上架决定可能不在其手；其“antinfortunistica/cassetta”电工类旁的网络类目有 value 上架缝但带宽窄
- 【假设】MEPA 专职口=公共采购是其业务线（守界）；私营窄位=其 cablaggio/电工类目旁的 value 上架位，低优先

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：mepa@evergreen1.it
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：mepa@evergreen1.it [Publicly listed; delivery not tested]; https://www.evergreen1.it
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 供应商挂品提案（作为 B2B 供应商而非 PA 终端）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：按供应商注册路径敲门：公司资质+分销价目——24 口 PoE++ 与工业宽温件作其 B2B/仓储自用与商业客户类目件；声明不走 PA 终端项目。
- **要问的问题**：供应商注册的流程与资料清单怎么走？（资质随附）
- **随附证明**：公司资质包 + 分销价目 + 边界声明（意/英）。

### 第 2 次跟进 · 工业级非管理 PoE（仓储/运营自用件）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：仓储/物流运营自用的宽温工业件试单。
- **要问的问题**：仓储运营点位的交换自用有需求吗？
- **随附证明**：宽温报告 + 试单价。

### 第 3 次跟进 · 管理型 PoE（自用/商业客户分段简件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：自用机房与商业客户分段简件；挂品谈判顺推。
- **要问的问题**：自用/商业客户的分段模板要不要挂一套？
- **随附证明**：VLAN 速查卡 + 梯价。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第10批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：罗马 Ciampino 综合货商+公共行政供货专精：B2B 电商底盘+PA 项目盘，Allied Resell（CSV 记录）。⚠️ 公共项目段边界。
- **产品线与在售品牌**：全类目电商+PA 技术与服务供货（其上游=我们这类供应商的挂品渠道）。
- **目标行业与场景**：公共行政采购（他的下游=公共，⚠️我们不做终端公共项目）；内部仓储/办公 IT 与商业客户段可谈。
- **团队与规模**：中小货商（Natale 集团关联）。
- **决策链与对接人**：供应商行政 amministrazione@evergreen1.it（CSV 9-27：供应商入口）；mepa@ 只用在其程式的公共报价并非我方主通道。
- **技术与认证**：ISO 徽标（官网）；Allied Resell（CSV 记录）。
- **采购与供应链信号**：他作为 PA 供货商会从供应商目录拿货：现实空间=①我们作为其 B2B 挂品供应商（供应商注册流程）②他自用/仓储运营 IT 件；公共终端项目不直接供（首节边界）。
- **近期动态与线索**：电商促销横幅常态（手机/家电折扣）。
- **与我方契合点**：作他的「供应商」而非「客户的客户」：分销价目+供货条款按 B2B 挂品谈；运营自用件按 SMB 逻辑补。
- **风险与注意**：别去谈 PA 终端项目（公共程序与中标语境）；供应商注册走其 amministrazione 流程，一次给全资质。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网首页明写：**专精公共行政技术与服务供货**（Soluzioni per la Pubblica Amministrazione）——mepa@ 即其公共报价入口（CSV）。
  > Siamo specializzati nella fornitura di tecnologie e servizi innovativi per la Pubblica Amministrazione, con competenza e affidabilità.
  > 来源：https://www.evergreen1.it/
- **【产品线与在售品牌】**站体裁为全类目电商（手机/家电/办公/标识/电料/打印），带 ISO 徽标与 Natale 集团图——综合货商基因+B2B 公共盘。
  > （类目横贯）telefonia · elettrodomestici · monitor · notebook · cablaggio（utensili/etichettatrici）· stampanti laser inkjet ‖（首屏）ISO 徽标与 natale-e-logo 集团图
  > 来源：https://www.evergreen1.it/
- **【决策链与对接人】**CSV 9-27：mepa@ 为公共部门报价入口，**供应商行政另有 amministrazione@evergreen1.it**；不用 PEC 法律邮箱营销。
  > 官网明确这是公共部门报价入口，另有供应商行政入口 amministrazione@evergreen1.it；不使用 PEC 法律邮箱作为普通营销入口（CSV 2026-09-27 记录）
  > 来源：https://www.evergreen1.it/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第20批.json`；价格均为 EXW 快照。

- **①背景再核**：目录电商（Esprinet 前端+PA 专职口）
- **②芯片/型号**：目录全谱
- **③KP 深挖**：mepa@
- **④Saga 对标**：私营店线 value 缝（窄位低优先）
- **⑤在乎与偏好**：—

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Soluzioni per la Pubblica Amministrazione…[catalog categories:] cablaggio, elettricità, telefonia…[上游迹:] fornitori/RCS/esprinet（商品图源）”
  > “Soluzioni per la Pubblica Amministrazione…[catalog categories:] cablaggio, elettricità, telefonia…[上游迹:] fornitori/RCS/esprinet（商品图源）”
  > 来源：https://www.evergreen1.it/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：目录式电商（Esprinet 前端+PA 守界）
- **产品线与在售品牌**：目录全谱
- **目标行业与场景**：B2B2C+PA（守界）
- **团队与规模**：小型
- **决策链与对接人**：mepa@ 口
- **技术与认证**：ISO
- **采购与供应链信号**：下拉 Esprinet
- **近期动态与线索**：促 70% banner
- **与我方契合点**：cablaggio 类目旁 value 上架缝（窄位低优先）
- **风险与注意**：上游依赖

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Evergreen1 目录电商（Esprinet 前端）：cablaggio 类目旁窄位低优先（$165 锚点一致）；MEPA 守界 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：专职
- **W**：依赖
- **O**：缝
- **T**：议价

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
  - [ ] 上架决定权
  - [ ] 私营店线结构

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Evergreen1 team,

Your catalogue runs from dry appliances to cablaggio supplies, with a public-administration line running beside it. (To be explicit: your MEPA and PA engagements stay fully out of scope here; this concerns only your private B2B catalogue.)

We manufacture a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW - a documented value item that fits naturally beside your cablaggio categories.

One question: in your private B2B catalogue, is there room for a documented PoE access switch line - and where does the listing decision sit: with you, or upstream with your catalogue partner?

If useful, I can send one unit plus listing documentation. If not a fit, one line and I close the loop.

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

- **KP 领英直达**:[Evergreen1 S.R.L · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Evergreen1%20S.R.L)(搜索链接,点入后核职位再加;来源:档案名(个人档))
- **中国进口与管制**:国别档位 中(Golden Power 5G/能源延伸;企业交换机不受限);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
