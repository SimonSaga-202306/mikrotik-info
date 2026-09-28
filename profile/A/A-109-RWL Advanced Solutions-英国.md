# RWL Advanced Solutions

> **评级 A**　|　英国 · London　|　档案编号 `A-109`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-109
rating: A
country: 英国
biz_org: 个体顾问（无官网）
business_model: 顾问项目制
decision_speed: fast
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: true, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；顾问项目制
- **商业模式**：顾问项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — 主场景匹配+首触只推一个型号的纪律；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | RWL Advanced Solutions（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / London | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |
| ⚠️ 信息缺口 | 本条**抓不到邮箱**，需人工补齐邮箱或改为电话单独跟进后再进群发名单 | 事实 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@rwlas.com
  - 状态：既有/公开
- **电话**：—
- **原始联系字段**：sales@rwlas.com（都柏林。自述「欧洲领先的数据布线与网络产品独立分销商」，代理 Panduit 等；覆盖电信/商用/数据中心。⚠️ 属**分销商**（转化率低），且主业是布线不是交换机）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 品类空缺提案（无源货架补有源层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：「布线+接入层一单配齐」类目建议书：24 口 PoE++ 上架给安装商渠道，附试点动销方案。
- **要问的问题**：你们的有源类目现在什么状态？试销位怎么谈？
- **随附证明**：类目建议书 + 货架提案（型号/价位/毛利）+ 公司一页（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（场馆/工业安装商 SKU）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：工业/场馆安装商：宽温 DIN PoE 与他布线机柜同货架组合装。
- **要问的问题**：工业场景的 SKU 试点愿意上哪几款？90 天 KPI 怎么定？
- **随附证明**：试点方案 + 宽温报告 + 营销物料。

### 第 3 次跟进 · 管理型 10G（类目扩展+渠道政策）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：试点动销后扩管理型：项目注册+价格保护+他的 Educational Programs 培训位。
- **要问的问题**：项目注册与培训位按你们的模板来？
- **随附证明**：渠道政策包 + 培训计划 + VLAN/ERPS 模板。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第6批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：三地（都柏林为总部）布线分销；⚠️ CSV 已注明：属分销商（转化率低）且主业是布线不是交换机——但「有源缺口」正是提案点。
- **产品线与在售品牌**：Panduit/Leviton/Excel 无源布线+机柜+电气+CEL-FI；未见自有有源交换品牌。（Allied 关系为 CSV 记录）
- **目标行业与场景**：安装商渠道的 DC/商业楼宇/电信配套；培训业务（Educational Programs）做渠道粘性。
- **团队与规模**：近 20 年三地公司（官网）。
- **决策链与对接人**：sales@rwlas.com（CSV 9-27 记录）；分销采购走品类经理。
- **技术与认证**：布线体系认证完善；Allied 代理（CSV 记录）。
- **采购与供应链信号**：分销商上架逻辑：类目空隙（有源 PoE/接入层）+安装商「布线+交换一单拿齐」的便利性是他的增收点。
- **近期动态与线索**：IE/UK/NL 三站分站运营常态。
- **与我方契合点**：无源货架补有源：24 口 PoE/工业件以「安装商一单配齐」提案上架，三地仓储是现成放大器。
- **风险与注意**：CSV 已预警分销转化率低：用「类目建议+试点 KPI」商务方式谈，不做技术宣讲；90 天动销试点定去留。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网自述：欧洲领先的数据布线与网络产品独立分销商，都柏林/伦敦/阿姆斯特丹三地覆盖欧洲及以外。
  > Europe’s leading independent distributor for Data Cabling and Network products. With locations in Dublin, London and Amsterdam, we have a comprehensive reach across Europe and beyond.
  > 来源：https://www.rwlas.com/
- **【产品线与在售品牌】**战略合作品牌：Panduit/Leviton/Excel 等无源巨头，向安装商分发交钥匙方案；近 20 年经营、数千客户。
  > We are strategically partnered with leading Global brands such as Panduit, Leviton and Excel. We distribute Turnkey solutions to installers across many different theatres. … With almost 20 years in business
  > 来源：https://www.rwlas.com/
- **【目标行业与场景】**方案类目九大件全是「无源+周边」：数据中心/铜缆/光纤/机柜/走线架/电气/标签/电信/CEL-FI 信号增强——有源交换类目缺位。
  > Data Centres · Copper Cabling · Fibre Optic · Cabinets & Racks · Cable Containment · Electrical · Labelling & Identification · Telecom · Nextivity CEL-FI Cellular Enhancement（Solutions 类目）
  > 来源：https://www.rwlas.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第11批.json`；价格均为 EXW 快照。

- **①背景再核**：欧洲布线网络分销（无源主干）；installer 渠道
- **②芯片/型号**：Panduit/Leviton/Excel
- **③KP 深挖**：sales@
- **④Saga 对标**：架上 active PoE 补位
- **⑤在乎与偏好**：证书+案例+文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Europe’s leading independent distributor for Data Cabling and Network products…strategically partnered with leading Global brands as we distribute Turnkey solutions to installers”
  > “Europe’s leading independent distributor for Data Cabling and Network products…strategically partnered with leading Global brands as we distribute Turnkey solutions to installers”
  > 来源：https://www.rwlas.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：覆盖
- **W**：空档未证
- **O**：补位
- **T**：大牌

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 一人/个体=单点与节奏风险

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
Hi RWL team,

Twenty years of turnkey distribution to installers, and the passive layer owned end to end - the open lane next to it is the active layer.

We build a 24-port Gigabit PoE switch (280W, 802.3af/at, Voice VLAN, watchdog) designed for exactly the active side of turnkey cabling. Reference: $165 USD EXW.

One question: in your catalog next to Panduit and Leviton, is there an open slot for an active PoE access switch?

If useful, I can send one unit with the full documentation pack. If not a fit, one line and I close the loop.

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
