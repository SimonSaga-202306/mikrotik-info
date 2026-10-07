# Troels E. Normolle / UNIFOSS

> **评级 A**　|　丹麦 · Lemming　|　档案编号 `A-002`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-002
rating: A
country: 丹麦
biz_org: 一人公司（TEN INVEST ApS 100% 控股壳）
business_model: 订阅制 NaaS（375 DKK/月起租网+29 更新+49 维保）
decision_speed: fast
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：**UNIFOSS ApS**（CVR **DK-35517111**），丹麦 Lemming（Østerbyvej 35, 8632），业主 **Troels Elkjær Nørmølle** 100% 经 TEN …
- **商业模式**：订阅制 NaaS（375 DKK/月起租网+29 更新+49 维保）
- **为什么值得跟**：有明确交换/供电需求（酒店/多住户、工业/楼宇），且有具体人直联
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — 租约盒主打少上门+低至 $99 即 2 个月租金回本；学校/仓储 24 口升档在第 2 步再谈；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Roughly how many site visits a month come from a hung AP or camera on your networks?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Troels E. Normolle / UNIFOSS（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 丹麦 / Lemming | 事实 |
| 网站 | unifoss.com | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Troels E. Normolle | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE | 事实（名录/自报口径） |
| 组织性质 | 一人公司（TEN INVEST ApS 100% 控股壳） | 【推断】 |
| 商业模式 | 订阅制 NaaS（375 DKK/月起租网+29 更新+49 维保） | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |
| R55·背景深描 | **UNIFOSS ApS**（CVR **DK-35517111**），丹麦 Lemming（Østerbyvej 35, 8632），业主 **Troels Elkjær Nørmølle** 100% 经 TEN INVEST ApS 控股，任两公司董事（2013-10 起）。公开设计外包档案自述「**one-person business**」。盈利 | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 站点未列明设备品牌（服务化包装，硬件被租约遮蔽）；三个案例的容量/骨干/MESH 描述指向 MikroTik 或同级 PoE 交换+无线。出货量：未公开——可用租约客户数×每点 1–3 台 PoE 交换估算隐性吞量。客户反馈：三段案例引用（Lars Maretti、Nørgaards、Christian Andersen 口径均正面）。 | 事实+【推断】混合，见证据摘录 |
| 批注 | 酒店只是 3 个案例之一且无 IPTV 证据；主推位=租约盒 8 口 PoE，不是 24 口酒店机 | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

站点未列明设备品牌（服务化包装，硬件被租约遮蔽）；三个案例的容量/骨干/MESH 描述指向 MikroTik 或同级 PoE 交换+无线。出货量：未公开——可用租约客户数×每点 1–3 台 PoE 交换估算隐性吞量。客户反馈：三段案例引用（Lars Maretti、Nørgaards、Christian Andersen 口径均正面）。

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- **UNIFOSS ApS**（CVR **DK-35517111**），丹麦 Lemming（Østerbyvej 35, 8632），业主 **Troels Elkjær Nørmølle** 100% 经 TEN INVEST ApS 控股，任两公司董事（2013-10 起）。公开设计外包档案自述「**one-person business**」。盈利侧：ownr.dk 载 UNIFOSS ApS 2024-25 净利 **506k DKK**、权益 475k DKK——一人公司做到 50 万丹麦克朗净利，现金流健康。模式=**设备租赁/订阅制网络运营商**：包月（375 起）含设备+更新（29/月）+维保（49/月）。案例：Erhvervshuset Midtjylland（2 万㎡仓储）、Nørgaards Højskole（骨干替换）、Kongensbro Kro（1648 年老旅馆 MESH）。

## 联系方式（已有/猜测分标）

- **邮箱**：troels@unifoss.com
  - 状态：既有/公开
- **电话**：+45 2279 1234
- **原始联系字段**：+45 2279 1234 / troels@unifoss.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Troels Elkjær Nørmølle | 业主/执行董事（TEN INVEST ApS→UNIFOSS ApS 100%） | troels@unifoss.com；info@unifoss.com；+45 2279 1234 | 邮箱官网+CSV 双源；MX 已验 | https://unifoss.com/ ・ https://ownr.dk/users/public-profile/4000636356 |
| —（社媒入口） | 业主本人社媒 | ownr 档案挂 LinkedIn/Facebook/Twitter 链接 | 入口已见，URL 未逐一展开（点击需登录） | https://ownr.dk/users/public-profile/4000636356 |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 租约盒 8 口 PoE（少上门=省钱）

