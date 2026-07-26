#!/usr/bin/env python3
"""Validate repository structure, skill metadata, links, scripts, and generated data."""

from __future__ import annotations

import csv
import py_compile
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md",
    "README.md",
    "ROADMAP.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "agents/openai.yaml",
    ".github/workflows/validate.yml",
    ".github/ISSUE_TEMPLATE/hardware-evidence.yml",
    "references/problem-analysis.md",
    "references/evidence-datasheets.md",
    "references/hardware-first.md",
    "references/power-electronics.md",
    "references/analog-instrumentation.md",
    "references/signals-communications.md",
    "references/control-robotics.md",
    "references/wheel-legged-inverted-pendulum.md",
    "references/vision-ai.md",
    "references/mcu-firmware.md",
    "references/dsp.md",
    "references/fpga.md",
    "references/platform-matrix.md",
    "references/debug-validation.md",
    "references/contest-execution.md",
    "references/historical-taxonomy.md",
    "references/output-templates.md",
    "references/source-catalog.md",
    "data/README.md",
    "data/provenance.yml",
    "data/historical-problems.csv",
    "data/historical-summary.md",
)


def local_links(path: Path, text: str) -> list[Path]:
    links: list[Path] = []
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        links.append((path.parent / target).resolve())
    return links


def check_frontmatter(skill_text: str, errors: list[str]) -> None:
    if not skill_text.startswith("---\n"):
        errors.append("SKILL.md must begin with YAML frontmatter")
        return
    parts = skill_text.split("---\n", 2)
    if len(parts) < 3:
        errors.append("SKILL.md frontmatter is not closed")
        return
    frontmatter = parts[1]
    keys = [line.split(":", 1)[0].strip() for line in frontmatter.splitlines() if re.match(r"^[a-z_]+:", line)]
    if keys != ["name", "description"]:
        errors.append(f"SKILL.md frontmatter keys must be name, description; found {keys}")
    if "name: nuedc-engineering-skill" not in frontmatter:
        errors.append("unexpected skill name")
    if len(skill_text.splitlines()) > 500:
        errors.append("SKILL.md exceeds 500 lines")


def check_csv(path: Path, errors: list[str]) -> None:
    if not path.exists():
        return
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required_headers = {"year", "event", "code", "title", "categories", "hardware_hints", "source", "source_path", "source_url"}
    if not rows:
        errors.append("historical-problems.csv is empty")
        return
    if not required_headers.issubset(rows[0]):
        errors.append("historical-problems.csv has missing headers")
    if len(rows) < 100:
        errors.append(f"historical-problems.csv has only {len(rows)} rows")
    if any(not row.get("categories") for row in rows):
        errors.append("historical-problems.csv contains unclassified rows")
    if any(not row.get("hardware_hints") for row in rows):
        errors.append("historical-problems.csv contains rows without hardware hints")

    allowed_events = {"national", "national-july", "national-october", "regional", "regional-jilin"}
    invalid_events = sorted({row.get("event", "") for row in rows} - allowed_events)
    if invalid_events:
        errors.append(f"historical-problems.csv contains invalid events: {invalid_events}")

    keys = [(row.get("year"), row.get("event"), row.get("code"), row.get("title")) for row in rows]
    if len(keys) != len(set(keys)):
        errors.append("historical-problems.csv contains duplicate year/event/code/title rows")
    if any("/blob/master/" in row.get("source_url", "") for row in rows):
        errors.append("historical-problems.csv contains stale GitHub master-branch links")
    if any(not row.get("source_url", "").startswith("https://") for row in rows):
        errors.append("historical-problems.csv contains a non-HTTPS source URL")

    summary_path = ROOT / "data/historical-summary.md"
    if summary_path.exists():
        match = re.search(r"Indexed problem records: \*\*(\d+)\*\*", summary_path.read_text(encoding="utf-8"))
        if not match or int(match.group(1)) != len(rows):
            errors.append("historical-summary.md record count does not match historical-problems.csv")

    provenance_path = ROOT / "data/provenance.yml"
    if provenance_path.exists():
        match = re.search(r"^records:\s*(\d+)\s*$", provenance_path.read_text(encoding="utf-8"), re.MULTILINE)
        if not match or int(match.group(1)) != len(rows):
            errors.append("data/provenance.yml record count does not match historical-problems.csv")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).exists():
            errors.append(f"missing required file: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.exists():
        skill_text = skill_path.read_text(encoding="utf-8")
        check_frontmatter(skill_text, errors)

    placeholder_pattern = re.compile(r"\[(?:TODO|PLACEHOLDER)[^\]]*\]|\bFIXME\b", re.IGNORECASE)
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix.lower() in {".pdf", ".doc", ".docx", ".zip"}:
            errors.append(f"copyright-sensitive binary should not be committed: {path.relative_to(ROOT)}")
        if path.suffix.lower() not in {".md", ".yaml", ".yml", ".py", ".cff"}:
            continue
        text = path.read_text(encoding="utf-8")
        if placeholder_pattern.search(text):
            errors.append(f"placeholder text remains in {path.relative_to(ROOT)}")
        if path.suffix.lower() == ".md":
            for linked in local_links(path, text):
                if ROOT not in linked.parents and linked != ROOT:
                    warnings.append(f"link leaves repository: {path.relative_to(ROOT)} -> {linked}")
                elif not linked.exists():
                    errors.append(f"broken local link: {path.relative_to(ROOT)} -> {linked.relative_to(ROOT)}")

    agent_yaml = ROOT / "agents/openai.yaml"
    if agent_yaml.exists():
        value = agent_yaml.read_text(encoding="utf-8")
        if "$nuedc-engineering-skill" not in value:
            errors.append("agents/openai.yaml default_prompt must mention $nuedc-engineering-skill")

    for script in (ROOT / "scripts").glob("*.py"):
        try:
            py_compile.compile(str(script), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"python compile failed for {script.name}: {exc.msg}")

    check_csv(ROOT / "data/historical-problems.csv", errors)

    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("project validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
