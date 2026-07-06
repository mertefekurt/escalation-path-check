# Escalation Path Check

<p align="center">
  <img src="assets/readme-cover.svg" alt="Escalation Path Check cover" width="100%" />
</p>

![stack](https://img.shields.io/badge/stack-Python-4b5563?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-2563eb?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-16a34a?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-dc2626?style=flat-square)

Check escalation matrices for owner, backup, and severity routing gaps.

## The short version

`escalation-path-check` is intentionally small: feed it a file, get deterministic findings, and decide whether the result should block a merge or just guide cleanup.

## Rule surface

| Rule | Severity | What it catches |
| --- | --- | --- |
| `unknown-owner` | high | owner is missing |
| `missing-backup` | medium | backup is missing |
| `missing-path` | low | escalation path missing |

## Usage

```bash
python -m pip install -e ".[dev]"
escalation-path-check examples/sample.txt
escalation-path-check examples/sample.txt --json --fail-on medium
```

## Useful defaults

| Option | Reason |
| --- | --- |
| `--json` | machine-readable output for scripts |
| `--fail-on medium` | stricter CI gate when warnings matter |
| `--format auto` | let the reader detect text, CSV, JSON, or JSONL |

## Local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m escalation_path_check --help
```
