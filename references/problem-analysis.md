# Problem Analysis and Score Contract

## Contents

1. Reading order
2. Score contract
3. Hidden constraints
4. Feasibility proof
5. Baseline and extensions
6. Acceptance tests
7. Report evidence

## 1. Reading Order

Read the original statement in this order:

1. Task diagram and physical object.
2. Basic requirements.
3. Extension requirements.
4. Notes and prohibited methods.
5. Judging operation and calibration permissions.
6. Scoring table.
7. Official clarifications and component list.

Do not begin with the title alone. A title such as “test instrument” does not reveal whether judging allows calibration, cable reconnection, manual adjustment, multiple supplies, or a commercial module.

## 2. Build the Score Contract

Create one row for every scored item and every mandatory note:

| ID | Points | Requirement | Metric/tolerance | Test stimulus | Time limit | Operator action | Proof method | Dependency | Status |
|---|---:|---|---|---|---|---|---|---|---|

Rewrite prose into observable pass/fail statements.

Bad: “测量应准确。”

Good: “For a 10 m to 50 m cable, display length within the stated relative error in less than the stated test time, after only the allowed start action.”

For every row, define:

- Input range and boundary values.
- Output format and update behavior.
- Allowed setup and calibration.
- Reference instrument or standard value.
- Number of repeated trials.
- Exact formula for error, time, overshoot, stability, or efficiency.
- Evidence to capture for the report.

## 3. Extract Hidden Constraints

Search the notes for constraints that often decide feasibility:

- One-button or unattended judging.
- No manual adjustment after start.
- No modification of the judging instrument.
- Maximum supply voltage, single-supply operation, or battery-only operation.
- Maximum size, mass, travel, angle, cable length, or safety enclosure.
- Calibration samples supplied on site.
- Prohibited sensing methods, commercial instrument modules, or finished control boards.
- Required self-made mechanical structures.
- Specific connector, shielding, grounding, or interface conditions.
- Reset, initial position, recovery, and total test time.

Add each constraint to the score contract even when it carries no explicit points. Violating a note can invalidate many scored functions.

## 4. Prove Feasibility Before Parts Selection

Perform minimum calculations for the problem class.

### Measurement

- Required resolution and effective number of bits.
- Noise, offset, gain, linearity, drift, reference, fixture, and repeatability contributions.
- Required analog bandwidth and settling time.
- Calibration model and number of calibration points.

### Control and Robotics

- Required force, torque, speed, travel, acceleration, braking distance, and control authority.
- Sensor range and update rate.
- Plant bandwidth, loop rate, latency, and actuator saturation.
- Mechanical tolerance, friction, backlash, balance, and center-of-mass uncertainty.

### Power Electronics

- Input/output range, peak and average power, current ripple, semiconductor stress, magnetic saturation, thermal loss, and protection thresholds.
- Measurement isolation and safe test equipment.

### Communication and DSP

- Carrier/sample/symbol rate, occupied bandwidth, SNR, dynamic range, synchronization time, data volume, and processing latency.
- Anti-aliasing and reconstruction requirements.

Reject a concept when the requirement has no quantitative path to margin.

## 5. Split Baseline from Extensions

Define three layers:

| Layer | Goal | Rule |
|---|---|---|
| Minimum verifiable baseline | Secure basic functions and judging flow | Use proven parts and the shortest observable signal chain |
| Robust baseline | Add calibration, fault handling, repeatability, and unattended operation | Complete before high-risk extensions |
| Score extensions | Add functions that directly increase points | Each extension must be independently disableable |

Do not let an extension destabilize the baseline. Use feature flags, separate state-machine branches, replaceable modules, or explicit build profiles.

Estimate each extension with:

`expected value = points × success probability - integration risk - recovery cost`

The formula is qualitative unless probabilities are measured, but it forces explicit tradeoffs.

## 6. Compare Architectures

Compare complete chains rather than isolated chips:

| Criterion | Weight | Option A | Option B | Evidence |
|---|---:|---:|---:|---|
| Basic score coverage | | | | |
| Extension score coverage | | | | |
| Analog/control margin | | | | |
| Parts and tools already available | | | | |
| Bring-up time | | | | |
| Calibration complexity | | | | |
| Repairability and observability | | | | |
| Safety and failure containment | | | | |

If the winning option changes when one optimistic assumption is removed, the decision is not robust. Measure that assumption first.

## 7. Write Acceptance Tests Before Implementation

For each score row, define:

1. Fixture and instruments.
2. Initial state.
3. Exact operator actions.
4. Input sequence and boundary points.
5. Expected result and tolerance.
6. Logs, screenshots, waveforms, photos, or measurements to retain.
7. Reset and repeat sequence.

Add robustness tests for power cycle, brownout, cable reconnect, sensor loss, communication timeout, actuator saturation, thermal rise, and calibration reload when relevant.

## 8. Design the Report Evidence

The report should explain why the device meets the scoring contract, not merely describe modules. Preserve:

- Architecture comparison and rejected alternatives.
- Equations, assumptions, and measured parameters.
- Schematics, PCB and mechanical drawings with revision identifiers.
- Calibration method and uncertainty budget.
- Test fixture, instrument models, settings, raw data, and repeated results.
- Failure cases and the fix that changed the evidence.

Build tables and plots during development. Reconstructing evidence at the end wastes contest time and hides regressions.
