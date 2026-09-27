# Michael Jezierski / IndyCar

> **评级 A**　|　美国 · Indianapolis　|　档案编号 `A-065`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、PoE/监控/门禁、组播/IPTV），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | IndyCar |
| 国家 | 美国 |
| 城市 | Indianapolis |
| 网站 | indycar.com |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCIPv6E+MTCSWE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328GP-4GX24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 持 MTCSWE；**专做美国赛车运动产业与车队（邮箱是 @indycar.com，人在 IndyCar 赛事方）**；业务：Layer 2/3、无线 LAN、PtP、**IP 视频与组播 IP Video & Multicast**、IP 对讲、**Audinate Dante 认证 1/2/3 级（专业音频 over IP）** → 赛事转播+ Dante 音频对交换机的 IGMP Snooping/组播/低时延要求极高，是极高门槛高单价的细分市场 |

## 三、人员与联系方式

- **对接人**：Michael Jezierski
- **邮箱**：mjezierski@indycar.com
- **电话**：+1 317 492 5005
- **原始联系字段**：+1 317 492 5005 / mjezierski@indycar.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCIPv6E、MTCSWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCIPv6E` — IPv6
- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：Audinate、Dante、MikroTik

## 五、跟进策略

**场景判断**：组播 / IPTV

### 推什么型号

**LT-S8328GP-4GX24GT-S（组播能力完整 + PoE 供电）**

> 系统初判型号：`LT-S8328GP-4GX24GT-S`（供参考，以实际沟通为准）

### 核心卖点

IGMP Snooping v2/v3、IGMP Querier、组播 VLAN、快速离开（Fast Leave）、**QoS/DSCP 优先级队列**（Dante 音频 over IP 与 IPTV 都靠它不丢包不抖动）

### 怎么开发

开口就问「IPTV 卡不卡？是不是组播没配好，全楼在泛洪？」；若是 Dante / 音频 over IP 场景，改问「音频有没有出现过断续或丢包？」——Dante 对组播和 QoS 极敏感，说中就是内行

### 风险点

组播出问题是满屏花屏，客户零容忍；必须先小规模（一个楼层）验证再铺开；要确认他的组播源和播放器兼容性

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 七、首触邮件（可直接发送）

**主题**：IGMP / multicast behaviour on your IPTV builds

```text
Hi Michael,

Multicast is where most IPTV and camera builds quietly fall over, and it is the part I specialise in on the access switch.

What caught my eye is that you work on Dante, Audinate, multicast and IGMP.

Where we may be useful: IGMP snooping v2/v3, a querier so the VLAN stops flooding, multicast VLAN, fast leave, and DSCP/QoS queues — the things that decide whether IPTV is watchable and whether Dante audio drops out.

Are you running IGMP snooping plus a querier, or still flooding the VLAN?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328GP-4GX24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
