# J A Shomer Company

> **评级 A**　|　美国 · OH　|　档案编号 `A-077`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-077
rating: A
country: 美国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — JA Shomer 克利夫兰老分销（Red Lion/HMS/Fieldbus）：温宽 PoE 补件（$74.8 锚点一致）；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | J A Shomer Company（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / OH | 事实 |
| 网站 | jashomer.com | 事实 |
| 类型 | 分销（HMS/N-Tron·Red Lion 渠道） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | N-Tron + Red Lion + Anybus + Ewon | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】J A Shomer Company（美国克利夫兰）：传感器/驱动/传动/盘表控制分销商——电子传感（感应/光电/电容/RFID/编码器、**Fieldbus 通信**、机器视觉）、电力传动（Quantis/Maxum/Tigear 等品牌减速机）、盘表控制（**CUB/PAX/GEM/Apollo 系列=Red Lion 盘表**）、AC/DC VSD 电机（Yaskawa/Baldor/Leeson）；CSV：N-Tron+Red Lion+Anybus+Ewon（HMS）；Charles Zaugg 联络
- 【推断】Fieldbus 通信+Red Lion 盘表+HMS 全家=其工业通信线成形；温宽 PoE 是随其传感/控制单的补件
- 【假设】Cleveland 老线分销；其 Drive 带 Web/Ethernet 通信选件皆需接入层

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：N-Tron + Red Lion + Anybus + Ewon）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@jashomer.com
  - 状态：待核·未验证投递（不进群发）
- **电话**：216-221-4157
- **原始联系字段**：电话 216-221-4157（总机，Charles Zaugg 直线同号）；sales@jashomer.com。President：Charles Zaugg（邮箱按 czaugg@jashomer.com 推测，未验证）
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 工业非管理 PoE（N-Tron 价位段补位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：直打 Red Lion/N-Tron 同规格价差：8 口宽温 DIN PoE 到岸成本约他现售件零头，商业项目做第二供应商不伤原厂关系。
- **要问的问题**：非政府类的产线项目，8 口工业 PoE 你们现在毛利空间被压吗？
- **随附证明**：价差对照（N-Tron 同规格）+ 到岸价目 + 交期（英文）。

### 第 2 次跟进 · 4 口工业 PoE（机器视觉/数采点位）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：机器视觉/数采安装商的零散点位：4 口小机按柜配货，起订量低、混批灵活——分销试单最轻量的一种。
- **要问的问题**：机器视觉项目的点位交换你们随柜配还是客户自购？
- **随附证明**：混批价目 + 宽温报告 + DIN 图。

### 第 3 次跟进 · 管理型 10G（OT 网络分段升级单）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：工厂 OT 网分段与 10G 上行需求上来时：管理型+ERPS+VLAN 打包给他的自动化客户做升级单，项目注册制保价。
- **要问的问题**：客户在 OT 网分段上有没有预算窗口？
- **随附证明**：项目注册政策 + VLAN/ERPS 模板 + 实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：克利夫兰工业分销小公司（1–10 人）：传感器/仪表/传动/驱动四大线，卖进俄亥俄工厂客户，HMS（Red Lion/N-Tron）渠道在册。
- **产品线与在售品牌**：Balluff 传感、Red Lion 面板表/数据采集、Yaskawa/Baldor/Leeson 驱动电机、SensoPart 视觉——工业交换机是他 Red Lion/N-Tron 线的一部分。
- **目标行业与场景**：俄亥俄制造业工厂的产线自动化：机器视觉、数采边缘、HMI 与 PLC 互连——全是工业以太网现场。
- **团队与规模**：1–10 人家庭式分销商（1703 Brookpark Rd / 1951 W 112th St, Cleveland OH 44109，CSV 记录）；老板 Charles Zaugg 直线同号。
- **决策链与对接人**：销售部 216-221-4157 / sales@jashomer.com；小公司总机=老板直线。
- **技术与认证**：分销技术型销售（按工况选型），无交换认证记录；卖 N-Tron/Red Lion 工交多年。
- **采购与供应链信号**：N-Tron 8 口约 $500+ 的价位段 vs 我们工业 8 口中性货约 $91（CSV 测算）——品类补位与第二供应商的账很好算。
- **近期动态与线索**：无公开动态；小而稳，靠老客户关系复购。
- **与我方契合点**：工业 PoE 价差 5 倍的第二供应商切入；机器视觉/数采客户现场需要 PoE 与上行，他能直接打包卖。
- **风险与注意**：⚠️ 中国产地不能做 TAA/NDAA 政府/电力项目（CSV 既有提醒）：只谈商业渠道；首次沟通即主动说明适用边界，反而专业。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网抬头：传感器/读数仪表/驱动与传动产品分销商——典型的俄亥俄工业分销老店。
  > Distributor of Sensors, Readouts, Drives, and Transmission Products · Working with you, making machines work.
  > 来源：https://jashomer.com/
