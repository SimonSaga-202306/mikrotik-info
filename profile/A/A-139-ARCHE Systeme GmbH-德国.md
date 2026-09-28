# ARCHE Systeme GmbH

> **评级 A**　|　德国 · Wilhelmshaven　|　档案编号 `A-139`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— 自动规则已跳过；人工指定
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | ARCHE Systeme GmbH |
| 国家 | 德国 |
| 城市 | Wilhelmshaven |
| 网站 | https://www.arche-systeme.de |
| 类型 | 集成商/代理（Allied Telesis） |
| 反向信号 | Allied Telesis（Marvell Prestera 接入层） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | Marvell Prestera 接入层切入 |
| 数据来源 | Allied Telesis 官方伙伴定位器（?country=germany） |
| 原备注 | 伙伴等级：Resell。 【2026-09-27 联系方式核验】公开邮箱·一方/伙伴来源。Sperry Marine 官方合作站名录公开 Wilhelmshaven ARCHE 邮箱；不是西班牙考古 ARCHEsystem。 来源：[2](https://www.sperrymarine.com/partner-service-stations/eur-arche-systeme-gmbh/) |

## 三、人员与联系方式

- **邮箱**：info@arche.de
- **电话**：—
- **原始联系字段**：info@arche.de [Publicly listed; delivery not tested]; https://www.arche-systeme.de

## 四、品牌与技术栈

**涉及品牌 / 技术**：（未记录）

## 五、跟进策略

**场景判断**：工业 / 楼宇自控

### 推什么型号

**STI-488XGGPM（Saga）（导轨式，4×10G 上行 + 8×千兆 PoE++）**

> 系统初判型号：`STC-424XGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

DIN 导轨安装、-40~75℃ 宽温、宽压输入、双电源冗余、ERPS 环网收敛 <20ms、PoE++ 90W 直接带工业相机和 AP

### 怎么开发

第一句就问「你工业现场现在用谁的交换机？环网收敛多少毫秒？」——用 ERPS 实测数据对比切入，然后要求送一台上机柜实测 30 天

### 风险点

工业客户认硬认证（CE / UL / EN50155 / 海事 DNV），缺一项直接出局；温度范围、MTBF、EMC 等级必须给书面数据，不能口头说；现场一旦上线几乎不换，所以第一次必须测通，否则永远没第二次

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第7批.json`。

- **业务定位**：北海威廉港的舰船电子承包商：军船加固硬件+舰船网络+港口/风场软件。⚠️ 其军船主业是我们的禁区；民用线（民船 Sperry 服务站/港口 SKSS/岸上 DC）是唯一可谈段。
- **产品线与在售品牌**：硬件开发/加固安装（军规）+军民用舰船网络+数据中心+SKSS 港口管理软件+风电雷达夜标。
- **目标行业与场景**：军：海军舰船厂（禁区）。民：商船导航服务（Sperry）、港口交通技术、风场空管、岸上数据中心。
- **团队与规模**：专业舰船电子工程公司（30+ 年历史感）。
- **决策链与对接人**：info@arche.de（CSV 9-27：Sperry 官方名录公开）。
- **技术与认证**：军规环境试验体系；Sperry Marine 服务站（CSV 记录）；Allied Resell（CSV 记录）。
- **采购与供应链信号**：⚠️ 军船采购链绝不可进（ITAR/北约标准/德国安全审查）；民船与港口商业段按普通商业件谈。
- **近期动态与线索**：军船景气（德国海军扩张期）——他的注意力在军段，民用段是小头。
- **与我方契合点**：很窄：民船导航服务站的岸基站/港口管理机房/他自家 DC 项目的商用交换件——只做这三处。
- **风险与注意**：第一封必须划线：军船/海军段不供——反而显得专业；若他主要需求在军段，就此打住归档（不强求）。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**⚠️ 官网自述：为军用与民用造船及数据中心建设复杂网络（铜缆+光缆）——军政船舶是其核心场。
  > Komplexe Netzwerke für den militärischen und zivilen Schiffbau sowie für Rechenzentren mit Kupfer- und Lichtwellenleitertechnik.
  > 来源：https://www.arche-systeme.de/
- **【技术与认证】**舰用硬件加固体系：适配各舰级（扫雷艇/护卫舰/补给舰/潜艇），过 EMV/磁性/气候/冲击/振动全套环境试验——⚠️ 军规等级，我们不做该段。
  > Härtung, Integration und Installation von Hardware für raue Bedingungen an Bord von Marineschiffen, mit Anpassung an die Bedingungen für verschiedene Bootsklassen (Minenboote, Fregatten, Einsatzgruppenversorger, U-Boote, etc.). Unsere Hardware durchläuft dabei verschiedene Umwelttests, wie EMV, Magnetik, Klima, Schock und Vibration.
  > 来源：https://www.arche-systeme.de/
- **【目标行业与场景】**客户与伙伴：德国海军、造船厂、THALES、Hagenuk、IBM、ESG、CONET、Blohm&Voss；与 Thyssen Krupp Marine Systems 合作潜艇项目。另有民用线：港口管理软件 SKSS 与风电场雷达夜标软件。
  > Kunden und Partner… sind die deutsche Marine, Werften und bekannte Unternehmen wie THALES, Hagenuk Marinekommunikation, IBM, ESG, CONET, Blohm&Voss Shipyards… Thyssen Krupp Marine Systeme in Kiel u. a. zur Durchführung von U-Boot Projekten ‖ SKSS - Hafenverwaltungssoftware · Softwareentwicklung zur radargestützten, bedarfsgesteuerten Nachtkennzeichnung für Windparks
  > 来源：https://www.arche-systeme.de/
- **【决策链与对接人】**CSV 9-27 记录：Sperry Marine 官方服务站名录公开 Wilhelmshaven ARCHE 邮箱（民船导航服务资质）。
  > Sperry Marine 官方合作站名录公开 Wilhelmshaven ARCHE 邮箱；不是西班牙考古 ARCHEsystem（CSV 2026-09-27 记录）
  > 来源：https://www.sperrymarine.com/partner-service-stations/eur-arche-systeme-gmbh/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（民船岸基/港口机房段，军段划线）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：开门见山划边界：仅供民用岸基（港口管理机房/Sperry 岸基站/办公 DC）的商用交换件，军船段不做——递 24 口规格。
- **要问的问题**：民用岸基与机房的接入层用什么？（附军段不供声明，德文）
- **随附证明**：适用边界声明 + 规格对照 + 商用合规包（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（港口户外/码头点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：港口码头户外点位（海风盐雾）：宽温 DIN PoE 商用段配套 SKSS 港口项目。
- **要问的问题**：码头户外点位的交换坏机率？
- **随附证明**：宽温/盐雾说明 + DIN 图 + 备件包价（德文）。

### 第 3 次跟进 · 管理型 PoE（民用段分段标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：其数据中心业务的商用接入管理件：VLAN/ERPS 模板技术评估。
- **要问的问题**：民用 DC 项目的接入管理件评估一下？
- **随附证明**：VLAN/ERPS 模板 + 实测（德文）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：Ring convergence + -40 to 75C switches

```text
Hi ARCHE,

I do industrial access switches — DIN rail, wide temperature, ERPS ring — which matches the environments you work in.

What caught my eye is that you work on marine.

Where we may be useful: DIN rail, -40 to 75 C, wide input voltage, dual power input, ERPS ring under 20 ms, PoE++ for cameras and APs on the same unit.

What ring protocol are you on today, and what convergence do you actually see?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424XGGPM-440W evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
