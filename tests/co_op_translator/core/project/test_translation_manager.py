import json
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest
from PIL import Image

from co_op_translator.core.project.translation import TranslationManager
from co_op_translator.utils.common.file_utils import generate_translated_filename
from co_op_translator.utils.common.metadata_utils import (
    TEXT_TRANSLATION_FAILURES_KEY,
    calculate_file_hash,
    save_text_failure_metadata_for_source,
)


class FakeMarkdownTranslator:
    def __init__(self):
        self.calls = []
        self.disclaimer_calls = []

    async def translate_markdown(
        self, document, language_code, source_path=None, **kwargs
    ):
        self.calls.append((document, language_code, Path(source_path), kwargs))
        return f"# Translated {language_code}\n\n{document}"

    async def generate_disclaimer(self, language_code):
        self.disclaimer_calls.append(language_code)
        return f"Disclaimer for {language_code}"


class FakeImageTranslator:
    def __init__(self):
        self.calls = []

    def translate_image(self, image_path, language_code, fast_mode=False):
        self.calls.append((Path(image_path), language_code, fast_mode))
        return Image.new("RGB", (10, 10), "blue")


class FakeNoTextImageTranslator(FakeImageTranslator):
    def translate_image(self, image_path, language_code, fast_mode=False):
        self.calls.append((Path(image_path), language_code, fast_mode))
        with Image.open(image_path) as original_image:
            return original_image.copy()


class FakeTruncatingMarkdownTranslator:
    async def translate_markdown(
        self, document, language_code, source_path=None, **kwargs
    ):
        return "# Truncated\n\nOnly the beginning survived.\n"

    async def generate_disclaimer(self, language_code):
        return ""


class FakeNotebookTranslator:
    def __init__(self):
        self.calls = []

    async def translate_notebook(
        self,
        document,
        language_code,
        source_path=None,
    ):
        self.calls.append(
            (
                document,
                language_code,
                Path(source_path) if source_path is not None else None,
            )
        )
        notebook = json.loads(document)
        notebook.setdefault("metadata", {})["translated_to"] = language_code
        return json.dumps(notebook)


def _write_lang_metadata(lang_dir, data: dict) -> None:
    lang_dir.mkdir(parents=True, exist_ok=True)
    (lang_dir / ".co-op-translator.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def _write_notebook(path: Path, text: str = "# Notebook") -> None:
    path.write_text(
        json.dumps(
            {
                "cells": [{"cell_type": "markdown", "metadata": {}, "source": [text]}],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            }
        ),
        encoding="utf-8",
    )


@pytest.fixture
def temp_project_dir(tmp_path):
    """Create a small source tree with markdown, notebook, and image inputs."""
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "test.md").write_text(
        "# Test Document\nThis is a test.", encoding="utf-8"
    )

    images_dir = tmp_path / "images"
    images_dir.mkdir()
    (images_dir / "test.png").write_bytes(b"fake-image")

    (tmp_path / "translations").mkdir()
    (tmp_path / "translated_images").mkdir()

    return tmp_path


@pytest.fixture
def translation_manager(temp_project_dir):
    return TranslationManager(
        root_dir=temp_project_dir,
        translations_dir=temp_project_dir / "translations",
        image_dir=temp_project_dir / "translated_images",
        language_codes=["ko", "ja"],
        excluded_dirs=["translations", "translated_images", "logs"],
        supported_image_extensions=[".png"],
        supported_notebook_extensions=[".ipynb"],
        markdown_translator=FakeMarkdownTranslator(),
        image_translator=FakeImageTranslator(),
        notebook_translator=FakeNotebookTranslator(),
        translation_types=["markdown", "notebook", "images"],
        add_disclaimer=False,
    )


@pytest.mark.asyncio
async def test_translate_markdown_writes_translation_and_metadata(
    translation_manager, temp_project_dir
):
    md_file = temp_project_dir / "docs" / "test.md"

    result = await translation_manager.translate_markdown(md_file, "ko")

    translated_path = temp_project_dir / "translations" / "ko" / "docs" / "test.md"
    assert Path(result) == translated_path
    assert translated_path.exists()
    assert "# Translated ko" in translated_path.read_text(encoding="utf-8")
    assert (
        temp_project_dir / "translations" / "ko" / ".co-op-translator.json"
    ).exists()


