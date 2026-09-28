# Nick Shore

> **评级 A**　|　英国 · Debenham　|　档案编号 `A-074`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Nick Shore |
| 国家 | 英国 |
| 城市 | Debenham |
| 网站 | shore.me.uk |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGM（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | WISP/ISP 方向；BGP、OSPF、防火墙、动态路由、流量管理、**switching**、VPN、CAPsMAN |

## 三、人员与联系方式

- **邮箱**：nick@shore.me.uk
- **电话**：+44 7588 286095
- **原始联系字段**：+44 7588 286095 / nick@shore.me.uk

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由

**涉及品牌 / 技术**：CAPsMAN、MikroTik

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**STC-424XGGPM-440W（Saga）（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`STC-424XGGM（Saga）`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。

- **业务定位**：英国 MikroTik 元老级顾问：Multithread 前 MD（已半退休），现按项目制接临时咨询——影响力与资历远大于当前业务量。
- **产品线与在售品牌**：咨询服务（BGP/OSPF/VPN/防火墙/WISP 设计）；早年亲手做过硬件分销（linitx.com 创始团队成员）。
- **目标行业与场景**：ISP/WISP 与企业广域网；NHS 网络基础设施（历史项目）；Suffolk 本地 WISP 圈。
- **团队与规模**：个人；Debenham（Suffolk 乡村）。
- **决策链与对接人**：Nick Shore 本人（+44 7588 286095 / nick@shore.me.uk；另有 Fediverse 账号 shore.me.uk/social/nick）。
- **技术与认证**：MTCNA+MTCRE（CSV 名录记录）；RB112 时代入行，对 MikroTik 硬件生态史如数家珍。
- **采购与供应链信号**：半退休=偶发项目的小批量选型；真正价值在他的英国 MikroTik 渠道人脉（linitx 系）。
- **近期动态与线索**：2025 起「mostly retired」+在做商业导师（Help to Grow 项目）——别按活跃顾问的频率打扰。
- **与我方契合点**：他做过的项目=接入层与 WISP 设备选型；更大价值=引荐+背书：向英国 MikroTik 圈介绍我们时他一句话顶十封邮件。
- **风险与注意**：低频联系人：一年 1–2 封高质量问候即可；别发推销模板信，尊重前辈身份。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【近期动态与线索】**本人 CV 页自述 2025 年夏天（55 岁）已「基本退休」，目前只接临时性商务/技术咨询——活跃度明显下降，如实标注。
  > In the summer of 2025, at the grand old age of 55, I decided to do something different, and I retired (mostly). · I'm also still available for business and technical consultancy on an ad-hoc project basis.
  > 来源：https://shore.me.uk/cv/
- **【团队与规模】**履历：Multithread 1999–2025（技术顾问→CTO→2021 起任董事总经理）；早年还参与运营 linitx.com（英国 MikroTik 分销老店，2003 年起）。
  > 2021-2025 Multithread Consultants - Managing Director · 1999-2014 - Technical Consultant │ linitx.com - 2003 onwards
  > 来源：https://shore.me.uk/cv/
- **【技术与认证】**MikroTik 专页自述：在还没有实体 RouterBOARD 之前就开始用 RouterOS，给 Suffolk 本地 WISP 搭过 mini-ITX 路由，并在英国卖过 RB112，「我们甚至用 MikroTik 建过一个 WISP」。
  > I started using Mikrotik RouterOS before there were actual physical RouterBoards ! · we built some mini ITX based routers using RouterOS for a local WISP in Suffolk · We even built a WISP using Mikrotik.
  > 来源：https://shore.me.uk/mikrotik/
- **【业务定位】**专页技能清单：静态/BGP/OSPF 路由、IPsec/WireGuard VPN、防火墙、DHCP/DNS、Winbox/ssh/ROMON 管理——老一代 WISP 全栈。
  > Routing — Static, BGP, OSPF · VPNs — IPSec, Wireguard · Management — Winbox, ssh, ROMON
  > 来源：https://shore.me.uk/mikrotik/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（手上项目配套）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：轻量问候式：他还在接零星咨询——24 口 PoE++ 作为「手上项目需要接入层时的一个可靠便宜选项」，附英文资料备着。
- **要问的问题**：您手上项目如果缺接入层，愿不愿意试一台？
- **随附证明**：规格书（英文 PDF）+ 英国交付说明。

### 第 2 次跟进 · 工业级非管理 PoE（WISP/室外点）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：情怀+实用：WISP 塔站/室外点的宽温免维护小机——聊聊他 Suffolk WISP 年代的供电痛点。
- **要问的问题**：当年塔站交换机坏机率高吗？现在这种宽温免配置的会不会省心点？
- **随附证明**：宽温报告 + 样机。

### 第 3 次跟进 · 管理型 PoE + 人脉引荐

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：请他看 L2/L3 实测数据（他看得懂）；若认可，请他向相熟的英国 MikroTik 经销商/顾问引荐——这是本户真正的产出。
- **要问的问题**：如果您觉得数据靠谱，方便引荐一两家您觉得合适我们聊聊的英国同行吗？
- **随附证明**：ERPS/收敛实测 + 引荐话术包（英文）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：L3 hardware offload + QinQ on access switching

```text
Hi Nick,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on WISP, switching and CAPsMAN.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424XGGM evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
