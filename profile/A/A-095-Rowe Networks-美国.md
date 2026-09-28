# Rowe Networks

> **评级 A**　|　美国 · Ohio　|　档案编号 `A-095`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Rowe Networks |
| 国家 | 美国 |
| 城市 | Ohio |
| 网站 | — |
| 类型 | WISP 集成商/代理（Netonix） |
| 反向信号 | Netonix 授权渠道（WISP 接入层交换机） |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | WISP 接入层替换 |
| 数据来源 | Netonix 官方分销/代理名录 |
| 原备注 | 【2026-09-23 用户裁决·保留】Netonix 交换机采用 **Vitesse** 芯片，并非 Marvell，严格按「Marvell 接入层生态」标准属于圈外；用户 2026-09-23 明确「先这样吧，没必要删」，故本条保留。注意：对其**不能使用「同芯片」话术**（详见 Netonix_WISP替换矩阵_2026-09.md），切入点应放在交期、宽温、上行与价格上。 Netonix 代理商。 【2026-09-27 挖邮箱·待人工】Site 只有联络表单。具名：Joshua Rowe（Business Owner，ZoomInfo 收录）。可试 joshua@/josh@ 前缀或表单 |

## 三、人员与联系方式

- **邮箱**：—
- **电话**：1-614-410-3535
- **原始联系字段**：1-614-410-3535；⚠️ 无邮箱：rowewireless.com 仅表单｜Site 只有联络表单。具名：Joshua Rowe（Business Owner，ZoomInfo 收录）。可试 joshua@/josh@ 前缀或表单

## 四、品牌与技术栈

**涉及品牌 / 技术**：（未记录）

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

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第5批.json`。

- **业务定位**：俄亥俄东南乡镇 WISP/网络集成小公司（Netonix 渠道，CSV 记录）：雇员 11–50 人，线上店停摆中。
- **产品线与在售品牌**：Netonix WISP 交换与配套+无线宽带服务（CSV 记录）；店恢复前货架明细不可见。
- **目标行业与场景**：乡镇宽带与本地企业网络项目。
- **团队与规模**：11–50 人（ZoomInfo 聚合）；老板 Joshua Rowe 直接管事。
- **决策链与对接人**：1-614-410-3535；站有联络表单（CSV 记录；具名 Joshua Rowe）。
- **技术与认证**：Netonix 渠道（CSV 记录）；⚠️ 禁用同芯片话术（Vitesse，用户 2026-09-23 裁决注明）。
- **采购与供应链信号**：乡镇 WISP 按点位小批量；店停摆=电商渠道中断，更需要电话直供与灵活起订。
- **近期动态与线索**：线上店维护停摆——正是「供应商自己被动摇」的窗口，值得直接电话。
- **与我方契合点**：塔站/点位工业 PoE 与接入层 24 口：按第二货源报价，起订量给足弹性。
- **风险与注意**：乡镇小户价格最敏感：首封就报到岸价+质保；别指望表单回复，电话为主。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【近期动态与线索】**官网电商当前整站「店铺不可用（维护）」——在线货架停摆，恢复时间未知。
  > Store Unavailable — This store is currently unavailable due to maintenance. It should be available again shortly.
  > 来源：https://www.rowewireless.com/
- **【团队与规模】**工商聚合页：俄亥俄 Byesville 主街 338 号、11–50 名员工、Joshua Rowe 为 Business Owner。
  > Rowe Networks corporate office is located in 338 Main St, Byesville, Ohio, 43723, United States and has 11-50 employees. · Joshua Rowe — Business Owner
  > 来源：https://www.zoominfo.com/pic/rowe-networks/1132675586

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE（乡镇项目接入层）

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他店停摆期切入：直连报价 24 口 PoE++ 到岸价与现货交期，起订量随意。
- **要问的问题**：（电话）接入层现在拿货顺吗？要不要备一个第二货源？
- **随附证明**：到岸价目 + 交期说明 + 质保政策。

### 第 2 次跟进 · 工业级非管理 PoE（塔站/点位）

- **推什么**：LT-IS6310G-2GX8GT PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：乡镇 WISP 塔站冬季故障高发：宽温 DIN PoE 备件包，先卖一盒备着。
- **要问的问题**：塔站冬天坏机多吗？备件怎么放？
- **随附证明**：宽温报告 + 备件包价 + DIN 图。

### 第 3 次跟进 · 管理型 PoE（汇聚/分段）

- **推什么**：LT-IS6312XG-4XS8GT（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：汇聚 10G 与 VLAN 分离用户/管理网：给一套乡镇 WISP 标准模板。
- **要问的问题**：用户网和管理网现在隔离吗？上行够不够？
- **随附证明**：VLAN/ERPS 模板 + 10G 实测。

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
Hi Rowe,

You work in switching, so I will skip the introduction: the interesting part is L3 hardware offload and QinQ at access-layer pricing.

What caught my eye is that you work on WISP.

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
