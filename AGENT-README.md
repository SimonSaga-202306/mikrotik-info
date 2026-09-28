# Agent 当前交接 · 2026-09-28

先读本文件、[宪法v2.0](AGENT-CONSTITUTION.md)、[用户要求总账](docs/requirements/用户要求总账.md)。
旧文件全部历史内容已**逐字原样归档**到 [截至5ac5c56的快照](docs/history/AGENT-README_截至5ac5c56.md)，不是删除历史；其中旧统计、reset配方、过期当前任务不再直接执行。

## 当前事实

- 仓库：`SimonSaga-202306/mikrotik-info`；工作目录 `/home/user/mikrotik-info`。
- 唯一工作分支：`arena/01a0c3ef-mikrotik-info`。不得切分支、推其他分支。
- 本轮基线：`ad0302b`（R49审计刷新；治理回归基线仍为`5ac5c56`；R50 内容提交+审计刷新见 git log）；实际最新提交与干净状态用git检查，不依赖本段猜测。
- 主表：`客户名单_反向信号_2026-09.csv`，UTF-8 BOM，**1033×22**；**A567/B179/C287**（R48升级6条B→A、R50提炼37条、R51达标升级9条、R52复核补升1条、R53 B段逐站复筛达标升136条：原号空缺不回填；R49回升23条C→B：原C-168/C-173/C-176/C-178/C-191/C-194/C-197/C-199/C-204/C-205/C-209/C-210/C-215/C-216/C-226/C-227/C-228/C-272/C-282/C-284/C-285/C-291/C-298号空缺不回填）。
- `档案编号`当前零基列19、`C级细分`20、`人工定级`21；写代码按表头定位，不硬猜。
- `profile/A/`567、`profile/B/`179、`profile/C/`287。编号和CSV物理顺序均冻结（升级行保持原物理位置）。
- 下一新增或升级A：**A568**。A段已完成至A431；R53 B段逐站复筛（283条带网站B行）已完成：136条达标升A（A-432–A-567）、136条维持B、11条待复核。当前工作＝**R54 只做A类：逐户深度加厚 + 3 步跟进计划**（第1–8批 A-001–A-160 完成，下一批从 A-161 起，约 20 户/批）。

## 当前任务与顺序

1. A联系方式补挖：已处理A080–A378（A段完成；少数行仍保留「待人工补信息」标注，见各批记录）。
2. **存量复核（R50–R53）**：不再新挖客户；R50 全表过筛升A 37条+31条去重提示；R51 达标升9条（A-422–A-430）；R52 复核补升1条（C-011→A-431）、另21条维持原因落档；**R53 B段逐站复筛283条带网站B行 → 136条达标升A（A-432–A-567）、136条维持B、11条待复核**；升级A只接末尾、保持原物理位置、不合并重复。
3. 复筛标准：先核验官网是否有交换机产品线/渠道证据，再按人工定级；不升级、失败、疑似重复同样落证；R50 升A采用「官方名录收录+工程师级认证+直达邮箱+非重复」人工定级。
4. **R54 A 类加厚（当前）**：只做 A 类；逐户抓官网/公开页面（原文+URL 落 `batch/A类加厚_*.json`），每户 ≥8 个维度 + 2–4 条原文证据 + **恰好 3 步**跟进计划（推什么型号/切入点/要问的问题/随附证明）；由 `scripts/make_profiles.py` 渲染为档案 §六/§七/§八；批次约 20 户、编号与顺序不动。
3. 全仓历史补证持续推进：已建立全文件/客户/URL索引，但549条客户没有逐项证据URL，其他484条也只是有结构化联络记录，不是全字段认证（R53后计数，见全仓审计）。

### 最近批次

