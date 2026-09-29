# SOTECH srl

> **评级 A**　|　意大利 · Calvisano (BS)　|　档案编号 `A-216`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-216
rating: A
country: 意大利
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
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Sotech Brescia MSP：fornitura hardware 主动采购块 value 硬缺口（$165 锚点一致）；四人具名——批内机选；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | SOTECH srl（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 / Calvisano (BS) | 事实 |
| 网站 | https://www.sotech.srl | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】SOTECH srl（意大利 Brescia 布雷西亚，团队 20 年 know-how）：**MSP 结构明确**——Servizi Gestiti 24/7 监控/咨询（HW/SW fornitura+file audit+reti nuova installazione）/Business Continuity/Backup on-premise e cloud/**Fornitura hardware（PMI 小站到大厂 IT 部门两侧自述）**；**团队四人全具名：Luca Paganin/Stefano Ferrari/Stefano Rolfi/Andrea Vanelli**；Sotech 自己说“recente ma i suoi professionisti no”
- 【推断】**“Fornitura hardware PMI 大企两侧”+reti nuova installazione 自述=het 关键随单服务块**；MSP 月费模式=其设备全生命周期运营+鳍网责任→value 件管理成本优势直接挂钩其 SLA 成本
- 【假设】Brescia 机械谷的 PMI 客户=工位/办公混合场景增支大热

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

- **邮箱**：info@sotech.srl
  - 状态：待核·未验证投递（不进群发）
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@sotech.srl（官网正文公开；未验证投递）；原入口：见 alliedtelesis.com 伙伴页
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（托管站点接入标准件）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：托管站点单站 BOM×站点数测算：24 口 PoE++ 作托管接入标准件。
- **要问的问题**：托管客户的接入层标准件现在什么型号？
- **随附证明**：单站 BOM 测算 + 梯价（意）。

### 第 2 次跟进 · 工业级非管理 PoE（制造客户车间点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：布雷西亚制造客户的车间点位：宽温 DIN PoE+备件包。
- **要问的问题**：车间点位坏机率？
- **随附证明**：宽温报告 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（托管分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：托管分段标准件：VLAN/ERPS 模板+监控速查。
- **要问的问题**：分段模板要不要做成托管标准？
- **随附证明**：VLAN/ERPS 模板 + 速查卡。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第11批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：布雷西亚 Calvisano 四人合伙 MSP：托管+咨询+硬件供应，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：24/7 监控托管/file audit/BC&DR/备份/硬件供应。
- **目标行业与场景**：布雷西亚省中小制造企业为主。
- **团队与规模**：小型四人核心（各 20 年功底）。
- **决策链与对接人**：info@sotech.srl（CSV 9-27：联系页 Via San Felice 15/A；⚠️与 STL Connext 同址注册——CSV 明示非同一客户、不合并）。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：托管栈=每站点标准件集中采购逻辑；硬件供应线=他给客户代购，梯价+库存承诺对口。
- **近期动态与线索**：2022 版式稳态运营（电话文化型 MSP）。
- **与我方契合点**：托管站点的接入层标准件+制造客户车间工业件。
- **风险与注意**：与 A-218 STL Connext 同址不同主体（CSV 原话照录）——勿把两家邮件串发。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网口号「数据安全/员工安心/老板开心」：布雷西亚 SMB 托管服务商——24/7 监控+网络效率干预。
  > Gli specialisti della gestione dei sistemi informatici. — Dati al sicuro · Collaboratori Sereni · Imprenditori Felici ‖ Servizi gestiti — monitoraggio del tuo ambiente IT 24/7 · interventi per la massima efficienza della rete
  > 来源：https://www.sotech.srl/
- **【决策链与对接人】**团队页四位创始人具名出镜：**Luca Paganin / Stefano Ferrari / Stefano Rolfi / Andrea Vanelli**——「公司新、人老道」自述二十年功底。
  > Sotech è recente, ma i suoi professionisti no! Con vent'anni di know how… Luca Paganin · Stefano Ferrari · Stefano Rolfi · Andrea Vanelli（团队页）
  > 来源：https://www.sotech.srl/
- **【产品线与在售品牌】**方案四件：托管服务/IT 咨询（file audit 数据流分析）/业务连续性与 DR/备份（固定或云）/硬件供应（小企业到带 IT 部的大公司）。
  > Servizi gestiti · Consulenza informatica · Business continuity plan · Backup system · Fornitura hardware（per PMI con poche postazioni / per grandi aziende con reparto IT interno）
  > 来源：https://www.sotech.srl/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第22批.json`；价格均为 EXW 快照。

- **①背景再核**：Brescia MSP（fornitura 主动买货=核心价值缺口）
- **②芯片/型号**：—
- **③KP 深挖**：四人具名最大可能 Paganin
- **④Saga 对标**：MSP fornitura value 件
- **⑤在乎与偏好**：SLA 成本挂钩文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Servizi gestiti…monitoraggio 24/7…Fornitura hardware: Gestione server e workstation per PMI con poche postazioni, per grandi aziende con reparto IT interno…nuova installazione reti di computer”
  > “Servizi gestiti…monitoraggio 24/7…Fornitura hardware: Gestione server e workstation per PMI con poche postazioni, per grandi aziende con reparto IT interno…nuova installazione reti di computer”
  > 来源：https://www.sotech.srl/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：Brescia MSP（HW fornitura 为菜单核心块）
- **产品线与在售品牌**：—
- **目标行业与场景**：Brescia 机械谷 PMI 小站→大企 IT 部两侧
- **团队与规模**：四人具名
- **决策链与对接人**：Luca Paganin 具名核心
- **技术与认证**：—
- **采购与供应链信号**：**HW fornitura 自述=餐厅主动买货**
- **近期动态与线索**：24/7 监控上线
- **与我方契合点**：MSP 的 fornitura 块 value 量件（$165 锚点直接对 PMI 报价结构）
- **风险与注意**：

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Sotech Brescia MSP：fornitura hardware 主动采购块 value 硬缺口（$165 锚点一致）；四人具名——批内机选 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：主动采购
- **W**：未定
- **O**：硬缺口
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
  - [ ] fornitura 现牌
  - [ ] 月站量
  - [ ] 付款结构

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Luca,

Hardware supply for PMI with a handful of seats on one side, corporate IT departments on the other - the fornitura block on your service wall is a real buying line, not a page decoration. And a 24/7 managed bench makes every remote switch reboot a cost line you know personally.

We manufacture a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog auto-reboot) with full documentation. Reference: $165 USD EXW - a value unit that prices cleanly into a PMI quotation and reboots itself at night so your on-call desk does not.

One question: which switch brand does your fornitura block hold today - and would a documented value alternative earn a bench test?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

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
