# Changelog

All notable changes are recorded by release. Versions follow Semantic Versioning; each entry states behavior, compatibility, verification, and rollback impact where applicable.

## [Unreleased]

- Continue expanding verified platform evidence, historical labels, real failure cases, and worked examples.

## [0.2.1] - 2026-07-27

### Fixed

- Correct the titles of five TI power-topology source documents after direct verification against the official PDFs.

### Compatibility and Verification

- No code, CLI, data, or Skill behavior changed from `v0.2.0`.
- `python scripts/check_project.py` and the existing CLI smoke tests remain the release gate.

## [0.2.0] - 2026-07-27

### Added

- Add a multi-topology power-conversion map covering non-isolated, isolated, resonant, bidirectional, PFC, inverter, AC-AC, and wireless-transfer families.
- Add AI code anti-hallucination, proportionate defensive-programming, minimal-abstraction, model-prefix, backup, versioning, and delivery rules.
- Add `VERSION`, `AI_PROVENANCE.md`, and a repository Pull Request template.
- Add official topology-selection and converter-comparison entries to the primary-source catalog.

### Changed

- Prefix project-owned GPT-generated Python symbols with `GPT_` while preserving CLI behavior.
- Require release-version consistency across `VERSION`, `CITATION.cff`, README, and this changelog.
- Expand the problem brief and output templates with backup, AI provenance, abstraction rationale, validation, and rollback fields.

### Compatibility and Rollback

- Command-line entry points and arguments are unchanged.
- Python helper symbols are internal; direct imports of the old unprefixed names require migration to `GPT_` names.
- Roll back to `v0.1.0` or commit `cde56ef` if the new policy is not desired.

### Verification

- Project structure, links, Python compilation, generated metadata, AI prefix rules, and version consistency are checked by `python scripts/check_project.py`.

## [0.1.0] - 2026-07-26

- Publish the initial hardware-grounded NUEDC workflow.
- Add references for power, analog, communications, control, robotics, vision, MCU, DSP, and FPGA work.
- Add 206 historical metadata records with separate 2022 events and explicit 2026 regional labeling.
- Add reproducible data provenance, project validation, score-first brief generation, and a public maintenance roadmap.
