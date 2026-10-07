# ATEC Security Ltd

> **评级 A**　|　英国 · Featherstone　|　档案编号 `A-085`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-085
rating: A
country: 英国
biz_org: 个体顾问（无官网）
business_model: 顾问项目制
decision_speed: fast
price_sensitivity: high
volume_potential: 1  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；顾问项目制
- **商业模式**：顾问项目制
- **为什么值得跟**：有明确交换/供电需求（PoE/监控/门禁），且有具体人直联
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — ATEC 英 30 年安防整合（全厂牌）：私营段监控柜 value PoE 补位（$180 锚点一致）；公共段边界；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | ATEC Security Ltd（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Featherstone | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】ATEC Security Ltd（英国）：30+ 年安防系统设计/安装/运维——伙伴墙含 **Allied Telesis（Marvell Prestera 接入层！）**、Axis、Milestone、Siklu、TagMaster、Tyco、Avigilon、Genetec、HID、Abloy 等 40+ 厂牌；市场：机场与边境、政府、交通基建（公共段多）、企业、教育、金融、医疗（公私混）
- 【推断】监控网络柜=其每张单的 PoE 供电层（Axis/Avigilon 摄像机都要）；商用/私营段是合规主巷
- 【假设】30 年老安防商与 Allied 长联播——我们定位为“value PoE 补位货架”，不当 Allied 对标

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@atec-security.co.uk
  - 状态：既有/公开
- **电话**：+44 3300 580 050
- **原始联系字段**：+44 3300 580 050 / info@atec-security.co.uk（备用 compliance@atec-security.co.uk；具名联系人 Michelle Hollinshead（Sales & Marketing Executive））
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（视频监控项目接入层）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：几百路摄像头的项目接入层：24 口 PoE++ + 4×10G 上行的单路成本，配全套合规/质保文件递过去。
- **要问的问题**：当前项目的接入交换机是哪个牌子、单端口到什么价？
- **随附证明**：单路成本测算 + 合规文件包 + 规格对照（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（周界/室外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：机场周界/停车场/库区的室外摄像头：宽温 DIN PoE 即装即走，恶劣环境少坏机=少上门。
- **要问的问题**：室外点位的坏机率一年几台？现在的替换成本？
- **随附证明**：宽温报告 + 备件包价 + 安装图。

### 第 3 次跟进 · 管理型 PoE（安防网段标准化）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：安防 VLAN 隔离+ERPS 冗余的统一模板：跨项目复制省设计工时，给工程师团队做标准件培训。
- **要问的问题**：安防网段与客户办公网的隔离现在怎么做的？
- **随附证明**：VLAN/ERPS 模板 + 收敛实测 + 培训素材（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第5批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：约克郡 30 年安防集成商：视频监控/门禁/入侵/对讲整体方案，Allied Telesis 挂名伙伴，强在高合规行业。
- **产品线与在售品牌**：一站式安防栈（LenelS2/Milestone/Axis/Avigilon/Genetec/Gallagher/HID）+ Allied Telesis 网络层。
- **目标行业与场景**：机场/边境/政府楼/医院/学校/交通枢纽约——全部是 PoE 摄像头成百上千路的项目。
- **团队与规模**：公司化集成商，设计-安装-维保全链条团队；具名联系 Michelle Hollinshead（销售市场，CSV 记录）。
- **决策链与对接人**：+44 3300 580 050 / info@atec-security.co.uk（备用 compliance@）；具名销售联系人（CSV 记录）。
- **技术与认证**：Allied Telesis 生态（Marvell Prestera 接入层）；安防平台多认证。
- **采购与供应链信号**：项目制：大型视频监控随项目批量采购接入层；高合规行业要求供应商文件齐全（产地声明等）。
- **近期动态与线索**：网站案例区挂模板占位文字——营销侧不投入，说明业务稳定、靠关系盘。
- **与我方契合点**：IP 视频接入层=24 口 PoE++ 最标准场景；周界/室外=工业件；合规文件我们随货给。
- **风险与注意**：机场/政府单有产地敏感：先给合规声明包再谈型号；被占域名类的小瑕疵（案例占位文）不要提。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：30+ 年安防系统设计/安装/维护老牌集成商，覆盖多行业。
  > At ATEC, we have been designing, installing and maintaining security systems across a variety of market sectors for more than three decades.
  > 来源：https://atec-security.co.uk/
