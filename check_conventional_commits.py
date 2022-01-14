#!/usr/bin/env python
import argparse
import re
import sys
from pathlib import Path
from typing import List


DEFAULT_VALID_TYPES = [
    # Rule 1 and 2.
    "feat",
    "fix",
]


parser = argparse.ArgumentParser()
parser.add_argument(
    "--extra-types",
    type=str,
    default="",
    help="additional commit types as comma separated text",
)
parser.add_argument(
    "msg_file_path",
    nargs="?",
    type=Path,
    help="commit message file by commit-msg hooks",
)


def validate_commit_message(msg: str, valid_types: List[str]) -> bool:
    rule = re.compile(
        r"(?P<type>[a-z]+)(\((?P<scope>\w+)\))?!?: (?P<desc>[^\r\n].+)(\n\n(<?P<body>.+))?"
    )
    matched = rule.match(msg)
    if not matched:
        print("Invalid format for 'Conventional Commits'.")
        print("Please see https://www.conventionalcommits.org/en/v1.0.0/")
        return False
    if matched.group("type") not in valid_types:
        print(f"Invalid type section. select one from [{', '.join(valid_types)}]")
        return False
    return True


def input_message() -> str:
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return "\n".join(lines)


def main():
    args = parser.parse_args()
    msg = args.msg_file_path.read_text() if args.msg_file_path else input_message()
    valid_types = DEFAULT_VALID_TYPES + args.extra_types.split(",")
    result = validate_commit_message(msg, valid_types)

    return 0 if result else 1


if __name__ == "__main__":
    sys.exit(main())
