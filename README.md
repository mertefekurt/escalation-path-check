# Escalation Path Check

![Escalation Path Check cover](assets/readme-cover.svg)

Check escalation matrices for owner, backup, and severity routing gaps.

## The rule file is the product

- `unknown-owner` (high): owner is missing. Fix: assign primary owner.
- `missing-backup` (medium): backup is missing. Fix: assign backup path.
- `missing-path` (low): escalation path missing. Fix: document page or contact route.

Everything else in the repo exists to feed records into those checks and render the answer in a way a person can act on.

## Shell session

```bash
git clone https://github.com/mertefekurt/escalation-path-check.git
cd escalation-path-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
escalation-path-check examples/sample.txt
escalation-path-check examples/sample.txt --json
```

## Repository shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
