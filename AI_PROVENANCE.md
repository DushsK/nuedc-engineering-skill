# AI Code Provenance

This file records project-owned code that was generated or materially rewritten with AI assistance. A prefix is an attribution and review aid, not proof of correctness.

## Current Registry

| Path | Generator family | Required prefix | Exact model | Human owner/reviewer | Introduced |
|---|---|---|---|---|---|
| <code>scripts/*.py</code> | OpenAI GPT through Codex | <code>GPT_</code> | Not exposed to this repository | DushsK | v0.2.0 |

## External-name Exceptions

No current project script requires an unprefixed external callback or public ABI symbol. Standard Python runtime names such as <code>__name__</code> are language contracts and are not project-owned identifiers.

## Update Rules

1. Add a row when AI creates or materially rewrites project-owned code.
2. Record the generator family, required prefix, date/version, reviewer, and exact model when known.
3. Record symbols that cannot be prefixed because an SDK, toolchain, protocol, framework, override, or public API requires exact spelling.
4. Do not remove or transfer a prefix without explicit human approval and a changelog entry.

See [AI Code Quality, Provenance, and Versioning](references/ai-code-quality.md).
