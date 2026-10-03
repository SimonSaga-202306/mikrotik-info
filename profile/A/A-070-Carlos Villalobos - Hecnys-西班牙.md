# Carlos Villalobos / Hecnys

> **评级 A**　|　西班牙 · Bormujos (Sevilla)　|　档案编号 `A-070`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-070
rating: A
country: 西班牙
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
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
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — Hecnys Ignition 官认 SCADA 集成：边缘/现场段温宽 PoE（$74.8 锚点一致）；发电/油气/港口边界守；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Carlos Villalobos / Hecnys（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 西班牙 / Bormujos (Sevilla) | 事实 |
| 网站 | hecnys.com | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Carlos Villalobos | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCTCE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Hecnys（西班牙）：**Ignition 官方认证集成商（自 2026）+15 年工控经验**——SCADA/IIoT（MQTT/Sparkplug B、OPC UA、SQL 历史）+**工业网线（分段/可靠/远维）**；行业：油气、发电、制药、石化、**港箱物流**、汽车；Carlos Villalobos MTCNA+MTCTCE
- 【推断】其工业网线=Ignition 平台脚下的真正网络底座：边缘节点/控制室/现场段都吞温宽工业交换件
- 【假设】“无层级工程制”（设计的人交付运维）=对设备的可靠与生命周期要求高于价格

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCTCE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：carlosvillalobos@hecnys.com
  - 状态：既有/公开
- **电话**：+34 645 396 100
- **原始联系字段**：+34 645 396 100 / carlosvillalobos@hecnys.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Carlos Villalobos**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（车间监控/办公接入）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：车间项目的监控与办公接入段：24 口 PoE++ 带摄像头/机器视觉上位/AP，4×10G 上行回主控——从 IT 侧先建立合作。
- **要问的问题**：项目里 CCTV 与办公接入的交换机现在用哪个牌子？
- **随附证明**：规格对照 + 工业场景供电预算表（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（PLC 柜/边缘节点）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：正对工业网络业务线：PLC 柜与边缘采集节点的宽温 DIN PoE，-40 冷启动、SFP 上行——按柜标配。
- **要问的问题**：柜内交换现在用什么型号？有没有 -40 或高温失效的案例？
- **随附证明**：宽温报告 + DIN 图 + 抗扰测试项清单。

### 第 3 次跟进 · 管理型 PoE（IT/OT 分段模板）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他做 segmentation 出身：管理型 VLAN/ACL/ERPS 模板对接他的 IT/OT 分段架构，方案写进他的标准设计。
- **要问的问题**：你的分段参考架构里接入层有没有候选型号空位？
- **随附证明**：分段架构对照 + VLAN/ERPS 模板 + 实测。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：塞维利亚工业自动化集成商：Ignition 平台 SCADA/IIoT + 工业网络建设，IT/OT 融合方向，工程师直连客户（设计与交付同一人）。
- **产品线与在售品牌**：项目制：Ignition（Inductive Automation）+ MQTT/OPC UA/SQL 技术栈 + 工业网络基础设施；硬件随项目选型。
- **目标行业与场景**：油气/发电/制药/石化/港口/汽车的车间网络：PLC 到现场的分段、边缘采集节点、监控与远程运维通道。
- **团队与规模**：小而精的工程团队（「designs = commissions = supports 同一工程师」）；支持时段周一到周五 8:00–18:00 CET。
- **决策链与对接人**：Carlos Villalobos 本人（+34 645 396 100 / carlosvillalobos@hecnys.com），工业工程师出身。
- **技术与认证**：MTCNA+MTCTCE（CSV 名录记录）+ Inductive Automation 官方集成商（2026 起）；工业协议栈（OPC UA/MQTT Sparkplug）母语级。
- **采购与供应链信号**：车间项目的网络设备由他设计选型：DIN 导轨、宽温、冗余是硬指标；项目复制性强（同平台架构复用）。
- **近期动态与线索**：刚拿到 Inductive Automation 官集资质（2026）=投标资格升级、项目量上行期。
- **与我方契合点**：工业网络这条业务线=我们的 DIN 工业线正对口：机器视觉/PLC 柜/边缘节点都要 PoE 与上行；港口/油气场景的室外点位更多。
- **风险与注意**：工业客户重认证（ATEX/IEC/行业规范）：先问清目标行业的认证要求再谈型号，别硬推不满足项。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网抬头：Inductive Automation 官方集成商，车间层的控制与数据工程。
  > Official Inductive Automation integrator · Control and data engineering for the plant floor · We design, integrate and support SCADA, IIoT and industrial network systems on Ignition.
  > 来源：https://hecnys.com/en
