# Yvan Laverdiere

> **评级 A**　|　加拿大 · Rouyn-Noranda, QC　|　档案编号 `A-011`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、PoE/监控/门禁），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Yvan Laverdiere |
| 国家 | 加拿大 |
| 城市 | Rouyn-Noranda, QC |
| 网站 | cegepat.qc.ca |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCINE+MTCSWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424DGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★ 持 **MTCSWE**；技能含 **VXLAN、VLAN**、RADIUS、MPLS/VPLS/VRF、IPSec/GRE/EoIP/IPIP、PPPoE、Hotspot、网络监控、Proxmox 集成；**任职于教育系统（cegepat.qc.ca 魁北克 CEGEP 学院）→ 校园网场景**；英法双语 |

## 三、人员与联系方式

- **邮箱**：yvan.laverdiere@cegepat.qc.ca
- **电话**：819-763-1411
- **原始联系字段**：819-763-1411 / yvan.laverdiere@cegepat.qc.ca

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCINE、MTCSWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCINE` — ISP 互联
- `MTCSWE` — **交换**（最能说明他卖交换机）

**涉及品牌 / 技术**：IPsec、MikroTik、Proxmox

## 五、跟进策略

**场景判断**：PoE / 监控 / 门禁

### 推什么型号

**STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）**

> 系统初判型号：`STC-424DGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

802.3bt 单口 90W、**PoE 看门狗（摄像头死机自动断电重启，省一趟上门）**、250m 延长供电、端口隔离、整机功率预算足

### 怎么开发

替他算一笔账：24 个 4K 头全开要多少瓦、满配后还剩多少余量——这是每个做监控的人都踩过的坑，算清楚就赢一半

### 风险点

**PoE 功率预算和供电稳定性是验收红线**，虚标功率会当场翻车；必须送测、必须给整机功率实测数；部分非标 PoE 相机存在兼容性问题，要先拿他的机型测

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。

- **业务定位**：魁北克 Cégep de l'Abitibi-Témiscamingue（3 校区）的网络技术人员/工程师，MikroTik 认证顾问。
- **产品线与在售品牌**：未公开品牌清单；技术面覆盖 VXLAN/VLAN、RADIUS、MPLS/VPLS/VRF、IPSec/GRE/EoIP、PPPoE、Hotspot、网络监控与 Proxmox 集成。
- **目标行业与场景**：校园网（CEGEP）：多校区互联、学生/教工分段、实验楼与体育设施、监控与门禁；另参与 Hotspot/PPPoE（宿舍）类需求。
- **团队与规模**：公共教育机构内部 IT（3 校区、22 个专业、Rouyn-Noranda / Val-d'Or / Amos）。
- **决策链与对接人**：yvan.laverdiere@cegepat.qc.ca；819-763-1411；英法双语。
- **技术与认证**：MTCNA+MTCRE+MTCWE+MTCINE+**MTCSWE**（交换）；VXLAN/VLAN、MPLS/VPLS/VRF 等进阶技能。
- **采购与供应链信号**：公立机构采购：走招标/年框，技术规格由他这类人写；一旦进入规格，后续几年都会带型号。
- **近期动态与线索**：学院官网 2026 年正常运营（招生、3 校区、22 专业），IT 项目随校区改造推进（本轮未取得具体网络项目公告）。
- **与我方契合点**：校园接入层是 24 口 PoE 的标准场景（教室 AP、走道摄像头、门禁）；实验楼/体育场需要工业款；多校区互联需要 ERPS/VLAN 分段与 10G 上行。
- **风险与注意**：周期长、招标流程重；不要催单，走「技术交流 + 写规格 + 试点」三步。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【目标行业与场景】**学院官网：3 校区 22 个专业，多校区运行。
  > 3 campus … 12 équipes sportives … 22 programmes d'études；Campus de Rouyn-Noranda｜Campus de Val-d'Or｜Campus d'Amos
  > 来源：https://www.cegepat.qc.ca/
- **【技术与认证】**既有记录：持 MTCSWE 与多项进阶网络技能，任职教育系统。
  > 持 MTCSWE；技能含 VXLAN、VLAN、RADIUS、MPLS/VPLS/VRF、IPSec/GRE/EoIP/IPIP、PPPoE、Hotspot、网络监控、Proxmox 集成；任职于 cegepat.qc.ca
  > 来源：https://mikrotik.com/consultants

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：校园接入层：教室/走廊 AP + 摄像头 + 门禁集中到一台 24 口 PoE++，配看门狗与端口隔离，减少寒暑假窗口期的上门。
- **要问的问题**：他们校区接入层现在的 PoE 口数与功率预算是多少、卡在哪里？
- **随附证明**：规格与功率表（法语/英语版）+ 测试机（假期窗口测试）。

### 第 2 次跟进 · 工业级非管理 PoE（实验楼/体育设施）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：实验楼、机械车间、体育场看台：非机房环境、温差大，工业款免配置进电箱。
- **要问的问题**：哪些点位没有空调机柜、但需要 PoE 接入？
- **随附证明**：宽温报告 + DIN 图 + 法语安装说明。

### 第 3 次跟进 · 管理型 PoE（多校区冗余）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：他会 VXLAN/MPLS/VPLS：谈 10G 上行 + ERPS 环网 + VLAN 分段（学生/教工/设备/摄像头四段）的落地清单。
- **要问的问题**：多校区互联的接入层冗余与 10G 上行，他们现网怎么做的？
- **随附证明**：ERPS 实测 + VLAN 分段模板 + 招标参数条目（法/英）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：PoE budget question on your camera jobs

```text
Hi Yvan,

I work on PoE access switches, and your CCTV / access control work is exactly the use case I keep running into.

What caught my eye is that you work on VXLAN, VLAN, RADIUS and IPsec.

Where we may be useful: 24 gigabit PoE++ ports at up to 90 W each, 4×10G uplink, per-port power budget you can actually plan against, PoE watchdog that power-cycles a hung camera instead of sending a truck.

How many cameras per job, and what wattage per port are you designing to?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424DGGPM-440W evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
