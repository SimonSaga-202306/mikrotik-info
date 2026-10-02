# Atlantik Elektronik

> **评级 A**　|　德国　|　档案编号 `A-312`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-312
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇），三星重点
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Atlantik Elektronik 德 40 年 B2B 分销 ODM（Lantronix 授权+design-in）：私营工业边缘段（AGV/充电/零售/场站监控）二轨窄位（$165 锚点一致）；政府/关键基建守界句；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Atlantik Elektronik（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 | 事实 |
| 网站 | https://www.atlantikelektronik.com | 事实 |
| 类型 | 分销（Lantronix 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Lantronix（Marvell 生态，工业 IoT/边缘） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Atlantik Elektronik（德国 München，40+ 年 B2B 分销+ODM 方案商）：**Lantronix 授权分销（全线+design-in，自 营 atestore.de 电商）**;方案页明列 **SOLUTIONS FOR GOVERNMENT AND CRITICAL INFRASTRUCTURE** 板块（守界句必压）旁另有联网充电/AGV 机器人/场站监控边缘 AI/AI 零售
- 【推断】大 B2B 分销+ODM：私营工业边缘段（AGV/充电/零售/场站监控）是其接入件真实消耗面；政府/关键基建段守界句先置
- 【假设】私营工业边缘方案里 Lantronix 旁的 value 二轨窄位

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Lantronix（Marvell 生态，工业 IoT/边缘））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@atlantikelektronik.com
  - 状态：既有/公开
- **电话**：+49 89 89 505 0
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：info@atlantikelektronik.com（atestore Lantronix专页联系信息）；+49 89 89 505 0；Lantronix授权分销页：atestore.de/en/lantronix/
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 声明边界+design-in 供应商一页

- **推什么**：STI-480DGGM（Saga）（工业管理 8×电口 + 4×千兆上联，ERPS）+板卡/整机 design-in 选项
- **切入点**：德/英一封：声明不跟政府/KRITIS 与 C2 军向项目；仅就其零售/充电/机器人方案的联网件，作为 design-in 供应商候选（LTS 供货年限+宽温参数一体）。
- **要问的问题**：零售/充电/机器人方案的联网件接 design-in 供应商评估吗？
- **随附证明**：design-in 一页+宽温/EMC/LTS 参数包。

### 第 2 次跟进 · 场地监控方案的 24 口 PoE

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：其 Edge AI 场地监控方案工业客户面的 24 口 PoE 接入位。
- **要问的问题**：场地监控方案的接入层谁在供？
- **随附证明**：一页报价（德/英）。

### 第 3 次跟进 · atestore 类目窄线

- **推什么**：SFP/收发器 目录
- **切入点**：atestore 配件类目邻位窄线提案；不回即冻结。
- **要问的问题**：配件类目有邻位窄线位吗？
- **随附证明**：窄线一页价卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第16批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：慕尼黑 40 年 Lantronix 授权 design-in 分销（**政府/关键基建+自主 C2 军向两面划出**；AI 零售/充电/机器人商业面是本库 Marvell 生态最对口 design-in 户）。
- **产品线与在售品牌**：Lantronix 全线+计算/视觉/连接组合件+ODM 定制+atestore 电商。
- **目标行业与场景**：商业面：零售 AI/充电设施/AGV 机器人/重机 ECU 的 OEM 客户。
- **团队与规模**：大中型分销（千级客户自述）。
- **决策链与对接人**：info@atlantikelektronik.com（atestore 专页，CSV 9-27）。
- **技术与认证**：Lantronix 多年获奖分销（CSV）。
- **采购与供应链信号**：**design-in 逻辑**：其零售/充电/机器人方案的联网件可 design-in 我们的工业/商业交换板卡与整机——供应商级合作（他们对 Lantronix 也是这关系）。
- **近期动态与线索**：2026 方案站大改版（fy26 矩阵）=新品类扩张年，评估窗口大。
- **与我方契合点**：工业交换机 design-in（板/整机）+24 口 PoE 用于其监控/零售方案。
- **风险与注意**：政府/KRITIS 与 C2 军向两面绝不跟进；design-in 资料要全（宽温/EMC/PoE 预算/LTS 供货年限）。

### R54 原文证据摘录（全部保留）

