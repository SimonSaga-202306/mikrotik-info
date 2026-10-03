# Juan Manuel Díaz Gómez

> **评级 A**　|　美国 · Tampa, FL　|　档案编号 `A-068`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-068
rating: A
country: 美国
biz_org: 个体顾问（无官网）
business_model: 培训交付
decision_speed: fast
price_sensitivity: high
volume_potential: 2  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: true}
p1: STC-28DGGPM
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；培训交付
- **商业模式**：培训交付
- **为什么值得跟**：有明确交换/供电需求（PoE/监控/门禁），且有具体人直联
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — Díaz Gómez 十证个人、足迹薄：WhatsApp 破冰薄档如实（$99 锚点一致）；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Which switch do you currently put on the bench for the VLAN/PoE lab demos?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Juan Manuel Díaz Gómez（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Tampa, FL | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik 认证顾问 10 证全拿 | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 培训交付 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Juan Manuel Díaz Gómez（美国籍列册，哥伦比亚手机）：sutik.oficial@gmail.com；十证全拿 MikroTik 顾问；公开站未查得（2026-09-28 搜索与抓取均无命中）
- 【推断】个人顾问/足迹薄；gmail+WhatsApp 联络先行
- 【假设】十证全=技术底子深；破冰后特性对话

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：MikroTik 认证顾问 10 证全拿）

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、教学教具
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 教学教具：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sutik.oficial@gmail.com
  - 状态：既有/公开
- **电话**：+57 315 649 0735
- **原始联系字段**：+57 315 649 0735 / sutik.oficial@gmail.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（城市监控项目）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：他做 CCTV ciudadano：几十路摄像头整网 PoE++ 一次到位，4×10G 上行回监控中心——按「每路口/每段一台」测算。
- **要问的问题**：CCTV 项目里接入交换现在用哪家的、每路功率预算怎么算？
- **随附证明**：PoE 预算测算表 + 规格对照（英/西语）。

### 第 2 次跟进 · 工业级非管理 PoE（WISP 塔站）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：WISP 塔站/高山点位：宽温宽压 DIN 免配置，配 SFP 上行回传——他建网时的塔上标准件。
- **要问的问题**：塔站交换与供电现在怎么配？雷击/高温故障多不多？
- **随附证明**：宽温报告 + DIN 图 + 塔站备件包价。

### 第 3 次跟进 · 管理型 PoE + 课程实验台

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：讲师收尾：管理型进他 MTCNA/MTCTCE 课的实验台（VLAN/QoS 实测），学员即未来客户。
- **要问的问题**：下一期班实验台缺不缺可做 VLAN/ERPS 实测的交换机？
- **随附证明**：实验机成本价 + 课程案例页 + 配置模板。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：哥伦比亚麦德林的 MikroTik 认证讲师+顾问（Wiretel SAS），通信名片登记在美国 Tampa——跨境服务美国拉美裔/拉美 WISP 市场，英西双语。
- **产品线与在售品牌**：课程（MTCNA/MTCTCE 等认证班）+ WISP 整网实施陪跑 + CCTV 城市监控项目 + 24×7 监控支持。
- **目标行业与场景**：拉美 WISP 从零建网、城市 CCTV 监控网、企业 LAN/WLAN；CCTV ciudadano=几十上百路摄像头的 PoE 大现场。
- **团队与规模**：讲师本人+Wiretel SAS 小团队；MUM 多国演讲者，拉美 MikroTik 圈活跃面孔。
- **决策链与对接人**：Juan Manuel 本人；+57 315 649 0735 / training@jmikrotik.co（官网）；CSV 另记 sutik.oficial@gmail.com。
- **技术与认证**：10 证全拿+认证讲师，18+ 年经验（CSV 名录记录）；MUM 演讲资料可公开核验其讲师资历。
- **采购与供应链信号**：WISP 实施=整批设备选型采购；CCTV 项目=PoE 交换机大户；培训实验台=持续教具需求。
- **近期动态与线索**：培训站 jmikrotik.co 本轮直连失败（搜索快照仍有效）——线上资产波动，触达走手机/Gmail。
- **与我方契合点**：CCTV ciudadano=24 口 PoE++ 刚需；WISP 塔站=工业件；讲师课=实验台硬件；西语资料我们也能配。
- **风险与注意**：跨境身份（CSV=Tampa/官网=Medellín）——报价与交付按哥伦比亚/美国两种路径都备好；关税与物流先讲清。

