# Urbino Lobo / MiniMeLabs

> **评级 A**　|　葡萄牙 · Funchal（马德拉）　|　档案编号 `A-053`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-053
rating: A
country: 葡萄牙
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: false, oem: false, hotel: true, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（酒店/多住户），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — MiniMeLabs 葡团伦敦场所 Wi-Fi/分析：高密 AP 项目 PoE 接入层随单（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Roughly how many site visits a month come from a hung AP or camera across your hospitality sites?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Urbino Lobo / MiniMeLabs（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 葡萄牙 / Funchal（马德拉） | 事实 |
| 网站 | minimelabs.com | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Urbino Lobo | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCUME | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCUME）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）、酒店/多住户
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - 酒店/多住户：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：urbino@minimelabs.com
  - 状态：既有/公开
- **电话**：+351 919 379 550
- **原始联系字段**：+351 919 379 550 / urbino@minimelabs.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Urbino Lobo**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 PoE++（酒店/商圈 WiFi 接入主设备）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他每个场景 24 口一次到位：PoE++ 带齐 AP+监控+话机；他的 captive portal 架构完全不动——架构上零冲突。
- **要问的问题**：一场景的 AP 平均多少个、楼层交换机现在是什么速位？
- **随附证明**：功率实测表 + AP/监控混合供电对照。

### 第 2 次跟进 · 工业非管理 PoE（室外广场点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：广场/外部场馆的室外 AP 点位：宽温宽压、DIN、免配置、坏了整机现场热换——给他减少外场上门次数。
- **要问的问题**：室外/广场点位冬天会出现什么供电问题？
- **随附证明**：宽温报告 + DIN 安装图 + 一台测试机。

### 第 3 次跟进 · 管理型 + GDPR/客人网分段

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：管理型 VLAN 多网段+访客隔离+SNMP 资产管理——与他 GDPR 话术对齐，把「客人/员工/监控」的分层写成分段模板。
- **要问的问题**：他的 captive portal 与 VLAN 分层怎么做的、每个场景分几个 VLAN？
- **随附证明**：VLAN/ERPS/ACL 模板 + ERPS 收敛实测（英文）+ SNMP 参数页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：马德拉（/伦敦）的场景体验公司：公共空间/酒店/零售的“位置感知+PWA+获客”平台，硬件依赖现场网络基础。
- **产品线与在售品牌**：Morfus（PWA）/MidasMoon（广告）/EzeHome（IoT）/Sentry——软件驱动，但任何案例都要配合现场 WiFi/NAC/供电与分网设备。
- **目标行业与场景**：广场/机场/商场/酒店/餐饮——高价位场景、对 WiFi 与 VLAN 分段/Guest-PSK 等有实质要求。
- **团队与规模**：小型软件+现场交付工程队。
- **决策链与对接人**：Urbino Lobo（+351 919 379 550 / urbino@minimelabs.com），工程师+BD 兼位。
- **技术与认证**：MTCNA+MTCUME（来源：CSV 既有 MikroTik 名录记录）——他们看得懂我方的管理面参数。
- **采购与供应链信号**：随场景项目订齐现场网络设备（每酒店/商圈单子都是一次设备采购窗口）。
- **近期动态与线索**：伦敦大型商圈项目知名度高，葡萄牙/马德拉本地酒店也在升级周期里——主要切入点。
- **与我方契合点**：WiFi 服务=我们的 PoE++：他们要的就是“24 口设备一次到位 + 分网监管”；管理型在给 GDPR/客人网隔离时也有说头。
- **风险与注意**：他卖的是方案与数据价值——我们要给能进技术标书的参数细节，不与纯低价竞争。

### R54 原文证据摘录（全部保留）

- **【业务定位】**MiniMeLabs：做“物理与数字桥接”的智能酒店/公共空间场景方案（7 年品牌历程）。
  > Bridging the Physical & Digital — Innovating the way people connect with the world around them for 7 years
  > 来源：https://minimelabs.com/
- **【目标行业与场景】**方案覆盖 Hospitality、Public Spaces、Retail、Food & Beverage——WiFi 接入与获客平台是他主力。
  > Seamless customer Wifi onboarding… Public spaces · Hospitality · Retail mall · Food & Beverage
  > 来源：https://minimelabs.com/
- **【近期动态与线索】**在伦敦高端商圈落地（Trafalgar Square/Oxford Street/Westminster 与机场/商场/场馆）。
  > Proudly operating digital engagement solutions throughout London, in the exquisite areas of Trafalgar square, Oxford street & other areas of Westminster.
  > 来源：https://minimelabs.com/
- **【技术与认证】**其核心是 WiFi 定位分析与客户洞察（GDPR 合规），意味着对接入层设备的管理性（DHCP/SNMP/VLAN）有专业要求。
  > Customer Insights That Overcome MAC Randomization — Our Wi-Fi analytics and communications platform… maintains GDPR compliance.
  > 来源：https://minimelabs.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第6批.json`；价格均为 EXW 快照。

- **①背景再核**：葡团伦敦落地场所数字互动平台；Wi-Fi 获客/分析+IoT 四件套
- **②芯片/型号**：MTCUME 对口门户；平台软面板
- **③KP 深挖**：Lobo 直达
- **④Saga 对标**：高密 AP PoE 接入层随单
- **⑤在乎与偏好**：整包快速部署

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“operating digital engagement solutions throughout London – Trafalgar Square, Oxford Street, Westminster…airports, shopping centers, arenas…Morfus Connect 绕 MAC 随机化的场所 Wi-Fi 分析”
  > “operating digital engagement solutions throughout London – Trafalgar Square, Oxford Street, Westminster…airports, shopping centers, arenas…Morfus Connect 绕 MAC 随机化的场所 Wi-Fi 分析”
  > 来源：https://minimelabs.com/
- **【联系方式】**urbino@minimelabs.com；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > urbino@minimelabs.com；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://minimelabs.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | MiniMeLabs 葡团伦敦场所 Wi-Fi/分析：高密 AP 项目 PoE 接入层随单（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：落地实证
- **W**：量波动
- **O**：滚动
- **T**：直采

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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Urbino,

Running live venue Wi-Fi and analytics across Trafalgar Square and Oxford Street is no slideshow - it means real dense AP grids.

We build 24-port Gigabit PoE switches (280W, 802.3af/at, silent for back-of-house, watchdog) sized exactly for those AP clusters. Reference: $165 USD EXW.

One question: in a typical venue deployment, how many APs land on one access switch for you?

If useful, I can send one unit plus a venue rack layout. If not a fit, one line and I close the loop.

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
