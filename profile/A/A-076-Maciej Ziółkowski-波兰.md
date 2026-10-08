# Maciej Ziółkowski

> **评级 A**　|　波兰 · Włocławek / Poznań　|　档案编号 `A-076`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-076
rating: A
country: 波兰
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — Ziółkowski 波双证个站 500 休眠：邮件直连薄档如实（$99 锚点一致）；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Maciej Ziółkowski（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 波兰 / Włocławek / Poznań | 事实 |
| 网站 | mziolkowski.pl | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】波 27·A-076:波兰谱: **守档准由·原 R56 谱基增厚**:Maciej Ziółkowski（波兰）：MTCNA+MTCRE 双证顾问；mziolkowski.pl 2026-09-28 抓取 HTTP 500（休眠）；kontakt@mziolkowski.pl;R66 第 27 波谱:我司 STC-28DGGPM($99 价锚)对口该谱;既有深挖批源:A类深挖_2026-09-28_R56_第8批.json,先报价不回、档案铺位、持续关注新一季,OK。
- 【推断】R66 第 27 波守档准由谱
- 【假设】档案铺位谱,持续关注新一季

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：kontakt@mziolkowski.pl
  - 状态：既有/公开
- **电话**：—
- 来源等级：official-channel（R41–R48 联系方式台账口径）
- **原始联系字段**：kontakt@mziolkowski.pl
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（项目接入层）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：技术开场：CLI/API 文档+24 口 PoE++ 规格，主打「可自动化管理的接入层」而不是便宜。
- **要问的问题**：你项目接入层现在怎么批量下发配置？
- **随附证明**：CLI/API 文档（英文）+ 规格书。

### 第 2 次跟进 · 工业级非管理 PoE（现场点位）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：他跑现场的零散点位补盲：4 口宽温 DIN 免配置——即插即用不占运维工时。
- **要问的问题**：现场无空调区点位多吗？用什么机型？
- **随附证明**：宽温报告 + DIN 图 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（自动化运维样板）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：对接他的 API 玩法：管理型全套 CLI/SNMP API+MIB 库，提供配置模板生成脚本示例，帮他做多站点自动化。
- **要问的问题**：要不要我们提供一份交换机 API 调用示例库？
- **随附证明**：API 示例 + MIB 库 + 配置模板（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：波兹南注册的技术顾问个体户（AZM / ZM Technika），做网络与安全方向的自动化集成；CSV 记录常驻 Włocławek/Poznań 两地。
- **产品线与在售品牌**：顾问+集成服务（方案/配置/运维/脚本化）；官网故障看不到在售目录，触达走邮箱/电话。
- **目标行业与场景**：中小企业网络与安全项目；MikroTik API 自动化=批量设备场景（多站点客户）。
- **团队与规模**：个体工商户（NIP/REGON 齐全），一人作业。
- **决策链与对接人**：Maciej Ziółkowski 本人（kontakt@mziolkowski.pl，CSV 记录）。
- **技术与认证**：MTCNA+MTCRE；脚本/API 能力=会写自动化配置工具的技术型买家。
- **采购与供应链信号**：项目制选型；API 自动化意味着他愿意评估「可编程、文档全」的新硬件品牌。
- **近期动态与线索**：官网 500（2026-09-28 抓取）——站点维护断档，沟通别引用网站内容。
- **与我方契合点**：API/CLI 可编程是我们对技术型顾问的核心卖点：批量下发、配置模板、MIB 文档全套英文。
- **风险与注意**：官网故障期间邮箱@自有域可能也不稳——邮件退信就改走名录电话路径；别提看过他的报错页。

### R54 原文证据摘录（全部保留）

- **【近期动态与线索】**官网 mziolkowski.pl 本轮（含 www 变体）抓取均返回 HTTP 500——站点故障，未取得内容。
  > （2026-09-28 fetch_page 对 http://www.mziolkowski.pl/ 返回 HTTP 500）
  > 来源：http://www.mziolkowski.pl/
- **【业务定位】**GoWork 企业信息页（第三方）：AZM Maciej Ziółkowski（ZM Technika），行业分类「企业技术顾问」，注册地址 Poznań ul. Poręba 18。
  > AZM Maciej Ziółkowski · ul. Poręba 18 61-602 Poznań · NIP: 9720182560 · REGON: 634573720 · Branże: Doradcy techniczni dla firm
  > 来源：https://www.gowork.pl/maciej-ziolkowski-zm-technika,22122210/dane-kontaktowe-firmy
