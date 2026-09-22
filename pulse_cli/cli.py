from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from pulse_cli import __version__
from pulse_cli.core import hash_file, summarize_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pulse-cli", description="Pulse CLI")
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    h = sub.add_parser("hash", help="SHA256 de um arquivo")
    h.add_argument("path")

    s = sub.add_parser("json", help="Resumo de um JSON")
    s.add_argument("path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.cmd == "hash":
        print(hash_file(Path(args.path)))
        return 0
    print(json.dumps(summarize_json(Path(args.path)), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
