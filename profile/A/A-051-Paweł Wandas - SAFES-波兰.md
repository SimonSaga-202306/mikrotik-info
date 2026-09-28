# Paweł Wandas / SAFES

> **评级 A**　|　波兰 · Kraków　|　档案编号 `A-051`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-051
rating: A
country: 波兰
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — SAFES 波高端物业/酒店 IT 全托管（PMS+SOC）：单店客房 Wi-Fi+安防 24 口 PoE 随单（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Paweł Wandas / SAFES（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 波兰 / Kraków | 事实 |
| 网站 | safes.pl | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Paweł Wandas | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE+MTCSWE+MTCEWE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCINE+MTCIPv6E+MTCSE+MTCSWE+MTCEWE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：biuro@safes.pl
  - 状态：既有/公开
- **电话**：+48 412 412 324
- **原始联系字段**：+48 412 412 324 / biuro@safes.pl
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Paweł Wandas**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 PoE++（托管酒店/物业项目替换件）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：托管 7×24 模式：换件仓库的逻辑——24 口 PoE++ 拿来做他的备用库存 + 项目替换机，性价比立现。
- **要问的问题**：替换件仓库现用哪个系列、备机放几台？
- **随附证明**：功率实测 + SNMP/MIB 明细 + 英文对照页。

### 第 2 次跟进 · 工业非管理 PoE（楼层/天花/室外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：运维商最怕的楼层吊顶/地下机槽点位：宽温宽压、免配置，坏了一台热换。
- **要问的问题**：楼层/室外小型节点一年换几台、上门成本多大？
- **随附证明**：宽温报告 + DIN 安装图 + 单机热换说明。

### 第 3 次跟进 · 管理型 + Zero Trust/VLAN 托管包

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：与 SOC/Zero Trust 话术对齐：管理型 VLAN 分段+SNMP 明细+ACL，写进他的托管方案里能涨服务费。
- **要问的问题**：客户托管包里 802.1X/VLAN 分段你们怎么卖、谁交付？
- **随附证明**：VLAN/ERPS/ACL 配置模板 + SNMP 对接说明 + ERPS 收敛实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Kraków 的托管 IT/网络安全服务商，面向酒店与高级物业，LAN/Zero Trust 话术清晰；工程侧做 LAN/WAN/Wi-Fi 代维。
- **产品线与在售品牌**：按项目选型（MikroTik 栈为主，顾问 Paweł Wandas 墙上全证）。
- **目标行业与场景**：酒店、商业楼宇、高级物业的全年无休设备托管——PoE 交换机是典型运维包里的硬件。
- **团队与规模**：服务/SOC 支持团队制，但决策集中。
- **决策链与对接人**：Paweł Wandas（+48 412 412 324 / biuro@safes.pl）。
- **技术与认证**：公司顾问墙上顾问持 MTCNA 至 MTCEWE/MTCSWE 全证（来源：CSV 既有 MikroTik 名录记录）；熟 The Dude/SNMP 运维文化，能看懂 SNMP/MIB 与资产发现类参数。
- **采购与供应链信号**：7×24 服务包模式：备件/换机库存是硬指标——「备用库存+快速热换」正是他们的购买逻辑。
- **近期动态与线索**：官网主打 SOC/Zero Trust 话术——客户项目多要求 VLAN 分段/802.1X，管理型 PoE 能写进他的托管方案。
- **与我方契合点**：酒店项目 PoE 运维、SOC 管理面安全、SNMP 细节——直接命中管理型；备件模式适合他的 7×24 运维。
- **风险与注意**：运维商对供货连续与更换件仓库敏感：讲备件比讲便宜更能成单。

### R54 原文证据摘录（全部保留）

- **【业务定位】**SAFES 自述：20 年为波兰与海外的高级物业/场馆做托管 IT 与网络安全，7×24。
  > Przejmujemy pełną odpowiedzialność za systemy IT… Od 20 lat obsługujemy obiekty premium w Polsce i za granicą – w trybie non-stop.
  > 来源：https://safes.pl/
- **【目标行业与场景】**基础设施服务项明确 LAN/WAN/Wi‑Fi 网络、服务器/虚拟化、高可用——托管型服务即其接口。
  > Infrastruktura IT… Sieci LAN/WAN/Wi-Fi · Serwery i wirtualizacja · Wysoka dostępność
  > 来源：https://safes.pl/
- **【技术与认证】**明确 SOC 与 Zero Trust 架构语言——安全分层是他给客户的答案。
  > Security Operations Center · Architektura Zero Trust · Ochrona PMS
  > 来源：https://safes.pl/
- **【产品线与在售品牌】**另有 enova365 ERP 的授权实施线（商业软件+网络安全+托管 IT 混合的工程有限公司）。
  > Autoryzowany Partner enova365
  > 来源：https://safes.pl/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第6批.json`；价格均为 EXW 快照。

- **①背景再核**：20 年高端物业 IT 托管（酒店味浓：PMS 防护）+SOC 自运营
- **②芯片/型号**：六证 MikroTik 全链
- **③KP 深挖**：Wandas biuro@ O365 直达
- **④Saga 对标**：单店 24 口 PoE 随单（客房 Wi-Fi+安防+话机）
- **⑤在乎与偏好**：包年托管=稳定+长期支持口径

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Od 20 lat obsługujemy obiekty premium w Polsce i za granicą – w trybie non-stop…Sieci LAN/WAN/Wi-Fi…SOC, Architektura Zero Trust, Ochrona PMS”
  > “Od 20 lat obsługujemy obiekty premium w Polsce i za granicą – w trybie non-stop…Sieci LAN/WAN/Wi-Fi…SOC, Architektura Zero Trust, Ochrona PMS”
  > 来源：https://safes.pl/
- **【联系方式】**biuro@safes.pl +48 412 412 324；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > biuro@safes.pl +48 412 412 324；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://safes.pl/kontakt/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | SAFES 波高端物业/酒店 IT 全托管（PMS+SOC）：单店客房 Wi-Fi+安防 24 口 PoE 随单（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：托管粘性
- **W**：无渠道
- **O**：项目滚动
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
Hi Paweł,

A hotel or premium-property IT team that runs SOC 24/7, Zero Trust and PMS protection is rare - SAFES wears all three.

We build a 24-port Gigabit PoE switch (280W, 802.3af/at, Voice VLAN, ERPS, PoE watchdog) sized exactly for property Wi-Fi plus camera closets, with multi-year supply guarantees for managed-estate rollouts. Reference: $165 USD EXW.

One question: in a typical property you manage, how many outlets and cameras land on one access cabinet?

If useful, I can send one unit plus a hotel reference design. If not a fit, one line and I close the loop.

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
