# Batna（anteny24.pl）

> **评级 A**　|　波兰　|　档案编号 `A-510`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— R53 B段复筛达标升级：B 段逐站复筛达标（站点在线 + 交换机品类/产品在售 + 网络/交换专营 + 小公司决策链短）；官网核对：Batna24（波兰，2001 年起）自述 **«Leader in the network equipment trade»**，UniFi Enterprise Partner Program 成员；**Switches 类目在售 Ubiquiti USW-Pro-XG-8-PoE（L3, 8×10GbE PoE, 155W）、USW-Pro-XG-24-PoE（16×10GbE+8…；原 B-258 升级，编号顺延 A-510
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Batna（anteny24.pl） |
| 国家 | 波兰 |
| 城市 | — |
| 网站 | batna24.com |
| 类型 | 分销（MikroTik 官方） |
| 反向信号 | MikroTik（Master+VAD） |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-IS6312XGP-4XS8GT |
| 切入点 | 卖 MikroTik 但缺工业/ERPS/PoE++ → 用同价位工业线补他的产品缺口 |
| 数据来源 | 2026-09-22 |
| 原备注 | Częstochowa；WISP 渠道 【2026-09-28 R49 复筛补录】来源等级：official-company。官网在线；货架含交换机品类与 MikroTik 线：batna24.com（Batna24，20+ 年，网络设备贸易）：在售 Switches 品类与 MikroTik / Ubiquiti / Teltonika / Mimosa 等品牌；波兰 Częstochowa 系 anteny24.pl 品牌经营 结论：维持 B（无采购/替换新证据）。 证据：[1](https://www.batna24.com/gb/)；批次：batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json#B-258 【2026-09-28 R53 B段复筛达标升级】官网核对：Batna24（波兰，2001 年起）自述 **«Leader in the network equipment trade»**，UniFi Enterprise Partner Program 成员；**Switches 类目在售 Ubiquiti USW-Pro-XG-8-PoE（L3, 8×10GbE PoE, 155W）、USW-Pro-XG-24-PoE（16×10GbE+8×2.5GbE+2×SFP28, 720W）、USW-WAN、USW-Flex-2.5G-8** 等；品牌 Ubiquiti／MikroTik／Teltonika／Mimosa。原 B-258 → 现 A-510，物理位置不动、原 B 号空置不回填；证据与原文摘录见批次文件。 证据：[1](https://www.batna24.com/gb/)；批次：batch/contact_research_2026-09-28_R53_B复筛升级.json#A-510 |

## 三、人员与联系方式

- **邮箱**：lukasz@anteny24.pl
- **电话**：+48 34 3610 448
- **原始联系字段**：+48 34 3610 448 / lukasz@anteny24.pl

## 四、品牌与技术栈

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：ISP / 骨干

### 推什么型号

**LT-S8328XG-4XS24GT-S（4×10G 上行，收敛比高）**

> 系统初判型号：`LT-IS6312XGP-4XS8GT`（供参考，以实际沟通为准）

### 核心卖点

4×10G 上行、QinQ 用户隔离、组播、端口隔离、广播抑制、SNMP 对接现有网管

### 怎么开发

问「接入层一台带多少用户？上行怎么收敛？」；他们按端口成本算账，把单端口价格摊到每个用户给他看

### 风险点

ISP 对设备故障率极度敏感，一台炸掉就是一批投诉；要先小批量试用跑半年；备件和 RMA 响应速度要提前承诺

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 七、首触邮件（可直接发送）

**主题**：Access layer cost per port

```text
Hi Batna（anteny24.pl）,

I do access switches for WISPs and small ISPs, where the number that matters is cost per subscriber port.

What caught my eye is that you work on WISP.

Where we may be useful: 4×10G uplink, QinQ subscriber isolation, port isolation, broadcast suppression, SNMP that drops into whatever NMS you already run.

How many subscribers per access switch, and what uplink ratio are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a LT-IS6312XGP-4XS8GT evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
