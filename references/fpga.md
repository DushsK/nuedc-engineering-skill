# FPGA Engineering

## 1. Choose FPGA for a Proven Reason

Use FPGA/CPLD when the problem needs deterministic parallel timing, high-rate data acquisition, precise pulse generation, custom protocols, many synchronized channels, streaming DSP, or hardware interfaces that an MCU cannot meet with verified margin.

Do not choose FPGA solely for prestige. Include HDL/tool learning, constraints, board power, configuration, and verification time in the architecture comparison.

## 2. Lock the Exact Device and Board

Record device family, part number, package, speed grade, board revision, configuration method, memory, oscillators, I/O bank voltages, connectors, ADC/DAC interfaces, and tool version.

Verify official device handbook/data sheet, pinout, clocking guide, I/O guide, configuration guide, errata/advisories, board schematic, and tool device support.

## 3. Partition the Design

Use explicit modules and clock domains:

- Reset and configuration supervision.
- Clock generation and monitoring.
- Input capture/deserialization.
- CDC and buffering.
- DSP/measurement/control pipeline.
- Output generation/serialization.
- Register/control interface.
- Fault monitor and safe output.
- Debug capture and test pattern generation.

Define latency, throughput, width, numeric format, backpressure, and reset behavior at every interface.

## 4. Clock and Reset Discipline

- Use dedicated clock-capable pins and documented clock resources.
- Constrain every primary and generated clock.
- Define clock relationships, uncertainty, and false/asynchronous paths deliberately.
- Synchronize reset deassertion within each clock domain.
- Handle PLL/MMCM lock loss and startup ordering.
- Do not use fabric-generated clocks when a clock enable or proper clock resource is required.

Simulation without timing constraints does not prove hardware timing.

## 5. Clock-domain Crossing

Classify each crossing:

- Single-bit level: synchronizer with source stability assumption.
- Pulse/event: pulse stretching, toggle handshake, or event counter.
- Multi-bit control: handshake or stable-bus protocol.
- Streaming data: asynchronous FIFO with verified depth and reset behavior.
- Gray counter/pointer: only with the complete approved pattern.

Never synchronize each bit of a multi-bit bus independently. Document metastability assumptions and run tool CDC analysis when available.

## 6. I/O and Board Electrical Review

Verify bank VCCO/VREF, I/O standard, drive strength, slew, differential termination, clock input type, external pull/termination, connector pinout, and startup/configuration state.

Check that configuration pins and unconfigured FPGA outputs cannot enable a power stage or hazardous actuator. Use external safe pulls and downstream enable logic.

For high-speed ADC/DAC or memory interfaces, review trace impedance, length/skew, reference clock, source/parallel termination, input delay resources, training/calibration, and board signal integrity.

## 7. Timing Constraints and Closure

At minimum:

- Create clocks and generated clocks.
- Constrain input/output delays relative to external devices.
- Define asynchronous groups and justified exceptions.
- Check setup, hold, pulse width, recovery/removal, and unconstrained paths.
- Review worst paths after implementation, not only synthesis.
- Preserve margin across process, voltage, temperature, and speed grade.

Do not fix timing by declaring false paths unless the path is functionally asynchronous and safely handled.

## 8. Streaming DSP and Numeric Design

Define pipeline rate, latency, bit growth, rounding, saturation, coefficient precision, BRAM/DSP use, and overflow flags. Align parallel metadata such as valid, channel, timestamp, and frame markers through every pipeline stage.

Use backpressure or overflow policy. A pipeline that silently drops samples invalidates measurement and control results.

## 9. HLS and Generated IP

Treat generated IP as code requiring review:

- Exact version and license.
- Interface protocol and clock/reset assumptions.
- Latency and initiation interval.
- Numeric conversion and resource use.
- Unsupported corner cases.
- Simulation model versus synthesized behavior.

Do not accept HLS results without post-synthesis timing/resource review and target test vectors.

## 10. Verification Ladder

1. Unit simulation with self-checking vectors.
2. CDC and lint/static checks.
3. Synthesis warnings and resource review.
4. Place-and-route timing with complete constraints.
5. On-board clock/reset/ID test.
6. Internal test pattern through the complete pipeline.
7. Logic-analyzer/ILA capture at boundaries.
8. External instrument verification.
9. Fault tests for clock loss, overflow, reset, link loss, and invalid control.

Keep a known-good bitstream, constraints, tool version, and programming path that does not depend on the latest experimental design.

Report `STOP` for unknown I/O bank voltage, unconstrained critical clocks/paths, unsafe configuration startup, unhandled CDC, or bitstreams built for an unverified device/package/board.
