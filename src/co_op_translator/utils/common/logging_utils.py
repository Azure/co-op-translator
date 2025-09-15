"""
Reusable logging setup for CLI commands.
"""

from __future__ import annotations

import logging
from pathlib import Path
from datetime import datetime, timezone
import os
import sys


def _tz_offset_str() -> str:
    """Return local timezone offset as +HHMM or -HHMM."""
    # Using strftime('%z') on an aware datetime for simplicity
    return datetime.now().astimezone().strftime("%z")


def _build_log_filename(command_name: str, level: str) -> str:
    tz = _tz_offset_str()
    pid = os.getpid()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = f"co-op-translator_{ts}{tz}_pid{pid}_level{level.upper()}.log"
    # keep command out of base to follow the recommended default; could be added later if desired
    return base


def setup_logging(
    root_dir: Path, debug: bool, save_logs: bool, command_name: str
) -> Path | None:
    """
    Configure logging for console and optional file outputs.

    - Console: CRITICAL by default, DEBUG when debug=True
    - File: when save_logs=True, write DEBUG level to logs/<timestamped>.log and logs/latest.log

    Returns the path to the timestamped log file if created, else None.
    """
    # Ensure absolute path
    root_dir = root_dir.resolve()

    # Determine overall log level for the root logger
    root_level = logging.DEBUG if (debug or save_logs) else logging.CRITICAL

    logger = logging.getLogger()

    # Reset previous configuration to avoid duplicate handlers between commands
    for handler in list(logger.handlers):
        logger.removeHandler(handler)
    logging.captureWarnings(True)

    logger.setLevel(root_level)

    # Console handler
    console_handler = logging.StreamHandler(stream=sys.stderr)
    console_handler.setLevel(logging.DEBUG if debug else logging.CRITICAL)
    console_formatter = logging.Formatter(fmt="%(levelname)s:%(name)s:%(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    log_file_path: Path | None = None

    if save_logs:
        logs_dir = root_dir / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

        filename = _build_log_filename(command_name, level="DEBUG")
        log_file_path = logs_dir / filename

        # File handler for timestamped file
        file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)s %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Also maintain logs/latest.log for convenience (overwrite each run)
        latest_path = logs_dir / "latest.log"
        latest_handler = logging.FileHandler(latest_path, mode="w", encoding="utf-8")
        latest_handler.setLevel(logging.DEBUG)
        latest_handler.setFormatter(file_formatter)
        logger.addHandler(latest_handler)

        logger.debug("File logging enabled: %s", str(log_file_path))

    return log_file_path
