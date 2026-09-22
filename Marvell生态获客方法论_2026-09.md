# Marvell 生态获客方法论（Saga 专用）

> 本文把 Claude 的 18 条 + GPT 的 12 条合并评估，**砍掉 20 条、保留 10 条**，
> 每条给出可执行的操作步骤与现成搜索串。
> 判断标准只有一条：**一个预算极小、一个人、靠邮件开发的小贸易商，本周能不能做。**

---

## 0. 三个前提必须先纠正（否则整套方法会走偏）

### 0.1 ⚠️ 台厂不是客户 —— GPT 的头号推荐在这里踩线了

GPT 把 **PLANET、ORing、Korenix、Atop** 列为 ⭐⭐⭐⭐⭐ 目标客户。
**这四家全是台湾厂。而你定的规矩是：台厂不是客户，只是信号源。**

这不是文字游戏，是两种完全不同的打法：

| | 把台厂当客户 | 把台厂当信号源 |
|---|---|---|
| 动作 | 发邮件问"要不要买我们的交换机" | 扒它的**欧洲经销商名录** |
| 结果 | 自己是做交换机的，不会买你的，还可能抄你的价 | 拿到几十家**已经在卖工业交换机**的欧洲分销商 |
| | | ← **这个才是客户** |

> 仓库里 64 家 `分销（ORing 授权）` 就是这么来的。
> 正确姿势：**台厂官网 → Dealer Locator / Where to buy → 逐国扒 → 进 CSV**。

### 0.2 你是贸易商，不是 OEM/ODM 厂

GPT 的框架按"Marvell Access Switch + Centec Core + OEM/ODM"写的，
里面大量方法默认你有：销售团队、官网、SEO 预算、付费数据库账号。

**你没有。** 所以凡是"需要先花钱或先建站才能开始"的，全部后移或砍掉。

### 0.3 别建"知识图谱"，先建"能直接发邮件的表"

"Marvell Knowledge Graph" 听起来很美，但它是**两年后才见效的资产**。
你现在需要的是**明天早上能发出去的邮件**。

判断标准：**这张表能不能直接变成一封邮件？** 能 → 做。不能 → 缓。

---

## 1. 方法总评：30 条 → 留 10 条

### ✅ 保留（按优先级）

| # | 方法 | 星级 | 为什么留 |
|---|---|---|---|
| 1 | **竞品经销商据点名录**（Dealer Locator） | ★★★★★ | **已验证**：705 家就是这么挖出来的 |
| 2 | **生命周期 / EOL 替换** | ★★★★★ | 客户"必须现在换"，唯一不用说服的痛点 |
| 3 | **型号替代矩阵** | ★★★★★ | 客户说"我用 CRS326"，你立刻回型号 |
| 4 | **LinkedIn / Apollo 换关键词** | ★★★★ | 搜 `Prestera` 不搜 `switch`，命中率差一个量级 |
| 5 | **ImportYeti 海关数据** | ★★★★ | 免费，能看到**真实进口行为** |
| 6 | **NMS / SCADA 生态** | ★★★★ | 做监控软件的客户价值远高于分销商 |
| 7 | **FCC ID + DoC/CE PDF** | ★★★ | 全免费公开，能查到"谁在出新机" |
| 8 | **Reddit / 垂直论坛** | ★★★ | 本轮就出了一条实证（WISP 换 Netonix） |
| 9 | **Marvell 品牌 / 芯片库** | ★★ | 长期资产，慢慢攒 |
| 10 | **Firmware / MIB 能力库** | ★★ | 回答"支不支持 API"，仓库里已有部分 |

### ❌ 砍掉（含理由）

