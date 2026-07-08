"""Rich-backed console progress helpers."""

from __future__ import annotations

import os
import logging
from contextlib import contextmanager
from dataclasses import dataclass, field
from importlib import metadata
from pathlib import Path
from typing import Iterable, Iterator

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskID,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.table import Table
from rich.text import Text

from co_op_translator.utils.common.events import (
    emit_translation_event,
    stage_key_for_label,
)


def _env_flag(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "on"}


def _package_version() -> str:
    for package_name in ("co-op-translator", "co_op_translator"):
        try:
            return metadata.version(package_name)
        except metadata.PackageNotFoundError:
            continue
    return "dev"


def _short_path(value: str | Path | None) -> str:
    if value is None:
        return "-"
    try:
        path = Path(value)
    except TypeError:
        return str(value)
    return str(path)


def _language_values(languages: str | Iterable[str] | None) -> list[str] | None:
    if languages is None:
        return None
    if isinstance(languages, str):
        return [code for code in languages.split() if code]
    return [str(code) for code in languages]


def _path_from_detail(detail: str | None) -> str | None:
    if not detail:
        return None
    prefix = "Current: "
    if detail.startswith(prefix):
        return detail[len(prefix) :].strip() or None
    return None


def _mirror_to_file_logs(message: str) -> None:
    """Mirror user-facing console output to file logs without duplicating stderr."""
    if not message:
        return

    root_logger = logging.getLogger()
    record = root_logger.makeRecord(
        "co_op_translator.console",
        logging.INFO,
        __file__,
        0,
        "%s",
        (message,),
        None,
    )
    for handler in root_logger.handlers:
        if isinstance(handler, logging.FileHandler):
            handler.handle(record)


