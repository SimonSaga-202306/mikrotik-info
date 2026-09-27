# Agent 当前交接 · 2026-09-27

先读本文件、[宪法v2.0](AGENT-CONSTITUTION.md)、[用户要求总账](docs/requirements/用户要求总账.md)。
旧文件全部历史内容已**逐字原样归档**到 [截至5ac5c56的快照](docs/history/AGENT-README_截至5ac5c56.md)，不是删除历史；其中旧统计、reset配方、过期当前任务不再直接执行。

## 当前事实

- 仓库：`SimonSaga-202306/mikrotik-info`；工作目录 `/home/user/mikrotik-info`。
- 唯一工作分支：`arena/01a0c3ef-mikrotik-info`。不得切分支、推其他分支。
- 本轮基线：`43af7ec`（治理回归基线仍为`5ac5c56`）；实际最新提交与干净状态用git检查，不依赖本段猜测。
- 主表：`客户名单_反向信号_2026-09.csv`，UTF-8 BOM，**1033×22**；**A378/B344/C311**。
- `档案编号`当前零基列19、`C级细分`20、`人工定级`21；写代码按表头定位，不硬猜。
- `profile/A/`378、`profile/B/`344、`profile/C/`311。编号和CSV物理顺序均冻结。
- 下一新增或升级A：**A379**。当前研究下一位：**A300**（A280–A299已完成）。

## 当前任务与顺序

1. 按现编号完成A联系方式补挖，**搞完为止**。已处理A080–A299；不等于全部A已完成。
2. **全部A完成后**，再仔细复筛B/C，升级A只接末尾。
3. 全仓历史补证持续推进：已建立全文件/客户/URL索引，但843条客户没有逐项证据URL，其他190条也只是有结构化联络记录，不是全字段认证。

### 最近批次

- **A280–A299（本轮）**：11条官网/官方结构化数据/官方登记邮箱（A292为账单专用弱通道、A291含RIPE注册次级地址、A282含第三方分地址）、1条第三方目录结构化数据后仍无正文邮箱（A281）、8条leads-only保留原电话。两份xlsx同步至A299；技术栈/策略/邮件逐字不变。
  - A280：官网联系页sales@/info@/accounting@/orders@四入口；Deliberant经销页另给invictusnetworks.com候选域名，不并入主字段。A281：Manta结构化数据给地址/电话/sameAs，站点抓取失败+Wayback 429，无邮箱。
  - A282：官网info@berdin.com+Belartza地址；madrid@/berdinonline/agil第三方分地址次级留档。A283：Jellyfish Broadband官网结构化数据hello@+0800电话；Companies House 15800355与ICO ZB722352互证自营WISP身份。
  - A285/A286/A287/A288：官网 info@dael.com、info@sdc.nl（verkoop@/support@同站）、info@gewoon-it.nl、klima@wifiprofi.cz（Kryštof Klíma，TR0001）。A291：info@adeodc.dk，RIPE另列ms@adeodc.dk。A294：ISP Supplies官方页sales@（mywisptraining本轮522，info@仅索引待核）。
  - A299：info@sn-solution.hu；匈牙利公司登记显示Bacskai Antal Gábor为该公司ügyvezető（名录人士即公司负责人）。A292：官网只有billing@panorafiber.com（注明非24/7），技术/采购邮箱仍缺。
  - A284/A289/A290/A293/A295/A296/A297/A298：遮罩邮箱或无可归属主体，保留原电话；遮罩与第三方拼接候选（A290 hotmail/gmail/borderstates、A294 sdischer@）不采信；同名外部主体（A293 prado.consulting/mikrohelp、A296、A297、A298）不冒用。