- **【产品线与在售品牌】**首页品牌墙含 Allied Telesis 与全套主流安防平台——IP 视频/门禁/对讲生态齐全，网络层用 Allied Telesis。
  > LenelS2 · Milestone · Siklu · Synectics · Tyco · 360 Vision · Abloy · Allied Telesis · Avigilon · Axis · Brivo · Commend · Eagle Eye Networks · FLIR · Gallagher · Genetec · HID · IndigoVision · ipsotek（首页品牌墙 Logo）
  > 来源：https://atec-security.co.uk/
- **【目标行业与场景】**机场与边境、政府、医疗、教育、金融、交通基建——高合规行业为主。
  > Airports & Borders · Corporate · Education · Finance & Banking · Government · Private & National Healthcare · Property & Development · Transport Infrastructure
  > 来源：https://atec-security.co.uk/
- **【团队与规模】**首页案例卡片两行仍挂 Lorem ipsum 占位文案——网站维护粗糙，业务靠老客户（如实标注）。
  > Case Study Title Here 3 — Lorem ipsum dolor sit amet, consetetur sadipscing elitr…（首页案例卡片占位文本）
  > 来源：https://atec-security.co.uk/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第9批.json`；价格均为 EXW 快照。

- **①背景再核**：30 年安防全厂牌整合；Allied Telesis 在位；公共段多守住
- **②芯片/型号**：Allied Telesis（Marvell Prestera）
- **③KP 深挖**：info@ 口；电话并行
- **④Saga 对标**：监控柜 value PoE 补位（私营段）
- **⑤在乎与偏好**：长期支持+全案兼容

### R55 证据摘录（全部保留 · 含数量）

- **【产品线】**伙伴墙：Axis, Milestone, Genetec, Avigilon, **Allied Telesis**, Siklu, TagMaster, Abloy 等
  > 伙伴墙：Axis, Milestone, Genetec, Avigilon, **Allied Telesis**, Siklu, TagMaster, Abloy 等
  > 来源：https://atec-security.co.uk/
- **【目标行业】**“Airports & Borders / Corporate / Education / Finance / Government / Healthcare / Property / Transport Infrastructure”
  > “Airports & Borders / Corporate / Education / Finance / Government / Healthcare / Property / Transport Infrastructure”
  > 来源：https://atec-security.co.uk/markets/
- **【联系方式】**info@atec-security.co.uk 0330 0580 050；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > info@atec-security.co.uk 0330 0580 050；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://atec-security.co.uk/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：英国 30 年安防工程商（全厂牌整合）
- **产品线与在售品牌**：Axis/Milestone/Allied Telesis 等 40+ 牌
- **目标行业与场景**：企业/教育/金融/私营医疗（公共段守界）
- **团队与规模**：全国性安防工程商
- **决策链与对接人**：info@ 口
- **技术与认证**：整案集成能力
- **采购与供应链信号**：项目随单（摄像头柜 PoE 是惯件）
- **近期动态与线索**：2026 站常态化
- **与我方契合点**：监控柜 24 口 PoE value 补位
- **风险与注意**：公共段边界+Allied 在位

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | ATEC 英 30 年安防整合（全厂牌）：私营段监控柜 value PoE 补位（$180 锚点一致）；公共段边界 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：全厂牌
- **W**：公共占比
- **O**：随单
- **T**：在位盘

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
  - [ ] Allied 线价位段
  - [ ] 私营段占比
  - [ ] 试点窗

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi ATEC team,

Thirty years of integrated security across 40+ vendor logos - your camera closets are where all of that meets power and cabling.

We build a 24-port Gigabit PoE switch (280W, 802.3af/at, watchdog, Voice VLAN) as a value-tier complement next to your existing network vendors for corporate and private-sector builds. Reference: $180 USD EXW. (We respect your public-sector procurement frameworks and do not pitch into them.)

One question: in a mid-size corporate camera build, which switch supplies the PoE layer today?

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
