from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Mapping

from co_op_translator.config.constants import (
    SUPPORTED_MARKDOWN_EXTENSIONS,
    SUPPORTED_NOTEBOOK_EXTENSIONS,
)
from co_op_translator.utils.common.files.discovery import filter_files
from co_op_translator.utils.common.files.project_paths import ProjectPathConfig
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    read_text_metadata_for_source,
)

PLAN_SCHEMA = "co-op.translation.plan.v1"


def build_translation_plan(
    *,
    paths: ProjectPathConfig,
    languages: Iterable[str],
    translation_types: Iterable[str],
    estimates: Mapping[str, int] | None = None,
    update: bool = False,
    readme_only: bool = False,
) -> dict[str, object]:
    modes = set(translation_types)
    extensions: set[str] = set()
    if "markdown" in modes:
        extensions.update(SUPPORTED_MARKDOWN_EXTENSIONS)
    if "notebook" in modes:
        extensions.update(SUPPORTED_NOTEBOOK_EXTENSIONS)

    if readme_only:
        readme_path = paths.source_root / "README.md"
        source_files = [readme_path] if readme_path.is_file() else []
    else:
        source_files = []
        for extension in sorted(extensions):
            source_files.extend(
                filter_files(
                    paths.source_root,
                    paths.discovery_exclusions(),
                    extension,
                    include_patterns=paths.include_patterns,
                    exclude_patterns=paths.exclude_patterns,
                )
            )

    buckets: dict[str, list[dict[str, str]]] = {
        "new_files": [],
        "outdated_files": [],
        "current_files": [],
    }
    for source_file in sorted(set(source_files)):
        relative = source_file.relative_to(paths.source_root)
        source_hash = calculate_file_hash(source_file)
        for language in languages:
            target = paths.output_root / language / relative
            item = {"file": relative.as_posix(), "language": language}
            if not target.exists():
                buckets["new_files"].append(item)
                continue
            metadata = read_text_metadata_for_source(
                paths.output_root / language, source_file
            )
            if update or metadata.get("original_hash") != source_hash:
                buckets["outdated_files"].append(item)
            else:
                buckets["current_files"].append(item)

    estimate_values = estimates or {}
    return {
        "schema": PLAN_SCHEMA,
        "source": str(paths.source_root).replace("\\", "/"),
        "output": str(paths.output_root).replace("\\", "/"),
        "include": list(paths.include_patterns),
        "exclude": [
            str(value).replace("\\", "/")
            for value in dict.fromkeys(
                paths.exclude_patterns + paths.discovery_exclusions()
            )
        ],
        "languages": list(languages),
        **buckets,
        "estimated_words": int(estimate_values.get("words", 0) or 0),
        "estimated_tokens": int(estimate_values.get("total", 0) or 0),
        "api_required": bool(
            buckets["new_files"] or buckets["outdated_files"] or "images" in modes
        ),
    }


def write_translation_plan(path: str | Path, plan: Mapping[str, object]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
