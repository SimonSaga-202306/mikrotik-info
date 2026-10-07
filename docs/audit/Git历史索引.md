# Git 历史索引

> 时间为Git committer timestamp，不是用户消息时间、网页发布时间或服务器观测时间。
> 只检索了可达本分支历史及客户CSV历史；不读取凭证、Git内部对象原文或已删除的不可达对象。

| Commit | 提交时间（原始时区） | 说明 |
|---|---|---|
| `92837c70106b` | 2026-10-07T13:33:16+00:00 | R65 第 2 批精修:B 类 4 无邮箱户 KP+facts 叠加(Kjellsson VD 双源自曝) |
| `db45d3f11144` | 2026-10-07T13:24:57+00:00 | R65:B 类全量 167 户升 v2 骨架(对齐 A 类标准;R57 备护深挖忠实转写) |
| `816063385afa` | 2026-10-07T12:47:53+00:00 | R64 收尾:12 户 KP 点名首触定制稿 + B 类 KP 猎捕第 1 批 14 户 + 总账 |
| `29696696a919` | 2026-10-07T12:16:48+00:00 | R64 收尾:测试白名单补丁+xlsx全量重导 ①tests 补 R63_BOUNCED(退信 8 户 入口/备注)白名单四层挂接+R63_PROMOTED/R61_REPLIED/R62_BOUNCED 入 xlsx 对比 skip 集 ②xlsx 两张(分级跟进表 A580/B167/C290+对照表反向信号名单 1037)按现行 CSV 重导 ③总账轮次计数 63→65 ④audit re-hash;29/29 OK 全过 0 skip+errors=0 |
| `2fe838493b4c` | 2026-10-07T12:06:23+00:00 | R64 KP猎捕第1波(R63新升12户)+A-575/576/581预留升级户复用: ①web_search 定 15 位 KP(含 etree 创始人CEO Twonski、Vodanet Founder Krakus+Purchase Mgr İhsan Aslan、EDOX 采购负责人 Weckerle、PEC 50%业主 Peter Jezernik、art2soft MD Thomas Thoma、Nim Wave Presidente Zito、Ronitek Tomer Shitrit)②scripts/R64_KP猎捕.py:6模式邮箱排列组合+域MX核验(115 候选全 MX 存活;SMTP 用户级沙箱不可验标 guessed-leads-only 不进群发)③12 档 profile 注入 R64 KP 节+A-571/A-578 人名待定 ④batch/KP猎捕_A_R64_第1波.json 落账 ⑤tests 注释 A-575/576/581 三号预留;29 tests OK+audit errors=0 |
| `0ad6ba2ba237` | 2026-10-07T11:49:03+00:00 | R63 退信9户处置+B类升A 12户(B-037/038/105/152/160/220/223/238/270/390/401/422→A-570..584): ①退信9户按 R58/R62 规则:永久 dead 7(A-342 R62 期满满止转永久/A-496/A-499/A-500 server-misconfigured/A-563/A-539/A-516 domain-not-found)+观察46h 2(A-441/A-457)+A-123 PASS 用户裁定;②B→A 升筛:R53 复筛 JSON 283 记录中抓取失败类 27 户→web_search 重核 26 户→12 户达标升 A(编号 A-570~A-584,A-575/576/581 腾空:B-171 SICE=B-489/B-190 wifihw=A-494/B-318 mikrotik.ro=A-527 库内已升);③STRUCT 568→580,A 档 v2 模板重构+R57-BC/R63 节保留;④tests 加 R63_PROMOTED/R63_PROMOTED_NEW/R63_PROMOTED_FIELDS,A 568→580/B 179→167 数适配;⑤audit errors=0/29 tests OK(skipped=5 浅克隆基线) |
| `5e7fb057dfba` | 2026-10-06T05:28:10+00:00 | R62 follow-up: rebase 残留 markers 清理修复+测试白名单收尾 ①tests/test_repository.py 4 段 conflict markers 清(R61+R62 双并保留) ②28 个 marker 文件逐文件接管 cdfe736 端正确版 ③tests R61_REPLIED_FIELDS 加『网站』(A-311 https://www.fikesmedia.com 填为空→filled 差异放行)/R62_BOUNCED_FIELDS 加『评级依据/网站/状态』覆盖 A-311/A-337/A-342/A-355 场景 ④audit re-hashes 后 29/29 OK(全过,无 skip)+errors=0/customers=1037 |
| `59703e8c28a7` | 2026-10-06T05:12:35+00:00 | R62 A-311入库+GPT讨论归档+退信批+4户补录: ①A-311 Fikes Media stage 00→02-replied(12分钟 Owner亲回 interested·问定制/API/规格),跟进记录3行,R62深挖节(GPT结论:技术评估阶段·API不答有无先拿需求·假期风控),复核 2026-10-08 ②GPT讨论归档:A-069 建议入 CRM v2.1 候选(Relationship Score/Success Path/Knowledge Contribution/Partner Type,本档案首版在 A-311 示范) ③退信 10 户按 R58 规则处置:A-170/123/355/424/434/439/458/476/088 永久 dead 标发不过去+替代路径(乌克兰守界只标注不主动挖);A-337 备注(fabio.mundadori7114@ingesw.onmicrosoft.com M365 tenant 猜测直邮被退);A-342 tnet 45h retry 观察 ④4 户人工新邮箱补录:A-251 beszerzes@macsoft.hu/A-258 biuro@csidet.edu.pl(均用户官网核验,level 升级 user-website-verified-2026-10-04,profile/STRUCT/CSV/生成器基线四端同步)/A-487 nfo@→info@marcomweb.it typo/A-520 support@axbyte.se 补作替代通道(与 A-064 同源) ⑤tests 加 R62 白名单(A-251/A-258 level 升格,R62 退信抽样跳过);29/29 OK+audit errors=0/customers=1037 |
| `99a24921eacf` | 2026-10-03T09:08:54+00:00 | R61 型号价格统一+A-069深挖(基于 R60 基座重放): ①全库 STC-424DG→STC-424XG 规整(DG=2.5G 应为 XG=10G):DGGPM-280W / DGGPM-440W / DGGM(非PoE) 累计 5383处 → XG,Saga产品目录 4×2.5G→4×10G 同步修 ②全库 $165→$180 主推款统一 3690处(Saga 历史 xlsx 原文、r55_sagify 内部历史快照不动) ③A-069 Gmail 4 轮邮件归置:profile 跟进记录+02-replied,R61补档(Bitflux Head of Technical/Service Operations·AS37714·AFRINIC IF3-AFRINIC·学历 Ilorin+MBA·认证 MTCNA/MTCRE)+CSV/STRUCT/xlsx 反向信号名单重导(Gmail PDF 源 main) ④scripts/R61_型号价格统一.py 入库;⑤tests 新增 R61_REPLIED_FIELDS/SAGIFY_R61 双链路归一化(A-069 行按白名单 A/B 两端 normalize);29/29 OK+audit errors=0/customers=1037 |
| `4221a0680199` | 2026-10-02T17:04:49+00:00 | R60 测试与导出收尾: CSV「未测试投递」清除行纳入冻结基线测试放行(r60_untested 逐行精确放行 入口/联系方式+备注 两字段)+xlsx 反向信号名单 sheet 按 R60 CSV 重导(A568/B179/C290/1037行)+A-103 退信标注位置修正(坏邮箱 uk@ 而非 sales.uk@); 29/29 OK |
| `407dd8db81f6` | 2026-10-02T16:55:07+00:00 | R60 合并 R59 双亲: R59 两项处置(资产池审核+A类三大优化)内容已含于本 tree;R60 A类运营判定注入为主方向 |
| `5e1fac83d9c3` | 2026-10-02T16:49:53+00:00 | R60 A类运营判定注入(仅A类568户,改内容不改顺序): ①KP领英直达注入每户R60区块(36户直链+440人名搜索+92公司搜索) ②全仓清除「未测试投递」标注(profile 53处+CSV 62处+batch JSON 39文件+docs/audit+溯源) ③5户退信标准化「发不过去+找新邮箱方法」 ④每户注入三项判定:中国进口与管制(国别烈度+户级信号/待定)、芯片谱Marvell专注度(六桶判定/待定首开问)、大概率Saga型号(needs判定,注明非开发信型号) ⑤batch/A类_三项判定与KP领英_R60_2026-09-29.json 568键落盘+scripts/R60_A类运营判定注入.py入库; 29/29 OK |
| `4da509705d59` | 2026-09-29T13:17:04+00:00 | R59 A类三大优化交付: ①docs/sales/A类_Saga型号速查(568户×型号双视图,STC-424DGGPM-280W 408户/STC-28DGGPM 57户/STI-288GP 36户/STI-480XGGM 1户/CONSULT-OEM 66户) ②docs/sales/A类_中国进口与管制风险(21国烈度档+82户中国品牌命中+美74户ImportYeti指引) ③docs/sales/A类_芯片Marvell专注度(91.9%已挂Marvell锚/Broadcom仅2户/Qualcomm仅2户/42户无信号/工业锚34户) +批JSON支持; 29/29 OK |
| `045dcb2137a5` | 2026-09-29T13:01:48+00:00 | R59 资产池审核处置: B-233/A-373 真重复合并(B-233旧→B-234、A-373旧→A-369),尾号复用(B-536→B-233 Tech Atlantix、A-569→A-373 Network Devices);A-205/B-200/B-295/A-568 四户 ★★★→★★;OEM Automatic 集团三分档互链(B-295 主档);CSV 1039→1037(A=568/B=179/C=290);溯源索引/structured_profiles/索引/总账 R59 段同步;29/29 OK |
| `2bde21b408ef` | 2026-09-29T12:21:14+00:00 | 客户资产池审核体系 2026-09-29: audit_customer_assets.py(749 户 A/B 对称+编号/邮箱/评级联动/疑似重复 12 维扫描,P0-P3 分级)+首轮报告(发现真重复 2 对 B-233/B-234、A-369/A-373 待合并;★★★ 无触达 4 户 A-205/B-200/B-295/A-568 待处置;同源集团分档 4 组待裁决) |
| `ead93797e31a` | 2026-09-29T11:32:26+00:00 | R58-BC 第1波 B-536 Tech Atlantix 深挖补齐(B 类 180/180 覆盖)+退信批 5 户处置落 CSV(A-054/096/101/103/105 联系方式+备注替代通道) |
| `592cb5db14fc` | 2026-09-29T10:56:16+00:00 | R58 竞品谱系挖客户第1波: 入库 6 户(A-568 Purdicom/A-569 Network Devices 深挖 v2 + B-536 Tech Atlantix + C-371/372/373 评估直入库);CSV+6行=1039;STRUCT覆盖;索引/xlsx/溯源/总账同步;R59轮次断言扩列 |
| `0bf3dbb9a121` | 2026-09-29T09:55:16+00:00 | R57 补记: 总账第57轮归档(B类深挖179/179全清)+索引深控件注+测试断言扩列 |
| `6ae8bf6b4810` | 2026-09-29T09:46:41+00:00 | R57-BC 第12波: B类收官 17 家深挖加厚(B类 179/179 全清) |
| `3b172732cf06` | 2026-09-29T09:46:24+00:00 | R57-BC 第11波: B类东南欧+高加索 20 家深挖加厚(162/179 完成) |
| `5d3a9dbbc133` | 2026-09-29T09:20:31+00:00 | R57-BC 第10波: B类中欧 20 家深挖加厚(142/179 完成) |
| `0a3fee3f3635` | 2026-09-29T09:11:59+00:00 | R57-BC 第9波: B类北欧+北美+以色列+冰岛 22 家深挖加厚(122/179 完成) |
| `e5812c80cbcc` | 2026-09-29T08:58:30+00:00 | R57-BC 第8波: B类荷兰7家+波兰6家深挖加厚(100/179 完成) |
| `3a063982f251` | 2026-09-29T08:50:51+00:00 | R57-BC 第7波: B类英国 9 家深挖加厚(87/179 完成) |
| `b18e1344a5ff` | 2026-09-29T08:39:21+00:00 | R57-BC 第6波: B类西班牙 11 家深挖加厚(78/179 完成) |
| `ec152812cce7` | 2026-09-29T08:29:05+00:00 | R57-BC 第5波: B类德国4家+意大利9家深挖加厚(67/179 完成) |
| `b966464676e4` | 2026-09-29T08:17:19+00:00 | R57-BC 第4波: B类法国 13 家深挖加厚(54/179 完成) |
| `bbe3f8b0b445` | 2026-09-29T07:59:09+00:00 | R57-BC 第3波: B类希腊 13 家深挖加厚(41/179 完成) |
| `20e53ccaf768` | 2026-09-29T07:49:27+00:00 | R57-BC 第2波: B类乌克兰 13 家深挖加厚(战争敏感守界句统一注记) |
| `717158292fb5` | 2026-09-29T07:30:27+00:00 | R57-BC 第1波: B类美国 15 家深挖加厚(A 规则轻量对齐,评级不动) |
| `19395ffef267` | 2026-09-29T06:50:54+00:00 | R57-复盘: 退信台账+关联实体群+三层十维入MD+深度入库审计(19项全绿) |
| `a0b92a30b078` | 2026-09-29T06:25:27+00:00 | A类全谱复盘修复(567档):①批55-56后未重渲染→R55小节/跟进/邮件并入27家MD;②R54 frozen计划440W停编档加现行对照注记(原文冻结不动);③A-275判位自洽改STC-424(原CONSULT-OEM与$165窄针矛盾);④A-514补A-516姊妹站回注;⑤13家建档供位push与p1矛盾规范化(A-272系9家+A-360系4家);⑥空tag×3补齐(A-305/329/333);⑦Unknowns小节接入R56深挖专属待问(547家);P1账本 STC406/CONSULT67/28DG57/STI36;audit 1251/0;29 tests OK |
| `403cfe69a2a5` | 2026-09-29T05:57:29+00:00 | 惯例清理：删除一次性生成器 gen_super9.py（批55-56已闭环验证） |
| `424b4cad866f` | 2026-09-29T05:56:51+00:00 | R56 第55-56批：A-541..A-567 深挖加厚 27 家=A 全谱 567/567 收官（美7+英7+荷4+西5+葡2+芬1+黑山1;STI×3:541 Marugged工业rugged守界军档·547 IcomTech工业PoE类目·556 Lextron 109项交换;553 SwitchSFP光模块→28DG随单;544 CRS328 $485/549 USW-24PoE £306/559 Campus48PoE €3397/563 Reyee €190 直接对照款;562↔564姊妹站;546 WAV巨头锚;566可再生EPC项目低密;567 R32降级注）；ENRICH55 54→56、OVERRIDES→A-567；P1账本 STC405/STI36/28DG57/CONSULT68；1033 dossiers；audit 1252/0；29 tests OK |
| `96ee12491993` | 2026-09-29T05:25:26+00:00 | R56 第51-54批：A-501..A-540 深挖加厚 40 家（波兰9家/美区12家集中；STI×5：503 Antaira·509 ORing+EN50155铁路·513 Moxa·523 工业嵌入·524 IIoT瑞士造；514/516同电话姊妹站；516/520/521授权分销诚实角窄针；517 Winncom EMEA大VAD；533自牌机柜对照+贴牌双路）；ENRICH55 50→54、OVERRIDES→A-540；P1账本 STC387/STI48/28DG62/CONSULT69；1033 dossiers；audit 1249/0；29 tests OK |
| `11e99acaa4bd` | 2026-09-29T05:07:31+00:00 | R56 第47-50批：A-461..A-500 深挖加厚 40 家（土MT MasterD三家低密/塞/奥/希STI+姊妹店/德FMS同法人+公购军列守界句/意培训+工业STI/拉厂方自营店/捷斯收录）；ENRICH55 46→50、OVERRIDES→A-500；P1 账本重归 STC356/STI74/28DG67/CONSULT69；1033 dossiers；audit 1245/0；29 tests OK |
| `16ff55107763` | 2026-09-29T04:44:58+00:00 | 深挖加厚 A-421..A-460（第43-46批/batch53-56）：东欧培训/UA分销电商九连/加拿大六连/匈牙利五连/保2+北马2+土4波；UA 9 家民用限定、DAEL/MBSI 守界句、A-450/A-453 P1=STI-288GP 工业件；ENRICH55 +4（46)、OVERRIDES +40(460)；P1 未登记 0；29 tests OK |
| `c2e7c9605cd8` | 2026-09-29T04:12:52+00:00 | 深挖加厚 A-381..A-420（第39-42批/batch49-52）：STC×17（SmartEye楼宇IaaS 30k AP/Spadhausen独立ISP/Ibersystems 8000项目/Archous白盒谱/PortUp官训/FUBAR关基守界/Codisa ENS守界等16家）+CONSULT-OEM×23（顾问/培训个体波：LanPixel实验室/YaTuAprendes #TR0299/ISPAcademny/XPD安全屋等；含A-401 mail.ru注/A-404+413占位页注/A-405域错配注/A-408谱变注）；A深挖覆盖至420/567；ENRICH55+4、OVERRIDES+40；build/make/audit(0 err)/unittest 29 OK |
| `38dd8a83a77c` | 2026-09-29T03:52:07+00:00 | R57 超批四波：A-341..A-380 加厚深挖 40 家（批35-38）落盘；21×STC-424 出信+13×CONSULT-OEM+6 建档（A-347 Kappa 同集团错峰/A-351 meconet 退市场/A-360 站504/A-365 同A-319主体/A-373 同人错峰/A-378 无邮箱）;STC-424=284 CONSULT-OEM=43;audit 0、unittest 29 OK； |
| `f94e8e7813c9` | 2026-09-29T03:21:00+00:00 | R57 超批三波：A-301..A-340 加厚深挖 40 家（批31-34）落盘；34/40 出自 AT 伙伴定位器源；30出信+4 CONSULT-OEM+3 红线建档（A-305/329/333)+3 建档供位（A-301/316/334);STC-424=278 CONSULT=26;audit 0、unittest 29 OK；（本地历史被沙盒重置回 dcc1ec1：commit-tree 正父修复，内容零变更） |
| `aa9b6204ce60` | 2026-09-29T02:18:07+00:00 | R57 超批二波：A-261..A-300 加厚深挖 40 家（批27-30）落盘；STC-424=256/CONSULT-OEM=22；audit 0 errors、unittest 29 OK； |
| `1afe10259436` | 2026-09-29T01:54:39+00:00 | R57超批 批23-26 (A-221..A-260 40家一次管线): KNT华沙30年MSP不花冤枉钱缺口句/TRIOTRONIK三板块二轨Polainer具名/Connect Data-Sintel明列LANSwitching二轨/The Junction Perle旁替补/DDS Kyland之上Hirschmann之下中档/Spectral渔场机柜备件/InterProjekt Ubiquiti主分销替补/FMS转售商二轨/Young分销官网宕期标注/VARIA入册服务商/10家MikroTik生态CONSULT-OEM(Leo死域活箱双核/A-243252同主体错峰)/A-249/251/258三无建档供位;30×STC-424+10×CONSULT 37出信3建档 audit0 unittest29; |
| `f90e8985d3b9` | 2026-09-29T01:17:56+00:00 | 批22 (A-211..A-220 意9西1): PAM墨西拿窄位/SCE建档供位同A-205/Sfera私营段/Sielco RENTRI软+Yealink支线/SIMNT Esperia-MePA守界私营主打/Sotech MSP fornitura硬缺口批内机选/SSC MEPA塔口一针/STL伦巴第布线双主业/Storelink ATM守界BMS窄位/LineasyCables三重守界Allied旁私营段;1/10建档 9出信 audit0 unittest29（沙盒历史事故重置恢复:已学备份取流正放）； |
| `bb7c916500b5` | 2026-09-28T16:09:58+00:00 | 批21 (A-201..A-210 全意): Goretti Reti支线/IFI 27牌墙缝/JM ITService窄位/LocalNet Allied-Omada双银二线/Masetto建档供位/NC 700人BU窄口/NAEL低信号/NSI自研NSGest(Newsoft Zebra-3CX同盟)/Omniconnect军事守界商业段；1/10建档 9出信 audit0 unittest29 |
| `18e7af08d94b` | 2026-09-28T15:58:34+00:00 | 批20 (A-191..A-200 全意): Coel Allied旁双线/ComputerTime MEPA守界/ConnectICS Yeastar/CTC硬件窄支线/Emilia Extreme二供位/Evergreen Esprinet前端窄位/FarPoint布线Cisco旁/Fiore自产Rack白牌/Gecopra铁路守界商业段/GIS安防私段；10/10出信 audit0 unittest29 |
| `cb0aa25bc1a4` | 2026-09-28T15:51:25+00:00 | 批19 (A-181..A-190 德6法1意3): thinkGROUP企业段/Tiefenbach OEM兼容哲学/TQ制造商建档/wp.DATA SAP双线/Ziegler混合屋/Zorn 50年电工/GroupeNetworks MARSEILLE/AGinformatica宽分销MEPA守界/Agomir三柱/Asit rackAsit白牌通道；1/10建档不出信 9出信 audit0 unittest29 |
| `0fd63a17fe64` | 2026-09-28T15:44:10+00:00 | 批18 (A-171..A-180 全德): Nutz楼宇一体化Konzern/OAS工业MES场站加固/Phoenix开源可负担/PKE柏林分部窄位/prego能源自身IT窄位/Prinzing 600人承包/RECOS WaaS成本敏/Selos威廉港Auerswald/Sittig JFK T6窗口/TELCAT私营工程Digitalpakt守界；10/10出信 audit0 unittest29 |
| `6f335945ddaa` | 2026-09-28T15:35:02+00:00 | 批17 (A-161..A-170 全德): JOTT信任文化/KWS交换能力块/M-IT公共守界KMU/m²厂房活动双场景/MECO ISO27001合规随单/M.Schmidt工业腹地/my-ITService监控门禁随单/N+P萨克森工业楼宇/Netz16集团化双路/NiTo电商Allied第四线；10/10出信 audit0 unittest29 |
| `a5e709ad0003` | 2026-09-28T15:28:49+00:00 | 批16 (A-151..A-160 全德): GBS TEMPEST密级红线/A-152与153同域dup标注/GU集团准入问询/GU-BKS SERVICE内循环建档/H&G教会福利二线/HMT北德安防随单/HumanArt Behörde红线私段/Inducio KRITIS守界/Insight规模排除建档/ISIMKO工业布线；3不出信 7/10出信 audit0 unittest29 |
| `df4e2870742d` | 2026-09-28T15:21:30+00:00 | 批15 (A-141..A-150 全德): BAIEN电商类目补位/bod交换选型直通/buerodata Ricoh子站弹性/CompData 1976行业rollout/dainox国防红线/Dallmeier同业建档/DATEL市政红线/DDS Allied实版二线/ProSoft定制二线/Eckmann aktive类目；3红线建档不出信 7/10出信 audit0 unittest29 |
| `1ccdc1e0cbf4` | 2026-09-28T15:13:02+00:00 | 批14 (A-131..A-140 德8荷1意1): SDC分销value上架/Nabacom H24供货对口/5G IT Allied实版第二供位/ACP公共KRITIS红线私营窄段/Acteos仓储WiFi随单/A+S中立维保/ALCO替代基因/AMRO Terra第二线/ARCHE军工红线建档不出信/Bachert网络A-Z；10/10 OK audit0 unittest29 |
| `0547dd7e6056` | 2026-09-28T15:05:35+00:00 | chore: 刷新全仓审计索引（批13后 audit errors:0） |
| `243be03f3e44` | 2026-09-28T15:01:04+00:00 | 批13 (A-121..A-130 全美): Nexware站点异常信号核实/Paramount SECaaS现金结构/PCS NO-MX降级/RTI教育仓储入库/Security101×2分支第二架(具名Victor)/Silco 45k客户免回访/UberData NaaS入门档/VARtek K12驻场/WireTech 30年直接对口；10/10 OK audit0 unittest29 |
| `e638c72abbe9` | 2026-09-28T14:53:33+00:00 | 批12 (A-111..A-120 美8瑞1英1): Universal 30年光纤补位/BRS NaaS×OT TCO/A3→CBX集团楼宇/Amplitel公营透明价/BCL女性持有设计指定/GSI厂商中立军红线/Griffon安装质量随单/HBS一线同盟第二架/ITC双主线无邮箱/Kidwell 75年交钥匙BOM；10/10 OK audit0 unittest29 |
| `76019040e343` | 2026-09-28T14:45:12+00:00 | 批11 (A-101..A-110 英9爱1): Lloret楼网MSI指定权/EAC私立教育随单/Bechtle规模排除建档不出信/Centerprise公共红线私营窄段/Cisilion警告截断排期冻结待核/DACC厂商中立铁路红线/Esotec安审边界窄段/Roadtech弱对口破冰/RWL分销active补位/Senseco楼内IP化；10/10 OK audit0 unittest29 |
| `9966b3e8d18a` | 2026-09-28T14:35:29+00:00 | 批10 (A-091..A-100 匈1美4英5): mikrotikgyor培训中心/Titan电子线监控柜/InternetTY POP小盒/Netonix×3纪律建档不推/LMG并入WAV信号/Networkology公共红线私营补位;29/29 OK audit0 |
| `88ed1fe8b38a` | 2026-09-28T14:28:07+00:00 | 批9 (A-081..A-090 瑞典1波1德1美1英3法2爱1荷1): Profcon生命周期补位/FMS白牌+教具/ATEC监控柜/Switchshop红线先行私营补位/Electromaster域名流落降级;29/29 OK audit0 |
| `d621ace728a6` | 2026-09-28T14:04:23+00:00 | 批8 (A-071..A-080 瑞典1美3英1荷1波1西3): Straznet SaaS转轨/McCharles教具样本/MyNetworkTraining 7万学员样本/JA Shomer老分销/A-080与A-066同人互注留档;29/29 OK audit0 |
| `04a6a4f421b3` | 2026-09-28T13:57:14+00:00 | 批7 (A-061..A-070 波1美2芬1瑞典1英2西3): CAPsMAN随单/Netrotik教具对比样本/Axbyte NOC/Hotelinking千店推荐位杠杆/Hecnys工业网温宽;29/29 OK audit0 |
| `4f2e7a81316f` | 2026-09-28T13:48:42+00:00 | 批6 (A-051..A-060 波1瑞1葡1瑞典1芬1英3美1): SAFES酒店物业托管/narrowin OT可见性试点推荐位/MiniMeLabs高密AP/Direktronik白牌补位/Sarlin能源站/独代柜内配位/AGL PoE上游/LinITX错价位+教具/INDYCAR交期痛点;29/29 OK audit0 |
| `a5e740d58ab9` | 2026-09-28T13:36:19+00:00 | 批5 (A-041..A-050 意2捷2摩1法1波4): Busatti WISP教父POP自愈/PF Tech三线/Westercom EOL补位/AIRICOM随单/CSI能源民营段边界/mtik全真教室教具;29/29 OK audit0 |
| `b6c4caad8abb` | 2026-09-28T13:26:51+00:00 | 批4 (A-031..A-040 德国1+意大利9): VARIA分销白牌/Aikom交换机纳新窗/1off OptiWize管理面/EFA工业温宽错位/Ciacci公立红线户；29/29 OK audit0 |
| `fff4065bd57a` | 2026-09-28T13:17:04+00:00 | 打通R56批3进入档案管道（ENRICH55注册+R56schema适配+OVERRIDE灌注P1/needs+custom_followup/email接线+渲染器防御）;批3希腊德国10档v2加厚生效 |
| `d96c7b79d10b` | 2026-09-28T13:03:07+00:00 | 批3 (A-021..A-030 希腊5+德国5) 深挖调研+10档v2加厚：HellasCom集团合并触达/GTA休眠站e-dreams现职/MBN工业温宽/SKYTRON 9证/Kehrlein NDA/Gisbers MTCSWE采购窗；MX 10域全验；29/29 OK audit0 |
| `14fb000aabda` | 2026-09-28T12:51:08+00:00 | 正名 Saga Telecom（替换 Saga Communications，567 档重生）+联系方式版式对齐 R41-R48 冻结断言+基线可达后测试转真实比对（29/29 OK） |
| `bb8598614d71` | 2026-09-28T12:28:06+00:00 | merge: 与远端 arena 分支合流（环境侧将分支指针回退至 dcc1ec1 后提交；本树已包含远端 59bddad 全部内容，采用新合并提交不reset不force） Co-authored-by: arena-agent <297053741+arena-agent@users.noreply.github.com> |
| `14771a087b5d` | 2026-09-28T12:25:44+00:00 | R56 v2 结构全量切换（A 类 567 档 17 节骨架+P1 单一决策+structured_profile YAML；规则书+A-002 评审样板邮件；README 零字节修复；29/29 测试 OK skipped=6） |
| `59bddadece0f` | 2026-09-28T11:07:39+00:00 | R55-β 深度再发掘·第2批（A-011–A-020，10户41条证据，28/28测试） |
| `fc0ab269173b` | 2026-09-28T10:49:51+00:00 | test: 轮次计数同步到 R55（56） |
| `9a2c7d1feb43` | 2026-09-28T10:49:11+00:00 | R55-β 深挖第1批 A-001–A-010: §九深度再发掘(6维+KP表+47条原文证据)+渲染器/冻结测试strip升级+R55轮次台账 |
| `7c0427aa2c34` | 2026-09-28T10:27:29+00:00 | R55 Saga全局替换: 三份价格表入库+目录对照文档+全库SmartByte→Saga迁移(CSV/strategy/17批JSON/两份xlsx)+审计与测试归一化 28/28 |
| `f8bcf9cb4c96` | 2026-09-28T10:01:17+00:00 | Saga price lists (user upload via main c377aaf): Marvell commercial managed xls + industrial managed PDF + industrial unmanaged xls |
| `b8d4706942a9` | 2026-09-28T09:50:19+00:00 | R54 第17批: A-321–A-340 加厚+3步跟进 (200 dims, 59 quoted facts, 20 plans) |
| `d99d8140222c` | 2026-09-28T09:31:18+00:00 | R54 第16批 A-301–A-320：A类加厚+3步跟进（20户/58条原文证据；Allied系15户分轨-GCI维保备件/Atlantik design-in/ITNI电话先行/Quadratek军段划出；A-319秘鲁待裁决） |
| `27f34a34a6c9` | 2026-09-28T08:50:08+00:00 | R54 第15批 A-281–A-300：A类加厚+3步跟进（20户/52条原文证据；ISP Supplies头号分销+GBE Allied白金+TR0001最高尊重型+失联8户首步人工；DJI/GGZ/市政/消防链划出） |
| `76e43f32057c` | 2026-09-28T08:32:36+00:00 | R54 第14批 A-261–A-280：A类加厚+3步跟进（20户/56条原文证据；顾问8户分轨+锚牌不替位+Netonix裁决话规+DCE白牌双轨；公立段划出） |
| `3476b0b1f723` | 2026-09-28T08:12:32+00:00 | R54 第13批 A-241–A-260：A类加厚+3步跟进（20户/58条原文证据；培训师/顾问生态+Perle深绑5户不替位+失联3户首步人工；公共补贴/ATC面划出） |
| `69d3f8819426` | 2026-09-28T07:47:04+00:00 | R54 第12批：A-221–A-240 逐户加厚+3步计划（荷/德/奥/瑞/波/捷/挪/葡/匈/瑞典/爱）+生成器ENRICH路径回退修复 |
| `3873d6327f37` | 2026-09-28T07:13:18+00:00 | R54 第11批：A-201–A-220 逐户加厚+3步计划（意19/西1 全Allied生态） |
| `afb6a2fcf46c` | 2026-09-28T06:27:18+00:00 | R54 第10批加厚：A-181–A-200（德6/法1/意13，Allied 集成/代理）200 维度+59 证据+3步计划 |
| `a6d5dc825c17` | 2026-09-28T06:06:31+00:00 | R54 第9批加厚：A-161–A-180（全德国20户，Allied 集成/代理）200 维度+63 证据+3步计划 |
| `e7b83b79ad3b` | 2026-09-28T05:42:03+00:00 | R54: A类逐户加厚第8批 A-141–A-160（全德国20户，全Allied Telesis集成/代理） |
| `bb075753ad19` | 2026-09-28T05:18:04+00:00 | R54: A类逐户加厚第7批 A-121–A-140（美10/德8/荷1/意1） |
| `d42bb408abea` | 2026-09-28T04:55:52+00:00 | R54: A类逐户加厚第6批 A-101–A-120（200维度+74条原文证据+恰好3步计划×20） |
| `176e0de8ff55` | 2026-09-28T04:35:32+00:00 | R54: A类逐户加厚第5批 A-081–A-100（200维度+67条原文证据+恰好3步计划×20） |
| `6acc9da9e928` | 2026-09-28T04:01:52+00:00 | R54: A-class deep enrichment + 3-step follow-up plans (batch 4: A-061-A-080) |
| `21db381429b4` | 2026-09-28T03:31:31+00:00 | R54: A-class deep enrichment + 3-step follow-up plans (batch 3: A-041-A-060) |
| `b4fa7bf0e36d` | 2026-09-28T02:52:05+00:00 | R54: A-class deep enrichment + 3-step follow-up plans (batch 2: A-021-A-040) |
| `6de2446d354f` | 2026-09-28T02:42:43+00:00 | R54: A-class deep enrichment + 3-step follow-up plans (batch 1: A-001-A-020) |
| `959f0d2ab845` | 2026-09-28T02:28:22+00:00 | R53: fix trailing blank line in audit MD and refresh audit artifacts |
| `b2dc57bec2cf` | 2026-09-28T02:28:09+00:00 | R53: B-segment site-by-site rescreen complete — 136 promotions (A-432–A-567) |
| `034c76e011b4` | 2026-09-28T02:24:22+00:00 | R53: B-segment rescreen batch 27 (B-318 mikrotik.ro promote) |
| `7fd8c132a069` | 2026-09-28T02:23:54+00:00 | R53: B-segment rescreen batch 26 (domain/entry retries, 4 promotions) |
| `758cb0cefc94` | 2026-09-28T02:20:21+00:00 | R53: B-segment rescreen batch 25 (pending-retry follow-ups, 11 promotions) |
| `d928756d3c46` | 2026-09-28T02:16:27+00:00 | R53: B-segment rescreen batch 24 (leftover DK/UA/IL/BG/IS/CZ/US/BE rows, 3 promotions) |
| `73084554c705` | 2026-09-28T02:12:58+00:00 | R53: B-segment rescreen batch 23 (PT+ES+AE/MT/ME/DE, 7 promotions) |
| `27ba6081b2dd` | 2026-09-28T02:10:51+00:00 | R53: B-segment rescreen batch 22 (NL, 4 promotions) |
| `ddd8ed492620` | 2026-09-28T02:10:26+00:00 | R53: B-segment rescreen batch 21 (UK, 7 promotions) |
| `d9fe27f9a0c4` | 2026-09-28T02:09:31+00:00 | R53: B-segment rescreen batch 20 (US+FI, 6 promotions) |
| `110efdac373c` | 2026-09-28T02:07:00+00:00 | R53: B-segment rescreen batch 19 (RO+US, 7 promotions) |
| `3d2d2b2a89a6` | 2026-09-28T02:05:49+00:00 | R53: B-segment rescreen batch 18 (US network distributors, 8 promotions) |
| `b62b95a23984` | 2026-09-28T02:04:58+00:00 | R53: B-segment rescreen batch 17 (CH/Kosovo/LT/RO, 4 promotions) |
| `a2246d317875` | 2026-09-28T02:04:29+00:00 | R53: B-segment rescreen batch 16 (IE/EE/SE/CH, 5 promotions) |
| `6bbcba61ed2f` | 2026-09-28T02:02:25+00:00 | R53: B-segment rescreen batch 15 (PL/BA/IE, 3 promotions) |
| `7adf2f4d34dc` | 2026-09-28T02:01:59+00:00 | R53: B-segment rescreen batch 14 (SE/FR/PL, 7 promotions) |
| `07bea7327426` | 2026-09-28T02:01:29+00:00 | R53: upgrade B-245 (MHz mhzshop) to promote after CRS switch-category verification |
| `2938f875452b` | 2026-09-28T02:01:02+00:00 | R53: B-segment rescreen batch 13 (France, 3 promotions) |
| `b6c5052ecedb` | 2026-09-28T02:00:33+00:00 | R53: B-segment rescreen batch 12 (SK/SI/GE/BE/FR, 3 promotions) |
| `e1db32221007` | 2026-09-28T02:00:02+00:00 | R53: upgrade B-195 (Discomp) to promote after switch-category verification |
| `92f8f4407060` | 2026-09-28T01:59:11+00:00 | R53: B-segment rescreen batch 11 (CZ/MD, 4 promotions) |
| `4bc712f00e8c` | 2026-09-28T01:57:57+00:00 | R53: B-segment rescreen batch 10 (IT/LV/NO/CZ, 3 promotions) |
| `df2f9dd89fed` | 2026-09-28T01:56:53+00:00 | R53: B-segment rescreen batches 8-9 (Germany/Italy, 6 promotions) |
| `63a074a3771e` | 2026-09-28T01:55:29+00:00 | R53: B-segment rescreen batch 7 (Greece/Germany, 5 promotions) |
| `3e07c87924ae` | 2026-09-28T01:55:02+00:00 | R53: B-segment rescreen batch 6 (Cyprus/Austria/Greece, 4 promotions) |
| `b134ecf8fca1` | 2026-09-28T01:53:58+00:00 | R53: B-segment rescreen batch 5 (Turkey/Serbia, 8 promotions) |
| `e3e3b591f576` | 2026-09-28T01:51:37+00:00 | R53: B-segment site rescreen batches 1-3 (13 promotions with URL evidence) |
| `6c8dae72a642` | 2026-09-28T01:45:26+00:00 | Refresh audit index after R52 commit |
| `3f117f069dec` | 2026-09-28T01:45:16+00:00 | R52: finish duplicate-hint review (C-011 to A-431, 21 rows held with reasons) |
| `7f4dfd3fc73c` | 2026-09-28T01:40:43+00:00 | Refresh audit index after R51 commit |
| `3a9e80117291` | 2026-09-28T01:40:34+00:00 | R51: upgrade qualifying duplicate-hint rows to A (user rule: upgrade when A standard met) |
| `6f2988b7ef51` | 2026-09-28T01:33:48+00:00 | Refresh audit index after R50 commit |
| `b98c0afd83e2` | 2026-09-28T01:33:37+00:00 | R50: mine existing 1033-row list for A-class (37 promotions, 31 dedup hints) |
| `ad0302bdf2e4` | 2026-09-28T01:20:02+00:00 | Refresh audit index after R49 commit |
| `822222e1e0fe` | 2026-09-28T01:19:53+00:00 | R49: backfill A-044/A-046 mailboxes, return 23 C rows to B, rescreen batch 2 |
| `a61a014ea753` | 2026-09-27T16:47:41+00:00 | Refresh audit index after R48 commit |
| `f956765ea0c3` | 2026-09-27T16:47:38+00:00 | Rescreen B/C batch 1: promote six verified switch channels to A-379-A-384 |
| `f974d9cda458` | 2026-09-27T16:13:24+00:00 | Refresh audit index after R47 commit |
| `d96040df3b6f` | 2026-09-27T16:13:13+00:00 | Research A360-A378 contacts with sourced official entries and explicit gaps |
| `44de7e74fc9a` | 2026-09-27T15:58:54+00:00 | Refresh audit index after R46 commit |
| `70da39c40fb7` | 2026-09-27T15:58:24+00:00 | Research A340-A359 contacts with sourced official entries and explicit gaps |
| `2b55a94c1bda` | 2026-09-27T15:49:59+00:00 | Research A320-A339 contacts with sourced official entries and explicit gaps |
| `e7c31313f22f` | 2026-09-27T15:27:13+00:00 | Research A300-A319 contacts with sourced official entries and explicit gaps |
| `7814c342b835` | 2026-09-27T15:15:34+00:00 | Research A280-A299 contacts with sourced official entries and explicit gaps |
| `43af7ece7284` | 2026-09-27T14:59:18+00:00 | Research A260-A279 contacts with sourced official entries and explicit gaps |
| `642238174fe3` | 2026-09-27T14:43:05+00:00 | Research A240-A259 contacts and distinguish legacy leads from verified sources |
| `0c5cdb4c2f65` | 2026-09-27T14:35:05+00:00 | Research A210-A239 contacts with scoped evidence and freeze strategy output |
| `d17cddc8e46b` | 2026-09-27T14:09:45+00:00 | 建立全仓溯源与逐轮需求总账，修复档案展示并顺号补挖A200至209 |
| `5ac5c565cc09` | 2026-09-27T13:53:01+00:00 | 顺号补挖 A-110..199 联系方式并保留冻结编号 |
| `a8687d611aa2` | 2026-09-27T13:40:22+00:00 | 对话38: 写入三条用户裁决 + A级排序铁律进 README |
| `985c4fc48629` | 2026-09-27T13:34:24+00:00 | 对话37-任务1c: 挖掘无邮箱客户联系方式（第1批 A-080..A-109，30家） |
| `7149cb7f743f` | 2026-09-27T13:29:37+00:00 | 对话37-任务1b: 加入国家分层，小国后压至 A-364..378 |
| `67cb0de1d649` | 2026-09-27T13:25:29+00:00 | 对话37-任务1a: A-050 之后按触达难度重排（329家） |
| `2c58e7fda9f4` | 2026-09-27T13:20:04+00:00 | 对话37: profile/ 按评级分目录(A/B/C) + 死路死链备案 |
| `8f92e15ada6a` | 2026-09-27T13:11:38+00:00 | Complete the Perle sweep; find Transition Networks is now Lantronix |
| `19e3da1086af` | 2026-09-27T13:09:55+00:00 | Complete the Perle sweep: Finland, Portugal and Ireland add 4 |
| `85cfb1d5801a` | 2026-09-27T13:05:51+00:00 | Restore Polish Microstar lost to a substring dedupe false positive |
| `885502ff728e` | 2026-09-27T13:05:08+00:00 | Perle sweep continues: Sweden, Norway, Poland add 3; Canada, Belgium, Austria yield nothing |
| `b510579483eb` | 2026-09-27T13:00:21+00:00 | Perle: Italy and Spain have no distributors; document the ?countryname key |
| `9c8b696fd591` | 2026-09-27T12:59:32+00:00 | Mine Perle distributor directory for US, UK and France: +8 |
| `7677e1857ea9` | 2026-09-27T12:53:43+00:00 | Refresh follow-up workbook and main workbook to 1020 rows |
| `5b4c878aaa01` | 2026-09-27T12:53:16+00:00 | Record Belden and Westermo as exhausted; identify Perle as next channel |
| `638f7e0b5b3a` | 2026-09-27T12:52:16+00:00 | Mine Westermo where-to-buy (static table): +16 European partners |
| `5c87490edb72` | 2026-09-27T12:47:24+00:00 | Finish Allied Telesis sweep; open Belden channel; A 356 -> 364 |
| `bdbac6a37b20` | 2026-09-27T12:46:02+00:00 | Allied Telesis: finish Norway, Finland, Portugal, Greece, Hungary; channel now fully swept Denmark and Ireland hold nothing usable - only Atea and Bechtle respectively, both too large. Teleste in Finland is flagged as a possible competitor rather than a customer since it makes access network equipment itself. This completes the Allied Telesis partner locator for all in-scope European countries and the United States. |
| `279d78779bb8` | 2026-09-27T12:41:39+00:00 | Allied Telesis: exhaust Spain, Netherlands, Belgium, Austria, Switzerland, Poland, Czechia, US |
| `2a0a18f17bb2` | 2026-09-27T12:40:14+00:00 | Allied Telesis US complete (2/2 pages): +4 security integrators |
| `52606bb3ce90` | 2026-09-27T12:39:18+00:00 | Allied Telesis Switzerland and Poland complete (1 page each): +8 |
| `3eb0558e9e43` | 2026-09-27T12:38:33+00:00 | Allied Telesis Belgium and Austria complete (1 page each): +6 |
| `b74299aaf1a0` | 2026-09-27T12:37:46+00:00 | Allied Telesis Spain and Netherlands complete (1 page each): +5 |
| `6b5d02caa3c2` | 2026-09-27T12:31:38+00:00 | Allied Telesis Italy complete (3/3 pages); A 328 -> 339 |
| `378eba1c105b` | 2026-09-27T12:30:12+00:00 | Allied Telesis Italy page 2: +19 |
| `cafa749989b1` | 2026-09-27T12:29:24+00:00 | Allied Telesis Italy page 1: +17 |
| `f902428ea732` | 2026-09-27T12:24:28+00:00 | Allied Telesis France complete (2/2 pages); A 285 -> 293 |
| `4305643ef9af` | 2026-09-27T12:23:33+00:00 | Allied Telesis France page 1: +9 |
| `b7fe67d920b0` | 2026-09-27T12:22:41+00:00 | Allied Telesis Germany complete (4/4 pages): +7, A 278 -> 285 |
| `72ebe2bbe1a6` | 2026-09-27T12:21:35+00:00 | Allied Telesis Germany page 3: +20 partners |
| `c67f9b99bf78` | 2026-09-27T12:15:59+00:00 | Open Allied Telesis Germany pool via country param; +32, A 226 -> 258 |
| `19cec7b8c3e7` | 2026-09-27T12:11:55+00:00 | Promote 77 no-email integrators to A pending manual info; A 149 -> 226 |
| `fe98af1141ad` | 2026-09-27T11:53:34+00:00 | Record exhausted veins and the Allied Telesis country-page lead; A 147 -> 149 |
| `77ba351ac144` | 2026-09-27T11:51:48+00:00 | Mine Allied Telesis UK reseller list (static page); UK 55 -> 77 rows, A 147 -> 149 |
| `056617b9530f` | 2026-09-27T11:39:40+00:00 | Add Belden/Hirschmann and Zyxel channel partners |
| `923fe61a1deb` | 2026-09-27T11:38:45+00:00 | Add Allied Telesis EU MSPs and 2 US integrators; A 144 -> 145 |
| `d65846cf813d` | 2026-09-27T11:31:58+00:00 | Sweep Benelux, Baltics, Balkans training partners; A 140 -> 144 |
| `5ce1cb1f5530` | 2026-09-27T11:25:03+00:00 | Mine MikroTik training partners across 10 countries; A 123 -> 140 |
| `b3296dfa1934` | 2026-09-27T11:13:53+00:00 | Extract shared numbering module; mark Netonix 14; A 122 -> 123 |
| `29edf4fbacec` | 2026-09-27T11:04:32+00:00 | Mine Teltonika and Allied Telesis channels; A 118 -> 122 |
| `eec7c6e05cbc` | 2026-09-27T11:02:50+00:00 | Classify C by reason, tighten B demotion; 14 Netonix channel; A 105 -> 118 |
| `0b40faf2b462` | 2026-09-27T10:47:15+00:00 | Demote 152 unreachable B accounts to C; mine training centres; A 94 -> 105 |
| `5952bf79644a` | 2026-09-27T10:34:48+00:00 | Add 11 US MikroTik consultants; 741 -> 752 |
| `09c147546bec` | 2026-09-27T10:32:15+00:00 | Freeze dossier numbering so it never reorders again |
| `68243e3a7856` | 2026-09-27T10:24:51+00:00 | Mine Dutch and Czech MikroTik consultants; 728 -> 741, A up to 91 |
| `ad547881d5fc` | 2026-09-27T10:18:50+00:00 | Stop mining distributors; the A-grade data says mine integrators |
| `6fef5c4fbd71` | 2026-09-27T09:56:11+00:00 | Add Netonix WISP replacement matrix |
| `4c030e300262` | 2026-09-27T09:52:58+00:00 | Reframe grades as Munger's yes/no/too-hard; stop dropping fields on B/C |
| `1bfb007de5b7` | 2026-09-27T09:43:04+00:00 | Mine EtherWAN and Advantech dealer networks; 721 -> 728 |
| `62ea7e841936` | 2026-09-23T01:11:57+00:00 | Mine Moxa's European and North American dealer network |
| `5981add86339` | 2026-09-22T16:12:37+00:00 | Find named contacts for the 10 A-grade accounts that had none |
| `2b8a0199eb5f` | 2026-09-22T15:54:18+00:00 | Mine PLANET's dealer network; fix Taiwan and scale-number misgrading |
| `89023bda7e00` | 2026-09-22T15:37:06+00:00 | Stop tracking __pycache__ and ignore Python build artefacts |
| `3be8e2df52b8` | 2026-09-22T15:32:11+00:00 | Fix out-of-region misgrading, keep all 30 methods, restate the Taiwan rule |
| `8a350df92ab3` | 2026-09-22T14:04:23+00:00 | Add Marvell sourcing methodology, EOL replacement matrix, 3 new accounts |
| `fe7afad2c518` | 2026-09-22T13:44:53+00:00 | Fix 12 broken index links, add Part H, correct five stale figures |
| `c06a739563f7` | 2026-09-22T13:34:31+00:00 | Add agent constitution v2.0 and context README with first deep audit |
| `725557358b43` | 2026-09-22T10:35:57+00:00 | Add a ready-to-send first contact mail to each A dossier |
| `775045d5a9a3` | 2026-09-22T10:22:19+00:00 | Add a per-customer dossier under profile/, one file each |
| `27fe4c528a22` | 2026-09-22T10:15:50+00:00 | Export the graded list as a working workbook |
| `cbdf4d41f0b0` | 2026-09-22T10:09:58+00:00 | Grade the list A/B/C and write per-account strategy for A tier |
| `fc142955efe7` | 2026-09-22T09:57:47+00:00 | Add the audit report for the reverse-signal list |
| `85e743cbfeac` | 2026-09-22T09:56:57+00:00 | Audit fixes: merge duplicates, normalise labels, cross-reference groups |
| `c74a92dba8e9` | 2026-09-22T08:56:36+00:00 | Final countries: North Macedonia, Kosovo, Montenegro, Malta, Moldova |
| `72734597448a` | 2026-09-22T08:52:44+00:00 | Record Hellascom as the first Greek MikroTik distributor |
| `dfb9062d4e19` | 2026-09-22T08:52:25+00:00 | Greek consultants: 20, plus Slovak, Bosnian and Albanian |
| `4fe58ac62e84` | 2026-09-22T08:50:45+00:00 | Croatian, Serbian and Bulgarian consultants; Slovenia has none |
| `fa7365a124b2` | 2026-09-22T08:50:04+00:00 | Austrian, Swiss, Belgian, Portuguese and Irish consultants |
| `1606b1cf9f98` | 2026-09-22T08:42:51+00:00 | Fold Wireless Netware's consultant profile into its existing row |
| `f41e24a41c10` | 2026-09-22T08:42:33+00:00 | Canadian consultants: 15, including a CCIE and a national ISP veteran |
| `b94e83a2c5f1` | 2026-09-22T08:41:32+00:00 | Enrich Link Technologies and IP ArchiTechs with their US consulting teams |
| `be293dcc5b74` | 2026-09-22T08:41:06+00:00 | US consultants: 19 people across 15 companies |
| `68941d91cbdd` | 2026-09-22T08:39:25+00:00 | Latvian and Lithuanian consultants, completing the Baltics |
| `b9bfb28a48d2` | 2026-09-22T08:30:31+00:00 | Estonian consultants: two, one focused on switching |
| `41ab41ffc497` | 2026-09-22T08:30:02+00:00 | Swedish and Finnish consultants; Norway has none |
| `7852cae45de6` | 2026-09-22T08:29:05+00:00 | Denmark consultants, and fold Pumait's consultant profile into its row |
| `d6fbf68a8b61` | 2026-09-22T08:28:25+00:00 | Hungarian and Romanian consultants, including two strong switching fits |
| `dd51b0a8336f` | 2026-09-22T08:23:12+00:00 | Italian consultants: 21 people across 19 companies |
| `775d1c331939` | 2026-09-22T08:22:00+00:00 | France and Spain consultants, plus a reusable batch import script |
| `0dd58c975064` | 2026-09-22T08:10:19+00:00 | Record the second DAEL consultant on the surviving row |
| `ddcf52da5809` | 2026-09-22T08:10:08+00:00 | Dutch consultants: 14, including a presales consultant at a VAD |
| `db37499a1864` | 2026-09-22T08:09:15+00:00 | UK consultants: 13, with LinITX holding three of them |
| `592267b9a982` | 2026-09-22T08:08:08+00:00 | Ukrainian consultants: 9 including two strong PoE and switching fits |
| `75facdc070d3` | 2026-09-22T08:04:15+00:00 | Link the WIFIPROFI distributor row to its owner's consultant profile |
| `6b4624d1e31d` | 2026-09-22T08:03:56+00:00 | Czech consultants: 5 including a product manager at 100MEGA |
| `67fe5bd3bea6` | 2026-09-22T08:03:07+00:00 | Finish the German consultant list: 9 consultants in total |
| `abe1ddf77a1a` | 2026-09-22T08:00:13+00:00 | Finish the Polish consultant list: 15 consultants in total |
| `185bac43ebd9` | 2026-09-22T07:59:41+00:00 | Polish MikroTik consultants, first page: 11 named contacts |
| `f5a54464b77c` | 2026-09-22T07:59:06+00:00 | Keep the other two FMS Web consultants reachable in one row |
| `4d376a772f5d` | 2026-09-22T07:44:46+00:00 | Open the MikroTik consultant directory: first 6 German consultants |
| `30921a6325fe` | 2026-09-22T07:43:32+00:00 | HMS USA page 8 of 8: completes the US N-Tron channel |
| `d4935472db7c` | 2026-09-22T07:42:56+00:00 | HMS USA page 7 of 8: 12 accounts including Wesco |
| `289385fc01a0` | 2026-09-22T07:42:11+00:00 | HMS USA page 6 of 8: 4 accounts, Rexel branch count corrected to 18 |
| `a9a6a2232e52` | 2026-09-22T07:39:31+00:00 | HMS USA page 5 of 8: 11 accounts including Rexel USA |
| `9dd7b75d85ab` | 2026-09-22T07:38:44+00:00 | HMS USA page 4 of 8: Lakeland Engineering plus Kendall's full branch list |
| `7086c6cfce33` | 2026-09-22T07:38:03+00:00 | HMS USA page 3 of 8: 12 accounts including Gexpro and Graybar Electric |
| `06145f6784fe` | 2026-09-22T07:37:09+00:00 | HMS USA page 2 of 8: 4 accounts, mostly multi-branch groups |
| `359570fc5f4d` | 2026-09-22T07:36:22+00:00 | HMS USA page 1 of 8: 12 accounts from 20 directory entries |
| `0b4b9db1bd0d` | 2026-09-22T07:28:30+00:00 | Add the Serbian and Croatian RBT Technologies branches |
| `9051cf31dd6f` | 2026-09-22T07:28:04+00:00 | Finish HMS Europe: Balkans, Nordics, Israel, Baltics (+6) |
| `cc6a3e1f06eb` | 2026-09-22T07:26:55+00:00 | Cross-link the three OEM Automatic entities (SE/PL/CZ) to one entry point |
| `a613a70d3a94` | 2026-09-22T07:26:14+00:00 | HMS Europe batch 2: FR, ES, IT, NO, PL, PT, RO, GR, HU, CZ, AT, FI, IE, SI (+21) |
| `eedf4ded27ea` | 2026-09-22T07:22:17+00:00 | HMS N-Tron/Red Lion channel: UK, Ireland, Canada, NL, DE, SE, BE (+30) |
| `24283e37136f` | 2026-09-22T07:13:42+00:00 | Sweep USA (27) and Canada (7): 396 accounts total |
| `a74ab8fa01a9` | 2026-09-22T07:12:27+00:00 | Finish the European sweep: Baltics, Ukraine, Balkans, Caucasus, Israel, Malta, Iceland |
| `c44bd99bfd55` | 2026-09-22T07:04:45+00:00 | Document the European country sweep: progress, 10 pan-European groups, single-brand targets |
| `9762783e894d` | 2026-09-22T07:04:13+00:00 | Sweep 7 more countries: Portugal, Romania, Hungary, Greece, Turkey, Ireland, Norway |
| `d9c7715a3bf3` | 2026-09-22T07:02:40+00:00 | Sweep MikroTik distributors in 9 more countries: 265 accounts total |
| `3c141469e37f` | 2026-09-22T06:55:35+00:00 | Mine MikroTik official distributor directory: 84 new accounts, 216 total |
| `77718d51eee6` | 2026-09-22T06:20:48+00:00 | Mine Antaira, Westermo, ComNet and HMS partner directories: 62 new accounts, 132 total |
| `c3fa7c73c80a` | 2026-09-22T06:12:21+00:00 | Add price rebuttal playbook and 28 new leads from ORing's European distributor locator |
| `83748945adba` | 2026-09-22T01:43:29+00:00 | Fix lead counts in reverse-signal doc and reorder workbook sheets |
| `89ed28dc93ad` | 2026-09-22T01:43:10+00:00 | Add CRM-ready lead CSV (44 accounts) and second batch from Southern Europe and Nordics |
| `fe613e595edc` | 2026-09-22T01:36:41+00:00 | Add outreach copy for ASSMANN/2direct/Intos and reverse-signal lead list with EU street-price anchors |
| `be4a9bbce4e4` | 2026-09-22T01:27:49+00:00 | Add key-account deep-dive with neutral-shipping playbook and SmartByte pricing ladder |
| `a5400abe9aa4` | 2026-09-22T01:17:33+00:00 | Add A-class account quick-reference and compliance checklist sheets to workbook |
| `32d52bcbf0a5` | 2026-09-22T01:17:32+00:00 | Merge arena branch (restore workbook sheets) Co-authored-by: arena-agent <297053741+arena-agent@users.noreply.github.com> |
| `33a0e00af01d` | 2026-09-22T01:16:37+00:00 | Add 12 A-class account battle cards with ready-to-send outreach, plus OEM compliance pack and contract templates |
| `b63666677894` | 2026-09-21T14:44:19+00:00 | Add Marvell-brand landscape sheet and development-cadence KPI sheet to workbook |
| `5a9039aed4a9` | 2026-09-21T14:43:31+00:00 | Merge arena branch (restore workbook sheets and prior deliverables) Co-authored-by: arena-agent <297053741+arena-agent@users.noreply.github.com> |
| `450459d0e706` | 2026-09-21T14:42:02+00:00 | Add Marvell-vendor landscape and long-term customer-development operating system |
| `724eab04f5d3` | 2026-09-21T13:08:00+00:00 | Add full MikroTik-customer playbook (spec matrices, adjacent competitors, country playbooks, talk tracks) |
| `67472d687583` | 2026-09-21T12:54:11+00:00 | Add MikroTik shipment-geography analysis with Comtrade data and regional entry priorities |
| `a1034f5d57a2` | 2026-09-21T12:45:04+00:00 | Merge remote-tracking branch 'origin/main' into arena/01a0c3ef-mikrotik-info Co-authored-by: arena-agent <297053741+arena-agent@users.noreply.github.com> |
| `886626a80325` | 2026-09-21T20:44:03+08:00 | Add files via upload |
| `3e8b1818447d` | 2026-09-21T12:43:14+00:00 | Add MikroTik customer entry analysis and MikroTik→SmartByte cross-reference workbook |
| `dcc1ec1e60c0` | 2026-09-21T20:26:42+08:00 | Add files via upload |
