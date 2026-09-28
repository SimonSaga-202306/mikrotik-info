# Bernhard Kröll / Giganet

> **评级 A**　|　奥地利 · Mayrhofen　|　档案编号 `A-018`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长、PoE/监控/门禁），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Giganet |
| 国家 | 奥地利 |
| 城市 | Mayrhofen |
| 网站 | giganet.at |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCTCE+MTCIPv6E+MTCSWE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328GP-4GX24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 持 MTCSWE；**23 年 MikroTik/RouterOS 经验**；从 SOHO 到企业网与数据中心（HC3 Scale Computing）；专长含 **switching、VLANs**、BGP、防火墙、隧道 VPN/IPsec/WireGuard、PPPoE、CAPsMAN、QoS 与队列、高可用与负载均衡、数据中心托管、监控、备份、自动化、网络审计 |

## 三、人员与联系方式

- **对接人**：Bernhard Kröll
- **邮箱**：bk@giganet.at
- **电话**：+43 5285 2022
- **原始联系字段**：+43 5285 2022 / bk@giganet.at

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCTCE、MTCIPv6E、MTCSWE

- `MTCNA` — 网络助理（入门）
- `MTCTCE` — 流量控制
- `MTCIPv6E` — IPv6
- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：CAPsMAN、IPsec、MikroTik、RouterOS、WireGuard

## 五、跟进策略

**场景判断**：PoE / 监控 / 门禁

### 推什么型号

**LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`LT-S8328GP-4GX24GT-S`（供参考，以实际沟通为准）

### 核心卖点

802.3bt 单口 90W、**PoE 看门狗（摄像头死机自动断电重启，省一趟上门）**、250m 延长供电、端口隔离、整机功率预算足

### 怎么开发

替他算一笔账：24 个 4K 头全开要多少瓦、满配后还剩多少余量——这是每个做监控的人都踩过的坑，算清楚就赢一半

### 风险点

**PoE 功率预算和供电稳定性是验收红线**，虚标功率会当场翻车；必须送测、必须给整机功率实测数；部分非标 PoE 相机存在兼容性问题，要先拿他的机型测

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。

- **业务定位**：奥地利 Mayrhofen 的 Giganet（Bernhard Kröll）：23 年 MikroTik/RouterOS 经验的网络工程与 IT 服务商，从 SOHO 到企业网与数据中心（HC3 Scale Computing）。
- **产品线与在售品牌**：MikroTik/RouterOS 主线；数据中心托管与监控/备份/自动化服务。
- **目标行业与场景**：本地企业、酒店/旅游区（Mayrhofen 是滑雪度假区，酒店与民宿密集）、小型数据中心。
- **团队与规模**：个人/小公司，决策链=本人。
- **决策链与对接人**：bk@giganet.at；+43 5285 2022。
- **技术与认证**：MTCNA+MTCTCE+MTCIPv6E+**MTCSWE**；专长 switching/VLANs、BGP、防火墙、VPN（IPsec/WireGuard）、PPPoE、CAPsMAN、QoS、高可用与负载均衡、数据中心托管、监控、备份、自动化、网络审计。
- **采购与供应链信号**：按项目采购；本地旅游区旺季前后是采购窗口。
- **近期动态与线索**：giganet.at 本轮抓取返回 HTTP 500（站点故障）——需在首次联系时确认站点状态；既有记录（2026-09 之前）显示其业务与技能覆盖完整。
- **与我方契合点**：酒店/民宿场景 = AP + 摄像头 + 门禁全 PoE；他会 CAPsMAN 与 VLAN 分段，管理型 PoE 是自然升级。
- **风险与注意**：站点 500 → 可能是临时故障；沟通中以「他的方案语言」（VLAN/CAPsMAN/可用性）切入。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【近期动态与线索】**giganet.at 本轮抓取 HTTP 500（服务器错误，未取得页面）。
  > （2026-09-28 fetch_page 返回 HTTP 500）
  > 来源：https://www.giganet.at/
- **【技术与认证】**既有记录：23 年经验、MTCSWE、从 SOHO 到企业与数据中心。
  > 持 MTCSWE；23 年 MikroTik/RouterOS 经验；专长含 switching、VLANs、BGP、防火墙、隧道 VPN/IPsec/WireGuard、PPPoE、CAPsMAN、QoS 与队列、高可用与负载均衡、数据中心托管、监控、备份、自动化、网络审计
  > 来源：https://mikrotik.com/consultants

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：滑雪区酒店/民宿：AP+摄像头+门禁集中到 24 口 PoE++，VLAN 分段与看门狗；旺季前是采购窗口。
- **要问的问题**：他手上酒店/民宿客户的接入层是怎样的（口数/分段/功率）？
- **随附证明**：功率实测 + VLAN 模板 + 旺季前交期承诺。

### 第 2 次跟进 · 工业级非管理 PoE（滑雪场/室外）

- **推什么**：LT-IS6306G-2GX4GT PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：雪场缆车站/户外监控箱：低温宽温是硬条件（-40°C 起），免配置、双电源。
- **要问的问题**：户外/缆车站点位现在的供电与温度条件是什么？
- **随附证明**：低温实测报告 + 户外箱体安装图 + 样品。

### 第 3 次跟进 · 管理型 PoE（高可用/环网）

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他讲高可用与负载均衡：ERPS 环网 + 双上行 + VLAN 分段，把他现有设计模板升级。
- **要问的问题**：他的高可用方案现在是 STP 还是 ERPS？收敛要求多少？
- **随附证明**：ERPS 收敛实测 + VLAN 模板 + MIB 清单。

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
Hi Bernhard,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on switching, VLAN, WireGuard, IPsec and CAPsMAN.

Where we may be useful: 24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.

How many cameras per job, and what wattage per port are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328GP-4GX24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