- **【业务定位】**慕尼黑 40+ 年 B2B 分销与 ODM 方案商：design-in 与定制集成，**Lantronix 多年获奖授权分销**（2022 EMEA Partner 等 CSV 记录），自营 atestore.de 电商。
  > Solution Provider and authorized Distributor — With more than 40 years of experience in development, design-in and sales of standard and customized solutions ‖ （CSV 记录）Lantronix 授权分销+全线产品 design-in 支持
  > 来源：https://www.atlantikelektronik.com/en
- **【目标行业与场景】**方案矩阵：AI 零售（智能售货/货架/支付）/联网充电基础设施/Edge AI 场地监控/AGV 与移动机器人/重机 ECU（商业可做）+ **Government & Critical Infrastructure、AI-powered C2 Systems（自主编队指挥控制系统）——政府关键基建与军向两面完全划出**。
  > SOLUTIONS FOR GOVERNMENT AND CRITICAL INFRASTRUCTURE ‖ AI-powered Command and Control Systems — Production-ready C2 Systems for autonomous fleets ‖ Solutions for AGVs and Mobile Robotics · Connected Charging Infrastructure
  > 来源：https://www.atlantikelektronik.com/en
- **【决策链与对接人】**info@atlantikelektronik.com（atestore Lantronix 专页+获奖新闻双证，CSV 9-27 official-company）；+49 89 89 505 0。
  > （CSV 2026-09-27 记录）自营电商 atestore 的 Lantronix 专页与获奖新闻给 info@atlantikelektronik.com、+49 89 89 505 0；official-company
  > 来源：https://www.atlantikelektronik.com/en

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第32批.json`；价格均为 EXW 快照。

- **①背景再核**：DE 大 B2B 分销（官网一手核）
- **②芯片/型号**：Lantronix 线
- **③KP 深挖**：info@
- **④Saga 对标**：二轨窄位（$165 锚点一致）
- **⑤在乎与偏好**：design-in 工程/方案完整

### R55 证据摘录（全部保留 · 含数量）

- **【目标行业】**Solutions: Government and Critical Infrastructure/Connected Charging/AGVs/Site Monitoring Edge AI——authorized Distributor & ODM 40+ years
  > Solutions: Government and Critical Infrastructure/Connected Charging/AGVs/Site Monitoring Edge AI——authorized Distributor & ODM 40+ years
  > 来源：https://www.atlantikelektronik.com

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：德国大 B2B 分销+ODM
- **产品线与在售品牌**：Lantronix 领衔多厂
- **目标行业与场景**：工业边缘/AGV/充电/零售（政府关键基建=守界注）
- **团队与规模**：大分销组织
- **决策链与对接人**：info@ 口
- **技术与认证**：—
- **采购与供应链信号**：分销泳道+design-in
- **近期动态与线索**：经贸方案页持续扩张
- **与我方契合点**：私营工业边缘段二轨窄位（政府/关键基建守界句）
- **风险与注意**：关键基建板块明列——守界句必压

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Atlantik Elektronik 德 40 年 B2B 分销 ODM（Lantronix 授权+design-in）：私营工业边缘段（AGV/充电/零售/场站监控）二轨窄位（$165 锚点一致）；政府/关键基建守界句 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：关键段
- **O**：私营
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
| 决策人识别 | ❓ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 替补机制
  - [ ] 占比

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hallo Atlantik Elektronik team,

Forty-plus years as B2B distributor and ODM - Lantronix design-in, AGV connectivity, charging infrastructure, edge-AI site monitoring. One boundary sentence: your government and critical-infrastructure solutions stay on their certified paths; this concerns the private industrial edge only.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation, plus an 8-port industrial PoE line. Reference: $165 USD EXW (2026-09-29).

One question: in your private-edge solutions, is there a value switching slot beside the current portfolio?

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

- **KP 领英直达**:[Atlantik Elektronik · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Atlantik%20Elektronik)(搜索链接,点入后核职位再加;来源:联络核验)
- **中国进口与管制**:国别档位 中(IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STI-288GP(工业导轨 24G+4×10G→机柜/自动化)、STC-28DGGPM(24G PoE+/4×25G→分销走量)(批量潜力高,可上 280W 旗舰对照行)(本行为调查分析结论,与开发信首推型号是两回事)
