"""check_system - Tool for checking that a system is ok"""

__version__ = "0.0.1b1"

from check_system.cli import cli_wrapper, main
from check_system.markers import MARKERS

__all__ = ["main", "cli_wrapper", "MARKERS"]
