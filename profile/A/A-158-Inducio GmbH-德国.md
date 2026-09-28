# Inducio GmbH

> **评级 A**　|　德国 · Traunstein　|　档案编号 `A-158`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— 自动规则已跳过；人工指定
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Inducio GmbH |
| 国家 | 德国 |
| 城市 | Traunstein |
| 网站 | https://www.inducio-services.net |
| 类型 | 集成商/代理（Allied Telesis） |
| 反向信号 | Allied Telesis（Marvell Prestera 接入层） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | Marvell Prestera 接入层切入 |
| 数据来源 | Allied Telesis 官方伙伴定位器（?country=germany） |
| 原备注 | 伙伴等级：Resell。 【2026-09-27 联系方式核验】公开邮箱·一方/伙伴来源。企业联系与 Impressum 页面公开，Traunstein；负责人 Siegmund Gromotka。 来源：[2](https://www.inducio-services.net/kontakt/) [3](https://inducio-services.net/en/impressum) |

## 三、人员与联系方式

- **邮箱**：info@inducio.de
- **电话**：—
- **原始联系字段**：info@inducio.de [Publicly listed; delivery not tested]; https://www.inducio-services.net

## 四、品牌与技术栈

**涉及品牌 / 技术**：（未记录）

## 五、跟进策略

场景信号不明确，先摸底：问清他接入层现在用谁的设备、痛点是供电、VLAN 还是环网，再定型号。

初判可参考型号：`STC-424XGGPM-440W（Saga）`

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第8批.json`。

- **业务定位**：巴伐利亚 Traunstein 的 NOC/监控 MSP：COD 厂商无关监控+NAC+漏洞/威胁监测 24/7，Allied Resell（伙伴墙+CSV 记录）。
- **产品线与在售品牌**：监控/NAC/安全检查/威胁监测托管；分销通路 Ingram/TD SYNNEX。
- **目标行业与场景**：KRITIS 运营商（划线）、机械制造、高中型企业的稳定与安全运营。
- **团队与规模**：约 25 人专家队（官网口径），30+ 技术伙伴。
- **决策链与对接人**：info@inducio.de；负责人 Siegmund Gromotka（CSV 9-27：联系/Impressum 公开）。
- **技术与认证**：Allied Resell（CSV+伙伴墙）；COD/NAC 体系（官网）。
- **采购与供应链信号**：托管栈进货走分销（Ingram/TD Synnex 在墙）：要么有能力跟分销并价，要么走「项目第二来源注册」绕开比价；SNMP/MIB 完备性是他的技术门槛。
- **近期动态与线索**：英文页新上线=在拓客（2026 版式）。
- **与我方契合点**：制造的/中型企业客户的接入层标准件：全 MIB/ERPS 配 COD 监控、NAC 动态 VLAN 兼容清单——技术评估先行。
- **风险与注意**：KRITIS 客户段不供（首封声明）；他懂监控协议细节——MIB 库/固件路线一次给全，别被问倒。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**官网（EN 页）：2010 年起的安全基设运营专家——NOC/监控/安全方案三件主业，约 25 人团队。
  > Since 2010, we have been helping companies operate complex IT infrastructures in a stable, transparent, and secure manner—with a focus on network operations (NOC), monitoring, and smart security solutions. ‖ a team of around 25 specialists
  > 来源：https://inducio-services.net/en
- **【目标行业与场景】**⚠️ 客户层：「从 KRITIS 运营商到机械制造与中型企业」——KRITIS 段划线，制造/中型企业段是正路。
  > we serve customers ranging from KRITIS operators to mechanical engineering companies and medium-sized enterprises with high requirements for availability and security.
  > 来源：https://inducio-services.net/en
- **【技术与认证】**核心栈 COD 平台（extocode 厂商无关监控）+NAC（基于 MAC 认证/动态 VLAN）——管理型交换是他的监控对象，SNMP 兼容是硬门槛；伙伴墙：Allied Telesis/HPE/Cisco/Fortinet/Huawei/Ingram/TD Synnex 等 30+。
  > Central Operations Dashboard (COD)… a manufacturer-independent platform that combines monitoring, network topologies, automated configuration backups, network access control (NAC), and firewall management ‖ Network access is controlled via NAC (e.g., MAC-based authentication, dynamic VLAN assignment)（伙伴墙 Logo 含 Allied Telesis · Cisco · HPE · Fortinet · Huawei · Ingram Micro · TD Synnex · RIPE · Greenbone · Nakivo）
  > 来源：https://inducio-services.net/en
- **【产品线与在售品牌】**服务四件：NOC 与基设监控（从可用性到 SNMP 全监）/资产+NAC/IT 安全检查（漏洞扫描）/网络安全监控（威胁情报）。
  > NOC & Infrastructure Monitoring — from simple availability checks to detailed SNMP monitoring ‖ Asset Management + Network Access Control ‖ IT security checks — regular vulnerability scans ‖ Network Security Monitoring — threat intelligence integration
  > 来源：https://inducio-services.net/en

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（监控兼容的接入标准件）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：贴他 COD 监控：24 口接入层全 SNMP MIB/ERPS，先过技术评估；KRITIS 客户段不供声明随附。
- **要问的问题**：制造/中型企业客户的接入层标准件要不要进 COD 评估？（KRITIS 段不供）
- **随附证明**：MIB 库 + 兼容清单 + 边界声明（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（机械制造客户车间段）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：机械制造客户的车间/室外点位：宽温 DIN PoE 减现场工单——正好扣他 24/7 运维成本线。
- **要问的问题**：车间/室外点位的工单量一年多少？
- **随附证明**：宽温报告 + 坏机工单测算（德文）。

### 第 3 次跟进 · 管理型 PoE（NAC 动态 VLAN 兼容验证）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：管理型接入件的 NAC（MAC 认证/动态 VLAN）兼容验证+分段模板——过了他这关就是标准件。
- **要问的问题**：NAC 动态 VLAN 全流程要不要对一遍？
- **随附证明**：NAC 兼容验证记录 + VLAN/ERPS 模板 + 样机（德文）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：Access switching — quick question

```text
Hi Inducio,

I build managed access switches (PoE and industrial) and your profile came up while I was looking at who is actually doing this work in your market.

What caught my eye is that you work on Resell, Impressum and Traunstein.

Where we may be useful: L3 hardware offload so forwarding does not eat the CPU, QinQ and VLAN translation/rewrite, ERPS and MSTP, full CLI plus SSH plus SNMP with a private MIB.

What are you using for access layer today, and where does it hurt?

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
