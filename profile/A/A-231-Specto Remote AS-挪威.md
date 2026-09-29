# Specto Remote AS

> **评级 A**　|　挪威 · Oslo　|　档案编号 `A-231`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-231
rating: A
country: 挪威
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
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Specto Remote 挪威海事/离岸/水产（Mowi/Cermaq 私营渔场）：监控机柜 PoE 正口+备件仓库叙事（$165 锚点一致）；alt STI-288GP 恶劣工况；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Specto Remote AS（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 挪威 / Oslo | 事实 |
| 网站 | https://spectoremote.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Specto Remote AS（挪威 Oslo+Bodø）：海事/离岸/水产养殖网络——Viking Line/Mowi/Cermaq 客户（商业养鱼场=私营）；机柜/点对点天线/监控/对讲全案
- 【推断】水产养殖私营关键场景：鱼场监控机柜=PoE+恶劣半户外接入，正位
- 【假设】鱼场/码头监控机柜的 PoE 接入随单（双城仓有备件叙事实锤）

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：post@spectoremote.com
  - 状态：待核·未验证投递（不进群发）
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：post@spectoremote.com（官网正文公开；未验证投递）；原入口：见 alliedtelesis.com 伙伴页
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 严酷环境工业件对口（监控杆/养殖机柜）

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温 DIN）
- **切入点**：给 SpectoWatch 杆与养殖机柜配套：-40~75°C 宽温小交换+PoE++，一箱试样起。
- **要问的问题**：SpectoWatch 杆和渔场机柜里现在用哪个牌子的小交换？
- **随附证明**：宽温件一页（英）+ 温度/IP 等级规格 + CNY 到岸价。

### 第 2 次跟进 · 巡检走廊 ERPS 环网

- **推什么**：STI-480XGGM（Saga）（工业管理 8×电口 + 4×万兆，ERPS）
- **切入点**：渔场/码头多点位的管理型 ERPS 环：断纤自愈+万兆上联视频回传。
- **要问的问题**：多点位视频回传有没有环网/断纤自愈需求？
- **随附证明**：ERPS 环网图示一页 + 配置速查（英）。

### 第 3 次跟进 · 备件库常备协议

- **推什么**：常备件清单（工业 8 口×5 + 收发器×10 + SFP 若干）
- **切入点**：按其备件仓习惯给常备件价格协议+快速补货条款。
- **要问的问题**：备件仓常备件走框架价还是按单？
- **随附证明**：常备件协议模板 + 阶梯价。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第12批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：挪威严酷环境网络商：Allied Resell（CSV 记录）；水产/海事场景=工业宽温件天然对口。
- **产品线与在售品牌**：海事/养殖联网+监控杆+对讲+办公网；无交换机品牌墙（采购走项目）。
- **目标行业与场景**：渡轮航线/养殖网箱/渔港/办公室四类私营场景。
- **团队与规模**：中小工程队（双址+备件仓+招聘中）。
- **决策链与对接人**：post@spectoremote.com / support@（官网正文，CSV 9-27）。
- **技术与认证**：Allied Resell（CSV）。
- **采购与供应链信号**：严酷环境=宽温/防腐蚀/直流供电刚需件常备；备件仓习惯=接受常备件合作。
- **近期动态与线索**：站上 2026-04 新照片+招聘岗位=活跃扩张窗口。
- **与我方契合点**：SpectoWatch 杆内与养殖机柜的 8 口 PoE++ 宽温件；巡检走廊 ERPS 环网；备件库常备协议。
- **风险与注意**：Nor 市场体量小但项目毛利高：报 CNY+运费到岸一口价，明确宽温/防盐雾参数。

### R54 原文证据摘录（全部保留）

- **【业务定位】**奥斯陆双址（+Bodø 分部）的严酷环境网络专营商：监控/离岸/海事/水产养殖场景设计。
  > We design reliable networking and communication systems for surveillance, offshore, maritime, and aquaculture, ensuring seamless connectivity in challenging environments.
  > 来源：https://spectoremote.com/
- **【目标行业与场景】**渡轮航线联网（客户墙 Viking Line）/养殖场（Mowi、Cermaq）/SpectoWatch 防盗 360° 监控杆/办公网/对讲——均为私营商业客户面。
  > Maritime Networking ... internet connectivity for marine traffic... on ferry's routes and by the ports ‖ Fish-farm Networking ‖ SpectoWatch is our theft problem solving solution... 360 view angle... vandalism proof
  > 来源：https://spectoremote.com/
- **【团队与规模】**Oslo 总部（Nils Hansens vei 5）+ Bodø（Tømrerveien 8）双址；备件仓库充足；站上在招人=扩张期。
  > Nils Hansens vei 5, 0667 Oslo ‖ Tømrerveien 8, 8004 Bodø ‖ Our warehouse is fully equipped with spare parts... Want to join our team?
  > 来源：https://spectoremote.com/
- **【决策链与对接人】**contact /support 分箱明确（CSV 9-27 官方）；两地址各自电话。
  > contact: post@spectoremote.com ‖ support: support@spectoremote.com ‖ +47 230 51 990 (Oslo) ‖ +47 469 03 532 (Bodø)
  > 来源：https://spectoremote.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第24批.json`；价格均为 EXW 快照。

- **①背景再核**：挪威海事水产专案（官网一手核）
- **②芯片/型号**：监控/天线集成
- **③KP 深挖**：post@
- **④Saga 对标**：机柜 PoE 正口（$165 锚点一致）
- **⑤在乎与偏好**：恶劣环境可靠/备件

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**Maritime/offshore/aquaculture networking——clients: Viking Line, Mowi, Cermaq；warehouse spare parts
  > Maritime/offshore/aquaculture networking——clients: Viking Line, Mowi, Cermaq；warehouse spare parts
  > 来源：https://spectoremote.com

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：挪威海事/水产网络专案商
- **产品线与在售品牌**：监控/天线/机柜集成
- **目标行业与场景**：渔场（Mowi/Cermaq)/码头/离岸
- **团队与规模**：Oslo+Bodø 双点
- **决策链与对接人**：post@ 口
- **技术与认证**：—
- **采购与供应链信号**：项目随单+仓库备件实锤
- **近期动态与线索**：SpectoWatch 防盗监控产品
- **与我方契合点**：鱼场机柜 PoE 正口
- **风险与注意**：恶劣环境需宽温注意（标注）

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Specto Remote 挪威海事/离岸/水产（Mowi/Cermaq 私营渔场）：监控机柜 PoE 正口+备件仓库叙事（$165 锚点一致）；alt STI-288GP 恶劣工况 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：对口
- **W**：宽温待核
- **O**：渔场
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
  - [ ] 宽温需求
  - [ ] 现供品牌

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Specto Remote team,

Maritime, offshore and aquaculture networking - Viking Line, Mowi, Cermaq. Keeping a fish farm or a port connected means living in cabinets at the water's edge, and your spare-parts warehouse story tells me you take that seriously.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29) - built for surveillance-heavy cabinets. For harsher mounting points we also offer an 8-port industrial unmanaged line.

One question: what run the switching in your farm and dock cabinets today - and would a documented value PoE unit earn a spare-shelf slot?

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
