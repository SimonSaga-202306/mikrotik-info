# Alessandro Del Ferro / Bitmagic

> **评级 A**　|　意大利 · Pesaro　|　档案编号 `A-035`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Bitmagic |
| 国家 | 意大利 |
| 城市 | Pesaro |
| 网站 | bitmagic.it |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 8 证（含 MTCSWE+MTCEWE） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | 持 MTCSWE（交换）+ MTCEWE（企业无线）+ MTCTCE（流量控制） |

## 三、人员与联系方式

- **对接人**：Alessandro Del Ferro
- **邮箱**：mikrotik_consultant@bitmagic.it
- **电话**：+39 339 651 8864
- **原始联系字段**：+39 339 651 8864 / mikrotik_consultant@bitmagic.it

## 四、品牌与技术栈

**持有认证**：MTCSWE、MTCEWE

- `MTCSWE` — **交换**（最能说明他卖交换机）
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：MTCSWE 交换认证

### 推什么型号

**STC-424XGGPM-440W（Saga）（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`STC-424XGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

他持有 MTCSWE（MikroTik 交换认证），交换是正式专长——**不用给他做科普**。开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」直接给 CLI 命令对比和转发实测数据

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全；含糊其辞会立刻失去这类技术型客户的信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第2批.json`。

- **业务定位**：佩萨罗的网络顾问/集成个体（Bitmagic，Alessandro Del Ferro）：MikroTik 生态的项目实施与顾问。
- **产品线与在售品牌**：未取得（官网本轮为「Sito in costruzione」占位页）；按 CSV 记录其认证结构属 MikroTik 生态。
- **目标行业与场景**：按既有记录为中小型网络项目与顾问服务（站点重建中）。
- **团队与规模**：个人/极小型，决策链 = 本人。
- **决策链与对接人**：mikrotik_consultant@bitmagic.it；+39 339 651 8864。
- **技术与认证**：MikroTik 认证顾问 8 证，含 **MTCSWE（交换）+ MTCEWE（企业无线）+ MTCTCE（流量控制）**——交换是正式专长。
- **采购与供应链信号**：按项目采购；以技术参数为主要判据（MTCSWE 背景）。
- **近期动态与线索**：bitmagic.it 本轮实测为「Sito in costruzione」（建设中）占位页 → 站点改版中，业务内容暂不可见；首次联系时顺带确认。
- **与我方契合点**：MTCSWE 专长：可直接谈 VLAN/QoS/环网与转发实测；24 口 PoE 与工业款都有明确落点。
- **风险与注意**：公开信息少（仅名录 + 建设中的站点）→ 首封邮件以技术内容破冰，先建立信任不催单。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【近期动态与线索】**bitmagic.it 为建设中占位页（无业务内容）。
  > Sito in costruzione（bitmagic.it 首页）
  > 来源：https://www.bitmagic.it/
- **【技术与认证】**既有记录：8 证含交换与企业无线、流量控制专项。
  > 持 MTCSWE（交换）+ MTCEWE（企业无线）+ MTCTCE（流量控制）（CSV 备注）
  > 来源：https://www.bitmagic.it/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：他持 MTCSWE：直接给硬货（整机功率曲线、VLAN 上限、看门狗、端口隔离），请他自测后给结论。
- **要问的问题**：他近期项目的接入层规格（口数/功率/上行）通常怎么定？
- **随附证明**：完整规格 + 实测数据 + 30 天测试机。

### 第 2 次跟进 · 工业级非管理 PoE（现场点位）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：现场电箱/室外点位：宽温宽压、DIN、免配置；他的项目里非机房点位用得上。
- **要问的问题**：有没有需要装进电箱/室外的接入点？
- **随附证明**：宽温报告 + DIN 图 + 样品价。

### 第 3 次跟进 · 管理型 PoE（QoS/环网）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他持 MTCTCE（流量控制）：给 QoS/队列与 ERPS 的实测与模板，对上他的专长。
- **要问的问题**：他项目里 QoS 与环网冗余的需求多不多？
- **随附证明**：QoS 模板 + ERPS 实测 + MIB 清单。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：Switching question for an MTCSWE holder

```text
Hi Alessandro,

You hold MTCSWE, so switching is a declared specialism rather than a side task — that is who I want to talk to.

What caught my eye is that you work on MTCSWE, MTCEWE and MTCTCE.

Where we may be useful: L3 hardware offload (line-rate forwarding off the CPU), QinQ and VLAN translation, ERPS and MSTP, ACLs and static routing, full CLI plus SSH plus SNMP with a private MIB.

What are you using for L2 redundancy today, and does it need ERPS-class convergence?

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
