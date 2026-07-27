# Roadmap

This project is maintained as an evidence-backed engineering system, not a one-time prompt collection. Priorities are ordered by their effect on contest reliability, safety, reproducibility, and verified score.

## Current Baseline

The `v0.2.0` baseline includes:

- A concise core Skill with domain routing and a required output contract.
- 19 engineering references and 6 worked cross-domain examples.
- 206 derived historical-problem records with source links and provenance.
- Static validation, metadata generation, and score-first brief tooling.
- Power-topology selection, AI code provenance prefixes, proportionate code-generation rules, and versioned backup/change-log gates.

## Near-term Priorities

### Evidence Packs

- Add exact-document packs for representative STM32, MSPM0, C2000, NXP, GD32, Microchip, RP-series, ESP32, AMD, Intel, and Lattice devices.
- Add common analog, ADC/DAC, gate-driver, motor-driver, current-sense, IMU, encoder, camera, PHY, power and protection evidence patterns.
- Record datasheet/TRM/errata/board-schematic relationships and revision-sensitive traps without copying vendor documents.

### Historical Knowledge Map

- Verify year, event, code, title, source and category with primary or independently corroborated metadata.
- Separate national, regional and special-session events instead of merging by year alone.
- Link recurring physical chains, judging constraints, calibration methods, failure modes and reusable acceptance tests.

### Engineering Calculators and Templates

- Add dependency-free calculators or worksheets for ADC settling, sampling/aliasing, timing budgets, uncertainty, thermal/current stress, actuator authority and battery sag.
- Add machine-checkable evidence ledgers, score matrices, I/O maps and bring-up records.
- Keep every tool auditable, bounded and useful without network access during competition.

### Real Failure Corpus

- Collect anonymized failures with reproduction, first divergence, root cause, minimal fix and regression test.
- Prioritize failures that look correct in code but fail physically: wrong pin mux, common-mode violation, insufficient gate drive, stale timestamps, reversed signs, saturation, cache/DMA incoherence and unsafe recovery.
- Never publish private team code, secrets, personal data or unlicensed contest attachments.

## Release Quality Gates

A stable `v1.0` requires:

1. Every domain route has a measurable output contract and hardware stop conditions.
2. Representative MCU, DSP, FPGA, analog, power, communication, vision and robot tasks have evidence-backed examples.
3. Historical metadata has reproducible provenance and a documented correction process.
4. Scripts pass on a clean checkout with the declared Python version and no undeclared dependencies.
5. Internal links, Skill metadata, generated counts and source branches are automatically checked.
6. Public contributions can add knowledge without redistributing copyrighted source documents.

## Contribution Strategy

Use small pull requests centered on one evidence set, one problem family, one failure case or one tool. A contribution is complete only when another team can locate the source, understand the physical consequence, reproduce the reasoning and verify the result.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and the Issue templates for hardware evidence, knowledge gaps and metadata corrections.
