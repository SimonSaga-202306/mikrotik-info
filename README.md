# mikrotik-info（Saga 客户情报库）

> 面向 EU/NA 市场的 PoE 交换客户开发情报库。1,033 行名单 → A 567 / B 179 / C 287。
> 用户侧总账：`docs/requirements/用户要求总账.md`（R01–R56 逐轮原文与实施状态）。
> Agent 操作手册：`AGENT-README.md`（与本文镜像同步）。

## 当前形态（2026-09-28 · R56）

- **档案**：`profile/A|B|C/` 共 1,033 份；**A 类全量 v2 骨架**（17 节：structured_profile YAML → SALES BRIEF → 事实/推断/假设分层 → 技术在用 → 需求场景 → HR 信号 → 联系方式 → KP → 跟进步骤(成功/退出) → R54/R55 要点(证据零丢失) → 产品决策(P1+备选) → SWOT → 红线+停止条件 → Qualification → Unknowns → 首触英文样板 → 跟进记录 → 下次复核）。
- **规则书**：`docs/rules/客户档案结构与内容规则.md`（外审 7 份意见的取舍台账，用户审定）。
- **机器可读档案**：`batch/structured_profiles_v1.json`（567 条；P1 白名单 STC-28DGGPM/STC-424DGGPM-280W/STI-288GP/STI-480XGGM/CONSULT-OEM）。
- **价格口径**：`$xx USD EXW（2026-09-28 快照，15 天有效，报价前核价）`；Saga 无对应规格（商用 bt90W/全万兆汇聚/8口10G）沿用旧对照并显式标注。
- **渲染**：`scripts/make_profiles.py`（A 类走 `scripts/render_v2.py`；B/C 旧模板）——profile/ 一律脚本生成，勿手改。
- **深挖进度**：R55 批 1–2（A-001–A-020）完成并 v2 化；批 3 起按「加厚+v2」一次成型；A-341 起加厚+深挖合并。
- **冻结纪律**：A-001 起编号/位置永不动，只改内容；教师/公立红线；R32 小国降级；中立包装；B/C 不投入。
- **质量关**：`python3 -m unittest discover -s tests`（29 项；历史基线依赖 6 项在浅克隆沙箱中 skip+注明）；`python3 scripts/audit_repository.py` 固定点 errors 0。

## 目录速查

- `客户名单_反向信号_2026-09.csv`——名单唯一事实源（23 列）
- `batch/`——调研原始 JSON（R54 加厚 17 批、R55 深挖 2 批、联系方式台账、结构化档案、型号映射）
- `docs/audit/`——仓库审计与批次速记　`docs/history/`——历史镜像　`docs/requirements/`——用户要求总账
- `检索/`、`profile/客户档案索引.md`——检索入口
- 我方 3 份价格表（2 xls + 1 pdf）在仓库根目录；对照分析 `Saga产品目录与SmartByte替换对照_2026-09-28.md`