@pytest.mark.asyncio
async def test_translate_markdown_appends_disclaimer_in_project_layer(
    temp_project_dir,
):
    markdown_translator = FakeMarkdownTranslator()
    translation_manager = TranslationManager(
        root_dir=temp_project_dir,
        translations_dir=temp_project_dir / "translations",
        image_dir=temp_project_dir / "translated_images",
        language_codes=["ko"],
        excluded_dirs=["translations", "translated_images", "logs"],
        supported_image_extensions=[".png"],
        supported_notebook_extensions=[".ipynb"],
        markdown_translator=markdown_translator,
        image_translator=FakeImageTranslator(),
        notebook_translator=FakeNotebookTranslator(),
        translation_types=["markdown"],
        add_disclaimer=True,
    )

    md_file = temp_project_dir / "docs" / "test.md"

    result = await translation_manager.translate_markdown(md_file, "ko")

    translated = Path(result).read_text(encoding="utf-8")
    assert "<!-- CO-OP TRANSLATOR DISCLAIMER START -->" in translated
    assert "Disclaimer for ko" in translated
    assert markdown_translator.disclaimer_calls == ["ko"]
    assert markdown_translator.calls[0][3] == {}


@pytest.mark.asyncio
async def test_translate_image_uses_configured_image_translator(
    translation_manager, temp_project_dir
):
    image_file = temp_project_dir / "images" / "test.png"

    result = await translation_manager.translate_image(image_file, "ko")

    translated_path = (
        temp_project_dir
        / "translated_images"
        / "ko"
        / generate_translated_filename(image_file.resolve(), "ko", temp_project_dir)
    )
    assert Path(result) == translated_path
    assert translated_path.exists()
    assert translation_manager.image_translator.calls == [
        (image_file.resolve(), "ko", False)
    ]
    assert (
        temp_project_dir / "translated_images" / "ko" / ".co-op-translator.json"
    ).exists()


@pytest.mark.asyncio
async def test_translate_image_saves_original_when_no_text_detected(
    translation_manager, temp_project_dir
):
    image_file = temp_project_dir / "images" / "blank.png"
    Image.new("RGB", (10, 10), "white").save(image_file)
    translation_manager.image_translator = FakeNoTextImageTranslator()

    result = await translation_manager.translate_image(image_file, "ko")

    translated_path = (
        temp_project_dir
        / "translated_images"
        / "ko"
        / generate_translated_filename(image_file.resolve(), "ko", temp_project_dir)
    )
    assert Path(result) == translated_path
    assert translated_path.exists()
    assert translation_manager.image_translator.calls == [
        (image_file.resolve(), "ko", False)
    ]


@pytest.mark.asyncio
async def test_translate_all_markdown_files_uses_public_workflow(
    translation_manager, temp_project_dir
):
    count, errors = await translation_manager.translate_all_markdown_files()

    assert count == 2
    assert errors == []
    assert (temp_project_dir / "translations" / "ko" / "docs" / "test.md").exists()
    assert (temp_project_dir / "translations" / "ja" / "docs" / "test.md").exists()


@pytest.mark.asyncio
async def test_process_api_requests_sequential_executes_tasks(translation_manager):
    seen = []

    async def task(value):
        seen.append(value)
        return value

    results = await translation_manager.process_api_requests_sequential(
        [lambda: task(1), lambda: task(2)], "Test tasks"
    )

    assert seen == [1, 2]
    assert results == [1, 2]


@pytest.mark.asyncio
async def test_process_api_requests_parallel_executes_tasks(translation_manager):
    seen = []

    async def task(value):
        seen.append(value)

    await translation_manager.process_api_requests_parallel(
        [task(1), task(2), task(3)], "Test tasks"
    )

    assert sorted(seen) == [1, 2, 3]


