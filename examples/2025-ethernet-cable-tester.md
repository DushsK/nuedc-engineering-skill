# Example: 2025 D - Ethernet Twisted-pair Cable Tester

Source metadata: [historical index](../data/historical-problems.csv).

## Score-first Interpretation

The problem combines two-ended wire-map/type/DC-resistance/attenuation measurement with one-ended length, short detection, and short-position measurement. It limits supply voltage, judging interaction, time, and the use of non-electrical or finished instrument methods.

## Separate the Measurement Modes

### Two-ended

- Wire map and crossover detection.
- Shield/type detection with a connector/chassis strategy.
- DC resistance with lead/contact compensation.
- High-frequency attenuation with controlled source/load impedance and fixture calibration.

### One-ended

- Cable presence and short detection.
- Length and fault location from an electrical propagation/reflection method.
- Propagation-velocity calibration using allowed reference cables.

## Critical Budgets

- Launch-pulse edge, timing resolution, threshold bias, connector delay and reflection ambiguity.
- Cable propagation variation and calibration interpolation.
- Source/load impedance at the attenuation frequency.
- DC excitation, ADC resolution, contact resistance and self-heating.
- Mode-switch leakage/parasitics and protection across eight conductors plus shield.

## Architecture Guidance

Use a fixture-aware analog front end, protected switching matrix, precise timing/capture path, calibrated ADC path, and state machine that completes each mode after one start action. FPGA/fast comparator/TDC-style timing may help only if the team can prove I/O voltage, timing calibration and resource constraints; a well-designed MCU capture path may be sufficient depending on the measured edge and cable range.

## Validation

- Straight/crossover maps and injected open/short faults.
- Multiple cable lengths and independent check points.
- Connector remating and shield cases.
- Near/far short locations.
- Attenuation fixture open/short/load characterization.
- Completion time and repeated cold start.

`STOP` for unsafe cable excitation, unverified I/O protection, or probe/fixture methods that violate the problem restriction.
