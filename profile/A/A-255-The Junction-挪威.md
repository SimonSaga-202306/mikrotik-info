# The Junction

> **评级 A**　|　挪威 · Drammen　|　档案编号 `A-255`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-255
rating: A
country: 挪威
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — The Junction 挪威专科分销 30+年（IT 基建板块明列工业管理交换机/PoE+Perle）：Perle 旁替补窄口（$180 锚点一致）；alt STI-288GP；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | The Junction（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 挪威 / Drammen | 事实 |
| 网站 | https://thejunction.eu | 事实 |
| 类型 | 分销/集成商（Perle 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】The Junction AS（挪威 Drammen，30+年）：专科硬件分销欧陆+斯堪的纳维亚——连接/嵌入式/ATC/录音/加固屏五块；IT Infrastructure 板块明列 media converter/Ethernet extender/工业管理型交换机/PoE/console server/LTE-5G 路由；品牌含 Perle/Connect Tech/Bluestone
- 【推断】IT 基建板块存在'工业管理型 PoE'明栏——STC-424 与 Perle 并排替补是正位窄口（批 26 分销双雄之一）
- 【假设】其 IT 基建板块的 value 替补槽：Perle 旁不撞车的工程件

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@thejunction.eu
  - 状态：既有/公开
- **电话**：+47 40 40 34 02
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@thejunction.eu（官网正文公开）；原入口：+47 40 40 34 02
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · Perle 类目外档：商业 L2+ 24 口 PoE 一页

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：认可 Perle 主关的短件：他们报价单缺商业级 24 口 PoE 类时，我们作为第二来源价位档（上架提案+分销条件）。
- **要问的问题**：客户问商业办公 24 口 PoE 时，你们报价指向哪里？
- **随附证明**：一页报价+规格（英）+ 分销条件。

### 第 2 次跟进 · 工业 ERPS 环第二来源

- **推什么**：STI-480DGGM（Saga）（工业管理 8×电口 + 4×千兆上联，ERPS）
- **切入点**：Perle 工业线邻位：环网协议件与高功率 PoE++ 价位档。
- **要问的问题**：ERPS 环网项目有第二价位档吗？
- **随附证明**：ERPS 配置示例一页（英）。

### 第 3 次跟进 · 现场宽温小件窄线

- **推什么**：STI-280GE（Saga）
- **切入点**：机柜/现场宽温小件窄线窄提案；不回即冻结。
- **要问的问题**：—
- **随附证明**：窄线一页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第13批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：德拉门老牌专业分销：**Perle 在供应商页坐实**（1976 起/Phoenix Contact 集团）；ATC/防务面划出。
- **产品线与在售品牌**：Perle 全线+Connect Tech 嵌入式+Bluestone 军屏+Cadmos 空管+FarSite/OptiLogix/Sangoma。
- **目标行业与场景**：工业/嵌入式/串口联网高端客群；空管/防务面不涉。
- **团队与规模**：中型专业分销（新闻门户+翻页目录体系）。
- **决策链与对接人**：info@thejunction.eu（官网 Contact and quotation request 页，CSV 9-27）。
- **技术与认证**：Perle 分销（CSV+官网供商页双证）。
- **采购与供应链信号**：Perle 深绑：IT Infra 类目=Perle SKU 主场——只谈**商业级 L2+ 24 口 PoE 接入层与 ERPS 环**（Perle 之外的类目档），禁替位话术。
- **近期动态与线索**：官网 2026 新版+新闻门户三档更新=上新窗口常态。
- **与我方契合点**：商业 L2+ 接入层（Perle 类目外的价位档）；机柜/户外 ERPS 环第二来源。
- **风险与注意**：ATC/空管/防务显示面完全不碰；与 Perle 主关系一句话认可、不质损。

### R54 原文证据摘录（全部保留）

- **【业务定位】**德拉门 30+ 年硬件/软件专业分销（欧洲+斯堪的纳维亚）：七大应用区 Embedded/Connectivity/IT Infrastructure/Monitors/**ATC 空管**/UC/TDM 录音。
  > The Junction supplies specialist hardware and software for data connectivity, embedded computing, air traffic control, voice recording and rugged display systems across Europe and Scandinavia.
  > 来源：https://thejunction.eu/
- **【产品线与在售品牌】**供应商页确凿：**Perle — since 1976, Phoenix Contact group**（串口服务器/控制台/光纤收发/以太延伸/工业交换/LTE-5G）；另 Connect Tech（NVIDIA Jetson Elite）/Bluestone 军规屏/Cadmos（空管）/FarSite/OptiLogix/Sangoma。
  > Perle — Device networking since 1976 · Phoenix Contact group. Serial-to-Ethernet device servers, console servers, fiber media converters, Ethernet extenders, industrial switches and LTE/5G routers.
  > 来源：https://thejunction.eu/
- **【风险与注意】**ATC 空管与军规/防务显示用例在应用区——**ATC/防务面完全划出不涉**（仅走商业 IT Infra 类目）。
  > Air Traffic Control — Rugged compute... for ATC and radar data infrastructure ‖ Monitors... for marine, industrial and defence use
  > 来源：https://thejunction.eu/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第26批.json`；价格均为 EXW 快照。

- **①背景再核**：NO 专科分销（官网一手核）
- **②芯片/型号**：Perle 等专科墙
- **③KP 深挖**：info@
- **④Saga 对标**：替补窄口（$180 锚点一致）
- **⑤在乎与偏好**：深度选型/僻域覆盖

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**IT Infrastructure: Fiber media converters, Ethernet extenders, industrial managed switches, PoE, console servers, LTE/5G routers——Perle 1976
  > IT Infrastructure: Fiber media converters, Ethernet extenders, industrial managed switches, PoE, console servers, LTE/5G routers——Perle 1976
  > 来源：https://thejunction.eu

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：挪威专科硬件分销（30+年）
- **产品线与在售品牌**：Perle 等专科品牌
- **目标行业与场景**：工厂/海事/ATC/录音等僻域
- **团队与规模**：专科分销团队
- **决策链与对接人**：info@ 口
- **技术与认证**：专科选型深度
- **采购与供应链信号**：分销泳道
- **近期动态与线索**：ATC/嵌入式新板块扩展
- **与我方契合点**：IT 基建板块 value 替补（Perle 旁守界前句）
- **风险与注意**：专科主线分量强——前句框定

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | The Junction 挪威专科分销 30+年（IT 基建板块明列工业管理交换机/PoE+Perle）：Perle 旁替补窄口（$180 锚点一致）；alt STI-288GP |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：分量
- **O**：替补
- **T**：Perle

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
  - [ ] Perle 排他

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi The Junction team,

Thirty-plus years of specialist distribution - media converters, extenders, industrial managed switches, PoE, console servers - Perle on the shelf and ATC/rugged lines beside. One sentence up front: we are not asking to displace Perle.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation, plus an 8-port industrial unmanaged PoE line. Reference: $180 USD EXW (2026-09-29) - the value substitute slot beside your specialist tier.

One question: does your IT Infrastructure board keep a value substitute tier - and would you evaluate one unit?

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