def test_get_outdated_translations_detects_stale_metadata(
    translation_manager, temp_project_dir
):
    source_file = temp_project_dir / "docs" / "test.md"
    translated_file = temp_project_dir / "translations" / "ko" / "docs" / "test.md"
    translated_file.parent.mkdir(parents=True, exist_ok=True)
    translated_file.write_text("# Old translation\n", encoding="utf-8")
    _write_lang_metadata(
        temp_project_dir / "translations" / "ko",
        {
            "docs/test.md": {
                "original_hash": "old-hash",
                "translation_date": "2026-01-01T00:00:00+00:00",
                "source_file": "docs/test.md",
                "language_code": "ko",
            }
        },
    )
    translation_manager.language_codes = ["ko"]

    outdated_files = translation_manager.get_outdated_translations()

    assert outdated_files == [(source_file, translated_file)]


def test_get_outdated_translations_detects_truncated_current_hash(
    translation_manager, temp_project_dir
):
    source_file = temp_project_dir / "docs" / "test.md"
    source_file.write_text(
        "\n".join(f"Line {index}" for index in range(40)) + "\n",
        encoding="utf-8",
    )
    translated_file = temp_project_dir / "translations" / "ko" / "docs" / "test.md"
    translated_file.parent.mkdir(parents=True, exist_ok=True)
    translated_file.write_text("# 번역\n\n중간에서 끝남\n", encoding="utf-8")
    _write_lang_metadata(
        temp_project_dir / "translations" / "ko",
        {
            "docs/test.md": {
                "original_hash": calculate_file_hash(source_file),
                "translation_date": "2026-01-01T00:00:00+00:00",
                "source_file": "docs/test.md",
                "language_code": "ko",
            }
        },
    )
    translation_manager.language_codes = ["ko"]

    outdated_files = translation_manager.get_outdated_translations()

    assert outdated_files == [(source_file, translated_file)]


@pytest.mark.asyncio
async def test_translate_markdown_does_not_save_incomplete_retry(
    translation_manager, temp_project_dir
):
    source_file = temp_project_dir / "docs" / "test.md"
    source_file.write_text(
        "\n".join(f"Line {index}" for index in range(40)) + "\n",
        encoding="utf-8",
    )
    translation_manager.language_codes = ["ko"]
    translation_manager.markdown_translator = FakeTruncatingMarkdownTranslator()

    result = await translation_manager.translate_markdown(source_file, "ko")

    translated_file = temp_project_dir / "translations" / "ko" / "docs" / "test.md"
    metadata_file = (
        temp_project_dir / "translations" / "ko" / ".co-op-translator.json"
    )
    metadata = json.loads(metadata_file.read_text(encoding="utf-8"))

    assert result == ""
    assert not translated_file.exists()
    assert (
        metadata[TEXT_TRANSLATION_FAILURES_KEY]["docs/test.md"]["status"] == "failed"
    )
    assert (
        metadata[TEXT_TRANSLATION_FAILURES_KEY]["docs/test.md"]["error_type"]
        == "RuntimeError"
    )


@pytest.mark.asyncio
async def test_translate_all_markdown_skips_unchanged_previous_failure(
    translation_manager, temp_project_dir
):
    source_file = temp_project_dir / "docs" / "test.md"
    lang_dir = temp_project_dir / "translations" / "ko"
    markdown_translator = FakeMarkdownTranslator()
    save_text_failure_metadata_for_source(
        lang_dir,
        source_file,
        "ko",
        root_dir=temp_project_dir,
        error=RuntimeError("previous incomplete translation"),
    )
    translation_manager.language_codes = ["ko"]
    translation_manager.markdown_translator = markdown_translator

    modified_count, errors = await translation_manager.translate_all_markdown_files()

    assert modified_count == 0
    assert errors == []
    assert markdown_translator.calls == []


