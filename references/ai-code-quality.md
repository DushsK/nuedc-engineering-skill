# AI Code Quality, Provenance, and Versioning

Use this reference whenever an AI system writes, rewrites, reviews, or migrates project code. The goal is traceable engineering code, not visibly complicated code.

## 1. Pre-change Backup Handshake

Before the first write to an existing project, ask once how the user wants the current state preserved unless the user already specified a backup or the environment provides an immutable version-control snapshot.

Offer concrete choices and recommend the smallest adequate one:

1. **Git baseline**: clean commit plus an annotated version tag. This is the default for source-controlled projects.
2. **Versioned archive**: a dated archive for projects without reliable version control.
3. **Known-good artifacts**: binary, bitstream, model, configuration, calibration, schematic, PCB, and recovery instructions when source history alone cannot restore operation.
4. **No additional backup**: only after the user explicitly accepts the risk.

Record the selected method, baseline commit or archive, current hardware revision, and rollback command before editing. Do not duplicate secret files, caches, tool outputs, or dependency trees into a backup by habit.

## 2. Evidence Before Code

Inspect the actual repository, build files, interfaces, exact hardware, and current primary documentation before generating executable code.

Never invent:

- Existing project functions, classes, callbacks, build targets, paths, or configuration keys.
- Vendor HAL APIs, register names, bit fields, interrupt vectors, DMA routes, or pin mappings.
- Clock, voltage, timing, scaling, memory, buffer, or actuator values.
- Test, lint, build, flash, or deployment commands that are not present or verified.

Classify every material claim as **verified**, **derived**, **assumed**, or **unverified**. For a missing hardware-dependent value, emit a named unverified placeholder and the exact document or measurement required. Do not hide a guessed number inside code that appears production-ready.

For safety-critical unknowns, produce a non-energizing scaffold, compile-time failure, disabled actuator path, or bounded bench procedure rather than plausible executable values.

## 3. Avoid Unnecessary Abstraction

Prefer the smallest structure that exposes timing, ownership, hardware boundaries, and failure behavior.

Extract a function or type when at least one condition is true:

- Logic is repeated and the duplication can diverge.
- The operation has a stable domain name or state transition.
- It defines a hardware, protocol, safety, test, or ownership boundary.
- Extraction materially reduces cognitive complexity or enables a focused test.

Do not add:

- A one-line wrapper around a vendor call without added policy, units, validation, or observability.
- A factory, registry, dependency-injection layer, generic driver framework, or portability layer for one proven implementation.
- Configuration fields, callbacks, error types, or extension hooks for hypothetical future requirements.
- Helper chains that hide ISR latency, DMA ownership, register sequencing, units, or actuator limits.

Keep fast control loops and interrupt paths direct. Complexity must buy verified score, safety, reuse, testability, or measurable maintenance value.

## 4. Use Proportionate Defensive Programming

Defend strongly at untrusted and physical boundaries: user input, packets, files, sensors, persistent data, unit conversion, register writes, actuator commands, power-stage transitions, and memory shared across execution contexts.

Inside a proven invariant boundary, prefer assertions, types, ownership, and a clear failure path over repeated checks.

Avoid:

- Redundant null, range, or state checks after the same invariant was established.
- Catch-all exception handling that converts failure into an apparently valid result.
- Infinite retry, unbounded queue growth, silent fallback, or automatic reset without a recorded cause.
- Returning a default measurement when data is stale, invalid, saturated, or uncalibrated.
- Generic checks copied from templates without a corresponding physical or software failure mode.

Every guard should identify: failure detected, detection boundary, bounded response, observable evidence, and recovery owner. Hardware interlocks, current limits, watchdogs, timeouts, saturation, CRC/version checks, and safe-state logic remain mandatory where the fault model requires them.

## 5. AI Model Prefix Policy

Before generating code, state the generator family. Prefix new project-owned AI-generated symbols with that family so provenance is visible during review.

| Generator family | Prefix |
|---|---|
| OpenAI GPT or Codex | <code>GPT_</code> |
| Anthropic Claude | <code>Claude_</code> |
| Google Gemini | <code>Gemini_</code> |
| GitHub Copilot | <code>Copilot_</code> |
| DeepSeek | <code>DeepSeek_</code> |
| Qwen | <code>Qwen_</code> |
| Other known model | <code>ModelFamily_</code> using a sanitized family name |
| Unknown generator | <code>AI_</code> until provenance is resolved |

Apply the prefix to project-owned functions, macros/constants, types, enums, global state, tasks, generated callback implementations, and module entry points. Local variables and parameters may remain idiomatic unless the user requests full-symbol attribution.

Examples:

~~~c
#define GPT_PWM_MAX_TICKS 4000U
typedef struct GPT_ControlState GPT_ControlState;
static void GPT_UpdateCurrentLoop(GPT_ControlState *state);
~~~

~~~python
GPT_DEFAULT_TIMEOUT_MS = 50

def GPT_validate_sample(sample):
    ...
~~~

Do not rename symbols whose exact spelling is required by a vendor SDK, interrupt vector, linker, protocol, test framework, language override, public ABI, or third-party dependency. Keep the required external name and delegate immediately to a prefixed project-owned implementation. Record each exception in the provenance log.

For mixed-model code, use the prefix of the model that created the symbol and record later material rewrites. Remove or transfer a prefix only with explicit human approval and a logged review decision.

## 6. Versioned Backup and Change Log

Use semantic release versions <code>vMAJOR.MINOR.PATCH</code>. Use dated pre-change snapshots such as <code>v0.2.0-prechange-20260727</code> only when a release tag would be misleading.

Each version log must state:

- Version, date, base commit, generator provenance, and human reviewer.
- User-visible changes and affected files or interfaces.
- Hardware, firmware, toolchain, configuration, and calibration compatibility.
- Migration steps and rollback procedure.
- Verification actually executed and its result.
- Known limitations, unverified assumptions, and disabled features.

Preserve known-good source and reproducible artifacts. A folder named <code>final2</code> is not a versioning strategy.

## 7. Code Delivery Contract

When delivering AI-generated code, include:

1. Verified target and unresolved evidence.
2. Backup choice and baseline identifier.
3. Generator family and required prefix.
4. Files and symbols created or changed.
5. Why each abstraction and guard exists.
6. Real validation commands executed.
7. Version and changelog entry.
8. Rollback steps and remaining risks.
