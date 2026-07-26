# Historical NUEDC Taxonomy

## Dataset Scope

The generated index currently contains 206 problem records spanning 1994-2026 from public repository metadata. The 2022 source set contains distinct July and October national events, which are preserved as `national-july` and `national-october`. All nine 2026 records currently indexed are from the April Jilin regional event and must not be presented as national competition problems.

See [`../data/historical-problems.csv`](../data/historical-problems.csv) and [`../data/historical-summary.md`](../data/historical-summary.md). Original problem PDFs are not redistributed by this project.

## Multi-label Counts

The initial rule-based index reports:

| Category | Records |
|---|---:|
| Control and robotics | 53 |
| Instrumentation | 44 |
| Power electronics | 41 |
| Analog and RF | 33 |
| Communications and networking | 30 |
| Sensing, vision, and AI | 22 |
| Integrated system / fallback | 18 |
| Digital systems and FPGA candidates | 15 |
| Biomedical and environmental | 11 |

Counts overlap because real problems combine domains. The overlap is the important lesson: a “car” problem may also require power, vision, communication, instrumentation, and mechanics.

## Evolution by Era

### 1994-2007: Fundamental Electronics and Instruments

Recurring themes include regulated sources, amplifiers, waveform generators, frequency/phase measurement, oscilloscopes, data acquisition, radio receivers, filters, and early autonomous vehicles.

Core preparation:

- Op-amp and transistor signal chains.
- ADC/DAC, counters, timers, memory, and displays.
- Input protection, calibration, triggering, timebase, and uncertainty.
- Basic RF/audio modulation and receivers.
- Motor drive and simple closed-loop motion.

### 2009-2015: Integrated Power, Control, and Communication

Problems increasingly combine converter control, autonomous vehicles, quadrotors, pendulums, spectrum/RF instruments, optical communication, and complex mechanical fixtures.

Core preparation:

- Synchronized PWM/ADC and protection.
- State machines, IMU/encoder estimation, and actuator sizing.
- Digital filtering, FFT, frequency response, and communication links.
- Mechanical design as part of the control problem.

### 2016-2021: Multi-domain Intelligent Systems

Common patterns include sorting and delivery mechanisms, tracking, wireless charging, Internet-connected measurement, mixed-signal transmission, energy storage, UAV tasks, and recognition.

Core preparation:

- Multi-controller interfaces and timestamps.
- Vision/sensing plus deterministic control.
- Energy management and battery sag.
- Automated calibration and unattended judging flows.
- Fault recovery and robust field operation.

### 2022-2025: Perception, Networking, Cooperative Systems, and Advanced Power

Examples include cooperative vehicles/UAVs, sound localization, modulation recognition, inverter parallel operation, cable and circuit-model measurement, monocular measurement, aiming, AI-assisted inspection, and active power filtering.

Core preparation:

- Edge vision/AI deployment with geometric calibration and fallback.
- Ethernet/differential cable physics, TDR-like timing, and impedance.
- Multi-rate DSP and model/parameter estimation.
- Distributed timing, synchronization, and communication failure handling.
- Bidirectional and grid-related power stages with hardware trip paths.

## Recurring Knowledge Chains

### Measurement Chain

`protected input -> range/gain -> anti-aliasing -> ADC/timebase -> estimation -> calibration -> display/report`

Repeated traps: input loading, common-mode violation, ADC settling, trigger ambiguity, timebase error, fixture parasitics, and confusing display resolution with accuracy.

### Power Chain

`source -> topology -> switches/magnetics -> sensing -> synchronized control -> hardware trip -> thermal validation`

Repeated traps: headline current ratings, missing dead time, unsynchronized sampling, saturated magnetics, unsafe probes, and software-only overcurrent protection.

### Motion Chain

`trajectory/state machine -> controller -> bounded actuator -> mechanism/contact -> sensor/estimator -> fault monitor`

Repeated traps: reversed signs, undersized torque, unmeasured latency, mechanical backlash, missing fall/stall logic, and tuning before identification.

### Communication Chain

`physical medium -> front end -> synchronization -> DSP/protocol -> validity/timestamp -> application fallback`

Repeated traps: no link budget, stale packets, uncontrolled AGC, clock mismatch, missing impedance control, and Internet dependency in an offline judging environment.

### Vision Chain

`optics/exposure -> calibrated image -> detection/geometry -> confidence/validity -> timestamp -> control permission`

Repeated traps: dataset leakage, pixel-to-distance shortcuts, frame age, lighting dependence, thermal throttling, and confidence used as a safety guarantee.

## Representative Cross-domain Lessons

- A digital storage oscilloscope problem couples input protection, analog bandwidth, trigger design, sample memory, timebase accuracy, and display behavior.
- A rotary inverted pendulum couples self-made mechanics, motor authority, swing-up, capture region, state estimation, travel limits, and disturbance recovery.
- A parallel inverter problem couples power-stage safety, synchronized sampling/PWM, phase/current control, hardware trip, and thermal/EMI layout.
- A signal-separation problem couples analog dynamic range, coherent sampling, DSP model selection, numeric scaling, and objective validation.
- A monocular measurement problem couples optics, calibration geometry, target detection, compute latency, uncertainty, and rejection of invalid views.
- An Ethernet cable tester couples connector mapping, DC resistance, impedance/attenuation, propagation delay, fixture calibration, timing resolution, and judging restrictions.

## How to Use the Taxonomy

When a new problem arrives:

1. Assign multiple categories and hardware hints.
2. Find historical problems with the same physical chain, not only similar titles.
3. Reuse test methods, failure modes, and architecture patterns.
4. Re-check current restrictions and component availability.
5. Avoid copying old circuits without recalculating the new range, accuracy, timing, and parts.

The taxonomy is a navigation aid, not a claim that every problem or knowledge point is completely captured. Improve it through evidence-backed pull requests and regenerate the data files with `scripts/build_problem_index.py`.
