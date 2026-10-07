# GOODSTORE

> **评级 B**　|　拉脱维亚　|　档案编号 `B-178`　|　优先级 ★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-178
rating: B
country: 拉脱维亚
biz_org: 分销/批发商（有官网）
business_model: 分销 stocking
decision_speed: moderate
price_sensitivity: high
volume_potential: 4  # 1-5
needs: {poe: true, industrial: true, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STI-288GP
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-10-07
```

## SALES BRIEF（压缩模型）

- **是谁**：GOODSTORE(拉脱维亚 Daugavpils,Muzeja iela 11 / Vidus iela 32, LV-5401;=**SIA "Goodman Group"**;**注册号 41503064521,V…
- **商业模式**：分销 stocking
- **为什么值得跟**：通用分销商信号，无差异化切入点，慢慢跟
- **P1（首触唯一主推）**：STI-288GP（工业非管理 8口 PoE） — 弱电安防垂直店的监控谱工业 PoE 供电轨；$74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：你们的监控/弱电项目柜里,DIN 轨工业 PoE 交换机现随哪家?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | GOODSTORE（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 拉脱维亚 | 事实 |
| 网站 | goodstore.lv | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Reseller） | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | GOODSTORE(拉脱维亚 Daugavpils,Muzeja iela 11 / Vidus iela 32, LV-5401;=**SIA "Goodman Group"**;**注册号 41503064521,VAT LV41503064521**;Swedbank AS HABALV22 账户件;**2013 创(弱电系统设计建造;2023 开 g | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | (待谱面二补) | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

(待谱面二补)

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电、工业/户外/宽温
  - PoE 接入供电：【推断】依据 CSV 信号/深挖
  - 工业/户外/宽温：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：info@goodstore.lv
  - 状态：既有/公开
- **电话**：+371 2701 7034
- **原始联系字段**：+371 2701 7034 / info@goodstore.lv
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

- 关键人未定位：首封信件以 info/通用邮箱开场并向其索要正确联系人。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP（工业非管理 8口 PoE）），备选型不进邮件。

### 第 1 次跟进 · 具名 kp 引路口

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：具名 kp 引路 → 采购/技术硬件分载线
- **要问的问题**：贵司 24 口 PoE 交换机的硬件采购线由哪位同事主责？
- **随附/动作**：规格页

### 第 2 次跟进 · 一页目录卡

- **推什么**：一页目录卡（统一口径=P1 系列，不外溢）
- **切入点**：价值层 PoE 谱链卡
- **要问的问题**：可否入谱链名录？
- **随附/动作**：卡

### 第 3 次跟进 · 留档+LinkedIn 谱

- **推什么**：—（统一口径=P1 系列，不外溢）
- **切入点**：谱链明智途径
- **要问的问题**：—
- **随附/动作**：—


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-08(R66-B 波 1)**；原始记录：`batch/B类深挖_2026-10-08_R66_BKP波2.json`；价格均为 EXW 快照。

- **背景深描**：GOODSTORE(拉脱维亚 Daugavpils,Muzeja iela 11 / Vidus iela 32, LV-5401;=**SIA "Goodman Group"**;**注册号 41503064521,VAT LV41503064521**;Swedbank AS HABALV22 账户件;**2013 创(弱电系统设计建造;2023 开 goodstore.lv 电商线)**;谱型=拉脱维亚认证安防系统集成+弱电/网络件电商(CCTV/安防/门禁/消防/安装材/线缆/网络件/光纤/电源/太阳能;聚焦高复杂度技术安防系统工程;goodman.lv)
- **芯片与在用型号**：(待谱面二补)
- **关键人KP**：**守档准由;R66 波次二点名**
- **关注点与资质**：认证集成+电商双线+注册号锁
- **优缺点SWOT**：S 认证集成+电商双线+注册号锁 / W 人名谱零命中 / O UR 登记册反查可破 / T 大牌安防件链
- **Saga产品适配**：24 口 value PoE($180 USD EXW (2026-10-07, 15天有效)):拉脱维亚 Daugavpils 安防集成+电商;守档:身份锁定(41503064521);R66 波次二点名(UR 董事层)

### R55 证据摘录（全部保留 · 含数量）

- **【业务定位】**GOODSTORE is an online store created by the company SIA "Goodman Group";Registration number: 41503064521;VAT: LV41503064521;Muzeja street 11, Daugavpils(goodstore.lv 官方 About 自署)
  > GOODSTORE is an online store created by the company SIA "Goodman Group";Registration number: 41503064521;VAT: LV41503064521;Muzeja street 11, Daugavpils(goodstore.lv 官方 About 自署)
  > 来源：https://goodstore.lv/en/about-us/
- **【业务定位】**Founded in 2013 Daugavpils;2023 Launch of Goodstore.lv;certified security system integrator in Latvia(goodman.lv 官方页)
  > Founded in 2013 Daugavpils;2023 Launch of Goodstore.lv;certified security system integrator in Latvia(goodman.lv 官方页)
  > 来源：https://goodman.lv/
- **【近期动态与线索】**2026-10-08 R66-B 波 2:身份=SIA Goodman Group 注册号锁;人名谱零命中→守档;波次二=拉脱维亚 UR(ur.gov.lv)按 41503064521 反查董事层
  > 2026-10-08 R66-B 波 2:身份=SIA Goodman Group 注册号锁;人名谱零命中→守档;波次二=拉脱维亚 UR(ur.gov.lv)按 41503064521 反查董事层
  > 来源：https://info.ur.gov.lv/

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP（工业非管理 8口 PoE） | 主场景 | $74.8 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 弱电安防垂直店的监控谱工业 PoE 供电轨 |

- **P1 规格一句话**：工业非管理 8口 PoE af/at，250m 延伸供电，冗余 DC44–57V（过压/反接保护），DIN 轨，3 年保
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S 认证集成+电商双线+注册号锁 / W 人名谱零命中 / O UR 登记册反查可破 / T 大牌安防件链

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

**停止开发条件（命中任一即停）**：3 次定向触达无任何实质回复；确认现用平台完全满足需求；只愿比价不愿谈场景；决策者确认接触不到；对方书面拒绝。

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（PoE/接入层池） | ✅ |
| 决策人识别 | ❓ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 硬件采购线在职者(波次二)
  - [ ] MikroTik 谱面份额

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE switching for your line

```text


We build a 24-port Gigabit PoE access switch (280W, 802.3af/at, watchdog). Reference: $180 USD EXW (2026-10-07, 15 days valid) — a value unit that rides along with each deployment. Could you point us to the colleague carrying the hardware purchasing line?

Best regards,
Saga Networks Export Desk
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

*建档日期：2026-09-22　|　结构 v2：2026-10-07（R56 规则 · R65 B 类对齐 A 标准）　|　数据来源：客户名单_反向信号_2026-09.csv + B 类深挖调研 JSON*
