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

## 九、深度再发掘（R55：背景 · 芯片/型号 · 关键人 · 在意点 · SWOT · Saga 适配）

> 调研日期 **2026-09-28**；来源含官网/公开工商与社媒页面，原文摘录见本节后部；原始记录：`batch/A类深挖_2026-09-28_R55_第1批.json`。涉及我方价格均为 EXW 快照（15 天有效，报价前核价）。

- **背景深描**：**Wireless Netware Technology**，Markham ON（货从 Toronto 仓发，IC 认证库存），**2011 年创立**、LinkedIn 规模 2–10 人、388 粉。自我定位 **「Value-Added MikroTik Master Distributor」**+**加拿大首位 MikroTik 官方培训师**（2017-04 授牌）+MikroTik 动力托管机房。副业务：**Bell/Rogers 批发上网服务转售**、SYNOXX 光模块与 **Wirelessnetware 自主牌网络器材**（贴牌资产已存在！）。Facebook 同名在册。
- **芯片与在用型号**：全系 MikroTik（RouterOS/SwitchOS 专家，MTCNA/MTCRE 培训课程常态排期）；自有品牌光学件 SYNOXX（SFP/SFP+/QSFP28/QSFP-DD 全档）——**证明其已打通中国/亚洲 OEM 贴牌供应链（光模块贴牌→交换贴牌是自然延伸）**。出货量：未公开；「Full MikroTik Range In Stock」+Toronto 仓=现货分销体量。客户反馈：LinkedIn 推荐语（Sarah Kerr：业内最懂的人之一）；学员评价常态。
- **关键人KP**：**Hani Rahrouh**（President, CEO & MikroTik Coordinator；加拿大首位官方 MikroTik 培训师；LinkedIn /in/hani-rahrouh-38019521，5K 粉、周更：Markham Board of Trade 活动、培训课程预告）。邮箱 **info@wirelessnetware.ca**（公开）+ 电话 +1 647 477 0163；模式猜测 **hani@wirelessnetware.ca**（未验证；pattern=firstname@ 与其家族式命名相符需验证）。渠道角色决定：**他是买手+培训双身份，见面先谈分销梯价与贴牌 MOQ**。
- **关注点与资质**：①**IC/ISED 认证**（首页头牌「IC Certified Products」——⚠️ Saga 现证为 FCC/CE/UKCA 族，加拿大 IC 多为认可 FCC 报告或需补 ISED，**报价前必须核实 IC 适用性并在信中如实处理**，这是加拿大零售/培训教具的门槛）；②培训教具批量（MTCNA/MTCRE 班期稳定=教具箱规需求）；③光模块贴牌伙伴升级路径（SYNOXX 交换/工业交换贴牌）；④Bell/Rogers 批发线=ISP 级 VLAN/QinQ 语境（L2+ flow-based QinQ 可对）。社交：LinkedIn/Facebook 双活跃，本地商会（Markham Board of Trade）刷脸型。
- **优缺点SWOT**：**S**：Master Distributor+培训+机房三栖=**他想做大白牌分销的心理账户已开好**（SYNOXX 先例）；Toronto 本地仓=我们的货可直发其意仓；加拿大 MikroTik 教学垄断位。**W**：体量 2–10 人，大资金单承接力有限；MikroTik 官方关系是其核心资产，引入第二硬件品牌要过「不砸招牌」审查。**O**：**OEM 白牌交换机=他 SYNOXX 逻辑的自然延伸**（我们中性包装/贴客户型号的标准交付正好嵌合）；培训教具用 Saga=学员长期种草；Bell/Rogers 批发客户的接入层量。**T**：MikroTik 及其他亚洲白牌（已有深圳竞争者在加活动）；IC 认证若补齐不及时，零售端束手。
- **Saga产品适配**：①**贴牌分销位**：STC/STI 全系可谈 Wirelessnetware-branded 交换线（对标 SYNOXX 光学），起量谈「定制 branding available」条款；②**教具位**：**STC-424DGGPM-280W**（EXW $165，MTCNA 班 VLAN/PoE 实验）/**STC-424XGGM**（EXW $143，MTCRE 班）；③**ISP 语境**：L2+ QinQ/VLAN-Mapping（批发上网客户二层透传）；④工业白牌 STI-288GP/280GE（EXW $74.8/$63.8）。首封信结构：SYNOXX 致敬→交换贴牌延伸提案→教具样机 offer→IC 认证如实说明（FCC/CE 版+ISED 评估中）。

### 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Hani Rahrouh | President & CEO / MikroTik Coordinator（加拿大首位官方培训师） | info@wirelessnetware.ca；+1 647 477 0163 | 官网公开；LinkedIn 5K 粉周更（可双通道） | https://ca.linkedin.com/company/wireless-netware ・ https://wirelessnetware.ca/ |
| —（模式猜测） | — | hani@wirelessnetware.ca | 模式猜测 · 未验证（MX Google 已验） | dns://wirelessnetware.ca/MX 2026-09-28 本机核验 |

### R55 证据摘录

- **【定位】**加拿大授权 MikroTik 分销+Toronto 仓现货，IC 认证。
  > Wireless Netware Technology is Canada's authorized MikroTik reseller, stocking the full range … All products are IC Certified for Canadian use and ship from our Toronto warehouse
  > 来源：https://wirelessnetware.ca/
- **【背景】**2011 年成立、2–10 人、Markham，LinkedIn 在册。
  > Value-Added MikroTik Master Distributor … Company size: 2-10 employees … Headquarters: Markham, Ontario … Founded: 2011
  > 来源：https://ca.linkedin.com/company/wireless-netware
- **【特项】**培训 partner + Bell/Rogers 批发上网转售 + The Dude 顾问。
  > MikroTik Certified Trainer Partner, Bell Wholesale Internet Service, Rogers Wholesale Internet Service, MikroTik Consultant, and The-Dude Consultant
  > 来源：https://ca.linkedin.com/company/wireless-netware
- **【自有品牌】**已有 SYNOXX 光模块与 Wirelessnetware 牌器材=贴牌路径已通。
  > Looking for SYNOXX optical transceivers or Wirelessnetware-branded networking gear? We carry those too — all in one place.
  > 来源：https://wirelessnetware.ca/
- **【KP】**Hani Rahrouh 任 President/CEO/MikroTik Coordinator。
  > Hani Rahrouh President, CEO, and MikroTik Coordinator @ Wireless Netware Technology | MikroTik Certified Trainer
  > 来源：https://ca.linkedin.com/company/wireless-netware
- **【口碑】**同行推荐：业内最懂的人之一。
  > I've done Mikrotik training & collaboration with Hani. Hes one of the most knowledgeable people in the industry.
  > 来源：https://www.linkedin.com/in/hani-rahrouh-38019521/

## 十、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十一、首触邮件（可直接发送）

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

## 十二、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
