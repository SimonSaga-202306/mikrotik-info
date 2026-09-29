# Andres Ocampo

> **评级 A**　|　美国 · Lake Grove, NY　|　档案编号 `A-072`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-072
rating: A
country: 美国
biz_org: 个体顾问（无官网）
business_model: 顾问项目制
decision_speed: fast
price_sensitivity: high
volume_potential: 1  # 1-5
needs: {poe: true, industrial: false, tenG: true, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；顾问项目制
- **商业模式**：顾问项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — Ocampo 美 7 证 Hotmail 个人：破冰薄档如实（$99 锚点一致）；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Andres Ocampo（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Lake Grove, NY | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCINE+MTCIPv6E+MTCSE | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Andres Ocampo（美国）：7 证 MikroTik 顾问（MTCNA+MTCRE+MTCTCE+MTCINE+MTCIPv6E+MTCxx 截断，CSV 原始口径）；Hotmail 联系方式；公开站未查得
- 【推断】个人顾问足迹薄；先短信/邮件破冰
- 【假设】含 MTCINE=骨干工程底，破冰后特性对话

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCINE+MTCIPv6E+MTCSE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、万兆上行/骨干
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sriandres@hotmail.com
  - 状态：既有/公开
- **电话**：+1 551 219 8239
- **原始联系字段**：+1 551 219 8239 / sriandres@hotmail.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（企业现场接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：顾问/MSP 通吃款：24 口 PoE++ 带 AP/监控/话机，用 VRRP+L2 话题开场（他的技能关键词），不谈价格。
- **要问的问题**：你现在手上项目的接入层用什么？（先确认身份与现状）
- **随附证明**：规格书（英文）+ L2 特性清单（VRRP/MSTP 支持项）。

### 第 2 次跟进 · 工业级非管理 PoE（弱电间/室外点位）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：4 口宽温小机做零散点位补盲：即插即用免维护，寄一台实测比讲道理快。
- **要问的问题**：要不要寄一台 4 口工业机给你测？
- **随附证明**：宽温报告 + 免费/成本样机政策。

### 第 3 次跟进 · 管理型 PoE（L2 冗余/分段方案）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：直打他的交换专长：MSTP/ERPS/VRRP 组合实测数据+VLAN 分段模板全套，技术人只认真机数据。
- **要问的问题**：ERPS 与 MSTP 在你项目里哪个用得多？我们的收敛实测要不要看看？
- **随附证明**：ERPS/MSTP 收敛实测 + VLAN 模板（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：纽约长岛 Lake Grove 的 MikroTik 认证顾问（可能同时在 MSP 任职）——公开线上足迹极少，属「名录型」人才。
- **产品线与在售品牌**：顾问服务：路由交换设计、防火墙、MPLS/VPN、无线 PtP/PtMP、带宽管理。
- **目标行业与场景**：企业网与 IPTV/服务商方向的 L2/L3 项目；若确在 MSP 任职，则多客户共享交付体系。
- **团队与规模**：个人；LinkedIn 仅 32 个联系人（同名档案），数字化存在极弱。
- **决策链与对接人**：Andres Ocampo 本人（+1 551 219 8239 / sriandres@hotmail.com，CSV 记录）。
- **技术与认证**：6 证（含 MTCINE/MTCSE）；交换技能写到 VRRP/STP/L2 过滤器粒度——L2 功底扎实。
- **采购与供应链信号**：项目制选型；若挂靠 MSP，则用量走公司库——首封邮件先摸清他现在是独立顾问还是雇员。
- **近期动态与线索**：无公开动态可考（本轮检索仅得 2019 年前后的静态档案页）。
- **与我方契合点**：交换技能对口：VRRP/生成树话题+管理型交换实测能直接对上话；Hotmail 级触点建议以电话为主。
- **风险与注意**：身份待核实（同名 LinkedIn 未确认）：先用中性问候确认身份与近况，不谈报价；回复率低要有心理准备。

### R54 原文证据摘录（全部保留）

- **【业务定位】**LinkedIn 公开档案（第三方页面，同名待核）：纽约 Queens 的 MSP 托管服务工程师（Lincoln IT）。
  > Managed Services Level 1 Engineer at Lincoln IT · Location: Queens County, New York, United States
  > 来源：https://www.linkedin.com/in/andres-ocampo-74878363/
- **【技术与认证】**CSV 既有 MikroTik 名录记录：MTCNA+MTCRE+MTCTCE+MTCINE+MTCIPv6E+MTCSE 6 证持证人。
  > MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCINE+MTCIPv6E+MTCSE（CSV 信号列）
  > 来源：https://mikrotik.com/consultants
- **【目标行业与场景】**CSV 既有记录：技能清单明确含 Switching（VRRP/生成树/L2 过滤器）、Routing & Switching、MPLS 与 VPN、带宽管理。
  > 技能清单明确含 Switching（VRRP、SPT 生成树、L2 过滤器）、Routing & Switching；高级防火墙与 Mangle、OSPF/BGP/路由过滤…（CSV 备注）
  > 来源：https://mikrotik.com/consultants

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第8批.json`；价格均为 EXW 快照。

- **①背景再核**：7 证个人、无站
- **②芯片/型号**：未公开
- **③KP 深挖**：本人 hotmail
- **④Saga 对标**：破冰后定
- **⑤在乎与偏好**：未知

### R55 证据摘录（全部保留 · 含数量）

- **【技术与认证】**CSV：Andres Ocampo 7 证（美国）
  > CSV：Andres Ocampo 7 证（美国）
  > 来源：https://mikrotik.com/consultants

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：美国个人顾问（足迹薄）
- **产品线与在售品牌**：未公开
- **目标行业与场景**：未公开
- **团队与规模**：个人
- **决策链与对接人**：Ocampo 本人
- **技术与认证**：7 证（含 MTCINE/IPv6E）
- **采购与供应链信号**：未知
- **近期动态与线索**：无
- **与我方契合点**：破冰后定
- **风险与注意**：薄档如实

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Ocampo 美 7 证 Hotmail 个人：破冰薄档如实（$99 锚点一致） |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：证齐
- **W**：薄
- **O**：未探
- **T**：不确定

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

- **深挖专属待问（R56）**：
  - [ ] 执业状态
  - [ ] 方向
  - [ ] 评测意愿

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Andres,

I found you on the MikroTik consultant list - a seven-certification stack is hard work made visible.

We build managed PoE switches with the L2+ features consultants usually chase (Voice VLAN, ERPS, watchdog).

One question: in your projects, is the switching layer ever open for alternatives?

If yes, I can send the feature table and an evaluation unit. If not, one line and I close the loop.

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
