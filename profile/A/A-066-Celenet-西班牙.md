# Celenet

> **评级 A**　|　西班牙 · Beniel (Murcia)　|　档案编号 `A-066`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、组播/IPTV），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Celenet |
| 国家 | 西班牙 |
| 城市 | Beniel (Murcia) |
| 网站 | celenet.es |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 10 证全拿 / 9 证（含 MTCSWE） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | 公司内 2 位顾问，均 9–10 证。Carlos：WISP、OSPF/BGP/MPLS、IPv6 规划、**组播 Multicast**、高可用、负载均衡、流量工程、QoS、CAPsMAN、Hotspot、RouterOS v7。Javier：OSPF/BGP/VLAN/EoIP/MPLS/VPLS、WiFi 部署、带宽管理 |

## 三、人员与联系方式

- **邮箱**：ccardenas@celenet.es、jprietove@celenet.es
- **电话**：+34 622 330 440、+34 649 395 961
- **原始联系字段**：Carlos Cardenas Cebrian +34 622 330 440 / ccardenas@celenet.es；Javier Prieto Vera +34 649 395 961 / jprietove@celenet.es

## 四、品牌与技术栈

**持有认证**：MTCSWE

- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：CAPsMAN、MikroTik、RouterOS

## 五、跟进策略

**场景判断**：组播 / IPTV

### 推什么型号

**STC-424DGGPM-440W（Saga）（组播能力完整 + PoE 供电）**

> 系统初判型号：`STC-424XGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

IGMP Snooping v2/v3、IGMP Querier、组播 VLAN、快速离开（Fast Leave）、**QoS/DSCP 优先级队列**（Dante 音频 over IP 与 IPTV 都靠它不丢包不抖动）

### 怎么开发

开口就问「IPTV 卡不卡？是不是组播没配好，全楼在泛洪？」；若是 Dante / 音频 over IP 场景，改问「音频有没有出现过断续或丢包？」——Dante 对组播和 QoS 极敏感，说中就是内行

### 风险点

组播出问题是满屏花屏，客户零容忍；必须先小规模（一个楼层）验证再铺开；要确认他的组播源和播放器兼容性

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第4批.json`。

- **业务定位**：穆尔西亚本地电信运营商（原 MikroTik 顾问团队升级）：FTTH 居民宽带 + 企业专线/VPN/安全 + 面向其他运营商的连接服务。
- **产品线与在售品牌**：自有接入网（FTTH）与移动转售套餐 + 企业网解决方案；设备自用并随企业项目外配。
- **目标行业与场景**：穆尔西亚本地家庭/企业、园区多站点企业、运营商间批发链路；FTTH 分光节点与企业机房的接入层。
- **团队与规模**：组织化运营商班底（客服/工程），2 位 9–10 证顾问（Carlos Cárdenas + Javier）坐镇技术。
- **决策链与对接人**：工程侧 Carlos Cardenas Cebrian（+34 622 330 440 / ccardenas@celenet.es）；商务走 856 005 555 / info@celenet.es。
- **技术与认证**：双顾问 9–10 证含 MTCSWE/组播/BGP/MPLS（CSV 名录记录）——骨干与接入都懂。
- **采购与供应链信号**：运营商级持续采购：FTTH 节点、企业项目接入层、机房配套——量级比纯顾问高一个台阶。
- **近期动态与线索**：品牌化升级完成（新站 celenet-conecta 主题），正在扩张覆盖与企业线——网络建设期=设备评估期。
- **与我方契合点**：FTTH 节点与机房接入=24 口/10G；企业项目交付=管理型统一模板；组播专长=IPTV 方案的 IGMP 优化可以聊透。
- **风险与注意**：运营商谈供应商要稳定供货与 RMA 承诺：首轮就带交期/RMA 政策，不只报价格。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**官网抬头已明确「电信运营商」身份——公司从集成商扩展成了持牌运营商。
  > Operador de telecomunicaciones · Fibra, móvil y redes para llegar más lejos. · Conectividad para hogares, empresas y operadores.
  > 来源：https://celenet.es/
- **【产品线与在售品牌】**居民线卖 FTTH+移动套餐；企业线卖光纤、专线备份、VPN 与网络安全——另有「operadores」批发方向。
  > Fibra óptica FTTH · Tarifas móviles · Fibra y móvil en un mismo paquete · Fibra e internet para empresas · Enlaces dedicados y respaldo · VPN, redes y ciberseguridad.
  > 来源：https://celenet.es/
- **【团队与规模】**官网统一触点：856 005 555 / info@celenet.es，按区覆盖查询制销售，组织化程度比以往个体顾问时期高。
  > 856 005 555 · info@celenet.es · Cobertura real — Indícanos dónde necesitas el servicio y confirmaremos las opciones disponibles.
  > 来源：https://celenet.es/
- **【技术与认证】**公司内 2 位顾问均 9–10 证（含 MTCSWE）；Carlos 专长含组播 Multicast 与高可用/流量工程（来源性质：CSV 既有记录）。
  > 公司内 2 位顾问，均 9–10 证。Carlos：WISP、OSPF/BGP/MPLS、IPv6 规划、组播 Multicast、高可用…（CSV 备注）
  > 来源：https://mikrotik.com/consultants

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（企业项目接入层）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他企业线做 VPN/安全/多站点：接入层 24 口 PoE++ + 4×10G 上行作为交付标配，企业客户一次到位。
- **要问的问题**：企业项目的接入交换机现在标准化在什么型号？
- **随附证明**：规格对照 + 交期/RMA 政策说明（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（FTTH 节点/外线箱）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：FTTH 分光节点与室外箱体：宽温 DIN 免配置 + 2.5G SFP 上行，给建设期的外线段补件。
- **要问的问题**：外线节点箱里的供电与交换现在用什么？
- **随附证明**：宽温报告 + DIN 图 + 节点备件包价。

### 第 3 次跟进 · 管理型 PoE（接入层模板+IPTV 组播）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他的组播/高可用专长：管理型 VLAN 分段 + IGMP 优化 + ERPS 环，做接入层统一模板，企业项目批量复制。
- **要问的问题**：企业接入层有没有做 ERPS 或组播优化的需求清单？
- **随附证明**：VLAN/IGMP/ERPS 模板 + 收敛实测（英文）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：IGMP / multicast behaviour on your IPTV builds

```text
Hi Celenet,

Multicast is where most IPTV and camera builds quietly fall over, and it is the part I specialise in on the access switch.

What caught my eye is that you work on multicast, WISP, VLAN and CAPsMAN.

Where we may be useful: IGMP snooping v2/v3, a querier so the VLAN stops flooding, multicast VLAN, fast leave, and DSCP/QoS queues — the things that decide whether IPTV is watchable and whether Dante audio drops out.

Are you running IGMP snooping plus a querier, or still flooding the VLAN?

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
