from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path


class ReviewSeverity(str, Enum):
    ERROR = "error"
    WARNING = "warning"


@dataclass(frozen=True)
class ReviewIssue:
    check: str
    severity: ReviewSeverity
    message: str
    path: Path | None = None
    language: str | None = None

    def location(self) -> str:
        if self.path is None:
            return "-"
        return str(self.path).replace("\\", "/")


@dataclass
class ReviewSummary:
    root_dir: Path
    source_files: list[Path] = field(default_factory=list)
    languages: list[str] = field(default_factory=list)
    issues: list[ReviewIssue] = field(default_factory=list)

    @property
    def error_count(self) -> int:
        return sum(1 for issue in self.issues if issue.severity == ReviewSeverity.ERROR)

    @property
    def warning_count(self) -> int:
        return sum(
            1 for issue in self.issues if issue.severity == ReviewSeverity.WARNING
        )

    def to_text(self) -> str:
        lines = [
            "Co-op review complete",
            f"Source files reviewed: {len(self.source_files)}",
            f"Languages reviewed: {', '.join(self.languages) if self.languages else '-'}",
            f"Errors: {self.error_count}",
            f"Warnings: {self.warning_count}",
        ]
        if self.issues:
            lines.append("")
            lines.append("Issues:")
            for issue in self.issues:
                language = f" [{issue.language}]" if issue.language else ""
                lines.append(
                    f"- {issue.severity.value.upper()} {issue.check}{language}: "
                    f"{issue.location()} - {issue.message}"
                )
        return "\n".join(lines)

    def to_github_markdown(self) -> str:
        status = "passed" if self.error_count == 0 else "failed"
        lines = [
            "## Co-op Review",
            "",
            f"Status: **{status}**",
            "",
            "| Metric | Count |",
            "| --- | ---: |",
            f"| Source files reviewed | {len(self.source_files)} |",
            f"| Languages reviewed | {len(self.languages)} |",
            f"| Errors | {self.error_count} |",
            f"| Warnings | {self.warning_count} |",
        ]
        if self.issues:
            lines.extend(
                [
                    "",
                    "| Severity | Check | Language | Path | Message |",
                    "| --- | --- | --- | --- | --- |",
                ]
            )
            for issue in self.issues:
                escaped_message = issue.message.replace("|", "\\|")
                lines.append(
                    "| "
                    f"{issue.severity.value} | "
                    f"{issue.check} | "
                    f"{issue.language or '-'} | "
                    f"`{issue.location()}` | "
                    f"{escaped_message} |"
                )
        return "\n".join(lines)