- 上一批：A260–A279：16条官网/关联机构正文邮箱（含1条可逆(at)/(dot)、1条历史具名仅存档）、1条官网搜索索引待核、1条第三方目录结构化数据、2条仍无匹配邮箱。两份xlsx同步至A279；技术栈/策略/邮件逐字不变。
  - A260：官网联系页info@与Haarlem地址、电话；LinkedIn/案例确认Maurice与GPE Networks；库内B-440同名同公司只关联不合并。A261：IP Techniek官网sales@，LinkedIn显示本人任职与Bladel一致。
  - A262：官方课程表确认里斯本培训伙伴；邮箱仅搜索索引且课程页404，标注待核。A263：官网可逆(at)/(dot)+sales@；旧电话与官网不同不改写客户字段。
  - A264/A265：官网 enquiries@ / sales@sphinxfrance.fr，与Perle名录地址一致；部门邮箱分层记录。A266：支持页supportdesk@、首页结构化sales@，2018 MUM的andy@仅历史。
  - A267/A268/A269/A270：官网正文 sales@industrialcomms.com、sales@5gstore.com、info@microtechnology.net、sales@data-connect.com（含分角色入口）。
  - A271：LinkedIn显示任职Interstellar并做MTPC 2026 spine-leaf演讲；官网集团邮箱info@；名录城市与LinkedIn所在地不同不改城市。
  - A273：官网 consulting@（原样含空格）；kevin.myers@仅2016 MUM PDF，历史具名。A274/A275/A276/A277：官网 info@joustsec.com、info@canservers.com、sales@neobits.com、contact@modelec.nl。
  - A272：官方名录邮箱为遮罩，保留原电话/WhatsApp，原“补邮箱”标注保留。A278：官网邮箱被遮罩，sales@仅有第三方目录支持，按public-register。A279：站点现为占位页、/contact-us/ 404，无邮箱，保留原电话。
- 上一批：A240–A259：14条官网/关联机构正文邮箱、2条公共登记、1条官网搜索待核；2条仅仓库旧邮箱未外部确认、1条仍无匹配邮箱/域名；两份xlsx同步至A259。
  - A240：AULAF现admin邮箱；Khalil具名邮箱只在旧页索引，旧页404。A241官网具名m.polainer；另存采购主管公开入口，不推断愿采购。
  - A242：MWTC info及Michał/Piotr具名入口。A243/A252：CS EDU两种法律主体，分别取个人经营者/公司的PARP登记；不合并不同人/实体。
  - A244/A245/A246/A248/A250：有当前公司邮箱，但个人关联依赖历史、目录或原电话交叉，具体限制各条保留，不当现任职认证。
  - A247：HC TECH明确info(at)，品牌官网互链；A254：Connect Data sales[at]与mailto一致。A257：弃旧404页，用现葡萄牙comercial邮箱，畸形http邮箱链接不作跳转。
  - A249：旧batch/be_pt_ie.json/B452有Camacho邮箱与同电话，但协会邮箱服务域名不能当个人官网；巴西/葡萄牙/Dublin关联未解决，旧邮箱未加入主联系字段。
  - A251：旧batch/hu.json/B083同名音符差异+同电话+旧邮箱；网站403，未外部确认，旧邮箱未加入主联系字段。
  - A253：Noriak旧域503、分销旧页跳首页，邮箱仅搜索索引；Canyon伙伴页502。A258：没有匹配邮箱/域名；排除Chicago招聘经理/演员，同名不冒用。MikroTik动态目录外壳不等于除名。
  - A259：官网确认Henk/MikroTrain；现隐私页及2023PDF邮箱，关联B443，仅记录不合并。
- 本轮证据：`batch/contact_research_2026-09-27_A280-A299.json`、[核验说明](docs/audit/2026-09-27_A280-A299联络核验.md)；R43已入唯一要求总账，精确消息时间未知。
- 上批证据：`batch/contact_research_2026-09-27_A260-A279.json`（A260–A279）。
- 更早批次证据：`batch/contact_research_2026-09-27_A240-A259.json`（A240–A259）。