- **R54（A 类逐户加厚 + 3 步跟进计划）**：第 1–9 批 A-001–A-180 完成（下一批 A-181 起；第 2 批 A-021–A-040：200 条维度 + 59 条原文证据；第 3 批 A-041–A-060：200 条维度 + 75 条原文证据，无官网户用企业登记/厂商名录/LinkedIn 公开页并标注性质；第 4 批 A-061–A-080：200 条维度 + 74 条原文证据，站点空挂/HTTP 500/反爬/检索零命中等异常如实标注；第 5 批 A-081–A-100：200 条维度 + 67 条原文证据，官网维护模式/域名被占博彩内容/店铺停摆/整站跳转并购（LMG→WAV）/无官网第三方页等异常如实标注，涉政府/防务客户先给合规边界；第 6 批 A-101–A-120：200 条维度 + 74 条原文证据，全 Allied Telesis 生态（英 11 / 美 8 / 瑞典 1），A3 域名已整站跳转 CBX Solutions 集团、Lloret 为 Allied 2024 官方获奖白金伙伴、Bechtle 为用户个案裁决保留的规模例外，涉政府/防务/共购合同（NASPO/TAA/BAA/NDAA 段）客户（A-104/107/111/113/114/115/116/120）在计划首节写入「只供商业段+合规声明」；第 7 批 A-121–A-140：200 条维度 + 73 条原文证据（美 10 / 德 8 / 荷 1 / 意 1），Nexware 整站 HTTP 500→检索快照、ARCHE 军船主业首封划线民用段、Silco/A+S 生命安全联动段只做非联动监控门禁、RTI/VARtek E-rate 与 ACP Halle KRITIS/Stadtwerke 与 Security 101 政府共购段首节写边界、SDC 为 MikroTik 官方培训伙伴按「工业宽温 PoE 类目空缺+课程对照机」排步、Security 101 两网点错峰；第 8 批 A-141–A-160：**200 条维度 + 71 条原文证据（全德国 20 户，全 Allied 集成/代理）**，dainox（FMN/AFCEA）与 GBS TEMPEST（六座 BSI 实验室）首封即声明军段/涉密段不供、无民用回响即归档，DATEL=Stadtwerke Dessau 市政公用+buerodata/condata 市政光纤+GU BKS SERVICE 公共/KRITIS+inducio KRITIS 客户+ISIMKO Verwaltung 段均首节写入边界，GU 集团三行 A-152 主触/A-153 不单独外联/A-154 错峰，buerodata 官网 403→集团页快照、Human Art 官网失败→官方隐私页快照+第三方目录）；第 9 批 A-161–A-180：**200 条维度 + 63 条原文证据（全德国 20 户，全 Allied 集成/代理）**，prego 能源市公（Stadtwerke/KRITIS 能源）终端项目不供只谈自用与商业段、TELCAT 消防生命安全+Digitalpakt 公立段不供、Behörde/公共机构段（M IT/schmidt IT/Phoenix）首节声明、Sittig PA/VA 人命广播联动控制链不碰只做 IP 广播端点 PoE 供电段（JFK T6/法兰克福 Auracast 项目潮为线索），集团链（Netz16→accompio 站点切入、PKE×Priva/Prinzing 600 人/TELCAT 大体系、Nutz 2026 改制 KG、RECOS 为 R&E AG 子）采购层级标注不越级，第三方待核邮箱两户（MECO/myITservice）首触先电话核，NiTo Allied 专卖深度绑定只做类目空档+第二来源）—— 每户 10 维度 + 2–4 条页面原文证据（带 URL）+ 恰好 3 步跟进计划；数据源 `batch/A类加厚_2026-09-28_R54_第1…9批.json`；档案新增 §六/§七/§八 由 `scripts/make_profiles.py` 渲染（勿手改 profile/）；无官网户用 MikroTik 名录/GitHub/LinkedIn 等公开页并标注来源性质。审计MD：`docs/audit/2026-09-28_R54_A类加厚与3步跟进计划.md`。

- **R53（B段逐站复筛）**：283条带网站B行按CSV顺序逐站抓取（27批）→ 达标136条升A-432–A-567、维持B 136条、待复核11条；R52维持清单中10条被新证据覆盖。逐站记录：`batch/B段复筛_2026-09-28_R53_第1..27批.json`；升级汇总：`batch/contact_research_2026-09-28_R53_B复筛升级.json`；审计MD：`docs/audit/2026-09-28_R53_B段逐站复筛.md`。

- **R52（31条重复提示行收尾）**：剩余 22 条逐条复核对 A 标准 → C-011 Kerberos（★★★+MTCEWE+邮箱；原C判定「大型」系我方模板词误伤）补升 A-431；21 条维持（无工程师级认证/真实大盘集团口径/无邮箱）；不合并。批次JSON：`batch/contact_research_2026-09-28_R52_达标复核补升.json`；审计MD：`docs/audit/2026-09-28_R52_重复提示达标复核.md`。

- **R51（达标即升级）**：用户规则「达到 A 级标准就可以升级」。R50 去重提示中的 9 条自身够标准（★★★+MTC*E+直达邮箱）→ 升 A-422–A-430（David Csongradi、FMS Web/Inacker、WIFIPROFI、Rein Podra、Aris Vink/SDC、Corné van Halteren/DAEL、Jasper Hagoort、Michiel Visser、MikroTrain）；其余 22 条维持；重复提示保留、不合并。批次JSON：`batch/contact_research_2026-09-28_R51_达标即升级.json`；审计MD：`docs/audit/2026-09-28_R51_达标即升级.md`。