- **【产品线与在售品牌】**四条业务线：Ignition SCADA、工业 IIoT（MQTT/Sparkplug+OPC UA）、工业网络（分段/可靠性/远程访问）、定制开发。
  > Ignition SCADA · Industrial IIoT — From plant-floor data to business systems, over MQTT/Sparkplug and OPC UA · Industrial networks — The infrastructure the data rides on: segmentation, reliability and remote access.
  > 来源：https://hecnys.com/en
- **【近期动态与线索】**2026 年新晋 Inductive Automation 认证集成商（15 年行业经验）——资质刚升级，正在扩项目盘。
  > Certified Integrator of Inductive Automation since 2026, with 15 years of experience in industrial control and integration.
  > 来源：https://hecnys.com/en
- **【目标行业与场景】**服务行业清单：油气、发电、制药、石化、集装箱港口物流、汽车——全部是重 PoE/工业交换场景。
  > Oil & Gas · Power generation · Pharmaceutical · Petrochemical · Container port logistics · Automotive
  > 来源：https://hecnys.com/en

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第7批.json`；价格均为 EXW 快照。

- **①背景再核**：Ignition 官认集成商；工业网线为其四大服务之一
- **②芯片/型号**：未公开
- **③KP 深挖**：Villalobos 直达
- **④Saga 对标**：边缘/现场温宽 PoE
- **⑤在乎与偏好**：生命周期与工程师直达

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Official Inductive Automation integrator…SCADA, IIoT and industrial network systems…Oil & Gas, Power generation, Pharmaceutical, Container port logistics, Automotive”
  > “Official Inductive Automation integrator…SCADA, IIoT and industrial network systems…Oil & Gas, Power generation, Pharmaceutical, Container port logistics, Automotive”
  > 来源：https://hecnys.com/en
- **【联系方式】**carlosvillalobos@hecnys.com +34 645 396 100（CSV）；MX=Hostinger（MX/DNS 级核验：域存活=邮件可投递到域）
  > carlosvillalobos@hecnys.com +34 645 396 100（CSV）；MX=Hostinger（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://hecnys.com/en/contacto

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：西班牙 Ignition 官认 SCADA/IIoT 集成商（15 年）
- **产品线与在售品牌**：Ignition 平台+托管工业网络工程
- **目标行业与场景**：制药/汽车/物流民营段优先；能源/油气边界
- **团队与规模**：工程师小团
- **决策链与对接人**：Carlos Villalobos
- **技术与认证**：MTCNA+MTCTCE
- **采购与供应链信号**：工业网络工程随单
- **近期动态与线索**：2026 年获 Ignition 官方集成商认证
- **与我方契合点**：边缘/现场段温宽工业 PoE 随单
- **风险与注意**：关键设施边界

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Hecnys Ignition 官认 SCADA 集成：边缘/现场段温宽 PoE（$74.8 锚点一致）；发电/油气/港口边界守 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424XGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：底座粘
- **W**：边界
- **O**：民营产线
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
| 决策人识别 | ✅ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 现场交换现供
  - [ ] 生命周期门槛
  - [ ] 试点窗

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Carlos,

Becoming an official Ignition integrator while running the industrial-network line yourself is exactly the stack where hardware decisions stick for a decade.

We build industrial managed PoE switches rated -40 to 75C with a hardware watchdog and lifecycle supply commitments - at an honest price next to the legacy brands. Reference: $74.8 USD EXW.

One question: in your edge and field segments, who supplies the Ethernet switching layer today?

If useful, I can send one unit with the full temperature test report. If not a fit, one line and I close the loop.

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

- **KP 领英直达**:[Carlos Villalobos · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Carlos%20Villalobos)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 低(务实采购;电信层只登记不排斥);战术: 可正面谈中国产能/成本优势;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STI-288GP(工业导轨 24G+4×10G→机柜/自动化)、STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
