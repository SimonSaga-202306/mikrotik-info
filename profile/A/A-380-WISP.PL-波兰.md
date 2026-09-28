# WISP.PL

> **评级 A**　|　波兰　|　档案编号 `A-380`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— B/C复筛第1批：官网核验渠道分销并含工业交换机（Scodeno）品类；原B-272升级，编号顺延A-380
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | WISP.PL |
| 国家 | 波兰 |
| 城市 | — |
| 网站 | wisp.pl |
| 类型 | 分销（MikroTik 官方） |
| 反向信号 | MikroTik（Master+VAD） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-488XGGPM（Saga） |
| 切入点 | 卖 MikroTik 但缺工业/ERPS/PoE++ → 用同价位工业线补他的产品缺口 |
| 数据来源 | 2026-09-22 |
| 原备注 | Bełk；【2026-09-28 B/C复筛第1批】来源等级：official-company（复筛核验）。原B-272。核验要点：站内为渠道分销（MikroTik/Ubiquiti/TP-Link/Teltonika/Cudy），并含工业交换机品类（Scodeno，/m242,scodeno.html）；站点横幅列 MBUM#11 Poznań 与 Solarix 机柜、USR-IoT LoRa → 交换机渠道证据成立，升A（A-380）。未获具名联系人，仅公开销售邮箱sklep@与电话+48 32 721 86 72（按人工定级A记录，公司与A-363等公司级入口同口径）。未发送邮件、未提交表单；公开邮箱不等于可投递或采购权限。 证据：[1](https://wisp.pl/) [2](https://wisp.pl/m242,scodeno.html) 仅覆盖所述渠道/产品线事实；批次：batch/contact_research_2026-09-28_BCrescreen_A379-A384.json#A-380 |

## 三、人员与联系方式

- **邮箱**：sklep@wisp.pl
- **电话**：+48 32 721 86 72
- **原始联系字段**：+48 32 721 86 72 / sklep@wisp.pl

## 四、品牌与技术栈

**涉及品牌 / 技术**：MikroTik、TP-Link、Teltonika、Ubiquiti

## 五、跟进策略

**场景判断**：工业 / 楼宇自控

### 推什么型号

**STI-488XGGPM（Saga）（导轨式，4×10G 上行 + 8×千兆 PoE++）**

> 系统初判型号：`STI-488XGGPM（Saga）`（供参考，以实际沟通为准）

### 核心卖点

DIN 导轨安装、-40~75℃ 宽温、宽压输入、双电源冗余、ERPS 环网收敛 <20ms、PoE++ 90W 直接带工业相机和 AP

### 怎么开发

第一句就问「你工业现场现在用谁的交换机？环网收敛多少毫秒？」——用 ERPS 实测数据对比切入，然后要求送一台上机柜实测 30 天

### 风险点

工业客户认硬认证（CE / UL / EN50155 / 海事 DNV），缺一项直接出局；温度范围、MTBF、EMC 等级必须给书面数据，不能口头说；现场一旦上线几乎不换，所以第一次必须测通，否则永远没第二次

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 七、首触邮件（可直接发送）

**主题**：Ring convergence + -40 to 75C switches

```text
Hi WISP.PL,

I do industrial access switches — DIN rail, wide temperature, ERPS ring — which matches the environments you work in.

What caught my eye is that you work on WISP.

Where we may be useful: DIN rail, -40 to 75 C, wide input voltage, dual power input, ERPS ring under 20 ms, PoE++ for cameras and APs on the same unit.

What ring protocol are you on today, and what convergence do you actually see?

If it is easier to judge from hardware than from a datasheet, I can send a STI-488XGGPM evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

Either way, no follow-up sequence from me.

Best,
[your name]
```

> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；③ 落款换成你自己的名字与公司；④ 一次只问一个问题。

## 八、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