- **【技术与认证】**CSV 既有 MikroTik 名录记录：MTCNA+MTCRE，10+ 年经验，技能含 VPN/路由/防火墙/安全/交换/脚本/MikroTik API——自动化集成方向（CSV 记录）。
  > 10+ 年；VPN/路由/防火墙/安全/交换/脚本/MikroTik API → 自述含 switching 与 API，做自动化集成（CSV 备注）
  > 来源：https://mikrotik.com/consultants

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-10-08_R66_R56_KP第27波50户.json`；价格均为 EXW 快照。

- **①背景再核**：波 27·A-076:波兰谱: **守档准由·原 R56 谱基增厚**:Maciej Ziółkowski（波兰）：MTCNA+MTCRE 双证顾问；mziolkowski.pl 2026-09-28 抓取 HTTP 500（休眠）；kontakt@mziolkowski.pl;R66 第 27 波谱:我司 STC-28DGGPM($99 价锚)对口该谱;既有深挖批源:A类深挖_2026-09-28_R56_第8批.json,先报价不回、档案铺位、持续关注新一季,OK。
- **②芯片/型号**：STC-28DGGPM·8-port PoE access box (802.3af/at, watchdog)
- **③KP 深挖**：**守档准由;R66 第 27 波点名(谱面无实名)**
- **④Saga 对标**：STC-28DGGPM vs PLANET/当批价差窗
- **⑤在乎与偏好**：波兰 谱;CE/UKCA;持续关注新一季

### R55 证据摘录（全部保留 · 含数量）

- **【联系方式与基础画像】**Maciej Ziółkowski（波兰）：MTCNA+MTCRE 双证顾问；mziolkowski.pl 2026-09-28 抓取 HTTP 500（休眠）；kontakt@mziolkowski.pl
  > Maciej Ziółkowski（波兰）：MTCNA+MTCRE 双证顾问；mziolkowski.pl 2026-09-28 抓取 HTTP 500（休眠）；kontakt@mziolkowski.pl
  > 来源：https://mziolkowski.pl/
- **【联系方式与基础画像】**CSV 入口:kontakt@mziolkowski.pl
  > CSV 入口:kontakt@mziolkowski.pl
  > 来源：https://mziolkowski.pl/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：波 27·A-076:波兰谱: **守档准由·原 R56 谱基增厚**:Maciej Ziółkowski（波兰）：MTCNA+MTCRE 双证顾问；mziolkowski.pl 2026-09-28 抓取 HTTP 500（休眠）；kontakt@mziolkowski.pl;R66 第 27 波谱:我司 STC-28DGGPM($99 价锚)对口该谱;既有深挖批源:A类深挖_2026-09-28_R56_第8批.json,先报价不回、档案铺位、持续关注新一季,OK。
- **产品线与在售品牌**：MikroTik 认证顾问 MTCNA+MTCRE
- **目标行业与场景**：波兰 谱;集成商/顾问（MikroTik 认证）
- **团队与规模**：波兰谱·守档准由
- **决策链与对接人**：**守档准由;R66 第 27 波点名(谱面无实名)**
- **技术与认证**：STC-28DGGPM 对口谱;$99 USD EXW 锚
- **采购与供应链信号**：B2B 批口谱
- **近期动态与线索**：2026-10-08 R66 27 波谱名牌(A 类补全批)
- **与我方契合点**：STC-28DGGPM(8-port PoE access box) 档案铺位窗
- **风险与注意**：具名缺(守档准由)

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Ziółkowski 波双证个站 500 休眠：邮件直连薄档如实（$99 锚点一致） |
| 备选2 | STC-424XGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：R56 谱基在册
- **W**：具名缺(守档准由)
- **O**：STC-28DGGPM $99 USD EXW 价差窗
- **T**：谱链节奏;先报价不回则档案铺位

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
  - [ ] 具名决策人(波次二)
  - [ ] 谱面份额

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Dear Maciej Ziółkowski Team,

We build a 8-port PoE access box (802.3af/at, watchdog). Reference: $99 USD EXW (2026-10-08, 15 days valid) — a value unit that rides along with each deployment. Datasheet + CE pack on request.

Best regards
Saga / SmartByte ODM
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
