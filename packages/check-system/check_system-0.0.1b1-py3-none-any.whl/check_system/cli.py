"""Main cli code."""

import argparse
import sys
from typing import Dict, List, Optional

import check_system


def parse_args(argv: Optional[List[str]] = None) -> Dict[str, str]:
    """Utility function for creating parser and parsing arguments."""
    parser = argparse.ArgumentParser()

    for marker, marker_data in check_system.MARKERS.items():
        parser.add_argument(
            f"--{marker.replace('_', '-')}",
            type=str,
            default=None,
            help=marker_data["help"],
        )

    args = parser.parse_args(argv)

    return vars(args)


def main(argv: Optional[List[str]] = None) -> None:
    """Main function of the cli"""
    args = parse_args(argv)

    for marker, value in args.items():
        if value:
            if check_system.MARKERS[marker]["value"] != value:
                raise SystemExit(
                    f"Check failed: {marker} was "
                    f"{check_system.MARKERS[marker]['value']}. Checked against: {value}"
                )


def cli_wrapper() -> None:
    """Wrapper function aroun main that reads arguments with sys.argv."""
    main(sys.argv[1:])
