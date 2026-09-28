# Martin Pina

> **评级 A**　|　捷克 · Olomouc　|　档案编号 `A-043`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Martin Pina |
| 国家 | 捷克 |
| 城市 | Olomouc |
| 网站 | hanacke.net |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCINE+MTCIPv6E+MTCSE+MTCSWE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 持 MTCSWE（交换）+ MTCINE（ISP 互联）；自述含 switching、高可用、网络监控与安全、远程运维 |

## 三、人员与联系方式

- **邮箱**：martin.pina@hanacke.net
- **电话**：+420 732 712 317
- **原始联系字段**：+420 732 712 317 / martin.pina@hanacke.net

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCINE、MTCIPv6E、MTCSE、MTCSWE

- `MTCNA` — 网络助理（入门）
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第3批.json`。

- **业务定位**：Olomouc 一人运营商+顾问：自有小 ISP（hanácké.net s.r.o.），做网络设计/运维/托管，持 MTCINE+MTCSWE 级证书并教 MikroTik 课。
- **产品线与在售品牌**：无分销目录；自用设备随站点与项目采购，MikroTik 栈为主。
- **目标行业与场景**：本地企业/居民接入、小企业组网与托管运维，远程运维工单制。
- **团队与规模**：一人公司（官方登记无雇员），专业口碑极佳（公开评价「最好的网工之一」）。
- **决策链与对接人**：Martin Pína 本人（+420 732 712 317 / martin.pina@hanacke.net），决策=本人当天。
- **技术与认证**：MTCNA+MTCINE+MTCIPv6E+MTCSE+MTCSWE（来源：CSV 既有 MikroTik 名录记录）；教授 MikroTik（第三方评价佐证）。
- **采购与供应链信号**：小而精：按站点/工单按需购买，重视设备可靠性与可远程管理；价格敏感但更看重省事。
- **近期动态与线索**：官网 hanacke.net 本轮抓取 HTTP 500（2026-09-28）——线上门面处于故障状态；联系走邮箱/电话。
- **与我方契合点**：他的接入点/塔站、企业组网项目都要交换机；他讲课——样机可进他的演示环境。
- **风险与注意**：单人专家决策：不要营销腔，直接给规格表与实测数据；官网抓取异常的事不要在邮件里提。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**hanácké.net 是他自己的本地 ISP 兼网络设计公司，自述提供上网接入并做网络设计与运维。
  > Poskytuji připojení k internetu. Provádím návrhy a správy sítí.
  > 来源：https://www.firmy.cz/detail/12764049-martin-pina-olomouc-nova-ulice.html
- **【技术与认证】**公开评价称他属捷克最好的网络工程师之列、教授 MikroTik 课程、自己的网络是样板（第三方评价原文）。
  > Pan Pina patří mezi nejlepší síťaře, školí MikroTiky, jeho síť je příkladem pro ostatní.
  > 来源：https://www.firmy.cz/detail/12764049-martin-pina-olomouc-nova-ulice.html
- **【决策链与对接人】**公司注册信息显示 hanácké.net s.r.o. 的唯一股东兼执行董事即 Bc. MARTIN PÍNA，自 2015-07-14 起 100% 持股——决策=本人。
  > Jednatel — Bc. MARTIN PÍNA Olomouc… Podíl: 100.00 %
  > 来源：https://rejstrik-firem.kurzy.cz/04241959/hanacke-net-sro/
- **【团队与规模】**第三方企业库登记为无雇员个体运营（Počet zaměstnanců: bez zaměstnanců），服务含互联网接入、组网设计、服务器托管与主机服务；官网 hanacke.net 本轮抓取 HTTP 500（如实标注）。
  > Služby: - poskytovatel internetu - návrh a správa sítě - provozování serverů - hosting.
  > 来源：https://www.edb.cz/firma-1000296-martin-pina-olomouc/kontakt

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 PoE++（小而多的接入点位）

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他的客户/塔站/宿舍式物业需要偶尔一次到位的 24 口 PoE++：直接给规格-价格对照，写清与 CRS328 的差异。
- **要问的问题**：你现在接入层 24 口 PoE 用什么型号、库存备机几台？
- **随附证明**：英文规格对照页 + 功率实测表。

### 第 2 次跟进 · 工业非管理 PoE（室外/弱电间）

- **推什么**：LT-IS6310G-2GX8GT PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：乡村塔站与弱电间点位：宽温、DIN、免配置，替他减少冬夏故障上门次数——一人运维最值钱的就是少跑。
- **要问的问题**：室外点位一年换机几次、上门路程多久？
- **随附证明**：宽温报告 + DIN 安装图 + 一台测试机寄 Olomouc。

### 第 3 次跟进 · 管理型进他的样板网络与课程

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他教 MikroTik 课、自己的网络是样板：让设备进他的参照拓扑——VLAN 分段 + ERPS + 10G 上行，学员即潜在客户。
- **要问的问题**：你的样板拓扑里缺不缺一台能演示 ERPS 的设备？
- **随附证明**：VLAN/ERPS 收敛实测 + 教学案例页。

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
Hi Martin,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on switching.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328XGP-4XS24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
