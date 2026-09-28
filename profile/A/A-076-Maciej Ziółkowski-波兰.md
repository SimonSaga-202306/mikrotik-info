# Maciej Ziółkowski

> **评级 A**　|　波兰 · Włocławek / Poznań　|　档案编号 `A-076`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Maciej Ziółkowski |
| 国家 | 波兰 |
| 城市 | Włocławek / Poznań |
| 网站 | mziolkowski.pl |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGM（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | 10+ 年；VPN/路由/防火墙/安全/**交换**/脚本/MikroTik API → 自述含 switching 与 API，做自动化集成 |

## 三、人员与联系方式

- **邮箱**：kontakt@mziolkowski.pl
- **电话**：—
- **原始联系字段**：kontakt@mziolkowski.pl

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

场景信号不明确，先摸底：问清他接入层现在用谁的设备、痛点是供电、VLAN 还是环网，再定型号。

初判可参考型号：`STC-424XGGM（Saga）`

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。

- **业务定位**：波兹南注册的技术顾问个体户（AZM / ZM Technika），做网络与安全方向的自动化集成；CSV 记录常驻 Włocławek/Poznań 两地。
- **产品线与在售品牌**：顾问+集成服务（方案/配置/运维/脚本化）；官网故障看不到在售目录，触达走邮箱/电话。
- **目标行业与场景**：中小企业网络与安全项目；MikroTik API 自动化=批量设备场景（多站点客户）。
- **团队与规模**：个体工商户（NIP/REGON 齐全），一人作业。
- **决策链与对接人**：Maciej Ziółkowski 本人（kontakt@mziolkowski.pl，CSV 记录）。
- **技术与认证**：MTCNA+MTCRE；脚本/API 能力=会写自动化配置工具的技术型买家。
- **采购与供应链信号**：项目制选型；API 自动化意味着他愿意评估「可编程、文档全」的新硬件品牌。
- **近期动态与线索**：官网 500（2026-09-28 抓取）——站点维护断档，沟通别引用网站内容。
- **与我方契合点**：API/CLI 可编程是我们对技术型顾问的核心卖点：批量下发、配置模板、MIB 文档全套英文。
- **风险与注意**：官网故障期间邮箱@自有域可能也不稳——邮件退信就改走名录电话路径；别提看过他的报错页。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【近期动态与线索】**官网 mziolkowski.pl 本轮（含 www 变体）抓取均返回 HTTP 500——站点故障，未取得内容。
  > （2026-09-28 fetch_page 对 http://www.mziolkowski.pl/ 返回 HTTP 500）
  > 来源：http://www.mziolkowski.pl/
- **【业务定位】**GoWork 企业信息页（第三方）：AZM Maciej Ziółkowski（ZM Technika），行业分类「企业技术顾问」，注册地址 Poznań ul. Poręba 18。
  > AZM Maciej Ziółkowski · ul. Poręba 18 61-602 Poznań · NIP: 9720182560 · REGON: 634573720 · Branże: Doradcy techniczni dla firm
  > 来源：https://www.gowork.pl/maciej-ziolkowski-zm-technika,22122210/dane-kontaktowe-firmy
- **【技术与认证】**CSV 既有 MikroTik 名录记录：MTCNA+MTCRE，10+ 年经验，技能含 VPN/路由/防火墙/安全/交换/脚本/MikroTik API——自动化集成方向（CSV 记录）。
  > 10+ 年；VPN/路由/防火墙/安全/交换/脚本/MikroTik API → 自述含 switching 与 API，做自动化集成（CSV 备注）
  > 来源：https://mikrotik.com/consultants

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（项目接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：技术开场：CLI/API 文档+24 口 PoE++ 规格，主打「可自动化管理的接入层」而不是便宜。
- **要问的问题**：你项目接入层现在怎么批量下发配置？
- **随附证明**：CLI/API 文档（英文）+ 规格书。

### 第 2 次跟进 · 工业级非管理 PoE（现场点位）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：他跑现场的零散点位补盲：4 口宽温 DIN 免配置——即插即用不占运维工时。
- **要问的问题**：现场无空调区点位多吗？用什么机型？
- **随附证明**：宽温报告 + DIN 图 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（自动化运维样板）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：对接他的 API 玩法：管理型全套 CLI/SNMP API+MIB 库，提供配置模板生成脚本示例，帮他做多站点自动化。
- **要问的问题**：要不要我们提供一份交换机 API 调用示例库？
- **随附证明**：API 示例 + MIB 库 + 配置模板（英文）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：Access switching — quick question

```text
Hi Maciej,

I build managed access switches (PoE and industrial) and your profile came up while I was looking at who is actually doing this work in your market.

What caught my eye is that you work on switching.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you using for access layer today, and where does it hurt?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424XGGM evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
