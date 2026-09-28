# CSI S.A.

> **评级 A**　|　波兰　|　档案编号 `A-047`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-047
rating: A
country: 波兰
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — 主场景匹配+首触只推一个型号的纪律；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | CSI S.A.（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 波兰 | 事实 |
| 网站 | csi.pl | 事实 |
| 类型 | 分销（Antaira 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Antaira | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Antaira）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：kontakt@csi.pl
  - 状态：既有/公开
- **电话**：+48 12 390 61 80
- **原始联系字段**：+48 12 390 61 80 / kontakt@csi.pl
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 PoE++（安防/Digital Signage 商用段）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他安防与 Digital Signage 客户量大：24 口 PoE++ 作为其工业线之外的商用段位补位——对标 TP-Link/Netgear 价位，品类经理一看就懂。
- **要问的问题**：安防线的 24 口 PoE 现状是分销 TP/Netgear 类、毛利受到挤压吗？
- **随附证明**：英文规格-价格对比表（对标主力段位）+ 测试机政策。

### 第 2 次跟进 · 工业非管理 PoE（交通/能源柜）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：能源与轨道交通客户的箱体供电：DIN、宽温宽压、免配置，Antaira 之外的第二来源备份。
- **要问的问题**：工业线对只差一级的低价二供态度如何？
- **随附证明**：宽温报告 + DIN 安装图 + 温度循环测试数据（英文）。

### 第 3 次跟进 · 管理型 + 品类上架与项目报价

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：给他通信品类加一档：管理型 PoE+10G、ERPS、双电源——随他的渠道流进能源/轨道标的采购；谈价格保护与项目注册。
- **要问的问题**：能源标里的冗余/管理面参数能否对上你方售卖段位？
- **随附证明**：ERPS 收敛实测（英文）+ 项目注册条款 + 两年供货承诺函。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Kraków 头部工控分销商（上市公司级体量），Antaira 授权分销（CSV 验证）；工业通信类目显性、轨道交通客户背书。
- **产品线与在售品牌**：工业计算机/工控机箱/Industrial Flash/Rugged 计算/工业通信（Antaira 等）/消费类电子（独立部门），工程型分销。
- **目标行业与场景**：工厂自动化、轨道交通、物流、能源、数字标牌、安防、AI 边缘计算——全是 PoE/工业交换机目标场景。
- **团队与规模**：大型分销：销售/技术支持/物流分层；采购按品类经理分工。
- **决策链与对接人**：kontakt@csi.pl / +48 12 390 61 80；通信品类经理是决策点（R37 策略：找品类经理不找 CPO）。
- **技术与认证**：Antaira 官方授权分销（CSV 既有验证）；ISO 体系与行业奖项（Gazele Biznesu/Diamenty Forbesa 等）。
- **采购与供应链信号**：已经有工业交换机线（Antaira），意味着他对品类成本结构一清二楚；二供空间在工业非管理与管理入门款——价格敏感且量足够。
- **近期动态与线索**：9 月同时出展 MSPO（防务）/ENERGETAB（能源）/TEK.day——能源与轨道交通客户集中，新品上架窗口。
- **与我方契合点**：源头厂的 DIN/宽温/PoE 全段位 + 价格带优势：做他 Antaira 之外的工程采购第二来源；他做轨道交通——ERPS/双电源管理型是对路品。
- **风险与注意**：大分销流程正式：第一封信就要是「品类经理信」格式——规格对比表+价格带 + 测试机政策，不要营销腔。

### R54 原文证据摘录（全部保留）

- **【产品线与在售品牌】**CSI 官网一级栏目含「Komunikacja przemysłowa（工业通信）」——交换机类目显性在线。
  > Komputery przemysłowe · Obudowy przemysłowe · Industrial Flash · Komputery Rugged · Komunikacja przemysłowa · Elektronika użytkowa
  > 来源：https://csi.pl/
- **【业务定位】**30+ 年工业计算机系统分销商，服务工业、交通、物流、数字标牌、安防、能源与 AI 场景。
  > Jesteśmy dystrybutorem przemysłowych systemów komputerowych, który od ponad 30 lat dostarcza kompletne rozwiązania… przemysł, transport, logistyka, Digital Signage, security, energetyka czy sztuczna inteligencja.
  > 来源：https://csi.pl/
- **【团队与规模】**公司自述规模体量：30+ 年、1 mln+ 订单、10 000+ 客户——波兰一线工控分销。
  > ponad 30 lat doświadczeń · ponad 1 mln zamówień · ponad 10 000 klientów
  > 来源：https://csi.pl/
- **【目标行业与场景】**公开参考项目：华沙有轨电车（Tramwaje Warszawskie）交通类供应——轨道交通客户线。
  > Referencje udzielone od spółki Tramwaje Warszawskie sp. z o.o.
  > 来源：https://csi.pl/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **W**：公开信息有限
- **O**：P1 场景切入（主场景匹配+首触只推一个型号的纪律）
- **T**：现有供应商惯性；价格竞争。

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

**主题**：Rugged 8-port PoE for outdoor/unheated cabinets

```text
Hi CSI,

I came across CSI S.A. - 分销（Antaira 授权）.

We build an unmanaged industrial 8-port PoE switch (af/at) with 250m extended reach, redundant 44–57V DC input with reverse-polarity protection, DIN-rail mount and a 3-year warranty. Reference: $74.8 USD EXW.

One question: Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?

If it is useful, I can send one unit for a 30-day evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)
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
