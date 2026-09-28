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
| 首推 Saga 型号 | STC-424XGGPM-440W（Saga） |
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

**STC-424XGGPM-440W（Saga）（24×千兆 + 4×万兆 SFP+，三层）**

> 系统初判型号：`STC-424XGGPM-440W（Saga）`（供参考，以实际沟通为准）

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

> 综合客户官网/公开资料与我方（Saga）型号与能力矩阵得出；**只做 3 次**，每次推进一个台阶，第三次后要么出单、要么降频。

### 第 1 次跟进 · 24 口 CCTV/PoE 入门款

- **推什么**：STC-424DGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）
- **切入点**：用他熟悉的语言：给他一份可直接跑的配置模板（VLAN/PoE/端口隔离）与实测数据，让他自己复现；他若满意，会带进实践日/社区。
- **要问的问题**：他手上的中小企业项目最常缺什么规格（口数/功率/上行）？
- **随附证明**：配置模板 + 实测数据 + 一台可长期测试的样机。

### 第 2 次跟进 · 工业级非管理 PoE（研究/实验环境）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：研究机构的实验台/车间环境：宽温、DIN、免配置，适合仪器与测试网络。
- **要问的问题**：实验环境里有没有需要宽温/导轨安装的网络点？
- **随附证明**：宽温报告 + DIN 安装照片 + 样品价。

### 第 3 次跟进 · 管理型 PoE（脚本化/自动化）

- **推什么**：STI-480DGGM（Saga） PoE 版（8G + 4×2.5G SFP）
- **切入点**：他写 RouterOS 脚本：管理型交换机的 CLI/MIB 与批量下发能力，可以让他的自动化工具链延伸过来。
- **要问的问题**：他愿不愿意把交换机也纳入他的自动化脚本（生成配置/批量升级）？
- **随附证明**：CLI 参考 + MIB 清单 + 一份批量配置示例脚本。

## 九、深度再发掘（R55：背景 · 芯片/型号 · 关键人 · 在意点 · SWOT · Saga 适配）

> 调研日期 **2026-09-28**；来源含官网/公开工商与社媒页面，原文摘录见本节后部；原始记录：`batch/A类深挖_2026-09-28_R55_第2批.json`。涉及我方价格均为 EXW 快照（15 天有效，报价前核价）。

- **背景深描**：**Tamás Gajdos**（1988 生），匈牙利 Szeged 个体顾问（公开名录 5 证：MTCNA+MTCRE+MTCWE+MTCINE+MTCIP）。GitHub **gajdipajti** 自述**就职 Furukawa Electric Institute of Technology**（古河电工在匈研发机构），自称「barefoot physicist (+PhD)」——物理+信息学双背景（塞格德大学物理系主页存档），**四门语言：匈牙利语/英语/塞尔维亚语/德语**。RouterOS 开源作者：wg-routeros-network（WireGuard 网络生成器）、mikrotik-certified-padawan（MikroTik 认证学员配置组）。2008 年曾赴贝尔格莱德 S&T 培训（塞语境+多语=巴尔干项目沟通无障碍）。
- **芯片与在用型号**：RouterOS 自动化/WireGuard 组网脚本作者=协议层玩家；物理实验室仪器+sysadmin 日常（munin 插件 fork）；Furukawa 圈=光通信/大企业研发环境（布线与光器件语境）。出货量：无（雇员+侧咨询）。客户反馈：GitHub 26 星的 munin 插件=社区小有认可。
- **关键人KP**：**Gajdos Tamás 本人**。邮箱 **crowbarlabs@outlook.com**（CSV 既有；outlook.com MX 有效）+ 电话 +36 30 243 2729；GitHub @gajdipajti（可 issue/私讯二通道）；（大学旧页 gajdos.tamas@stud.u-szeged.hu 为历史邮箱不投）。LinkedIn 未见。
- **关注点与资质**：①开源/自动化优先（会读源码的买家，给他 MIB/CLI 文档比彩页有用）；②WireGuard/IPv6 新协议兴趣（MTCIP 持证佐证）；③多语人脉（塞/德/英）；④学术严谨=虚标零容忍。参展/社媒：GitHub 即社媒。
- **优缺点SWOT**：**S**：极客深度+多语+大厂研发履历=完美技术对话者；MTCINE/IP 高阶证=能评估 L3 边界。**W**：侧咨询属性=采购主动权弱、量小；outlook 个人邮无商务外壳。**O**：实验室级样机（STI 工业线 10G 环/ERPS 玩具属性正中）；Furukawa 产业圈的长尾可能（不主动刺探雇主项目，只谈个人）。**T**：雇员身份决定响应慢、成交偶发。
- **Saga产品适配**：技术玩家样机：**STI-480XGGM**（工业 L2+ 8口 4×10G，**EXW $253**，ERPS<20ms 环网自测）+ **STC-424XGGM**（**EXW $143**，L2+/L3 两档对比实验）。随附特性表与「L3 系无 Voice VLAN/PC3 无 HTTPS」的诚实边界说明——这种买家最吃如实标注。

### 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Gajdos Tamás | 个体顾问 / Furukawa Electric IT 研发雇员（GitHub 自述） | crowbarlabs@outlook.com；+36 30 243 2729；GitHub @gajdipajti | 邮箱既有；MX（outlook.com）已验；GitHub 身份已核 | https://github.com/gajdipajti ・ http://www.stud.u-szeged.hu/Gajdos.Tamas/home.html |

### R55 证据摘录

- **【现职】**GitHub 资料：Furukawa Electric Institute of Technology，Szeged。
  > Gajdos Tamás gajdipajti - Furukawa Electric Institute of Technology - Szeged, Hungary
  > 来源：https://github.com/gajdipajti
- **【开源作品】**RouterOS WireGuard 网络生成器等开源项目作者。
  > wg-routeros-network Public Tools for generating a Wireguard network for Mikrotik RouterOS … mikrotik-certified-padawan Public Mikrotik Certified Padawan group Mikrotik configurations.
  > 来源：https://github.com/gajdipajti
- **【自述画像】**物理+PhD、仪器与 sysadmin 方向。
  > A barefoot physicist (+PhD), I've never been much of a coder … Lab instruments, sysadmin stuff, munin love.
  > 来源：https://github.com/gajdipajti?tab=stars
- **【语言能力】**匈/英/塞/德四语。
  > Spoken Languages: Hungarian, English, Serbian, German
  > 来源：http://www.stud.u-szeged.hu/Gajdos.Tamas/home.html

## 十、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 十一、首触邮件（可直接发送）

**主题**：Switching question for an MTCSWE holder

```text
Hi Tamás,

You hold MTCSWE, so switching is a declared specialism rather than a side task — that is who I want to talk to.

What caught my eye is that you work on WireGuard.

Where we may be useful: L3 hardware offload (line-rate forwarding off the CPU), QinQ and VLAN translation, ERPS and MSTP, ACLs and static routing, full CLI plus SSH plus SNMP with a private MIB.

What are you using for L2 redundancy today, and does it need ERPS-class convergence?

If it is easier to judge from hardware than from a datasheet, I can send a STC-424XGGPM-440W evaluation unit and you can put it in a rack for 30 days. Otherwise a two-page spec sheet is one email away.

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