| 方法 | 原推荐 | 砍掉的理由 |
|---|---|---|
| SONiC / ONIE 生态 | ★★★★ | 技术门槛太高、决策链太长，**Claude 自己也同意砍** |
| Gartner / IDC / MarketsandMarkets | 付费推荐 | 报告里是**大企业案例**，你的客户是中小分销商 |
| Panjiva / ImportGenius / Zoominfo / D&B | ★★★★ | 全是付费，**与"预算极小"直接冲突**。用免费的 ImportYeti 替代 |
| Jungle Scout / Helium 10（亚马逊反查） | ★★ | 付费工具 + 亚马逊卖家要的是消费级价格，你打不过 |
| Kickstarter / Indiegogo | ★★ | 众筹硬件要的是 ODM 伙伴，你不是工厂 |
| **招聘 / SDK 反推** | ★★★★★ | **本轮实测证伪**：公开网络检索拿不到有效职位信息，搜出来全是 Linux 内核邮件列表和厂商软文 |
| 专利数据库 | ★★★ | 投入产出比最低的一条 |
| 图片反搜 | 实用 | 效率低，且找到的多半还是竞品官网 |
| 展会名单 | ★★★ | 名单质量参差，且展会恢复后成本高 |
| 行业采购平台（Thomasnet 等） | ★★★ | 工业品询盘为主，交换机很少在上面找供应商 |
| Digi-Key / Mouser / Arrow 找品牌 | ★★★ | 那是**元器件**分销，整机管理型交换机基本不在上面卖 |
| 规格书 SEO 长尾页 | ★★★★ | 方向对，但**前提是你有官网**；有的话排第 11 位做，没有就先不做 |
| **"Marvell Knowledge Graph"** | 终极目标 | 过度工程。**先把表建到能发邮件，再谈图谱** |

---

## 2. 保留方法：操作步骤 + 现成搜索串

### ① 竞品经销商据点名录（最高 ROI，已验证）

**逻辑**：卖竞品的渠道商 = 已经在卖、已有客户、已懂技术的人。

**操作步骤**
1. 进竞品官网找 `Where to buy` / `Dealer Locator` / `Partner Locator` / `Find a reseller`
2. **逐国筛选**，不要只看总部所在国
3. 拿到公司名 → 官网 → 找联系人 → 进 CSV
4. 优先标记：**同时代理 ≥2 个竞品品牌**的（说明它是纯渠道，不忠于单一品牌）

**已扒过的**（勿重复）：ORing（64 家）、Antaira、Westermo、ComNet、HMS/N-Tron/Red Lion、MikroTik 官方分销商
**还没扒的**：PLANET、Moxa、EtherWAN、CTC Union、Advantech、Korenix、Atop、Netonix、Ubiquiti UISP

> ⚠️ 扒台厂名录是**找它的经销商**，不是找台厂本身（见 0.1）

---

### ② 生命周期 / EOL（本轮新增，转化最高）

**逻辑**：客户不是不想换，是**还没到必须换**。停产 = 备件断供 = 他必须现在决定。

**操作步骤**
1. 定期看 MikroTik 分销商的停产清仓页（不是官方，官方没有统一 EOL 页）
   - `mikrotik-store.eu/en/archive-discontinued`
   - `cloudrouterswitches.com/mikrotik-eol.asp`
2. **必须双源确认**才能写进表 —— 一次误报"你的设备停产了"直接毁信任
3. 每个停产型号 → 配 SmartByte 替换型号 + 进价
4. 见 → `MikroTik停产机型替换矩阵_2026-09.md`

**获客钩子（一句话）**
> "你们手里还有多少 CRS125 / CRS226 / CRS112 的老客户？"

答得出数字 → A 级；答"有一些" → B 级；答"主要卖 CRS3xx" → C 级

**⚠️ 已排除的错误源**：`linknewnet.com` 那篇把在售的 CRS326/CRS328/CRS520 说成 EOL。别用。

---

### ③ 型号替代矩阵

**状态**：仓库里已有 `MikroTik_vs_SmartByte_替代对照表.xlsx` → 表页 `替代对照表`（19 行 × 13 列），
含 MSRP、进价、匹配度、"你赢在/你输在"。