@pytest.mark.asyncio
async def test_translate_all_markdown_retries_failure_after_version_change(
    translation_manager, temp_project_dir
):
    source_file = temp_project_dir / "docs" / "test.md"
    lang_dir = temp_project_dir / "translations" / "ko"
    markdown_translator = FakeMarkdownTranslator()
    save_text_failure_metadata_for_source(
        lang_dir,
        source_file,
        "ko",
        root_dir=temp_project_dir,
        error=RuntimeError("previous incomplete translation"),
        translator_version="old-version",
    )
    translation_manager.language_codes = ["ko"]
    translation_manager.markdown_translator = markdown_translator

    modified_count, errors = await translation_manager.translate_all_markdown_files()
    metadata = json.loads(
        (lang_dir / ".co-op-translator.json").read_text(encoding="utf-8")
    )

    assert modified_count == 1
    assert errors == []
    assert markdown_translator.calls
    assert (lang_dir / "docs" / "test.md").exists()
    assert TEXT_TRANSLATION_FAILURES_KEY not in metadata


@pytest.mark.asyncio
async def test_translate_all_markdown_update_keeps_previous_translation_on_failure(
    translation_manager, temp_project_dir
):
    source_file = temp_project_dir / "docs" / "test.md"
    translated_file = temp_project_dir / "translations" / "ko" / "docs" / "test.md"
    translated_file.parent.mkdir(parents=True)
    translated_file.write_text("# Previous translation\n", encoding="utf-8")
    old_hash = calculate_file_hash(source_file)
    _write_lang_metadata(
        temp_project_dir / "translations" / "ko",
        {
            "docs/test.md": {
                "original_hash": old_hash,
                "translation_date": "2026-01-01T00:00:00+00:00",
                "source_file": "docs/test.md",
                "language_code": "ko",
            }
        },
    )
    source_file.write_text(
        "\n".join(f"Updated line {index}" for index in range(40)) + "\n",
        encoding="utf-8",
    )
    translation_manager.language_codes = ["ko"]
    translation_manager.markdown_translator = FakeTruncatingMarkdownTranslator()

    modified_count, errors = await translation_manager.translate_all_markdown_files(
        update=True
    )
    metadata = json.loads(
        (temp_project_dir / "translations" / "ko" / ".co-op-translator.json").read_text(
            encoding="utf-8"
        )
    )

    assert modified_count == 0
    assert errors == [
        f"Failed to translate markdown file: {source_file.resolve()} (lang: ko)"
    ]
    assert translated_file.read_text(encoding="utf-8") == "# Previous translation\n"
    assert metadata["docs/test.md"]["original_hash"] == old_hash
    assert (
        metadata[TEXT_TRANSLATION_FAILURES_KEY]["docs/test.md"]["original_hash"]
        == calculate_file_hash(source_file)
    )


@pytest.mark.asyncio
async def test_translate_markdown_preserves_previous_translation_on_write_failure(
    translation_manager, temp_project_dir, monkeypatch
):
    source_file = temp_project_dir / "docs" / "test.md"
    translated_file = temp_project_dir / "translations" / "ko" / "docs" / "test.md"
    translated_file.parent.mkdir(parents=True)
    translated_file.write_text("# Previous translation\n", encoding="utf-8")
    old_hash = calculate_file_hash(source_file)
    _write_lang_metadata(
        temp_project_dir / "translations" / "ko",
        {
            "docs/test.md": {
                "original_hash": old_hash,
                "translation_date": "2026-01-01T00:00:00+00:00",
                "source_file": "docs/test.md",
                "language_code": "ko",
            }
        },
    )
    original_replace = Path.replace

    def fail_replace(path, target):
        if Path(target) == translated_file:
            raise OSError("replace failed")
        return original_replace(path, target)

    monkeypatch.setattr(Path, "replace", fail_replace)
    translation_manager.language_codes = ["ko"]

    result = await translation_manager.translate_markdown(source_file, "ko")
    metadata = json.loads(
        (temp_project_dir / "translations" / "ko" / ".co-op-translator.json").read_text(
            encoding="utf-8"
        )
    )

    assert result == ""
    assert translated_file.read_text(encoding="utf-8") == "# Previous translation\n"
    assert metadata["docs/test.md"]["original_hash"] == old_hash
    assert TEXT_TRANSLATION_FAILURES_KEY not in metadata


