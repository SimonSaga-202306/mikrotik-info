# Controller Service and Sales

> **评级 B**　|　美国　|　档案编号 `B-340`　|　优先级 ★★　|　状态：未触达

---

## 一、评级与结论

- **评级**：B　**Maybe** —— 不太明显，慢跟待验证
- **评级依据**：有信号（交换专长、工业/楼宇）但需先验证需求或联系人不具体
- **下次复核**：收到反馈后重新评级

## 二、公司概览

| 项 | 内容 |
|---|---|
| 公司名 | Controller Service and Sales |
| 国家 | 美国 |
| 城市 | — |
| 网站 | controllerservice.com |
| 类型 | 分销（Moxa 授权） |
| 反向信号 | Moxa 授权分销商，Moxa SDS-3008 系列工业智能交换机用户手册扉页标注其为 Authorized Distributor |
| 是否自有品牌 | 否 |
| 首推 Saga 型号 | STI-488XGGPM（Saga） |
| 切入点 | 台厂渠道话术 |
| 数据来源 | Moxa 渠道名录（经销商定位法） |
| 原备注 | sales@controllerservice.com；电话 (800) 584-5565。【2026-09-22 补】经 Moxa 渠道名录确认为 Moxa 官方分销商（台厂 Moxa 旗下欧洲/北美渠道）。 【2026-09-28 R49 复筛补录】来源等级：official-company。站点 HTTP 500，本轮无法核验（失败站重试）：controllerservice.com 直连返回 HTTP 500（连续复现，本轮无法核验站点内容） 结论：维持 B（无采购/替换新证据）。 证据：[1](https://www.controllerservice.com/)；批次：batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json#B-340 |

## 三、人员与联系方式

- **邮箱**：sales@controllerservice.com
- **电话**：—
- **原始联系字段**：官网联系页

## 四、品牌与技术栈

**涉及品牌 / 技术**：Moxa

## 五、跟进策略

**场景**：工业 / 楼宇自控

发工业线资料（宽温 / 导轨 / ERPS），问现场工况和认证要求，缺认证就别浪费时间。

参考型号：`STI-488XGGPM（Saga）`

## 六、注意点

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**，只是信号源。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据。
4. 大集团先问清采购层级（国别 vs 集团统一）。
5. 样机先送测，再谈价格。

## 备护深挖(2026-09-29 · R57-BC 轻量对齐 A · 评级不动、不出信）

**深挖三层**
- 【事实】Controller Service and Sales（马萨诸塞 Avon）：电气/自动化老牌分销=Moxa 授权官方分销商（Moxa 手册页印出"Your Authorized Distributor")；在架 ABB/Eaton Cutler-Hammer/IDEC/Moxa/Hammond/Puls/Datalogic/Honeywell/Ferraz；Moxa EDS-G512E-4GSFP $1,399、EDS-G516E-4GSFP $1,749 直接印刷价在页
- 【推断】纯工业自动化 VAD 谱（电柜件全家）;Moxa 工业交换线（$1,399 档）下演了价值空档——我们的 STI-288GP $74.8 可入 DIN 轨 value 位
- 【假设】自动化件的客户工柜里，PoE 网线是次生子系统——从「Moxa 主干环之外那些非核子装口」入手，他宁可用 value 档

**SWOT 速描**
- **S**: 电气/自动化深谱+价锚透明
- **W**: Moxa 铁忠+厂牌框架固化
- **O**: STI-288GP 入非主环路岗位 DIN 轨空档
- **T**: Moxa 厂方制圈导账期/让利

**证据（quote → 来源）**
- 「Your Authorized Distributor is: Controller Service and Sales…(800)584-5565」 — https://www.controllerservice.com/content/downloads/moxa/user_manual/Moxa_Industrial_Smart_Ethernet_UM_e1.0.pdf
- 「MOXA EDS-G512E-4GSFP…$1,399.00ea / EDS-G516E-4GSFP…$1,749.00ea」 — https://www.controllerservice.com/index.jsp?path=home&pgl=false

