from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class ProjectPathConfig:
    """Normalized source discovery and translation output paths."""

    source_root: Path
    output_root: Path
    include_patterns: tuple[str, ...] = ()
    exclude_patterns: tuple[str, ...] = ()

    @classmethod
    def resolve(
        cls,
        *,
        source: str | Path = ".",
        output: str | Path | None = None,
        include: Iterable[str] | None = None,
        exclude: Iterable[str] | None = None,
    ) -> "ProjectPathConfig":
        source_root = Path(source).resolve()
        if not source_root.exists():
            raise ValueError(f"Source directory does not exist: {source}")
        if not source_root.is_dir():
            raise ValueError(f"Source path is not a directory: {source}")

        if output is None:
            output_root = source_root / "translations"
        else:
            output_path = Path(output)
            if output_path.is_absolute():
                output_root = output_path.resolve()
            else:
                cwd_candidate = output_path.resolve()
                try:
                    cwd_candidate.relative_to(source_root)
                except ValueError:
                    output_root = (source_root / output_path).resolve()
                else:
                    output_root = cwd_candidate
        if output_root.exists() and not output_root.is_dir():
            raise ValueError(f"Output path is not a directory: {output_root}")

        return cls(
            source_root=source_root,
            output_root=output_root,
            include_patterns=tuple(_normalize_patterns(include)),
            exclude_patterns=tuple(_normalize_patterns(exclude)),
        )

    def discovery_exclusions(self) -> tuple[str, ...]:
        exclusions: list[str] = []
        try:
            self.output_root.relative_to(self.source_root)
        except ValueError:
            pass
        else:
            exclusions.append(str(self.output_root))
        return tuple(dict.fromkeys(exclusions))

    def to_dict(self) -> dict[str, object]:
        return {
            "source": str(self.source_root),
            "output": str(self.output_root),
            "include": list(self.include_patterns),
            "exclude": list(
                dict.fromkeys(self.exclude_patterns + self.discovery_exclusions())
            ),
        }


def _normalize_patterns(values: Iterable[str] | None) -> list[str]:
    if values is None:
        return []
    return [
        value.strip().replace("\\", "/") for value in values if value and value.strip()
    ]