- **R50（存量全表复核与A级提炼）**：1033行全表过筛（硬排除→★★★→有邮箱→工程师级认证→去重）：37条升A（A-385–A-421；原B号清单与逐条判据见批次JSON与审计MD）；31条与A行同邮箱/域名/人名去重提示（29条写入备注、2条早前已记）；C级288条细分理由齐全无可提升；新增批次JSON两个、审计MD一篇；未新挖客户、未发邮件、未提表单。

- **A360–A378（本轮）**：19条顺号研究：18条官网/官方结构化数据/官方登记邮箱（含官方mikrotik.com培训中心与顾问名录、公司站联系页）、1条public-register（A372官网正文未列邮箱文字，邮箱取自公司登记/工商目录）、1条leads-only（A378无公开邮箱，保留原电话与「待人工补信息」）；A372/A376/A377移除该块。两份xlsx同步至A378；技术栈/策略/邮件逐字不变。
  - A360：trainer@mikrotik.net.ua（官方培训中心名录；名录9项证书 vs 原备注“全部十证”仅备注；第二入口smart.center@elko.ua）。A361：dobsovic@itlearning.sk（IT LEARNING SLOVAKIA；+info@itlearning.sk）。A362：ivan.dolnak@connet-group.sk（ConNet Group；+info@connet-group.sk）。A363：sales@soselectronic.com（官网Contact us销售部；Košice总部；具名部门联系人留档）。
  - A364：olisian.sulaj@gmail.com（官方顾问名录条目一致；同页Dritan Vreshta/Erion Demiri留档）。A365：johann@nexus.com.mt（官方顾问名录；+hello@/support@）。A366：info@magit.lt（官网；+pagalba@；原robertas@保留）。A367：training@pgnetpro.bg（官方培训中心名录全十证；+info@mikrotikbg.shop）。
  - A368：trainer@mikrotik-training.lt（官方名录6证含MTCSWE；主体名MB Tikslingi mokslai仅备注）。A369/A373：office@academia-mikrotik.ro（官方名录8证；A373名录现列MTCSWE与原备注差异仅记录；+vsamburski@gmail.com）。A370：oltionnikolla@gmail.com（官方顾问名录；+admin@router.al）。
  - A371：martin.soovares@gmail.com（官方顾问名录）。A372：ekomunikacija@pondi.hr（公司登记/工商目录；官网联系页仅电话；原手机保留）。A374：rein.podra@ccisrd.eu（官方顾问名录；名录电话/城市/证书差异仅备注）。A375：jj@netops.lv（官方培训中心名录8证含MTCSWE）。A376：jernej.suhadolc@virtua.si（官方名录MTCNA；virtua-it.si；info@线索仅备注）。A377：ivan.jezerinac@infiniti.hr（官方名录+公司站一致；+trening@infiniti.hr）。A378：未获邮箱，保留人工补信息。
- **A340–A359**：15条官网/官方结构化数据/官方登记邮箱、2条official-named（A355具名导师邮箱、A359自营培训站具名邮箱）、1条official-search-only（A343邮箱见公司自设PDF与Kompass，官网仅表单/PEC）、1条public-register（A344无官网，邮箱见2024市镇公开招标文件与工商PEC）、1条partner-directory（A357邮箱取自Zyxel官方分销名录）、12条移除「待人工补信息」标注（本批含块者全部）。两份xlsx同步至A359；技术栈/策略/邮件逐字不变。
  - A340：mail@netengineering.it（AT伙伴页列SpA/Sesto S.Giovanni、+39 02 2412541；官网作Srl/Milano-Reggio-Roma；不与Padova工程公司netspa.com合并）。A341：info@securcrea.com（Follonica，Toscana/Piemonte两线）。A342：info@tnet.it（Milano；support@/account@留档）。A343：info@technocenter.it（官网联系页仅表单/PEC；邮箱见公司自设简介PDF+Kompass，标注官网未复现）。A344：worldtechnology@tiscali.it（无官网；2024公开招标文件+PEC worldtechnology@pec.it，触达前复核）。
  - A345：info@avelution.nl（AT写Veghel、官网写Schijndel 5482 NN，未改城市）。A346：info@kappadata.nl（Utrecht）。A347：info@kappadata.be（De Pinte；与荷兰实体不混用）。A348：post@nlogic.no（Oslo；salg@销售）。A349：geral@c2f.pt（Barcarena）。
  - A350：info@landatel.com（Las Rozas；清算状态写入备注待核实；Netonix行保留且禁用同芯片话术）。A351：info@meconet.de（Siegen，店内在售Netonix）。A352：info@mhzshop.com（Marquixanes）。A353：info@elmat.com（Padova）。A354：sales@ntsdirect.com（Bolton MA）。
  - A355：vartan@mikrotikls.com.ua（具名导师；通用info@留档；根页抓取失败，索引+价目页互证）。A356：info@xpatit.gr（XPATIT，Rafina；培训training@）。A357：sales@digitalsima.gr（Zyxel官方名录；官网仅表单）。A358：lexis@lexis.gr（Gerakas；分公司thes@）。A359：vadsco@gmail.com（自营mikrotik.coach；英国站点地址差异仅备注，CSV城市Kyiv保留）。
