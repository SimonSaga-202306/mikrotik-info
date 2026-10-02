# Fernando Trigueiro / Straznet

> **评级 A**　|　瑞典 · Kungsbacka　|　档案编号 `A-071`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-071
rating: A
country: 瑞典
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
- **为什么值得跟**：有明确交换/供电需求（交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Straznet 瑞南部 SMB 托管+SaaS 转轨：SMB 机柜 24 口 PoE 随单（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Fernando Trigueiro / Straznet（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 瑞典 / Kungsbacka | 事实 |
| 网站 | straznet.se | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Fernando Trigueiro | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCSE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Straznet（瑞典 Kungsbacka/哥德堡）：25 年经验 SMB IT 伙伴——外部 IT 部（单一支持号）、云（2026-06 上线自有 SaaS：Nextcloud+EuroOffice 致数据本地可控）、网络（安装/优化/排障/安全）、IT 安全审计；合作墙 Microsoft/Bitdefender/Synology/MikroTik；Fernando Trigueiro MTCNA+MTCSE；Peter Straznyk 博客常驻（AI 三阶段实务）
- 【推断】SMB 网络+存储（Synology）一线：客户机柜接入层随行；自有 SaaS 机房位为二轨
- 【假设】其 SMB 客户随单滚动+AI 实务博客显其处增长期

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCSE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@straznet.se
  - 状态：既有/公开
- **电话**：+46 300 307 80
- **原始联系字段**：+46 300 307 80 / info@straznet.se
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Fernando Trigueiro**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（外包客户现场接入）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：他给中小企业全包 IT：客户现场 AP/话机/监控一张网——24 口 PoE++ 做交付标配，帮他把「无忧 IT」的成本打下来。
- **要问的问题**：客户现场接入层现在标准化在什么型号？
- **随附证明**：规格对照 + 质保政策 + 到岸价目（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（仓储/车间客户）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：制造/仓储类客户的无空调区点位：宽温 DIN 免配置——他工具箱里的省心备件。
- **要问的问题**：工业类客户现场的交换故障多吗？用什么替换策略？
- **随附证明**：宽温报告 + DIN 图 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（SaaS 机房+客户标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：双线：他 SaaS 机房接入/带外管理段 + 外包客户网统一 VLAN/ERPS 模板——标准件思维对得上他的规模化打法。
- **要问的问题**：客户网的标准配置模板里接入层定型了吗？
- **随附证明**：VLAN/ERPS 模板 + CLI 速查 + 实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：哥德堡南的全包 IT 服务商：外包 IT 部门+云+网络+安全，正在从服务型升级为自有 SaaS 平台（NextCloud 系）。
- **产品线与在售品牌**：服务合同制；伙伴栈 Microsoft/Bitdefender/Synology/MikroTik——MikroTik 在其交付体系里有正式位置。
- **目标行业与场景**：Kungsbacka/哥德堡地区中小企业的整体 IT 外包；他自建 SaaS 的机房与交付客户现场都是交换场景。
- **团队与规模**：本地化公司团队（博客署名 Peter Straznyk 等），承诺全天候响应——服务密度高。
- **决策链与对接人**：Fernando Trigueiro（+46 300 307 80 / info@straznet.se，CSV 名录：MTCNA+MTCSE，近十年专做 MikroTik）。
- **技术与认证**：MTCNA+MTCSE + 20 年 IT 经验（CSV 记录）；自述专注 advanced routing、switching、network design。
- **采购与供应链信号**：外包模式=客户现场设备大包采购+自有 SaaS 机房设备——复购稳定；扩张期在评估新供应源。
- **近期动态与线索**：SaaS 转型（2026-06 官宣）+ AI 服务线（2026-08 博客）双线扩张——机房与交付量都在涨。
- **与我方契合点**：客户现场接入层=24 口 PoE；SaaS 机房接入/带外=10G 机型；交付工具箱=工业件备件。
- **风险与注意**：他重「服务品质」叙事：首轮给规格与质保承诺，别用低价冲锋抢占注意力。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网抬头：Kungsbacka 与哥德堡的 IT 伙伴，全天候（全年无休）专家支持。
  > IT-PARTNER I KUNGSBACKA OCH GÖTEBORG — Straznet är din IT-leverantör för snabb support, personlig service och bekymmersfri IT. Dygnet runt, alla dagar om året.
  > 来源：https://straznet.se/
