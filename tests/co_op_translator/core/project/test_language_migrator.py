from pathlib import Path
from co_op_translator.core.project.language_migrator import LanguageFolderMigrator


def test_detect_alias_folders(tmp_path: Path):
    # Arrange a fake project with alias folders
    root = tmp_path
    translations = root / "translations"
    images = root / "translated_images"
    fast = root / "translated_images_fast"

    (translations / "tw").mkdir(parents=True)
    (images / "cn").mkdir(parents=True)
    (fast / "br").mkdir(parents=True)

    migrator = LanguageFolderMigrator(root_dir=root)

    # Act
    entries = migrator.detect_alias_folders()

    # Assert
    mapping = {(e.base_dir.name, e.alias, e.canonical) for e in entries}
    assert ("translations", "tw", "zh-TW") in mapping
    assert ("translated_images", "cn", "zh-CN") in mapping
    assert ("translated_images_fast", "br", "pt-BR") in mapping


def test_execute_fs_rename(tmp_path: Path):
    # Arrange alias source and missing canonical destination
    root = tmp_path
    translations = root / "translations"
    (translations / "tw").mkdir(parents=True)
    (translations / "tw" / "foo").mkdir()

    migrator = LanguageFolderMigrator(root_dir=root)
    entries = migrator.detect_alias_folders()

    # Precondition
    assert (translations / "tw").exists()
    assert not (translations / "zh-TW").exists()

    # Act: execute with dry_run first
    renamed, msgs = migrator.execute(entries, use_git=False, dry_run=True)
    # No changes in dry run
    assert renamed == 0
    assert (translations / "tw").exists()
    assert not (translations / "zh-TW").exists()

    # Act: real rename (filesystem)
    renamed, msgs = migrator.execute(entries, use_git=False, dry_run=False)

    # Assert rename happened
    assert renamed == 1
    assert not (translations / "tw").exists()
    assert (translations / "zh-TW").exists()
