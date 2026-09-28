# Tamás Gajdos

> **评级 A**　|　匈牙利 · Szeged　|　档案编号 `A-014`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：A　**Yes** —— 明显该做，直接投入精力
- **评级依据**：有明确交换/供电需求（交换认证 MTCSWE、交换专长），且有具体人直联
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Tamás Gajdos |
| 国家 | 匈牙利 |
| 城市 | Szeged |
| 网站 | — |
| 类型 | 集成商/顾问（MikroTik 认证） |
| 反向信号 | MikroTik 认证顾问 MTCNA+MTCRE+MTCWE+MTCINE+MTCIPv6E+MTCSE+MTCSWE+MTCEWE |
| 是否自有品牌 | 否 |
| 首推 SmartByte 型号 | LT-S8328XGP-4XS24GT-S |
| 切入点 | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 数据来源 | 2026-09-22 |
| 原备注 | 8 证含 MTCSWE（交换）+ MTCEWE（企业无线）；中小企业 IT、WireGuard VPN；英匈塞三语 |

## 三、人员与联系方式

- **邮箱**：crowbarlabs@outlook.com
- **电话**：+36 30 243 2729
- **原始联系字段**：+36 30 243 2729 / crowbarlabs@outlook.com

## 四、品牌与技术栈

**持有认证**：MTCNA、MTCRE、MTCWE、MTCINE、MTCIPv6E、MTCSE、MTCSWE、MTCEWE

- `MTCNA` — 网络助理（入门）
- `MTCRE` — 路由
- `MTCWE` — 无线
- `MTCINE` — ISP 互联
- `MTCIPv6E` — IPv6
- `MTCSE` — 安全
- `MTCSWE` — **交换**（最能说明他卖交换机）
- `MTCEWE` — 企业无线

**涉及品牌 / 技术**：MikroTik、WireGuard

## 五、跟进策略

**场景判断**：MTCSWE 交换认证

### 推什么型号

**LT-S8328XGP-4XS24GT-S（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`LT-S8328XGP-4XS24GT-S`（供参考，以实际沟通为准）

### 核心卖点

**L3 硬件卸载（线速转发不占 CPU）**、QinQ、ERPS/MSTP、ACL、静态路由、完整 CLI + SSH + SNMP + 私有 MIB、VLAN 翻译重写

### 怎么开发

他持有 MTCSWE（MikroTik 交换认证），交换是正式专长——**不用给他做科普**。开口问「你二层环网现在跑什么协议？STP 还是 ERPS？」直接给 CLI 命令对比和转发实测数据

### 风险点

他会拿 Cisco / 锐捷的功能逐条对表，缺一项就被记在小本子上；文档、MIB、CLI 手册必须一次给全；含糊其辞会立刻失去这类技术型客户的信任

## 六、深度加厚（R54 逐户调研）

> 调研日期 **2026-09-28**；来源为客户官网/公开页面抓取，原文摘录见下一节，原始记录：`batch/A类加厚_2026-09-28_R54_第1批.json`。

- **业务定位**：塞格德（Szeged）的网络/系统工程师，MikroTik 认证顾问；本职在 Furukawa Electric Institute of Technology（研究机构）做系统/实验仪器方向，同时在 MikroTik 社区活跃（开源工具、培训实践日）。
- **产品线与在售品牌**：MikroTik 生态为主（开源 wg-routeros-network：批量生成 RouterOS WireGuard 网络；mikrotik-certified-padawan 配置仓库）。
- **目标行业与场景**：中小企业 IT、实验/研究环境、WireGuard VPN 组网；也曾代 Alphasonic Kft（匈牙利 MikroTik 分销）主持免费的 MikroTik 实践日。
- **团队与规模**：个人（研究机构职员 + 社区讲师），决策链=本人。
- **决策链与对接人**：crowbarlabs@outlook.com；+36 30 243 2729；GitHub gajdipajti。
- **技术与认证**：8 项 MikroTik 认证含 **MTCSWE + MTCEWE**；GitHub 自述「barefoot physicist (+PhD)」、系统管理与实验仪器方向。
- **采购与供应链信号**：个人采购、预算有限但对技术内容要求高；他影响本地社区（实践日/开源），可作种子用户。
- **近期动态与线索**：GitHub 持续维护 MikroTik 相关工具；2025 年 2 月以 Gajdos Tamás 名义代 Alphasonic 主持 MikroTik 免费实践日与头脑风暴活动。
- **与我方契合点**：他写脚本、跑自动化：管理型交换机的 CLI/MIB/批量配置正好给他「可脚本化」的卖点；8G/24 口 PoE 可用于他的实验与中小企业项目。
- **风险与注意**：预算小、以技术内容换参与；先用开源/脚本友好的材料建立关系，再谈小批量。