- A210–A239（更早批次）：**22当前官网/商城正文 / 2协会或公共登记 / 2旧官方PDF / 2官网搜索索引 / 1身份城市待核 / 1仅电话线索**。该批两份xlsx同步到A239。
  - A212：Pomezia S.C.E.目录电话；无匹配邮箱，不冒用Modena/Zevio同名公司。
  - A215：SIM NT官网关闭、旧页404，邮箱搜索索引待核。A233：Young官网抓取500，报价邮箱仅索引待核。
  - A218：2023年官方PDF；A236：2007年演讲PDF，现任单位/邮箱有效性待核；旧域名跳转不证明个人仍在职。
  - A227：官网Warszawa与主表Olsztyn不同；第三方同域名同电话桥接未完成登记核对，邮箱只作候选，主表城市及空白网站保留。
  - A221、A238：邮箱显示文字与mailto冲突，采用另一条显示/链接一致的通用/销售邮箱。
  - A232：官网公开网络产品经理Vitor Gama及直线，不猜个人邮箱。
  - 关联候选：A234↔A031、A235↔A013、A236↔B297、A237↔B299、A239↔A083/B141/B149；仅记录，不合并、不改前49、不算B/C复筛。
- 上批证据：`batch/contact_research_2026-09-27_A210-A239.json`；[核验说明](docs/audit/2026-09-27_A210-A239联络核验.md)。本轮只改网站/联系方式/备注，原评级依据不动。

- A110–A199（基线5ac5c56）：88条公开邮箱（87个独立主邮箱）；A111/A119仅线索。A118/A123/A165/A167第三方待核；A152/A153共享集团入口，不合并账户。
- A200–A209（上一批）：**7官网正文 / 1第三方旧目录 / 1旧官网搜索索引 / 1仅名录身份线索**。
  - A201：旧目录m.fucelli邮箱，官网只给表单，待核；不是官网证实。
  - A202：assistenza支持邮箱，不是采购人；旧info邮箱PDF已失效，不冒充当前证据。
  - A205：Allied Telesis名录确认姓名和地址，无匹配邮箱/电话；不能冒用Cargill同名人。
  - A206：info邮箱来自旧官网搜索索引，新站未复见、旧页404；新站表单有效。700全球人员是官网自述，只记录规模风险，不擅改级。
- 批次证据：`batch/contact_research_2026-09-27_A200-A209.json`，包含身份、字段范围、原文摘录、URL、检索日期与限制；在CSV/档案备注及证据MD可查。
- 本轮在原xlsx内按冻结编号补三个基础字段，不运行覆盖式导出；其余单元格、手填列、工作表保持不变。档案在隔离目录生成并验证原文件无手写差异后，仅接受本批与索引修改。

## 用户硬要求（完整逐轮见总账）

### 新增治理要求

- 深搜整仓，不忽略档案/脚本/历史/Office角落；准确报告未核验范围。
- 信息必须带证据来源，写MD或内容旁，便于溯源、索引、更新；无证据标待补证。
- 仓库结构准确可读；结构整理不允许客户重排。
- **所有可恢复用户要求集中到唯一MD，每轮带时间信息**。真实消息时间缺失就未知；记录时间单列；旧Agent摘要不能伪装用户原话，Git时间不能替代对话时间。
- 每轮更新README并用 `grep -c` 核验写入。

### 长期边界

- 大陆小贸易商Saga/Saga Telecom，极小预算；Marvell Prestera / 接入层 / 欧洲+美加 / 真正合适的A，数量无所谓。
- 台厂不是客户；狠狠挖它们欧美渠道，但不联系台厂自身。既有获客方法（含死路）全部保留。
- 不主动推进被否决的OEM合同路线、四个工厂问题和客户未回复前的细策略设计。
- 新A与升级A永远追加末尾，**不插中间、不重排、不填空号**。前49位不动；第37轮尾部一次性排序已结束。
- 不擅改ABC评级规则；所有等级资料全量保留。人工定级的无邮箱集成商A为已授权例外。
- SI/HR/RS/RO/BG/EE/LV/LT/LU/IS小国暂不主动挖；存量A后置仍保留，除非新指示。
- 官网info/sales优先，无邮箱查域名/表单/LinkedIn/Facebook/X/论坛/具名人；个人未穷尽线索不得直接C。
- 邮箱须完整公开，不猜格式、不把遮罩当找到、不用外包商/模板邮箱；公开不等于投递成功。
- **跟进记录线下维护**，用户报告实际回复并要求才入库。不要主动维护、追问或设计流程。
- **Bechtle Direct A103保级**仅个案；A080证书风险用户说OK只代表知悉，不代表有效。
- 客户交付xlsx，英语客户邮件、中文源注；档案仍在 `profile/`。
- 非破坏Git操作可正常进行；reset/rebase/force-push/merge先授权，不能照抄历史恢复配方。

