# Gemellaro Systems Integration (GSI)

> **评级 A**　|　美国 · Troy, MI　|　档案编号 `A-116`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-116
rating: A
country: 美国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — GSI 密歇根 30 年安防/网络（厂商中立）：客户墙能源/汽车段接入层（$180 锚点一致）；USACE 联邦红线明示不触；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Gemellaro Systems Integration (GSI)（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Troy, MI | 事实 |
| 网站 | https://securityandnetworks.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】GSI Gemellaro Systems Integration（密歇根 Troy）：30+ 年高规格物理安防+网络基建集成商——客户墙：**US Army Corps of Engineers（联邦红线）、DTE、Consumers Energy、Ford、Rocket Mortgage、AAA、Marathon、Detroit Lions、EMU、St. Joseph's Health**；自述“untied to any specific vendor（不受任何单一厂商绑定）”
- 【推断】厂商中立自述+客户墙横跨能源/汽车/金融/体育/医疗——接入层指定权大，联邦军段红线不触不碍其余
- 【假设】“untied to any specific vendor”=对新候选件开放评——进函直引原话

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@securityandnetworks.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@securityandnetworks.com [Publicly listed; delivery not tested]; https://securityandnetworks.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（厂区/园区安防接入层）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：厂商中立即邀请比价：24 口 PoE++ 成本对照现用件，商业厂区项目接入层。
- **要问的问题**：厂区安防项目的接入层现在在比哪几个型号？
- **随附证明**：单端口测算 + 规格对照 + 交付说明（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（周界/堆场/库区）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：底特律冬季+厂区环境：周界摄像头宽温 DIN PoE，坏机率下降=能源客户运维预算下降。
- **要问的问题**：周界点位的冬季坏机一年几台？
- **随附证明**：宽温/-40 冷启动报告 + 坏机测算 + DIN 图。

### 第 3 次跟进 · 管理型 PoE（安防网段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：园区级项目的安防 VLAN/ERPS 模板：不动 OT 生产网，只做商业安防段。
- **要问的问题**：园区安防网段和客户设施网怎么隔离的？
- **随附证明**：VLAN/ERPS 模板 + 收敛实测 + 评估样机（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第6批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：底特律 Troy 30 年安防+网络基建集成商：能源/汽车/体育/医疗大客户的指挥中心与园区安防老手，Allied 代理（CSV 记录）。
- **产品线与在售品牌**：安防系统/网络基础设施/托管服务三线；厂商中立自述（Allied 为 CSV 记录渠道）。
- **目标行业与场景**：能源公司（DTE/Consumers/Marathon）厂区、汽车总部、体育馆、医院、大学园区。⚠️ 客户含 US Army Corps——军方相关单划线。
- **团队与规模**：成熟公司、全国项目能力（自述 nationally）。
- **决策链与对接人**：info@securityandnetworks.com（CSV 9-27 核验：官网条款页明文地址）。
- **技术与认证**：Allied 代理（CSV 记录）。
- **采购与供应链信号**：能源/汽车厂区项目=工业 PoE 与接入层批量；厂商中立=成本对照能上桌。
- **近期动态与线索**：官网新闻停更在 2008 年（占位图未见更新）但客户墙 Logo 为近年上传——业务运转正常、网站营销荒废，直接工程师对工程师沟通最有效。
- **与我方契合点**：厂区/园区的安防接入层 24 口+周界工业件；指挥中心 UPS 段以外不做。
- **风险与注意**：US Army Corps 客户史→军/政关键设施段划线；能源公司 OT 段只做商业配套。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：30+ 年全国性高等级物理安防与网络基础设施项目领导者，底特律都会区团队。
  > Gemellaro Systems Integration® is a proven leader in developing hi-level physical security and network infrastructure projects nationally for over 30 years.
  > 来源：https://securityandnetworks.com/
- **【采购与供应链信号】**官网自述「不绑定任何厂商，只为你的场景选最优方案」——对第二品牌天然开放。
  > Untied to any specific vendor, we can offer the best solution for your unique case.
  > 来源：https://securityandnetworks.com/
- **【目标行业与场景】**客户墙：US Army Corps（陆军工兵）、Williams International、DTE、Consumers Energy、Ford、Rocket Mortgage、AAA、底特律雄狮、东密歇根大学等。
  > （客户墙 Logo）US army corps · Williams International · DTE · Rocket Mortgage · AAA · Consumers Energy · Detroit Lions · Eastern Michigan University · Ford · Hines · Marathon · St Joseph’s Health
  > 来源：https://securityandnetworks.com/
- **【产品线与在售品牌】**三条服务线：安防系统/网络基础设施/托管服务（Command Center 指挥中心项目履历）。
  > Security Systems · Network Infrastructure · Managed Services ‖ Clients Entrust GSI with Command Centers
  > 来源：https://securityandnetworks.com/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第12批.json`；价格均为 EXW 快照。

- **①背景再核**：30 年安防/网络集成（厂商中立）；客户墙能源/汽车/金融/体育
- **②芯片/型号**：Allied 信号
- **③KP 深挖**：info@
- **④Saga 对标**：中立候选件
- **⑤在乎与偏好**：指定级文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Untied to any specific vendor, we can offer the best solution for your unique case…US Army Corps, DTE, Ford, Rocket Mortgage, Detroit Lions”
  > “Untied to any specific vendor, we can offer the best solution for your unique case…US Army Corps, DTE, Ford, Rocket Mortgage, Detroit Lions”
  > 来源：https://securityandnetworks.com/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：密歇根 30 年安防/网络集成（厂商中立）
- **产品线与在售品牌**：安防/网络基建/托管（Allied 信号）
- **目标行业与场景**：能源/汽车/金融/体育/医疗
- **团队与规模**：东南密歇根全国项目
- **决策链与对接人**：info@ 口
- **技术与认证**：30+ 年
- **采购与供应链信号**：指定权+中立
- **近期动态与线索**：指挥中心项目史
- **与我方契合点**：中立语境候选件
- **风险与注意**：联邦军段红线

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | GSI 密歇根 30 年安防/网络（厂商中立）：客户墙能源/汽车段接入层（$180 锚点一致）；USACE 联邦红线明示不触 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：中立
- **W**：军红线
- **O**：能源
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
  - [ ] 接入层现供
  - [ ] 能源场景件
  - [ ] 评测窗

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi GSI team,

"Untied to any specific vendor, we can offer the best solution for your unique case" - that independence is exactly where we hope to earn a bench evaluation.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, Voice VLAN, watchdog) with full test documentation. Reference: $180 USD EXW. (To be explicit: our note concerns your commercial and industrial customers only - we do not pursue federal engagements.)

One question: across your energy, automotive and enterprise projects, which switch brand holds the PoE access layer for cameras and wireless today?

If useful, I can send one unit for evaluation. If not a fit, one line and I close the loop.

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

- **KP 领英直达**:[Gemellaro Systems Integration (GSI) · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Gemellaro%20Systems%20Integration%20%28GSI%29%20Gemellaro%20Systems%20Integration)(搜索链接,点入后核职位再加;来源:档案名(个人档))
- **中国进口与管制**:国别档位 高(Covered List+SECURE Act+§301 关税;采购方警惕中国标签,话术锚 Marvell(美企)+FCC);战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
