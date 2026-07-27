# Power Electronics

## Safety Boundary

Treat mains, high voltage, large capacitors, batteries, high-current inductors, and motor buses as hazardous. Require isolation, discharge verification, current limiting, guarded probes, appropriate differential measurement, and experienced supervision. Never suggest defeating protective earth or measuring a floating switching node with an unsafe grounded probe connection.

## Applicable Problem Families

- AC-DC, DC-DC, AC-AC, inverter, UPS, active power filter, microgrid, parallel converter.
- Electronic load, energy recovery, charging, wireless power, LED power, current source.
- Motor drive and regenerative braking when the main difficulty is the power stage.

## 1. Freeze the Electrical Contract

Record minimum/nominal/maximum input and output, allowable ripple, transient response, efficiency target, power factor or distortion metric, isolation requirement, bidirectional behavior, startup time, load profile, and test instrument limits.

Separate:

- Continuous versus transient power.
- RMS, average, peak, and inrush current.
- Nominal versus worst-case source and load.
- Device electrical stress versus thermal stress.
- Basic-score operating region versus extension region.

## 2. Select Topology by Stress and Testability

Compare topology using:

| Question | Evidence required |
|---|---|
| Can it meet conversion ratio across the complete range? | Duty/modulation limits and verified device ratings |
| Can it carry peak and RMS current? | Semiconductor, magnetics, capacitor, connector, and copper loss |
| Can the controller observe the required states? | Voltage/current sensing range, bandwidth, isolation, and ADC timing |
| Can it fail safely? | Fuse/current limit, trip path, gate disable, discharge, and fault latch |
| Can it be built and debugged in contest time? | Parts, magnetics, PCB, instruments, and proven firmware |

Prefer a topology whose worst switching loop and control loop can be observed with available equipment.

### 2.1 Topology Map

Do not treat a topology name as a complete design. First classify conversion direction, isolation, source/load quadrants, gain range, power, switching frequency, transient requirement, EMI/common-mode constraints, available magnetics, controller resources, and safe test capability.

| Family | Common topologies | Typical reason to consider | Main evidence or risk |
|---|---|---|---|
| Non-isolated step-down/up | Buck, boost, inverting buck-boost, non-inverting four-switch buck-boost | Simple DC conversion; output always below, always above, or crossing the input range | Duty limits, switch/diode stress, right-half-plane zero where applicable, mode transition, current ripple |
| Non-isolated extended-gain | SEPIC, Cuk, Zeta, cascaded or interleaved stages | Input/output range or ripple/current-continuity requirement not met by a basic stage | Extra reactive parts, capacitor RMS current, efficiency, startup and control complexity |
| Isolated low/medium power | Flyback, active-clamp flyback, forward, active-clamp forward, push-pull | Isolation, multiple outputs, or transformer ratio is required | Core reset, leakage spikes, clamp loss, cross-regulation, flux imbalance, isolation construction |
| Isolated medium/high power | Half bridge, full bridge, phase-shifted full bridge, LLC/series resonant | Higher power density, lower switch stress, or soft switching | Transformer design, circulating current, ZVS/ZCS operating range, synchronous timing, burst/light-load behavior |
| Bidirectional DC-DC | Synchronous buck/boost, four-switch buck-boost, current-fed bridge, dual-active bridge, CLLC | Storage, regenerative load, energy routing, or two DC buses | Both power directions, precharge, bus absorption, current reversal, phase-shift range, fault isolation |
| AC-DC and PFC | Diode bridge plus boost, interleaved boost, bridgeless/totem-pole, Vienna rectifier, active front end | Power-factor, harmonic, efficiency, or bidirectional grid-interface requirement | Mains isolation, zero crossing, inrush, common-mode EMI, current reconstruction, reverse-recovery/dead-time behavior |
| DC-AC inverter | Single-phase half bridge/H bridge, three-phase two-level bridge, NPC/T-type or other multilevel stages | AC waveform, motor drive, grid/load interface, or reduced device voltage/dv/dt | Neutral-point balance, modulation limits, dead time, output filter, regenerative bus rise, protection coordination |
| AC-AC | Phase-angle regulator, cycloconverter, matrix converter, back-to-back active stages | Direct AC control or variable-frequency conversion | Commutation, bidirectional switch implementation, input/output filtering, mains safety, control complexity |
| Wireless or resonant transfer | Series/parallel compensation, LCC/LCL networks, resonant inverter/rectifier combinations | Loose coupling, isolation through the field, or scoring based on transfer efficiency | Coil alignment, coupling variation, detuning, circulating current, foreign-object heating, measurement method |

For each viable candidate, fill this comparison before selecting:

<code>topology | gain range | isolation | power directions | device stress | magnetics | loss estimate | control order | sensing | EMI | startup/pre-bias | fault path | build/test time</code>

