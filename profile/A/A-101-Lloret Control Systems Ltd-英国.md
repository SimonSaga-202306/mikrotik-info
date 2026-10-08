# Lloret Control Systems Ltd

> **评级 A**　|　英国 · Coulsdon　|　档案编号 `A-101`　|　优先级 ★★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: A-101
rating: A
country: 英国
biz_org: 个体顾问（无官网）
business_model: 顾问项目制
decision_speed: fast
price_sensitivity: high
volume_potential: 1  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: true, voice: true, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-09-28
```

## SALES BRIEF（压缩模型）

- **是谁**：个体顾问（无官网）；顾问项目制
- **商业模式**：顾问项目制
- **为什么值得跟**：【人工定级】A —— 自动规则已跳过；信息待人工补齐（见备注）
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — Lloret 英智慧楼宇 MSI：Converged Network Systems 楼网总包指定权切入（$180 锚点一致）；Budd 具名；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：Do any of your nodes sit outdoors or in unheated cabinets, and how do you recover a frozen PoE device there today?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；采购量未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Lloret Control Systems Ltd（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 / Coulsdon | 事实 |
| 网站 | —（无公开站点） | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 个体顾问（无官网） | 【推断】 |
| 商业模式 | 顾问项目制 | 【推断】 |
| 团队规模 | 一人/微型 | 【推断】 |
| 决策链 | 短（本人即决策） | 【推断】 |
| ⚠️ 信息缺口 | 本条**抓不到邮箱**，需人工补齐邮箱或改为电话单独跟进后再进群发名单 | 事实 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】波 R67 批4·A-101:英谱: **Lloret Control Systems Ltd 深挖(Companies House/corpsignals/companycheck/endole/pomanda 五源互证)**:Company Number 01745436,**1983-08-11 创(42 年)**,SIC 43210 电气安装;注册 **Lloret House,20 Ullswater Crescent,Coulsdon Surrey CR5 2HR(大伦敦南边)**;**员工 53(corpsignals);£7,976,288 总资产;5 董事 1 股东 1 PSC;5.0 Google 评分 10 review**;**进出口线谱=Regular importer(60 个月连续进口光学/医疗工具器件)+Regular exporter(3 个月电机设备出口)=端法律来源可以供谱口**;**KP 金谱矩阵:Stig Johan Sjoblom(f1956-07=69 岁,**瑞典籍 Chair 主席**,1994-03 任至今 32 年,Endole+Companies House 直证)+Raymond George Smith(f1949-12=76 岁,Group Technical Director,1994-10 任)+Darren Anthony Lovelock(f1969-09=56 岁,**Managing Director**,2014-01 任)+Cara Louise Young(f1987-06=38 岁,**Finance Director+公司秘书 2020-04/10 双职**)=4 人矩阵**;**集团谱:Commtech Control Systems Ltd+Commtech Services Ltd(审计链)+Lloret Holdings Ltd+Llant Lloret Fire Solutions Ltd(Sjoblom/Young mutual companies)**;**业务=Trend Technology Centre(「established as a prominent Trend Technology Centre」)+BEMS(Building Energy Management Systems 建筑能耗管理)+Fire Alarm(Gent product authorized installation+open protocol option=**Gent 火警授权品安装谱**)+Lighting Control 照明控制+BMS 集成**;lloret.co.uk;Trend Controls/Gent 双授权品谱=集成商集成谱;**给我方挂念:Lovelock MD+Sjoblom 主席 4 人矩阵直通;Gent/Trand 授权品谱=同类铺位候选;BEMS PoE 载线强需求**。
- 【推断】R67 推土机深挖 批4 具名 KP 金谱矩阵(Trend/Gent 授权品+进出口线+瑞典主席)
- 【假设】STC-424XGGPM-280W($165 USD EXW (2026-10-08, 15天有效))Lovelock MD/Sjoblom 主席 BEMS/Gent 火警 PoE 载线引路

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

（待深挖批覆盖；当前仅有 CSV 名录口径：Allied Telesis（Marvell Prestera 接入层））

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温、L2+ 交换管理（VLAN/ERPS/QinQ）、VoIP/Voice VLAN
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖
  - L2+ 交换管理（VLAN/ERPS/QinQ）：【推断】依据 CSV 信号/深挖
  - VoIP/Voice VLAN：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sales@lloret.co.uk
  - 状态：既有/公开
- **电话**：—
- 来源等级：official-channel（R41–R48 联系方式台账口径）
- **原始联系字段**：Graham Budd（Commissioning Manager）- graham.budd@lloret.co.uk【主通道】；sales@lloret.co.uk【抄送】。主业**电气控制系统/楼宇自控**，92 人 → 工业交换机对口
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。
- **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
  - **Darren Anthony Lovelock**(Managing Director(2014-01-09 任;DOB Sep 1969=56 岁;Ascot Berkshire 谱;Companies House 直证))— dlovelock@lloret.co.uk(推断,送完核)/公司台口转 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://find-and-update.company-information.service.gov.uk/company/01745436/officers〕
  - **Stig Johan Sjoblom**(Chair Director(主席,1994-03-08 任=32 年;DOB Jul 1956=69 岁;Swedish 瑞典籍;Coulsdon 谱;Lloret Holdings+Fire Solutions 集团谱互))— ssjoblom@lloret.co.uk(推断) 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://find-and-update.company-information.service.gov.uk/company/01745436/officers〕
  - **Raymond George Smith**(Group Technical Director(1994-10-20 任=32 年;DOB Dec 1949=76 岁;Kingswood Surrey 谱))— rsmith@lloret.co.uk(推断) 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://find-and-update.company-information.service.gov.uk/company/01745436/officers〕
  - **Cara Louise Young**(Finance Director+Company Secretary(双职 Companies House 直证;Finance Dir 2020-10-01 任+Secretary 2020-04-29 任;DOB Jun 1987=38 岁))— cyoung@lloret.co.uk(推断) 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://find-and-update.company-information.service.gov.uk/company/01745436/officers〕


- **退信实测（2026-09-29）**：`sales@lloret.co.uk` 服务器拒收（Your message to sales@lloret.co.uk has been blocked）→ 停用该地址；替代通道：graham.budd@lloret.co.uk（Graham Budd · Commissioning Manager，CSV 具名）
  > 处置：sales@ 角色箱被挡（反垃圾概率高）；改走具名 graham.budd@（人名通道通过率高）；保留 sales@ 为抄送位
## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Darren Anthony Lovelock | Managing Director(2014-01-09 任;DOB Sep 1969=56 岁;Ascot Berkshire 谱;Companies House 直证) | dlovelock@lloret.co.uk(推断,送完核)/公司台口转 | Companies House 直证 O 级;邮箱推断 G 级 | https://find-and-update.company-information.service.gov.uk/company/01745436/officers |
| Stig Johan Sjoblom | Chair Director(主席,1994-03-08 任=32 年;DOB Jul 1956=69 岁;Swedish 瑞典籍;Coulsdon 谱;Lloret Holdings+Fire Solutions 集团谱互) | ssjoblom@lloret.co.uk(推断) | Companies House+Endole 双源 O 级;邮箱推断 G 级 | https://find-and-update.company-information.service.gov.uk/company/01745436/officers |
| Raymond George Smith | Group Technical Director(1994-10-20 任=32 年;DOB Dec 1949=76 岁;Kingswood Surrey 谱) | rsmith@lloret.co.uk(推断) | Companies House+Endole 双源 O 级;邮箱推断 G 级 | https://find-and-update.company-information.service.gov.uk/company/01745436/officers |
| Cara Louise Young | Finance Director+Company Secretary(双职 Companies House 直证;Finance Dir 2020-10-01 任+Secretary 2020-04-29 任;DOB Jun 1987=38 岁) | cyoung@lloret.co.uk(推断) | Companies House 直证 O 级;邮箱推断 G 级 | https://find-and-update.company-information.service.gov.uk/company/01745436/officers |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 24 口 CCTV/PoE（CNS 楼层接入层成本对照）

- **推什么**：STC-424XGGPM-440W（Saga）（24×千兆 PoE++ + 4×万兆上行）（现行对照：STC-424XGGPM-280W——P 表唯一登记，440W 档已停编）
- **切入点**：顺着他的 CNS 奖项项目：楼层接入 24 口 PoE++ 与 Allied 同展位的规格/成本对照表，定位「项目毛利优化选项」而非替换。
- **要问的问题**：CNS 项目的楼层接入段，有没有兴趣看一份同规格成本对照？
- **随附证明**：规格对照 + 单端口测算 + 英国交付说明（英文）。

### 第 2 次跟进 · 工业级非管理 PoE（管井/机房外零散点位）

- **推什么**：STI-240GE（Saga） PoE 版（4G + 2×SFP，DIN，-40~75°C）
- **切入点**：楼宇管井、屋面、停车层的 BMS/监控零散点位：4 口宽温 DIN 小机减少弱电间占用。
- **要问的问题**：屋面和管井里的 PoE 点位现在怎么供电交换？
- **随附证明**：宽温报告 + DIN 安装图 + 备件包价。

### 第 3 次跟进 · 管理型 PoE（CNS 分段标准件评估）

- **推什么**：STI-480XGGM（Saga）（8G + 4×SFP+ 10G，PoE 版）
- **切入点**：CNS 的分段设计（BMS/安防/租户三网隔离）：管理型 VLAN/ERPS 模板给 Jonathan（Network Architect）做技术评估。
- **要问的问题**：三网隔离的 VLAN/ERPS 模板要不要让我们的工程师陪跑一次评估？
- **随附证明**：VLAN/ERPS 模板 + 收敛实测 + 评估样机政策（英文）。


## R54 调研要点（加厚 · 全文见原始 JSON）

> 调研日期 **2026-09-28**；原始记录：`batch/A类加厚_2026-09-28_R54_第6批.json`。以下为要点压缩，证据原文全部保留。

- **业务定位**：伦敦南 Coulsdon 的智能楼宇集团：Lloret Controls（BMS/CNS/MSI）+ Lloret Fire（2008 年起家，东南区头部独立消防报警）双品牌，92 人。
- **产品线与在售品牌**：BEMS（Distech 等）+ CNS 融合网络（Allied Telesis，获奖合作伙伴）+ MSI + 安防/照明控制 + 消防系统。
- **目标行业与场景**：伦敦甲级写字楼（40 Leadenhall、Victoria House 等）、商业综合体改造（TVC Phase 2 与 Multiplex 同台）——楼宇楼层配线间是 PoE 主战场。
- **团队与规模**：约 92 人（CSV 记录）；Network Architect Jonathan 等自有网络架构师（CNS 培训课新闻）；工程总监 Oli 进 BCIA 管委会。
- **决策链与对接人**：sales@lloret.co.uk；具名 Graham Budd（Commissioning Manager）graham.budd@lloret.co.uk（CSV 9-27 记录）。
- **技术与认证**：Allied Telesis Platinum Partner（CSV 记录）+ 2024 Partner Growth 官方获奖；BCIA 行业组织席位。
- **采购与供应链信号**：CNS 项目随楼而定：楼层接入/配线间批量采购；与 Allied 关系深厚但对「项目级成本优化」永远听得进。
- **近期动态与线索**：2026 年持续活跃（TVC 学徒交换项目 2026-04；BCIA 任职 2026-01）——获奖后的扩张期，项目排期满。
- **与我方契合点**：CNS 楼层接入层=24 口 PoE++ 的标准图库位；机房外/管井=工业小机；给他「获奖伙伴以外的第二报价」做项目毛利。
- **风险与注意**：与 Allied 绑定极深（刚拿奖）：话术走「同场景成本对照」绝不替位；先与 Graham（调试经理）技术聊，再触达工程总监。

### R54 原文证据摘录（全部保留）

- **【业务定位】**官网口号：交付智能、安全、可持续、健康的建筑——BMS 起家的智能楼宇集成商。
  > We deliver smart, safe, sustainable, healthy buildings.
  > 来源：https://lloret.co.uk/
- **【产品线与在售品牌】**四大板块：BEMS（楼控）/ Converged Network Systems (ICT) / MSI / 安防与照明控制——CNS 融合网络正是 Allied 方案的落点。
  > Lloret specialises in the design, supply, installation, manufacture and ongoing maintenance of intelligent building systems, including Building Energy Management and Automatic Control Systems (BEMS), Converged Network Systems (ICT), Master Systems Integration, Security Systems and Lighting Control Solutions.
  > 来源：https://lloret.co.uk/
- **【技术与认证】**官网新闻：2025-03 获 Allied Telesis「Outstanding Achievement 2024 Partner Growth」奖，工程总监 Oliver 赴马拉加全球大会领奖——Allied 白金级关系获官方背书。
  > Lloret in March won the ‘Outstanding Achievement 2024 Partner Growth’ award from Allied Telesis. Our Engineering Director, Oliver, collected the award at their annual global conference that took place in Malaga.
  > 来源：https://lloret.co.uk/
- **【近期动态与线索】**同条新闻：2024 年与 Allied 合作在 Victoria House、Stonecutter Court、Carlton House Terrace 三处交付 CNS 融合网络；另有 40 Leadenhall（90 万平方英尺）Distech BMS 宣传片、工程总监进入 BCIA 管理委员会（2026-01 起 3 年任期）。
  > 2024 saw us successfully collaborating together to deliver the Converged Network Systems (CNS) on Victoria House, Stonecutter Court and Carlton House Terrace. · Our Engineering Director Joins the BCIA Management Committee（2026-01）
  > 来源：https://lloret.co.uk/

## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **—**；原始记录：`batch/A类深挖_2026-10-08_R67_R56_推土机批4.json`；价格均为 EXW 快照。

- **①背景再核**：1983 创 42 年;Coulsdon Surrey 南边;Lloret House 谱;£7.98M 资产
- **②芯片/型号**：BEMS+Gent 火警+照明+BMS 集成;PoE 24 口楼宇控制载线
- **③KP 深挖**：Sjoblom 主席 69+Lovelock MD 56+Smith 技总 76+Young 财董 38 四矩阵 O 级
- **④Saga 对标**：BEMS/Gent 火警楼宇控制 → 24 口 PoE 载;Trend 谱口
- **⑤在乎与偏好**：Trend/Gent 授权品;Carb 谱;Coulsdon 谱

### R55 证据摘录（全部保留 · 含数量）

- **【法体登册】**LLORET CONTROL SYSTEMS LIMITED Company No 01745436;Incorporated On 11 August 1983;SIC 43210;Lloret House 20 Ullswater Crescent Coulsdon Surrey CR5 2HR;53 employees;£7,976,288 assets;5 directors 1 shareholders 1 PSC;five director changes
  > LLORET CONTROL SYSTEMS LIMITED Company No 01745436;Incorporated On 11 August 1983;SIC 43210;Lloret House 20 Ullswater Crescent Coulsdon Surrey CR5 2HR;53 employees;£7,976,288 assets;5 directors 1 shareholders 1 PSC;five director changes
  > 来源：https://companycheck.co.uk/company/01745436/LLORET-CONTROL-SYSTEMS-LIMITED/companies-house-data
- **【KP 四矩阵】**SJOBELOM, Stig Johan(DOB Jul 1956,Swedish)Chair Director 1994-03-08;SMITH, Raymond George(DOB Dec 1949)Group Technical Director 1994-10-20;LOVELOCK, Darren Anthony(DOB Sep 1969)Managing Director 2014-01-09;YOUNG, Cara Louise(DOB Jun 1987)Finance Director 2020-10-01+Company Secretary 2020-04-29
  > SJOBELOM, Stig Johan(DOB Jul 1956,Swedish)Chair Director 1994-03-08;SMITH, Raymond George(DOB Dec 1949)Group Technical Director 1994-10-20;LOVELOCK, Darren Anthony(DOB Sep 1969)Managing Director 2014-01-09;YOUNG, Cara Louise(DOB Jun 1987)Finance Director 2020-10-01+Company Secretary 2020-04-29
  > 来源：https://find-and-update.company-information.service.gov.uk/company/01745436/officers
- **【进出口谱】**Regular importer of optical and medical tools and devices(60 months imported);Regular exporter of electrical machinery and equipment(3 months exported);Holding company;large company;£7,976,288 assets
  > Regular importer of optical and medical tools and devices(60 months imported);Regular exporter of electrical machinery and equipment(3 months exported);Holding company;large company;£7,976,288 assets
  > 来源：https://corpsignals.com/companies/uk/lloret-control-systems-ltd-01745436.html
- **【Trend/Gent 谱】**Established as a prominent Trend Technology Centre;Lorem offers Building Energy Management Systems(BEMS),Fire Alarm Systems(Lloret offers Gent product installations and open protocol options),Lighting Control Systems,BMS Integration
  > Established as a prominent Trend Technology Centre;Lorem offers Building Energy Management Systems(BEMS),Fire Alarm Systems(Lloret offers Gent product installations and open protocol options),Lighting Control Systems,BMS Integration
  > 来源：https://open.endole.co.uk/insight/company/01745436-lloret-control-systems-limited

### R56 十维速览（深挖笔记 · 事实与推断混合，证据见上节）

- **业务定位**：Lloret Control Systems Ltd(01745436,1983 创 42 年):Coulsdon Surrey 南端火/安防/楼宇控制集成商(Trend+Gent 授权品谱)
- **产品线与在售品牌**：BEMS+Fire Alarm(Gent authorized+open protocol)+Lighting Control+BMS 集成+Trend Technology Centre 谱
- **目标行业与场景**：大伦敦+Surrey 边谱;商用楼宇+火警;进出口线谱口
- **团队与规模**：53 员工(corpsignals);42 年;5 董事;£7.98M 总资产;4 人董事矩阵 O 级
- **决策链与对接人**：Stig Johan Sjoblom(Chair 主席,瑞典,69 岁,1994-03 任 32 年)+Darren Lovelock(MD,56 岁,2014-01 任)+Raymond Smith(Group Tech Dir,76 岁,1994-10 任)+Cara Louise Young(Fin Dir+秘书,38 岁,2020-10 任)
- **技术与认证**：SIC 43210;SHAB 2020-04/10 Young 双职档;Endole/Companies House 登实;Google 5.0 评 10 review
- **采购与供应链信号**：Regular importer 60mo 光学/医疗器件+Regular exporter 3mo 电机设备=端口谱口;Trend/Gent 授权品谱=同类铺位位
- **近期动态与线索**：SHAB 谱;Google 5.0 评;Lloret Fire Solutions 集团互谱;进出口线端法律来源
- **与我方契合点**：Lovelock MD+Sjoblom 主席 → 24 口 PoE(BEMS/Gent 火警楼宇控制 PoE 载线)
- **风险与注意**：**员数 53 单源注;进出口线=进口光学/医疗器件+出口电机设备(两端谱口);集团谱子司注;Sjoblom 瑞典籍谱位注**

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | Lloret 英智慧楼宇 MSI：Converged Network Systems 楼网总包指定权切入（$180 锚点一致）；Budd 具名 |
| 备选2 | STC-28DGGPM（8口 PoE 接入盒） | 升级/延展场景 | $99 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STI-288GP（工业非管理 8口 PoE） | 升级/延展场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

- **S**：42 年+Trend/Gent 授权品
- **W**：进出口线=光学/医疗进口注
- **O**：BEMS 楼宇控制 PoE 扭
- **T**：员数 53 单源注+集团子司

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**本户特别红线/停止条件**

- 一人/个体=单点与节奏风险

**停止开发条件（命中任一即停）**：3 次定向触达无任何实质回复；确认现用平台完全满足需求；只愿比价不愿谈场景；决策者确认接触不到；对方书面拒绝。

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（PoE/接入层池） | ✅ |
| 决策人识别 | ✅ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] MikroTik 谱位在售线需官网核
  - [ ] Lovelock 直邮推档
  - [ ] 进出口线端源精确次年订

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your projects

```text
Darren and Stig Team,

We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $165 USD EXW (2026-10-08, 15 days valid) — a value unit for BEMS, Gent fire alarm and building control deployment lines. Datasheet + CE pack on request.

Best regards
Saga / SmartByte ODM
```

> 发送前检查：① 不出现「Made in China」或原产地信息；② 不承诺未实测的指标；③ 落款换成你自己的名字与公司；④ **一次只问一个问题**；⑤ 货币单位一律 USD 并带快照日期；⑥ 该客户为教师/公立身份时先读「本户特别红线」。

## 跟进记录

| 日期 | 渠道（邮件/电话/LinkedIn/展会） | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 首次触达前留空；发出邮件后填入日期与渠道。有新进展时告诉我，我来更新本档案并重评 stage。

## 下次复核

- 固定节点：首触发出后 **14 天**无回复 → 复核是否降频/降级；有任何回复 → 当即重评 stage 与评级。
- 报价纪律：全部价格为 USD EXW 快照（2026-09-28，15 天有效）；过窗先核价再报价。

---

*建档日期：2026-09-22　|　结构 v2：2026-09-28（R56 规则）　|　数据来源：客户名单_反向信号_2026-09.csv + R54/R55 调研 JSON*