## 七、原文证据摘录（R54）

> 下列引用为 2026-09-28 抓取的页面原文（非我方转述）；点不开或内容变动时，以抓取 JSON 中的记录为准。

- **【技术与认证】**GitHub 主页：Szeged、Furukawa Electric Institute of Technology、MikroTik 开源工具作者。
  > A barefoot physicist (+PhD) … Lab instruments, sysadmin stuff, munin love. Furukawa Electric Institute of Technology；Szeged, Hungary；Pinned: wg-routeros-network — Tools for generating a Wireguard network for Mikrotik RouterOS
  > 来源：https://github.com/gajdipajti
- **【近期动态与线索】**2025 年 2 月代 Alphasonic Kft 主持 MikroTik 免费实践日（本人为协调人）。
  > MikroTik Díjmentes Gyakorlónap és Ötletbörze … Az eseményt koordinálja: Gyenese László távollétében: Gajdos Tamás
  > 来源：https://www.alphasonic.hu/esemeny/mikrotik-gyakorlonap/
- **【目标行业与场景】**既有记录：8 证含 MTCSWE/MTCEWE；中小企业 IT、WireGuard VPN；英匈塞三语。
  > 8 证含 MTCSWE（交换）+ MTCEWE（企业无线）；中小企业 IT、WireGuard VPN；英匈塞三语
  > 来源：https://mikrotik.com/consultants

## 八、3 步跟进计划（R54，**最多 3 次**）

> 综合客户官网/公开资料与我方（Saga/SmartByte）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：LT-S8328GP-4GX24GT-S（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：用他熟悉的语言：给他一份可直接跑的配置模板（VLAN/PoE/端口隔离）与实测数据，让他自己复现；他若满意，会带进实践日/社区。
- **要问的问题**：他手上的中小企业项目最常缺什么规格（口数/功率/上行）？
- **随附证明**：配置模板 + 实测数据 + 一台可长期测试的样机。

### 第 2 次跟进 · 工业级非管理 PoE（研究/实验环境）

- **推什么**：LT-IS6306G-2GX4GT PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：研究机构的实验台/车间环境：宽温、DIN、免配置，适合仪器与测试网络。
- **要问的问题**：实验环境里有没有需要宽温/导轨安装的网络点？
- **随附证明**：宽温报告 + DIN 安装照片 + 样品价。

### 第 3 次跟进 · 管理型 PoE（脚本化/自动化）

- **推什么**：LT-IS6312G-4GX8GT PoE 版（8G + 4×2.5G SFP）
- **切入点**：他写 RouterOS 脚本：管理型交换机的 CLI/MIB 与批量下发能力，可以让他的自动化工具链延伸过来。
- **要问的问题**：他愿不愿意把交换机也纳入他的自动化脚本（生成配置/批量升级）？
- **随附证明**：CLI 参考 + MIB 清单 + 一份批量配置示例脚本。

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
Hi Tamás,

You hold MTCSWE, so switching is a declared specialism rather than a side task — that is who I want to talk to.

What caught my eye is that you work on WireGuard.

Where we may be useful: L3 hardware offload (line-rate forwarding off the CPU), QinQ and VLAN translation, ERPS and MSTP, ACLs and static routing, full CLI plus SSH plus SNMP with a private MIB.

What are you using for L2 redundancy today, and does it need ERPS-class convergence?

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
