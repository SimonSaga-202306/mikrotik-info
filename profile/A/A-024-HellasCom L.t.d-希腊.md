# HellasCom L.t.d.

> **评级 A**　|　希腊　|　档案编号 `A-024`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-024
rating: A
country: 希腊
biz_org: 公司/工作室（有官网）
business_model: 培训交付
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: true, oem: false, hotel: true, training: true}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：有明确交换/供电需求（工业/楼宇、组播/IPTV），且有具体人直联
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — HellasCom 酒店 6Play 楼层标准件（WiFi/IPTV/CCTV/VoIP 混载）；隧道/机场公共段不跟，仅私营酒店线；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Roughly how many site visits a month come from a hung AP or camera across your hospitality sites?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | HellasCom L.t.d.（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 希腊 | 事实 |
| 网站 | hellascom.gr | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Master+VAD） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】希腊 HellasCom LTD（Piraeus, 12 Themistokleous Coast, Freatyda 185 36；sales@hellascom.gr；+30 210 4511087 / +30 210 4523890；官网 hellascom.gr 产品线列 MikroTik/TAIT/Ruckus/Omnitronics/Zetron/IPTV）。LinkShop.GR 官方 Facebook 页自曝：HellasCom 是希腊首家 MikroTik Certified Sales Associate、MikroTik value added Distributor，并列点名 Stavros Maragoudakis 与 Eleftherios Liodakis。LinkedIn 命中 Stavros Maragkoudakis（自署 HELLASCOM LTD，MikroTik Certified Trainer，名下 LinkShop.GR 商城与 mikrotiktraining.gr 培训中心）与 George Maragoudakis（worksFor HELLASCOM LTD，1972 年起创业）。排噪：SEVE 所登 HellasCom International S.A.（Marousi，OTE 集团）同名异司已排。
- 【推断】R69 第 1 波 KP 猎获（LinkedIn 谱面 + 官方页点名双锚）
- 【假设】分销位 KP 双锁；LinkedIn 猜测位直发需 opt-in；公司邮箱转接

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik（Master+VAD））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、VoIP/Voice VLAN、酒店/多住户、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖
  - 酒店/多住户：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@hellascom.gr
  - 状态：既有/公开
- **电话**：+30 210 4523890
- 来源等级：official-channel（R41–R48 联系方式台账口径）
- **原始联系字段**：+30 210 4523890 / sales@hellascom.gr
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Stavros Maragkoudakis**(MikroTik Certified Trainer / 培训中心与商城负责人)— LinkedIn 公开面（公司邮箱 sales@hellascom.gr 转接） 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://www.linkedin.com/in/maragkoudakisstavros/〕
  - **George Maragoudakis**(资深/疑似创始（1972 年起创业）)— LinkedIn 公开面 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://www.linkedin.com/in/george-maragoudakis-838a5431/〕
  - **Eleftherios Liodakis**(公司代表（FB 官页点名，职衔待核）)— 无公开邮箱；FB 官页点名 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://www.facebook.com/linkshopgr/〕

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Stavros Maragkoudakis | MikroTik Certified Trainer / 培训中心与商城负责人 | LinkedIn 公开面（公司邮箱 sales@hellascom.gr 转接） | leads-only·待 opt-in（LinkedIn 公开面；FB 官页点名加持） | https://www.linkedin.com/in/maragkoudakisstavros/ |
| George Maragoudakis | 资深/疑似创始（1972 年起创业） | LinkedIn 公开面 | leads-only·待 opt-in（LinkedIn 公开面） | https://www.linkedin.com/in/george-maragoudakis-838a5431/ |
| Eleftherios Liodakis | 公司代表（FB 官页点名，职衔待核） | 无公开邮箱；FB 官页点名 | leads-only·待 opt-in（FB 官页点名） | https://www.facebook.com/linkshopgr/ |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：酒店一层/一栋楼的 AP+IPTV+CCTV：24 口 PoE++ 一台吃下，重点讲 PoE 预算、端口隔离（客房/设备网段）与 250m 延长（老楼布线救急）。
- **要问的问题**：他们 hospitality 项目里 24 口 PoE 现在用什么型号、缺什么规格？
- **随附证明**：功率实测 + 老楼延长方案（250m/端口隔离）+ 与 CRS328-24P 对照。

### 第 2 次跟进 · 工业级非管理 PoE（隧道/机房外/塔站）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：隧道与高速公路现场的通信箱、隧道口设备柜：宽温宽压、DIN、免配置，配合他们的漏缆/PA 系统。
- **要问的问题**：隧道/道路项目的现场箱体目前用什么品牌规格？
- **随附证明**：宽温报告 + 双电源接线图 + 隧道场景选型页。

