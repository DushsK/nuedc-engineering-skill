# DSP and Real-time Signal Processing

## 1. Start from the Signal Contract

Record input range, bandwidth, sample rate, channel count, SNR/dynamic range, latency, output metric, update rate, and scoring tolerance. Define the analog anti-aliasing and reconstruction chain before digital algorithms.

## 2. Prove the Rate Plan

For every stage, document:

`physical bandwidth | sample rate | numeric format | block size | latency | compute cost | memory | output rate`

Verify alias attenuation before each decimator and image rejection after each interpolator. A high ADC sample rate does not replace an analog anti-alias filter.

For block processing, include acquisition time and queueing delay. A fast FFT kernel can still violate end-to-end latency because the block must first fill.

## 3. Numeric Representation

Choose floating point or fixed point based on verified processor capability, dynamic range, latency, and team experience.

For fixed point:

- Define Q format at every interface.
- Track headroom, coefficient quantization, intermediate width, rounding, and saturation.
- Prove accumulator width for worst-case inputs.
- Use scaled test vectors near zero and full scale.
- Compare target output against a high-precision reference.

For floating point, still define NaN/Inf, denormal, overflow, casting, and reproducibility behavior.

## 4. Filtering

Specify passband, stopband, ripple, attenuation, transition width, phase/group delay, startup transient, and coefficient precision.

- FIR offers linear phase and predictable stability at a potentially higher compute cost.
- IIR is efficient but requires stability, coefficient sensitivity, state initialization, and saturation analysis.
- Adaptive filters require reference-signal validity, convergence, step-size bounds, and behavior during signal loss.

Test impulse, step, sine sweep, noise, full-scale, and reset/state-transition behavior.

## 5. FFT, Spectrum, and Parameter Estimation

Define coherent sampling or window choice, FFT length, overlap, amplitude normalization, noise bandwidth, peak interpolation, and update rate.

Distinguish:

- Bin spacing from true resolution.
- Display noise floor from analog system noise floor.
- Peak amplitude from RMS/energy metrics.
- Frequency estimate bias from clock error and leakage.

For phase, modulation, distortion, or impedance estimates, validate with synthetic vectors and laboratory signals whose uncertainty is better than the scoring tolerance.

## 6. Real-time Data Movement

Design the data path before kernels:

`peripheral trigger -> DMA/EDMA -> ping-pong/ring buffer -> processing -> output DMA/peripheral`

Define buffer ownership, cache behavior, alignment, burst size, overflow/underflow, deadline monitor, and stale-output policy. Avoid copying large blocks when ownership transfer or zero-copy is safe and simpler.

Budget bus/memory contention between ADC, DAC, camera, display, logging, and CPU/accelerator.

## 7. Dedicated DSP and C2000 Review

Verify exact memory architecture, DMA/EDMA, cache, accelerator/CLA, peripheral triggers, compiler options, library version, linker sections, and debug behavior.

For C2000 control/DSP workloads, coordinate ePWM, ADC SOC/EOC, CMPSS/trip zones, CLA/DMA, and control computation so the sample-to-actuation delay is measured and deterministic.

For CMSIS-DSP or vendor libraries, verify supported core, data type, initialization, buffer requirements, coefficient layout, and scaling. Library availability does not prove the entire pipeline fits its deadline.

## 8. Multi-rate and Multi-core Systems

- Make rate changes explicit and timestamp signals.
- Define producer/consumer ownership and synchronization.
- Keep one authoritative state for calibration and mode.
- Bound inter-core/inter-processor transport latency.
- Define output when a worker misses its deadline or returns invalid data.

## 9. Verification

Maintain golden vectors with expected output and tolerances. Run them on the target build, not only in Python/MATLAB.

Test:

- Zero, impulse, step, single tone, multi-tone, noise, full-scale, overrange, and discontinuities.
- Frequency/sample-rate boundaries.
- Buffer wrap, dropped samples, deadline misses, and reset mid-stream.
- Fixed-point extremes and coefficient corruption.
- End-to-end latency and output accuracy on target hardware.

Report `STOP` when aliasing, numeric overflow, missed deadlines, DMA corruption, or invalid output can propagate into hazardous actuation without containment.
