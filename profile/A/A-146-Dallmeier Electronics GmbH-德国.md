# Dallmeier Electronics GmbH

> **评级 A**　|　德国 · Regensburg　|　档案编号 `A-146`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-146
rating: A
country: 德国
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
- **P1（首触唯一主推）**：STC-28DGGPM（8口 PoE 接入盒） — Dallmeier 视频监控制造商同业：厂家非客户建档不出信；$99 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：How many PoE ports does a typical site of yours need today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Dallmeier Electronics GmbH（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Regensburg | 事实 |
| 网站 | https://www.dallmeier.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Dallmeier Electronics（德国雷根斯堡，1984 年创）：**视频监控制造商**——Panomera 多焦传感器专利/Domera 摄像系/SeMSy VMS/Hemisphere；机场/赌场/体育场/关键基建方案；**“Video Technology Made in Germany”**，全球 installer/integrator 渠道
- 【推断】制造商同业（视频安防厂牌）——是设备厂家不是采购客户；按其渠道结构，其合作伙伴（installer/integrator）才是接入交换的买家
- 【假设】同业建档不出信（厂家非客户纪律，同 Round15 台湾信号源逻辑）；CSV 以 Allied 信号录入，如实标注同业身份

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@dallmeier.com
  - 状态：既有/公开
- **电话**：—
- 来源等级：official（R41–R48 联系方式台账口径）
- **原始联系字段**：info@dallmeier.com [Publicly listed; delivery not tested]; https://www.dallmeier.com
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8口 PoE 接入盒）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（监控大项目接入层互补 BOM）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：定位说清：不是替代谁的摄像，是补交钥匙项目里的网络接入层——24 口 PoE++（4×10G）规格+全套文档包。
- **要问的问题**：交钥匙项目里的接入层 BOM 现在有固定件吗？
- **随附证明**：规格表 + CE/MTBF 文档包 + FAT 对接说明（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（周界/场外点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：体育场周界与场外杆点：宽温 DIN PoE 扛户外，SFP 长距上行配光纤回传。
- **要问的问题**：场外杆点的供电与回传怎么配？
- **随附证明**：宽温报告 + SFP 上行方案 + DIN 图（德文）。

### 第 3 次跟进 · 管理型 PoE（多焦面项目分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：大型视频网的分段与环网模板：VLAN/ERPS+组播设计建议，进他的「基础设施咨询」参考库。
- **要问的问题**：大视频网的分段模板要不要进你们的规划库？
- **随附证明**：VLAN/ERPS/组播模板 + 收敛实测 + 样机（德文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第8批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：雷根斯堡视频安防大厂 Dallmeier 的交付臂：大项目设计-实施-支持一体，Allied Resell（CSV 记录）。⚠️ 集团是制造商非小集成商（CSV 提醒不故降级）。
- **产品线与在售品牌**：自有摄像/录像平台+Panomera®+3D 规划+交钥匙项目管理；网络/电气为辅材 BOM。
- **目标行业与场景**：体育场/赛事、机场交通、城市安全、工业厂区的大型视频项目；24/7/365 托管与现场保障。
- **团队与规模**：大厂集团+三地交付点具名经理。
- **决策链与对接人**：info@dallmeier.com（CSV 9-27：总部公共邮箱；具名区域经理可经其转接）。
- **技术与认证**：Allied Resell（CSV 记录）；DIN VDE 0100 安装规范（官网）。
- **采购与供应链信号**：大项目 BOM 制：网络接入层作为「基础设施咨询/交钥匙」的一部分招标——他要规格与文档过硬、FAT 流程能对接的供应商。
- **近期动态与线索**：Panomera®+大事件保障（足球赛事）常态。
- **与我方契合点**：监控大项目的 PoE 接入层是互补不抢位（他不是交换厂）：大功率 PoE++/10G 上行正是大场面多焦面海量像素的承载段。
- **风险与注意**：制造商级客户标准高：完整文档包（CE/声明/MTBF）+FAT 对接说明一次给足；走 Region 经理转接的路径比直投 info@ 有效。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网：视频安防名厂 Dallmeier 的子公司 Dallmeier Systems——「顾问、安装商、集成商与系统屋」的项目交付臂。
  > Das Dallmeier Tochterunternehmen „Dallmeier Systems“ ist der regionale Ansprechpartner für die Planung, Umsetzung und Support von Videosicherheitsprojekten. Wir unterstützen unsere Kunden als Berater, Errichter, Integrator und Systemhaus.
  > 来源：https://www.dallmeier.com/de/ueber-uns/dallmeier-systems
