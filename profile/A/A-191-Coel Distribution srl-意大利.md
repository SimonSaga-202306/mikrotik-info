# Coel Distribution srl

> **评级 A**　|　意大利 · Muggiò　|　档案编号 `A-191`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-191
rating: A
country: 意大利
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
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Coel 弱电分销：Allied 实版旁 value 二线+Coel Cables 贴牌双通道（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Coel Distribution srl（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Muggiò | 事实 |
| 网站 | https://www.coeldistribution.it | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Coel Distribution srl（意大利）：**弱电/网络分销品牌墙实版**——R&M/Rosenberger/Datwyler/Legrand/Leviton/Prysmian/Acome/Beta Cavi 线缆系+Metz Connect/Nexconec/Optotecnika/OWL/Patchsee 连接系+**Allied Telesis（CSV 信号实锤在品牌页）**+Planet Networking/LevelOne/TP-Link Omada/Trend Networks 网络系+**Coel Cables 自有贴牌**+ITRack/HellermannTyton 配套
- 【推断】**CSV Allied 信号实锤+自有贴牌=双通道**：Allied 旁的 value 二线（公开上架）或 Coel Cables 式 ODM 贴牌（深度 ODM）
- 【假设】其品牌结构既有高端（Allied）也有中低品牌（Planet/LevelOne/Omada）——value 档位的“文档可靠件”有自然空档

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@coeldistribution.it
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@coeldistribution.it [Publicly listed; delivery not tested]; https://www.coeldistribution.it
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（缆旁高功率 PoE++ 补位）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：缆+交换联合 BOM 话术：24 口 PoE++ 当布线项目的大功率电源位——他平民线堆头薄的档位。
- **要问的问题**：布线项目的大功率 PoE++ 档位目录里有吗？（意/英）
- **随附证明**：类目档位分析 + 分销价目。

### 第 2 次跟进 · 工业级非管理 PoE（第二来源/价格带补位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他 Planet 工业线在：按第二来源+价格带补位谈宽温 DIN PoE，不争主锚。
- **要问的问题**：工业件有没有第二来源/更优价格带的需求？
- **随附证明**：价格带对照 + 宽温报告（意/英）。

### 第 3 次跟进 · 管理型 PoE（项目第二来源 SKU）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：管理型（ERPS/L3/10G）项目第二来源 SKU 上架评估。
- **要问的问题**：项目比价的第二来源管理件要不要评估？
- **随附证明**：VLAN/ERPS 速查 + 分销条款（意/英）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第10批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：蒙扎旁 Muggiò 布线与 IT 部件分销商：缆与无源件为骨、交换/视监为辅，Allied Resell（CSV 记录；品牌墙含 Allied 本体）。
- **产品线与在售品牌**：布线大厂牌+工具熔接+Allied/Planet/LevelOne 交换线+海康/GeoVision 视监线+自有 Coel Cables。
- **目标行业与场景**：北意安装商/数据中心项目方（B2B 分销正路）。
- **团队与规模**：中型专业分销。
- **决策链与对接人**：info@coeldistribution.it（CSV 9-27：联系页明细位）。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：他已经有 Allied+Planet（Planet 有工业宽温线）——直接对撞类目不可取；现实空间：①PoE++ 大功率商用接入层他的平民线堆头薄 ②单端口进价优势的第二来源 ③缆旁供电件的套装话术（缆+交换成套）。
- **近期动态与线索**：品牌墙 2026 年更新活跃（NTT AT/GeoVision/Shinho 2026 新上）。
- **与我方契合点**：缆旁供电件的套装逻辑：他卖缆，我们交换——联合 BOM 话术谈；或作高功率 PoE++ 补位 SKU。
- **风险与注意**：别硬顶其 Allied/Planet 锚位：以「缆旁补位/大功率空档」话术进入；先问类目经理缺什么档。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：IT 基础设施部件与系统分销商——品牌墙含 **Allied Telesis 本体**+Planet/LevelOne 平民交换系+海康/GeoVision 视监系。
  > componenti e sistemi per le infrastrutture tecnologiche nell'IT ‖（品牌墙）Allied Telesis · Planet Networking · LevelOne · Hikvision · GeoVision
  > 来源：https://www.coeldistribution.it/
- **【产品线与在售品牌】**布线主线厚：Prysmian/Datwyler/R&M/Rosenberger/Legrand/Leviton/Acome/Beta Cavi+工具（Klein/Trend Networks）与熔接（Shinho/Fujikura 系）——缆与无源件是骨。
  > （品牌墙）Prysmian Group · Datwyler · Reichle & De-Massari · Rosenberger · Legrand · Leviton · Acome · Beta Cavi · Klein Tools · Trend Networks · Shinho · Patchsee · NTT AT · Metz Connect · HellermannTyton
  > 来源：https://www.coeldistribution.it/
- **【决策链与对接人】**CSV 9-27：联系页明确列 Muggiò 地址/税号/邮箱；第三方聚合站误置印度不采用。
  > 官网联系页明确列出 Muggiò 地址、税号及邮箱；第三方聚合站把本公司误放印度，不采用其信息（CSV 2026-09-27 记录）
  > 来源：https://www.coeldistribution.it/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第20批.json`；价格均为 EXW 快照。

- **①背景再核**：弱电分销（30 牌+自贴牌+Allied 实版）
- **②芯片/型号**：Allied/Planet/LevelOne/Omada 实版
- **③KP 深挖**：info@
- **④Saga 对标**：value 二线+ODM 贴牌双通道
- **⑤在乎与偏好**：分销文档+对照

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“[brands:] Allied Telesis, Planet Networking, LevelOne, Omada by TP-Link, Metz Connect…Coel Cables[自有贴牌]…componenti e sistemi per le infrastrutture tecnologiche nell’IT”
  > “[brands:] Allied Telesis, Planet Networking, LevelOne, Omada by TP-Link, Metz Connect…Coel Cables[自有贴牌]…componenti e sistemi per le infrastrutture tecnologiche nell’IT”
  > 来源：https://www.coeldistribution.it/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：意大利弱电网络分销（自贴牌+Allied）
- **产品线与在售品牌**：约 30 品牌+Coel Cables
- **目标行业与场景**：安装商/集成商客户群
- **团队与规模**：分销中型
- **决策链与对接人**：info@ 口
- **技术与认证**：品牌级
- **采购与供应链信号**：分销目录
- **近期动态与线索**：Metz Connect 2026 新加
- **与我方契合点**：Allied 旁 value 二线+ODM 贴牌双通道
- **风险与注意**：Allied 同盟

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Coel 弱电分销：Allied 实版旁 value 二线+Coel Cables 贴牌双通道（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：贴牌
- **W**：同盟
- **O**：二线
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
  - [ ] value 档缝
  - [ ] 贴牌深度
  - [ ] 分销结构

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Coel Distribution team,

Your brands page reads like a catalog of everything an installer needs - Allied Telesis at the top end, Planet and LevelOne at the practical end, and your own Coel Cables proving you know the private-label logic from the inside.

We manufacture a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW - a documented value layer for exactly the middle tier between Allied and Planet.

One question: is there room in your networking assortment for a documented value PoE access line - open Saga brand, or under a private label like Coel Cables, whichever model fits your house?

If useful, I can send a sample unit with the complete distribution pack. If not a fit, one line and I close the loop.

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