- **A320–A339**：18条官网/官方结构化数据/官方登记邮箱、1条官网可逆(at)写法（A335，已规范）、1条leads-only（A334官网为无关占位页，第三方旧案例页联系方式未互证）、19条移除「待人工补信息」标注、1条保留（A334）。两份xlsx同步至A339；技术栈/策略/邮件逐字不变。
  - A320：contact@evelem.fr（官网首页/服务页；客户空间support@；自社FB同邮箱同电话）。A321：vertrieb@edvpartner.de（Hamburg；Oberhausen的edv-partner.com为同名异主体，不合并）。A322：contact@alphacron.de（Impressum/Datenschutz；AS28748，Inhaber Marc Pauls）。A323：info@berg-duda.de（Sebastian Berg-Duda）。A324：info@hm-electronics.de（AGB页Anbieterkennzeichnung；第三方thomas.hoffmann@不采用）。
  - A325：info@inseid.de（Ingo Seidenberg IT-Beratung）。A326：info@merlinedv.de（MERLIN Kommunikationstechnik e.K.，Erlangen；CSV城市字段“Bayern”为地区，未改）。A327：contact@cfigroupe.com（AT名录地址为旧址Saint-Ouen，官网现址Saint-Denis Carré Pleyel）。A328：contact@deltasertec.com（Marseille；DPO/招聘邮箱同级留档）。A329：contact@gtd-international.com（GTD集团法国子公司；Kompass具名邮箱不并入）。
  - A330：contact@nxo.eu（总部2026-03-30迁Puteaux；法律页仍Rueil-Malmaison）。A331：contact@synexie.fr（官网+自社FB；现址Toulon，CSV城市为旧址La Valette-du-Var）。A332：info@adrianetsrl.it（2025年由snc转SRL；PEC留档）。A333：info@cgtelettronica.it（罗马/维泰博同邮箱）。
  - A334：无可核证官网页邮箱，保留原电话与「待人工补信息」；第三方旧案例页邮箱/电话未获互证，不写主字段。A335：info@dpsinformatica.it（官网可逆(at)写法，规范书写；commerciale@/sistemi@/tecnici@留档）。A336：info@eulogic.it（Bari/Milano）。A337：info@ingesw.com（官网联系页仅表单；邮箱见公司自设European Job Days档案+名录，域内一致；法定Roma/运营Aprilia）。A338：info@irenesrl.it（运营Genova；注册Savona）。A339：info@mlsoftware.it（Catania；PEC留档）。
