"""Stable process exit codes for automation-facing CLI commands."""

from __future__ import annotations

import click

EXIT_SUCCESS = 0
EXIT_VALIDATION = 1
EXIT_PARTIAL_FAILURE = 2
EXIT_CONFIGURATION = 3
EXIT_FATAL = 4


class CliExitError(click.ClickException):
    """A Click error with a documented automation-facing exit code."""

    def __init__(self, message: str, exit_code: int) -> None:
        super().__init__(message)
        self.exit_code = exit_code


class PartialTranslationError(RuntimeError):
    """Raised after a run completes with one or more failed translation units."""

    def __init__(
        self,
        translated: int,
        errors: list[object],
        *,
        failed: int | None = None,
    ) -> None:
        self.translated = translated
        self.errors = list(errors)
        self.failed = len(self.errors) if failed is None else failed
        preview = "; ".join(str(error) for error in self.errors[:3])
        if self.failed > 3:
            preview += f"; and {self.failed - 3} more"
        super().__init__(f"Translation failed for {self.failed} file(s): {preview}")
