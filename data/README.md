# Historical Metadata

This directory contains derived metadata and statistics, not redistributed contest documents.

## Files

- `historical-problems.csv`: one normalized problem record per row.
- `historical-summary.md`: generated category, hardware-hint and year counts.
- `provenance.yml`: source repositories, exact revisions and generation metadata.

## Current Scope

The current index contains 206 records spanning 1994-2026. The 2022 July and October national events are represented separately. All currently indexed 2026 records are from the April Jilin regional event; they are not national-problem records.

## CSV Schema

| Column | Meaning |
|---|---|
| `year` | Event year parsed from the source path |
| `event` | `national`, `national-july`, `national-october`, `regional`, or `regional-jilin` |
| `code` | Normalized problem code such as `A` or `B` |
| `title` | Normalized title derived from source metadata |
| `categories` | Semicolon-separated rule-based domain labels |
| `hardware_hints` | Semicolon-separated likely physical-platform hints |
| `source` | Source repository identifier |
| `source_path` | Original source-relative path or filename |
| `source_url` | Link to the source repository path on its recorded branch |

Categories and hardware hints are navigation aids, not official classifications and not proof that a specific platform is required.

## Regeneration

From the repository root:

```powershell
python scripts/build_problem_index.py `
  --tree-file path\to\topic_tree.txt `
  --corpus-dir path\to\nuedc\docs\problems `
  --out-csv data\historical-problems.csv `
  --out-summary data\historical-summary.md
```

After regeneration, update `provenance.yml`, review event boundaries and aliases, inspect duplicates, then run `python scripts/check_project.py`.

## Known Limitations

- Public repositories can contain naming errors, regional material, repeated attachments or incomplete years.
- Rule-based title classification cannot replace reading the original statement and scoring table.
- A source link identifies provenance; it does not grant redistribution rights.
- Current metadata is a maintained snapshot, not an official complete catalog.

Report corrections with the Problem metadata correction Issue template and an authoritative source.