- **A300–A319**：18条官网/官方结构化数据/官方登记邮箱（A301仅社媒信箱、A316无公开邮箱，两条leads-only；A307为官网培训页商务信箱、A315为品牌页隐私政策公布邮箱、A319国别待人工确认）、15条移除「待人工补信息」标注、2条保留（A301/A316）。两份xlsx同步至A319；技术栈/策略/邮件逐字不变。
  - A300：info@gbeconverge.com（AT Platinum、隶属Mitie；荷兰EMEA邮箱info@gbeconvergebv.com次级）。A302：contact@accyotta.com（help@支持同站）。A303：info@trusol.com（Electracom Projects Ltd为另一家，不合并）。A304：sales@euroele.com（techsupport@技术）。
  - A305：info@quadratek.net（主体PH15 Ventures Ltd）。A306：enquiries@holkerit.co.uk（AT UK Partner of the Year+Platinum；次级reassuringit@/support@）。A307：ec@bluebearsit.com（官网培训页商务信箱；第三方contact@/cg@仅候选）。A311：sales@fikesmedia.com。
  - A308：contact@itni.fr（官网反诈提示供应商往来须先电话）。A309：info@gci.it（米兰/罗马/Lacchiarella，本行城市对应罗马办公室）。A310：office@ittrust.at（无HTTPS旧站+FirmenABC登记Andreas Smeczka）。A312：info@atlantikelektronik.com（Lantronix获奖分销，Planegg）。A313：info@powertechcontrols.com（Ronkonkoma NY）。
  - A314：info@ningaloo.nl（顾问名录电话与Maurik公司官网电话一致）。A315：roelof.daleboudt@ip-central.nl（品牌页隐私政策公布；2025-08并入NiceCloud）。A317：info@sheaelectricllc.com（第三方项目页csheskey@候选）。A318：deinta@deinta.com（CIF B99060089；DPO privacidad@）。A319：ventas@nexus.com.pe（elioplus标注Peru，本行原为西班牙，国别待人工确认，未改字段/编号）。
  - A301/A316：无官网页邮箱，保留原电话与「待人工补信息」；A301的social@3tec.co.uk仅为社媒信箱，A316不采信第三方邮箱格式站点推断。
- 上一批：A280–A299：11条官网/官方结构化数据/官方登记邮箱（A292为账单专用弱通道、A291含RIPE注册次级地址、A282含第三方分地址）、1条第三方目录结构化数据后仍无正文邮箱（A281）、8条leads-only保留原电话。两份xlsx同步至A299；技术栈/策略/邮件逐字不变。
  - A280：官网联系页sales@/info@/accounting@/orders@四入口；Deliberant经销页另给invictusnetworks.com候选域名，不并入主字段。A281：Manta结构化数据给地址/电话/sameAs，站点抓取失败+Wayback 429，无邮箱。
  - A282：官网info@berdin.com+Belartza地址；madrid@/berdinonline/agil第三方分地址次级留档。A283：Jellyfish Broadband官网结构化数据hello@+0800电话；Companies House 15800355与ICO ZB722352互证自营WISP身份。
  - A285/A286/A287/A288：官网 info@dael.com、info@sdc.nl（verkoop@/support@同站）、info@gewoon-it.nl、klima@wifiprofi.cz（Kryštof Klíma，TR0001）。A291：info@adeodc.dk，RIPE另列ms@adeodc.dk。A294：ISP Supplies官方页sales@（mywisptraining本轮522，info@仅索引待核）。
  - A299：info@sn-solution.hu；匈牙利公司登记显示Bacskai Antal Gábor为该公司ügyvezető（名录人士即公司负责人）。A292：官网只有billing@panorafiber.com（注明非24/7），技术/采购邮箱仍缺。
  - A284/A289/A290/A293/A295/A296/A297/A298：遮罩邮箱或无可归属主体，保留原电话；遮罩与第三方拼接候选（A290 hotmail/gmail/borderstates、A294 sdischer@）不采信；同名外部主体（A293 prado.consulting/mikrohelp、A296、A297、A298）不冒用。
- 更早批次：A260–A279：16条官网/关联机构正文邮箱（含1条可逆(at)/(dot)、1条历史具名仅存档）、1条官网搜索索引待核、1条第三方目录结构化数据、2条仍无匹配邮箱。两份xlsx同步至A279；技术栈/策略/邮件逐字不变。
  - A260：官网联系页info@与Haarlem地址、电话；LinkedIn/案例确认Maurice与GPE Networks；库内B-440同名同公司只关联不合并。A261：IP Techniek官网sales@，LinkedIn显示本人任职与Bladel一致。
  - A262：官方课程表确认里斯本培训伙伴；邮箱仅搜索索引且课程页404，标注待核。A263：官网可逆(at)/(dot)+sales@；旧电话与官网不同不改写客户字段。
  - A264/A265：官网 enquiries@ / sales@sphinxfrance.fr，与Perle名录地址一致；部门邮箱分层记录。A266：支持页supportdesk@、首页结构化sales@，2018 MUM的andy@仅历史。
  - A267/A268/A269/A270：官网正文 sales@industrialcomms.com、sales@5gstore.com、info@microtechnology.net、sales@data-connect.com（含分角色入口）。
  - A271：LinkedIn显示任职Interstellar并做MTPC 2026 spine-leaf演讲；官网集团邮箱info@；名录城市与LinkedIn所在地不同不改城市。
  - A273：官网 consulting@（原样含空格）；kevin.myers@仅2016 MUM PDF，历史具名。A274/A275/A276/A277：官网 info@joustsec.com、info@canservers.com、sales@neobits.com、contact@modelec.nl。
  - A272：官方名录邮箱为遮罩，保留原电话/WhatsApp，原“补邮箱”标注保留。A278：官网邮箱被遮罩，sales@仅有第三方目录支持，按public-register。A279：站点现为占位页、/contact-us/ 404，无邮箱，保留原电话。
