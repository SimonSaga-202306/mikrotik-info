# Nabacom

> **评级 A**　|　意大利　|　档案编号 `A-132`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-132
rating: A
country: 意大利
biz_org: 公司/工作室（有官网）
business_model: 工程/集成项目制
decision_speed: moderate
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；工程/集成项目制
- **商业模式**：工程/集成项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；人工指定
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 主场景匹配+首触只推一个型号的纪律；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Nabacom（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 意大利 | 事实 |
| 网站 | https://www.nabacom.it | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@nabacom.it（既有/公开）
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@nabacom.it [Publicly listed; delivery not tested]; https://www.nabacom.it
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（视频监控大项目接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：顺其 AI 视频监控与热成像线：普通+热成像混合项目的 24 口 PoE++（4×10G SFP+ 上行接长距光纤）。
- **要问的问题**：大监控项目的接入层现在配什么？（英意资料随附合规包）
- **随附证明**：规格对照 + 合规文件包 + 单端口测算（英意双语）。

### 第 2 次跟进 · 工业级非管理 PoE（室外热成像/周界点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：室外热成像与周界点位：宽温 DIN PoE+2.5G SFP 长距上行组合——他热成像项目的天然配套。
- **要问的问题**：热成像长距点位的供电与上行怎么做的？
- **随附证明**：宽温报告 + SFP 上行方案 + DIN 图。

### 第 3 次跟进 · 管理型 PoE（DC 交钥匙接入候选）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他 DC 交钥匙：接入层管理型（VLAN/ERPS/SNMP）进 BOM 候选，配 RMA 与备件条款给他的 H24 托管兜底。
- **要问的问题**：DC 项目的接入层 BOM 候选评估走什么流程？
- **随附证明**：VLAN/ERPS 模板 + RMA 条款 + 收敛实测（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第7批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：意大利全能基建集成商（srl）：网络/DC 交钥匙/视频监控/安防实体/云托管一体，Allied 伙伴（CSV 记录）。
- **产品线与在售品牌**：全栈：布线/网络/终端/话务/云/网安/视频监控（含热成像+AI+控制室）/DC 交钥匙/研发。
- **目标行业与场景**：企业与机构客户的机房与园区基建、视频监控大项目、楼宇自动化。
- **团队与规模**：sistemi senior 级工程师建制（官网岗位话术）；规模中型。
- **决策链与对接人**：info@nabacom.it（CSV 9-27 核验：联系页公开；注意别混萨尔瓦多 nabacom.com）。
- **技术与认证**：Allied 伙伴（CSV 记录）；官网设 Certificazioni 专页。
- **采购与供应链信号**：交钥匙 DC 与大监控项目=批量接入层与工业 PoE；H24 托管=对坏机率与 RMA 敏感。
- **近期动态与线索**：官网导航含 Whistleblowing 专页（欧盟合规意识强）——供应商审查正式化，材料要正规。
- **与我方契合点**：DC 交钥匙的接入层+监控项目（热成像长距=光纤 SFP 组合，正好配我们 SFP 上行件）。
- **风险与注意**：意大利文沟通起步：报价单先英文+关键段意文；医疗研发场景只做网络配套段；合规文件包随首封发。

### R54 原文证据摘录（全部保留）

- **【业务定位】**服务目录（Facciamo 页）：24×7×365 技术值守与服务台的网络/话务/服务器/安全/终端/视频监控/有线光纤 LAN 全托管商。
  > MANUTENZIONE — PRESIDI TECNICI E SISTEMICI, SERVIZI DI HELPDESK, INTERVENTI TECNICI ON SITE E/O DA REMOTO IN H24 365GG ANNO NEI SEGUENTI AMBITI: networking – fonia – server – sicurezza – endpoint – videosorveglianza – reti LAN e geografiche in rame e fibra ottica
  > 来源：https://www.nabacom.it/facciamo/
- **【产品线与在售品牌】**网络线全栈：路由-SDWAN-交换-Wi-Fi 的设计/供货/安装/配置+铜缆光纤布线与认证、楼宇自动化、门禁。
  > NETWORKING — PROGETTAZIONE, FORNITURA, INSTALLAZIONE E CONFIGURAZIONE APPARATI DI ROUTING – SDWAN – SWITCH – WI.FI – CABLAGGIO IN RAME ED IN FIBRA OTTICA, CON RELATIVE CERTIFICAZIONI, OPERE INFRASTRUTTURALI, BUILDING AUTOMATION, CONTROLLO ACCESSI
  > 来源：https://www.nabacom.it/facciamo/
- **【目标行业与场景】**交钥匙数据中心（含机架空调/UPS/柴发/消防/门禁）＋普通与热成像视频监控＋AI 分析——基建级交付能力。
  > DATA CENTER — PROGETTAZIONE E REALIZZAZIONE DI DATA CENTER CHIAVI IN MANO… VIDEOSORVEGLIANZA — SISTEMI DI VIDEOSORVEGLIANZA ORDINARIE E TERMICHE… SOFTWARE AVANZATI CON INTELLIGENZA ARTIFICIALE… VIDEOWALL – SALA CONTROLLO
  > 来源：https://www.nabacom.it/facciamo/
- **【近期动态与线索】**研发线与大学及软件公司合作做远程医疗/远程监护应用——⚠️ 医疗敏感场景存在（网络件只做配套段）。
  > RICERCA E SVILUPPO — SVILUPPIAMO IN COLLABORAZIONE CON UNIVERSITÀ E SOFTWARE HOUSE APPLICATIVI DI: telemedicina – teleconsulto – monitoraggio pazienti da remoto
  > 来源：https://www.nabacom.it/facciamo/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 主场景匹配+首触只推一个型号的纪律 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：【人工定级】A —— 自动规则已跳过；人工指定
- **W**：公开信息有限
- **O**：P1 场景切入（主场景匹配+首触只推一个型号的纪律）
- **T**：现有供应商惯性；价格竞争。

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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：8-port PoE with auto-recovery for your field deployments

```text
Hi Nabacom,

I came across Nabacom - 集成商/代理（Allied Telesis）.

We build a compact 8-port Gigabit PoE switch (240W budget, af/at) with a hardware PoE watchdog that power-cycles a frozen AP or camera automatically, plus clean 802.1Q VLAN / ERPS / sFlow on the management side. Reference: $99 USD EXW.

One question: How many PoE ports does a typical site of yours need today?

If it is useful, I can send one unit for a 30-day evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

Best regards,
Saga Communications - PoE switch OEM/ODM (neutral packing available)
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
