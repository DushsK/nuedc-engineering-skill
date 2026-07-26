# Example: 2025 C - Monocular Target Measurement

Source metadata: [historical index](../data/historical-problems.csv).

## Score-first Interpretation

The basic path uses one camera and one-button operation to measure target distance and a geometric dimension for several target types. The system must also measure its supply current. Extensions add multiple/overlapping squares, numbered-target selection, oblique target planes, and power optimization under explicit restrictions on sensors, commercial ranging products, PCs, and current-measurement modules.

## Minimum Verifiable Baseline

- Fixed, rigid camera and known baseline/axis geometry.
- Calibrated intrinsics/distortion and a physically observable scale model.
- Deterministic shape segmentation for the controlled black-on-white targets.
- Rejection of frames with invalid border/pose/blur/exposure.
- Self-designed current-sense chain with independent calibration.

## Key Geometry Questions

- Which known plane, border, camera height/pose, or target feature makes distance observable from one camera?
- How does pixel uncertainty propagate into distance and dimension error?
- What changes when the target plane rotates by the allowed angle?
- How are overlapping or numbered squares selected without confusing detection confidence with geometry validity?

## Platform Decision

Classical OpenCV/geometry may be more reliable than a learned model for the controlled targets. Select MCU/OpenMV, AI MCU, FPGA, or SBC only after proving camera bandwidth, frame latency, power, boot time, library/tool support, and the no-PC restriction.

## Validation

- Independent calibration and check distances/sizes.
- Distance and dimension boundaries.
- Each target type, overlaps, numbering and oblique pose.
- Lighting, exposure, focus, target absence and invalid pose.
- Repeated cold start and one-button measurement time.
- Supply-current/power measurement against a reference instrument.

`STOP` if the design secretly depends on a forbidden ranging sensor/module or if invalid geometry can still produce an accepted result.
