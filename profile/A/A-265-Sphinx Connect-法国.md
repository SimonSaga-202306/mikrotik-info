# Sphinx Connect

> **评级 A**　|　法国 · Montaigu　|　档案编号 `A-265`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），三星重点
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Sphinx Connect |
| 国家 | 法国 |
| 城市 | Montaigu |
| 网站 | https://www.sphinxfrance.com |
| 类型 | 分销/集成商（Perle 授权） |
| 反向信号 | Perle Systems（工业 PoE 交换机 / 媒体转换 / 串口设备联网） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | Marvell Prestera 接入层切入 |
| 数据来源 | Perle Systems 官方分销名录 |
| 原备注 | Perle 授权分销商。⚠️ 与库内 Sphinx Italia / Sphinx Computer Vertriebs（德）**同为 Sphinx 系但不同法人**，勿当成重复合并。 【2026-09-27 A260–A279联络核验】来源等级：official-company。Sphinx France官网联系页正文给出sales@sphinxfrance.fr、+33 2 51 09 26 60与Montaigu地址Parc de la Bretonnière，与Perle法国名录中的Sphinx Connect地址一致；Advantech伙伴目录另给mail@sphinxconnect.fr作旁证。库内C-214 Sphinx France、C-047 Sphinx Italia及德Sphinx Computer Vertriebs为不同法人/品牌，勿合并。 证据：[1](https://www.sphinxfrance.com/contactez-nous) [2](https://www.perle.com/howtobuy/distributors.aspx?countryname=France) [3](https://www.advantech.com/emt/partners/channel/419) 仅覆盖所述联络/关联事实，不证明投递、在职、采购权、芯片或需求；批次：batch/contact_research_2026-09-27_A260-A279.json#A-265 |

## 三、人员与联系方式

- **邮箱**：sales@sphinxfrance.fr
- **电话**：—
- **原始联系字段**：sales@sphinxfrance.fr（官网联系页正文；未测试投递）；原入口：见 Perle 名录（distributor=642）

## 四、品牌与技术栈

**涉及品牌 / 技术**：（未记录）

## 五、跟进策略

**场景判断**：PoE / 监控 / 门禁

### 推什么型号

**STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`STC-424XGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

802.3bt 单口 90W、**PoE 看门狗（摄像头死机自动断电重启，省一趟上门）**、250m 延长供电、端口隔离、整机功率预算足

### 怎么开发

替他算一笔账：24 个 4K 头全开要多少瓦、满配后还剩多少余量——这是每个做监控的人都踩过的坑，算清楚就赢一半

### 风险点

**PoE 功率预算和供电稳定性是验收红线**，虚标功率会当场翻车；必须送测、必须给整机功率实测数；部分非标 PoE 相机存在兼容性问题，要先拿他的机型测

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第14批.json`。

- **业务定位**：法国 25 年 IIoT 分销（Moxa 锚牌+OT 安全门面）：工业交换机在架——**Moxa 之下价位档与窄线是口子**。
- **产品线与在售品牌**：Moxa/Semtech/Sintrones/Kerlink/Adder/InHand 等+工业交换机/4G 路由/串口/KVM 类目。
- **目标行业与场景**：法国工业/能源/交通集成商渠道；OT 安全话题客群。
- **团队与规模**：中型 VAD（商城+博客+25 年）。
- **决策链与对接人**：sales@sphinxfrance.fr（官网联系页正文，CSV 9-27 official-company）；+33 2 51 09 26 60。
- **技术与认证**：Perle 授权分销（CSV 记录）+Moxa 等在架。
- **采购与供应链信号**：Moxa 锚位极深：只做**非管理低价档工业件**与 Moxa EOL 替换报价单旁的价位档——EOL 横幅=老型号替换需求在流动。
- **近期动态与线索**：Moxa EOL 通知挂首页=替换潮窗口主动。
- **与我方契合点**：工业非管理 8 口低价档（CNY）+EOL 替换场景的收发器/小件。
- **风险与注意**：不提替位 Moxa；Sphinx 系三法人勿混淆（只发法国主体）。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**旺代 Montaigu 的 25 年 M2M/IIoT 分销：自述随客户是「distributeur / intégrateur / installateur」都陪跑，OT 网络安全（IEC 62443）为门面主题。
  > Que vous soyez distributeur, intégrateur ou installateur de systèmes, Sphinx France vous accompagne ‖ Cybersécurité OT : Des solutions certifiées… IEC 62443 ‖ 25 ans（横幅）
  > 来源：https://sphinxfrance.com/
- **【产品线与在售品牌】**品牌墙：**Moxa（锚牌，EOL 通告横幅）**/Semtech-Sierra Wireless/Sintrones/Kerlink/Adder/InHand Networks/SECKIOT/Tyrex/Tosibox；类目=工业交换机/4G 路由/工控机/LoRaWAN 网关/串口转换/KVM。Perle 授权（CSV 记录）。
  > （品牌墙）Moxa · Semtech-Sierra Wireless · Sintrones · Kerlink · Adder · InHand ‖ Switch industriel · Routeur 4G industriel · PC industriel · Gateway LoRaWAN · Convertisseur RS232…
  > 来源：https://sphinxfrance.com/
- **【风险与注意】**⚠️ 与库内 Sphinx Italia / Sphinx Computer Vertriebs（德）同属 Sphinx 系但**不同法人**，CSV 明示勿当重复合并、勿跨主体串话。
  > （CSV 记录）与库内 Sphinx Italia / Sphinx Computer Vertriebs（德）同为 Sphinx 系但不同法人，勿当成重复合并
  > 来源：https://sphinxfrance.com/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · Moxa 邻位：工业非管理低价档一页

- **推什么**：STI-280GE（Saga）（工业非管理 8×电口 + 2×上联光，宽温）
- **切入点**：法语一封：其工业交换机类目录下补「友善价位」非管理档（分销条件+CE 一体），不碰 Moxa 管理机排位。
- **要问的问题**：工业交换类目录在 Moxa 之外有没有低价位非管理档需求？
- **随附证明**：工业件一页（法）+ CE/EMC/宽温参数。

### 第 2 次跟进 · EOL 替换旁位件

- **推什么**：收发器 + 串口联网件邻位窄线
- **切入点**：随 Moxa EOL 潮的替换报价里可搭的光电转换/串口邻位件（Perle 谱系邻位）。
- **要问的问题**：EOL 替换单的邻位件（收发器类）有供应空档吗？
- **随附证明**：窄线一页价卡（法）。

### 第 3 次跟进 · 分销条款包收口

- **推什么**：—（条款）
- **切入点**：中性发货/梯价/首单条件条款包；不回即冻结。
- **要问的问题**：（无需回）条款留档。
- **随附证明**：分销条款一页（法/英）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：PoE budget question on your camera jobs

```text
Hi Sphinx,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on Perle, Sphinx and Italia.

Where we may be useful: 24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.

How many cameras per job, and what wattage per port are you designing to?

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