**判位备档**(参考位，评级仍 B · 不出信）
- 参考 P1: `STI-288GP` — Moxa 授权老分销+在架千美元档：value DIN 轨 8 口（$74.8）入子位置最对口
- 第一问: 你们的电柜项目里，那些非主环路的 PoE 点（视频/传感支线）现用什么 value 解决？
- 标签: 美国|马萨诸塞|Moxa老牌|电气自动化VAD

**备养出信稿（未触发，供后续用户启用参考）**
```text
Hi Controller Service team,

Authorized ABB/Eaton/IDEC/Moxa on one wall - that's a control cabinet distribution DNA we recognize. Not every PoE endpoint in those cabinets deserves a four-figure switch.

We build an 8-port Gigabit industrial PoE switch (DIN-rail, fanless, -40..75C class) with full English documentation. Reference: $74.8 USD EXW (2026-09-29) - built exactly for the auxiliary PoE runs next to your Moxa backbone lines.

One question: for the non-ring, auxiliary PoE endpoints in your control cabinet projects, which value-side switch are you standardizing on today?

If useful, I can send one unit with the complete test pack (surge 6 kV, EFT/ESD data sheet, cold-start log). If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE switch OEM/ODM
```

**待补证清单**
1. 在架 Moxa SDS-3008(unmanaged value 段）与 EDS 的中空价值区间位置
2. 电气柜侧哪些子件（ABB/IDEC/Hammond）的装里 PoE 点最多

**跟进建议（守档节奏）**
- D+3 对比表 STI-288GP vs Moxa SDS-3008（价/温宽/口数）一页
- D+10 样机+冷热启动测试包
- D+30 无果归档观察

<!-- BDEEP:B类深挖_2026-09-29_R57-BC_第1波 -->
## 七、跟进记录

| 日期 | 方式 | 我方动作 | 对方回应 | 下一步 |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- 有新进展时把内容告诉我，我来更新本档案并重评级 -->

---

*建档日期：2026-09-22　|　数据来源：客户名单_反向信号_2026-09.csv*

## 2026-10-07 R64 KP 猎捕（B 类第 1 批）

**结论**:Avon MA,38 员工;Michael Sandonato 销售市场总监
**域 MX**:{"controllerservice.com": ["controllerservice-com.mx1.arsmtp.com", "controllerservice-com.mx2.arsmtp.com"]}
- **Mark O'Day** — President(2005 至今,三代家族;祖父 1926 创立;Brown AB+Chicago MBA)（源:https://www.dnb.com/business-directory/company-profiles.controller_service__sales_co_inc.65ac94bbcbb878dab554ba6fd7598a67.html）
  - `mark@controllerservice.com`(first@(controllerservice.com))
  - `mark.o'day@controllerservice.com`(first.last@(controllerservice.com))
  - `m.o'day@controllerservice.com`(f.last@(controllerservice.com))
  - `marko'day@controllerservice.com`(firstlast@(controllerservice.com))
  - `mo'day@controllerservice.com`(flast@(controllerservice.com))
  - `o'day@controllerservice.com`(last@(controllerservice.com))
- **Scott O'Day** — VP Sales and Marketing(兄弟共管)（源:https://rocketreach.co/controller-service-sales-inc-management_b5fee96bf60669ae）
  - `scott@controllerservice.com`(first@(controllerservice.com))
  - `scott.o'day@controllerservice.com`(first.last@(controllerservice.com))
  - `s.o'day@controllerservice.com`(f.last@(controllerservice.com))
  - `scotto'day@controllerservice.com`(firstlast@(controllerservice.com))
  - `so'day@controllerservice.com`(flast@(controllerservice.com))
  - `o'day@controllerservice.com`(last@(controllerservice.com))
- **Jim Long** — Corporate Controller（源:同 RocketReach 源）
  - `jim@controllerservice.com`(first@(controllerservice.com))
  - `jim.long@controllerservice.com`(first.last@(controllerservice.com))
  - `j.long@controllerservice.com`(f.last@(controllerservice.com))
  - `jimlong@controllerservice.com`(firstlast@(controllerservice.com))
  - `jlong@controllerservice.com`(flast@(controllerservice.com))
  - `long@controllerservice.com`(last@(controllerservice.com))