- **推什么**：STC-28DGGPM（P1；$99 USD EXW 2026-09-28 快照 15 天）（统一口径=P1 系列，不外溢）
- **切入点**：他按月出租整套网络：每台交换机都是他自己的资产，每次上门都是他自己的成本。PoE 看门狗自动冷重启卡死 AP/摄像头，一趟上门≈500–1000 DKK 工时油费
- **要问的问题**：Roughly how many call-outs a month come from a hung AP or camera on your rental networks?（全封信只问这一个问题）
- **随附/动作**：无附页；一句话带过 802.1Q 干净透传+远程管理，网页页脚规格链接即可

### 第 2 次跟进 · 骨干/24 口升档（学校·仓储大单）

- **推什么**：STC-424XGGPM-280W（备选1；$165）/ STC-424XGGM（备选2；$143，L2+/L3 两档）（统一口径=P1 系列，不外溢）
- **切入点**：Nørgaards 仓储与学校案例是 24 口+万兆上联的自然台阶；只在第 1 步有信号后进入
- **要问的问题**：在学校和仓储这两个案例上，单站接入端口数通常是多少？现在骨干什么品牌？
- **随附/动作**：L2+ 特性表 1 页（ERPS<20ms/QinQ/Private VLAN/sFlow）+ Voice VLAN 注明仅 L2+ 系

### 第 3 次跟进 · 户外/工业补位（农业·电网·音乐节，CSV 备注未证）

- **推什么**：STI-288GP（备选；$74.8，3 年保）（统一口径=P1 系列，不外溢）
- **切入点**：CSV 备注行的农业/电网/音乐节方向**未经官网证实**【假设】：先用一个问题验证再推，不当作事实开价
- **要问的问题**：Do you actually take outdoor/temporary-event nodes today, or were those older engagements?
- **随附/动作**：STI-288GP 规格摘要（冗余 DC44–57V、250m 延伸、DIN 轨）；⚠️ 商用线 1 年保 vs 工业线 3 年保——对「设备寿命=承诺」的他，说明边界别含糊


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。以下为要点压缩，证据原文全部保留。

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

