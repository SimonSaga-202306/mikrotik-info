# Ryszard Labus / SINUX

> **评级 A**　|　波兰 · Warszawa　|　档案编号 `A-050`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-050
rating: A
country: 波兰
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换认证 MTCSWE、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — SINUX 华沙个体双高阶（MTCSWE+MTCEWE）：特性表+电话核实（NIP 在册真实存续）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Ryszard Labus / SINUX（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 波兰 / Warszawa | 事实 |
| 网站 | sinux.pl | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Ryszard Labus | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCSE+MTCSWE+MTCEWE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】SINUX（Ryszard Labus，华沙 Domaniewska 47/10，NIP 548-138-01-53）：5 证 MikroTik 顾问（MTCNA+MTCRE+MTCSE+MTCSWE+MTCEWE 双高阶）；官网为 WordPress 默认单页（极简/新架或休眠），NIP 登记旁证真实存续
- 【推断】华沙个体顾问，双高阶（交换+企业无线）；公开内容面极薄——按工商存续+NIP 采信，邮件层运转
- 【假设】MTCSWE+MTCEWE 对口企业 WLAN/交换工程线

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE+MTCSE+MTCSWE+MTCEWE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：r.labus@sinux.pl
  - 状态：既有/公开
- **电话**：+48 666 385 002
- **原始联系字段**：+48 666 385 002 / r.labus@sinux.pl
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Ryszard Labus**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 PoE++（楼宇项目打包）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：楼控/门禁/监控一栋楼 24 口 PoE++ 一次打包——对照他现在的方案，单点成本价说清楚。
- **要问的问题**：楼宇项目交换机谁供、是否存在电源/温度问题？
- **随附证明**：功率预算表 + 24 口 PoE++ 规格单页（英文）。

### 第 2 次跟进 · 工业非管理 PoE（机电间/管道井）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：楼内机电间、管道井、设备间的现场节点：宽温宽压、DIN、免配置，装完不用再维护。
- **要问的问题**：机电间常用的 5/8 口小交换机用什么段位、更换麻烦吗？
- **随附证明**：DIN 安装图 + 宽温报告 + 一台测试机。

### 第 3 次跟进 · 管理型（楼控多网段隔离）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：BMS+楼控+客人网+监控网共网段的安全议题：管理型 VLAN 分段 + ERPS，让他的方案更硬。
- **要问的问题**：楼控网段跟办公场所是不是分开的、怎么分的？
- **随附证明**：VLAN 分段模板 + ERPS 实测 + 英文参数页。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Warszawa 个人楼宇自动化/网络工程师：BMS 厂牌授权服务商 + MikroTik 顾问，做楼内的 VLAN/VPN 与自动化联动网段。
- **产品线与在售品牌**：项目选型（MikroTik 链路 + 楼控设备Delta Controls 等）。
- **目标行业与场景**：楼宇自动化系统联网、设备间分网、工程跨界（BMS+IT 网络）——工业线对口。
- **团队与规模**：个人工程师，一人决策。
- **决策链与对接人**：Ryszard Labus 本人（+48 666 385 002 / r.labus@sinux.pl）。
- **技术与认证**：MTCNA+MTCRE+MTCSE+MTCSWE+MTCEWE（CSV 既有记录）+ Delta Controls 授权服务（厂商名录佐证）。
- **采购与供应链信号**：随项目采购；楼控项目总包内常含一段网络硬件，他对价格与参数结构的理解都到位。
- **近期动态与线索**：自建站是模板默认页——营销不靠官网，直接联系更有效。
- **与我方契合点**：楼控项目的机房外机电间供电、DIN 卡组装全部对口工业非管理；会议/门禁/闸机网段可用管理型。
- **风险与注意**：个人规模+官网半荒废：先确认他当前活跃状态（电邮直联）；不要期待平台级合作。

### R54 原文证据摘录（全部保留）

