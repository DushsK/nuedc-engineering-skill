# Contest Execution and Field Survival

## 1. Organize Around a Demonstrable Baseline

The first milestone is not “all modules written.” It is one end-to-end function that can be judged with visible evidence.

Maintain three branches of work:

- **Known-good baseline**: always buildable and demonstrable.
- **Integration candidate**: current combined system.
- **Experimental extension**: isolated high-risk scoring work.

Do not develop risky extensions directly on the only working build.

## 2. Allocate Team Roles by Interfaces

Typical roles:

- Hardware/power/PCB and safety.
- Firmware/control/DSP/FPGA.
- Mechanical/vision/test/report.

Define ownership at interfaces: connector, message, coordinate frame, calibration file, sample rate, actuator command, and test fixture. Every interface needs an agreed unit, sign, range, timing, and failure behavior.

## 3. Timebox by Proof

Adapt the exact schedule to the event duration, but preserve this order:

1. Parse scoring and restrictions.
2. Freeze the baseline architecture and buy/build list.
3. Prove power, core controller, and one signal path.
4. Demonstrate the minimum end-to-end function.
5. Add calibration and repeatability.
6. Integrate score extensions one at a time.
7. Freeze hardware, then software features.
8. Run full judging rehearsals and finish the report from saved evidence.

Set abandonment criteria for every extension. Examples: missing critical part, no observable prototype by the deadline, unstable baseline after integration, or unbounded calibration time.

## 4. Version Everything That Changes Results

Record:

- Source commit and build artifact hash.
- Toolchain, libraries, FPGA project/tool version, model/runtime version.
- PCB/schematic/BOM and mechanical revision.
- Wiring and connector map.
- Configuration and calibration version.
- Test fixture, instrument, settings, and raw data.

Keep a one-command or one-page recovery procedure for programming the known-good build.

## 5. Parts and Physical Logistics

- Maintain a BOM with quantity, substitutes, package, and location.
- Keep spare regulators, drivers, sensors, connectors, cables, storage media, and mechanically fragile parts.
- Pre-build test fixtures, programming cables, adapters, attenuators, dummy loads, and current-limited power paths.
- Label boards, cables, polarities, and revisions.
- Keep tools for field repair and a clean area for precision analog/optical work.

Substitutes require rechecking pinout, electrical limits, compensation, timing, and calibration. “Drop-in compatible” is not accepted without evidence.

## 6. Freeze Strategy

Freeze in layers:

1. Mechanical envelope and critical geometry.
2. Power and connector interfaces.
3. Basic hardware revision.
4. Baseline firmware/logic.
5. Calibration format and judging UI.
6. Extensions.

After freeze, accept only changes with a named score or reliability benefit, a rollback path, and a targeted verification plan.

## 7. Judging Rehearsal

Recreate:

- Device transport and cold start.
- Official initial state, supplied samples, cables, targets, and allowed calibration.
- Exact button presses and operator actions.
- Judge-visible display and status indicators.
- Test order, reset, and timeout.
- Failure recovery without opening a laptop unless allowed.

Ask a teammate unfamiliar with the latest build to operate from the written procedure. Ambiguous UI or hidden setup steps should fail rehearsal.

## 8. Field Reliability Checklist

- Deterministic startup and clear self-test result.
- Safe output through reset, programming, and cable disconnect.
- Battery/rail monitoring and brownout behavior.
- Thermal margin after repeated operation.
- Sensor and connector strain relief.
- Calibration verification standard.
- Offline operation without fragile Internet/cloud dependency.
- Error code or log retrieval without destroying evidence.
- Spare configuration and factory-default recovery.
- Known-good binary/bitstream/model on multiple media.

## 9. Report While Building

Create figures, tables, equations, calibration plots, test results, and failure analysis as evidence becomes available. Keep design claims tied to the score contract.

The report should include:

- Architecture comparison.
- Key theoretical analysis and component evidence.
- Complete signal/power/control chain.
- Calibration and uncertainty.
- Test setup, raw/processed results, repeatability, and limitations.
- Safety and fault handling.

Do not fabricate missing data near the deadline. Mark unverified extensions honestly and protect the proven baseline.

## 10. Final Release Gate

Before transport or submission:

- [ ] Three unattended full judging runs pass.
- [ ] Power-cycle and reset behavior pass.
- [ ] Known-good artifact and rollback instructions exist.
- [ ] Calibration and configuration reload pass.
- [ ] Hardware, wiring, mechanical, and firmware revisions match the report.
- [ ] All `STOP` and `FIX` findings are closed or the affected feature is disabled.
- [ ] The team can demonstrate the basic function without development tools.
