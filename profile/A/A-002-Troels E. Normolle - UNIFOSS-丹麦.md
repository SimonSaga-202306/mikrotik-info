# Troels E. Normolle / UNIFOSS

> **评级 A**　|　丹麦 · Lemming　|　档案编号 `A-002`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（酒店/多住户、工业/楼宇），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | UNIFOSS |
| 国家 | 丹麦 |
| 城市 | Lemming |
| 网站 | unifoss.com |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-IS6312XGP-4XS8GT |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 网络公司创始人，服务行业列举：**农业、能源与电网控制 Energy and grid control、音乐节 Festivals、医疗、酒店 Hospitality、ISP、办公、零售** → 电网控制与农业是工业级场景，音乐节是临时大容量组网，酒店是 PoE 接入，一家公司覆盖三种需求 |

## 三、人员与联系方式

- **对接人**：Troels E. Normolle
- **邮箱**：troels@unifoss.com
- **电话**：+45 2279 1234
- **原始联系字段**：+45 2279 1234 / troels@unifoss.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：酒店 / 多住户

### 推什么型号

**LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`LT-IS6312XGP-4XS8GT`（供参考，以实际沟通为准）

### 核心卖点

客房 VLAN 隔离、端口隔离（防客人私接路由器）、PoE 同时供 AP / IPTV 机顶盒 / IP 话机、组播 IPTV 不卡

### 怎么开发

问「一间客房下几根线？AP 怎么供电？IPTV 走不走组播？」——酒店是多期项目，一期做进去后面几期跟着走

### 风险点

酒店项目周期长且受装修进度牵制，别押季度指标；采购决定权常在弱电总包而非业主，要找到总包；客房网络出问题客人直接投诉，稳定性零容忍

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。

- **业务定位**：丹麦中小企业「网络即服务」商：网络+互联网按月出租（375 DKK/月起），另有更新协议（29 DKK/月）与维护协议（49 DKK/月），卖的是「不用操心的稳定运行」。
- **产品线与在售品牌**：未公开披露品牌清单；方案以 WiFi/网络为核心，含 Mesh 组网、跨楼组网（bygning til bygning）与高密度容量设计。
- **目标行业与场景**：案例三类可作画像：① 20,000 m² 仓储/办公楼（Erhvervshuset Midtjylland，租户数量经常变化）；② 高密度学校（Nørgaards Højskole，流媒体/社媒压力）；③ 老建筑酒店/客栈（Kongensbro Kro，要求不破坏观感、尽量少布线 → 全靠 PoE 接入）。CSV 记录的服务行业还包括农业、能源与电网控制、音乐节、医疗、ISP、零售。
- **团队与规模**：小团队（官网团队照与创始人 Troels 出镜）；以服务协议+外包安装为主，规模不大、决策链短。
- **决策链与对接人**：Troels E. Normolle（创始人）；troels@unifoss.com；+45 2279 1234。
- **技术与认证**：MikroTik 认证顾问（MTCNA+MTCRE，见档案原始记录与官方名录）；方案语言是「容量/覆盖/服务协议」，不是芯片参数。
- **采购与供应链信号**：按月出租设备意味着设备是他们的资产：单价、故障率、远程可维护性（能远程重启/恢复）比一次性毛利更重要。
- **近期动态与线索**：2026 年继续用案例营销（Erhvervshuset / Nørgaards Højskole / Kongensbro Kro 三个 case study），并在网站强调「先看现有网络能不能升级，不行才整套换新」。
- **与我方契合点**：他们做的每一个案例都需要一台多口 PoE 交换机喂 AP：学校（教室 AP）、仓储（大范围覆盖）、酒店（藏在吊顶/柜里的静音供电口）。PoE 看门狗 + 远程重启对我们而言是「减少上门次数」= 直接降低他服务协议的成本。
- **风险与注意**：他不卖硬件参数，卖服务；沟通要换算成「少一趟上门 = 多少钱」。另外丹麦市场对能效/电压合规敏感。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**网络按月租：设备+互联网+服务打包，另设更新与维护协议。
  > Internet og WiFi — Lej en komplet netværksløsning – inklusiv internet. Fra 375,- / md.；Opdateringsaftale Fra 29,- / md.；Vedligeholdelsesaftale Fra 49,- / md.
  > 来源：https://unifoss.com/
- **【目标行业与场景】**仓储存量改造案例：2 万 m²、用户数经常变化、要求可扩展。
  > Erhvervshuset Midtjylland udlejer over 20.000 m2 lagerplads … Det eksisterende netværk var aldrende … Et skalerbart system, som kan tilpasses det skiftende antal lejere. Én centralt styret system med mindre administration.
  > 来源：https://unifoss.com/
- **【目标行业与场景】**酒店/客栈场景明确要「少布线、别破坏观感」——PoE 接入是唯一解。
  > Kongensbro Kro … Diskret installation, der skåner den fine, gamle bygning. Moderne MESH teknologi … Minimeret kabeltræk, så man undgår synlige ledninger og bokse.
  > 来源：https://unifoss.com/
- **【采购与供应链信号】**先修后换的商业逻辑，说明他对设备生命周期成本敏感。
  > Vi sælger jer ikke noget, I ikke har brug for. Kan jeres nuværende netværk opgraderes og repareres til en god standard, anbefaler vi dét.
  > 来源：https://unifoss.com/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：按「少一趟上门」算钱：24 口 PoE 喂 AP/摄像头，PoE 看门狗把挂死的设备自动断电重启——他的服务协议里最贵的就是上门。
- **要问的问题**：他现在的服务协议里，每个月有多少次是因为 AP/摄像头死机要上门的？
- **随附证明**：看门狗实测（断电重启日志）+ 远程重启/批量升级的演示配置。

### 第 2 次跟进 · 工业级非管理 PoE（现场电箱/室外）

- **推什么**：LT-IS6306G-2GX4GT PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：农业、能源与电网控制、音乐节这些场景设备都装在非机房环境：宽温宽压、DIN 导轨、免配置，配一个小机箱就是一个现场节点。
- **要问的问题**：有没有装在现场（农机房、配电箱、临时场地）的网络节点？
- **随附证明**：宽温测试报告 + 一页现场接线图 + 样品机。

### 第 3 次跟进 · 管理型 PoE（多站点统一运维）

- **推什么**：LT-IS6312G-4GX8GT PoE 版（8G + 4×2.5G SFP，管理型）
- **切入点**：他管的是「一批客户的一堆站点」：统一 VLAN/端口模板 + 环网冗余，让不同客户的站点用同一套模板交付维护。
- **要问的问题**：多客户/多站点之间，他希不希望用同一套交换机配置模板来运维？
- **随附证明**：配置模板 + 环网切换实测 + 集中管理（SNMP/MIB）清单。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：PoE + VLAN per room — question on your hotel jobs

```text
Hi Troels,

I build PoE access switches for hotel and multi-dwelling networks, which is where you seem to spend most of your time.

What caught my eye is that you work on hospitality, grid control and festival.

Where we may be useful: 24 gigabit PoE++ ports (APs, IP phones and IPTV boxes on one cable), per-room VLAN isolation, port isolation to stop guests plugging in their own router, IGMP snooping for the TV.

How many drops per room, and is your IPTV running on multicast?

If it is easier to judge from hardware than from a datasheet, I can send a LT-IS6312XGP-4XS8GT evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
