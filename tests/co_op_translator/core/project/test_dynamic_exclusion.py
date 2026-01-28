from pathlib import Path
from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.utils.common.file_utils import filter_files


def test_dynamic_exclusion_of_root_language_dirs(tmp_path: Path):
    root = tmp_path
    # Create root-level language dirs (canonical and alias) and a normal docs folder
    (root / "zh-TW").mkdir()
    (root / "cn").mkdir()
    (root / "docs").mkdir()

    # Create files
    (root / "zh-TW" / "a.md").write_text("x", encoding="utf-8")
    (root / "cn" / "b.md").write_text("y", encoding="utf-8")
    (root / "docs" / "c.md").write_text("z", encoding="utf-8")

    # Initialize translator (this will compute dynamic exclusions)
    pt = ProjectTranslator(
        language_codes="ko",
        root_dir=str(root),
        translation_types=["markdown"],
    )

    files = filter_files(root, pt.excluded_dirs, extension=".md")
    paths = {str(p.relative_to(root)).replace("\\", "/") for p in files}

    # Only docs/c.md should be present; language-dir files must be excluded
    assert "docs/c.md" in paths
    assert "zh-TW/a.md" not in paths
    assert "cn/b.md" not in paths
