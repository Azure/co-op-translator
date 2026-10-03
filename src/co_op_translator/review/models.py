from __future__ import annotations

import json
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

    def to_dict(self) -> dict[str, str]:
        payload = {
            "check": self.check,
            "severity": self.severity.value,
            "message": self.message,
            "path": self.location(),
        }
        if self.language is not None:
            payload["language"] = self.language
        return payload


@dataclass
class ReviewSummary:
    SCHEMA = "co-op.translation.verification.v1"

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

    def _has_issue(self, *checks: str) -> bool:
        return any(issue.check in checks for issue in self.issues)

    def to_dict(self) -> dict[str, object]:
        missing_blocks = sum(issue.check == "missing-blocks" for issue in self.issues)
        duplicated_blocks = sum(
            issue.check == "duplicated-blocks" for issue in self.issues
        )
        suspicious_prose = sum(
            issue.check == "suspicious-untranslated-prose" for issue in self.issues
        )
        return {
            "schema": self.SCHEMA,
            "root": str(self.root_dir).replace("\\", "/"),
            "source_files": [
                str(path).replace("\\", "/") for path in self.source_files
            ],
            "languages": list(self.languages),
            "status": "passed" if self.error_count == 0 else "failed",
            "counts": {
                "errors": self.error_count,
                "warnings": self.warning_count,
                "missing_blocks": missing_blocks,
                "duplicated_blocks": duplicated_blocks,
                "suspicious_untranslated_prose": suspicious_prose,
            },
            "verification": {
                "source_hash_current": not self._has_issue("freshness"),
                "markdown_structure_valid": not self._has_issue(
                    "markdown-integrity", "notebook-integrity"
                ),
                "translation_appears_complete": not self._has_issue(
                    "structure",
                    "missing-blocks",
                    "duplicated-blocks",
                    "suspicious-untranslated-prose",
                ),
                "protected_literals_preserved": not self._has_issue(
                    "protected-literals"
                ),
                "links_valid": not self._has_issue("local-link", "image-link"),
            },
            "issues": [issue.to_dict() for issue in self.issues],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2, sort_keys=True)

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