- **【产品线与在售品牌】**电子传感器页品牌墙含 Balluff、Encoder Products、SensoPart，以及 hms-networks.com/red-lion——印证 Red Lion（HMS 旗下，含 N-Tron）渠道关系（原图链接）。
  > 品牌墙外链：balluff.com · encoder.com · hms-networks.com/red-lion · senso-part.com（electronic-sensors 页）
  > 来源：https://jashomer.com/electronic-sensors/
- **【目标行业与场景】**控制与数采产品线：Fieldbus 通信、工业 RFID、机器视觉、数据采集设备、Red Lion CUB/PAX/GEM/Apollo 面板表——工厂自动化边缘网络密集。
  > Human Machine Interface, Process Measurement and Control, Digital Measurement, Fieldbus Communications… data-acquisition devices… CUB, PAX, GEM & Apollo.
  > 来源：https://jashomer.com/
- **【决策链与对接人】**官网订购触点：销售部直线与邮箱。
  > To order, or for further information about our J.A. Shomer products, please contact our Sales Department at 216-221-4157 or email us at sales@jashomer.com
  > 来源：https://jashomer.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第8批.json`；价格均为 EXW 快照。

- **①背景再核**：克利夫兰工控老牌分销；Red Lion/HMS/Yaskawa 在册
- **②芯片/型号**：Red Lion+N-Tron
- **③KP 深挖**：Zaugg sales@
- **④Saga 对标**：温宽 PoE 补件
- **⑤在乎与偏好**：老关系节奏

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Distributor of Sensors, Readouts, Drives, and Transmission Products…Fieldbus Communications…Red Lion CUB/PAX/GEM/Apollo”
  > “Distributor of Sensors, Readouts, Drives, and Transmission Products…Fieldbus Communications…Red Lion CUB/PAX/GEM/Apollo”
  > 来源：https://jashomer.com/
- **【联系方式】**sales@jashomer.com 216-221-4157；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > sales@jashomer.com 216-221-4157；MX=O365（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://jashomer.com/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：克利夫兰工控分销（传感+驱动+盘表+通信）
- **产品线与在售品牌**：Red Lion/N-Tron/HMS+Yaskawa/Baldor/Leeson
- **目标行业与场景**：制造/自动化
- **团队与规模**：地区老分销
- **决策链与对接人**：Charles Zaugg（CSV）sales@
- **技术与认证**：Fieldbus/驱动全链
- **采购与供应链信号**：常规随单
- **近期动态与线索**：站常态化
- **与我方契合点**：其 Fieldbus 盘旁的温宽 PoE 补件
- **风险与注意**：老分销重关系节奏

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | JA Shomer 克利夫兰老分销（Red Lion/HMS/Fieldbus）：温宽 PoE 补件（$74.8 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：老牌
- **W**：慢
- **O**：补件
- **T**：美系

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
  - [ ] 销售额带
  - [ ] 在售矩阵
  - [ ] 框架条件

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Charles,

A catalog that carries Red Lion panel meters, HMS connectivity and Fieldbus communications already speaks industrial Ethernet fluently.

We build industrial managed PoE switches rated -40 to 75C - the kind of line item that sits naturally next to that portfolio. Reference: $74.8 USD EXW.

One question: in your automation orders, who supplies the Ethernet switching layer today?

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

---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:[Charles Zaugg · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Charles%20Zaugg%20J%20A%20Shomer%20Company)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 高(Covered List+SECURE Act+§301 关税;采购方警惕中国标签,话术锚 Marvell(美企)+FCC);战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:待定(档案无芯片信号,首开先问品牌谱)
- **大概率用到的 Saga 型号**:大概率会用: STI-288GP(工业导轨 24G+4×10G→机柜/自动化)、STC-28DGGPM(24G PoE+/4×25G→分销走量)(批量潜力高,可上 280W 旗舰对照行)(本行为调查分析结论,与开发信首推型号是两回事)