Compare at least two candidates when a meaningful alternative exists. Reject a candidate immediately if it cannot cover the full operating range, safely absorb reverse energy, meet required isolation, or be validated with available instruments. Resonant, bridgeless, multilevel, and bidirectional stages require an explicit operating-region and mode-transition analysis; their best-case efficiency is not sufficient evidence.

Use the official topology-selection and converter-comparison sources in [source-catalog.md](source-catalog.md), then verify the exact controller, switch, magnetic, and reference-design assumptions for the selected stage.

## 3. Calculate the Stress Table

Create a table for every switching device, diode, inductor/transformer, capacitor, shunt, connector, and regulator:

`normal | startup | load step | short/stall | regenerative | maximum source | minimum source | thermal steady state`

Verify:

- Voltage overshoot and ringing, not only ideal bus voltage.
- RMS and peak current in semiconductors and capacitors.
- Inductor/transformer peak flux and saturation margin.
- MOSFET conduction and switching loss at actual gate drive and temperature.
- Diode reverse recovery or synchronous-rectification timing.
- Shunt pulse energy and amplifier common-mode behavior.
- Capacitor ripple current, ESR heating, bias derating, and lifetime.
- Thermal path from junction to ambient under enclosure and airflow conditions.

Do not use headline current ratings without the datasheet test conditions and thermal assumptions.

## 4. Gate Drive and Hardware Trip

- Verify gate voltage, source/sink current, gate resistor, Miller immunity, bootstrap refresh, UVLO, propagation delay, and common-mode transient limits.
- Derive dead time from switch and driver behavior. Excess dead time also creates distortion and loss; copied values are not evidence.
- Route overcurrent, desaturation, comparator, trip-zone, or break input to disable PWM without waiting for the main loop.
- Define startup and reset gate states with hardware pulls.
- Confirm debugger halt, firmware crash, and clock loss cannot leave both switches conducting.

## 5. Sensing and Sampling

For each voltage/current channel, define:

- Full-scale range including transients.
- Isolation and common-mode range.
- Sensor bandwidth, delay, noise, offset, drift, and saturation recovery.
- Anti-aliasing and protection.
- ADC trigger relative to switching edges.
- Acquisition time, source impedance, calibration, and synchronized multi-channel behavior.

Place current samples away from switching transients or explicitly model and filter them. Validate timing on an oscilloscope using PWM, trigger, and sample markers.

## 6. Digital Control Architecture

Use a layered structure:

1. Hardware protection and PWM trip.
2. Fast current or inductor-state loop.
3. Slower voltage/power/energy loop.
4. Supervisory state machine and mode transitions.
5. Telemetry, logging, calibration, and user interface.

Define loop rates, execution budget, ADC-to-PWM latency, saturation, anti-windup, soft start, precharge, zero-crossing or phase synchronization, bumpless transfer, and safe restart.

For C2000 or motor-control MCUs, verify ADC SOC/EOC routing, ePWM synchronization, comparator subsystem, trip zone, CLA/DMA ownership, and errata. For general MCUs, verify advanced-timer break inputs, complementary PWM, dead-time resolution, ADC triggering, and DMA latency.

## 7. Layout Priorities

1. Minimize high-dI/dt power loops.
2. Keep gate-drive loops compact and separate from current-sense inputs.
3. Use Kelvin sensing for shunts and critical feedback nodes.
4. Control switch-node copper and capacitive coupling.
5. Place decoupling and bootstrap components at the device pins.
6. Separate power return, signal return, shield, and chassis intentionally.
7. Provide safe probe points and clearance around hazardous nodes.

## 8. Staged Bring-up

1. Validate controller and PWM timing with the power stage disabled.
2. Confirm hardware trip using a low-energy stimulus.
3. Power gate drivers and inspect gate waveforms without the main bus.
4. Apply a reduced, current-limited bus with a benign load.
5. Run open loop at bounded duty and confirm polarity and sensing.
6. Close the inner loop with conservative limits.
7. Add outer loops, mode transitions, and regenerative cases.
8. Increase voltage/current while recording loss, temperature, ripple, and fault margin.

## 9. Required Tests

- Minimum/maximum input and load.
- Startup, shutdown, repeated restart, and pre-biased output.
- Load step and command step.
- Short, overcurrent, sensor fault, and lost-control tests at safe energy.
- Regeneration and source removal when applicable.
- Efficiency and thermal mapping across the scoring region.
- Harmonic, ripple, power-factor, or dynamic metrics using the official calculation method.
- Brownout and watchdog behavior.

Report `STOP` for unsafe isolation, missing hardware overcurrent, uncontrolled gate state, saturated magnetics, or measurement setups that can short hazardous nodes.