### 第 3 次跟进 · 管理型 PoE（IPTV 组播 + 环网）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）或 STC-424XGGPM-440W（Saga）（24×PoE + 4×SFP+）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：他们做 IPTV 与船用 WiFi：IGMP snooping/querier、组播 VLAN、ERPS 环网，直接对上技术标书条目。
- **要问的问题**：IPTV/组播项目里，他们对交换机最看哪几个指标？
- **随附证明**：组播不泛洪实测 + ERPS 收敛数据 + 招标参数条目（希腊语/英语）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：比雷埃夫斯的技术-贸易公司（1998 年成立、ISO 9001:2015、28+ 年、500+ 项目）：网络基础设施、酒店/机场 hospitality 方案、隧道与高速公路通信、无线电系统；**希腊第一家 MikroTik 分销商（2001 起）+ 认证培训中心（2011 起）**。
- **产品线与在售品牌**：自营网店 LinkShop.gr 面向经销商；代理/分销品牌含 MikroTik、Ruckus(CommScope)、TAIT、Omnitronics、Zetron、BHE、Teleste、2N(Axis)、Yeastar、Snom、Fanvil、Dahua、Hikvision、Cambium、Mimosa(Airspan)、Ubiquiti、TP-Link、Synology、LeoLabs、3CX。
- **目标行业与场景**：四个主战场：① 酒店/民宿/机场（WiFi、IPTV、CCTV、VoIP、光纤）；② 隧道与高速公路（漏缆、IP-PA、多传感器 SCADA：Aktio-Preveza 海底隧道、Kakia Skala 隧道、地拉那-爱尔巴桑隧道、Rio-Antirrio 大桥、Skaramangas 船厂、Egnatia 高速）；③ 航运与公共安全（radio/PTT/RoIP）；④ 企业网络与 IT 支持。
- **团队与规模**：自设研发/集成/技术支持部门（连停产件的备件级支持都做）+ 进口部门 + 物理门店（Ακτή Θεμιστοκλέους 12, Πειραιάς），船用 WiFi、KNX 楼宇自控、IPTV 组播项目经验。
- **决策链与对接人**：Smaragdos（smarag@hellascom.gr；+30 210 451 1087）；销售部 sales@hellascom.gr；总机 +30 210 4523890。
- **技术与认证**：MikroTik 官方分销 + 认证培训（讲师含 10 证）；项目能力涵盖 HotSpot/Netinstall/脚本/桥接/RADIUS/3G-LTE/CAPsMAN/The Dude/故障切换与负载均衡/隧道 VPN/长距离 PtP-PtMP-Mesh/L7 流量整形/虚拟化/防火墙 Mangle/OSPF-BGP/QoS/KNX/IPTV。
- **采购与供应链信号**：他是「希腊 MikroTik 生态的源头」：既能吃我们的货进 LinkShop.gr 零售/分销，又能在 hospitality 与隧道项目里把型号写进标书；工业/宽温/高 PoE 规格是其 MikroTik 线目前缺的补位。
- **近期动态与线索**：官网 2026 年在线并突出 hospitality（基克拉泽斯、克里特、阿提卡、十二群岛、爱奥尼亚）；2026 年 10–11 月 MTCNA/MTCSE 课程在其培训中心开课（见 A-022）。
- **与我方契合点**：酒店 6Play、IPTV 组播、隧道 SCADA、船用 WiFi：全是接入层 PoE + 光纤 + 组播分段的场景；工业款可补他 MikroTik 体系没有的宽温/导轨线。
- **风险与注意**：同体系账号 A-022（培训中心）——技术对话走 A-022、商务/项目走这里，避免双报价；他是本地龙头，谈「补规格 + 第二供应商」而不是替代。

### R54 原文证据摘录（全部保留）

- **【业务定位】**公司概况与数据（1998 成立、ISO、项目数）。
  > Η HELLASCOM είναι Τεχνική - Εμπορική εταιρεία … Βρίσκεται στο χώρο από το 1998；1998 Ίδρυση｜ISO 9001 : 2015｜28+ Χρόνια Εμπειρίας｜500+ Ολοκληρωμένα Έργα
  > 来源：https://www.hellascom.gr/el
- **【目标行业与场景】**隧道/高速公路与大型基础设施项目清单（含漏缆、IP-PA、SCADA）。
  > Ραδιοεπικοινωνιακά συστήματα Trunking & Ακτινοβολούντος Καλωδίου, Ανακοινώσεις IP-PA & Multi-Sensors SCADA σε μεγάλα έργα: Υποθαλάσσια σήραγγα Ακτίου-Πρεβέζης, Σήραγγα Κακιάς Σκάλας, Διπλή σήραγγα Τιράνων-Ελμπασάν, Γέφυρα Ρίου-Αντιρρίου, Ναυπηγεία Σκαραμαγκά, Σήραγγες Εγνατίας
  > 来源：https://www.hellascom.gr/el
