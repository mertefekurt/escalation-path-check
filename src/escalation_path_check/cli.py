from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from escalation_path_check import __version__
from escalation_path_check.core import (
    audit_records,
    read_records,
    render_json,
    render_markdown,
    should_fail,
)
from escalation_path_check.rules import PROJECT_NAME


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='escalation-path-check',
        description=(
                        'Check escalation matrices for owner, backup, and severity routing gaps.'
                    ),
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("input", nargs="?", type=Path, help='escalation matrix text')
    parser.add_argument(
        "--format",
        choices=("auto", "text", "jsonl", "csv", "json"),
        default="auto",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON instead of Markdown")
    parser.add_argument("--fail-on", choices=("low", "medium", "high"), default="high")
    parser.add_argument("--out", type=Path, help="write report to a file")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.input is None:
        parser.print_help()
        return 0
    try:
        records = read_records(args.input, args.format)
        report = audit_records(records)
        output = render_json(report) if args.json else render_markdown(report, PROJECT_NAME)
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(output, encoding="utf-8")
        else:
            print(output, end="")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"escalation-path-check: error: {exc}", file=sys.stderr)
        return 1
    return 2 if should_fail(report, args.fail_on) else 0
