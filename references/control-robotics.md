# Control and Robotics

## 1. Define the Plant Before the Controller

Record:

- Controlled outputs and allowed error, overshoot, settling time, path deviation, or recovery time.
- Actuators, transmission, force/torque constants, current limits, speed limits, travel, backlash, friction, and saturation.
- Sensors, range, mounting, resolution, bandwidth, delay, bias, drift, and failure indicators.
- Mass, inertia, center of mass, geometry, contact, aerodynamic or fluid effects, and cable forces.
- Disturbances and judging initial conditions.

Use measured plant identification when model parameters are uncertain. A copied PID gain is not a model.

## 2. Size Hardware for Control Authority

Calculate the worst required force/torque and speed at the most difficult pose or operating point. Include acceleration, gravity, friction, transmission efficiency, and disturbance margin.

Verify:

- Motor and driver peak/continuous current under thermal limits.
- Gear ratio versus speed, torque, reflected inertia, backlash, and controllability.
- Encoder resolution at the controlled coordinate.
- Sensor range under transient motion.
- Supply sag and regenerative energy.
- Mechanical hard stops and safe failure posture.

If the actuator spends normal operation near saturation, the controller has little disturbance authority and anti-windup cannot fix undersized hardware.

## 3. Establish the Timing Architecture

Define each rate and deadline from physics:

| Task | Trigger | Rate/deadline | Worst execution | Input age | Output |
|---|---|---:|---:|---:|---|
| Current/torque loop | PWM/ADC | | | | |
| Attitude/state loop | timer/data-ready | | | | |
| Position/path loop | timer | | | | |
| Vision/planning | frame/event | | | | |
| Telemetry/UI | low priority | | | | |

Timestamp measurements at acquisition. Do not fuse values merely because they are read in the same main-loop iteration.

## 4. Build State Estimation Explicitly

Separate raw sensors, calibration, filtering, coordinate transforms, state estimation, validity, and controller inputs.

Check:

- Axis conventions, signs, units, zero definitions, and frame transforms.
- Encoder wrap, index/home, direction, missed counts, and slip.
- IMU bias, scale, alignment, vibration, acceleration contamination, and timestamp.
- Range/vision outliers, lost targets, confidence, and stale frames.
- Observability of the required states.

Use complementary filtering, observers, EKF/UKF, or optimization only when the measurement model and noise assumptions are stated. Always define fallback for invalid state estimates.

## 5. Use a Layered Controller

Typical order:

1. Hardware current/voltage/force limit.
2. Current or torque loop.
3. Speed/attitude/height loop.
4. Position/path/trajectory loop.
5. Planner and mission state machine.

Keep saturations and rate limits visible between layers. Implement anti-windup where an integrator sees a saturated downstream command. Use bumpless transfer between modes.

Choose:

- PID/lead-lag for single-input loops with measurable bandwidth and sufficient decoupling.
- Feedforward plus feedback when the reference dynamics are known.
- State feedback/LQR for coupled linearized dynamics with observable states.
- Gain scheduling for verified operating regions with smooth transitions.
- MPC only when constraints and coupling justify the computation and a simpler controller cannot meet the score.

## 6. Platform Patterns

### Wheeled Vehicles

Calibrate left/right wheel radius, track width, encoder scale, motor feedforward, dead zone, and friction. Handle slip and path-sensor loss. Separate velocity control from path/pose control.

### Ball-and-plate, Ball-and-beam, and Rolling Systems

Measure plate/beam angle and ball position latency. Start with one axis, identify coupling, then integrate. Bound tilt and acceleration to prevent loss of contact or sensor field of view.

### Magnetic Levitation

Treat current, force-distance nonlinearity, sensor range, magnetic hysteresis, and actuator heating as first-class constraints. Provide hardware current limit and catch/support structure. Close the fast inner current loop before position control.

### UAV and Air-ground Systems

Verify thrust margin, propeller direction, motor/ESC protocol, frame vibration, IMU placement, center of mass, battery sag, arming logic, geofence/test cage, and loss-of-link behavior. Validate attitude control while restrained or in a safe rig before free flight.

### Tracking, Aiming, and Gimbals

Calibrate camera/sensor to actuator coordinates, backlash, travel, latency, and target confidence. Separate detection, prediction, pointing control, and firing/output permission. Missing target must inhibit hazardous output.

## 7. State Machine and Safety

Use explicit states such as:

`BOOT -> SELF_TEST -> CALIBRATE -> READY -> RUN -> DEGRADED -> FAULT -> SAFE`

Define entry action, exit condition, timeout, allowed commands, actuator limits, and logging for every state. Require a deliberate reset after destructive or repeated faults.

Critical protections include emergency stop, fall/tilt detection, travel limits, stall/overcurrent, sensor invalid, communication timeout, deadline miss, battery/rail limits, and watchdog reset cause.

## 8. Tuning and Validation

1. Verify signs and units with low-power manual commands.
2. Identify actuator dead zone, feedforward, and plant response.
3. Close the innermost loop with conservative limits.
4. Measure bandwidth, delay, noise, saturation, and disturbance response.
5. Add outer loops one at a time.
6. Test mode transitions and fault recovery.
7. Repeat from all official initial conditions.

Retain time-aligned logs of references, states, estimates, commands, saturations, fault flags, and supply/current. A video alone is insufficient to diagnose control failure.
