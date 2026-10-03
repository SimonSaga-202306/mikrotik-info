# Pijl Solutions

> **评级 A**　|　荷兰 · Honselersdijk　|　档案编号 `A-221`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-221
rating: A
country: 荷兰
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
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Pijl 荷兰 SMB 远距托管：托管现场随单 value 口（$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Pijl Solutions（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 荷兰 / Honselersdijk | 事实 |
| 网站 | https://pijlsolutions.nl | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Pijl Solutions（荷兰 SMB 远距 ICT 服务商）：官网主打远程 IT 托管、安全稳定环境、WiFi 网络管理、Microsoft Copilot——面向中小企的一站式外包口
- 【推断】SMB 托管场景下交换机=随单件；其'安全稳定环境'叙事后端必含网络柜配套
- 【假设】托管客户扩容/换柜时的随单位网络件缺口

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@pijlsolutions.nl
  - 状态：待核·未验证投递（不进群发）
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@pijlsolutions.nl（官网正文公开；未验证投递）；原入口：见 alliedtelesis.com 伙伴页
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 呼应 WiFi 管理热题 + PoE 接入层

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：呼应其一月 WiFi 管理专题：托管 WiFi 背后要稳定的 PoE 接入层——24 口 PoE++ 一台覆盖一层/一仓。
- **要问的问题**：托管 WiFi/办公网项目的接入层现在配什么牌？
- **随附证明**：一页报价 + 规格要点（英/荷）。

### 第 2 次跟进 · 监控/门禁扩展位

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ 全万兆上联）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：摄像头/门禁类项目的高功率 PoE++ 余量与万兆上行版本。
- **要问的问题**：监控/门禁项目单点 30W~90W 供电需求多吗？
- **随附证明**：PoE 预算计算表 + 比牌一页（不偏提 Allied）。

### 第 3 次跟进 · 现场级宽温小件

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温 DIN）
- **切入点**：温室园艺/厂房现场环境的宽温非管理小件，Stocking 少量试样。
- **要问的问题**：周边温室/厂房现场有没有 -40~75°C 级需求？
- **随附证明**：宽温件一页 + CE/EMC 证书附件。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第12批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：荷兰 Westland 温室园艺腹地 Honselersdijk 的 SMB 托管 MSP：Allied Resell（CSV 记录）。
- **产品线与在售品牌**：方案三支柱：安全稳定 ICT 环境/高效协作/连接；WiFi 管理为内容主线。
- **目标行业与场景**：区域 SMB 托管项目：办公网/WiFi/监控；周边温室园艺设施可带现场级需求。
- **团队与规模**：小型托管团队（官网 2026-09 内容双更=活跃）。
- **决策链与对接人**：info@pijlsolutions.nl（官网联系页，CSV 9-27）；0174 766020。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：托管 MSP 模式=每开一个客户站点就要接入层件，走量稳但单小。
- **近期动态与线索**：2026-09-09 WiFi 管理新闻=首封可直接呼应的话题钩子。
- **与我方契合点**：托管 WiFi 项目的 PoE 接入层 24 口；温室/厂房周边的宽温小件。
- **风险与注意**：小 MSP 价格敏感：一页价卡+连带宽温件选项，勿长文。

### R54 原文证据摘录（全部保留）

- **【业务定位】**SMB 托管商自我定位「远程的你的 ICT 部门」——托管/外包型 IT 部门模式，接入层随托管项目走。
  > # Uw ICT-afdeling op afstand
  > 来源：https://pijlsolutions.nl/
- **【目标行业与场景】**三大方案支柱：安全稳定 ICT 环境 / 高效协作 / 保持在线连接——WiFi/网络在支柱内。
  > Veilige, stabiele ICT-omgeving · Efficiënt samenwerken · Verbonden zijn en blijven
  > 来源：https://pijlsolutions.nl/
- **【近期动态与线索】**新闻区 2026-09 双更（WiFi 管理专题+Copilot 技巧）=活跃内容窗口，WiFi 管理正是交换机对口话题。
  > 09/09/2026 — Wifi-beheer: waarom is een veilig en stabiel WiFi netwerk belangrijk? ‖ 23/09/2026 — Tip van de maand: Van Outlook-vlaggetje naar concrete taak met Copilot
  > 来源：https://pijlsolutions.nl/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第23批.json`；价格均为 EXW 快照。

- **①背景再核**：SMB 远程托管商（官网一手核）
- **②芯片/型号**：（无硬品牌证据）Microsoft
- **③KP 深挖**：info@
- **④Saga 对标**：随单位 value PoE（$180 锚点一致）
- **⑤在乎与偏好**：稳定/省心/单一接口

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**远程 ICT 托管/安全稳定环境/WiFi 管理/Copilot——SMB 一站式服务
  > 远程 ICT 托管/安全稳定环境/WiFi 管理/Copilot——SMB 一站式服务
  > 来源：https://pijlsolutions.nl

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：荷兰 SMB 远程 ICT 托管商
- **产品线与在售品牌**：（未明示硬品牌）Microsoft 栈
- **目标行业与场景**：SMB 办公现场/托管环境
- **团队与规模**：小型团队
- **决策链与对接人**：info@ 口
- **技术与认证**：Microsoft 生态叙事
- **采购与供应链信号**：随单夹带
- **近期动态与线索**：—
- **与我方契合点**：随单位 value PoE 口
- **风险与注意**：托管毛利率敏感、硬件非主角

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Pijl 荷兰 SMB 远距托管：托管现场随单 value 口（$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：托管粘性
- **W**：硬件弱
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
  - [ ] 托管体量
  - [ ] 现供硬件

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Pijl Solutions team,

Remote-managed IT, a safe and stable environment, WiFi management, and Copilot on top - a tight one-stop offer for Dutch SMBs. Behind every stable environment sits a network closet, and that is our corner.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $180 USD EXW (2026-09-29) - a value unit that rides along when a managed customer site needs switching.

One question: when a customer site needs switches, where do you source them today - and would a documented value PoE line earn a slot on your shelf?

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

- **KP 领英直达**:[Pijl Solutions · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Pijl%20Solutions)(搜索链接,点入后核职位再加;来源:联络核验)
- **中国进口与管制**:国别档位 中(NCSC 政府供应商排除;企业网自由);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
