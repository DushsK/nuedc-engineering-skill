# Vision and Edge AI

## 1. Decide Whether AI Is Necessary

Prefer deterministic geometry, thresholding, color/shape analysis, template matching, classical tracking, or signal processing when the target and environment are controlled. Use a learned model only when variation cannot be handled reliably by simpler methods and the dataset/compute path is available.

Complexity must buy score, robustness, or setup speed.

## 2. Freeze the Perception Contract

Record target classes/features, size/distance range, lighting, background, motion, occlusion, camera pose, required accuracy, update rate, latency, confidence behavior, and allowed calibration.

Separate:

- Detection accuracy from geometric measurement accuracy.
- Frame rate from end-to-end control latency.
- Model confidence from physical validity.
- Lab images from judging-domain images.

## 3. Camera and Geometry

Verify sensor, lens, focus, exposure, rolling/global shutter behavior, field of view, distortion, mounting rigidity, and interface bandwidth.

For monocular measurement:

- Define the geometric assumptions that make scale observable.
- Calibrate intrinsics and distortion.
- Calibrate camera-to-object/robot coordinates.
- Quantify depth, pose, plane, or known-size sensitivity.
- Reject frames that violate the geometric assumptions.

Do not convert pixels to millimeters with one constant across changing depth or perspective unless the geometry proves it.

## 4. Dataset and Model Discipline

When using AI:

- Split data by scene/session/device, not adjacent frames, to avoid leakage.
- Include expected lighting, blur, scale, angle, occlusion, clutter, and negative examples.
- Record labeling rules and ambiguous cases.
- Evaluate precision/recall and task-level error, not only training accuracy.
- Test quantized/deployed models on the target hardware.
- Measure cold-start time, memory, peak latency, thermal throttling, and frame drops.
- Version model, preprocessing, labels, calibration, and runtime together.

Never claim generalization beyond tested conditions.

## 5. Pipeline and Timing

Define:

`capture -> exposure completion -> transfer -> preprocessing -> inference/vision -> geometry/filter -> decision -> communication -> actuation`

Timestamp near capture. Bound queues and discard stale frames rather than controlling from old data. Separate the latest result from a valid result.

If a Linux/SBC or accelerator handles perception, keep emergency stop and fast actuator limits on a deterministic controller when possible.

## 6. Robustness and Fallback

Monitor exposure, blur, saturation, target confidence, geometric consistency, frame age, calibration validity, and communication health.

Define fallback behavior:

- Hold position or reduce speed.
- Use the last valid estimate for a bounded time.
- Switch to a simpler sensor or geometric mode.
- Return to a search/reacquire state.
- Inhibit aiming, firing, high-speed motion, or other hazardous actions.

Confidence alone is not a safety permission.

## 7. Hardware Selection

- MCU/OpenMV-class devices suit bounded classical vision and small models with modest resolution.
- RISC-V/AI accelerators and NPUs suit compact inference but require verified toolchain, operators, memory, camera interfaces, and deployment behavior.
- Raspberry Pi/Jetson-class systems suit OpenCV, larger models, networking, and UI but introduce OS scheduling, boot, storage, thermal, and power complexity.
- FPGA suits deterministic streaming, custom sensors, preprocessing, and low-latency pipelines when development skill and verification time exist.

Verify exact camera electrical interface, connector, clock, voltage, driver, and bandwidth.

## 8. Validation Matrix

Test combinations of minimum/maximum distance, angle, lighting, background, motion, partial occlusion, target absence, distractors, power cycle, camera reconnect, dropped frames, and thermal steady state.

Report task-level outputs: physical measurement error, pointing error, reacquisition time, false action rate, and end-to-end latency. Preserve representative raw frames and metadata for regression.

Report `STOP` when perception loss can trigger hazardous motion/output without an independent inhibit or when camera/compute electrical and timing compatibility is unverified.
