# Analog and Instrumentation

## 1. Start with the Measurement Equation

Write the equation that maps the physical quantity to the displayed result. List every parameter that must be known, generated, measured, calibrated, or assumed.

Examples include gain/offset conversion, impedance from amplitude and phase, cable length from propagation delay, frequency from counted time, RMS/distortion from samples, and object dimension from calibrated geometry.

Do not select an ADC from bit depth alone. Required performance is determined by the complete signal chain and uncertainty budget.

## 2. Build an Uncertainty Budget

List at least:

- Reference uncertainty and drift.
- Sensor or source tolerance.
- Front-end gain, offset, bias, noise, nonlinearity, common-mode and temperature behavior.
- ADC/DAC offset, gain, INL/DNL, noise, reference, clock, and acquisition settling.
- Fixture, cable, connector, shielding, grounding, loading, and environmental effects.
- Calibration fit error, interpolation, quantization, and repeatability.
- Algorithm windowing, leakage, threshold, timing, and numerical error.

Use root-sum-square only when error terms are suitably independent and statistical. Use worst-case or bounded analysis when dependence is unknown or judging is deterministic.

Target uncertainty comfortably below the allowed error; a design whose theoretical uncertainty equals the tolerance has no manufacturing or field margin.

## 3. Define the Signal Chain at Every Node

| Node | Min/max | Common mode | Source/load impedance | Bandwidth | Noise | Protection | Test point |
|---|---:|---:|---:|---:|---:|---|---|

Review:

- Input impedance and loading of the device under test.
- Attenuation, gain switching, offset injection, and range protection.
- Op-amp input common-mode range and output swing at the actual supply and load.
- Stability with capacitive loads, muxes, ADC kickback, transimpedance nodes, and programmable-gain networks.
- Clamp leakage and capacitance on precision/high-speed nodes.
- Anti-alias filter, reconstruction filter, and group delay.

## 4. ADC Acquisition Is an Analog Event

Verify the ADC input model, sampling capacitor, acquisition window, switch resistance, source impedance, driver settling, channel-to-channel memory, reference drive, and trigger timing.

For multiplexed channels:

- Check worst transition between full-scale channels.
- Allow settling or use dummy conversions if documented and justified.
- Keep source impedance within the calculated limit.
- Validate with an oscilloscope and code histogram, not only a DC display.

For high-speed sampling:

- Derive sample rate and analog bandwidth from the highest relevant input frequency and desired amplitude/phase accuracy.
- Include aperture jitter and clock phase noise when they affect SNR.
- Separate acquisition memory depth, trigger latency, processing throughput, and display rate.

## 5. Waveform Generation and Reconstruction

Define frequency resolution, amplitude accuracy, offset, distortion, load, update artifacts, and reconstruction filtering. Compare DAC, PWM plus filter, DDS, timer toggle, FPGA waveform memory, and analog oscillator based on the score contract.

Verify DAC settling and output compliance or PWM timer resolution and carrier leakage. Do not call a waveform “sine” without measuring harmonics and amplitude across frequency/load.

## 6. Common Instrument Classes

### Oscilloscope and Data Acquisition

Separate input protection/attenuation, trigger, ADC/sample memory, timebase, interpolation, and display. Validate trigger level/hysteresis, pre/post-trigger depth, aliasing, and calibration for every range.

### Frequency, Phase, and Time

Choose reciprocal counting, gated counting, capture timing, phase detector, correlation, or FFT based on range and update time. Budget timebase error, trigger noise, quantization, and channel skew.

### LCR and Impedance

Specify excitation frequency/amplitude, source impedance, fixture compensation, phase measurement, parasitics, and model validity. Use open/short/load calibration when allowed. Check that the chosen equivalent circuit matches the test frequency.

### Spectrum, Distortion, and Modulation

Budget analog front-end linearity, ADC dynamic range, coherent sampling, windowing, FFT length, leakage, noise floor, and amplitude correction. Separate display resolution from true resolution bandwidth.

### Cable and Fault Location

Choose DC mapping/resistance, capacitance, propagation delay/TDR, frequency-response, or impedance methods according to the explicit prohibition list. For delay methods, characterize propagation velocity, threshold bias, launch pulse, termination, connector delay, and reflection ambiguity. For attenuation, control source/load impedance and fixture calibration.

## 7. Calibration Strategy

Define:

- Factory/team calibration versus on-site calibration.
- Reference standards and instrument traceability.
- Number and placement of calibration points.
- Stored coefficients, version, CRC, temperature, and validity range.
- Recovery when calibration is missing or corrupt.
- Fast verification standard for judging day.

Never hide manual tuning inside a process that judging rules require to be automatic.

## 8. PCB and Fixture Rules

- Keep high-impedance nodes short, clean, guarded when necessary, and away from digital/switch nodes.
- Use controlled return paths and avoid forcing sensitive currents through connector or power returns.
- Place reference, decoupling, RC filters, and driver components at the converter pins.
- Model fixture and cable parasitics as part of the instrument.
- Provide ground-safe, repeatable connectors and labeled calibration fixtures.

## 9. Validation

Test zero, near-zero, mid-scale, full-scale, overrange, frequency boundaries, temperature drift, supply variation, repeatability, and cross-channel interference. Retain raw values and final displayed values so algorithm and hardware error can be separated.

Report `STOP` for input ranges that exceed protection or common-mode limits, unsafe probe grounding, missing isolation, or calibration methods that violate the problem statement.
