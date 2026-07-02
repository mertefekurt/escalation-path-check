# escalation-path-check

> Check escalation matrices for owner, backup, and severity routing gaps.

## Review card Overview

Check escalation matrices for owner, backup, and severity routing gaps. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts escalation matrix text. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
escalation-path-check examples/sample.txt
escalation-path-check examples/sample.txt --json --fail-on medium
python -m escalation_path_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `unknown-owner` | high | owner is missing |
| `missing-backup` | medium | backup is missing |
| `missing-path` | low | escalation path missing |

## Validation Notes

```bash
ruff check .
pytest
python -m escalation_path_check --help
```

Example risky input:

```text
severity p0 owner unknown backup none path missing
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