- 更早批次：A240–A259：14条官网/关联机构正文邮箱、2条公共登记、1条官网搜索待核；2条仅仓库旧邮箱未外部确认、1条仍无匹配邮箱/域名；两份xlsx同步至A259。
  - A240：AULAF现admin邮箱；Khalil具名邮箱只在旧页索引，旧页404。A241官网具名m.polainer；另存采购主管公开入口，不推断愿采购。
  - A242：MWTC info及Michał/Piotr具名入口。A243/A252：CS EDU两种法律主体，分别取个人经营者/公司的PARP登记；不合并不同人/实体。
  - A244/A245/A246/A248/A250：有当前公司邮箱，但个人关联依赖历史、目录或原电话交叉，具体限制各条保留，不当现任职认证。
  - A247：HC TECH明确info(at)，品牌官网互链；A254：Connect Data sales[at]与mailto一致。A257：弃旧404页，用现葡萄牙comercial邮箱，畸形http邮箱链接不作跳转。
  - A249：旧batch/be_pt_ie.json/B452有Camacho邮箱与同电话，但协会邮箱服务域名不能当个人官网；巴西/葡萄牙/Dublin关联未解决，旧邮箱未加入主联系字段。
  - A251：旧batch/hu.json/B083同名音符差异+同电话+旧邮箱；网站403，未外部确认，旧邮箱未加入主联系字段。
  - A253：Noriak旧域503、分销旧页跳首页，邮箱仅搜索索引；Canyon伙伴页502。A258：没有匹配邮箱/域名；排除Chicago招聘经理/演员，同名不冒用。MikroTik动态目录外壳不等于除名。
  - A259：官网确认Henk/MikroTrain；现隐私页及2023PDF邮箱，关联B443，仅记录不合并。
- 本轮证据：`batch/contact_research_2026-09-27_A340-A359.json`、[核验说明](docs/audit/2026-09-27_A340-A359联络核验.md)；R46已入唯一要求总账，精确消息时间未知。
- 上批证据：`batch/contact_research_2026-09-27_A320-A339.json`、[核验说明](docs/audit/2026-09-27_A320-A339联络核验.md)；R45已入唯一要求总账，精确消息时间未知。
- 更早批次证据：`batch/contact_research_2026-09-27_A300-A319.json`、[核验说明](docs/audit/2026-09-27_A300-A319联络核验.md)。
- 更早批次证据：`batch/contact_research_2026-09-27_A280-A299.json`（A280–A299）。
- 更早批次证据：`batch/contact_research_2026-09-27_A260-A279.json`（A260–A279）。
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

- R48 只做B/C复筛的人工定级升级，**没有运行grade.py、不改自动评级口径**；禁止把来源说明中的词当作新的客户需求证据；升级行的证据在批次JSON与备注中逐条可查。
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

**从A360继续**；每条保存具体URL、字段、原文摘录、检索日期、来源等级与未确认事项。A340–A359已完成：A343（官网仅表单，邮箱见公司自设PDF/Kompass）、A344（无官网，邮箱见公开招标文件）、A357（邮箱取自厂商名录）为非官网正文来源；A350公司清算状态待人工核实；A340主体名/地址差异与A345/A356/A359地址差异仅备注。A334仍缺可核证正文邮箱（保留原电话与待人工补）；A326/A327/A330/A331城市字段与地区/旧址/现址差异仅备注说明。A280–A299：A284/A289/A290/A293/A295/A296/A297/A298仍缺可验证正文邮箱（保留原电话与待人工补），A292只有账单弱通道，A281站点与Wayback均失败。A205是仅身份线索，A201/A206待确认，不能遗漏复核。A212/A215/A218/A227/A233/A236、A249/A251/A253/A258、A262/A272/A273/A278/A279、A280/A281（Netonix保留豁免，禁用同芯片话术）及A301/A316等限制继续保留。A仍未完成，不启动B/C升级。
本轮用户要求/发言时间缺口、R37轮次冲突完整保留于总账；不要宣称恢复了不存在的聊天全文。