**还缺的**：
- Netonix 替代（WISP 垂直，见 ⑧ 的实证）
- Ubiquiti UISP / EdgeSwitch 替代
- Allied Telesis 老型号替代（欧洲渠道深、价格 3–5×，最大替换池）
- 本轮新增的 8 个停产型号（已完成）

**用法**：客户说"我用 XXX"→ 打开表 → 30 秒内回型号 + 差价 + 我赢在哪。

---

### ④ LinkedIn / Apollo 换关键词

**核心改动**：**不要搜 `switch`**，太宽，全是求职者。

**搜技能关键词（不是职位关键词）**
```
Prestera  ·  98DX  ·  Marvell  ·  Industrial Ethernet
PoE Switch  ·  Fiber Switch  ·  Managed Ethernet
Layer2 Switch  ·  Layer3 Switch  ·  Network Appliance
ERPS  ·  ITU-T G.8032  ·  DIN-rail switch  ·  IEC 61850
```

**职位优先搜 Product Manager**（不是采购）
> 产品经理懂技术、懂缺口、而且**有动力找第二供应商**；
> 采购只会问价格。GPT 这条说得对。

**公司规模筛 51–200 人**（决策链短）

**地区**：意 / 西 / 波 / 德 / 希 / 捷 / 葡 / 乌（MikroTik 生态活跃区）
**避开**：北欧、波罗的海（生态几乎空白，实测：挪威 0、冰岛 0、斯洛文尼亚 0）

**Apollo.io**：免费版每月有额度，可按行业+规模+地区筛，直接导出邮箱

---

### ⑤ ImportYeti 海关数据（免费）

**操作**
1. `importyeti.com` → 搜 `ethernet switch` 或 HS Code **`8517.62`**
2. 看：**谁在从中国进口交换机、进口频率、数量、对应出口商**
3. 筛出**持续、批量**进口的欧洲/北美公司 → 这些是**现成的中国供应链买家**

**为什么对你是高价值**
> 能过滤掉"嘴上说要、手上不买"的公司。进口记录是**真金白银的行为证据**。

**进阶**：同一家进口商如果在跟**多家**中国出口商买，说明它在比价 → **你插进去的机会最大**

---

### ⑥ NMS / SCADA 生态（客户价值最高）

**逻辑**：做网络监控 / 工业监控软件的公司在给客户做方案，
**方案里必须有交换机**，而且它自己不造硬件 —— 完美互补。

**搜**
```
network monitoring software company Europe
SCADA + industrial ethernet + integration
"network management" software vendor + OEM hardware
remote monitoring solution provider
```

**为什么优先级高于分销商**
- 分销商卖的是**价格**，随时被更低价的替换
- 方案商卖的是**方案**，交换机嵌在里面，替换成本极高

> 仓库里 A 级客户里有几家就是这类（备注含"监控/自动化"）——
> 但注意：中文"监控"有歧义，要区分 **NMS 网管** 与 **CCTV 视频监控**（详见 README 坑 5）

---

### ⑦ FCC ID + DoC/CE PDF（全免费）

**FCC（北美）**
- `fcc.gov/oet/ea/fccid` → 搜 `ethernet switch` 或按公司名
- 能看到：**哪家公司在认证网络产品、具体型号、认证时间**
- **认证时间新 = 新产品即将上市 = 采购窗口期**

**CE / DoC（欧洲）**
```
"Declaration of Conformity" "ethernet switch" filetype:pdf
"CE" "managed switch" filetype:pdf manufacturer importer
```
DoC 里常写明 **Manufacturer / OEM / Importer** —— 能直接看出**谁在贴牌、谁在代工**

**用法**：发现某欧洲品牌的新品刚过认证 → 说明它在扩产线 → **马上联系，推第二供应商**

---

### ⑧ Reddit / 垂直论坛（本轮出了实证）

