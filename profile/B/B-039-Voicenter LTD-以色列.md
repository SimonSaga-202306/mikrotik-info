# Voicenter LTD

> **评级 B**　|　以色列　|　档案编号 `B-039`　|　优先级 ★★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：B　**Maybe** —— 不太明显，慢跟待验证
- **评级依据**：通用分销商信号，无差异化切入点，慢慢跟
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Voicenter LTD |
| 国家 | 以色列 |
| 城市 | — |
| 网站 | voicenter.co.il |
| 类型 | 分销（MikroTik 官方） |
| 反向信号 | MikroTik（Master） |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STC-48DGGM-U（Saga） |
| 切入点 | MikroTik 官方分销，商用线可直接比价，工业线为零 → 新品类增量 |
| 数据来源 | 2026-09-22 |
| 原备注 | Tel Aviv |

## 三、人员与联系方式

- **邮箱**：info@voicenter.co.il
- **电话**：+972 72 2776 771
- **原始联系字段**：+972 72 2776 771 / info@voicenter.co.il

## 四、品牌与技术栈

**涉及品牌 / 技术**：MikroTik

## 五、跟进策略

**场景**：待摸底

保持低频联系，等他出现交换机需求信号再提级为 A。

参考型号：`STC-48DGGM-U（Saga）`

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。


## 备护深挖(2026-09-29 · R57-BC 轻量对齐 A · 评级不动、不出信）

**深挖三层**
- 【事实】Voicenter LTD(Tel Aviv Yigal Alon 159;2007 创 101-200 人,~$9.75M;**判型翻转=云 VoIP PBX/呼叫中心运营商(非分销)**——自营 5-7 个全球电信数据中心(美/欧/亚/澳/以);CEO Nitzan Gutman;创始人 CTO **Shlomi Gutman 曾在 MUM NL16 登台讲 MikroTik debug VoIP**(技术圈实名);阿姆斯特丹 QXIP 姐妹公司(开源语音);Master 挂证应源自其企业客户部署配送 MikroTik CPE
- 【推断】云通信运营商:企业客户桌面全是 **PoE IP 话机**——其托管部署/混合方案里 PoE 交换随单是天然场景;技术型 CTO 曾在 MikroTik MUM 演讲=懂硬件
- 【假设】开口角度=「云 PBX 部署的桌面话机 PoE 交换随单/OEM」:STC-424 以其企业部署/托管 CPE 场景的 PoE 位入,具名技术型团队开口(引其 MUM 演讲背书)

**SWOT 速描**
- **S**: 2007 老牌+全球 5-7 DC+技术型 CTO(MUM 演讲者)
- **W**: 运营商本体,不零售硬件
- **O**: 桌面话机 PoE 部署随单/OEM 白标
- **T**: 自研中心,硬件谱敏感

**证据（quote → 来源）**
- 「cloud-based VoIP PBX & call center service providers, and operates five telecom data-centers, distributed worldwide…since 2007」 — https://www.zoominfo.com/c/voicenter/461174517
- 「Shlomi Gutman, CTO of Voicenter…Founder and CTO…How to debug, troubleshoot and monitor VoIP using MikroTik (MUM NL16 presentation)」 — https://mum.mikrotik.com/presentations/NL16/presentation_3876_1479372782.pdf

**判位备档**(参考位，评级仍 B · 不出信）
- 参考 P1: `STC-424DGGPM-280W` — 云 PBX 运营商企业部署的桌面 IP 话机 PoE 交换随单/OEM 白标位(同 SEWAN 逻辑,技术型 CTO 具名开口)
- 第一问: 你们企业部署/托管场景里,桌面 IP 话机的 PoE 交换现随哪家?白标 OEM 件可谈吗?
- 标签: 以色列|特拉维夫|云PBX运营商|5DC|MUM演讲CTO

**备养出信稿（未触发，供后续用户启用参考）**
```text
Hi Shlomi, hi Voicenter team,

Five telecom datacenters worldwide, an open-source telephony DNA, and a CTO who has literally stood on the MUM stage teaching VoIP debugging on MikroTik - you understand exactly what happens on the wire.

Every hosted-PBX customer desktop you deploy is a PoE phone load. We build a 24-port PoE+ managed switch (280W, L2-lite) with full English documentation. Reference: $165 USD EXW (2026-09-29) - built for carrier deployment fleets, fully open to Voicenter white-label.

One question: in your enterprise and hosted deployments, which PoE switch feeds the desktop phone fleets today - and would a documented OEM unit earn a lab test in your datacenter bench?

If useful, I can send one unit with the complete test pack. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

**待补证清单**
1. 企业部署随单 PoE 件现供与 OEM 白标开放度
2. 其客户桌面话机谱(Yealink/Poly?)PoE 功率需求

**跟进建议（守档节奏）**
- D+3 话机 PoE 部署随单页
- D+14 info@voicenter.co.il 具名 Shlomi
- D+30 果归守档

<!-- BDEEP:B类深挖_2026-09-29_R57-BC_第9波 -->
## 七、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*
