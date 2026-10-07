# eltrox.pl

> **评级 B**　|　波兰　|　档案编号 `B-274`　|　优先级 ★★　|　状态：未触达
>
> **触达状态（Stage）**：00-researched　|　结构版本：结构化档案 v2（R56 规则，2026-09-28 用户审定）

```yaml structured_profile
code: B-274
rating: B
country: 波兰
biz_org: 分销/批发商（有官网）
business_model: 分销 stocking
decision_speed: moderate
price_sensitivity: high
volume_potential: 5  # 1-5
needs: {poe: true, industrial: false, tenG: false, l2plus: false, voice: false, oem: false, hotel: false, training: false}
p1: STC-424XGGPM-280W
stage: 00-researched
struct_version: v2  # v2 骨架
updated: 2026-10-07
```

## SALES BRIEF（压缩模型）

- **是谁**：ELTROX Sp. z o.o.(Częstochowa ul. Warszawska 74;NIP 6462490527, KRS 0000175807, REGON 276916481；股本 560K zł;**Z…
- **商业模式**：分销 stocking
- **为什么值得跟**：通用分销商信号，无差异化切入点，慢慢跟
- **P1（首触唯一主推）**：STC-424XGGPM-280W（24口 PoE + 4×10G） — 波兰安防巨头的监控/报警安装商随单 24 口 280W PoE 走量位(40 门店架)；$180 USD EXW（2026-09-28 快照，15 天有效，报价前核价）
- **第一问（只问一个）**：你们的监控/报警安装商客户,24 口管理型 PoE+ 现随哪家?门店架上 value 档有位吗?
- **最大未知（影响成交的）**：现有交换机品牌与 PoE 预算未确认；集团/分销内部决策层级未确认
- **下一步**：发出首触邮件（见文末样板）→ 等待信号；14 天无回复按降频规则处理

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | eltrox.pl（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 波兰 | 事实 |
| 网站 | eltrox.pl | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Master） | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | ELTROX Sp. z o.o.(Częstochowa ul. Warszawska 74;NIP 6462490527, KRS 0000175807, REGON 276916481；股本 560K zł;**Zbigniew Dąbrowski = Prezes Zarządu(董事会主席)**;Barbara Otolińska 大股东（504/ | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 【推断】40 门店安防巨头=安装商客户当天提货网络;监控/报警安装商的核心随单就是 PoE 交换机;其 MikroTik 在架以路由/CRS 为主,PoE 专业档稀缺;体量堪比西班牙波 DMI 但谱更聚焦安防 | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |


**深挖三层（R56 · 一句话版 · 全文见原始 JSON）**

- 【事实】Eltrox Sp. z o.o.(Częstochowa ul. Warszawska 74,KRS 0000175807,股本 560 万 zł;2000 创,**501-1000 员工**):**波兰最大的安防设备分销商**——『największy w kraju dystrybutor sprzętu zapewniającego bezpieczeństwo』,**全国近 40 家门店**(Bydgoszcz/Gdańsk/Gdynia/Gliwice/Kraków…);零售+电商+加盟+批发多渠道;谱=监控/报警系统/智能家居/光伏可再生/计算机网络/IT/TV;MikroTik Master 挂证;批发支持 dropshipping(hurton)+安装商项目合作 | R65 深挖:Częstochowa 大国谱；Otolińska 家族结构 90% 股主
- 【推断】40 门店安防巨头=安装商客户当天提货网络;监控/报警安装商的核心随单就是 PoE 交换机;其 MikroTik 在架以路由/CRS 为主,PoE 专业档稀缺;体量堪比西班牙波 DMI 但谱更聚焦安防
- 【假设】开口角度=「安防巨头的监控/报警安装商随单 PoE 走量位」:STC-424 做 40 门店架的 24 口 280W 安装商档,批发号+dropshipping 管道对口

## 技术与在用（芯片/型号/规格/出货·客户反馈尽量核实）

【推断】40 门店安防巨头=安装商客户当天提货网络;监控/报警安装商的核心随单就是 PoE 交换机;其 MikroTik 在架以路由/CRS 为主,PoE 专业档稀缺;体量堪比西班牙波 DMI 但谱更聚焦安防

> 诚实边界：出货量/订单信息、客户反馈若无公开来源一律写「无公开」，不编造；在用品牌未获客户本人确认前一律视为【假设】。

## 需求与场景（推断标签）

- **推断需求面**：PoE 接入供电
  - PoE 接入供电：【推断】依据 CSV 信号/深挖

## HR 与规模信号（招聘/团队/绿旗）

- 暂无可核实的招聘/团队规模公开信号（LinkedIn 员工枚举登录墙外不可见，2026-09-28 纪律）。

## 联系方式（已有/猜测分标）

- **邮箱**：sklep@eltrox.pl
  - 状态：既有/公开
- **电话**：34 333 57 04
- **原始联系字段**：34 333 57 04 / sklep@eltrox.pl
- **验证口径**：MX/DNS 级核验（域存活=可投递到域）；沙箱 SMTP RCPT 被拒，用户级不验——「有 MX 记录 ≠ 邮箱存在」，2026-09-28 用户确认按此口径执行。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Zbigniew Dąbrowski | Prezes Zarządu（主席） | 经 eltrox.pl/finanse@eltrox.pl | aleo/KRS 双源实名 | https://aleo.com/int/company/eltrox-pl |
| Barbara Otolińska | 大股东（90%) | 同上 | 同源 | 同上 |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W（24口 PoE + 4×10G）），备选型不进邮件。

### 第 1 次跟进 · 守档 D+3 · 安防安装商随单页

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「安防巨头的监控/报警安装商随单 PoE 走量位」:STC-424 做 40 门店架的 24 口 280W 安装商档,批发号+dropshipping 管道对口
- **要问的问题**：你们的监控/报警安装商客户,24 口管理型 PoE+ 现随哪家?门店架上 value 档有位吗?
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 2 次跟进 · 守档 D+14 · sklep@eltrox.pl 开口

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「安防巨头的监控/报警安装商随单 PoE 走量位」:STC-424 做 40 门店架的 24 口 280W 安装商档,批发号+dropshipping 管道对口
- **要问的问题**：你们的监控/报警安装商客户,24 口管理型 PoE+ 现随哪家?门店架上 value 档有位吗?
- **随附/动作**：随附 1 页特性对照/测试包说明

### 第 3 次跟进 · 守档 D+30 · 果归守档

- **推什么**：STC-424XGGPM-280W（统一口径=P1 系列，不外溢）
- **切入点**：开口角度=「安防巨头的监控/报警安装商随单 PoE 走量位」:STC-424 做 40 门店架的 24 口 280W 安装商档,批发号+dropshipping 管道对口
- **要问的问题**：你们的监控/报警安装商客户,24 口管理型 PoE+ 现随哪家?门店架上 value 档有位吗?
- **随附/动作**：随附 1 页特性对照/测试包说明


## R55 再发掘要点（深挖 · 全文见原始 JSON）

> 调研日期 **2026-10-07(R65 第 13 批精修 = R57 转写 + 本轮登记新挖)**；原始记录：`batch/B类深挖_2026-10-07_R65_第13批.json`；价格均为 EXW 快照。

- **背景深描**：ELTROX Sp. z o.o.(Częstochowa ul. Warszawska 74;NIP 6462490527, KRS 0000175807, REGON 276916481；股本 560K zł;**Zbigniew Dąbrowski = Prezes Zarządu(董事会主席)**;Barbara Otolińska 大股东（504/560 股=90%);Wiktor Dąbrowski 小股东；Michał Piotr Dawid 理事；电信设备配件谱
- **芯片与在用型号**：【推断】40 门店安防巨头=安装商客户当天提货网络;监控/报警安装商的核心随单就是 PoE 交换机;其 MikroTik 在架以路由/CRS 为主,PoE 专业档稀缺;体量堪比西班牙波 DMI 但谱更聚焦安防
- **关键人KP**：Zbigniew Dąbrowski = Prezes Zarządu(董事会主席);Barbara Otolińska 大股东（90%)
- **关注点与资质**：MikroTik（Master） 
- **优缺点SWOT**：S:安防巨头+40 门店+多渠道+1000 人 / W:谱宽采购决策分层多 / O:监控安装随单 24 口 PoE 走量位 / T:Hikvision/Dahua 绑定件挤压
- **Saga产品适配**：波兰安防巨头的监控/报警安装商随单 24 口 280W PoE 走量位(40 门店架)