@pytest.mark.asyncio
async def test_check_outdated_files_migrates_legacy_inline_metadata(
    translation_manager, temp_project_dir
):
    root_readme = temp_project_dir / "README.md"
    root_readme.write_text("# Root\n", encoding="utf-8")
    nested_readme = temp_project_dir / "lesson-1" / "README.md"
    nested_readme.parent.mkdir(parents=True, exist_ok=True)
    nested_readme.write_text("# Nested\n", encoding="utf-8")

    lang_dir = temp_project_dir / "translations" / "ko"
    (lang_dir / "README.md").parent.mkdir(parents=True, exist_ok=True)
    (lang_dir / "README.md").write_text("# 번역\n", encoding="utf-8")
    (lang_dir / "lesson-1" / "README.md").parent.mkdir(parents=True, exist_ok=True)
    (lang_dir / "lesson-1" / "README.md").write_text(
        '<!--\nCO_OP_TRANSLATOR_METADATA:\n{\n  "original_hash": "deadbeef",\n  "translation_date": "2026-01-01T00:00:00+00:00",\n  "source_file": "lesson-1/README.md",\n  "language_code": "ko"\n}\n-->\n# 번역\n',
        encoding="utf-8",
    )
    _write_lang_metadata(
        lang_dir,
        {
            "README.md": {
                "original_hash": calculate_file_hash(root_readme),
                "translation_date": "2026-01-01T00:00:00+00:00",
                "source_file": "README.md",
                "language_code": "ko",
            }
        },
    )
    translation_manager.language_codes = ["ko"]
    translation_manager.retranslate_outdated_files = AsyncMock()

    modified_count, errors = await translation_manager.check_outdated_files()

    metadata = json.loads(
        (lang_dir / ".co-op-translator.json").read_text(encoding="utf-8")
    )
    assert errors == []
    assert modified_count >= 1
    assert "lesson-1/README.md" in metadata
    translation_manager.retranslate_outdated_files.assert_awaited_once()


@pytest.mark.asyncio
async def test_check_outdated_files_does_not_synthesize_missing_legacy_metadata(
    translation_manager, temp_project_dir
):
    source_file = temp_project_dir / "guide.md"
    source_file.write_text("# Source\n", encoding="utf-8")
    lang_dir = temp_project_dir / "translations" / "ko"
    translated_file = lang_dir / "guide.md"
    translated_file.parent.mkdir(parents=True, exist_ok=True)
    translated_file.write_text("# Manual translated content\n", encoding="utf-8")

    translation_manager.language_codes = ["ko"]
    translation_manager.retranslate_outdated_files = AsyncMock()

    modified_count, errors = await translation_manager.check_outdated_files()

    assert errors == []
    assert modified_count == 1
    assert not (lang_dir / ".co-op-translator.json").exists()
    translation_manager.retranslate_outdated_files.assert_awaited_once_with(
        [(source_file, translated_file)]
    )


@pytest.mark.asyncio
async def test_retranslate_outdated_files_routes_markdown_and_notebooks(
    translation_manager, temp_project_dir
):
    notebook_file = temp_project_dir / "test.ipynb"
    _write_notebook(notebook_file)
    md_file = temp_project_dir / "test.md"
    md_file.write_text("# Test", encoding="utf-8")
    outdated_files = [
        (notebook_file, temp_project_dir / "translations" / "ko" / "test.ipynb"),
        (md_file, temp_project_dir / "translations" / "ko" / "test.md"),
    ]
    translation_manager.language_codes = ["ko"]
    translation_manager.translate_notebook = AsyncMock(return_value="notebook_result")
    translation_manager.translate_markdown = AsyncMock(return_value="markdown_result")

    await translation_manager.retranslate_outdated_files(outdated_files)

    translation_manager.translate_notebook.assert_called_once_with(notebook_file, "ko")
    translation_manager.translate_markdown.assert_called_once_with(md_file, "ko")


