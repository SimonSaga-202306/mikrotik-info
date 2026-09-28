# DeInta

> **评级 A**　|　西班牙 · Zaragoza　|　档案编号 `A-318`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-318
rating: A
country: 西班牙
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: true, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — 主场景匹配+首触只推一个型号的纪律；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | DeInta（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 西班牙 / Zaragoza | 事实 |
| 网站 | https://www.deinta.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis + Axis + 3CX + HP | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis + Axis + 3CX + HP）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：deinta@deinta.com
  - 状态：既有/公开
- **电话**：+34 976 798 180
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：deinta@deinta.com（官网页脚+法定告知；联系页另列personal@deinta.com、DPO privacidad@deinta.com）；+34 976 798 180
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · Axis 项目旁位 24 口监控 PoE 一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）
- **切入点**：西语一封：Axis 监控项目的 24 口大 PoE 接入层第二来源（视频 VLAN 预设+其 Alman'd 平台无厂商依赖的契合点）。
- **要问的问题**：监控项目的大口数 PoE 目前由谁供应？有第二来源位吗？
- **随附证明**：一页报价（西）+ VLAN 预设。

### 第 2 次跟进 · 维保替换备件

- **推什么**：STI-280GE（Saga） 等窄线
- **切入点**：全国 SLA 维保网的现场替换备件小批（批次一致性+RMA 先行）。
- **要问的问题**：维保替换件有常备目录吗？
- **随附证明**：备件一页价卡。

### 第 3 次跟进 · 条款收口

- **推什么**：—（条款）
- **切入点**：梯价/备件条款收口；不回即冻结。
- **要问的问题**：（无需回）条款留档。
- **随附证明**：条款一页（西/英）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第16批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：萨拉戈萨安防集成商（自研 Alman'd 纳管平台=品牌中性、24/7 维保呼叫中心=替换件持续消耗）。
- **产品线与在售品牌**：安防工程/维保/远维/自研软件；Allied+Axis+3CX+HP。
- **目标行业与场景**：西班牙多站点企事业单位（multisede 客群）。
- **团队与规模**：中型（24/7 呼叫中心+全国 SLA 网）。
- **决策链与对接人**：deinta@deinta.com（页脚/法定告知，CSV 9-27）。
- **技术与认证**：ISO 9001/14001+内政部 homologación（官网）。
- **采购与供应链信号**：**双位**：Axis 监控项目旁的 24 口 PoE 接入层+其维保体系的替换备件（GCI 同款逻辑）。
- **近期动态与线索**：Alman'd 平台迭代=其接新设备的意愿自带（开放纳管架构）。
- **与我方契合点**：24 口监控 PoE+维保替换备件。
- **风险与注意**：Axis 锚位不碰；内政部资质是其安防专营面（不等于公共采购，正常商业可谈）。

### R54 原文证据摘录（全部保留）

- **【业务定位】**萨拉戈萨电子安防+电信集成商「Tu socio tecnológico」：工程/交钥匙项目/**24/7 技术呼叫中心+全国 SLA 维保**/远程运维+**自研 Alman'd 多站点集成平台**；ISO 9001/14001+内政部安防资质。
  > DEINTA SEGURIDAD… ofrecer las mejores soluciones tecnológicas ‖ Un call center técnico con asistencia 24/7 ‖ Alman’d es una plataforma abierta de integración de sistemas… multisede ‖ homologada por el Ministerio del Interior
  > 来源：https://deinta.com/
- **【产品线与在售品牌】**Allied Telesis + Axis + 3CX + HP（CSV）；自研平台把各厂设备统一纳管——**品牌中性集成商，吃设备不绑厂商**。
  > （CSV 记录）Allied + Axis + 3CX + HP ‖ Alman’d… permite… relacionarse entre ellos y con sistemas externos（设备统一纳管）
  > 来源：https://deinta.com/
- **【决策链与对接人】**deinta@deinta.com 页脚/法定告知+personal@ 联系页（CSV 9-27 official-company）；+34 976 798 180；Grupo Enebro 投资集团旗下。
  > （CSV 2026-09-27 记录）页脚/法定告知给 deinta@deinta.com、CIF B99060089；联系页另列 personal@deinta.com；elioplus 列 VOIP/AT 渠道伙伴；official-company
  > 来源：https://deinta.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
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

**主题**：24-port PoE + 10G uplinks for your larger sites

```text
Hi DeInta,

I came across DeInta - 集成商/代理（Allied Telesis）.

We build a 24-port Gigabit PoE switch (280W, af/at) with 4×10G SFP+ uplinks, Voice VLAN and a hardware PoE watchdog that reboots hung APs/cameras without a site visit. Reference: $165 USD EXW.

One question: How many PoE ports does a typical site of yours need today?

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
