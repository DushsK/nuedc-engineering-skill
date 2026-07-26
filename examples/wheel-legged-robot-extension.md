# Example Extension: Wheel-legged Balancing Robot

This is a forward-looking training scenario rather than a claim about a specific national NUEDC problem.

## Goal

Design a two-wheel, variable-leg-length robot that can stand, balance, drive, change height, tolerate a push, and enter a safe state after a fall.

## Minimum Verifiable Baseline

- Rigid chassis with measured center of mass and leg geometry.
- Wheel and joint encoders, IMU, motor current/voltage measurement, and physical enable.
- Current/torque protection and reduced-power test stand.
- Fixed-height balance before variable-height operation.
- Synchronized logs and deterministic state machine.

## State and Control Layers

Candidate state:

`[body pitch/rate, wheel position/velocity, left/right leg coordinates/rates, body height, contact state]`

Layers:

1. Driver hardware trip and current bounds.
2. Motor torque/current loops.
3. Wheel and joint servo loops.
4. Body pitch plus height/leg-force control.
5. Velocity/position command.
6. Contact-aware mode and trajectory planning.

Start with a measured linearized model and LQR/cascaded control at one leg geometry. Add gain scheduling or virtual model control only after verifying kinematics, torque mapping, singularities, contact and actuator limits.

## Evidence Required

- Motor/driver/battery peak and continuous current/thermal proof.
- Encoder and IMU axes/signs/timestamps.
- Leg Jacobian and force-to-joint-torque mapping.
- Loop rates and measured sample-to-actuation delay.
- Fall/catch thresholds, safe torque state and emergency stop.
- Regenerative bus behavior and low-battery authority.

## Development Sequence

1. Supported sensor/actuator sign tests.
2. Current and motor characterization.
3. Fixed-height estimator validation.
4. Fixed-height balance at reduced limits.
5. Push and battery-sag tests.
6. Slow height change with gain scheduling.
7. Contact/lift/fall detection.
8. Only then add aggressive motion, jumping, MPC or whole-body control.

`STOP` for unrestrained first motion, unknown torque sign, missing current limit, automatic maximum-torque recovery after a fall, or optimization output without a safe fallback.