## 治理轮整仓审计与修复（历史，继续适用）

入口：[审计报告](docs/audit/全仓审计.md) / [修复验证](docs/audit/2026-09-27_修复与验证.md) / [资料地图](docs/evidence/来源规则与资料地图.md)。

- 全业务文件机械读取、Office全部sheet/单元格/关系、DOCX正文/表格/页眉页脚/批注；ZIP CRC及内嵌图片计数。**未OCR、未逐图、未全网回访。**
- 新增SHA-256文件目录、URL反向索引、缺证候选段落、Git提交索引、1033客户按冻结编号的证据/缺证账。
- 修复profile索引1033个相对链接多出一层profile/的问题，含括号文件名仍用 `<...>`。
- 修复C级细分变量被目录路径覆盖；C档案“19列”改读实际列宽22；只修展示，不做B/C升级复筛。
- 历史猜测邮箱不再被提取到“邮箱”列表，原联系字段保留警告（J A Shomer等）。Industrial Solutions不完整bob@/amy@仍不算找到。
- 历史A策略按国家分组不是跟进顺序；旧数量/参数标注历史与待证，不重排主表。

## 重建/验证注意

- 本轮只补联系方式，**没有运行grade.py，不改评级口径**；禁止把来源说明中的词当作新的客户需求证据。
- `make_profiles.py`已将明确的`【日期 Axxx–Ayyy联络核验】`追加段隔离于场景、品牌和邮件个性化之外，避免地址Campus/产品经理等词污染需求判断；本批第四节起与基线逐字相同。旧无标记备注仍有启发式风险。
- `make_profiles.py`会删除重建派生档案；自身检查日期型手填跟进表。运行前还应核查用户手写文本，不能只靠正则。
- `export_abc.py`会覆盖工作簿，**不保留手填跟进单元格**；用户有回复记录时先保护。现阶段不主动维护跟进。
- 原CSV顺序和xlsx物理行顺序未按编号重排；profile索引数字排序仅用于阅读。
- 对照工作簿的`反向信号名单`需另行按身份+编号同步，不能重编号去迁就旧显示。其他sheet必须逐单元格不变。
- `add_batch.py`仍构造17列并用旧去重规则，`fix_audit.py`是历史修补脚本；未经schema/身份测试不要在22列主表直接重跑。
- `strategy.py`/`emails.py`仍有未经逐SKU实证的卖点；不能称全仓数据可靠，详见缺证索引。

```bash
python3 scripts/audit_repository.py --date 2026-09-27
python3 -m unittest discover -s tests -v
grep -c '所有可恢复用户要求' README.md AGENT-README.md
git -c core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol diff --check
```

## 交接下一步

**从A300继续**；每条保存具体URL、字段、原文摘录、检索日期、来源等级与未确认事项。A280–A299已完成：A284/A289/A290/A293/A295/A296/A297/A298仍缺可验证正文邮箱（保留原电话与待人工补），A292只有账单弱通道，A281站点与Wayback均失败。A205是仅身份线索，A201/A206待确认，不能遗漏复核。A212/A215/A218/A227/A233/A236、A249/A251/A253/A258、A262/A272/A273/A278/A279及本批A280/A281（Netonix保留豁免，禁用同芯片话术）等限制继续保留。A仍未完成，不启动B/C升级。
本轮用户要求/发言时间缺口、R37轮次冲突完整保留于总账；不要宣称恢复了不存在的聊天全文。
