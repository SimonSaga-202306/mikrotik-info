# Katsariotis Dimitrios / IME

> **评级 A**　|　希腊 · Patra　|　档案编号 `A-025`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-025
rating: A
country: 希腊
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — IME 软件商交叉销售（imeFoodService 门店）：餐饮一盒网络 8 口 PoE；ΔΕΥΑ 水务市政段规避；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Katsariotis Dimitrios / IME（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 希腊 / Patra | 事实 |
| 网站 | ime.com.gr | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Katsariotis Dimitrios | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCSE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】IME Πληροφορική（帕特雷总部 Αγ. Διονυσίου 20-22 + 雅典分部 Θρασυμάχου 8）：自研商务软件公司（ΔΕΥΑ 水务计账、imeFoodService 餐饮点单、imeSales/imeRetail ERP/零售），Microsoft Certified/Gold Partner；CSV 口径 MikroTik 顾问 Katsariotis Dimitrios（MTCNA+MTCRE+MTCTCE+MTCSE 4 证）
- 【推断】软件商但手握餐饮/零售/水务客户群——其客户开店与门店网络改造时有接入层需求（类 A-020 交叉销售型）
- 【假设】imeFoodService 餐饮系统部署随带门店网络（AP/PoS 打印/客显）接入层 PoE 机会

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCSE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：dkats@ime.com.gr
  - 状态：既有/公开
- **电话**：+30 697 762 8291
- **原始联系字段**：+30 697 762 8291 / dkats@ime.com.gr
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Katsariotis Dimitrios**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：门店/站点标准包：24 口 PoE++ 一次配齐 AP、摄像头、POS 终端；远程看门狗让他们少跑门店。
- **要问的问题**：他们给连锁客户做门店网络时，接入层现在怎么配？
- **随附证明**：门店标准包报价单（交换机+AP+线材）+ 看门狗演示。

### 第 2 次跟进 · 工业级非管理 PoE（水厂/泵站）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：水务站点的户外柜：宽温宽压、DIN、免配置，停电恢复自动回到工作状态。
- **要问的问题**：水务/排水项目里有没有户外站点？
- **随附证明**：宽温报告 + 户外柜接线图 + 备件政策。

### 第 3 次跟进 · 管理型 PoE（多站点统一模板）

- **推什么**：STI-480DGGM（Saga） PoE 版（8G + 4×2.5G SFP）
- **切入点**：他们给同一客户维护几十个门店/站点：统一 VLAN 模板 + ERPS 冗余 + SNMP 监控，一套模板复制。
- **要问的问题**：多站点客户愿不愿意用统一交换模板运维？
- **随附证明**：配置模板 + SNMP/MIB 清单 + ERPS 实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：帕特雷的信息化公司 ΙΜΕ（软件开发为主：水务计费 ΔΕΥΑ、餐饮点单、门店零售 imeRetail，另做硬件与软件全支持），在雅典设第二办公室。
- **产品线与在售品牌**：以自研软件 + 配套硬件为主；网络方案按项目采购（顾问本人持 MikroTik 多证）。
- **目标行业与场景**：公共事业（水务/排水）、餐饮连锁、零售门店链——门店/站点分散、需要稳定的门店网络与实时数据回传。
- **团队与规模**：帕特雷 + 雅典两地办公；官网强调「全希腊合作伙伴网络 + 365 天支持」。
- **决策链与对接人**：Katsariotis Dimitrios（dkats@ime.com.gr；+30 697 762 8291）；公司总线 +30 2610 452363 / info@ime.com.gr。
- **技术与认证**：MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCSE，自述 20+ 年网络基础设施设计/实施/管理，专长明确含 **switching**。
- **采购与供应链信号**：软件公司的硬件随项目走：门店改造、水厂站点、客户机房升级；对「一次配齐 + 远程可维护」的设备接受度高。
- **近期动态与线索**：官网 2025 年更新（imeFoodService、ΔΕΥΑ 应用），位于帕特雷 Αγ. Διονυσίου 20–22 与雅典 Θρασυμάχου 8。
- **与我方契合点**：水务/门店场景 = 分散站点接入：24 口 PoE（门店/站点）、工业款（水厂/泵站现场）、管理型（多站点统一配置）。
- **风险与注意**：其公司主业是软件，网络采购量取决于项目；联系时直奔「门店/站点接入层」而不是大而全。

### R54 原文证据摘录（全部保留）

- **【业务定位】**公司自述：覆盖企业信息化全谱，硬件软件全支持，总部帕特雷、服务全希腊。
  > Καλύπτουμε όλο το φάσμα της Μηχανογράφησης-Μηχανοργάνωσης οποιασδήποτε μορφής επιχείρησης. Έχοντας έδρα την Πάτρα … πλήρεις υπηρεσίες υποστήριξης (Hardware και Software) σε όλη την Ελλάδα
  > 来源：https://ime.com.gr/
