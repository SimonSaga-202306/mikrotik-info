# Ihor Hreskiv / mtik.pl

> **评级 A**　|　波兰 · Kraków　|　档案编号 `A-048`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-048
rating: A
country: 波兰
biz_org: 公司/工作室（有官网）
business_model: 培训交付
decision_speed: moderate
price_sensitivity: medium
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: true, voice: false, oem: false, hotel: false, training: true}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：公司/工作室（有官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：有明确交换/供电需求（交换专长），且有具体人直联
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — mtik.pl 全真硬件教室：MTCSWE 工位交换教具期期消耗（$99 锚点一致）；师者红线；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Ihor Hreskiv / mtik.pl（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 波兰 / Kraków | 事实 |
| 网站 | mtik.pl | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Ihor Hreskiv | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 10 证全拿 | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 10 证全拿）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、L2+ 交换管理（VLAN/ERPS/QinQ）、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：biuro@mtik.pl
  - 状态：既有/公开
- **电话**：+48 512 438 083
- **原始联系字段**：+48 512 438 083 / biuro@mtik.pl
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- **Ihor Hreskiv**（本人直达；角色=业主/顾问本人，依据名录）

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 PoE++（实验台备用与学员自费）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他每个班最多 8 人、人手一机：24 口 PoE++ 做助教备机 + 学员课后自购的推荐位，给他一张和 CRS328 的教学对照页。
- **要问的问题**：下一期 MTCSWE 班实验台的交换机缺几台？
- **随附证明**：英文教学对照页 + 单台价格表。

### 第 2 次跟进 · 工业非管理 PoE（与课程场景对齐）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：课程中工业组网的演示机：宽温、DIN、免配置——放进他的极客实验角，上课时拿来讲电源与环境容忍度。
- **要问的问题**：课程里工业/室外话题用不用得着演示机？
- **随附证明**：一台样机 + DIN 安装图 + 宽温报告。

### 第 3 次跟进 · 管理型 + 联合课程案例

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：把管理方案（VLAN/ERPS/10G）写成他 MTCRE/MTCSWE 课的补充案例：他获得内容，我们获得工程圈入口；学员=潜在客户。
- **要问的问题**：闭门课里要不要加一个 ERPS/VLAN 案例实验？
- **随附证明**：VLAN/ERPS 收敛实测 + 教学案例页 + 英文测试报告。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：Kraków 的 MikroTik 认证培训及个人品牌（mtik.pl / Ihor Hreskiv），波兰最有排期的讲师之一；交换课程成熟。
- **产品线与在售品牌**：不卖硬件，卖课程；但教学真机是常耗品——315+ 场课背后的设备池长期更新。
- **目标行业与场景**：ISP/WISP 工程师、企业网络团队、定制闭门课；英/波/乌三语教学。
- **团队与规模**：个人品牌+小助教团队；Kraków Starowiślna 20/3 培训室。
- **决策链与对接人**：Ihor Hreskiv 本人（+48 512 438 083 / biuro@mtik.pl）。
- **技术与认证**：MikroTik 全证 + Trainer（来源：CSV 既有记录+官网自述）。
- **采购与供应链信号**：每个班 6–8 台交换机实验台的重复采购——稳定小批量；学员讲台上的设备=长期曝光。
- **近期动态与线索**：2026-10 起 MTCNA / MTCIPv6E / MTCRE 连排，秋冬课程密度高；MTCINE 也能排——流量好。
- **与我方契合点**：交换课正是我们的强项：24 口 PoE++/管理型的真实参数进入他的讲义与实验台——学员=渠道。
- **风险与注意**：他做 MikroTik 生态培训，不要把设备叫作「替代 MikroTik」——讲「配套硬件/教学备机」为正。

### R54 原文证据摘录（全部保留）

- **【业务定位】**Kraków 的 MikroTik 认证培训点：到 2026-09-28 累计 315+ 场培训、1675+ 名学员。
  > 315+ szkoleń · 1675+ kursantów
  > 来源：https://mtik.pl/
- **【采购与供应链信号】**培训只用真机（不用模拟器/虚拟机），每个学员一台真机实验台——交换机是他的常耗硬件。
  > Każdy uczestnik ma do dyspozycji własne stanowisko laboratoryjne z fizycznym sprzętem MikroTik (routery, switche, access pointy). Nie używamy symulatorów ani maszyn wirtualnych
  > 来源：https://mtik.pl/
- **【技术与认证】**课程体系含 MTCSWE 3 天课的完整交换专题，学员提到的含交换课程评价。
  > [MTCSWE3 dni](https://mtik.pl/courses/mtcswe)… Brewes GmbH, MTCSWE — Polecam wszystkim zainteresowanym tematyką mikrotik szkolenia w Krakowie
  > 来源：https://mtik.pl/
- **【目标行业与场景】**面向厂商/企业提供闭门课程，可上门到客户办公室。
  > Szkolenia zamknięte dla firm — Program dopasowany do sieci klienta, w siedzibie firmy lub w Krakowie.
  > 来源：https://mtik.pl/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第5批.json`；价格均为 EXW 快照。

- **①背景再核**：克拉科夫全真硬件培训教室（8 人小班）；十证 Trainer；315+ 期 1675+ 学员
- **②芯片/型号**：教具全真 MikroTik（路由/交换/AP）
- **③KP 深挖**：Hreskiv biuro@ 直达
- **④Saga 对标**：MTCSWE 工位交换教具——STC-28DGGPM（期期消耗）
- **⑤在乎与偏好**：教具要真硬件、可搬动（内训）

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“315+ szkoleń / 1675+ kursantów / Stacjonarnie, na realnym sprzęcie, w grupach do 8 osób…Routery, switche, AP — fizyczne, nie wirtualne”
  > “315+ szkoleń / 1675+ kursantów / Stacjonarnie, na realnym sprzęcie, w grupach do 8 osób…Routery, switche, AP — fizyczne, nie wirtualne”
  > 来源：https://mtik.pl/
- **【近期动态】**“MTCNA 4-6 października 2026 1400 PLN / MTCIPv6E 11-12 / MTCRE 18-19 1900 PLN Kraków ul. Starowiślna 20/3”
  > “MTCNA 4-6 października 2026 1400 PLN / MTCIPv6E 11-12 / MTCRE 18-19 1900 PLN Kraków ul. Starowiślna 20/3”
  > 来源：https://mtik.pl/szkolenia
- **【联系方式】**biuro@mtik.pl +48 512 438 083；MX=smtp.google.com（MX/DNS 级核验：域存活=邮件可投递到域）
  > biuro@mtik.pl +48 512 438 083；MX=smtp.google.com（MX/DNS 级核验：域存活=邮件可投递到域）
  > 来源：https://mtik.pl/kontakt

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | mtik.pl 全真硬件教室：MTCSWE 工位交换教具期期消耗（$99 锚点一致）；师者红线 |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：全真教室口碑
- **W**：个人带宽
- **O**：MTCSWE 耗材
- **T**：官配

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

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Ihor,

I found mtik.pl - a real-hardware classroom in Kraków, 315+ courses, 1.675+ students, everything physical, no simulators. That is the right religion.

We build a compact 8-port managed PoE switch that fits a per-student switching bench for MTCSWE days (STP/VLAN/L2 labs, 802.3af/at). Reference: $99 USD EXW per unit, trainer pricing for bench sets.

One question: which switch do you put on each student bench for the switching labs today?

If useful, I can send a bench unit plus a suggested lab topology. If not a fit, one line and I close the loop.

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