**搜**
```
r/wisp  ·  r/networking  ·  r/sysadmin  ·  r/homelab
"netonix alternative"  ·  "replace netonix"
"mikrotik switch" recommendation  ·  "looking for switch"
```

**本轮实证（r/wisp）**
> "The ASIC family in the CRS3xx uses **Marvell Prestera** (same chipset Cisco Meraki uses)"
> "we are starting to see a lot of our clients **use the CRS328 to replace Netonix**"

**两条结论**
1. **CRS3xx = Marvell Prestera** 得到用户侧确认（与 MikroTik 官方文档一致）
2. **WISP 运营商正在成批换掉 Netonix** —— 这是个活的替换窗口，且 WISP 是 PoE + 户外场景，正是工业款强项

**下一步**：整理 Netonix → SmartByte 替代表（Netonix 主力型号：WS-8-150-DC、WS-24-400A 等）

---

### ⑨ Marvell 品牌 / 芯片库（长期）

**状态**：表页 `Marvell品牌全景`（46 行 × 8 列）已有品牌 / 国家 / Marvell 证据 / 优先级

**继续补的字段**
```
芯片型号  ·  SDK 版本  ·  是否 OEM  ·  竞争关系  ·  对应 SmartByte 型号
```

**已知实证**（可直接引用）
| 品牌 | 芯片 | 证据 |
|---|---|---|
| MikroTik | 98DX3236 / 3257 / 226S / 2528 / 8332 / 4310 | **官方文档**逐型号列出 |
| Allied Telesis | 98DX3236 / 3336 / 4251 | Linux 内核补丁（作者邮箱 `alliedtelesis.co.nz`） |
| Edgecore（Accton） | 98DX3236 | 官方规格书 |

---

### ⑩ Firmware / MIB 能力库

**状态**：仓库已有 `Marvell Based CLI Manual.docx` / `Web Manual.docx`

**补的字段**
```
SNMP · MIB · Trap · CLI · SSH · REST API · NETCONF · Ansible · Cloud
```

**用途**：客户问"支不支持 API？" → 打开表 → 30 秒回答 + 知道差距在哪

---

## 3. 执行顺序（按 ROI 排序）

| 序 | 动作 | 产出 | 周期 |
|---|---|---|---|
| 1 | 扒 PLANET / Moxa / EtherWAN / Netonix / Ubiquiti 的 Dealer Locator | 预计 +80~150 家 | 1–2 天 |
| 2 | EOL 替换钩子群发给现有 705 家 | 直接询盘 | 半天 |
| 3 | Netonix → SmartByte 替代表 | 一张表，WISP 垂直专用 | 半天 |
| 4 | Apollo.io 按 `Prestera`/`Industrial Ethernet` 筛 PM | 联系人清单 | 1 天 |
| 5 | ImportYeti 查 `8517.62` 欧洲进口商 | 真实买家清单 | 1 天 |
| 6 | Allied Telesis 老型号替代表 | 欧洲最大替换池 | 1 天 |
| 7 | NMS/SCADA 方案商名单 | 高价值客户池 | 持续 |
| 8 | FCC ID 新认证监控（季度） | 采购窗口预警 | 每季 |
| 9 | 品牌/芯片库补全 | 长期资产 | 持续 |
| 10 | 规格书 SEO 长尾页 | 需先有官网 | 待定 |

---

## 4. 一句话总结

> **别再想"找更多客户"，先想"找正在被迫做决定的客户"。**
> 停产替换、方案商配套、海关数据里的真实进口商 —— 这三类人今天就有痛点。
> 剩下的 27 条方法里，大部分是在找"可能需要的人"。

---

*整理：2026-09-22 ｜ 基于 Claude 18 条 + GPT 12 条合并评估*
*本轮实测：EOL 双源验证成立、招聘反推证伪、Reddit 出实证（WISP 换 Netonix）、Netonix 替代待补*