- **【决策链与对接人】**自建站仅显示：SINUX Ryszard Labus，Domaniewska 47/10，02-672 Warszawa，NIP 548-138-01-53——更深层内容未维护。
  > SINUX Ryszard Labus · ul. Domaniewska 47/10 · 02-672 Warszawa · NIP 548-138-01-53
  > 来源：https://sinux.pl/
- **【目标行业与场景】**Delta Controls（楼控厂牌）波兰官网把他列为授权服务公司，属于楼宇自动化 BMS 方向——CSV 里「BMS/楼宇自动化」来源性质得到厂商名录佐证。
  > AUTORYZOWANE FIRMY SERWISUJĄCE… SINUX Ryszard Labus ul. Domaniewska 47/10 02-672 Warszawa
  > 来源：https://deltacontrols.com/pl-partnerzy-delta
- **【近期动态与线索】**官网是默认 WordPress 模板（Iconic One 主题），内容多年未更新——活跃度低，但登记与厂商名录仍在用。
  > [Iconic One](https://themonic.com/iconic-one/) Theme | Powered by [Wordpress](https://wordpress.org/)
  > 来源：https://sinux.pl/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第5批.json`；价格均为 EXW 快照。

- **①背景再核**：华沙 NIP 在册个体顾问；MTCSWE+MTCEWE 双高阶；站单页
- **②芯片/型号**：未公开
- **③KP 深挖**：Labus r.labus@ 与站互证
- **④Saga 对标**：双高阶特性对话
- **⑤在乎与偏好**：直接

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“SINUX Ryszard Labus, ul. Domaniewska 47/10, 02-672 Warszawa, NIP 548-138-01-53, tel 666 385 002”
  > “SINUX Ryszard Labus, ul. Domaniewska 47/10, 02-672 Warszawa, NIP 548-138-01-53, tel 666 385 002”
  > 来源：https://sinux.pl/
- **【技术与认证】**CSV：Ryszard Labus/SINUX MTCNA+MTCRE+MTCSE+MTCSWE+MTCEWE
  > CSV：Ryszard Labus/SINUX MTCNA+MTCRE+MTCSE+MTCSWE+MTCEWE
  > 来源：https://mikrotik.com/consultants

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：华沙个体顾问（NIP 登记）；MTCSWE+MTCEWE 双高阶
- **产品线与在售品牌**：咨询
- **目标行业与场景**：交换/企业无线工程（证书推断）
- **团队与规模**：个体
- **决策链与对接人**：Labus 本人
- **技术与认证**：MTCNA+MTCRE+MTCSE+MTCSWE+MTCEWE
- **采购与供应链信号**：未知
- **近期动态与线索**：官网 WordPress 默认单页（名称/地址/电话/NIP）
- **与我方契合点**：双高阶特性对话
- **风险与注意**：公开内容薄，如实标注；电话核实

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | SINUX 华沙个体双高阶（MTCSWE+MTCEWE）：特性表+电话核实（NIP 在册真实存续） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：双高阶
- **W**：内容薄
- **O**：随单
- **T**：竞争

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
| 决策人识别 | ✅ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 项目方向
  - [ ] 随单现供
  - [ ] 评测意愿

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Ryszard,

I found SINUX on the MikroTik consultant list - MTCSWE and MTCEWE together points to switching and enterprise wireless work.

We build managed PoE switches with a full L2+ table (Voice VLAN, ERPS, watchdog). Reference: 24-port model $165 USD EXW; bench 8-port $99.

One question: do your client projects leave room for an alternative on the switching layer?

If yes, I can send the feature table and an evaluation unit. If not, one line and I close the loop.

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

- **KP 领英直达**:[Ryszard Labus · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Ryszard%20Labus)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 中(NCSA 2024 高风险供应商禁(5G/军队);亲美倾向);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STI-288GP(工业导轨 24G+4×10G→机柜/自动化)、STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
