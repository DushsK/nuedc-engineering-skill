---
name: nuedc-engineering-skill
description: >-
  Hardware-grounded engineering workflow for the National Undergraduate Electronics Design Contest (NUEDC/全国大学生电子设计竞赛) and similar electronics competitions. Use when analyzing a contest problem, converting scoring rules into requirements, selecting MCU/DSP/FPGA/SBC hardware, designing analog, power, RF, sensing, control, robotics, vision, or communication systems, reviewing schematics and embedded code, reading datasheets, planning bring-up, debugging a physical prototype, preparing tests, or writing the design report. Trigger on 电赛, NUEDC, 赛题分析, 硬件选型, 原理图审查, 嵌入式调试, 小车, 无人机, 倒立摆, 轮腿机器人, 磁悬浮, 电源, 仪器仪表, 信号处理, DSP, FPGA, MCU, and hardware-safety requests.
---

# NUEDC Engineering Skill

## Mission

Turn a contest statement into a measurable, buildable, hardware-safe system. Treat code as one layer of a physical machine, not as the whole solution.

## Non-negotiable Rules

1. Optimize for verified score, not architectural novelty.
2. Read the complete problem statement, notes, prohibited methods, test sequence, power limits, dimensions, and scoring table before proposing hardware.
3. Separate stated facts, measured facts, calculated values, assumptions, and proposals.
4. Verify every part-specific claim against current primary documentation for the exact part number, package, board revision, and document revision.
5. Never invent pin mappings, clock frequencies, voltage tolerances, ADC timing, timer routing, memory sizes, peripheral instances, or FPGA resources.
6. Distinguish absolute maximum ratings from recommended operating conditions. Never design to absolute maximum ratings.
7. Model the energy path, signal path, timing path, control path, mechanical path, and failure path before implementation.
8. Build a minimum verifiable baseline first. Add scoring extensions only after the baseline repeatedly passes.
9. Put hardware protection at the actuator boundary. Do not rely only on upstream software checks.
10. Stop and request missing evidence when an unknown can damage hardware, create unsafe motion, invalidate measurement accuracy, or determine whether a peripheral can work.

## Severity Model

| Level | Meaning | Required response |
|---|---|---|
| `STOP` | Risk of injury, fire, destructive overvoltage/current, uncontrolled motion, shoot-through, invalid isolation, or an impossible hardware assumption | Do not recommend energizing or publishing executable control values until corrected |
| `FIX` | Likely task failure, unstable control, timing overrun, inaccurate measurement, deadlock, data loss, or noncompliance with the problem statement | Correct before integration |
| `IMPROVE` | Reliability, maintainability, observability, or scoring opportunity | Track explicitly; may defer |

Do not downgrade a physical risk because software compiles or simulation passes.

## Select the Working Mode

- **Problem analysis**: build the scoring matrix, constraints, acceptance tests, and risk register.
- **Architecture**: compare complete signal/power/control chains and choose the minimum viable baseline.
- **Hardware review**: inspect power, protection, grounding, interfaces, clocks, reset, programming, test points, thermal paths, and mechanics.
- **Firmware design**: define timing, interrupts, DMA, state machines, fault handling, calibration, logging, and resource budgets.
- **Algorithm/control**: derive sampling, estimation, control, DSP, vision, or communication requirements from the plant and scoring metrics.
- **Bring-up/debug**: isolate layers, collect evidence, reproduce failures, and change one variable at a time.
- **Final validation**: execute the official test sequence, uncertainty analysis, robustness tests, and report evidence.

## Core Workflow

### 1. Establish the Evidence Set

Collect the original problem, official clarifications, component list, exact board and part numbers, datasheets, reference manuals/TRMs, errata, board schematics, application notes, SDK examples, available instruments, spare parts, machining capability, team skills, and remaining time.

Use [evidence-datasheets.md](references/evidence-datasheets.md). Search current official sources when rules or documentation may have changed.

### 2. Convert the Statement into a Score Contract

Create one row per scored or mandatory item:

`ID | requirement | points | metric | allowed operation | test condition | proof method | dependency | risk | status`

Capture one-button operation, no-adjustment periods, calibration allowances, single-supply limits, prohibited modules, physical dimensions, setup time, and recovery behavior. Read [problem-analysis.md](references/problem-analysis.md). Generate acceptance tests before selecting components.

### 3. Build the Physical Model

Describe six linked chains:

1. **Energy**: source -> conversion -> distribution -> load -> protection -> heat.
2. **Signal**: physical quantity -> sensor/front end -> conversion -> processing -> output.
3. **Timing**: event -> acquisition -> transport -> compute -> actuation -> observation.
4. **Control**: reference -> controller -> saturation -> plant -> sensor -> estimator.
5. **Mechanical**: force/torque -> transmission -> structure -> friction/backlash/contact -> motion.
6. **Failure**: initiating fault -> propagation -> detection -> containment -> safe state -> recovery.

Read [hardware-first.md](references/hardware-first.md). Reject architectures whose critical chain cannot be measured or bounded.

### 4. Compare Complete Architectures

Compare at least two viable end-to-end solutions when a meaningful alternative exists. Score expected points, completion time, proven parts, accuracy, bandwidth, latency, control authority, resource margin, PCB/mechanical complexity, repairability, calibration burden, observability, and failure containment.

Prefer a boring architecture with measurable margin over an elegant architecture that depends on unverified assumptions.

### 5. Freeze Interfaces and Budgets

Write explicit budgets for:

- Voltage, current, power, ripple, thermal rise, and energy reserve.
- Input range, gain, noise, bandwidth, dynamic range, ADC settling, and uncertainty.
- Loop rate, sample rate, interrupt time, DMA throughput, end-to-end latency, and jitter.
- CPU, RAM, flash, stack, FPGA LUT/FF/BRAM/DSP, and communication bandwidth.
- Motor torque/speed/current, mechanism travel, center of mass, backlash, and structural margin.

