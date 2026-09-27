# Atlantik Elektronik

> **评级 A**　|　德国　|　档案编号 `A-312`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（工业/楼宇），三星重点
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Atlantik Elektronik |
| 国家 | 德国 |
| 城市 | — |
| 网站 | https://www.atlantikelektronik.com |
| 类型 | 分销（Lantronix 授权） |
| 反向信号 | Lantronix（Marvell 生态，工业 IoT/边缘） |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | Marvell 接入层生态切入 |
| 数据来源 | 厂商官网分销页（当前） |
| 原备注 | Lantronix 授权分销，官网自述提供**全线产品 + design-in 支持**，可协助把嵌入式模块与网络产品整合进标准或定制项目。亦经营 atestore.de 电商。 【2026-09-27 A300–A319联络核验】来源等级：official-company。自营电商atestore的Lantronix专页与获奖新闻给info@atlantikelektronik.com、+49 89 89 505 0；Lantronix多年获奖分销（2022 EMEA Partner of the Year），总部Planegg。 证据：[1](https://www.atestore.de/en/lantronix/) [2](https://bcdatlantik.co.uk/en/news/atlantik-elektronik-becomes-emea-distributor-partner-of-the-year-again) [3](https://www.atestore.de/en/info/ate-services.html) [4](https://exhibitors.electronica.de/exhibitor-portal/2024/list-of-exhibitors/exhibitordetails/atlantik-elektronik-gmbh/) 仅覆盖所述联络/关联事实，不证明投递、在职、采购权、芯片或需求；批次：batch/contact_research_2026-09-27_A300-A319.json#A-312 |

## 三、人员与联系方式

- **邮箱**：info@atlantikelektronik.com
- **电话**：+49 89 89 505 0
- **原始联系字段**：info@atlantikelektronik.com（atestore Lantronix专页联系信息）；+49 89 89 505 0；Lantronix授权分销页：atestore.de/en/lantronix/

## 四、品牌与技术栈

**涉及品牌 / 技术**：（未记录）

## 五、跟进策略

**场景判断**：工业 / 楼宇自控

### 推什么型号

**LT-IS6312XGP-4XS8GT（导轨式，4×10G 上行 + 8×千兆 PoE++）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

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
Hi Atlantik,

I do industrial access switches — DIN rail, wide temperature, ERPS ring — which matches the environments you work in.

What caught my eye is that you work on Lantronix, design-in and atestore.

Where we may be useful: DIN rail, -40 to 75 C, wide input voltage, dual power input, ERPS ring under 20 ms, PoE++ for cameras and APs on the same unit.

What ring protocol are you on today, and what convergence do you actually see?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328XGP-4XS24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
