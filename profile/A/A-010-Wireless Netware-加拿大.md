# Wireless Netware

> **评级 A**　|　加拿大 · Ontario　|　档案编号 `A-010`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Wireless Netware |
| 国家 | 加拿大 |
| 城市 | Ontario |
| 网站 | wirelessnetware.ca |
| 类型 | 分销（MikroTik 官方） |
| 反向信号 | MikroTik（Master+VAD） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-480XGGM（Saga） |
| 切入点 | 卖 MikroTik 但缺工业/ERPS/PoE++ → 用同价位工业线补他的产品缺口 |
| 数据来源 | 2026-09-22 |
| 原备注 | 同时是 MikroTik 认证顾问（Hani Rahrouh，647-477-0163 / hr@wirelessnetware.ca，8 证含 MTCSWE）；有顾问团队；简历明确写「**Switching：熟悉 RouterOS 7.xx 的全部新交换功能，例如 L3 硬件卸载**」→ 他懂硬件卸载，能直接谈芯片规格；同时精通 RouterOS 与 SwitchOS；路由 BGP/OSPF、无线 PtP/PtMP/Mesh、CAPsMAN、API 与系统集成 |

## 三、人员与联系方式

- **邮箱**：info@wirelessnetware.ca、hr@wirelessnetware.ca
- **电话**：+1 647 477 0163
- **原始联系字段**：+1 647 477 0163 / info@wirelessnetware.ca

## 四、品牌与技术栈

**涉及品牌 / 技术**：CAPsMAN、MikroTik、RouterOS、SwitchOS

## 五、跟进策略

**场景判断**：交换专长

### 推什么型号

**STC-424XGGPM-440W（Saga）（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`STI-480XGGM（Saga）`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

这类人不用科普，直接给 CLI 命令对比和转发/芯片实测数据；开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全，含糊其辞立刻失去信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。

- **业务定位**：加拿大第一家 MikroTik 认证培训中心 + 授权代理（Toronto 仓库发货、全境配送）+ 咨询与托管机房（MikroTik-powered co-location）。
- **产品线与在售品牌**：MikroTik 全线现货（routers、**switches**、无线 AP、SFP 模块、配件，IC 认证）；另有 **SYNOXX** 光模块（SFP/SFP+/QSFP28/QSFP-DD）与自有品牌网络配件。
- **目标行业与场景**：ISP/运营商、企业、网络运营商客户：从中小企业到多站点 ISP 网络；培训覆盖官方认证课程与定制工作坊。
- **团队与规模**：小团队但角色多重（培训+分销+咨询+机房）；负责人 Hani Rahrouh 本人有 8 项认证含 MTCSWE。
- **决策链与对接人**：Hani Rahrouh；hr@wirelessnetware.ca；info@wirelessnetware.ca；+1 647 477 0163；网店 shop.wirelessnetware.ca。
- **技术与认证**：RouterOS & SwitchOS 认证专家；加拿大首个 MikroTik 培训师；既有记录提及其熟悉 RouterOS 7.x 交换新特性与 **L3 硬件卸载**。
- **采购与供应链信号**：他本身就是渠道（授权代理+现货仓库）：我们要以「OEM/补充线」而不是「找经销商」的身份谈；他的 SYNOXX 光模块业务说明他能接受非 MikroTik 体系的配件。
- **近期动态与线索**：官网 2026 年更新：强调 IC 认证、Toronto 现货、SYNOXX 光模块、托管机房；答疑区（FAQ）明确「全系列现货、海岸到海岸配送」。
- **与我方契合点**：他既卖设备又培训、还做托管机房：24 口 PoE（企业/ISP 接入）、工业款（室外塔站/机箱）与光模块配套（他有 SYNOXX）三条线都能接；L3 卸载的细节对话他也接得住。
- **风险与注意**：官方代理身份意味着 MikroTik 是他的核心利益，不要谈「替代 MikroTik」；谈「补 MikroTik 没有的规格/价位的第二线」，并把光模块配套做成组合拳。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**官网定位：授权代理 + 加拿大首个 MikroTik 培训中心 + 咨询 + 托管机房。
  > Canada's First MikroTik Certified Trainer；Authorized Reseller；MikroTik Consulting in Canada — RouterOS & SwitchOS Experts；MikroTik-Powered Co-Location
  > 来源：https://www.wirelessnetware.ca/
- **【产品线与在售品牌】**全线现货 + SYNOXX 光模块。
  > stocking the full range of MikroTik routers, switches, wireless access points, SFP modules, and accessories. All products are IC Certified … Ships from Toronto Warehouse；SYNOXX SFP, SFP+, QSFP28, and QSFP-DD optical transceivers
  > 来源：https://www.wirelessnetware.ca/
- **【技术与认证】**既有记录：负责人持 8 证含 MTCSWE，熟悉 RouterOS 7 交换新特性（L3 硬件卸载）。
  > Hani Rahrouh … 8 证含 MTCSWE；简历明确写「Switching：熟悉 RouterOS 7.xx 的全部新交换功能，例如 L3 硬件卸载」
  > 来源：https://mikrotik.com/consultants

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他是渠道：用「加拿大现货仓库 + 与他现售 MikroTik 24 口 PoE 的规格/价位差」对话，把他当潜在分销商而不是终端客户。
- **要问的问题**：他愿意先上几个 SKU 试销（24 口 PoE 与工业 8 口），还是先做项目配套？
- **随附证明**：FOB/到岸价目表（含 IC 认证资料）+ 现货/交期说明 + 与 SYNOXX 光模块的组合清单。

### 第 2 次跟进 · 工业级非管理 PoE（ISP/塔站场景）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：他服务 ISP 与运营商：塔站/室外机箱用宽温 DIN 款，配他的光模块做长距离回传。
- **要问的问题**：ISP 客户的塔站/室外设备箱现在用什么型号、缺什么价位段？
- **随附证明**：宽温报告 + 光模块兼容清单 + 样品组合（交换机+SFP）。

### 第 3 次跟进 · 管理型 PoE + 培训合作

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）或 STC-448XGGM（Saga L3）（L3，PoE 版）
- **切入点**：他开课：把我们的管理型交换机做成培训实验与案例（L3 卸载/ERPS 实测），既是销售也是影响力。
- **要问的问题**：他愿不愿意在课程里加入一两个我们的实验案例？
- **随附证明**：可公开的实测数据 + 培训用配置模板 + 实验机（成本价）。

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
Hi Wireless,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on switching, L3, CAPsMAN and SwitchOS.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you running for L2 redundancy — STP/RSTP/MSTP, or ERPS?

If it is easier to judge from hardware than from a datasheet, I can send a STI-480XGGM evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