### R55 证据摘录（全部保留 · 含数量）

- **【R57备护深挖证据】**Firma Eltrox Sp. z o.o. powstała…w 2000 roku. Jesteśmy największym w kraju dystrybutorem sprzętu zapewniającego bezpieczeństwo…sieci niemal 
  > Firma Eltrox Sp. z o.o. powstała…w 2000 roku. Jesteśmy największym w kraju dystrybutorem sprzętu zapewniającego bezpieczeństwo…sieci niemal 40 salonów w największych miastach Polski…501-1000 pracowników
  > 来源：https://pl.linkedin.com/company/eltrox
- **【R57备护深挖证据】**monitoring, systemy alarmowe, automatyka domowa, smart home, odnawialne źródła energii, fotowoltaika, sieci komputerowe, IT, TV i multimedia
  > monitoring, systemy alarmowe, automatyka domowa, smart home, odnawialne źródła energii, fotowoltaika, sieci komputerowe, IT, TV i multimedia…Dropshipping z hurton…Firmy instalatorskie
  > 来源：https://www.eltrox.pl/sprzet-it/sieci-komputerowe/mikrotik/akcesoria.html
- **【R65 商业登记】**ELTROX KRS 0000175807 · NIP 6462490527 · Częstochowa Warszawska 74 · Z.Dąbrowski Prezes+ B.Otolińska 90% 大股东
  > Zbigniew Dąbrowski Prezes Zarządu … Barbara Otolińska 504 udziały … ELTROX sp. z o.o. z siedzibą w Częstochowie (KRS, 0000175807 NIP 6462490527)
  > 来源：https://aleo.com/int/company/eltrox-pl

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424XGGPM-280W（24口 PoE + 4×10G） | 主场景 | $180 USD EXW（2026-09-28 快照，15 天有效，报价前核价） | 波兰安防巨头的监控/报警安装商随单 24 口 280W PoE 走量位(40 门店架) |

