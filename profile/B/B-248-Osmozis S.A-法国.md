# Osmozis S.A.

> **评级 B**　|　法国　|　档案编号 `B-248`　|　优先级 ★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：B　**Maybe** —— 不太明显，慢跟待验证
- **评级依据**：通用分销商信号，无差异化切入点，慢慢跟
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Osmozis S.A. |
| 国家 | 法国 |
| 城市 | — |
| 网站 | osmozis.com |
| 类型 | 分销（MikroTik 官方） |
| 反向信号 | MikroTik（Master） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-480XGGM（Saga） |
| 切入点 | 卖 MikroTik 但缺工业/ERPS/PoE++ → 用同价位工业线补他的产品缺口 |
| 数据来源 | 2026-09-22 |
| 原备注 | Clapiers |

## 三、人员与联系方式

- **邮箱**：support@osmozis.com
- **电话**：+33 4 11 93 27 51
- **原始联系字段**：+33 4 11 93 27 51 / support@osmozis.com

## 四、品牌与技术栈

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景**：待摸底

保持低频联系，等他出现交换机需求信号再提级为 A。

参考型号：`STI-480XGGM（Saga）`

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 备护深挖(2026-09-29 · R57-BC 轻量对齐 A · 评级不动、不出信）

**深挖三层**
- 【事实】Osmozis S.A.(法国中南部 Clapiers/Montpellier 34830 7 avenue de l'Europe):**法国第一的露营地 WiFi/IoT 运营商+自研**——自制 bornes WiFi hotspots(户外 bornes)+软件全家(OsmoGestion/OsmoVentes/OsmoPay/OsmoKey/OsmoPower/OsmoWater);CA €1M+;曾启动 Alternext 上市计划;FB 页主「opérateur majeur de réseaux Wifi et de l'Internet des Objets」
- 【推断】「自研 outdoor bornes+软件全家」血脉有力:上游自产 AP/IoT 不与我们 PoE 交换正对面;整个 bornes 组网刚需 PoE 接入交换(我们补后特正位)
- 【假设】开口角度=「露营地 bornes 组网的回程部署 PoE 位随单/OEM 后特」:STC-424 在 bornes backhaul 里（中心 narc 室）+STI-288GP DIN 轨（每个 bornes 节子服务）。P1 双联呈

**SWOT 速描**
- **S**: 法国第一露营 WiFi 运营+自牌血统
- **W**: 主路径 WiFi harvest 不是 PoE
- **O**: bornes 组网 backhaul/备触 PoE 刚需随单
- **T**: 其自研 AP 和我 outdoor 在我司面同向

**证据（quote → 来源）**
- 「OSMOZIS S.A. est opérateur majeur de réseaux Wifi et de l'Internet des Objets (IoT) dédiés aux campings」 — https://www.facebook.com/osmozis.wifi/
- 「Osmozis fabrique et installe des bornes WiFi hotspots adaptées aux terrains de campings…OsmoGestion/OsmoVentes/Wi-Fi Camping/OsmoKey/OsmoPay/OsmoPower」 — https://www.gestion-camping.com/fournisseurs-camping/646/osmozis.html

**判位备档**(参考位，评级仍 B · 不出信）
- 参考 P1: `STC-424DGGPM-280W` — 露营 WiFi 自用网络的 PoE 组网接线(bornes backhaul 位+中心接入双样）
- 第一问: 你们的 bornes 组网(backhaul + camp LAN)里,PoE 接层现供哪个 OEM？OEM 贴牌？
- 标签: 法国|Montpellier|露营WiFi|自研bornes

**备养出信稿（未触发，供后续用户启用参考）**
```text
Hi Osmozis team,

France's leading WiFi-and-IoT operator for campgrounds with your own bornes, your own software stack (OsmoGestion / OsmoPay / OsmoPower…), and a network story so good it once had you looking at Alternext - bornes everywhere, and every single one of them is a PoE load.

We build PoE switches for exactly that job: a 24-port PoE+ managed switch (280W, L2-lite, $165 USD EXW ref. 2026-09-29) for the camp LAN core, and an 8-port Gigabit industrial PoE switch (DIN-rail, fanless, -40..75C class, $74.8 EXW) for the individual borne cabinets. Full English/French documentation, fully open to Osmozis own branding.

One question: across your bornes and camp LAN installations, which PoE source are your borne boxes and the camp core running on today - and would a documented OEM unit earn a bench test?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

**待补证清单**
1. 自产 bornes 组网中 PoE 接层/回程现供(每个 bornes/共 camp LAN 中心）
2. Alternext 上市计划构成谱压力(公众化后采购单层面）

**跟进建议（守档节奏）**
- D+3 bornes PoE 接线部署页(核心+节子双联）
- D+14 样机 OEM 贴牌提案
- D+30 果归守档

<!-- BDEEP:B类深挖_2026-09-29_R57-BC_第4波 -->
## 七、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
