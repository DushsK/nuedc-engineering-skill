# Signals and Communications

## 1. Freeze the Link Contract

Record source waveform, carrier/baseband range, bandwidth, modulation, symbol/data rate, channel medium, distance, impedance, allowed transmit power, latency, error metric, synchronization time, and judging operation.

Separate:

- Analog fidelity from digital payload correctness.
- Carrier frequency from occupied bandwidth and sample rate.
- Update rate from end-to-end latency.
- Nominal laboratory channel from field interference and multipath.

## 2. Build a Link and Dynamic-range Budget

For every stage, track signal level, noise, gain/loss, bandwidth, linearity, headroom, impedance, and expected interference.

For RF or optical links include path/optical loss, antenna or emitter/receiver pattern, polarization/alignment, legal and contest limits, receiver noise figure/sensitivity, blocker tolerance, and required SNR.

For wired links include source/load impedance, cable loss, reflections, common-mode behavior, shielding, connector effects, and ground-potential differences.

Do not assume a module range or data rate without the exact antenna, supply, environment, protocol overhead, and test conditions.

## 3. Synchronization and Timing

Define acquisition, carrier/timing recovery, frame detection, buffering, processing, retransmission, and output latency. Identify the reference clock and its accuracy/drift.

Verify:

- Sample-clock relationship to carrier/symbol rates.
- Timer/capture or FPGA clock resolution.
- Packet timestamp point and clock-domain crossings.
- Buffer depth under worst burst and processing delay.
- Behavior after lost lock, packet loss, cable reconnect, or channel switch.

## 4. Analog and RF Front End

Review input protection, matching, filters, LNA/VGA/mixer linearity, LO leakage, image response, AGC dynamics, ADC drive, DAC reconstruction, and power-supply coupling.

Measure compression, intermodulation, spurious responses, noise floor, and gain flatness when they can affect scoring. A clean single-tone simulation does not prove multi-tone or blocker performance.

## 5. DSP Chain

Define scaling and rate at each stage:

`ADC -> DC removal/AGC -> filtering -> mixing -> decimation/interpolation -> synchronization -> estimation/demodulation -> decision/output`

For every block specify numeric format, saturation, coefficient precision, state reset, group delay, CPU/FPGA cost, and test vector.

Use coherent sampling when possible. When not possible, apply an appropriate window and correct amplitude/energy interpretation. Verify alias rejection before decimation.

## 6. Communication Families

### Audio and Acoustic

Account for microphone/speaker response, enclosure, AGC, room reflections, ambient noise, propagation delay, and nonlinear distortion. For localization, calibrate channel delay and geometry; timestamp channels from a common clock.

### Visible-light and Infrared

Account for ambient light, emitter modulation bandwidth, photodiode/transimpedance range, optical alignment, saturation, field of view, and safety limits. Provide a loss-of-signal fallback.

### Ethernet and Differential Cables

Treat magnetics, PHY, common-mode termination, differential impedance, connector/shield, clocking, and cable fixtures as part of the system. For custom cable measurement, separate DC continuity/resistance, propagation/reflection, and frequency-response methods.

### Short-range Wireless

Define channel, coexistence, retry and timeout policy, packet freshness, pairing/startup, antenna clearance, and offline fallback. Avoid cloud or Internet dependencies unless the problem explicitly requires and permits them.

### RF Receiver/Transmitter Instruments

Separate analog tuning, LO/reference accuracy, channel filtering, gain control, detection/demodulation, and displayed metrics. Verify spurious and image responses across the full input range.

## 7. Platform Choice

- Choose an MCU when rates and latency fit verified ADC/DMA/timer/CPU budgets.
- Choose a DSP when repeated multiply-accumulate, fixed-point control, or deterministic multi-rate processing dominates.
- Choose an FPGA when parallel I/O, precise timing, high-rate data movement, custom interfaces, or deterministic pipelines dominate.
- Choose an SBC/edge accelerator when vision, large models, networking stacks, or high-level UI dominate, while keeping safety-critical timing on a deterministic controller when needed.

Do not split processing across devices without a timestamp, ownership, transport, startup, and failure plan.

## 8. Validation

Use golden waveforms and recorded channels. Test amplitude/frequency boundaries, weak and strong signals, blockers, noise, offset, clock error, packet loss, reconnect, multipath/alignment, supply variation, and repeated cold start.

Measure end-to-end output, not only intermediate constellation or FFT plots. Preserve raw samples and known test vectors for regression.

Report `STOP` for unsafe RF power, illegal transmission, missing isolation, incompatible I/O levels, or measurement connections that can damage equipment.
