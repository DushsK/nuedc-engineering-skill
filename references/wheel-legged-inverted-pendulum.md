# Wheel-legged Robots and Inverted Pendulum Systems

## Scope

Use this reference for rotary/cart inverted pendulums, two-wheel self-balancing vehicles, reaction-wheel pendulums, wheel-legged robots, variable-height balancing platforms, and related underactuated systems.

These systems are hardware-limited dynamic plants. Mechanical geometry, actuator current, state latency, ground contact, and saturation matter as much as the control law.

## 1. Establish Coordinates and Signs

Draw the mechanism and define:

- Positive wheel/arm rotation.
- Body or pendulum angle and zero reference.
- Motor torque/current sign.
- Encoder count direction and wrap convention.
- IMU axes and body/world frames.
- Leg joint angles, leg length, contact point, and center-of-mass coordinates.

Verify each sign by manually moving one coordinate and observing raw sensor change before closing a loop. One reversed sign can produce immediate full-power divergence.

## 2. Measure the Plant

Record or identify:

- Body/pendulum mass, center of mass, and inertia.
- Wheel radius, track width, arm length, leg geometry, and joint limits.
- Motor torque constant, back-EMF constant, resistance, gear ratio, efficiency, no-load/stall data, and driver current limit.
- Encoder resolution after gearing.
- Friction, backlash, compliance, cable force, tire deformation, and ground slope.
- IMU bias/noise/latency and structural vibration.
- Battery voltage under acceleration and regenerative conditions.

Use low-energy identification tests. Do not infer torque from no-load speed or use stall current as a continuous operating point.

## 3. Prove Controllability and Authority

For a linear operating point, define a state such as:

`x = [position, velocity, body_angle, body_rate, ...]`

and a model:

`x_dot = A x + B u`

Check that the selected sensors make the required states observable and that the actuator can generate restoring acceleration with margin at the expected battery voltage.

For wheel-legged systems extend the state with leg length/angle, joint rates, wheel states, contact state, and body height as required. The model must change when contact, leg geometry, or support configuration changes materially.

## 4. Pendulum Swing-up and Balance

Separate swing-up from balance.

### Swing-up

Use an energy or trajectory objective rather than high-gain position control. Define desired upright energy, measured energy, command direction, travel bounds, and switch condition. Respect motor current, arm travel, joint limits, and repeated impact.

### Capture and Balance

Switch to a local stabilizer only inside a verified capture region for angle, angular rate, actuator position, and state confidence. Use hysteresis and dwell time to avoid mode chatter.

### Local Stabilizer

- LQR/state feedback is appropriate when the linearized model and states are credible.
- Cascaded PID can work for simpler two-wheel systems when inner rate/attitude and outer position loops are clearly separated.
- Add integral action only where steady bias requires it and saturation handling is implemented.

For LQR, document state scaling and the cost:

`J = integral(x^T Q x + u^T R u) dt`

Do not present `Q` and `R` as magic tuning matrices. Explain which physical deviations and actuator effort they penalize.

## 5. Wheel-legged Control Hierarchy

A practical hierarchy may contain:

1. Hardware current/torque protection.
2. Motor current or torque loop.
3. Wheel speed and joint servo loops.
4. Body pitch and height/leg-force controller.
5. Position/velocity controller.
6. Contact-aware state machine and trajectory planner.

Possible methods include LQR, virtual model control (VMC), whole-body control, gain scheduling, and MPC. Choose the simplest method that handles the required coupling and constraints.

### Virtual Model Control

Map desired virtual body forces/torques into joint/wheel torques through verified kinematics/Jacobians. Check singularities, force limits, contact assumptions, and torque allocation.

### Whole-body or Optimization Control

Use only when multiple contacts, joint limits, force distribution, or coupled objectives justify it. Bound solver time and provide a safe command when optimization fails or misses its deadline.

### Variable Leg Geometry

Recompute or schedule dynamics across leg length/angle. A controller tuned for one height can lose margin at another height because center of mass, inertia, leverage, and contact force change.

## 6. Estimation

Fuse encoders and IMU with common timestamps. Estimate at least body angle/rate, wheel position/velocity, and any leg/joint state required by the controller.

Account for:

- Accelerometer corruption during translation, impacts, and vibration.
- Gyro bias and temperature drift.
- Encoder quantization at low speed and slip at high acceleration.
- Flexible structure causing the IMU frame to differ from the modeled rigid body.
- Contact loss or wheel lift invalidating ground-relative assumptions.

Use contact detection from current/torque, acceleration, joint geometry, or dedicated sensors when the control law depends on contact.

## 7. Timing and Compute

Derive rates from the fastest unstable mode, motor/current dynamics, sensor bandwidth, and total delay. Example rate bands from another robot are not specifications.

Budget:

- Sensor acquisition and timestamp.
- Filter/estimator latency.
- Controller execution.
- Communication to motor drivers.
- PWM/current-loop update.
- Jitter and missed-deadline behavior.

Keep logging and vision outside hard real-time loops unless their worst-case cost is bounded.

## 8. Mechanical and Electrical Requirements

- Use rigid encoder and IMU mounts with known axes.
- Minimize backlash, compliance, eccentric wheels, and loose leg joints.
- Provide mechanical stops that do not create destructive impacts.
- Size drivers and battery for peak torque without brownout.
- Handle regenerative current and bus overvoltage.
- Add current sensing, physical enable, emergency stop, and a tether/test stand.
- Route high-current motor wiring away from encoders, IMU, and communication lines.

## 9. Fall, Recovery, and Fault Policy

Define thresholds using angle, angular rate, position/travel, contact, current, and state confidence.

When recovery is no longer physically plausible:

1. Stop balance integration and trajectory generation.
2. Command bounded zero or a verified safe posture.
3. Disable hazardous torque through the closest safe layer.
4. Latch the fault if repeated automatic retries can damage the mechanism.
5. Preserve pre-fault logs.

Do not keep applying maximum torque to a fallen or jammed robot.

## 10. Development Sequence

1. Validate each sensor and actuator sign with the robot supported.
2. Characterize motor command, current, speed, friction, and dead zone.
3. Validate current/torque protection.
4. Run a simulation or numerical model with measured parameters.
5. Test the estimator using manually moved hardware.
6. Close balance at reduced voltage/current in a tether or stand.
7. Add position, leg, height, or swing-up functions one at a time.
8. Test battery sag, pushes, slope, contact change, sensor dropout, and deadline miss.
9. Repeat unattended start and safe shutdown from every allowed initial condition.

## 11. Required Logs

Log synchronized reference, estimated state, raw sensors, actuator command, current/voltage, saturation, contact state, controller mode, deadline status, and fault code. Keep enough pre-trigger history to explain a fall.

Report `STOP` for unrestrained first tests, missing emergency disable, unbounded torque, unknown sign, insufficient actuator proof, or a controller that assumes contact/state validity without detection.
