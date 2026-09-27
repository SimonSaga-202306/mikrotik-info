# BRS Networks AB

> **评级 A**　|　瑞典　|　档案编号 `A-127`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（光纤接入），三星重点
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | BRS Networks AB |
| 国家 | 瑞典 |
| 城市 | — |
| 网站 | — |
| 类型 | 集成商/代理（Allied Telesis） |
| 反向信号 | Allied Telesis（Marvell Prestera 接入层）+ Fortinet |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | Marvell 接入层生态切入 |
| 数据来源 | 厂商官方渠道名录 |
| 原备注 | **光纤网络方案商，业务覆盖瑞典、丹麦、德国** —— 北欧+德语区三地经营。 |

## 三、人员与联系方式

- **邮箱**：—
- **电话**：—
- **原始联系字段**：见 elioplus 渠道库

## 四、品牌与技术栈

**涉及品牌 / 技术**：Fortinet

## 五、跟进策略

**场景判断**：光纤接入 / FTTH

### 推什么型号

**LT-S8328XG-4XS24GT-S（24×千兆 + 4×万兆 SFP+）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

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
Hi BRS,

I build access switches for FTTH and fixed wireless — per-subscriber isolation and uplink aggregation are the whole job.

Where we may be useful: 4×10G SFP+ uplink, QinQ per subscriber, port isolation, broadcast storm control, IGMP for IPTV.

How are you isolating subscribers now — QinQ per user, or something simpler?

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
