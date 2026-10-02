# Ziegler Systemhaus GmbH

> **评级 A**　|　德国 · Stuttgart　|　档案编号 `A-185`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-185
rating: A
country: 德国
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424DGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-424DGGPM-280W（24口 PoE + 4×10G） — Ziegler 142 人电气+IT 混合屋：WLAN/楼宇项目随单（$165 锚点一致）；$165 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Ziegler Systemhaus GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Stuttgart | 事实 |
| 网站 | https://www.ziegler-systemhaus.de | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Ziegler Systemhaus GmbH（德国斯图加特+Schwieberdingen 双点，2001 创，25+ 年）：**142 人电气+IT 混合系统屋**——电气工程/网络信息技术（“erfolgreich VERNETZEN”）/再生能源/安全技术/**活动与展会供电专线**；500+ 项目；项目新闻：Messehalle 展馆灯光改造+**专业 WLAN 覆盖（Ausleuchtung）项目**；14 培训生在训
- 【推断】电气+网络双工+展馆活动供电=弱电随单活跃；WLAN Ausleuchtung 项目自述=无线工程在撒单
- 【假设】“namhafte Kunden”高层客户+快速招人=增长型中型

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@ziegler-sh.de
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@ziegler-sh.de [Publicly listed; delivery not tested]; https://www.ziegler-systemhaus.de
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（楼项目 WLAN/监控供电接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424DGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：顺他 WLAN 勘测项目：AP/监控点位的 24 口 PoE++ 接入层现场对照。
- **要问的问题**：楼项目 AP/监控点位的供电交换现在配什么？
- **随附证明**：规格对照 + 项目价 + DIN/上架双模图（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（活动/竖井/车库点位）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：活动临时网与竖井/车库点位：4-8 口宽温小机试单价。
- **要问的问题**：活动/竖井点位的小交换用什么？
- **随附证明**：宽温报告 + 试单价（德文）。

### 第 3 次跟进 · 管理型 PoE（楼宇网分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：楼宇弱电的分段标准件：VLAN/ERPS 模板进他的规划库。
- **要问的问题**：弱电分段模板要不要进规划库？
- **随附证明**：VLAN/ERPS 模板 + 实测（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第10批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：斯图加特 142 人电气与楼宇技术商：网络/安全/新能源/活动供电五板块，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：电气安装/网络信息技术（WLAN/布线/交换）/安防/光伏/展馆与活动临时供电。
- **目标行业与场景**：商业楼与展馆项目（Messehallen 照明案例）；活动临时基建。
- **团队与规模**：142 人中型，双点运营。
- **决策链与对接人**：info@ziegler-sh.de（CSV 9-27：总部地址匹配 Stuttgart，非分支展会专用邮箱）。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：电气总包节奏：网络分包里的交换/PoE 件随楼项目走；WLAN 勘测项目=无线 AP 的 PoE 供电层刚配——项目 BOM 明。
- **近期动态与线索**：2026-09 六名新学徒入职+展馆照明项目交付。
- **与我方契合点**：楼项目 WLAN/监控的 PoE 接入层+活动临时网的工业小件。
- **风险与注意**：电气公司网络件随项目窗口谈；德文报价+规格对照一页式。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网五板块中第二即「网络信息技术——数字化不受干扰」——它是电气公司为骨的全面商，另有活动供电新线。
  > Geschäftsfelder: Elektrotechnik（Intelligent steuern）· Netzwerk-Informationstechnik（Weltweit verbinden – Digitalisierung – wir sichern störungsfreie Abläufe zu jeder Zeit）· Erneuerbare Energien · Sicherheitstechnik · Energieversorgung bei Veranstaltungen（Ob Messe, Konzert, Festival）
  > 来源：https://www.ziegler-systemhaus.de/
- **【团队与规模】**官网硬数据：500+ 项目完成、142 名员工（14 名学徒）、2001 年起、双点 Stuttgart+Schwieberdingen。
  > 500+ Erfolgreich abgeschlossene Projekte · 140+ Hochspezialisierte Mitarbeitende · 25+ Jahre in der Branche tätig ‖ Seit 2001 · 142 Mitarbeitende · 14 Auszubildende ‖ Büros in Stuttgart und Schwieberdingen
  > 来源：https://www.ziegler-systemhaus.de/
- **【近期动态与线索】**项目新闻：三馆展馆照明改造+专业 WLAN 无线勘测（WLAN-Ausleuchtung）——网络项目常态在接。
  > Beleuchtungstausch in drei Messehallen（项目）‖ Professionelle WLAN-Ausleuchtung – Die Basis für ein stabiles Netzwerk（项目）
  > 来源：https://www.ziegler-systemhaus.de/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第19批.json`；价格均为 EXW 快照。

- **①背景再核**：142 人电气+IT 混合屋（WLAN 项目+活动供电线）
- **②芯片/型号**：未明示
- **③KP 深挖**：info@
- **④Saga 对标**：网络项目随单 value 件
- **⑤在乎与偏好**：电工级可靠文档

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“142 Mitarbeitende…14 Auszubildende…Namhafte Kunden…Professionelle WLAN-Ausleuchtung – Die Basis für ein stabiles Netzwerk…500+ Erfolgreich abgeschlossene Projekte”
  > “142 Mitarbeitende…14 Auszubildende…Namhafte Kunden…Professionelle WLAN-Ausleuchtung – Die Basis für ein stabiles Netzwerk…500+ Erfolgreich abgeschlossene Projekte”
  > 来源：https://www.ziegler-systemhaus.de/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：斯图加特电气+IT 混合系统屋（活动供电特色）
- **产品线与在售品牌**：未明示
- **目标行业与场景**：楼宇/活动/企业
- **团队与规模**：142 人
- **决策链与对接人**：info@ 口
- **技术与认证**：电工+IT 双证
- **采购与供应链信号**：随单
- **近期动态与线索**：WLAN 覆盖项目+展厅灯改
- **与我方契合点**：网络技术线接入随单 value 件
- **风险与注意**：

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W（24口 PoE + 4×10G） | 主场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Ziegler 142 人电气+IT 混合屋：WLAN/楼宇项目随单（$165 锚点一致） |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：双工
- **W**：体量
- **O**：随单
- **T**：在位

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
  - [ ] 接入现供
  - [ ] 活动网络模式
  - [ ] 年量

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Ziegler team,

142 people across Stuttgart and Schwieberdingen, 500+ projects - from Messehallen lighting to professional WLAN coverage. Where you lay the wireless basis, an access switch sits at the end of every fibre run.

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog) with full documentation. Reference: $165 USD EXW - a value unit for the access layer inside your network-technology projects.

One question: in your WLAN and building projects, which switch brand holds the PoE access layer today - and would a documented value alternative earn a bench test?

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

---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:[Ziegler Systemhaus GmbH · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Ziegler%20Systemhaus%20GmbH)(无具名 KP 信号,先搜公司再加人;待查)
- **中国进口与管制**:国别档位 中(IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
