# Péter Major

> **评级 A**　|　匈牙利 · Budapest　|　档案编号 `A-250`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-250
rating: A
country: 匈牙利
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: true, voice: true, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — MacSoft 匈六线集成（网络设计/运维+MikroTik 培训副业）：项目随单（$165 锚点一致）；beszerzes@=匈语采购箱直达；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Péter Major（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 匈牙利 / Budapest | 事实 |
| 网站 | https://macsoft.hu | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证，持 MTCNA MTCRE MTCWE MTCTCE MTCUME MTCIPv6E MTCSE MTCSWE MTCEWE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】MacSoft Kft.（匈牙利）：WiFi 设计测量/网络设计/服务器运维/IT 咨询/MikroTik 官方培训/系统管理员外包六线；团队含无线→服务器→应用开发
- 【推断】集成六线+MikroTik 教师副业——网络设计主业使硬件随单真实存在（生态脚踩但主线对口）；beszerzes@=采购专用箱（匈牙利语）
- 【假设】其网络设计/运维项目的 value PoE 随单（采购箱直达）正位

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证，持 MTCNA MTCRE MTCWE MTCTCE MTCUME MTCIPv6E MTCSE MTCSWE MTCEWE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：beszerzes@macsoft.hu
  - 状态：既有/公开
- **电话**：+36 30 4963340
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：beszerzes@macsoft.hu（关联公司官网入口；个人归属/现任职限制见备注；未测试投递）；原入口：+36 30 4963340
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 直达采购箱：设计 BOM 接入层第二来源一页

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：经 beszerzes@ 直达：其网络设计项目 BOM 的 24 口 PoE 接入层第二来源（匈语/英语一页，规格+交付期+保修一体）。
- **要问的问题**：设计项目 BOM 里的接入层目前有第二来源位吗？
- **随附证明**：一页报价+规格（匈/英）+ 保修/RMA。

### 第 2 次跟进 · WiFi 勘测配套 PoE 与运维备件

- **推什么**：STI-280GE（Saga） 等小批
- **切入点**：WiFi 勘测/运维线的现场小件与备件常备位。
- **要问的问题**：运维备件池走常备价吗？现场有宽温需求吗？
- **随附证明**：备件小批页 + 宽温参数。

### 第 3 次跟进 · 培训线的中性尊重短件（可选）

- **推什么**：STC-424XGGPM-440W（Saga） 演示机（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：随后短件给其 MikroTik 培训线的自用实验位（与采购主件分开、不打扰课程）。
- **要问的问题**：培训实验环境用得上演示机吗？
- **随附证明**：演示机条款一页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第13批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：布达佩斯设计+运维型系统屋（六服务含 MikroTik 官方培训）：**采购专用箱 beszerzes@ 直达**。
- **产品线与在售品牌**：WiFi 勘测/网络设计/服务器运维/外包管理员；MikroTik 培训线。
- **目标行业与场景**：匈牙利企业网设计与运维项目客群。
- **团队与规模**：多学科小团队（无线到服务器到应用开发自述）。
- **决策链与对接人**：beszerzes@macsoft.hu（采购箱，CSV 9-27 官网记录）。
- **技术与认证**：MikroTik 官方培训线（站页）；持 MTCSWE（CSV 9-27）。
- **采购与供应链信号**：**设计=规格定牌、运维=补件消耗**：接入层进其 BOM 位最快；WiFi 勘测热区=PoE AP 配套上行。
- **近期动态与线索**：Demján 计划支持+服务目录完整=稳定增长期。
- **与我方契合点**：网络设计 BOM 的 24 口 PoE 接入层第二来源+运维备件小批。
- **风险与注意**：Demján 程序资金支持面按公共资出注意、该面不经由我们；发送直达采购箱少寒暄。

### R54 原文证据摘录（全部保留）

- **【业务定位】**布达佩斯系统屋六服务：WiFi 设计勘测/IT 咨询/网络设计/网络与服务器运维/MikroTik 官方培训/系统管理员外包——**设计+运维双采购触发位的集成商**。
  > Wifi tervezés és mérés · IT-tanácsadás · Hálózattervezés · Hálózat és szerver üzemeltetés · MikroTik oktatás · Rendszergazda szolgáltatás
  > 来源：https://macsoft.hu/
- **【决策链与对接人】**beszerzes@macsoft.hu=**采购（beszerzés）专用箱**（CSV 9-27：official-company）——预算对口直达，别走信息箱。
  > （CSV 2026-09-27 记录）beszerzes@macsoft.hu（关联公司官网入口）；MacSoft
  > 来源：https://macsoft.hu/
- **【近期动态与线索】**页脚挂 Demján Sándor Program 支持（匈牙利经济计划）——程序支持期=投入扩张窗口（程序资金面按公共资出注意）。
  > A weboldal a Demján Sándor Program keretében és támogatásával valósult meg.
  > 来源：https://macsoft.hu/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第25批.json`；价格均为 EXW 快照。

- **①背景再核**：HU 六线集成商（官网一手核）
- **②芯片/型号**：—
- **③KP 深挖**：beszerzes@ 采购箱
- **④Saga 对标**：value 随单（$165 锚点一致）
- **⑤在乎与偏好**：多技能/项目制

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**Hálózattervezés/Hálózat és szerver üzemeltetés/Wifi tervezés/MikroTik oktatás/Rendszergazda
  > Hálózattervezés/Hálózat és szerver üzemeltetés/Wifi tervezés/MikroTik oktatás/Rendszergazda
  > 来源：https://macsoft.hu

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：匈牙利六线集成商
- **产品线与在售品牌**：—
- **目标行业与场景**：企业网络设计/运维
- **团队与规模**：多技能团队
- **决策链与对接人**：beszerzes@ 采购箱
- **技术与认证**：MikroTik 官方培训身份
- **采购与供应链信号**：项目随单（采购箱实锤）
- **近期动态与线索**：Demján Sándor Program hotel subsidy讲究
- **与我方契合点**：采购箱直达的 value 随单正口
- **风险与注意**：MikroTik 培训副业（话术诚实）

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | MacSoft 匈六线集成（网络设计/运维+MikroTik 培训副业）：项目随单（$165 锚点一致）；beszerzes@=匈语采购箱直达 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：踩脚
- **O**：随单
- **T**：大牌

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
  - [ ] 现供
  - [ ] MikroTik 占比

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi MacSoft team,

Network design, server operations, WiFi planning - with an official MikroTik training line beside. Full honesty on the training side: we build PoE switches, so let me speak directly to your project work, where hardware choice is yours.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29) - a value unit for the networks you design and run. I write to your procurement box on purpose.

One question: which switching line do you specify in projects today - and would a documented value PoE unit earn a test?

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