- **【产品线与在售品牌】**四大板块：外包 IT 部门、云、网络（安装/优化/排障/安全）、IT 安全；合作伙伴栏挂 Microsoft/Bitdefender/Synology/MikroTik。
  > Extern IT-avdelning · Moln · Nätverk — Vi hjälper er med allt från installation och optimering till felsökning och säkerhet · IT-säkerhet（合作伙伴 Logo：Microsoft、Bitdefender、Synology、MikroTik）
  > 来源：https://straznet.se/
- **【近期动态与线索】**2026-06 官宣上线 NextCloud+EuroOffice 自有 SaaS（自述 25 年云与运维经验），转型正式 SaaS 公司——业务扩张期。
  > Nu tar vi på Straznet, med 25 års erfarenhet av molntjänster och driftsäkerhet, ett stort steg framåt: vi lanserar vår nya SaaS-lösning och blir ett fullfjädrat SaaS-företag.（2026-06-18 博客）
  > 来源：https://straznet.se/
- **【团队与规模】**办公点 Kabelgatan 5, 434 37 Kungsbacka；总机 0300-30 780 / info@straznet.se；AI 博客显示团队在跟新技术线。
  > Kabelgatan 5, 434 37, Kungsbacka · 0300-30 780 · info@straznet.se · 2026-08-07 — AI för företag – tre nivåer i praktiken（博客）
  > 来源：https://straznet.se/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第8批.json`；价格均为 EXW 快照。

- **①背景再核**：25 年 SMB 托管；2026-06 转 SaaS 公司
- **②芯片/型号**：MikroTik 合作在册
- **③KP 深挖**：Trigueiro+info@
- **④Saga 对标**：SMB 机柜 24 口
- **⑤在乎与偏好**：叽实文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Extern IT-avdelning…Nätverk…IT-säkerhet…partners Microsoft, Bitdefender, Synology, MikroTik”
  > “Extern IT-avdelning…Nätverk…IT-säkerhet…partners Microsoft, Bitdefender, Synology, MikroTik”
  > 来源：https://straznet.se/
- **【近期动态】**“Straznet lanserar NextCloud och EuroOffice…ett fullfjädrat SaaS-företag”（2026-06-18）
  > “Straznet lanserar NextCloud och EuroOffice…ett fullfjädrat SaaS-företag”（2026-06-18）
  > 来源：https://straznet.se/straznet-lanserar-nextcloud-och-eurooffice/
- **【联系方式】**info@straznet.se 0300-30 780；MX 自托管（MX/DNS 级核验：域存活=邮件可投递到域）
  > info@straznet.se 0300-30 780；MX 自托管（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://straznet.se/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：瑞南部 SMB IT 托管（外部 IT 部+云+网络+安全）
- **产品线与在售品牌**：Microsoft/Bitdefender/Synology/MikroTik
- **目标行业与场景**：哥德堡地区 SMB
- **团队与规模**：小中托管
- **决策链与对接人**：Trigueiro（MTCNA+MTCSE）+Straznyk
- **技术与认证**：MTCSE；25 年云经验
- **采购与供应链信号**：SMB 随行随单
- **近期动态与线索**：2026-06 Nextcloud+EuroOffice 自有 SaaS 上线
- **与我方契合点**：SMB 机柜 24 口 PoE 随行
- **风险与注意**：SMB 价敏

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Straznet 瑞南部 SMB 托管+SaaS 转轨：SMB 机柜 24 口 PoE 随单（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：粘性
- **W**：价敏
- **O**：机房
- **T**：大厂

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
  - [ ] 机柜量
  - [ ] 接入层现供
  - [ ] 滚动量

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Fernando,

An external-IT partner that just turned its cloud offering into a full SaaS stack knows what sits in a customer cabinet.

We build a 24-port Gigabit PoE switch (280W, 802.3af/at, Voice VLAN, watchdog) sized for exactly those SMB cabinets. Reference: $165 USD EXW.

One question: in your SMB network jobs, who supplies the access switching layer today?

If useful, I can send one unit with full documentation. If not a fit, one line and I close the loop.

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

- **KP 领英直达**:[Fernando Trigueiro · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Fernando%20Trigueiro)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 高(PTS 2020 全面禁华为 5G;政治偏冷);战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
