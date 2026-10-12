# MADER.cz

> **评级 C**　|　捷克　|　档案编号 `C-040`　|　优先级 ★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：C　**Too hard** —— 太难（大公司 / 集团 / 自有品牌 / 竞品 / 区域外），**先放着不动，精力只给 A**
- **评级依据**：【2026-09-23 复核下放】无邮箱（群发触达不到），按「B 只做群发」原则沉 C 待命；全量信息保留，出现以下任一情形可重评：①补到邮箱 ②对方主动询价 ③出现 EOL 替换需求 ④冒出内部联系人。原判：有信号（PoE/监控/门禁、工业/楼宇）但需先验证需求或联系人不具体
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | MADER.cz |
| 国家 | 捷克 |
| 城市 | — |
| 网站 | mader.cz |
| 类型 | 电商 |
| 反向信号 | 工业PoE |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-288GP（Saga） |
| 切入点 | 中性货试单 |
| 数据来源 | 反向信号/2026-09 |
| 原备注 | — |

## 三、人员与联系方式

- **邮箱**：—
- **电话**：—
- **原始联系字段**：官网

## 四、品牌与技术栈

**涉及品牌 / 技术**：（未记录）

## 五、跟进策略

集团 / 大公司，决策链长、采购集中。

**切口**：先问清是国别决策还是集团统一采购；**找品类经理，不要找 CPO**。

> **C 级细分：`B下放·无邮箱（群发触达不到）`**

> ⛔ **Too hard pile**：本条进「太难」堆，**当前不投入跟进精力**，不必为它写开发信或做方案。
> 信息已**全量留档**（本档案 + 总表 22 列），待出现明确触发条件再捞出来重评：
> ① 对方主动询价；② 出现停产替换需求；③ 我方补齐对应认证；④ 你从别处拿到其内部人线索。

## 六、R73 A/B标准深度调研与加厚（仅研究，不触达）

> 调研日期 **2026-10-12**；原始批次：`batch/C类AB标准加厚_2026-10-12_R73_第2批.json`；按公司名+国家绑定，档案编号采用当前 CSV 编号 `C-040`。

- **法定主体与网站身份**：MADER 联系页自列经营主体 MADER s.r.o.、IČO 64793419、DIČ CZ64793419；CSV 使用的网站/商号为 MADER.cz。该信息来自公司官网联系页，本轮没有额外核验其财务、员工或集团结构。
- **业务模式与品类广度**：MADER 首页将网站描述为电脑/笔记本/显示器销售与维修，并公开呈现汽车、家电、照片与安防、组件/网络/办公、手机、电脑、体育/健康/园艺/工具等广泛零售品类；支持综合电商定位，不足以认定其是工业网络系统集成商。
- **TP-Link 工业交换机商品证据**：MADER 网店列 TP-Link Omada IES210GPP Easy Managed 10 口千兆工业交换机：8×RJ45（2×PoE++、6×PoE+）+ 2×RJ45/SFP combo，240W 总 PoE、-40…+75°C、IP40、DIN/壁挂；页面显示 6,350 CZK 含税/5,248 CZK 未税、60 个月保修，抓取时标“网店有货”，提示仅按 1 件计算。
- **另一个工业 SKU 与库存边界**：MADER 网店还列 DIGITUS DN-650107 工业 PoE 交换机：4×10/100 PoE + 1×10/100 上联、802.3af/at、48–57VDC 冗余电源、-40…+85°C；抓取时页面标记“不可用”，展示价格 1,525/1,260 CZK（含税/未税）。产品列表不等于当前有货或持续供应。
- **采购/集成能力**：当前核到的是零售目录页，而非面向系统集成的项目案例、系统设计服务或公开批量采购记录。本轮所查页面未找到可明确归属 MADER 的工业交换机集成项目；这是检索范围内未发现，不证明公司从不承接相关业务。
- **关键人/供应商准入与联系边界**：联系页可识别公司法定主体，但没有公开交换机品类买手、供应商准入流程、采购负责人或年采购量；零售客户服务/商品页面不能当采购决策人。无任何联系、邮件、电话或商品询价。
- **商品价格/库存口径**：IES210GPP 与 DN-650107 的公开价为 MADER 网店零售页面时点价格，不是批发价、实际成交价、采购成本或对 Saga 可比报价；IES210GPP 的库存提示限定为单件，DN-650107 抓取时不可用。动态价格与库存须带日期，不能推断销量。
- **优势与风险（SWOT）**：优势：捷克本地综合网店、公开商品价格/保修/库存状态，当前至少一款 TP-Link 工业 PoE 交换机可见网店单件库存。风险：工业网络产品只是跨品类零售的一部分；未见工业集成/项目和规模采购证据；SKU 库存动态，另一个工业型号抓取时不可用；无供应商开放或新品引入线索。
- **Saga 适配与竞合判断**：MADER 可作为零售货架/公开价格监测对象；IES210GPP 与 DN-650107 的产品目录与 Saga 部分工业 PoE 型号交叠。但本轮不足以支持“工业分销客户”或批量采购结论，也没有低价、第二来源或替代需求证据；维持 C。
- **证据边界与合规**：主体/类别来自 MADER 官网；产品参数、价格和库存来自 MADER 商品页，按 2026-10-12 抓取快照使用。公开零售售卖只证明展示/网页状态，不证明销量、采购价、库存可持续性、客户项目或采购意向。只研究、不触达、不改评级或主表。

### R73 原文证据摘录（全部保留）

