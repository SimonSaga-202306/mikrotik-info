# A3 Communications

> **评级 A**　|　美国 · Cumberland Foreside, ME　|　档案编号 `A-113`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-113
rating: A
country: 美国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — A3/CBX 美全国楼宇集团：安防/网络一体接入柜（$165 锚点一致）；集团采购中心化注意；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | A3 Communications（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Cumberland Foreside, ME | 事实 |
| 网站 | https://www.cookandboardman.com/division/a3-communications | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：salesteam@a3communications.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：salesteam@a3communications.com [Publicly listed; delivery not tested]; https://www.cookandboardman.com/division/a3-communications
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（私立教育/商业项目接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：整合期递信：私立教育/商业项目（非共购合同）的 24 口接入层成本对照+适用边界声明（TAA 段不供）。
- **要问的问题**：私立/商业项目的接入层用什么？（附 TAA 边界声明）
- **随附证明**：适用边界声明 + 单端口测算 + 规格对照（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（体育场/停车室外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：体育馆外场与停车场的摄像头/门禁：宽温 DIN PoE 严寒缅因州也扛得住。
- **要问的问题**：外场点位的坏机率与维护成本？
- **随附证明**：宽温报告 + 坏机测算 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（商业段标准件+项目注册）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：商业段的 VLAN/ERPS 标准件+项目注册制，绕开共购合同体系单。
- **要问的问题**：商业项目走项目注册供货行不行？
- **随附证明**：项目注册政策 + VLAN/ERPS 模板（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第6批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：近 40 年安防+网络集成商，现为 Cook & Boardman 集团（CBX Solutions 新品牌）分支；CSV 记录 Cumberland Foreside ME 办事处——在全国多点运营。
- **产品线与在售品牌**：电子安防与通信（Division 27/28）+门五金+预施工/安装/售后全家桶；Genetec 生态；Allied 代理（CSV 记录）。
- **目标行业与场景**：K-12/高校体育设施、公共安全（法警/警局）、商业楼宇；共购合同覆盖 FL/HI/ME/MO/NV/NM/SC/TN 多州。
- **团队与规模**：集团化（CBX 全国分支网络），工程师评估框架标准化（官网）。
- **决策链与对接人**：salesteam@a3communications.com（CSV 9-27 核验：集团官网明确列出 Cumberland ME 办事处及该邮箱）。
- **技术与认证**：Allied 代理（CSV 记录）；NASPO/Sourcewell/TIPS 供应商资质。
- **采购与供应链信号**：⚠️ 共购合同（NASPO/Sourcewell）通常要求 TAA 合规——公共采购段基本不可行；商业/私立教育段可谈。
- **近期动态与线索**：集团品牌升级 CBX Solutions（跳转中）→ 采购归并期，供应商清单重排。
- **与我方契合点**：商业/私立教育项目的接入层与体育场馆室外点位；整合期递「第二货源」资料。
- **风险与注意**：别混用同名公关公司域名（CSV 提醒）；公共合同段（NASPO/TIPS 下的单）一律不做；跟进对象为 ME 办公室线索。

### R54 原文证据摘录（全部保留）

- **【近期动态与线索】**a3communications.com 抓取已整站跳转至 cbxsolutions.com（Cook & Boardman 集团品牌升级为 CBX Solutions）——组织整合期。
  > （a3communications.com → cbxsolutions.com 跳转）A3 COMMUNICATION-Irmo | CBX SOLUTIONS 700
  > 来源：https://www.a3communications.com/
- **【业务定位】**集团分支页自述：近 40 年为全美客户定制网络与安全方案。
  > For nearly four decades, A3 Communications has created custom networking and security solutions for customers across the US.
  > 来源：https://www.cbxsolutions.com/branches/irmo-700/
- **【采购与供应链信号】**⚠️ 共购合同矩阵：NASPO ValuePoint/Sourcewell/TIPS/多州合同（南卡 HPE 网络产品、Cisco、Juniper、Ruckus 等）——公共采购渠道深厚。
  > Co-Operative Purchasing Programs: NASPO ValuePoint Security & Fire Protection Services · Sourcewell Technology Products and Services (121923A3C) · TIPS - Technology Solutions Products and Services ‖ South Carolina: Cisco Hardware and Software Products and Services · HPE Network Products and Services · Juniper Networks Hardware & Software · Ruckus Wireless
  > 来源：https://www.cbxsolutions.com/branches/irmo-700/
- **【目标行业与场景】**代表项目：克莱姆森大学体育馆（门禁+视频+生物识别）、Richmond County 法警办公室（与 Genetec 合作）——教育体育+公共安全双场景。
  > Jervey Gym and Watt Family Performance and Wellness Center — Owner: Clemson University · Richmond County Marshal’s Office — partnering with Genetec, we streamlined the security infrastructure
  > 来源：https://www.cbxsolutions.com/branches/irmo-700/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第12批.json`；价格均为 EXW 快照。

- **①背景再核**：CBX 全国集团（A3 为安防/网络事业部）；2025 更名整合
- **②芯片/型号**：Allied 信号（网络事业部接入层）
- **③KP 深挖**：salesteam@a3（CSV）
- **④Saga 对标**：楼宇接入柜 value 位
- **⑤在乎与偏好**：集团认证+文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Integrated commercial openings, security, and technology - delivered as one…structured cabling, network infrastructure, and A/V systems…National Presence. Local Service.”
  > “Integrated commercial openings, security, and technology - delivered as one…structured cabling, network infrastructure, and A/V systems…National Presence. Local Service.”
  > 来源：https://www.cbxsolutions.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | A3/CBX 美全国楼宇集团：安防/网络一体接入柜（$165 锚点一致）；集团采购中心化注意 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：管线
- **W**：集权
- **O**：整合窗
- **T**：在位

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
Hi A3 / CBX Solutions team,

Congratulations on the rebrand into CBX Solutions - uniting doors, security and network technology under one national team is a big, well-timed move.

Where access control and video surveillance meet structured cabling, there is a PoE access cabinet on every floor. That is the switch we build: 24-port, 280W, 802.3af/at, Voice VLAN, watchdog. Reference: $165 USD EXW.

One question: across CBX network-solutions projects, who supplies the PoE access switches today?

If useful, I can send one unit with the full compliance and documentation pack for evaluation. If not a fit, one line and I close the loop.

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