- **【目标行业与场景】**酒店/民宿主推位：WiFi/IPTV/CCTV/VoIP/光纤，覆盖岛屿与 mainland 旅游区。
  > WiFi, IPTV, CCTV, VoIP PBX, Οπτικές Ίνες & Δίκτυα - Εξειδικευμένες υπηρεσίες για Ξενοδοχεία, AirBNB & Καταλύματα σε Κυκλάδες, Κρήτη, Αττική, Δωδεκάνησα & Επτάνησα
  > 来源：https://www.hellascom.gr/el
- **【产品线与在售品牌】**自述为 MikroTik 分销商与认证培训方（2001 起），并列出自营网店与培训中心。
  > Ως Distributors & Certified Trainers MikroTik από το 2001, αντιπρόσωποι TAIT, Omnitronics, Zetron, BHE & Ruckus；Το e-shop μας (LinkShop.gr) παρέχει στους μεταπωλητές και πελάτες μια καινοτόμα επιλογή αξιόπιστων προϊόντων
  > 来源：https://www.hellascom.gr/el

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-10-09_R69_R56_KP第1波.json`；价格均为 EXW 快照。


### R55 证据摘录（全部保留 · 含数量）

- **【证据】**sales@hellascom.gr · +30 210 4511087 / +30 210 4523890 · 12 Themistokleous Coast, Freatyda, Piraeus 185 36, Greece（官网产品页联系方式）
  > sales@hellascom.gr · +30 210 4511087 / +30 210 4523890 · 12 Themistokleous Coast, Freatyda, Piraeus 185 36, Greece（官网产品页联系方式）
  > 来源：https://www.hellascom.gr/en/products
- **【证据】**Stavros can introduce you to 1 people at HELLASCOM LTD · MikroTik Certified Trainer · linkshop.gr / mikrotiktraining.gr
  > Stavros can introduce you to 1 people at HELLASCOM LTD · MikroTik Certified Trainer · linkshop.gr / mikrotiktraining.gr
  > 来源：https://www.linkedin.com/in/maragkoudakisstavros/
- **【证据】**HellasCom L.t.d. is 1st #MikroTik Certified Sales Associate and is recognized as a MikroTik value added Distributor in Greece. Stavros Maragoudakis and Eleftherios Liodakis
  > HellasCom L.t.d. is 1st #MikroTik Certified Sales Associate and is recognized as a MikroTik value added Distributor in Greece. Stavros Maragoudakis and Eleftherios Liodakis
  > 来源：https://www.facebook.com/linkshopgr/
- **【证据】**Experience: HELLASCOM LTD · Location: Greece（George Maragoudakis，1972 年起创业）
  > Experience: HELLASCOM LTD · Location: Greece（George Maragoudakis，1972 年起创业）
  > 来源：https://www.linkedin.com/in/george-maragoudakis-838a5431/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：希腊 MikroTik value added 分销（TAIT/Ruckus/Omnitronics 多线）
- **决策链与对接人**：KP 双锁（Stavros 主对口）
- **产品线与在售品牌**：MikroTik（官方 VAD）+ TAIT/Ruckus/Omnitronics/Zetron
- **团队与规模**：希腊 Piraeus 总部
- **技术与认证**：MikroTik Certified Sales Associate（希腊首家）
- **采购与供应链信号**：分销采购线
- **近期动态与线索**：Stavros 2026-05 活跃发布 MikroTik 产品动态（hAP be lite 文）

## 同谱竞合谱注（R67：MikroTik 官方分销位竞合判定）

> 谱注日期 **2026-10-08**；来源=CSV 类型/信号列+R54/R55 深挖档；原始记录：`batch/A类竞合谱注_2026-10-08_R67_批1.json`。本节为定位判定，不改级、不改档。

- **官方位**：MikroTik（Master+VAD）
- **谱位**：安防接入
- **判定**：该户为 MikroTik 官方分销(Master+VAD)+VAD 认证价值型:其 MikroTik 授权位/服务网=不可替资产,我方不与 MT 官方线硬碰;谱策=安防集成位:补位谱=PoE++ 大功率(PTZ)/工业温宽位,摄像接入层对口。报价纪律=补位不硬冲(MT 有 SKU 的型号不报价;MT 空档报 STC/STI 谱)。

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | HellasCom 酒店 6Play 楼层标准件（WiFi/IPTV/CCTV/VoIP 混载）；隧道/机场公共段不跟，仅私营酒店线 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：有明确交换/供电需求（工业/楼宇、组播/IPTV），且有具体人直联

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 教师红线：不打学员名单、不经培训语境推销

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
  - [ ] KP 个人邮箱未公开
  - [ ] Eleftherios Liodakis 职衔待核

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
sales@hellascom.gr
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
