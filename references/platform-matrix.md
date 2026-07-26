# Platform Selection Matrix

## Principle

Choose the smallest platform that meets verified I/O, timing, memory, toolchain, and team-skill requirements with margin. A more powerful processor can reduce algorithm risk while increasing power, boot, software, and integration risk.

## Platform Classes

| Class | Strong fit | Main strengths | Main blind spots |
|---|---|---|---|
| Low-cost MCU | UI, sensors, simple instruments, state machines, moderate control | Fast startup, deterministic timers, low power, simple PCB | Limited analog quality, memory, compute, high-rate interfaces |
| Control MCU | Motors, inverters, power conversion, precise synchronized sampling | Advanced PWM/ADC/comparator/trip resources | Steeper peripheral and power-stage learning curve |
| High-performance MCU | Multi-rate control, USB/Ethernet, larger DSP, displays | CPU, DMA, memory, rich peripherals | Cache/coherency, power, complex clocks, larger software stack |
| Dedicated DSP | Real-time filters, FFT, control, multi-channel acquisition | Deterministic MAC/data movement and control peripherals | Numeric scaling, toolchain, memory architecture, smaller ecosystem |
| FPGA/CPLD | Parallel timing, high-speed acquisition, protocol logic, deterministic pipelines | Precise concurrency and custom interfaces | HDL verification, timing closure, board/clock/I/O complexity |
| FPGA SoC | FPGA pipeline plus Linux/control/UI | Tight heterogeneous integration | Boot, memory, software/logic partition, high complexity |
| SBC/edge AI | Vision, large models, networking, UI | Mature high-level libraries and compute | OS latency, boot, storage, thermal, power, weak hard-real-time behavior |
| Hybrid controller + SBC/FPGA | Vision or high-speed processing plus safe control | Separates workloads and preserves deterministic safety | Timestamping, protocols, startup ordering, ownership, more hardware |

## Common Families to Consider

This table is a routing guide, not a specification. Verify the exact current device documentation.

| Family | Typical contest role | Required review focus |
|---|---|---|
| STM32 G4/F4/H7 and related | General control, instruments, motor/power, displays, Ethernet/USB | Exact device/package, clocks, timer/ADC/DMA routing, advanced PWM, cache on M7, board schematic and errata |
| TI MSPM0 | Entry/general control, analog-assisted sensing, official-board ecosystems | Exact TRM, event/timer routing, ADC/comparator resources, SysConfig output, LaunchPad schematic |
| TI C2000 | Digital power, motor control, synchronized high-rate control | ePWM, ADC SOC, CMPSS/trip zone, CLA/DMA, loop latency, real-time debug, errata |
| TI TM4C and other Cortex-M | General control and communication | Clock/pin/DMA/timer/ADC specifics and board revision |
| NXP Kinetis/i.MX RT | High-performance control, audio, networking, displays | FlexPWM/timers, ADC, cache, external memory, high-speed PCB, SDK/errata |
| GD32 and compatible-looking MCUs | Cost-sensitive general control | Never assume STM32 equivalence; verify clocks, peripherals, errata, libraries and pins |
| Microchip SAM E5x / dsPIC33-class | General embedded, motor control, digital power, mixed-signal timing | Event routing, PWM/ADC synchronization, DSP engine/compiler behavior, exact package, errata and board support |
| RP2040/RP2350-class | Custom I/O with PIO, education, moderate control | PIO/DMA timing, external flash/boot, dual-core ownership, ADC/board limitations |
| ESP32-S3 and related | Wireless, UI, camera, moderate edge AI | RTOS/radio jitter, boot straps, exact module, ADC limitations, PSRAM/cache, antenna and power |
| Kendryte/Sipeed-class AI devices | Embedded vision and accelerators | Camera interfaces, supported operators, memory, toolchain, deployment determinism and documentation |
| AMD/Xilinx Artix-7/Zynq-7000 | High-rate acquisition, custom DSP, FPGA plus processor | I/O banks, clocking, constraints, CDC, configuration, board memory and tool support |
| Intel Cyclone 10 and related | FPGA timing, acquisition, custom protocols | Device handbook, I/O banks, PLLs, timing constraints, configuration and Quartus support |
| Lattice ECP5/iCE40-class | Compact FPGA glue logic, timing engines and moderate streaming pipelines | Exact device/package, sysIO banks, PLLs, configuration flash, open/vendor tool support and timing closure |
| Raspberry Pi/Jetson-class SBC | OpenCV, AI, networking, UI | Boot, storage, OS scheduling, camera drivers, thermal/power, deterministic-controller interface |

## Selection Questions

Answer before choosing:

1. What is the fastest physical deadline and what creates it?
2. Which peripherals must be synchronized in hardware?
3. What analog performance must be external regardless of processor?
4. What is the worst data rate and memory depth?
5. Which functions require hard real time versus soft real time?
6. What platforms has the team already brought up and debugged?
7. Can the PCB, power, clock, and signal-integrity requirements be met in time?
8. What is the fallback if the advanced platform or toolchain fails?

## Partitioning Rules

- Keep emergency stop, actuator bounds, and fastest safety trips near the hardware.
- Keep camera/AI/UI/networking on a richer processor when required, but timestamp and validate every command crossing into control hardware.
- Use FPGA for deterministic streaming/timing, not merely because it appears advanced.
- Avoid two controllers performing the same control decision without a clear authority protocol.
- Define boot ordering, version compatibility, heartbeat, timeout, safe defaults, firmware update, and log correlation for every inter-processor link.

## Decision Output

Produce:

`candidate | verified resources | missing evidence | development risk | baseline fit | extension fit | fallback`

Reject any candidate whose critical capability is supported only by family reputation, a marketplace description, or a generated configuration screenshot.
