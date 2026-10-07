# Ronitek

> **评级 A**　|　以色列　|　档案编号 `A-570`　|　优先级 ★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-570
rating: A
country: 以色列
biz_org: 公司/工作室（有官网）
business_model: MikroTik 官方分销
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

- **是谁**：公司/工作室（有官网）；MikroTik 官方分销
- **商业模式**：MikroTik 官方分销
- **为什么值得跟**：通用分销商信号，无差异化切入点，慢慢跟 【2026-10-06 R63 B升A批复第1波】原 B-037；理由:MikroTik 交换机专营页+CCR/CRS 在售，Trunk/LACP/VLAN企业客户
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — 【2026-10-06 R63 B升A】MikroTik 官方分销画像；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which 24-port managed PoE+ model currently carries your enterprise/WISP builds?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Ronitek（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 以色列 | 事实 |
| 网站 | ronitek.co.il | 事实 |
| 类型 | MikroTik 官方分销 | 事实（CSV 名录口径） |
| 关键人 | Ronitek | 事实 |
| 反向信号（资质/品牌） | MikroTik（Reseller） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | MikroTik 官方分销 | 【推断】 |
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

- **邮箱**：Info@ronitek.co.il
  - 状态：official-company
- **电话**：+972 77 249 5881 
- **原始联系字段**：Info@ronitek.co.il
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Ronitek**（本人直达；角色=业主/顾问本人，依据名录）

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
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 【2026-10-06 R63 B升A】MikroTik 官方分销画像 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：通用分销商信号，无差异化切入点，慢慢跟 【2026-10-06 R63 B升A批复第1波】原 B-037；理由:MikroTik 交换机专营页+CCR/CRS 在售，Trunk/LACP/VLAN企业客户
- **W**：公开信息有限
- **O**：P1 场景切入（【2026-10-06 R63 B升A】MikroTik 官方分销画像）
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
Hi Ronitek,

I came across Ronitek - MikroTik 官方分销.

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
- 【事实】Ronitek Distribution Ltd(Tel Aviv Ben Tzvi 84;ח.פ 516918844):**以色列网络设备中坚分销(希伯来语电商+B2B)**——Ubiquiti/MikroTik/TP-Link/Teltonika/Huawei/Cisco/Supermicro/RF Elements/Synology/Yealink/HPE Aruba/Juniper/NVIDIA 全谱;官方进口商口径;在架 MikroTik 深(RDS2216/CCR/CRS,SFP 类目 27 项);WhatsApp 商务线
- 【推断】同 etree/Ronitek 画像:中东市场电商型全谱分销;Teltonika+Ubiquiti 均在架=PoE 需求谱明确;希伯来语本地服务是其护城河
- 【假设】开口角度=「以色列电商分销的 24 口 280W 管理型 PoE value 档」:STC-424 以其 CRS/UniFi 之间的 value 空档入架

**SWOT 速描**
- **S**: 全谱+官方进口+本地希语服务
- **W**: Ubiquiti 走量压
- **O**: 24 口 280W 管理型 value 空档
- **T**: 地缘物流与合规

**证据（quote → 来源）**
- 「Ubiquiti, MikroTik, TP-Link, Teltonika, Huawei, Cisco, Supermicro, RF Elements, Synology, Yealink…HPE Aruba, Juniper, NETGEAR, NVIDIA」 — https://www.ronitek.co.il
- 「MikroTik RDS2216…Switches [27]…Routers and Firewalls [17]…SFP optical modules [18]」 — https://www.ronitek.co.il/products/cat/Mikrotik

**判位备档**(参考位，评级仍 B · 不出信）
- 参考 P1: `STC-424XGGPM-280W` — 以色列中坚分销的 24 口 280W 管理型 PoE value 架位
- 第一问: 你们架上 24 口管理型 PoE+ 现供哪款?UniFi/CRS 之间 value 档有位吗?
- 标签: 以色列|特拉维夫|全谱分销|MikroTik深架

**备养出信稿（未触发，供后续用户启用参考）**
```text
Hi Ronitek team,

A full-spectrum importer in Tel Aviv stocking everything from RDS2216 down to hAP, with UniFi, Teltonika and Yealink on the same shelf - your catalog knows where the PoE gaps are.

We build a 24-port PoE+ managed switch (280W, L2-lite) with full English documentation. Reference: $180 USD EXW (2026-09-29) - the documented value tier between your UniFi and CRS shelves, white-label friendly.

One question: on your shelves today, which 24-port managed PoE switch holds the value tier - and would a documented unit earn a listing test?

If useful, I can send one unit with the complete test pack (note: we can align on Israeli import certification needs). If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

**待补证清单**
1. 其安装商/ISP 客层 PoE 随单结构
2. 新品牌入架的认证门槛(以色列进口认证)

**跟进建议（守档节奏）**
- D+3 价档对照页
- D+14 info@ronitek.co.il 开口
- D+30 果归守档

<!-- BDEEP:B类深挖_2026-09-29_R57-BC_第9波 -->

## 2026-10-06 R63 B升A 第1波

**决策**：B → A(原号 B-037 → 新号 A-570,原 B 编号释放回池)

**评级依据**：官网 MikroTik 交换机专营页+CCR/CRS/变速箱在售,专为思科替代定位 B2B/集成商

**核验路径**：2026-10-06 web_search 核实（官方名录/官网交换机在售/创始人背景），达 R50 复筛达标口径（站点在线+交换机品类+网络专营+决策链短）。

**状态**：未触达,纳入 A 池，按 A 池节奏推进首触。
