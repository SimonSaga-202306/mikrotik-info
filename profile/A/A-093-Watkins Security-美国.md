# Watkins Security

> **评级 A**　|　美国 · Johnstown, PA　|　档案编号 `A-093`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-093
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
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Watkins 60 年安防：场馆高密摄像柜 PoE（$165 锚点一致）；DHS 联邦红线不触；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Watkins Security（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Johnstown, PA | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |

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

- **邮箱**：info@watkins-security.com
  - 状态：既有/公开
- **电话**：—
- **原始联系字段**：info@watkins-security.com（官网 contact 页；Principal/CEO Christopher Watkins）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（商业项目接入层，限定商业）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：合规先行再报价：开场即说明「仅商业项目适用」+合规声明，再递度假村/园区类 24 口接入层成本测算。
- **要问的问题**：商业项目的接入层现在用什么型号？（附合规声明）
- **随附证明**：合规声明包 + 单路成本测算 + 规格对照（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（室外/周界点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：积雪带（宾州西部）室外摄像头点位：宽温 -40 冷启动 DIN PoE，坏机率低的硬卖点。
- **要问的问题**：冬季室外点位坏机多吗？现在用什么型号？
- **随附证明**：宽温/-40 冷启动报告 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（安防网段标准化）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：AI 监控流量大：VLAN 隔离+ERPS+10G 上行给视频骨干让路，模板化复制到多项目。
- **要问的问题**：视频骨干现在千兆还是万兆？有拥塞投诉吗？
- **随附证明**：VLAN/ERPS 模板 + 10G 实测 + 收敛数据。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第5批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：宾州西部家族安防公司（现 CEO Christopher Watkins）：安防/消防/网络一体集成，自建设计-安装-培训闭环。
- **产品线与在售品牌**：AI 视频监控+门禁+消防+网络全套；Allied Telesis Resell 伙伴（CSV 记录）。
- **目标行业与场景**：园区/市政/度假设施/活动安保；历史单含政府与大型赛事。
- **团队与规模**：中小公司、深资历团队（组合 60+ 年经验）；Service & Support 自养。
- **决策链与对接人**：info@watkins-security.com；Principal/CEO Christopher Watkins（CSV 记录）。
- **技术与认证**：Allied Telesis Resell（CSV 记录）；系统工程师班底。
- **采购与供应链信号**：项目制批量；政府/赛事单对供应链合规（TAA/NDAA）要求严格。
- **近期动态与线索**：AI 监控叙事升级中（新包装的服务页），产品线在往「AI 分析」靠。
- **与我方契合点**：商业设施（度假村/园区）视频监控接入层与室外工业件的价差替换。
- **风险与注意**：⚠️ 国土安全部/G20 客户史=产地红线：明确只供商业项目、首次沟通主动讲边界（中国产，不做政府/关键设施单）。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网服务全家福：安防+IP 视频监控+消防探测+门禁+网络+IT 一整套。
  > Providing a Complete Suite of Security, IP Video Surveillance, Fire Detection, Access Control, Networking, and IT Solutions
  > 来源：https://www.watkins-security.com/
- **【产品线与在售品牌】**主打 AI 驱动的监控方案：设计-实施-培训全流程，开放架构可集成视频/门禁/考勤/广播。
  > Securing Your World with AI-Powered Surveillance Solutions · We personally visit your location… conducting a thorough facility tour · The systems that we install are built on open architecture platforms.
  > 来源：https://www.watkins-security.com/
- **【团队与规模】**官网数字：60+ 年组合经验、1000 客户、2M+ 安装产品、3 国、5+ 行业荣誉。
  > 60+ Years of Experience · 1,000 Satisfied Clientele · 2M+ Products Installed · 3 Countries World Wide · 5+ Industry Recognitions
  > 来源：https://www.watkins-security.com/
- **【目标行业与场景】**历史客户墙含美国国土安全部、美网公开赛、G20 匹兹堡峰会、Vail 度假村——⚠️ 涉政府/重大赛事史。
  > Past Clients — Seal of the United States Department of Homeland Security · US Open · G20-Pittsburgh 2009 · Vail（客户 Logo 墙）
  > 来源：https://www.watkins-security.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第10批.json`；价格均为 EXW 快照。

- **①背景再核**：60 年安防+IT 全链；联邦/赛事/度假村混合；DHS 红线
- **②芯片/型号**：Allied Telesis
- **③KP 深挖**：Principal info@
- **④Saga 对标**：高密摄像柜 PoE（私营段）
- **⑤在乎与偏好**：集成能力

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“AI-Powered Surveillance…IP Video Surveillance, Fire Detection, Access Control, Networking, and IT Solutions”
  > “AI-Powered Surveillance…IP Video Surveillance, Fire Detection, Access Control, Networking, and IT Solutions”
  > 来源：https://www.watkins-security.com/
- **【风险与注意】**Past Clients：US Department of Homeland Security（联邦红线不涉）/US Open/G20 Pittsburgh/Vail
  > Past Clients：US Department of Homeland Security（联邦红线不涉）/US Open/G20 Pittsburgh/Vail
  > 来源：https://www.watkins-security.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Watkins 60 年安防：场馆高密摄像柜 PoE（$165 锚点一致）；DHS 联邦红线不触 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：战绩
- **W**：红线
- **O**：场地
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
Hi Watkins team,

From the US Open to Vail resorts - venues of that density tell camera-closet stories most integrators never see.

We build a 24-port Gigabit PoE switch (280W, 802.3af/at, watchdog, Voice VLAN) for exactly those closets, at a value price point. Reference: $165 USD EXW. (To be explicit: we work strictly in the private commercial segment and do not pitch into federal engagements.)

One question: at a venue-scale deployment, how many cameras land on one access switch for you?

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
