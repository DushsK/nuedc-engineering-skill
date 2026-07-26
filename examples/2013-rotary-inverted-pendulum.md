# Example: 2013 C - Rotary Inverted Pendulum

Source metadata: [historical index](../data/historical-problems.csv).

## Score-first Interpretation

The problem separates energy-building/swing-up, externally assisted capture, autonomous swing-up, disturbance recovery, and arm rotation while maintaining balance. Mechanical dimensions and travel limits are part of the control contract.

## Minimum Verifiable Baseline

- Self-made mechanism with measured arm/pendulum geometry and low backlash.
- Encoder/state sensing with verified signs and timestamps.
- Bounded motor driver with current limit and emergency disable.
- Manual near-upright capture followed by a local stabilizer.
- Logs for arm angle, pendulum angle/rate, command, saturation, current and mode.

## Architecture

`encoder(s) -> calibrated state estimate -> capture/swing-up state machine -> local state feedback -> bounded current/voltage command -> motor/arm/pendulum`

Use energy shaping or a measured swing trajectory for swing-up. Use LQR/state feedback or a carefully separated cascaded controller near upright. Switch only inside a verified capture region with hysteresis.

## Critical Risks

- Reversed angle or torque sign.
- Insufficient motor authority at low battery voltage.
- Encoder backlash or flexible mounting.
- Controller tuned without measuring total latency.
- Integrator windup against arm travel or current limit.
- Automatic retry after a fall causing repeated impact.

## Test Sequence

1. Supported low-power sign and range tests.
2. Motor command/current characterization.
3. Manual motion state-estimator verification.
4. Local balance in a guarded stand with reduced limits.
5. Capture-region and disturbance tests.
6. Swing-up with explicit travel/energy bounds.
7. Full official initial-state repetitions and safe fall handling.
