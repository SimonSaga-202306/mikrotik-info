# Sasa Blagojevic

> **评级 A**　|　塞尔维亚 · Niš　|　档案编号 `A-017`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长、组播/IPTV），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Sasa Blagojevic |
| 国家 | 塞尔维亚 |
| 城市 | Niš |
| 网站 | — |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCTCE+MTCSWE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-424DGGPM-440W（Saga） |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | ★★ 持 MTCSWE；**简历的交换专长段落与 IP ArchiTechs / LinkTechs 完全一致**（VLAN q-in-q、s/c tag、重写翻译、生成树、LACP 绑定、GPON、二层传输与冗余），说明他属于同一技术体系/合作网络；设计方向：运营商 WISP/Wireline、企业园区分支、数据中心；服务含 IPTV 与实时视频 |

## 三、人员与联系方式

- **邮箱**：sajberista@gmail.com
- **电话**：+381 64 910 8717
- **原始联系字段**：+381 64 910 8717 / sajberista@gmail.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCTCE、MTCSWE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCTCE` — 流量控制
- `MTCSWE` — **交换**（最能说明他卖交换机）
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景判断**：组播 / IPTV

### 推什么型号

**STC-424DGGPM-440W（Saga）（组播能力完整 + PoE 供电）**

> 系统初判型号：`STC-424DGGPM-440W（Saga）`（供参考，以实际沟通为准）

### 核心卖点

IGMP Snooping v2/v3、IGMP Querier、组播 VLAN、快速离开（Fast Leave）、**QoS/DSCP 优先级队列**（Dante 音频 over IP 与 IPTV 都靠它不丢包不抖动）

### 怎么开发

开口就问「IPTV 卡不卡？是不是组播没配好，全楼在泛洪？」；若是 Dante / 音频 over IP 场景，改问「音频有没有出现过断续或丢包？」——Dante 对组播和 QoS 极敏感，说中就是内行

### 风险点

组播出问题是满屏花屏，客户零容忍；必须先小规模（一个楼层）验证再铺开；要确认他的组播源和播放器兼容性

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。

- **业务定位**：塞尔维亚 Niš 的网络架构师/工程师，MikroTik 认证讲师（Trainer ID TR0507、Academy Trainer ACTR0658），与 3Net（塞尔维亚）和 All4Net（北马其顿）合作办 MTCNA 培训；为 IP ArchiTechs 的 Niš 实验室撰写 MikroTik CHR 100G 实测文章。
- **产品线与在售品牌**：MikroTik 生态为主（含 CHR 虚拟化、100G 级转发测试）；交换专长段落与 IP ArchiTechs/LinkTechs 体系一致（VLAN q-in-q、s/c tag、STP、LACP、GPON、二层传输与冗余）。
- **目标行业与场景**：运营商 WISP/Wireline、企业园区/分支、数据中心；服务含 IPTV 与实时视频。
- **团队与规模**：个人 + 培训合作网络（3Net/All4Net/IP ArchiTechs 生态）。
- **决策链与对接人**：LinkedIn：Sasa Blagojevic（DojoNetworks）；培训机构联系人（经 3Net/All4Net）；本轮未取得新邮箱（既有记录 sajberista@gmail.com 待复核）。
- **技术与认证**：MikroTik 认证（MTCNA/MTCRE/MTCWE/MTCUME/MTCINE/MTCIPv6E/MTCTCE 等，含 2018 年讲师资格）+ Cambium ePMP 培训；以英文/技术写作见长（stubarea51 文章）。
- **采购与供应链信号**：技术选型影响力大（培训+实验室+写作），可带来案例与二次传播；本人不一定是采购人，但能进入方案。
- **近期动态与线索**：2021 年撰写 MikroTik CHR 100G 全双工实测（实验室在 Niš，IP ArchiTechs 的开发实验室）；LinkedIn 认证清单显示其持续持证；与 3Net/All4Net 的培训合作仍在（3Net 站点有他的培训页）。
- **与我方契合点**：他关注转发性能与二层冗余：管理型 PoE（ERPS/LACP/q-in-q）与 10G 上行能对话；培训合作可把我们设备写成教学案例。
- **风险与注意**：技术门槛最高的一类客户：不要讲虚的，只给可复现实测与文档；联系人邮箱需先核实。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【技术与认证】**LinkedIn 认证栏：多项 MikroTik 认证 + 讲师资格（TR0507 / ACTR0658）。
  > Mikrotik Trainer — Credential ID TR0507；Mikrotik Academy Trainer — Credential ID ACTR0658；MTCINE 1806INE2171｜MTCWE 1806WE2064｜MTCUME 1806UME2105｜MTCIPv6E 1806IPv6E2209；ePMP Training Cambium Networks
  > 来源：https://www.linkedin.com/in/sasa-blagojevic-3ba87230/
- **【近期动态与线索】**3Net 培训页显示他与 3Net/All4Net 合作办 MTCNA 培训。
  > Saša Blagojević sertifikovan Mikrotik trener, u saradnji sa kompanijom 3Net iz Srbije i All4Net iz Makedonije, održaće MTCNA (Mikrotik Certified Network Associate) obuku.
  > 来源：http://3net.rs/tag/sasa-blagojevic/
- **【与我方契合点】**为 IP ArchiTechs 的 Niš 实验室撰写 CHR 100G 实测（200G 聚合吞吐）。
  > Shout out to Sasa Blagojevic who wrote up an in-depth article on how IP Architechs pushed the MikroTik CHR to 100Gbps full duplex (200Gbps total throughput). All of the testing was performed at our new development lab in Nis, Serbia.
  > 来源：https://www.linkedin.com/posts/ipa-kevin-myers_mikrotik-chr-breaking-the-100g-barrier-activity-6876079340556165120-VRiU/

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：园区/运营商接入层：24 口 PoE++ + 4×10G 上行；先给硬指标（转发时延、每口功率、VLAN 数量、LACP 哈希），他会自己复测。
- **要问的问题**：他给园区/运营商方案时，接入层的关键门限是什么？
- **随附证明**：完整规格 + 可复现测试方法 + 样机（他自测后给结论）。

### 第 2 次跟进 · 工业级非管理 PoE（室外/站点机柜）

- **推什么**：STI-280GE（Saga） PoE 版（8G + 2×2.5G SFP，DIN，-40~75°C）
- **切入点**：运营商站点与室外机柜：宽温宽压、DIN、免配置；作为「现场盒」补他方案里的边缘点位。
- **要问的问题**：他的方案里边缘点位（塔下/路边柜）现在用什么设备？
- **随附证明**：宽温/宽压报告 + 安装图 + 两台测试机。

### 第 3 次跟进 · 管理型 PoE（q-in-q / ERPS / 10G）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）或 STI-4240XGGM（Saga）（24G + 4×SFP+ + DI/DO/RS485）
- **切入点**：他会 q-in-q、GPON、二层冗余：给 VLAN/q-in-q 模板 + ERPS 收敛实测 + 10G 光模块兼容表；若合适，把我们的设备做成他下一篇文章的案例。
- **要问的问题**：他愿不愿意用我们的设备做一次可公开的二层冗余/10G 实测？
- **随附证明**：测试机 + 测试脚本 + 承诺不干预结论（数据由他发布）。

## 九、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十、首触邮件（可直接发送）

**主题**：IGMP / multicast behaviour on your IPTV builds

```text
Hi Sasa,

Multicast is where most IPTV and camera builds quietly fall over, and it is the part I specialise in on the access switch.

What caught my eye is that you work on IPTV, WISP, GPON and VLAN.

Where we may be useful: IGMP snooping v2/v3, a querier so the VLAN stops flooding, multicast VLAN, fast leave, and DSCP/QoS queues — the things that decide whether IPTV is watchable and whether Dante audio drops out.

Are you running IGMP snooping plus a querier, or still flooding the VLAN?

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
