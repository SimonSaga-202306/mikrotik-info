# Lanmarket

> **评级 A**　|　乌克兰　|　档案编号 `A-434`　|　优先级 ★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-434
rating: A
country: 乌克兰
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
- **为什么值得跟**：【人工定级】A —— R53 B段复筛达标升级：B 段逐站复筛达标（站点在线 + 交换机品类/产品在售 + 网络/交换专营 + 小公司决策链短）；官网核对：Lanmarket 为网络/电信设备专营（零售+批发），在售 MikroTik（NetBox 5、SXT LTE、CCR2004-16G-2S+、Q+DA0001 40G 线缆）与 PON OLT 交换机品类、OTDR 等；原 B-015 升级，编号顺延 A-434
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Lanmarket 乌批零店（MT/Ubiquiti/ZTE OLT/OTDR；报价制）：项目报价单接入档（UA 民用限定；$180 锚点一致）；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Lanmarket（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 乌克兰 | 事实 |
| 网站 | lanmarket.ua | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Reseller） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Lanmarket（乌克兰）：Lanmarket(UA）网络装备批零店（Bitrix):MikroTik 大区（CCR2004/NetBox 5/SXT)+Ubiquiti airFiber/AF60+TP-Link+ZTE OLT+OTDR/熔接机+IoT 传感；多品'цена пока неизвестна'=报价制；Telegram bot 在售
- 【推断】报价制批发=中型单逻辑；牌谱全=PON+无线，接入交换档空缺互补
- 【假设】报价制项目随单对照行（民用限定）

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik（Reseller））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sale@lanmarket.net
  - 状态：既有/公开
- **电话**：+380 50 666 78 58
- 来源等级：official-company（R41–R48 联系方式台账口径）
- **原始联系字段**：+380 50 666 78 58 / sale@lanmarket.net
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 对照行

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：报价单接入档（民用限定）
- **要问的问题**：进报价单吗？
- **随附/动作**：规格页

### 第 2 次跟进 · 留档

- **推什么**：—（统一口径=P1 系列，不外溢）
- **切入点**：无响——留档
- **要问的问题**：—
- **随附/动作**：—

### 第 3 次跟进 · 留档

- **推什么**：—（统一口径=P1 系列，不外溢）
- **切入点**：留档
- **要问的问题**：—
- **随附/动作**：—


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第44批.json`；价格均为 EXW 快照。

- **①背景再核**：https://lanmarket.ua|CCR2004+ZTE OLT 墙+报价制
- **②芯片/型号**：——
- **③KP 深挖**：批零多年
- **④Saga 对标**：STC-424 对照行（$180 锚点一致）
- **⑤在乎与偏好**：报价制=可谈条款

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**Lanmarket: розничная и оптовая продажа; CCR2004-16G-2S+ / ZTE OLT / OTDR 上架；多品报价制
  > Lanmarket: розничная и оптовая продажа; CCR2004-16G-2S+ / ZTE OLT / OTDR 上架；多品报价制
  > 来源：https://lanmarket.ua

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：乌网络装备批零店（报价制）
- **产品线与在售品牌**：MikroTik/Ubiquiti/ZTE OLT/OTDR
- **目标行业与场景**：装维/ISP/集成
- **团队与规模**：中型
- **决策链与对接人**：sale@lanmarket.net 口
- **技术与认证**：Telegram bot 在售
- **采购与供应链信号**：报价制片面观
- **近期动态与线索**：—
- **与我方契合点**：接入交换档对照行（民用限定）
- **风险与注意**：报价制——首轮=进报价单

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Lanmarket 乌批零店（MT/Ubiquiti/ZTE OLT/OTDR；报价制）：项目报价单接入档（UA 民用限定；$180 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：项目档
- **W**：PON 优先
- **O**：接入档
- **T**：ZTE

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
  - [ ] 报价口
  - [ ] 首发量

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Lanmarket team,

You quote project lists for ISPs every day - CCRs beside ZTE OLTs, bridges beside fused fibre. The one line those lists usually lack: an access PoE switch that does not eat the margin. One honest framing note first: our offer is strictly for civilian commercial networking - nothing dual-use, nothing for state or military buyers. Ours is a documented 24-port Gigabit PoE unit at $180 USD EXW (2026-09-29).

We build a 24-port Gigabit PoE access switch (280W total budget, 802.3af/at, per-port watchdog, desktop or rack) with full English documentation. Reference: $180 USD EXW (2026-09-29) - a documented value tier beside the lines you already carry, not a replacement.

One question: would your project quotes carry a documented value PoE row?

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

- **KP 领英直达**:[Lanmarket · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Lanmarket)(无具名 KP 信号,先搜公司再加人;待查)
- **中国进口与管制**:国别档位 中(战争期;华为/中兴仍在售,部分转向北约标准;货款周期与物流保险另计);档案信号: 在卖中国品牌 TP-Link/ZTE → 对中国产线接受度已被事实验证;战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STI-288GP(工业导轨 24G+4×10G→机柜/自动化)、STC-28DGGPM(24G PoE+/4×25G→分销走量)(批量潜力高,可上 280W 旗舰对照行)(本行为调查分析结论,与开发信首推型号是两回事)
