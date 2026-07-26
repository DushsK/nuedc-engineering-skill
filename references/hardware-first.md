# Hardware-first System Review

## Contents

1. Six physical chains
2. Schematic gate
3. PCB and wiring gate
4. Mechanical and actuator gate
5. First-power-on sequence
6. Failure containment

## 1. Review Six Physical Chains

### Energy Chain

Map every source, converter, rail, load, return path, protection element, stored-energy element, and thermal path. Calculate normal, startup, stall, transient, and fault current.

### Signal Chain

Map the physical quantity through sensor, bias/protection, gain/filter, conversion, transport, processing, reconstruction, and output. Record range, bandwidth, noise, common mode, impedance, and saturation at every boundary.

### Timing Chain

Map acquisition, queueing, DMA, interrupt, computation, communication, actuation, and observation delays. Use worst-case values and include jitter.

### Control Chain

Map references, mode selection, controller, saturations, plant, sensors, estimator, fault monitors, and safe state. Make every hidden limiter explicit.

### Mechanical Chain

Map torque/force, transmission, stiffness, compliance, backlash, friction, travel stops, center of mass, contact, and structure. A software diagram is not a plant model.

### Failure Chain

For each credible fault, identify propagation, detection latency, containment, safe output, recovery condition, and retained evidence.

## 2. Schematic Gate

### Power and Protection

- Verify source polarity, connector rating, fuse/current limit, reverse protection, transient suppression, and discharge paths.
- Check regulator input/output capacitor type, value, ESR, placement, startup, dropout, stability, and thermal dissipation.
- Separate noisy actuator power from sensitive analog power while preserving a controlled return path.
- Add local decoupling at every IC supply pin according to the manufacturer layout guidance.
- Protect externally accessible analog and digital pins against expected ESD, overvoltage, reverse current, and connector mistakes.
- Provide a physical actuator disable that defaults safe during reset and programming.

### Digital Interfaces

- Verify voltage domains, pull-up rail, drive direction, open-drain versus push-pull, termination, connector order, and startup contention.
- Verify clock source, reset, boot straps, debug pins, programming connector, and recovery access.
- Ensure external signals cannot back-power an unpowered board without an intentional path.

### Analog Interfaces

- Verify source impedance, bias, input common mode, protection leakage, anti-aliasing, ADC acquisition settling, reference drive, and output compliance.
- Separate sensor ground, power return, switching-current return, and shield/chassis strategy by function, not by decorative ground labels.
- Add calibration injection points and test points before and after each major analog stage.

### Power Stages and Actuators

- Verify dead time, shoot-through prevention, freewheel path, current sensing, hardware overcurrent, thermal shutdown, stall behavior, and fault truth table.
- Bound PWM duty, command slew, speed, travel, and force at the closest safe layer to the hardware output.
- Make reset, watchdog, debugger halt, and cable disconnect states safe.

## 3. PCB and Wiring Gate

- Place switching loops, gate-drive loops, current shunts, decoupling, and high-frequency return paths before routing convenience signals.
- Keep clock, ADC reference, high-impedance analog nodes, and sensor lines away from high-dV/dt and high-dI/dt regions.
- Use controlled impedance and termination where edge rate or interface standard requires it.
- Verify copper width, via current, thermal vias, creepage, clearance, connector current, and mechanical strain relief.
- Add readable silkscreen for polarity, pin 1, rail names, connector functions, test points, and dangerous voltages.
- Review cable shield termination, chassis connection, and ground-loop risk.

## 4. Mechanical and Actuator Gate

- Measure mass, center of mass, inertia, travel, hard stops, backlash, friction, stiffness, and cable force.
- Verify torque/current at the worst position, not only at nominal posture.
- Ensure sensors are rigidly mounted and their axes are documented.
- Guard propellers, pinch points, hot surfaces, lasers, and high-energy moving parts.
- Use a tether, stand, reduced voltage/current, or unloaded fixture for first motion.
- Provide manual emergency stop and a test method that does not require entering the motion envelope.

## 5. First-power-on Sequence

1. Compare assembled board against schematic and BOM revision.
2. Inspect polarity, solder bridges, connector orientation, unpopulated options, and mechanical shorts.
3. Measure resistance from each rail to ground and between isolated domains.
4. Power one rail at a time with current limit below the expected fault-damage level.
5. Record startup current, steady current, rail voltage, ripple, and temperature.
6. Verify reset and clock before enabling peripherals.
7. Load firmware that keeps all actuators disabled and exposes a heartbeat.
8. Enable one interface or load at a time.
9. Increase voltage, current, duty, speed, or force in bounded steps.
10. Save measurements and the exact hardware/firmware revision.

## 6. Failure Containment

At minimum, define behavior for:

- Brownout, reset, watchdog, debugger halt, and corrupted configuration.
- Sensor invalid, stale, disconnected, saturated, or out of range.
- I2C/SPI/UART/CAN/Ethernet timeout, framing error, or stuck line.
- DMA overflow, missed deadline, numerical NaN/Inf, and controller saturation.
- Motor stall, encoder loss, overcurrent, overheating, and mechanical limit.
- Battery sag, reverse polarity, charger/source removal, and power-stage fault.

Prefer fault latching for conditions that can recur destructively. Require an explicit safe reset condition rather than automatic rapid retries.

## Review Output

Report findings as:

`Level | location | physical consequence | evidence | required change | verification`

Do not approve energizing while any `STOP` item remains.
