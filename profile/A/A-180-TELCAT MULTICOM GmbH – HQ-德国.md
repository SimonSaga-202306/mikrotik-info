# TELCAT MULTICOM GmbH – HQ

> **评级 A**　|　德国 · Salzgitter　|　档案编号 `A-180`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-180
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 主场景匹配+首触只推一个型号的纪律；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | TELCAT MULTICOM GmbH – HQ（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Salzgitter | 事实 |
| 网站 | https://www.telcat.de | 事实 |
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

- **邮箱**：info@telcat.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@telcat.de [Publicly listed; delivery not tested]; https://www.telcat.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（商业 IT/网项目接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：酒店/商业项目的网络段：24 口 PoE++ 规格对照+合规文件包；声明消防与 Digitalpakt 公立项目段不供。
- **要问的问题**：商业 IT/网项目的接入层现在配什么？（边界声明随附）
- **随附证明**：边界声明 + 规格对照 + CE 文件包（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（周界/监控室外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：周界/室外监控点位：宽温 DIN PoE+备件包。
- **要问的问题**：周界点位的坏机率？
- **随附证明**：宽温报告 + 备件包价（德文）。

### 第 3 次跟进 · 管理型 PoE（商业分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：商业项目的安全网分段标准件：VLAN/ERPS 模板+样机进工程库。
- **要问的问题**：商业分段模板要不要进工程库？
- **随附证明**：VLAN/ERPS 模板 + 样机（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第9批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：萨尔茨吉特总部、全国多站点的大型 ITK 系统屋：安全基础设施+消防+反无人机+总承多工种，Allied Integrate/Resell（CSV 记录）。⚠️ 集团采购链风险保留（CSV）。
- **产品线与在售品牌**：IT 安全/网络/视频监控分析/门禁/报警/消防/反无人机/充电桩线。
- **目标行业与场景**：酒店/医疗/学校（Digitalpakt 公共段划线）/商业地产项目；安全关键设施客户群。
- **团队与规模**：大型集团（全国站点图+中央招聘）。
- **决策链与对接人**：info@telcat.de（CSV 9-27：联系页匹配 Salzgitter 总部）。
- **技术与认证**：Allied Integrate/Resell（CSV 记录）；Lancom 伙伴（官网项目）。
- **采购与供应链信号**：视频/周界/门禁 IP 项目的接入层刚需；⚠️ 消防（生命安全）段与 Digitalpakt 公立项目段不供（首节声明）；反无人机项只做商业 IT 网段分寸内。
- **近期动态与线索**：Brandmeldertausch 换新潮营销+反无人机新线布。
- **与我方契合点**：酒店/商业项目的 IT/网件与监控周界的工业 PoE——大集团项目流里打配套。
- **风险与注意**：集团大合规强：文件包/供应商登记流程走全；生命安全与公立项目段坚决不碰。

### R54 原文证据摘录（全部保留）

- **【团队与规模】**官网自述：「德国最大 ITK 系统屋之一」——多站点全国集团，免费 0800 服务号+充电桩专档。
  > Die TELCAT Unternehmensgruppe zählt zu den größten ITK-Systemhäusern Deutschlands. ‖ Zentrale +49 5341 21-191 88 · Service +49 800 8888-100
  > 来源：https://www.telcat.de/
- **【产品线与在售品牌】**主板块「安全基础设施」：IT 安全/安全网络/监控与视频分析/门禁/**⚠️消防（Brandmeldetechnik）**/报警/**无人机防御**——生命安全与安防敏感风光并存。
  > SICHERE INFRASTRUKTUR — von IT-Sicherheit und sicheren Netzwerken über Videoüberwachung, Zutrittskontrolle, Brandschutz, Alarmierung bis hin zur Drohnenabwehr… Brandmeldertausch（专页）· Drohnenabwehr（专页）· Perimeterschutz
  > 来源：https://www.telcat.de/
- **【目标行业与场景】**项目格：Helmstedt 小学 WLAN（**Digitalpakt Schul** 公共项目，Lancom 伙伴）/Buff 医疗度假村消防/SCHAUMWERK 洗车楼消防总包/Holiday Inn Wiesbaden 12 工种 IT+媒体总包。
  > Neues WLAN für Wissbegierige! In Helmstedts Grundschulen… dank Mitteln aus dem Digitalpakt Schule. Mit dem Partner Lancom startet TELCAT ein Projekt für die Zukunft. ‖ Holiday Inn Express Hotel Wiesbaden… übernahm die Generalunternehmerschaft von insgesamt 12 Gewerken.
  > 来源：https://www.telcat.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第18批.json`；价格均为 EXW 快照。

- **①背景再核**：大型 ITK 集团（酒店随单为主，Digitalpakt 守界）
- **②芯片/型号**：Lancom 等
- **③KP 深挖**：info@+全国站点
- **④Saga 对标**：私营工程随单 value 位（学校红线守界）
- **⑤在乎与偏好**：工程级文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“TELCAT Unternehmensgruppe zählt zu den größten ITK-Systemhäusern Deutschlands…Holiday Inn Express…12 Gewerke…Neues WLAN für Helmstedts Grundschulen…Digitalpakt Schule”
  > “TELCAT Unternehmensgruppe zählt zu den größten ITK-Systemhäusern Deutschlands…Holiday Inn Express…12 Gewerke…Neues WLAN für Helmstedts Grundschulen…Digitalpakt Schule”
  > 来源：https://www.telcat.de/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：总包
- **W**：墙
- **O**：私营
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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi TELCAT team,

From a 12-trade general-contracting build for Holiday Inn Express to fire-alarm systems for medical resorts - your private-sector engineering projects run on network closets that never make the brochure but never get to fail either. (For clarity: your Digitalpakt school work stays fully out of scope here; this concerns your commercial engineering projects only.)

We manufacture a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with a complete engineering dossier. Reference: $165 USD EXW.

One question: in your commercial engineering projects - hotels, facilities, security builds - which switch brand holds the PoE access layer today, and does supplier onboarding run through individual branches or Group procurement?

If useful, I can send one unit with the complete dossier. If not a fit, one line and I close the loop.

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
