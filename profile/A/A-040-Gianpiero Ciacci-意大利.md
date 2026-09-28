# Gianpiero Ciacci

> **评级 A**　|　意大利 · Siena　|　档案编号 `A-040`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Gianpiero Ciacci |
| 国家 | 意大利 |
| 城市 | Siena |
| 网站 | — |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCSE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328GP-4GX24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | WISP、OSPF、防火墙、动态路由、流量管理、带宽整形、**switching**、VPN |

## 三、人员与联系方式

- **邮箱**：gciacci@gmail.com
- **电话**：+39 338 248 7996
- **原始联系字段**：+39 338 248 7996 / gciacci@gmail.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCSE

- `MTCNA` — 网络助理（入门）
- `MTCSE` — 安全

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328GP-4GX24GT-S`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：锡耶纳的注册工程师（Ingegnere，1998 年取得资格）——**锡耶纳外国人大学（Università per Stranieri di Siena）IT 服务中心主任（2001 年起）**，同时做 LAN/WiFi/VPN 网络工程与信息安全顾问、计算机课程讲师。
- **产品线与在售品牌**：未公开品牌清单；专业方向为网络设计（LAN/WiFi/VPN）、数据库与信息安全。
- **目标行业与场景**：高校与公共机构网络（大学 IT 中心 + 多次担任公共采购项目的技术负责人 RUP）、企业 IT 安全顾问。
- **团队与规模**：个人身份（大学 IT 主任 + 顾问双轨），在机构采购里具技术决策影响力。
- **决策链与对接人**：gciacci@gmail.com；+39 338 248 7996；公开渠道另有大学邮箱 gianpiero.ciacci@unistrasi.it。
- **技术与认证**：MikroTik 认证顾问 MTCNA+MTCSE；自述专长含 **switching**、OSPF、动态路由、流量管理、带宽整形、VPN；大学讲师（IT Security 课程）。
- **采购与供应链信号**：公共机构采购：由他这类人写技术规格与担任 RUP（采购负责人）→ 一旦进入规格库，校园网络多年复购。
- **近期动态与线索**：公开可查：锡耶纳外国人大学 IT 服务中心主任（2001 起）、该校公开招标记录中任 RUP、曾任锡耶纳大学合同讲师；个人无公司站点。
- **与我方契合点**：校园接入层是 24 口 PoE 的标准场景（教室 AP、监控、门禁），机房外点位用工业款，多楼栋主干用管理型（VLAN 分段 + ERPS）；他是规格与采购的技术端。
- **风险与注意**：公共采购流程长、需合规文件；以「技术交流 + 参数入库 + 试点」节奏推进，不做价格催促。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**大学官方页面：IT 服务中心主任（2001 年起）、工程师背景、网络与安全方向。
  > Gianpiero Ciacci … laureato in Ingegneria Informatica nel 1998 … L'attività professionale si incentra sulla progettazione e realizzazione di basi di dati aziendali con interfaccia web, sulla progettazione ed allestimento di reti LAN, WiFi e VPN e sulla consulenza in ambito di sicurezza informatica. Presso l'Università per Stranieri di Siena ricopre il ruolo di Direttore del Centro Servizi Informatici dal 2001.
  > 来源：https://online.unistrasi.it/docenti/Persona.asp?ID=411&ID2=227
- **【采购与供应链信号】**公共采购文件显示其担任项目技术负责人（RUP）。
  > Dettaglio gara — Gara aggiudicata a "VITA BYTE s.n.c."! Tipo di appalto: Forniture — R.U.P.: Ing. Gianpiero Ciacci
  > 来源：https://unistrasi.traspare.com/announcements/235
- **【技术与认证】**既有记录：持 MTCNA+MTCSE，专长含 switching/OSPF/流量管理与 VPN。
  > MTCNA+MTCSE；专长含 switching、OSPF、动态路由、流量管理、带宽整形、VPN（CSV 备注）
  > 来源：https://mikrotik.com/consultants

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：以校园接入层为题做技术交流：教室 AP/监控/门禁一次喂满，PoE 看门狗与端口隔离；配合他把参数写进采购规格（他是 RUP）。
- **要问的问题**：他们校区接入层现在按什么规格采购 PoE 交换机？
- **随附证明**：规格参数页（中英）+ 实测数据 + 可写入标书的条目。

### 第 2 次跟进 · 工业级非管理 PoE（楼栋外/实验室）

- **推什么**：LT-IS6310G-2GX8GT PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：校园里非标准机房点位（实验楼、体育设施、室外）：宽温 DIN 免配置，直接进弱电箱。
- **要问的问题**：哪些点位没有空调机柜但需要 PoE 接入？
- **随附证明**：宽温报告 + DIN 安装图 + 一页选型对照。

### 第 3 次跟进 · 管理型 PoE（多楼栋冗余与分段）

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：多楼栋校园网：VLAN 分段（学生/教工/设备/监控）+ ERPS 环网 + 10G 上行，正好是他作为规格制定者关心的条目。
- **要问的问题**：校园主干与接入之间要不要做环网冗余？
- **随附证明**：ERPS 实测 + VLAN 模板 + 招标参数条目（双语）。

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
Hi Gianpiero,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on WISP and switching.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

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
