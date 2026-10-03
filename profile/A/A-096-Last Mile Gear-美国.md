# Last Mile Gear

> **评级 A**　|　美国 · Washington　|　档案编号 `A-096`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-096
rating: A
country: 美国
biz_org: 个体顾问（无官网）
business_model: 顾问项目制
decision_speed: fast
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；顾问项目制
- **商业模式**：顾问项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长），三星重点
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Last Mile Gear→已并入 WAV 集团（301+同 MX 设施双信号）：Netonix-out 纪律建档；WAV 入口价值留档；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Last Mile Gear（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Washington | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | WISP 集成商/代理（Netonix） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Netonix 授权渠道（WISP 接入层交换机） | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Last Mile Gear（美国）：Netonix 授权渠道（WISP 接入层交换机）；**lastmilegear.com 现 301 至 wavonline.com——WAV 为美国头部 WISP/ISP 分销（$25M+ 在仓、70K SKU、1 万客户、35+ 年；RUCKUS/viaPhoton/Cambium/Tarana 全谱）；两域共享同一 ppe-hosted 邮件基础设施（并入信号强）**；CSV：sales@lastmilegear.com 双向印证（官网+X @LastMileGear）
- 【推断】LMG 疑并入 WAV 集团：sales@lastmilegear.com 邮箱仍活（MX 同 WAV 设施），邮件大概率有 WAV 团队接收——但 Netonix-out 纪律优先
- 【假设】WAV 庞大的 WISP 客群是反向观察样本；用户口径放开后其价值相当于“WAV 的入口”

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Netonix 授权渠道（WISP 接入层交换机））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@lastmilegear.com
  - 状态：既有/公开
- **电话**：—
- **原始联系字段**：sales@lastmilegear.com（官网与 X（@LastMileGear）双向印证；另有 info@lastmilegear.com(发不过去·2026-09-29 退信:地址不存在 not-found)。自述卖 Cambium / SAF 等 WISP 设备）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。


- **退信实测（2026-09-29）**：`info@lastmilegear.com` 地址不存在（address couldn't be found / unable to receive mail）→ 停用该地址；替代通道：sales@lastmilegear.com（官网与 X(@LastMileGear) 双向印证，CSV 主联系）
  > 处置：info@ 判定不存在→永久停用；主通道=sales@；X 私信作第三通道
## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 品类空缺（交换类目价位段提案，经原 LMG 关系人引荐）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行） / STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：借原 Last Mile Gear 联系人引荐进 WAV：货架交换类目的高性价比空档+工业 PoE，附类目建议书与商业段合规说明。
- **要问的问题**：能否帮忙引荐 WAV 交换类目采购？（先发类目一页纸）
- **随附证明**：类目建议书 + 公司介绍 + 合规边界说明（英文）。

### 第 2 次跟进 · 工业非管理 PoE（塔站货架 SKU）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：WISP 塔站/室外箱的宽温 DIN PoE：SKU 少而精（3–5 个型号起），动销逻辑与 Cyclone 防雷件同货架。
- **要问的问题**：塔站类件的动销 KPI 怎么定？先上哪几款？
- **随附证明**：货架提案（型号/价位/毛利）+ 宽温报告 + 营销物料。

### 第 3 次跟进 · 管理型 10G（汇聚段类目扩展）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：类目扩展：管理型 8G+4×10G 给 WISP 客户的汇聚/机房段，配渠道培训与项目注册。
- **要问的问题**：汇聚/机房段的供应商现在是谁？RUCKUS 价位段下有空间吗？
- **随附证明**：同档价差对照 + ERPS 实测 + 渠道培训计划。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第5批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：原 Last Mile Gear 已并入 WAV（WISP/ISP 头部分销商）——按 WAV 口径推进，体量与货架深度远超普通渠道户。
- **产品线与在售品牌**：7 万 SKU：Cambium/Tarana/RUCKUS/Cyclone/viaPhoton/NetPoint 等+机柜分光防雷全套周边；交换类目在售（RUCKUS 主打）。
- **目标行业与场景**：美国 WISP/ISP/MSP 渠道：固定无线、private LTE、光纤配套、机房机柜——塔站到机房全覆盖。
- **决策链与对接人**：原 LMG 联系人线索：sales@lastmilegear.com、info@、X @LastMileGear（CSV 9-27 记录）；WAV 总机 800-678-2419。
- **团队与规模**：WAV 集团化（多仓现货：College Station TX / West Chicago IL 等），1 万+客户关系。
- **技术与认证**：成熟渠道认证体系（BABA 合规标识可见于部分在售品）；Netonix 历史渠道（CSV 记录）。
- **采购与供应链信号**：上架评估逻辑（品牌/价位段/合规）；⚠️ 页面可见 BABA 合规标——美国政府单段会排除非合规货，商业 WISP 段可谈。
- **近期动态与线索**：收购整合期：LMG 品牌跳转归并，货架在重排——新进品牌的窗口通常开在整合后 6–12 个月。
- **与我方契合点**：交换类目里「高性价比管理型+工业 PoE」价位空档：以品类提案+商业 WISP 段切入，绕开 BABA 约束段。
- **风险与注意**：大分销商周期长：先找到原 LMG 关系人过渡引荐（X/邮箱），不走冷冰冰的供应商注册表；合规边界先讲清。

