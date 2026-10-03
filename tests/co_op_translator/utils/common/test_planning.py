from pathlib import Path

from co_op_translator.utils.common.files.project_paths import ProjectPathConfig
from co_op_translator.utils.common.metadata_utils import save_text_metadata_for_source
from co_op_translator.utils.common.planning import PLAN_SCHEMA, build_translation_plan


def _write(root: Path, relative: str, content: str) -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_plan_reports_resolved_paths_filters_status_and_estimates(tmp_path):
    source = tmp_path / "docs"
    output = source / "i18n"
    current = _write(source, "current.md", "# Current\n")
    outdated = _write(source, "nested/outdated.md", "# Old\n")
    _write(source, "new.md", "# New\n")
    _write(source, "skip/ignored.md", "# Ignore\n")
    _write(output, "ko/current.md", "# 현재\n")
    _write(output, "ko/nested/outdated.md", "# 이전\n")
    _write(output, "ko/phantom.md", "# Generated output\n")
    save_text_metadata_for_source(output / "ko", current, "ko", root_dir=source)
    save_text_metadata_for_source(output / "ko", outdated, "ko", root_dir=source)
    outdated.write_text("# Updated\n", encoding="utf-8")

    paths = ProjectPathConfig.resolve(
        source=source,
        output=output,
        include=["**/*.md"],
        exclude=["skip/**"],
    )
    assert paths.discovery_exclusions() == (str(output),)
    plan = build_translation_plan(
        paths=paths,
        languages=["ko"],
        translation_types=["markdown"],
        estimates={"words": 123, "total": 456},
    )

    assert plan["schema"] == PLAN_SCHEMA
    assert plan["source"] == source.as_posix()
    assert plan["output"] == output.as_posix()
    assert plan["include"] == ["**/*.md"]
    assert "skip/**" in plan["exclude"]
    assert output.as_posix() in plan["exclude"]
    assert plan["new_files"] == [{"file": "new.md", "language": "ko"}]
    assert plan["outdated_files"] == [{"file": "nested/outdated.md", "language": "ko"}]
    assert plan["current_files"] == [{"file": "current.md", "language": "ko"}]
    assert plan["estimated_words"] == 123
    assert plan["estimated_tokens"] == 456
    assert plan["api_required"] is True
    assert all("phantom.md" not in str(items) for items in plan.values())
