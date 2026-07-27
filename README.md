# NUEDC Engineering Skill

[![Validate](https://github.com/DushsK/nuedc-engineering-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/DushsK/nuedc-engineering-skill/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

面向全国大学生电子设计竞赛（NUEDC/电赛）的开源 AI 工程 Skill。

它不是“万能代码模板”，而是一套**硬件优先、证据驱动、评分导向**的工作流：让 AI 在提出电路、固件、控制、DSP、FPGA 或视觉方案前，先理解真实的电压、电流、噪声、时序、机械约束、测试条件和失效后果。

## 为什么需要它

AI 很容易生成语法正确、物理上错误的方案，例如：

- 凭空猜测引脚复用、定时器通道、晶振频率或 ADC 采样能力。
- 把器件的绝对最大额定值当成可长期工作的设计值。
- 忽略驱动死区、采样建立时间、输入共模范围、地回流、热设计和机械饱和。
- 只给 PID 参数或代码，却没有对象模型、控制周期、执行器余量和失效保护。
- 为了“高级”而上 AI、FPGA 或复杂算法，反而错过基本分。

本项目把这些盲区变成可执行的证据检查、预算表、硬件门禁、分层联调和验收流程。

## 核心能力

- 将原题、说明和评分表转换为可验证的得分合同。
- 从历年题目识别电源多拓扑、仪器、模拟/RF、通信、控制、机器人、视觉、DSP、FPGA 等知识链。
- 建立能量链、信号链、时序链、控制链、机械链和故障链。
- 按精确器件型号核对 datasheet、参考手册/TRM、勘误表、开发板原理图和应用笔记。
- 审查电源完整性、保护、模拟前端、ADC/DAC、时钟、DMA、中断、总线和执行器安全。
- 覆盖 STM32、TI MSPM0/TM4C/C2000、NXP、GD32、RP2040、ESP32、DSP、FPGA 和边缘计算平台的选型方法。
- 扩展倒立摆、旋转摆、磁悬浮、两轮平衡、轮腿机器人、无人机和多机协同等动态系统。
- 生成分阶段上电、标定、联调、故障注入、回滚和现场验收计划。
- 约束 AI 代码幻觉、无意义防御、过度抽象，记录生成模型前缀、备份、版本和变更日志。

## 当前覆盖

- 206 条历年题目派生元数据，覆盖 1994-2026；2022 两场赛事与 2026 吉林区域赛已单独标记。
- 19 个按需加载的工程参考模块，覆盖硬件、模拟、电源、通信、控制、视觉、MCU、DSP、FPGA、AI 代码治理和现场执行。
- 6 个跨题型示例，包括数字示波器、旋转倒立摆、并联逆变器、单目测量、网线测试和轮腿机器人。
- 3 个无第三方依赖的 Python 工具，用于生成题库索引、创建赛题工作表和验证项目完整性。

这是一套持续维护的工程基线，不宣称穷尽所有赛题或器件。数据边界见 [`data/README.md`](data/README.md)，长期建设方向见 [`ROADMAP.md`](ROADMAP.md)。

## 大道至简

核心入口只有一个 [`SKILL.md`](SKILL.md)。详细知识按需加载，放在 [`references/`](references/) 中，避免把所有知识一次性塞进模型上下文。

```text
原题与评分表
    ↓
得分合同与验收指标
    ↓
物理链路与预算
    ↓
架构和器件证据
    ↓
硬件门禁
    ↓
固件 / DSP / FPGA / 控制实现
    ↓
分层联调与故障注入
    ↓
现场测试与设计报告
```

## 快速使用

### Codex

```powershell
git clone https://github.com/DushsK/nuedc-engineering-skill.git $HOME\.codex\skills\nuedc-engineering-skill
```

然后使用：

```text
使用 $nuedc-engineering-skill 分析这道电赛题。先建立评分矩阵和缺失证据，
再给出基础分方案、发挥分路线、硬件门禁、联调顺序和验收测试。
```

### 其他支持 SKILL.md 的 Agent

将仓库放入对应的 skills 目录，确保入口文件为 `SKILL.md`。不同工具的安装路径可能不同，以工具当前官方文档为准。

## 仓库结构

```text
ROADMAP.md                      长期维护和版本路线
SKILL.md                        核心工作流与路由
VERSION                         当前发布版本
CHANGELOG.md                    分版本变更记录
AI_PROVENANCE.md                AI 生成代码的模型、前缀与例外
references/                     按领域加载的工程知识
scripts/build_problem_index.py  历年题目元数据和分类生成器
scripts/new_problem_brief.py    新赛题分析工作表生成器
scripts/check_project.py        项目结构与链接检查
data/                            题目元数据、统计和生成溯源，不再分发原题 PDF
examples/                        跨题型示例
agents/openai.yaml               Skill UI 元数据
```

## 历年题目数据

项目使用公开题目仓库的**文件名和题目元数据**构建知识图谱，不把原题 PDF 重新打包进本仓库。当前索引为 206 条记录；输入版本记录在 [`data/provenance.yml`](data/provenance.yml)。重新生成索引：

```powershell
python scripts/build_problem_index.py `
  --tree-file path\to\topic_tree.txt `
  --corpus-dir path\to\nuedc\docs\problems `
  --out-csv data\historical-problems.csv `
  --out-summary data\historical-summary.md
```

原题版权归原作者、竞赛组织方或相应权利人所有。请从官方平台或来源仓库获取，并遵守其使用条款。

## 设计原则

1. **评分优先**：先稳定拿到基础分，再扩展发挥分。
2. **证据优先**：器件级结论必须可追溯到一手资料。
3. **硬件优先**：软件不能修复错误电平、错误接线、错误带宽或不足的执行器能力。
4. **可测优先**：没有测试点、日志或基准信号的系统不可调。
5. **降级优先**：故障时进入安全、可解释、可恢复的状态。
6. **简单优先**：复杂方案必须证明它确实换来了得分或鲁棒性。
7. **溯源优先**：AI 生成代码必须标明模型家族前缀、备份基线、版本日志和真实验证。

## AI 代码、备份与版本

- 修改现有工程前，Skill 会先确认采用 Git 提交/标签、版本压缩包、已知良好固件与配置，还是由用户明确接受不额外备份。
- AI 新建的项目自有函数、宏/常量、类型、全局状态和任务入口使用模型家族前缀，例如 `GPT_`、`Claude_`、`Gemini_`。厂商 SDK、启动文件、中断向量、协议和公共 ABI 要求的固定名称不强制改名，而是立即转调带前缀的实现并登记例外。
- 只在存在真实复用、边界、测试、所有权或复杂度收益时抽函数和类型；防御性检查必须对应具体故障、有限响应和可观测证据。
- 版本使用 `vMAJOR.MINOR.PATCH`，当前版本写在 [`VERSION`](VERSION)，每次发布同步更新 [`CHANGELOG.md`](CHANGELOG.md) 和 [`AI_PROVENANCE.md`](AI_PROVENANCE.md)。

详细规则见 [`references/ai-code-quality.md`](references/ai-code-quality.md)。

## 项目状态

当前为 `v0.2.1`：新增电源多拓扑选择矩阵、AI 代码抗幻觉与简洁性规则、模型前缀溯源、备份询问、语义化版本和变更日志门禁，并校正官方电源资料标题。后续建设按 [`ROADMAP.md`](ROADMAP.md) 持续扩展。

## 示例

- [`examples/2001-digital-storage-oscilloscope.md`](examples/2001-digital-storage-oscilloscope.md)
- [`examples/2013-rotary-inverted-pendulum.md`](examples/2013-rotary-inverted-pendulum.md)
- [`examples/2023-parallel-inverter.md`](examples/2023-parallel-inverter.md)
- [`examples/2025-monocular-measurement.md`](examples/2025-monocular-measurement.md)
- [`examples/2025-ethernet-cable-tester.md`](examples/2025-ethernet-cable-tester.md)
- [`examples/wheel-legged-robot-extension.md`](examples/wheel-legged-robot-extension.md)

## 贡献

欢迎提交原题元数据纠错、经官方手册验证的平台注意事项、匿名化调试案例、新 MCU/DSP/FPGA 支持、示例和自动化检查。

请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。器件结论可通过 Hardware evidence Issue 提交；不要提交盗版资料、未经授权的完整题目附件、密钥、私有代码或无法确认许可的工程文件。

## 致谢与来源

- 历史题目入口参考 [chenshuo/nuedc](https://github.com/chenshuo/nuedc) 与 [CCBP/NUEDC_Topic](https://github.com/CCBP/NUEDC_Topic)。
- 硬件安全分层思想受到 MIT 许可项目 [embedded-hardware-safety-review](https://github.com/016darling610/embedded-hardware-safety-review) 启发；本项目重新设计了面向完整电赛流程的原创结构和内容。
- 一手资料入口见 [`references/source-catalog.md`](references/source-catalog.md)。

## 安全声明

本项目不替代合格教师、实验室安全规范、厂商手册或专业工程评审。涉及市电、高压、大电流、锂电池、旋转机械、螺旋桨、激光、加热器和高速运动平台时，必须由具备资质或经验的人员现场监督，并使用合适的隔离、限流、防护和测量设备。

## License

[MIT](LICENSE)
