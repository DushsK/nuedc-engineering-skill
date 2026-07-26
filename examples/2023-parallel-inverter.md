# Example: 2023 A - Parallel Single-phase Inverters

Source metadata: [historical index](../data/historical-problems.csv).

## Score-first Interpretation

The basic path requires one inverter to produce a tightly regulated 50 Hz low-voltage AC output at the stated current, distortion, efficiency, and load-regulation targets. Extensions add two independent inverters in parallel, grid-connected current control, and programmable current sharing.

## Minimum Verifiable Baseline

- One inverter with isolated/controlled measurement, hardware overcurrent and safe gate disable.
- Closed-loop output regulation with synchronized ADC/PWM.
- Verified THD, efficiency including auxiliary consumption, and load regulation.
- Test points that avoid rewiring during judging.

## Extension Architecture

Each inverter needs an independent controller as required by the problem. Coordinate using a clearly defined synchronization/reference method without sharing one control processor. Current sharing requires measured current, bounded setpoint ratio, communication/reference-loss behavior, and a safe transition between standalone, parallel-load, and grid-connected modes.

## Required Evidence

- Switch, driver, magnetic, capacitor and thermal stress table.
- ADC sample instant relative to PWM edges.
- Hardware trip path and measured disable latency.
- Output voltage/current phase, THD, efficiency and regulation test setup.
- Grid connection conditions, isolation and supervised safe procedure.

## Stop Conditions

- `STOP`: no hardware overcurrent or gate-safe reset state.
- `STOP`: unsafe grid/probe/isolation plan.
- `FIX`: auxiliary power omitted from efficiency accounting.
- `FIX`: two-inverter startup or reference loss can create circulating current.
- `IMPROVE`: store pre-fault synchronized current/voltage/PWM logs.