- **P1 规格一句话**：24口 GE PoE af/at 280W + 4×10G SFP+，L2+ 全特性含 Voice VLAN，PoE 看门狗
- **口径纪律**：档案内如出现其他型号（历史段落），以本节 P1 为准；Saga 暂无对应规格的口子（商用 PoE bt 90W / 全万兆汇聚 / 8口商用 10G 上联）**不得**现编型号，按规则继续沿用旧对照并显式标注。

## SWOT

S:安防巨头+40 门店+多渠道+1000 人 / W:谱宽采购决策分层多 / O:监控安装随单 24 口 PoE 走量位 / T:Hikvision/Dahua 绑定件挤压

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
| 决策人识别 | ✅ |
| 触达通道 | ✅ 邮箱域已验 MX |
| 现用交换品牌 | ❓ 未确认 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- **深挖专属待问（R56）**：
  - [ ] 其监控谱 PoE 交换现供价位带与品牌结构
  - [ ] dropshipping/安装商号的 MOQ 与账期门槛

- [ ] 现有交换机/PoE 品牌与型号（问法：见首触邮件第一问）
- [ ] 典型站点端口数与供电预算
- [ ] 上门/故障频次（订阅制客户的核心成本）
- [ ] 采购决策人与付款口径

## 首触邮件（英文样板 · 可直接发送）

**主题**：PoE value slot for your line

```text
Hi Eltrox team,

Poland's largest security-equipment distributor with nearly 40 stores nationwide - every CCTV and alarm installer walking your aisles needs a PoE switch on the same receipt.

We build a 24-port PoE+ managed switch (280W, L2-lite) with full English/Polish documentation. Reference: $180 USD EXW (2026-09-29) - built for the installer value tier on a security shelf, white-label friendly, wholesale and dropshipping ready.

One question: inside your monitoring and alarm catalog, which 24-port managed PoE switch rides along with camera installs today - and is there a value-tier slot on the store shelf?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
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
