# Amir Seifi / Magenta Networks

> **评级 A**　|　加拿大 · Scarborough, ON　|　档案编号 `A-006`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Magenta Networks |
| 国家 | 加拿大 |
| 城市 | Scarborough, ON |
| 网站 | magentanetworks.net |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCUME+MTCINE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328GP-4GX24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 精通 RouterOS 与 **SwitchOS**；核心能力明确包含「**二层交换、VLAN 配置、链路聚合、端口优化管理**」；另有高级路由 OSPF/BGP、防火墙加固、DDoS 缓解、定制脚本与自动化 |

## 三、人员与联系方式

- **对接人**：Amir Seifi
- **邮箱**：support@magentanetworks.net
- **电话**：+1-647-812-5170
- **原始联系字段**：+1-647-812-5170 / support@magentanetworks.net

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCTCE、MTCUME、MTCINE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCTCE` — 流量控制
- `MTCUME` — 用户管理（Hotspot / PPPoE）
- `MTCINE` — ISP 互联

**涉及品牌 / 技术**：MikroTik、RouterOS、SwitchOS

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

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。

- **业务定位**：多伦多的托管 IT 服务商（Magenta Networks Inc.）：网络管理、Helpdesk、咨询、网络安全、备份与恢复、云服务。
- **产品线与在售品牌**：未公开品牌清单；自述精通 RouterOS 与 **SwitchOS**，能力含二层交换、VLAN 配置、链路聚合、端口优化管理，以及 OSPF/BGP、防火墙加固、DDoS 缓解、脚本自动化。
- **目标行业与场景**：官网列出服务行业：中小企业、零售、医疗、制造、酒店、金融；公开运营数据：19 个在管站点、5 个在建项目、310 个端点。
- **团队与规模**：小型 MSP 团队（19 站点/310 端点规模），决策链短（老板/技术负责人即决策人）。
- **决策链与对接人**：Amir Seifi；support@magentanetworks.net / info@ / ops@magentanetworks.net；+1-647-812-5170；周一至周五 9–18，周末预约。
- **技术与认证**：MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCUME+MTCINE；技能覆盖交换、路由、用户管理（Hotspot/PPPoE）。
- **采购与供应链信号**：MSP 模式：设备进他的资产池随客户站点部署；关注「到货快、可远程管理、故障率低」。
- **近期动态与线索**：官网（.ca 域名，CSV 记为 .net）2026 年仍在更新：新增「运营快照」指标区（19 站点/5 项目/310 端点）与服务行业页。
- **与我方契合点**：19 个站点 + 310 端点说明他反复在做同样的接入层：24 口 PoE 喂 AP/摄像头、VLAN 分客户、环网保稳定。我们的看门狗与远程重启正好降低 MSP 上门成本。
- **风险与注意**：硬件采购可能走现有分销渠道；要用「同规格更快到货 + 可远程管理 + 试点价」切入，别只谈单价。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【目标行业与场景】**官网公开运营指标与行业清单（19 站点 / 5 在建 / 310 端点）。
  > 19 Active sites；5 ongoing projects；310 endpoints；Industries we serve: SMBs｜Retail｜Healthcare｜Manufacturing｜Hospitality｜Financial Industry
  > 来源：https://magentanetworks.ca/
- **【业务定位】**服务目录：网络管理、Helpdesk、咨询、网络安全、备份与恢复、云服务。
  > Our services … Network Management｜Helpdesk Services｜Consulting Services｜Cybersecurity Solutions｜Backup & Recovery｜Cloud Services
  > 来源：https://magentanetworks.ca/
- **【决策链与对接人】**官网联系页给出销售/运维两条直达邮箱与客服电话。
  > Customer Service & Sales: +1-647-812-5170；General Inquiries: info@magentanetworks.net；Operations & Sales: ops@magentanetworks.net
  > 来源：https://magentanetworks.ca/contact/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：按 MSP 账本谈：19 个站点里，每减少一次上门就省一笔。24 口 PoE++ + 看门狗 + 远程重启/批量升级，直接摊到他的服务成本里。
- **要问的问题**：他管 19 个站点，每个月因为接入交换/AP 上门几次？
- **随附证明**：远程管理演示（SNMP/看门狗日志）+ 30 天试点机。

### 第 2 次跟进 · 工业级非管理 PoE（制造/仓储客户现场）

- **推什么**：LT-IS6306G-2GX4GT PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：他的制造业与仓储客户现场条件差：宽温宽压 DIN 款，插上就用、坏了换机，不占他工程师的时间。
- **要问的问题**：制造业客户里有没有产线/仓库边上的网络点位？
- **随附证明**：宽温报告 + 一页现场安装图 + 备件政策。

### 第 3 次跟进 · 管理型 PoE（客户隔离与统一模板）

- **推什么**：LT-IS6312G-4GX8GT PoE 版（8G + 4×2.5G SFP）或 LT-S8328XGP-4XS24GT-S（24×PoE + 4×SFP+）
- **切入点**：19 个站点、多客户：VLAN 隔离 + 环网 + 统一配置模板，一套模板复制到所有客户，减少他团队的记忆负担。
- **要问的问题**：他希不希望所有站点的交换机用同一套配置模板交付？
- **随附证明**：配置模板 + ERPS 实测 + MIB/自动化脚本示例。

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
Hi Amir,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on VLAN and SwitchOS.

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
