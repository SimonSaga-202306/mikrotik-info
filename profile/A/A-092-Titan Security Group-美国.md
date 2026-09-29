# Titan Security Group

> **评级 A**　|　美国 · Chicago, IL　|　档案编号 `A-092`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-092
rating: A
country: 美国
biz_org: 个体顾问（无官网）
business_model: 顾问项目制
decision_speed: fast
price_sensitivity: high
volume_potential: 1  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；顾问项目制
- **商业模式**：顾问项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、PoE/监控/门禁），三星重点
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Marksman Titan 安保合并电子线：全国楼宇监控柜 value PoE（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Titan Security Group（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Chicago, IL | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Titan Security Group / Marksman Security Corporation（美国）：安保服务巨头合并案（boutique national footprint）——安保服务+礼宾/前台+**Titan Electronics 电子安防线**+咨询培训；CSV：Allied Telesis（Marvell Prestera 接入层）在册
- 【推断】Titan Electronics=楼宇监控/门禁工程线=摄像头柜 PoE 惯件
- 【假设】全国性大客户楼宇=翻修滚动量

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@titan-security.com
  - 状态：既有/公开
- **电话**：—
- **原始联系字段**：info@titan-security.com（经 marksman-titan.com 取得（Titan Security 现为 Marksman Titan）。具名：Todd Sheetz、Anthony Hernandez（VP））
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（电子安防项目接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：合并整合期切入：给 Titan Electronics 递「同规格更低成本」的接入层选项，全国多项目的量配上多仓交付说明。
- **要问的问题**：合并后项目接入层的标准件选型定了吗？
- **随附证明**：单路成本测算 + 全国交付说明 + 质保政策（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（周界/车库室外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：楼宇周界与车库的室外摄像头点位：宽温 DIN PoE 降低上门维护率——安保公司算账最懂「少跑一趟」的价值。
- **要问的问题**：室外点位的维护上门一年多少趟？
- **随附证明**：宽温报告 + 坏机替换测算 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（安防网段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：合并后标准化：安防 VLAN 隔离+ERPS 冗余一套模板全国复制，项目注册保价。
- **要问的问题**：全国项目的网络标准有没有统一窗口期？
- **随附证明**：VLAN/ERPS 模板 + 项目注册政策 + 收敛实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第5批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：芝加哥老牌安防集团（已并入 Marksman Titan）：人力安保+电子安防集成+礼宾服务一体，全国化布局，Allied Telesis 转售伙伴（CSV 记录）。
- **产品线与在售品牌**：Titan Electronics 线：视频监控/门禁/入侵系统设计安装；伙伴墙（官网 12 个 Logo 位）+Allied Telesis（CSV 记录）。
- **目标行业与场景**：商业楼宇/酒店/园区的综合安防；合并后跨区域项目增多。
- **团队与规模**：全国性精品安防服务商（合并后量级升级）；具名联系人 Todd Sheetz、Anthony Hernandez（VP）（CSV 9-27 记录）。
- **决策链与对接人**：info@titan-security.com（经 marksman-titan.com 取得，CSV 9-27 记录）；现站 contact 表单。
- **技术与认证**：Allied Telesis Resell 伙伴等级（CSV 记录）；安防系统多平台工程师班底。
- **采购与供应链信号**：电子安防项目=IP 视频/门禁 PoE 接入层批量采购；合并整合期=供应商池重排窗口。
- **近期动态与线索**：Titan×Marksman 合并（官网头条）——采购归并与标准件重选型正在进行时。
- **与我方契合点**：电子安防项目的接入层 24 口 PoE++ 与周界工业件；全国项目需要多仓交付能力——我们能配合。
- **风险与注意**：合并期内部流程乱：报价单写清 SKU/质保/交付，降低他整合期的决策成本；别催、跟节奏。

### R54 原文证据摘录（全部保留）

- **【近期动态与线索】**官网头条公告：Titan Security Group 与 Marksman Security Corporation 战略合并，组成全国网络的精品安防服务商——组织整合期。
  > Titan Security Group and Marksman Security Corporation Announce Strategic Merger; Creating A Boutique Security Services Provider With A National Footprint
  > 来源：https://marksman-titan.com/
- **【业务定位】**四条业务线：人力安保、酒店礼宾、Titan Electronics（电子安防集成）、咨询培训——集成臂是 Titan Electronics。
  > Security Services · Hospitality & Concierge Services · Titan Electronics · Security Consulting & Training Services
  > 来源：https://marksman-titan.com/
- **【目标行业与场景】**「没有做不了的大项目」自我定位，全国化客户盘（合并公告）。
  > Our vast experience allows us to handle complex and diverse projects. No project is too big or too complex for us to handle.
  > 来源：https://marksman-titan.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第10批.json`；价格均为 EXW 快照。

- **①背景再核**：安保两大合并全国化；电子线在册
- **②芯片/型号**：Allied Telesis
- **③KP 深挖**：info@集团口
- **④Saga 对标**：监控柜 value PoE
- **⑤在乎与偏好**：集团流程表面档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Titan Security Group and Marksman Security Corporation Announce Strategic Merger…boutique security services provider with a national footprint…Titan Electronics”
  > “Titan Security Group and Marksman Security Corporation Announce Strategic Merger…boutique security services provider with a national footprint…Titan Electronics”
  > 来源：https://marksman-titan.com/
- **【联系方式】**info@titan-security.com；双域 MX=Google（MX/DNS 级核验：域存活=邮件可投递到域）
  > info@titan-security.com；双域 MX=Google（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://marksman-titan.com/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：美国全国性安保集团（合并后生）
- **产品线与在售品牌**：安保/礼宾/电子线+Allied Telesis
- **目标行业与场景**：商业楼宇/场馆
- **团队与规模**：全国性
- **决策链与对接人**：info@ 口
- **技术与认证**：工程整合
- **采购与供应链信号**：全国项目随单
- **近期动态与线索**：Titan+Marksman 合并公告
- **与我方契合点**：Titan Electronics 监控柜 PoE
- **风险与注意**：大集团采购流程

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Marksman Titan 安保合并电子线：全国楼宇监控柜 value PoE（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：全国
- **W**：流程
- **O**：电子线
- **T**：在位

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
  - [ ] Electronics 线规模
  - [ ] 项目点密度
  - [ ] 采购结构

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Titan team,

A merged national security group with an electronics line means one thing operationally - a lot of camera closets that have to power up and stay up.

We build a 24-port Gigabit PoE switch (280W, 802.3af/at, hardware watchdog, Voice VLAN) as a value-tier complement for the Titan Electronics shelf. Reference: $165 USD EXW.

One question: in a typical commercial building build, how many cameras land on one access cabinet for your team?

If useful, I can send one unit with full documentation. If not a fit, one line and I close the loop.

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
