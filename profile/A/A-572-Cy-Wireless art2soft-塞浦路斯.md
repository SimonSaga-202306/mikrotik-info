# Cy-Wireless（art2soft）

> **评级 A**　|　塞浦路斯　|　档案编号 `A-572`　|　优先级 ★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-572
rating: A
country: 塞浦路斯
biz_org: 公司/工作室（有官网）
business_model: 六牌官方分销
decision_speed: fast
price_sensitivity: medium
volume_potential: 3  # 1-5
needs: {poe: true, industrial: false, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-10-06
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；六牌官方分销
- **商业模式**：六牌官方分销
- **为什么值得跟**：通用分销商信号，无差异化切入点，慢慢跟 【2026-10-06 R63 B升A批复第1波】原 B-105；理由:六牌官方分销(UBNT/MikroTik/Cambium/RF Elements/Fanvil/Yeastar),Cyprus 官方认证经销名录(altostrat/FB)
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — 【2026-10-06 R63 B升A】六牌官方分销画像；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which 24-port managed PoE+ model currently carries your enterprise/WISP builds?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Cy-Wireless art2soft（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 塞浦路斯 | 事实 |
| 网站 | prod.cy-wireless.com | 事实 |
| 类型 | 六牌官方分销 | 事实（CSV 名录口径） |
| 关键人 | Cy-Wireless art2soft | 事实 |
| 反向信号（资质/品牌） | MikroTik（Reseller） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 六牌官方分销 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik（Reseller））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@cy-wireless.com
  - 状态：official-company
- **电话**：+357 22 814 244 
- **原始联系字段**：info@cy-wireless.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Cy-Wireless art2soft**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次 · 首触（P1 单型号 + 一个问题）

- **推什么**：STC-424XGGPM-280W（24口 PoE + 4×10G）
- **要问的问题**：Which 24-port managed PoE+ model currently carries your enterprise/WISP builds?
- **成功标准**：对方回复任一实质信息（现用品牌/端口数/上门频次）或同意收样机
- **失败退出**：14 天无回复 → 进入季度低频；退信 → 标记通道失效换 KP

### 第 2 次 · 价值换信息

- **动作**：补一份 1 页特性摘要（L2+ 特性表），再问一个递进问题
- **成功标准**：给出场景细节或引荐技术对接人
- **失败退出**：再无回复 → 降为季度触达

### 第 3 次 · 收束

- **动作**：明确提议 30 天评估样机或确认无需求后归档
- **成功标准**：样机单/报价请求
- **退出**：书面无兴趣或三次均无实质回应 → **停止主动开发**（停止条件见红线节）


## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 【2026-10-06 R63 B升A】六牌官方分销画像 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：通用分销商信号，无差异化切入点，慢慢跟 【2026-10-06 R63 B升A批复第1波】原 B-105；理由:六牌官方分销(UBNT/MikroTik/Cambium/RF Elements/Fanvil/Yeastar),Cyprus 官方认证经销名录(altostrat/FB)
- **W**：公开信息有限
- **O**：P1 场景切入（【2026-10-06 R63 B升A】六牌官方分销画像）
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

**主题**：24-port PoE + 10G uplinks for your larger sites

```text
Hi Cy-Wireless,

I came across Cy-Wireless art2soft - 六牌官方分销.

We build a 24-port Gigabit PoE switch (280W, af/at) with 4×10G SFP+ uplinks, Voice VLAN and a hardware PoE watchdog that reboots hung APs/cameras without a site visit. Reference: $180 USD EXW.

One question: Which 24-port managed PoE+ model currently carries your enterprise/WISP builds?

If it is useful, I can send one unit for a 30-day evaluation - just tell me where to ship it. If not a fit, one line and I close the loop.

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

---

## 备护深挖(2026-09-29 · R57-BC 轻量对齐 A · 评级不动、不出信）

**深挖三层**
- 【事实】A.K. ART2SOFT LTD / CY-WIRELESS(Nicosia Lakatameia;2006 创,**起点即 Ubiquiti 分销面向 WISP 市场**;2009 扩路由交换,**2012 加 VoIP 谱(IP PBX/SIP 话机/网关)**,后加布线/UPS;自述 500+ 分销商/2000+ 客户/10000+ 项目;具名 Theodoulos Vikarios(采购与业务开发)、Timoleon Charilaou(销售工程师);thomas.thoma@art2soft.com)
- 【推断】塞浦路斯 WISP→VoIP 专营分销:12+ 年 IP 话机谱=桌面话机 PoE 随单场景厚(Voicenter 逻辑),WISP 侧又带站点位
- 【假设】开口角度=「话机+WISP 双谱的 PoE 随单位」:STC-424 主力档,具名 Theodoulos(采购)开口

**SWOT 速描**
- **S**: WISP+VoIP 双专谱 500+ reseller
- **W**: 实体团队小(壳 4 人)
- **O**: 桌面话机 PoE 随单放量
- **T**: 单岛市场规模上限

**证据（quote → 来源）**
- 「ART2SOFT was founded in 2006 with its primary focus to distribute Ubiquiti wireless products primarily for the emerging WISP market … in 2012 to VoIP products including IP PBX systems, SIP phones, Gateways」 — https://prod.cy-wireless.com/index.php?route=information/contact
- 「We serve over 500 resellers all over Cyprus … 2000+ Clients … 10000+ Projects Completed」 — https://art2soft.eu/

**判位备档**(参考位，评级仍 B · 不出信）
- 参考 P1: `STC-424XGGPM-280W` — WISP+VoIP 专营分销的话机/站点 PoE 随单位
- 第一问: 你们的 IP 话机/WISP 项目里,PoE 管理型交换现随哪家?
- 标签: 塞浦路斯|Nicosia|WISP+VoIP专营|具名Theodoulos

**备养出信稿（未触发，供后续用户启用参考）**
```text
Hi Theodoulos,

From Ubiquiti WISP distribution in 2006 to a full VoIP line with IP PBX and SIP phones - your resellers deploy phones and radios, and both settle onto the same PoE switch. That makes the PoE line behind your catalog a quiet volume driver.

We build a 24-port PoE+ managed switch (280W, L2-lite) with full English documentation. Reference: $180 USD EXW (2026-09-29) - the documented value-tier PoE unit for your reseller-facing catalog, white-label friendly.

One question: for your IP telephony and wireless deployments, which managed PoE switch rides in the same order today?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

**待补证清单**
1. 话机谱 PoE 交换现供
2. 全谱分销与白标接受度

**跟进建议（守档节奏）**
- D+3 话机谱 PoE 页
- D+14 thomas.thoma@art2soft.com 开口(抄送具名 Theodoulos 角度)
- D+30 果归守档

<!-- BDEEP:B类深挖_2026-09-29_R57-BC_第11波 -->

## 2026-10-06 R63 B升A 第1波

**决策**：B → A(原号 B-105 → 新号 A-572,原 B 编号释放回池)

**评级依据**：六牌官方分销(UBNT/MikroTik/Cambium/RF Elements/Fanvil/Yeastar),Cyprus 官方认证经销名录

**核验路径**：2026-10-06 web_search 核实（官方名录/官网交换机在售/创始人背景），达 R50 复筛达标口径（站点在线+交换机品类+网络专营+决策链短）。

**状态**：未触达,纳入 A 池，按 A 池节奏推进首触。

## 2026-10-07 R64 KP 猎捕(第 1 波)

**方法**:web_search 公开源(领英摘要/工商登记/contactout/RocketReach)定人 → 排列组合猜邮箱 → 域 MX 核验。SMTP 用户级沙箱不可验,**guessed 一律不进群发**,仅供手动/小批量试探;查不出写待定。
**域 MX**:{"art2soft.com": ["art2soft-com.mail.protection.outlook.com"], "cy-wireless.com": ["mail.cy-wireless.com"]}
- **Thomas Thoma** — Managing Director(2006 至今)（源:https://rocketreach.co/thomas-thoma-email_51793668）
  - `thomas@art2soft.com`(first@(art2soft.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `thomas.thoma@art2soft.com`(first.last@(art2soft.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `t.thoma@art2soft.com`(f.last@(art2soft.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `thomasthoma@art2soft.com`(firstlast@(art2soft.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `tthoma@art2soft.com`(flast@(art2soft.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `thoma@art2soft.com`(last@(art2soft.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `thomas@cy-wireless.com`(first@(cy-wireless.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `thomas.thoma@cy-wireless.com`(first.last@(cy-wireless.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `t.thoma@cy-wireless.com`(f.last@(cy-wireless.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `thomasthoma@cy-wireless.com`(firstlast@(cy-wireless.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `tthoma@cy-wireless.com`(flast@(cy-wireless.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))
  - `thoma@cy-wireless.com`(last@(cy-wireless.com);guessed-leads-only(域 MX 存活;SMTP 用户级未验;不进群发))

**备注**:MikroTik 官方 reseller 名录曾列 thomas.thoma@art2soft.com

## 2026-10-07 R64 首触定制稿(KP 点名)

**对象**:Thomas Thoma(Managing Director)
**通道**:thomas.thoma@art2soft.com(名录源)/ info@cy-wireless.com(官网)

**主题**:PoE switching for your WISP/ISP channel in Cyprus

```text
Hi Thomas,

Six vendor lines through Nicosia - MikroTik, Ubiquiti, Cambium, RF elements, Fanvil, Yeastar - suggests your installers live on PoE budgets.

We manufacture a 24-port Gigabit PoE+ switch (280W, 4x10G uplinks, ERPS<20ms, watchdog that cold-reboots frozen APs) under neutral packing. Reference: $180 USD EXW (2026-10-07, valid 15 days).

One question: which PoE switch do your Cyprus/WISP installers default to at 24 ports - and would a documented evaluation unit get a fair test at ART2SOFT?

Best regards,
Saga Telecom - PoE switch OEM/ODM (neutral packing available)
```

> 发送前检查:①不出现「Made in China」;②落款换用户本人;③guessed 邮箱先单发试探,退信即换通道;④问 API 话题先反问架构(纪律)。