- **【技术与认证】**专利 Panomera® 多焦面技术+3D 规划「数字孪生」+工厂验收 FAT 流程——大型项目交付体系完整。
  > weitreichende Kompetenzen mit der patentierten Panomera® Multifocal-Technologie ‖ Erstellung eines „Digitalen Zwillings“ der Kundenumgebung ‖ Vollumfängliche Nutzung des Dallmeier Factory Acceptance Test (FAT) Verfahrens
  > 来源：https://www.dallmeier.com/de/ueber-uns/dallmeier-systems
- **【目标行业与场景】**交钥匙大包：总承包含「入侵报警/门禁等子装修项的项目管理」+基础设施咨询（电气/网络/安装/网络安全）。
  > Schlüsselfertige Anlage mit Projektsteuerung sämtlicher Subgewerke (z. B. Einbruchmeldeanlage, Zutrittskontrolle) ‖ Detaillierte Infrastrukturberatung (Elektro, Netzwerk, Installationsbedingungen, Cybersecurity u.a.)
  > 来源：https://www.dallmeier.com/de/ueber-uns/dallmeier-systems
- **【决策链与对接人】**区域触点具名三处：汉堡 André Haack、盖尔森基兴 Stephan Leberecht、慕尼黑 Roland Feil；支持上限 24/7/365（含赛事现场保障）。
  > Dallmeier Systems HAMBURG — Kontakt: André Haack · GELSENKIRCHEN — Stephan Leberecht · MÜNCHEN（Aschheim）— Roland Feil ‖ Support nach Kundenanforderung bis zu 24/7/365 · Vor-Ort Einsatzbegleitung（z. B. bei Großereignissen, Fußballspielen）
  > 来源：https://www.dallmeier.com/de/ueber-uns/dallmeier-systems

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-09-28_R56_第15批.json`；价格均为 EXW 快照。

- **①背景再核**：视频监控制造商（Made in Germany）同业
- **②芯片/型号**：不适用（同业）
- **③KP 深挖**：建档不出信
- **④Saga 对标**：不适用
- **⑤在乎与偏好**：—

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**“Video Technology Made in Germany…A large network of installers and integrators use Dallmeier products”
  > “Video Technology Made in Germany…A large network of installers and integrators use Dallmeier products”
  > 来源：https://www.dallmeier.com/

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：德国视频监控制造商（同业）
- **产品线与在售品牌**：Panomera/Domera/SeMSy
- **目标行业与场景**：机场/赌场/体育场/KRITIS
- **团队与规模**：中型制造商
- **决策链与对接人**：—
- **技术与认证**：Made in Germany
- **采购与供应链信号**：—（厂家）
- **近期动态与线索**：St. Louis 机场案例
- **与我方契合点**：无直接（同业）；其 installer 渠道为后续独立触点池
- **风险与注意**：同业身份

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-28DGGPM（8口 PoE 接入盒） | 主场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Dallmeier 视频监控制造商同业：厂家非客户建档不出信 |
| 备选2 | STC-424XGGPM-280W（24口 PoE + 4×10G） | 升级/延展场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：8口 GE(7)+SFP，PoE af/at 240W，DC 随附电源，L2+ 全特性（VLAN/ERPS<20ms/QinQ/Private VLAN/sFlow），PoE 看门狗自动冷重启
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：厂牌
- **W**：非客户
- **O**：生态
- **T**：不评

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

- **深挖专属待问（R56）**：
  - [ ] —

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
（不出信——制造商同业建档。动作：仅建档与 MX 核验。判定依据：官网自述视频技术制造商身份（Panomera/SeMSy）；厂家不是采购客户，其 installer/integrator 网络为公开生态线索。）
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

- **KP 领英直达**:[André Haack · 领英搜索直达](https://www.linkedin.com/search/results/people/?keywords=Andr%C3%A9%20Haack%20Dallmeier%20Electronics%20GmbH)(搜索链接,点入后核职位再加;来源:档案正文提取)
- **中国进口与管制**:国别档位 中(IT-SiG 2.0/BSI 5G 关键组件去华为化;企业网开放,备 CE/SBOM);战术: 中性处理,客户追问原产时答 CE/RED/RoHS 合规+Marvell 芯片;户级进口史: 档案无信号(是否从中国进口过 → 待定)
- **芯片谱(Marvell 专注度)**:Marvell 锚已挂(在卖 MikroTik 谱=Prestera 芯片事实);Marvell 首发即对
- **大概率用到的 Saga 型号**:大概率会用: STC-28DGGPM(24G PoE+/4×25G→分销走量)(本行为调查分析结论,与开发信首推型号是两回事)