- **【目标行业与场景】**产品线即行业线索：水务、餐饮点单、零售连锁。
  > Εφαρμογές – ΔΕΥΑ（Πλήρης διαχείριση διαδικασιών ΔΕΥΑ）｜imeFoodService – Σύστημα παραγγελιοληψίας｜imeSales – Eμπορολογιστική Eφαρμογή｜imeRetail – λύση για αλυσίδες καταστημάτων
  > 来源：https://ime.com.gr/
- **【团队与规模】**两地办公与全国支持承诺。
  > Αγ. Διονυσίου 20 – 22, 262 23, Πάτρα｜Θρασυμάχου 8, 104 42, Αθήνα；365 ημέρες τον χρόνο υποστήριξη｜Πανελλαδικό δίκτυο συνεργατών
  > 来源：https://ime.com.gr/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第3批.json`；价格均为 EXW 快照。

- **①背景再核**：帕特雷自研软件四线（水务/餐饮/ERP/零售）+雅典分部；Microsoft Gold；365 日支持承诺
- **②芯片/型号**：软件为主；硬件伙伴墙未见
- **③KP 深挖**：Dimitrios Katsariotis（4 证顾问、Patra）唯一懂网 KP；dkats@ime.com.gr
- **④Saga 对标**：门店小盒 STC-28DGGPM 随餐饮系统交叉销售
- **⑤在乎与偏好**：随单打包、省心为先；非价格最敏感型

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Ανάπτυξη εξειδικευμένου λογισμικού…Εφαρμογές–ΔΕΥΑ/imeFoodService/imeSales/imeRetail”+“Microsoft certified/gold partner”牌
  > “Ανάπτυξη εξειδικευμένου λογισμικού…Εφαρμογές–ΔΕΥΑ/imeFoodService/imeSales/imeRetail”+“Microsoft certified/gold partner”牌
  > 来源：https://ime.com.gr/
- **【联系方式】**“Αγ. Διονυσίου 20–22, Πάτρα T:2610452363 / Θρασυμάχου 8, Αθήνα T:2114113700 / E: info@ime.com.gr”；MX=mail.ime.com.gr（MX/DNS 级核验：域存活=邮件可投递到域）
  > “Αγ. Διονυσίου 20–22, Πάτρα T:2610452363 / Θρασυμάχου 8, Αθήνα T:2114113700 / E: info@ime.com.gr”；MX=mail.ime.com.gr（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://ime.com.gr/
- **【技术与认证】**CSV 名录：Katsariotis Dimitrios MTCNA+MTCRE+MTCTCE+MTCSE（Patra）
  > CSV 名录：Katsariotis Dimitrios MTCNA+MTCRE+MTCTCE+MTCSE（Patra）
  > 来源：https://mikrotik.com/consultants

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：帕特雷自研商务软件商（水务计账/餐饮点单/ERP/零售四线），Microsoft Gold 伙伴
- **产品线与在售品牌**：自研软件 ΔΕΥΑ/imeFoodService/imeSales/imeRetail；硬件非主业
- **目标行业与场景**：餐饮门店/零售连锁/市政水务（ΔΕΥΑ 段涉公共，规避）
- **团队与规模**：双办公点（帕特雷+雅典）；365 日支持
- **决策链与对接人**：Dimitrios Katsariotis（顾问 4 证）为最懂网之人；info@ 通用口
- **技术与认证**：MTCNA+MTCRE+MTCTCE+MTCSE（个人）；Microsoft Gold
- **采购与供应链信号**：硬件偶发随项目采购
- **近期动态与线索**：2025-08 官网仍在更新产品页
- **与我方契合点**：餐饮/零售门店网络随单接入层 PoE（类 A-020 交叉销售）
- **风险与注意**：ΔΕΥΑ 水务=市政公共段，仅跟私营餐饮/零售线

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | IME 软件商交叉销售（imeFoodService 门店）：餐饮一盒网络 8 口 PoE；ΔΕΥΑ 水务市政段规避 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：餐饮/零售客户群在手
- **W**：硬件非主业
- **O**：餐饮数字化潮
- **T**：集成商截胡

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
  - [ ] 门店部署时交换机现供方
  - [ ] 打包意愿与加价结构
  - [ ] 单店 PoE 点位数

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Dimitrios,

I noticed you on the MikroTik consultant list (MTCNA/MTCRE/MTCTCE/MTCSE) and that IME ships imeFoodService across Greek restaurants.

We build a compact 8-port managed PoE switch that fits exactly the restaurant-in-a-box corner: order terminals, kitchen printers, customer displays and one AP on a single box. Reference: $99 USD EXW.

One question: when you deploy imeFoodService, who supplies the in-store switching today?

If useful, I can send one unit for evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

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

- **KP 领英直达**:[Dimitrios Katsariotis · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Dimitrios%20Katsariotis)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 低(政治摇摆、Cosco 比港;华为存量大);战术: 可正面谈中国产能/成本优势;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