@pytest.mark.asyncio
async def test_translate_project_async_runs_public_workflow_for_outdated_files(
    translation_manager, temp_project_dir
):
    test_md = temp_project_dir / "docs" / "test.md"
    translation_manager.language_codes = ["ko"]
    translation_manager.get_outdated_translations = MagicMock(
        return_value=[
            (test_md, temp_project_dir / "translations" / "ko" / "docs" / "test.md")
        ]
    )
    translation_manager.retranslate_outdated_files = AsyncMock()
    translation_manager.translate_all_markdown_files = AsyncMock(return_value=(0, []))
    translation_manager.translation_types = ["markdown"]
    translation_manager.directory_manager = MagicMock()
    translation_manager.directory_manager.cleanup_orphaned_translations.return_value = 0
    translation_manager.directory_manager.sync_directory_structure.return_value = (
        0,
        0,
        [],
    )
    translation_manager.directory_manager.migrate_markdown_image_links.return_value = 0
    translation_manager.directory_manager.migrate_notebook_image_links.return_value = 0

    await translation_manager.translate_project_async()

    translation_manager.directory_manager.cleanup_orphaned_translations.assert_called_once()
    translation_manager.directory_manager.sync_directory_structure.assert_called_once()
    translation_manager.get_outdated_translations.assert_called_once()
    translation_manager.retranslate_outdated_files.assert_awaited_once()
    translation_manager.translate_all_markdown_files.assert_awaited_once()


@pytest.mark.asyncio
async def test_translate_project_runs_link_migration_when_no_images(
    translation_manager, monkeypatch
):
    monkeypatch.setattr(
        "co_op_translator.core.project.translation.translation_workflow.migrate_translated_image_filenames",
        lambda *args, **kwargs: {},
    )
    monkeypatch.setattr(
        "co_op_translator.core.project.translation.translation_workflow.migrate_images_to_webp",
        lambda *args, **kwargs: {},
    )
    monkeypatch.setattr(
        "co_op_translator.core.project.translation.translation_workflow.canonicalize_image_links_in_translations",
        lambda *args, **kwargs: (0, 0),
    )
    translation_manager.translation_types = ["markdown"]
    translation_manager.get_outdated_translations = MagicMock(return_value=[])
    translation_manager.translate_all_markdown_files = AsyncMock(return_value=(0, []))
    translation_manager.directory_manager = MagicMock()
    translation_manager.directory_manager.cleanup_orphaned_translations.return_value = 0
    translation_manager.directory_manager.sync_directory_structure.return_value = (
        0,
        0,
        [],
    )
    translation_manager.directory_manager.migrate_markdown_image_links.return_value = 0
    translation_manager.directory_manager.migrate_notebook_image_links.return_value = 0

    await translation_manager.translate_project_async()

    translation_manager.directory_manager.migrate_markdown_image_links.assert_called_once()
    translation_manager.directory_manager.migrate_notebook_image_links.assert_called_once()


@pytest.mark.asyncio
async def test_translate_notebook_writes_translation_and_metadata(
    translation_manager, temp_project_dir
):
    notebook_file = temp_project_dir / "test.ipynb"
    _write_notebook(notebook_file)

    result = await translation_manager.translate_notebook(notebook_file, "ko")

    translated_path = temp_project_dir / "translations" / "ko" / "test.ipynb"
    assert Path(result) == translated_path
    assert translated_path.exists()
    assert (
        json.loads(translated_path.read_text(encoding="utf-8"))["metadata"][
            "translated_to"
        ]
        == "ko"
    )
    assert (
        temp_project_dir / "translations" / "ko" / ".co-op-translator.json"
    ).exists()