### R54 原文证据摘录（全部保留）

- **【近期动态与线索】**lastmilegear.com 抓取已整站跳转至 wavonline.com——品牌已并入 WAV（头部 WISP/ISP 分销集团），原门户不再独立运营。
  > （lastmilegear.com → wavonline.com 整站跳转）Top Wireless Equipment Distributor For WISP & ISP
  > 来源：https://www.lastmilegear.com/
- **【业务定位】**WAV 官网定位：有线+无线设备分销商，专注把终端客户接上互联网（private LTE/FWA/交换/Wi-Fi/光纤）。
  > We are a wired and wireless equipment distributor specializing in connecting your customers to the Internet. From private LTE to fixed wireless broadband, network switches, Wi-Fi, and fiber, we partner with top manufacturers to help your business succeed.
  > 来源：https://www.wavonline.com/
- **【团队与规模】**体量数字：2500 万美元+日常现货、7 万+ SKU、1 万+信任客户、35+ 年经验——美国 WISP 分销头部。
  > $25+ Million Daily On Hand Inventory · 70,000 + SKUs Available · 10,000+ Trusted Customers · Over 35+ Years Of Experience
  > 来源：https://www.wavonline.com/
- **【产品线与在售品牌】**在推品牌：RUCKUS（交换促销横幅）、Tarana、Cambium、Cyclone、viaPhoton 等；机柜/分光器等周边齐全。
  > RUCKUS Full Speed Switching Promo（首页横幅）· Tarana Wireless 6GHz Remote Node Bundle · Cambium Networks ePMP 3000 · Cyclone 36U Cabinet
  > 来源：https://www.wavonline.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第10批.json`；价格均为 EXW 快照。

- **①背景再核**：LMG→疑似并入 WAV；两域邮件设施同群
- **②芯片/型号**：Netonix 历史/WAV 全谱
- **③KP 深挖**：sales@ 箱仍在
- **④Saga 对标**：—
- **⑤在乎与偏好**：—

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**lastmilegear.com → wavonline.com（301）；WAV：$25M+ on-hand inventory / 70,000+ SKUs / 10,000+ customers
  > lastmilegear.com → wavonline.com（301）；WAV：$25M+ on-hand inventory / 70,000+ SKUs / 10,000+ customers
  > 来源：https://www.wavonline.com/
- **【联系方式】**sales@lastmilegear.com；两域 MX 同为 mx1-us1.ppe-hosted.com（并入信号）（MX/DNS 级核验：域存活=邮件可投递到域）
  > sales@lastmilegear.com；两域 MX 同为 mx1-us1.ppe-hosted.com（并入信号）（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://www.lastmilegear.com/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：LMG：Netonix 渠道→已并入 WAV 集团（疑似）
- **产品线与在售品牌**：Netonix（历史）+WAV 全谱
- **目标行业与场景**：WISP/ISP/MSP
- **团队与规模**：集团规模
- **决策链与对接人**：sales@lastmilegear.com（箱仍在）
- **技术与认证**：—
- **采购与供应链信号**：集团级
- **近期动态与线索**：域名 301 至 WAV+邮箱基础设施同群
- **与我方契合点**：纪律建档（潜在 WAV 入口价值）
- **风险与注意**：Netonix-out 纪律

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Last Mile Gear→已并入 WAV 集团（301+同 MX 设施双信号）：Netonix-out 纪律建档；WAV 入口价值留档 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：—
- **W**：—
- **O**：WAV 入口
- **T**：—

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
  - [ ] 并入正式口径
  - [ ] 口径放开后路径

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
（不出信——Round-28 Netonix-out 纪律。备注：若放开，WAV 作为 1 万客户的 WISP 大分销，其 value PoE 档位空缺值得以集团名义进函。）
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

> 找新邮箱方法(R60 用户授权留存):① 官网 contact/about 页重扫;② Hunter.io 扫域名公开邮箱;③ 领英私信 KP(本档 R60 区块有直达链);④ 按 firstname.lastname@域名 格式推断并用 verify 工具核;⑤ 总机电话转 KP 直线

---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:[Last Mile Gear · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Last%20Mile%20Gear)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 高(Covered List+SECURE Act+§301 关税;采购方警惕中国标签,话术锚 Marvell(美企)+FCC);战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:待定(档案无芯片信号,首开先问品牌谱)
- **大概率用到的 Saga 型号**:大概率会用: STI-288GP(工业导轨 24G+4×10G→机柜/自动化)、STC-424XGGPM-280W(48G PoE++/4×25G→智算安防酒店全谱)(批量潜力高,可上 280W 旗舰对照行)(本行为调查分析结论,与开发信首推型号是两回事)
