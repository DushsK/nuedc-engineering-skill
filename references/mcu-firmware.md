# MCU and Firmware Engineering

## 1. Select by Verified Resources

Build a resource table before choosing a controller:

| Resource | Required | Device evidence | Margin | Risk |
|---|---:|---:|---:|---|
| CPU cycles and worst latency | | | | |
| RAM/stack/heap | | | | |
| Flash/nonvolatile writes | | | | |
| ADC channels/rate/trigger | | | | |
| DAC/comparator/op-amp | | | | |
| PWM/capture/encoder/dead time/break | | | | |
| DMA request routes | | | | |
| UART/SPI/I2C/CAN/USB/Ethernet | | | | |
| Voltage domains and package pins | | | | |

Peripheral names are not proof that the needed trigger, channel, pin, DMA request, or simultaneous mode exists.

## 2. Prove the Clock Tree

Document the complete chain:

`source -> oscillator/clock input -> PLL/dividers -> core/bus -> peripheral -> timer/ADC/communication clock`

For each clock state:

- Source tolerance and startup behavior.
- PLL input/output constraints.
- Flash wait states and voltage range.
- Bus prescalers and any timer clock multiplication behavior.
- Peripheral kernel clock selection.
- Clock failure, switching, and low-power behavior.
- Measured output using a clock-out pin, timer toggle, or instrument.

Never paste a timer prescaler without the verified upstream clock and counter mode.

## 3. Lock Pin and Board Reality

Verify exact package pinout, alternate functions, analog capability, five-volt tolerance, current limits, boot/debug pins, oscillator connections, level shifters, LEDs/buttons, solder bridges, and connector wiring from the datasheet plus board schematic.

Create a pin-ownership table:

`pin | startup state | owner | mode | voltage domain | external pull/load | conflict | test`

Do not repurpose programming/debug pins until recovery is proven. Do not assume a clone MCU is pin/peripheral compatible with an STM32 or another vendor family.

## 4. Use a Safe Startup Sequence

1. Hardware pulls establish safe actuator states before code runs.
2. Reset handler keeps output registers and enables safe.
3. Configure voltage/flash/clock with timeout and fallback.
4. Initialize GPIO output values before switching pin modes.
5. Initialize fault inputs and actuator disable before PWM.
6. Initialize timebase, logging, sensors, communication, and calibration.
7. Run self-test and validate required sensors/rails.
8. Enter `READY`; require an explicit condition before `RUN`.

Define brownout, watchdog reset, software reset, debugger attachment, bootloader failure, and corrupted configuration behavior.

## 5. Timing, Interrupts, and DMA

Use timer/data-ready events for periodic work. Keep hard deadlines out of an unbounded main loop or network task.

For every interrupt:

- Trigger source and rate.
- Priority and maximum execution time.
- Data ownership and synchronization.
- Allowed APIs and blocking prohibition.
- Overrun detection and degraded behavior.

For DMA:

- Request mapping and trigger.
- Buffer size, alignment, ownership, and double-buffer policy.
- Overrun/underrun behavior.
- Cache maintenance on cached cores.
- Memory region accessibility and bus contention.
- Timestamp relation to the physical sample.

Measure execution with a hardware timer, trace, or GPIO marker. Average timing is not a deadline proof.

## 6. Peripheral-specific Gates

### ADC

Verify reference, input range, acquisition time, source impedance, calibration, trigger, sequence, DMA, channel transition, internal sensor setup, and errata. Separate sample rate from effective accuracy.

### PWM and Motor Control

Verify counter mode, frequency/resolution, complementary outputs, dead time, synchronization, preload/update event, break/trip input, startup output state, and fault latch. Limit command in the driver boundary.

### Encoder and Capture

Verify electrical input mode, filtering, timer width, overflow extension, direction, index/home, speed estimation at low speed, and missed-edge detection.

### I2C/SPI/UART/CAN

Define voltage/pulls/termination, transaction timeout, retry count, bus recovery, stale-data policy, framing/CRC, queue limits, and reconnect behavior. Never block the control loop indefinitely.

### Flash and Configuration

Verify erase granularity, endurance, voltage/clock restrictions, execution stall, power-loss behavior, CRC/version, dual-copy or rollback strategy, and when writes are permitted.

## 7. State and Data Integrity

Use explicit state machines and validity flags. A numeric value without timestamp, range, calibration version, and validity is not a trustworthy measurement.

Protect shared data with ownership, short critical sections, atomics, or message passing appropriate to the architecture. `volatile` does not make compound operations atomic or solve cache coherency.

Check numerical boundaries before integer conversion or register writes. Define NaN/Inf, overflow, divide-by-zero, wraparound, and saturation behavior.

## 8. Family-specific Review Points

### STM32

Verify exact reference manual, datasheet, errata, Cube/HAL/LL version, board schematic, clock tree, timer clock behavior, ADC calibration/trigger, advanced-timer break/dead time, DMA request mapping, and cache/MPU behavior on applicable M7 devices.

### TI MSPM0

Verify exact device TRM/datasheet/errata, SysConfig-generated routing, clock system, timer/event fabric, ADC trigger and memory behavior, comparator/op-amp resources where present, DMA, low-power transitions, and LaunchPad schematic. Treat generated configuration as output to review, not primary evidence.

### TI C2000

Treat it as a real-time control platform: verify ePWM synchronization, ADC SOC/EOC timing, CMPSS, trip zones, CLA/DMA ownership, memory sections, control-loop latency, real-time debug behavior, and device errata. Read [dsp.md](dsp.md) and [power-electronics.md](power-electronics.md).

### NXP, GD32, and Other Cortex-M Families

Verify vendor-specific clocks, pin mux, DMA/event routing, timer/PWM, ADC, cache, flash, and errata. Do not port by register-name resemblance alone.

### RP2040/RP2350-class Boards

Verify exact chip and board. Account for external flash/boot design, PIO state machines, DMA pacing, dual-core ownership, clocking, ADC limits, and board voltage/regulator connections.

### ESP32-class SoCs

Separate hard real-time work from Wi-Fi/Bluetooth, RTOS scheduling, flash/cache stalls, and dynamic power behavior. Verify boot straps, ADC calibration/limitations, pin matrix, voltage, radio/antenna layout, PSRAM, and exact module variant.

### RISC-V and AI MCUs

Verify toolchain maturity, debug, peripheral documentation, memory map, accelerator operator support, camera/display interfaces, DMA/cache coherence, and reproducible deployment. Marketing TOPS does not prove end-to-end latency.

## 9. Firmware Output Contract

Before producing code, state:

- Exact target and documentation revision.
- Clock and timing derivation.
- Pin/peripheral ownership.
- State machine and safety outputs.
- ISR/DMA/task schedule.
- Buffer and memory budget.
- Calibration and configuration format.
- Fault and recovery behavior.
- Bench test that proves each hardware-facing module.

If any required part-specific value is unverified, emit a named placeholder and the exact document/measurement needed rather than a plausible number.
