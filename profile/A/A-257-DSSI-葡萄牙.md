# DSSI

> **评级 A**　|　葡萄牙 · Agualva-Cacém　|　档案编号 `A-257`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-257
rating: A
country: 葡萄牙
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — DSSI 葡 VAD 六域（Ubiquiti+Perle 双驻）：网络域替补窄位（$165 锚点一致）；comercial@ 商务口；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | DSSI（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 葡萄牙 / Agualva-Cacém | 事实 |
| 网站 | https://dssi.pt | 事实 |
| 类型 | 分销/集成商（Perle 授权） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】DSSI（葡萄牙 VAD）：存储/备份/监控/网络/安全/云六域；品牌含 Ubiquiti+Perle+SolarWinds+Proxmox+Wasabi+NAKIVO 等；个性化实施支持叙事
- 【推断】VAD 网络域窄口：Ubiquiti+Perle 双驻——二轨替补窄位
- 【假设】其经销商带的 value PoE 替补窄口

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：comercial@dssi.pt
  - 状态：既有/公开
- **电话**：+351 21 805 15 60
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：comercial@dssi.pt（官网正文公开；未测试投递）；原入口：+351 21 805 15 60
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · Networking 域上架提案（24 口 PoE）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行 L2+）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：对 comercial@：Networking 域的 24 口监控 PoE 接入层新供应商提案（分销条件+葡语资料包+阶梯价）。
- **要问的问题**：Networking 域开新硬件供应商位吗？
- **随附证明**：上架一页提案（葡/英）+ 证书包。

### 第 2 次跟进 · 工业窄线

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：机房外/仓储/户外点位的宽温小件窄线。
- **要问的问题**：工业件窄线有位吗？
- **随附证明**：工业件一页 + CE。

### 第 3 次跟进 · 分销条款包

- **推什么**：—（条款）
- **切入点**：中性发货+价格保护+首单 MOQ 的条款包收口。
- **要问的问题**：（无需回）条款留档。
- **随附证明**：分销条款一页（英）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第13批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：葡萄牙 VAD（Networking 五域之一）：Perle+Ubiquiti 同墙——商业接入层与工业件双类目有现成通路。
- **产品线与在售品牌**：Perle/Ubiquiti 双牌+SMB 软件栈十余厂。
- **目标行业与场景**：葡国企业渠道经销商网络。
- **团队与规模**：小中型 VAD（新闻/活动/EDM 运营勤）。
- **决策链与对接人**：comercial@dssi.pt（官网 contactos，CSV 9-27）。
- **技术与认证**：Perle/Ubiquiti 现墙（CSV+官网厂牌页）。
- **采购与供应链信号**：Networking 域=上架提案直通：24 口商业监控 PoE 接入层+工业窄线两条线；SMB 软件栈客群=价格敏感。
- **近期动态与线索**：2026-02/03/05 厂牌徽标持续更新+EDM 活跃=拓品窗口期。
- **与我方契合点**：24 口 PoE 接入层 VAD 上架提案+工业件窄线+分销条款包三步走。
- **风险与注意**：Perle/Ubiquiti 在位：话术类目空档/价位档，不替位；别碰其软件主业。

### R54 原文证据摘录（全部保留）

- **【业务定位】**里斯本都市圈 Agualva-Cacém 的葡萄牙 VAD（Distribuidor Tecnológico de Valor Acrescentado）：五域举 **Networking** 在内。
  > A DSSI – o seu Distribuidor Tecnológico de Valor Acrescentado ‖ Armazenamento, Backup, Arquivo, Partilha & Virtualização · Monitorização e Help Desk · Networking · Segurança e Mobilidade · Cloud
  > 来源：https://dssi.pt/
- **【产品线与在售品牌】**厂牌墙含 **Perle 与 Ubiquiti**（2026-02 新版徽标），另有 Wasabi/NAKIVO/Proxmox/SolarWinds/MailStore/Kiteworks 等 SMB 软件栈。
  > （厂牌墙 2026-02/03 徽标）perle · ubuquiti · wasabi · nakivo · proxmox · solarwinds · mailstore
  > 来源：https://dssi.pt/
- **【决策链与对接人】**comercial@dssi.pt 官网 contactos 正文（CSV 9-27：official，旧 owncloud 页 404 备注在档）。
  > （CSV 2026-09-27 记录）comercial@dssi.pt（官网正文）；旧 owncloud 页实际 404
  > 来源：https://dssi.pt/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第26批.json`；价格均为 EXW 快照。

- **①背景再核**：PT VAD（官网一手核）
- **②芯片/型号**：Ubiquiti/Perle 墙
- **③KP 深挖**：comercial@
- **④Saga 对标**：替补窄位（$165 锚点一致）
- **⑤在乎与偏好**：品牌组合/实施支持

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**Distribuidor Tecnológico de Valor Acrescentado——Armazenamento/Backup/Monitorização/Networking/Segurança/Cloud；Ubiquiti+Perle 品牌墙
  > Distribuidor Tecnológico de Valor Acrescentado——Armazenamento/Backup/Monitorização/Networking/Segurança/Cloud；Ubiquiti+Perle 品牌墙
  > 来源：https://dssi.pt

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：葡萄牙 VAD（六域）
- **产品线与在售品牌**：Ubiquiti/Perle 等在墙
- **目标行业与场景**：经销商/企业
- **团队与规模**：分销团队
- **决策链与对接人**：comercial@ 口
- **技术与认证**：—
- **采购与供应链信号**：分销泳道
- **近期动态与线索**：Cyberhaven/新牌持续入册
- **与我方契合点**：网络域替补窄位
- **风险与注意**：SKU 主权强——守界前句

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | DSSI 葡 VAD 六域（Ubiquiti+Perle 双驻）：网络域替补窄位（$165 锚点一致）；comercial@ 商务口 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：通道
- **W**：线在墙
- **O**：替补
- **T**：引力

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
  - [ ] 替补机制
  - [ ] 品牌权责

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi DSSI team,

A value-added distributor across backup, monitoring, security, cloud - and a networking line already carrying Ubiquiti and Perle. One sentence up front: we are not asking to displace either.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW (2026-09-29) - a value substitute in the networking domain for deals where the headline tier is overspecified.

One question: does your networking domain keep a substitute slot - and would you evaluate one unit?

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
