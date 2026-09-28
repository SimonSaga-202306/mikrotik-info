# Michael Schmidt IT GmbH

> **评级 A**　|　德国 · Spardorf　|　档案编号 `A-166`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：【人工定级】A —— 自动规则已跳过；人工指定
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Michael Schmidt IT GmbH |
| 国家 | 德国 |
| 城市 | Spardorf |
| 网站 | https://www.msit-gmbh.de |
| 类型 | 集成商/代理（Allied Telesis） |
| 反向信号 | Allied Telesis（Marvell Prestera 接入层） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | Marvell Prestera 接入层切入 |
| 数据来源 | Allied Telesis 官方伙伴定位器（?country=germany） |
| 原备注 | 伙伴等级：Resell。 【2026-09-27 联系方式核验】公开邮箱·一方/伙伴来源。官网明确列出；Spardorf，企业网络及 IT 安全服务。 来源：[1](https://www.msit-gmbh.de/) [3](https://www.msit-gmbh.de/dokumentation/) |

## 三、人员与联系方式

- **邮箱**：info@msit-gmbh.de
- **电话**：—
- **原始联系字段**：info@msit-gmbh.de [Publicly listed; delivery not tested]; https://www.msit-gmbh.de

## 四、品牌与技术栈

**涉及品牌 / 技术**：（未记录）

## 五、跟进策略

场景信号不明确，先摸底：问清他接入层现在用谁的设备、痛点是供电、VLAN 还是环网，再定型号。

初判可参考型号：`STC-424XGGPM-440W（Saga）`

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第9批.json`。

- **业务定位**：埃尔朗根区系统屋（schmidt IT 品牌）：安全为纲的外包型 IT 服务，Allied Resell（CSV 记录）。
- **产品线与在售品牌**：安全/外包/虚拟化/ITK/云安全/微软栈支持；全天候监控自述。
- **目标行业与场景**：企业与⚠️公共机构（公共段划线只谈商业）。
- **团队与规模**：区域系统屋（Michael Schmidt 品牌）。
- **决策链与对接人**：info@msit-gmbh.de（CSV 9-27：官网明确列出，另有 dokumentation 页）。
- **技术与认证**：Allied Resell（CSV 记录）。
- **采购与供应链信号**：外包全托管逻辑=站点标准件批量；安全话术=分段与准入是舒适话题。
- **近期动态与线索**：2024 新版式上线，站活跃。
- **与我方契合点**：外包栈接入标准件+分段模板（NAC/VLAN 语境他很熟）。
- **风险与注意**：公共机构段划线；别把「数据主权」话题说破嘴——给合规材料包就好。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【业务定位】**官网：埃尔朗根-纽伦堡区系统屋——服务「企业与⚠️公共机构」的安全 IT（公共段划线）。
  > IT-Systemhaus für die Region Erlangen-Nürnberg — bieten wir Unternehmen und öffentlichen Einrichtungen innovative, sichere IT-Lösungen und erstklassigen Service.
  > 来源：https://www.msit-gmbh.de/
- **【产品线与在售品牌】**六大安全主题件：IT 安全/外包/虚拟化/ITK 通信/云安全/微软支持——病毒会讲到合规与数据主权。
  > IT-Sicherheit · IT-Outsourcing · IT-Virtualisierung · ITK-Kommunikation · Sichere IT-Cloud-Lösungen · Umfassender Microsoft Support…（含）Compliance und Datenhoheit（合规与数据主权）
  > 来源：https://www.msit-gmbh.de/
- **【采购与供应链信号】**外包=外部 IT 部模式：客户网由他全管——标准件采购频繁。
  > Als externe IT-Abteilung stellen wir die Sicherheit und Effizienz Ihrer IT-Systeme sicher.（外包页）
  > 来源：https://www.msit-gmbh.de/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（外包栈接入标准件）

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：外包站点标准件：24 口 PoE++ 单端口成本+质保+材料包（合规声明随附划公共段）。
- **要问的问题**：外包客户的接入层标准件现在什么型号？
- **随附证明**：单站 BOM 测算 + 合规材料包（德文）。

### 第 2 次跟进 · 工业级非管理 PoE（车间/库房点位）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：制造商业客户的车间/库房：宽温 DIN PoE。
- **要问的问题**：车间点位的坏机率？
- **随附证明**：宽温报告 + 备件包价（德文）。

### 第 3 次跟进 · 管理型 PoE（分段/准入标准件）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：安全语境：管理型（VLAN/ERPS/NAC 配合）分段件+配置基线。
- **要问的问题**：分段基线要不要进你们的方案库？
- **随附证明**：VLAN/ERPS/NAC 兼容说明 + 基线样例（德文）。

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
Hi Michael,

I build managed access switches (PoE and industrial) and your profile came up while I was looking at who is actually doing this work in your market.

What caught my eye is that you work on Resell, Spardorf and https.

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