@dataclass
class ProgressReporter:
    """Small facade that keeps terminal output consistent across commands."""

    console: Console = field(default_factory=Console)
    output_style: str = "auto"
    no_progress: bool = False

    def __post_init__(self) -> None:
        env_style = os.getenv("CO_OP_TRANSLATOR_OUTPUT_STYLE")
        if env_style:
            self.output_style = env_style.strip().lower()
        self.no_progress = self.no_progress or _env_flag("CO_OP_TRANSLATOR_NO_PROGRESS")

    @property
    def rich_enabled(self) -> bool:
        if self.output_style == "plain":
            return False
        if self.output_style == "rich":
            return True
        if _env_flag("CI"):
            return False
        return bool(self.console.is_terminal)

    @property
    def progress_enabled(self) -> bool:
        return self.rich_enabled and not self.no_progress

    def print(
        self,
        message: str = "",
        *,
        style: str | None = None,
        markup: bool = True,
    ) -> None:
        plain_text = Text.from_markup(message).plain if markup else message
        if self.rich_enabled:
            self.console.print(message, style=style, markup=markup)
        else:
            self.console.print(plain_text, soft_wrap=True)
        _mirror_to_file_logs(plain_text)

    def info(self, message: str) -> None:
        self.print(message, style="cyan")

    def success(self, message: str) -> None:
        self.print(f"Done: {message}", style="green")

    def warning(self, message: str) -> None:
        self.print(f"Warning: {message}", style="yellow")

    def error(self, message: str) -> None:
        self.print(f"Error: {message}", style="red")

    def header(
        self,
        *,
        command: str,
        root_dir: str | Path | None = None,
        languages: str | Iterable[str] | None = None,
        modes: Iterable[str] | None = None,
    ) -> None:
        """Render a compact command header for interactive terminals."""
        table = Table.grid(padding=(0, 2))
        table.add_column(style="bold cyan", no_wrap=True)
        table.add_column(style="white")
        log_parts = [f"Command: {command}", f"Version: {_package_version()}"]
        table.add_row("Command", command)
        table.add_row("Version", _package_version())
        if modes:
            table.add_row("Mode", ", ".join(modes))
            log_parts.append(f"Mode: {', '.join(modes)}")
        if languages:
            if isinstance(languages, str):
                language_text = languages
            else:
                language_text = ", ".join(languages)
            table.add_row("Target", language_text)
            log_parts.append(f"Target: {language_text}")
        if root_dir is not None:
            table.add_row("Root", _short_path(root_dir))
            log_parts.append(f"Root: {_short_path(root_dir)}")

        plain_header = f"Co-op Translator | {' | '.join(log_parts)}"
        _mirror_to_file_logs(plain_header)
        emit_translation_event(
            "run_started",
            command=command,
            root_dir=_short_path(root_dir) if root_dir is not None else None,
            languages=_language_values(languages),
            modes=list(modes) if modes else None,
            metadata={"version": _package_version()},
        )
        if not self.rich_enabled:
            self.console.print(plain_header, soft_wrap=True)
            return

        title = Text("Co-op Translator", style="bold white")
        panel = Panel(
            table,
            title=title,
            border_style="cyan",
            box=box.ROUNDED,
            padding=(1, 2),
        )
        self.console.print(panel)

    def estimate_summary(
        self,
        *,
        title: str,
        total_tokens: int,
        total_words: int | None,
        rows: Iterable[tuple[str, int]],
        fallback: str,
    ) -> None:
        """Print token estimates as a Rich table or as a plain fallback line."""
        rows = list(rows)
        _mirror_to_file_logs(fallback)
        emit_translation_event(
            "estimate_ready",
            total_tokens=total_tokens,
            total_words=total_words,
            metadata={"title": title, "rows": rows},
        )
        if not self.rich_enabled:
            self.console.print(fallback, soft_wrap=True)
            return

        table = Table(
            title=title,
            box=box.SIMPLE_HEAVY,
            show_header=True,
            header_style="bold cyan",
        )
        table.add_column("Scope")
        table.add_column("Tokens", justify="right")
        for label, value in rows:
            table.add_row(label, f"{value:,}")
        table.add_section()
        table.add_row("Total", f"{total_tokens:,}", style="bold")
        if total_words is not None:
            table.caption = f"Estimated words: {total_words:,}"
        self.console.print(table)

    def key_value_summary(
        self,
        *,
        title: str,
        rows: Iterable[tuple[str, str]],
        fallback_lines: Iterable[str],
    ) -> None:
        """Print a compact key/value summary."""
        fallback_text = "\n".join(fallback_lines)
        _mirror_to_file_logs(fallback_text)
        if not self.rich_enabled:
            for line in fallback_text.splitlines():
                self.console.print(line, soft_wrap=True)
            return

        table = Table(title=title, box=box.SIMPLE_HEAVY, show_header=False)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", justify="right")
        for label, value in rows:
            table.add_row(label, value)
        self.console.print(table)

    @contextmanager
    def status(self, description: str) -> Iterator[None]:
        if self.progress_enabled:
            with self.console.status(description, spinner="dots"):
                yield
        else:
            yield

    @contextmanager
    def task(
        self,
        description: str,
        *,
        total: int | None = None,
        unit: str = "item",
        stage_key: str | None = None,
    ) -> Iterator["ProgressTask"]:
        """Create a polished progress task that degrades cleanly in CI."""
        resolved_stage_key = stage_key or stage_key_for_label(description)
        emit_translation_event(
            "stage_started",
            stage_key=resolved_stage_key,
            stage_label=description,
            total=total,
            metadata={"unit": unit},
        )
        if not self.progress_enabled:
            task = ProgressTask(
                None,
                None,
                description,
                total,
                unit,
                stage_key=resolved_stage_key,
            )
            try:
                yield task
            except Exception:
                raise
            else:
                emit_translation_event(
                    "stage_completed",
                    stage_key=resolved_stage_key,
                    stage_label=description,
                    completed=task.completed,
                    total=total,
                    metadata={"unit": unit},
                )
                if total is not None and task.completed:
                    self.success(task.summary)
            return

        progress = Progress(
            SpinnerColumn(style="cyan"),
            TextColumn("[bold cyan]{task.description}"),
            BarColumn(bar_width=None),
            MofNCompleteColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            TextColumn("[dim]{task.fields[detail]}"),
            console=self.console,
            transient=True,
            expand=True,
        )
        with progress:
            task_id = progress.add_task(
                description,
                total=total,
                unit=unit,
                detail="",
            )
            task = ProgressTask(
                progress,
                task_id,
                description,
                total,
                unit,
                stage_key=resolved_stage_key,
            )
            try:
                yield task
            except Exception:
                raise
            else:
                emit_translation_event(
                    "stage_completed",
                    stage_key=resolved_stage_key,
                    stage_label=description,
                    completed=task.completed,
                    total=total,
                    metadata={"unit": unit},
                )
        if task.completed:
            self.success(task.summary)

    def iter(
        self,
        iterable: Iterable,
        *,
        description: str,
        total: int | None = None,
        unit: str = "item",
        stage_key: str | None = None,
    ) -> Iterator:
        if total is None:
            try:
                total = len(iterable)  # type: ignore[arg-type]
            except TypeError:
                total = None

        with self.task(
            description, total=total, unit=unit, stage_key=stage_key
        ) as task:
            for item in iterable:
                yield item
                task.update(1)


