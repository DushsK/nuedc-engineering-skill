# Debugging and Validation

## 1. Debug by Layer, Not by Hope

Use this order:

1. Power and physical assembly.
2. Clock, reset, debugger, and startup state.
3. One electrical interface or peripheral.
4. Raw sensor/actuator behavior.
5. Timing, DMA, communication, and data validity.
6. Algorithm with recorded or synthetic input.
7. Open-loop plant behavior.
8. Inner closed loop.
9. Outer loops and state machine.
10. Full judging sequence.

Do not tune control or AI parameters while rails, signs, timestamps, or sensor validity remain uncertain.

## 2. Create an Observation Plan

For each layer define:

`expected signal | measurement point | instrument/log | normal range | fault signature | next decision`

Add test points and firmware markers for rails, reset, clocks, ADC triggers, PWM updates, DMA boundaries, communication frames, controller mode, saturation, and faults.

Use a GPIO timing marker or trace facility for hard real-time events. Logs alone can perturb timing or omit the event that caused a reset.

## 3. Reproduce Before Changing

Record:

- Hardware revision, wiring, fixture, supply, battery state, firmware commit/build, configuration, calibration, and tool versions.
- Exact initial state and operator sequence.
- Expected versus observed behavior.
- First observable divergence, not only final failure.
- Whether the failure is deterministic, intermittent, thermal, supply-related, or motion-related.

Change one causal variable at a time. If multiple emergency changes are unavoidable, preserve the previous known-good state and document the bundle.

## 4. Use a Fault Tree

Start from the observed failure and branch by physical layer.

Example for unstable motion:

- Wrong plant direction or coordinate sign.
- Sensor invalid, delayed, noisy, saturated, or misaligned.
- Actuator current/torque insufficient or saturated.
- Loop timing or state update irregular.
- Controller/model/tuning error.
- Mechanical backlash, compliance, contact loss, or power sag.

Use tests that distinguish branches. Do not replace evidence with repeated gain changes.

## 5. Golden Inputs and Loopback

- Feed known voltages, frequencies, packets, waveforms, images, encoder pulses, or recorded sensor streams.
- Add internal loopback/test patterns for communication, FPGA, DSP, and display paths.
- Compare raw input, intermediate values, and final output against a reference implementation.
- Keep golden vectors versioned with tolerances.

When a module passes only with live hardware, it is difficult to regression-test and isolate.

## 6. Timing and Data-integrity Tests

Measure worst-case:

- ISR/task execution, jitter, and missed deadlines.
- DMA fill/consume timing, overflow, buffer wrap, and cache effects.
- End-to-end sample/command latency and age.
- Communication loss, duplicate/out-of-order frames, and reconnect.
- Stack high-water mark, heap fragmentation, queue depth, and log pressure.
- FPGA timing margin, CDC flags, FIFO levels, and backpressure.

Test at maximum channel count, data rate, UI/logging load, and extension-feature combination.

## 7. Calibration Validation

Separate calibration acquisition from measurement validation. Use independent check points not included in the fit. Test coefficient corruption, wrong version, missing data, temperature change, and restore after power cycle.

Retain raw calibration data, fit residuals, coefficient version, date, environment, and reference instrument.

## 8. Fault Injection

At safe energy, inject:

- Power cycle, brownout, reset, and watchdog.
- Sensor disconnect, frozen value, saturation, out-of-range, and stale timestamp.
- Bus timeout, stuck I2C line, packet loss, cable reconnect, and corrupted frame.
- ADC overrange, numerical NaN/Inf, buffer overflow, and deadline miss.
- Motor stall, encoder loss, mechanical limit, and emergency stop.
- Camera loss, invalid confidence, and dropped frames.

Verify detection latency, output containment, latched state, recovery condition, and retained evidence.

## 9. Acceptance Matrix

| Test ID | Score row | Fixture/input | Initial state | Procedure | Expected | Tolerance/time | Evidence | Repeats | Result |
|---|---|---|---|---|---|---|---|---:|---|

Run nominal, minimum, maximum, boundary, repeated cold-start, and disturbance tests. Use the same operator actions and sequence expected during judging.

## 10. Regression Discipline

After every meaningful change:

1. Run the smallest module test that targets the change.
2. Run affected integration tests.
3. Run the complete basic-score sequence.
4. If hardware-facing or timing-sensitive, repeat power-cycle and fault tests.
5. Update the known-good tag only after evidence is saved.

Do not call a build “stable” because it worked once. Require repeated unattended runs and preserve a rollback image, configuration, calibration, schematic/BOM revision, and programming instructions.

## Debug Output

Report:

`symptom | first divergence | evidence | ruled-out causes | root cause or proof gap | minimal fix | verification | regression risk`

When root cause is unknown, say so and propose discriminating tests rather than a speculative rewrite.