@pytest.mark.asyncio
async def test_translate_notebook_rewrites_paths_and_appends_disclaimer(
    temp_project_dir,
):
    docs_dir = temp_project_dir / "docs"
    images_dir = docs_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    image_file = images_dir / "hero.png"
    image_file.write_text("image", encoding="utf-8")
    notebook_file = docs_dir / "tutorial.ipynb"
    notebook_file.write_text(
        json.dumps(
            {
                "cells": [
                    {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": ["# Tutorial\n", "![Hero](images/hero.png)\n"],
                    }
                ],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            }
        ),
        encoding="utf-8",
    )

    markdown_translator = FakeMarkdownTranslator()
    notebook_translator = FakeNotebookTranslator()
    translation_manager = TranslationManager(
        root_dir=temp_project_dir,
        translations_dir=temp_project_dir / "translations",
        image_dir=temp_project_dir / "translated_images",
        language_codes=["ko"],
        excluded_dirs=["translations", "translated_images", "logs"],
        supported_image_extensions=[".png"],
        supported_notebook_extensions=[".ipynb"],
        markdown_translator=markdown_translator,
        image_translator=FakeImageTranslator(),
        notebook_translator=notebook_translator,
        translation_types=["notebook", "images"],
        add_disclaimer=True,
    )

    result = await translation_manager.translate_notebook(notebook_file, "ko")

    translated_path = (
        temp_project_dir / "translations" / "ko" / "docs" / "tutorial.ipynb"
    )
    assert Path(result) == translated_path
    translated_notebook = json.loads(translated_path.read_text(encoding="utf-8"))
    cell_source = "".join(translated_notebook["cells"][0]["source"])
    disclaimer_source = "".join(translated_notebook["cells"][-1]["source"])

    assert "images/hero.png" not in cell_source
    assert "../../../translated_images/ko/hero." in cell_source
    assert "Disclaimer for ko" in disclaimer_source
    assert markdown_translator.disclaimer_calls == ["ko"]
    assert notebook_translator.calls[0][2] == notebook_file.resolve()


@pytest.mark.asyncio
async def test_translate_all_notebook_files_skips_up_to_date_notebook(
    translation_manager, temp_project_dir
):
    original_notebook = temp_project_dir / "test.ipynb"
    _write_notebook(original_notebook, "# Original")
    translated_notebook = temp_project_dir / "translations" / "ko" / "test.ipynb"
    translated_notebook.parent.mkdir(parents=True)
    translated_payload = json.loads(original_notebook.read_text(encoding="utf-8"))
    translated_payload["metadata"]["coopTranslator"] = {
        "original_hash": calculate_file_hash(original_notebook),
        "translation_date": "2026-01-01T00:00:00+00:00",
        "source_file": "test.ipynb",
        "language_code": "ko",
    }
    translated_notebook.write_text(json.dumps(translated_payload), encoding="utf-8")
    translation_manager.language_codes = ["ko"]
    translation_manager.translate_notebook = AsyncMock(return_value="translated_result")

    modified_count, errors = await translation_manager.translate_all_notebook_files()

    assert modified_count == 0
    assert errors == []
    translation_manager.translate_notebook.assert_not_called()


@pytest.mark.asyncio
async def test_translate_all_notebook_files_retranslates_outdated_notebook(
    translation_manager, temp_project_dir
):
    original_notebook = temp_project_dir / "test.ipynb"
    _write_notebook(original_notebook, "# Original")
    translated_notebook = temp_project_dir / "translations" / "ko" / "test.ipynb"
    translated_notebook.parent.mkdir(parents=True)
    translated_payload = json.loads(original_notebook.read_text(encoding="utf-8"))
    translated_payload["metadata"]["coopTranslator"] = {
        "original_hash": "old-hash",
        "translation_date": "2026-01-01T00:00:00+00:00",
        "source_file": "test.ipynb",
        "language_code": "ko",
    }
    translated_notebook.write_text(json.dumps(translated_payload), encoding="utf-8")
    translation_manager.language_codes = ["ko"]
    translation_manager.translate_notebook = AsyncMock(
        return_value="updated_translation"
    )

    modified_count, errors = await translation_manager.translate_all_notebook_files()

    assert modified_count == 1
    assert errors == []
    translation_manager.translate_notebook.assert_called_once_with(
        original_notebook.resolve(), "ko"
    )