- **【法定主体/登记号码（公司联系页）】**MADER 联系页自列法定经营主体 MADER s.r.o.、IČO 64793419、DIČ CZ64793419；CSV 名称为网站商号 MADER.cz。
  > Mader s.r.o.
  > IČO: 64793419
  > DIČ: CZ64793419
  > 来源：https://www.mader.cz/kontakty
- **【综合零售品类】**MADER 首页同时列汽车/摩托、大小家电、照片/安防、组件/网络/办公、手机、电脑、体育/健康/园艺/工具等跨品类分类，支持综合零售商定位，不证明工业集成能力。
  > KATEGORIE
  > AUTO - MOTO
  > ELEKTRO BÍLÉ VELKÉ
  > ELEKTRO MALÉ, TV
  > FOTO, ZABEZPEČENÍ
  > KOMPONENTY, SÍTĚ, KANCELÁŘ
  > MOBILNÍ TELEFONY
  > NOTEBOOKY a POČÍTAČE
  > SPORT, ZDRAVÍ, KRÁSA, HOBBY
  > ZAHRADA, NÁŘADÍ, DŮM
  > 来源：https://www.mader.cz/
- **【TP-Link IES210GPP 网店价格/库存/保修快照】**MADER 商品页列 IES210GPP，页面价格 6,350 CZK 含税/5,248 CZK 未税、保修 60 个月；抓取时显示“网店有货”，库存说明明确按 1 件计。仅为当日零售网页快照。
  > IES210GPP Omada Industr Easy man.switch
  > 6350 Kč
  > 5248 Kč bez DPH
  > Dostupnost: Skladem v eshopu
  > Záruka: 60 měsíců
  > Zboží máme skladem, odesíláme následující pracovní den (pokud není uvedeno jinak), platí pro 1ks
  > 来源：https://www.mader.cz/tplink-omada-10port-gigabit-industrial-easy-managed-switch-with-6port-poe-and-2port-poe
- **【TP-Link IES210GPP 端口/PoE/工业环境规格】**商品页将 IES210GPP 描述为 10 口千兆工业 Easy Managed；8×千兆 RJ45（2×PoE++、6×PoE+）+ 2×RJ45/SFP combo，PoE 预算最高 240W、-40…+75°C、IP40，可 DIN/壁挂。网页卖家规格尚未按生产商正式数据表独立复核。
  > Omada 10portový gigabitový průmyslový Easy Managed switch se 6 porty PoE+ a 2 porty PoE++
  > 8× gigabitových RJ45 portů (2× PoE++, 6× PoE+)
  > 2× kombinované gigabitové RJ45/SFP sloty
  > Napájecí rozpočet 240 W*
  > Provozní teplota -40 °C až 75 °C
  > Odolné hliníkové pouzdro s krytím IP40 a možností montáže na DIN lištu nebo na stěnu
  > 来源：https://www.mader.cz/tplink-omada-10port-gigabit-industrial-easy-managed-switch-with-6port-poe-and-2port-poe
- **【DIGITUS DN-650107 工业 PoE 目录/不可用状态】**MADER 另列 DIGITUS DN-650107 4×10/100 PoE + 1×10/100 上联，支持 802.3af/at、冗余 48–57VDC、-40…+85°C；抓取时状态为不可用。价格为当日网页展示，SKU 列表/价格不等于当前可供库存。
  > Digitus DN-650107 DIGITUS Professional Industrial 4-Port Fast Ethernet PoE Switch + 1 uplink port
  > 1525 Kč
  > 1260 Kč bez DPH
  > Dostupnost: Nedostupné
  > 4 x 10/100Base-TX Ethernet PoE porty
  > 1 x 10/100Base-TX Ethernet uplink port
  > Podporuje IEEE802.3af/at
  > Redundantní napájení: 48~57 V DC
  > Rozšířený rozsah provozních teplot, -40 °C ~ +85 °C
  > 来源：https://www.mader.cz/digitus-professional-industrial-4port-fast-ethernet-poe-switch-1-uplink-port

### R73 本轮评估

保持 C。R73 确认 MADER s.r.o. 的官网法定标识、跨品类电商定位和两款工业 PoE 交换机商品页；其中 TP-Link IES210GPP 抓取时显示一件网店库存，DIGITUS DN-650107 抓取时不可用。零售页面及单件库存不证明系统集成、销量、批量采购、采购成本或 Saga 供应商需求。未找到可归属于 MADER 的工业交换机集成案例或公开采购意向；未联系客户、未改主表/评级。

### R73 后续核验步骤（不代表已获采购意向）

- 如继续公开核验，只按品牌方正式数据表复核 IES210GPP、DN-650107 的精确版本/认证，并在后续记录动态页面日期；不以零售价替代批发或采购成本。
- 如研究采购可能性，只保留供应商准入、批量价格、真实可供库存、采购人和工业项目等为未知；本轮不询价、不提交网站表单、不联系 MADER。

### R73 待核事项与证据边界

- MADER 实际员工数、营收、工业网络业务占比、批发/系统集成业务及工业交换机销量。
- IES210GPP 页面显示单件库存的持续时间、实际成交价、采购成本、补货周期和客户销售记录。
- DIGITUS DN-650107 的恢复供货/停售状态及当前制造商替代型号。
- 是否接纳工业交换机新品牌、供应商审核/准入方式、批量起订量、采购决策人/采购量。
- 是否存在其他公开项目或终端客户采用 MADER 工业交换机；本轮核查页面未发现，不能据此断言不存在。

## 七、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 八、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
