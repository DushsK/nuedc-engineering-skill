# Contributing

感谢你帮助完善电赛开源 Skill。

## 可接受的贡献

- 修正题目元数据、年份、题号和多标签分类。
- 增加由官方 datasheet、TRM、勘误表、原理图或应用笔记支持的硬件知识。
- 提交匿名化的真实故障、测试记录和复盘。
- 增加可复现的赛题示例、脚本检查和文档。

## 证据要求

任何具体器件结论都应包含：

- 精确器件型号、后缀、封装、开发板和硬件版本。
- 官方文档标题、编号、修订版、章节或页码以及访问日期。
- 被验证的具体结论，而不是仅粘贴产品页链接。
- 该结论对原理图、PCB、固件、控制、测试或安全的影响。
- 计算、测量或最小复现实验，以及仍未消除的假设。

论坛、博客和视频可以作为线索，但不能替代一手资料。提交前请查看 [`references/evidence-datasheets.md`](references/evidence-datasheets.md) 和 [`references/source-catalog.md`](references/source-catalog.md)。也可以使用 Hardware evidence Issue 模板先提交证据条目。

## 版权与隐私

- 不提交未经授权的完整原题 PDF、教材扫描件或商业资料。
- 不提交密钥、账号、校内私有代码、个人信息或未获授权的队伍工程。
- 引用开源项目时遵守其许可证并保留必要声明。

## 修改流程

1. 新建分支并进行聚焦修改。
2. 运行 `python scripts/check_project.py`。
3. 若修改题目分类，重新生成 `data/historical-problems.csv` 和 `data/historical-summary.md`。
4. 同步更新 `data/provenance.yml` 中的输入版本和记录数。
5. 在 PR 中说明证据、验证方式和剩余风险。

核心 `SKILL.md` 保持简洁，详细知识放入 `references/`。明确区分事实、假设、计算和建议。
