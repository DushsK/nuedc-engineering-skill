# Example: 2001 B - Digital Storage Oscilloscope

Source metadata: [historical index](../data/historical-problems.csv). Obtain the original statement from the source link in that row.

## Score-first Interpretation

The core chain is:

`protected high-impedance input -> selectable attenuation/gain -> trigger -> ADC/timebase -> acquisition memory -> reconstruction/display`

The basic score depends on single-trigger acquisition, input loading, vertical/time ranges, bandwidth/accuracy, adjustable rising-edge trigger, and visibly low distortion. Extensions add continuous acquisition, dual channel, deeper memory/navigation, and higher sensitivity.

## Minimum Verifiable Baseline

- One protected channel and two proven vertical ranges.
- One accurate timebase range first, then the remaining ranges.
- Rising-edge trigger with observable level and hysteresis.
- Capture memory with deterministic trigger position.
- Output to a standard oscilloscope/display path without requiring forbidden adjustment.

## Critical Budgets

- Input impedance and capacitance across frequency.
- Front-end common mode, protection leakage, noise, gain and bandwidth.
- ADC sample rate, ENOB, acquisition settling and clock error.
- Memory depth versus time span and trigger latency.
- Reconstruction/display update rate versus acquisition integrity.

## Hardware Gate

- `STOP`: input protection or common-mode range is unverified.
- `FIX`: vertical accuracy has no calibration path.
- `FIX`: trigger and acquisition do not share a deterministic timebase.
- `IMPROVE`: store raw samples and calibration coefficients for repeatable tests.

## Bring-up

1. Validate input resistance/protection unpowered.
2. Calibrate DC gain/offset with known voltages.
3. Inject a low-frequency sine and verify sampled values.
4. Validate trigger with a square wave and GPIO timing marker.
5. Sweep frequency/amplitude and compare displayed result with a reference instrument.
6. Add memory navigation and dual-channel features only after the basic chain passes.
