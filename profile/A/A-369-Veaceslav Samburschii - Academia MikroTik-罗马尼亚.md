# Veaceslav Samburschii / Academia MikroTik

> **评级 A**　|　罗马尼亚 · Brașov　|　档案编号 `A-369`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Academia MikroTik |
| 国家 | 罗马尼亚 |
| 城市 | Brașov |
| 网站 | academia-mikrotik.ro |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCUME+MTCINE+MTCSE+MTCSWE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 8 证含 MTCSWE（交换）+ MTCEWE（企业无线）；**经营罗马尼亚 MikroTik 学院 academia-mikrotik.ro（培训机构）** → 影响力型渠道：他讲什么设备，学员就用什么设备 【2026-09-27 A360–A378联络核验】来源等级：official-company。官方培训中心名录（罗马尼亚筛选）列Veaceslav Samburski / Academia Mikrotik Romania（Brasov, Romania）：电话+40 364086906、+40 748511932，邮箱office@academia-mikrotik.ro，站点academia-mikrotik.ro；所列证书8项含MTCSWE、MTCEWE（MTCNA、MTCRE、MTCWE、MTCUME、MTCINE、MTCSE、MTCSWE、MTCEWE），评分87%，与本行原备注一致。学院站cursuri页另给vsamburski@gmail.com与0748511932（次级入口）。CSV公司名写法“Samburschii”与名录“Samburski”拼写不同，仅备注，未改字段。 证据：[1](https://mikrotik.com/training/centers?region=Romania&category=training) [2](https://www.academia-mikrotik.ro/cursuri/) 仅覆盖所述联络/关联事实，不证明投递、在职、采购权、芯片或需求；批次：batch/contact_research_2026-09-27_A360-A378.json#A-369 |

## 三、人员与联系方式

- **对接人**：Veaceslav Samburschii
- **邮箱**：vsamburski@gmail.com、office@academia-mikrotik.ro
- **电话**：+40 748 511 932、+40 364 086 906
- **原始联系字段**：+40 748 511 932 / vsamburski@gmail.com；office@academia-mikrotik.ro（官方培训中心名录）；+40 364 086 906

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCUME、MTCINE、MTCSE、MTCSWE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCUME` — 用户管理（Hotspot / PPPoE）
- `MTCINE` — ISP 互联
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：校园 / 教育

### 推什么型号

**LT-S8328GP-4GX24GT-S（PoE 供 AP 与摄像头）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

PoE 供 AP / 摄像头 / 门禁、按楼栋或按班级 VLAN 隔离、组播、端口隔离、整机功率足

### 怎么开发

校园是分期扩建的，问「今年新增几栋楼 / 几个班？」；寒暑假是施工窗口，提前一个季度谈

### 风险点

校园网常走政府招标或教育局集采，要提前摸清是不是框架协议内；开学季绝对不能出问题，验收极严

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 七、首触邮件（可直接发送）

**主题**：PoE access switching for campus / school builds

```text
Hi Veaceslav,

Campus and school networks are mostly a PoE and VLAN isolation problem, which is the part I build for.

What caught my eye is that you work on MTCSWE, MTCEWE and MikroTik.

Where we may be useful: PoE++ for APs, cameras and door controllers, per-building or per-classroom VLAN isolation, port isolation, IGMP snooping, enough total power budget to run a full floor.

Are APs and cameras on the same switching layer, and how are you segmenting them?

If it is easier to judge from hardware than from a datasheet, I can send a LT-S8328XGP-4XS24GT-S evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

Either way, no follow-up sequence from me.

Best,
[your name]
```

> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；③ 落款换成你自己的名字与公司；④ 一次只问一个问题。

## 八、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
