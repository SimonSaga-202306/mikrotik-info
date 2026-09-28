# Westercom

> **评级 A**　|　捷克/斯洛伐克　|　档案编号 `A-044`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-044
rating: A
country: 捷克/斯洛伐克
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: true, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — Westercom 工业分销（Advantech EKI/Westermo）：EOL 替代场景低位温宽 PoE 补位不当对标（$74.8 锚点一致）；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Westercom（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 捷克/斯洛伐克 | 事实 |
| 网站 | westercom.eu | 事实 |
| 类型 | 分销（Westermo Silver） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Westermo, B+B SmartWorx | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Westermo, B+B SmartWorx）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：eshop@westercom.eu
  - 状态：既有/公开
- **电话**：+420 603 509 790、+420 607 550 014
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：+420 603 509 790 / eshop@westercom.eu（官网 /cs/kontakt 正文；站内另列 +420 607 550 014）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 PoE++（安防/轨道站台的商用段位补充）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他的工业线强项在苛刻场景，但 CVBS 级的站台/机房 24 口 PoE++ 段位他靠高价工业款硬填——用同规格对照把成本差摆上桌。
- **要问的问题**：站台/机房的常规 24 口 PoE 你们现在用哪个段位、价差敏感吗？
- **随附证明**：规格-价格对照表（英/捷）+ 宽温报告。

### 第 2 次跟进 · 工业非管理 PoE（变电站/轨旁箱体）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：对着他的变电站叙述切：DIN、宽温宽压、免配置单机型，能做他 Westermo 之外的第二来源试换。
- **要问的问题**：轨旁/变电站箱体设备你们的供货周期如何、是否需要第二来源备份？
- **随附证明**：一台测试机（-40~75°C）+ DIN 装配方案 + 反向防护说明。

### 第 3 次跟进 · 管理型 + 项目注册报价体系

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：建立项目联动机制：轨道交通/能源投标项目注册后，我们给直通报价与交期承诺，ERPS/冗余让方案对得上他们的技术标。
- **要问的问题**：下一个轨道交通/能源标什么时候开标、技术标里的冗余协议怎么写？
- **随附证明**：ERPS <50ms 收敛实测（英文）+ 项目注册与价格保护条款页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：捷克 Brno 的工业网络分销商（Westermo Silver 认证 + Advantech EKI 渠道），专做能源/铁路/制造/隧道等苛刻通信项目。
- **产品线与在售品牌**：Westermo（工业交换机/路由）、B+B SmartWorx 全线、Advantech（EKI 工业以太网/无风扇 IPC）、NVIDIA Jetson 边缘 AI——工业网络线最硬。
- **目标行业与场景**：变电站/配电网通信、铁路车载·站台·隧道、工厂自动化、水务、城市交通——全部 DIN/宽温场景。
- **团队与规模**：中型专业分销商（不详列人数）；技术选型服务是标准配置（Pomůžeme s výběrem…）。
- **决策链与对接人**：eshop@westercom.eu + +420 603 509 790；B2B 电商 + 项目报价双通道。
- **技术与认证**：Westermo Silver 伙伴（CSV 既有验证记录）；技术经理能逐条对规格。
- **采购与供应链信号**：同时背 Westermo 与 Advantech EKI 两套工业线——对「同一规格更便宜的第二来源」态度开放，尤其 PoE/宽温段位。
- **近期动态与线索**：2026 版首页改版为能源/铁路等场景插图 + Advantech 全线目录扩充——正在丰富工业通信类目。
- **与我方契合点**：我们做工业以太网源头厂：DIN/宽温/PoE 全段，能做他 Westermo 之外的性价比第二品线，并支持项目注册与价格保护。
- **风险与注意**：与 Westermo 关系是核心资产——首轮别攻击其主牌，主打「联合选型表 + 高性价比补位」。

### R54 原文证据摘录（全部保留）

- **【业务定位】**Westercom s.r.o. 定位为「苛刻工业场景」的工业通信与边缘基础设施供应商，支持选型、旧设备替换与项目供货。
  > Průmyslová komunikace a edge infrastruktura — Technologie pro náročné průmyslové provozy… Pomůžeme s výběrem vhodného typu, náhradou staršího zařízení i projektovou dodávkou.
  > 来源：https://www.westercom.eu/cs/
- **【目标行业与场景】**能源/关键基础设施板块明示工业交换机用于变电站、监控与配电基础设施。
  > Průmyslové switche, routery a synchronizace času pro rozvodny, dohled a distribuční infrastrukturu.
  > 来源：https://www.westercom.eu/cs/
- **【目标行业与场景】**铁路板块强调车载/轨旁/站台通信需耐振、宽温、冗余与长生命周期——正是 DIN/宽温交换机的目标市场。
  > Odolné switche, počítače a komunikační prvky pro vlaky, tratě, stanice a palubní systémy… vibrace, široké teplotní rozsahy, redundanci a dlouhý životní cyklus.
  > 来源：https://www.westercom.eu/cs/
- **【产品线与在售品牌】**产品树以 Advantech EKI（工业以太网）系列打头，含 EN50155 车载与轨旁控制器线。
  > EKI — prvky průmyslového Ethernetu… EN50155 Panel PC pro železniční aplikace… Řadič Wayside
  > 来源：https://www.westercom.eu/cs/37-produkty

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第5批.json`；价格均为 EXW 快照。

- **①背景再核**：工业通信分销（Advantech 全线+Westermo+B+B）；EOL 替代店招
- **②芯片/型号**：EKI/Westermo 工业以太网在册
- **③KP 深挖**：eshop@第一口；项目报价团队
- **④Saga 对标**：温宽 PoE 低价位补位（不当 Westermo 对标）
- **⑤在乎与偏好**：EU 现货/交期/生命周期承诺

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Průmyslová komunikace a edge infrastruktura…Nástupnické modely a alternativy za ukončené produktové řady / Projektové nabídky / Dostupnost v EU”
  > “Průmyslová komunikace a edge infrastruktura…Nástupnické modely a alternativy za ukončené produktové řady / Projektové nabídky / Dostupnost v EU”
  > 来源：https://www.westercom.eu/cs/
- **【产品线】**“ADAM – moduly pro sběr dat｜EKI — prvky průmyslového Ethernetu｜UNO/ARK”+CSV：Westermo, B+B SmartWorx
  > “ADAM – moduly pro sběr dat｜EKI — prvky průmyslového Ethernetu｜UNO/ARK”+CSV：Westermo, B+B SmartWorx
  > 来源：https://www.westercom.eu/cs/37-produkty
- **【目标行业】**“Energetika a kritická infrastruktura…Železnice a doprava…Výroba a automatizace…Vodárenství”
  > “Energetika a kritická infrastruktura…Železnice a doprava…Výroba a automatizace…Vodárenství”
  > 来源：https://www.westercom.eu/cs/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Westercom 工业分销（Advantech EKI/Westermo）：EOL 替代场景低位温宽 PoE 补位不当对标（$74.8 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：多垂直+EOL 店
- **W**：强牌已多
- **O**：EOL 补位
- **T**：公共壁垒

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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Westercom team,

I see Westercom takes EOL replacements seriously - "successor models and alternatives for discontinued series" is a service customers genuinely need.

We build industrial managed PoE switches rated -40 to 75C with a hardware PoE watchdog - positioned as a complement at a much lighter price point than the lines you carry. Reference: $74.8 USD EXW.

One question: in your EOL-replacement list, is there an open slot for an industrial PoE switch?

If useful, I can send one unit with the full test report. If not a fit, one line and I close the loop.

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
