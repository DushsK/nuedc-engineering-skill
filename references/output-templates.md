# Output Templates

## Full Problem Analysis

```markdown
## Known Facts and Missing Evidence
- Verified facts:
- Missing documents/measurements:
- Assumptions and how to remove them:

## Score Contract
| ID | Points | Requirement | Metric | Test | Dependency | Status |

## Baseline and Extensions
- Minimum verifiable baseline:
- Robustness work:
- Extension packages and abandonment criteria:

## Architecture Decision
| Option | Chain | Score fit | Margin | Risk | Evidence |

## Budgets
- Power/thermal:
- Analog/uncertainty:
- Timing/latency:
- CPU/memory/FPGA:
- Force/torque/mechanics:

## Hardware Gate
- STOP:
- FIX:
- IMPROVE:

## Implementation
- State machine:
- Module ownership:
- ISR/DMA/task schedule:
- Calibration/configuration:
- Fault/degraded behavior:

## Bring-up and Acceptance
1. ...
```

## Datasheet Evidence Ledger

```markdown
| Claim | Exact part/board | Document/revision | Section/page | Result | Design impact |
|---|---|---|---|---|---|
```

## Hardware Review Finding

```markdown
### [STOP/FIX/IMPROVE] Short title
- Location: schematic/PCB/connector/module/code boundary
- Physical consequence:
- Evidence:
- Required change:
- Verification:
- Remaining uncertainty:
```

## Firmware Plan

```markdown
## Target Evidence
- MCU/board/package:
- Clock sources:
- Manual/errata/SDK revisions:

## Ownership
| Peripheral/data | Owner | Trigger | Rate | Buffer | Timeout/fault |

## State Machine
| State | Entry | Allowed output | Exit | Timeout | Fault |

## Timing Budget
| Task/ISR | Period/deadline | Worst execution | Jitter | Proof |

## Hardware-facing Guards
- Startup safe state:
- Bounds/slew/dead time:
- Watchdog progress condition:
- Communication recovery:
- Configuration CRC/rollback:
```

## Control Review

```markdown
## Plant and Coordinates
- State, input, output, units, signs:
- Actuator limits and authority:
- Sensor range, delay, and validity:

## Controller
- Model/identification evidence:
- Loop hierarchy and rates:
- Saturation/anti-windup:
- Mode transitions and capture region:

## Safety
- Fall/stall/travel/current thresholds:
- Emergency disable:
- Safe recovery:

## Tests
- Open-loop identification:
- Step/disturbance response:
- Boundary and fault injection:
```

## Debug Report

```markdown
## Reproduction
- Revision/build/configuration:
- Initial state and steps:
- Expected/observed:

## First Divergence
- Signal/time:
- Evidence:

## Fault Tree
- Ruled out:
- Still possible:

## Root Cause or Proof Gap

## Minimal Fix

## Verification and Regression
```

## Final Release Gate

```markdown
- [ ] Complete judging sequence passed three times unattended
- [ ] Cold start, power cycle, reset and brownout passed
- [ ] Calibration/configuration restore passed
- [ ] Known-good binary/bitstream/model and rollback instructions saved
- [ ] Hardware, wiring, mechanical and report revisions match
- [ ] STOP/FIX findings closed or affected feature disabled
- [ ] Team can operate without development tools
```
