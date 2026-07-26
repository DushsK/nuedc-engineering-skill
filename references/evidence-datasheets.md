# Evidence and Datasheet Protocol

## Contents

1. Evidence hierarchy
2. Identity lock
3. Evidence ledger
4. Reading checklists
5. AI anti-hallucination rules
6. Documentation refresh

## 1. Evidence Hierarchy

Use sources in this order:

1. Current official competition rules, problem, clarification, and component list.
2. Manufacturer datasheet for the exact ordering code and package.
3. Reference manual or technical reference manual.
4. Manufacturer errata for the exact silicon revision.
5. Official board user guide and schematic for the exact board revision.
6. Official application note, design guide, SDK, example, or reference design.
7. Applicable standard or primary research paper.
8. Community material only as a lead to evidence above.

Do not use a blog, forum answer, generated summary, marketplace listing, or another board's pinout as final evidence.

## 2. Lock Exact Identity

Record:

- Manufacturer and complete part number.
- Package and temperature grade.
- Development board name and PCB revision.
- Silicon revision when errata matters.
- Document title, number, revision, publication date, and retrieval date.
- SDK/toolchain and example version.

Family-level names are insufficient. “STM32H7”, “C2000”, “Artix-7”, or “ESP32” can describe devices with materially different pins, memories, peripherals, voltages, and errata.

## 3. Maintain an Evidence Ledger

| Claim | Exact part/board | Source document | Revision | Section/table/page | Design consequence | Confidence |
|---|---|---|---|---|---|---|

Classify each claim:

- **Verified**: directly supported by current primary documentation.
- **Calculated**: derived from verified values; include equation and units.
- **Measured**: include setup, instrument, conditions, and repeatability.
- **Assumed**: explicitly state the assumption and the experiment required to remove it.

Do not upgrade an assumption to a fact because a common development board behaves that way.

## 4. Reading Checklists

### MCU, DSP, and SoC

Read at minimum:

- Recommended operating conditions and I/O voltage domains.
- Pin tables, alternate-function matrix, package-dependent limitations, and debug/bootstrap pins.
- Clock source limits, PLL constraints, bus clocks, timer clocks, and clock-failure behavior.
- Reset, brownout, watchdog, boot ROM, flash programming, and startup pin states.
- ADC input model, source impedance/settling, calibration, trigger routing, DMA, and errata.
- Timer synchronization, complementary outputs, dead time, break/trip input, encoder mode, and capture limits.
- DMA request map, buffer alignment, cache coherency, arbitration, and overflow behavior.
- Interrupt priority implementation and latency-relevant architecture details.
- Memory map, stack/heap limits, flash endurance, and nonvolatile-write restrictions.
- Thermal limits and package current limits.

### FPGA and CPLD

- Device/package pinout, I/O banks, VCCO/VREF, supported I/O standards, and configuration pins.
- Clock-capable pins, PLL/MMCM resources, jitter limits, and reset/configuration sequence.
- Timing constraints, speed grade, transceiver/reference-clock requirements, and configuration memory.
- CDC guidance, metastability assumptions, memory/DSP resources, and tool-version device support.
- Board schematic and all level shifters, termination, oscillators, and bank supplies.

### Op-amp, ADC, DAC, and Analog Front End

- Supply range, input common-mode range, output swing versus load, input protection, and phase-reversal behavior.
- Gain-bandwidth, slew rate, noise density, bias current, offset, drift, distortion, and stability conditions.
- ADC reference, acquisition time, input capacitance, driver requirements, anti-aliasing, clock jitter, and digital timing.
- DAC settling, glitch energy, output compliance, reconstruction filtering, and load drive.
- Layout, grounding, decoupling, and exposed-pad requirements.

### Power IC, MOSFET, Gate Driver, and Motor Driver

- Recommended operating area, transient ratings, thermal impedance, switching losses, and safe operating area.
- Gate voltage/current, UVLO, bootstrap limits, dead-time behavior, shoot-through protection, and fault truth table.
- Current limit tolerance, current-sense common mode, blanking/filtering, and fault latch/retry behavior.
- Inductor/transformer saturation, capacitor ripple current, loop compensation, startup and pre-bias behavior.
- Layout-critical current loops and measurement ground strategy.

### Sensor and Module

- Electrical interface levels, current, startup time, reset sequence, address/ID, and communication timing.
- Measurement range, noise, bandwidth, cross-axis sensitivity, drift, calibration, and temperature behavior.
- Mounting orientation, mechanical stress, field-of-view, optical/acoustic path, and environmental limits.
- Data-ready semantics, FIFO behavior, timestamp availability, and invalid-data indicators.

## 5. AI Anti-hallucination Rules

Never infer:

- Pin compatibility from similar names.
- Board oscillator frequency from a typical reference design.
- Five-volt tolerance from a GPIO family.
- ADC accuracy from nominal bit depth.
- Timer frequency without the complete clock tree.
- DMA or trigger connectivity from peripheral presence.
- Motor-driver current capability from the marketing headline alone.
- FPGA pin voltage from the device family alone.
- Mechanical torque margin from no-load motor speed.

When evidence is unavailable, state: `unverified — requires <document or measurement>`. Provide a safe test or alternative architecture instead of fabricating a value.

## 6. Refresh Current Documentation

Before publishing a part-specific recommendation:

1. Visit the official product page.
2. Check datasheet, TRM/reference manual, errata, board files, and SDK release notes.
3. Compare document revisions with any cached copy.
4. Record the retrieval date and changed assumptions.
5. Prefer stable document identifiers over search-result summaries.

Use [source-catalog.md](source-catalog.md) as a starting map, not as a substitute for checking the current product page.
