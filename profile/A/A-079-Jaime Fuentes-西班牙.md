# Jaime Fuentes

> **评级 A**　|　西班牙 · Alcalá la Real　|　档案编号 `A-079`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-079
rating: A
country: 西班牙
biz_org: 个体顾问（无官网）
business_model: 培训交付
decision_speed: fast
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: true, l2plus: false, voice: false, oem: false, hotel: false, training: true}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：有明确交换/供电需求（光纤接入），且有具体人直联
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — Fuentes 西三证个人：WhatsApp 破冰薄档如实（$99 锚点一致）；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Jaime Fuentes（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 西班牙 / Alcalá la Real | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、万兆上行/骨干、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - 万兆上行/骨干：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：jaimefuentesit@gmail.com
  - 状态：既有/公开
- **电话**：+34 615 800 589
- **原始联系字段**：+34 615 800 589 / jaimefuentesit@gmail.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（ISP 接入节点/村网点）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：顺着他的乡区铺网：接入节点 24 口 PoE++ 带 AP/监控/村网 CPE，4×10G 上行回镇机房——给总工看单端口成本。
- **要问的问题**：村网节点的接入交换现在用什么型号？交期呢？
- **随附证明**：单端口成本测算 + 规格对照（西/英）。

### 第 2 次跟进 · 工业级非管理 PoE（乡区塔站/室外箱）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：Sierra Sur 的塔站与室外箱：宽温宽压 DIN 免配置+SFP 上行，备件包按镇配。
- **要问的问题**：室外节点夏天故障率多少？现在谁供？
- **随附证明**：宽温报告 + 节点备件包价 + DIN 图。

### 第 3 次跟进 · 管理型 PoE（接入层模板+课程案例）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：总工+讲师双线：接入层 VLAN/ERPS 模板进他的运维标准；课堂用真机做 L2/L3 演示=学员（本地 ISP 工程师）跟着买。
- **要问的问题**：下一期课在什么时候？接入段演示用什么设备？
- **随附证明**：VLAN/ERPS 模板 + 实验机成本价 + 课程素材。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：安达卢西亚乡区 ISP 老兵+MikroTik 讲师：现任 Getecom 总工程师，掌运营商级网络；业余上 MikroTik 认证课。
- **产品线与在售品牌**：本职=ISP 网络工程（FTTH/乡区无线）；副业=认证培训；Hillstone HCSA 说明防火墙采购也过他手。
- **目标行业与场景**：西班牙乡村 FTTH/WISP 铺网（Sierra Sur de Jaén 类）、ISP 核心与接入运维、学员=本地 ISP 工程师。
- **团队与规模**：Getecom 公司内部编制+个人讲师身份双线。
- **决策链与对接人**：Jaime Fuentes 本人（+34 615 800 589 / jaimefuentesit@gmail.com）；500+ LinkedIn 联系人，社群活跃。
- **技术与认证**：MTCNA+MTCRE+MTCTCE+MikroTik 讲师（2019 起）；RIPE/HCSA 复证到期时间窗口清楚。
- **采购与供应链信号**：ISP 总工=接入/汇聚设备选型拍板人；乡村铺网 PoE 与室外件需求持续；课程实验台另有需求。
- **近期动态与线索**：RIPE 证 2026-01、HCSA 2026-05 到期=复证/培训活跃窗口；刚稳定在新东家（2023-11 起）第三年，建设期。
- **与我方契合点**：乡村 WISP/FTTH 节点=工业 PoE 与万兆上行；总工选型权+讲师传播权一人双——打透一个顶两个。
- **风险与注意**：他是 Hillstone 持证防火墙用户：安全域别硬碰；我们聚焦交换/接入层，避开防火墙话题。

### R54 原文证据摘录（全部保留）

- **【技术与认证】**LinkedIn 公开档案（第三方页面）：MikroTik 讲师证（2019-02 发）；另持 Hillstone HCSA（2024-05 发，2026-05 到期）与 RIPE 数据库专家证。
  > MikroTik Trainer · MikroTik · Issued Feb 2019 · HCSA — Hillstone Networks — Issued May 2024 Expires May 2026 · RIPE Database Associate — RIPE NCC — Issued Jan 2023 Expires Jan 2026
  > 来源：https://es.linkedin.com/in/jaime-fuentes-perez
- **【业务定位】**同页现任职务：Getecom 总工程师（2023-11 至今）；曾任 ISPGestion Provider 技术总监（2019–2023）——长期在 ISP 体系内。
  > CSE | MikroTik Trainer · Director técnico ISPGestion Provider Mar 2019 - Oct 2023 · Getecom Nov 2023 - now — Chief system engineer · Location: Alcalá la Real
  > 来源：https://es.linkedin.com/in/jaime-fuentes-perez
- **【目标行业与场景】**履历详情页（聚合快照）：早年在本地运营商用 MikroTik 给 Sierra Sur de Jaén 多个村镇供网，GNU/Linux 服务器+Asterisk 话务+Python/Shell 自动化。
  > Administrar la red Mikrotik mediante la cual se suministraba internet a varias poblaciones de la comarca de la Sierra Sur de Jaén… centralitas basadas en asterix… shell script y python
  > 来源：https://deepenrich.com/profile/0c85/jaime-fuentes-p%C3%A9rez-0011u3b7c
- **【决策链与对接人】**CSV 既有记录：手机直联+个人 Gmail（CSV 记录）。
  > +34 615 800 589 / jaimefuentesit@gmail.com（CSV 入口列）
  > 来源：https://mikrotik.com/consultants

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第8批.json`；价格均为 EXW 快照。

- **①背景再核**：三证个人、无站
- **②芯片/型号**：未知
- **③KP 深挖**：本人 gmail
- **④Saga 对标**：破冰后定
- **⑤在乎与偏好**：未知

### R55 证据摘录（全部保留 · 含数量）

- **【技术与认证】**CSV：Jaime Fuentes MTCNA+MTCRE+MTCTCE（西班牙）
  > CSV：Jaime Fuentes MTCNA+MTCRE+MTCTCE（西班牙）
  > 来源：https://mikrotik.com/consultants

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Fuentes 西三证个人：WhatsApp 破冰薄档如实（$99 锚点一致） |
| 备选2 | STC-424DGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $165 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：证在册
- **W**：薄
- **O**：未探
- **T**：不确定

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 一人/个体=单点与节奏风险
- 教师红线：不打学员名单、不经培训语境推销

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

**主题**：PoE switching for your projects

```text
Hi Jaime,

I found you on the MikroTik consultant list (MTCNA/MTCRE/MTCTCE).

We build managed PoE switches with the L2+ table consultants look for in access layers they can trust (Voice VLAN, ERPS, watchdog).

One question: in your projects, is the switching layer ever open for alternatives?

If yes, I can send the feature table and an evaluation unit. If not, one line and I close the loop.

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
