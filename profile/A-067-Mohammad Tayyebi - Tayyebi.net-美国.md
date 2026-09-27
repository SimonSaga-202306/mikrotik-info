# Mohammad Tayyebi / Tayyebi.net

> **评级 A**　|　美国 · Austin, TX　|　档案编号 `A-067`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　重点，且好跟进（有具体对接人、决策链短）
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长、组播/IPTV），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Tayyebi.net |
| 国家 | 美国 |
| 城市 | Austin, TX |
| 网站 | tayyebi.net |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCTCE+MTCUME+MTCINE+MTCIPv6E+MTCSWE |
| 原备注 | ★★ 8 证含 **MTCSWE**；20+ 年 ISP/WISP 与数据中心；**MikroTik 认证讲师 + 学术讲师（Academy Trainer）**；做托管网络服务（设计/实施/迁移/监控/加固/安全，24/7）；专长含 **交换（MAC-based VLAN、QinQ）**、高可用 VRRP/LACP/绑定、DDoS 防护、组播、MPLS/VPLS/VRF；**还能把 MikroTik 与别的品牌集成并做双向迁移** → 最懂多厂商替代的人 |

## 三、人员与联系方式

- **对接人**：Mohammad Tayyebi
- **邮箱**：MohammadTayyebi@Gmail.Com
- **电话**：1-512-713-6825
- **原始联系字段**：1-512-713-6825 / MohammadTayyebi@Gmail.Com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCTCE、MTCUME、MTCINE、MTCIPv6E、MTCSWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCTCE` — 流量控制
- `MTCUME` — 用户管理（Hotspot / PPPoE）
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：MikroTik

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
Hi Mohammad,

Multicast is where most IPTV and camera builds quietly fall over, and it is the part I specialise in on the access switch.

What caught my eye is that you work on WISP, QinQ and VLAN.

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
