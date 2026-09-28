# HellasCom L.t.d.

> **评级 A**　|　希腊　|　档案编号 `A-024`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（工业/楼宇、组播/IPTV），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | HellasCom L.t.d. |
| 国家 | 希腊 |
| 城市 | — |
| 网站 | hellascom.gr |
| 类型 | 分销（MikroTik 官方） |
| 反向信号 | MikroTik（Master+VAD） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-488XGGPM（Saga） |
| 切入点 | 卖 MikroTik 但缺工业/ERPS/PoE++ → 用同价位工业线补他的产品缺口 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★★ 【升级：希腊 MikroTik 生态的源头】自述「**本公司是希腊第一家 MikroTik 分销商（2001 年起），并从 2011 年起是希腊的 MikroTik 培训中心**」。联系人 Smaragdos，+30 210 451 1087 / smarag@hellascom.gr。项目能力：HotSpot、Netinstall、脚本、桥接、RADIUS、3G/LTE、CAPsMAN、The Dude 监控、故障切换与负载均衡、隧道与 VPN、长距离无线 PtP/PtMP/Mesh、L7 流量整形、虚拟化、防火墙 Mangle、OSPF/BGP、QoS 与队列、**船用 WiFi 项目 Marine WiFi**、VoIP、网络视频流、RoIP、**KNX（楼宇自控总线）**、**IPTV 项目（用 MikroTik 组播）** → 分销+培训+集成三位一体，希腊第一优先账号 |

## 三、人员与联系方式

- **邮箱**：sales@hellascom.gr、smarag@hellascom.gr
- **电话**：+30 210 4523890
- **原始联系字段**：+30 210 4523890 / sales@hellascom.gr

## 四、品牌与技术栈

**涉及品牌 / 技术**：CAPsMAN、KNX、MikroTik、The Dude

## 五、跟进策略

**场景判断**：组播 / IPTV

### 推什么型号

**STC-424DGGPM-440W（Saga）（组播能力完整 + PoE 供电）**

> 系统初判型号：`STI-488XGGPM（Saga）`（供参考，以实际沟通为准）

### 核心卖点

IGMP Snooping v2/v3、IGMP Querier、组播 VLAN、快速离开（Fast Leave）、**QoS/DSCP 优先级队列**（Dante 音频 over IP 与 IPTV 都靠它不丢包不抖动）

### 怎么开发

开口就问「IPTV 卡不卡？是不是组播没配好，全楼在泛洪？」；若是 Dante / 音频 over IP 场景，改问「音频有没有出现过断续或丢包？」——Dante 对组播和 QoS 极敏感，说中就是内行

### 风险点

组播出问题是满屏花屏，客户零容忍；必须先小规模（一个楼层）验证再铺开；要确认他的组播源和播放器兼容性

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

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

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

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

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：酒店一层/一栋楼的 AP+IPTV+CCTV：24 口 PoE++ 一台吃下，重点讲 PoE 预算、端口隔离（客房/设备网段）与 250m 延长（老楼布线救急）。
- **要问的问题**：他们 hospitality 项目里 24 口 PoE 现在用什么型号、缺什么规格？
- **随附证明**：功率实测 + 老楼延长方案（250m/端口隔离）+ 与 CRS328-24P 对照。

### 第 2 次跟进 · 工业级非管理 PoE（隧道/机房外/塔站）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：隧道与高速公路现场的通信箱、隧道口设备柜：宽温宽压、DIN、免配置，配合他们的漏缆/PA 系统。
- **要问的问题**：隧道/道路项目的现场箱体目前用什么品牌规格？
- **随附证明**：宽温报告 + 双电源接线图 + 隧道场景选型页。

### 第 3 次跟进 · 管理型 PoE（IPTV 组播 + 环网）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）或 STC-424XGGPM-440W（Saga）（24×PoE + 4×SFP+）
- **切入点**：他们做 IPTV 与船用 WiFi：IGMP snooping/querier、组播 VLAN、ERPS 环网，直接对上技术标书条目。
- **要问的问题**：IPTV/组播项目里，他们对交换机最看哪几个指标？
- **随附证明**：组播不泛洪实测 + ERPS 收敛数据 + 招标参数条目（希腊语/英语）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：IGMP / multicast behaviour on your IPTV builds

```text
Hi HellasCom,

Multicast is where most IPTV and camera builds quietly fall over, and it is the part I specialise in on the access switch.

What caught my eye is that you work on IPTV, RADIUS, KNX, marine, VoIP, The Dude, CAPsMAN and Netinstall.

Where we may be useful: IGMP snooping v2/v3, a querier so the VLAN stops flooding, multicast VLAN, fast leave, and DSCP/QoS queues — the things that decide whether IPTV is watchable and whether Dante audio drops out.

Are you running IGMP snooping plus a querier, or still flooding the VLAN?

If it is easier to judge from hardware than from a datasheet, I can send a STI-488XGGPM evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

Either way, no follow-up sequence from me.

Best,
[your name]
```

> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；③ 落款换成你自己的名字与公司；④ 一次只问一个问题。

## 十一、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