@dataclass
class ProgressTask:
    """Adapter used by translation code without importing Rich directly."""

    progress: Progress | None
    task_id: TaskID | None
    description: str
    total: int | None
    unit: str
    stage_key: str
    completed: int = 0
    detail: str | None = ""
    language: str | None = None

    def update(self, advance: int = 1) -> None:
        self.completed += advance
        if self.progress is not None and self.task_id is not None:
            self.progress.update(self.task_id, advance=advance)
        emit_translation_event(
            "stage_progress",
            stage_key=self.stage_key,
            stage_label=self.description,
            language=self.language,
            current_path=_path_from_detail(self.detail),
            completed=self.completed,
            total=self.total,
            metadata={"unit": self.unit},
        )

    def set_detail(self, detail: str | None) -> None:
        self.detail = "" if detail is None or detail == "None" else detail
        if self.progress is not None and self.task_id is not None:
            self.progress.update(self.task_id, detail=self.detail)

    def set_description(self, description: str) -> None:
        self.description = description
        if self.progress is not None and self.task_id is not None:
            self.progress.update(self.task_id, description=description)

    set_description_str = set_description
    set_postfix_str = set_detail

    def file_started(
        self,
        current_path: str | Path,
        language: str | None = None,
    ) -> None:
        self.language = language
        self.set_detail(f"Current: {current_path}")
        emit_translation_event(
            "file_started",
            stage_key=self.stage_key,
            stage_label=self.description,
            language=language,
            current_path=str(current_path),
        )

    def file_completed(
        self,
        current_path: str | Path,
        language: str | None = None,
    ) -> None:
        emit_translation_event(
            "file_completed",
            stage_key=self.stage_key,
            stage_label=self.description,
            language=language,
            current_path=str(current_path),
        )

    def file_failed(
        self,
        current_path: str | Path,
        language: str | None = None,
        message: str | None = None,
    ) -> None:
        emit_translation_event(
            "file_failed",
            stage_key=self.stage_key,
            stage_label=self.description,
            language=language,
            current_path=str(current_path),
            message=message,
            level="error",
        )

    @property
    def summary(self) -> str:
        if self.total is None:
            return f"{self.description} ({self.completed} {self.unit})"
        if self.detail:
            return (
                f"{self.description} ({self.completed}/{self.total} "
                f"{self.unit}; {self.detail})"
            )
        return f"{self.description} ({self.completed}/{self.total} {self.unit})"


_DEFAULT_REPORTER = ProgressReporter()


def get_progress_reporter() -> ProgressReporter:
    return _DEFAULT_REPORTER
