# Dinko Ivanov / MBN Glasfaser

> **评级 A**　|　德国 · Westhofen　|　档案编号 `A-027`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（光纤接入），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | MBN Glasfaser |
| 国家 | 德国 |
| 城市 | Westhofen |
| 网站 | mbn-glasfaser.de |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCSE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XG-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 光纤接入 ISP（公司名带 Glasfaser）→ FTTH 项目需要接入层交换机 |

## 三、人员与联系方式

- **对接人**：Dinko Ivanov
- **邮箱**：dinko.ivanov@mbn-glasfaser.de
- **电话**：+49 6344 9442084
- **原始联系字段**：+49 6344 9442084 / dinko.ivanov@mbn-glasfaser.de

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCSE` — 安全

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：光纤接入 / FTTH

### 推什么型号

**LT-S8328XG-4XS24GT-S（24×千兆 + 4×万兆 SFP+）**

> 系统初判型号：`LT-S8328XG-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

4×10G SFP+ 上行、QinQ 做用户隔离、端口隔离、组播、广播风暴抑制

### 怎么开发

问「OLT 下面挂多少用户？每用户怎么隔离？上行带宽怎么收敛？」——他们是按端口数买设备的，算单端口成本最有效

### 风险点

户外机柜场景要确认温度和防雷等级；运营商类客户可能要求入网许可或本地认证，先问清楚再报价

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 七、首触邮件（可直接发送）

**主题**：Per-subscriber isolation on your FTTH build

```text
Hi Dinko,

I build access switches for FTTH and fixed wireless — per-subscriber isolation and uplink aggregation are the whole job.

What caught my eye is that you work on FTTH.

Where we may be useful: 4×10G SFP+ uplink, QinQ per subscriber, port isolation, broadcast storm control, IGMP for IPTV.

How are you isolating subscribers now — QinQ per user, or something simpler?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328XG-4XS24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