### R54 原文证据摘录（全部保留）

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

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类深挖_2026-09-28_R55_第1批.json`；价格均为 EXW 快照。

- **背景深描**：**UNIFOSS ApS**（CVR **DK-35517111**），丹麦 Lemming（Østerbyvej 35, 8632），业主 **Troels Elkjær Nørmølle** 100% 经 TEN INVEST ApS 控股，任两公司董事（2013-10 起）。公开设计外包档案自述「**one-person business**」。盈利侧：ownr.dk 载 UNIFOSS ApS 2024-25 净利 **506k DKK**、权益 475k DKK——一人公司做到 50 万丹麦克朗净利，现金流健康。模式=**设备租赁/订阅制网络运营商**：包月（375 起）含设备+更新（29/月）+维保（49/月）。案例：Erhvervshuset Midtjylland（2 万㎡仓储）、Nørgaards Højskole（骨干替换）、Kongensbro Kro（1648 年老旅馆 MESH）。
- **芯片与在用型号**：站点未列明设备品牌（服务化包装，硬件被租约遮蔽）；三个案例的容量/骨干/MESH 描述指向 MikroTik 或同级 PoE 交换+无线。出货量：未公开——可用租约客户数×每点 1–3 台 PoE 交换估算隐性吞量。客户反馈：三段案例引用（Lars Maretti、Nørgaards、Christian Andersen 口径均正面）。
- **关键人KP**：**Troels Elkjær Nørmølle**（拼写以登记为准：Nørmølle；CSV 作 Normolle）=唯一决策人。邮箱 **troels@unifoss.com**（既有）+ **info@unifoss.com**（官网页脚公开）+ 电话 +45 2279 1234。ownr 公开档案挂 LinkedIn/Facebook/Twitter 入口。MX 已验 Google Workspace。
- **关注点与资质**：①**长期主义**：案例话术全是「langtidsholdbar / fremtidssikrer」——设备寿命与保修年限是他对客户的承诺点（Saga 工业 3 年保可直接对上）；②可扩容/可服务性（skalerbart）；③服务协议定价成熟（SaaS 式收费，硬件成本敏感度中等——设备越便宜租约毛利越高）；④未参展痕迹，获客靠电工转介（Birger Brødløs 案例）与口碑。
- **优缺点SWOT**：**S**：一人决策零链条、净利健康、三个可引用案例覆盖仓储/教育/酒店、订阅模式锁客。**W**：一人=单点故障与带宽上限；无技术团队页；品牌能见度低（2020 年才做品牌重塑）。**O**：租约毛利模型下，设备降本直接增厚利润——Saga 8口 PoE EXW $99 对欧洲同级半价的吸引力直接；骨干替换案例证明他做大单。**T**：若 MikroTik/UniFi 给他体系内优惠价，第二供应商说服成本上升；一人公司采购节奏慢。
- **Saga产品适配**：租约盒首选 **STC-28DGGPM**（8口 PoE af/at 240W，**EXW $99**，DC 输入随附电源）；学校/仓储骨干替换对标他 Nørgaards 案例 → **STC-424XGGM**（4×10G+24GE，**EXW $143**）；旅馆 MESH 前端 PoE → **STC-48DGGPM-U**（**EXW $115.5**）。卖点对齐：「设备寿命=3 年保（工业线）/1 年（商用）+ 一次性买断，租约期内零品牌溢价」。报价 EXW 15 天有效。

### R55 证据摘录（全部保留 · 含数量）

- **【法定信息】**UNIFOSS ApS，CVR DK-35517111，Østerbyvej 35, 8632 Lemming，info@unifoss.com。
  > UNIFOSS ApS … Adresse: Østerbyvej 35, 8632 Lemming … CVR: DK-35517111
  > 来源：http://www.unifoss.com/
- **【股权与盈利】**Troels 100% 控股（TEN INVEST ApS），2024-25 净利 506k DKK。
  > TEN INVEST ApS Ejerandel: 100% … Det bedste regnskab i 2024-25 var et overskud på 506' DKK (UNIFOSS ApS).
  > 来源：https://ownr.dk/users/public-profile/4000636356
- **【一人公司】**品牌重塑供应商档案确认一人公司形态。
  > Unifoss is one-person business owned and founded by Troels E. Nørmølle.
  > 来源：https://www.victoriataulbaek.dk/kopi-af-airshoot
- **【商业模式】**设备打包进月租（375 起）+更新/维保订阅。
  > Lej en komplet netværksløsning – inklusiv internet. … Fra 375,- / md.
  > 来源：https://unifoss.com/
- **【骨干替换能力】**Nørgaards Højskole 案例=整网骨干替换，大单能力证据。
  > Udskiftning af rygraden i netværket for at håndtere den massive datamængde.
  > 来源：https://unifoss.com/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 租约盒主打少上门+低至 $99 即 2 个月租金回本；学校/仓储 24 口升档在第 2 步再谈 |
| 备选2 | STC-424XGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

**S**：一人决策零链条、净利健康、三个可引用案例覆盖仓储/教育/酒店、订阅模式锁客。**W**：一人=单点故障与带宽上限；无技术团队页；品牌能见度低（2020 年才做品牌重塑）。**O**：租约毛利模型下，设备降本直接增厚利润——Saga 8口 PoE EXW $99 对欧洲同级半价的吸引力直接；骨干替换案例证明他做大单。**T**：若 MikroTik/UniFi 给他体系内优惠价，第二供应商说服成本上升；一人公司采购节奏慢。

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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：Fewer call-outs on your rental network boxes

```text
Hi Troels,

You rent complete networks to Danish businesses (Erhvervshuset, Nørgaards Højskole, Kongensbro Kro), so every switch in the field is your own asset - and every call-out is your own cost.

We build PoE switches with a hardware watchdog that power-cycles a frozen AP or camera automatically, with clean 802.1Q VLAN and remote management, so they sit quietly downstream of MikroTik cores. The 8-port PoE unit (STC-28DGGPM, 240W, af/at) is $99 USD EXW (price snapshot 2026-09-28, valid 15 days) - against a 375 DKK/month rental box, the hardware pays for itself in about two months of rent.

One question: roughly how many call-outs a month come from a hung AP or camera on your networks?

If useful, I can ship one 8-port unit to Lemming to try on a single site for 30 days. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)
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
