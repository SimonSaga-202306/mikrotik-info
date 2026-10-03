# GIS s.r.l.

> **评级 A**　|　意大利 · Pedrengo (BG)　|　档案编号 `A-200`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-200
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
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — GIS 安防 SI 集团 100 人：GDO/工业物流私段（$180 锚点一致）；公共/基建两段守界；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | GIS s.r.l.（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Pedrengo (BG) | 事实 |
| 网站 | https://gisimp.it | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】GIS s.r.l.（意大利，Hu.Tech Group 一部分，GIS+Tecnos 两公司 100 人集团）：**安防系统商**——security integrazita（风险分析/系统设计/安装/维保）；域线：videosorveglianza/antintrusione/controllo accessi/rivelazione incendio-EVAC/domotica e building automation/gestione e monitoraggio；行业四分：**Pubblico/Infrastrutture e trasporti（守界两段）+GDO 大零售/Industria e logistica（私营双段）**；Tecnos 姊妹做电气安装
- 【推断】100 人集团安防 SI+电气姊妹=随单大口径（同 GESA 族）；公共/基建运输两段守界，零售/工业物流双私段主打
- 【假设】“intelligenza umana”顾问式自述=方案导向销售，组件选择听工程判断

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：gis@gisimp.it
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：gis@gisimp.it [官网正文公开邮箱]; https://gisimp.it
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（商业 TVCC/门禁接入层；公共/EVAC 段划线）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：GDO/工业物流的 TVCC+门禁 IP 项目：24 口 PoE++ 接入层对照，声明公共与消防 EVAC 段不涉。
- **要问的问题**：TVCC/门禁项目的接入层现在配什么？（意/英材料包）
- **随附证明**：规格对照 + 一页报价 + 边界声明。

### 第 2 次跟进 · 工业级非管理 PoE（仓储/户外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：工业物流仓储与户外监控点位：宽温 DIN PoE+备件包。
- **要问的问题**：仓储/户外点位坏机率？
- **随附证明**：宽温报告 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（商业安防网分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：楼自动化/安防网分段标准件：VLAN/ERPS 模板进他设计库。
- **要问的问题**：安防网分段模板要不要进设计库？
- **随附证明**：VLAN/ERPS 模板 + 实测（意/英）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第10批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：贝加莫 Pedrengo 综合安全集成商（Hu.Tech 集团=GIS 安全+Tecnos 电气 100 人版），Allied Resell（CSV 记录）。⚠️ 火灾/EVAC 生命安全段与 Pubblico 公共段划线。
- **产品线与在售品牌**：TVCC/入侵/门禁/楼自动化/管理监控正路；火灾 EVAC 段不涉；电气姊妹司 Tecnos 一体。
- **目标行业与场景**：GDO 零售/工业物流/基础设施交通商业段（正路）；⚠️Pubblico 公共与消防 EVAC 段不碰。
- **团队与规模**：集团 100 人（2 司）。
- **决策链与对接人**：gis@gisimp.it（CSV 9-27：联系页明址 Pedrengo；集团层级——采购层级风险保留 CSV 口径）。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：TVCC/门禁/楼自动化 IP 化=PoE 接入层稳定消耗；GDO/工业物流大场景=室外/仓储工业件；集团架构=先 GIS 站点关系再谈集团。
- **近期动态与线索**：站体 2023 焕新+集团 hutechgroup.it 上线。
- **与我方契合点**：TVCC/门禁项目的 24 口与室外工业件；不碰 EVAC 联动与公共段。
- **风险与注意**：生命安全与公共段首节声明；勿跨司多头联系（Tecnos 电气线另走）。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网口号「Human intelligence for security development」：综合安全系统集成为本（风险分析→方案→设计→施工→售后五步）。
  > Progettiamo, realizziamo e gestiamo sistemi di sicurezza integrata ‖ Analisi del rischio · Proposta del sistema più adatto · Progettazione · Installazione · Servizio post-vendita
  > 来源：https://gisimp.it/
- **【产品线与在售品牌】**六类解决方案：视监（TVCC）/入侵报警/门禁/**⚠️火灾探测与 EVAC（生命安全段）**/家居与楼宇自动化/管理监控。
  > Videosorveglianza (TVCC) · Antintrusione · Controllo accessi · Rivelazione incendio – EVAC · Domotica e building automation · Gestione e monitoraggio
  > 来源：https://gisimp.it/
- **【团队与规模】**⚠️ Hu.Tech Group 架构：1 集团 2 司 100 名专业人员——GIS（安全）+Tecnos（电气）一体；行业含 **Pubblico** 公共段。
  > Un unico gruppo, due aziende — 1 gruppo, 2 aziende, 100 professionisti ‖ Hu.Tech Group unisce… GIS e Tecnos ‖ Settori: Pubblico · Infrastrutture e trasporti · GDO · Industria e logistica
  > 来源：https://gisimp.it/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第20批.json`；价格均为 EXW 快照。

- **①背景再核**：安防 SI 集团 100 人（公共/基建守界，GDO/工业物流私段）
- **②芯片/型号**：未明
- **③KP 深挖**：gis@
- **④Saga 对标**：零售/工业物流安防随单件（公共守界）
- **⑤在乎与偏好**：集成级文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Un unico gruppo, due aziende…100 professionisti…[settori:] Pubblico, Infrastrutture e trasporti, GDO, Industria e logistica…videosorveglianza, controllo accessi…”
  > “Un unico gruppo, due aziende…100 professionisti…[settori:] Pubblico, Infrastrutture e trasporti, GDO, Industria e logistica…videosorveglianza, controllo accessi…”
  > 来源：https://gisimp.it/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：意大利安防 SI 集团（GDO/工业物流私段）
- **产品线与在售品牌**：大牌体系
- **目标行业与场景**：GDO/工业物流（主）+公共/基建（守界）
- **团队与规模**：100 人两公司
- **决策链与对接人**：gis@ 口
- **技术与认证**：集成级
- **采购与供应链信号**：项目随单
- **近期动态与线索**：Hu.Tech Group 结构
- **与我方契合点**：零售/工业物流 PoE 安防随单 value 位
- **风险与注意**：公共基建两段

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | GIS 安防 SI 集团 100 人：GDO/工业物流私段（$180 锚点一致）；公共/基建两段守界 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：口径
- **W**：公共
- **O**：私段
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
  - [ ] 接入现供
  - [ ] 姊妹配套
  - [ ] 年项目量

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi GIS team,

One hundred professionals under Hu.Tech, designing integrated security for grocery retail and industrial logistics alike - every camera, badge reader and EVAC panel rides upstream on a PoE layer. (For clarity: your Pubblico and Infrastrutture/trasporti engagements stay fully out of scope here; this concerns the GDO and industrial-logistics segments only.)

We manufacture a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full integration documentation. Reference: $180 USD EXW - a value unit for the access layer inside your private-sector security projects.

One question: in your GDO and industrial-logistics installations, which switch brand holds the PoE access layer today - and would a documented value alternative earn a bench test?

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

---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:[GIS s.r.l · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=GIS%20s.r.l%20GIS%20s.r.l.)(搜索链接,点入后核职位再加;来源:档案名(个人档))
- **中国进口与管制**:国别档位 中(Golden Power 5G/能源延伸;企业交换机不受限);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