### R54 原文证据摘录（全部保留）

- **【业务定位】**培训官网（本轮直接抓取失败，内容经搜索引擎快照核实）：电信工程师，10+ 年 MikroTik，认证顾问+讲师，Wiretel SAS CEO。
  > Ingeniero de Telecomunicaciones Universidad Santo Tomás sede Medellín, gran experiencia trabajando con equipos de la marca MikroTik por más de 10 años. Consultor y entrenador Certificado MikroTik. — Juan Manuel Díaz Gómez CEO Wiretel SAS
  > 来源：https://jmikrotik.co/
- **【目标行业与场景】**官网服务范围：LAN、无线网、WISP 实施与「CCTV 市民监控」，WISP 项目从选型到 24×7 驻场/远程支持全陪跑。
  > redes LAN, redes inalámbricas, WISP´s, CCTV ciudadano — Implementación de WISP´S … monitoreo de red … soporte en sitio y remoto 24X7
  > 来源：https://jmikrotik.co/
- **【决策链与对接人】**官网触点：麦德林办公地址、手机与培训邮箱；CSV 记录通信地址在美国 Tampa（英西双语，拉美方向）。
  > +57 315 649 0735 · training@jmikrotik.co · Calle 32f # 66C - 67 Medellín - Antioquia · @jmmikrotik2
  > 来源：https://jmikrotik.co/
- **【技术与认证】**MUM 洪都拉斯 2020 演讲者：2008 年起用 MikroTik，当时已持 MTCNA/MTCTCE（与 CSV「10 证全拿+认证讲师」记录为同一人）。
  > Experiencia con Mikrotik desde el año 2008 · Certificaciones obtenidas: MTCNA-MTCTCE · Juan Manuel Diaz Gómez, Ingeniero de Telecomunicaciones
  > 来源：https://mum.mikrotik.com/presentations/HN20/presentation_7422_1580111784.pdf

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第7批.json`；价格均为 EXW 快照。

- **①背景再核**：十证个人；无站
- **②芯片/型号**：未公开
- **③KP 深挖**：本人 gmail
- **④Saga 对标**：破冰后定
- **⑤在乎与偏好**：未知

### R55 证据摘录（全部保留 · 含数量）

- **【技术与认证】**CSV：Juan Manuel Díaz Gómez 十证全
  > CSV：Juan Manuel Díaz Gómez 十证全
  > 来源：https://mikrotik.com/consultants

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：个人十证顾问（足迹薄）
- **产品线与在售品牌**：未公开
- **目标行业与场景**：未公开
- **团队与规模**：个人
- **决策链与对接人**：Díaz Gómez 本人
- **技术与认证**：十证全
- **采购与供应链信号**：未知
- **近期动态与线索**：无
- **与我方契合点**：破冰后定
- **风险与注意**：足迹薄如实

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Díaz Gómez 十证个人、足迹薄：WhatsApp 破冰薄档如实（$99 锚点一致） |
| 备选2 | STC-424XGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：十证
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

- **深挖专属待问（R56）**：
  - [ ] 市场口径
  - [ ] 项目方向
  - [ ] 评测意愿

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Hi Juan Manuel,

A ten-certification MikroTik stack is rare air - I found you on the official consultant list.

We build managed PoE switches that aim at exactly the layer MikroTik consultants replace most often (Voice VLAN, ERPS, watchdog). Short and honest note since I could not find public material about your practice.

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

---

### R60 客户运营判定(2026-09-29 · 仅 A 类 · 改内容不改顺序)

- **KP 领英直达**:[Díaz Gómez · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=D%C3%ADaz%20G%C3%B3mez)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 高(Covered List+SECURE Act+§301 关税;采购方警惕中国标签,话术锚 Marvell(美企)+FCC);战术: 首触点不亮中国原产,强调 Marvell(美企)芯片+FCC/CE 合规+产地声明随报价备询;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
