#!/usr/bin/env python3
"""Create a score-first NUEDC analysis worksheet."""

from __future__ import annotations

import argparse
from pathlib import Path


GPT_TEMPLATE = """# {title}

## 1. Evidence Set

- Event/year: {year}
- Problem code: {code}
- Candidate platform: {platform}
- Original problem and clarification revision:
- Official component list:
- Exact board/part numbers:
- Available instruments and mechanical capability:
- Missing evidence that can change feasibility:

## 2. Score Contract

| ID | Requirement | Points | Metric/tolerance | Test condition | Allowed operation | Proof method | Risk | Status |
|---|---|---:|---|---|---|---|---|---|
| B1 | | | | | | | | |

## 3. Minimum Verifiable Baseline

- Baseline functions:
- Fastest proof path:
- Features deliberately deferred:

## 4. Architecture Comparison

| Option | Signal/power/control chain | Expected score | Main risk | Required evidence | Decision |
|---|---|---:|---|---|---|
| A | | | | | |
| B | | | | | |

## 5. Physical Chains

- Energy chain:
- Signal chain:
- Timing chain:
- Control chain:
- Mechanical chain:
- Failure chain:

## 6. Budgets

| Budget | Requirement | Estimate | Margin | Evidence/test |
|---|---:|---:|---:|---|
| Power | | | | |
| Bandwidth | | | | |
| Latency | | | | |
| Accuracy/uncertainty | | | | |
| CPU/RAM/FPGA | | | | |
| Torque/force/travel | | | | |

## 7. Hardware Gate

- [ ] Power tree, limits, protection, thermal path
- [ ] Logic levels, pin mux, clocks, reset and startup states
- [ ] Analog range, common mode, settling, anti-aliasing and references
- [ ] Driver flyback/dead time/current sensing/emergency disable
- [ ] Grounding, return paths, decoupling, connectors and test points
- [ ] Mechanical travel, interference, center of mass and guards

## 8. Firmware / DSP / FPGA Plan

- State machine:
- Timing and interrupt/DMA ownership:
- Data validity and calibration:
- Fault detection, degraded mode and watchdog policy:
- Logging and observable signals:

## 9. AI Code, Backup, and Version

- User-selected backup method:
- Baseline commit/tag/archive:
- Target version and changelog entry:
- Generator family and required prefix:
- AI-created files/symbols:
- External-name exceptions:
- Why each new abstraction exists:
- Failure mode behind each defensive check:
- Rollback procedure:

## 10. Bring-up Sequence

1. Unpowered inspection.
2. Current-limited rails.
3. Clock/reset/debugger.
4. One peripheral at a time.
5. Sensor and timing validation.
6. Reduced-limit actuator test.
7. Open-loop identification.
8. Closed-loop integration.

## 11. Acceptance and Fault Tests

| Test | Stimulus | Expected result | Instrument/log | Pass criteria | Result |
|---|---|---|---|---|---|
| Nominal | | | | | |
| Boundary | | | | | |
| Power cycle | | | | | |
| Sensor/communication loss | | | | | |

## 12. Findings

- `STOP`:
- `FIX`:
- `IMPROVE`:
"""


def GPT_main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True)
    parser.add_argument("--year", default="unknown")
    parser.add_argument("--code", default="unknown")
    parser.add_argument("--platform", default="undecided")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    content = GPT_TEMPLATE.format(title=args.title, year=args.year, code=args.code, platform=args.platform)
    if args.output:
        if args.output.exists():
            raise SystemExit(f"refusing to overwrite existing file: {args.output}")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
        print(args.output)
    else:
        print(content, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(GPT_main())