Include at least 20% implementation margin unless a different value is justified by verified constraints.

### 6. Pass the Hardware Gate

Before energizing:

- Verify polarity, logic levels, input protection, current limiting, reverse protection, flyback paths, dead time, gate states, and emergency disable.
- Verify decoupling, regulator stability, ground returns, analog/digital partitioning, references, clocks, reset straps, programming pins, and connector pinout.
- Verify every unused or startup pin has a safe state.
- Add test points for every critical rail, reference, feedback signal, clock, reset, actuator command, and fault output.
- Define staged current limits and a first-power-on procedure.

Use [hardware-first.md](references/hardware-first.md) and the relevant domain reference. Do not proceed through a `STOP` item.

### 7. Implement Deterministic Firmware or Logic

Define startup/shutdown state machines, safe outputs, interrupt ownership, DMA buffer ownership, communication recovery, sensor validity, timestamping, watchdog policy, persistent configuration integrity, bounded actuator commands, slew limits, anti-windup, and fault latching.

Route to [mcu-firmware.md](references/mcu-firmware.md), [dsp.md](references/dsp.md), or [fpga.md](references/fpga.md). Keep part-specific register values out of the answer until verified.

### 8. Design the Algorithm Around the Plant

Choose the simplest algorithm that closes the scoring gap with margin. Derive rates from bandwidth and latency. Quantify saturation, noise, bias, drift, quantization, aliasing, packet loss, and computation delay. Provide fallback behavior for invalid measurements or missed deadlines. Validate with recorded data, simulation, or hardware-in-the-loop before full-power operation.

### 9. Bring Up in Layers

Use this order unless a safer order is required:

1. Unpowered inspection and resistance checks.
2. Current-limited rails and static current.
3. Clock, reset, debugger, and minimal heartbeat.
4. One peripheral at a time with known stimulus.
5. Sensor acquisition and timestamp validation.
6. Actuator output without load, then with reduced limits.
7. Open-loop plant identification.
8. Inner loop, then outer loop.
9. Integrated state machine.
10. Official test sequence and fault injection.

Read [debug-validation.md](references/debug-validation.md). Record expected and observed values.

### 10. Validate Score and Survival

Run official tests in judging order, boundary and repeatability tests, power-cycle and brownout tests, cable reconnect, sensor timeout, communication loss, actuator saturation, thermal and rail-sag tests, calibration restore, factory defaults, and at least three unattended full runs after the last change.

Read [contest-execution.md](references/contest-execution.md). Freeze a known-good build and preserve rollback artifacts.

## Domain Routing

| Problem content | Required reference |
|---|---|
| Power converters, inverters, active filters, electronic loads, charging | [power-electronics.md](references/power-electronics.md) |
| Measurement instruments, op-amps, ADC/DAC, LCR, oscilloscopes, cable tests | [analog-instrumentation.md](references/analog-instrumentation.md) |
| RF, audio, modulation, optical links, Ethernet, synchronization | [signals-communications.md](references/signals-communications.md) |
| Cars, UAVs, ball/beam, maglev, tracking, coordinated motion | [control-robotics.md](references/control-robotics.md) |
| Inverted pendulum, rotary pendulum, two-wheel balance, wheel-legged systems | [wheel-legged-inverted-pendulum.md](references/wheel-legged-inverted-pendulum.md) |
| Vision, monocular measurement, recognition, edge AI | [vision-ai.md](references/vision-ai.md) |
| MCU selection and firmware architecture | [mcu-firmware.md](references/mcu-firmware.md) |
| Real-time filtering, FFT, fixed point, C2000 or dedicated DSP | [dsp.md](references/dsp.md) |
| Parallel logic, high-speed acquisition, custom timing, FPGA SoC | [fpga.md](references/fpga.md) |

Use [platform-matrix.md](references/platform-matrix.md) when the platform is undecided. Use [historical-taxonomy.md](references/historical-taxonomy.md) for recurring patterns.

## Required Output Contract

For a full solution, output:

1. Known facts and missing evidence.
2. Score/requirement matrix.
3. Minimum viable baseline and score extensions.
4. Architecture comparison and selected chain.
5. Verified component/platform evidence.
6. Electrical, timing, resource, control, and uncertainty budgets.
7. Hardware schematic/PCB/mechanical checklist.
8. Firmware/FPGA/DSP module and state-machine plan.
9. Bring-up and calibration sequence.
10. Acceptance tests, fault injection, and rollback plan.
11. `STOP` / `FIX` / `IMPROVE` findings.

Use [output-templates.md](references/output-templates.md).

## Stop Conditions

Stop and state exactly what is missing when:

- Exact chip, package, board revision, schematic, or power source is unknown and changes electrical validity.
- High-energy or mains-connected hardware lacks isolation, protection, supervision, or safe measurement equipment.
- A motor, propeller, heater, laser, high-voltage stage, or moving mechanism lacks a physical disable and bounded first-test procedure.
- Required accuracy has no calibration path or uncertainty budget.
- Required throughput has no timing/resource proof.
- The proposed method violates an explicit contest restriction.
- Third-party design material has unclear provenance or incompatible licensing.

Do not hide uncertainty behind “adjust as needed.” Convert it into a measurement, calculation, experiment, or explicit question.

## Repository Utilities

- Run `python scripts/build_problem_index.py --help` to rebuild historical metadata.
- Run `python scripts/new_problem_brief.py --help` to create a score-first worksheet.
- Run `python scripts/check_project.py` before publishing changes.
- Consult [source-catalog.md](references/source-catalog.md) for primary-source starting points.
